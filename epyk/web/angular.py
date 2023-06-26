from ..core.py import primitives
from ..core import Page
from ..core.js import JsUtils
from ..core.css import css_files_loader
from ..core.html import Standalone, html_template_loader
from . import npm, node, templates

import logging
import zipfile
import sys
import re
import os
import json
import subprocess
from collections import OrderedDict
from typing import Any, Dict, List
from pathlib import Path


def to_component(
        component: Standalone.Component, name: str = "ek-angular-{selector}-{version}", out_path: str = None,
        version: str = None, init_value: Any = "", init_options: dict = None) -> Dict[str, str]:
    """

    :param component:
    :param name:
    :param out_path:
    :param version:
    :param init_value:
    :param init_options:
    """
    component_files = {}
    # Write component definition to the assets folder
    if out_path is None:
        out_path = Path().cwd()
    out_path = Path(out_path, component.selector)
    out_path.mkdir(parents=True, exist_ok=True)
    init_options = init_options or {}

    component_files = {"js": name.format(selector=component.selector, version=version) + ".js"}
    with open(Path(out_path, component_files["js"]), "w") as jf:
        js_path = Path(component.component_url)
        with open(js_path) as hf:
            jf.write(npm.to_module(hf.read(), component.requirements))

    component_files["css"] = name.format(selector=component.selector, version=version) + ".css"
    with open(Path(out_path, component_files["css"]), "w") as cf:
        css_styles = css_files_loader(component.style_urls, minify=False)
        if css_styles:
            cf.write(css_styles)

    component_files["html"] = name.format(selector=component.selector, version=version) + ".html"
    with open(Path(out_path, component_files["html"]), "w") as hf:
        html_def = html_template_loader(component.template_url, ref_expr="#%s" % component.__name__.lower())
        hf.write(html_def["template"])

    component_files["spec"] = name.format(selector=component.selector, version=version) + ".component.spec.ts"
    with open(Path(Path(out_path).parent, component_files["spec"]), "w") as sf:
        sf.write(templates.ANGULAR_COMPONENT_SPEC % {
            "asset_class": component.__name__,
        })

    component_files["component"] = name.format(selector=component.selector, version=version) + ".component.ts"
    js_frgs = ["@Input() %s" % var for var in html_def['vars']]
    # @Input() label;
    with open(Path(Path(out_path).parent, component_files["component"]), "w") as sf:
        sf.write(templates.ANGULAR_COMPONENT % {
            "asset_class": component.__name__,
            "selector": component.selector,
            "asset_path": "./%s/%s" % (Path(out_path).name, name.format(selector=component.selector, version=version)),
            "js": '%s ; component; @ViewChild("%s", { static: true }) input;' % (
                ";".join(js_frgs), component.__name__.lower()),
            "init_value": json.dumps(init_value),
            "init_options": init_options,
            "html": html_def["template"],
        })

    if version is not None:
        out_zip_name = name.format(selector=component.selector, version=version) + ".zip"
        with zipfile.ZipFile(out_zip_name, 'w') as zip_object:
            zip_object.write(str(Path(component.selector, component_files["js"])),
                             str(Path(component.selector, component_files["js"])))
            zip_object.write(str(Path(component.selector, component_files["css"])),
                             str(Path(component.selector, component_files["css"])))
            zip_object.write(str(Path(component.selector, component_files["html"])),
                             str(Path(component.selector, component_files["html"])))
            zip_object.write(component_files["spec"], component_files["spec"])
            zip_object.write(component_files["component"], component_files["component"])
            # delete files in the folder
            Path(out_path, component_files["js"]).unlink()
            Path(out_path, component_files["css"]).unlink()
            Path(out_path, component_files["html"]).unlink()
            Path(Path(out_path).parent, component_files["spec"]).unlink()
            Path(Path(out_path).parent, component_files["component"]).unlink()
    return component_files


