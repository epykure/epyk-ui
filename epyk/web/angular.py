from ..core.js import JsUtils
from ..core.css import css_files_loader
from ..core.html import Standalone, html_template_loader
from . import npm, node, templates

import logging
import zipfile
import re
import os
import json
import subprocess
from collections import OrderedDict
from typing import Any, Dict, List, Union
from pathlib import Path


# Angular system files / templates
COMPONENT_NAME_TEMPLATE = "app.%s.component"
ANGULAR_JSON_CONFIG = "angular.json"
APP_FILE = 'app.module.ts'
APP_ROUTE_FILE = "app-routing.module.ts"
PROJECT_SRC_ALIAS = "src"


def to_view(web_page, selector: str, app_path: Path) -> Dict[str, str]:
    """

    """
    class_name = node.selector_to_clss(selector)
    return to_component(web_page.outs.component(selector=selector), name="", out_path=app_path)


def to_component(
        component: Standalone.Component, name: str = "ek-angular-{selector}-{version}", out_path: Union[str, Path] = None,
        version: str = None, init_value: Any = "", init_options: dict = None) -> Dict[str, str]:
    """
    Export of a standalone component to an Angular one.

    :param component: Component object
    :param name: Component's name
    :param out_path: Output path for component
    :param version: Version number for the component
    :param init_value: Values to be passed to the constructor
    :param init_options: Default options for the component
    """
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
            "selector": component.selector,
            "asset_class": component.__name__,
        })

    component_files["component"] = name.format(selector=component.selector, version=version) + ".component.ts"
    js_frgs = ["@Input() %s" % var for var in html_def['vars']]
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
        app_path: Union[str, Path],
        folder: str = "assets",
        name: str = "{selector}",
        raise_exception: bool = False,
        view_path: str = node.APP_FOLDER
) -> dict:
    """
      This will add the component directly tp the src folder in the linked application.
      All components generated will be put in a sub folder.

      To start the angular application: ng serve --open

      This will also update the required angular system files accordingly

      :param components: List of components to add to an Angular application
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
            root_path=Path(app_path, PROJECT_SRC_ALIAS, view_path))
    angular_config_path = Path(app_path, ANGULAR_JSON_CONFIG)
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
    app_module_path = Path(app_path, PROJECT_SRC_ALIAS, view_path, "app.module.ts")
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


def app(root_path: Union[Path, str], name: str = None):
    """
    Get the Angular server path.

    :param root_path: The server path
    :param name: Optional. The application name on the server
    """
    return Angular(root_path, name)


class NGModule:

    def __init__(self, server):
        """ This will run CLI in the Angular project """
        self.server = server

    def class_(self, name: str):
        """
        Creates a new generic class definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#class-command

        :param name: The name of the interface
        """
        subprocess.run('ng generate class %s' % name, shell=True, cwd=self.server.app_path)

    def component(self, name: str):
        """
        Creates a new generic component definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#component-command

        :param name: The name of the interface
        """
        subprocess.run('ng generate component %s' % name, shell=True, cwd=self.server.app_path)

    def directive(self, name: str):
        """
        Creates a new generic directive definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#directive-command

        :param name: The name of the interface
        """
        subprocess.run('ng generate directive %s' % name, shell=True, cwd=self.server.app_path)

    def enum(self, name: str):
        """
        Generates a new, generic enum definition for the given or default project.

        Related Pages:

          https://angular.io/cli/generate#enum-command

        :param name: The name of the interface
        """
        subprocess.run('ng generate enum %s' % name, shell=True, cwd=self.server.app_path)

    def guard(self, name: str):
        """
        Generates a new, generic route guard definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#guard-command

        :param name: The name of the new route guard
        """
        subprocess.run('ng generate guard %s' % name, shell=True, cwd=self.server.app_path)

    def interceptor(self, name: str):
        """
        Creates a new, generic interceptor definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#interceptor-command

        :param name: The name of the interceptor
        """
        subprocess.run('ng generate interceptor %s' % name, shell=True, cwd=self.server.app_path)

    def interface(self, name: str, type: str):
        """
        Creates a new generic interface definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#interface-command

        :param name: The name of the interface
        :param type: Adds a developer-defined type to the filename, in the format "name.type.ts"
        """
        subprocess.run('ng generate interface %s %s' % (name, type), shell=True, cwd=self.server.app_path)

    def library(self, name: str, type: str):
        """
        Creates a new generic library project in the current workspace.

        Related Pages:

          https://angular.io/cli/generate#library-command

        :param name: The name of the interface
        :param type:
        """
        subprocess.run('ng generate library %s %s' % (name, type), shell=True, cwd=self.server.app_path)

    def module(self, name: str, type: str):
        """
        Creates a new generic NgModule definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#library-command

        :param name: The name of the interface
        :param type:
        """
        subprocess.run('ng generate module %s %s' % (name, type), shell=True, cwd=self.server.app_path)

    def service(self, name: str, type: str):
        """
        Creates a new, generic service definition in the given or default project.

        Related Pages:

          https://angular.io/cli/generate#library-command

        :param name: The name of the interface
        :param type:
        """
        subprocess.run('ng generate service %s %s' % (name, type), shell=True, cwd=self.server.app_path)


class NG:

    def __init__(self, server, env: str = None):
        self.server, self.envs = server, env

    def e2e(self, app_name: str = None):
        """
        Builds and serves an Angular app, then runs end-to-end tests using Protractor.

        Related Pages:

          https://angular.io/cli/e2e

        :param app_name: The application name
        """
        if app_name:
            self._app_name = app_name
        if app_name is None:
            raise ValueError("An Angular application name is required!")

        subprocess.run('ng e2e %s' % app_name, shell=True, cwd=self.server.app_path)

    def lint(self, app_name: str = None):
        """
        Builds and serves an Angular app, then runs end-to-end tests using Protractor.

        Related Pages:

          https://angular.io/cli/lint

        :param app_name: The application name
        """
        app_name = app_name or self.server.app_path.name
        subprocess.run('ng lint %s' % app_name, shell=True, cwd=self.server.root_path)

    def new(self, name: str, path: str = None):
        """
        Builds and serves an Angular app, then runs end-to-end tests using Protractor.

        Related Pages:

          https://angular.io/cli/new

        :param name: The application name
        :param path: The server path
        """
        if path is not None:
            subprocess.run('ng new %s --directory %s' % (name, path), shell=True, cwd=self.server.app_path)
        else:
            subprocess.run('ng new %s' % name, shell=True, cwd=self.server.app_path)
        logging.info('ng new %s' % name)

    def doc(self, keyword: str):
        """
        Opens the official Angular documentation (angular.io) in a browser, and searches for a given keyword.

        Related Pages:

          https://angular.io/cli

        :param keyword:
        """
        subprocess.run('ng doc %s' % keyword, shell=True, cwd=self.server.app_path)

    def add(self, package: str):
        """
        Add package to the Angular server node modules.

        Related Pages:

          https://angular.io/cli

        :param package: The package name
        """
        if self.envs is not None:
            for env in self.envs:
                subprocess.run(env, shell=True, cwd=self.server.app_path)
        subprocess.run('ng add %s' % package, shell=True, cwd=self.server.app_path)
        logging.info("%s packages installed" % package)

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
            subprocess.run('ng help', shell=True, cwd=self.server.app_path)
        else:
            subprocess.run('ng help %s' % options, shell=True, cwd=self.server.app_path)

    def test(self, app_name: str = None):
        """
        Run the set of tests for the given application.

        Related Pages:

          https://angular.io/cli

        :param app_name: The application name (folder name)
        """
        app_name = app_name or self._app_name
        if app_name is None:
            raise ValueError("An Angular application name is required!")

        subprocess.run('ng test %s' % app_name, shell=True, cwd=self.server.app_path)

    def build(self, app_name: str = None):
        """
        Compiles an Angular app into an output directory named dist/ at the given output path.
        Must be executed from within a workspace directory.

        Related Pages:

          https://angular.io/cli

        :param app_name: The application name (folder name)
        """
        app_name = app_name or self._app_name
        if app_name is None:
            raise ValueError("An Angular application name is required!")

        subprocess.run('ng build %s' % app_name, shell=True, cwd=self.server.app_path)

    def version(self):
        """ Builds and serves an Angular app, then runs end-to-end tests using Protractor """
        subprocess.run('ng version', shell=True, cwd=self.server.app_path)

    def serve(self, host: str = "localhost", port: int = 8081):
        """
        Builds and serves an Angular app, then runs end-to-end tests using Protractor.

        Related Pages:

          https://angular.io/cli/serve

        :param host: The server url
        :param port: The server port
        """
        subprocess.run('ng serve --open --host=%s --port=%s' % (host, port), shell=True, cwd=self.server.app_path)

    def npm(self, packages: List[str], styles: List[str] = None, scripts: List[str] = None):
        """
        This will add the npm requirements to the Angular app but also update directly the angular.json for anything
        needed at the start of the application.

        This is mainly used for generic and common libraries like Jquery and Jquery UI

        :param packages: The package's names to install
        :param styles: All the bespoke styles to be added to the global configuration
        :param scripts: All the bespoke scripts to be added to the global configuration
        """
        if self.envs is not None:
            for env in self.envs:
                subprocess.run(env, shell=True, cwd=self.server.app_path)
        packages = node.npm_packages(packages)
        subprocess.run('npm install %s' % " ".join(packages), shell=True, cwd=self.server.app_path)
        angular_config_path = Path(self.server.app_path, ANGULAR_JSON_CONFIG)
        if angular_config_path.exists():
            with open(angular_config_path) as ap:
                angular_config = json.loads(ap.read(), object_pairs_hook=OrderedDict)
                if styles is not None:
                    for style in styles:
                        angular_config["projects"][self.server.app_path.name]["architect"]["build"]["options"]["styles"].insert(0, style)
                if scripts is not None:
                    for script in scripts:
                        angular_config["projects"][self.server.app_path.name]["architect"]["build"]["options"]["scripts"].insert(0, script)
            with open(angular_config_path, "w") as ap:
                json.dump(angular_config, ap, indent=2)

    @property
    def create(self) -> NGModule:
        """ Shortcut to the various generate entry points in the Angular Framework. """
        return NGModule(self.server)

    def generate(self, schematic: str, name: str):
        """
        Generates and/or modifies files based on a schematic.

        Related Pages:

          https://angular.io/cli/generate

        :param schematic:
        :param name:
        """
        subprocess.run('ng generate %s %s' % (schematic, name), shell=True, cwd=self.server.app_path)


class RouteModule:

    def __init__(self, component: str, alias: str, server):
        self.component, self.alias, self.server = component, alias, server
        self.modules, self.routes, self.ng_modules = {}, {}, None

        # parse the Angular route module
        imported_module_pattern = re.compile("import { (.*) } from '(.*)';")
        imported_route_pattern = re.compile("{ path: '(.*)', component: (.*) }")
        router_file = Path(server.views_path, APP_ROUTE_FILE)
        if router_file.exists():
            self.ngModule = "@NgModule"
            with open(router_file) as f:
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
            self.ng_modules = NgModules(self.server)
            self.ng_modules.modules[component] = "../../%s/%s" % (
                path.replace("\\", "/"), COMPONENT_NAME_TEMPLATE % alias)
        self.modules[component] = "../../%s/%s" % (path.replace("\\", "/"), COMPONENT_NAME_TEMPLATE % alias)
        self.routes[component] = alias

    def export(self, folder: str = None):
        """
        Publish the new Angular routing Application.

        :param folder: Optional. The new routing file
        """
        if folder is not None:
            target_path = Path(self.server.views_path, folder, APP_ROUTE_FILE)
        else:
            target_path = Path(self.server.views_path, APP_ROUTE_FILE)
        with open(target_path, "w") as f:
            for k, v in self.modules.items():
                f.write("import { %s } from '%s';\n" % (k, v))
            f.write("\n\n")
            f.write("const routes: Routes = [\n")
            for k, v in self.routes.items():
                f.write("    { path: '%s', component: %s },\n" % (v, k))
            f.write("]\n\n")
            f.write("\n")
            f.write(self.ngModule)
        self.ng_modules.export(APP_ROUTE_FILE)


class NgModules:

    def __init__(self, server):
        self.server = server
        self.modules, self.imports, self.declarations, self.providers, self.bootstrap = {}, [], [], [], []

        # parse the Angular route module
        imported_module_pattern = re.compile("import { (.*) } from '(.*)';")
        with open(Path(self.server.views_path, APP_ROUTE_FILE)) as f:
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

    def export(self, file_name: Path = None):
        """

        :param file_name: Optional. The filename
        """
        with open(Path(self.server.views_path, file_name or APP_FILE), "w") as f:
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

    def __init__(self, server):
        self.imports, self.vars, self.server = {}, {}, server
        self.__comp_structure = {}

    def export(self, selector: str):
        """
        Export the spec of the component.

        TODO: make this generation more flexible

        :param selector:
        """
        if not self.server.views_path.exists():
            self.server.views_path.mkdir(parents=True, exist_ok=True)
        with open(Path(self.server.views_path, "%s.spec.ts" % COMPONENT_NAME_TEMPLATE % selector), "w") as f:
            f.write(templates.ANGULAR_COMPONENT_SPEC % {"asset_class": selector, "selector": "app"})


class Components:

    def __init__(self, app: str, count: int = 0):
        self._app, self.count_comp, self.page = app, count, app.server.page

    def router(self):
        """ """
        from epyk.web.components.angular import standards
        return standards.Router(self.page, None)

    @property
    def materials(self):
        """ The Angular Material components """
        from epyk.web.components.angular import materials
        return materials.Components(app=self._app, page=self.page)

    @property
    def primeng(self):
        """ The PrimeNG Angular components """
        from epyk.web.components.angular import primeng
        return primeng.Components(self)


class App:

    def __init__(self, server):
        self.imports = {'Component': '@angular/core',
                        # 'HttpClient': '@angular/common/http',
                        # 'HttpHeaders': '@angular/common/http', 'Injectable': '@angular/core',
                        # 'ViewChild': '@angular/core'
                        }
        self.vars, self.__map_var_names, self.server, self.file_name = {}, {}, server, None
        self.__components = None
        self.__comp_structure, self.htmls, self.__fncs, self.__injectable_prop = {}, [], {}, {'providedIn': 'root'}
        self.spec = ComponentSpec(server)
        self.comps, self.module_path = {}, None

    @property
    def clarity(self):
        """ Load Angular Clarity components """
        from epyk.web.components.angular import clarity
        return clarity.Package(self.server.page, self)

    @property
    def bootstrap(self):
        """ Load Angular Bootstrap components """
        from epyk.web.components.angular import bootstrap
        return bootstrap.Package(self.server.page, self)

    def add_var(self, name: str, value: Any = None):
        """
        Add a global variable name.

        :param name: Variable's name
        :param value: Variable's content
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
        """  Shortcut to prefined framework components """
        if self.__components is None:
            self.__components = Components(self)
        return self.__components

    def constructor(self):
        pass

    def ngOnInit(self):
        pass

    def ngAfterViewInit(self):
        return

    def http(self, end_point: str, js_funcs, profile, server: str, port: int):
        """

        :param end_point:
        :param js_funcs:
        :param profile:
        :param server:
        :param port:
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        end_point = JsUtils.jsConvertData(end_point, None)
        return "this.httpClient.post('%(server)s:%(port)s/' + %(end_point)s, {}).subscribe((data)=>{ %(funcs)s });" % {
            "funcs": js_funcs, "end_point": end_point, "server": server, "port": port}

    def export(self, selector: str):
        """

        :param selector:
        """

        logging.info("export %s to: %s" % (selector, self.server.views_path))
        self.server.views_path.mkdir(parents=True, exist_ok=True)

        # Write all the component
        add_to_app(self.server.page._props["schema"].values(), self.server.app_path, folder=self.server.assets_path.name)

        # Write the view
        to_view(self.server.page, selector, self.server.views_path)


class Angular(node.Node):

    def __init__(self, root_path: str, name: str = None, page = None, app_folder: str = node.APP_FOLDER,
                 assets_folder: str = node.ASSET_FOLDER):
        super(Angular, self).__init__(root_path, name, page)
        self._app_folder, self._app_asset, self.__clis = app_folder, assets_folder, None
        self.__app = None # The active application to the server

    @property
    def routing(self) -> str:
        """ The system routing file name """
        return APP_ROUTE_FILE

    @property
    def views_path(self) -> Path:
        """ The application views path """
        return Path(self._app_path, self._app_name, PROJECT_SRC_ALIAS, self._app_folder)

    @property
    def node_modules_path(self) -> Path:
        """ The application node_modules path """
        return Path(self._app_path, self._app_name, "node_modules")

    def assets_path(self):
        """ The application assets / components path """
        return Path(self._app_path, self._app_name, PROJECT_SRC_ALIAS, self._app_asset)

    def create(self, name: str):
        """
        To create a new project, run:

        Related Pages:

          https://cli.vuejs.org/guide/creating-a-project.html

        :param name: The application name
        """
        project_path = Path(self.root_path, name)
        self._app_name = name
        if not project_path.exists():
            logging.info("Creating %s to this location %s" % (name, self.root_path))
            subprocess.run('ng new %s' % name, shell=True, cwd=str(self.root_path))
        else:
            logging.info("Application %s already available here %s" % (name, self.root_path))

    def serve(self, name: str = None, host: str = None, port: int = None):
        """
        Builds and serves an Angular app, then runs end-to-end tests using Protractor.

        Related Pages:

          https://angular.io/cli/serve

        :param name: The application name
        :param host: The url name
        :param port: the server port
        """
        if name is not None:
            self._app_name = name
        subprocess.run('ng serve --open --host=%s --port=%s' % (
            host or self.HOST, port or self.PORT), shell=True, cwd=str(self.app_path))

    def router(self, name: str = None, **kwargs):
        """
        Create a routing file in the Angular application if is does not exist yet.

        Related Pages:

          https://stackoverflow.com/questions/44990030/how-to-add-a-routing-module-to-an-existing-module-in-angular-cli-version-1-1-1

        :param name: The application / view name to be added to the Angular server
        """
        if name is not None:
            self._app_name = name
        routing_file = Path(self.app_path, self.routing)
        if not routing_file.exists():
            subprocess.run('ng generate module app-routing --module app --flat', shell=True, cwd=str(self.app_path))
            with open(Path(self.app_path, self.routing), "w") as f:
                f.write(templates.ANGULAR_ROUTER)
        else:
            logging.warning("Router already exist please update it manually with the above content")

    def ng(self, app_name: str = None):
        """
        Angular specific command lines

        Related Pages:

          https://angular.io/cli/

        :param app_name: The angular application name
        """
        if app_name is not None:
            self._app_name = app_name
        return NG(self, self.envs)

    def cli(self, app_name: str = None):
        """
        Angular specific command lines

        Related Pages:

          https://angular.io/cli/

        :param app_name: The angular application name
        """
        if app_name is not None:
            self._app_name = app_name
        return NG(self, self.envs)

    def get_view(self, name: str = "") -> Path:
        """ Get the path for a specific view in the Application """
        return Path(self.views_path, name)

    def app(self, page=None, target_folder: str = node.APP_FOLDER) -> App:
        """
        Create a specific Application as a component in the Angular framework.

        Unlike a basic component, the application will be routed to be accessed directly.

        :param page: The web page (Report) object to be converted
        :param target_folder: The target sub folder for the applications (default app/)
        """
        if target_folder is not None:
            self._app_folder = target_folder
        if page is not None:
            self._page = page
        if self.__app is None:
            self.__app = App(server=self)
        return self.__app

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
                self._fmw_modules = NgModules(self)
        return self._fmw_modules

    def route(self, component: str, alias: str) -> RouteModule:
        """
        Read the file app-routing.module.ts from the Angular app

        :param component: The component reference / selector
        :param alias: The url alias
        """
        if self._route is None:
            self._route = RouteModule(component, alias, self)
        return self._route

    def publish(self, alias: str, selector: str = None, page=None, install: bool = False,
                target_folder: str = node.APP_FOLDER):
        """
        This will create the View / Application to the Angular server.
        It will also create all the underlying components used to render the different items to the page.

        :param alias: The url endpoint for the new page
        :param selector: Component / Application internal selector (name)
        :param page: The web page (Report) object to be converted
        :param install: Flag to force install of missing packages
        :param target_folder: The target sub folder for the applications (default app/)
        """
        if target_folder is not None:
            self._app_folder = target_folder
        if self.__app is None:
           self.__app = self.app(page)
        self.__app.export(selector=selector)
        self.route(selector, alias)
        packages = node.requirements(self.page, self.node_modules_path)
        missing_package = [k for k, v in packages.items() if not v]
        if install and missing_package:
            self.npm(missing_package)

    def home_page(self, page=None, app_name=None, install: bool = False,
                  target_folder: str = node.APP_FOLDER):
        """
        Change the Angular App home page

        :param page: The web page (Report) object to be converted
        :param app_name:
        :param install: Flag to force install of missing packages
        :param target_folder: The target sub folder for the applications (default app/)
        """
        if app_name is not None:
            self._app_name = app_name
        self.__app = self.app(page)
        self.__app.export(selector="app-root")
        packages = node.requirements(self.page, self.node_modules_path)
        missing_package = [k for k, v in packages.items() if not v]
        if install and missing_package:
            self.npm(missing_package)
