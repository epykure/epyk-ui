
import os
import sys
import logging

import collections
import subprocess

from epyk.core import Page
from epyk.core.js import Imports


def requirements(report, app_path=None):
  """
  Description:
  ------------
  Get the list of all the packages required in the Node Application

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
        npm_name = Imports.JS_IMPORTS[req]['register']['npm']
        npms.append(npm_name)
        if app_path is not None:
          npm_package_path = os.path.join(app_path, npm_name)
          if not os.path.exists(npm_package_path):
            print("Missing package: %s" % npm_name)
      else:
        print("No npm requirement defined for %s" % req)
    else:
      print("No npm requirement defined for %s" % req)
  return npms


class App(object):

  def __init__(self, app_path, app_name, alias, name, report=None, target_folder="views"):
    self.imports = collections.OrderedDict({"http": 'http', 'url': 'url', 'fs': 'fs'})
    self.import_launchers = []
    self.vars, self.__map_var_names, self._report = {}, {}, report
    self._app_path, self._app_name = app_path, app_name
    self.alias, self.__path, self.className, self.__components = alias, target_folder, name, None
    self.comps = {}

  def require(self, module, alias=None, launcher=""):
    """
    Description:
    ------------
    Add external modules to the application

    Related Pages:

      https://www.w3schools.com/nodejs/nodejs_modules.asp

    Attributes:
    ----------
    :param module: String. The module name.
    :param alias: String. Optional. The alias name for the JavaScript Variable name
    :param launcher: String. Optional. The JavasCript String to be added to the page just after the imports
    """
    self.imports[module] = alias or module
    if launcher:
      self.import_launchers.append(launcher)

  @property
  def name(self):
    """
    Description:
    ------------
    Return the prefix of the component module (without any extension)
    """
    return self.className

  @property
  def path(self):
    """
    Description:
    ------------
    Return the full path of the component modules
    """
    return os.path.join("./", self.__path, self.name).replace("\\", "/")

  def checkImports(self, app_path=None):
    """
    Description:
    ------------
    Check if the npm modules are defined on the server for the defined application.

    Attributes:
    ----------
    :param app_path: String. Optional. the Path of the NodeJs application
    """
    app_path = app_path or self._app_path
    node_modules = os.path.join(app_path, "node_modules")
    self.imports = {"showdown": "showdown"}
    for imp, alias in self.imports.items():
      if imp in Imports.JS_IMPORTS:
        if 'register' in Imports.JS_IMPORTS[imp]:
          if not os.path.exists(os.path.join(node_modules, Imports.JS_IMPORTS[imp]['register'].get('npm', imp))):
            logging.warning("Missing module - %s - on the nodeJsServer" % imp)

  def export(self, path=None, target_path=None):
    """
    Description:
    ------------
    Export the NodeJs application

    Attributes:
    ----------
    :param path: String. The NodeJs server path
    :param target_path: String. The folder location on the server. for example ['src', 'app']
    """
    self.__path = path or self.__path
    if target_path is None:
      target_path = []
    target_path.append(self.__path)
    module_path = os.path.join(self._app_path, *target_path)
    if not os.path.exists(module_path):
      os.makedirs(module_path)
    self._report.outs.html_file(path=module_path, name=self.name)
    requirements = []
    for imp, alias in self.imports.items():
      if imp in Imports.JS_IMPORTS:
        if 'register' in Imports.JS_IMPORTS[imp]:
          imp = Imports.JS_IMPORTS[imp]['register'].get('npm', imp)
          alias = Imports.JS_IMPORTS[imp]['register'].get('alias', alias)
      requirements.append("var %s = require('%s')" % (alias, imp))
    js_reqs = ";\n".join(requirements)

    # Write the JavaScript launcher
    with open(os.path.join(module_path, "%s.js" % self.name), "w") as f:
      f.write('''
%s;

fs.readFile('./%s.html', function (err, html) {
    if (err) {throw err;}       
    http.createServer(function(request, response) {  
        response.writeHeader(200, {"Content-Type": "text/html"});  
        response.write(html);  
        response.end();  
    }).listen(8000);
}); ''' % (js_reqs, self.name))


class Cli(object):

  def __init__(self, app_path):
    self._app_path = app_path

  def angular(self):
    """
    https://cli.angular.io/

    """
    subprocess.run('npm install -g @angular/cli', shell=True, cwd=self._app_path)

  def vue(self):
    """
    https://cli.vuejs.org/
    """
    subprocess.run('npm install -g @vue/cli', shell=True, cwd=self._app_path)

  def react(self):
    return


class Node(object):

  def __init__(self, app_path, name=None):
    self._app_path, self._app_name = app_path, name
    self._route, self._fmw_modules = None, None
    self._page = None

  @property
  def clis(self):
    if self._app_name is not None:
      path = os.path.join(self._app_path, self._app_name)
    else:
      path = self._app_path
    return Cli(path)

  def npm(self, packages):
    """
    Description:
    ------------
    Use npm install on a package.
    Can be done directly on the nodeJs app using the command line:
      npm install package1 package2 .....

    Attributes:
    ----------
    :param packages: List. The list of packages to install retrieved from requirements()
    """
    subprocess.run('npm install %s --save' % " ".join(packages), shell=True, cwd=self._app_path)
    print("%s packages installed" % len(packages))

  def ls(self):
    """
    Description:
    ------------
    Search the registry for packages matching terms
    """
    subprocess.run('npm ls', shell=True, cwd=self._app_path)

  def launcher(self, app_name, target_path, port=3000):
    """
    Description:
    ------------
    Create a single launcher for the application.

    Attributes:
    ----------
    :param app_name: String. The deno path (This should contain the deno.exe file)
    :param target_path: String. The target path for the views
    """
    out_path = os.path.join(self._app_path, "launchers")
    if not os.path.exists(out_path):
      os.makedirs(out_path)
    router_path = os.path.join(out_path, "launcher_%s.js" % app_name)
    with open(os.path.join(self._app_path, "run_%s.bat" % app_name), "w") as f:
      f.write("node.exe ./launchers/launcher_%s.js" % app_name)
    with open(router_path, "w") as f:
      f.write('''
var http = require('http');
var url = require('url');
var fs = require('fs');

fs.readFile('./%s/%s.html', function (err, html) {
    if (err) {throw err;}       
    http.createServer(function(request, response) {  
        response.writeHeader(200, {"Content-Type": "text/html"});  
        response.write(html);  
        response.end();  
    }).listen(%s);
}); ''' % (target_path, app_name, port))

  def launch(self, app_name, target_folder=None, port=3000):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param app_name: String
    :param target_folder: String.
    :param port: Integer.
    """
    out_path = os.path.join(self._app_path, "launchers")
    router_path = os.path.join(out_path, "launcher_%s.js" % app_name)
    target_folder = target_folder or self.target_folder
    if not os.path.exists(router_path) and target_folder is not None:
      self.launcher(app_name, target_folder, port)
    self.run(name="./launchers/launcher_%s.js" % app_name)

  def router(self, target_folder, port=3000):
    """
    Description:
    ------------
    Create a simple router file for your different views on your server.

    Attributes:
    ----------
    :param target_folder: String. The target path where the views are stored
    :param port: Integer.
    """
    router_path = os.path.join(self._app_path, "server.js")
    with open(router_path, "w") as f:
      f.write('''
var http = require('http');
var fs = require('fs');
var parser = require('url');

http.createServer(function(request, response) {
    url = parser.parse(request.url, true);  
    fs.readFile('./%s'+ url.path +'.html', function (err, html) {
      if (err) {throw err;} 
      response.writeHeader(200, {"Content-Type": "text/html"});  
      response.write(html);  
      response.end();  
    });
}).listen(%s);
 ''' % (target_folder, port))

  def run(self, name, port=3000):
    """
    Description:
    ------------
    The file you have just created must be initiated by Node.js before any action can take place.

    Related Pages:

      https://www.w3schools.com/nodejs/nodejs_get_started.asp

    Attributes:
    ----------
    :param name: String. The script name
    :param port: Integer. The port number for the node server
    """
    print("Node server url: 127.0.0.1:%s" % port)
    subprocess.run('node %s --port %s' % (name, port), shell=True, cwd=self._app_path)

  def inspect(self, name, from_launcher=False):
    """

    :param name:
    :param from_launcher:
    """
    if from_launcher:
      subprocess.run('node --inspect ./launchers/launcher_%s.js' % name, shell=True, cwd=self._app_path)
    else:
      subprocess.run('node --inspect %s ' % name, shell=True, cwd=self._app_path)

  def docs(self, package):
    """
    Description:
    ------------
    Display the README.md / documentation / npmjs.org page of a give library

    Attributes:
    ----------
    :param package: String. The package alias
    """
    subprocess.run('npm docs %s' % package, shell=True, cwd=self._app_path)

  def update(self, packages):
    """
    Description:
    ------------
    Update all the packages listed to the latest version (specified by the tag config). Also install missing packages

    Attributes:
    ----------
    :param packages: List. The list of packages to be installed
    """
    subprocess.run('npm update %s' % " ".join(packages), shell=True, cwd=self._app_path)
    print("%s packages updated" % len(packages))

  def uninstall(self, packages):
    """
    Description:
    ------------
    Uninstall a package, completely removing everything npm installed on its behalf

    Attributes:
    ----------
    :param packages: List. The list of packages to be installed
    """
    subprocess.run('npm uninstall %s' % " ".join(packages), shell=True, cwd=self._app_path)
    print("%s packages uninstalled" % len(packages))

  def install(self):
    """
    Description:
    ------------
    Install or update Vue.Js on the defined path
    """
    subprocess.run('npm install -g @vue/cli', shell=True, cwd=self._app_path)
    print("Angular CLI installed")

  def page(self, selector=None, name=None, report=None, auto_route=False, target_folder="views"):
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
      if selector is None:
        selector = script.replace("_", "-")
    report = report or Page.Report()
    report.framework("NODE")
    self._page = App(self._app_path, self._app_name, selector, name, report=report)
    self.auto_route = auto_route
    self.target_folder = target_folder
    return self._page

  def publish(self, target_folder=None):
    """
    Description:
    ------------
    Publish the Node.js application

    Attributes:
    ----------
    :param target_folder: String. The target path for the transpiled views
    """
    out_path = os.path.join(self._app_path, target_folder or self.target_folder)
    if self._page is not None:
      self._page.export(target_path=target_folder)
    if self.auto_route:
      self.launcher(self.name, out_path)
