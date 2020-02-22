from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi


class RadialGradient(object):
  def __init__(self, x0, y0, r0, x1, y1, r1):
    self.x0, self.y0, self.r0, self.x1, self.y1, self.r1 = x0, y0, r0, x1, y1, r1

  def addColorStop(self, stop, color):
    """
    Description:
    ------------
    The addColorStop() method specifies the colors and position in a gradient object.

    The addColorStop() method is used together with createLinearGradient() or createRadialGradient().

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/createRadialGradient

    Attributes:
    ----------
    :param stop: Float. A value between 0.0 and 1.0 that represents the position between start and end in a gradient
    :param color: String. A CSS color value to display at the stop position
    """
    return "%s.addColorStop(%s, %s)" % ()


class Context2D(object):

  def fillStyle(self):
    """
    Description:
    ------------
    The fillStyle property sets or returns the color, gradient, or pattern used to fill the drawing.

    https://www.w3schools.com/tags/canvas_fillstyle.asp

    :return:
    """

  def arc(self):
    pass

  def beginPath(self):
    pass

  def createLinearGradient(self):
    """
    The createLinearGradient() method creates a linear gradient object.

    The gradient can be used to fill rectangles, circles, lines, text, etc.

    https://www.w3schools.com/tags/canvas_createlineargradient.asp
    """

  def createPattern(self):
    """
    The createPattern() method repeats the specified element in the specified direction.

    The element can be an image, video, or another <canvas> element.

    https://www.w3schools.com/tags/canvas_createpattern.asp
    :return:
    """

  def createRadialGradient(self, x0, y0, r0, x1, y1, r1):
    """
    Description:
    ------------
    The createRadialGradient() method is specified by six parameters, three defining the gradient's start circle, and three defining the end circle.

    Related Pages:
    --------------
    https://www.w3schools.com/tags/canvas_createradialgradient.asp
    """
    return RadialGradient(x0, y0, r0, x1, y1, r1)

  def addColorStop(self):
    """
    The addColorStop() method specifies the colors and position in a gradient object.

    https://www.w3schools.com/tags/canvas_addcolorstop.asp
    """

  def shadowBlur(self):
    """
    The shadowBlur property sets or returns the blur level for shadows.

    https://www.w3schools.com/tags/canvas_shadowblur.asp
    """

  def shadowColor(self):
    """
    The shadowColor property sets or returns the color to use for shadows.

    https://www.w3schools.com/tags/canvas_shadowcolor.asp
    """

  def shadowOffsetX(self):
    """
    The shadowOffsetX property sets or returns the horizontal distance of the shadow from the shape.

    https://www.w3schools.com/tags/canvas_shadowoffsetx.asp
    """

  def shadowOffsetY(self):
    """
    The shadowOffsetY property sets or returns the vertical distance of the shadow from the shape.

    https://www.w3schools.com/tags/canvas_shadowoffsety.asp
    """

  def stroke(self):
    pass

  def strokeStyle(self):
    """
    The strokeStyle property sets or returns the color, gradient, or pattern used for strokes.

    https://www.w3schools.com/tags/canvas_strokestyle.asp

    :return:
    """

  def strokeRect(self):
    """
    https://www.w3schools.com/tags/canvas_strokestyle.asp
    :return:
    """

  def drawImage(self):
    pass


class Canvas(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlId = varName if varName is not None else htmlObj.htmlId
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlId, "", None
    self._src, self._report = htmlObj, report
    self._js, self.__2d_context = [], None
    self._jquery, self._jquery_ui = None, None

  @property
  def getContext2D(self):
    """

    rtype: Context2D
    """
    if self.__2d_context is None:
      self.__2d_context = Context2D(self._src)
    return self.__2d_context

  @property
  def val(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.value, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlId, self.varName))

  @property
  def events(self):
    """

    :rtype: JsNodeDom.JsDomEvents
    :return:
    """
    return JsNodeDom.JsDomEvents(self._src)

  @property
  def jquery(self):
    """

    :return:
    :rtype: JsQuery.JQuery
    """
    if self._jquery is None:
      self._jquery = JsQuery.JQuery(src=self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlId))
    return self._jquery

  @property
  def jquery_ui(self):
    """

    :return:
    :rtype: JsQuery.JQuery
    """
    if self._jquery_ui is None:
      self._jquery_ui = JsQueryUi.JQueryUI(self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlId))
    return self._jquery_ui
