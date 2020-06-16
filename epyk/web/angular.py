"""
Draft version

"""

from epyk.core import Page
from epyk.web import node
from epyk.core.js import Imports

import sys
import re
import os
import json
import subprocess


def app(path, name=None):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param path:
  """
  return Angular(path, name)


def requirements(report):
  """
  Description:
  ------------
  Get the list of all the packages required in the Angular Application

  Packages can be installed in the app using the command
    > nmp install package1 package2 .....

  Attributes:
  ----------
  :param report: Python object. The report object
  """
  npms = []
  importMng = Imports.ImportManager(online=True, report=report)
  for req in importMng.cleanImports(report.jsImports, Imports.JS_IMPORTS):
    if 'register' in Imports.JS_IMPORTS[req]:
      if 'npm' in Imports.JS_IMPORTS[req]['register']:
        npms.append(Imports.JS_IMPORTS[req]['register']['npm'])
      else:
        print("No npm requirement defined for %s" % req)
    else:
      print("No npm requirement defined for %s" % req)
  return npms


JS_MODULES_IMPORTS = {
  'showdown': '''
import Showdown from 'showdown';
var showdown = Showdown;
'''
}


class NGModule(object):

  def __init__(self, ang_app_path):
    self._ang_app_path = ang_app_path

  def class_(self, name):
    """
    Description:
    ------------
    Creates a new generic class definition in the given or default project.

    Related Pages:

      https://angular.io/cli/generate#class-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate class %s' % name, shell=True, cwd=self._ang_app_path)

  def component(self, name):
    """
    Description:
    ------------
    Creates a new generic component definition in the given or default project.

    Related Pages:

			https://angular.io/cli/generate#component-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate component %s' % name, shell=True, cwd=self._ang_app_path)

  def directive(self, name):
    """
    Description:
    ------------
    Creates a new generic directive definition in the given or default project.

    Related Pages:

			https://angular.io/cli/generate#directive-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate directive %s' % name, shell=True, cwd=self._ang_app_path)

  def enum(self, name):
    """
    Description:
    ------------
    Generates a new, generic enum definition for the given or default project.

    Related Pages:

			https://angular.io/cli/generate#enum-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate enum %s' % name, shell=True, cwd=self._ang_app_path)

  def guard(self, name):
    """
    Description:
    ------------
    Generates a new, generic route guard definition in the given or default project.

    Related Pages:

      https://angular.io/cli/generate#guard-command

    Attributes:
    ----------
    :param name: String. The name of the new route guard.
    """
    subprocess.run('ng generate guard %s' % name, shell=True, cwd=self._ang_app_path)

  def interceptor(self, name):
    """
    Description:
    ------------
    Creates a new, generic interceptor definition in the given or default project.

    Related Pages:

      https://angular.io/cli/generate#interceptor-command

    Attributes:
    ----------
    :param name: String. The name of the interceptor.
    """
    subprocess.run('ng generate interceptor %s' % name, shell=True, cwd=self._ang_app_path)

  def interface(self, name, type):
    """
    Description:
    ------------
    Creates a new generic interface definition in the given or default project.

    Related Pages:

      https://angular.io/cli/generate#interface-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    :param type: String. Adds a developer-defined type to the filename, in the format "name.type.ts".
    """
    subprocess.run('ng generate interface %s %s' % (name, type), shell=True, cwd=self._ang_app_path)

  def library(self, name, type):
    """
    Description:
    ------------
    Creates a new generic library project in the current workspace.

    Related Pages:

      https://angular.io/cli/generate#library-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate library %s %s' % (name, type), shell=True, cwd=self._ang_app_path)

  def module(self, name, type):
    """
    Description:
    ------------
    Creates a new generic NgModule definition in the given or default project

    Related Pages:

      https://angular.io/cli/generate#library-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate module %s %s' % (name, type), shell=True, cwd=self._ang_app_path)

  def service(self, name, type):
    """
    Description:
    ------------
    Creates a new, generic service definition in the given or default project.

    Related Pages:

      https://angular.io/cli/generate#library-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate service %s %s' % (name, type), shell=True, cwd=self._ang_app_path)


