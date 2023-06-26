#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
import json
import zipfile
from pathlib import Path
from typing import List, Union, Any, Dict
import subprocess

from ..core.html import Standalone, html_template_loader
from ..core.css import css_files_loader
from ..core import Page
from . import node, npm, templates


JS_MODULES_IMPORTS = {
    'showdown': '''
import Showdown from 'showdown';
var showdown = Showdown;
'''
}


def to_component(
        component: Standalone.Component, name: str = "ek-react-{selector}-{version}", out_path: str = None,
        version: str = None, init_value: Any = "", init_options: dict = None) -> Dict[str, str]:
    """
    Convert a Standalone component to a valid React component.

    Usage::

        import epyk as ek
        result = ek.helpers.to_react_component(MyStandaloneComp, version="0.0.1")

    A react component will be written in a sub folder.

    :param component:
    :param name:
    :param out_path:
    :param version:
    :param init_value:
    :param init_options:
    """
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

    # Then add the component definition to the root
    html_def = html_template_loader(
        component.template_url, new_var_format="{ this.state.%s }", ref_expr="ref={ this.dom }")
    component_files["component"] = name.format(selector=component.selector, version=version) + ".component.js"
    # Special formatting for React
    html_def["template"] = html_def["template"].replace("class=", "className=").replace("for=", "htmlFor=").replace(
        '"{ this.state.cssStyle }"', "{ this.state.cssStyle }")
    with open(Path(Path(out_path).parent, component_files["component"]), "w") as sf:
        sf.write(templates.REACT_COMPONENT % {
            "asset_class": component.__name__,
            "asset_path": "./%s/%s" % (Path(out_path).name, name.format(selector=component.selector, version=version)),
            "js": 'this.dom = React.createRef(); this.state = {"label": "", "cssClass": "", "cssStyle": {}}',
            "init_value": json.dumps(init_value),
            "init_options": init_options,
            "html": html_def["template"],
        })

    if version is not None:
        out_zip_name = name.format(selector=component.selector, version=version) + ".zip"
        with zipfile.ZipFile(out_zip_name, 'w') as zip_object:
            zip_object.write(str(Path(component.selector, component_files["js"])), str(Path(component.selector, component_files["js"])))
            zip_object.write(str(Path(component.selector, component_files["css"])), str(Path(component.selector, component_files["css"])))
            zip_object.write(component_files["component"], component_files["component"])
            # delete files in the folder
            Path(out_path, component_files["js"]).unlink()
            Path(out_path, component_files["css"]).unlink()
            Path(Path(out_path).parent, component_files["component"]).unlink()
    return component_files


def add_to_app(
        components: List[Standalone.Component],
        app_path: str,
        folder: str = "assets",
        name: str = "{selector}",
        raise_exception: bool = False
) -> dict:
    """
    This will add the component directly tp the src folder in the linked application.
    All components generated will be put in a sub folder.

    To start the React application: npm serve

    :param components: List of components to add to a React application
    :param app_path: React application path (root)
    :param folder: Components' folder
    :param name: Component's files name format
    :param raise_exception: Flag to raise exception if error
    """
    result = {"dependencies": {}}
    for component in components:
        result[component.selector] = npm.check_component_requirements(component, app_path, raise_exception)
        result["dependencies"].update(result[component.selector])
        assets_path = Path(app_path, "src", folder)
        assets_path.mkdir(parents=True, exist_ok=True)
        to_component(component, name=name, out_path=str(assets_path))
    return result


def to_library(
        components_path: Union[Path, str],
        name: str,
        version: str,
        node_modules_path: Union[Path, str],
        raise_exception: bool = False,
        **kwargs
):
    """
    This will creation a package from the components file.
    To work, components need to be installed within a valid React application.

    Related Pages:

      https://levelup.gitconnected.com/publish-react-components-as-an-npm-package-7a671a2fb7f

    :param components_path: Path with all the components (in sub folders)
    :param name: The package name
    :param version: The package version
    :param node_modules_path: Optional. The application node_modules path
    :param raise_exception: Optional. Raise an exception if component not correctly structured
    :param kwargs: Any extra Optional. argument will be added as properties to the package.json file
    """
    component_cls = {}
    components_path = Path(components_path)
    for component_path in components_path.iterdir():
        if component_path.is_file() and "component" in component_path.stem:
            with open(component_path) as cf:
                results = re.findall("export default (\w+);", cf.read())
                for result in results:
                    component_cls[result] = "./%s/%s" % (components_path.stem, component_path.stem)

    # export default BsDateComponent;
    # Write the index.js file
    with open(Path(components_path, "index.js"), "w") as fp:
        comps = []
        for component, path in component_cls.items():
            fp.write("import %s from '%s';\n" % (component, path))
            comps.append(component)
        fp.write("\nexport { %s }\n" % ", ".join(comps))


