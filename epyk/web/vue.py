import subprocess
import os
import json
import zipfile
import logging
from typing import Any, List, Dict
from pathlib import Path

from ..core.css import css_files_loader
from ..core.html import Standalone, html_template_loader
from . import node, npm, templates

# React system files / templates
PROJECT_SRC_ALIAS = "src"


def to_view(web_page, selector: str, app_path: Path):
    result = web_page.outs.web()
    result['alias'] = selector
    result['js_module'] = node.selector_to_clss(selector)
    result['builders'] = ", ".join(list(result['jsFrgsCommon'].keys()))
    #  href="https://use.fontawesome.com/releases/v5.13.0/css/all.css"
    #  @import "https://use.fontawesome.com/releases/v5.13.0/css/all.css"
    result['cssImports'] = result['cssImports'].replace('<link rel="stylesheet" href=', "@import ").replace(
        ' type="text/css">', "")
    with open(Path(app_path, "%s.vue" % selector), "w") as f:
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
    ''' % result)

    with open(Path(app_path, selector, "%s.js" % result['js_module']), "w") as jf:
        jf.write(npm.to_module(", ".join(list(result['jsFrgsCommon'].keys())), web_page.imports.requirements))


def to_component(
        component: Standalone.Component, name: str = "ek-vue-{selector}-{version}", out_path: str = None,
        version: str = None, init_value: Any = "", init_options: dict = None) -> Dict[str, str]:
    """
    Convert a Standalone component to a valid Vue component.

    Usage::

        class MyComponent(ek.standalone):
            selector = "bs-my-comp"
            requirements = ("bootstrap", )
            component_url = "./assets/awesome/bs-my-comp.js"
            style_urls = ["./assets/awesome/bs-my-comp.css"]
            template_url = "./assets/awesome/bs-my-comp.html"

        result = ek.helpers.to_vue_component(MyComponent, version="0.0.1")

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
    component_files["html"] = name.format(selector=component.selector, version=version) + ".html"
    with open(Path(out_path, component_files["html"]), "w") as hf:
        html_def = html_template_loader(
            component.template_url, new_var_format="{ this.state.%s }", ref_expr="ref={ this.dom }")
        hf.write(html_def["template"])

    component_files["component"] = name.format(selector=component.selector, version=version) + ".component.vue"
    with open(Path(Path(out_path).parent, component_files["component"]), "w") as sf:
        sf.write(templates.VUE_COMPONENT % {
            "asset_path": "./%s/%s" % (Path(out_path).name, name.format(selector=component.selector, version=version)),
        })

    if version is not None:
        out_zip_name = name.format(selector=component.selector, version=version) + ".zip"
        with zipfile.ZipFile(out_zip_name, 'w') as zip_object:
            zip_object.write(str(Path(component.selector, component_files["js"])),
                             str(Path(component.selector, component_files["js"])))
            zip_object.write(str(Path(component.selector, component_files["css"])),
                             str(Path(component.selector, component_files["css"])))
            zip_object.write(str(Path(component.selector, component_files["html"])),
                             str(Path(component.selector, component_files["html"])))
            zip_object.write(component_files["component"], component_files["component"])
            # delete files in the folder
            Path(out_path, component_files["js"]).unlink()
            Path(out_path, component_files["css"]).unlink()
            Path(out_path, component_files["html"]).unlink()
            Path(Path(out_path).parent, component_files["component"]).unlink()
    return component_files


def add_to_app(
        components: List[Standalone.Component],
        app_path: str,
        folder: str = node.ASSET_FOLDER,
        name: str = "{selector}",
        raise_exception: bool = False
) -> dict:
    """
    This will add the component directly tp the src folder in the linked application.
    All components generated will be put in a sub folder.

    :param components: List of components to add to a Vue application
    :param app_path: Vue application path (root)
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


class VueCli:
    def __init__(self, server, env):
        self.server, self.envs = server, env

    def version(self):
        """
        Return the version of Vue.js on the server

        Related Pages:

          https://cli.vuejs.org/guide/installation.html
        """
        subprocess.run('vue --version', shell=True, cwd=self.server.root_path)

    def linter(self):
        """ Update the linter options and remove the no-unused-vars. """
        with open(Path(self.server.root_path, "package.json"), 'r') as f:
            package = json.load(f)
        # Remove some rules to Vue.js configuration
        package['eslintConfig']['rules']['no-unused-vars'] = 'off'
        package['eslintConfig']['rules']['no-extra-semi'] = 1
        with open(Path(self._vue_app_path, "package.json"), 'w') as f:
            json.dump(package, f, indent=4)

    def ui(self):
        """
        You can also create and manage projects using a graphical interface with the vue ui command:

        Related Pages:

          https://cli.vuejs.org/guide/creating-a-project.html#vue-create
        """
        subprocess.run('vue ui', shell=True, cwd=self.server.root_path)

    def install(self, packages: List[str]):
        """
        Install packages to the Vue server.

        :param packages: The list of packages
        """
        if self.envs is not None:
            for env in self.envs:
                subprocess.run(env, shell=True, cwd=self.server.root_path)
        packages = node.npm_packages(packages)
        subprocess.run('npm install %s' % " ".join(packages), shell=True, cwd=self.server.root_path)

    def add_router(self):
        """
        Add a router file via the CLI command.

        Related Pages:

          https://router.vuejs.org/installation.html#npm
        """
        subprocess.run('vue add router', shell=True, cwd=self.server.root_path)


class App:
    """
    Features associated to an application running on a Vue server.
    This will get the underlying server in order to render a standard structure.

    Expected structure for an Svelte application:

         /<svelteApp>
            /src
                /lib
                /routes
                    /app
                        All the views / applications
                    /assets
                        All the components
    """

    def __init__(self, app_path: Path, app_name: str, server):
        self.vars, self.__map_var_names, self.server = {}, {}, server
        self._app_path, self._app_name, self.__components = app_path, app_name, None
        self.comps, self.module_path, self.imports = {}, None, {}

    def route(self, component: str, alias: str):
        """
        Add the app to the routing mechanism

        :param component: The module name
        :param alias: The url route
        """
        index_router = Path(self.server.app_path, PROJECT_SRC_ALIAS, 'router', "index.js")
        if not index_router.exists():
            raise ValueError("Router is not installed, run: vue add router in the Vue app")

        with open(index_router) as f:
            route = f.read()

        split_route = route.split("Vue.use(VueRouter)")
        imports = split_route[0].strip()
        if not "import %s from" % component in imports:
            imports = "%s\nimport %s from '../%s/%s.vue'" % (imports, component, self.server.views_path.name, component)
            split_maps = split_route[1].split("const routes = [")
            routes = split_maps[1].strip()
            routes = "\n { path: '/%s', name: '%s', component: %s },\n %s" % (alias, alias, component, routes)
            new_content = "%s\n\nVue.use(VueRouter)%s\n\nconst routes = [%s" % (imports, split_maps[0].strip(), routes)
            with open(index_router, "w") as f:
                f.write(new_content)

    def export(self, selector: str):
        """
        Export of view / application from Python to Svelte.

        :param selector: The component alias / reference
        """
        logging.info("export %s to: %s" % (selector, self.server.views_path))
        self.server.views_path.mkdir(parents=True, exist_ok=True)

        # Write all the component
        add_to_app(self.server.page._props["schema"].values(), self.server.app_path, folder=self.server.assets_path.name)

        # Write the view
        to_view(self.server.page, selector, self.server.views_path)


class VueJs(node.Node):

    def __init__(self, root_path: str, name: str = None, page = None, app_folder: str = node.APP_FOLDER,
                 assets_folder: str = node.ASSET_FOLDER):
        super(VueJs, self).__init__(root_path, name, page)
        self._app_folder, self._app_asset, self.__clis = app_folder, assets_folder, None
        self.__app = None # The active application to the server

    @property
    def views_path(self) -> Path:
        """ The application views path """
        return Path(self._app_path, self._app_name, PROJECT_SRC_ALIAS, self._app_folder)

    @property
    def node_modules_path(self) -> Path:
        """ The application node_modules path """
        return Path(self._app_path, "node_modules")

    def assets_path(self):
        """ The application assets / components path """
        return Path(self._app_path, self._app_name, PROJECT_SRC_ALIAS, self._app_asset)

    def create(self, name: str):
        """
        To create a new project, run:

        Related Pages:

          https://cli.vuejs.org/guide/creating-a-project.html

        :param name: The application name
        """
        if name is None:
            subprocess.run('vue create --help', shell=True, cwd=self._app_path)
        else:
            subprocess.run('vue create %s' % name, shell=True, cwd=self._app_path)

    def cli(self, app_name: str = None):
        """
        Vue specific command lines.

        Related Pages:

          https://vuejs.org/v2/guide/installation.html

        :param app_name: The application name (folder name) in the Svelte project
        """
        if app_name is not None:
            self._app_name = app_name
        return VueCli(self, self.envs)

    def serve(self, app_name: str = None, port: int = 8081):
        """
        Return the version of Vue.js on the server

        Related Pages:

          https://cli.vuejs.org/guide/cli-service.html#using-the-binary

        :param app_name: The application name (folder name) in the Svelte project
        :param port: Port number
        """
        if app_name is not None:
            self._app_name = app_name
        subprocess.run('npm run serve -- --port %s' % port, shell=True, cwd=self.app_path)

    def router(self, app_name: str = None, **kwargs):
        """

        Related Pages:

          https://router.vuejs.org/installation.html#direct-download-cdn

        :param app_name: The application name (folder name) in the Svelte project
        """
        if app_name is not None:
            self._app_name = app_name
        subprocess.run('npm install vue-router', shell=True, cwd=self.app_path)

    def help(self, app_name: str = None):
        """
        Return the version of Vue.js on the server

        Related Pages:

          https://cli.vuejs.org/guide/cli-service.html#using-the-binary

        :param app_name: The application name (folder name) in the Svelte project
        """
        if app_name is not None:
            self._app_name = app_name
        subprocess.run('npx %s help' % app_name, shell=True, cwd=self.app_path)

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
        Publish the Vue.js application

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