class NG(object):
  def __init__(self, app_path, app_name=None):
    self._app_path, self._app_name = app_path, app_name

  def e2e(self, app_name=None):
    """
    Description:
    ------------
    Builds and serves an Angular app, then runs end-to-end tests using Protractor.

    Related Pages:

      https://angular.io/cli/e2e

    Attributes:
    ----------
    :param app_name:
    """
    app_name = app_name or self._app_name
    if app_name is None:
      raise Exception("An Angular aplication name is required!")

    subprocess.run('ng e2e %s' % app_name, shell=True, cwd=os.path.join(self._app_path, self._app_name))

  def lint(self, app_name=None):
    """
    Description:
    ------------
    Builds and serves an Angular app, then runs end-to-end tests using Protractor.

    Related Pages:

			https://angular.io/cli/lint

		Attributes:
    ----------
    :param app_name:
    """
    app_name = app_name or self._app_name
    if app_name is None:
      raise Exception("An Angular aplication name is required!")

    subprocess.run('ng lint %s' % app_name, shell=True, cwd=os.path.join(self._app_path, self._app_name))

  def new(self, name, path=None):
    """
    Description:
    ------------
    Builds and serves an Angular app, then runs end-to-end tests using Protractor.

    Related Pages:

			https://angular.io/cli/new

		Attributes:
    ----------
    :param name:
    :param path:
    """
    if path is not None:
      subprocess.run('ng new %s --directory %s' % (name, path), shell=True, cwd=self._app_path)
    else:
      subprocess.run('ng new %s' % name, shell=True, cwd=self._app_path)
    print('ng new %s' % name)

  def doc(self, keyword):
    """
    Description:
    ------------
    Opens the official Angular documentation (angular.io) in a browser, and searches for a given keyword.

    Related Pages:

			https://angular.io/cli

		Attributes:
    ----------
    :param keyword:
    """
    subprocess.run('ng doc %s' % keyword, shell=True, cwd=self._app_path)

  def add(self, package):
    """
    Description:
    ------------

    Related Pages:

			https://angular.io/cli

		Attributes:
    ----------
    :param package:
    """
    subprocess.run('ng add %s' % package, shell=True, cwd=os.path.join(self._app_path, self._app_name))
    print("%s packages installed" % package)

  def analytics(self):
    """
    https://angular.io/cli
    """
    pass

  def help(self, options=None):
    """
    Description:
    ------------
    Lists available commands and their short descriptions.

    Related Pages:

			https://angular.io/cli

		Attributes:
    ----------
    :param app_name:
    """
    if options is None:
      subprocess.run('ng help', shell=True, cwd=self._app_path)
    else:
      subprocess.run('ng help %s' % options, shell=True, cwd=os.path.join(self._app_path, self._app_name))

  def test(self, app_name=None):
    """
    Description:
    ------------

    Related Pages:

			https://angular.io/cli

    Attributes:
    ----------
    :param app_name:
    """
    app_name = app_name or self._app_name
    if app_name is None:
      raise Exception("An Angular aplication name is required!")

    subprocess.run('ng test %s' % app_name, shell=True, cwd=os.path.join(self._app_path, app_name))

  def build(self, app_name=None):
    """
    Description:
    ------------
    Compiles an Angular app into an output directory named dist/ at the given output path. Must be executed from within a workspace directory.

    Related Pages:

			https://angular.io/cli

    Attributes:
    ----------
    :param app_name:
    """
    app_name = app_name or self._app_name
    if app_name is None:
      raise Exception("An Angular aplication name is required!")

    subprocess.run('ng build %s' % app_name, shell=True, cwd=os.path.join(self._app_path, app_name))

  def version(self):
    """
    Description:
    ------------
    Builds and serves an Angular app, then runs end-to-end tests using Protractor.
    """
    subprocess.run('ng version', shell=True, cwd=os.path.join(self._app_path, self._app_name))

  def serve(self):
    """
    Description:
    ------------
    Builds and serves an Angular app, then runs end-to-end tests using Protractor.

    Related Pages:

			https://angular.io/cli/serve
    """
    subprocess.run('ng serve --open', shell=True, cwd=os.path.join(self._app_path, self._app_name))

  @property
  def create(self):
    """
    Description:
    ------------
    Shortcut to the various generate entry points in the Angular Framework
    """
    return NGModule(os.path.join(self._app_path, self._app_name))

  def generate(self, schematic, name):
    """
    Description:
    ------------
    Generates and/or modifies files based on a schematic.

    Related Pages:

			https://angular.io/cli/generate

    Attributes:
    ----------
    :param schematic:
    :param name:
    """
    subprocess.run('ng generate %s %s' % (schematic, name), shell=True, cwd=os.path.join(self._app_path, self._app_name))


class RouteModule(object):

  def __init__(self, app_path, app_name, file_name=None):
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

  def add(self, component, alias, path):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param component:
    :param alias:
    :param path:
    """
    if self.ng_modules is None:
      self.ng_modules = NgModules(self._app_path, self._app_name)
      self.ng_modules.modules[component] = path
    self.modules[component] = path
    self.routes[component] = alias

  def export(self, file_name=None, target_path=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param file_name: String. Optional. The filename
    """
    file_name = 'app-routing.module_new.ts' or self.file_name
    if target_path is None:
      target_path = []
    target_path.append(file_name)
    with open(os.path.join(self._app_path, self._app_name, *target_path), "w") as f:
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