def add_to_app(
        components: List[Standalone.Component],
        app_path: str,
        folder: str = "assets",
        name: str = "{selector}",
        raise_exception: bool = False,
        view_path: str = "app"
) -> dict:
    """
      This will add the component directly tp the src folder in the linked application.
      All components generated will be put in a sub folder.

      To start the angular application: ng serve --open

      This will also update the required angular system files accordingly

      :param components: List of components to add to a Angular application
      :param app_path: Angular application path (root)
      :param folder: Components' folder
      :param name: Component's files name format
      :param raise_exception: Flag to raise exception if error
      :param view_path: The path for the Angular view (the app file). default app/
      """
    result = {"dependencies": {}, "styles": [], "scripts": [], "modules": {}}
    for component in components:
        result[component.selector] = npm.check_component_requirements(component, app_path, raise_exception)
        result["dependencies"].update(result[component.selector])
        assets_path = Path(app_path, "src", folder)
        assets_path.mkdir(parents=True, exist_ok=True)
        component_files = to_component(component, name=name, out_path=str(assets_path))
        result["styles"].extend(npm.get_styles(component.requirements))
        result["scripts"].extend(npm.get_scripts(component.requirements))
        result["modules"][component.__name__] = component.get_import(
            "../%s/%s" % (folder, component_files["component"][:-3]), suffix="Component",
            root_path=Path(app_path, "src", view_path))
    angular_config_path = Path(app_path, "angular.json")
    if angular_config_path.exists():
        app_path = Path(app_path)
        with open(angular_config_path) as ap:
            angular_config = json.loads(ap.read(), object_pairs_hook=OrderedDict)
            for cat in ["styles", "scripts"]:
                for style in set(result[cat]):
                    if style not in angular_config["projects"][app_path.name]["architect"]["build"]["options"][cat]:
                        angular_config["projects"][app_path.name]["architect"]["build"]["options"][cat].insert(0, style)
        with open(angular_config_path, "w") as ap:
            json.dump(angular_config, ap, indent=2)
    else:
        count_styles = len(result["styles"])
        count_scripts = len(result["scripts"])
        logging.warning("%s styles and %s scripts not added" % (count_styles, count_scripts))
        logging.warning("Cannot locate file: %s" % angular_config_path)
    app_module_path = Path(app_path, "src", view_path, "app.module.ts")
    if app_module_path.exists():
        auto_update = False
        with open(app_module_path) as am:
            imports, config = map(lambda x: x.strip(), am.read().split("@NgModule"))
            imports = imports + "\n\n// Auto generated"
            for module in result["modules"].values():
                if module not in imports:
                    imports = "%s\n%s;" % (imports, module)
                    auto_update = True
        if auto_update:
            with open(app_module_path, "w") as am:
                am.write("%s\n\n@NgModule%s" % (imports, config))
    return result


# To be added to the tsconfig.json file
# strictPropertyInitialization: True


def app(path: str, name: str = None):
    """

    :param path: The server path
    :param name: Optional. The application name on the server
    """
    return Angular(path, name)


JS_MODULES_IMPORTS = {
    'showdown': '''
import Showdown from 'showdown';
var showdown = Showdown;
'''
}

COMPONENT_NAME_TEMPLATE = "app.%s.component"


