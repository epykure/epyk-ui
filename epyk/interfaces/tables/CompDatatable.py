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

  def table(self, recordSet, cols, rows, header=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """

    :param recordSet:
    :param cols:
    :param rows:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:

    :rtype: html_tables.HtlmTableDatatable.DataTableNew

    :return:
    """
    if header is None:
      header = {}
    return self.parent.context.register(
      html_tables.HtlmTableDatatable.DataTable(self.parent.context.rptObj, recordSet, cols, rows, header, width, height,
                                                  htmlCode, options, profile))

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