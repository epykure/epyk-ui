
import subprocess
import sys
import os

from epyk.core import Page
from epyk.web import node


JS_MODULES_IMPORTS = {
  'showdown': '''
import Showdown from 'showdown';
var showdown = Showdown;
'''
}


class VueCli(object):
  def __init__(self, vue_app_path):
    self._vue_app_path = vue_app_path

  def version(self):
    """
    Description:
    ------------
    Return the version of Vue.js on the server

    Related Pages:

      https://cli.vuejs.org/guide/installation.html

    """
    subprocess.run('vue --version', shell=True, cwd=self._vue_app_path)

  def create(self, name=None):
    """
    Description:
    ------------
    To create a new project, run:

    Related Pages:

      https://cli.vuejs.org/guide/creating-a-project.html

    Attributes:
    ----------
    :param name: String. The application name
    """
    if name is None:
      subprocess.run('vue create --help', shell=True, cwd=self._vue_app_path)
    else:
      subprocess.run('vue create %s' % name, shell=True, cwd=self._vue_app_path)

  def ui(self):
    """
    Description:
    ------------
    You can also create and manage projects using a graphical interface with the vue ui command:

    Related Pages:

      https://cli.vuejs.org/guide/creating-a-project.html#vue-create
    """
    subprocess.run('vue ui', shell=True, cwd=self._vue_app_path)


class App(object):

  def __init__(self, app_path, app_name, alias, name, report=None):
    self.imports = {}
    self.vars, self.__map_var_names, self._report = {}, {}, report
    self._app_path, self._app_name = app_path, app_name
    self.alias, self.__path, self.className, self.__components = alias, 'apps', name, None
    self.comps = {}

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
    page['alias'] = self.alias
    page['js_module'] = self.alias.replace("-", "_")
    page['builders'] = ", ".join(list(page['jsFrgsCommon'].keys()))
    #  href="https://use.fontawesome.com/releases/v5.13.0/css/all.css"
    #  @import "https://use.fontawesome.com/releases/v5.13.0/css/all.css"
    page['cssImports'] = page['cssImports'].replace('<link rel="stylesheet" href=', "@import ").replace(' type="text/css">', "")
    with open(os.path.join(module_path, "%s.vue" % self.name), "w") as f:
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

    with open(os.path.join(module_path, "%s.js" % page['js_module']), "w") as f:
      for js_dep in JS_MODULES_IMPORTS:
        if js_dep in self._report.jsImports:
          f.write("%s\n" % JS_MODULES_IMPORTS[js_dep])
      for buider in page['jsFrgsCommon'].values():
        f.write("export %s;\n" % buider)


class VueJs(node.Node):

  def cli(self, app_name=None):
    """
    Description:
    ------------
    Vue specific command lines

    Related Pages:

      https://vuejs.org/v2/guide/installation.html

    Attributes:
    ----------
    :param app_name: String. The Vue.js application name
    """
    return VueCli(self._app_path)

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
    report.framework("VUE")
    self._page = App(self._app_path, self._app_name, selector, name, report=report)
    #if auto_route:
    #  self.route.add(self.__page.className, self.__page.alias, self.__page.path)
    return self._page

  def publish(self, app_name=None, target_path=None):
    """
    Description:
    ------------
    Publish the Vue.js application

    Attributes:
    ----------
    :param app_name:
    :param target_path: List  for example ['src', 'app']
    """
    if self._page is not None:
      self._page.export(target_path=target_path)
    #if self.__route is not None:
    #  self.route.export()
