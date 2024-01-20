from epyk.core.js import Imports

from typing import Tuple, List, Union, Dict
from pathlib import Path
from collections import OrderedDict
import logging
import json

from urllib.request import urlopen, Request


PACKAGES = {

    'ag-grid-community': {
        "path": 'dist',
        'imports': [
            "import * as agGrid from 'ag-grid-community'",
        ],
        "styles": [
            "ag-grid-community/styles/ag-grid.css",
            "ag-grid-community/styles/ag-theme-alpine.css"
        ]
    },

    'chart.js': {
        "path": 'dist',
        'imports': [
            "import {{ Chart, registerables }} from 'chart.js'",
            "Chart.register(...registerables)"
        ]
    },

    'accounting': {
        "path": 'lib',
    },

    "chartist": {
        "path": 'dist',
        'imports': [
                "import { %(chartClass)s } from 'chartist'"
        ],
        "styles": [
            "node_modules/chartist/dist/chartist.css"
        ]
    },

    'underscore': {
        "imports": [
            "import _, {{ map }} from 'underscore'"
        ]
    },

    "bootstrap": {
        "styles": [
            "node_modules/bootstrap/scss/bootstrap.scss"
        ],
        "scripts": [
            "node_modules/bootstrap/dist/js/bootstrap.bundle.min.js"
        ]
    },

    'bootstrap-icons': {
        "styles": [
            "node_modules/bootstrap-icons/font/bootstrap-icons.css"
        ]
    },

    "@eonasdan/tempus-dominus": {
        "imports": [
            "import * as tempusDominus from '@eonasdan/tempus-dominus'"
        ],
        "styles": [
            "node_modules/@eonasdan/tempus-dominus/dist/css/tempus-dominus.css"
        ]
    },

    "moment": {
        "imports": [
            "import * as moment from 'moment'"
        ]
    },

    'tabulator-tables': {
        "imports": [
            "import {{ TabulatorFull as Tabulator }} from 'tabulator-tables'"
        ],
        "styles": [
            "node_modules/tabulator-tables/dist/css/tabulator.css"
        ]
    },

    'jquery': {
        "imports": [
            "declare var $: any"
        ],
        "scripts": [
            "node_modules/jquery/dist/jquery.min.js"
        ]
    },

    'jqueryui': {
        "scripts": [
            "node_modules/jquery-ui/jquery-ui.js"
        ]
    },

    'apexcharts': {
        "scripts": [
            "node_modules/apexcharts/dist/apexcharts.min.js"
        ]
    },

    'billboard.js': {
        "imports": [
            'import bb from "billboard.js"'
        ]
    },

    'frappe-charts': {
        "imports": [
            'import * as frappe from "frappe-charts"'
        ]

    },

    'showdown': {
        "imports": [
            'import * as showdown from "showdown"'
        ]
    }

}


def get_version(
        package_name: str,
        node_modules_path: Union[str, Path] = None,
        check_version: bool = True
) -> Dict[str, str]:
    """
    Get the version for a package within the current context (application setup and internal configuration).

    :param package_name: The package name
    :param node_modules_path: The application node_modules path
    :param check_version: Flag to specify if the version needs to be extracted from npm api
    """
    latest_version, version, category = None, None, "NOT_FOUND"
    if check_version:
        # get the current version from NPM Api
        httprequest = Request("https://registry.npmjs.org/%s/latest" % package_name, headers={
            "Accept": "application/json"})
        with urlopen(httprequest) as response:
            if response.status == 200:
                latest_version = json.loads(response.read().decode())["version"]

    if node_modules_path is not None:
        pkg_path = Path(node_modules_path, package_name, "package.json")
        if pkg_path.exists():
            with open(pkg_path) as pkp:
                version = json.loads(pkp.read()).get("version", None)
                category = "NODE_MODULE"

    if not version and package_name in Imports.JS_IMPORTS:
        version = Imports.JS_IMPORTS[package_name].get("version", "")
        category = "JS_INTERNAL"

    if not version and package_name in Imports.CSS_IMPORTS:
        version = Imports.CSS_IMPORTS[package_name].get("version", "")
        category = "CSS_INTERNAL"

    return {"version": version, "type": category, "latest": latest_version}


