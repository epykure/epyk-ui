
from epyk.core.html import tables as html_tables


class Plotly:

  def __init__(self, ui):
    self.page = ui.page

  def table(self, records, cols=None, rows=None, header=None, width=(100, '%'), height=(None, 'px'), html_code=None,
            options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plot.ly/javascript/table-subplots/

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param cols: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param header:
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%')
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px")
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    data_rows, _header = [], []
    cols = cols or []
    rows = rows or []
    if len(records) > 0 and not cols and not rows:
      cols = list(records[0].keys())
    for r in rows:
      data_rows.append([])
      _header.append(r)
    data_cols = []
    for r in cols:
      data_cols.append([])
      _header.append(r)
    for rec in records:
      for i, r in enumerate(rows):
        data_rows[i].append(rec.get(r, ''))
      for i, r in enumerate(cols):
        data_cols[i].append(rec.get(r, ''))

    header = header or _header
    options = options or {}
    options.update({'type': 'table', 'mode': ''})
    h_table = html_tables.HtmlTablePlotly.Table(self.page, width, height, options, html_code, profile)
    h_table.add_trace(data_rows + data_cols)
    h_table.options.responsive = True
    h_table.data.header.values = [[h] for h in header]
    h_table.layout.no_background()
    return h_table
