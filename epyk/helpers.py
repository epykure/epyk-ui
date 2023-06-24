import logging

from epyk.core.css.themes import Theme
from epyk.core.css import Icons, css_files_loader
from epyk.core.html import Standalone, html_template_loader

from epyk.web import templates, npm

from typing import Dict, Union, Any, List

from collections import OrderedDict
import zipfile
import json
from pathlib import Path


def scss_colors(out_file_path: str = "COLORS.SCSS", theme: Theme.Theme = None):
    """
    Create a SCSS template file for the definition of colors theme.
    It will generate a schema based on the default theme definition.

    Usages::

        import epyk as ek
        ek.helpers.scss_colors()

    :param out_file_path: Optional. The full scss file path
    :param theme: Optional. The theme to export
    """
    with open(out_file_path, "w") as fp:
        fp.write("/* Auto generated SCSS files for colors definition */ \n")
        if theme is None:
            theme = Theme.ThemeDefault()
        mapped_groups = {"theme": "colors", "grey": "greys"}
        for group in theme.groups:
            fp.write("\n/* Colors codes for %s */ \n" % group)
            for i, color in enumerate(getattr(theme, mapped_groups.get(group, group))[::-1]):
                if i == 0:
                    fp.write("$color-%s-50: %s;\n" % (group, color))
                else:
                    fp.write("$color-%s-%s: %s;\n" % (group, i * 100, color))

        fp.write("\n\n/* Colors codes for charts */ \n")
        if not theme.chart_categories:
            fp.write("/*$charts: (green, blue, purple, yellow, orange, red, brown) ; */ \n")
            fp.write("$charts: default ; \n\n")
            for i, color in enumerate(theme.charts):
                if i == 0:
                    fp.write("$chart-default-50: %s;\n" % color)
                else:
                    fp.write("$chart-default-%s: %s;\n" % (i * 100, color))
        else:
            if len(theme.chart_categories) > 1:
                fp.write("/*$charts: (%s) ; */ \n" % ", ".join(theme.chart_categories))
            else:
                fp.write("/*$charts: (green, blue, purple, yellow, orange, red, brown) ; */ \n")
                fp.write("$charts: %s ; \n\n" % theme.chart_categories[0])
            for group in theme.chart_categories:
                for i, color in enumerate(theme.charts):
                    if i == 0:
                        fp.write("$chart-%s-50: %s;\n" % (group, color))
                    else:
                        fp.write("$chart-%s-%s: %s;\n" % (group, i * 100, color))


def scss_icons(out_file_path: str = "ICONS.SCSS"):
    """
    Create a SCSS template file for the definition of Icons.
    It will generate a schema based on the default definition using font-awesome icons.

    Usages::

        import epyk as ek
        ek.helpers.scss_icons()

    :param out_file_path: Optional. The full scss file path
    """
    with open(out_file_path, "w") as fp:
        fp.write("/* Auto generated SCSS files for icons definition */ \n\n")
        for k, v in Icons._ICON_MAPPINGS["font-awesome"].items():
            fp.write("$%s: %s;\n" % (k, v))


def check_component_requirements(component: Standalone.Component, app_path: str,
                                 raise_exception: bool = False) -> Dict[str, Union[bool, str]]:
    """
    Check modules installed in the current NodeJs environment to validate the compatibility with the component.
    This will not check the version (only the installed packages).

    Check on the version can be done based on the function return.

    :param component: The Standalone component
    :param app_path: The NodeJs application path (any NodeJs application)
    :param raise_exception: Flag to raise an exception if packages missing
    """
    node_modules_path = Path(Path(app_path), "node_modules")
    if not node_modules_path.exists():
        node_modules_path = Path(Path(app_path).parent, "node_modules")
    if not node_modules_path.exists():
        raise ValueError("Path does not seem to be a valid NodeJs app (%s missing)" % node_modules_path)

    packages_status = {}
    for req in component.requirements:
        package_path = Path(node_modules_path, req)
        if package_path.exists():
            try:
                with open(Path(package_path, "package.json")) as fp:
                    content = json.load(fp)
                    packages_status[req] = content["version"]
            except:
                packages_status[req] = "NA"
        else:
            packages_status[req] = False
    if raise_exception:
        missing_pkgs = [k for k, v in packages_status.items() if not v]
        if len(missing_pkgs):
            raise ValueError("Missing dependencies run: npm -i %s" % ",".join(missing_pkgs))

    return packages_status


