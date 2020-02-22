from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi
from epyk.core.js import JsUtils


class MesuredText(object):
  def __init__(self, varId):
    self.varId = varId

  @property
  def width(self):
    return JsNumber.JsNumber("%s.width" % self.varId, isPyData=False)


class RadialGradient(object):
  def __init__(self, varId):
    self.varId = varId

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
    return "%s.addColorStop(%s, %s)" % (self.varId, stop, color)


class Context2D(object):
  def __init__(self, src):
    self.varId = '%s.getContext("2d")' % src.dom.varId

  def arc(self, x, y, r, sAngle, eAngle, counterclockwise=None):
    """
    The arc() method creates an arc/curve (used to create circles, or parts of circles).

    https://www.w3schools.com/tags/canvas_arc.asp

    :param x:
    :param y:
    :param r:
    :param sAngle:
    :param eAngle:
    :param counterclockwise:
    """
    return "%s.arc(%s, %s, %s, %s, %s)" % (self.varId, x, y, r, sAngle, eAngle)

  def beginPath(self):
    """

    :return:
    """
    return "%s.beginPath()" % self.varId

  def bezierCurveTo(self, cp1x, cp1y, cp2x, cp2y, x, y):
    return "%s.bezierCurveTo(%s, %s, %s, %s, %s, %s)" % (self.varId, cp1x, cp1y, cp2x, cp2y, x, y)

  def clearRect(self, x, y, width, height):
    """
    The clearRect() method clears the specified pixels within a given rectangle.

    https://www.w3schools.com/tags/canvas_clearrect.asp

    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    return "%s.clearRect(%s, %s, %s, %s)" % (self.varId, x, y, width, height)

  def clip(self):
    """
    The clip() method clips a region of any shape and size from the original canvas.

    https://www.w3schools.com/tags/canvas_clip.asp

    :return:
    """
    return "%s.clip()" % self.varId

  def closePath(self):
    """
    The closePath() method creates a path from the current point back to the starting point.

    https://www.w3schools.com/tags/canvas_closepath.asp

    :return:
    """
    return "%s.closePath()" % self.varId

  def createPattern(self, image, repeatType):
    """
    The createPattern() method repeats the specified element in the specified direction.

    The element can be an image, video, or another <canvas> element.

    https://www.w3schools.com/tags/canvas_createpattern.asp

    :param image:
    :param repeatType:

    :return:
    """
    return "createPattern()"

  def createRadialGradient(self, x0, y0, r0, x1, y1, r1):
    """
    Description:
    ------------
    The createRadialGradient() method is specified by six parameters, three defining the gradient's start circle, and three defining the end circle.

    Related Pages:
    --------------
    https://www.w3schools.com/tags/canvas_createradialgradient.asp

    :param x0:
    :param y0:
    :param r0:
    :param x1:
    :param y1:
    :param r1:
    :return:
    """
    gradient_id = "%s.createRadialGradient(%s, %s, %s, %s, %s, %s)" % (self.varId, x0, y0, r0, x1, y1, r1)
    return RadialGradient(varId=gradient_id)

  def createLinearGradient(self, x0, y0, x1, y1):
    """

    :param x0:
    :param y0:
    :param x1:
    :param y1:
    :return:
    """
    gradient_id = "%s.createLinearGradient(%s, %s, %s, %s)" % (self.varId, x0, y0, x1, y1)
    return RadialGradient(varId=gradient_id)

  def fill(self, color=None):
    if color is None:
      return "%s.fill()" % self.varId

    return "%s; %s.fill()" % (self.fillStyle(color), self.varId)

  def fillStyle(self, color):
    """
    Description:
    ------------
    The fillStyle property sets or returns the color, gradient, or pattern used to fill the drawing.

    https://www.w3schools.com/tags/canvas_fillstyle.asp

    :return:
    """
    color = JsUtils.jsConvertData(color, None)
    return "%s.fillStyle = %s" % (self.varId, color)

  def fillText(self, text, x, y, maxWidth=None, fillStyle=None):
    """

    :param text:
    :param x:
    :param y:
    :param maxWidth:
    """
    if isinstance(text, list):
      text = " + ".join([str(JsUtils.jsConvertData(t, None)) for t in text])
    else:
      text = JsUtils.jsConvertData(text, None)
    if fillStyle is not None:
      return "%s; %s.fillText(%s, %s, %s)" % (self.fillStyle(fillStyle), self.varId, text, x, y)

    return "%s.fillText(%s, %s, %s)" % (self.varId, text, x, y)

  def lineCap(self, value):
    """
    The lineCap property sets or returns the style of the end caps for a line.

    https://www.w3schools.com/tags/canvas_linecap.asp

    :param value:
    :return:
    """
    value = JsUtils.jsConvertData(value, None)
    return "%s.lineCap = %s" % (self.varId, value)

  def lineJoin(self, value):
    """
    The lineJoin property sets or returns the type of corner created, when two lines meet.

    https://www.w3schools.com/tags/canvas_linejoin.asp

    :param value:
    :return:
    """
    value = JsUtils.jsConvertData(value, None)
    return "%s.lineJoin = %s" % (self.varId, value)

  def lineTo(self, x, y):
    """
    Adds a new point and creates a line to that point from the last specified point in the canvas

    https://www.w3schools.com/tags/canvas_lineto.asp

    :param x:
    :param y:
    :return:
    """
    return "%s.lineTo(%s, %s)" % (self.varId, x, y)

  def lineWidth(self, value):
    return "%s.lineWidth = %s" % (self.varId, value)

  def moveTo(self, x, y):
    """
    Moves the path to the specified point in the canvas, without creating a line

    :param x:
    :param y:

    :return:
    """
    return "%s.moveTo(%s, %s)" % (self.varId, x, y)

  def rect(self, x, y, width, height):
    """
    The rect() method creates a rectangle.

    https://www.w3schools.com/tags/canvas_rect.asp

    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    return "%s.rect(%s, %s, %s, %s)" % (self.varId, x, y, width, height)

  def fillRect(self, x, y, width, height):
    """
        The rect() method creates a rectangle.

        https://www.w3schools.com/tags/canvas_rect.asp

        :param x:
        :param y:
        :param width:
        :param height:
        :return:
        """
    return "%s.fillRect(%s, %s, %s, %s)" % (self.varId, x, y, width, height)

  def font(self, fontStyle):

    fontStyle = JsUtils.jsConvertData(fontStyle, None)
    return "%s.font = %s" % (self.varId, fontStyle)

  def globalAlpha(self, number):
    """
    The globalAlpha property sets or returns the current alpha or transparency value of the drawing.

    The globalAlpha property value must be a number between 0.0 (fully transparent) and 1.0 (no transparancy).

    https://www.w3schools.com/tags/canvas_globalalpha.asp

    :param number:
    """
    return "%s.globalAlpha = %s" % (self.varId, number)

  def isPointInPath(self, x, y):
    """
    The isPointInPath() method returns true if the specified point is in the current path, otherwise false.

    https://www.w3schools.com/tags/canvas_ispointinpath.asp

    :param x:
    :param y:
    :return:
    """
    return JsBoolean.JsBoolean("%s.isPointInPath(%s, %s)" % (self.varId, x, y), isPyData=False)

  def measureText(self, text):
    """
    The measureText() method returns an object that contains the width of the specified text, in pixels.

    https://www.w3schools.com/tags/canvas_measuretext.asp

    :param text:
    """
    if isinstance(text, list):
      text = " + ".join([str(JsUtils.jsConvertData(t, None)) for t in text])
    else:
      text = JsUtils.jsConvertData(text, None)
    return MesuredText("%s.measureText(%s)" % (self.varId, text))

  def rotate(self, angle):
    """
    The rotate() method rotates the current drawing.

    https://www.w3schools.com/tags/canvas_rotate.asp

    :param angle:
    :return:
    """
    return "%s.rotate(%s)" % (self.varId, angle)

  def scale(self, scalewidth, scaleheight):
    """
    The scale() method scales the current drawing, bigger or smaller.

    https://www.w3schools.com/tags/canvas_scale.asp

    :param scalewidth: Float. Scales the width of the current drawing (1=100%, 0.5=50%, 2=200%, etc.)
    :param scaleheight: Float. Scales the height of the current drawing (1=100%, 0.5=50%, 2=200%, etc.)
    :return:
    """
    return "%s.scale(%s, %s)" % (self.varId, scalewidth, scaleheight)

  def shadowBlur(self, value):
    """
    The shadowBlur property sets or returns the blur level for shadows.

    https://www.w3schools.com/tags/canvas_shadowblur.asp
    """
    return "%s.shadowBlur = %s" % (self.varId, value)

  def shadowColor(self, color):
    """
    The shadowColor property sets or returns the color to use for shadows.

    https://www.w3schools.com/tags/canvas_shadowcolor.asp
    """
    color = JsUtils.jsConvertData(color, None)
    return "%s.shadowColor = %s" % (self.varId, color)

  def shadowOffsetX(self, value):
    """
    The shadowOffsetX property sets or returns the horizontal distance of the shadow from the shape.

    https://www.w3schools.com/tags/canvas_shadowoffsetx.asp
    """
    return "%s.shadowOffsetX = %s" % (self.varId, value)

  def shadowOffsetY(self, value):
    """
    The shadowOffsetY property sets or returns the vertical distance of the shadow from the shape.

    https://www.w3schools.com/tags/canvas_shadowoffsety.asp
    """
    return "%s.shadowOffsetY = %s" % (self.varId, value)

  def stroke(self):

    return "%s.stroke()" % self.varId

  def strokeWeight(self, val):
    return "%s.strokeWeight = %s" % (self.varId, val)

  def strokeStyle(self, color):
    """
    The strokeStyle property sets or returns the color, gradient, or pattern used for strokes.

    https://www.w3schools.com/tags/canvas_strokestyle.asp

    :return:
    """
    color = JsUtils.jsConvertData(color, None)
    return "%s.strokeStyle = %s" % (self.varId, color)

  def strokeRect(self):
    """
    https://www.w3schools.com/tags/canvas_strokestyle.asp
    :return:
    """

  def strokeText(self, text, x, y, maxWidth=None):
    """

    https://www.w3schools.com/tags/canvas_stroketext.asp

    :param text:
    :param x:
    :param y:
    :param maxWidth:
    :return:
    """
    if isinstance(text, list):
      text = " + ".join([str(JsUtils.jsConvertData(t, None)) for t in text])
    else:
      text = JsUtils.jsConvertData(text, None)
    return "%s.strokeText(%s, %s, %s)" % (self.varId, text, x, y)

  def textAlign(self, position):
    """

    :param position:
    :return:
    """
    position = JsUtils.jsConvertData(position, None)
    return "%s.textAlign = %s" % (self.varId, position)

  def translate(self, x, y):
    return "%s.translate(%s, %s)" % (self.varId, x, y)

  def textBaseline(self, position):
    """
    The textBaseline property sets or returns the current text baseline used when drawing text.

    :param position:

    :return:
    """
    position = JsUtils.jsConvertData(position, None)
    return "%s.textBaseline = %s" % (self.varId, position)

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
