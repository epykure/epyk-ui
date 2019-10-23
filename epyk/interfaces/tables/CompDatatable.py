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


class Datatables(object):
  def __init__(self, context):
    self.parent = context

  def table(self, records, cols, rows, header=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """

    :param records:
    :param cols:
    :param rows:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:

    :return:
    """
    table = html_tables.HtlmTableDatatable.DataTable(self.parent.context.rptObj, records, cols, rows, header or {},
                                                     width, height, htmlCode, options, profile)
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
