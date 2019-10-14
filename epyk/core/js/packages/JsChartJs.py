"""
ChartJs API

https://www.chartjs.org/docs/latest/developers/api.html
https://www.chartjs.org/docs/latest/developers/updates.html

"""

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import DataAttrs


EASING_OPTIONS = ['linear', 'easeInQuad', 'easeOutQuad', 'easeInOutQuad', 'easeInCubic', 'easeOutCubic',
                  'easeInOutCubic', 'easeInQuart', 'easeOutQuart', 'easeInOutQuart', 'easeInQuint', 'easeOutQuint',
                  'easeInOutQuint', 'easeInSine', 'easeOutSine', 'easeInOutSine', 'easeInExpo', 'easeOutExpo',
                  'easeInOutExpo', 'easeInCirc', 'easeOutCirc', 'easeInOutCirc', 'easeInElastic', 'easeOutElastic',
                  'easeInOutElastic', 'easeInBack', 'easeOutBack', 'easeInOutBack', 'easeInBounce', 'easeOutBounce',
                  'easeInOutBounce']


class CHartJsConfig(object):
  """
  ChartJs Configuration object

  Documentation
  https://www.chartjs.org/docs/latest/developers/api.html
  """

  __duration, __lazy, __easing = None, None, None

  @property
  def duration(self):
    return self.__duration

  @duration.setter
  def duration(self, time):
    self.__duration = time

  @property
  def lazy(self):
    return self.__lazy

  @lazy.setter
  def lazy(self, flag):
    self.__lazy = flag

  @property
  def easing(self):
    return self.__easing

  @easing.setter
  def easing(self, value):
    """
    Set the easing option

    Documentation
    https://www.chartjs.org/docs/latest/configuration/animations.html

    :param value: A String from the available easing values

    :return:
    """
    if value not in EASING_OPTIONS:
      raise Exception("%s is not allowed" % value)

    self.__easing = value


