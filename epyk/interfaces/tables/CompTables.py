
# Check if pandas is available in the current environment
# if it is the case this module can handle DataFrame directly
try:
  import pandas as pd
  has_pandas = True

except:
  has_pandas = False


from epyk.core.html import tables as html_tables
from epyk.core import js

from epyk.interfaces.tables import CompTabulator
from epyk.interfaces.tables import CompDatatable
from epyk.interfaces.tables import CompTablesPlotly
from epyk.interfaces.tables import CompTableD3
from epyk.interfaces.tables import CompAgGrid
from epyk.interfaces.tables import CompPivot


class Tables(object):
  def __init__(self, context):
    self.context = context

  @property
  def aggrid(self):
    """
    Description:
    -----------
    ag-Grid is the industry standard for JavaScript Enterprise Applications.
    Developers using ag-Grid are building applications that would not be possible if ag-Grid did not exist.

    Related Pages:

      https://www.ag-grid.com/javascript-grid/
    """
    return CompAgGrid.AgGrid(self)

  @property
  def tabulators(self):
    """
    Description:
    -----------
    Interface to the different Tabulator configurations

    Related Pages:
http://tabulator.info/
    """
    return CompTabulator.Tabulators(self)

  @property
  def pivots(self):
    """
    Description:
    -----------
    Interface to the different Pivot Table configurations

    Related Pages:
https://pivottable.js.org/examples/
    """
    return CompPivot.Pivottable(self)

  @property
  def d3(self):
    """
    Description:
    -----------
    Interface to the different Tabulator configurations

    Related Pages:

			https://github.com/d3/d3/wiki/Gallery

    :rtype: CompTableD3.D3
    """
    return CompTableD3.D3(self)

  @property
  def plotlys(self):
    """
    Interface to the different Tabulator configurations

    Related Pages:
http://tabulator.info/

    :rtype: CompTabulator.Tabulators
    """
    return CompTablesPlotly.Plotly(self)

  @property
  def datatables(self):
    """
    Description:
    -----------
    Interface to the different Datatable configurations

    Related Pages:

			https://datatables.net/

    :rtype: CompDatatable.Datatables
    """
    return CompDatatable.Datatables(self)

  def pivot(self, recordSet=None, rows=None, cols=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    -----------
    Create a HTML Pivot table

    Usage::

      Related Pages:

			https://pivottable.js.org/examples/
    https://react-pivottable.js.org/
    https://jsfiddle.net/nicolaskruchten/w86bgq9o/
    """
    table = html_tables.HtmlTablePivot.PivotTable(self.context.rptObj, recordSet, rows, cols, width, height, htmlCode, helper, options, profile)
    self.context.register(table)
    return table

  def datatable(self, recordSet=None, header=None, dataFncs=None, aggFnc='sum', cols=None, rows=None, title='',
            width=(100, '%'), height=(None, 'px'), options=None, htmlCode=None,
            profile=None):
    """
    Description:
    -----------
    The python interface to the javascript Datatable framework. Not all the functions have been wrapped here but you should be able to
    do the most frequent events and interactions with this component from the available function.
    Please keep in mind that the javascript is only trigger on the web browser (namely not with the Python code)

    Usage::

      Related Pages:

			https://datatables.net/reference/index
    https://datatables.net/reference/option/
    https://datatables.net/reference/option/ajax.data
    https://datatables.net/reference/option/drawCallback
    https://datatables.net/extensions/buttons/examples/initialisation/custom.html

    :rtype: html_tables.HtlmTableDatatable.DataTable
    """
    rows = rows or []
    cols = cols or []
    # if recordSet is not None and cols is None and rows is None:
    #   if isinstance(recordSet, list):
    #     recordSet = self.context.rptObj.df(recordSet)
    #   if header is not None:
    #     rows, cols = [], []
    #     for i, colType in enumerate(recordSet.dtypes):
    #       colName = recordSet.dtypes.index[i]
    #       if not colName in header and (isinstance(header, dict) and not colName in header.get('_order', [])):
    #         continue
    #
    #       if colType in ['float64', 'bool', 'int64']:
    #         cols.append(colName)
    #       else:
    #         rows.append(colName)
    #   else:
    #     rows, cols = ['_index'], []
    #     header = {'_index': {'visible': False}}
    #     for i, colType in enumerate(recordSet.dtypes):
    #       colName = recordSet.dtypes.index[i]
    #       if colType in ['float64', 'bool', 'int64']:
    #         cols.append(colName)
    #       else:
    #         rows.append(colName)
    #
    # if '_index' in rows:
    #   recordSet['_index'] = recordSet.index
    _tableOptions = {'autoWidth': True} # 'scrollX': True
    if options is None:
      options = {}
    _tableOptions.update(options)
    jsFncs, systemCols = [], {}
    if _tableOptions.get('system', {}).get('age'):
      systemCols['age'] = []
      for colName in cols:
        systemCols['age'].append("%s.age" % colName)

    if _tableOptions.get('system', {}).get('quality'):
      systemCols['quality'] = []
      for colName in cols:
        systemCols['quality'].append("%s.quality" % colName)

    if _tableOptions.get('system', {}).get('intensity'):
      systemCols['intensity'] = []
      for colName in cols:
        systemCols['intensity'].append("%s.intensity" % colName)

    #if tableTypes == 'hierarchy':
    #  rows = ['_id', '_level'] + rows

    if isinstance(aggFnc, str):
      if cols is None:
        cols = []
      jsFncs.append((aggFnc, rows, cols + systemCols.get('age', []) + systemCols.get('intensity', []) + systemCols.get('quality', [])))
    else:
      jsFncs.append(aggFnc)
    # if isinstance(recordSet, list):
    #   recordSet = self.context.rptObj.df(recordSet)
    if dataFncs is not None:
      jsFncs += dataFncs
    if header is None:
      header = {'_order': rows + cols}

    elif isinstance(header, list):
      tmpHeader = {'_order': []}
      for h in header:
        if isinstance(h, dict):
          tmpHeader[h['data']] = h.get('title', h['data'])
          tmpHeader['_order'].append(h['data'])
        else:
          tmpHeader[h] = h
          tmpHeader['_order'].append(h)
      header = tmpHeader
    if profile:
      self.context.rptObj.jsOnLoadFnc.add(self.context.rptObj.jsConsole("", isPyData=True))
      self.context.rptObj.jsOnLoadFnc.add(self.context.rptObj.jsConsole("************************", isPyData=True))
      self.context.rptObj.jsOnLoadFnc.add(self.context.rptObj.jsConsole("Profiling mode for table", isPyData=True))
    return self.context.register(html_tables.HtlmTableDatatable.DataTable(self.context.rptObj, js.AresJs.Js(self.context.rptObj, recordSet, profile=profile).fncs(jsFncs, systemCols), header,
                                                                               title, width, height, _tableOptions, htmlCode, profile))

  def tabulator(self, recordSet=None, header=None, cols=None, rows=None, title=None, align="left", width=(100, '%'),
                height=(None, 'px'), options=None, htmlCode=None, profile=None):
    """
    Description:
    -----------

    Usage::

      Related Pages:
http://tabulator.info/

    Attributes:
    ----------
    :param recordSet:
    :param header:
    :param cols:
    :param rows:
    :param title:
    :param align:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    :param profile:

    :rtype: html.HtmlDataTable.DataTabulator

    :return:
    """
    table_options_dflts = {'selectable': False, 'index': '_row', 'layout': 'fitColumns', 'pagination': 'local',
                           'paginationSize': 25, 'resizableRows': False, 'movableColumns': True}
    if height[0] is not None and height[1] == 'px':
      table_options_dflts['height'] = height[0]
      height = (height[0] + 26, height[1])
    tmp_header = {}
    if header is not None:
      # Apply a formatting to the specific columns
      if '_formats' in header:
        for col in header['_formats']:
          if not 'cols' in col:
            raise Exception("List of columns should be defined in the key cols")

          cols_format = list(col['cols'])
          del col['cols']

          for cf in cols_format:
            if cf not in header:
              header[cf] = {'field': cf, 'title': cf, 'align': 'center'}
              header[cf].update(col)
        del header['_formats']

      for k, v in header.items():
        r = {'field': k, 'title': k, 'align': 'center'}
        r.update(v)
        tmp_header[k] = r
    elif recordSet is not None and len(recordSet) > 0:
      cols = recordSet[0].keys()

    order_cols = []
    if cols is not None:
      for col in cols:
        if col not in tmp_header:
          tmp_header[col] = {'title': col, 'field': col, 'align': 'center'}
        order_cols.append(col)
    if rows is not None:
      for row in rows:
        if row not in tmp_header:
          tmp_header[row] = {'title': row, 'field': row, 'formatter': 'number', 'align': 'center'}
          if options is not None and 'digits' in options:
            tmp_header[row]['pyOptions'] = {"digits": options['digits']}
        order_cols.append(row)
    if len(order_cols) == 0:
      order_cols = tmp_header.keys()
    if options is not None:
      table_options_dflts.update(options)
    if not table_options_dflts.get('paginationSize'):
      del table_options_dflts['pagination']
      del table_options_dflts['paginationSize']

    elif 'pageLength' in table_options_dflts:
      table_options_dflts['pagination'] = 'local'
      table_options_dflts['paginationSize'] = table_options_dflts['pageLength']
      del table_options_dflts['pageLength'] # datatable parameter
    if 'cellsType' in table_options_dflts:
      for c in tmp_header:
        # Do not override existing configuration
        for k, v in table_options_dflts['cellsType'].items():
          if k not in tmp_header[c]:
            tmp_header[c][k] = v
      del table_options_dflts['cellsType']

    if 'header' in table_options_dflts:
      for k, v in table_options_dflts["header"].items():
        for h, d in tmp_header.items():
          d[k] = v
    return self.context.register(html_tables.HtmlTableTabulator.DataTabulator(self.context.rptObj, js.AresJs.Js(self.context.rptObj, recordSet, profile=profile),
              [tmp_header[c] for c in order_cols if c in tmp_header], align, title, width, height,
               table_options_dflts, htmlCode, profile))

  def config(self, htmlCode, visible=False, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param htmlCode:
    :param visible:
    :param profile:
    """
    return self.context.register(
      html_tables.HtmlTableConfig.ConfigTable(self.context.rptObj, htmlCode, visible, profile))

  def basic(self, records, cols, rows, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    -----------

    Usage::

      simple_table = rptObj.ui.tables.basic(df.to_dict("records"), cols=["COL1"], rows=["COL2"])
    simple_table.add({"COL1": "Value"})

    Attributes:
    ----------
    :param records:
    :param cols:
    :param rows:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:

    :return:
    """
    table = html_tables.HtmlTable.Bespoke(self.context.rptObj, records, cols, rows, width, height, htmlCode, options, profile)
    self.context.register(table)
    return table

  def grid(self, records, cols, rows, width=(None, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """

    Usage::

      """
    width_cells, width_rows_header = 50, 100
    for rec in records:
      for c in cols:
        if c not in rec:
          rec[c] = 0
    table = html_tables.HtmlTable.Bespoke(self.context.rptObj, records, cols, rows, width, height, htmlCode, options, profile)
    table.css({"width": "%spx" % (width_rows_header + len(cols) * width_cells)})
    # table[0][0]._vals = ""
    for i in table[1:]:
      for j in range(len(rows)):
        i[j].attr["name"] = "row_header"
        i[j].css({"width": "%spx" % width_rows_header})
      for cell in i[j:]:
        cell.attr["contenteditable"] = 'true'
        cell.css({"width": '%spx' % width_cells})
    table.style.clear()
    # Set the style for the table grid
    # table.style.add_classes.table.grid_row_header()
    table.style.add_classes.table.grid_vals()
    # table.style.add_classes.table.grid_no_header()
    self.context.register(table)
    return table