class NGModule:

    def __init__(self, ang_app_path: str):
        self._ang_app_path = ang_app_path

    def class_(self, name: str):
        """
        Creates a new generic class definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#class-command

        :param name: The name of the interface
        """
        subprocess.run('ng generate class %s' % name, shell=True, cwd=self._ang_app_path)

    def component(self, name: str):
        """
        Creates a new generic component definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#component-command

        :param name: The name of the interface
        """
        subprocess.run('ng generate component %s' % name, shell=True, cwd=self._ang_app_path)

    def directive(self, name: str):
        """
        Creates a new generic directive definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#directive-command

        :param name: The name of the interface
        """
        subprocess.run('ng generate directive %s' % name, shell=True, cwd=self._ang_app_path)

    def enum(self, name: str):
        """
        Generates a new, generic enum definition for the given or default project.

        Related Pages:

          https://angular.io/cli/generate#enum-command

        :param name: The name of the interface
        """
        subprocess.run('ng generate enum %s' % name, shell=True, cwd=self._ang_app_path)

    def guard(self, name: str):
        """
        Generates a new, generic route guard definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#guard-command

        :param name: The name of the new route guard
        """
        subprocess.run('ng generate guard %s' % name, shell=True, cwd=self._ang_app_path)

    def interceptor(self, name: str):
        """
        Creates a new, generic interceptor definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#interceptor-command

        :param name: The name of the interceptor
        """
        subprocess.run('ng generate interceptor %s' % name, shell=True, cwd=self._ang_app_path)

    def interface(self, name: str, type: str):
        """
        Creates a new generic interface definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#interface-command

        :param name: The name of the interface
        :param type: Adds a developer-defined type to the filename, in the format "name.type.ts"
        """
        subprocess.run('ng generate interface %s %s' % (name, type), shell=True, cwd=self._ang_app_path)

    def library(self, name: str, type: str):
        """
        Creates a new generic library project in the current workspace.

        Related Pages:

          https://angular.io/cli/generate#library-command

        :param name: The name of the interface
        :param type:
        """
        subprocess.run('ng generate library %s %s' % (name, type), shell=True, cwd=self._ang_app_path)

    def module(self, name: str, type: str):
        """
        Creates a new generic NgModule definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#library-command

        :param name: The name of the interface
        :param type:
        """
        subprocess.run('ng generate module %s %s' % (name, type), shell=True, cwd=self._ang_app_path)

    def service(self, name: str, type: str):
        """
        Creates a new, generic service definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#library-command

        :param name: The name of the interface
        :param type:
        """
        subprocess.run('ng generate service %s %s' % (name, type), shell=True, cwd=self._ang_app_path)


