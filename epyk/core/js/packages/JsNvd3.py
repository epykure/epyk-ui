"""

http://nvd3-community.github.io/nvd3/examples/documentation.html
"""


class JsNvd3Axis(object):
  def axisLabel(self, text):
    pass

  def tickFormat(self, jsFnc):
    pass

  def tickValues(self, values):
    pass


class JsNvd3(object):
  def title(self, text):
    pass

  def titleOffset(self, value):
    pass

  def options(self, opts):
    pass

  def width(self, value):
    pass

  def height(self, value):
    pass

  def margin(self, options):
    pass

  def useInteractiveGuideline(self, flag):
    pass

  def transitionDuration(self, time):
    pass

  def showLegend(self, flag):
    pass

  def showYAxis(self, flag):
    pass

  def showXAxis(self, flag):
    pass

  def update(self):
    pass

  def showControls(self, flag):
    pass

  def color(self, d3ColorScale):
    pass

  def noData(self):
    pass


class JsNvd3Area(JsNvd3):
  def x(self, jsFnc):
    pass

  def y(self, jsFnc):
    pass

  def rotateLabels(self, value):
    pass

  def reduceXTicks(self, flag):
    pass

  def rightAlignYAxis(self, flag):
    pass

  def clipEdge(self, flag):
    pass


class JsNvd3Bar(JsNvd3):
  def x(self, jsFnc):
    pass

  def y(self, jsFnc):
    pass

  def rotateLabels(self, value):
    pass

  def reduceXTicks(self, flag):
    pass

  def staggerLabels(self, flag):
    pass

  def tooltips(self, flag):
    pass

  def showValues(self, flag):
    pass

  def groupSpacing(self, value):
    pass


class JsNvd3Pie(JsNvd3):

  def x(self, jsFnc):
    pass

  def y(self, jsFnc):
    pass

  def showLabels(self, flag):
    pass

  def labelThreshold(self, value):
    pass

  def labelType(self, text):
    pass

  def donut(self, flag):
    pass

  def donutRatio(self, value):
    pass

  def rotateLabels(self, value):
    pass

  def reduceXTicks(self, flag):
    pass

  def staggerLabels(self, flag):
    pass

  def tooltips(self, flag):
    pass

  def showValues(self, flag):
    pass

  def groupSpacing(self, value):
    pass
