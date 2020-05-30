
from epyk.core.html import tables as html_tables


class Google(object):
  def __init__(self, context):
    self.parent = context

  def table(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

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
    """
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'type': 'Table'}
    if options is not None:
      table_options_dflts.update(options)

    data = self.parent.context.rptObj.data.google.table(records, cols, rows)
    table = html_tables.HtmlTableGoogle.Table(self.parent.context.rptObj, data, width, height, htmlCode, table_options_dflts, profile)
    for c in cols + rows:
      table.add_column(c)
    self.parent.context.register(table)
    return table
