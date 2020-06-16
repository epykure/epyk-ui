
import os

import subprocess

from epyk.core import Page
from epyk.web import node


JS_MODULES_IMPORTS = {
  'showdown': '''
import Showdown from 'showdown';
var showdown = Showdown;
'''
}


class NpxCli(object):
  def __init__(self, vue_app_path):
    self._vue_app_path = vue_app_path

  def create(self, name=None):
    """
    Description:
    ------------
    The create-react-app is an officially supported way to create React applications.

    Related Pages:

      https://fr.reactjs.org/docs/create-a-new-react-app.html
    https://www.w3schools.com/react/default.asp

    Attributes:
    ----------
    :param name:
    """
    if name is None:
      subprocess.run('npx create-react-app --help', shell=True, cwd=self._vue_app_path)
    else:
      subprocess.run('npx create-react-app %s' % name, shell=True, cwd=self._vue_app_path)

  def build(self):
    """
    Description:
    ------------
    Builds the app for production to the build folder.
    It correctly bundles React in production mode and optimizes the build for the best performance.

    Related Pages:

      https://create-react-app.dev/docs/getting-started/
    """
    subprocess.run('npm run build', shell=True, cwd=self._vue_app_path)

  def start(self):
    """
    Description:
    ------------
    Runs the app in development mode. Open http://localhost:3000 to view it in the browser.

    Related Pages:

      https://create-react-app.dev/docs/getting-started/
    """
    subprocess.run('npm test', shell=True, cwd=self._vue_app_path)

  def test(self):
    """
    Description:
    ------------
    Runs the test watcher in an interactive mode. By default, runs tests related to files changed since the last commit.

    Related Pages:

      https://create-react-app.dev/docs/getting-started/
    """
    subprocess.run('npm test', shell=True, cwd=self._vue_app_path)


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
    page['name'] = self.name
    page['js_module'] = self.alias.replace("-", "_")
    page['builders'] = ", ".join(list(page['jsFrgsCommon'].keys()))
    with open(os.path.join(module_path, "%s.css" % self.name), "w") as f:
      f.write(page['cssStyle'])
    # export default %(alias)s
    with open(os.path.join(module_path, "%s.js" % self.name), "w") as f:
      f.write('''
import React from 'react';
import ReactDOM from 'react-dom';
import { %(builders)s } from './%(js_module)s.js'
import './%(name)s.css';

class %(alias)s extends React.Component {
  render() {
    return %(body)s;
  }
}

export default AppRoot;
ReactDOM.render(<%(alias)s />, document.getElementById('root'); %(jsFrgs)s);
''' % page)

    with open(os.path.join(module_path, "%s.js" % page['js_module']), "w") as f:
      for js_dep in JS_MODULES_IMPORTS:
        if js_dep in self._report.jsImports:
          f.write("%s\n" % JS_MODULES_IMPORTS[js_dep])
      for buider in page['jsFrgsCommon'].values():
        f.write("export %s;\n" % buider)


class React(node.Node):

  def cli(self, app_name=None):
    """
    Description:
    ------------
    Create React App is an officially supported way to create single-page React applications.
    It offers a modern build setup with no configuration.

    Related Pages:

      https://create-react-app.dev/docs/getting-started

    Attributes:
    ----------
    :param app_name: String. The React.js application name
    """
    return NpxCli(self._app_path)

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
    Publishh the Vue.js application

    Attributes:
    ----------
    :param app_name:
    :param target_path: List  for example ['src', 'app']
    """
    if self._page is not None:
      self._page.export(target_path=target_path)
    #if self.__route is not None:
    #  self.route.export()