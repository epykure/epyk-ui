import os
import re
import json
import logging

import collections
import subprocess
from typing import List, Dict, Union
from pathlib import Path

from epyk.core.py import primitives
from epyk.core.js import Imports

from . import templates


# Default settings for the server components (application and components)
APP_FOLDER = "app"
ASSET_FOLDER = "assets"
DEFAULT_PORT = 3000


def check_install(modules_path: str, package_json_path: str) -> Dict[str, str]:
    """
    Check the status of the packages in the node setup,
    Some modules would require extra files in order to work correctly.

    :param modules_path: Node modules path from the NodeJs set up
    :param package_json_path: The dependencies file
    """
    warnings = {}
    with open(package_json_path) as fp:
        package_json = json.load(fp)
        for dependency, version in package_json["dependencies"].items():
            for module in Imports.JS_IMPORTS.get(dependency, {}).get("modules", []):
                if "register" in Imports.JS_IMPORTS[dependency]:
                    register_def = Imports.JS_IMPORTS[dependency]["register"]
                    if "module" in register_def:
                        js_module = "%s.js" % register_def["module"]
                    else:
                        js_module = module["script"]
                    if "npm_path" in register_def:
                        npm_path = Path(modules_path, dependency, register_def["npm_path"], js_module)
                        if not npm_path.exists():
                            warnings[dependency] = "Not installed"
                    elif "node_path" in module:
                        node_path = Path(modules_path, dependency, module["node_path"][:-1], js_module)
                        if not node_path.exists():
                            warnings[dependency] = "Not installed"
                    else:
                        other_path = Path(modules_path, dependency, js_module)
                        if not other_path.exists():
                            warnings[dependency] = "Not installed"
                elif "node_path" in module:
                    npm_path = Path(modules_path, dependency, module["node_path"], module["script"])
                    if not npm_path.exists():
                        warnings[dependency] = "Not installed"
                else:
                    other_path = Path(modules_path, dependency, module["script"])
                    if not other_path.exists():
                        warnings[dependency] = "Not installed"
    return warnings


def requirements(page: primitives.PageModel, node_modules: Union[Path, str] = None) -> Dict[str, bool]:
    """
    Get the list of all the packages required in the Node Application.

    Packages can be installed in the app using the command
      > nmp install package1 package2 .....

    :param page: Python object. The report object
    :param node_modules: The application node_modules path
    """
    npms = {}
    import_mng = Imports.ImportManager(page=page)
    import_mng.online = True
    for npm_name in import_mng.cleanImports(page.jsImports, Imports.JS_IMPORTS):
        if npm_name in Imports.JS_IMPORTS:
            if not npm_name.startswith("local_") and not Path(Imports.JS_IMPORTS[npm_name]["modules"][0]["cdnjs"]).is_file():
                npms[npm_name] = True
                if node_modules is not None:
                    npm_package_path = Path(node_modules, npm_name)
                    if not npm_package_path.exists():
                        logging.warning("Missing package: %s" % npm_name)
                        npms[npm_name] = False
    return npms


def npm_packages(packages: List[str]) -> List[str]:
    """
    Return the NPM named to be used to import the various packages.

    TODO: Fully align the names

    :param packages: All the packages
    """
    mapped_packages = []
    for p in packages:
        if p in Imports.JS_IMPORTS:
            mapped_packages.append(Imports.JS_IMPORTS[p].get('register', {}).get('npm', p))
        else:
            mapped_packages.append(p)
    return mapped_packages


def selector_to_clss(selector: str) -> str:
    """
    Convert a component selector to a valid class name.
    This is used in the App generation.

    :param selector: The App selector
    """
    values = []
    for frag in selector.split("-"):
        for s in frag.split("_"):
            values.append(s.capitalize())
    return "".join(values)


