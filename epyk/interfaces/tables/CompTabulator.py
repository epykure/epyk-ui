"""

"""

# Check if pandas is available in the current environment
# if it is the case this module can handle DataFrame directly
try:
  import pandas as pd
  has_pandas = True

except:
  has_pandas = False


from epyk.core.html import tables as html_tables


class Tabulators(object):
  def __init__(self, context):
    self.parent = context

  def table(self, records, cols, rows, header=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """

    :param records:
    :param cols:
    :param rows:
    :param header:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:

    :rtype: html_tables.HtmlTableTabulator.DataTabulator
    :return:
    """
    table_options_dflts = {'selectable': False, 'index': '_row', 'layout': 'fitColumns', 'pagination': 'local',
                           'paginationSize': 25, 'resizableRows': False, 'movableColumns': True}
    if options is not None:
      table_options_dflts.update(options)
    return self.parent.context.register(
      html_tables.HtmlTableTabulator.DataTabulator(self.parent.context.rptObj, records, cols, rows, header or {}, width, height,
                                                      htmlCode, table_options_dflts, profile))

  def heatmap(self):
    pass

  def intensity(self):
    pass

  def hierarchy(self):
    pass
