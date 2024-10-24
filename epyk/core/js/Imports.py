"""Core module in charge of linking the Python report request to the corresponding external packages required.
This package will resolve the external Javascript and CSS dependencies.
It can also help or retrieve external Python packages from the official Python Page Index online repository
"""

import re
import os
import sys
import json
import importlib
import collections
import logging
import base64
import traceback
from typing import Union, Optional, List, Dict, Any
from pathlib import Path

try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request, ProxyHandler, build_opener, install_opener
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError, ProxyHandler, build_opener, install_opener

from epyk.conf import global_settings


# To fully disable the automatic pip install request when a package is missing
AUTOLOAD = False
PROXY = ''
PCK_REPO = ''
STATIC_PATH = "/static"


def requires(name: str, reason: str = 'Missing Package', install=None, package=None, raise_except=False,
             source_script=None, pip_attrs=None):
    """Import the necessary external packages and provide explicit message to find a way to solve this error message.
    This method should also explain why this module is required to make sure this is really expected to get an error.

    :param str name:
    :param str reason:
    :param install:
    :param package:
    :param raise_except:
    :param source_script:
    :param pip_attrs: Optional. The pip attributes  https://packaging.python.org/tutorials/installing-packages/

    return: The python module
    """
    if install is None:
        install = name
    try:
        mod = importlib.import_module(name)
        if package is not None:
            return getattr(mod, package)

        return mod

    except Exception as err:
        if pip_attrs is None:
            pip_attrs = []
        if PROXY:
            pip_attrs.extend(['--proxy', PROXY])
        if PCK_REPO:
            pip_attrs.extend(['--no-index', '--find-links', PCK_REPO])

        if str(err).startswith("Missing required dependencies") and AUTOLOAD:
            logging.warning("Error with %s in script %s, autoload set to %s" % (name, source_script, AUTOLOAD))
            deps = json.loads(str(err).replace("Missing required dependencies ", "").replace("'", '"'))
            import subprocess
            for d in deps:
                exe_out = subprocess.call([sys.executable, '-m', "pip", 'install'] + pip_attrs + [d])
                logging.warning(exe_out)
            return requires(name, reason, install, package=package, raise_except=raise_except)

        if AUTOLOAD:
            if isinstance(AUTOLOAD, dict) and not AUTOLOAD.get(install, False):
                # Module not set in the configuration to be automatically loaded
                raise ValueError(err)

            logging.warning("Error with %s in script %s, autoload set to %s" % (name, source_script, AUTOLOAD))
            import subprocess
            subprocess.call([sys.executable, '-m', "pip", 'install'] + pip_attrs + [install])
            return requires(name, reason, install, package=package, raise_except=raise_except)

        if raise_except:
            logging.warning("Error with %s in script %s, autoload set to %s" % (name, source_script, AUTOLOAD))
            logging.warning("*** Module %s required ***" % name)
            logging.warning(reason)
            if install:
                logging.warning("Command to fix this error:")
                logging.warning(">>> pip install %s" % install)
            raise ValueError(err)


def load_package(package_name: str, pip_attrs: Optional[list] = None, action: str = 'install'):
    """Force the package to be installed manually to the current python distribution.
    This will run a pip command to the running python set up.

    Usage::

      load_package("pandas")

    `PYPI <https://pypi.org/>`_

    :param package_name: The external package reference (e.g. pandas)
    :param pip_attrs: Optional. The pip attributes  https://packaging.python.org/tutorials/installing-packages/
    :param action: Optional. The pip command (default install)
    """
    import subprocess

    if pip_attrs is None:
        pip_attrs = ['--ignore-installed', '--upgrade'] if action == 'install' else []
    if PROXY is not None:
        subprocess.call([sys.executable, '-m', "pip", action, '--proxy="%s"' % PROXY] + pip_attrs + [package_name])
    else:
        subprocess.call([sys.executable, '-m', "pip", action] + pip_attrs + [package_name])


def installed_packages():
    """Returns the list of packages installed on the running Python distribution.
    This will require an internet connection as it will run the pip command behind the scene.
    It will return to the console a table with the status of the obsolescence of all the python packages.

    Usage::

      installed_packages()
    """
    import subprocess
    subprocess.call(["pip", 'list', '-o'])


def string_to_base64(content: str, is_binary: bool = False) -> str:
    """Format a String content to a base64 object.

    :param content: String content
    :param is_binary: Optional. Flag to specify if content need to be encoded
    """
    if not is_binary:
        content = content.encode()
    base64_bytes = base64.b64encode(content)
    return base64_bytes.decode('ascii')


# Module variable to be updated in environment to share info related to packages.
PACKAGE_STATUS = {}

# Shortcut to always point to NPM repo via unpk
USE_NPM_UNPK = False
CDNJS_REPO = 'https://cdnjs.cloudflare.com/ajax/libs'
JSDELIVER = "https://cdn.jsdelivr.net/npm"

# Mapping to match the folder names in Jupyter
# If the folder are the same as the alias it is not included in this mapping
# Purpose is to not double load the modules in Jupyter
NOTEBOOK_MAPPING = {
    'MathJax': 'mathjax',
    'jquery-ui': 'jqueryui',
}

TABULATOR_EXTENSIONS = '0.0.29'