class NG:
    def __init__(self, app_path: str, app_name: str = None, env: str = None):
        self._app_path, self._app_name, self.envs = app_path, app_name, env

    def e2e(self, app_name: str = None):
        """
        Builds and serves an Angular app, then runs end-to-end tests using Protractor.

        Related Pages:

          https://angular.io/cli/e2e

        :param app_name: The application name
        """
        app_name = app_name or self._app_name
        if app_name is None:
            raise ValueError("An Angular application name is required!")

        subprocess.run('ng e2e %s' % app_name, shell=True, cwd=os.path.join(self._app_path, self._app_name))

    def lint(self, app_name: str = None):
        """
        Builds and serves an Angular app, then runs end-to-end tests using Protractor.

        Related Pages:

          https://angular.io/cli/lint

        :param app_name: The application name
        """
        app_name = app_name or self._app_name
        if app_name is None:
            raise ValueError("An Angular aplication name is required!")

        subprocess.run('ng lint %s' % app_name, shell=True, cwd=os.path.join(self._app_path, self._app_name))

    def new(self, name: str, path: str = None):
        """
        Builds and serves an Angular app, then runs end-to-end tests using Protractor.

        Related Pages:

          https://angular.io/cli/new

        :param name: The application name
        :param path: The server path
        """
        if path is not None:
            subprocess.run('ng new %s --directory %s' % (name, path), shell=True, cwd=self._app_path)
        else:
            subprocess.run('ng new %s' % name, shell=True, cwd=self._app_path)
        print('ng new %s' % name)

    def doc(self, keyword: str):
        """
    Opens the official Angular documentation (angular.io) in a browser, and searches for a given keyword.

    Related Pages:

      https://angular.io/cli

    :param keyword:
    """
        subprocess.run('ng doc %s' % keyword, shell=True, cwd=self._app_path)

    def add(self, package: str):
        """
        Add package to the Angular server node modules.

        Related Pages:

          https://angular.io/cli

        :param package: The package name
        """
        if self.envs is not None:
            for env in self.envs:
                subprocess.run(env, shell=True, cwd=os.path.join(self._app_path, self._app_name))
        subprocess.run('ng add %s' % package, shell=True, cwd=os.path.join(self._app_path, self._app_name))
        print("%s packages installed" % package)

    def analytics(self):
        """

        Related Pages:

          https://angular.io/cli
        """
        pass

    def help(self, options: dict = None):
        """
        Lists available commands and their short descriptions.

        Related Pages:

          https://angular.io/cli

        :param options:
        """
        if options is None:
            subprocess.run('ng help', shell=True, cwd=self._app_path)
        else:
            subprocess.run('ng help %s' % options, shell=True, cwd=os.path.join(self._app_path, self._app_name))

    def test(self, app_name: str = None):
        """

        Related Pages:

          https://angular.io/cli

        :param app_name:
        """
        app_name = app_name or self._app_name
        if app_name is None:
            raise ValueError("An Angular application name is required!")

        subprocess.run('ng test %s' % app_name, shell=True, cwd=os.path.join(self._app_path, app_name))

    def build(self, app_name: str = None):
        """
        Compiles an Angular app into an output directory named dist/ at the given output path.
        Must be executed from within a workspace directory.

        Related Pages:

          https://angular.io/cli

        :param app_name:
        """
        app_name = app_name or self._app_name
        if app_name is None:
            raise ValueError("An Angular application name is required!")

        subprocess.run('ng build %s' % app_name, shell=True, cwd=os.path.join(self._app_path, app_name))

    def version(self):
        """ Builds and serves an Angular app, then runs end-to-end tests using Protractor """
        subprocess.run('ng version', shell=True, cwd=os.path.join(self._app_path, self._app_name))

    def serve(self, host: str = "localhost", port: int = 8081):
        """
        Builds and serves an Angular app, then runs end-to-end tests using Protractor.

        Related Pages:

          https://angular.io/cli/serve

        :param host: The server url
        :param port: The server port
        """
        subprocess.run('ng serve --open --host=%s --port=%s' % (host, port), shell=True,
                       cwd=os.path.join(self._app_path, self._app_name))

    def npm(self, packages: list):
        """
        This will add the npm requirements to the Angular app but also update directly the angular.json for anything
        needed at the start of the application.

        This is mainly used for generic and common libraries like Jquery and Jquery UI

        :param packages: The packages names to install
        """
        if self.envs is not None:
            for env in self.envs:
                subprocess.run(env, shell=True, cwd=os.path.join(self._app_path, self._app_name))
        packages = node.npm_packages(packages)
        subprocess.run('npm install %s' % " ".join(packages), shell=True,
                       cwd=os.path.join(self._app_path, self._app_name))
        map_modules = {
            "jquery": "./node_modules/jquery/dist/jquery.min.js",
            "chart.js": "./node_modules/chart.js/dist/Chart.js",
            "jquery-ui-dist": "./node_modules/jquery-ui-dist/jquery-ui.js",
        }
        angular_conf_path = os.path.join(self._app_path, self._app_name, "angular.json")
        with open(angular_conf_path) as f:
            angular_conf = json.load(f)
        config_updated = False
        scripts = angular_conf["projects"][self._app_name]["architect"]['build']['options']["scripts"]
        for mod, path in map_modules.items():
            if mod in packages:
                if path not in scripts:
                    config_updated = True
                    scripts.append(path)
        if config_updated:
            with open(angular_conf_path, "w") as f:
                json.dump(angular_conf, f, indent=2)

    @property
    def create(self) -> NGModule:
        """ Shortcut to the various generate entry points in the Angular Framework. """
        return NGModule(os.path.join(self._app_path, self._app_name))

    def generate(self, schematic: str, name: str):
        """
        Generates and/or modifies files based on a schematic.

        Related Pages:

          https://angular.io/cli/generate

        :param schematic:
        :param name:
        """
        subprocess.run(
            'ng generate %s %s' % (schematic, name), shell=True, cwd=os.path.join(self._app_path, self._app_name))