def to_svelte_component(
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


def to_angular_component(
        component: Standalone.Component, name: str = "ek-angular-{selector}-{version}", out_path: str = None,
        version: str = None, init_value: Any = "", init_options: dict = None) -> Dict[str, str]:
    """

    :param component:
    :param name:
    :param out_path:
    :param version:
    :param init_value:
    :param init_options:
    """
    component_files = {}
    # Write component definition to the assets folder
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

    component_files["html"] = name.format(selector=component.selector, version=version) + ".html"
    with open(Path(out_path, component_files["html"]), "w") as hf:
        html_def = html_template_loader(component.template_url, ref_expr="#%s" % component.__name__.lower())
        hf.write(html_def["template"])

    component_files["spec"] = name.format(selector=component.selector, version=version) + ".component.spec.ts"
    with open(Path(Path(out_path).parent, component_files["spec"]), "w") as sf:
        sf.write(templates.ANGULAR_COMPONENT_SPEC % {
            "asset_class": component.__name__,
        })

    component_files["component"] = name.format(selector=component.selector, version=version) + ".component.ts"
    js_frgs = ["@Input() %s" % var for var in html_def['vars']]
    # @Input() label;
    with open(Path(Path(out_path).parent, component_files["component"]), "w") as sf:
        sf.write(templates.ANGULAR_COMPONENT % {
            "asset_class": component.__name__,
            "selector": component.selector,
            "asset_path": "./%s/%s" % (Path(out_path).name, name.format(selector=component.selector, version=version)),
            "js": '%s ; component; @ViewChild("%s", { static: true }) input;' % (
                ";".join(js_frgs), component.__name__.lower()),
            "init_value": json.dumps(init_value),
            "init_options": init_options,
            "html": html_def["template"],
        })

    if version is not None:
        out_zip_name = name.format(selector=component.selector, version=version) + ".zip"
        with zipfile.ZipFile(out_zip_name, 'w') as zip_object:
            zip_object.write(str(Path(component.selector, component_files["js"])), str(Path(component.selector, component_files["js"])))
            zip_object.write(str(Path(component.selector, component_files["css"])), str(Path(component.selector, component_files["css"])))
            zip_object.write(str(Path(component.selector, component_files["html"])), str(Path(component.selector, component_files["html"])))
            zip_object.write(component_files["spec"], component_files["spec"])
            zip_object.write(component_files["component"], component_files["component"])
            # delete files in the folder
            Path(out_path, component_files["js"]).unlink()
            Path(out_path, component_files["css"]).unlink()
            Path(out_path, component_files["html"]).unlink()
            Path(Path(out_path).parent, component_files["spec"]).unlink()
            Path(Path(out_path).parent, component_files["component"]).unlink()
    return component_files


def to_react_component(
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


def to_vue_component(
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
            zip_object.write(str(Path(component.selector, component_files["js"])), str(Path(component.selector, component_files["js"])))
            zip_object.write(str(Path(component.selector, component_files["css"])), str(Path(component.selector, component_files["css"])))
            zip_object.write(str(Path(component.selector, component_files["html"])), str(Path(component.selector, component_files["html"])))
            zip_object.write(component_files["component"], component_files["component"])
            # delete files in the folder
            Path(out_path, component_files["js"]).unlink()
            Path(out_path, component_files["css"]).unlink()
            Path(out_path, component_files["html"]).unlink()
            Path(Path(out_path).parent, component_files["component"]).unlink()
    return component_files


def add_to_svelte_app(
        components: Standalone.Component,
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
        result[component.selector] = check_component_requirements(component, app_path, raise_exception)
        result["dependencies"].update(result[component.selector])
        assets_path = Path(app_path, "src", "routes", folder)
        assets_path.mkdir(parents=True, exist_ok=True)
        to_svelte_component(component, name=name, out_path=str(assets_path))
    return result


def add_to_react_app(
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
        result[component.selector] = check_component_requirements(component, app_path, raise_exception)
        result["dependencies"].update(result[component.selector])
        assets_path = Path(app_path, "src", folder)
        assets_path.mkdir(parents=True, exist_ok=True)
        to_react_component(component, name=name, out_path=str(assets_path))
    return result


def add_to_angular_app(
        components: Standalone.Component,
        app_path: str,
        folder: str = "assets",
        name: str = "{selector}",
        raise_exception: bool = False,
        view_path: str = "app"
) -> dict:
    """
    This will add the component directly tp the src folder in the linked application.
    All components generated will be put in a sub folder.

    To start the angular application: ng serve --open

    This will also update the required angular system files accordingly

    :param components: List of components to add to a Angular application
    :param app_path: Angular application path (root)
    :param folder: Components' folder
    :param name: Component's files name format
    :param raise_exception: Flag to raise exception if error
    :param view_path: The path for the Angular view (the app file). default app/
    """
    result = {"dependencies": {}, "styles": [], "scripts": [], "modules": {}}
    for component in components:
        result[component.selector] = check_component_requirements(component, app_path, raise_exception)
        result["dependencies"].update(result[component.selector])
        assets_path = Path(app_path, "src", folder)
        assets_path.mkdir(parents=True, exist_ok=True)
        component_files = to_angular_component(component, name=name, out_path=str(assets_path))
        result["styles"].extend(npm.get_styles(component.requirements))
        result["scripts"].extend(npm.get_scripts(component.requirements))
        result["modules"][component.__name__] = component.get_import(
            "../%s/%s" % (folder, component_files["component"][:-3]), suffix="Component",
            root_path=Path(app_path, "src", view_path))
    angular_config_path = Path(app_path, "angular.json")
    if angular_config_path.exists():
        app_path = Path(app_path)
        with open(angular_config_path) as ap:
            angular_config = json.loads(ap.read(), object_pairs_hook=OrderedDict)
            for cat in ["styles", "scripts"]:
                for style in set(result[cat]):
                    if style not in angular_config["projects"][app_path.name]["architect"]["build"]["options"][cat]:
                        angular_config["projects"][app_path.name]["architect"]["build"]["options"][cat].insert(0, style)
        with open(angular_config_path, "w") as ap:
            json.dump(angular_config, ap, indent=2)
    else:
        count_styles = len(result["styles"])
        count_scripts = len(result["scripts"])
        logging.warning("%s styles and %s scripts not added" % (count_styles, count_scripts))
        logging.warning("Cannot locate file: %s" % angular_config_path)
    app_module_path = Path(app_path, "src", view_path, "app.module.ts")
    if app_module_path.exists():
        auto_update = False
        with open(app_module_path) as am:
            imports, config = map(lambda x: x.strip(), am.read().split("@NgModule"))
            imports = imports + "\n\n// Auto generated"
            for module in result["modules"].values():
                if module not in imports:
                    imports = "%s\n%s;" % (imports, module)
                    auto_update = True
        if auto_update:
            with open(app_module_path, "w") as am:
                am.write("%s\n\n@NgModule%s" % (imports, config))
    return result


def add_to_vue_app(
        components: List[Standalone.Component],
        app_path: str,
        folder: str = "assets",
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
        result[component.selector] = check_component_requirements(component, app_path, raise_exception)
        result["dependencies"].update(result[component.selector])
        assets_path = Path(app_path, "src", folder)
        assets_path.mkdir(parents=True, exist_ok=True)
        to_react_component(component, name=name, out_path=str(assets_path))
    return result