JS_IMPORTS = {
    #
    'intersection-observer': {
        "license": "W3C Software and Document License",
        "repository": "https://github.com/w3c/IntersectionObserver/tree/main/polyfill",
        "version": "0.12.0",
        "polyfill": True,
        'modules': [
            {'script': 'intersection-observer.js', 'path': 'intersection-observer@%(version)s/', 'cdnjs': JSDELIVER},
        ],
    },

    # numbers formatting
    'accounting': {
        "repository": "https://github.com/openexchangerates/accounting.js",
        "version": "0.4.1",
        "license": "MIT License",
        'register': {'alias': 'accounting', 'module': 'accounting.min', 'name': 'accounting'},
        'v_prefix': 'v',
        'modules': [
            {'script': 'accounting.min.js', "node_path": "", 'path': 'accounting.js/%(version)s/', 'cdnjs': CDNJS_REPO},
        ],
        'website': 'https://openexchangerates.github.io/accounting.js/'},

    # highcharts
    'highcharts': {
        'version': '11.2.0',
        "unpkg": False,
        "license": "License",
        "pricing": "https://shop.highcharts.com/",
        'modules': [
            {'script': 'highcharts.min.js', 'path': 'highcharts/%(version)s/', 'cdnjs': CDNJS_REPO},
            {'script': 'highcharts-more.min.js', 'path': 'highcharts/%(version)s/', 'cdnjs': CDNJS_REPO},
            {'script': 'highcharts-3d.min.js', 'path': 'highcharts/%(version)s/', 'cdnjs': CDNJS_REPO},
            {'script': 'accessibility.min.js', 'path': 'highcharts/%(version)s/modules/', 'cdnjs': CDNJS_REPO},
        ],
        'repository': 'https://github.com/highcharts/highcharts',
        "website": "https://www.highcharts.com/demo"
    },

    # Chartist
    'chartist': {
        'version': '0.11.4',
        "unpkg": False,
        "license": "MIT License",
        'modules': [
            {'script': 'chartist.min.js', 'path': 'chartist/%(version)s/', 'cdnjs': CDNJS_REPO},
        ],
        'repository': 'https://github.com/gionkunz/chartist-js',
        'register': {'alias': 'chartist', 'module': 'chartist.min', 'npm': 'chartist'},
        'website': 'https://gionkunz.github.io/chartist-js/?utm_source=cdnjs&utm_medium=cdnjs_link&utm_campaign=cdnjs_library'},

    # QR Code
    'qrcodejs': {
        'version': '1.0.0',
        "license": "MIT License",
        'modules': [
            {'script': 'qrcode.min.js', 'path': 'qrcodejs/%(version)s/', 'cdnjs': CDNJS_REPO},
        ],
        'repository': 'https://github.com/llyys/qrcodejs',
        'register': {'alias': 'Qrcode', 'module': 'qrcode.min', 'npm': 'qrcodejs'},
        'website': 'https://davidshimjs.github.io/qrcodejs/'},

    # data transformation
    'underscore': {
        'version': '1.13.6',
        'repository': 'https://github.com/jashkenas/underscore',
        "license": "MIT License",
        'modules': [
            {'script': 'underscore-min.js', 'path': 'underscore.js/%(version)s/', 'cdnjs': CDNJS_REPO},
            {'script': 'underscore-min.js.map', 'path': 'underscore.js/%(version)s/', 'cdnjs': CDNJS_REPO},
        ],
        'website': 'https://openexchangerates.github.io/accounting.js/'},

    # Plolyfill
    'promise-polyfill': {
        "license": "MIT License",
        'modules': [
            # Better to use the bundle version to avoid the import issue with popper.js
            {'script': 'polyfill.min.js', 'node_path': 'dist/', 'path': 'promise-polyfill@8/dist/',
             'cdnjs': 'https://cdn.jsdelivr.net/npm'},
        ],
        'version': '8.2.0',
        'repository': 'https://github.com/taylorhakes/promise-polyfill',
        'website': 'https://github.com/taylorhakes/promise-polyfill'},

    # Plolyfill for urlSearchParam for very old version of IE
    'url-search-params': {
        "license": "MIT License",
        "repository": "https://github.com/WebReflection/url-search-params?utm_source=cdnjs&utm_medium=cdnjs_link&utm_campaign=cdnjs_library",
        'version': '1.1.0',
        'modules': [
            # Better to use the bundle version to avoid the import issue with popper.js
            {'script': 'url-search-params.js', 'node_path': 'build/', 'path': 'url-search-params/%(version)s/', 'cdnjs': CDNJS_REPO},
        ],
        'website': 'https://github.com/taylorhakes/promise-polyfill'},

    # Common module for browser versions compatibilities
    'babel-polyfill': {
        'repository': 'https://github.com/babel/babel-polyfills',
        "license": "MIT License",
        'version': '7.4.4',
        'website': 'https://babeljs.io/',
        'register': {'alias': 'babel', 'module': 'polyfill', 'name': 'babel'},
        'modules': [
            {'script': 'polyfill.js', 'node_path': 'dist/', 'path': 'babel-polyfill/%(version)s/', 'cdnjs': CDNJS_REPO},
        ]
    },

    # module are written from the first one to load to the last one
    'bootstrap': {
        'req': [{'alias': 'jquery'}, {'alias': '@popperjs/core'}],
        'v_prefix': 'v',
        'version': '4.6.0',
        'license': 'MIT license',
        'repository': 'https://github.com/twbs/bootstrap',
        'modules': [
            # Better to use the bundle version to avoid the import issue with popper.js
            {'script': 'bootstrap.min.js', 'node_path': 'dist/js/', 'path': 'twitter-bootstrap/%(version)s/js/',
             'cdnjs': CDNJS_REPO},
        ],
        'assets': [
            {'script': 'bootstrap.min.js.map', 'node_path': 'dist/js/', 'path': 'twitter-bootstrap/%(version)s/js/',
             'cdnjs': CDNJS_REPO},
        ],
        'website': 'https://getbootstrap.com/'},

    'moment': {
        "version": "2.29.4",
        'repository': 'https://github.com/moment/moment',
        'register': {'alias': 'moment', 'module': 'moment.min', 'npm': 'moment'},
        'license': 'MIT license',
        'modules': [
            {'script': 'moment.min.js', 'node_path': 'min/', 'path': 'moment.js/%(version)s/', 'cdnjs': CDNJS_REPO},
        ],
        'assets': [
            {'script': 'moment.min.js.map', 'node_path': 'min/', 'path': 'moment.js/%(version)s/', 'cdnjs': CDNJS_REPO},
        ],
        'website': 'https://momentjs.com/',
    },

    'quill': {
        "version": "2.0.2",
        'repository': 'https://quilljs.com/',
        'register': {'alias': 'quill', 'module': 'quill.min', 'npm': 'quill'},
        'license': 'MIT license',
        'modules': [
            {'script': 'quill.min.js', 'node_path': 'dist/', 'path': 'quill/%(version)s/', 'cdnjs': CDNJS_REPO},
            #{'script': 'quill.core.min.js', 'node_path': 'dist/', 'path': 'quill/%(version)s/', 'cdnjs': CDNJS_REPO},
        ],
        'assets': [
            {'script': 'quill.js.map', 'node_path': 'dist/', 'path': 'quill/%(version)s/', 'cdnjs': CDNJS_REPO},
            {'script': 'quill.core.js.map', 'node_path': 'dist/', 'path': 'quill/%(version)s/', 'cdnjs': CDNJS_REPO},
        ],
        'website': 'https://momentjs.com/',
    },

    # AG Grid tables
    'ag-grid-community': {
        'website': 'https://www.ag-grid.com/javascript-grid/',
        'repository': 'https://github.com/ag-grid/ag-grid',
        'version': '31.2.0',
        'enterprise': '31.2.0',
        'license': 'MIT license',
        "pricing": "https://www.ag-grid.com/license-pricing/",
        "register": {"alias": "agGrid", "module": "ag-grid-community.min", "npm": 'ag-grid-community'},
        'modules': [
            {'script': 'ag-grid-community.min.js', 'node_path': 'dist/', 'path': 'ag-grid/%(version)s/',
             'cdnjs': CDNJS_REPO}]
    },

    # AG Charts
    'ag-charts-community': {
        'website': 'https://www.ag-grid.com/charts/javascript/quick-start/',
        'repository': 'https://github.com/ag-grid/ag-charts',
        'version': '10.2.0',
        'enterprise': '10.2.0',
        'license': 'MIT license',
        "pricing": "https://www.ag-grid.com/charts/license-pricing/",
        "register": {"alias": "agCharts", "module": "ag-charts-community.min", "npm": 'ag-charts-community'},
        'modules': [
            {'script': 'ag-charts-community.js', 'node_path': 'dist/',
              'path': 'ag-charts-community@%(version)s/dist/umd/', 'cdnjs': JSDELIVER}]
    },

    # module for tabulator
    'tabulator-tables': {
        'req': [{'alias': 'promise-polyfill'}, {'alias': 'moment'}],
        'repository': 'https://github.com/olifolkerd/tabulator',
        'license': 'MIT license',
        'version': '6.0.0', # '4.9.3',  # '5.3.1', # '4.9.3',
        'register': {'alias': 'Tabulator', 'module': 'tabulator.min', 'npm': 'tabulator-tables'},
        'modules': [
            # core only needed for Jupyter for some reasons
            {'script': 'tabulator.min.js', 'node_path': 'tabulator/dist/js', 'path': 'tabulator/%(version)s/js/',
             'cdnjs': CDNJS_REPO}
        ],
        'website': 'http://tabulator.info/'
    },

    # Tabulator configurations
    # Different modules part of the npm project to load specific configurations
    'tabulator-inputs': {
        "unpkg": False,
        'req': [{'alias': 'tabulator-tables'}],
        'modules': [
            {'script': 'formatters-inputs.js', 'version': TABULATOR_EXTENSIONS,
             'path': 'npm/tabulator-extensions@%(version)s/formatters/', 'cdnjs': 'https://cdn.jsdelivr.net'},
        ],
        'website': 'http://tabulator.info/'
    },

    'tabulator-drop': {
        "unpkg": False,
        'req': [{'alias': 'tabulator-tables'}],
        'modules': [
            {'script': 'formatters-drop.js', 'version': TABULATOR_EXTENSIONS,
             'path': 'npm/tabulator-extensions@%(version)s/formatters/', 'cdnjs': 'https://cdn.jsdelivr.net'},
        ],
        'website': 'http://tabulator.info/'
    },

    'tabulator-mutators-inputs': {
        "unpkg": False,
        'req': [{'alias': 'tabulator-tables'}],
        'modules': [
            {'script': 'mutators-inputs.js', 'version': TABULATOR_EXTENSIONS,
             'path': 'npm/tabulator-extensions@%(version)s/mutators/', 'cdnjs': 'https://cdn.jsdelivr.net'},
        ],
        'website': 'http://tabulator.info/'
    },

    'editors-inputs': {
        "unpkg": False,
        'req': [{'alias': 'tabulator-tables'}],
        'modules': [
            {'script': 'editors-inputs.js', 'version': TABULATOR_EXTENSIONS,
             'path': 'npm/tabulator-extensions@%(version)s/editors/', 'cdnjs': 'https://cdn.jsdelivr.net'}],
        'website': 'http://tabulator.info/'
    },

    'editors-dates': {
        "unpkg": False,
        'req': [{'alias': 'tabulator-tables'}],
        'modules': [
            {'script': 'editors-dates.js', 'version': TABULATOR_EXTENSIONS,
             'path': 'npm/tabulator-extensions@%(version)s/editors/', 'cdnjs': 'https://cdn.jsdelivr.net'},
        ],
        'website': 'http://tabulator.info/'
    },

    'editors-selects': {
        "unpkg": False,
        'req': [
            {'alias': 'tabulator-tables'}],
        'modules': [
            {'script': 'editors-selects.js', 'version': TABULATOR_EXTENSIONS,
             'path': 'npm/tabulator-extensions@%(version)s/editors/', 'cdnjs': 'https://cdn.jsdelivr.net'
             },
        ],
        'website': 'http://tabulator.info/'
    },

    'tabulator-icons': {
        "unpkg": False,
        'req': [{'alias': 'tabulator-tables'}],
        'modules': [
            # core only needed for Jupyter for some reasons
            {'script': 'formatters-icons.js', 'version': TABULATOR_EXTENSIONS,
             'path': 'npm/tabulator-extensions@%(version)s/formatters/', 'cdnjs': 'https://cdn.jsdelivr.net'},
        ],
        'website': 'http://tabulator.info/'
    },

    'tabulator-numbers': {
        "unpkg": False,
        'req': [
            {'alias': 'tabulator-tables'},
            {'alias': 'accounting'},
            {'alias': 'd3-scale'},
        ],
        'modules': [
            # core only needed for Jupyter for some reasons
            {'script': 'formatters-numbers.js', 'version': TABULATOR_EXTENSIONS,
             'path': 'npm/tabulator-extensions@%(version)s/formatters/', 'cdnjs': 'https://cdn.jsdelivr.net'},
            {'script': 'formatters-titles.js', 'version': TABULATOR_EXTENSIONS,
             'path': 'npm/tabulator-extensions@%(version)s/formatters/', 'cdnjs': 'https://cdn.jsdelivr.net'},
        ],
        'website': 'http://tabulator.info/'
    },

    # module for the awesome icons
    'font-awesome': {
        'version': '6.4.0',
        'unpkg': False,
        "license": "Free License",
        "pricing": "https://fontawesome.com/plans",
        "repository": "https://github.com/FortAwesome/Font-Awesome",
        'register': {'alias': 'fontawesome', 'module': 'fontawesome', 'npm': '@fortawesome/fontawesome-free',
                     'npm_path': 'js'},
        'package': {'zip': 'https://use.fontawesome.com/releases/v%(version)s/fontawesome-free-%(version)s-web.zip',
                    'root': 'fontawesome-free-%(version)s-web', 'folder': 'releases', 'path': 'v%(version)s'},
        'modules': [{'script': 'fontawesome.js', 'node_path': 'fontawesome-free/js/', 'path': 'releases/v%(version)s/js/', 'cdnjs': 'https://use.fontawesome.com'}],
        'website': 'https://fontawesome.com/'},

    # Javascript packages to handle DataTables
    'datatables': {
        'unpkg': False,
        'license': 'MIT license',
        "pricing": "https://datatables.net/purchase/index",
        'req': [{'alias': 'jquery'}],
        "website": "https://datatables.net/",
        "repository": "https://github.com/DataTables/DataTables",
        'version': '1.10.21',
        'register': {'alias': 'datatables', 'module': 'jquery.dataTables.min'},
        'modules': [
            {'reqAlias': 'datatables', 'script': 'jquery.dataTables.min.js', 'path': 'datatables/%(version)s/js/',
             'cdnjs': CDNJS_REPO},
        ]},

    # Datatable Buttons
    'datatables-buttons': {
        'unpkg': False,
        'license': 'MIT license',
        'version': '1.6.1',
        'website': 'https://datatables.net/extensions/buttons/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'dataTables.buttons.min.js', 'path': 'buttons/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable Select
    'datatables-select': {
        'unpkg': False,
        'license': 'MIT license',
        'version': '1.3.1',
        'website': 'https://datatables.net/extensions/select/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'dataTables.select.min.js', 'path': 'select/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable Scroller
    'datatables-scroller': {
        'unpkg': False,
        'version': '2.0.1',
        'website': 'https://datatables.net/extensions/scroller/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'dataTables.scroller.min.js', 'path': 'scroller/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable SearchPanes
    'datatables-searchPanes': {
        'unpkg': False,
        'version': '1.0.1',
        'website': 'https://datatables.net/extensions/searchPanes/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'dataTables.searchPanes.min.js', 'path': 'searchpanes/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable responsive
    'datatables-responsive': {
        'unpkg': False,
        'version': '2.2.3',
        'website': 'https://datatables.net/extensions/responsive/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'dataTables.responsive.min.js', 'path': 'responsive/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable KeyTable
    'datatables-keytable': {
        'unpkg': False,
        'version': '2.5.1',
        'website': 'https://datatables.net/extensions/keytable/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'dataTables.keyTable.min.js', 'path': 'keytable/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable autoFill
    'datatables-autoFill': {
        'unpkg': False,
        'version': '2.1.0',
        'website': 'https://datatables.net/extensions/autofill/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'dataTables.autoFill.min.js', 'path': 'autofill/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable group rows
    'datatables-rows-group': {
        'unpkg': False,
        'req': [{'alias': 'datatables'}],
        'version': '1.0.0',
        'modules': [
            {'script': 'dataTables.rowsGroup.js', 'path': 'datatables-rowsgroup/v%(version)s/',
             'cdnjs': 'https://cdn.rawgit.com/ashl1'}
        ],
        'website': 'https://datatables.net/forums/discussion/29319/new-rowsgroup-plugin-merge-cells-vertically-rowspan'},

    # Datatable group row
    'datatables-row-group': {
        'unpkg': False,
        'req': [{'alias': 'datatables'}],
        'version': '1.1.1',
        'modules': [
            {'script': 'dataTables.rowGroup.min.js', 'path': 'rowgroup/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}],
        'website': 'https://datatables.net/extensions/rowgroup/'},

    # Datatable fixed column
    'datatables-fixed-columns': {
        'unpkg': False,
        'req': [{'alias': 'datatables'}],
        'version': '3.2.2',
        'modules': [
            {'script': 'dataTables.fixedColumns.min.js', 'path': 'fixedcolumns/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}],
        'website': 'https://datatables.net/extensions/fixedcolumns/'},

    # Datatable Fixed header
    'datatables-fixed-header': {
        'unpkg': False,
        'req': [{'alias': 'datatables'}],
        'version': '3.1.3',
        'modules': [
            {'script': 'dataTables.fixedHeader.min.js', 'path': 'fixedheader/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}],
        'website': 'https://datatables.net/extensions/fixedheader/'},

    # Datatable data export
    'datatables-export': {
        'unpkg': False,
        'version': '1.5.2',
        'req': [
            {'alias': 'datatables'},
            {'alias': 'jszip'},
            {'alias': 'pdfmake'}],
        'website': 'https://datatables.net/extensions/buttons/',
        'modules': [
            {'script': 'buttons.colVis.min.js', 'path': 'buttons/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'},
            {'script': 'buttons.bootstrap4.min.js', 'path': 'buttons/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'},
            {'script': 'buttons.foundation.min.js', 'path': 'buttons/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'},
            {'script': 'buttons.html5.min.js', 'path': 'buttons/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'},
            {'script': 'buttons.jqueryui.min.js', 'path': 'buttons/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'},
            {'script': 'buttons.print.min.js', 'path': 'buttons/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'},
            {'script': 'buttons.semanticui.min.js', 'path': 'buttons/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}
        ]},

    # Datatable column reordering modules
    'datatables-col-order': {
        'unpkg': False,
        'req': [{'alias': 'datatables'}],
        'version': '1.5.1',
        'register': {'alias': 'datatableColOrd', 'module': 'dataTables.colReorder.min'},
        'website': 'https://datatables.net/extensions/colreorder/',
        'modules': [
            {'reqAlias': 'datatableColOrd', 'script': 'dataTables.colReorder.min.js',
             'path': 'colreorder/%(version)s/js/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Echarts A powerful, interactive charting and data visualization library for browser
    'echarts': {
        'unpkg': False,
        "license": "Apache-2.0 license",
        "repository": "https://github.com/apache/echarts",
        'version': '5.5.0',
        'website': 'https://echarts.apache.org/en/index.html',
        'modules': [
            {'script': 'echarts.min.js', 'node_path': 'dist/', 'path': 'echarts/%(version)s/', 'cdnjs': CDNJS_REPO}
        ]
    },

    # gridstack Build interactive dashboards in minute
    'gridstack': {
        'unpkg': False,
        'version': '9.5.1',
        "license": "MIT license",
        "repository": "https://github.com/gridstack/gridstack.js",
        'website': 'https://gridstackjs.com/',
        'modules': [
            {'script': 'gridstack-all.min.js', 'path': 'gridstack.js/%(version)s/', 'cdnjs': CDNJS_REPO}],
    },

    # jszip, Create, read and edit .zip files with Javascript http://stuartk.com/jszip
    'jszip': {
        'website': 'https://stuk.github.io/jszip/?utm_source=cdnjs&utm_medium=cdnjs_link&utm_campaign=cdnjs_library',
        'repository': 'https://github.com/Stuk/jszip',
        "license": "MIT license",
        'version': '3.10.1',
        'modules': [
            {'reqAlias': 'jszip', 'script': 'jszip.min.js', 'node_path': 'dist/', 'path': 'jszip/%(version)s/',
             'cdnjs': CDNJS_REPO},
        ]},

    # Reactive Extensions Library for JavaScript
    'rxjs': {
        'website': 'https://rxjs.dev/',
        "license": "Apache-2.0 license",
        "repository": "https://github.com/ReactiveX/rxjs",
        'version': '7.8.1',
        'modules': [
            {'reqAlias': 'jszip', 'script': 'rxjs.umd.min.js', 'node_path': 'dist/', 'path': 'rxjs/%(version)s/',
             'cdnjs': CDNJS_REPO},
        ]},

    #
    'json-formatter-js': {
        'website': 'https://azimi.me/json-formatter-js/',
        'version': '2.3.4',
        'repository': 'https://github.com/mohsen1/json-formatter-js',
        'register': {'alias': 'JSONFormatter', 'module': 'json-formatter.umd.min'},
        'modules': [
            {'script': 'json-formatter.umd.min.js', 'node_path': 'dist/', 'path': 'json-formatter-js@%(version)s/dist/',
             'cdnjs': "https://cdn.jsdelivr.net/npm"},
        ]},

    # Datatable pivot
    'pivottable': {
        'req': [{'alias': 'jqueryui'}],
        "license": "MIT license",
        "repository": 'https://github.com/nicolaskruchten/pivottable',
        'version': '2.23.0',
        'website': 'https://github.com/nicolaskruchten/pivottable',
        'register': {'alias': 'PivotTable', 'module': 'pivot.min'},
        'modules': [
            {'script': 'pivot.min.js', 'node_path': 'dist/', 'path': 'pivottable/%(version)s/', 'cdnjs': CDNJS_REPO}
        ]
    },

    # require.js
    'requirejs': {
        'unpkg': False,
        'website': 'https://requirejs.org/',
        'version': '2.3.6',
        'repository': 'https://github.com/requirejs/r.js',
        'modules': [
            {'script': 'require.min.js', 'path': 'require.js/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # topojson
    'topojson': {
        'website': 'https://requirejs.org/',
        'version': '3.0.2',
        'repository': 'https://github.com/requirejs/r.js',
        'register': {'alias': 'topojson', 'module': 'topojson.min'},
        'modules': [
            {'script': 'topojson.min.js', 'node_path': 'dist/', 'path': 'topojson/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # Pivot Table SubTotal
    'subtotal': {
        'req': [{'alias': 'pivottable'}],
        'node_folder': 'pivottable',
        'register': {'alias': 'subtotal', 'module': 'subtotal'},
        'website': 'http://nagarajanchinnasamy.com/subtotal/examples/',
        'repository': 'https://github.com/nagarajanchinnasamy/subtotal',
        'modules': [
            {'script': 'subtotal.js', 'node_path': 'dist/', 'version': '1.10.0', 'path': 'subtotal@%(version)s/dist/',
             'cdnjs': 'https://cdn.jsdelivr.net/npm'}
        ]},

    # Pivot Table pivot C3 renderer
    'pivot-c3': {
        'req': [
            {'alias': 'd3', 'version': '3.5.5'},
            {'alias': 'c3', 'version': '0.4.11'},
            {'alias': 'pivottable'}
        ],
        'website': 'https://github.com/nicolaskruchten/pivottable',
        'version': '2.23.0',
        'node_folder': 'pivottable',
        'modules': [
            {'script': 'c3_renderers.min.js', 'node_path': 'dist/', 'path': 'pivottable/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ]},

    # Pivot Table pivot plotly renderer
    'pivot-plotly': {
        'req': [
            {'alias': 'plotly.js'},
            {'alias': 'pivottable'}
        ],
        'node_folder': 'pivottable',
        'version': '2.23.0',
        'register': {'alias': 'pivot_plotly', 'module': 'plotly_renderers.min', 'npm': 'pivottable',
                     'npm_path': 'dist'},
        'website': 'https://github.com/nicolaskruchten/pivottable',
        'modules': [
            {'script': 'plotly_renderers.min.js', 'node_path': 'dist/', 'path': 'pivottable/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'plotly_renderers.min.js.map', 'node_path': 'dist/', 'path': 'pivottable/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ]
    },

    # Pivot Table pivot D3 renderer
    'pivot-d3': {
        'req': [
            {'alias': 'd3', 'version': '3.5.5'},
            {'alias': 'pivottable'}
        ],
        'node_folder': 'pivottable',
        'version': '2.23.0',
        'register': {'alias': 'pivot_d3', 'module': 'd3_renderers.min', 'npm': 'pivottable', 'npm_path': 'dist'},
        'website': 'https://github.com/nicolaskruchten/pivottable',
        'modules': [
            {'script': 'd3_renderers.min.js', 'node_path': 'dist/', 'path': 'pivottable/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ]},

    # Jquery package width CDN links
    'jquery': {
        'website': 'http://jquery.com/',
        "license": "MIT license",
        'repository': "https://github.com/jquery/jquery",
        'register': {'alias': '$', 'module': 'jquery.min', 'npm': 'jquery', 'npm_path': 'dist'},
        'version': '3.7.1',
        'modules': [
            {'script': 'jquery.min.js', 'node_path': 'dist/', 'path': 'jquery/%(version)s/', 'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'jquery.min.map', 'node_path': 'dist/', 'path': 'jquery/%(version)s/', 'cdnjs': CDNJS_REPO}
        ]
    },

    # Jquery vector Maps
    'jqvmap': {
        'req': [{'alias': 'jquery'}],
        "license": "MIT license",
        'website': 'https://www.10bestdesign.com/jqvmap/',
        'repository': "https://github.com/10bestdesign/jqvmap/",
        'register': {'alias': 'jqvmap', 'module': 'jquery.vmap.min', 'npm': 'jqvmap', "init_fnc": 'jQuery = $'},
        'version': '1.5.1',
        'modules': [
            {'script': 'jquery.vmap.min.js', 'node_path': 'dist/', 'path': 'jqvmap/%(version)s/', 'cdnjs': CDNJS_REPO},
        ],
    },

    # QUnit package width CDN links
    'qunit': {
        'website': 'https://qunitjs.com',
        "license": "MIT license",
        'version': '2.13.0',
        'modules': [
            {'script': 'qunit.js', 'node_path': 'qunit', 'path': 'qunit/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # Used to produce sparkline charts in a document and in Tabulator
    'jquery-sparkline': {
        'req': [{'alias': 'jquery'}],
        'version': '2.1.2',
        'website': 'https://omnipotent.net/jquery.sparkline/#s-about',
        'register': {'alias': 'sparkline', 'module': 'jquery.sparkline.min', 'npm': 'jquery-sparkline', 'npm_path': ''},
        'modules': [
            {'script': 'jquery.sparkline.min.js', 'path': 'jquery-sparklines/%(version)s/', 'cdnjs': CDNJS_REPO}
        ]
    },

    # Jquery UI package width CDN links
    'jqueryui': {
        'req': [{'alias': 'jquery'}, {'alias': '@popperjs/core'}],
        'website': 'http://jquery.com/',
        'repository': 'https://github.com/jquery/jqueryui.com',
        'version': '1.13.3',
        'register': {'alias': 'jqueryui', 'module': 'jquery-ui.min', 'npm': 'jquery-ui-dist', 'npm_path': ''},
        'modules': [
            {'script': 'jquery-ui.min.js', 'node_path': '', 'path': 'jqueryui/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # Jquery-bracket package width CDN links
    'jquery-bracket': {
        'website': 'http://www.aropupu.fi/bracket/',
        'version': '0.11.1',
        'req': [{'alias': 'jquery'}],
        'modules': [
            {'script': 'jquery.bracket.min.js', 'node_path': 'dist/', 'path': 'jquery-bracket/%(version)s/',
             'cdnjs': CDNJS_REPO}]},

    # Jquery timepicker width CDN links
    'timepicker': {
        'website': 'https://www.jonthornton.com/jquery-timepicker/',
        'version': '1.13.18',
        'register': {'alias': 'timepicker', 'module': 'jquery.timepicker.min'},
        'repository': 'https://github.com/jonthornton/jquery-timepicker',
        'req': [
            {'alias': 'jquery'},
            # {'alias': 'jqueryui'}
        ],
        'modules': [
            {'script': 'jquery.timepicker.min.js', 'path': 'jquery-timepicker/%(version)s/', 'cdnjs': CDNJS_REPO}
        ]},

    # To display a context menu when right click on an item
    'jquery-context-menu': {
        'unpkg': False,
        'website': 'http://swisnl.github.io/jQuery-contextMenu/demo.html',
        'register': {'alias': 'jQueryContext', 'module': 'jquery.contextMenu.min'},
        'req': [{'alias': 'jquery'}, {'alias': 'jqueryui'}],
        'modules': [
            {'script': 'jquery.contextMenu.min.js', 'version': '2.6.4', 'path': 'jquery-contextmenu/%(version)s/',
             'cdnjs': CDNJS_REPO}]},

    # To customize the scrollbar width CDN links
    # https://github.com/malihu/malihu-custom-scrollbar-plugin
    # http://manos.malihu.gr/repository/custom-scrollbar/demo/examples/complete_examples.html
    'jquery-scrollbar': {
        'unpkg': False,
        'website': 'http://manos.malihu.gr/jquery-custom-content-scroller/',
        'register': {'alias': 'jQueryScrollBar', 'module': 'jquery.mCustomScrollbar.concat.min'},
        'req': [{'alias': 'jquery'}],
        'modules': [
            {'script': 'jquery.mCustomScrollbar.concat.min.js', 'version': '3.1.5',
             'path': 'malihu-custom-scrollbar-plugin/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # Javascript packages for the PDF transformation width CDN links
    'pdfmake': {
        'website': '',
        'version': '0.1.70',
        'modules': [
            {'reqAlias': 'pdfmake', 'node_path': 'build/', 'script': 'pdfmake.min.js', 'path': 'pdfmake/%(version)s/',
             'cdnjs': CDNJS_REPO},
            {'reqAlias': 'vfs_fonts', 'node_path': 'build/', 'script': 'vfs_fonts.js', 'path': 'pdfmake/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'node_path': 'build/', 'script': 'pdfmake.min.js.map', 'path': 'pdfmake/%(version)s/',
             'cdnjs': CDNJS_REPO},
        ]
    },

    # The script allows you to take "screenshots" of webpages or parts of it, directly on the users browser.
    'html2canvas': {
        'version': '1.4.1',
        'website': 'https://html2canvas.hertzen.com/',
        'repository': 'https://github.com/niklasvh/html2canvas',
        'modules': [
            {'node_path': 'dist/', 'script': 'html2canvas.min.js', 'path': 'html2canvas/%(version)s/',
             'cdnjs': CDNJS_REPO},

        ]
    },

    # DOMPurify is a DOM-only, super-fast, uber-tolerant XSS sanitizer for HTML, MathML and SVG.
    'dompurify': {
        'website': 'https://github.com/cure53/DOMPurify',
        'repository': 'https://github.com/cure53/DOMPurify',
        'version': '2.2.6',
        'modules': [
            {'node_path': 'dist/', 'script': 'purify.min.js', 'path': 'dompurify/%(version)s/', 'cdnjs': CDNJS_REPO},
        ]
    },

    # Javascript packages for the PDF transformation width CDN links (Tabulator)
    'jspdf': {
        "unpkg": False,
        'req': [
            {'alias': 'dompurify'},
            {'alias': 'html2canvas'},
        ],
        'website': 'https://github.com/mrrio/jspdf',
        'repository': 'https://github.com/mrrio/jspdf',
        'version': '2.5.1',
        'modules': [
            {'reqAlias': 'jspdf', 'node_path': 'dist/', 'script': 'jspdf.umd.min.js', 'path': 'jspdf/%(version)s/',
             'cdnjs': CDNJS_REPO},
            {'script': 'polyfills.umd.min.js', 'path': 'jspdf/%(version)s/', 'cdnjs': CDNJS_REPO},
        ]},

    # Clipboard features width CDN links
    'clipboard': {
        'website': 'https://clipboardjs.com/',
        "license": "MIT license",
        "repository": "https://github.com/zenorocha/clipboard.js",
        'version': '2.0.11',
        'modules': [
            {'reqAlias': 'clipboard', 'script': 'clipboard.min.js', 'node_path': 'dist/',
             'path': 'clipboard.js/%(version)s/',
             'cdnjs': CDNJS_REPO}]},

    # Javascript dependencies for D3 and NVD2 components width CDN links
    'd3': {
        'website': 'https://d3js.org/',
        "license": "ISC license",
        "repository": "https://github.com/d3/d3",
        'v_prefix': 'v',
        'register': {'alias': 'd3', 'module': 'd3.min'},
        'version': '6.3.1',
        'modules': [
            {'reqAlias': 'd3', 'reqMod': 'ignore', 'node_path': 'dist/', 'script': 'd3.min.js', 'path': 'd3/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ]},

    # D3 Tips Package
    'd3-tip': {
        "license": "ISC license",
        'req': [{'alias': 'd3'}],
        'v_prefix': 'v',
        'version': '0.9.1',
        'modules': [
            {'script': 'd3-tip.min.js', 'node_path': 'dist/', 'path': 'd3-tip/%(version)s/', 'cdnjs': CDNJS_REPO}
        ]
    },

    # D3 axis
    'd3-axis': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-axis',
        'v_prefix': 'v',
        'version': '3.0.0',
        'register': {'variable': 'd3Axis', 'module': 'd3-axis.min'},
        'modules': [
            {'script': 'd3-axis.min.js', 'node_path': 'dist/', 'path': 'd3-axis@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 ease
    'd3-ease': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-ease',
        'v_prefix': 'v',
        'version': '3.0.1',
        'register': {'variable': 'd3Ease', 'module': 'd3-ease.min'},
        'modules': [
            {'script': 'd3-ease.min.js', 'node_path': 'dist/', 'path': 'd3-ease@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 DSV
    'd3-dsv': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-dsv',
        'v_prefix': 'v',
        'version': '3.0.1',
        'register': {'variable': 'd3Dsv', 'module': 'd3-dsv.min'},
        'modules': [
            {'script': 'd3-dsv.min.js', 'node_path': 'dist/', 'path': 'd3-dsv@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 dispatch
    'd3-dispatch': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-dispatch',
        'v_prefix': 'v',
        'version': '3.0.1',
        'register': {'variable': 'd3Dispatch', 'module': 'd3-dispatch.min'},
        'modules': [
            {'script': 'd3-dispatch.min.js', 'node_path': 'dist/', 'path': 'd3-dispatch@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 transition
    'd3-transition': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-interpolate',
        'v_prefix': 'v',
        'version': '3.0.1',
        'req': [
            {'alias': 'd3-dispatch'},
            {'alias': 'd3-selection'},
            {'alias': 'd3-color'},
            {'alias': 'd3-ease'},
            {'alias': 'd3-interpolate'},
            {'alias': 'd3-timer'},
        ],
        'register': {'variable': 'd3Transition', 'module': 'd3-transition.min'},
        'modules': [
            {'script': 'd3-transition.min.js', 'node_path': 'dist/', 'path': 'd3-transition@%(version)s/dist/', 'cdnjs': JSDELIVER}
        ]},

    # D3 Selection
    'd3-selection': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-selection',
        'v_prefix': 'v',
        'version': '3.0.0',
        'register': {'variable': 'd3Selection', 'module': 'd3-selection.min'},
        'modules': [
            {'script': 'd3-selection.min.js', 'node_path': 'dist/', 'path': 'd3-selection@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Interpolate
    'd3-interpolate': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-interpolate',
        'v_prefix': 'v',
        'version': '3.0.1',
        'register': {'variable': 'd3Interpolate', 'module': 'd3-interpolate.min'},
        'req': [
            {'alias': 'd3-color'}
        ],
        'modules': [
            {'script': 'd3-interpolate.min.js', 'node_path': 'dist/', 'path': 'd3-interpolate@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Time format
    'd3-time-format': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-time-format',
        'v_prefix': 'v',
        'version': '4.0.0',
        'register': {'variable': 'd3TimeFormat', 'module': 'd3-time-format.min'},
        'req': [
            {'alias': 'd3-time'}],
        'modules': [
            {'script': 'd3-time-format.min.js', 'node_path': 'dist/', 'path': 'd3-time-format@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Time
    'd3-time': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-time',
        'v_prefix': 'v',
        'version': '3.0.0',
        'register': {'variable': 'd3Time', 'module': 'd3-time.min'},
        'req': [
            {'alias': 'd3-array'},
        ],
        'modules': [
            {'script': 'd3-time.min.js', 'node_path': 'dist/', 'path': 'd3-time@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Format
    'd3-array': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-array',
        'v_prefix': 'v',
        'version': '3.0.1',
        'register': {'variable': 'd3Array', 'module': 'd3-array.min'},
        'modules': [
            {'script': 'd3-array.min.js', 'node_path': 'dist/', 'path': 'd3-array@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Format
    'd3-format': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-format',
        'v_prefix': 'v',
        'version': '3.0.1',
        'register': {'variable': 'd3Format', 'module': 'd3-format.min'},
        'modules': [
            {'script': 'd3-format.min.js', 'node_path': 'dist/', 'path': 'd3-format@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Timer
    'd3-timer': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-timer',
        'version': '3.0.1',
        'v_prefix': 'v',
        'register': {'variable': 'd3Timer', 'module': 'd3-timer.min'},
        'modules': [
            {'script': 'd3-timer.min.js', 'node_path': 'dist/', 'path': 'd3-timer@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 collection
    'd3-collection': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-collection',
        'version': '1.0.7',
        'v_prefix': 'v',
        'register': {'variable': 'd3Collection', 'module': 'd3-collection.min'},
        'modules': [
            {'script': 'd3-collection.min.js', 'node_path': 'dist/', 'path': 'd3-collection@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Scale
    'd3-scale': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-scale',
        'v_prefix': 'v',
        'version': '4.0.0',
        'register': {'variable': 'd3Scale', 'module': 'd3-scale.min'},
        'req': [
            {'alias': 'd3-array'},
            {'alias': 'd3-format'},
            {'alias': 'd3-collection'},
            {'alias': 'd3-interpolate'},
            {'alias': 'd3-time-format'}],
        'modules': [
            {'script': 'd3-scale.min.js', 'node_path': 'dist/', 'path': 'd3-scale@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 color module
    'd3-color': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-color',
        'v_prefix': 'v',
        'version': '3.0.1',
        'register': {'variable': 'd3Color', 'module': 'd3-color.min'},
        'modules': [
            {'script': 'd3-color.min.js', 'node_path': 'dist/', 'path': 'd3-color@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Brush module
    'd3-brush': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-brush',
        'v_prefix': 'v',
        'version': '3.0.0',
        'req': [
            {'alias': 'd3-interpolate'},
        ],
        'register': {'variable': 'd3Brush', 'module': 'd3-brush.min'},
        'modules': [
            {'script': 'd3-brush.min.js', 'node_path': 'dist/', 'path': 'd3-brush@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Brush module
    'd3-drag': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-drag',
        'v_prefix': 'v',
        'version': '3.0.0',
        'req': [
            {'alias': 'd3-selection'},
            {'alias': 'd3-dispatch'},
        ],
        'register': {'variable': 'd3Drag', 'module': 'd3-drag.min'},
        'modules': [
            {'script': 'd3-drag.min.js', 'node_path': 'dist/', 'path': 'd3-drag@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Shape module
    'd3-shape': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-shape',
        'v_prefix': 'v',
        'version': '3.0.1',
        'req': [
            {'alias': 'd3-path'},
        ],
        'register': {'variable': 'd3Shape', 'module': 'd3-shape.min'},
        'modules': [
            {'script': 'd3-shape.min.js', 'node_path': 'dist/', 'path': 'd3-shape@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Zoom module
    'd3-zoom': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-zoom',
        'v_prefix': 'v',
        'version': '3.0.0',
        'req': [
            {'alias': 'd3-interpolate'},
            {'alias': 'd3-selection'},
            {'alias': 'd3-transition'},
        ],
        'register': {'variable': 'd3Zoom', 'module': 'd3-zoom.min'},
        'modules': [
            {'script': 'd3-zoom.min.js', 'node_path': 'dist/', 'path': 'd3-zoom@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # D3 Path module
    'd3-path': {
        "license": "ISC license",
        'website': 'https://github.com/d3/d3-path',
        'v_prefix': 'v',
        'version': '3.0.1',
        'register': {'variable': 'd3Path', 'module': 'd3-path.min'},
        'modules': [
            {'script': 'd3-path.min.js', 'node_path': 'dist/', 'path': 'd3-path@%(version)s/dist/', 'cdnjs': JSDELIVER}]},

    # Javascript dependencies for Plotly width CDN links
    'plotly.js': {
        "license": "ISC license",
        'website': 'https://plot.ly/javascript/',
        'repository': 'https://github.com/plotly/plotly.js',
        'register': {'alias': 'Plotly', 'module': 'plotly.min', 'npm': 'plotly.js'},
        # 'version': '1.58.4',
        'version': '2.23.1',
        'modules': [
            {'script': 'plotly.min.js', 'node_path': 'dist/', 'path': 'plotly.js/%(version)s/', 'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'africa_50m.json', 'node_path': 'dist/topojson/', 'path': '/',
             'cdnjs': "https://www.hpcoders.com.au/ravel/plotly.js/dist/topojson"},
            {'script': 'europe_50m.json', 'node_path': 'dist/topojson/', 'path': '/',
             'cdnjs': "https://www.hpcoders.com.au/ravel/plotly.js/dist/topojson"},
        ]
    },

    # NVD3 Components width CDN links
    'nvd3': {
        'website': 'http://nvd3.org/',
        "license": "Apache License",
        'repository': 'https://github.com/novus/nvd3',
        'req': [{'alias': 'd3', 'version': '3.5.17'}],
        'register': {'alias': 'nvd3', 'module': 'nv.d3.min', 'npm': 'nvd3'},
        'version': '1.8.6',
        'modules': [
            {'script': 'nv.d3.min.js', 'node_path': 'build/', 'path': 'nvd3/%(version)s/', 'cdnjs': CDNJS_REPO}],
        'assets': [
            {'script': 'nv.d3.min.js.map', 'node_path': 'build/', 'path': 'nvd3/%(version)s/', 'cdnjs': CDNJS_REPO},
        ]
    },

    # C3 modules width CDN links
    'c3': {
        'website': 'https://c3js.org/',
        "license": "MIT license",
        'repository': 'https://github.com/c3js/c3',
        'req': [{'alias': 'd3', 'version': '5.0.0'}],
        'register': {'alias': 'c3', 'module': 'c3.min', 'npm': 'c3'},
        'version': '0.7.20',
        'modules': [
            {'script': 'c3.min.js', 'path': 'c3/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    'crossfilter': {
        'website': 'http://square.github.io/crossfilter/',
        "license": "Apache License",
        'repository': 'https://github.com/crossfilter/crossfilter',
        'version': '1.3.12',
        'register': {'alias': 'xfilter', 'module': 'crossfilter.min', 'npm': 'crossfilter'},
        'modules': [
            {'script': 'crossfilter.min.js', 'path': 'crossfilter/%(version)s/', 'cdnjs': CDNJS_REPO}
        ]
    },

    'svgjs': {
        "license": "MIT License",
        'version': '2.6.2',
        "repository": "https://github.com/svgdotjs/svg.js",
        'register': {'alias': 'svg', 'module': 'svg.min', 'npm': 'svgjs',  # "init_fnc": "window.SVG = svg"
                     },
        'modules': [
            {'script': 'svg.min.js', 'node_path': 'dist/', 'path': 'svgjs@%(version)s/dist/', 'cdnjs': JSDELIVER}
        ]
    },

    'apexcharts': {
        "license": "MIT license",
        'req_js': [  # depn only for requirejs
            {'alias': 'svgjs'},
        ],
        'website': 'https://apexcharts.com/',
        'repository': 'https://github.com/apexcharts/apexcharts.js',
        'version': '3.40.0',
        'register': {'alias': 'ApexCharts', 'module': 'apexcharts.min', 'npm': 'apexcharts'},
        'modules': [
            {'script': 'apexcharts.min.js', 'node_path': 'dist/', 'path': 'apexcharts@%(version)s/dist/', 'cdnjs': JSDELIVER}
        ],
    },

    # DC modules width CDN links
    'dc': {
        'website': 'https://dc-js.github.io/dc.js/examples/',
        "license": "Apache-2.0 license",
        'repository': 'https://github.com/dc-js/dc.js',
        'register': {'alias': 'dc', 'module': 'dc.min', 'npm': 'dc'},
        'req': [
            {'alias': 'd3'},
            {'alias': 'crossfilter'},
        ],
        'version': '4.2.7',
        'modules': [
            {'script': 'dc.min.js', 'node_path': 'dist/', 'path': 'dc/%(version)s/', 'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'dc.min.js.map', 'node_path': 'dist/', 'path': 'dc/%(version)s/', 'cdnjs': CDNJS_REPO}
        ]
    },

    # Vega Charts
    'vega': {
        'website': 'https://vega.github.io/vega-lite/',
        "license": "BSD-3-Clause license",
        'repository': 'https://observablehq.com/@uwdata/introduction-to-vega-lite',
        'register': {'alias': 'vega', 'module': 'vega.min'},
        'version': '5.25.0',
        'modules': [
            {'script': 'vega.min.js', 'node_path': 'build/', 'path': 'vega@%(version)s/build/', 'cdnjs': JSDELIVER},
        ]
    },

    # JS VEGA Utils
    "vega-tooltip": {
        "license": "BSD-3-Clause license",
        'req_js': [
            {"alias": "vega-util"}
        ],
        'website': 'https://github.com/vega/vega-util/',
        'register': {'variable': 'vegaTooltip', 'module': 'vega-tooltip.min'},
        'version': '0.32.0',
        'modules': [
            {'script': 'vega-tooltip.min.js', 'node_path': 'build/', 'path': 'vega-tooltip@%(version)s/build/', 'cdnjs': JSDELIVER},
        ]
    },
    # JS VEGA Utils
    "vega-util": {
        "license": "BSD-3-Clause license",
        'website': 'https://github.com/vega/vega-util/',
        'register': {'variable': 'vegaUtil', 'module': 'vega-util.min'},
        'version': '1.16.1',
        'modules': [
            {'script': 'vega-util.min.js','node_path': 'build/', 'path': 'vega-util@%(version)s/build/', 'cdnjs': JSDELIVER},
        ]
    },

    # JS VEGA Lite
    'vega-lite': {
        "license": "BSD-3-Clause license",
        'req': [
            {"alias": "vega"}
        ],
        'req_js': [
            {"alias": "vega-tooltip"},
            {"alias": "vega"},
        ],
        'website': 'https://vega.github.io/vega-lite/',
        'repository': 'https://observablehq.com/@uwdata/introduction-to-vega-lite',
        'register': {'variable': 'vegaLite', 'module': 'vega-lite.min'},
        'version': '5.9.2',
        'modules': [
            {'script': 'vega-lite.min.js','node_path': 'build/', 'path': 'vega-lite@%(version)s/build/', 'cdnjs': JSDELIVER},
        ]
    },

    # JS VEGA Embed
    'vega-embed': {
        "license": "BSD-3-Clause license",
        'req': [
            {"alias": "vega-lite"}
        ],
        'website': 'https://vega.github.io/vega-embed/',
        'repository': 'https://github.com/vega/vega-embed?utm_source=cdnjs&utm_medium=cdnjs_link&utm_campaign=cdnjs_library',
        'register': {'variable': 'vegaEmbed', 'module': 'vega-embed.min'},
        'version': '6.22.1',
        'modules': [
            {'script': 'vega-embed.min.js','node_path': 'build/', 'path': 'vega-embed@%(version)s/build/', 'cdnjs': JSDELIVER},
        ]
    },

    # billboard modules width CDN links
    'billboard.js': {
        "license": "MIT license",
        "repository": "https://github.com/naver/billboard.js",
        'website': 'https://naver.github.io/billboard.js/release/latest/doc/',
        'req': [
            {'alias': 'd3-axis'},
            {'alias': 'd3-color'},
            {'alias': 'd3-ease'},
            {'alias': 'd3-dsv'},
            {'alias': 'd3-brush'},
            {'alias': 'd3-drag'},
            {'alias': 'd3-selection'},
            {'alias': 'd3-scale'},
            {'alias': 'd3-shape'},
            {'alias': 'd3-time-format'},
            {'alias': 'd3-transition'},
            {'alias': 'd3-interpolate'},
            {'alias': 'd3-zoom'},
        ],
        'version': '3.8.1',
        'register': {'variable': 'bb', 'module': 'billboard.min', 'npm': 'billboard.js'},
        'modules': [
            {'script': 'billboard.min.js', 'node_path': 'dist/', 'path': 'billboard.js/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'billboard.min.js.map', 'node_path': 'dist/', 'path': 'billboard.js/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ]
    },

    # Rough Viz charts
    'rough-viz': {
        "license": "MIT license",
        'repository': 'https://github.com/jwilber/roughViz',
        'website': 'https://www.jwilber.me/roughviz/',
        'req': [{'alias': 'd3'}],
        'version': '1.0.6',
        'register': {'alias': 'roughViz', 'module': 'roughviz.min'},
        'modules': [
            {'script': 'roughviz.min.js', 'node_path': 'dist/', 'path': 'rough-viz@%(version)s/dist/', 'cdnjs': "https://unpkg.com"}
        ],
    },

    # Frappe-Charts module
    'frappe-charts': {
        "license": "MIT license",
        'repository': 'https://github.com/frappe/charts',
        'website': 'https://frappe.io/charts/docs',
        'version': '1.6.2',
        'register': {'alias': 'Frappe', 'module': 'frappe-charts.min.iife'},
        'modules': [
            {'script': 'frappe-charts.min.umd.min.js', 'node_path': 'dist/', 'path': 'frappe-charts/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ],

    },

    # MuzeJs module
    '@chartshq/muze': {
        'website': 'https://muzejs.org/',
        'version': '2.0.0',
        'register': {'alias': 'muze ', 'module': 'muze'},
        'modules': [
            {'script': 'muze.js', 'node_path': 'dist/', 'path': '@chartshq/muze@2.0.0/dist/',
             'cdnjs': "https://cdn.jsdelivr.net/npm"}
        ],

    },

    # ChartJs modules width CDN links
    'chart.js': {
        "license": "MIT license",
        'website': 'https://www.chartjs.org/',
        'version': '3.9.1',  # 2.9.4
        'v_prefix': 'v',
        'repository': 'https://github.com/chartjs/Chart.js',
        'register': {'alias': 'Chart', 'module': 'chart.umd', 'npm': 'chart.js', 'npm_path': 'dist',
                     "npm_imports": [
                         "import { Chart, registerables } from 'chart.js'",
                         "Chart.register(...registerables)"
                     ]},
        'modules': [
            {'script': 'chart.min.js', 'node_path': 'dist/', 'path': 'Chart.js/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # ChartJs stacked100 plugin modules width CDN links
    'chartjs-plugin-stacked100': {
        "license": "MIT license",
        "unpkg": False,
        'website': 'https://github.com/y-takey/chartjs-plugin-stacked100',
        'version': '1.3.0',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'index.min.js', 'path': 'chartjs-plugin-stacked100@%(version)s/build/',
             'cdnjs': "https://cdn.jsdelivr.net/npm"}]},

    # ChartJs Matrix plugin modules width CDN links
    'chartjs-chart-matrix': {
        "license": "MIT license",
        'website': 'https://github.com/kurkle/chartjs-chart-matrix',
        'version': '2.0.1',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'chartjs-chart-matrix.min.js', 'path': 'chartjs-chart-matrix@%(version)s/dist/',
             'node_path': 'dist/', 'cdnjs': "https://cdn.jsdelivr.net/npm"}]},

    # ChartJs Sankey plugin modules width CDN links
    'chartjs-chart-sankey': {
        "license": "MIT license",
        'website': 'https://github.com/kurkle/chartjs-chart-sankey',
        'version': '0.12.0',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'chartjs-chart-sankey.min.js', 'path': 'chartjs-chart-sankey@%(version)s/dist/',
             'node_path': 'dist/', 'cdnjs': "https://cdn.jsdelivr.net/npm"}]},

    # ChartJs WordCloud plugin modules width CDN links
    'chartjs-chart-wordcloud': {
        "license": "MIT license",
        'website': 'https://github.com/sgratzl/chartjs-chart-wordcloud',
        'version': '4.1.1',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'index.umd.min.js', 'path': 'chartjs-chart-wordcloud@%(version)s/build/',
             'node_path': 'build/', 'cdnjs': "https://cdn.jsdelivr.net/npm"}]},

    # ChartJs Venn plugin modules width CDN links
    'chartjs-chart-venn': {
        "license": "MIT license",
        'website': 'https://github.com/kurkle/chartjs-chart-sankey',
        'version': '4.1.1',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'index.umd.min.js', 'path': 'chartjs-chart-venn@%(version)s/build/',
             'node_path': 'build/', 'cdnjs': "https://cdn.jsdelivr.net/npm"}]},

    # ChartJs Crosshair plugin modules width CDN links
    'chartjs-plugin-dragdata': {
        "license": "MIT license",
        'website': 'https://www.chartjs.org/',
        'version': 'latest',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'chartjs-plugin-dragdata.min.js', 'path': 'chartjs-plugin-dragdata@%(version)s/dist/',
             'node_path': 'dist/', 'cdnjs': "https://cdn.jsdelivr.net/npm"}]},

    # ChartJs Treemap
    'chartjs-chart-treemap': {
        "license": "MIT license",
        'website': 'https://github.com/kurkle/chartjs-chart-treemap',
        'version': '2.3.0',  # 2.0.2
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'chartjs-chart-treemap.min.js', 'path': 'chartjs-chart-treemap@%(version)s/dist/',
             'node_path': 'dist/', 'cdnjs': "https://cdn.jsdelivr.net/npm"}]},

    # ChartJs Crosshair plugin modules width CDN links
    'chartjs-plugin-annotation': {
        "license": "MIT license",
        'website': 'https://www.chartjs.org/',
        'version': '2.1.2',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'chartjs-plugin-annotation.min.js', 'path': 'chartjs-plugin-annotation/%(version)s/',
             'node_path': 'dist/', 'cdnjs': CDNJS_REPO}]},

    # ChartJs deferred plugin modules width CDN links
    'chartjs-plugin-deferred': {
        "license": "MIT license",
        'version': '2.0.0',
        'website': 'https://chartjs-plugin-deferred.netlify.app/guide/',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'chartjs-plugin-deferred.min.js', 'path': 'chartjs-plugin-deferred@%(version)s/dist/',
             'node_path': 'dist/', 'cdnjs': 'https://cdn.jsdelivr.net/npm'}]},

    # ChartJs hierarchical plugin modules width CDN links
    'chartjs-plugin-hierarchical': {
        "license": "MIT license",
        'version': '4.1.1',
        'website': 'https://github.com/sgratzl/chartjs-plugin-hierarchical',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'index.umd.min.js', 'path': 'chartjs-plugin-hierarchical@%(version)s/build/',
             'node_path': 'build/', 'cdnjs': 'https://cdn.jsdelivr.net/npm'}]},

    # ChartJs datalabels plugin modules width CDN links
    'chartjs-plugin-datalabels': {
        "license": "MIT license",
        'version': '2.2.0',
        'website': 'https://chartjs-plugin-datalabels.netlify.app/',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'chartjs-plugin-datalabels.min.js', 'path': 'chartjs-plugin-datalabels@%(version)s/dist/',
             'node_path': 'dist/', 'cdnjs': 'https://cdn.jsdelivr.net/npm'}]},

    # ChartJs Labels plugin modules width CDN links
    'chartjs-plugin-labels': {
        "license": "MIT license",
        'version': '1.1.0',
        'website': 'https://github.com/emn178/chartjs-plugin-labels',
        'req': [{'alias': 'chart.js'}],
        'v_prefix': 'v',
        'modules': [
            {'script': 'chartjs-plugin-labels.js', 'path': '/',
             'node_path': 'src/', 'cdnjs': "https://emn178.github.io/chartjs-plugin-labels/src"}
        ]},

    # ChartJs Crosshair plugin modules width CDN links
    'chartjs-plugin-crosshair': {
        "license": "MIT license",
        'version': '1.2.0',
        'website': 'https://www.chartjs.org/',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'chartjs-plugin-crosshair.min.js', 'path': '',
             'node_path': 'dist/', 'cdnjs': "https://chartjs-plugin-crosshair.netlify.app/"}]},

    # ChartJs Zoom plugin modules width CDN links
    'chartjs-plugin-zoom': {
        "license": "MIT license",
        'website': 'https://www.chartjs.org/',
        'version': '2.0.0',
        'req': [{'alias': 'chart.js'}, {"alias": 'hammer'}],
        'modules': [
            {'script': 'chartjs-plugin-zoom.min.js', 'node_path': 'dist/',
             'path': 'chartjs-plugin-zoom/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # ChartJs addon to add some Geo charts
    'chartjs-chart-geo': {
        "license": "MIT license",
        'version': '4.1.2',  # '3.1.0'
        'website': 'https://github.com/sgratzl/chartjs-chart-geo',
        'req': [{'alias': 'chart.js'}],
        'modules': [
            {'script': 'index.umd.min.js', 'path': 'chartjs-chart-geo@%(version)s/build/',
             'node_path': 'build/', 'cdnjs': JSDELIVER}
        ]},

    # For ChartJs Zoom to get the gesture details.
    'hammer': {
        "license": "MIT license",
        "unpkg": False,
        'version': '2.0.8',
        "repository": "https://github.com/hammerjs/hammer.js",
        'website': 'http://hammerjs.github.io/',
        'modules': [
            {'script': 'hammer.min.js', 'path': 'hammer.js/%(version)s/', 'cdnjs': CDNJS_REPO}
        ],
    },

    # Cannot add properly the dependency in this one as my algorithm does not work for shared dependencies ....
    # 'meter': {'req': ['d3'], 'modules': ['d3.meter.js'], 'website': '', 'version': '', "status": 'deprecated'},

    # Popper tooltips used by bootstrap in the dropdown components
    '@popperjs/core': {
        "license": "MIT license",
        'req': [{'alias': 'jquery'}],
        'v_prefix': 'v',
        'version': '2.11.8',
        'repository': 'https://github.com/popperjs/popper-core',
        'website': 'https://github.com/popperjs/popper-core',
        'modules': [
            {'reqAlias': 'popper', 'script': 'popper.min.js', 'node_path': 'dist/umd/',
             'path': 'popper.js/%(version)s/umd/',
             'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'popper.min.js.map', 'node_path': 'dist/umd/', 'path': 'popper.js/%(version)s/umd/',
             'cdnjs': CDNJS_REPO}
        ]
    },

    # Javascript module for the simple select component. issue with Bootstrap 4 width CDN links
    'bootstrap-select': {
        "license": "MIT license",
        'website': 'http://silviomoreto.github.io/bootstrap-select/',
        'version': '1.13.18',
        'repository': 'https://github.com/snapappointments/bootstrap-select',
        'register': {'alias': 'selectBs', 'module': 'bootstrap-select.min', 'npm_path': 'dist/js'},
        'req': [
            {'alias': '@popperjs/core', 'version': '1.14.6'},  # Cannot be upgraded bug with bootstrap select
            {'alias': 'jquery'},
            {'alias': 'bootstrap'}],
        'modules': [
            {'reqAlias': 'selectBs', 'script': 'bootstrap-select.min.js', 'node_path': 'dist/js/',
             'path': 'bootstrap-select/%(version)s/js/', 'cdnjs': CDNJS_REPO},
        ],
        'assets': [
            {'script': 'bootstrap-select.min.js.map', 'node_path': 'dist/js/',
             'path': 'bootstrap-select/%(version)s/js/',
             'cdnjs': CDNJS_REPO},
        ]
    },

    'ajax-bootstrap-select': {
        "license": "MIT license",
        'version': '1.4.5',
        'website': 'https://github.com/truckingsim/Ajax-Bootstrap-Select',
        'register': {'alias': 'selectAjax', 'module': 'ajax-bootstrap-select.min', 'npm_path': 'dist/js'},
        'req': [{"alias": 'bootstrap-select'}
                ],
        'modules': [
            {'script': 'ajax-bootstrap-select.min.js', 'node_path': 'dist/js/',
             'path': 'ajax-bootstrap-select/%(version)s/js/', 'cdnjs': CDNJS_REPO}
        ]
    },

    # https://cdnjs.cloudflare.com/ajax/libs/ajax-bootstrap-select/1.4.5/js/ajax-bootstrap-select.min.js
    # javascript package for the Venn chart
    # 'venn': {'req': ['d3'], 'modules': ['venn.js'], 'website': '', 'version': '',},

    # Vis Javascript Packages
    'vis': {
        "license": "Apache-2.0, MIT licenses found",
        'register': {'alias': 'vis', 'module': 'vis.min', 'npm': 'vis', 'npm_path': 'dist'},
        'website': 'http://visjs.org/',
        'version': '4.21.0',
        "repository": "https://github.com/visjs/vis-graph3d",
        'modules': [
            {'script': 'vis.min.js', 'node_path': 'dist/', 'path': 'vis/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # Vis Timeline style with CDN Links
    'vis-timeline': {
        "license": "Apache-2.0, MIT licenses found",
        'register': {'alias': 'vis-timeline', 'npm': 'vis-timeline', 'npm_path': 'dist'},
        'website': 'http://visjs.org/',
        'version': '7.3.7',
        'modules': [
            {'script': 'vis-timeline-graph2d.min.js', 'node_path': 'dist/', 'path': 'vis-timeline/%(version)s/',
             'cdnjs': CDNJS_REPO}]},

    # Mapbox GL
    'mapbox-gl': {
        'register': {'alias': 'mapbox-gl', 'npm_path': 'dist'},
        "license": "Copyright © 2021 - 2023 Mapbox, Inc. All rights reserved",
        "repository": "https://github.com/mapbox/mapbox-gl-js",
        "pricing": "https://www.mapbox.com/pricing",
        'website': 'https://www.mapbox.com/',
        'version': '2.14.1',
        'modules': [
            {'script': 'mapbox-gl.js', 'node_path': 'dist/', 'path': 'mapbox-gl/%(version)s/', 'cdnjs': CDNJS_REPO}]
    },

    # Javascript package to display mathematical formulas
    # https://codingislove.com/display-maths-formulas-webpage/
    # https://github.com/mathjax/mathjax
    'mathjax': {
        'website': 'https://www.mathjax.org/',
        "license": "Apache-2.0 license",
        'version': '3.2.2',
        'repository': 'https://github.com/mathjax/MathJax',
        'package': {'zip': 'https://github.com/mathjax/MathJax/archive/%(version)s.zip', 'root': 'MathJax-%(version)s',
                    'folder': 'mathjax'},
        'modules': [
            {'script': 'tex-mml-chtml.js', "node_path": "es5/", 'path': 'mathjax/%(version)s/es5/', 'cdnjs': CDNJS_REPO}],
    },

    # Socket IO
    'socket.io': {
        'version': '3.0.4',
        "license": "MIT license",
        'website': 'https://github.com/socketio/socket.io',
        'repository': 'https://github.com/socketio/socket.io',
        'req': [{'alias': 'jquery'}],
        'modules': [
            {'script': 'socket.io.min.js', 'node_path': 'client-dist/', 'path': 'socket.io/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'socket.io.min.js.map', 'node_path': 'client-dist/', 'path': 'socket.io/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ]
    },

    # Code mirror
    'codemirror': {
        'version': '6.65.7',
        "license": "MIT License",
        "repository": "https://github.com/codemirror/dev/",
        'website': 'https://codemirror.net/',
        'modules': [
            {'script': 'codemirror.js', 'node_path': 'lib/', 'path': 'codemirror/%(version)s/', 'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'python.js', 'node_path': 'mode/python/', 'path': 'codemirror/%(version)s/mode/python/',
             'cdnjs': CDNJS_REPO},
            {'script': 'r.js', 'node_path': 'mode/r/', 'path': 'codemirror/%(version)s/mode/r/', 'cdnjs': CDNJS_REPO},
            {'script': 'css.js', 'node_path': 'mode/css/', 'path': 'codemirror/%(version)s/mode/css/',
             'cdnjs': CDNJS_REPO},
            {'script': 'javascript.js', 'node_path': 'mode/javascript/',
             'path': 'codemirror/%(version)s/mode/javascript/',
             'cdnjs': CDNJS_REPO},
            {'script': 'markdown.js', 'node_path': 'mode/markdown/', 'path': 'codemirror/%(version)s/mode/markdown/',
             'cdnjs': CDNJS_REPO},
            {'script': 'php.js', 'node_path': 'mode/php/', 'path': 'codemirror/%(version)s/mode/php/',
             'cdnjs': CDNJS_REPO},
            {'script': 'ruby.js', 'node_path': 'mode/ruby/', 'path': 'codemirror/%(version)s/mode/ruby/',
             'cdnjs': CDNJS_REPO},
        ]
    },

    'codemirror-search': {
        "license": "MIT License",
        'req': [
            {'alias': 'codemirror'}
        ],
        'node_folder': 'codemirror',
        'website': 'https://codemirror.net/demo/search.html',
        'modules': [
            {'script': 'searchcursor.js', 'node_path': 'addon/search/', 'path': 'codemirror/%(version)s/addon/search/',
             'cdnjs': CDNJS_REPO},
            {'script': 'search.js', 'node_path': 'addon/search/', 'path': 'codemirror/%(version)s/addon/search/',
             'cdnjs': CDNJS_REPO},
            {'script': 'matchesonscrollbar.js', 'node_path': 'addon/search/',
             'path': 'codemirror/%(version)s/addon/search/', 'cdnjs': CDNJS_REPO},
            {'script': 'jump-to-line.js', 'node_path': 'addon/search/', 'path': 'codemirror/%(version)s/addon/search/',
             'cdnjs': CDNJS_REPO},
            {'script': 'dialog.js', 'node_path': 'addon/dialog/', 'path': 'codemirror/%(version)s/addon/dialog/',
             'cdnjs': CDNJS_REPO}
        ]},

    'codemirror-placeholder': {
        "license": "MIT License",
        'req': [
            {'alias': 'codemirror'}
        ],
        'node_folder': 'codemirror',
        'website': 'https://codemirror.net/demo/placeholder.html',
        'modules': [
            {'script': 'placeholder.js', 'node_path': 'addon/dialog/', 'path': 'codemirror/%(version)s/addon/display/',
             'cdnjs': CDNJS_REPO}
        ]},

    'codemirror-trailingspace': {
        "license": "MIT License",
        'req': [
            {'alias': 'codemirror'}
        ],
        'node_folder': 'codemirror',
        'website': 'https://codemirror.net/demo/trailingspace.html',
        'modules': [
            {'script': 'trailingspace.js', 'node_path': 'addon/edit/', 'path': 'codemirror/%(version)s/addon/edit/',
             'cdnjs': CDNJS_REPO}
        ]},

    'codemirror-fullscreen': {
        "license": "MIT License",
        'req': [
            {'alias': 'codemirror'}
        ],
        'node_folder': 'codemirror',
        'website': 'https://codemirror.net/demo/trailingspace.html',
        'modules': [
            {'script': 'fullscreen.js', 'node_path': 'addon/display/', 'path': 'codemirror/%(version)s/addon/display/',
             'cdnjs': CDNJS_REPO}
        ]},

    'codemirror-highlighter': {
        "license": "MIT License",
        'req': [
            {'alias': 'codemirror'}
        ],
        'node_folder': 'codemirror',
        'website': 'https://codemirror.net/demo/matchhighlighter.html',
        'modules': [
            {'script': 'annotatescrollbar.js', 'node_path': 'addon/scroll/',
             'path': 'codemirror/%(version)s/addon/scroll/',
             'cdnjs': CDNJS_REPO},
            {'script': 'matchesonscrollbar.js', 'node_path': 'addon/search/',
             'path': 'codemirror/%(version)s/addon/search/', 'cdnjs': CDNJS_REPO},
            {'script': 'searchcursor.js', 'node_path': 'addon/search/', 'path': 'codemirror/%(version)s/addon/search/',
             'cdnjs': CDNJS_REPO},
            {'script': 'match-highlighter.js', 'node_path': 'addon/search/',
             'path': 'codemirror/%(version)s/addon/search/',
             'cdnjs': CDNJS_REPO},
        ]},

    'codemirror-hint': {
        "license": "MIT License",
        'req': [
            {'alias': 'codemirror'}
        ],
        'node_folder': 'codemirror',
        'website': 'https://codemirror.net/demo/complete.html',
        'modules': [
            {'script': 'show-hint.js', 'node_path': 'addon/hint/', 'path': 'codemirror/%(version)s/addon/hint/',
             'cdnjs': CDNJS_REPO},
        ]},

    'codemirror-panel': {
        "license": "MIT License",
        'req': [
            {'alias': 'codemirror'}
        ],
        'node_folder': 'codemirror',
        'website': 'https://codemirror.net/demo/panel.html#',
        'modules': [
            {'script': 'panel.js', 'node_path': 'addon/display/', 'path': 'codemirror/%(version)s/addon/display/',
             'cdnjs': CDNJS_REPO},
        ]},

    'codemirror-fold': {
        "license": "MIT License",
        'req': [
            {'alias': 'codemirror'}
        ],
        'node_folder': 'codemirror',
        'website': 'https://codemirror.net/demo/folding.html',
        'modules': [
            {'script': 'foldcode.js', 'node_path': 'addon/fold/', 'path': 'codemirror/%(version)s/addon/fold/',
             'cdnjs': CDNJS_REPO},
            {'script': 'foldgutter.js', 'node_path': 'addon/fold/', 'path': 'codemirror/%(version)s/addon/fold/',
             'cdnjs': CDNJS_REPO},
            {'script': 'brace-fold.js', 'node_path': 'addon/fold/', 'path': 'codemirror/%(version)s/addon/fold/',
             'cdnjs': CDNJS_REPO},
            {'script': 'xml-fold.js', 'node_path': 'addon/fold/', 'path': 'codemirror/%(version)s/addon/fold/',
             'cdnjs': CDNJS_REPO},
            {'script': 'indent-fold.js', 'node_path': 'addon/fold/', 'path': 'codemirror/%(version)s/addon/fold/',
             'cdnjs': CDNJS_REPO},
            {'script': 'markdown-fold.js', 'node_path': 'addon/fold/', 'path': 'codemirror/%(version)s/addon/fold/',
             'cdnjs': CDNJS_REPO},
            {'script': 'comment-fold.js', 'node_path': 'addon/fold/', 'path': 'codemirror/%(version)s/addon/fold/',
             'cdnjs': CDNJS_REPO},
        ]},

    # highlight
    'highlight.js': {
        "license": "BSD-3-Clause license",
        'version': '11.9.0',
        'website': 'https://highlightjs.org/',
        'repository': 'https://github.com/highlightjs/highlight.js',
        # 'register': {'alias': 'hljs', 'npm': 'highlight.js', 'npm_path': 'lib/core'},
        'modules': [
            {'script': 'highlight.min.js', 'node_path': 'lib/', 'path': 'highlight.js/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ]},

    # Leaflet
    'leaflet': {
        'version': '1.9.4',
        "license": "BSD-2-Clause license",
        'website': 'https://leafletjs.com/',
        'repository': 'https://github.com/Leaflet/Leaflet',
        'register': {'alias': 'L', 'module': 'leaflet', 'npm': 'leaflet'},
        'modules': [
            {'script': 'leaflet.js', 'node_path': 'dist/', 'path': 'leaflet/%(version)s/', 'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'leaflet.js.map', 'node_path': 'dist/', 'path': 'leaflet/%(version)s/', 'cdnjs': CDNJS_REPO}
        ]
    },

    # showdown
    'showdown': {
        'version': '2.1.0',
        "license": "MIT license",
        'website': 'https://github.com/showdownjs/showdown',
        'repository': 'https://github.com/showdownjs/showdown',
        'register': {'alias': 'showdown', 'module': 'showdown.min', 'npm': 'showdown', 'npm_path': 'dist'},
        'modules': [
            {'script': 'showdown.min.js', 'node_path': 'dist/', 'path': 'showdown/%(version)s/', 'cdnjs': CDNJS_REPO}
        ]
    },

    # Sortable framework
    'sortablejs': {
        'register': {'alias': 'Sortable', 'npm': 'sortablejs'},
        "license": "MIT license",
        'repository': 'https://github.com/SortableJS/Sortable',
        'version': '1.15.1',
        'modules': [
            {'script': 'Sortable.min.js', 'path': 'Sortable/%(version)s/', 'cdnjs': CDNJS_REPO},
        ],
        'website': 'https://github.com/SortableJS/Sortable'},

    'google-platform': {
        "unpkg": False,
        'website': 'https://apis.google.com/',
        'req': [],
        'modules': [
            {'script': 'platform.js', 'version': '', 'path': 'js/', 'cdnjs': 'https://apis.google.com'}]},

    'facebook-sdk': {
        "unpkg": False,
        'website': 'https://connect.facebook.net',
        'req': [],
        'version': '0.3.3',
        'modules': [
            {'script': 'sdk.js', 'path': 'en-GB/', 'cdnjs': 'https://connect.facebook.net'}]},

    # Tiny slider for carousels
    'tiny-slider': {
        "license": "MIT license",
        'version': '2.9.3',
        'register': {'alias': 'tns', 'npm': 'tiny-slider'},
        'modules': [
            {'script': 'tiny-slider.js', 'node_path': 'dist/min/', 'path': 'tiny-slider/%(version)s/min/',
             'cdnjs': CDNJS_REPO},
        ],
        'website': 'https://github.com/ganlanyuan/tiny-slider',
    },

    # Date picker - tiny size, no dependencies
    '@easepick/bundle': {
            "unpkg": False,
            'version': "1.2.1",
            'modules': [
                {'script': 'index.umd.min.js', 'node_path': 'dist/',
                 'path': '@easepick/bundle@%(version)s/dist/', 'cdnjs': JSDELIVER},
            ],
            'website': 'https://easepick.com/'
        },

    # A lightweight and elegant JavaScript color picker. Written in vanilla ES6, no dependencies. Accessible.
    '@melloware/coloris': {
            "unpkg": False,
            'version': "0.24.0",
            'modules': [
                {'script': 'coloris.min.js',
                 'path': '@melloware/coloris@%(version)s/dist/umd/', 'cdnjs': JSDELIVER},
            ],
            'website': 'https://coloris.js.org/'
        },

    # JavaScript mangler and compressor toolkit
    'terser': {
            "unpkg": False,
            'version': "5.34.1",
            'modules': [
                {'script': 'bundle.min.js', "node_path": "dist/", 'path': 'terser@%(version)s/dist/', 'cdnjs': JSDELIVER},
            ],
            'website': 'https://terser.org/'
    }
}

CSS_IMPORTS = {
    'jqueryui': {
        'modules': [
            {'script': 'jquery-ui.min.css', 'node_path': '', 'path': 'jqueryui/%(version)s/themes/base/', 'cdnjs': CDNJS_REPO},
        ]
    },

    'chartist': {
        'modules': [
            {'script': 'chartist.min.css', 'path': 'chartist/%(version)s/', 'cdnjs': CDNJS_REPO},
        ]
    },

    '@chartshq/muze': {
        "repository": "https://github.com/chartshq/muze",
        'modules': [
            {'script': 'muze.css', 'path': '@chartshq/muze@%(version)s/dist/',
             'cdnjs': "https://cdn.jsdelivr.net/npm"}]},

    # Chart.css
    'charts.css': {
        'website': 'https://github.com/ChartsCSS/charts.css#readme',
        "license": "MIT license",
        'version': "1.0.0",
        'modules': [
            {'script': 'charts.min.css', 'path': 'charts.css/dist/', 'cdnjs': "https://cdn.jsdelivr.net/npm/"}
        ],
    },

    # The Apexcharts CDN links
    'apexcharts': {
        'modules': [
            {'script': 'apexcharts.css', 'node_path': 'dist/', 'path': 'apexcharts/%(version)s/',
             'cdnjs': CDNJS_REPO}]},

    # The Quill CDN links
    'quill': {
        'modules': [
            #{'script': 'quill.core.min.css', 'node_path': 'dist/', 'path': 'quill/%(version)s/', 'cdnjs': CDNJS_REPO},
            {'script': 'quill.snow.min.css', 'node_path': 'dist/', 'path': 'quill/%(version)s/', 'cdnjs': CDNJS_REPO},
        ]},

    # fluent ui icons
    'office-ui-fabric-core': {
        "license": "MIT License",
        "repository": "https://github.com/OfficeDev/office-ui-fabric-core",
        'register': {'alias': 'fluentui', 'module': 'fluentui', 'npm_path': 'dist/css'},
        'modules': [{'script': 'fabric.min.css', 'version': '11.0.0', 'path': 'office-ui-fabric-core/%(version)s/css/',
                     'cdnjs': "https://static2.sharepointonline.com/files/fabric"}],
        'website': 'https://developer.microsoft.com/en-us/fluentui#/styles/web/icons'},

    # fluent ui icons
    'office-ui-fabric-react': {
        "license": "MIT License",
        'register': {'alias': 'fluentui', 'module': 'fluentui', 'npm_path': 'dist/css'},
        'modules': [{'script': 'fabric.min.css', 'version': '11.0.0', 'path': 'office-ui-fabric-core/%(version)s/css/',
                     'cdnjs': "https://static2.sharepointonline.com/files/fabric"}],
        'website': 'https://developer.microsoft.com/en-us/fluentui#/styles/web/icons'},

    # QUnit package width CDN links
    'qunit': {
        'modules': [
            {'script': 'qunit.css', 'node_path': 'qunit', 'path': 'qunit/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # jqvmap
    'jqvmap': {
        'modules': [
            {'script': 'jqvmap.min.css', 'node_path': 'dist', 'path': 'jqvmap/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # Jquery-bracket package width CDN links
    'jquery-bracket': {
        'modules': [
            {'script': 'jquery.bracket.min.css', 'node_path': 'dist/', 'path': 'jquery-bracket/%(version)s/',
             'cdnjs': CDNJS_REPO}]},

    # To display a context menu when right click on an item width CDN links
    # http://swisnl.github.io/jQuery-contextMenu/demo.html#jquery-context-menu-demo-gallery
    'jquery-context-menu': {
        'website': 'https://github.com/swisnl/jQuery-contextMenu/blob/master/dist/jquery.contextMenu.min.css.map',
        'req': [{'alias': 'jqueryui'}],
        'modules': [
            {'script': 'jquery.contextMenu.min.css', 'version': '2.6.4', 'path': 'jquery-contextmenu/%(version)s/',
             'cdnjs': CDNJS_REPO}]},

    # Jquery timepicker width CDN links
    'timepicker': {
        'modules': [
            {'script': 'jquery.timepicker.min.css', 'path': 'jquery-timepicker/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # To customize the scrollbar width CDN links
    'jquery-scrollbar': {
        'website': 'http://manos.malihu.gr/jquery-custom-content-scroller/',
        'req': [{'alias': 'jqueryui'}],
        'modules': [
            {'script': 'jquery.mCustomScrollbar.min.css', 'version': '3.1.5',
             'path': 'malihu-custom-scrollbar-plugin/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # Tabulator definition
    'tabulator-tables': {
        'modules': [
            {'script': 'tabulator.min.css', 'node_path': 'dist/css/', 'path': 'tabulator/%(version)s/css/',
             'cdnjs': CDNJS_REPO}
        ]
    },

    'datatables': {
        'website': 'https://datatables.net/',
        'req': [{'alias': 'bootstrap'}],
        'modules': [
            {'script': 'jquery.dataTables.min.css', 'version': '1.10.19', 'path': '%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}
        ]},

    # Datatable Buttons
    'datatables-buttons': {
        'website': 'https://datatables.net/extensions/buttons/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'buttons.dataTables.min.css', 'version': '1.6.1', 'path': 'buttons/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable Select
    'datatables-select': {
        'website': 'https://datatables.net/extensions/select/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'select.dataTables.min.css', 'version': '1.3.1', 'path': 'select/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable Scroller
    'datatables-scroller': {
        'website': 'https://datatables.net/extensions/scroller/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'scroller.dataTables.min.css', 'version': '2.0.1', 'path': 'scroller/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable SearchPanes
    'datatables-searchPanes': {
        'website': 'https://datatables.net/extensions/searchpanes/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'searchPanes.dataTables.min.css', 'version': '1.0.1', 'path': 'searchpanes/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable Responsive
    'datatables-responsive': {
        'website': 'https://datatables.net/extensions/responsive/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'responsive.dataTables.min.css', 'version': '2.2.3', 'path': 'responsive/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable KeyTable
    'datatables-keytable': {
        'website': 'https://datatables.net/extensions/keytable/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'keyTable.dataTables.min.css', 'version': '2.5.1', 'path': 'keytable/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable autoFill
    'datatables-autoFill': {
        'website': 'https://datatables.net/extensions/autofill/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'autoFill.dataTables.min.css', 'version': '2.1.0', 'path': 'autofill/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable group row
    'datatables-row-group': {
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'rowGroup.dataTables.min.css', 'version': '1.1.1', 'path': 'rowgroup/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable fixed column
    'datatables-fixed-columns': {
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'fixedColumns.bootstrap4.min.css', 'version': '3.2.2', 'path': 'fixedcolumns/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable fixed header
    'datatables-fixed-header': {
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'fixedHeader.bootstrap4.min.css', 'version': '3.1.3', 'path': 'fixedheader/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable export module
    'datatables-export': {
        'website': 'https://datatables.net/',
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'buttons.bootstrap4.min.css', 'version': '1.5.2', 'path': 'buttons/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Datatable column ordering
    'datatables-col-order': {
        'req': [{'alias': 'datatables'}],
        'modules': [
            {'script': 'colReorder.bootstrap4.min.css', 'version': '1.5.1', 'path': 'colreorder/%(version)s/css/',
             'cdnjs': 'https://cdn.datatables.net'}]},

    # Bootstrap style width CDN links
    'bootstrap': {
        'modules': [
            {'script': 'bootstrap.min.css', 'node_path': 'dist/css/', 'path': 'twitter-bootstrap/%(version)s/css/',
             'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'bootstrap.min.css.map', 'node_path': 'dist/css/', 'path': 'twitter-bootstrap/%(version)s/css/',
             'cdnjs': CDNJS_REPO}
        ]
    },

    # Font awesome style width CDN links
    'font-awesome': {
        'register': {'alias': 'fontawesome', 'module': 'fontawesome', 'npm': '@fortawesome/fontawesome-free',
                     'npm_path': 'css'},
        'website': 'https://fontawesome.com/',
        'package': {'zip': 'https://use.fontawesome.com/releases/v%(version)s/fontawesome-free-%(version)s-web.zip',
                    'root': 'fontawesome-free-%(version)s-web', 'folder': 'releases', 'path': 'v%(version)s'},
        'modules': [
            {'script': 'all.css', 'version': '5.13.1', 'node_path': 'fontawesome-free/css/', 'path': 'releases/v%(version)s/css/',
             'cdnjs': 'https://use.fontawesome.com'}],
        'assets': [
            {'script': 'fa-brands-400.woff2', 'version': '5.13.1', 'path': 'releases/v%(version)s/webfonts/',
             'cdnjs': 'https://use.fontawesome.com', 'npm_path': 'webfonts'},
            {'script': 'fa-regular-400.woff2', 'version': '5.13.1', 'path': 'releases/v%(version)s/webfonts/',
             'cdnjs': 'https://use.fontawesome.com', 'npm_path': 'webfonts'},
            {'script': 'fa-solid-900.woff2', 'version': '5.13.1', 'path': 'releases/v%(version)s/webfonts/',
             'cdnjs': 'https://use.fontawesome.com', 'npm_path': 'webfonts'},
        ]
    },

    # NVD3 Components width CDN links
    'nvd3': {
        'modules': [
            {'script': 'nv.d3.min.css', 'node_path': 'build/', 'path': 'nvd3/%(version)s/', 'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'nv.d3.min.css.map', 'node_path': 'build/', 'path': 'nvd3/%(version)s/', 'cdnjs': CDNJS_REPO}]
    },

    # C3 modules width CDN links
    'c3': {
        'modules': [
            {'script': 'c3.min.css', 'path': 'c3/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # DC modules width CDN links
    'dc': {
        'modules': [
            {'script': 'dc.css', 'node_path': 'dist/style', 'path': 'dc/%(version)s/style/', 'cdnjs': CDNJS_REPO}]},

    # billboard modules width CDN links
    'billboard.js': {
        'modules': [
            {'script': 'billboard.min.css', 'node_path': 'dist/', 'path': 'billboard.js/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'billboard.min.css.map', 'node_path': 'dist/', 'path': 'billboard.js/%(version)s/',
             'cdnjs': CDNJS_REPO}
        ]
    },

    # bootstrap icons
    'bootstrap-icons': {
        "license": "MIT license",
        "repository": "https://github.com/twbs/icons",
        'website': 'https://icons.getbootstrap.com/',
        'version': '1.10.3',
        'modules': [
            {'script': 'bootstrap-icons.min.css', 'path': 'bootstrap-icons/%(version)s/font/', 'cdnjs': CDNJS_REPO}]},

    # Javascript module for the simple select component. issue with Bootstrap 4 width CDN links
    'bootstrap-select': {
        'modules': [
            {'script': 'bootstrap-select.min.css', 'node_path': 'dist/css/',
             'path': 'bootstrap-select/%(version)s/css/',
             'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'bootstrap-select.css.map', 'node_path': 'dist/css/',
             'path': 'bootstrap-select/%(version)s/css/',
             'cdnjs': CDNJS_REPO}
        ]

    },

    'ajax-bootstrap-select': {
        'modules': [
            {'script': 'ajax-bootstrap-select.min.css', 'node_path': 'dist/css/', 'version': '1.4.5',
             'path': 'ajax-bootstrap-select/%(version)s/css/', 'cdnjs': CDNJS_REPO}
        ]
    },

    # Pivot table style with CDN Links
    'pivottable': {
        'modules': [
            {'script': 'pivot.min.css', 'node_path': 'dist/', 'path': 'pivottable/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # Vis style with CDN Links
    'vis': {
        'modules': [
            {'script': 'vis.min.css', 'version': '4.21.0', 'path': 'vis/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # Vis Timeline style with CDN Links
    'vis-timeline': {
        'modules': [
            {'script': 'vis-timeline-graph2d.min.css', 'path': 'vis-timeline/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # Code mirror
    'codemirror': {
        'modules': [
            {'script': 'codemirror.css', 'node_path': 'lib/', 'path': 'codemirror/%(version)s/', 'cdnjs': CDNJS_REPO}
        ]},

    'codemirror-search': {
        'modules': [
            {'script': 'matchesonscrollbar.css', 'node_path': 'addon/search/',
             'path': 'codemirror/%(version)s/addon/search/',
             'cdnjs': CDNJS_REPO},
            {'script': 'dialog.css', 'node_path': 'addon/dialog/', 'path': 'codemirror/%(version)s/addon/dialog/',
             'cdnjs': CDNJS_REPO}
        ]},

    'codemirror-fullscreen': {
        'modules': [
            {'script': 'fullscreen.css', 'node_path': 'addon/display/', 'path': 'codemirror/%(version)s/addon/display/',
             'cdnjs': CDNJS_REPO}
        ]},

    'codemirror-fold': {
        'modules': [
            {'script': 'foldgutter.css', 'node_path': 'addon/fold/', 'path': 'codemirror/%(version)s/addon/fold/',
             'cdnjs': CDNJS_REPO}
        ]},

    'codemirror-hint': {
        'modules': [
            {'script': 'show-hint.css', 'node_path': 'addon/hint/', 'path': 'codemirror/%(version)s/addon/hint/',
             'cdnjs': CDNJS_REPO}
        ]},

    # highlight
    'highlight.js': {
        'modules': [
            {'script': 'default.min.css', 'node_path': 'styles/', 'path': 'highlight.js/%(version)s/styles/',
             'cdnjs': CDNJS_REPO}
        ]},

    # Leaflet
    'leaflet': {
        'modules': [
            {'script': 'leaflet.css', 'node_path': 'dist/', 'path': 'leaflet/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    # Mapbox modules width CDN links
    'mapbox-gl': {
        'modules': [
            {'script': 'mapbox-gl.min.css', 'path': 'mapbox-gl/%(version)s/', 'cdnjs': CDNJS_REPO}]},

    #
    'json-formatter-js': {
        'modules': [
            {'script': 'json-formatter.css', 'node_path': 'dist/', 'path': 'json-formatter-js@%(version)s/dist/',
             'cdnjs': "https://cdn.jsdelivr.net/npm"},
        ]},

    # AG Grid tables
    'ag-grid-community': {
        'modules': [
            {'script': 'ag-grid.min.css', 'node_path': 'styles/', 'path': 'ag-grid/%(version)s/styles/',
             'cdnjs': CDNJS_REPO}
        ],
        'assets': [
            {'script': 'ag-theme-alpine.min.css', 'node_path': 'styles/', 'path': 'ag-grid/%(version)s/styles/',
             'cdnjs': CDNJS_REPO},
            {'script': 'ag-theme-bootstrap.min.css', 'node_path': 'styles/', 'path': 'ag-grid/%(version)s/styles/',
             'cdnjs': CDNJS_REPO},
            {'script': 'ag-theme-material.min.css', 'node_path': 'styles/', 'path': 'ag-grid/%(version)s/styles/',
             'cdnjs': CDNJS_REPO},
        ]
    },

    # Tiny slider for carousels
    'tiny-slider': {
        'modules': [
            {'script': 'tiny-slider.min.css', 'node_path': 'dist/', 'path': 'tiny-slider/%(version)s/',
             'cdnjs': CDNJS_REPO},
        ],
    },

    # gridstack Build interactive dashboards in minute
    'gridstack': {
        'modules': [
            {'script': 'gridstack.min.css', 'node_path': 'dist/', 'path': 'gridstack.js/%(version)s/',
             'cdnjs': CDNJS_REPO},
        ],
    },

    # A lightweight and elegant JavaScript color picker. Written in vanilla ES6, no dependencies. Accessible.
    '@melloware/coloris': {
        'modules': [
            {'script': 'coloris.min.css', 'node_path': 'dist/',
             'path': '@melloware/coloris@%(version)s/dist/',
             'cdnjs': JSDELIVER},
        ],
    }
}

_SERVICES = {}

GOOGLE_EXTENSIONS = {
    'charts': {'modules': [
        {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
    ],
        'website': 'https://developers.google.com/chart/interactive/docs',
        'launcher': "if(typeof google !== 'undefined'){google.charts.load('current', {'packages':['corechart']})}",
    },
    'geochart': {'modules': [
        {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
    ],
        'website': 'https://developers.google.com/chart/interactive/docs',
        'launcher': "if(typeof google !== 'undefined'){google.charts.load('current', {'packages':['geochart']})}",
    },
    'tables': {'modules': [
        {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
    ],
        'website': 'https://developers.google.com/chart/interactive/docs',
        'launcher': "if(typeof google !== 'undefined'){google.charts.load('current', {'packages':['table']})}",

    },
    'gauge': {'modules': [
        {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
    ],
        'website': 'https://developers.google.com/chart/interactive/docs',
        'launcher': "if(typeof google !== 'undefined'){google.charts.load('current', {'packages':['gauge']})}",

    },
    'maps': {'modules': [
        {'script': 'js?v=3.exp', 'version': '', 'path': 'api/', 'cdnjs': 'https://maps.googleapis.com/maps'},
    ],
        'website': 'https://developers.google.com/chart'
    },
    'streetview': {'modules': [
        {'script': 'js?v=3.exp', 'version': '', 'path': 'api/', 'cdnjs': 'https://maps.googleapis.com/maps'},
    ],
        'website': 'https://developers.google.com/chart'
    },
    'visualization': {'modules': [
        {'script': 'js?key=%(api_key)s&libraries=visualization', 'version': '', 'path': 'api/',
         'cdnjs': 'https://maps.googleapis.com/maps'},
    ],
        'website': 'https://developers.google.com/chart',
        'launcher': "if(typeof google !== 'undefined'){google.charts.load('current', {'packages':['corechart']})}",
    },
    'captcha': {'modules': [
        {'script': 'api.js?render=%(site_key)s', 'version': '', 'path': '',
         'cdnjs': 'https://www.google.com/recaptcha'},
    ],
    }
}


def script_version(alias: str, script_details: dict, with_prefix: bool = False):
    """Return the script version number with or without prefix.
    This will ensure a standard way to get the version number for a given CSS or JavaScript script in the framework.

    :param alias: The package reference alias in the framework and in NPM
    :param script_details: The script definition in the framework
    :param with_prefix: Optional. Flag to specify if the full version number is required (with the prefix)
    """
    if "version" in script_details:
        if with_prefix:
            if 'v_prefix' in JS_IMPORTS[alias]:
                return "%s%s" % (JS_IMPORTS[alias]['v_prefix'], script_details["version"])

        return script_details["version"]

    if with_prefix:
        if 'v_prefix' in JS_IMPORTS[alias]:
            return "%s%s" % (JS_IMPORTS[alias]['v_prefix'], JS_IMPORTS[alias]["version"])

    if alias in JS_IMPORTS:
        if 'node_folder' in JS_IMPORTS[alias]:
            # use the version of the node folder
            JS_IMPORTS[alias]["version"] = JS_IMPORTS[JS_IMPORTS[alias]['node_folder']]['version']
        return JS_IMPORTS[alias]["version"]

    if alias in CSS_IMPORTS:
        return CSS_IMPORTS[alias].get("version")


def script_cdnjs_path(alias: str, script_details: dict, with_prefix: bool = False) -> str:
    """Get the script path to retrieve the content locally.
    This is mainly used by PyNpm package in order to retrieve the content of the script to produce local copies of them.
    Having script copied locally will speed up the loading of the page and also will ensure a run offline.

    :param alias: The package reference alias in the framework and in NPM
    :param script_details: The script definition in the framework
    :param with_prefix: Optional. Flag to specify if the full version number is required (with the prefix)
    """
    details = dict(script_details)
    if global_settings.PACKAGES_PATH is not None:
        local_path = Path(global_settings.PACKAGES_PATH) / details['script']
        if local_path.exists():
            logging.debug("IMPORTS | Package | file %s used from %s" % (
                details['script'], global_settings.PACKAGES_PATH))
            return str(local_path)

    details["version"] = script_version(alias, script_details, with_prefix)
    details["path"] = details["path"] % details
    if "cdnjs" not in details:
        details["cdnjs"] = CDNJS_REPO
    if USE_NPM_UNPK and JS_IMPORTS.get(alias, {}).get("unpkg", True):
        if "node_path" not in details:
            details["node_path"] = ""
        return "https://www.unpkg.com/" + alias + "@latest/%(node_path)s%(script)s" % details

    try:
        return global_settings.IMPORTS_EXPR % details
    except:
        return "%(cdnjs)s/%(path)s%(script)s" % details


def script_npm_path(alias: str, script_details: dict, static_path: str, with_prefix: bool = False):
    """

    :param alias: The package reference alias in the framework and in NPM
    :param script_details: The script definition in the framework
    :param static_path:
    :param with_prefix: Optional. Flag to specify if the full version number is required (with the prefix)
    """
    details = dict(script_details)
    details["version"] = script_version(alias, script_details, with_prefix)
    details["node_path"] = str(details.get("node_path", "\\") % details).replace("/", "\\")
    details["alias"] = JS_IMPORTS[alias].get("node_folder", alias)
    details["static"] = static_path
    if not details["node_path"].endswith("\\"):
        details["node_path"] += "\\"
    return r"%(static)s\%(alias)s\%(node_path)s%(script)s" % details


def extend(reference: str, module_path, version: str, cdnjs_url: str = CDNJS_REPO, required: Optional[list] = None):
    """Function to extend the internal CSS and JS registered modules.

    :param reference: The internal reference in the framework
    :param module_path: The different modules and location
    :param version: The version number. Can be an internal module reference to point to follow its version number
    :param cdnjs_url: The CDNJS reference path
    :param required: Optional. The list of dependency modules
    """
    for module, path in module_path:
        config = JS_IMPORTS if module.endswith(".js") else CSS_IMPORTS
        if reference not in config:
            config[reference] = {"modules": []}
            if required is not None:
                reqs = [{'alias': req} for req in required if req in config]
                if reqs:
                    config[reference]['req'] = reqs
        if version in config:
            version = config[version].get('version') or config[version]['modules'][0]['version']
        config[reference]["modules"].append({'script': module, 'version': version, 'path': path, 'cdnjs': cdnjs_url})


def extend_imports(extension: dict):
    """Hook to extend the imports in the centralised Import module.
    Packages definition is quite similar to the one in Imports.py except that CSS and JS are grouped together for
    simplicity.

    :param extension: The list of packages to be added grouped by alias
    """
    global CSS_IMPORTS, JS_IMPORTS

    for alias, mod in extension.items():
        css, js = {'website': mod.get('website', ''), 'modules': []}, {'website': mod.get('website', ''), 'modules': []}
        if 'register' in mod:
            js['register'] = mod['register']
        if 'req' in mod:
            css['req'], js['req'] = [], []
            for req in mod['req']:
                if req['alias'] in CSS_IMPORTS:
                    css['req'].append(req)
                if req['alias'] in JS_IMPORTS:
                    js['req'].append(req)
        if 'modules' in mod:
            for module in mod['modules']:
                if 'cdnjs' not in module:
                    module['cdnjs'] = CDNJS_REPO
                module['version'] = mod['version']  # propagate the version tag
                if module['script'].endswith(".js"):
                    js['modules'].append(module)
                elif module['script'].endswith(".css"):
                    css['modules'].append(module)
            if css['modules']:
                CSS_IMPORTS[alias] = css
            if js['modules']:
                JS_IMPORTS[alias] = js
        if 'services' in mod:
            for service in mod['services']:
                service['pmts'] = ";".join(["%s=%s" % (k, v) for k, v in service['values'].items()])
                if service['type'] not in _SERVICES:
                    _SERVICES[alias] = {}
                _SERVICES[alias].setdefault(service['type'], []).append("%(url)s?%(pmts)s" % service)


class ImportModule:
    overriden = False

    def __init__(self, name: str, js: dict, css: dict, links: Optional[dict] = None, page=None):
        self._name = name
        self.page = page
        self.community_version = True
        self._defer, self._async, self.attrs = False, False, {}
        if page is not None and name not in js and name.startswith("local_"):
            # In this case the configuration needs to be retrieved from the page context instead
            self._js = self.page.imports.jsImports[name]
        else:
            self._js = js[name]
        self._css = css.get(name, {})
        if links is not None:
            links[self._name] = self

    @property
    def name(self):
        return self._name

    @property
    def alias(self) -> str:
        """Get the NPM alias name."""
        return self._name

    @property
    def defer(self) -> bool:
        """If the defer attribute is set, it specifies that the script is downloaded in parallel to parsing the page,
        and executed after the page has finished parsing.

        `Defer <https://www.w3schools.com/tags/att_script_defer.asp>`_
        """
        return self._defer

    @defer.setter
    def defer(self, flag: bool):
        self._defer = flag

    @property
    def asynchrone(self) -> bool:
        """Specifies that the script is downloaded in parallel to parsing the page, and executed as soon as it is
        available (before parsing completes) (only for external scripts).

        `Defer <https://www.w3schools.com/tags/att_script_defer.asp>`_
        """
        return self._async

    @asynchrone.setter
    def asynchrone(self, flag: bool):
        self._async = flag

    @property
    def nomodule(self) -> bool:
        """Specifies that the script should not be executed in browsers supporting ES2015 modules.

        `Tag Script <https://www.w3schools.com/tags/tag_script.asp>`_
        """
        return self.attrs.get("nomodule")

    @nomodule.setter
    def nomodule(self, flag: bool):
        self.attrs["nomodule"] = flag

    @property
    def eferrerpolicy(self) -> str:
        """Specifies which referrer information to send when fetching a script.

        Related Pages:

          https://www.w3schools.com/tags/att_script_referrepolicy.asp
        """
        return self.attrs.get("eferrerpolicy")

    @eferrerpolicy.setter
    def eferrerpolicy(self, value: str):
        self.attrs["eferrerpolicy"] = value

    @property
    def version(self):
        """Return the package version number defined in the framework. """
        return self._js["versions"]

    @version.setter
    def version(self, val: str):
        new_js = collections.OrderedDict()
        for k, v in self._js["main"].items():
            new_js[k.replace(v, val)] = val
        self._js["versions"] = [val]
        self._js["main"] = new_js
        # Change the package for ChartJs versions above 4
        # https://www.chartjs.org/docs/latest/migration/v4-migration.html
        if self.alias == "chart.js" and int(val.split(".")[0]) > 3:
            new_js = collections.OrderedDict()
            for k, v in self._js["main"].items():
                new_js[k.replace(v, val).replace("chart.min.js", "chart.umd.min.js")] = val
            self._js["main"] = new_js
        if self._css:
            new_css = collections.OrderedDict()
            for k, v in self._css["main"].items():
                new_css[k.replace(v, val)] = val
            self._css["versions"] = [val]
            self._css["main"] = new_css

    @property
    def path(self) -> str:
        """Get the package path used to retrieve the various modules. """
        mod = JS_IMPORTS[self._name]['modules'][0]
        mod["version"] = self.version[0]
        mod["path"] = mod["path"] % mod
        return "%(cdnjs)s/%(path)s" % mod

    @path.setter
    def path(self, full_path: str):
        if full_path.endswith("/"):
            full_path = full_path[:-1]
        for mod in JS_IMPORTS[self._name]['modules']:
            mod["cdnjs"] = full_path
            mod["path"] = ""
        if self._name in CSS_IMPORTS:
            for mod in CSS_IMPORTS[self._name]['modules']:
                mod["cdnjs"] = full_path
                mod["path"] = ""

    @property
    def scripts(self):
        """Get the list of external files used for this package.

        Usage::

          pkgs = page.imports().pkgs
          pkgs.tabulator.version = "4.8.7"
          print(pkgs.tabulator.scripts)
        """
        return self._js["main"].keys() | self._css["main"].keys()

    @property
    def js(self) -> list:
        return list(self._js["main"].keys())

    @property
    def css(self) -> list:
        return list(self._css["main"].keys())

    def add(self):
        """Force a package to be added to the external requirements."""
        if self._name in JS_IMPORTS:
            self.page.jsImports.add(self._name)
        if self._name in CSS_IMPORTS:
            self.page.cssImport.add(self._name)

    def from_cdnjs(self):
        """Just change the overridden flag of this package to ensure it will not be changed by the set_local method.
        Indeed, this method will not impact any modules with this flag set to True.
        """
        self.overriden = True

    def set_local(self, static_url: str = "/static"):
        """Route the package to the local path.
        Check first of the modules exist and raise an error otherwise.

        :param static_url: Optional. The static root on the server. (default value /static/)
        """
        if self.overriden:
            return

        # TODO Find way to fix the change of name in a better way
        mapped_name = self._name
        if not self.community_version and self._name == "ag-grid-community":
            mapped_name = "ag-grid-enterprise"
        new_js = collections.OrderedDict()
        for v in JS_IMPORTS[self._name]["modules"]:
            if os.path.exists(v['cdnjs']):
                continue

            node_path = v.get("node_path", "")
            if not node_path.endswith("/"):
                node_path += "/"
            new_js["%s/%s/%s%s" % (static_url, mapped_name, node_path, v["script"])] = self.version
        if new_js:
            self._js["main"] = new_js
        if self._css:
            new_css = collections.OrderedDict()
            for v in CSS_IMPORTS[self._name]["modules"]:
                if os.path.exists(v['cdnjs']):
                    continue

                node_path = v.get("node_path", "")
                if not node_path.endswith("/"):
                    node_path += "/"
                new_css["%s/%s/%s%s" % (static_url, mapped_name, node_path, v["script"])] = self.version
            if new_css:
                self._css["main"] = new_css
        self.overriden = True

    def set_enterprise(self, version: str = None, license_key: str = None):
        """Change the package to the enterprise version.
        This feature will only work for few modules like AGGrid.

        Usage::

          page = pk.Page()
          page.imports.pkgs.ag_grid.set_enterprise()

        :param version: Set the package version number
        :param license_key: Optional. The license key
        """
        pgks = ("ag-grid-community", 'ag-charts-community')
        if self._name not in pgks:
            raise NotImplementedError("Noting implemented for this package %s, please contact epyk team" % self._name)

        self.community_version = False
        self.page.imports.add(self._name)
        if self._name == 'ag-charts-community':
            version = version or JS_IMPORTS[self._name]["enterprise"]
        if self._name == 'ag-grid-community':
            version = version or JS_IMPORTS['ag-grid-community']["enterprise"]
            JS_IMPORTS['ag-grid-community']["version"] = version
            JS_IMPORTS['ag-grid-community']["register"]["module"] = "ag-grid-enterprise.min"
            JS_IMPORTS['ag-grid-community']["register"]["npm"] = "ag-grid-enterprise"
            JS_IMPORTS['ag-grid-community']['modules'] = [
                {'script': 'ag-grid-enterprise.min.js', 'node_path': 'dist/', 'path': 'ag-grid-enterprise@%(version)s/dist/',
                 'cdnjs': JSDELIVER},
            ]
            self._js["main"] = {
                "%s/ag-grid-enterprise@%s/dist/ag-grid-enterprise.min.js" % (JSDELIVER, version): version}
            self._js["type"] = {
                "%s/ag-grid-enterprise@%s/dist/ag-grid-enterprise.min.js" % (JSDELIVER, version): 'text/javascript'}
            self._js["dep"] = ["/static\\ag-grid/%s/ag-grid-enterprise.min.js" % version]
            self._js["versions"] = [version]

            CSS_IMPORTS['ag-grid-community']['modules'] = [
                {'script': 'ag-grid.min.css', 'node_path': 'styles/', 'path': 'ag-grid-enterprise@%(version)s/styles/', 'cdnjs': JSDELIVER},
            ]
            self._css["main"] = {
                "%s/ag-grid-enterprise@%s/styles/ag-grid.min.css" % (JSDELIVER, version): version}
            self._css["type"] = {
                "%s/ag-grid-enterprise@%s/styles/ag-grid.min.css" % (JSDELIVER, version): 'text/javascript'}
            self._css["dep"] = ["/static\\ag-grid/%s/styles/ag-theme-alpine.min.css" % version]
            self._css["versions"] = [version]
            if license_key is not None:
                self.page.properties.js.add_text("if(window['agGrid']){agGrid.LicenseManager.setLicenseKey('%s')}" % license_key)

    def set_access_token(self, value: str = None, name: str = ""):
        """Set an access token to use this package

        Related Pages:

          https://docs.mapbox.com/mapbox-gl-js/example/globe/

        Usage::

          page = pk.Page()
          page.imports.pkgs.mapbox.set_access_token(
            "XXXXXX",
            "mapboxgl.accessToken"
          )

        :param value: The access token to set to use the library
        :param name: The access token variable name
        """
        self.page.imports.add(self._name)
        self.page.properties.js.add_text("%s = '%s'" % (name, value))


class ImportPackagesPivotExts:
    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str):
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)

    @property
    def c3(self):
        """Shortcut to C3 package. """
        return self.get("pivot-c3")

    @property
    def plotly(self):
        """Shortcut to Plotly package."""
        return self.get("pivot-plotly")

    @property
    def d3(self):
        """Shortcut to D3 package."""
        return self.get("pivot-d3")

    @property
    def subtotal(self):
        """Shortcut to Sub total table package."""
        return self.get("subtotal")


class ImportPackagesCodeMirrorExts:
    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str):
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)

    @property
    def search(self) -> ImportModule:
        """Shortcut to CodeMirror Search addon."""
        return self.get("codemirror-search")

    @property
    def placeholder(self) -> ImportModule:
        """Shortcut to CodeMirror PlaceHolder addon."""
        return self.get("codemirror-placeholder")

    @property
    def trailingspace(self) -> ImportModule:
        """Shortcut to CodeMirror Trainling Space addon."""
        return self.get("codemirror-trailingspace")

    @property
    def fullscreen(self) -> ImportModule:
        """Shortcut to CodeMirror Full Screen addon."""
        return self.get("codemirror-fullscreen")

    @property
    def highlighter(self) -> ImportModule:
        """Shortcut to CodeMirror Highligher addon."""
        return self.get("codemirror-highlighter")

    @property
    def hint(self) -> ImportModule:
        """Shortcut to Code Mirror Hint addon."""
        return self.get("codemirror-hint")

    @property
    def panel(self) -> ImportModule:
        """Shortcut to CodeMirror Panel addon."""
        return self.get("codemirror-panel")

    @property
    def fold(self) -> ImportModule:
        """Shortcut to CodeMirror Fold addon."""
        return self.get("codemirror-fold")


class ImportPackagesD3Exts:
    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str):
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)

    @property
    def tip(self) -> ImportModule:
        """ Shortcut to D3 Tip addon. """
        return self.get("d3-tip")

    @property
    def axis(self) -> ImportModule:
        """ Shortcut to D3 Axis addon. """
        return self.get("d3-axis")

    @property
    def ease(self) -> ImportModule:
        """ Shortcut to D3 Ease addon. """
        return self.get("d3-ease")

    @property
    def dsv(self) -> ImportModule:
        """ Shortcut to D3 Dsv addon. """
        return self.get("d3-dsv")

    @property
    def dispatch(self) -> ImportModule:
        """ Shortcut to D3 Dispatch addon. """
        return self.get("d3-dispatch")

    @property
    def transition(self) -> ImportModule:
        """ Shortcut to D3 Transition addon. """
        return self.get("d3-transition")

    @property
    def selection(self) -> ImportModule:
        """ Shortcut to D3 Selection addon. """
        return self.get("d3-selection")

    @property
    def interpolate(self) -> ImportModule:
        """ Shortcut to D3 Interpolate addon. """
        return self.get("d3-interpolate")

    @property
    def time_format(self) -> ImportModule:
        """ Shortcut to D3 Time Format addon. """
        return self.get("d3-time-format")

    @property
    def time(self) -> ImportModule:
        """ Shortcut to D3 Time addon. """
        return self.get("d3-time")

    @property
    def array(self) -> ImportModule:
        """ Shortcut to D3 Array addon. """
        return self.get("d3-array")

    @property
    def format(self) -> ImportModule:
        """ Shortcut to D3 Format addon. """
        return self.get("d3-format")

    @property
    def timer(self) -> ImportModule:
        """ Shortcut to D3 Timer addon. """
        return self.get("d3-timer")

    @property
    def collection(self) -> ImportModule:
        """ Shortcut to D3 Collection addon. """
        return self.get("d3-collection")

    @property
    def scale(self) -> ImportModule:
        """ Shortcut to D3 Scale addon. """
        return self.get("d3-scale")

    @property
    def color(self) -> ImportModule:
        """ Shortcut to D3 Color addon. """
        return self.get("d3-color")

    @property
    def brush(self) -> ImportModule:
        """ Shortcut to D3 Brush addon. """
        return self.get("d3-brush")

    @property
    def drag(self) -> ImportModule:
        """ Shortcut to D3 Drag addon. """
        return self.get("d3-drag")

    @property
    def shape(self) -> ImportModule:
        """ Shortcut to D3 Shape addon. """
        return self.get("d3-shape")

    @property
    def zoom(self) -> ImportModule:
        """ Shortcut to D3 Zoom addon. """
        return self.get("d3-zoom")

    @property
    def path(self) -> ImportModule:
        """ Shortcut to D3 Path addon. """
        return self.get("d3-path")


class ImportPackagesDataTableExts:
    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str):
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)


class ImportPackagesChartJsExts:

    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str):
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)

    @property
    def treemap(self) -> ImportModule:
        """
        Adds treemap chart type.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-treemap")

    @property
    def annotation(self) -> ImportModule:
        """
        Draws lines and boxes on the chart area.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-annotation")

    @property
    def datalabels(self) -> ImportModule:
        """
        Displays labels on data for any type of charts.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-datalabels")

    @property
    def deferred(self) -> ImportModule:
        """
        Defers initial chart update until chart scrolls into viewport.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-deferred")

    @property
    def hierarchical(self) -> ImportModule:
        """
        Chart.js module for adding a new categorical scale which mimics a hierarchical tree.

        Related Pages:

          https://github.com/sgratzl/chartjs-plugin-hierarchical
        """
        return self.get("chartjs-plugin-hierarchical")

    @property
    def zoom(self) -> ImportModule:
        """
        Enables zooming and panning on charts.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-zoom")

    @property
    def crosshair(self) -> ImportModule:
        """
        Adds a data crosshair to line and scatter charts.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-crosshair")

    @property
    def stacked100(self) -> ImportModule:
        """
        This plugin for Chart.js that makes your bar chart to 100% stacked bar chart.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-stacked100")

    @property
    def matrix(self) -> ImportModule:
        """
        Adds matrix chart type.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-matrix")

    @property
    def sankey(self) -> ImportModule:
        """
        Adds sankey diagram chart type.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-sankey")

    @property
    def wordcloud(self) -> ImportModule:
        """
        Adds word-cloud chart type.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-wordcloud")

    @property
    def venn(self) -> ImportModule:
        """
        Adds venn and euler chart type.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-venn")

    @property
    def dragdata(self) -> ImportModule:
        """
        Lets users drag data points on the chart.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-dragdata")

    @property
    def geo(self) -> ImportModule:
        """
        Adds geographic map chart types such as choropleth and bubble map.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-geo")

    @property
    def labels(self) -> ImportModule:
        """ Shortcut to ChartKs Plugin labels addon. """
        return self.get("chartjs-plugin-labels")


class ImportPackagesTabulatorExts:

    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str) -> ImportModule:
        """
        Generic way to retrieve packages from the framework.

        This is a shortcut to change any properties for the package (version, path...).

        :param name: The package alias to be loaded
        """
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)

    @property
    def formatter_inputs(self) -> ImportModule:
        """ Shortcut to Tabulator Inputs addon. """
        return self.get("tabulator-inputs")

    @property
    def formatter_icons(self) -> ImportModule:
        """ Shortcut to Tabulator Icons addon. """
        return self.get("tabulator-icons")

    @property
    def formatter_numbers(self) -> ImportModule:
        """ Shortcut to Tabulator Numbers addon. """
        return self.get("tabulator-numbers")

    @property
    def formatter_drops(self) -> ImportModule:
        """ Shortcut to Tabulator Drop addon. """
        return self.get("tabulator-drop")

    @property
    def mutators_inputs(self) -> ImportModule:
        """ Shortcut to Tabulator Mutators Inputs addon. """
        return self.get("tabulator-mutators-inputs")

    @property
    def editors_inputs(self) -> ImportModule:
        """ Shortcut to Tabulator Editors Inputs addon. """
        return self.get("editors-inputs")

    @property
    def editors_dates(self) -> ImportModule:
        """ Shortcut to Tabulator Editors Dates addon. """
        return self.get("editors-dates")

    @property
    def editors_selects(self) -> ImportModule:
        """ Shortcut to Tabulator Selects addon. """
        return self.get("editors-selects")


class ImportPackages:

    def __init__(self, js: dict, css: dict, page=None):
        self._js = js
        self._css = css
        self.page = page
        self.__linked = {}

    def get(self, name: str) -> ImportModule:
        """ 
        Generic way to retrieve packages from the framework.

        This is a shortcut to change any properties for the package (version, path...).
    
        :param name: The package alias to be loaded
        """
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked, page=self.page)

    @property
    def vis(self) -> ImportModule:
        """
        A dynamic, browser based visualization library..

        TODO: Add the split of packages

        Related Pages:

          http://visjs.org
        """
        return self.get("vis")

    @property
    def d3(self) -> ImportModule:
        """
        D3.js is a JavaScript library for manipulating documents based on data.

        TODO: Add the split of packages

        Related Pages:

          https://d3js.org/
        """
        return self.get("d3")

    @property
    def dc(self) -> ImportModule:
        """
        dc.js is a javascript charting library with native crossfilter support, allowing highly efficient exploration on
        large multi-dimensional datasets.

        Related Pages:

          https://dc-js.github.io/dc.js
        """
        return self.get("dc")

    @property
    def nvd3(self) -> ImportModule:
        """
        This project is an attempt to build re-usable charts and chart components for d3.js without taking away
        the power that d3.js gives you.

        Related Pages:

          http://nvd3.org/
        """
        return self.get("nvd3")

    @property
    def c3(self) -> ImportModule:
        """ 
        C3.js D3-based reusable chart library.

        Related Pages:
    
          https://c3js.org/
        """
        return self.get("c3")

    @property
    def billboard(self) -> ImportModule:
        """ 
        Re-usable, easy interface JavaScript chart library, based on D3 v4+.

        Related Pages:
    
          https://naver.github.io/billboard.js/
        """
        return self.get("billboard.js")

    @property
    def chart_js(self) -> ImportModule:
        """ 
        Simple yet flexible JavaScript charting for designers & developers.

        Related Pages:
    
          https://www.chartjs.org/
        """
        return self.get("chart.js")

    @property
    def chart_js_extensions(self) -> ImportPackagesChartJsExts:
        """ 
        Simple yet flexible JavaScript charting for designers & developers.

        Related Pages:
    
          https://www.chartjs.org/
        """
        return ImportPackagesChartJsExts(self._js, self._css, self.__linked)

    @property
    def crossfilter(self) -> ImportModule:
        """
        Fast Multidimensional Filtering for Coordinated Views.

        Related Pages:

          http://square.github.io/crossfilter
        """
        return self.get("crossfilter")

    @property
    def apexcharts(self) -> ImportModule:
        """
        Modern & Interactive Open-source Charts.

        Related Pages:

          https://apexcharts.com
        """
        return self.get("apexcharts")

    @property
    def plotly(self) -> ImportModule:
        """
        Plotly JavaScript Open Source Graphing Library.

        Related Pages:

          https://plot.ly/javascript/
        """
        return self.get("plotly.js")

    @property
    def ag_grid(self) -> ImportModule:
        """
        The Best JavaScript Grid in the World.

        Related Pages:

          https://www.ag-grid.com/javascript-grid/
        """
        return self.get("ag-grid-community")

    @property
    def bootstrap(self) -> ImportModule:
        """
        The most popular front-end framework for developing responsive, mobile first projects on the web.

        Related Pages:

          https://getbootstrap.com/
        """
        return self.get("bootstrap")

    @property
    def jquery(self) -> ImportModule:
        """
        JavaScript library for DOM operations.

        Related Pages:

          https://jquery.com
        """
        return self.get("jquery")

    @property
    def jqueryui(self) -> ImportModule:
        """
        jQuery UI is a curated set of user interface interactions, effects, widgets, and themes built on top of the
        jQuery JavaScript Library.

        Related Pages:

          https://jqueryui.com/
        """
        return self.get("jqueryui")

    @property
    def jquery_bracket(self) -> ImportModule:
        """
        jQuery bracket is a jQuery plugin that lets users create and display single and double elimination brackets for
        tournament play.

        Related Pages:

          http://www.aropupu.fi/bracket/
        """
        return self.get("jquery-bracket")

    @property
    def jquery_sparkline(self) -> ImportModule:
        """
        This jQuery plugin generates sparklines (small inline charts) directly in the browser using data supplied
        either inline in the HTML, or via javascript.

        Related Pages:

          https://omnipotent.net/jquery.sparkline
        """
        return self.get("jquery-sparkline")

    @property
    def jqvmap(self) -> ImportModule:
        """
        JQVMap is a jQuery plugin that renders Interactive, Clickable Vector Maps.

        Related Pages:

          https://www.10bestdesign.com/jqvmap/
        """
        return self.get("jqvmap")

    @property
    def qunit(self) -> ImportModule:
        """
        The powerful, easy-to-use JavaScript testing framework.

        Related Pages:

          https://qunitjs.com/
        """
        return self.get("qunit")

    @property
    def accounting(self) -> ImportModule:
        """
        Number, money and currency formatting library.

        Related Pages:

          http://openexchangerates.github.io/accounting.js
        """
        return self.get("accounting")

    @property
    def qrcodejs(self) -> ImportModule:
        """
        QRCode.js is javascript library for making QRCode.

        QRCode.js supports Cross-browser with HTML5 Canvas and table tag in DOM. QRCode.js has no dependencies.

        Related Pages:

          https://davidshimjs.github.io/qrcodejs
        """
        return self.get("qrcodejs")

    @property
    def underscore(self) -> ImportModule:
        """
        accounting.js is a tiny JavaScript library by Open Exchange Rates, providing simple and advanced number,
        money and currency formatting.

        Related Pages:

          https://openexchangerates.github.io/accounting.js/
        """
        return self.get("underscore")

    @property
    def tabulator(self) -> ImportModule:
        """
        Interactive table generation JavaScript library.

        Related Pages:

          http://tabulator.info/
        """
        return self.get("tabulator-tables")

    @property
    def tabulator_extensions(self) -> ImportPackagesTabulatorExts:
        """ Get all the defined extension for tabulator. """
        return ImportPackagesTabulatorExts(self._js, self._css, self.__linked)

    @property
    def datatables(self) -> ImportModule:
        """ 
        Add advanced interaction controls to your HTML tables the free & easy way.

        Related Pages:
    
          https://datatables.net/
        """
        return self.get("datatables")

    @property
    def datatable_extensions(self) -> ImportPackagesDataTableExts:
        """ Get all the defined extension for DataTable. """
        return ImportPackagesDataTableExts(self._js, self._css, self.__linked)

    @property
    def mathjax(self) -> ImportModule:
        """
        Beautiful and accessible math in all browsers.

        Related Pages:

          https://www.mathjax.org/
        """
        return self.get("mathjax")

    @property
    def mapbox(self) -> ImportModule:
        """
        Maps and location for developers.

        Related Pages:

          https://docs.mapbox.com/mapbox.js/api/v3.3.1/
        """
        return self.get("mapbox-gl")

    @property
    def moment(self) -> ImportModule:
        """
        Parse, validate, manipulate, and display dates and times in JavaScript.

        Related Pages:

          https://momentjs.com/
        """
        return self.get("moment")

    @property
    def hammer(self) -> ImportModule:
        """
        Add touch gestures to your webapp.

        Related Pages:

          https://hammerjs.github.io/
        """
        return self.get("hammer")

    @property
    def popper_js(self) -> ImportModule:
        """ Tooltip & Popover Positioning Engine.

    Related Pages:

      https://github.com/popperjs/popper-core
    """
        return self.get("@popperjs/core")

    @property
    def font_awesome(self) -> ImportModule:
        """
        The next generation of our icon library + toolkit is coming with more icons, more styles, more services,
        and more awesome.

        Related Pages:

          https://fontawesome.com
        """
        return self.get("font-awesome")

    @property
    def json_formatter(self) -> ImportModule:
        """
        Render JSON objects in HTML with a collapsible navigation.

        Related Pages:

          https://azimi.me/json-formatter-js/
        """
        return self.get("json-formatter-js")

    @property
    def pivottable(self) -> ImportModule:
        """
        Open-source Javascript Pivot Table (aka Pivot Grid, Pivot Chart, Cross-Tab) implementation with drag'n'drop.

        Related Pages:

          https://github.com/nicolaskruchten/pivottable
        """
        return self.get("pivottable")

    @property
    def require_js(self) -> ImportModule:
        """ RequireJS is a JavaScript file and module loader.

    It is optimized for in-browser use, but it can be used in other JavaScript environments, like Rhino and Node.

    Related Pages:

      https://requirejs.org/
    """
        return self.get("requirejs")

    @property
    def timepicker(self) -> ImportModule:
        """ jQuery TimePicker is a plugin to enhance standard form input fields, helping users to select (or type) times.

        Related Pages:

          https://timepicker.co
        """
        return self.get("timepicker")

    @property
    def socket(self) -> ImportModule:
        """ Real-time application framework.

    Socket.IO enables real-time bidirectional event-based communication.

    Related Pages:

      https://github.com/socketio/socket.io
    """
        return self.get("socket.io")

    @property
    def codemirror(self) -> ImportModule:
        """ CodeMirror is a versatile text editor implemented in JavaScript for the browser.

    Related Pages:

      https://codemirror.net
    """
        return self.get("codemirror")

    @property
    def codemirror_extensions(self) -> ImportPackagesCodeMirrorExts:
        """ Code mirror extensions """
        return ImportPackagesCodeMirrorExts(self._js, self._css, self.__linked)

    @property
    def highlight(self) -> ImportModule:
        """
        Syntax highlighting for the Web.

        Related Pages:

          https://highlightjs.org/
        """
        return self.get("highlight.js")

    @property
    def leaflet(self) -> ImportModule:
        """
        An open-source JavaScript library for mobile-friendly interactive maps.

        Related Pages:

          https://leafletjs.com/
        """
        return self.get("leaflet")

    @property
    def showdown(self) -> ImportModule:
        """
        Showdown is a Javascript Markdown to HTML converter.

        Related Pages:

          https://github.com/showdownjs/showdown
        """
        return self.get("showdown")

    @property
    def sortablejs(self) -> ImportModule:
        """
        Create and reorder lists with drag-and-drop. For use with modern browsers and touch devices.

        Related Pages:

          https://github.com/SortableJS/Sortable
        """
        return self.get("sortablejs")


class ImportManager:
    """
    The main class in charge of defining the order of the imports in the header.

    There is no check on the presence of the modules on the server. The only purpose of this module is to produce the
    string with the module names and the correct paths to your final HTML report.
    """

    online: bool = True
    self_contained: bool = False
    _static_path: Optional[str] = None
    set_exports: bool = False

    def __init__(self, page=None):
        """
        Load the hierarchy of modules.

        This module will define the import section in the header of the final HTML page.

        It will create links to the official online websites or link to an internal copy if no internet connection is
        available. To run a report using the online mode to False it is requires to get all the packages locally
        saved with the expected structured (basically the one of the CDNJS repository)

        :param page: Optional. The internal report object with all the required external modules
        """
        self.page, ovr_version, self.__pkgs = page, {}, None
        self.force_position = {}
        self.reload()

    def packages_from_json(self, dependency_file: str, ext_packages: Dict[str, dict]):
        """
        reduce the list of packages to the ones defined in the packages.json.
        This will also add the requirements for those packages.

        Usage::

            page = ek.Page()
            page.imports.packages_from_json(r"./assets/package.json")

            # Loading external packages
            ext_pkgs = {
                "@eonasdan/tempus-dominus": {
                    'version': "6.7.7",
                    'req': [{'alias': '@popperjs/core'}, {'alias': 'bootstrap'}],
                    'modules': [
                      {'script': 'tempus-dominus.min.css', 'node_path': 'dist/css/', 'path': 'tempus-dominus/%(version)s/'},
                      {'script': 'tempus-dominus.min.js', 'node_path': 'dist/js/', 'path': 'tempus-dominus/%(version)s/'},
                    ]}}

            page.imports.packages_from_json(r"./assets/package.json", ext_pkgs)

        :param dependency_file: Path for the file packages.json
        :param ext_packages: A dictionary with all the external packages to add added to the internal imports
        """
        global JS_IMPORTS
        global CSS_IMPORTS
        temp_js, temp_css = {}, {}
        for k, v in ext_packages.items():
            self.addPackage(k, v)
        with open(dependency_file) as fp:
            package_json = json.load(fp)
            for dependency, version in package_json["dependencies"].items():
                if dependency in JS_IMPORTS:
                    if version and "version" in JS_IMPORTS[dependency]:
                        if version.startswith("^"):
                            JS_IMPORTS[dependency]["version"] = version[1:]
                            for module in JS_IMPORTS[dependency]["modules"]:
                                module["version"] = version[1:]
                        else:
                            JS_IMPORTS[dependency]["version"] = version
                            for module in JS_IMPORTS[dependency]["modules"]:
                                module["version"] = version
                    temp_js[dependency] = JS_IMPORTS[dependency]
                    for req in JS_IMPORTS[dependency].get("req", []):
                        temp_js[req["alias"]] = JS_IMPORTS[req["alias"]]
                if dependency in CSS_IMPORTS:
                    if version:
                        if version.startswith("^"):
                            CSS_IMPORTS[dependency]["version"] = version[1:]
                            for module in CSS_IMPORTS[dependency]["modules"]:
                                module["version"] = version[1:]
                        else:
                            CSS_IMPORTS[dependency]["version"] = version
                            for module in CSS_IMPORTS[dependency]["modules"]:
                                module["version"] = version
                    temp_css[dependency] = CSS_IMPORTS[dependency]
                    for req in CSS_IMPORTS[dependency].get("req", []):
                        temp_css[req["alias"]] = CSS_IMPORTS[req["alias"]]
        JS_IMPORTS = temp_js
        CSS_IMPORTS = temp_css
        self.reload()

    def reload(self):
        ovr_version = {}
        if self.page is not None and self.page.ext_packages is not None:
            extend_imports(self.page.ext_packages)
        # if report is not None and self._report.run.report_name is not None and self._report.run.local_path is not None
        # and os.path.exists(os.path.join(self._report.run.local_path, '__init__.py')):
        # Force the version of some external Javascript or CSS packages
        #  packages = importlib.import_module("%s.__init__" % self._report.run.report_name)
        #  ovr_version = getattr(packages, 'MODULES', {})
        if self.page is not None:
            self.page._with_google_imports = False
            # Apply the different reports overrides on the packages versions
            ovr_version.update(self.page._props.get('packages', {}))
        self.jsImports, self.cssImports, self.moduleConfigs, self.reqVersion = {}, {}, {}, {}
        self.__add_imports([('js', self.jsImports, JS_IMPORTS), ('css', self.cssImports, CSS_IMPORTS)])

    def __add_imports(self, modules: list, ovr_version: Optional[dict] = None):
        for folder, import_dict, import_type in modules:
            if folder is None and import_type is None:
                continue

            if folder is None:
                for alias, definition in dict(import_type).items():
                    main_css = collections.OrderedDict()
                    main_js, main_js_types = collections.OrderedDict(), collections.OrderedDict()
                    for i, mod in enumerate(definition['modules']):
                        if ovr_version is not None and alias in ovr_version:
                            mod['version'] = ovr_version[alias]
                        else:
                            mod["version"] = definition["version"]
                        script_path = script_cdnjs_path(alias, mod)
                        if script_path.endswith(".js"):
                            main = main_js
                            main_js_types[script_path] = mod.get("type", 'text/javascript')
                        else:
                            main = main_css
                        if 'url' in definition:
                            main["%s%s" % (definition['url'], mod['script'])] = mod['version']
                        else:
                            main[script_path] = script_version(alias, mod)
                    modules = collections.OrderedDict()
                    self.getModules(modules, alias, folder, import_type)
                    if 'config' in definition:
                        self.moduleConfigs[alias] = definition['config']
                    if main_css:
                        self.cssImports[alias] = {'main': main_css, 'dep': list(modules.keys()),
                                                  'versions': list(main_css.values())}
                    if main_js:
                        self.jsImports[alias] = {'main': main_js, 'dep': list(modules.keys()),
                                                 'versions': list(main_js.values()),
                                                 "type": main_js_types}
            else:
                for alias, definition in dict(import_type).items():
                    main, main_types = collections.OrderedDict(), collections.OrderedDict()
                    for i, mod in enumerate(definition['modules']):
                        if ovr_version is not None and alias in ovr_version:
                            mod['version'] = ovr_version[alias]
                        script_path = script_cdnjs_path(alias, mod)
                        mod_type = "stylesheet" if script_path.endswith(".css") else 'text/javascript'
                        if 'url' in definition:
                            main["%s%s" % (definition['url'], mod['script'])] = mod['version']
                            main_types["%s%s" % (definition['url'], mod['script'])] = mod_type
                        else:
                            main[script_path] = script_version(alias, mod)
                            main_types[script_path] = mod_type
                    modules = collections.OrderedDict()
                    self.getModules(modules, alias, folder, import_type)
                    if 'config' in definition:
                        self.moduleConfigs[alias] = definition['config']
                    main_keys, versions = [], []
                    for k, v in main.items():
                        main_keys.append(k)
                        versions.append(v)
                    import_dict[alias] = {
                        'main': main, 'dep': list(modules.keys()), 'versions': versions, "type": main_types}

    @property
    def static_url(self) -> str:
        return self._static_path

    @static_url.setter
    def static_url(self, path: str):
        if path is not None:
            self.online = False
        self._static_path = path

    def add(self, alias: str, incl_css: bool = True, incl_js: bool = True):
        """Add package to the page external required modules.

        :param alias: The external module alias
        :param incl_css: Optional. Include CSS files
        :param incl_js: Optional. Include Js files
        """
        if alias in JS_IMPORTS and incl_js:
            self.page.jsImports.add(alias)
        if alias in CSS_IMPORTS and incl_css:
            self.page.cssImport.add(alias)

    def extend(self, aliases: List[str]):
        """Add multiple aliases to the external requirements.

        :param aliases: The list of package aliases to be added
        """
        for alias in aliases:
            self.add(alias)

    @property
    def requirements(self) -> set:
        """Retrieve all the mandatory requirements required to display the final HTML page.

        Usage::

          print(page.imports().requirements)
        """
        module_alias = set(self.cleanImports(self.page.jsImports, JS_IMPORTS))
        for css in self.cleanImports(self.page.cssImport, CSS_IMPORTS):
            module_alias.add(css)
        return module_alias

    def getModules(self, modules: dict, alias: Union[str, dict], folder: Optional[str] = None,
                   module_details: Optional[dict] = None):
        """Return the list of modules for a given entry.
        This will be used recursively to resolve all the dependencies.

        Usage::

          modules = collections.OrderedDict()
          ImportManager().getModules(modules, 'c3')

        :param modules: The ordered definition of modules
        :param alias: The module reference in the above JS and CSS dictionaries
        :param folder: Optional. The folder name
        :param module_details: Optional. The module definition. Default check in the Javascript modules

        :return: The list of modules
        """
        if isinstance(alias, dict):
            alias = alias['alias']

        if module_details is None or alias not in module_details:
            module_details = dict(JS_IMPORTS)
        import_ref = JS_IMPORTS
        if self.page.ext_packages is not None and alias in self.page.ext_packages:
            import_ref = self.page.ext_packages

        for mod in module_details[alias]['modules']:
            if 'version' not in mod:
                # take the version from the main package definition
                mod['version'] = import_ref[alias]["version"] if alias in import_ref else CSS_IMPORTS[alias]["version"]
            script = "".join([mod['path'] % mod, mod['script']])
            if 'url' in module_details[alias]:
                modules["%s/%s" % (module_details[alias]['url'], script)] = True
            else:
                modules[r"%s\%s" % (STATIC_PATH.replace("\\", "/"), script)] = True
        for req in module_details.get(alias, {}).get('req', []):
            self.getModules(modules, req, folder, module_details)
        return modules

    def getReq(self, mod: str, modules: List[dict], import_hierarchy: Optional[dict] = None,
               use_require_js: bool = False):
        """
        Set the list pf required modules for a given alias to the modules list.

        Usage::

          deps = []
          page.imports.getReq("c3", deps)
          print(deps)

        :param mod: The alias of the external package
        :param modules: The list of packages aliases in the inverse dependency order
        :param import_hierarchy: Optional. The package definition (Javascript | CSS) from the above import list
        :param use_require_js: Optional. Define if this is using requirejs to load imports. Default False
        """
        import_hierarchy = import_hierarchy or JS_IMPORTS
        if isinstance(mod, dict):
            # This will allow different versions of packages according to the modules
            # For example NVD3 cannot use any recent version of D3
            if 'version' in mod:
                if self.page is not None and self.page.verbose:
                    logging.warning("Setting %(alias)s to version %(version)s" % mod)
                if self.reqVersion.get(mod['alias']) is None or mod['version'] < self.reqVersion[mod['alias']]:
                    self.reqVersion[mod['alias']] = mod['version']
                new_main_for_alias, new_main_for_alias_css = collections.OrderedDict(), collections.OrderedDict()
                for path in self.jsImports[mod['alias']]['main']:
                    for v in self.jsImports[mod['alias']]['versions']:
                        new_main_for_alias[path.replace(v, self.reqVersion[mod['alias']])] = self.reqVersion[
                            mod['alias']]
                if mod['alias'] in self.cssImports:
                    for path in self.cssImports[mod['alias']]['main']:
                        for v in self.cssImports[mod['alias']]['versions']:
                            new_main_for_alias_css[path.replace(v, self.reqVersion[mod['alias']])] = self.reqVersion[
                                mod['alias']]
                    self.cssImports[mod['alias']]['main'] = new_main_for_alias_css
                # Store the new dictionary with the key and version updated for the module
                self.jsImports[mod['alias']]['main'] = new_main_for_alias
                for i, path in enumerate(self.jsImports[mod['alias']]['dep']):
                    for v in self.jsImports[mod['alias']]['versions']:
                        path = path.replace(v, self.reqVersion[mod['alias']])
                    self.jsImports[mod['alias']]['dep'][i] = path
            mod = mod['alias']
        modules.append(mod)
        # if self.page.ext_packages is not None and mod in self.page.ext_packages:
        #  import_hierarchy = self.page.ext_packages
        req_key = "req"
        if use_require_js:
            if "req_js" in import_hierarchy.get(mod, {}):
                req_key = "req_js"
        for req in import_hierarchy.get(mod, {}).get(req_key, []):
            self.getReq(req, modules, import_hierarchy, use_require_js=use_require_js)

    def cleanImports(self, imports: List[str], import_hierarchy: Optional[dict] = None, use_require_js: bool = False):
        """
        Remove the underlying imports to avoid duplicated entries.

        Usage::

          >>> ImportManager().cleanImports(['c3'], JS_IMPORTS)
        ['jquery', 'd3', 'c3']

        :param imports: An array with the list of aliases for the external packages
        :param import_hierarchy: Optional. The package definition (Javascript | CSS) from the above import list
        :param use_require_js: Optional. Define if this is using requirejs to load imports. Default False

        :return: Return the list with the full list of aliases (including dependencies)
        """
        import_resolved, polyfills = [], []
        for mod in imports:
            self.getReq(mod, import_resolved, import_hierarchy or JS_IMPORTS, use_require_js=use_require_js)
        for a in set(import_resolved):
            if a in PACKAGE_STATUS:
                if not PACKAGE_STATUS[a].get("allowed", True):
                    raise ValueError("Package %s not allowed" % a)

                if self.page is not None and "info" in PACKAGE_STATUS[a]:
                    # Change this to be info logs instead of warnings
                    logging.info("%s: %s" % (a, PACKAGE_STATUS[a]["info"]))
            occurrences = [j for j, x in enumerate(import_resolved) if x == a]
            if len(occurrences) > 1:
                for j in occurrences[::-1][1:]:
                    import_resolved.pop(j)
            if JS_IMPORTS.get(a, {}).get("polyfill"):
                import_resolved.remove(a)
                polyfills.append(a)
        local_pkgs, ext_pkgs = [], []
        for pkg in import_resolved[::-1]:
          if pkg.startswith("local_"):
            local_pkgs.append(pkg)
          else:
            ext_pkgs.append(pkg)
        return polyfills + ext_pkgs + local_pkgs

    def cssResolve(self, css_aliases: List[str], local_css: Optional[dict] = None, excluded: List[str] = None):
        """
        Return the list of CSS modules to add to the header.

        Usage::

          >>> ImportManager().cssResolve(['c3'])
        '<link rel="stylesheet" href="/static/c3/0.6.12/c3.min.css" type="text/css">'

        :param css_aliases: An array with the list of aliases for the external packages
        :param local_css: Optional. The external file overrides with the full path
        :param excluded: Optional. Packages excluded from the result object (mandatory for some frameworks
          already onboarding modules).

        :return: The string to be added to the header.
        """
        css = []
        self.__add_imports([(None, None, self.page.ext_packages)])
        # Import hierarchy will rely on the JS_IMPORT definition.
        css_aliases = [c for c in self.cleanImports(css_aliases, JS_IMPORTS) if c in self.cssImports or c in _SERVICES]
        for css_alias in css_aliases:
            if excluded is not None and css_alias in excluded:
                continue

            if not self.online:
                self.pkgs.get(css_alias).set_local(static_url=self.static_url)
            if css_alias in _SERVICES:
                # Add services url
                for service in _SERVICES[css_alias].get('css', []):
                    css.append('<link rel="stylesheet" href="%s">' % service)
                continue

            for urlModule in list(self.cssImports[css_alias]['main']):
                if self.page._node_modules is not None:
                    node_sub_path = CSS_IMPORTS.get(css_alias, {}).get('register', {}).get('npm_path')
                    if node_sub_path is not None:
                        css_file = os.path.split(urlModule)[1]
                        npm_alias = CSS_IMPORTS[css_alias]['register'].get('npm', css_alias)
                        package_path = os.path.join(
                            self.page._node_modules[0], "node_modules", npm_alias, node_sub_path, css_file)
                        if os.path.exists(package_path):
                            urlModule = os.path.join(
                                self.page._node_modules[1], npm_alias, node_sub_path, css_file).replace("\\", "/")
                if os.path.isabs(urlModule) and Path(urlModule).exists():
                    with open(urlModule, "rb") as fp:
                        base64_bytes = base64.b64encode(fp.read())
                        base64_message = base64_bytes.decode('ascii')
                        urlModule = "data:text/css;base64,%s" % base64_message
                elif self.self_contained:
                    try:
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                            'Accept-Encoding': 'none',
                            'Accept-Language': 'en-US,en;q=0.8',
                            'Connection': 'keep-alive'}
                        request = Request(urlModule, None, headers)
                        with urlopen(request) as response:
                            base64_bytes = base64.b64encode(response.read())
                            base64_message = base64_bytes.decode('ascii')
                            urlModule = "data:text/css;base64,%s" % base64_message
                    except Exception as err:
                        print(urlModule)
                        print(traceback.format_exc())

                css.append('<link rel="stylesheet" href="%s" type="text/css">' % urlModule)
        if local_css is not None:
            for css_file in local_css:
                css.append('<link rel="stylesheet" href="%s" type="text/css">' % css_file)
        return "\n".join(css)

    def cssURLs(self, css_str: str):
        """
        Retrieve the list of CSS dependencies URL from a header.

        :param css_str: The CSS String in the page

        :return: A Python list with all the CSS external URL to be imported.
        """
        return re.findall('<link rel="stylesheet" href="(.*?)" type="text/css">', css_str)

    def jsResolve(self, js_aliases: List[str], local_js: Optional[dict] = None, excluded: Optional[List[str]] = None,
                  local_title=""):
        """Return the list of Javascript modules to add to the header.

        Usage::

          >>> ImportManager().jsResolve(['c3'])
        '<script language="javascript" type="text/javascript" src="/static/jquery/3.4.1/jquery.min.js"></script>\n<script language="javascript" type="text/javascript" src="/static/d3/5.9.7/d3.min.js"></script>\n<script language="javascript" type="text/javascript" src="/static/c3/0.6.12/c3.min.js"></script>'

        :param js_aliases: An array with the list of aliases for the external packages
        :param local_js: Optional. The external file overrides with the full path
        :param excluded: Optional. Packages excluded from the result object
           (mandatory for some frameworks already onboarding modules)
        :param local_title: Optional. Local JavaScript file title description

        :return: The string to be added to the header
        """
        from epyk.conf.global_settings import (ASSETS_SPLIT, ASSETS_SPLIT_MINIFY, ASSETS_PRINT_PATHS, ASSETS_OUT_PATH,
                                               ASSETS_STATIC_ROUTE, ASSETS_STATIC_PATH, ASSETS_STATIC_JS)

        js = []
        if self.set_exports:
            # Fix for missing require function
            js.append("<script>var exports = {}; function require(a){return window[a]}</script>")
        # self.__add_imports([(None, None, self._report.ext_packages)])
        js_aliases = self.cleanImports(js_aliases, JS_IMPORTS)
        for js_alias in js_aliases:
            if excluded is not None and js_alias in excluded:
                continue

            if not self.online:
                self.pkgs.get(js_alias).set_local(static_url=self.static_url)
            extra_configs = "?%s" % self.moduleConfigs[js_alias] if js_alias in self.moduleConfigs else ""
            for url_module in list(self.jsImports.get(js_alias, {}).get('main', [])):
                if self.page._node_modules is not None:
                    node_sub_path = JS_IMPORTS.get(js_alias, {}).get('register', {}).get('npm_path')
                    if node_sub_path is not None:
                        js_file = os.path.split(url_module)[1]
                        npm_alias = JS_IMPORTS[js_alias]['register'].get('npm', js_alias)
                        package_path = os.path.join(
                            self.page._node_modules[0], "node_modules", npm_alias, node_sub_path, js_file)
                        if os.path.exists(package_path):
                            url_module = os.path.join(
                                self.page._node_modules[1], npm_alias, node_sub_path, js_file).replace("\\", "/")

                # if '/mode/' in url_module:
                #  js.append('<script type="module" language="javascript" src="%s%s"></script>' % (url_module, extra_configs))
                mod_type = self.jsImports[js_alias]['type'].get(url_module, "text/javascript")
                mod_title = os.path.split(url_module)[-1]
                if os.path.isabs(url_module) and not url_module.startswith("/static"):
                    file_name, file_extension = os.path.splitext(url_module)
                    if not file_extension.endswith(".js"):
                        continue

                    self.jsImports[js_alias]['title'] = os.path.split(url_module)[-1]
                    module_exists = os.path.exists(url_module)
                    if module_exists:
                        with open(url_module, "rb") as fp:
                            if mod_type == "text/javascript":
                                # export cannot be used in javascript scripts not set as modules
                                tmp_file = []
                                for line in fp.readlines():
                                    for m_expr, m_rep in {b"^export ": b""}.items():
                                        line = re.sub(m_expr, m_rep, line)
                                    tmp_file.append(line)
                                js_content = b"".join(tmp_file)
                            else:
                                js_content = fp.read()
                            if ASSETS_SPLIT:
                                js_path = Path(ASSETS_STATIC_PATH) / ASSETS_STATIC_JS
                                if not js_path.exists():
                                    js_path.mkdir(parents=True, exist_ok=True)
                                with open(js_path / self.jsImports[js_alias]['title'], "wb") as fp:
                                    fp.write(js_content)
                                url_module = "%s/%s/%s" % (ASSETS_STATIC_ROUTE, ASSETS_STATIC_JS, self.jsImports[js_alias]['title'])
                            else:
                                base64_bytes = base64.b64encode(js_content)
                                base64_message = base64_bytes.decode('ascii')
                                url_module = "data:text/js;base64,%s" % base64_message
                    else:
                        logging.warning("Missing File: %s" % url_module)
                elif self.self_contained:
                    try:
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                            'Accept-Encoding': 'none',
                            'Accept-Language': 'en-US,en;q=0.8',
                            'Connection': 'keep-alive'}
                        request = Request(url_module, None, headers)
                        with urlopen(request) as response:
                            base64_bytes = base64.b64encode(response.read())
                            base64_message = base64_bytes.decode('ascii')
                            url_module = "data:text/js;base64,%s" % base64_message
                    except Exception as err:
                        logging.error(url_module)
                        logging.error(traceback.format_exc())
                if self.pkgs.get(js_alias).defer:
                    js.append(
                        '<script title="%s" language="javascript" type="%s" src="%s%s" defer></script>' % (
                            mod_title, mod_type, url_module, extra_configs))
                elif self.pkgs.get(js_alias).asynchrone:
                    js.append(
                        '<script title="%s" language="javascript" type="%s" src="%s%s" async></script>' % (
                            mod_title, mod_type, url_module, extra_configs))
                else:
                    js.append(
                        '<script title="%s" language="javascript" type="%s" src="%s%s"></script>' % (
                        mod_title, mod_type, url_module, extra_configs))
        if local_js is not None and len(local_js) > 0:
            for local_js_file in local_js:
                js.append('<script title="%s" language="javascript" type="text/javascript" src="%s"></script>' % (
                    local_title, local_js_file))
        return "\n".join(js)

    def jsURLs(self, expr: str):
        """
        Retrieve the list of Javascript dependencies URL from a header.

        :param expr: The Javascript String in the page

        :return: A Python list with all the Javascript external URL to be imported.
        """
        return re.findall('<script language="javascript" type="text/javascript" src="(.*?)"></script>', expr)

    def getFiles(self, css_alias: List[str], js_alias: List[str]):
        """
        Retrieve the package definition from the list of module aliases

        Usage::

          >>> ImportManager().getFiles(['c3'], ['c3'])
        f['css'][0]['file']['script']

        :param css_alias: An array with the list of aliases for the CSS external packages
        :param js_alias: An array with the list of aliases for the Js external packages

        :return: A dictionary with the CSS and JS files definition.
        """
        files = {'css': [], 'js': []}
        mod_css, mod_js = {}, {}
        for alias, details in CSS_IMPORTS.items():
            mod_css[alias] = []
            for module in details['modules']:
                mod_css[alias].append(
                    {'version': module.get('version', ''), 'alias': alias, 'file': module,
                     'website': details.get('website', ''),
                     'status': details.get('status', '')})
        for alias, details in JS_IMPORTS.items():
            mod_js[alias] = []
            for module in details['modules']:
                mod_js[alias].append(
                    {'version': module.get('version', ''), 'alias': alias, 'file': module,
                     'website': details.get('website', ''),
                     'status': details.get('status', '')})
        for css_file in self.cleanImports(css_alias, CSS_IMPORTS):
            files['css'].extend(mod_css[css_file])
        for js_file in self.cleanImports(js_alias, JS_IMPORTS):
            files['js'].extend(mod_js[js_file])
        return files

    def cssGetAll(self):
        """
        To retrieve the full list of available modules on the server.

        This will return the dependencies as they should be included in the HTML page.
        The order and the path resolution is already performed.

        If split is True the generated css file will be not included.

        Usage::

          print(page.imports.cssGetAll())
        """
        return self.cssResolve(set(CSS_IMPORTS.keys()))

    def jsGetAll(self):
        """
        To retrieve the full list of available modules on the server.

        This will return the dependencies as they should be included in the HTML page.
        The order and the path resolution is already performed.

        If split is True the generated JS file will be not included.

        Usage::

          print(page.imports.jsGetAll())
        """
        return self.jsResolve(set(JS_IMPORTS.keys()))

    def getFullPackage(self, alias: str, version: Optional[str] = None, static_path: Optional[str] = None,
                       reload: bool = False):
        """Download a full package (CSS and JS) locally for a server or full offline mode.

        Usage::

          Imports.ImportManager(report=Report()).getFullPackage('font-awesome')

        :param alias: The package reference in the above list
        :param version: Optional. The package version to retrieve
        :param static_path: Optional. The path in which the files should be copied to
        :param reload: Optional. Flag to force the package reloading if the folder already exists. Default False

        :return: The Python Import manager.
        """

        import zipfile
        import shutil
        import io
        import os

        if not hasattr(self.page, "py"):
            from epyk.core.py.PyRest import PyRest
            webscrapper = PyRest().webscrapping
        else:
            webscrapper = self.page.py.requests.webscrapping

        if 'package' in JS_IMPORTS[alias]:
            if 'version' not in JS_IMPORTS[alias]['modules'][0]:
                JS_IMPORTS[alias]['modules'][0]['version'] = JS_IMPORTS[alias]['version']
            version_dict = {'version': JS_IMPORTS[alias]['modules'][0]['version'] if version is None else version}
            package_path = JS_IMPORTS[alias]['package']['zip'] % version_dict
            if static_path is None:
                static_path = os.path.join(
                    os.path.dirname(__file__), '..', '..', 'static', JS_IMPORTS[alias]['package']['folder'])
            else:
                static_path = os.path.join(static_path, "static")
            if not os.path.exists(static_path):
                # Create the destination folders if missing
                os.makedirs(static_path)
            dst_path = os.path.join(
                static_path, JS_IMPORTS[alias]['package'].get('folder', ''),
                JS_IMPORTS[alias]['package'].get('path', '%(version)s') % version_dict)
            v_reload_path = True
            if os.path.exists(dst_path):
                if not reload:
                    v_reload_path = False
                else:
                    shutil.rmtree(dst_path)

            if v_reload_path:
                logging.warning("  > Downloading package %s" % package_path)
                r = webscrapper(package_path)
                z = zipfile.ZipFile(io.BytesIO(r))
                z.extractall(static_path)
                if JS_IMPORTS[alias]['package']['root'] is not None:
                    root = JS_IMPORTS[alias]['package']['root'] % version_dict
                    shutil.copytree(os.path.join(static_path, root), dst_path)
                    shutil.rmtree(os.path.join(static_path, root))
                logging.warning("  < Package %s. Done ! " % alias)
            else:
                logging.warning("  < Package %s already loaded " % alias)
        return self

    def setVersion(self, alias: str, version: str, js: Optional[dict] = None, css: Optional[dict] = None,
                   verbose: bool = None) -> bool:
        """Allow the use of different version of a package.
        This will change the Import important to the Python env.

        Usage::

          page.imports.setVersion(page.imports.pkgs.popper_js.alias, "1.00.0")

        :param alias: The package reference in the above list
        :param version: The new version to be used globally
        :param js: Optional. The JavaScript packages to be added
        :param css: Optional. The CSS packages to be added
        :param verbose: Optional. Display version details (default True)
        """
        global CSS_IMPORTS, JS_IMPORTS

        self.reqVersion[alias] = version
        current_version = JS_IMPORTS.get(alias, CSS_IMPORTS.get(alias, {})).get('version')
        if version == current_version:
            return False

        if verbose:
            print("Moving %s from %s to %s" % (alias, current_version, version))
        if alias in CSS_IMPORTS:
            CSS_IMPORTS[alias]['version'] = version
            for module in CSS_IMPORTS[alias].get('modules', []):
                module['version'] = version
        if alias in JS_IMPORTS:
            JS_IMPORTS[alias]['version'] = version
            for module in JS_IMPORTS[alias].get('modules', []):
                module['version'] = version
        if js is not None:
            if not js:
                if alias in JS_IMPORTS:
                    del self.jsImports[alias]
                    del JS_IMPORTS[alias]

            else:
                self.jsImports[alias] = {'main': collections.OrderedDict(), 'dep': [], 'versions': version}
                for k, v in js.items():
                    JS_IMPORTS[alias][k] = v
                    for module in js["modules"]:
                        module["path"] = module["path"] % {"version": version}
                        self.jsImports[alias]['main'][global_settings.IMPORTS_EXPR % module] = version
        if css is not None:
            if not css:
                if alias in CSS_IMPORTS:
                    del self.cssImports[alias]
                    del CSS_IMPORTS[alias]

            else:
                for k, v in css.items():
                    CSS_IMPORTS.setdefault(alias, {})[k] = v
                for module in css["modules"]:
                    module["path"] = module["path"] % {"version": version}
                    self.cssImports.setdefault(alias, {}).setdefault('main', {})[
                        global_settings.IMPORTS_EXPR % module] = version
        return True

    def addPackage(self, alias: str, config: dict):
        """Add a new package or update an existing one with new parameters.
        Only few parameters are available here in order to limit the changes.

        Usage::

          i.addPackage('test',
          {
            'req': [{'alias': 'd3'}],
            'modules': [
              {'script': 'dc.min.css', 'version': '3.0.9', 'path': 'dc/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
              {'script': 'dc.min.js', 'version': '3.0.9', 'path': 'dc/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
            ]},
          )

        :param alias: The package alias
        :param config: The Python dictionary with the package details

        :return: The import Manager.
        """

        global CSS_IMPORTS
        global JS_IMPORTS

        mod_entry = {'css': {}, 'js': {}}
        for mod in config.get('modules', []):
            if "version" not in mod and "version" in config:
                mod["version"] = config["version"]
            if mod['script'].endswith(".css"):
                if "cdnjs" not in mod:
                    mod["cdnjs"] = CDNJS_REPO
                mod_entry['css'].setdefault('modules', []).append(mod)
                if 'req' in config:
                    for req in config['req']:
                        if req['alias'] in CSS_IMPORTS:
                            mod_entry['css'].setdefault('req', []).append(req)
            elif mod['script'].endswith(".js") or mod['script'].startswith("js") or mod['script'].startswith("api"):
                if "cdnjs" not in mod:
                    mod["cdnjs"] = CDNJS_REPO
                mod_entry['js'].setdefault('modules', []).append(mod)
                if 'register' in config:
                    mod_entry['js']['register'] = config['register']
                if 'req' in config:
                    for req in config['req']:
                        if req['alias'] in JS_IMPORTS:
                            mod_entry['js'].setdefault('req', []).append(req)
        if len(mod_entry['css']) > 0:
            CSS_IMPORTS.setdefault(alias, {}).update(mod_entry['css'])
            self.cssImports[alias] = {
                "main": collections.OrderedDict(), 'versions': [config.get("version", "")], 'dep': [],
                "type": collections.OrderedDict()}
            for pkg in mod_entry.get('css', {}).get("modules", []):
                self.cssImports[alias]["main"][
                    script_cdnjs_path(alias, pkg)] = pkg.get("version", config["version"])
                if "type" in pkg:
                    self.cssImports[alias]["type"][script_cdnjs_path(alias, pkg)] = pkg["type"]
                else:
                    self.cssImports[alias]["type"][script_cdnjs_path(alias, pkg)] = 'stylesheet'
        if len(mod_entry['js']) > 0:
            JS_IMPORTS.setdefault(alias, {}).update(mod_entry['js'])
            JS_IMPORTS[alias]["version"] = config.get("version", "")
            self.jsImports[alias] = {
                "main": collections.OrderedDict(), 'versions': [JS_IMPORTS[alias]["version"]], 'dep': [],
                "type": collections.OrderedDict()}
            for pkg in mod_entry['js']["modules"]:
                self.jsImports[alias]["main"][script_cdnjs_path(alias, pkg)] = pkg.get("version", config.get("version", ''))
                if "type" in pkg:
                    self.jsImports[alias]["type"][script_cdnjs_path(alias, pkg)] = pkg["type"]
                else:
                    self.jsImports[alias]["type"][script_cdnjs_path(alias, pkg)] = 'text/javascript'
        return self

    def to_requireJs(self, data: dict, excluded_packages: Optional[list] = None):
        """

        :param data: The Report modules to resolve
        :param excluded_packages: Optional. The packages to exclude
        """
        deps_level, alias_to_name, alias_to_var, name_to_alias, results = {}, {}, {}, {}, {'jsFrgs': data['jsFrgs'],
                                                                                           'paths': {}}
        m_versions = {}
        # Check first if some specific versions are required for the packages
        for m in self.page.jsImports:
            import_ref = JS_IMPORTS
            if self.page.ext_packages is not None and m in self.page.ext_packages:
                import_ref = self.page.ext_packages
            req_alias = "req_js" if "req_js" in import_ref[m] else "req"
            for req in import_ref[m].get(req_alias, []):
                if 'version' in req:
                    m_versions[req['alias']] = req['version']
        # Produce the dependency tree for requirejs
        for m in self.cleanImports(self.page.jsImports, JS_IMPORTS, use_require_js=True):
            if m.startswith("local_") or (excluded_packages is not None and m in excluded_packages):
                continue

            if not self.online:
                self.pkgs.get(m).set_local(static_url=self.static_url)

            import_ref = JS_IMPORTS
            if self.page.ext_packages is not None and m in self.page.ext_packages:
                import_ref = self.page.ext_packages
            if 'register' in import_ref[m]:
                alias = import_ref[m]['register'].get('alias', m)
                first_module = import_ref[m]['modules'][0]
                if 'version' not in first_module:
                    first_module['version'] = import_ref[m]['version']
                if m in m_versions:
                    first_module['version'] = m_versions[m]
                if not self.online:
                    self.pkgs.get(m).set_local(static_url=self.static_url)
                    results['paths']["'%s'" % alias] = list(self.jsImports[m]["main"].keys())[0][:-3]
                else:
                    results['paths']["'%s'" % alias] = "%s/%s%s" % (
                        first_module["cdnjs"], first_module['path'] % first_module,
                        import_ref[m]['register'].get('module', first_module['script'][:-3]))
                alias_to_name[m] = alias
                alias_to_var[m] = import_ref[m]['register'].get('variable', alias)
                name_to_alias[alias] = m
                req_alias = 'req_js' if 'req_js' in import_ref[m] else "req"
                if req_alias in import_ref[m]:
                    req_levels = [deps_level.get(req_def["alias"], -1) for req_def in import_ref[m][req_alias]]
                    deps_level[m] = max(req_levels) + 1
                else:
                    deps_level[m] = 0
        # Create the chains of modules to be loaded
        level, group = None, []
        for k, v in sorted(deps_level.items(), key=lambda item: item[1])[::-1]:
            if level is None:
                level = v
            if level != v:
                for g, var in group:
                    if 'init_fnc' in JS_IMPORTS[name_to_alias[g]]['register']:
                        results['jsFrgs'] = "%s; %s" % (
                        JS_IMPORTS[name_to_alias[g]]['register']['init_fnc'], results['jsFrgs'])
                results['jsFrgs'] = "require(['%s'], function (%s) { %s })" % (
                    "', '".join([g for g, _ in group]), ", ".join([g for _, g in group]), results['jsFrgs'])
                level, group = v, [(alias_to_name[k], alias_to_var[k])]
            else:
                group.append((alias_to_name[k], alias_to_var[k]))
        if group:
            for g, var in group:
                import_ref = JS_IMPORTS
                if self.page.ext_packages is not None and name_to_alias[g] in self.page.ext_packages:
                    import_ref = self.page.ext_packages
                if 'init_fnc' in import_ref[name_to_alias[g]]['register']:
                    results['jsFrgs'] = "%s; %s" % (
                    import_ref[name_to_alias[g]]['register']['init_fnc'], results['jsFrgs'])
            results['jsFrgs'] = "require(['%s'], function (%s) { %s })" % (
                "', '".join([g for g, _ in group]), ", ".join([g for _, g in group]), results['jsFrgs'])
        return results

    def show(self, all: bool = False):
        """Show all the underlying packages used in a report or available in the framework.

        :param all: Optional. A flag to specify if only the one requested in the report should be displayed
        """
        packages = {}
        if not all:
            for imp, repo in [(self.page.cssImport, CSS_IMPORTS), (self.page.jsImports, JS_IMPORTS)]:
                pkg = self.cleanImports(imp, repo)
                for c in pkg:
                    for s in repo[c].get('modules', []):
                        if 'version' not in s:  # propagate the version number if not supplied from JS definition
                            s["version"] = JS_IMPORTS[c]['version'] if c in JS_IMPORTS else CSS_IMPORTS[c]['version']
                        s['path'] = s['path'] % s
                        packages.setdefault(c, []).append({"script": global_settings.IMPORTS_EXPR % s, 'version': s['version']})
        else:
            for mod in [CSS_IMPORTS, JS_IMPORTS]:
                for c, pkg in mod.items():
                    for s in pkg.get('modules', []):
                        if 'version' not in s:  # propagate the version number if not supplied from JS definition
                            s["version"] = JS_IMPORTS[c]['version'] if c in JS_IMPORTS else CSS_IMPORTS[c]['version']
                        s['path'] = s['path'] % s
                        packages.setdefault(c, []).append(
                            {"script": global_settings.IMPORTS_EXPR % s, 'version': s['version']})
        return packages

    def google_products(self, products: List[str], api_key: Optional[str] = None,
                        site_key: str = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"):
        """Enable the google predefined products.
        Those are by default disabled as they are sharing data with Google.

        TODO: Add the use of the API Key.

        Usage::

          page.imports.google_products(['charts'])
          page.imports.google_products(['maps'])
          page.imports.google_products(['tables'])

          https://developers.google.com/recaptcha/docs/faq#id-like-to-run-automated-tests-with-recaptcha.-what-should-i-do

        :param products: The various Google products to enable in the report
        :param api_key: Optional. The Google developer API key
        :param site_key: Optional. The Google site key: https://developers.google.com/recaptcha/docs/v3
        """
        global JS_IMPORTS

        for p in products:
            for m in GOOGLE_EXTENSIONS[p].get("modules", []):
                m["script"] = m["script"] % {"api_key": api_key, 'site_key': site_key}
            self.addPackage("google-%s" % p, GOOGLE_EXTENSIONS[p])
            JS_IMPORTS["google-%s" % p] = GOOGLE_EXTENSIONS[p]
            if 'launcher' in GOOGLE_EXTENSIONS[p]:
                self.page.properties.js.add_builders(GOOGLE_EXTENSIONS[p]['launcher'])
        self.page._with_google_imports = True

    def locals(self, aliases: List[str], end_points: Optional[str] = None):
        """Short circuit the import mechanism and retrieve the selected ones from a local static path.
        This could help on the debugging and the improvement of the packages before submitting them for review.

        :param aliases: The list of aliases
        :param end_points: Optional. The end point on the server (The module static_path as default)
        """
        global JS_IMPORTS
        global CSS_IMPORTS

        logging.warning("Routing packages %s locally this should not be put on a server !" % aliases)
        for alias in aliases:
            if alias in JS_IMPORTS:
                for m in JS_IMPORTS[alias]['modules']:
                    m.update({'path': '', 'cdnjs': end_points or self.static_url})
        for alias in aliases:
            if alias in CSS_IMPORTS:
                for m in CSS_IMPORTS[alias]['modules']:
                    m.update({'path': '', 'cdnjs': end_points or self.static_url})

    @property
    def pkgs(self) -> ImportPackages:
        """Shortcut properties to the various package definitions.
        This can be used in the script in order to change the path of the version of any external modules used.
        """
        return ImportPackages(self.jsImports, self.cssImports, page=self.page)

    def website(self, alias: str) -> str:
        """Get the official website for a JavaScript library.

        :param alias: The JavaScript module alias (usually the one used by npm)
        """
        return JS_IMPORTS.get(alias, {}).get('website', "")

    def append_to(self, alias: str, js_modules: List[dict] = None, css_modules: List[dict] = None, version: str = None):
        """Update an existing configuration by adding addon scripts or styles.

        :param alias: NPM package alias
        :param js_modules: JavaScript modules extension
        :param css_modules: CSS styles extension
        :param version: The package version (if different)
        """
        if js_modules is not None:
            version = version or JS_IMPORTS[alias]["version"]
            cdnjs = None
            if JS_IMPORTS[alias]['modules']:
                cdnjs = JS_IMPORTS[alias]['modules'][0].get("cdnjs")
            for js_module in js_modules:
                if "cdnjs" not in js_module and cdnjs is not None:
                    js_module["cdnjs"] = cdnjs
                self.jsImports[alias]["main"][script_cdnjs_path(alias, js_module)] = version
                self.jsImports[alias]["type"][script_cdnjs_path(alias, js_module)] = 'text/javascript'
        if css_modules is not None:
            version = version or CSS_IMPORTS[alias].get("version") or JS_IMPORTS[alias]["version"]
            cdnjs = None
            if CSS_IMPORTS[alias]['modules']:
                cdnjs = CSS_IMPORTS[alias]['modules'][0].get("cdnjs")
            for css_module in css_modules:
                if "cdnjs" not in css_module and cdnjs is not None:
                    css_module["cdnjs"] = cdnjs
                self.jsImports[alias]["main"][script_cdnjs_path(alias, css_module)] = version
                self.jsImports[alias]["type"][script_cdnjs_path(alias, css_module)] = 'stylesheet'

    def attach_data(self, name: str, data: Any, **kwargs):
        """Attach data to a common data.

        :param name: Main JavaScript variable name
        :param data: JavaScript Data written to the file
        :param kwargs: Optional. Other key / values data to register to the file
        """
        from epyk.conf.global_settings import ASSETS_SPLIT, ASSETS_STATIC_DATA, ASSETS_STATIC_PATH, ASSETS_STATIC_ROUTE
        main_data = ["var %s = %s;" % (name.upper(), json.dumps(data))]
        for k, v in kwargs.items():
            main_data.append("var %s = %s;" % (k.upper(), json.dumps(v)))
        if ASSETS_SPLIT:
            data_path = Path(ASSETS_STATIC_PATH) / ASSETS_STATIC_DATA
            if not data_path.exists():
                data_path.mkdir(parents=True, exist_ok=True)
            with open(data_path / ("%s.js" % name), "w") as fp:
                fp.write("\n".join(main_data))
            self.page.headers.add_script(
                "%s/%s/%s.js" % (ASSETS_STATIC_ROUTE, ASSETS_STATIC_DATA, name), {"title": "static data"})
        else:
            self.page.properties.js.add_constructor(name, "\n".join(main_data))
        return self.page.js.getVar(name.upper())

    def insert_path(self, path: str, n: int = 0) -> bool:
        """Add a path to the global path.

        :param path: Path to add
        :param n: Position in the resources list
        """
        if not Path(path).exists():
            return False

        for p in global_settings.PRIMARY_RESOURCE_PATHS:
            if p == path:
                return False

        global_settings.PRIMARY_RESOURCE_PATHS.insert(n, path)
        return True


class Package:

    @property
    def all(self):
        """
        Get the definition of the package defined in this version of the package.

        This will simplify the compatibility with the interface.
        """
        return ImportManager().pkgs

    @classmethod
    def avoid_cache(cls, name: str) -> str:
        """
        This will allow the creation and the change of external packages usually cached by the browser.

        It will add a unique ID to make sure the browser will always try to reload it.

        Usage::

          return jsonify({
            "import_pkg": pk.package.avoid_cache(r"/static/formatters-numbers-new.js")})

        :param name: The package name
        """
        import random

        return "%s?version=%s" % (name, random.random())


def save_resources(out_path: str, aliases: List[str] = None, headers = None):
    """Copy the external resources to an specific directory.

    :param out_path:
    :param aliases:
    """
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
    if aliases is None:
        aliases = set(JS_IMPORTS.keys()).union(set(CSS_IMPORTS.keys()))
    for alias in aliases:
        for pkg_gro in [CSS_IMPORTS, JS_IMPORTS]:
            if alias in pkg_gro:
                pkg_def = pkg_gro[alias]
                for f in pkg_def.get("modules", []):
                    f_path = "%(cdnjs)s/%(path)s%(script)s" % f
                    if "version" in f:
                        r_path = f_path % f
                    elif "version" not in pkg_def and "version" in JS_IMPORTS.get(alias, {}):
                        r_path = f_path % JS_IMPORTS[alias]
                    else:
                        if "version" not in pkg_def:
                            continue

                        r_path = f_path % pkg_def
                    request = Request(r_path, None, headers)
                    try:
                        with urlopen(request) as response:
                            with open(r"%s\%s" % (out_path, f["script"]), "wb") as fp:
                                fp.write(response.read())
                    except Exception as err:
                        logging.warning("Error with %s: %s" % (alias, r_path))
