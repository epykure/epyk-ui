
import subprocess
import sys
import os
import json

from epyk.core import Page
from epyk.web import node


JS_MODULES_IMPORTS = {
  'showdown': '''
import Showdown from 'showdown';
var showdown = Showdown;
''',
  'jquery': "import $ from 'jquery';",
  'jqueryui': '''
import 'jquery-ui-dist/jquery-ui.min.css';
import 'jquery-ui-dist/jquery-ui.min.js';
''',
}


class VueCli:
  def __init__(self, vue_app_path, env):
    self._vue_app_path, self.envs = vue_app_path, env

  def version(self):
    """
    Return the version of Vue.js on the server

    Related Pages:

      https://cli.vuejs.org/guide/installation.html
    """
    subprocess.run('vue --version', shell=True, cwd=self._vue_app_path)

  def linter(self):
    """
    Updat the linter options and remove the no-unused-vars.
    """
    with open(os.path.join(self._vue_app_path, "package.json"), 'r') as f:
      package = json.load(f)
    # Remove some rules to Vue.js configuration
    package['eslintConfig']['rules']['no-unused-vars'] = 'off'
    package['eslintConfig']['rules']['no-extra-semi'] = 1
    with open(os.path.join(self._vue_app_path, "package.json"), 'w') as f:
      json.dump(package, f, indent=4)

  def ui(self):
    """
    You can also create and manage projects using a graphical interface with the vue ui command:

    Related Pages:

      https://cli.vuejs.org/guide/creating-a-project.html#vue-create
    """
    subprocess.run('vue ui', shell=True, cwd=self._vue_app_path)

  def npm(self, packages):
    """

    :param packages:
    """
    if self.envs is not None:
      for env in self.envs:
        subprocess.run(env, shell=True, cwd=self._vue_app_path)
    packages = node.npm_packages(packages)
    subprocess.run('npm install %s' % " ".join(packages), shell=True, cwd=self._vue_app_path)

  def add_router(self):
    """

    Related Pages:

      https://router.vuejs.org/installation.html#npm
    """
    subprocess.run('vue add router', shell=True, cwd=self._vue_app_path)


class App:

  def __init__(self, app_path, app_name, alias, name, page=None, target_folder="components"):
    self.imports = {}
    self.vars, self.__map_var_names, self.page = {}, {}, page
    self._app_path, self._app_name = app_path, app_name
    self.alias, self.__path, self.className, self.__components = alias, target_folder, name, None
    self.comps, self.module_path = {}, None

  @property
  def name(self):
    """
    Return the prefix of the component module (without any extension)
    """
    return self.className

  @property
  def path(self):
    """
    Return the full path of the component modules
    """
    return os.path.join("./", self.__path, self.name).replace("\\", "/")

  def route(self, component, alias, path):
    """
    Add the app to the routing mechanism
 
    :param component: String. The module name
    :param alias: String. The url route
    :param path: String. The .vue module path
    """
    index_router = os.path.join(self._app_path, 'src', 'router', "index.js")
    if not os.path.exists(index_router):
      raise ValueError("Router is not installed, run: vue add router in the Vue app")

    with open(index_router) as f:
      route = f.read()  # .split("\n\n")

    split_route = route.split("Vue.use(VueRouter)")
    imports = split_route[0].strip()
    if not "import %s from" % component in imports:
      imports = "%s\nimport %s from '../views/%s.vue'" % (imports, component, component)
      split_maps = split_route[1].split("const routes = [")
      routes = split_maps[1].strip()
      routes = "\n { path: '/%s', name: '%s', component: %s },\n %s" % (alias, alias, component, routes)
      new_content = "%s\n\nVue.use(VueRouter)%s\n\nconst routes = [%s" % (imports, split_maps[0].strip(), routes)
      with open(index_router, "w") as f:
        f.write(new_content)

  def export(self, path=None, target_path=None):
    """
 
    :param path:
    :param target_path: for example ['src', 'app']
    """
    self.__path = path or self.__path
    if target_path is None:
      target_path = []
    target_path.append(self.__path)
    self.module_path = os.path.join(self._app_path, *target_path)
    if not os.path.exists(self.module_path):
      os.makedirs(self.module_path)
    page = self.page.outs.web()
    page['alias'] = self.alias
    page['js_module'] = self.alias.replace("-", "_")
    page['builders'] = ", ".join(list(page['jsFrgsCommon'].keys()))
    #  href="https://use.fontawesome.com/releases/v5.13.0/css/all.css"
    #  @import "https://use.fontawesome.com/releases/v5.13.0/css/all.css"
    page['cssImports'] = page['cssImports'].replace('<link rel="stylesheet" href=', "@import ").replace(' type="text/css">', "")
    with open(os.path.join(self.module_path, "%s.vue" % self.name), "w") as f:
      f.write('''
<template>
  %(body)s
</template>\n\n
<script>
import { %(builders)s } from './%(js_module)s.js'

export default {
  name: '%(alias)s',
  mounted: function() {%(jsFrgs)s}
}
</script>
\n
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
%(cssStyle)s
%(cssImports)s
</style>
''' % page)

    with open(os.path.join(self.module_path, "%s.js" % page['js_module']), "w") as f:
      for js_dep in JS_MODULES_IMPORTS:
        if js_dep in self.page.jsImports:
          f.write("%s\n" % JS_MODULES_IMPORTS[js_dep])
      for buider in page['jsFrgsCommon'].values():
        f.write("export %s;\n" % buider)


class VueJs(node.Node):

  def create(self, name):
    """
    To create a new project, run:

    Related Pages:

      https://cli.vuejs.org/guide/creating-a-project.html
 
    :param name: String. The application name
    """
    if name is None:
      subprocess.run('vue create --help', shell=True, cwd=self._app_path)
    else:
      subprocess.run('vue create %s' % name, shell=True, cwd=self._app_path)

  def cli(self, app_name):
    """
    Vue specific command lines

    Related Pages:

      https://vuejs.org/v2/guide/installation.html
    """
    path = os.path.join(self._app_path, app_name)
    return VueCli(path, self.envs)

  def serve(self, app_name, port=8081):
    """
    Return the version of Vue.js on the server

    Related Pages:

      https://cli.vuejs.org/guide/cli-service.html#using-the-binary

    """
    path = os.path.join(self._app_path, app_name)
    subprocess.run('npm run serve -- --port %s' % port, shell=True, cwd=path)

  def router(self, app_name):
    """

    Related Pages:

      https://router.vuejs.org/installation.html#direct-download-cdn
 
    :param app_name:
    """
    path = os.path.join(self._app_path, app_name)
    subprocess.run('npm install vue-router', shell=True, cwd=path)

  def help(self, app_name):
    """
    Return the version of Vue.js on the server

    Related Pages:

      https://cli.vuejs.org/guide/cli-service.html#using-the-binary

    """
    subprocess.run('npx %s help' % app_name, shell=True, cwd=self._app_path)

  def page(self, selector=None, name=None, report=None, auto_route=False, target_folder="apps"):
    """
    Create a specific Application as a component in the Angular framework.

    Unlike a basic component, the application will be routed to be accessed directly.

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
    self._page = App(self._app_path, self._app_name, selector, name, page=page, target_folder=target_folder)
    self.__route = auto_route
    return self._page

  def publish(self, app_name=None, target_path=None):
    """
    Publish the Vue.js application
 
    :param app_name:
    :param target_path: List  for example ['src', 'app']
    """
    if self._page is not None:
      self._page.export(target_path=target_path)
    node.requirements(self._page.page, self._page.module_path)
    if self.__route:
      self._page.route(self._page.name, self._page.alias, self._page.path)