class ChartJs(object):
  lib_alias = 'Chart.js'

  class __internal(object):
    jqId, htmlId, jsImports, cssImport = 'chart', '', set([]), set([])

  def __init__(self, htmlId, config, src=None, varName=None, setVar=True):
    self.src = src if src is not None else self.__internal()
    self._selector = 'new Chart(document.getElementById("%s").getContext("2d"), %s)' % (htmlId, config.toStr())
    self.varName, self.setVar = varName or self._selector, setVar
    self.src.jsImports.add(self.lib_alias)
    self._js = []

  def update(self, config=None):
    """
    Triggers an update of the chart. This can be safely called after updating the data object.

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :param config: A Python dictionary. A config object can be provided with additional configuration for the update proces

    :return:
    """
    if config is None:
      return JsObjects.JsObject.JsObject("%s.update()" % self.toStr())

    config = JsUtils.jsConvertData(config, None)
    return JsObjects.JsObject.JsObject("%s.update(%s)" % (self.toStr(), config))

  def reset(self):
    """
    Reset the chart to it's state before the initial animation.
    A new animation can then be triggered using update.

    Example
    myLineChart.reset()

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.reset()" % self.toStr())

  def stop(self):
    """
    Use this to stop any current animation loop. This will pause the chart during any current animation frame.

    Example
    chart.stop()

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :return: 'this' for chainability
    """
    self._js.append("stop()")
    return self

  def resize(self):
    """
    Use this to manually resize the canvas element.

    This is run each time the canvas container is resized, but you can call this method manually if you change the size of the canvas nodes container element.

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :return: 'this' for chainability
    """
    self._js.append("%s.resize()" % self.toStr())
    return self

  def clear(self):
    """
    Will clear the chart canvas. Used extensively internally between animation frames, but you might find it useful.

    Example
    chart.clear()

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :return: 'this' for chainability
    """
    self._js.append("%s.clear()" % self.toStr())
    return self

  def toBase64Image(self):
    """
    This returns a base 64 encoded string of the chart in it's current state.

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :return: png data url of the image on the canvas
    """
    return JsObjects.JsObject.JsObject("%s.toBase64Image()" % self.toStr())

  def generateLegend(self):
    """
    Returns an HTML string of a legend for that chart. The legend is generated from the legendCallback in the options.

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :return: HTML string of a legend for this chart
    """
    return JsObjects.JsObject.JsObject("%s.generateLegend()" % self.toStr())

  def getElementAtEvent(self, jsEvent):
    """
    Calling getElementAtEvent(event) on your Chart instance passing an argument of an event, or jQuery event, will return the single element at the event position

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :param jsEvent:

    :return: the first element at the event point.
    """
    jsEvent = JsUtils.jsConvertData(jsEvent, None)
    return JsObjects.JsObject.JsObject("%s.getElementAtEvent(%s)" % (self.toStr(), jsEvent))

  def getElementsAtEvent(self, jsEvent):
    """
    Looks for the element under the event point, then returns all elements at the same data index.

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :param jsEvent:

    :return:
    """
    jsEvent = JsUtils.jsConvertData(jsEvent, None)
    return JsObjects.JsObject.JsObject("%s.getElementsAtEvent(%s)" % (self.toStr(), jsEvent))

  def getDatasetAtEvent(self, jsEvent):
    """
    Looks for the element under the event point, then returns all elements from that dataset.

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :param jsEvent:

    :return: an array of elements
    """
    jsEvent = JsUtils.jsConvertData(jsEvent, None)
    return JsObjects.JsArray.JsArray("%s.getDatasetAtEvent(%s)" % (self.toStr(), jsEvent))

  def getDatasetMeta(self, index):
    """
    Looks for the dataset that matches the current index and returns that metadata.

    Example
    chart.getDatasetMeta(0)

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :param index:

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.getDatasetMeta(%s)" % (self.toStr(), index))

  def render(self, config):
    """
    Triggers a redraw of all chart elements. Note, this does not update elements for new data. Use .update() in that case.

    Example
    chart.render({duration: 800, lazy: false, easing: 'easeOutBounce'})

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    :param config: A python dictionary as config object

    :return:
    """
    config = JsUtils.jsConvertData(config, None)
    return JsObjects.JsObject.JsObject("%s.render(%s)" % (self.toStr(), config))

  def destroy(self):
    """
    Use this to destroy any chart instances that are created.

    Documentation
    https://www.chartjs.org/docs/latest/developers/api.html

    """
    return JsObjects.JsObject.JsObject("%s.destroy()" % self.toStr())

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    if self.setVar:
      if len(self._js) > 0:
        strData = ".".join(self._js)
        strData = "var %s = %s.%s" % (self.varName, self._selector, strData)
      else:
        strData = "var %s = %s" % (self.varName, self._selector)
      self.setVar = False
    else:
      if len(self._js) > 0:
        strData = ".".join(self._js)
        strData = "%s.%s" % (self.varName, strData)
      else:
        strData = self.varName
    self._js = [] # empty the stack
    return strData


class ChartJsOptTicks(DataAttrs):
  def beginAtZero(self, flag):
    self._attrs["beginAtZero"] = JsUtils.jsConvertData(flag, None)
    return self

  def display(self, flag):
    self._attrs["display"] = JsUtils.jsConvertData(flag, None)
    return self


