
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
    if not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'selectable': False, 'index': '_row', 'layout': 'fitColumns', 'pagination': 'local',
                           'paginationSize': 25, 'resizableRows': False, 'movableColumns': True}
    if options is not None:
      table_options_dflts.update(options)

    table = html_tables.HtmlTableTabulator.Table(self.parent.context.rptObj, records, width, height, htmlCode, options, profile)
    for c in cols + rows:
      table.add_column(c)
      #col_def.cssClass.center() # = "dt-center, dt-test"
    self.parent.context.register(table)
    return table

  def heatmap(self):
    pass

  def intensity(self):
    pass

  def hierarchy(self):
    pass
