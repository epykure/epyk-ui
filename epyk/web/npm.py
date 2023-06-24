from typing import Tuple, List


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
            'import showdown from "showdown"'
        ]
    }

}


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
