
from epyk.core.html import tables as html_tables


class Plotly(object):
  def __init__(self, context):
    self.parent = context

  def table(self, records, cols, rows, header=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None,
            profile=None):
    """

    https://plot.ly/javascript/table-subplots/

    :param records:
    :param cols:
    :param rows:
    :param header:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile: 
    """
    h_table = html_tables.HtmlTablePlotly.Table(self.parent.context.rptObj, width, height, "", options or {}, htmlCode,
                                                None, profile)
    self.parent.context.register(h_table)
    h_table.add_trace([
      ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
      [1200000, 20000, 80000, 2000, 12120000],
      [1300000, 20000, 70000, 2000, 130902000],
      [1300000, 20000, 120000, 2000, 131222000],
      [1400000, 20000, 90000, 2000, 14102000]])
    h_table.options.responsive = True
    h_table.data.header.values = [["<b>EXPENSES</b>"], ["<b>Q1</b>"],
				 ["<b>Q2</b>"], ["<b>Q3</b>"], ["<b>Q4</b>"]]
    return h_table
