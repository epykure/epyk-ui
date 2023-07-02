import sys
import os
from pathlib import Path
from typing import Union

from epyk.core.py import primitives
from epyk.web import node
from epyk.web import angular
from epyk.web import svelte
from epyk.web import vue
from epyk.web import react
from epyk.web import jupyter


class AppRoute:

    def __init__(self, page: primitives.PageModel):
        self.page = page

    def _name(self, value: str = None) -> str:
        """ Return the appropriate application name """
        if value is not None:
            return value

        return os.path.split(sys.argv[0])[1][:-3]

    def _selector(self, value: str = None) -> str:
        """ Return the selector application name """
        if value is not None:
            return value

        return os.path.split(sys.argv[0])[1][:-3]

    def nodejs(
            self, root_path: Union[Path, str],
            app_folder: str = node.APP_FOLDER, assets_folder: str = node.ASSET_FOLDER) -> node.Node:
        """
        Entry point to a local NodeJs setup.
        This will allow the framework to convert modules and integrate them to an external Node App.

        If selector or name is defined a page will be added to the app.

        Usage::

            import epyk as ek
            cps = ek.standalone.from_json(r".\standalones\assets", is_parent=True)

            page = ek.Page()
            ...

            nodejs_app = page.apps.nodejs(r".\Dev\nodejs")
            nodejs_app.publish("test", selector="node-app")

        :param root_path: Root path for the NodeJs server
        :param app_folder: The applications sub folder (default app)
        :param assets_folder: The components sub folder (default assets)
        """
        node_srv = node.Node(root_path, page=self.page, app_folder=app_folder, assets_folder=assets_folder)
        node_srv.app()
        return node_srv

    def angular(
            self, root_path: Union[Path, str], app_name: str,
            app_folder: str = node.APP_FOLDER, assets_folder: str = node.ASSET_FOLDER) -> angular.Angular:
        """
        Entry point to a local Angular setup.
        This will allow the framework to convert modules and integrate them to an external Angular App.

        If selector or name is defined a page will be added to the app.

        :param root_path: Root path for the Angular server
        :param app_name: The application name (sub folder on the Angular server)
        :param app_folder: The applications sub folder (default app)
        :param assets_folder: The components sub folder (default assets)
        """
        ang_srv = angular.Angular(
            root_path, app_name, page=self.page, app_folder=app_folder, assets_folder=assets_folder)
        ang_srv.create(app_name)
        ang_srv.app()
        return ang_srv

    def react(self, root_path: Union[Path, str], app_name: str,
              app_folder: str = node.APP_FOLDER, assets_folder: str = node.ASSET_FOLDER) -> react.React:
        """
        Entry point to a local React setup.
        This will allow the framework to convert modules and integrate them to an external React App.

        If selector or name is defined a page will be added to the app.

        :param root_path: Root path for the React server
        :param app_name: The application name (sub folder on the Angular server)
        :param app_folder: The applications sub folder (default app)
        :param assets_folder: The components sub folder (default assets)
        """
        react_srv = react.React(
            root_path=root_path, page=self.page, app_folder=app_folder, assets_folder=assets_folder)
        react_srv.create(app_name.lower())
        react_srv.app()
        return react_srv

    def vue(
            self, root_path: Union[Path, str], app_name: str,
            app_folder: str = node.APP_FOLDER, assets_folder: str = node.ASSET_FOLDER) -> vue.VueJs:
        """
        Entry point to a local Vue setup.
        This will allow the framework to convert modules and integrate them to an external Vue App.

        If selector or name is defined a page will be added to the app.

        :param root_path: Root path for the vue server
        :param app_name: The application name (sub folder on the vue server)
        :param app_folder: The applications sub folder (default app)
        :param assets_folder: The components sub folder (default assets)
        """
        vue_srv = vue.VueJs(
            root_path=root_path, name=app_name, page=self.page, app_folder=app_folder, assets_folder=assets_folder)
        vue_srv.create(app_name)
        vue_srv.app()
        return vue_srv

    def svelte(self, root_path: Union[Path, str], app_name: str,
               app_folder: str = node.APP_FOLDER, assets_folder: str = node.ASSET_FOLDER) -> svelte.Svelte:
        """
        Entry point to a local Svelte setup.
        This will allow the framework to convert modules and integrate them to an external Svelte App.

        If selector or name is defined a page will be added to the app.

        :param root_path: Root path for the Svelte server
        :param app_name: The application name (sub folder on the Svelte server)
        :param app_folder: The applications sub folder (default app)
        :param assets_folder: The components sub folder (default assets)
        """
        svelte_srv = svelte.Svelte(
            root_path=root_path, name=app_name, page=self.page, app_folder=app_folder, assets_folder=assets_folder)
        # svelte_srv.create(app_name)
        svelte_srv.init(app_name)
        svelte_srv.app()
        return svelte_srv

    @property
    def jupyter(self):
        """
        Entry point to a local Jupyter configuration.
        This will provide some information concerning the configuration of the local Jupyter instance.
        """
        return jupyter.Jupyter(self.page)
