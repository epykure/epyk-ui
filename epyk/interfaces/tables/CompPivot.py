
from epyk.core.html import tables as html_tables


class Pivottable(object):

  def __init__(self, context):
    self.parent = context

  def pivotUI(self, recordSet=None, rows=None, cols=None, width=(100, '%'), height=(None, 'px'), htmlCode=None,
            helper=None, options=None, profile=False):
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
    table = html_tables.HtmlTablePivot.PivotUITable(self.parent.context.rptObj, recordSet, rows, cols, width, height, htmlCode,
                                                  helper, options, profile)
    self.parent.context.register(table)
    return table

  def heatmap(self, recordSet=None, rows=None, cols=None, values=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=False):
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
    table = html_tables.HtmlTablePivot.PivotTable(self.parent.context.rptObj, recordSet, rows, cols, width, height, htmlCode,
                                                  helper, options, profile)
    table.renderers.heatmap()
    if values is not None:
      table.aaggregators.sumOverSum(values)
    self.parent.context.register(table)
    return table