class ChartJsOptGridLines(DataAttrs):

  def display(self, flag=False):
    """
    If false, do not display grid lines for this axis.

    :param flag:
    :return:
    """
    self._attrs["display"] = JsUtils.jsConvertData(flag, None)
    return self

  def circular(self, flag=False):
    """
    If true, gridlines are circular (on radar chart only).

    :param flag:
    :return:
    """
    self._attrs["circular"] = JsUtils.jsConvertData(flag, None)
    return self

  def color(self, colors=""):
    """
    The color of the grid lines.
    If specified as an array, the first color applies to the first grid line, the second to the second grid line and so on.

    :param colors:
    :return:
    """
    self._attrs["color"] = JsUtils.jsConvertData(colors, None)
    return self

  def borderDash(self, narray):
    """

    :param narray:
    :return:
    """
    self._attrs["borderDash"] = JsUtils.jsConvertData(narray, None)
    return self

  def borderDashOffset(self, n=0.0):
    """
    Offset for line dashes

    :param n:
    :return:
    """
    self._attrs["borderDashOffset"] = JsUtils.jsConvertData(n, None)
    return self

  def lineWidth(self, num):
    """
    Stroke width of grid lines.

    :param num:
    :return:
    """
    self._attrs["lineWidth"] = JsUtils.jsConvertData(num, None)
    return self

  def drawBorder(self, flag=True):
    """
    If true, draw border at the edge between the axis and the chart area.

    :param flag:
    :return:
    """
    self._attrs["drawBorder"] = JsUtils.jsConvertData(flag, None)
    return self

  def drawOnChartArea(self, flag=True):
    """
    If true, draw lines on the chart area inside the axis lines.
    This is useful when there are multiple axes and you need to control which grid lines are drawn.

    :param flag:
    :return:
    """
    self._attrs["drawOnChartArea"] = JsUtils.jsConvertData(flag, None)
    return self

  def drawTicks(self, flag=True):
    """
    If true, draw lines beside the ticks in the axis area beside the chart.

    :param flag:
    :return:
    """
    self._attrs["drawTicks"] = JsUtils.jsConvertData(flag, None)
    return self

  def tickMarkLength(self, n=10):
    """
    Length in pixels that the grid lines will draw into the axis area.

    :param n:
    :return:
    """
    self._attrs["tickMarkLength"] = JsUtils.jsConvertData(n, None)
    return self

  def zeroLineWidth(self, n=1):
    """
    Stroke width of the grid line for the first index (index 0).

    :param n:
    :return:
    """
    self._attrs["zeroLineWidth"] = JsUtils.jsConvertData(n, None)
    return self

  def zeroLineColor(self, color="rgba(0, 0, 0, 0.25)"):
    """
    Stroke color of the grid line for the first index (index 0).

    :param color:
    :return:
    """
    self._attrs["zeroLineColor"] = JsUtils.jsConvertData(color, None)
    return self

  def zeroLineBorderDash(self, narray):
    """
    Length and spacing of dashes of the grid line for the first index (index 0)

    :param narray:
    :return:
    """
    self._attrs["zeroLineBorderDash"] = JsUtils.jsConvertData(narray, None)
    return self

  def zeroLineBorderDashOffset(self, n=0.0):
    """
    Offset for line dashes of the grid line for the first index (index 0).

    :param n:
    :return:
    """
    self._attrs["zeroLineBorderDashOffset"] = JsUtils.jsConvertData(n, None)
    return self

  def offsetGridLines(self, flag=True):
    """
    If true, the bars for a particular data point fall between the grid lines.
    The grid line will move to the left by one half of the tick interval, which is the space between the grid lines.
    If false, the grid line will go right down the middle of the bars.
    This is set to true for a category scale in a bar chart while false for other scales or chart types by default.

    :param flag:
    :return:
    """
    self._attrs["offsetGridLines"] = JsUtils.jsConvertData(flag, None)
    return self


class ChartJsOptScale(DataAttrs):

  def ticks(self):
    pass

  @property
  def gridLines(self):
    """

    :rtype: ChartJsOptGridLines
    """
    if not "gridLines" in self._attrs:
      self._attrs["gridLines"] = ChartJsOptGridLines(self._report)
    return self._attrs["gridLines"]

  def stacked(self, flag=False):
    pass


class ChartJsOptScaleBar(ChartJsOptScale):
  def barPercentage(self, n=0.9):
    """
    Percent (0-1) of the available width each bar should be within the category width.
    1.0 will take the whole category width and put the bars right next to each other

    :param n:

    :return:
    """
    if n > 1:
      raise Exception("n cannot exceed 1")

    self._attrs["barPercentage"] = JsUtils.jsConvertData(n, None)
    return self

  def categoryPercentage(self, n=0.8):
    """
    Percent (0-1) of the available width each category should be within the sample width.

    :param n:
    :return:
    """
    self._attrs["categoryPercentage"] = JsUtils.jsConvertData(n, None)
    return self

  def barThickness(self, width="flex"):
    """
    Manually set width of each bar in pixels.

    If set to 'flex', it computes "optimal" sample widths that globally arrange bars side by side.
    If not set (default), bars are equally sized based on the smallest interval.

    :return:
    """
    self._attrs["barThickness"] = JsUtils.jsConvertData(width, None)
    return self

  def maxBarThickness(self, width):
    """
    Set this to ensure that bars are not sized thicker than this.

    :param width: A float
    :return:
    """
    self._attrs["barThickness"] = JsUtils.jsConvertData(width, None)
    return self

  def minBarLength(self, width):
    """

    :param width:
    :return:
    """
    self._attrs["minBarLength"] = JsUtils.jsConvertData(width, None)
    return self


