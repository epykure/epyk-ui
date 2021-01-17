"""
Core module in charge of linking the Python report request to the corresponding external pacakges required.

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

try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request, ProxyHandler, build_opener, install_opener
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError, ProxyHandler, build_opener, install_opener


# To fully disable the automatic pip install request when a package is missing
AUTOLOAD = False
PROXY = ''
PCK_REPO = ''
STATIC_PATH = "/static"


def requires(name, reason='Missing Package', install=None, package=None, raise_except=False, source_script=None, pip_attrs=None):
  """
  Description:
  ------------
  System module

  Import the necessary external packages and provide explicit message to find a way to solve this error message.
  This method should also explain why this module is required to make sure this is really expected to get an error.

  Attributes:
  ----------
  :param name:
  :param reason:
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
        raise Exception(err)

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
      raise Exception(err)


def load_package(package_name, pip_attrs=None, action='install'):
  """
  Description:
  ------------
  Force the package to be installed manually to the currently python distribution.
  This will run a pip command to the running python set up

  Example
  load_package("pandas")

  Related Pages:

      https://pypi.org/

  Attributes:
  ----------
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
  """
  Description:
  ------------
  Returns the list of packages installed on the running Python distribution

  This will require an internet connection as it will run the pip command behind the scene.
  It will return in the console a table with the status of the obsolescence of all the python packages

  Example
  installed_packages()
  """
  import subprocess
  subprocess.call(["pip", 'list', '-o'])


# Module variable to be updated in environment to share info related to packages.
PACKAGE_STATUS = {}


CDNJS_REPO = 'https://cdnjs.cloudflare.com/ajax/libs'

# Mapping to match the folder names in Jupyter
# If the folder are the same as the alias it is not included in this mapping
# Purpose is to not double load the modules in Jupyter
NOTEBOOK_MAPPING = {
  'MathJax': 'mathjax',
  'jquery-ui': 'jqueryui',
}


TABULATOR_EXTENSIONS = '0.0.27'


JS_IMPORTS = {
  # numbers formatting
  'accounting': {
    "repository": "https://github.com/openexchangerates/accounting.js",
    "version": "0.4.1",
    'v_prefix': 'v',
    'modules': [
      {'script': 'accounting.min.js', 'path': 'accounting.js/%(version)s/', 'cdnjs': CDNJS_REPO},
    ],
    'website': 'https://openexchangerates.github.io/accounting.js/'},

  # QR Code
  'qrcodejs': {
    'version': '1.0.0',
    'modules': [
      {'script': 'qrcode.min.js', 'path': 'qrcodejs/%(version)s/', 'cdnjs': CDNJS_REPO},
    ],
    'repository': 'https://github.com/llyys/qrcodejs',
    'website': 'https://davidshimjs.github.io/qrcodejs/'},

  # data transformation
  'underscore': {
    'version': '1.12.0',
    'repository': 'https://github.com/jashkenas/underscore',
    'modules': [
      {'script': 'underscore-min.js', 'path': 'underscore.js/%(version)s/', 'cdnjs': CDNJS_REPO},
      {'script': 'underscore-min.js.map', 'path': 'underscore.js/%(version)s/', 'cdnjs': CDNJS_REPO},
    ],
    'website': 'https://openexchangerates.github.io/accounting.js/'},

  # Plolyfill
  'promise-polyfill': {
    'modules': [
      # Better to use the bundle version to avoid the import issue with popper.js
      {'script': 'polyfill.min.js', 'node_path': 'dist/', 'path': 'promise-polyfill@8/dist/', 'cdnjs': 'https://cdn.jsdelivr.net/npm'},
    ],
    'version': '8.2.0',
    'website': 'https://github.com/taylorhakes/promise-polyfill'},

  # Plolyfill for urlSearchParam for very old version of IE
  'url-search-params': {
    'version': '1.1.0',
    'modules': [
      # Better to use the bundle version to avoid the import issue with popper.js
      {'script': 'url-search-params.js', 'path': 'url-search-params/%(version)s/', 'cdnjs': CDNJS_REPO},
    ],
    'website': 'https://github.com/taylorhakes/promise-polyfill'},


  # Common module for browser versions compatibilities
  'babel-polyfill': {
    'version': '7.4.4',
    'website': 'https://babeljs.io/',
    'register': {'alias': 'babel', 'module': 'polyfill', 'name': 'babel'},
    'modules': [
      {'script': 'polyfill.js', 'path': 'babel-polyfill/%(version)s/', 'cdnjs': CDNJS_REPO},
    ]
  },

  # module are written from the first one to load to the last one
  'bootstrap': {
    'req': [{'alias': 'jquery'}, {'alias': '@popperjs/core'}],
    'v_prefix': 'v',
    'version': '4.5.3',
    'repository': 'https://github.com/twbs/bootstrap',
    'modules': [
      # Better to use the bundle version to avoid the import issue with popper.js
      {'script': 'bootstrap.min.js', 'node_path': 'dist/js/', 'path': 'twitter-bootstrap/%(version)s/js/', 'cdnjs': CDNJS_REPO},
      #{'script': 'bootstrap.min.js', 'version': '4.4.1', 'path': 'bootstrap/%(version)s/js/', 'cdnjs': 'https://stackpath.bootstrapcdn.com'},
    ],
    'assets': [
      {'script': 'bootstrap.min.js.map', 'node_path': 'dist/js/', 'path': 'twitter-bootstrap/%(version)s/js/', 'cdnjs': CDNJS_REPO},
    ],
    'website': 'https://getbootstrap.com/'},

  'moment': {
    "version": "2.29.1",
    'repository': 'https://github.com/moment/moment',
    'modules': [
      {'script': 'moment.min.js', 'node_path': 'min/', 'path': 'moment.js/%(version)s/', 'cdnjs': CDNJS_REPO},
    ],
    'assets': [
      {'script': 'moment.min.js.map', 'node_path': 'min/', 'path': 'moment.js/%(version)s/', 'cdnjs': CDNJS_REPO},
    ],
    'website': 'https://momentjs.com/',
  },

  # AG Grid tables
  'ag-grid-community': {
    'website': 'https://www.ag-grid.com/javascript-grid/',
    'repository': 'https://github.com/ag-grid/ag-grid',
    'version': '24.1.0',
    'modules': [
      {'script': 'ag-grid-community.min.js', 'node_path': 'dist/', 'path': 'ag-grid/%(version)s/', 'cdnjs': CDNJS_REPO}]
  },

  # module for tabulator
  'tabulator-tables': {
    'req': [{'alias': 'promise-polyfill'}, {'alias': 'moment'}],
    #'register': {'alias': 'Tabulator', 'module': 'tabulator.min', 'npm': 'tabulator', 'npm_path': ''},
    'version': '4.9.3',
    'modules': [
      # core only needed for Jupyter for some reasons
      #{'script': 'tabulator_core.min.js', 'version': '4.4.3', 'path': 'tabulator/%(version)s/js/', 'cdnjs': CDNJS_REPO}, # 'reqAlias': 'tabulator_core',
      {'script': 'tabulator.min.js', 'node_path': 'tabulator/dist/js', 'path': 'tabulator/%(version)s/js/', 'cdnjs': CDNJS_REPO}
    ],
    'website': 'http://tabulator.info/'
  },

  # Tabulator configurations
  # Different modules part of the npm project to load specific configurations
  'tabulator-inputs': {
    'req': [{'alias': 'tabulator-tables'}],
    'modules': [
      {'script': 'formatters-inputs.js', 'version': TABULATOR_EXTENSIONS, 'path': 'npm/tabulator-extensions@%(version)s/formatters/', 'cdnjs': 'https://cdn.jsdelivr.net'},
    ],
    'website': 'http://tabulator.info/'
  },

  'tabulator-drop': {
    'req': [{'alias': 'tabulator-tables'}],
    'modules': [
      {'script': 'formatters-drop.js', 'version': TABULATOR_EXTENSIONS, 'path': 'npm/tabulator-extensions@%(version)s/formatters/', 'cdnjs': 'https://cdn.jsdelivr.net'},
    ],
    'website': 'http://tabulator.info/'
  },

  'tabulator-mutators-inputs': {
    'req': [{'alias': 'tabulator-tables'}],
    'modules': [
      {'script': 'mutators-inputs.js', 'version': TABULATOR_EXTENSIONS, 'path': 'npm/tabulator-extensions@%(version)s/mutators/', 'cdnjs': 'https://cdn.jsdelivr.net'},
    ],
    'website': 'http://tabulator.info/'
  },

  'editors-inputs': {
    'req': [{'alias': 'tabulator-tables'}],
    'modules': [
      {'script': 'editors-inputs.js', 'version': TABULATOR_EXTENSIONS, 'path': 'npm/tabulator-extensions@%(version)s/editors/', 'cdnjs': 'https://cdn.jsdelivr.net'}],
    'website': 'http://tabulator.info/'
  },

  'editors-dates': {
    'req': [{'alias': 'tabulator-tables'}],
    'modules': [
      {'script': 'editors-dates.js', 'version': TABULATOR_EXTENSIONS, 'path': 'npm/tabulator-extensions@%(version)s/editors/', 'cdnjs': 'https://cdn.jsdelivr.net'},
    ],
    'website': 'http://tabulator.info/'
  },

  'editors-selects': {
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
    'req': [{'alias': 'tabulator-tables'}],
    'modules': [
      # core only needed for Jupyter for some reasons
      {'script': 'formatters-icons.js', 'version': TABULATOR_EXTENSIONS, 'path': 'npm/tabulator-extensions@%(version)s/formatters/', 'cdnjs': 'https://cdn.jsdelivr.net'},
    ],
    'website': 'http://tabulator.info/'
  },

  'tabulator-numbers': {
      'req': [
        {'alias': 'tabulator-tables'},
        {'alias': 'accounting'},
        {'alias': 'd3-scale'},
      ],
      'modules': [
        # core only needed for Jupyter for some reasons
        {'script': 'formatters-numbers.js', 'version': TABULATOR_EXTENSIONS, 'path': 'npm/tabulator-extensions@%(version)s/formatters/', 'cdnjs': 'https://cdn.jsdelivr.net'},
        {'script': 'formatters-titles.js', 'version': TABULATOR_EXTENSIONS, 'path': 'npm/tabulator-extensions@%(version)s/formatters/', 'cdnjs': 'https://cdn.jsdelivr.net'},
      ],
      'website': 'http://tabulator.info/'
    },

  # module for the awesome icons
  'font-awesome': {
    'version': '5.13.1',
    'register': {'alias': 'fontawesome', 'module': 'fontawesome', 'npm': '@fortawesome/fontawesome-free', 'npm_path': 'js'},
    'package': {'zip': 'https://use.fontawesome.com/releases/v%(version)s/fontawesome-free-%(version)s-web.zip',
                'root': 'fontawesome-free-%(version)s-web', 'folder': 'releases', 'path': 'v%(version)s'},
    'modules': [{'script': 'fontawesome.js', 'path': 'releases/v%(version)s/js/', 'cdnjs': 'https://use.fontawesome.com'}],
    'website': 'https://fontawesome.com/'},

  # Javascript packages to handle DataTables
  'datatables': {
    'req': [{'alias': 'jquery'}],
    'version': '1.10.19',
    'register': {'alias': 'datatables', 'module': 'jquery.dataTables.min'},
    'modules': [
      {'reqAlias': 'datatables', 'script': 'jquery.dataTables.min.js', 'path': 'datatables/%(version)s/js/', 'cdnjs': CDNJS_REPO},
  ]},

  # Datatable Buttons
  'datatables-buttons': {
    'version': '1.6.1',
    'website': 'https://datatables.net/extensions/buttons/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'dataTables.buttons.min.js', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable Select
  'datatables-select': {
    'version': '1.3.1',
    'website': 'https://datatables.net/extensions/select/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'dataTables.select.min.js', 'path': 'select/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable Scroller
  'datatables-scroller': {
    'version': '2.0.1',
    'website': 'https://datatables.net/extensions/scroller/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'dataTables.scroller.min.js', 'path': 'scroller/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable SearchPanes
  'datatables-searchPanes': {
    'version': '1.0.1',
    'website': 'https://datatables.net/extensions/searchPanes/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'dataTables.searchPanes.min.js', 'path': 'searchpanes/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable responsive
  'datatables-responsive': {
    'version': '2.2.3',
    'website': 'https://datatables.net/extensions/responsive/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'dataTables.responsive.min.js', 'path': 'responsive/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable KeyTable
  'datatables-keytable': {
    'version': '2.5.1',
    'website': 'https://datatables.net/extensions/keytable/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'dataTables.keyTable.min.js', 'path': 'keytable/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable autoFill
  'datatables-autoFill': {
    'version': '2.1.0',
    'website': 'https://datatables.net/extensions/autofill/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'dataTables.autoFill.min.js', 'path': 'autofill/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable group rows
  'datatables-rows-group': {
    'req': [{'alias': 'datatables'}],
    'version': '1.0.0',
    'modules': [
      {'script': 'dataTables.rowsGroup.js', 'path': 'datatables-rowsgroup/v%(version)s/', 'cdnjs': 'https://cdn.rawgit.com/ashl1'}
    ],
    'website': 'https://datatables.net/forums/discussion/29319/new-rowsgroup-plugin-merge-cells-vertically-rowspan'},

  # Datatable group row
  'datatables-row-group': {
    'req': [{'alias': 'datatables'}],
    'version': '1.1.1',
    'modules': [
      {'script': 'dataTables.rowGroup.min.js', 'path': 'rowgroup/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}],
    'website': 'https://datatables.net/extensions/rowgroup/'},

  # Datatable fixed column
  'datatables-fixed-columns': {
    'req': [{'alias': 'datatables'}],
    'version': '3.2.2',
    'modules': [
      {'script': 'dataTables.fixedColumns.min.js', 'path': 'fixedcolumns/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}],
    'website': 'https://datatables.net/extensions/fixedcolumns/'},

  # Datatable Fixed header
  'datatables-fixed-header': {
    'req': [{'alias': 'datatables'}],
    'version': '3.1.3',
    'modules': [
      {'script': 'dataTables.fixedHeader.min.js', 'path': 'fixedheader/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}],
    'website': 'https://datatables.net/extensions/fixedheader/'},

  # Datatable data export
  'datatables-export': {
    'version': '1.5.2',
    'req': [
      {'alias': 'datatables'},
      {'alias': 'jszip'},
      {'alias': 'pdfmake'}],
    'website': 'https://datatables.net/extensions/buttons/',
    'modules': [
      {'script': 'buttons.colVis.min.js', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.bootstrap4.min.js', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.foundation.min.js', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.html5.min.js', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.jqueryui.min.js', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.print.min.js', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.semanticui.min.js', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable column reordering modules
  'datatables-col-order': {
    'req': [{'alias': 'datatables'}],
    'version': '1.5.1',
    'register': {'alias': 'datatableColOrd', 'module': 'dataTables.colReorder.min'},
    'website': 'https://datatables.net/extensions/colreorder/',
    'modules': [
      {'reqAlias': 'datatableColOrd', 'script': 'dataTables.colReorder.min.js', 'path': 'colreorder/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  #
  'jszip': {
    'website': 'https://datatables.net/extensions/buttons/',
    'version': '3.5.0',
    'modules': [
      {'reqAlias': 'jszip', 'script': 'jszip.min.js', 'node_path': 'dist/', 'path': 'jszip/%(version)s/', 'cdnjs': CDNJS_REPO},
    ]},

  #
  'json-formatter-js': {
    'website': 'https://azimi.me/json-formatter-js/',
    'version': '2.3.4',
    'repository': 'https://github.com/mohsen1/json-formatter-js',
    #'register': {'alias': 'JSONFormatter', 'module': 'json-formatter.umd.min', 'npm': 'json-formatter-js'},
    'modules': [
      {'script': 'json-formatter.umd.min.js', 'node_path': 'dist/', 'path': 'json-formatter-js@%(version)s/dist/', 'cdnjs': "https://cdn.jsdelivr.net/npm"},
    ]},

  # Datatable pivot
  'pivottable': {
    'req': [{'alias': 'jqueryui'}],
    #'register': {'alias': 'pivot', 'module': 'pivot.min', 'npm': 'pivottable', 'npm_path': 'dist'},
    "repository": 'https://github.com/nicolaskruchten/pivottable',
    'version': '2.23.0',
    'website': 'https://github.com/nicolaskruchten/pivottable',
    'modules': [
      {'script': 'pivot.min.js', 'node_path': 'dist/', 'path': 'pivottable/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]
  },

  # require.js
  'requirejs': {
    'website': 'https://requirejs.org/',
    'version': '2.3.6',
    'repository': 'https://github.com/requirejs/r.js',
    'modules': [
      {'script': 'require.min.js', 'path': 'require.js/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # Pivot Table SubTotal
  'subtotal': {
    'req': [{'alias': 'pivottable'}],
    'node_folder': 'pivottable',
    'register': {'alias': 'subtotal', 'module': 'subtotal'},
    'website': 'http://nagarajanchinnasamy.com/subtotal/examples/',
    'repository': 'https://github.com/nagarajanchinnasamy/subtotal',
    'modules': [
      {'script': 'subtotal.js', 'node_path': 'dist/', 'version': '1.10.0', 'path': 'subtotal@%(version)s/dist/', 'cdnjs': 'https://cdn.jsdelivr.net/npm'}
    ]},

  # Pivot Table pivot C3 renderer
  'pivot-c3': {
    'req': [
      {'alias': 'd3', 'version': '3.5.5'},
      {'alias': 'c3', 'version': '0.4.11'},
      {'alias': 'pivottable'}
    ],
    #'register': {'alias': 'pivot_c3', 'module': 'c3_renderers.min', 'npm': 'pivottable', 'npm_path': 'dist'},
    'website': 'https://github.com/nicolaskruchten/pivottable',
    'version': '2.23.0',
    'node_folder': 'pivottable',
    'modules': [
      {'script': 'c3_renderers.min.js', 'node_path': 'dist/', 'path': 'pivottable/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]},

  # Pivot Table pivot plotly renderer
  'pivot-plotly': {
    'req': [
      {'alias': 'plotly.js'},
      {'alias': 'pivottable'}
    ],
    'node_folder': 'pivottable',
    'version': '2.23.0',
    'register': {'alias': 'pivot_plotly', 'module': 'plotly_renderers.min', 'npm': 'pivottable', 'npm_path': 'dist'},
    'website': 'https://github.com/nicolaskruchten/pivottable',
    'modules': [
      {'script': 'plotly_renderers.min.js', 'node_path': 'dist/', 'path': 'pivottable/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]},

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
        {'script': 'd3_renderers.min.js', 'node_path': 'dist/', 'path': 'pivottable/%(version)s/', 'cdnjs': CDNJS_REPO}
  ]},

  # Jquery package width CDN links
  'jquery': {
    'website': 'http://jquery.com/',
    'repository': "https://github.com/jquery/jquery",
    'register': {'alias': '$', 'module': 'jquery.min', 'npm': 'jquery', 'npm_path': 'dist'},
    'version': '3.5.1',
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
    'website': 'https://www.10bestdesign.com/jqvmap/',
    'repository': "https://github.com/10bestdesign/jqvmap/",
    'version': '1.5.1',
    'modules': [
      {'script': 'jquery.vmap.min.js', 'node_path': 'dist/', 'path': 'jqvmap/%(version)s/', 'cdnjs': CDNJS_REPO},
    ],
  },

  # QUnit package width CDN links
  'qunit': {
    'website': 'https://qunitjs.com',
    'version': '2.13.0',
    'modules': [
      {'script': 'qunit.js', 'node_path': 'qunit', 'path': 'qunit/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # Used to produce sparkline charts in a document and in Tabulator
  'jquery-sparkline': {
    'req': [{'alias': 'jquery'}],
    'version': '2.1.2',
    #'register': {'alias': 'sparklines', 'module': 'jquery.sparkline.min', 'npm': 'jquery-sparkline', 'npm_path': ''},
    'website': 'https://omnipotent.net/jquery.sparkline/#s-about',
    'modules': [
      {'script': 'jquery.sparkline.min.js', 'path': 'jquery-sparklines/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]
  },

  # Jquery UI package width CDN links
  'jqueryui': {
    'req': [{'alias': 'jquery'}],
    'website': 'http://jquery.com/',
    'repository': 'https://github.com/jquery/jqueryui.com',
    'version': '1.12.1',
    'register': {'alias': 'jqueryui', 'module': 'jquery-ui.min', 'npm': 'jquery-ui-dist', 'npm_path': ''},
    'modules': [
      {'script': 'jquery-ui.min.js', 'version': '1.12.1', 'path': 'jqueryui/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # Jquery-bracket package width CDN links
  'jquery-bracket': {
    'website': 'http://www.aropupu.fi/bracket/',
    'version': '0.11.1',
    #'register': {'alias': 'jQueryBracket', 'module': 'jquery.bracket.min'},
    'req': [{'alias': 'jquery'}],
    'modules': [
      {'script': 'jquery.bracket.min.js', 'node_path': 'dist/', 'path': 'jquery-bracket/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # Jquery UI package
  # Attempt to try to solve conflict with Bootstrap
  #'jquery-ui': {'req': ['jquery', 'bootstrap'], 'modules': ['jquery-ui.min.js']},

  # Jquery timepicker width CDN links
  'timepicker': {
    'website': 'https://timepicker.co/',
    #'register': {'alias': 'jQueryTime', 'module': 'jquery.timepicker.min'},
    'version': '1.13.16',
    'repository': 'https://github.com/jonthornton/jquery-timepicker',
    'req': [
      {'alias': 'jquery'},
      {'alias': 'jqueryui'}],
    'modules': [
      {'script': 'jquery.timepicker.min.js', 'path': 'jquery-timepicker/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]},

  # To display a context menu when right click on an item
  'jquery-context-menu': {
    'website': 'http://swisnl.github.io/jQuery-contextMenu/demo.html',
    'register': {'alias': 'jQueryContext', 'module': 'jquery.contextMenu.min'},
    'req': [{'alias': 'jquery'}, {'alias': 'jqueryui'}],
    'modules': [
      {'script': 'jquery.contextMenu.min.js', 'version': '2.6.4', 'path': 'jquery-contextmenu/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # To customize the scrollbar width CDN links
  # https://github.com/malihu/malihu-custom-scrollbar-plugin
  # http://manos.malihu.gr/repository/custom-scrollbar/demo/examples/complete_examples.html
  'jquery-scrollbar': {
    'website': 'http://manos.malihu.gr/jquery-custom-content-scroller/',
    'register': {'alias': 'jQueryScrollBar', 'module': 'jquery.mCustomScrollbar.concat.min'},
    'req': [{'alias': 'jquery'}],
    'modules': [
      {'script': 'jquery.mCustomScrollbar.concat.min.js', 'version': '3.1.5', 'path': 'malihu-custom-scrollbar-plugin/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # Javascript packages for the PDF transformation width CDN links
  'pdfmake': {
    'website': '',
    'version': '0.1.68',
    'modules': [
      {'reqAlias': 'pdfmake', 'node_path': 'build/', 'script': 'pdfmake.min.js', 'path': 'pdfmake/%(version)s/', 'cdnjs': CDNJS_REPO},
      {'reqAlias': 'vfs_fonts', 'node_path': 'build/', 'script': 'vfs_fonts.js', 'path': 'pdfmake/%(version)s/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'node_path': 'build/', 'script': 'pdfmake.min.js.map', 'path': 'pdfmake/%(version)s/', 'cdnjs': CDNJS_REPO},
    ]
  },

  # Javascript packages for the PDF transformation width CDN links (Tabulator)
  'jspdf': {
    'website': 'https://github.com/mrrio/jspdf',
    'repository': 'https://github.com/mrrio/jspdf',
    'version': '2.2.0',
    'modules': [
      {'reqAlias': 'jspdf', 'node_path': 'dist/',  'script': 'jspdf.min.js',  'path': 'jspdf/%(version)s/', 'cdnjs': CDNJS_REPO},
      {'reqAlias': 'autotable', 'script': 'jspdf.plugin.autotable.min.js', 'version': '3.1.1', 'path': 'jspdf-autotable/%(version)s/', 'cdnjs': CDNJS_REPO},
    ]},

  # Clipboard features width CDN links
  'clipboard': {
    'website': 'https://clipboardjs.com/',
    'version': '2.0.6',
    #'register': {'alias': 'clipboard', 'module': 'clipboard.min'},
    'modules': [
      {'reqAlias': 'clipboard', 'script': 'clipboard.min.js', 'node_path': 'dist/', 'path': 'clipboard.js/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # Javascript dependencies for D3 and NVD2 components width CDN links
  'd3': {
    'website': 'https://d3js.org/',
    'v_prefix': 'v',
    'version': '6.3.1',
    #'register': {'alias': 'd3', 'module': 'd3.min', 'npm': 'd3', 'npm_path': 'dist'},
    #'req': [{'alias': 'jquery'}],
    'modules': [
      {'reqAlias': 'd3', 'reqMod': 'ignore', 'script': 'd3.min.js', 'path': 'd3/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]},

  # D3 Tips Package
  'd3-tip': {
    'req': [{'alias': 'd3'}],
    'v_prefix': 'v',
    'version': '0.9.1',
    'modules': [
      {'script': 'd3-tip.min.js', 'node_path': 'dist/', 'path': 'd3-tip/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]
  },

  # D3 Packages
  # 'd3-packages': {
  #     'website': 'https://github.com/d3',
  #     'req': [{'alias': 'd3'}],
  #     'modules': [
  #         {'reqAlias': 'd3_time_format', 'script': 'd3-time-format.min.js', 'version': '2.1.1', 'path': 'd3-time-format/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_shape', 'script': 'd3-shape.min.js', 'version': '1.2.0', 'path': 'd3-shape/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_zoom', 'script': 'd3-zoom.min.js', 'version': '1.7.1', 'path': 'd3-zoom/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_dsv', 'script': 'd3-dsv.min.js', 'version': '1.0.8', 'path': 'd3-dsv/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_ease', 'script': 'd3-ease.min.js', 'version': '1.0.3', 'path': 'd3-ease/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_scale', 'script': 'd3-scale.min.js', 'version': '1.0.7', 'path': 'd3-scale/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_brush', 'script': 'd3-brush.min.js', 'version': '1.0.4', 'path': 'd3-brush/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_selection', 'script': 'd3-selection.min.js', 'version': '1.2.0', 'path': 'd3-selection/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_transition', 'script': 'd3-transition.min.js', 'version': '1.1.1', 'path': 'd3-transition/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_array', 'script': 'd3-array.min.js', 'version': '1.2.2', 'path': 'd3-array/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_collection', 'script': 'd3-collection.min.js', 'version': '1.0.5', 'path': 'd3-collection/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_drag', 'script': 'd3-drag.min.js', 'version': '1.2.1', 'path': 'd3-drag/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_interpolate', 'script': 'd3-interpolate.min.js', 'version': '1.3.0', 'path': 'd3-interpolate/%(version)s/', 'cdnjs': CDNJS_REPO},
  #         {'reqAlias': 'd3_axis', 'script': 'd3-axis.min.js', 'version': '1.0.10', 'path': 'd3-axis/%(version)s/', 'cdnjs': CDNJS_REPO},
  #       ]},

  # D3 ease
  'd3-ease': {
      'website': 'https://github.com/d3/d3-ease',
      'v_prefix': 'v',
      'version': '1.0.3',
      'modules': [
        {'script': 'd3-ease.min.js', 'node_path': 'dist/', 'path': 'd3-ease/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # D3 dispatch
  'd3-dispatch': {
      'website': 'https://github.com/d3/d3-dispatch',
      'v_prefix': 'v',
      'version': '1.0.3',
      'modules': [
        {'script': 'd3-dispatch.min.js', 'node_path': 'dist/', 'path': 'd3-dispatch/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # D3 transition
  'd3-transition': {
      'website': 'https://github.com/d3/d3-interpolate',
      'v_prefix': 'v',
      'version': '1.1.1',
      'req': [{'alias': 'd3-dispatch'}],
      'modules': [
        {'script': 'd3-transition.min.js', 'node_path': 'dist/', 'path': 'd3-transition/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # D3 Selection
  'd3-selection': {
      'website': 'https://github.com/d3/d3-selection',
      'v_prefix': 'v',
      'version': '1.2.0',
      'modules': [
        {'script': 'd3-selection.min.js', 'node_path': 'dist/', 'path': 'd3-selection/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # D3 Interpolate
  'd3-interpolate': {
      'website': 'https://github.com/d3/d3-interpolate',
      'v_prefix': 'v',
      'version': '1.3.0',
      'req': [{'alias': 'd3-color'}],
      'modules': [
        {'script': 'd3-interpolate.js', 'node_path': 'dist/', 'path': 'd3-interpolate/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # D3 Time format
  'd3-time-format': {
      'website': 'https://github.com/d3/d3-time-format',
      'v_prefix': 'v',
      'version': '2.1.1',
      'req': [{'alias': 'd3-time'}],
      'modules': [
        {'script': 'd3-time-format.min.js', 'node_path': 'dist/', 'path': 'd3-time-format/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # D3 Time
  'd3-time': {
      'website': 'https://github.com/d3/d3-time',
      'v_prefix': 'v',
      'version': '1.0.8',
      'modules': [
        {'script': 'd3-time.min.js', 'node_path': 'dist/', 'path': 'd3-time/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # D3 Format
  'd3-array': {
      'website': 'https://github.com/d3/d3-format',
      'v_prefix': 'v',
      'version': '1.2.2',
      'modules': [
        {'script': 'd3-array.min.js', 'node_path': 'dist/', 'path': 'd3-array/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # D3 Format
  'd3-format': {
      'website': 'https://github.com/d3/d3-format',
      'v_prefix': 'v',
      'version': '1.3.0',
      'modules': [
        {'script': 'd3-format.min.js', 'node_path': 'dist/', 'path': 'd3-format/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # D3 collection
  'd3-collection': {
      'website': 'https://github.com/d3/d3-collection',
      'version': '1.0.5',
      'v_prefix': 'v',
      'modules': [
        {'script': 'd3-collection.min.js', 'node_path': 'dist/', 'path': 'd3-collection/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # D3 Scale
  'd3-scale': {
      'website': 'https://github.com/d3/d3-scale',
      'v_prefix': 'v',
      'version': '1.0.7',
      'req': [
        {'alias': 'd3-array'},
        {'alias': 'd3-format'},
        {'alias': 'd3-interpolate'},
        {'alias': 'd3-time-format'}],
      'modules': [
        {'script': 'd3-scale.min.js', 'node_path': 'dist/', 'path': 'd3-scale/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # D3 color module
  'd3-color': {
    'website': 'https://github.com/d3/d3-color',
    'v_prefix': 'v',
    'version': '1.2.1',
    'modules': [
      {'script': 'd3-color.min.js', 'node_path': 'dist/', 'path': 'd3-color/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # Javascript dependencies for Plotly width CDN links
  'plotly.js': {
    'website': 'https://plot.ly/javascript/',
    'repository': 'https://github.com/plotly/plotly.js',
    'version': '1.58.4',
    'req': [{'alias': 'd3'}],
    'modules': [
      {'script': 'plotly.min.js', 'node_path': 'dist/', 'path': 'plotly.js/%(version)s/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'script': 'africa_50m.json', 'node_path': 'dist/topojson/', 'path': '/', 'cdnjs': "https://www.hpcoders.com.au/ravel/plotly.js/dist/topojson"},
      {'script': 'europe_50m.json', 'node_path': 'dist/topojson/', 'path': '/', 'cdnjs': "https://www.hpcoders.com.au/ravel/plotly.js/dist/topojson"},
    ]
  },

  # NVD3 Components width CDN links
  'nvd3': {
    'website': 'http://nvd3.org/',
    'repository': 'https://github.com/novus/nvd3',
    'req': [{'alias': 'd3', 'version': '3.5.17'}],
    'version': '1.8.6',
    #'register': {'alias': 'nv', 'module': 'nv.d3.min', 'npm': 'nvd3'},
    'modules': [
      {'script': 'nv.d3.min.js', 'node_path': 'build/', 'path': 'nvd3/%(version)s/', 'cdnjs': CDNJS_REPO}],
    'assets': [
      {'script': 'nv.d3.min.js.map', 'node_path': 'build/', 'path': 'nvd3/%(version)s/', 'cdnjs': CDNJS_REPO},
    ]
  },

  # C3 modules width CDN links
  'c3': {
    'website': 'https://c3js.org/',
    'repository': 'https://github.com/c3js/c3',
    'req': [{'alias': 'd3'}],
    'version': '0.7.20',
    'modules': [
      {'script': 'c3.min.js', 'path': 'c3/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  'crossfilter': {
    'website': 'http://square.github.io/crossfilter/',
    'repository': 'https://github.com/crossfilter/crossfilter',
    'version': '1.3.12',
    'modules': [
      {'script': 'crossfilter.min.js', 'path': 'crossfilter/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]
  },

  'apexcharts': {
    'website': 'https://apexcharts.com/',
    'repository': 'https://github.com/apexcharts/apexcharts.js',
    'version': '3.23.1',
    'modules': [
      {'script': 'apexcharts.min.js', 'node_path': 'dist/', 'path': 'apexcharts/%(version)s/', 'cdnjs': CDNJS_REPO}
    ],
  },

  # DC modules width CDN links
  'dc': {
    'website': 'https://dc-js.github.io/dc.js/examples/',
    'repository': 'https://github.com/dc-js/dc.js',
    'req': [
      {'alias': 'd3'},
      {'alias': 'crossfilter'},
    ],
    'version': '4.2.3',
    'modules': [
      {'script': 'dc.min.js', 'node_path': 'dist/', 'path': 'dc/%(version)s/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'script': 'dc.min.js.map', 'node_path': 'dist/', 'path': 'dc/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]
  },

  # billboard modules width CDN links
  'billboard.js': {
    'website': 'https://naver.github.io/billboard.js/release/latest/doc/',
    #'register': {'alias': 'billboard', 'module': 'billboard.pkgd.min', 'npm': 'billboard.js', 'var': 'bb', 'init_fnc': 'var bb = billboard.bb'},
    'req': [{'alias': 'd3'}],
    'version': '2.1.4',
    'modules': [
      {'script': 'billboard.min.js', 'node_path': 'dist/', 'path': 'billboard.js/%(version)s/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'script': 'billboard.min.js.map', 'node_path': 'dist/', 'path': 'billboard.js/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]
  },

  # ChartJs modules width CDN links
  'chart.js': {
    'website': 'https://www.chartjs.org/',
    'version': '2.9.4',
    'v_prefix': 'v',
    'repository': 'https://github.com/chartjs/Chart.js',
    'register': {'alias': 'Chart', 'module': 'Chart.min', 'npm': 'chart.js', 'npm_path': 'dist'},
    'modules': [
      #{'script': 'Chart.bundle.min.js', 'version': '2.9.4', 'path': 'Chart.js/%(version)s/', 'cdnjs': CDNJS_REPO},
      {'script': 'Chart.min.js', 'node_path': 'dist/', 'path': 'Chart.js/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # ChartJs Crosshair plugin modules width CDN links
  'chartjs-plugin-dragdata': {
    'website': 'https://www.chartjs.org/',
    'version': 'latest',
    'req': [{'alias': 'chart.js'}],
    'modules': [
      {'script': 'chartjs-plugin-dragdata.min.js', 'path': 'chartjs-plugin-dragdata@%(version)s/dist/', 'cdnjs': "https://cdn.jsdelivr.net/npm"}]},

  # ChartJs Crosshair plugin modules width CDN links
  'chartjs-plugin-annotation': {
    'website': 'https://www.chartjs.org/',
    'version': '0.5.7',
    'req': [{'alias': 'chart.js'}],
    'modules': [
      {'script': 'chartjs-plugin-annotation.min.js', 'path': 'chartjs-plugin-annotation/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # ChartJs datalabels plugin modules width CDN links
  'chartjs-plugin-datalabels': {
    'version': '0.7.0',
    'website': 'https://chartjs-plugin-datalabels.netlify.app/',
    'req': [{'alias': 'chart.js'}],
    'modules': [
      {'script': 'chartjs-plugin-datalabels.min.js', 'path': 'chartjs-plugin-datalabels@%(version)s/dist/', 'cdnjs': 'https://cdn.jsdelivr.net/npm'}]},

  # ChartJs Labels plugin modules width CDN links
  'chartjs-plugin-labels': {
    'version': '1.1.0',
    'website': 'https://github.com/emn178/chartjs-plugin-labels',
    'req': [{'alias': 'chart.js'}],
    'v_prefix': 'v',
    'modules': [
      {'script': 'chartjs-plugin-labels.js', 'path': '/', 'cdnjs': "https://emn178.github.io/chartjs-plugin-labels/src"}]},

  # ChartJs Crosshair plugin modules width CDN links
  'chartjs-plugin-crosshair': {
    'version': '1.1.6',
    'website': 'https://www.chartjs.org/',
    'req': [{'alias': 'chart.js'}],
    'modules': [
      {'script': 'chartjs-plugin-crosshair.js', 'path': '', 'cdnjs': "https://chartjs-plugin-crosshair.netlify.app/"}]},

  # ChartJs Zoom plugin modules width CDN links
  'chartjs-plugin-zoom': {
    'website': 'https://www.chartjs.org/',
    'version': '0.7.7',
    'req': [{'alias': 'chart.js'}, {"alias": 'hammer'}],
    'modules': [
      {'script': 'chartjs-plugin-zoom.min.js', 'path': 'chartjs-plugin-zoom/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # ChartJs addon to add some Geo charts
  'chartjs-chart-geo': {
      'version': '2.1.0',
      'website': 'https://github.com/sgratzl/chartjs-chart-geo',
      'req': [{'alias': 'chart.js'}],
      'modules': [
        {'script': 'Chart.Geo.min.js', 'path': 'chartjs-chart-geo@%(version)s/build/', 'cdnjs': 'https://cdn.jsdelivr.net/npm'}
      ]},

  # For ChartJs Zoom to get the gesture details.
  'hammer': {
      'version': '2.0.8',
      'website': 'http://hammerjs.github.io/',
      'modules': [
        {'script': 'hammer.min.js', 'path': 'hammer.js/%(version)s/', 'cdnjs': CDNJS_REPO}
      ],
  },

  # Cannot add properly the dependency in this one as my algorithm does not work for shared dependencies ....
  # 'meter': {'req': ['d3'], 'modules': ['d3.meter.js'], 'website': '', 'version': '', "status": 'deprecated'},

  # Popper tooltips used by bootstrap in the dropdown components
  '@popperjs/core': {
    'req': [{'alias': 'jquery'}],
    'v_prefix': 'v',
    'version': '2.6.0',
    'repository': 'https://github.com/popperjs/popper-core',
    'website': 'https://github.com/popperjs/popper-core',
    'modules': [
      {'reqAlias': 'popper', 'script': 'popper.min.js', 'node_path': 'dist/umd/', 'path': 'popper.js/%(version)s/umd/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'script': 'popper.min.js.map', 'node_path': 'dist/umd/', 'path': 'popper.js/%(version)s/umd/', 'cdnjs': CDNJS_REPO}
    ]
  },

  # Javascript module for the simple select component. issue with Bootstrap 4 width CDN links
  'bootstrap-select': {
    'website': 'http://silviomoreto.github.io/bootstrap-select/',
    'version': '1.13.18',
    'repository': 'https://github.com/snapappointments/bootstrap-select',
    #'register': {'alias': 'selectBs', 'module': 'bootstrap-select.min', 'npm_path': 'dist/js'},
    'req': [
      {'alias': '@popperjs/core', 'version': '1.14.6'}, # Cannot be upgraded bug with bootstrap select
      {'alias': 'jquery'},
      {'alias': 'bootstrap'}],
    'modules': [
      {'reqAlias': 'selectBs', 'script': 'bootstrap-select.min.js', 'node_path': 'dist/js/', 'path': 'bootstrap-select/%(version)s/js/', 'cdnjs': CDNJS_REPO},
    ],
    'assets': [
      {'script': 'bootstrap-select.min.js.map', 'node_path': 'dist/js/', 'path': 'bootstrap-select/%(version)s/js/', 'cdnjs': CDNJS_REPO},
    ]
  },

  'ajax-bootstrap-select': {
    'version': '1.4.5',
    'website': 'https://github.com/truckingsim/Ajax-Bootstrap-Select',
    'register': {'alias': 'selectAjax', 'module': 'ajax-bootstrap-select.min', 'npm_path': 'dist/js'},
    'req': [{"alias": 'bootstrap-select'}
    ],
    'modules': [
      {'script': 'ajax-bootstrap-select.min.js', 'node_path': 'dist/js/', 'path': 'ajax-bootstrap-select/%(version)s/js/', 'cdnjs': CDNJS_REPO}
    ]
  },

  # https://cdnjs.cloudflare.com/ajax/libs/ajax-bootstrap-select/1.4.5/js/ajax-bootstrap-select.min.js
  # javascript package for the Venn chart
  # 'venn': {'req': ['d3'], 'modules': ['venn.js'], 'website': '', 'version': '',},

  # Vis Javascript Packages
  'vis': {
    'register': {'alias': 'vis', 'module': 'vis.min', 'npm': 'vis', 'npm_path': 'dist'},
    'website': 'http://visjs.org/',
    'version': '4.21.0',
    'modules': [
      {'script': 'vis.min.js', 'path': 'vis/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # Vis Timeline style with CDN Links
  'vis-timeline': {
    'register': {'alias': 'vis-timeline', 'npm': 'vis-timeline', 'npm_path': 'dist'},
    'website': 'http://visjs.org/',
    'version': '7.3.7',
    'modules': [
      {'script': 'vis-timeline-graph2d.min.js', 'path': 'vis-timeline/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # Javascript package to display mathematical formulas
  # https://codingislove.com/display-maths-formulas-webpage/
  # https://github.com/mathjax/mathjax
  'mathjax': {
    'website': 'https://www.mathjax.org/',
    'version': '3.1.2',
    'repository': 'https://github.com/mathjax/MathJax',
    'package': {'zip': 'https://github.com/mathjax/MathJax/archive/%(version)s.zip', 'root': 'MathJax-%(version)s', 'folder': 'mathjax'},
    'modules': [
      {'script': 'MathJax.js', 'path': 'mathjax/%(version)s/', 'cdnjs': CDNJS_REPO}],
    # To use the full module online
    #'url': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/',
    'config': "config=TeX-AMS-MML_HTMLorMML"},

  # Socket IO
  'socket.io': {
    'version': '3.0.4',
    'website': 'https://github.com/socketio/socket.io',
    'repository': 'https://github.com/socketio/socket.io',
    'req': [{'alias': 'jquery'}],
    'modules': [
      {'script': 'socket.io.min.js', 'node_path': 'client-dist/', 'path': 'socket.io/%(version)s/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'script': 'socket.io.min.js.map', 'node_path': 'client-dist/', 'path': 'socket.io/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]
  },

  # Code mirror
  'codemirror': {
    'version': '5.59.0',
    'website': 'https://codemirror.net/',
    'modules': [
      {'script': 'codemirror.js', 'node_path': 'lib/', 'path': 'codemirror/%(version)s/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'script': 'python.js', 'node_path': 'mode/python/', 'path': 'codemirror/%(version)s/mode/python/', 'cdnjs': CDNJS_REPO},
      {'script': 'r.js', 'node_path': 'mode/r/', 'path': 'codemirror/%(version)s/mode/r/', 'cdnjs': CDNJS_REPO},
      {'script': 'css.js', 'node_path': 'mode/css/', 'path': 'codemirror/%(version)s/mode/css/', 'cdnjs': CDNJS_REPO},
      {'script': 'javascript.js', 'node_path': 'mode/javascript/', 'path': 'codemirror/%(version)s/mode/javascript/', 'cdnjs': CDNJS_REPO},
      {'script': 'markdown.js', 'node_path': 'mode/markdown/', 'path': 'codemirror/%(version)s/mode/markdown/', 'cdnjs': CDNJS_REPO},
      {'script': 'php.js', 'node_path': 'mode/php/', 'path': 'codemirror/%(version)s/mode/php/', 'cdnjs': CDNJS_REPO},
      {'script': 'ruby.js', 'node_path': 'mode/ruby/', 'path': 'codemirror/%(version)s/mode/ruby/', 'cdnjs': CDNJS_REPO},
    ]
  },

  # highlight
  'highlight.js': {
    'version': '10.4.1',
    'website': 'https://highlightjs.org/',
    'repository': 'https://github.com/highlightjs/highlight.js',
    #'register': {'alias': 'hljs', 'npm': 'highlight.js', 'npm_path': 'lib/core'},
    'modules': [
      {'script': 'highlight.min.js', 'node_path': 'lib/', 'path': 'highlight.js/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]},

  # Leaflet
  'leaflet': {
    'version': '1.7.1',
    'website': 'https://leafletjs.com/',
    'repository': 'https://github.com/Leaflet/Leaflet',
    'modules': [
      {'script': 'leaflet.js', 'node_path': 'dist/', 'path': 'leaflet/%(version)s/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'script': 'leaflet.js.map', 'node_path': 'dist/', 'path': 'leaflet/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]
  },

  # showdown
  'showdown': {
    'version': '1.9.1',
    'website': 'https://github.com/showdownjs/showdown',
    'repository': 'https://github.com/showdownjs/showdown',
    #'register': {'alias': 'showdown', 'npm': 'showdown', 'npm_path': 'dist'},
    'modules': [
      {'script': 'showdown.min.js', 'node_path': 'dist/', 'path': 'showdown/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]
  },

  # Sortable framework
  'sortablejs': {
    'register': {'alias': 'Sortable', 'npm': 'sortablejs'},
    'repository': 'https://github.com/SortableJS/Sortable',
    'version': '1.10.2',
    'modules': [
      {'script': 'Sortable.min.js', 'path': 'Sortable/%(version)s/', 'cdnjs': CDNJS_REPO},
    ],
    'website': 'https://github.com/SortableJS/Sortable'},

  'google-platform': {
    'website': 'https://apis.google.com/',
    'req': [],
    'modules': [
      {'script': 'platform.js', 'version': '', 'path': 'js/', 'cdnjs': 'https://apis.google.com'}]},

  'facebook-sdk': {
    'website': 'https://connect.facebook.net',
    'req': [],
    'version': '0.3.3',
    'modules': [
      {'script': 'sdk.js', 'path': 'en-GB/', 'cdnjs': 'https://connect.facebook.net'}]},

  # Tiny slider for carousels
  'tiny-slider': {
    'version': '2.9.3',
    'register': {'alias': 'tns', 'npm': 'tiny-slider'},
    'modules': [
      {'script': 'tiny-slider.js', 'node_path': 'dist/min/', 'path': 'tiny-slider/%(version)s/min/', 'cdnjs': CDNJS_REPO},
    ],
    'website': 'https://github.com/ganlanyuan/tiny-slider',
  }
}


CSS_IMPORTS = {
  'jqueryui': {
    'modules': [
      {'script': 'jquery-ui.min.css', 'path': 'jqueryui/%(version)s/', 'cdnjs': CDNJS_REPO},
    ]
  },

  # ChartJs modules width CDN links
  'chart.js': {
    'modules': [
      {'script': 'Chart.min.css', 'node_path': 'dist/', 'path': 'Chart.js/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # The Apexcharts CDN links
  'apexcharts': {
    'modules': [
      {'script': 'apexcharts.css', 'node_path': 'dist/', 'path': 'apexcharts/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # material design icons
  'material-design-icons': {
    'register': {'alias': 'icons', 'module': 'icons', 'npm': 'material-design-icons', 'npm_path': 'iconfont'},
    'modules': [{'script': 'material-icons.css', 'version': '3.0.1', 'path': 'material-design-icons/%(version)s/iconfont/', 'cdnjs': CDNJS_REPO}],
    'assets': [
        {'script': 'MaterialIcons-Regular.ttf', 'version': '3.0.1', 'path': 'material-design-icons/%(version)s/iconfont/', 'cdnjs': CDNJS_REPO},
        {'script': 'MaterialIcons-Regular.woff', 'version': '3.0.1', 'path': 'material-design-icons/%(version)s/iconfont/', 'cdnjs': CDNJS_REPO},
        {'script': 'MaterialIcons-Regular.woff2', 'version': '3.0.1', 'path': 'material-design-icons/%(version)s/iconfont/', 'cdnjs': CDNJS_REPO},
    ],
    'website': 'https://google.github.io/material-design-icons/'},

  # fluent ui icons
  'office-ui-fabric-core': {
    'register': {'alias': 'fluentui', 'module': 'fluentui', 'npm_path': 'dist/css'},
    'modules': [{'script': 'fabric.min.css', 'version': '11.0.0', 'path': 'office-ui-fabric-core/%(version)s/css/', 'cdnjs': "https://static2.sharepointonline.com/files/fabric"}],
    'website': 'https://developer.microsoft.com/en-us/fluentui#/styles/web/icons'},

  # fluent ui icons
  'office-ui-fabric-react': {
    'register': {'alias': 'fluentui', 'module': 'fluentui', 'npm_path': 'dist/css'},
    'modules': [{'script': 'fabric.min.css', 'version': '11.0.0', 'path': 'office-ui-fabric-core/%(version)s/css/', 'cdnjs': "https://static2.sharepointonline.com/files/fabric"}],
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
      {'script': 'jquery.bracket.min.css', 'node_path': 'dist/', 'path': 'jquery-bracket/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # To display a context menu when right click on an item width CDN links
  # http://swisnl.github.io/jQuery-contextMenu/demo.html#jquery-context-menu-demo-gallery
  'jquery-context-menu': {
    'website': 'https://github.com/swisnl/jQuery-contextMenu/blob/master/dist/jquery.contextMenu.min.css.map',
    'req': [{'alias': 'jqueryui'}],
    'modules': [
      {'script': 'jquery.contextMenu.min.css', 'version': '2.6.4', 'path': 'jquery-contextmenu/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # Jquery timepicker width CDN links
  'timepicker': {
    'modules': [
      {'script': 'jquery.timepicker.min.css', 'path': 'jquery-timepicker/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # To customize the scrollbar width CDN links
  'jquery-scrollbar': {
    'website': 'http://manos.malihu.gr/jquery-custom-content-scroller/',
    'req': [{'alias': 'jqueryui'}],
    'modules': [
      {'script': 'jquery.mCustomScrollbar.min.css', 'version': '3.1.5', 'path': 'malihu-custom-scrollbar-plugin/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  # Tabulator definition
  'tabulator-tables': {
    'modules': [
      {'script': 'tabulator.min.css', 'node_path': 'dist/css/', 'path': 'tabulator/%(version)s/css/', 'cdnjs': CDNJS_REPO}
    ]
  },

  'datatables': {
    'website': 'https://datatables.net/',
    'req': [{'alias': 'bootstrap'}],
    'modules': [
      {'script': 'jquery.dataTables.min.css', 'version': '1.10.19', 'path': '%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}
  ]},

  # Datatable Buttons
  'datatables-buttons': {
    'website': 'https://datatables.net/extensions/buttons/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'buttons.dataTables.min.css', 'version': '1.6.1', 'path': 'buttons/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable Select
  'datatables-select': {
    'website': 'https://datatables.net/extensions/select/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'select.dataTables.min.css', 'version': '1.3.1', 'path': 'select/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable Scroller
  'datatables-scroller': {
    'website': 'https://datatables.net/extensions/scroller/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'scroller.dataTables.min.css', 'version': '2.0.1', 'path': 'scroller/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable SearchPanes
  'datatables-searchPanes': {
    'website': 'https://datatables.net/extensions/searchpanes/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'searchPanes.dataTables.min.css', 'version': '1.0.1', 'path': 'searchpanes/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable Responsive
  'datatables-responsive': {
    'website': 'https://datatables.net/extensions/responsive/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'responsive.dataTables.min.css', 'version': '2.2.3', 'path': 'responsive/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable KeyTable
  'datatables-keytable': {
    'website': 'https://datatables.net/extensions/keytable/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'keyTable.dataTables.min.css', 'version': '2.5.1', 'path': 'keytable/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable autoFill
  'datatables-autoFill': {
    'website': 'https://datatables.net/extensions/autofill/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'autoFill.dataTables.min.css', 'version': '2.1.0', 'path': 'autofill/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable group row
  'datatables-row-group': {
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'rowGroup.dataTables.min.css', 'version': '1.1.1', 'path': 'rowgroup/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable fixed column
  'datatables-fixed-columns': {
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'fixedColumns.bootstrap4.min.css', 'version': '3.2.2', 'path': 'fixedcolumns/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable fixed header
  'datatables-fixed-header': {
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'fixedHeader.bootstrap4.min.css', 'version': '3.1.3', 'path': 'fixedheader/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable export module
  'datatables-export': {
    'website': 'https://datatables.net/',
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'buttons.bootstrap4.min.css', 'version': '1.5.2', 'path': 'buttons/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable column ordering
  'datatables-col-order': {
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'colReorder.bootstrap4.min.css', 'version': '1.5.1', 'path': 'colreorder/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Bootstrap style width CDN links
  'bootstrap': {
    'modules': [
      {'script': 'bootstrap.min.css', 'node_path': 'dist/css/', 'path': 'twitter-bootstrap/%(version)s/css/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'script': 'bootstrap.min.css.map', 'node_path': 'dist/css/', 'path': 'twitter-bootstrap/%(version)s/css/', 'cdnjs': CDNJS_REPO}
    ]
  },

  # Font awesome style width CDN links
  'font-awesome': {
    'register': {'alias': 'fontawesome', 'module': 'fontawesome', 'npm': '@fortawesome/fontawesome-free', 'npm_path': 'css'},
    'website': 'https://fontawesome.com/',
    'package': {'zip': 'https://use.fontawesome.com/releases/v%(version)s/fontawesome-free-%(version)s-web.zip',
                    'root': 'fontawesome-free-%(version)s-web', 'folder': 'releases', 'path': 'v%(version)s'},
    'modules': [
      {'script': 'all.css', 'version': '5.13.1', 'path': 'releases/v%(version)s/css/', 'cdnjs': 'https://use.fontawesome.com'}],
    'assets': [
      {'script': 'fa-brands-400.woff2', 'version': '5.13.1', 'path': 'releases/v%(version)s/webfonts/', 'cdnjs': 'https://use.fontawesome.com', 'npm_path': 'webfonts'},
      {'script': 'fa-regular-400.woff2', 'version': '5.13.1', 'path': 'releases/v%(version)s/webfonts/', 'cdnjs': 'https://use.fontawesome.com', 'npm_path': 'webfonts'},
      {'script': 'fa-solid-900.woff2', 'version': '5.13.1', 'path': 'releases/v%(version)s/webfonts/', 'cdnjs': 'https://use.fontawesome.com', 'npm_path': 'webfonts'},
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
      {'script': 'dc.css', 'path': 'dc/%(version)s/style/', 'cdnjs': CDNJS_REPO}]},

  # billboard modules width CDN links
  'billboard.js': {
    'modules': [
      {'script': 'billboard.min.css', 'node_path': 'dist/', 'path': 'billboard.js/%(version)s/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'script': 'billboard.min.css.map', 'node_path': 'dist/', 'path': 'billboard.js/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]
  },

  #'epyk': {'req': ['bootstrap'], 'modules': ['bdi.css'], 'website': 'internal lib', 'version': '0'},

  # Javascript module for the simple select component. issue with Bootstrap 4 width CDN links
  'bootstrap-select': {
    'modules': [
      {'script': 'bootstrap-select.min.css', 'node_path': 'dist/css/', 'path': 'bootstrap-select/%(version)s/css/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'script': 'bootstrap-select.css.map', 'node_path': 'dist/css/', 'path': 'bootstrap-select/%(version)s/css/', 'cdnjs': CDNJS_REPO}
    ]

  },

  'ajax-bootstrap-select': {
    'modules': [
          {'script': 'ajax-bootstrap-select.min.css', 'node_path': 'dist/css/', 'version': '1.4.5', 'path': 'ajax-bootstrap-select/%(version)s/css/', 'cdnjs': CDNJS_REPO}
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
      {'script': 'codemirror.css', 'node_path': 'lib/', 'version': '5.58.3', 'path': 'codemirror/%(version)s/', 'cdnjs': CDNJS_REPO}
    ]},

  # highlight
  'highlight.js': {
    'modules': [
      {'script': 'default.min.css', 'node_path': 'styles/', 'path': 'highlight.js/%(version)s/styles/', 'cdnjs': CDNJS_REPO}
    ]},

  # Leaflet
  'leaflet': {
    'modules': [
      {'script': 'leaflet.css', 'node_path': 'dist/', 'path': 'leaflet/%(version)s/', 'cdnjs': CDNJS_REPO}]},

  #
  'json-formatter-js': {
    'modules': [
      {'script': 'json-formatter.css', 'node_path': 'dist/', 'path': 'json-formatter-js@%(version)s/dist/', 'cdnjs': "https://cdn.jsdelivr.net/npm"},
    ]},

  # AG Grid tables
  'ag-grid-community': {
    'modules': [
      {'script': 'ag-grid.min.css', 'node_path': 'dist/styles/', 'path': 'ag-grid/%(version)s/styles/', 'cdnjs': CDNJS_REPO}
    ],
    'assets': [
      {'script': 'ag-theme-alpine.min.css', 'node_path': 'dist/styles/', 'path': 'ag-grid/%(version)s/styles/', 'cdnjs': CDNJS_REPO},
      {'script': 'ag-theme-bootstrap.min.css', 'node_path': 'dist/styles/', 'path': 'ag-grid/%(version)s/styles/', 'cdnjs': CDNJS_REPO},
      {'script': 'ag-theme-material.min.css', 'node_path': 'dist/styles/', 'path': 'ag-grid/%(version)s/styles/', 'cdnjs': CDNJS_REPO},
    ]
  },

  # Tiny slider for carousels
  'tiny-slider': {
    'modules': [
      {'script': 'tiny-slider.min.css', 'node_path': 'dist/', 'path': 'tiny-slider/%(version)s/', 'cdnjs': CDNJS_REPO},
    ],
  }
}


_SERVICES = {}


MATERIAL_DESIGN_COMPONENTS = {
  'material-icons': {
    'website': 'https://material.io/resources/icons/?style=baseline',
    'services': [
      {'type': 'css', 'url': 'https://fonts.googleapis.com/icon', 'values': {'family': 'Material+Icons'}},
    ]
  },

  'material-components-web': {
    'version': '9.0.0',
    'website': 'https://material.io/components',
    'register': {'alias': 'mdc', 'module': 'material-components-web.min', 'npm': 'mdc'},
    'modules': [
      {'script': 'material-components-web.min.js', 'path': 'material-components-web/%(version)s/'},
      {'script': 'material-components-web.min.css', 'path': 'material-components-web/%(version)s/'}
  ]},
}


BOOTSTRAP = {
  'bootstrap-datetimepicker': {
    'version': '4.17.47',
    'req': [
      {'alias': 'moment'},
      {'alias': 'bootstrap', 'version': '3.4.1'}],
    'website': 'https://material.io/components',
    'register': {'alias': 'datetimepicker', 'module': 'bootstrap-datetimepicker.min', 'npm': 'datetimepicker'},
    'modules': [
      {'script': 'bootstrap-datetimepicker.min.js', 'path': 'bootstrap-datetimepicker/%(version)s/js/'},
      {'script': 'bootstrap-datetimepicker.min.css', 'path': 'bootstrap-datetimepicker/%(version)s/css/'},
    ]},
}


GOOGLE_EXTENSIONS = {
  'charts': {'modules': [
      {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
    ],
    'website': 'https://developers.google.com/chart/interactive/docs',
    'launcher': "google.charts.load('current', {'packages':['corechart']})",

  },
  'geochart': {'modules': [
        {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
      ],
      'website': 'https://developers.google.com/chart/interactive/docs',
      'launcher': "google.charts.load('current', {'packages':['geochart']})",

  },
  'tables': {'modules': [
          {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
        ],
        'website': 'https://developers.google.com/chart/interactive/docs',
        'launcher': "google.charts.load('current', {'packages':['table']})",

    },
  'gauge': {'modules': [
        {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
      ],
      'website': 'https://developers.google.com/chart/interactive/docs',
      'launcher': "google.charts.load('current', {'packages':['gauge']})",

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
      {'script': 'js?key=%(api_key)s&libraries=visualization', 'version': '', 'path': 'api/', 'cdnjs': 'https://maps.googleapis.com/maps'},
    ],
    'website': 'https://developers.google.com/chart',
    'launcher': "google.charts.load('current', {'packages':['corechart']})",
  },
  'captcha': {'modules': [
      {'script': 'api.js?render=%(site_key)s', 'version': '', 'path': '', 'cdnjs': 'https://www.google.com/recaptcha'},
    ],
  }
}


def script_version(alias, script_details, with_prefix=False):
  """
  Description:
  -----------
  Return the script version number with or without prefix.
  This will ensure a standard way to get the version number for a given CSS or JavaScript script in the framework.

  Usage:
  -----

  Attributes:
  ----------
  :param alias: String. The package reference alias in the framework and in NPM.
  :param script_details: Dictionary. The script definition in the framework.
  :param with_prefix: Boolean. Optional. Flag to specify if the full version number is required (with the prefix)
  """
  if "version" in script_details:
    if with_prefix:
      if 'v_prefix' in JS_IMPORTS[alias]:
        return "%s%s" % (JS_IMPORTS[alias]['v_prefix'], script_details["version"])

    return script_details["version"]

  if with_prefix:
    if 'v_prefix' in JS_IMPORTS[alias]:
      return "%s%s" % (JS_IMPORTS[alias]['v_prefix'], JS_IMPORTS[alias]["version"])

  return JS_IMPORTS[alias]["version"]


def script_cdnjs_path(alias, script_details, with_prefix=False):
  """
  Description:
  -----------
  Get the script path to retrieve the content locally.
  This is mainly used by PyNpm package in order to retrieve the content of the script to produce local copies of them.

  Having script copied locally will speed up the loading of the page and also will ensure a run offline.

  Usage:
  -----

  Attributes:
  ----------
  :param alias: String. The package reference alias in the framework and in NPM.
  :param script_details: Dictionary. The script definition in the framework.
  :param with_prefix: Boolean. Optional. Flag to specify if the full version number is required (with the prefix)
  """
  details = dict(script_details)
  details["version"] = script_version(alias, script_details, with_prefix)
  details["path"] = details["path"] % details
  return "%(cdnjs)s/%(path)s%(script)s" % details


def script_npm_path(alias, script_details, static_path, with_prefix=False):
  """
  Description:
  -----------

  Attributes:
  ----------
  :param alias: String. The package reference alias in the framework and in NPM.
  :param script_details: Dictionary. The script definition in the framework.
  :param static_path: String.
  :param with_prefix: Boolean. Optional. Flag to specify if the full version number is required (with the prefix)
  """
  details = dict(script_details)
  details["version"] = script_version(alias, script_details, with_prefix)
  details["node_path"] = str(details.get("node_path", "\\") % details).replace("/", "\\")
  details["alias"] = JS_IMPORTS[alias].get("node_folder", alias)
  details["static"] = static_path
  if not details["node_path"].endswith("\\"):
    details["node_path"] += "\\"
  return r"%(static)s\%(alias)s\%(node_path)s%(script)s" % details


def extend(reference, module_path, version, cdnjs_url=CDNJS_REPO, required=None):
  """
  Description:
  ------------
  Function to extend the internal CSS and JS registered modules.

  Related Pages:
  --------------
  :param reference: String. The internal reference in the framework
  :param module_path: List of tuple. The different modules and location
  :param version: String. The version number. Can be an internal module reference to point to follow its version number
  :param cdnjs_url: String. The CDNJS reference path
  :param required: List. The list of dependency modules
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
      # take the version from another registered module
      version = config[version].get('version') or config[version]['modules'][0]['version']
    config[reference]["modules"].append({'script': module, 'version': version, 'path': path, 'cdnjs': cdnjs_url})


