
PACKAGES = {

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

    :param package_name:
    """
    if package_name in PACKAGES:
        return ";\n".join(PACKAGES[package_name].get("imports", [])).format(**kwargs) + "\n"

    return ""
