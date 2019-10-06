"""

https://nvd3-community.github.io/nvd3/examples/documentation.html
"""

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsString


class JsNvd3Axis(object):

  def __init__(self, id):
    self._selector = id
    self._js = []

  def axisLabel(self, text):
    """
    Chart axis settings

    Example
    chart.xAxis.axisLabel('Time (ms)')

    :param text:

    :return:
    """
    text = JsUtils.jsConvertData(text, None)
    self._js.append("axisLabel(%s)" % text)
    return self

  def tickFormat(self, jsFnc):
    """
    Chart axis settings

    Example
    chart.xAxis.tickFormat(d3.format(',r'))

    :param jsFnc:

    :return:
    """
    jsFnc = JsUtils.jsConvertData(jsFnc, None)
    self._js.append("tickFormat(%s)" % jsFnc)
    return self

  def tickValues(self, values):
    """
    Chart axis settings

    Example
    chart.xAxis.tickValues(10)

    :param values:

    :return:
    """
    values = JsUtils.jsConvertData(values, None)
    self._js.append("tickValues(%s)" % values)
    return self

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._selector

    strData = "%(jqId)s.%(items)s" % {'jqId': self._selector, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return strData


class JsNvd3Utils(object):
  """

  """

  def windowResize(self, jsFnc):
    """
    Update the chart when window resizes.

    :param jsFnc:

    :return:
    """
    return "nv.utils.windowResize(%s)" % jsFnc


class JsNvd3(object):
  chartFnc = "lineChart"

  class __internal(object):
    # By default it will attach eveything to the body
    jqId, jsImports, cssImport = 'd3.select("body")', set([]), set([])

  def __init__(self, src=None, varName=None, setVar=True):
    self.src = src if src is not None else self.__internal()
    self._selector = "nv.models.%s()" % self.chartFnc
    self.varName, self.setVar = varName, setVar
    self.src.jsImports.add('nvd3')
    self.src.cssImport.add('nvd3')
    self._js, self._xaxis, self._yaxis = [], None, None

  @property
  def var(self):
    return JsString.JsString(self.varName, isPyData=False)

  def set_var(self, flag):
    self.setVar = flag
    return self

  @property
  def varId(self):
    """
    The Javascript and Python reference ID

    :return: The Javascript String of the object variable name
    """
    return self._selector if self.varName is None else self.varName

  def options(self, opts):
    pass

  def width(self, value):
    """
    The width the graph or component created inside the SVG should be made.
    The width of the container element (normally the svg itself)

    Documentation
    https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param value: A python integer

    :return:
    """
    self._js.append("width(%s)" % value)
    return self

  def height(self, value):
    """
    The height the graph or component created inside the SVG should be made.
    The height of the container element (normally the svg itself)

    Documentation
    https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param value:

    :return:
    """
    self._js.append("height(%s)" % value)
    return self

  def margin(self, options):
    """
    Object containing the margins for the chart or component.
    You can specify only certain margins in the object to change just those parts.
    Default options: { "top": 15, "right": 10, "bottom": 50, "left": 60 }

    Documentation
    https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param options: A python dictionary with the options
    """
    options = JsUtils.jsConvertData(options, None)
    self._js.append("margin(%s)" % options)
    return self

  def useInteractiveGuideline(self, flag):
    pass

  def transitionDuration(self, time):
    pass

  def showLegend(self, flag):
    pass

  @property
  def xAxis(self):
    """

    :return:
    """
    if self._xaxis is None:
      self._xaxis = JsNvd3Axis("%s.xAxis" % self.varName)
    return self._xaxis

  @property
  def yAxis(self):
    """

    :return:
    """
    if self._yaxis is None:
      self._yaxis = JsNvd3Axis("%s.yAxis" % self.varName)
    return self._yaxis

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

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    strData = ".".join(self._js)
    if self.setVar:
      strData = "var %s = %s.%s" % (self.varName, self._selector, strData)
      self.setVar = False
    else:
      strData = "%s.%s" % (self.varName, strData)
    self._js = [] # empty the stack
    return strData


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
  chartFnc = "discreteBarChart"

  def x(self, column=None, jsFnc=None):
    if column is not None:
      self._js.append("x(function(d){return d.%s})" % column)
    elif jsFnc is not None:
      jsFnc = JsUtils.jsConvertFncs(jsFnc)
      self._js.append("x(%s)" % jsFnc)
    return self

  def y(self, column=None, jsFnc=None):
    if column is not None:
      self._js.append("y(function(d){return d.%s})" % column)
    elif jsFnc is not None:
      jsFnc = JsUtils.jsConvertFncs(jsFnc)
      self._js.append("y(%s)" % jsFnc)
    return self

  def rotateLabels(self, value):
    """
    Rotates the X axis labels by the specified degree.

    Documentation
    https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param value:
    :return:
    """
    self._js.append("rotateLabels(%s)" % value)
    return self

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
  chartFnc = "pieChart"

  def x(self, column=None, jsFnc=None):
    if column is not None:
      self._js.append("x(function(d){return d.%s})" % column)
    elif jsFnc is not None:
      jsFnc = JsUtils.jsConvertFncs(jsFnc)
      self._js.append("x(%s)" % jsFnc)
    return self

  def y(self, column=None, jsFnc=None):
    if column is not None:
      self._js.append("y(function(d){return d.%s})" % column)
    elif jsFnc is not None:
      jsFnc = JsUtils.jsConvertFncs(jsFnc)
      self._js.append("y(%s)" % jsFnc)
    return self

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

  def title(self, text):
    """
    Text to include within the middle of a donut chart

    Documentation
    https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param text:

    :return:
    """
    title = JsUtils.jsConvertData(text, None)
    self._js.append("title(%s)" % title)
    return self

  def titleOffset(self, value):
    pass
