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

# To fully disable the automatic pip install request when a package is missing
AUTOLOAD = False
PROXY = ''
PCK_REPO = ''
STATIC_PATH = "/static"


def requires(name, reason='Missing Package', install=None, package=None, raise_except=False, source_script=None, pip_attrs=None):
  """
  System module

  Import the necessary external packages and provide explicit message to find a way to solve this error message.
  This method should also explain why this module is required to make sure this is really expected to get an error.

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
      print("Error with %s in script %s, autoload set to %s" % (name, source_script, AUTOLOAD))
      deps = json.loads(str(err).replace("Missing required dependencies ", "").replace("'", '"'))
      import subprocess
      for d in deps:
        exe_out = subprocess.call([sys.executable, '-m', "pip", 'install'] + pip_attrs + [d])
        print(exe_out)
      return requires(name, reason, install, package=package, raise_except=raise_except)

    if AUTOLOAD:
      if isinstance(AUTOLOAD, dict) and not AUTOLOAD.get(install, False):
        # Module not set in the configuration to be automatically loaded
        raise Exception(err)

      print("Error with %s in script %s, autoload set to %s" % (name, source_script, AUTOLOAD))
      import subprocess
      subprocess.call([sys.executable, '-m', "pip", 'install'] + pip_attrs + [install])

      return requires(name, reason, install, package=package, raise_except=raise_except)

    if raise_except:
      print("Error with %s in script %s, autoload set to %s" % (name, source_script, AUTOLOAD))
      print("*** Module %s required ***" % name)
      print(reason)
      if install:
        print("Command to fix this error:")
        print(">>> pip install %s" % install)
      print('')
      raise Exception(err)


def load_package(package_name, pip_attrs=None, action='install'):
  """
  Force the package to be installed manually to the currently python distribution.
  This will run a pip command to the running python set up

  Example
  load_package("pandas")

  Documentation
  https://pypi.org/

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
  Returns the list of packages installed on the running Python distribution

  This will require an internet connection as it will run the pip command behind the scene.
  It will return in the console a table with the status of the obsolescence of all the python packages

  Example
  installed_packages()
  """
  import subprocess
  subprocess.call(["pip", 'list', '-o'])


JS_IMPORTS = {
  # Plolyfill
  'promise-polyfill': {
    'modules': [
      # Better to use the bundle version to avoid the import issue with popper.js
      {'reqAlias': 'bootstrap', 'script': 'polyfill.min.js', 'version': '4.2.1', 'path': 'promise-polyfill@8/dist/', 'cdnjs': 'https://cdn.jsdelivr.net/npm'},
    ],
    'website': 'https://github.com/taylorhakes/promise-polyfill'},

  # Common module for browser versions compatibilities
  'babel-polyfill': {
    'website': 'https://babeljs.io/',
    'modules': [
      {'reqAlias': 'babel', 'script': 'polyfill.js', 'version': '7.4.4', 'path': 'babel-polyfill/%(version)s/',
       'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
    ]
  },

  # module are written from the first one to load to the last one
  'bootstrap': {
    'req': [
      {'alias': 'jquery'},
    ],
    'modules': [
      # Better to use the bundle version to avoid the import issue with popper.js
      {'reqAlias': 'bootstrap', 'script': 'bootstrap.bundle.min.js', 'version': '4.2.1', 'path': 'bootstrap/%(version)s/js/', 'cdnjs': 'https://stackpath.bootstrapcdn.com'},
    ],
    'website': 'https://getbootstrap.com/'},

  'moment': {
    'dsc': 'Module used by Tabulator for datetime objects',
    'modules': [
      {'reqAlias': 'moment', 'script': 'moment.min.js', 'version': '2.24.0', 'path': '%(version)s/',
       'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs/moment.js'},
    ],
    'website': 'https://momentjs.com/',
  },

  # module for tabulator
  'tabulator': {
    'req': [
      {'alias': 'promise-polyfill'},
    ],
    'modules': [
      # core only needed for Jupyter for some reasons
      {'reqAlias': 'tabulator_core', 'script': 'tabulator_core.min.js', 'version': '4.4.1', 'path': '%(version)s/js/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs/tabulator'},
      {'reqAlias': 'tabulator', 'script': 'tabulator.min.js', 'version': '4.4.1', 'path': '%(version)s/js/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs/tabulator'}
    ],
    'website': 'http://tabulator.info/'
  },

  # module for the awesome icons
  'font-awesome': {
    'package': {'zip': 'https://use.fontawesome.com/releases/v%(version)s/fontawesome-free-%(version)s-web.zip',
                'root': 'fontawesome-free-%(version)s-web', 'folder': 'releases', 'path': 'v%(version)s'},
    'modules': [
      {'reqAlias': 'fontawesome', 'script': 'fontawesome.js', 'version': '5.11.2', 'path': 'releases/v%(version)s/js/', 'cdnjs': 'https://use.fontawesome.com'}],
    'website': 'https://fontawesome.com/'},

  # Javascript packages to handle DataTables
  'datatables': {
    'req': [
      {'alias': 'jquery'},
      {'alias': 'bootstrap'}],
    'modules': [
      {'reqAlias': 'datatables', 'script': 'jquery.dataTables.min.js', 'version': '1.10.19', 'path': 'datatables/%(version)s/js/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
      {'script': 'dataTables.buttons.min.js', 'version': '1.0.1', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'dataTables.responsive.min.js', 'version': '2.1.1', 'path': 'responsive/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable group rows
  'datatables-rows-group': {
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'dataTables.rowsGroup.js', 'version': '1.0.0', 'path': 'datatables-rowsgroup/v%(version)s/', 'cdnjs': 'https://cdn.rawgit.com/ashl1'}],
       'website': 'https://datatables.net/forums/discussion/29319/new-rowsgroup-plugin-merge-cells-vertically-rowspan'},

  # Datatable group row
  'datatables-row-group': {
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'dataTables.rowGroup.min.js', 'version': '1.0.4', 'path': 'rowgroup/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}],
    'website': 'https://datatables.net/extensions/rowgroup/'},

  # Datatable fixed column
  'datatables-fixed-columns': {
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'dataTables.fixedColumns.min.js', 'version': '3.2.2', 'path': 'fixedcolumns/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}],
    'website': 'https://datatables.net/extensions/fixedcolumns/'},

  # Datatable Fixed header
  'datatables-fixed-header': {
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'dataTables.fixedHeader.min.js', 'version': '3.1.3', 'path': 'fixedheader/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}],
    'website': 'https://datatables.net/extensions/fixedheader/'},

  # Datatable data export
  'datatables-export': {
    'req': [
      {'alias': 'datatables'},
      {'alias': 'jszip'},
      {'alias': 'pdfmake'}],
    'website': 'https://datatables.net/extensions/buttons/',
    'modules': [
      {'script': 'buttons.colVis.min.js', 'version': '1.5.2', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.bootstrap4.min.js', 'version': '1.5.2', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.foundation.min.js', 'version': '1.5.2', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.html5.min.js', 'version': '1.5.2', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.jqueryui.min.js', 'version': '1.5.2', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.print.min.js', 'version': '1.5.2', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.semanticui.min.js', 'version': '1.5.2', 'path': 'buttons/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable column reordering modules
  'datatables-col-order': {
    'req': [{'alias': 'datatables'}],
    'website': 'https://datatables.net/extensions/colreorder/',
    'modules': [
      {'reqAlias': 'datatableColOrd', 'script': 'dataTables.colReorder.min.js', 'version': '1.5.1', 'path': 'colreorder/%(version)s/js/', 'cdnjs': 'https://cdn.datatables.net'}]},

  #
  'jszip': {
    'website': 'https://datatables.net/extensions/buttons/',
    'modules': [
      {'reqAlias': 'jszip', 'script': 'jszip.min.js', 'version': '3.1.5', 'path': 'jszip/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
    ]},

  #
  # # Datatable column reordering modules
  # 'dataTables-select': {
  #   'req': [{'alias': 'dataTables'}], "status": 'deprecated',
  #                       'website': 'https://datatables.net/extensions/select/', 'version': '1.2.5',
  #                       'modules': ['dataTables.select.min.js'],
  #                       'cdnjs': ['https://cdn.datatables.net/select/1.2.5/js/']},

  # Datatable column resizable
  # 'dataTables-colResizable': {
  #   'req': [{'alias': 'dataTables'}],
  #   'modules': [
  #     {'script': 'dataTables.colResize.js', 'version': '0.0.11', 'path': 'ColResize/%(version)s/js/', 'cdnjs': 'https://cdn.rawgit.com/smasala'}],
  #   'website': 'https://github.com/Silvacom/colResize'},

  # Datatable pivot
  'pivot': {
    'req': [{'alias': 'jqueryui'}],
    'website': 'https://github.com/nicolaskruchten/pivottable',
    'modules': [
      {'reqAlias': 'pivot', 'script': 'pivot.min.js', 'version': '2.23.0', 'path': 'pivottable/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # require.js
  'require.js': {
    'website': 'https://requirejs.org/',
    'modules': [
      {'script': 'require.min.js', 'version': '2.3.6', 'path': 'require.js/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Pivot Table SubTotal
  'pivot-sub-total': {
    'req': [{'alias': 'pivot'}],
    'website': 'http://nagarajanchinnasamy.com/subtotal/examples/',
    'modules': [
      {'reqAlias': 'subtotal', 'script': 'subtotal.js', 'version': '1.10.0', 'path': 'subtotal@%(version)s/dist/', 'cdnjs': 'https://cdn.jsdelivr.net/npm'}]},

  # Datatable pivot C3 renderer
  'pivot-c3': {
    'req': [{'alias': 'pivot'}],
    'website': 'https://github.com/nicolaskruchten/pivottable',
    'modules': [
      {'reqAlias': 'pivotC', 'script': 'c3_renderers.min.js', 'version': '2.21.0', 'path': 'pivottable/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Jquery package width CDN links
  'jquery': {
    'website': 'http://jquery.com/',
    'modules': [
      {'script': 'jquery.min.js', 'version': '3.4.1', 'path': 'jquery/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # QUnit package width CDN links
  'qunit': {
    'website': 'https://qunitjs.com',
    'modules': [
      {'script': 'qunit.min.js', 'version': '2.9.2', 'path': 'qunit/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Used to produce sparkline charts in a document and in Tabulator
  'jquery-sparklines': {
    'req': [{'alias': 'jquery'}],
    'website': 'https://omnipotent.net/jquery.sparkline/#s-about',
    'modules': [
      {'script': 'jquery.sparkline.min.js', 'version': '2.1.2', 'path': 'jquery-sparklines/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}
    ]
  },

  # Jquery UI package width CDN links
  'jqueryui': {
    'req': [{'alias': 'jquery'}],
    'website': 'http://jquery.com/',
    'modules': [
      {'reqAlias': 'jQueryUi', 'script': 'jquery-ui.min.js', 'version': '1.12.1', 'path': 'jqueryui/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Jquery-brackets package width CDN links
  'jquery-brackets': {
    'website': 'http://www.aropupu.fi/bracket/',
    'req': [{'alias': 'jquery'}],
    'modules': [
      {'reqAlias': 'jQueryBracket', 'script': 'jquery.bracket.min.js', 'version': '0.11.1', 'path': 'jquery-bracket/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Jquery UI package
  # Attempt to try to solve conflict with Bootstrap
  #'jquery-ui': {'req': ['jquery', 'bootstrap'], 'modules': ['jquery-ui.min.js']},

  # Jquery timepicker width CDN links
  'timepicker': {
    'website': 'https://timepicker.co/',
    'req': [
      {'alias': 'jquery'},
      {'alias': 'jqueryui'}],
    'modules': [
      {'reqAlias': 'jQueryTime', 'script': 'jquery.timepicker.min.js', 'version': '1.3.5', 'path': 'timepicker/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # To display a context menu when right click on an item
  'jquery-context-menu': {
    'website': 'http://swisnl.github.io/jQuery-contextMenu/demo.html',
    'req': [
      {'alias': 'jquery'},
      {'alias': 'jqueryui'}],
    'modules': [
      {'reqAlias': 'jQueryContext', 'script': 'jquery.contextMenu.min.js', 'version': '2.6.4', 'path': 'jquery-contextmenu/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # To customize the scrollbar width CDN links
  # https://github.com/malihu/malihu-custom-scrollbar-plugin
  # http://manos.malihu.gr/repository/custom-scrollbar/demo/examples/complete_examples.html
  'jquery-scrollbar': {
    'website': 'http://manos.malihu.gr/jquery-custom-content-scroller/',
    'req': [{'alias': 'jquery'}],
    'modules': [
      {'reqAlias': 'jQueryScrollBar', 'script': 'jquery.mCustomScrollbar.concat.min.js', 'version': '3.1.5', 'path': 'malihu-custom-scrollbar-plugin/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Javascript packages for the PDF transformation width CDN links
  'pdfmake': {
    'website': '',
    'modules': [
      {'reqAlias': 'pdfmake', 'script': 'pdfmake.min.js', 'version': '0.1.57', 'path': 'pdfmake/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
      {'reqAlias': 'vfs_fonts', 'script': 'vfs_fonts.js', 'version': '0.1.57', 'path': 'pdfmake/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Javascript packages for the PDF transformation width CDN links (Tabulator)
  'jspdf': {
    'website': '',
    'modules': [
      {'reqAlias': 'jspdf', 'script': 'jspdf.min.js', 'version': '1.5.3', 'path': 'jspdf/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
      {'reqAlias': 'autotable', 'script': 'jspdf.plugin.autotable.min.js', 'version': '3.1.1', 'path': 'jspdf-autotable/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
    ]},

  # Clipboard features width CDN links
  'clipboard': {
    'website': 'https://clipboardjs.com/',
    'modules': [
      {'reqAlias': 'clipboard', 'script': 'clipboard.min.js', 'version': '2.0.1', 'path': 'clipboard.js/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Javascript dependencies for D3 and NVD2 components width CDN links
  'd3': {
    'website': 'https://d3js.org/',
    'req': [{'alias': 'jquery'}],
    'modules': [
      {'reqAlias': 'd3', 'reqMod': 'ignore', 'script': 'd3.min.js', 'version': '5.9.7', 'path': 'd3/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}
    ]},

  # D3 Tips Package
  'd3-tip': {
    'req': [{'alias': 'd3'}],
    'modules': [
      {'reqAlias': 'd3_tip', 'script': 'd3-tip.min.js', 'version': '0.9.1', 'path': 'd3-tip/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}
    ]
  },

  # D3 Packages
  'd3-packages': {
      'website': 'https://github.com/d3',
      'req': [{'alias': 'd3'}],
      'modules': [
          {'reqAlias': 'd3_time_format', 'script': 'd3-time-format.min.js', 'version': '2.1.1', 'path': 'd3-time-format/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_shape', 'script': 'd3-shape.min.js', 'version': '1.2.0', 'path': 'd3-shape/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_zoom', 'script': 'd3-zoom.min.js', 'version': '1.7.1', 'path': 'd3-zoom/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_dsv', 'script': 'd3-dsv.min.js', 'version': '1.0.8', 'path': 'd3-dsv/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_ease', 'script': 'd3-ease.min.js', 'version': '1.0.3', 'path': 'd3-ease/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_scale', 'script': 'd3-scale.min.js', 'version': '1.0.7', 'path': 'd3-scale/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_brush', 'script': 'd3-brush.min.js', 'version': '1.0.4', 'path': 'd3-brush/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_selection', 'script': 'd3-selection.min.js', 'version': '1.2.0', 'path': 'd3-selection/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_transition', 'script': 'd3-transition.min.js', 'version': '1.1.1', 'path': 'd3-transition/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_array', 'script': 'd3-array.min.js', 'version': '1.2.2', 'path': 'd3-array/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_collection', 'script': 'd3-collection.min.js', 'version': '1.0.5', 'path': 'd3-collection/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_drag', 'script': 'd3-drag.min.js', 'version': '1.2.1', 'path': 'd3-drag/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_interpolate', 'script': 'd3-interpolate.min.js', 'version': '1.3.0', 'path': 'd3-interpolate/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
          {'reqAlias': 'd3_axis', 'script': 'd3-axis.min.js', 'version': '1.0.10', 'path': 'd3-axis/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
        ]},

  # D3 color module
  'd3-color': {
      'website': 'https://github.com/d3/d3-color',
      'req': [{'alias': 'd3'}],
      'modules': [
        {'reqAlias': 'd3_color', 'script': 'd3-color.min.js', 'version': '1.2.1', 'path': 'd3-color/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Javascript dependencies for Plotly width CDN links
  'plotly.js': {
    'website': 'https://plot.ly/javascript/',
    'req': [{'alias': 'd3'}],
    'modules': [
      {'reqAlias': 'Plotly', 'script': 'plotly.min.js', 'version': '1.51.1', 'path': 'plotly.js/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # NVD3 Components width CDN links
  'nvd3': {
    'website': 'http://nvd3.org/',
    'req': [{'alias': 'd3', 'version': '3.5.17'}],
    'modules': [
      {'reqAlias': 'nvd3', 'script': 'nv.d3.min.js', 'version': '1.8.6', 'path': 'nvd3/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # C3 modules width CDN links
  'c3': {
    'website': 'https://c3js.org/',
    'req': [{'alias': 'd3'}],
    'modules': [
      {'reqAlias': 'c3', 'script': 'c3.min.js', 'version': '0.7.15', 'path': 'c3/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  'crossfilter': {
    'website': 'http://square.github.io/crossfilter/',
    'modules': [
      {'reqAlias': 'crossfilter', 'script': 'crossfilter.min.js', 'version': '1.3.12', 'path': 'crossfilter/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}
    ]
  },

  # DC modules width CDN links
  'dc': {
    'website': 'https://dc-js.github.io/dc.js/examples/',
    'req': [
      {'alias': 'd3'},
      {'alias': 'crossfilter'},
    ],
    'modules': [
      {'reqAlias': 'dc', 'script': 'dc.min.js', 'version': '3.2.1', 'path': 'dc/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # billboard modules width CDN links
  'billboard': {
    'website': 'https://naver.github.io/billboard.js/release/latest/doc/',
    'req': [{'alias': 'd3'}],
    'modules': [
      {'reqAlias': 'bb', 'script': 'billboard.min.js', 'version': '1.11.1', 'path': 'billboard.js/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # ChartJs modules width CDN links
  'Chart.js': {
    'website': 'https://www.chartjs.org/',
    'req': [{'alias': 'd3'}],
    'modules': [
      {'script': 'Chart.bundle.min.js', 'version': '2.9.3', 'path': 'Chart.js/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
      {'reqAlias': 'Chart', 'script': 'Chart.min.js', 'version': '2.9.3', 'path': 'Chart.js/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # ChartJs addon to add label width CDN links
  'chartjs-pie-labels': {
      'website': 'https://chartjs-plugin-datalabels.netlify.com/',
      'req': [{'alias': 'Chart.js'}],
      'modules': [
        {'reqAlias': 'ChartDataLabel', 'script': 'chartjs-plugin-datalabels.min.js', 'version': '0.5.0', 'path': 'chartjs-plugin-datalabels@%(version)s/dist/', 'cdnjs': 'https://cdn.jsdelivr.net/npm'}]},

  # Cannot add properly the dependency in this one as my algorithm does not work for shared dependencies ....
  # 'meter': {'req': ['d3'], 'modules': ['d3.meter.js'], 'website': '', 'version': '', "status": 'deprecated'},

  # Popper tooltips used by bootstrap in the dropdown components
  'popper': {
    'req': [
      {'alias': 'jquery'}],
    'website': 'https://popper.js.org/',
    'modules': [
      {'reqAlias': 'popper', 'script': 'popper.min.js', 'version': '1.14.6', 'path': 'popper.js/%(version)s/umd/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Javascript module for the simple select component. issue with Bootstrap 4 width CDN links
  'select': {
    'website': 'http://silviomoreto.github.io/bootstrap-select/',
    'req': [
      {'alias': 'jquery'},
      {'alias': 'bootstrap'}],
    'modules': [
      {'reqAlias': 'selectBs', 'script': 'bootstrap-select.min.js', 'version': '1.13.9', 'path': 'bootstrap-select/%(version)s/js/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
    ]},

  'select-ajax': {
    'website': 'https://github.com/truckingsim/Ajax-Bootstrap-Select',
    'req': [
      {"alias": 'select'}
    ], 'modules': [
          {'reqAlias': 'selectAjax', 'script': 'ajax-bootstrap-select.min.js', 'version': '1.4.5',
           'path': 'ajax-bootstrap-select/%(version)s/js/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}
    ]
  },

  # https://cdnjs.cloudflare.com/ajax/libs/ajax-bootstrap-select/1.4.5/js/ajax-bootstrap-select.min.js
  # javascript package for the Venn chart
  # 'venn': {'req': ['d3'], 'modules': ['venn.js'], 'website': '', 'version': '',},

  # Vis Javascript Packages
  'vis': {
    'website': 'http://visjs.org/',
    'modules': [
      {'reqAlias': 'vis', 'script': 'vis.min.js', 'version': '4.21.0', 'path': 'vis/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # javascript library to style the content of a paragrap according to the type of code displayed
  'prism': {
    'website': 'https://prismjs.com/',
    'modules': [
      {'reqAlias': 'prism', 'script': 'prism.js', 'version': '1.11.0', 'path': 'prism/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Javascript package to display mathematical formulas
  # https://codingislove.com/display-maths-formulas-webpage/
  # https://github.com/mathjax/mathjax
  'mathjs': {
    'website': 'https://www.mathjax.org/',
    'package': {'zip': 'https://github.com/mathjax/MathJax/archive/%(version)s.zip', 'root': 'MathJax-%(version)s', 'folder': 'mathjax'},
    'modules': [
      {'reqAlias': 'mathjax', 'script': 'MathJax.js', 'version': '2.7.5', 'path': 'mathjax/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}],
    # To use the full module online
    #'url': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/',
    'config': "config=TeX-AMS-MML_HTMLorMML"},

  # Socket IO
  'socket.io': {
    'website': 'https://github.com/socketio/socket.io',
    'req': [{'alias': 'jquery'}],
    'modules': [
      {'reqAlias': 'socketio', 'script': 'socket.io.js', 'version': '2.2.0', 'path': 'socket.io/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Code mirror
  'codemirror': {
    'website': 'https://codemirror.net/',
    'modules': [
      {'script': 'codemirror.js', 'version': '5.42.2', 'path': 'codemirror/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
      {'script': 'python.js', 'version': '5.42.2', 'path': 'codemirror/%(version)s/mode/python/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
      {'script': 'r.js', 'version': '5.42.2', 'path': 'codemirror/%(version)s/mode/r/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
      {'script': 'markdown.js', 'version': '5.42.2', 'path': 'codemirror/%(version)s/mode/markdown/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
      {'script': 'placeholder.js', 'version': '5.42.2', 'path': 'codemirror/%(version)s/addon/display/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Leaflet
  'leaflet': {
    'website': 'https://leafletjs.com/',
    'modules': [
      {'script': 'leaflet.js', 'version': '1.6.0', 'path': 'leaflet/%(version)s/',
       'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},
}


CSS_IMPORTS = {
  'jqueryui': {
    'website': 'http://jquery.com/',
    'modules': [
      {'script': 'jquery-ui.min.css', 'version': '1.12.1', 'path': 'jqueryui/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
      {'script': 'jquery-ui.structure.min.css', 'version': '1.12.1', 'path': 'jqueryui/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
      {'script': 'jquery-ui.theme.min.css', 'version': '1.12.1', 'path': 'jqueryui/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # QUnit package width CDN links
  'qunit': {
    'website': 'https://qunitjs.com',
    'modules': [
      {'script': 'qunit.min.css', 'version': '2.9.2', 'path': 'qunit/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Jquery-brackets package width CDN links
  'jquery-brackets': {
    'req': [{'alias': 'jqueryui'}],
    'modules': [
      {'script': 'jquery.bracket.min.css', 'version': '0.11.1', 'path': 'jquery-bracket/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # To display a context menu when right click on an item width CDN links
  # http://swisnl.github.io/jQuery-contextMenu/demo.html#jquery-context-menu-demo-gallery
  'jquery-context-menu': {
    'website': 'https://github.com/swisnl/jQuery-contextMenu/blob/master/dist/jquery.contextMenu.min.css.map',
    'req': [{'alias': 'jqueryui'}],
    'modules': [
      {'script': 'jquery.contextMenu.min.css', 'version': '2.6.4', 'path': 'jquery-contextmenu/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Jquery timepicker width CDN links
  'timepicker': {
    'website': 'https://timepicker.co/',
    'req': [{'alias': 'jqueryui'}],
    'modules': [
      {'script': 'jquery.timepicker.min.css', 'version': '1.3.5', 'path': 'timepicker/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # To customize the scrollbar width CDN links
  'jquery-scrollbar': {
    'website': 'http://manos.malihu.gr/jquery-custom-content-scroller/',
    'req': [{'alias': 'jqueryui'}],
    'modules': [
      {'script': 'jquery.mCustomScrollbar.min.css', 'version': '3.1.5', 'path': 'malihu-custom-scrollbar-plugin/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Tabulator definition
  'tabulator': {
    'website': 'http://tabulator.info',
    'modules': [
      # '4.1.5'
      {'script': 'tabulator.min.css', 'version': '4.4.3', 'path': 'tabulator/%(version)s/css/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}
    ]
  },

  'datatables': {
    'website': 'https://datatables.net/',
    'req': [{'alias': 'bootstrap'}],
    'modules': [
      {'script': 'jquery.dataTables.min.css', 'version': '1.10.19', 'path': '%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'responsive.dataTables.min.css', 'version': '2.1.1', 'path': 'responsive/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'},
      {'script': 'buttons.dataTables.min.css', 'version': '1.5.2', 'path': 'buttons/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # Datatable group row
  'datatables-row-group': {
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'rowGroup.dataTables.min.css', 'version': '1.0.4', 'path': 'rowgroup/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

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

  # Datatable column reordering modules
  'datatables-select': {
    'req': [{'alias': 'datatables'}],
    'modules': [
      {'script': 'select.bootstrap4.min.css', 'version': '1.2.5', 'path': 'select/%(version)s/css/', 'cdnjs': 'https://cdn.datatables.net'}]},

  # # Datatable column resizable
  # 'dataTables-colResizable': {
  #   'req': [{'alias': 'dataTables'}],
  #   'modules': ['dataTables.colResize.css'], 'version': '2.6',
  #                             'cdnjs': ['https://cdn.rawgit.com/smasala/ColResize/v2.6.0/css/'],
  #                             'website': 'https://smasala.github.io/ColResize/', "status": 'deprecated'},

  # Bootstrap style width CDN links
  'bootstrap': {
    'website': 'https://getbootstrap.com/',
    'req': [{'alias': 'font-awesome'}],
    'modules': [
      {'script': 'bootstrap.min.css', 'version': '4.2.1', 'path': 'bootstrap/%(version)s/css/', 'cdnjs': 'https://stackpath.bootstrapcdn.com'}]},

  # Font awesome style width CDN links
  'font-awesome': {
    'website': 'https://fontawesome.com/',
    'package': {'zip': 'https://use.fontawesome.com/releases/v%(version)s/fontawesome-free-%(version)s-web.zip',
                    'root': 'fontawesome-free-%(version)s-web', 'folder': 'releases', 'path': 'v%(version)s'},
    'modules': [
      {'script': 'all.css', 'version': '5.11.2', 'path': 'releases/v%(version)s/css/', 'cdnjs': 'https://use.fontawesome.com'}]},

  # NVD3 Components width CDN links
  'nvd3': {
    'website': 'http://nvd3.org/',
    'modules': [
      {'script': 'nv.d3.min.css', 'version': '1.8.6', 'path': 'nvd3/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # C3 modules width CDN links
  'c3': {
    'website': 'https://c3js.org/',
    'modules': [
      {'script': 'c3.min.css', 'version': '0.7.15', 'path': 'c3/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # DC modules width CDN links
  'dc': {
    'website': 'https://dc-js.github.io/dc.js/examples/',
    'modules': [
      {'script': 'dc.min.css', 'version': '3.2.1', 'path': 'dc/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # billboard modules width CDN links
  'billboard': {
    'modules': [
      {'script': 'billboard.min.css', 'version': '1.11.1', 'path': 'billboard.js/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}],
    'website': 'https://naver.github.io/billboard.js/release/latest/doc/'},

  #'epyk': {'req': ['bootstrap'], 'modules': ['bdi.css'], 'website': 'internal lib', 'version': '0'},

  # Javascript module for the simple select component. issue with Bootstrap 4 width CDN links
  'select': {
    'website': 'https://github.com/silviomoreto/bootstrap-select',
    'req': [
      {'alias': 'jqueryui'},
      {'alias': 'bootstrap'}],
    'modules': [
      {'script': 'bootstrap-select.min.css', 'version': '1.13.6', 'path': 'bootstrap-select/%(version)s/css/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}
    ]},

  'select-ajax': {
    'website': 'https://github.com/truckingsim/Ajax-Bootstrap-Select',
    'req': [
      {"alias": 'select'}
    ], 'modules': [
          {'reqAlias': 'selectAjax', 'script': 'ajax-bootstrap-select.min.css', 'version': '1.4.5',
           'path': 'ajax-bootstrap-select/%(version)s/css/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}
    ]
  },

  # Pivot table style with CDN Links
  'pivot': {
    'website': 'https://github.com/nicolaskruchten/pivottable',
    'modules': [
      {'script': 'pivot.min.css', 'version': '2.23.0', 'path': 'pivottable/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Vis style with CDN Links
  'vis': {
    'website': 'http://visjs.org/',
    'modules': [
      {'script': 'vis.min.css', 'version': '4.21.0', 'path': 'vis/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Prism style with CDN Links
  'prism': {
    'website': 'https://prismjs.com/',
    'modules': [
      {'script': 'prism.css', 'version': '1.11.0', 'path': 'prism/%(version)s/themes/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Code mirror
  'codemirror': {
    'website': 'https://codemirror.net/',
    'modules': [
      {'script': 'codemirror.css', 'version': '5.39.2', 'path': 'codemirror/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

  # Leaflet
  'leaflet': {
    'website': 'https://leafletjs.com/',
    'modules': [
      {'script': 'leaflet.css', 'version': '1.6.0', 'path': 'leaflet/%(version)s/',
       'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'}]},

}


class ImportManager(object):
  """
  The main class in charge of defining the order of the imports in the header.

  There is no check on the presence of the modules on the server. The only purpose of this module is to produce the
  string with the module names and the correct paths to your final HTML report.
  """

  def __init__(self, online=False, report=None):
    """
    Load the hierarchy of modules.
    This module will define the import section in the header of the final HTML page.

    It will create links to the official online websites or link to an internal copy if no internet connection is
    available. To run a report using the online mode to False it is requires to get all the packages locally
    saved with the expected structured (basically the one of the CDNJ repository)

    :param online: Optional. A flag to specify if the report can use an internet connection. Default False
    :param report: Optional. The internal report object with all the required external modules
    """
    self._report, ovr_version = report, {}
    if report is not None and self._report.run.report_name is not None and self._report.run.local_path is not None and os.path.exists(os.path.join(self._report.run.local_path, '__init__.py')):
      # Force the version of some external Javascript or CSS packages
      packages = importlib.import_module("%s.__init__" % self._report.run.report_name)
      ovr_version = getattr(packages, 'MODULES', {})
    if report is not None:
      # Apply the different reports overrides on the packages versions
      ovr_version.update(self._report._props.get('packages', {}))
    self.jsImports, self.cssImports, self.moduleConfigs, self.reqVersion = {}, {}, {}, {}
    for folder, import_cict, import_type in [('js', self.jsImports, JS_IMPORTS), ('css', self.cssImports, CSS_IMPORTS)]:
      for alias, definition in import_type.items():
        main = collections.OrderedDict()
        for i, mod in enumerate(definition['modules']):
          if alias in ovr_version:
            mod['version'] = ovr_version[alias]
          script = "".join([mod['path'] % mod, mod['script']])
          if online:
            main["%s/%s" % (mod['cdnjs'], script)] = mod['version']
          elif 'url' in definition:
            main["%s%s" % (definition['url'], script)] = mod['version']
          else:
            main["%s/%s" % (STATIC_PATH.replace("\\", "/"), script)] = mod['version']
        modules = collections.OrderedDict()
        self.getModules(modules, alias, folder, import_type)
        if 'config' in definition:
          self.moduleConfigs[alias] = definition['config']

        mainKeys, versions = [], []
        for k, v in main.items():
          mainKeys.append(k)
          versions.append(v)
        import_cict[alias] = {'main': main, 'dep': list(modules.keys()), 'versions': versions}

  def getModules(self, modules, alias, folder=None, module_details=None):
    """
    Return the list of modules for a given entry.
    This will be used recursively to resolve all the dependencies

    Example
    modules = collections.OrderedDict()
    ImportManager().getModules(modules, 'c3')

    :param modules: The list of modules
    :param alias: The module reference in the above JS and CSS dictionaries
    :param folder: Optional. The folder name
    :param module_details: Optional. The module definition. Default check in the Javascipt modules

    :return: The list of modules
    """
    if module_details is None:
      module_details = dict(JS_IMPORTS)
    if isinstance(alias, dict):
      alias = alias['alias']
    for mod in module_details[alias]['modules']:
      script = "".join([mod['path'] % mod, mod['script']])
      if 'url' in module_details[alias]:
        modules["%s/%s" % (module_details[alias]['url'], script)] = True
      else:
        modules[r"%s\%s" % (STATIC_PATH.replace("\\", "/"), script)] = True
    for req in module_details[alias].get('req', []):
      self.getModules(modules, req, folder, module_details)
    return modules

  def getReq(self, mod, modules, import_hierarchy):
    """
    Returns the list pf required modules for a given alias

    :param mod:
    :param modules:
    :param import_hierarchy:

    """
    if isinstance(mod, dict):
      # This will allow different versions of packages according to the modules
      # For example NVD3 cannot use any recent version of D3
      if 'version' in mod:
        self.reqVersion[mod['alias']] = mod['version']
        new_main_for_alias = collections.OrderedDict()
        for path in self.jsImports[mod['alias']]['main']:
          for v in self.jsImports[mod['alias']]['versions']:
            new_main_for_alias[path.replace(v, mod['version'])] = mod['version']
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

  def cleanImports(self, imports, import_hierarchy):
    """
    Remove the underlying imports to avoid duplicated entries

    Example
    >>> ImportManager().cleanImports(['c3'], JS_IMPORTS)
    ['jquery', 'd3', 'c3']

    :param imports: An array with the list of aliases for the external packages
    :param import_hierarchy: The package definition (Javascript or CSS) from the above import lists

    :return: Return the list with the full list of aliases (including dependencies)
    """
    import_resolved = []
    for mod in imports:
      self.getReq(mod, import_resolved, import_hierarchy)
    for a in set(import_resolved):
      occurences = [j for j, x in enumerate(import_resolved) if x == a]
      if len(occurences) > 1:
        for j in occurences[::-1][1:]:
          import_resolved.pop(j)
    return import_resolved[::-1]

  def cssResolve(self, css_aliases, local_css=None, excluded=None):
    """
    Return the list of CSS modules to add to the header

    Example
    >>> ImportManager().cssResolve(['c3'])
    '<link rel="stylesheet" href="/static/c3/0.6.12/c3.min.css" type="text/css">'

    :param css_aliases: An array with the list of aliases for the external packages
    :param local_css: Optional. The file overrides
    :param excluded: Optional. Packages excluded from the result object (mandatory for some frameworks already emboarding modules)

    :return: The string to be added to the header
    """
    css = []
    css_aliases = self.cleanImports(css_aliases, CSS_IMPORTS)
    for css_alias in css_aliases:
      if excluded is not None and css_alias in excluded:
        continue

      for urlModule in list(self.cssImports[css_alias]['main']):
        css.append('<link rel="stylesheet" href="%s" type="text/css">' % urlModule)
    if local_css is not None:
      for localCssFile in local_css:
        css.append('<link rel="stylesheet" href="%s/users/%s)" type="text/css">' % (STATIC_PATH.replace("\\", "/"), localCssFile))
    return "\n".join(css)

  def cssURLs(self, css_str):
    """
    Retrieve the list of CSS dependencies URL from a header

    :param css_str: The CSS String in the page

    :return: A Python list with all the CSS external URL to be imported
    """
    return re.findall('<link rel="stylesheet" href="(.*?)" type="text/css">', css_str)

  def jsResolve(self, js_aliases, local_js=None, excluded=None):
    """
    Return the list of Javascript modules to add to the header

    Example
    >>> ImportManager().jsResolve(['c3'])
    '<script language="javascript" type="text/javascript" src="/static/jquery/3.4.1/jquery.min.js"></script>\n<script language="javascript" type="text/javascript" src="/static/d3/5.9.7/d3.min.js"></script>\n<script language="javascript" type="text/javascript" src="/static/c3/0.6.12/c3.min.js"></script>'

    :param js_aliases: An array with the list of aliases for the external packages
    :param local_js: Optional. The file overrides
    :param excluded: Optional. Packages excluded from the result object (mandatory for some frameworks already emboarding modules)

    :return: The string to be added to the header
    """
    js = []
    js_aliases = self.cleanImports(js_aliases, JS_IMPORTS)
    for js_alias in js_aliases:
      if excluded is not None and js_alias in excluded:
        continue

      extra_configs = "?%s" % self.moduleConfigs[js_alias] if js_alias in self.moduleConfigs else ""
      for url_module in list(self.jsImports[js_alias]['main']):
        if '/mode/' in url_module:
          js.append('<script type="module" language="javascript" src="%s%s"></script>' % (url_module, extra_configs))
        else:
          js.append('<script language="javascript" type="text/javascript" src="%s%s"></script>' % (url_module, extra_configs))
    if local_js is not None and len(local_js) > 0:
      extra_configs = "?%s" % self.moduleConfigs[js_alias] if js_alias in self.moduleConfigs else ""
      for local_js_file in local_js:
        js.append('<script language="javascript" type="text/javascript" src="%s/users/%s%s"></script>' % (STATIC_PATH.replace("\\", "/"), local_js_file, extra_configs))
    return "\n".join(js)

  def jsURLs(self, js_str):
    """
    Retrieve the list of Javascript dependencies URL from a header

    :param js_str: The Javascript String in the page

    :return: A Python list with all the Javascript external URL to be imported
    """
    return re.findall('<script language="javascript" type="text/javascript" src="(.*?)"></script>', js_str)

  def getFiles(self, cssAlias, jsAlias):
    """
    retrieve the package definition from the list of module aliases

    Example
    >>> ImportManager().getFiles(['c3'], ['c3'])
    f['css'][0]['file']['script']

    :param cssAlias: An array with the list of aliases for the CSS external packages
    :param jsAlias: An array with the list of aliases for the Js external packages

    :return: A dictionary with the CSS and JS files definition
    """
    files = {'css': [], 'js': []}
    mod_css, mod_js = {}, {}
    for alias, details in CSS_IMPORTS.items():
      mod_css[alias] = []
      for module in details['modules']:
        mod_css[alias].append({'version': module.get('version', ''), 'alias': alias, 'file': module, 'website':
          details.get('website', ''), 'status': details.get('status', '')} )
    for alias, details in JS_IMPORTS.items():
      mod_js[alias] = []
      for module in details['modules']:
        mod_js[alias].append({'version': module.get('version', ''), 'alias': alias, 'file': module, 'website':
          details.get('website', ''), 'status': details.get('status', '')} )
    for css_file in self.cleanImports(cssAlias, CSS_IMPORTS):
      files['css'].extend(mod_css[css_file])
    for js_file in self.cleanImports(jsAlias, JS_IMPORTS):
      files['js'].extend(mod_js[js_file])
    return files

  def cssGetAll(self):
    """ To retrieve the full list of available modules on the server """
    return self.cssResolve(set(CSS_IMPORTS.keys()))

  def jsGetAll(self):
    """ To retrieve the full list of available modules on the server """
    return self.jsResolve(set(JS_IMPORTS.keys()))

  def getPackage(self, alias, version=None, static_path=None, with_dep=False, reload=True):
    """
    Function in charge of downloading the different external CSS and JS packages locally.
    This will guarantee the install without having to get any extra features saved on a repository.
    Saved copies of the modules can be done in order to guarantee a offline mode

    Example
    Imports.ImportManager(report=Report()).getPackage('jqueryui')

    :param alias: The package reference in the above list
    :param version: Optional. The package version to retrieve
    :param static_path: Optional. The path in which the files should be copied to
    :param with_dep: Optional. Flag to specify if the dependencies should be updated. Default False
    :param reload: Optional. Flag to force the package reloading if the folder already exists. Default Yes

    """
    if not hasattr(self._report, "py"):
      from epyk.core.py.PyRest import PyRest
      webscrapper = PyRest().webscrapping
    else:
      webscrapper = self._report.py.requests.webscrapping

    if not static_path.endswith("static"):
      static_path = os.path.join(static_path, "static")
    packages = {}
    _static_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static') if static_path is None else static_path
    if not _static_path.endswith("static"):
      _static_path = os.path.join(_static_path, "static")
    for pckg in [JS_IMPORTS, CSS_IMPORTS]:
      if with_dep:
        for depAlias in self.cleanImports([alias], pckg):
          if depAlias != alias:
            self.getPackage(depAlias, reload=reload)
      if 'package' in pckg.get(alias, {}):
        packages[alias] = os.path.join(_static_path, pckg[alias]['package']['folder'])
      for mod in pckg.get(alias, {}).get('modules', []):
        _version = self.reqVersion.get(alias, mod['version']) if version is None else version
        script = "".join([mod['path'] % {'version': _version}, mod['script']])
        path = os.path.join(_static_path, mod['path'] % {'version': _version})
        if not os.path.exists(path):
          os.makedirs(path)
        reloadModule = True
        extFilePath = r"%s\%s" % (path, mod['script'])
        if os.path.exists(extFilePath) and not reload:
          reloadModule = False

        if reloadModule:
          page = webscrapper("%s/%s" % (mod['cdnjs'], script))
          if hasattr(page, 'code') and page.code == 404:
            print(" # Error - %s: Script %s/%s not found " % (alias, mod['cdnjs'], script))
            continue

          try:
            extFileName = open(extFilePath, "wb")
            extFileName.write(page)
            extFileName.close()
            print("  > %s - %s, version %s. Done !" % (alias, mod['script'], _version))
          except Exception as err:
            print(" # Exception - %s: %s/%s, %s" % (alias, mod['script'], _version, err))
            print(err)
        else:
          print("  > %s - %s, version %s. Already defined !" % (alias, mod['script'], _version))

    if len(packages) > 0:
      print("")
      print("Downloading %s packages, this might take few minutes" % len(packages))
      for pckg, folder in packages.items():
        self.getFullPackage(pckg, version=version, static_path=static_path, reload=reload)

  def getFullPackage(self, alias, version=None, static_path=None, reload=False):
    """
    Download a full package (CSS and JS) locally for a server or full offline mode

    Example
    Imports.ImportManager(report=Report()).getFullPackage('font-awesome')

    :param alias: The package reference in the above list
    :param version: Optional. The package version to retrieve
    :param static_path: Optional. The path in which the files should be copied to
    :param reload: Optional. Flag to force the package reloading if the folder already exists. Default False

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
        print("  > Downloading package %s" % packagePath)
        r = webscrapper(packagePath)
        z = zipfile.ZipFile(io.BytesIO(r))
        #z = zipfile.ZipFile(io.BytesIO(r))
        z.extractall(static_path)
        if JS_IMPORTS[alias]['package']['root'] is not None:
          root = JS_IMPORTS[alias]['package']['root'] % versionDict
          shutil.copytree(os.path.join(static_path, root), dstPath)
          shutil.rmtree(os.path.join(static_path, root))
        print("  < Package %s. Done ! " % alias)
      else:
        print("  < Package %s already loaded " % alias)
    return self

  def package(self, alias):
    """
    Returns the packages used in the Framework for both Js and CSS perimeters

    Example
    >>> len(ImportManager().package('jqueryui')['modules'])
    4

    :param alias: The package reference in the above lists

    :return: A dictionary with the package details
    """
    res = {}
    if alias in CSS_IMPORTS:
      res.update(CSS_IMPORTS[alias])
    if alias in JS_IMPORTS:
      for k, v in JS_IMPORTS[alias].items():
        if k in res:
          if isinstance(v, list):
            res[k].extend(v)
        else:
          res[k] = v
    return res

  def setVersion(self, alias, version):
    """
    Allow the use of different version of a package.

    This will change the Import important to the Python env

    :param alias: The package reference in the above list
    :param version: The new version to be used globally

    """
    self.reqVersion[alias] = version
    for modType in [CSS_IMPORTS, JS_IMPORTS]:
      if alias in modType:
        for mod in modType[alias].get('modules', []):
          mod['version'] = version

  def addPackage(self, alias, config):
    """
    Add a new package or update an existing one with new parameters.
    Only few parameters are available here in order to limit the changes

    Example
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

    :return: The import Manager
    """

    global CSS_IMPORTS
    global JS_IMPORTS

    mod_entry = {'css': {}, 'js': {}}
    for mod in config['modules']:
      if mod['script'].endswith(".css"):
        mod_entry['css'].setdefault('modules', []).append(mod)
        if 'req' in config:
          for req in config['req']:
            if req['alias'] in CSS_IMPORTS:
              mod_entry['css'].setdefault('req', []).append(req)
      elif mod['script'].endswith(".js"):
        mod_entry['js'].setdefault('modules', []).append(mod)
        if 'req' in config:
          for req in config['req']:
            if req['alias'] in JS_IMPORTS:
              mod_entry['js'].setdefault('req', []).append(req)
    if len(mod_entry['css']) > 0:
      CSS_IMPORTS.setdefault(alias, {}).update(mod_entry['css'])
    if len(mod_entry['js']) > 0:
      JS_IMPORTS.setdefault(alias, {}).update(mod_entry['js'])
    return self

  def getPackages(self, static_path=None, reload=False, exclude=None):
    """
    Download all the CSS and Js packages from the official CDNJS configured in the configuration.
    It is possible to get the configuration settings by calling the function getPackageInfo(aliasName) attached to the report

    :param static_path: The package reference in the above list
    :param reload: Optional. Flag to force the package reloading if the folder already exists. Default False

    :return: The Python Import manager
    """
    if exclude is None:
      exclude = []
    if not static_path.endswith("static"):
      static_path = os.path.join(static_path, "static")
    aliases = list(set(list(CSS_IMPORTS.keys()) + list(JS_IMPORTS.keys())))
    for alias in aliases:
      self.getPackage(alias, static_path=static_path, reload=reload)
    return self