class RouteModule:

    def __init__(self, app_path: str, app_name: str, file_name: str = None):
        self._app_path, self._app_name = app_path, app_name
        self.file_name = file_name or 'app-routing.module.ts'
        self.modules, self.routes, self.ng_modules = {}, {}, None

        # parse the Angular route module
        imported_module_pattern = re.compile("import { (.*) } from '(.*)';")
        imported_route_pattern = re.compile("{ path: '(.*)', component: (.*) }")

        self.ngModule = "@NgModule"
        with open(os.path.join(self._app_path, app_name, 'src', 'app', 'app-routing.module.ts')) as f:
            content = f.read()
            split_content = content.split("@NgModule")
            for module_def in imported_module_pattern.findall(split_content[0]):
                self.modules[module_def[0]] = module_def[1]

            for alias, component in imported_route_pattern.findall(split_content[0]):
                self.routes[component] = alias
            self.ngModule = "%s%s" % (self.ngModule, split_content[1])

    def add(self, component: str, alias: str, path: str):
        """
        Add an entry to the Angular routing app.

        :param component: String the Component module name
        :param alias: The url shortcut
        :param path: The component relative path
        """
        if self.ng_modules is None:
            self.ng_modules = NgModules(self._app_path, self._app_name)
            self.ng_modules.modules[component] = "../../%s/%s" % (
                path.replace("\\", "/"), COMPONENT_NAME_TEMPLATE % alias)
        self.modules[component] = "../../%s/%s" % (path.replace("\\", "/"), COMPONENT_NAME_TEMPLATE % alias)
        self.routes[component] = alias

    def export(self, file_name=None, target_path: str = None):
        """
        Publish the new Angular routing Application.

        :param file_name: Optional. The filename
        :param target_path: Optional. The new routing file
        """
        file_name = 'app-routing.module.ts' or self.file_name
        if target_path is None:
            target_path = []
        target_path.append(file_name)
        with open(os.path.join(self._app_path, self._app_name, 'src', 'app', *target_path), "w") as f:
            for k, v in self.modules.items():
                f.write("import { %s } from '%s';\n" % (k, v))
            f.write("\n\n")
            f.write("const routes: Routes = [\n")
            for k, v in self.routes.items():
                f.write("    { path: '%s', component: %s },\n" % (v, k))
            f.write("]\n\n")
            f.write("\n")
            f.write(self.ngModule)
        self.ng_modules.export(file_name)


class NgModules:

    def __init__(self, app_path: str, app_name: str, file_name: str = None):
        self._app_path, self._app_name = app_path, app_name
        self.file_name = file_name or 'app.module.ts'
        self.modules, self.imports, self.declarations, self.providers, self.bootstrap = {}, [], [], [], []

        # parse the Angular route module
        imported_module_pattern = re.compile("import { (.*) } from '(.*)';")
        with open(os.path.join(self._app_path, self._app_name, 'src', 'app', self.file_name)) as f:
            content = f.read()
            for module_def in imported_module_pattern.findall(content):
                self.modules[module_def[0]] = module_def[1]

            matches = re.search(r"\@NgModule\((.*)?\)", content, re.DOTALL)
            json_stuff = re.sub(r"([a-z_\-\.A-Z0-9]+)", r'"\1"', matches.group(1))
            json_stuff = re.sub(r",[\W]*?([\}\]])", r"\n\1", json_stuff)
            json_dict = json.loads(json_stuff)
            self.declarations = json_dict['declarations']
            self.providers = json_dict['providers']
            self.imports = json_dict['imports']
            self.bootstrap = json_dict['bootstrap']

        # Add mandatory core modules
        self.add_import("HttpClientModule", '@angular/common/http')

    def add(self, component: str, path: str):
        """

        :param component: The component name
        :param path: The component path
        """
        self.modules[component] = path

    def add_import(self, component: str, path: str):
        """

        :param component:
        :param path:
        """
        self.modules[component] = path

        if component not in self.imports:
            self.imports.append(component)

    def export(self, file_name: str = None, target_path: str = None):
        """

        :param file_name: Optional. The filename
        :param target_path:
        """
        file_name = 'app.module.ts' or self.file_name
        if target_path is None:
            target_path = []
        target_path.append(file_name)
        with open(os.path.join(self._app_path, self._app_name, 'src', 'app', *target_path), "w") as f:
            for k, v in self.modules.items():
                f.write("import { %s } from '%s';\n" % (k, v))
            f.write("\n\n")
            f.write("@NgModule({\n")
            for name, vars in [
                ("declarations", self.declarations), ('imports', self.imports), ('providers', self.providers),
                ('bootstrap', self.bootstrap)]:
                f.write("  %s: [\n" % name)
                for d in vars:
                    f.write("    %s,\n" % d)
                f.write("  ],\n")
            f.write("})\n\n")
            f.write("export class AppModule { }")


