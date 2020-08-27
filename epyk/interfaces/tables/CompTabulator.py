
from epyk.core.html import tables as html_tables


class Tabulators(object):
  def __init__(self, context):
    self.parent = context

  def table(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
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
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'selectable': False, 'index': '_row', 'layout': 'fitColumns', 'pagination': 'local',
                           'paginationSize': 25, 'resizableRows': False, 'movableColumns': True}
    if options is not None:
      table_options_dflts.update(options)

    table = html_tables.HtmlTableTabulator.Table(self.parent.context.rptObj, records, width, height, htmlCode, table_options_dflts, profile)
    for c in cols + rows:
      table.add_column(c)
    return table

  def heatmap(self):
    pass

  def intensity(self):
    pass

  def hierarchy(self):
    pass
