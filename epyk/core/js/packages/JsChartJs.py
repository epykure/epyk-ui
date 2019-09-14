"""
ChartJs API

https://www.chartjs.org/docs/latest/developers/api.html
https://www.chartjs.org/docs/latest/developers/updates.html

"""

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class ChartJs(object):
  """

  """
  class __internal(object):
    jqId, htmlId, jsImports, cssImport = 'table', '', set([]), set([])

  def __init__(self, src=None):
    self.src = src if src is not None else self.__internal()
    self.selector = self.src.jqId
    self.src.jsImports.add('Chart.js')
    self._js = []

  def update(self, jsData=None):
    """
    Triggers an update of the chart. This can be safely called after updating the data object.

    https://www.chartjs.org/docs/latest/developers/api.html

    :return:
    """
    if jsData is None:
      return JsObjects.JsObject.JsObject("%s.update()" % self.toStr())

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObject.JsObject("%s.update(%s)" % (self.toStr(), jsData))

  def reset(self):
    """
    Reset the chart to it's state before the initial animation.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.reset()" % self.toStr())

  def stop(self):
    """
    Use this to stop any current animation loop. This will pause the chart during any current animation frame.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.stop()" % self.toStr())

  def resize(self):
    """
    Use this to manually resize the canvas element.

    This is run each time the canvas container is resized, but you can call this method manually if you change the size of the canvas nodes container element.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.resize()" % self.toStr())

  def clear(self):
    """
    Will clear the chart canvas. Used extensively internally between animation frames, but you might find it useful.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.clear()" % self.toStr())

  def toBase64Image(self):
    """
    This returns a base 64 encoded string of the chart in it's current state.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.toBase64Image()" % self.toStr())

  def generateLegend(self):
    """
    Returns an HTML string of a legend for that chart. The legend is generated from the legendCallback in the options.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.generateLegend()" % self.toStr())

  def getElementAtEvent(self, jsEvent):
    """
    Calling getElementAtEvent(event) on your Chart instance passing an argument of an event, or jQuery event, will return the single element at the event position

    :return:
    """
    jsEvent = JsUtils.jsConvertData(jsEvent, None)
    return JsObjects.JsObject.JsObject("%s.getElementAtEvent(%s)" % (self.toStr(), jsEvent))

  def getElementsAtEvent(self, jsEvent):
    """
    Looks for the element under the event point, then returns all elements at the same data index.

    :param jsEvent:
    :return:
    """
    jsEvent = JsUtils.jsConvertData(jsEvent, None)
    return JsObjects.JsObject.JsObject("%s.getElementsAtEvent(%s)" % (self.toStr(), jsEvent))

  def getDatasetAtEvent(self, jsEvent):
    """
    Looks for the element under the event point, then returns all elements from that dataset.

    :param jsEvent:
    :return:
    """
    jsEvent = JsUtils.jsConvertData(jsEvent, None)
    return JsObjects.JsObject.JsObject("%s.getDatasetAtEvent(%s)" % (self.toStr(), jsEvent))

  def getDatasetMeta(self, jsIndex):
    """
    Looks for the dataset that matches the current index and returns that metadata.

    :param jsIndex:
    :return:
    """
    return JsObjects.JsObject.JsObject("%s.getDatasetMeta(%s)" % (self.toStr(), jsIndex))

  def render(self, jsData):
    """
    Triggers a redraw of all chart elements. Note, this does not update elements for new data. Use .update() in that case.

    :return:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObject.JsObject("%s.render(%s)" % (self.toStr(), jsData))

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self.selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self.selector

    strData = "%(jqId)s.%(items)s" % {'jqId': self.selector, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return JsObjects.JsObject.JsObject.get(strData)
