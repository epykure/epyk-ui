
from epyk.core.html import tables as html_tables


class AgGrid(object):

  def __init__(self, context):
    self.parent = context

  def table(self, records=None, cols=None, rows=None, width=(100, '%'), height=(300, 'px'), htmlCode=None, options=None, profile=None):
    """

    :param records:
    :param cols:
    :param rows:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    cols = cols or []
    rows = rows or []
    if not cols and not rows:
      if records is not None:
        cols = list(records[0].keys())

    table_options_dflts = {'headerHeight': 30, 'rowHeight': '50'}
    if options is not None:
      table_options_dflts.update(options)

    table = html_tables.HtmlTableAgGrid.Table(self.parent.context.rptObj, records, width, height, htmlCode, table_options_dflts, profile)
    for c in cols + rows:
      table.add_column(c)
    return table
