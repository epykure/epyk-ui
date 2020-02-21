
from epyk.core.html import graph


class Canvas(object):

  def __init__(self, context):
    self.parent = context

  def new(self, height=(100, "%"), width=(30, "px")):
    if not isinstance(width, tuple):
      width = (width, "px")
    html_svg = graph.GraphCanvas.Canvas(self.parent.context.rptObj, height, width)
    self.parent.context.register(html_svg)
    return html_svg
