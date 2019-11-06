"""
Wrapper to the Tabulator library

http://tabulator.info/
"""

from epyk.core.html import Html

from epyk.core.js.packages import JsTabulator

# The list of CSS classes
from epyk.core.css.groups import CssGrpClsTable


class DataTabulator(Html.Html):
  name, category, callFnc = 'Tabulator', 'Table', 'tabulator'
  __reqCss, __reqJs = ['tabulator'], ['tabulator']
  _grpCls = CssGrpClsTable.CssClassTabulator

  def __init__(self, report, records, cols, rows, header, width, height, htmlCode, options, profile):
    self.header, columns = rows + cols, []
    for h in self.header:
      _head = {"title": h, "field": h}
      _head.update(header.get(h, {}))
      columns.append(_head)
    self._ctx = {"data": records, "columns": columns}
    self._ctx.update(options)
    super(DataTabulator, self).__init__(report, self._ctx, code=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                  heightUnit=height[1], profile=profile)

  @property
  def tableId(self):
    """
    Return the Javascript variable of the tabulator object
    """
    return "window['%s_table']" % self.htmlId

  @property
  def js(self):
    """
    Return the Javascript internal object

    :return: A Javascript object

    :rtype: JsTabulator.Tabulator
    """
    if self._js is None:
      self._js = JsTabulator.Tabulator(self._report, selector=self.tableId, setVar=False, parent=self)
    return self._js

  def add_options(self, key, val=None):
    """
    Set the Tabulator options

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

  @property
  def _js__builder__(self):
    return "window[htmlObj.getAttribute('id') +'_table'] = new Tabulator('#'+ htmlObj.getAttribute('id'), data)"

  def __str__(self):
    return "<div %s></div>" % (self.get_attrs(pyClassNames=self.defined))