class ComponentSpec:

    def __init__(self, app_path: str, app_name: str, alias: str, name: str):
        self.imports, self.vars = {}, {}
        self._app_path, self._app_name, self.__path = app_path, app_name, 'apps'
        self.alias, self.name = alias, name
        self.__comp_structure = {}

    def export(self, path: str = None, target_path: str = None):
        """
        Export the spec of the component.

        TODO: make this generation more flexible

        :param path:
        :param target_path: for example ['src', 'app']
        """
        self.__path = path or self.__path
        if target_path is None:
            target_path = []
        target_path.append(self.__path)
        module_path = os.path.join(self._app_path, self._app_name, *target_path)
        if not os.path.exists(module_path):
            os.makedirs(module_path)

        with open(os.path.join(module_path, "%s.spec.ts" % COMPONENT_NAME_TEMPLATE % self.alias), "w") as f:
            f.write('''
import { TestBed, async } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { %(name)s } from './app.component';

describe('%(name)s', () => {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [
        RouterTestingModule
      ],
      declarations: [
        %(name)s
      ],
    }).compileComponents();
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(%(name)s);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have as title '%(alias)s'`, () => {
    const fixture = TestBed.createComponent(%(name)s);
    const app = fixture.componentInstance;
    expect(app.title).toEqual('%(alias)s');
  });

  it('should render title', () => {
    const fixture = TestBed.createComponent(%(name)s);
    fixture.detectChanges();
    const compiled = fixture.nativeElement;
    expect(compiled.querySelector('.content span').textContent).toContain('%(alias)s app is running!');
  });
});
''' % {"path": module_path, 'name': self.name, 'alias': self.alias})


class Components:

    def __init__(self, app: str, count: int = 0, page: primitives.PageModel = None):
        self._app, self.count_comp, self.page = app, count, page

    def router(self):
        """

    """
        from epyk.web.components.angular import standards

        return standards.Router(self.page, None)

    @property
    def materials(self):
        """

        """
        from epyk.web.components.angular import materials

        return materials.Components(app=self._app, page=self.page)

    @property
    def primeng(self):
        """

        """
        from epyk.web.components.angular import primeng

        return primeng.Components(self.page)


