"""

https://plot.ly/javascript/reference/
https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot
"""

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject
from epyk.core.js.packages import JsPackage


class JsPlotly(JsPackage):
  lib_alias = {'js': 'plotly.js'}

  def newPlot(self, htmlId, data, layout):
    """

    :return:
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    data = JsUtils.jsConvertData(data, None)
    layout = JsUtils.jsConvertData(layout, None)
    return JsObject.JsObject.get("Plotly.newPlot(%s, %s, %s)" % (htmlId, data, layout))

  def react(self):
    pass

  def plot(self):
    pass

  def restyle(self):
    pass

  def relayout(self):
    pass

  def update(self):
    pass

  def validate(self):
    pass

  def makeTemplate(self):
    pass

  def validateTemplate(self):
    pass

  def addTraces(self):
    pass

  def deleteTraces(self):
    pass

  def moveTraces(self):
    pass

  def extendTraces(self):
    pass

  def prependTraces(self):
    pass

  def addFrames(self):
    pass

  def animate(self):
    pass

  def purge(self):
    pass

  def toImage(self):
    pass

  def downloadImage(self):
    pass


class JsPlotlyLegend(object):

  def x(self):
    pass

  def y(self):
    pass

  def bgcolor(self):
    pass

  def bordercolor(self):
    pass

  def traceorder(self):
    pass

  def font(self):
    pass

  def yref(self):
    pass

  def showlegend(self):
    pass


class JsPlotlyAxis(object):

  def title(self):
    pass

  def showline(self):
    pass

  def showticklabels(self):
    pass

  def showgrid(self):
    pass

  def zeroline(self):
    pass

  def range(self):
    pass

  def autorange(self):
    pass


class JsPlotlyMargin(object):

  def autoexpand(self):
    pass

  def l(self):
    pass

  def r(self):
    pass

  def t(self):
    pass


class JsPlotlyAnnotation(object):
  pass


class JsPlotlyLayout(object):

  def __init__(self, attrs):
    self.__attrs = {}

  @property
  def width(self):
    return ""

  @property
  def height(self):
    return

  def legend(self):
    pass

  def title(self):
    pass

  def paper_bgcolor(self):
    pass

  def plot_bgcolor(self):
    pass

  def showlegend(self):
    pass

  def bargap(self):
    pass

  def barmode(self):
    pass

  def xaxis(self):
    pass

  def toStr(self):
    return {}


class PlotlyFont(object):

  def size(self):
    pass


class PlotlyMarkers(object):

  def arearatio(self):
    pass

  def sizemin(self):
    pass

  def sizemax(self):
    pass

  def blend(self):
    pass

  def border(self):
    pass
  
  def color(self):
    pass

  def size(self):
    pass

  def line(self):
    pass

  def sizeref(self):
    pass

  def opacity(self):
    pass

  def sizemode(self):
    pass


class JsPlotlyTrace(object):

  def __init__(self, src, varName):
    self._src, self.varName = src, varName
    self._layout = None

  def mode(self):
    pass

  def type(self):
    pass

  def name(self):
    pass

  def text(self):
    pass

  def line(self):
    pass

  def connectgaps(self):
    pass


class Line(JsPlotlyTrace):

  @property
  def layout(self):
    if self._layout is None:
      self._layout = JsPlotlyLayout({})
    return self._layout


if __name__ == '__main__':
  pass