class NgModules(object):

  def __init__(self, app_path, app_name, file_name=None):
    self._app_path, self._app_name = app_path, app_name
    self.file_name = file_name or 'app.module.ts'
    self.modules, self.imports, self.declarations, self.providers, self.bootstrap = {}, [], [], [], []

    # parse the Angular route module
    imported_module_pattern = re.compile("import { (.*) } from '(.*)';")
    with open(os.path.join(self._app_path, app_name, 'src', 'app', self.file_name)) as f:
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

  def add(self, component, path):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param component: String. The component name
    :param path: String. The component path
    """
    self.modules[component] = path

  def add_import(self, component, path):
    self.modules[component] = path

    if component not in self.imports:
      self.imports.append(component)

  def export(self, file_name=None, target_path=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param file_name: String. Optional. The filename
    """
    file_name = 'app.module_new.ts' or self.file_name
    if target_path is None:
      target_path = []
    target_path.append(file_name)
    with open(os.path.join(self._app_path, self._app_name, *target_path), "w") as f:
      for k, v in self.modules.items():
        f.write("import { %s } from '%s';\n" % (k, v))
      f.write("\n\n")
      f.write("@NgModule({\n")
      for name, vars in [("declarations", self.declarations), ('imports', self.imports), ('providers', self.providers), ('bootstrap', self.bootstrap)]:
        f.write("  %s: [\n" % name)
        for d in vars:
          f.write("    %s,\n" % d)
        f.write("  ],\n")
      f.write("})\n\n")
      f.write("export class AppModule { }")


