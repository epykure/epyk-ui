"""
ChartJs API

https://www.chartjs.org/docs/latest/developers/api.html
https://www.chartjs.org/docs/latest/developers/updates.html

"""

import json

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


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


class ChartJsOptTicks(object):

  def __init__(self):
    self.__attrs = {}

  def beginAtZero(self, flag):
    self.__attrs["beginAtZero"] = JsUtils.jsConvertData(flag, None)
    return self

  def display(self, flag):
    self.__attrs["display"] = JsUtils.jsConvertData(flag, None)
    return self

  def custom(self, name, value, isPyData=False):
    if isPyData:
      self.__attrs[name] = json.dumps(value)
    else:
      self.__attrs[name] = value
    return self

  def __str__(self):
    return "{%s}" % ", ".join(["%s: %s" % (k, v) for k, v in self.__attrs.items()])


class ChartJsOptScale(object):

  def __init__(self, options):
    self._options = options

  def ticks(self):
    pass

  def gridLines(self):
    pass

  def stacked(self):
    pass


class ChartJsOptLegend(object):

  def __init__(self, options):
    self._options = options

  def display(self, flag):
    self._options["display"] = flag


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
    self._data_attrs["pointStyle"] = text
    return self

  def borderColor(self, colors):
    """

    :param colors:
    :return:
    """
    self._data_attrs["backgroundColor"] = colors
    return self

  def fill(self, flag):
    """

    :param flag:
    :return:
    """
    self._data_attrs["fill"] = flag
    return self

  def steppedLine(self, flag):
    self._data_attrs["steppedLine"] = flag
    return self

  def maintainAspectRatio(self, flag):
    self._opts_attrs["maintainAspectRatio"] = flag
    return self

  def responsive(self, flag):
    self._opts_attrs["responsive"] = flag
    return self

  def scaleShowLabels(self, flag):
    self._opts_attrs["scaleShowLabels"] = flag
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


chart_data = ChartJsOptTicks()
chart_data.beginAtZero(True).custom("test", "function(){}")

print(chart_data)