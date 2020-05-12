
from epyk.core.html import tables as html_tables


class Datatables(object):
  def __init__(self, context):
    self.parent = context

  def table(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), htmlCode=None,
            options=None, profile=None):
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
    data = []
    cols = cols or []
    rows = rows or []
    if not cols and not rows:
      cols = list(records[0].keys())
    for rec in records:
      data.append([rec.get(c) for c in cols + rows])

    table = html_tables.HtlmTableDatatable.Table(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)
    for c in cols + rows:
      col_def = table.config.columns
      col_def.title = c
      col_def.className.center()
    table.style.themes.compact()
    table.config.scrollX = True
    self.parent.context.register(table)
    return table

  def heatmap(self):
    pass

  def intensity(self):
    pass

  def hierarchy(self):
    pass

  def delta_signed(self):
    pass

  def delta_abs(self):
    pass

  def comments(self):
    pass