class App:

    def __init__(self, app_path: str, app_name: str, alias: str, name: str,
                 page: primitives.PageModel = None, target_folder: str = "views"):
        self.imports = {'Component': '@angular/core',
                        # 'HttpClient': '@angular/common/http',
                        # 'HttpHeaders': '@angular/common/http', 'Injectable': '@angular/core',
                        # 'ViewChild': '@angular/core'
                        }
        self.vars, self.__map_var_names, self.page, self.file_name = {}, {}, page, None
        self._app_path, self._app_name, self._node_path = app_path, app_name, app_path
        self.alias, self.__path, self.className, self.__components = alias, target_folder, name, None
        self.__comp_structure, self.htmls, self.__fncs, self.__injectable_prop = {}, [], {}, {'providedIn': 'root'}
        self.spec = ComponentSpec(app_path, app_name, alias, name)
        self.comps, self.module_path = {}, None

    @property
    def clarity(self):
        """

        """
        from epyk.web.components.angular import clarity

        return clarity.Package(self.page, self)

    @property
    def bootstrap(self):
        """

        """
        from epyk.web.components.angular import bootstrap

        return bootstrap.Package(self.page, self)

    def add_var(self, name: str, value=None):
        """

        :param name:
        :param value:
        """
        if value is not None:
            if 'constructor' not in self.__comp_structure:
                self.__comp_structure['constructor'] = []
            self.__comp_structure['constructor'].append("this.%s = %s" % (name, json.dumps(value)))
        self.vars[name] = value

    def add_fnc(self, name: str, funcs):
        """

        :param name:
        :param funcs:
        """
        self.__fncs[name] = funcs

    def add_imports(self, name: str, path: str):
        """

        :param str name:
        :param str path:
        """
        pass

    @property
    def components(self) -> Components:
        """

        """
        if self.__components is None:
            self.__components = Components(self, page=self.page)
        return self.__components

    def constructor(self):
        pass

    def ngOnInit(self):
        pass

    def ngAfterViewInit(self):
        return

    @property
    def name(self):
        """ Return the prefix of the component module (without any extension) """
        return self.file_name or COMPONENT_NAME_TEMPLATE % self.alias

    def http(self, end_point: str, js_funcs, profile):
        """

        :param end_point:
        :param js_funcs:
        :param profile:
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        end_point = JsUtils.jsConvertData(end_point, None)
        return "this.httpClient.post('http://127.0.0.1:5000/' + %s, {}).subscribe((data)=>{ %s });" % (
            end_point, js_funcs)

    @property
    def path(self) -> str:
        """ Return the full path of the component modules """
        return os.path.join("../../", self.__path, self.name).replace("\\", "/")

    def export(self, path: str = None, target_path: str = None):
        """

        :param path:
        :param target_path: for example ['src', 'app']
        """
        self.__path = path or self.__path
        if target_path is None:
            target_path = []
        target_path.append(self.__path)
        self.module_path = os.path.join(self._app_path, *target_path)
        print("export  to: %s" % self.module_path)
        if not os.path.exists(self.module_path):
            os.makedirs(self.module_path)
        page = self.page.outs.web()
        self.spec.export(path=self.module_path, target_path=None)
        self.__fncs['ngAfterViewInit'] = [page['jsFrgs']]

        with open(os.path.join(self.module_path, "%s.ts" % self.name), "w") as f:
            for comp, path in self.imports.items():
                f.write("import { %s } from '%s';\n" % (comp, path))
            for path, classNames in self.page._props.get('web', {}).get('modules', {}).items():
                f.write("import { %s } from '%s';\n" % (",".join(classNames), path))
            if page['jsFrgsCommon']:
                f.write("import { %s } from './module_%s.js';" % (
                    ", ".join(list(page['jsFrgsCommon'].keys())), self.alias.replace("-", "_")))
            f.write("\n")
            if 'jquery' in self.page.jsImports:
                f.write("\ndeclare var $: any;")
                f.write("\n")
            # All applications need this as they will interact with a Flask backend
            # f.write("@Injectable({\n")
            # for k , v in self.__injectable_prop.items():
            #  f.write(" %s: %s\n" % (k, json.dumps(v)))
            # f.write("})\n")
            f.write("\n")
            f.write("@Component({\n")
            f.write("  selector: '%s',\n" % self.alias)
            f.write("  templateUrl: '%s',\n" % "./%s.html" % self.name)
            f.write("  styleUrls: ['%s']\n" % "./%s.css" % self.name)
            f.write("})\n")
            f.write("\n")
            f.write("export class %s {\n" % self.className)
            f.write("  // Component link section\n")
            for k, v in self.comps.items():
                f.write("  @ViewChild('%s') %s: any;;\n" % (k, k))

            f.write("  // Variable section\n")
            for var in self.vars.keys():
                f.write("  %s;\n" % var)
            f.write("\n")
            if 'constructor' in self.__comp_structure:
                f.write("  constructor(private httpClient: HttpClient){\n")
                f.write("    %s" % "; ".join(self.__comp_structure['constructor']))
                f.write("  }\n")
            f.write("\n")
            for name, fnc_def in self.__fncs.items():
                f.write("  %s(){ %s } \n" % (name, ";".join(fnc_def)))
            f.write("}\n")

        if page['jsFrgsCommon']:
            with open(os.path.join(self.module_path, "module_%s.js" % self.alias.replace("-", "_")), "w") as f:
                for js_dep in JS_MODULES_IMPORTS:
                    if js_dep in self.page.jsImports:
                        f.write("%s\n" % JS_MODULES_IMPORTS[js_dep])
                for buider in page['jsFrgsCommon'].values():
                    f.write("export %s;\n" % buider)

        with open(os.path.join(self.module_path, "%s.html" % self.name), "w") as f:
            f.write("%(cssImports)s\n\n%(body)s" % page)

        with open(os.path.join(self.module_path, "%s.css" % self.name), "w") as f:
            f.write(page['cssStyle'])


class Angular(node.Node):

    def create(self, name: str):
        """ To create a new project, run:

        Related Pages:

          https://cli.vuejs.org/guide/creating-a-project.html

        :param name: The application name
        """
        subprocess.run('ng new %s' % name, shell=True, cwd=self._app_path)

    def serve(self, app_name: str, host: str = "localhost", port: int = 8081):
        """
        Builds and serves an Angular app, then runs end-to-end tests using Protractor.

        Related Pages:

          https://angular.io/cli/serve

        :param app_name:
        :param host:
        :param port:
        """
        path = os.path.join(self._app_path, app_name)
        subprocess.run('ng serve --open --host=%s --port=%s' % (host, port), shell=True, cwd=path)

    def router(self, app_name: str):
        """

        Related Pages:

          https://stackoverflow.com/questions/44990030/how-to-add-a-routing-module-to-an-existing-module-in-angular-cli-version-1-1-1

        :param app_name:
        """
        path = os.path.join(self._app_path, app_name)
        subprocess.run('ng generate module app-routing --module app --flat', shell=True, cwd=path)
        with open(os.path.join(self._app_path, app_name, "src", "app", "app-routing.module.ts"), "w") as f:
            f.write('''
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';


const routes: Routes = [
]


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

''')

    def ng(self, app_name: str = None):
        """
        Angular specific command lines

        Related Pages:

          https://angular.io/cli/

        :param app_name: The angular application name
        """
        app_name = app_name or self._app_name
        return NG(self._app_path, app_name, self.envs)

    def cli(self, app_name: str):
        """
        Angular specific command lines

        Related Pages:

          https://angular.io/cli/

        :param app_name: The angular application name
        """
        app_name = app_name or self._app_name
        return NG(self._app_path, app_name, self.envs)

    def page(self, selector: str = None, name: str = None, page: primitives.PageModel = None, auto_route: bool = False,
             target_folder: str = "apps"):
        """
        Create a specific Application as a component in the Angular framework.

        Unlike a basic component, the application will be routed to be accessed directly.

        :param page: A report object
        :param selector: The url route for this report in the Angular app
        :param name: The component classname in the Angular framework
        :param auto_route:
        :param target_folder:
        """
        if name is None:
            script = os.path.split(sys._getframe().f_back.f_code.co_filename)[1][:-3]
            name = "".join([s.capitalize() for s in script.split("_")])
            if selector is None:
                selector = script.replace("_", "-")
        page = page or Page.Report()
        self._page = App(self._app_path, self._app_name, selector, name, page=page, target_folder=target_folder)
        if auto_route:
            self.route().add(self._app_name, self._page.alias, self._page.path)
        return self._page

    def ng_modules(self, app_name: str = None, file_name: str = None) -> NgModules:
        """
        Read the file app.module.ts

        :param app_name: Optional. THe Angular application name
        :param file_name: Optional.
        """
        if self._fmw_modules is None:
            if self._route is not None and self._route.ng_modules is not None:
                self._fmw_modules = self._route.ng_modules
            else:
                self._fmw_modules = NgModules(self._app_path, app_name or self._app_name, file_name)
        return self._fmw_modules

    def route(self, app_name: str = None, file_name: str = None) -> RouteModule:
        """
        Read the file app-routing.module.ts from the Angular app

        :param app_name: Optional. THe Angular application name
        :param file_name: Optional.
        """
        if self._route is None:
            path, name = os.path.split(self._app_path)
            self._route = RouteModule(path, name, file_name)
        return self._route

    def publish(self, app_name: str = None, target_path: list = None):
        """

        :param app_name:
        :param target_path: List for example ['src', 'app']
        """
        if self._page is not None:
            self._page.export(target_path=target_path)
        node.requirements(self._page.page, self._page.module_path)
        if self._route is not None:
            self._route.export()

    def home_page(self, page, app_name: str = None, with_router: bool = False):
        """
        Change the Angular App home page

        :param page:
        :param app_name:
        :param with_router:
        """
        with open(os.path.join(self._app_path, app_name, "src", "app", "app.component.html")) as f:
            html_home = f.read()
        self._app_name = app_name
        router_outlet = "<router-outlet></router-outlet>" in html_home
        self._app_path = os.path.join(self._app_path, self._app_name)
        home = self.page("app-root", name="AppComponent", page=page, target_folder="src/app")
        if with_router:
            home.components.router()
        home.file_name = "app.component"
        home.export()