def get_imports(package_name: str, **kwargs) -> str:
    """
    Get all the imports to be added to the component module to run correctly within any
    web framework.

    This will add the explicit imports required in JavaScript / TypeScript modules.
    Those lines cannot be added to the js file since standalone page can't import Js modules
    and modules are not compatible with all browsers.

    :param package_name: The component package name
    """
    if package_name in PACKAGES:
        return ";\n".join(PACKAGES[package_name].get("imports", [])).format(**kwargs) + "\n"

    return ""


def to_module(content: str, requirements: Tuple[str]) -> str:
    """
    Change a component file (javascript) to a module file.

    :param content: The javaScript component content
    :param requirements: The list of npm alias requirements
    """
    content = "\n" + content
    for used_package in requirements:
        content = get_imports(used_package) + content
    return content


def get_styles(requirements: Tuple[str], **kwargs) -> List[str]:
    """
    Get the list of style files to be explicitly added to the core framework.

    :param requirements: The list of npm alias requirements
    """
    extra_styles = []
    for used_package in requirements:
        extra_styles.extend(PACKAGES.get(used_package, {}).get("styles", []))
    return extra_styles


def get_scripts(requirements: Tuple[str], **kwargs) -> List[str]:
    """
    Get the list of script files to be explicitly added to the core framework.

    :param requirements: The list of npm alias requirements
    """
    extra_scripts = []
    for used_package in requirements:
        extra_scripts.extend(PACKAGES.get(used_package, {}).get("scripts", []))
    return extra_scripts


def to_library(
        components_path: Union[Path, str],
        name: str,
        version: str,
        node_modules_path: Union[Path, str] = None,
        raise_exception: bool = False,
        **kwargs
):
    """
    Add the necessary files to create a library from the set of components.
    
    :param components_path: Path with all the components (in sub folders)
    :param name: The package name
    :param version: The package version
    :param node_modules_path: Optional. The application node_modules path
    :param raise_exception: Optional. Raise an exception if component not correctly structured
    :param kwargs: Any extra Optional. argument will be added as properties to the package.json file
    """
    # Check if package.json already exist
    # This will maintain other non-dynamic fields + packages version
    package_json_file = Path(components_path, "package.json")
    package_json, pkg_dep = {}, {}
    if package_json_file.exists():
        with open(package_json_file) as fp:
            package_json = json.loads(fp.read(), object_pairs_hook=OrderedDict)
    package_json.update({"name": name, "version": version})
    package_json.update(kwargs)

    # Look for all components
    requirements = set()
    for component_path in Path(components_path).iterdir():
        if component_path.is_dir():
            component_config_path = Path(component_path, "component.json")
            if not component_config_path.exists():
                if raise_exception:
                    raise ValueError("Component file does not exist: %s" % component_path)

                logging.error("Component file does not exist: %s" % component_path)
                continue

            with open(component_config_path) as fp:
                content = json.load(fp)
                for r in content.get('requirements', []):
                    requirements.add(r)
    pkg_versions = {r: get_version(r, node_modules_path) for r in requirements}

    # Update package.json file
    for k, v in pkg_versions.items():
        if k in package_json["dependencies"]:
            v_current = package_json["dependencies"][k].replace("^", "")
            if not v_current:
                v_current = v["version"]
            if v.get("latest") is not None and v_current != v["latest"]:
                logging.warning("%s current %s < %s " % (k, v_current, v["latest"]))
        else:
            package_json["dependencies"][k] = v


def check_component_requirements(
        component, app_path: str,
        raise_exception: bool = False
) -> Dict[str, Union[bool, str]]:
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
            except Exception as err:
                logging.error(err)
                packages_status[req] = "NA"
        else:
            packages_status[req] = False
    if raise_exception:
        missing_pkgs = [k for k, v in packages_status.items() if not v]
        if len(missing_pkgs):
            raise ValueError("Missing dependencies run: npm -i %s" % ",".join(missing_pkgs))

    return packages_status
