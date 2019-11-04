"""
HTML module dedicated to provide Datatable configurations

https://datatables.net/
"""

from epyk.core.html import Html
from epyk.core.js.packages import JsDatatable

# The list of CSS classes
from epyk.core.css.groups import CssGrpClsTable


# The object with all the different configurations available for the table interface
# This factory will pick up automatically when the server is restarted all the new configurations
FACTORY = None


# External Datatable extensions added on demand to add some extra features
# Details of the different extensions are available on the different websites
# https://datatables.net/extensions/
extensions = {
  'rowsGroup': {'jsImports': ['datatables-rows-group']},
  'rowGroup': {'jsImports': ['datatables-row-group'], 'cssImport': ['datatables-row-group']},
  'fixedHeader': {'jsImports': ['datatables-fixed-header'], 'cssImport': ['datatables-fixed-header']},
  'colReorder': {'jsImports': ['datatables-col-order'], 'cssImport': ['datatables-col-order'] },
  'colResize': {'jsImports': ['datatables-col-resizable'], 'cssImport': ['datatables-col-resizable']},
  'fixedColumns': {'jsImports': ['datatables-fixed-columns'], 'cssImport': ['datatables-fixed-columns']}
}


class DataTable(Html.Html):
  name, category, callFnc = 'Table', 'Tables', 'table'
  __reqCss, __reqJs = ['datatables', 'datatables-export'], ['datatables', 'datatables-export']
  _grpCls = CssGrpClsTable.CssClassDataTable

  def __init__(self, report, records, cols, rows, header, width, height, htmlCode, options, profile):
    data, columns = [], []
    self.header = rows + cols
    for h in self.header:
      _head = {"title": h}
      _head.update(header.get(h, {}))
      columns.append(_head)
    for rec in records:
      data.append([rec[c] for c in self.header])
    super(DataTable, self).__init__(report, {"data": data, "columns": columns}, code=htmlCode, width=width[0],
                                    widthUnit=width[1], height=height[0], heightUnit=height[1], profile=profile)

  @property
  def tableId(self):
    """
    Return the Javascript variable of the datatable
    """
    return "window['%s_table']" % self.htmlId

  @property
  def js(self):
    """
    :rtype: JsDatatable.DatatableAPI
    """
    if self._js is None:
      self._js = JsDatatable.DatatableAPI(self._report, selector=self.tableId, setVar=False, parent=self)
    return self._js

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__,
                      "window[htmlObj.attr('id') +'_table'] = htmlObj.DataTable(data)")

  def add_options(self, key, val=None):
    """
    Set the Datatable options

    Example
    table.add_options({"searching": False, 'paginate': False, 'dom': 'Bfrtip', 'buttons': ['copy', 'csv', 'excel', 'pdf', 'print']})

    Documentation
    https://datatables.net/extensions/buttons/examples/initialisation/simple.html

    :param key: The key to add the table dictionary or a dictionary of options
    :param val: The value corresponding to the key
    :return:
    """
    if isinstance(key, dict):
      for k, v in key.items():
        self.vals[k] = v
    else:
      self.vals[key] = val
    return self

  def order(self, vals):
    """
    Set the default order for the Datatable
    This is a shortcut to the add_option('order') definition.

    Example
    table.order([[ 0, "desc" ]])

    Documentation
    https://datatables.net/examples/basic_init/table_sorting.html

    :param vals:
    :return:
    """
    self.vals['order'] = vals
    return self

  def columns(self, columnDefs):
    """
    Shortcut to change the datatable columns

    Example
    table.columns([{"targets": [0], 'visible': False}])
    table.columns([{"targets": [0], 'searchable': False}])

    Documentation
    https://datatables.net/examples/basic_init/hidden_columns.html

    :param columnDefs:

    :return:
    """
    for c in columnDefs:
      if c.get("searchable", False):
        self.vals["searching"] = True
    self.vals["columnDefs"] = columnDefs
    return self

  def __str__(self):
    return "<table %s></table>" % (self.get_attrs(pyClassNames=self.defined))

