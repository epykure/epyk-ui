#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import re
import json
import zipfile
from pathlib import Path
from typing import List, Union, Any, Dict, Tuple
import subprocess

from ..core.html import Standalone, html_template_loader
from ..core.css import css_files_loader, inline_to_dict
from . import node, npm, templates


# React system files / templates
PROJECT_SRC_ALIAS = "src"


def clean_html(html_template: str, js_frags: str) -> Tuple[str, str]:
    """

    :param html_template:
    :param js_frags:
    """
    html = html_template.replace("class=", "className=").replace("for=", "htmlFor=").replace(
        '"{ this.state.cssStyle }"', "{ this.state.cssStyle }")

    css_maps = set()
    for style in re.findall('style="([a-zA-Z0-9%;: -]*)"', html):
        css_maps.add(style)
    for style in re.findall("style='([a-zA-Z0-9%;: -]*)'", html):
        css_maps.add(style)
    js_vars = []
    for i, k in enumerate(css_maps):
        js_vars.append("const cssStyle%s = %s" % (i, json.dumps(inline_to_dict(k))))
        html = html.replace('style="%s"' % k, 'style={ cssStyle%s }' % i).replace("style='%s'" % k, 'style={ cssStyle%s }' % i)
    js_frags = js_frags + ";\n  ".join(js_vars)
    return "<>%s</>" % html, js_frags


def to_view(web_page, selector: str, app_path: Path):
    """

    """
    class_name = node.selector_to_clss(selector)
    result = web_page.outs.web()
    # with open(Path(resource_path, component_files["js"]), "w") as jf:
    #     jf.write(npm.to_module(", ".join(list(result['jsFrgsCommon'].keys())), web_page.imports.requirements))

    component_files = {"css": class_name + ".css"}
    with open(Path(app_path, component_files["css"]), "w") as cf:
        cf.write(result['cssStyle'])

    init_value = {}
    init_options = {}
    component_files["component"] = class_name + ".js"
    js_frags = ""
    html_content, js_frags = clean_html(result["content"], js_frags)
    with open(Path(app_path, component_files["component"]), "w") as sf:
        sf.write(templates.REACT_APP % {
            "app_class": class_name,
            "js": js_frags,
            "require": '',
            "init_value": json.dumps(init_value),
            "init_options": init_options,
            "html": html_content,
        })


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
        app_path: Union[Path, str],
        folder: str = node.ASSET_FOLDER,
        name: str = "{selector}",
        raise_exception: bool = False
) -> dict:
    """
    This will add the component directly tp the src folder in the linked application.
    All components generated will be put in a sub folder.

    To start the React application: npm serve

    :param components: List of components to add to a React application
    :param app_path: React application path (root + name)
    :param folder: Components' folder
    :param name: Component's files name format
    :param raise_exception: Flag to raise exception if error
    """
    result = {"dependencies": {}}
    for component in components:
        result[component.selector] = npm.check_component_requirements(component, app_path, raise_exception)
        result["dependencies"].update(result[component.selector])
        assets_path = Path(app_path, PROJECT_SRC_ALIAS, folder)
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

    def __init__(self, server, env: str):
        self.server, self.envs = server, env

    def create(self, name: str = None):
        """
        The create-react-app is an officially supported way to create React applications.

        Related Pages:

          https://fr.reactjs.org/docs/create-a-new-react-app.html
          https://www.w3schools.com/react/default.asp

        :param name: The application name to create
        """
        if name is None:
            subprocess.run('npx create-react-app --help', shell=True, cwd=self.server.root_path)
        else:
            subprocess.run('npx create-react-app %s' % name, shell=True, cwd=self.server.root_path)

    def build(self):
        """
        Builds the app for production to the build folder.
        It correctly bundles React in production mode and optimizes the build for the best performance.

        Related Pages:

          https://create-react-app.dev/docs/getting-started/
        """
        subprocess.run('npm run build', shell=True, cwd=self.server.app_path)

    def start(self):
        """
        Runs the app in development mode. Open http://localhost:3000 to view it in the browser.

        Related Pages:

          https://create-react-app.dev/docs/getting-started/
        """
        subprocess.run('npm start', shell=True, cwd=self.server.app_path)

    def test(self):
        """
        Runs the test watcher in an interactive mode. By default, runs tests related to files changed since the last
        commit.

        Related Pages:

          https://create-react-app.dev/docs/getting-started/
        """
        subprocess.run('npm test', shell=True, cwd=self.server.app_path)

    def npm(self, packages: List[str]):
        """
        This will add the npm requirements to the Angular app but also update directly the angular.json for anything
        needed at the start of the application.

        :param packages: List. The package names to install
        """
        if self.envs is not None:
            for env in self.envs:
                subprocess.run(env, shell=True, cwd=self.server.app_path)
        packages = node.npm_packages(packages)
        subprocess.run('npm install %s' % " ".join(packages), shell=True, cwd=self.server.app_path)


