
import os
import sys

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
  def __init__(self, app_path, app_name, env):
    self._react_app_path, self.envs = os.path.join(app_path, app_name), env

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
      subprocess.run('npx create-react-app --help', shell=True, cwd=self._react_app_path)
    else:
      subprocess.run('npx create-react-app %s' % name, shell=True, cwd=self._react_app_path)

  def build(self):
    """
    Description:
    ------------
    Builds the app for production to the build folder.
    It correctly bundles React in production mode and optimizes the build for the best performance.

    Related Pages:

      https://create-react-app.dev/docs/getting-started/
    """
    subprocess.run('npm run build', shell=True, cwd=self._react_app_path)

  def start(self):
    """
    Description:
    ------------
    Runs the app in development mode. Open http://localhost:3000 to view it in the browser.

    Related Pages:

      https://create-react-app.dev/docs/getting-started/
    """
    subprocess.run('npm test', shell=True, cwd=self._react_app_path)

  def test(self):
    """
    Description:
    ------------
    Runs the test watcher in an interactive mode. By default, runs tests related to files changed since the last commit.

    Related Pages:

      https://create-react-app.dev/docs/getting-started/
    """
    subprocess.run('npm test', shell=True, cwd=self._react_app_path)

  def npm(self, packages):
    """
    Description:
    ------------
    This will add the npm requirements to the Angular app but also update directly the angular.json for anything needed
    at the start of the application.

    Attributes:
    ----------
    :param packages: List. The packages names to install
    """
    if self.envs is not None:
      for env in self.envs:
        subprocess.run(env, shell=True, cwd=self._react_app_path)
    packages = node.npm_packages(packages)
    subprocess.run('npm install %s' % " ".join(packages), shell=True, cwd=self._react_app_path)


class App(object):

  def __init__(self, app_path, app_name, alias, name, report=None, target_folder="views"):
    self.imports = {}
    self.vars, self.__map_var_names, self._report = {}, {}, report
    self._app_path, self._app_name = app_path, app_name
    self.alias, self.__path, self.className, self.__components = alias, target_folder, name, None
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

  def route(self, component, alias, path):
    """
    Description:
    ------------
    Add the app to the routing mechanism.
    By default all the views are in a view folder within the Raact App.

    Attributes:
    ----------
    :param component: String. The module name
    :param alias: String. The url route
    :param path: String. The .js module path
    """
    index_router = os.path.join(self._app_path, 'src', "index.js")
    if not os.path.exists(index_router):
      raise Exception("Problem with the React app")

    with open(index_router) as f:
      route = f.read()  # .split("\n\n")

    if not component in route:
      routes = route.split("import { Route, Link, BrowserRouter as Router } from 'react-router-dom';")
      routes[0] = "%s\nimport %s from '%s';\n" % (routes[0].strip(), component, path.replace("./src", "."))
      dis_route = routes[1].split("\n")
      for i, line in enumerate(dis_route):
        if line.strip().startswith("<Route "):
          break

      else:
        raise Exception("Issue with file, please udpate the index.js manually")

      route_end = dis_route[:i] + ['      <Route path="/%s" component={%s} />' % (alias, component)] + dis_route[i:]

      with open(index_router, "w") as f:
        f.write("\n".join([routes[0]] + ["import { Route, Link, BrowserRouter as Router } from 'react-router-dom';"] + route_end))

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
    module_path = os.path.join(self._app_path, *target_path)
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
import { %(builders)s } from './%(js_module)s_modules.js'
import './%(name)s.css';

class %(alias)s extends React.Component {
  render() {
    return %(body)s;
  }
}

export default AppRoot;
ReactDOM.render(<%(alias)s />, document.getElementById('root'); %(jsFrgs)s);
''' % page)

    with open(os.path.join(module_path, "%s_modules.js" % page['js_module']), "w") as f:
      for js_dep in JS_MODULES_IMPORTS:
        if js_dep in self._report.jsImports:
          f.write("%s\n" % JS_MODULES_IMPORTS[js_dep])
      for buider in page['jsFrgsCommon'].values():
        f.write("export %s;\n" % buider)


class React(node.Node):

  def create(self, name):
    """
    Description:
    ------------
    To create a new project, run:

    Related Pages:

      https://create-react-app.dev/docs/getting-started/

    Attributes:
    ----------
    :param name: String. The application name
    """
    if name is None:
      subprocess.run('npx create-react-app --help', shell=True, cwd=self._app_path)
    else:
      subprocess.run('npx create-react-app %s' % name, shell=True, cwd=self._app_path)

  def serve(self, app_name, port=8081):
    """
    Description:
    ------------
    Return the version of React.js on the server

    Related Pages:

      https://create-react-app.dev/docs/getting-started/

    Attributes:
    ----------
    :param app_name:
    :param port:
    """
    path = os.path.join(self._app_path, app_name)
    subprocess.run('npm start --port %s' % port, shell=True, cwd=path)

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
    app_name = app_name or self._app_name
    return NpxCli(self._app_path, app_name, self.envs)

  def router(self, app_name):
    """
    Description:
    ------------
    React Router is the de-facto React routing library, and it’s one of the most popular projects built on top of React.
    This function will also update the module index.js in order to add the router automatically is missing

    Related Pages:

      https://flaviocopes.com/react-router/

    Attributes:
    ----------
    :param app_name:
    """
    path = os.path.join(self._app_path, app_name, 'src', 'index.js')
    #subprocess.run('npm install react-router-dom', shell=True, cwd=path)
    with open(path) as f:
      content = f.read()
    if 'react-router-dom' not in content:
      pass
      new_files, with_router = [], False
      for line in content.split("\n"):
        if line.strip() and not line.startswith("import") and not with_router:
          with_router = True
          new_files.append("import { Route, Link, BrowserRouter as Router } from 'react-router-dom';")
          new_files.append('''
const routing = (
  <Router>
    <div>
      <Route exact path="/" component={App} />
    </div>
  </Router>
)
''')
        new_files.append(line)
      new_files.append('''
ReactDOM.render(
  routing,
  document.getElementById('root')
);
''')
      with open(path, "w") as f:
        f.write("\n".join(new_files))

  def page(self, selector=None, name=None, report=None, auto_route=False, target_folder="apps"):
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
    self._page = App(self._app_path, self._app_name, selector, name, report=report, target_folder=target_folder)
    self.__route = auto_route
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
    #if self._page is not None:
    #  self._page.export(target_path=target_path)
    if self.__route:
      self._page.route(self._page.name, self._page.alias, self._page.path)

  def home_page(self, report, app_name=None, with_router=False):
    """
    Description:
    ------------
    Change the Angular App home page

    Attributes:
    ----------
    :param report:
    :param app_name:
    :param with_router:
    """