def extend_imports(extension):
  """
  Description:
  ------------
  Hook to extend the imports in the centralised Import module.
  The packages definition is quite similar to the one in IMports.py except that CSS and JS are grouped together for
  simplicity

  :param extension: Dictionary. The list of packages to be added grouped by alias
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

  def __init__(self, name, js, css):
    self._name = name
    self._js = js[name]
    self._css = css.get(name, {})

  @property
  def version(self):
    """
    Description:
    -----------
    Return the package version number defined in the framework.
    """
    return self._js["versions"]

  @version.setter
  def version(self, val):
    new_js = collections.OrderedDict()
    for k, v in self._js["main"].items():
      new_js[k.replace(v, val)] = val
    self._js["versions"] = [val]
    self._js["main"] = new_js

    if self._css:
      new_css = collections.OrderedDict()
      for k, v in self._css["main"].items():
        new_css[k.replace(v, val)] = val
      self._css["versions"] = [val]
      self._css = new_css

  @property
  def path(self):
    """
    Description:
    -----------
    Get the package path used to retrieve the various modules.
    """
    mod = JS_IMPORTS[self._name]['modules'][0]
    mod["version"] = self.version
    mod["path"] = mod["path"] % mod
    return "%(cdnjs)s/%(path)s" % mod

  @path.setter
  def path(self, full_path):
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
    """
    Description:
    -----------
    Get the list of external files used for this package.

    Usage:
    -----

      pkgs = page.imports().pkgs
      pkgs.tabulator.version = "4.8.7"
      print(pkgs.tabulator.scripts)
    """
    return self._js["main"].keys() | self._css["main"].keys()

  def from_cdnjs(self):
    """
    Description:
    -----------
    Just change the overriden flag of this package to ensure it will not be changed by the set_local method.
    Indeed this method will not impact any modules with this flag set to True.

    Usage:
    -----

    """
    self.overriden = True

  def set_local(self, static_url="/static"):
    """
    Description:
    -----------
    Route the package to the local path.
    Check first of the modules exist and raise an error otherwise.

    Usage:
    -----

    Attributes:
    ----------
    :param static_url: String. Optional. The static root on the server. (default value /static/).
    """
    if self.overriden:
      return

    new_js = collections.OrderedDict()
    for v in JS_IMPORTS[self._name]["modules"]:
      node_path = v.get("node_path", "")
      if not node_path.endswith("/"):
        node_path += "/"
      new_js["%s/%s/%s%s" % (static_url, self._name, node_path, v["script"])] = self.version
    self._js["main"] = new_js

    if self._css:
      new_css = collections.OrderedDict()
      for v in CSS_IMPORTS[self._name]["modules"]:
        node_path = v.get("node_path", "")
        if not node_path.endswith("/"):
          node_path += "/"
        new_css["%s/%s/%s%s" % (static_url, self._name, node_path, v["script"])] = self.version
      self._css = new_css
    self.overriden = True


class ImportPackages:

  def __init__(self, js, css):
    self._js = js
    self._css = css

  def get(self, name):
    """
    Description:
    ------------
    Generic way to retrieve packages from the framework.
    This is a shortcut to change any properties for the package (version, path...).

    Usage:
    -----


    Attributes:
    ----------
    :param name: String. The package alias to be loaded.
    """
    return ImportModule(name, self._js, self._css)

  @property
  def vis(self):
    """
    Description:
    ------------
    A dynamic, browser based visualization library..

    TODO: Add the split of packages

    Related Pages:

      http://visjs.org
    """
    return ImportModule("vis", self._js, self._css)

  @property
  def d3(self):
    """
    Description:
    ------------
    D3.js is a JavaScript library for manipulating documents based on data.

    TODO: Add the split of packages

    Related Pages:

      https://d3js.org/
    """
    return ImportModule("d3", self._js, self._css)

  @property
  def dc(self):
    """
    Description:
    ------------
    dc.js is a javascript charting library with native crossfilter support, allowing highly efficient exploration on large multi-dimensional datasets.

    Related Pages:

      https://dc-js.github.io/dc.js
    """
    return ImportModule("dc", self._js, self._css)

  @property
  def nvd3(self):
    """
    Description:
    ------------
    This project is an attempt to build re-usable charts and chart components for d3.js without taking away the power that d3.js gives you.

    Related Pages:

      http://nvd3.org/
    """
    return ImportModule("nvd3", self._js, self._css)

  @property
  def c3(self):
    """
    Description:
    ------------
    C3.js D3-based reusable chart library.

    Related Pages:

      https://c3js.org/
    """
    return ImportModule("c3", self._js, self._css)

  @property
  def billboard(self):
    """
    Description:
    ------------
    Re-usable, easy interface JavaScript chart library, based on D3 v4+.

    Related Pages:

      https://naver.github.io/billboard.js/
    """
    return ImportModule("billboard.js", self._js, self._css)

  @property
  def chart_js(self):
    """
    Description:
    ------------
    Simple yet flexible JavaScript charting for designers & developers.

    Related Pages:

      https://www.chartjs.org/
    """
    return ImportModule("chart.js", self._js, self._css)

  @property
  def crossfilter(self):
    """
    Description:
    ------------
    Fast Multidimensional Filtering for Coordinated Views.

    Related Pages:

      http://square.github.io/crossfilter
    """
    return ImportModule("crossfilter", self._js, self._css)

  @property
  def apexcharts(self):
    """
    Description:
    ------------
    Modern & Interactive Open-source Charts.

    Related Pages:

      https://apexcharts.com
    """
    return ImportModule("apexcharts", self._js, self._css)

  @property
  def plotly(self):
    """
    Description:
    ------------
    Plotly JavaScript Open Source Graphing Library.

    Related Pages:

      https://plot.ly/javascript/
    """
    return ImportModule("plotly.js", self._js, self._css)

  @property
  def ag_grid(self):
    """
    Description:
    ------------
    The Best JavaScript Grid in the World.

    Related Pages:

      https://www.ag-grid.com/javascript-grid/
    """
    return ImportModule("ag-grid-community", self._js, self._css)

  @property
  def bootstrap(self):
    """
    Description:
    ------------
    The most popular front-end framework for developing responsive, mobile first projects on the web.

    Related Pages:

      https://getbootstrap.com/
    """
    return ImportModule("bootstrap", self._js, self._css)

  @property
  def jquery(self):
    """
    Description:
    ------------
    JavaScript library for DOM operations.

    Related Pages:

      https://jquery.com
    """
    return ImportModule("jquery", self._js, self._css)

  @property
  def jqueryui(self):
    """
    Description:
    ------------
    jQuery UI is a curated set of user interface interactions, effects, widgets, and themes built on top of the jQuery JavaScript Library.

    Related Pages:

      https://jqueryui.com/
    """
    return ImportModule("jqueryui", self._js, self._css)

  @property
  def jquery_bracket(self):
    """
    Description:
    ------------
    jQuery bracket is a jQuery plugin that lets users create and display single and double elimination brackets for tournament play.

    Related Pages:

      http://www.aropupu.fi/bracket/
    """
    return ImportModule("jquery-bracket", self._js, self._css)

  @property
  def jquery_sparkline(self):
    """
    Description:
    ------------
    This jQuery plugin generates sparklines (small inline charts) directly in the browser using data supplied either inline in the HTML, or via javascript.

    Related Pages:

      https://omnipotent.net/jquery.sparkline
    """
    return ImportModule("jquery-sparkline", self._js, self._css)

  @property
  def jqvmap(self):
    """
    Description:
    ------------
    JQVMap is a jQuery plugin that renders Interactive, Clickable Vector Maps.

    Related Pages:

      https://www.10bestdesign.com/jqvmap/
    """
    return ImportModule("jqvmap", self._js, self._css)

  @property
  def qunit(self):
    """
    Description:
    ------------
    The powerful, easy-to-use JavaScript testing framework.

    Related Pages:

      https://qunitjs.com/
    """
    return ImportModule("qunit", self._js, self._css)

  @property
  def accounting(self):
    """
    Description:
    ------------
    number, money and currency formatting library.

    Related Pages:

      http://openexchangerates.github.io/accounting.js
    """
    return ImportModule("accounting", self._js, self._css)

  @property
  def qrcodejs(self):
    """
    Description:
    ------------
    QRCode.js is javascript library for making QRCode.
    QRCode.js supports Cross-browser with HTML5 Canvas and table tag in DOM. QRCode.js has no dependencies.

    Related Pages:

      https://davidshimjs.github.io/qrcodejs
    """
    return ImportModule("qrcodejs", self._js, self._css)

  @property
  def underscore(self):
    """
    Description:
    ------------
    accounting.js is a tiny JavaScript library by Open Exchange Rates, providing simple and advanced number, money and currency formatting.

    Related Pages:

      https://openexchangerates.github.io/accounting.js/
    """
    return ImportModule("underscore", self._js, self._css)

  @property
  def tabulator(self):
    """
    Description:
    ------------
    Interactive table generation JavaScript library.

    Related Pages:

      http://tabulator.info/
    """
    return ImportModule("tabulator-tables", self._js, self._css)

  @property
  def datatables(self):
    """
    Description:
    ------------
    Add advanced interaction controls to your HTML tables the free & easy way.

    Related Pages:

      https://datatables.net/
    """
    return ImportModule("tabulator-tables", self._js, self._css)

  @property
  def mathjax(self):
    """
    Description:
    ------------
    Beautiful and accessible math in all browsers.

    Related Pages:

      https://www.mathjax.org/
    """
    return ImportModule("mathjax", self._js, self._css)

  @property
  def moment(self):
    """
    Description:
    ------------

    Related Pages:


    """
    return ImportModule("moment", self._js, self._css)

  @property
  def hammer(self):
    """
    Description:
    ------------
    Add touch gestures to your webapp.

    Related Pages:

      https://hammerjs.github.io/
    """
    return ImportModule("hammer", self._js, self._css)

  @property
  def popper_js(self):
    """
    Description:
    ------------
    Tooltip & Popover Positioning Engine.

    Related Pages:

      https://github.com/popperjs/popper-core
    """
    return ImportModule("@popperjs/core", self._js, self._css)

  @property
  def font_awesome(self):
    """
    Description:
    ------------
    The next generation of our icon library + toolkit is coming with more icons, more styles, more services, and more awesome

    Related Pages:

      https://fontawesome.com
    """
    return ImportModule("font-awesome", self._js, self._css)

  @property
  def json_formatter(self):
    """
    Description:
    ------------
    Render JSON objects in HTML with a collapsible navigation.

    Related Pages:

      https://azimi.me/json-formatter-js/
    """
    return ImportModule("json-formatter-j", self._js, self._css)

  @property
  def pivottable(self):
    """
    Description:
    ------------
    Open-source Javascript Pivot Table (aka Pivot Grid, Pivot Chart, Cross-Tab) implementation with drag'n'drop.

    Related Pages:

      https://github.com/nicolaskruchten/pivottable
    """
    return ImportModule("pivottable", self._js, self._css)

  @property
  def require_js(self):
    """
    Description:
    ------------
    RequireJS is a JavaScript file and module loader. It is optimized for in-browser use, but it can be used in other JavaScript environments, like Rhino and Node

    Related Pages:

      https://requirejs.org/
    """
    return ImportModule("requirejs", self._js, self._css)

  @property
  def timepicker(self):
    """
    Description:
    ------------
    jQuery Timepicker is a plugin to enhance standard form input fields, helping users to select (or type) times.

    Related Pages:

      https://timepicker.co
    """
    return ImportModule("timepicker", self._js, self._css)

  @property
  def socket(self):
    """
    Description:
    ------------
    Realtime application framework.
    Socket.IO enables real-time bidirectional event-based communication.

    Related Pages:

      https://github.com/socketio/socket.io
    """
    return ImportModule("socket.io", self._js, self._css)

  @property
  def codemirror(self):
    """
    Description:
    ------------
    CodeMirror is a versatile text editor implemented in JavaScript for the browser.

    Related Pages:

      https://codemirror.net
    """
    return ImportModule("codemirror", self._js, self._css)

  @property
  def highlight(self):
    """
    Description:
    ------------
    Syntax highlighting for the Web.

    Related Pages:

      https://highlightjs.org/
    """
    return ImportModule("highlight.js", self._js, self._css)

  @property
  def leaflet(self):
    """
    Description:
    ------------
    An open-source JavaScript library for mobile-friendly interactive maps.

    Related Pages:

      https://leafletjs.com/
    """
    return ImportModule("leaflet", self._js, self._css)

  @property
  def showdown(self):
    """
    Description:
    ------------
    Showdown is a Javascript Markdown to HTML converter.

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return ImportModule("showdown", self._js, self._css)

  @property
  def sortablejs(self):
    """
    Description:
    ------------
    Create and reorder lists with drag-and-drop. For use with modern browsers and touch devices.

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return ImportModule("sortablejs", self._js, self._css)


class ImportManager:
  """
  Description:
  ------------
  The main class in charge of defining the order of the imports in the header.

  There is no check on the presence of the modules on the server. The only purpose of this module is to produce the
  string with the module names and the correct paths to your final HTML report.
  """

  online = True
  static_path = '/static'

  def __init__(self, report=None):
    """
    Description:
    ------------
    Load the hierarchy of modules.
    This module will define the import section in the header of the final HTML page.

    It will create links to the official online websites or link to an internal copy if no internet connection is
    available. To run a report using the online mode to False it is requires to get all the packages locally
    saved with the expected structured (basically the one of the CDNJ repository)

    Attributes:
    ----------
    :param report: Optional. The internal report object with all the required external modules
    """
    self._report, ovr_version = report, {}
    if report is not None and report.ext_packages is not None:
      extend_imports(report.ext_packages)
    #if report is not None and self._report.run.report_name is not None and self._report.run.local_path is not None and os.path.exists(os.path.join(self._report.run.local_path, '__init__.py')):
      # Force the version of some external Javascript or CSS packages
    #  packages = importlib.import_module("%s.__init__" % self._report.run.report_name)
    #  ovr_version = getattr(packages, 'MODULES', {})
    if report is not None:
      self._report._with_google_imports = False
      # Apply the different reports overrides on the packages versions
      ovr_version.update(self._report._props.get('packages', {}))
    self.jsImports, self.cssImports, self.moduleConfigs, self.reqVersion = {}, {}, {}, {}
    for folder, import_cict, import_type in [('js', self.jsImports, JS_IMPORTS), ('css', self.cssImports, CSS_IMPORTS)]:
      for alias, definition in import_type.items():
        main = collections.OrderedDict()
        for i, mod in enumerate(definition['modules']):
          if alias in ovr_version:
            mod['version'] = ovr_version[alias]
          #elif 'version' not in mod:
          #  # take the version from the main package definition
          #  mod['version'] = JS_IMPORTS[alias]["version"] if alias in JS_IMPORTS else CSS_IMPORTS[alias]["version"]
          #script = "".join([mod['path'] % mod, mod['script']])
          script_path = script_cdnjs_path(alias, mod)
          if 'url' in definition:
            main["%s%s" % (definition['url'], mod['script'])] = mod['version']
          else:
            main[script_path] = script_version(alias, mod)
          #if online:
          #  main["%s/%s" % (mod['cdnjs'], script)] = mod['version']
          #elif 'url' in definition:
          #  main["%s%s" % (definition['url'], script)] = mod['version']
          #else:
          #  main["%s/%s" % (STATIC_PATH.replace("\\", "/"), script)] = mod['version']
        modules = collections.OrderedDict()
        self.getModules(modules, alias, folder, import_type)
        if 'config' in definition:
          self.moduleConfigs[alias] = definition['config']
        mainKeys, versions = [], []
        for k, v in main.items():
          mainKeys.append(k)
          versions.append(v)
        import_cict[alias] = {'main': main, 'dep': list(modules.keys()), 'versions': versions}

  @property
  def requirements(self):
    """
    Description:
    ------------
    Retrieve all the mandatory requirements required to display the final HTML page.

    Usage:

      print(page.imports().requirements)
    """
    module_alias = set(self.cleanImports(self._report.jsImports, JS_IMPORTS))
    for css in self.cleanImports(self._report.cssImport, CSS_IMPORTS):
      module_alias.add(css)
    return module_alias

  def getModules(self, modules, alias, folder=None, module_details=None):
    """
    Description:
    ------------
    Return the list of modules for a given entry.
    This will be used recursively to resolve all the dependencies.

    Usage:
    -----

      modules = collections.OrderedDict()
      ImportManager().getModules(modules, 'c3')

    Attributes:
    ----------
    :param modules: List. The list of modules
    :param alias: String. The module reference in the above JS and CSS dictionaries
    :param folder: String. Optional. The folder name
    :param module_details: Optional. The module definition. Default check in the JavaScipt modules

    :return: The list of modules
    """
    if module_details is None:
      module_details = dict(JS_IMPORTS)
    if isinstance(alias, dict):
      alias = alias['alias']

    for mod in module_details[alias]['modules']:
      if 'version' not in mod:
        # take the version from the main package definition
        mod['version'] = JS_IMPORTS[alias]["version"] if alias in JS_IMPORTS else CSS_IMPORTS[alias]["version"]
      script = "".join([mod['path'] % mod, mod['script']])
      if 'url' in module_details[alias]:
        modules["%s/%s" % (module_details[alias]['url'], script)] = True
      else:
        modules[r"%s\%s" % (STATIC_PATH.replace("\\", "/"), script)] = True
    for req in module_details.get(alias, {}).get('req', []):
      self.getModules(modules, req, folder, module_details)
    return modules

  def getReq(self, mod, modules, import_hierarchy=None):
    """
    Description:
    ------------
    Set the list pf required modules for a given alias to the modules list.

    Usage:
    -----

      deps = []
      page.imports.getReq("c3", deps)
      print(deps)

    Attributes:
    ----------
    :param mod: String. The alias of the external package.
    :param modules: List. The list of packages aliases in the inverse dependency order.
    :param import_hierarchy: Dictionary. Optional. The package definition (Javascript or CSS) from the above import lists.

    """
    import_hierarchy = import_hierarchy or JS_IMPORTS
    if isinstance(mod, dict):
      # This will allow different versions of packages according to the modules
      # For example NVD3 cannot use any recent version of D3
      if 'version' in mod:
        if self._report is not None and self._report.verbose:
          logging.warning("Setting %(alias)s to version %(version)s" % mod)
        self.reqVersion[mod['alias']] = mod['version']
        new_main_for_alias, new_main_for_alias_css = collections.OrderedDict(), collections.OrderedDict()
        for path in self.jsImports[mod['alias']]['main']:
          for v in self.jsImports[mod['alias']]['versions']:
            new_main_for_alias[path.replace(v, mod['version'])] = mod['version']
        if mod['alias'] in self.cssImports:
          for path in self.cssImports[mod['alias']]['main']:
            for v in self.cssImports[mod['alias']]['versions']:
              new_main_for_alias_css[path.replace(v, mod['version'])] = mod['version']
          self.cssImports[mod['alias']]['main'] = new_main_for_alias_css
        # Store the new dictionary with the key and version updated for the module
        self.jsImports[mod['alias']]['main'] = new_main_for_alias
        for i, path in enumerate(self.jsImports[mod['alias']]['dep']):
          for v in self.jsImports[mod['alias']]['versions']:
            path = path.replace(v, mod['version'])
          self.jsImports[mod['alias']]['dep'][i] = path
      mod = mod['alias']
    modules.append(mod)
    for req in import_hierarchy.get(mod, {}).get("req", []):
      self.getReq(req, modules, import_hierarchy)

  def cleanImports(self, imports, import_hierarchy=None):
    """
    Description:
    ------------
    Remove the underlying imports to avoid duplicated entries.

    Usage:
    -----

      >>> ImportManager().cleanImports(['c3'], JS_IMPORTS)
    ['jquery', 'd3', 'c3']

    Attributes:
    ----------
    :param imports: List. An array with the list of aliases for the external packages.
    :param import_hierarchy: Dictionary. Optional. The package definition (Javascript or CSS) from the above import lists.

    :return: Return the list with the full list of aliases (including dependencies)
    """
    import_resolved = []
    for mod in imports:
      self.getReq(mod, import_resolved, import_hierarchy or JS_IMPORTS)
    for a in set(import_resolved):
      if a in PACKAGE_STATUS:
        if not PACKAGE_STATUS[a].get("allowed", True):
          raise Exception("Package %s not allowed" % a)
        if self._report is not None and self._report.verbose:
          logging.warning("%s: %s" % (a, PACKAGE_STATUS[a].get("info", "")))
      occurences = [j for j, x in enumerate(import_resolved) if x == a]
      if len(occurences) > 1:
        for j in occurences[::-1][1:]:
          import_resolved.pop(j)
    return import_resolved[::-1]

  def cssResolve(self, css_aliases, local_css=None, excluded=None):
    """
    Description:
    ------------
    Return the list of CSS modules to add to the header.

    Usage:
    -----

      >>> ImportManager().cssResolve(['c3'])
    '<link rel="stylesheet" href="/static/c3/0.6.12/c3.min.css" type="text/css">'

    Attributes:
    ----------
    :param css_aliases: List. An array with the list of aliases for the external packages.
    :param local_css: Dictionary. Optional. The external file overrides with the full path.
    :param excluded: List. Optional. Packages excluded from the result object (mandatory for some frameworks already onboarding modules).

    :return: The string to be added to the header.
    """
    css = []
    # Import hierarchy will rely on the JS_IMPORT definition.
    css_aliases = [c for c in self.cleanImports(css_aliases, JS_IMPORTS) if c in CSS_IMPORTS]
    for css_alias in css_aliases:
      if excluded is not None and css_alias in excluded:
        continue

      if not self.online:
        self.pkgs.get(css_alias).set_local(static_url=self.static_path)

      if css_alias in _SERVICES:
        # Add services url
        for service in _SERVICES[css_alias].get('css', []):
          css.append('<link rel="stylesheet" href="%s">' % service)
        continue

      for urlModule in list(self.cssImports[css_alias]['main']):
        if self._report._node_modules is not None:
          node_sub_path = CSS_IMPORTS.get(css_alias, {}).get('register', {}).get('npm_path')
          if node_sub_path is not None:
            css_file = os.path.split(urlModule)[1]
            npm_alias = CSS_IMPORTS[css_alias]['register'].get('npm', css_alias)
            package_path = os.path.join(self._report._node_modules[0], "node_modules", npm_alias, node_sub_path, css_file)
            if os.path.exists(package_path):
              urlModule = os.path.join(self._report._node_modules[1], npm_alias, node_sub_path, css_file).replace("\\", "/")
        css.append('<link rel="stylesheet" href="%s" type="text/css">' % urlModule)
    if local_css is not None:
      for localCssFile in local_css:
        css.append('<link rel="stylesheet" href="%s" type="text/css">' % localCssFile)
    return "\n".join(css)

  def cssURLs(self, css_str):
    """
    Description:
    ------------
    Retrieve the list of CSS dependencies URL from a header

    Usage:
    -----

    Attributes:
    ----------
    :param css_str: String. The CSS String in the page

    :return: A Python list with all the CSS external URL to be imported
    """
    return re.findall('<link rel="stylesheet" href="(.*?)" type="text/css">', css_str)

  def jsResolve(self, js_aliases, local_js=None, excluded=None):
    """
    Description:
    ------------
    Return the list of Javascript modules to add to the header.

    Usage:
    -----

      >>> ImportManager().jsResolve(['c3'])
    '<script language="javascript" type="text/javascript" src="/static/jquery/3.4.1/jquery.min.js"></script>\n<script language="javascript" type="text/javascript" src="/static/d3/5.9.7/d3.min.js"></script>\n<script language="javascript" type="text/javascript" src="/static/c3/0.6.12/c3.min.js"></script>'

    Attributes:
    ----------
    :param js_aliases: List. An array with the list of aliases for the external packages.
    :param local_js: Dictionary. Optional. The external file overrides with the full path.
    :param excluded: List. Optional. Packages excluded from the result object (mandatory for some frameworks already onboarding modules).

    :return: The string to be added to the header
    """
    js = []
    js_aliases = self.cleanImports(js_aliases, JS_IMPORTS)
    for js_alias in js_aliases:
      if excluded is not None and js_alias in excluded:
        continue

      if not self.online:
        self.pkgs.get(js_alias).set_local(static_url=self.static_path)
      extra_configs = "?%s" % self.moduleConfigs[js_alias] if js_alias in self.moduleConfigs else ""
      for url_module in list(self.jsImports[js_alias]['main']):
        if self._report._node_modules is not None:
          node_sub_path = JS_IMPORTS.get(js_alias, {}).get('register', {}).get('npm_path')
          if node_sub_path is not None:
            js_file = os.path.split(url_module)[1]
            npm_alias = JS_IMPORTS[js_alias]['register'].get('npm', js_alias)
            package_path = os.path.join(self._report._node_modules[0], "node_modules", npm_alias, node_sub_path, js_file)
            if os.path.exists(package_path):
              url_module = os.path.join(self._report._node_modules[1], npm_alias, node_sub_path, js_file).replace("\\", "/")

        if '/mode/' in url_module:
          js.append('<script type="module" language="javascript" src="%s%s"></script>' % (url_module, extra_configs))
        else:
          js.append('<script language="javascript" type="text/javascript" src="%s%s"></script>' % (url_module, extra_configs))
    if local_js is not None and len(local_js) > 0:
      for local_js_file in local_js:
        js.append('<script language="javascript" type="text/javascript" src="%s"></script>' % local_js_file)
    return "\n".join(js)

  def jsURLs(self, js_str):
    """
    Description:
    ------------
    Retrieve the list of Javascript dependencies URL from a header

    Usage:
    -----

    Attributes:
    ----------
    :param js_str: String. The Javascript String in the page.

    :return: A Python list with all the Javascript external URL to be imported
    """
    return re.findall('<script language="javascript" type="text/javascript" src="(.*?)"></script>', js_str)

  def getFiles(self, cssAlias, jsAlias):
    """
    Description:
    ------------
    retrieve the package definition from the list of module aliases

    Usage:
    -----

      >>> ImportManager().getFiles(['c3'], ['c3'])
    f['css'][0]['file']['script']

    Attributes:
    ----------
    :param cssAlias: List. An array with the list of aliases for the CSS external packages
    :param jsAlias: List. An array with the list of aliases for the Js external packages

    :return: A dictionary with the CSS and JS files definition
    """
    files = {'css': [], 'js': []}
    mod_css, mod_js = {}, {}
    for alias, details in CSS_IMPORTS.items():
      mod_css[alias] = []
      for module in details['modules']:
        mod_css[alias].append({'version': module.get('version', ''), 'alias': alias, 'file': module, 'website':
          details.get('website', ''), 'status': details.get('status', '')})
    for alias, details in JS_IMPORTS.items():
      mod_js[alias] = []
      for module in details['modules']:
        mod_js[alias].append({'version': module.get('version', ''), 'alias': alias, 'file': module, 'website':
          details.get('website', ''), 'status': details.get('status', '')})
    for css_file in self.cleanImports(cssAlias, CSS_IMPORTS):
      files['css'].extend(mod_css[css_file])
    for js_file in self.cleanImports(jsAlias, JS_IMPORTS):
      files['js'].extend(mod_js[js_file])
    return files

  def cssGetAll(self):
    """
    Description:
    ------------
    To retrieve the full list of available modules on the server.

    This will return the dependencies as they should be included in the HTML page.
    The order and the path resolution is already performed.

    If split is True the generated css file will be not included.

    Usage:
    -----

      print(page.imports.cssGetAll())
    """
    return self.cssResolve(set(CSS_IMPORTS.keys()))

  def jsGetAll(self):
    """
    Description:
    ------------
    To retrieve the full list of available modules on the server.

    This will return the dependencies as they should be included in the HTML page.
    The order and the path resolution is already performed.

    If split is True the generated JS file will be not included.

    Usage:
    -----

      print(page.imports.jsGetAll())
    """
    return self.jsResolve(set(JS_IMPORTS.keys()))

  # def getPackage(self, alias, version=None, static_path=None, with_dep=False, reload=True):
  #   """
  #   Description:
  #   ------------
  #   Function in charge of downloading the different external CSS and JS packages locally.
  #   This will guarantee the install without having to get any extra features saved on a repository.
  #   Saved copies of the modules can be done in order to guarantee a offline mode
  #
  #   Usage:
  #   -----
  #
  #     Imports.ImportManager(report=Report()).getPackage('jqueryui')
  #
  #   Attributes:
  #   ----------
  #   :param alias: String. The package reference in the above list
  #   :param version: String. Optional. The package version to retrieve
  #   :param static_path: Optional. The path in which the files should be copied to
  #   :param with_dep: Optional. Flag to specify if the dependencies should be updated. Default False
  #   :param reload: Optional. Flag to force the package reloading if the folder already exists. Default Yes
  #
  #   """
  #   if not hasattr(self._report, "py"):
  #     from epyk.core.py.PyRest import PyRest
  #     webscrapper = PyRest().webscrapping
  #   else:
  #     webscrapper = self._report.py.requests.webscrapping
  #
  #   if not static_path.endswith("static"):
  #     static_path = os.path.join(static_path, "static")
  #   packages = {}
  #   _static_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static') if static_path is None else static_path
  #   if not _static_path.endswith("static"):
  #     _static_path = os.path.join(_static_path, "static")
  #   for pckg in [JS_IMPORTS, CSS_IMPORTS]:
  #     if with_dep:
  #       for depAlias in self.cleanImports([alias], pckg):
  #         if depAlias != alias:
  #           self.getPackage(depAlias, reload=reload)
  #     if 'package' in pckg.get(alias, {}):
  #       packages[alias] = os.path.join(_static_path, pckg[alias]['package']['folder'])
  #     for mod in pckg.get(alias, {}).get('modules', []):
  #       if 'version' not in mod:
  #         mod['version'] = pckg.get(alias, {})['version']
  #       _version = self.reqVersion.get(alias, mod['version']) if version is None else version
  #       script = "".join([mod['path'] % {'version': _version}, mod['script']])
  #       path = os.path.join(_static_path, mod['path'] % {'version': _version})
  #       if not os.path.exists(path):
  #         os.makedirs(path)
  #       reloadModule = True
  #       extFilePath = r"%s\%s" % (path, mod['script'])
  #       if os.path.exists(extFilePath) and not reload:
  #         reloadModule = False
  #
  #       if reloadModule:
  #         page = webscrapper("%s/%s" % (mod['cdnjs'], script))
  #         if hasattr(page, 'code') and page.code == 404:
  #           logging.warning(" # Error - %s: Script %s/%s not found " % (alias, mod['cdnjs'], script))
  #           continue
  #
  #         try:
  #           extFileName = open(extFilePath, "wb")
  #           extFileName.write(page)
  #           extFileName.close()
  #           logging.warning("  > %s - %s, version %s. Done !" % (alias, mod['script'], _version))
  #         except Exception as err:
  #           logging.warning(" # Exception - %s: %s/%s, %s" % (alias, mod['script'], _version, err))
  #           logging.warning(err)
  #       else:
  #         logging.warning("  > %s - %s, version %s. Already defined !" % (alias, mod['script'], _version))
  #
  #   if len(packages) > 0:
  #     logging.warning("Downloading %s packages, this might take few minutes" % len(packages))
  #     for pckg, folder in packages.items():
  #       self.getFullPackage(pckg, version=version, static_path=static_path, reload=reload)

  def getFullPackage(self, alias, version=None, static_path=None, reload=False):
    """
    Description:
    ------------
    Download a full package (CSS and JS) locally for a server or full offline mode.

    Usage:
    -----

      Imports.ImportManager(report=Report()).getFullPackage('font-awesome')

    Attributes:
    ----------
    :param alias: String. The package reference in the above list
    :param version: String. Optional. The package version to retrieve
    :param static_path: String. Optional. The path in which the files should be copied to
    :param reload: Boolean. Optional. Flag to force the package reloading if the folder already exists. Default False

    :return: The Python Import manager
    """

    import zipfile
    import shutil
    import io
    import os

    if not hasattr(self._report, "py"):
      from epyk.core.py.PyRest import PyRest
      webscrapper = PyRest().webscrapping
    else:
      webscrapper = self._report.py.requests.webscrapping

    if 'package' in JS_IMPORTS[alias]:
      if 'version' not in JS_IMPORTS[alias]['modules'][0]:
        JS_IMPORTS[alias]['modules'][0]['version'] = JS_IMPORTS[alias]['version']
      versionDict = {'version': JS_IMPORTS[alias]['modules'][0]['version'] if version is None else version}
      packagePath = JS_IMPORTS[alias]['package']['zip'] % versionDict
      if static_path is None:
        static_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static', JS_IMPORTS[alias]['package']['folder'])
      else:
        static_path = os.path.join(static_path, "static")
      if not os.path.exists(static_path):
        # Create the destination folders if missing
        os.makedirs(static_path)
      dstPath = os.path.join(static_path, JS_IMPORTS[alias]['package'].get('folder', ''), JS_IMPORTS[alias]['package'].get('path', '%(version)s') % versionDict)
      vReloadPath = True
      if os.path.exists(dstPath):
        if not reload:
          vReloadPath = False
        else:
          shutil.rmtree(dstPath)

      if vReloadPath:
        logging.warning("  > Downloading package %s" % packagePath)
        r = webscrapper(packagePath)
        z = zipfile.ZipFile(io.BytesIO(r))
        #z = zipfile.ZipFile(io.BytesIO(r))
        z.extractall(static_path)
        if JS_IMPORTS[alias]['package']['root'] is not None:
          root = JS_IMPORTS[alias]['package']['root'] % versionDict
          shutil.copytree(os.path.join(static_path, root), dstPath)
          shutil.rmtree(os.path.join(static_path, root))
        logging.warning("  < Package %s. Done ! " % alias)
      else:
        logging.warning("  < Package %s already loaded " % alias)
    return self

  # def package(self, alias):
  #   """
  #   Description:
  #   ------------
  #   Returns the packages used in the Framework for both Js and CSS perimeters.
  #
  #   Usage:
  #   -----
  #
  #     >>> len(ImportManager().package('jqueryui')['modules'])
  #   4
  #
  #   Attributes:
  #   ----------
  #   :param alias: The package reference in the above lists
  #
  #   :return: A dictionary with the package details
  #   """
  #   res = {}
  #   if alias in CSS_IMPORTS:
  #     res.update(CSS_IMPORTS[alias])
  #   if alias in JS_IMPORTS:
  #     for k, v in JS_IMPORTS[alias].items():
  #       if k in res:
  #         if isinstance(v, list):
  #           res[k].extend(v)
  #       else:
  #         res[k] = v
  #   return res

  def setVersion(self, alias, version):
    """
    Description:
    ------------
    Allow the use of different version of a package.

    This will change the Import important to the Python env.

    Usage:
    -----

    Attributes:
    ----------
    :param alias: String. The package reference in the above list.
    :param version: String. The new version to be used globally.
    """
    self.reqVersion[alias] = version
    for modType in [CSS_IMPORTS, JS_IMPORTS]:
      if alias in modType:
        for mod in modType[alias].get('modules', []):
          mod['version'] = version

  def addPackage(self, alias, config):
    """
    Description:
    ------------
    Add a new package or update an existing one with new parameters.
    Only few parameters are available here in order to limit the changes.

    Usage:
    -----

      i.addPackage('test',
      {
        'req': [{'alias': 'd3'}],
        'modules': [
          {'script': 'dc.min.css', 'version': '3.0.9', 'path': 'dc/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'script': 'dc.min.js', 'version': '3.0.9', 'path': 'dc/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
        ]},
      )

    Attributes:
    ----------
    :param alias: String. The package alias.
    :param config: Dictionary. The Python dictionary with the package details.

    :return: The import Manager.
    """

    global CSS_IMPORTS
    global JS_IMPORTS

    mod_entry = {'css': {}, 'js': {}}
    for mod in config['modules']:
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
        if 'req' in config:
          for req in config['req']:
            if req['alias'] in JS_IMPORTS:
              mod_entry['js'].setdefault('req', []).append(req)
    if len(mod_entry['css']) > 0:
      CSS_IMPORTS.setdefault(alias, {}).update(mod_entry['css'])
      self.cssImports[alias] = {"main": collections.OrderedDict(), 'versions': [], 'dep': []}
      for pkg in mod_entry['js']["modules"]:
        self.cssImports[alias]["main"][script_cdnjs_path(alias, pkg)] = pkg.get("version", config["version"])
    if len(mod_entry['js']) > 0:
      JS_IMPORTS.setdefault(alias, {}).update(mod_entry['js'])
      JS_IMPORTS[alias]["version"] = config.get("version", "")
      self.jsImports[alias] = {"main": collections.OrderedDict(), 'versions': [], 'dep': []}
      for pkg in mod_entry['js']["modules"]:
        self.jsImports[alias]["main"][script_cdnjs_path(alias, pkg)] = pkg.get("version", config.get("version", ''))
    return self

  # def getPackages(self, static_path=None, reload=False, exclude=None):
  #   """
  #   Description:
  #   ------------
  #   Download all the CSS and Js packages from the official CDNJS configured in the configuration.
  #   It is possible to get the configuration settings by calling the function getPackageInfo(aliasName) attached to the report
  #
  #   Usage:
  #   -----
  #
  #   Attributes:
  #   ----------
  #   :param static_path: The package reference in the above list
  #   :param reload: Optional. Flag to force the package reloading if the folder already exists. Default False
  #   :param exclude: Optional.
  #
  #   :return: The Python Import manager
  #   """
  #   if exclude is None:
  #     exclude = []
  #   if not static_path.endswith("static"):
  #     static_path = os.path.join(static_path, "static")
  #   aliases = list(set(list(CSS_IMPORTS.keys()) + list(JS_IMPORTS.keys())))
  #   for alias in aliases:
  #     self.getPackage(alias, static_path=static_path, reload=reload)
  #   return self

  def to_requireJs(self, data, excluded_packages=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data: Dictionary. The Report modules to resolve
    :param excluded_packages: Optional. List. The packages to exclude
    """
    deps_level, alias_to_name, name_to_alias, results = {}, {}, {}, {'jsFrgs': data['jsFrgs'], 'paths': {}}
    m_versions = {}

    # Check first if some specific versions are required for the packages
    for m in self._report.jsImports:
      for req in JS_IMPORTS[m].get('req', []):
        if 'version' in req:
          m_versions[req['alias']] = req['version']

    # Produce the dependency tree for requirejs
    for m in self.cleanImports(self._report.jsImports, JS_IMPORTS):
      if excluded_packages is not None and m in excluded_packages:
        continue

      if 'register' in JS_IMPORTS[m]:
        alias = JS_IMPORTS[m]['register']['alias']
        first_module = JS_IMPORTS[m]['modules'][0]
        if 'version' not in first_module:
          first_module['version'] = JS_IMPORTS[m]['version']
        if m in m_versions:
          first_module['version'] = m_versions[m]
        results['paths'][alias] = "%s/%s%s" % (first_module['cdnjs'], first_module['path'] % first_module,
                                     JS_IMPORTS[m]['register'].get('module', first_module['script'][:-3]))
        alias_to_name[m] = alias
        name_to_alias[alias] = m
        if 'req' in JS_IMPORTS[m]:
          max_level = max([deps_level[alias['alias']] if alias['alias'] in deps_level else -1 for alias in
                           JS_IMPORTS[m]['req']])
          deps_level[m] = max_level + 1
        else:
          deps_level[m] = 0

    # Create the chains of modules to be loaded
    level, group = None, []
    for k, v in sorted(deps_level.items(), key=lambda item: item[1])[::-1]:
      if level is None:
        level = v
      if level != v:
        for g in group:
          if 'init_fnc' in JS_IMPORTS[name_to_alias[g]]['register']:
            results['jsFrgs'] = "%s; %s" % (JS_IMPORTS[name_to_alias[g]]['register']['init_fnc'], results['jsFrgs'])
        results['jsFrgs'] = "require(['%s'], function (%s) { %s })" % (
        "', '".join([g for g in group]), ", ".join([g for g in group]), results['jsFrgs'])
        level, group = v, [alias_to_name[k]]
      else:
        group.append(alias_to_name[k])
    if group:
      for g in group:
        if 'init_fnc' in JS_IMPORTS[name_to_alias[g]]['register']:
          results['jsFrgs'] = "%s; %s" % (JS_IMPORTS[name_to_alias[g]]['register']['init_fnc'], results['jsFrgs'])
      results['jsFrgs'] = "require(['%s'], function (%s) { %s })" % (
      "', '".join([g for g in group]), ", ".join([g for g in group]), results['jsFrgs'])
    return results

  def show(self, all=False):
    """
    Description:
    ------------
    Show all the underlying packages used in a report or available in the framework.

    Usage:
    -----

    Attributes:
    ----------
    :param all: Boolean. Optional. A flag to specify if only the one requested in the report should be displayed
    """
    packages = {}
    if not all:
      for imp, repo in [(self._report.cssImport, CSS_IMPORTS), (self._report.jsImports, JS_IMPORTS)]:
        pkg = self.cleanImports(imp, repo)
        for c in pkg:
          for s in repo[c].get('modules', []):
            if 'version' not in s:
              s["version"] = JS_IMPORTS[c]['version'] if c in JS_IMPORTS else CSS_IMPORTS[c]['version'] # propagate the version number if not supplied from JS definition
            s['path'] = s['path'] % s
            packages.setdefault(c, []).append({"script": "%(cdnjs)s/%(path)s/%(script)s" % s, 'version': s['version']})
    else:
      for mod in [CSS_IMPORTS, JS_IMPORTS]:
        for c, pkg in mod.items():
          for s in pkg.get('modules', []):
            if 'version' not in s:
              s["version"] = JS_IMPORTS[c]['version'] if c in JS_IMPORTS else CSS_IMPORTS[c]['version'] # propagate the version number if not supplied
            s['path'] = s['path'] % s
            packages.setdefault(c, []).append({"script": "%(cdnjs)s/%(path)s/%(script)s" % s, 'version': s['version']})
    return packages

  def google_products(self, products, api_key=None, site_key="6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"):
    """
    Description:
    ------------
    Enable the google predefined products.

    Those are by default disabled as they are sharing data with Google.

    TODO: Add the use of the API Key.

    Usage:
    -----

      page.imports.google_products(['charts'])
      page.imports.google_products(['maps'])
      page.imports.google_products(['tables'])

      https://developers.google.com/recaptcha/docs/faq#id-like-to-run-automated-tests-with-recaptcha.-what-should-i-do

    Attributes:
    ----------
    :param products: List. The various Google products to enable in the report.
    :param api_key: String. Optional. The Google developer API key.
    :param site_key: String. Optional. The Google site key. https://developers.google.com/recaptcha/docs/v3
    """
    global JS_IMPORTS

    for p in products:
      for m in GOOGLE_EXTENSIONS[p].get("modules", []):
        m["script"] = m["script"] % {"api_key": api_key, 'site_key': site_key}
      self.addPackage("google-%s" % p, GOOGLE_EXTENSIONS[p])
      JS_IMPORTS["google-%s" % p] = GOOGLE_EXTENSIONS[p]
      if 'launcher' in GOOGLE_EXTENSIONS[p]:
        self._report._props.setdefault('js', {}).setdefault("builders", []).append(GOOGLE_EXTENSIONS[p]['launcher'])
    self._report._with_google_imports = True

  def locals(self, aliases, end_points=None):
    """
    Description:
    ------------
    Short circuit the import mechanism and retrieve the selected ones from a local static path.
    This could help on the debugging and the improvement of the packages before submitting them for review.

    Usage:
    -----

    Attributes:
    ----------
    :param aliases: List. Mandatory. The list of aliases
    :param end_points: String. Optional. The end point on the server (The module static_path as default)
    """
    global JS_IMPORTS
    global CSS_IMPORTS

    logging.warning("Routing packages %s locally this should not be put on a server !" % aliases)
    for alias in aliases:
      if alias in JS_IMPORTS:
        for m in JS_IMPORTS[alias]['modules']:
          m.update({'path': '', 'cdnjs': end_points or self.static_path})
    for alias in aliases:
      if alias in CSS_IMPORTS:
        for m in CSS_IMPORTS[alias]['modules']:
          m.update({'path': '', 'cdnjs': end_points or self.static_path})

  @property
  def pkgs(self):
    """
    Description:
    ------------
    Shortcut properties to the various package definitions.
    This can be used in the script in order to change the path of the version of any external modules used.
    """
    return ImportPackages(self.jsImports, self.cssImports)