class ComponentSpec(object):

  def __init__(self, app_path, app_name, alias, name):
    self.imports, self.vars = {}, {}
    self._app_path, self._app_name, self.__path = app_path, app_name, 'apps'
    self.alias, self.name = alias, name
    self.__comp_structure = {}

  def export(self, path=None, target_path=None):
    """
    Description:
    ------------
    Export the spec of the component

    TODO: make this generation more flexible

    Attributes:
    ----------
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

    with open(os.path.join(module_path, "app.%s.component.spec.ts" % self.alias), "w") as f:
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


class Components(object):

  def __init__(self, app, count=0, report=None):
    self._app, self.count_comp, self._report = app, count, report

  def chart(self, vars, alias=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param vars:
    :param alias:
    """
    map_var_names = {}
    alias = alias or self.count_comp
    for k, v in vars.items():
      map_var_names[k] = "%s%s" % (k, alias)
      self._app.add_var(map_var_names[k], v)
    map_var_names["ref"] = "chart%s" % alias
    self._app.comps["chart%s" % alias] = "chart%s" % alias
    self.count_comp += 1
    self._app.htmls.append('''
<div class="container">
		<pr-chart [values]='%(values)s' [labels]='%(labels)s' type='{{ %(type)s }}' #%(ref)s></pr-chart>
</div>''' % map_var_names)
    return "chart%s" % alias

  def table(self, vars, alias=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param vars:
    :param alias:
    """
    map_var_names = {}
    alias = alias or self.count_comp
    for k, v in vars.items():
      map_var_names[k] = "%s%s" % (k, alias)
      self._app.add_var(map_var_names[k], v)
    map_var_names["ref"] = "table%s" % alias
    self._app.comps["table%s" % alias] = "table%s" % alias
    self.count_comp += 1
    self._app.htmls.append('''<pr-grid #%(ref)s></pr-grid>''' % map_var_names)
    return "table%s" % alias

  def input(self):
    self._app.comps["input"] = "input"
    self._app.htmls.append('''<input type='text' #input />''')

  def button(self, value):
    return self._report.ui.button(value)


class App(object):

  def __init__(self, app_path, app_name, alias, name, report=None):
    self.imports = {'Component': '@angular/core',
                    #'HttpClient': '@angular/common/http',
                    #'HttpHeaders': '@angular/common/http', 'Injectable': '@angular/core',
                    #'ViewChild': '@angular/core'
                    }
    self.vars, self.__map_var_names, self._report = {}, {}, report
    self._app_path, self._app_name = app_path, app_name
    self.alias, self.__path, self.className, self.__components = alias, 'apps', name, None
    self.__comp_structure, self.htmls, self.__fncs, self.__injectable_prop = {}, [], {}, {'providedIn': 'root'}
    self.spec = ComponentSpec(app_path, app_name,  alias, name)
    self.comps = {}

  def add_var(self, name, value=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param value:
    """
    if value is not None:
      if 'constructor' not in self.__comp_structure:
        self.__comp_structure['constructor'] = []
      self.__comp_structure['constructor'].append("this.%s = %s" % (name, json.dumps(value)))
    self.vars[name] = value

  def add_fnc(self, name, fncs):
    self.__fncs[name] = fncs

  def add_imports(self, name, path):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param path:
    """
    pass

  @property
  def components(self):
    """
    Description:
    ------------

    """
    if self.__components is None:
      self.__components = Components(self, report=self._report)
    return self.__components

  def constructor(self):
    pass

  def ngOnInit(self):
    pass

  def ngAfterViewInit(self):
    return

  @property
  def name(self):
    """
    Description:
    ------------
    Return the prefix of the component module (without any extension)
    """
    return "app.%s.component" % self.alias

  def http(self, end_point, jsFncs):
    return "this.httpClient.post('http://127.0.0.1:5000/%s', {}).subscribe((data)=>{ %s });" % (end_point, ";".join(jsFncs))

  @property
  def path(self):
    """
    Description:
    ------------
    Return the full path of the component modules
    """
    return os.path.join("./", self.__path, self.name).replace("\\", "/")

  def export(self, path=None, target_path=None):
    """
    Description:
    ------------

    Attributes:
    ----------
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

    page = self._report.outs.web()

    self.spec.export(path=path, target_path=None)
    self.__fncs['ngAfterViewInit'] = [page['jsFrgs']]

    with open(os.path.join(module_path, "%s.ts" % self.name), "w") as f:
      for comp, path in self.imports.items():
        f.write("import { %s } from '%s';\n" % (comp, path))
      f.write("import { %s } from './%s.js';" % (", ".join(list(page['jsFrgsCommon'].keys())),  self.alias.replace("-", "_")))
      f.write("\n")
      # All the applicatops need this as they will interact with a Flask backend
      #f.write("@Injectable({\n")
      #for k , v in self.__injectable_prop.items():
      #  f.write(" %s: %s\n" % (k, json.dumps(v)))
      #f.write("})\n")
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

    with open(os.path.join(module_path, "%s.js" % self.alias.replace("-", "_")), "w") as f:
      for js_dep in JS_MODULES_IMPORTS:
        if js_dep in self._report.jsImports:
          f.write("%s\n" % JS_MODULES_IMPORTS[js_dep])
      for buider in page['jsFrgsCommon'].values():
        f.write("export %s;\n" % buider)

    with open(os.path.join(module_path, "%s.html" % self.name), "w") as f:
      f.write("%(cssImports)s\n\n%(body)s" % page)

    with open(os.path.join(module_path, "%s.css" %  self.name), "w") as f:
      f.write(page['cssStyle'])


class Angular(node.Node):

  def create(self, node_path):
    """
    Description:
    ------------

    """

  def ng(self, app_name=None):
    """
    Description:
    ------------
    Angular specific command lines

    Related Pages:

			https://angular.io/cli/

    Attributes:
    ----------
    :param app_name: String. The angular application name
    """
    app_name = app_name or self._app_name
    return NG(self._app_path, app_name)

  def page(self, selector=None, name=None, report=None, auto_route=False):
    """
    Description:
    ------------
    Create a specific Application as a component in the Angular framework.

    Unlike a basic component, the application will be routed to be accessed directly.

    Description:
    ------------
    :param report: Object. A report object
    :param selector: String. The url route for this report in the Angular app
    :param name: String. The component classname in the Angular framework
    """
    if name is None:
      script = os.path.split(sys._getframe().f_back.f_code.co_filename)[1][:-3]
      name = "".join([s.capitalize() for s in script.split("_")])
      if selector is None:
        selector = script.replace("_", "-")
    report = report or Page.Report()
    report.framework("ANGULAR")
    self.__page = App(self._app_path, self._app_name, selector, name, report=report)
    if auto_route:
      self.route.add(self.__page.className, self.__page.alias, self.__page.path)
    return self.__page

  def ng_modules(self, app_name=None, file_name=None):
    """
    Description:
    ------------
    Read the file app.module.ts

    :param app_name: String. Optinal. THe Angular application name

    :rtype: NgModules
    """
    if self.__ng_modules is None:
      if self.__route is not None and self.__route.ng_modules is not None:
        self.__ng_modules = self.__route.ng_modules
      else:
        self.__ng_modules = NgModules(self._app_path, app_name or self._app_name, file_name)
    return self.__ng_modules

  @property
  def route(self, app_name=None, file_name=None):
    """
    Description:
    ------------

    Read the file app-routing.module.ts from the Angular app

    Attributes:
    ----------
    :param app_name: String. Optinal. THe Angular application name
    :param file_name: String. Optinal.

    :rtype: RouteModule
    """
    if self.__route is None:
      self.__route = RouteModule(self._app_path, app_name or self._app_name, file_name)
    return self.__route

  def publish(self, app_name=None, target_path=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param app_name:
    :param target_path: List  for example ['src', 'app']
    """
    if self.__page is not None:
      self.__page.export(target_path=target_path)
    if self.__route is not None:
      self.route.export()