class ChartJsOptTooltip(DataAttrs):
  pass


class ChartJsOptTitle(DataAttrs):
  pass


class ChartJsOptLabels(DataAttrs):
  pass


class ChartJsOptLegend(DataAttrs):
  def display(self, flag=True):
    """
    Is the legend shown?

    Documentation
    https://www.chartjs.org/docs/latest/configuration/legend.html

    :param flag:
    :return:
    """
    self._attrs["display"] = JsUtils.jsConvertData(flag, None)
    return self

  def position(self, location="top"):
    """
    Position of the legend

    :param location:
    :return:
    """
    self._attrs["position"] = JsUtils.jsConvertData(location, None)
    return self

  def fullWidth(self, flag=True):
    """

    :param flag:
    :return:
    """

  def onClick(self, callback):
    """
    A callback that is called when a click event is registered on a label item.

    :param callback:
    :return:
    """
    self._attrs["onClick"] = JsUtils.jsConvertFncs(callback)
    return self

  def onHover(self, callback):
    """
    A callback that is called when a 'mousemove' event is registered on top of a label item.

    :param callback:
    :return:
    """
    self._attrs["onHover"] = JsUtils.jsConvertFncs(callback)
    return self

  def onLeave(self, callback):
    """

    :param callback:
    :return:
    """
    self._attrs["onLeave"] = JsUtils.jsConvertFncs(callback)
    return self

  def reverse(self, flag=False):
    """
    Legend will show datasets in reverse order.

    :param flag:
    :return:
    """
    self._attrs["reverse"] = JsUtils.jsConvertFncs(flag)
    return self

  @property
  def labels(self):
    """

    :rtype: ChartJsOptLabels
    :return:
    """
    if not 'labels' in self._attrs:
      self._attrs["labels"] = ChartJsOptLabels(self._report)
    return self._attrs["labels"]


class ChartJsType(object):
  def __init__(self, type, data):
    self._type, self._data = type, data
    self._data_attrs, self._opts_attrs = {}, {}

  def toStr(self):
    return '{type: "%s", data: %s}' % (self._type, self._data.toStr())

  def backgroundColor(self, colors):
    """
    Data attribute to change the background color (the area between the line chart and the x axis)

    :param colors: Array. The list of colors to add to the data definition
    :return: The ChartJs configuration dictionary for chaining
    """
    self._data_attrs["backgroundColor"] = colors
    return self

  def pointStyle(self, text):
    """

    Documentation

    :param text:
    :return:
    """
    self._data_attrs["pointStyle"] = text
    return self

  def borderColor(self, colors):
    """

    Documentation

    :param colors:
    :return:
    """
    self._data_attrs["backgroundColor"] = colors
    return self

  def fill(self, flag):
    """

    Documentation

    :param flag:
    :return:
    """
    self._data_attrs["fill"] = flag
    return self

  def steppedLine(self, flag):
    self._data_attrs["steppedLine"] = flag
    return self

  def customDataAttr(self, name, value):
    """
    Add a bespoke attribute to the ChartJs definition

    Example

    Documentation

    :param name: The name of the option
    :param value: The value of the option

    :return:
    """
    self._data_attrs[name] = JsUtils.jsConvertData(value, None)
    return self

  def maintainAspectRatio(self, flag):
    """

    Example

    Documentation

    :param flag:
    :return:
    """
    self._opts_attrs["maintainAspectRatio"] = flag
    return self

  def responsive(self, flag):
    self._opts_attrs["responsive"] = flag
    return self

  def scaleShowLabels(self, flag):
    self._opts_attrs["scaleShowLabels"] = flag
    return self

  def customOption(self, name, value):
    """
    Add a bespoke option to the ChartJs definition

    :param name: The name of the option
    :param value: The value of the option

    :return:
    """
    self._opts_attrs[name] = JsUtils.jsConvertData(value, None)
    return self

  @property
  def legend(self):
    return ChartJsOptLegend()

  @property
  def xAxes(self):
    self._opts_attrs.setdefault("scales", {})["xAxes"] = []
    return ChartJsOptScale(self._opts_attrs.setdefault("scales", {})["xAxes"])

  @property
  def yAxes(self):
    self._opts_attrs.setdefault("scales", {})["yAxes"] = []
    return ChartJsOptScale(self._opts_attrs.setdefault("scales", {})["yAxes"])


