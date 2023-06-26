import subprocess
import json
import zipfile
from typing import Any, Dict, List
from pathlib import Path

from . import node, npm, templates
from ..core.css import css_files_loader
from ..core.html import Standalone, html_template_loader


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



class Svelte(node.Node):
    def create(self, name: str):
        """
        To create a new project, run:

        Related Pages:

          https://svelte.dev/docs

        :param name: String. The application name
        """
        if name is None:
            subprocess.run('npm create svelte@latest --help', shell=True, cwd=self._app_path)
        else:
            subprocess.run('npm create svelte@latest %s' % name, shell=True, cwd=self._app_path)

    def install(self, name: str = None):
        if not name:
            subprocess.run('npm install', shell=True, cwd=self._app_path)
        else:
            subprocess.run('cd %s;npm install' % name, shell=True, cwd=self._app_path)

    def serve(self, name: str = None):
        """

        """
        if not name:
            subprocess.run('npm run dev', shell=True, cwd=self._app_path)
        else:
            subprocess.run('cd %s;npm run dev' % name, shell=True, cwd=self._app_path)
