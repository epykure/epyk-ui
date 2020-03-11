
from epyk.core.html import tables as html_tables


class Plotly(object):
  def __init__(self, context):
    self.parent = context

  def table(self, records, cols, rows, header=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None,
            profile=None):
    pass