class ChartJsTypeBar(object):

  def __init__(self, report, type, data):
    self._report = report
    self._data_attrs, self._opts_attrs = {}, {}
    self._data_attrs.update({"type": JsUtils.jsConvertData(type, None), "data": data})

  def backgroundColor(self, colors='rgba(0, 0, 0, 0.1)'):
    """

    Documentation
    https://www.chartjs.org/docs/latest/charts/bar.html

    :param colors:
    :return:
    """
    if not isinstance(colors, list):
      colors = [colors]
    self._data_attrs["backgroundColor"] = colors
    return self

  def borderColor(self, colors='rgba(0, 0, 0, 0.1)'):
    """

    Documentation
    https://www.chartjs.org/docs/latest/charts/bar.html

    :param colors:
    :return:
    """
    if not isinstance(colors, list):
      colors = [colors]
    self._data_attrs["borderColor"] = colors
    return self

  def borderSkipped(self, text='bottom'):
    """
    This setting is used to avoid drawing the bar stroke at the base of the fill.
    In general, this does not need to be changed except when creating chart types that derive from a bar chart.

    Documentation
    https://www.chartjs.org/docs/latest/charts/bar.html#borderskipped

    :param text: A value among ['bottom', 'left', 'top', 'right', False]

    :return:
    """
    skipped_pos = ['bottom', 'left', 'top', 'right', False]
    if not text in skipped_pos:
      raise Exception("text value should be in %s" % skipped_pos)

    self._data_attrs["borderSkipped"] = JsUtils.jsConvertData(text, None)
    return self

  def borderWidth(self, n=0):
    """
    If this value is a number, it is applied to all sides of the rectangle (left, top, right, bottom), except borderSkipped.
    If this value is an object, the left property defines the left border width.
    Similarly the right, top and bottom properties can also be specified. Omitted borders and borderSkipped are skipped.

    Documentation
    https://www.chartjs.org/docs/latest/charts/bar.html#borderwidth

    :param n:
    :return:
    """
    self._data_attrs["borderWidth"] = n
    return self

  def hoverBackgroundColor(self, colors):
    pass

  def hoverBorderColor(self, colors):
    pass

  def hoverBorderWidth(self, n):
    pass

  def label(self, text):
    """
    The label for the dataset which appears in the legend and tooltips.

    :param text:
    :return:
    """
    self._data_attrs["label"] = JsUtils.jsConvertData(text, None)
    return self

  def xAxisID(self, axisId):
    """
    The ID of the x axis to plot this dataset on.

    Documentation
    https://www.chartjs.org/docs/latest/charts/bar.html#general

    :param axisId: The ID of the x axis to plot this dataset on.

    """

  def yAxisID(self, axisId):
    pass

  @property
  def scales(self):
    """

    :rtype: ChartJsOptScaleBar
    :return:
    """
    if not "scales" in self._data_attrs:
      self._data_attrs["scales"] = ChartJsOptScaleBar(self._report)
    return self._data_attrs["scales"]

  def __str__(self):
    return "{%s}" % ", ".join(["%s: %s" % (k, v) for k, v in self._data_attrs.items()])


if __name__ == '__main__':
  chart_bar = ChartJsTypeBar(None, "bar", []).label("test")
  chart_bar.scales.barPercentage(0.4).barThickness(3)
  chart_bar.scales.gridLines.circular(True).color(["red"]).drawTicks()
  print(chart_bar)