class App:

    def __init__(self, server):
        self.imports = collections.OrderedDict({"http": 'http', 'url': 'url', 'fs': 'fs'})
        self.import_launchers = []
        self.vars, self.__map_var_names, self.server = {}, {}, server
        self.__components = None
        self.comps = {}

    def require(self, module: str, alias: str = None, launcher: str = ""):
        """
        Add external modules to the application.

        Related Pages:

          https://www.w3schools.com/nodejs/nodejs_modules.asp

        :param module: The module name
        :param alias: Optional. The alias name for the JavaScript Variable name
        :param launcher: Optional. The JavasCript String to be added to the page just after the imports
        """
        self.imports[module] = alias or module
        if launcher:
            self.import_launchers.append(launcher)

    def checkImports(self, app_path: str = None):
        """
        Check if the npm modules are defined on the server for the defined application.

        :param app_path: Optional. the Path of the NodeJs application
        """
        app_path = app_path or self.server.app_path
        node_modules = os.path.join(app_path, "node_modules")
        self.imports = {"showdown": "showdown"}
        for imp, alias in self.imports.items():
            if imp in Imports.JS_IMPORTS:
                if 'register' in Imports.JS_IMPORTS[imp]:
                    if not os.path.exists(
                            os.path.join(node_modules, Imports.JS_IMPORTS[imp]['register'].get('npm', imp))):
                        logging.warning("Missing module - %s - on the nodeJsServer" % imp)

    def export(self, name: str, out_path: Path = None, port: int = DEFAULT_PORT):
        """
        Export the NodeJs application.

        :param name: The component name / reference
        :param out_path: The target path for the views
        :param port: The application's port
        """
        if out_path is None:
            out_path = Path(self.server.root_path.parent, APP_FOLDER)
        if not out_path.exists():
            out_path.mkdir(parents=True, exist_ok=True)
        self.server.page.outs.html_file(path=out_path, name=name)
        requires = []
        for imp, alias in self.imports.items():
            if imp in Imports.JS_IMPORTS:
                if 'register' in Imports.JS_IMPORTS[imp]:
                    imp = Imports.JS_IMPORTS[imp]['register'].get('npm', imp)
                    alias = Imports.JS_IMPORTS[imp]['register'].get('alias', alias)
            requires.append("var %s = require('%s')" % (alias, imp))
        js_reqs = ";\n".join(requires)

        # Write the JavaScript launcher
        with open(os.path.join(out_path, "%s.js" % name), "w") as f:
            f.write('''
%s;

fs.readFile('./%s.html', function (err, html) {
    if (err) {throw err;}       
    http.createServer(function(request, response) {  
        response.writeHeader(200, {"Content-Type": "text/html"});  
        response.write(html);  
        response.end();  
    }).listen(%s);
}); ''' % (js_reqs, name, port))


class Cli:

    def __init__(self, server, env: str):
        self.server, self.envs = server, env

    def angular(self):
        """
        Add Angular CLI to the node setup.

        Related Pages:

          https://cli.angular.io/
        """
        if self.envs is not None:
            for env in self.envs:
                subprocess.run(env, shell=True, cwd=self.server.app_path)
        subprocess.run('npm install -g @angular/cli', shell=True, cwd=self.server.app_path)

    def vue(self):
        """
        Add Vue CLI to the node setup.

        Related Pages:

          https://cli.vuejs.org/
        """
        if self.envs is not None:
            for env in self.envs:
                subprocess.run(env, shell=True, cwd=self.server.app_path)
        subprocess.run('npm install -g @vue/cli', shell=True, cwd=self.server.app_path)

    def react(self):
        """
        react.cli is ReactJS command line interface.

        Using this cli you can generate modules and components very easily. This cli was created for
        React-Redux-Boilerplate.
        If your project does not have a similar architecture, you can not use this tool.

        Related Pages:

          https://github.com/Babunashvili/react.cli#readme
        """
        if self.envs is not None:
            for env in self.envs:
                subprocess.run(env, shell=True, cwd=self.server.app_path)
        subprocess.run('npm install react.cli -g', shell=True, cwd=self.server.app_path)