class NpxCli:
    def __init__(self, app_path, app_name, env):
        self._react_app_path, self.envs = os.path.join(app_path, app_name), env

    def create(self, name: str = None):
        """
        The create-react-app is an officially supported way to create React applications.

        Related Pages:

          https://fr.reactjs.org/docs/create-a-new-react-app.html
          https://www.w3schools.com/react/default.asp

        :param name: The application name to create
        """
        if name is None:
            subprocess.run('npx create-react-app --help', shell=True, cwd=self._react_app_path)
        else:
            subprocess.run('npx create-react-app %s' % name, shell=True, cwd=self._react_app_path)

    def build(self):
        """
        Builds the app for production to the build folder.
        It correctly bundles React in production mode and optimizes the build for the best performance.

        Related Pages:

          https://create-react-app.dev/docs/getting-started/
        """
        subprocess.run('npm run build', shell=True, cwd=self._react_app_path)

    def start(self):
        """
        Runs the app in development mode. Open http://localhost:3000 to view it in the browser.

        Related Pages:

          https://create-react-app.dev/docs/getting-started/
        """
        subprocess.run('npm test', shell=True, cwd=self._react_app_path)

    def test(self):
        """
        Runs the test watcher in an interactive mode. By default, runs tests related to files changed since the last
        commit.

        Related Pages:

          https://create-react-app.dev/docs/getting-started/
        """
        subprocess.run('npm test', shell=True, cwd=self._react_app_path)

    def npm(self, packages: List[str]):
        """
        This will add the npm requirements to the Angular app but also update directly the angular.json for anything
        needed at the start of the application.

        :param packages: List. The package names to install
        """
        if self.envs is not None:
            for env in self.envs:
                subprocess.run(env, shell=True, cwd=self._react_app_path)
        packages = node.npm_packages(packages)
        subprocess.run('npm install %s' % " ".join(packages), shell=True, cwd=self._react_app_path)


class App:

    def __init__(self, app_path, app_name, alias, name, page=None, target_folder="views"):
        self.imports = {}
        self.vars, self.__map_var_names, self.page = {}, {}, page
        self._app_path, self._app_name = app_path, app_name
        self.alias, self.__path, self.className, self.__components = alias, target_folder, name, None
        self.comps = {}

    @property
    def name(self):
        """ Return the prefix of the component module (without any extension) """
        return self.className

    @property
    def path(self):
        """ Return the full path of the component modules """
        return os.path.join("./", self.__path, self.name).replace("\\", "/")

    def route(self, component: str, alias: str, path: str):
        """
        Add the app to the routing mechanism.
        By default all the views are in a view folder within the Raact App.

        :param component: The module name
        :param alias: The url route
        :param path: The .js module path
        """
        index_router = os.path.join(self._app_path, 'src', "index.js")
        if not os.path.exists(index_router):
            raise ValueError("Problem with the React app")

        with open(index_router) as f:
            route = f.read()  # .split("\n\n")

        if component not in route:
            routes = route.split("import { Route, Link, BrowserRouter as Router } from 'react-router-dom';")
            routes[0] = "%s\nimport %s from '%s';\n" % (routes[0].strip(), component, path.replace("./src", "."))
            dis_route = routes[1].split("\n")
            for i, line in enumerate(dis_route):
                if line.strip().startswith("<Route "):
                    break

            else:
                raise ValueError("Issue with file, please udpate the index.js manually")

            route_end = dis_route[:i] + ['      <Route path="/%s" component={%s} />' % (alias, component)] + dis_route[
                                                                                                             i:]
            with open(index_router, "w") as f:
                f.write("\n".join([routes[0]] + [
                    "import { Route, Link, BrowserRouter as Router } from 'react-router-dom';"] + route_end))

    def export(self, path: str = None, target_path: List[str] = None):
        """

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

        page = self.page.outs.web()
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
                if js_dep in self.page.jsImports:
                    f.write("%s\n" % JS_MODULES_IMPORTS[js_dep])
            for buider in page['jsFrgsCommon'].values():
                f.write("export %s;\n" % buider)


class React(node.Node):

    def create(self, name: str):
        """
        To create a new project, run:

        Related Pages:

          https://create-react-app.dev/docs/getting-started/

        :param name: String. The application name
        """
        if name is None:
            subprocess.run('npx create-react-app --help', shell=True, cwd=self._app_path)
        else:
            subprocess.run('npx create-react-app %s' % name, shell=True, cwd=self._app_path)

    def serve(self, app_name: str, port: int = 8081):
        """
        Return the version of React.js on the server

        Related Pages:

          https://create-react-app.dev/docs/getting-started/

        :param app_name:
        :param port:
        """
        path = os.path.join(self._app_path, app_name)
        subprocess.run('npm start --port %s' % port, shell=True, cwd=path)

    def cli(self, app_name: str = None):
        """
        Create React App is an officially supported way to create single-page React applications.
        It offers a modern build setup with no configuration.

        Related Pages:

          https://create-react-app.dev/docs/getting-started

        :param app_name: The React.js application name
        """
        app_name = app_name or self._app_name
        return NpxCli(self._app_path, app_name, self.envs)

    def router(self, app_name: str, **kwargs):
        """
        React Router is the de-facto React routing library, and it’s one of the most popular projects built on top of React.
        This function will also update the module index.js in order to add the router automatically is missing

        Related Pages:

          https://flaviocopes.com/react-router/

        :param app_name:
        """
        path = os.path.join(self._app_path, app_name, 'src', 'index.js')
        # subprocess.run('npm install react-router-dom', shell=True, cwd=path)
        with open(path) as f:
            content = f.read()
        if 'react-router-dom' not in content:
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

    def page(self, selector: str = None, name: str = None, page=None, auto_route: bool = False,
             target_folder: str = "apps"):
        """
        Create a specific Application as a component in the Angular framework.

        Unlike a basic component, the application will be routed to be accessed directly.

        :param page:  A report object
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
        self.__route = auto_route
        return self._page

    def publish(self, app_name: str = None, target_path: str = None):
        """
        Publish the React application

        :param app_name:
        :param target_path: List  for example ['src', 'app']
        """
        # if self._page is not None:
        #  self._page.export(target_path=target_path)
        if self.__route:
            self._page.route(self._page.name, self._page.alias, self._page.path)

    def home_page(self, page, app_name=None, with_router=False):
        """
        Change the Angular App home page

        :param page:
        :param app_name:
        :param with_router:
        """
