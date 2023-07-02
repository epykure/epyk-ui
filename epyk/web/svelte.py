import subprocess
import json
import zipfile
import logging
from typing import Any, Dict, List
from pathlib import Path

from . import node, npm, templates
from ..core.css import css_files_loader
from ..core.html import Standalone, html_template_loader


# React system files / templates
PROJECT_SRC_ALIAS = "src"


def to_view(web_page, selector: str, app_path: Path):
    """

    """
    resource_path = Path(app_path, selector)
    resource_path.mkdir(parents=True, exist_ok=True)


def to_component(
        component: Standalone.Component, name: str = "ek-svelte-{selector}-{version}", out_path: str = None,
        version: str = None, init_value: Any = "", init_options: dict = None) -> Dict[str, str]:
    """
    Convert a Standalone component to a valid Svelte component.

    Adding a version will create a zip archive to ease the component management and sharing.

    TODO: Extend this to any components
    TODO: add concept of views to get more bespoke components from page object

    :param component: The component class
    :param name: The component name
    :param out_path: Optional. The output path to generate the component's assets
    :param version: Optional. The component version (to store all files to a zip archive)
    :param init_value: Optional. Initial values
    :param init_options: Optional. Component options
    """
    if out_path is None:
        out_path = Path().cwd()
    init_options = init_options or {}

    component_files = {"js": name.format(selector=component.selector, version=version) + ".js"}
    with open(Path(out_path, component_files["js"]), "w") as jf:
        js_path = Path(component.component_url)
        with open(js_path) as hf:
            jf.write(npm.to_module(hf.read(), component.requirements))

    component_files["component"] = name.format(selector=component.selector, version=version) + ".svelte"
    with open(Path(out_path, component_files["component"]), "w") as sf:
        css_styles = css_files_loader(component.style_urls, minify=False)
        html_def = html_template_loader(
            component.template_url, new_var_format="{ %s }",
            ref_expr="bind:this={{ %s }}" % component.__name__.lower())
        js_expr = ["export let %s" % v for v in html_def["vars"]]
        js_expr.append("export let %s")
        js_expr.append("import { onMount } from 'svelte'")
        js_expr.append("import { %s } from './%s'" % (component.__name__, component_files["js"]))
        js_expr.append('onMount(() => {component = new %s(%s, %s, %s);})' % (
            component.__name__, component.__name__.lower(), json.dumps(init_value), init_options))
        sf.write(templates.SVELTE_COMPONENT % {
            "css": css_styles, # Add the CSS Styles
            "html": html_def["template"],  # Add HTML
            "js": "; \n".join(js_expr)  # Add script section
        })

    if version is not None:
        out_zip_name = name.format(selector=component.selector, version=version) + ".zip"
        with zipfile.ZipFile(out_zip_name, 'w') as zip_object:
            zip_object.write(component_files["js"], component_files["js"])
            zip_object.write(component_files["component"], component_files["component"])
            # delete files in the folder
            Path(out_path, component_files["js"]).unlink()
            Path(out_path, component_files["component"]).unlink()
    return component_files


def add_to_app(
        components: List[Standalone.Component],
        app_path: str,
        folder: str = "assets",
        name: str = "{selector}",
        raise_exception: bool = False
) -> dict:
    """
    This will add the component directly tp the src/routes folder in the linked application.
    All components generated will be put in a sub folder.

    :param components: List of components to add to a Svelte application
    :param app_path: React application path (root)
    :param folder: Components' folder
    :param name: Component's files name format
    :param raise_exception: Flag to raise exception if error
    """
    result = {"dependencies": {}}
    for component in components:
        result[component.selector] = npm.check_component_requirements(component, app_path, raise_exception)
        result["dependencies"].update(result[component.selector])
        assets_path = Path(app_path, "src", "routes", folder)
        assets_path.mkdir(parents=True, exist_ok=True)
        to_component(component, name=name, out_path=str(assets_path))
    return result


class App:

    def __init__(self, app_path, app_name, server):
        self.imports = {}
        self.vars, self.__map_var_names, self.server, self.__components = {}, {}, server, None
        self._app_path, self._app_name = app_path, app_name
        self.comps = {}

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

    def export(self, selector: str):
        """

        :param selector: Component / Application internal selector (name)
        """
        logging.info("export %s to: %s" % (selector, self.server.views_path))
        self.server.views_path.mkdir(parents=True, exist_ok=True)

        # Write all the component
        add_to_app(
            self.server.page._props["schema"].values(), self.server.app_path, folder=self.server.assets_path.name)

        # Write the view
        to_view(self.server.page, selector, self.server.views_path)


class Svelte(node.Node):

    def __init__(self, root_path: str, name: str = None, page = None, app_folder: str = node.APP_FOLDER,
                 assets_folder: str = node.ASSET_FOLDER):
        super(Svelte, self).__init__(root_path, name, page)
        self._app_folder, self._app_asset, self.__clis = app_folder, assets_folder, None
        self.__app = None # The active application to the server


    @property
    def views_path(self) -> Path:
        """ The application views path """
        return Path(self.root_path, self._app_name, PROJECT_SRC_ALIAS, "routes", self._app_folder)

    @property
    def node_modules_path(self) -> Path:
        """ The application node_modules path """
        return Path(self.root_path, self._app_name, "node_modules")

    @property
    def assets_path(self):
        """ The application assets / components path """
        return Path(self.root_path, self._app_name, PROJECT_SRC_ALIAS, "routes", self._app_asset)

    def create(self, name: str = None):
        """
        To create a new project, run:

        Related Pages:

          https://svelte.dev/docs

        :param name: The application name
        """
        if name is not None:
            self._app_name = name
            if Path(self.root_path, name).exists():
                logging.info("React app %s already available" % name)
            else:
                subprocess.run('npm create svelte@latest %s' % name, shell=True, cwd=self.root_path)
        else:
            subprocess.run('npm create svelte@latest --help', shell=True, cwd=self.root_path)

    def install(self, name: str = None):
        """

        :param name: The application name
        """
        if not name:
            subprocess.run('npm install', shell=True, cwd=self.app_path)
        else:
            self._app_name = name
            subprocess.run('cd %s;npm install' % name, shell=True, cwd=self.root_path)

    def init(self, name: str = None):
        """
        To create a new project, run:

        Related Pages:

          https://svelte.dev/docs

        :param name: The application name
        """
        if name is not None:
            self._app_name = name
            if Path(self.root_path, name).exists():
                logging.info("React app %s already available" % name)
            else:
                subprocess.run('npm init svelte@next %s' % name, shell=True, cwd=self.root_path)
        else:
            subprocess.run('npm init svelte@next --help', shell=True, cwd=self.root_path)

    def serve(self, name: str = None):
        """

        :param name: The application name
        """
        if not name:
            subprocess.run('npm run dev', shell=True, cwd=self.app_path)
        else:
            self._app_name = name
            subprocess.run('cd %s;npm run dev' % name, shell=True, cwd=self.root_path)

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
            self.__app = App(self.root_path, self._app_name, server=self)
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

    def home_page(self, page, app_name=None, with_router=False):
        """
        Change the Angular App home page

        :param page:
        :param app_name:
        :param with_router:
        """
