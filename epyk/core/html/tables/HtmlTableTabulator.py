"""
Wrapper to the Tabulator library

http://tabulator.info/
"""

from epyk.core.html import Html

from epyk.core.js.packages import JsTabulator


class DataTabulator(Html.Html):
  name, category, callFnc = 'Tabulator', 'Table', 'tabulator'
  __reqCss, __reqJs = ['tabulator'], ['tabulator']
  __pyStyle = ['CssTabulator', 'CssTabulatorHeaders', 'CssTabulatorCol', 'CssTabulatorEvenRow', 'CssTabulatorRow',
               'CssTabulatorOddRow', 'CssTabulatorGroups', 'CssTabulatorFooter', 'CssTabulatorFooterPagination',
               'CssTabulatorHeader', 'CssTabulatorColContent', 'CssTabulatorSelected', 'CssTabulatorTreeControl',
               'CssTabulatorTreeControlExpand', 'CssTabulatorCell']

  def __init__(self, report, recordSet, cols, rows, header, width, height, htmlCode, options, profile):
    self.header, columns = rows + cols, []
    for h in self.header:
      _head = {"title": h, "field": h}
      _head.update(header.get(h, {}))
      columns.append(_head)
    self._ctx = {"data": recordSet, "columns": columns}
    self._ctx.update(options)
    super(DataTabulator, self).__init__(report, self._ctx, code=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                  heightUnit=height[1], profile=profile)

  @property
  def js(self):
    """

    :return: A Javascript object
    :rtype: JsTabulator.Tabulator
    """
    if self._js is None:
      self._js = JsTabulator.Tabulator(self._report)
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

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, " new Tabulator('#%s', data)" % (self.htmlId))

  def __str__(self):
    return "<div %s></div>" % (self.strAttr(pyClassNames=self.pyStyle))