class App:

    def __init__(self, server):
        self.imports, self.comps = {}, {}
        self.vars, self.__map_var_names, self.server, self.__components = {}, {}, server, None

    def route(self, component: str, alias: str):
        """
        Add the app to the routing mechanism.
        By default all the views are in a view folder within the React App.

        :param component: The module name
        :param alias: The url route
        """
        index_router = Path(self.server.app_path, "index.js")
        if not index_router.exists():
            logging.warning("Creating a router file...")

        route = ""
        if index_router.exists():
            with open(index_router) as f:
                route = f.read()
        if component not in route:
            routes = route.split("import { Route, Link, BrowserRouter as Router } from 'react-router-dom';")
            if routes:
                routes[0] = "%s\nimport %s from '%s';\n" % (routes[0].strip(), component, "./%s/%s.component" % (
                    self.server.app_path.name, component))
                dis_route = routes[1].split("\n")
            else:
                routes.append("import %s from '%s';\n" % (component, "./%s/%s.component" % (
                    self.server.app_path.name, component)))
                dis_route = []
            for i, line in enumerate(dis_route):
                if line.strip().startswith("<Route "):
                    break

            else:
                raise ValueError("Issue with file, please update the index.js manually")

            route_end = dis_route[:i] + ['      <Route path="/%s" component={%s} />' % (
                alias, component)] + dis_route[i:]
            with open(index_router, "w") as f:
                f.write("\n".join([routes[0]] + [
                    "import { Route, Link, BrowserRouter as Router } from 'react-router-dom';"] + route_end))

    def export(self, selector: str):
        """
        Export the web application from Python to a React Application.

        :param selector: The application reference / name
        """
        logging.info("export %s to: %s" % (selector, self.server.views_path))
        self.server.views_path.mkdir(parents=True, exist_ok=True)

        # Write all the component
        add_to_app(self.server.page._props["schema"].values(), self.server.app_path, folder=self.server.assets_path.name)

        # Write the view
        to_view(self.server.page, selector, self.server.views_path)


class React(node.Node):

    def __init__(self, root_path: str, name: str = None, page = None, app_folder: str = node.APP_FOLDER,
                 assets_folder: str = node.ASSET_FOLDER):
        super(React, self).__init__(root_path, name, page)
        self._app_folder, self._app_asset, self.__clis = app_folder, assets_folder, None
        self.__app = None # The active application to the server

    @property
    def index_path(self) -> Path:
        """ The application views path """
        return Path(self.root_path, self._app_name, PROJECT_SRC_ALIAS)

    @property
    def views_path(self) -> Path:
        """ The application views path """
        return Path(self.root_path, self._app_name, PROJECT_SRC_ALIAS, self._app_folder)

    @property
    def node_modules_path(self) -> Path:
        """ The application node_modules path """
        return Path(self.root_path, self._app_name, "node_modules")

    @property
    def assets_path(self):
        """ The application assets / components path """
        return Path(self.root_path, self._app_name, PROJECT_SRC_ALIAS, self._app_asset)

    def create(self, name: str = None):
        """
        To create a new project, run:

        Related Pages:

          https://create-react-app.dev/docs/getting-started/

        :param name: The application name
        """
        if name is not None:
            self._app_name = name
        if Path(self.root_path, name).exists():
            logging.info("React app %s already available" % name)
        else:
            if name is None:
                subprocess.run('npx create-react-app --help', shell=True, cwd=str(self.root_path))
            else:
                subprocess.run('npx create-react-app %s' % name, shell=True, cwd=str(self.root_path))

    def serve(self, app_name: str = None, port: int = None):
        """
        Return the version of React.js on the server

        Related Pages:

          https://create-react-app.dev/docs/getting-started/

        :param app_name: Application name / folder on the React server
        :param port:  Port to run the application
        """
        if app_name is not None:
            self._app_name = app_name
        subprocess.run('npm start --port %s' % (port or self.PORT), shell=True, cwd=str(self.app_path))

    def cli(self, app_name: str = None) -> NpxCli:
        """
        Create React App is an officially supported way to create single-page React applications.
        It offers a modern build setup with no configuration.

        Related Pages:

          https://create-react-app.dev/docs/getting-started

        :param app_name: The React.js application name
        """
        if app_name is not None:
            self._app_name = app_name
        if self.__clis is None:
            self.__clis = NpxCli(self, self.envs)
        return self.__clis

    def router(self, app_name: str = None, **kwargs):
        """
        React Router is the de-facto React routing library, and it’s one of the most popular projects built on top of React.
        This function will also update the module index.js in order to add the router automatically is missing

        Related Pages:

          https://flaviocopes.com/react-router/

        :param app_name: The application name
        """
        if app_name is not None:
            self._app_name = app_name
        path = Path(self.app_path, PROJECT_SRC_ALIAS, 'index.js')
        # subprocess.run('npm install react-router-dom', shell=True, cwd=path)
        self.npm(['react-router-dom'], check_first=True)
        if path.exists():
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
)''')
                    new_files.append(line)
                new_files.append('''
ReactDOM.render(
  routing,
  document.getElementById('root')
);''')
                with open(path, "w") as f:
                    f.write("\n".join(new_files))

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

    def publish(self, alias: str, selector: str = None, page=None, install: bool = False,
                target_folder: str = node.APP_FOLDER):
        """
        Publish the React application.
        This will also add the page to the router automatically.

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
        self.__app.route(selector, alias)
        packages = node.requirements(self.page, self.node_modules_path)
        missing_package = [k for k, v in packages.items() if not v]
        if install and missing_package:
            self.npm(missing_package)

    def home_page(self, page=None, app_name=None):
        """
        Change the Angular App home page

        :param app_name:
        :param app_name:
        """
        if app_name is not None:
            self._app_name = app_name
        if page is not None:
            self._page = page
        to_view(self._page, "App", self.index_path)