class Node:

    HOST: str = "localhost"
    PORT: int = 8081

    def __init__(self, root_path: str, name: str = None, page=None, app_folder: str = APP_FOLDER,
                 assets_folder: str = ASSET_FOLDER):
        self._app_path, self._app_name = root_path, name
        self._route, self._fmw_modules, self.__app = None, None, None
        self._page, self.envs = page, None
        self._app_folder, self._app_asset = app_folder, assets_folder

    @property
    def page(self):
        """ Underlying page object """
        return self._page

    @property
    def root_path(self) -> Path:
        """ The node server root path """
        return Path(self._app_path)

    @property
    def app_path(self) -> Path:
        """ The application root path """
        return Path(self._app_path, self._app_name)

    @property
    def app_name(self) -> str:
        return self._app_name

    @property
    def node_modules_path(self) -> Path:
        """ The application node_modules path """
        return Path(self._app_path, "node_modules")

    @property
    def clis(self) -> Cli:
        """ All the CLI for the most popular web frameworks. """
        return Cli(self, self.envs)

    def proxy(self, username: str, password: str, proxy_host: str, proxy_port: int, protocols: list = None):
        """
        Set NPM proxy.

        :param username:
        :param password:
        :param proxy_host:
        :param proxy_port:
        :param protocols:
        """
        if self.envs is None:
            self.envs = []
        self.envs.append('npm config set strict-ssl false --global')
        if protocols is None:
            protocols = ["https-proxy", "proxy"]
        for protocol in protocols:
            self.envs.append('npm config set %s "http://%s:%s@%s:%s"' % (
                protocol, username, password, proxy_host, proxy_port))

    def npm(self, packages: List[str], check_first: bool = False):
        """
        Use npm install on a package.

        Can be done directly on the nodeJs app using the command line:
          npm install package1 package2 .....

        :param packages: The list of packages to install retrieved from requirements()
        :param check_first: Check first if packages are already in the npm node_module folder
        """
        if check_first:
            tmp_packages = []
            for package in packages:
                if not Path(self.node_modules_path, package).exists():
                    tmp_packages.append(package)
            packages = tmp_packages
            
        if packages:
            if self.envs is not None:
                for env in self.envs:
                    subprocess.run(env, shell=True, cwd=self.node_modules_path.parent)
            packages = npm_packages(packages)
            subprocess.run('npm install %s --save' % " ".join(packages), shell=True, cwd=self.node_modules_path.parent)
            logging.info("%s packages installed" % len(packages))

    def ls(self):
        """ Search the registry for packages matching terms """
        subprocess.run('npm ls', shell=True, cwd=self.node_modules_path.parent)

    def launcher(self, app_name: str, port: int = DEFAULT_PORT, target_folder: Union[str, Path] = APP_FOLDER):
        """
        Create a single launcher for the application.

        :param app_name: The application name
        :param port: The application's port
        :param target_folder: The target folder for the launcher
        """
        launcher_path = Path(self.root_path.parent, "launchers")
        if not launcher_path.exists():
            launcher_path.mkdir(parents=True, exist_ok=True)
        router_path = Path(launcher_path, "launcher_%s.js" % app_name)
        with open(Path(self.root_path.parent, "run_%s.bat" % app_name), "w") as f:
            f.write("node.exe ./launchers/launcher_%s.js\n" % app_name)
            f.write("PAUSE")
        with open(router_path, "w") as f:
            f.write(templates.NODE_LAUNCHER % {"app_path": target_folder, "selector": app_name, "port": port})

    def launch(self, app_name: str, out_path: Path = None, port: int = DEFAULT_PORT):
        """

        :param app_name: The application name
        :param out_path: The target path for the views
        :param port: The application's port
        """
        launcher_path = Path(self.root_path.parent, "launchers")
        if not launcher_path.exists():
            launcher_path.mkdir(parents=True, exist_ok=True)
        router_path = Path(launcher_path, "launcher_%s.js" % app_name)
        target_folder = out_path or Path(self.root_path.parent, APP_FOLDER)
        if not router_path.exists() and target_folder is not None:
            self.launcher(app_name, port, out_path)
        self.run(name="./launchers/launcher_%s.js" % app_name)

    def router(self, component: str, alias: str, target_folder: str, port: int = DEFAULT_PORT,
               requires: Dict[str, str] = None):
        """
        Create a simple router file for your different views on your server.

        :param component: The component name
        :param alias: The endpoint url starting with /
        :param target_folder: The target path where the views are stored
        :param port: The port number for the node server
        :param requires: Extra package required for the router
        """
        if not alias.startswith("/"):
            raise ValueError("Route alias must start with /")

        if requires is None:
            requires = {}
        requires.update({"http": "http", "url": "parser", "fs": "fs"})
        server_file = Path(self.root_path.parent, "server.js")
        urls_map = {alias: component}
        if server_file.exists():
            with open(server_file, "r") as fs:
                result = json.loads('{%s}' % re.findall("var MAP_ROUTES = {(.*)};", fs.read())[0])
                for a, v in result.items():
                    urls_map[a.strip()] = v.strip()
        with open(server_file, "w") as f:
            f.write(templates.NODE_ROUTER % {
                "require": "\n".join(["var %s = require('%s');" % (v, k) for k, v in requires.items()]),
                "map": json.dumps(urls_map), "app_path": target_folder, "port": port})
        router_file = Path(self.root_path.parent, "node_router.bat")
        with open(router_file, "w") as r:
            r.write("ECHO ON \n")
            r.write("ECHO http://%s:%s\n" % (self.HOST, port))
            r.write("ECHO ---\n")
            for url in urls_map:
                r.write("ECHO http://%s:%s%s\n" % (self.HOST, port, url))
            r.write("ECHO ---\n\n")
            r.write("node.exe server.js\n")
            r.write("PAUSE")

    def run(self, name: str, port: int = DEFAULT_PORT):
        """
        The file you have just created must be initiated by Node.js before any action can take place.

        Related Pages:

          https://www.w3schools.com/nodejs/nodejs_get_started.asp

        :param name: The script name
        :param port: The port number for the node server
        """
        logging.info("Node server url: %s:%s" % (self.HOST, port))
        subprocess.run('node %s --port %s' % (name, port), shell=True, cwd=self._app_path)

    def inspect(self, name: str, from_launcher: bool = False):
        """

        :param name: The script name
        :param from_launcher:
        """
        if from_launcher:
            subprocess.run(
                'node --inspect ./launchers/launcher_%s.js' % name, shell=True, cwd=self._app_path)
        else:
            subprocess.run('node --inspect %s ' % name, shell=True, cwd=self.node_modules_path.parent)

    def docs(self, package: str):
        """
        Display the README.md / documentation / npmjs.org page of a give library

        :param package: The package alias
        """
        subprocess.run('npm docs %s' % package, shell=True, cwd=self.node_modules_path.parent)

    def update(self, packages: List[str]):
        """
        Update all the packages listed to the latest version (specified by the tag config).

        Also install missing packages

        :param packages: The list of packages to be installed
        """
        if self.envs is not None:
            for env in self.envs:
                subprocess.run(env, shell=True, cwd=self.node_modules_path.parent)
        subprocess.run('npm update %s' % " ".join(packages), shell=True, cwd=self.node_modules_path.parent)
        logging.info("%s packages updated" % len(packages))

    def uninstall(self, packages: List[str]):
        """
        Uninstall a package, completely removing everything npm installed on its behalf.

        :param packages: The list of packages to be installed
        """
        subprocess.run('npm uninstall %s' % " ".join(packages), shell=True, cwd=self.node_modules_path.parent)
        logging.info("%s packages uninstalled" % len(packages))

    def app(self, page=None, target_folder: str = APP_FOLDER) -> App:
        """
        Create a specific Application as a component in the Angular framework.

        Unlike a basic component, the application will be routed to be accessed directly.

        :param page: The web page (Report) object to be converted
        :param target_folder: The target sub folder for the applications (default app/)
        """
        if page is not None:
            self._page = page
        if self.__app is None:
            self.__app = App(server=self)
        return self.__app

    def publish(self, alias: str, selector: str = None, page=None, target_folder: str = APP_FOLDER):
        """
        Publish the Node.js application

        :param alias: The url endpoint for the new page
        :param selector: The view reference / selector name
        :param page: The web page (Report) object to be converted
        :param target_folder: The application target folder for the transpiled views
        """
        selector = selector or alias
        if self.__app is None:
            self.app(page, target_folder)
        self.__app.export(name=selector)
        self.router(selector, alias, target_folder=target_folder)
        self.launcher(selector, target_folder=target_folder)
