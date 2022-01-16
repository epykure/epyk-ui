#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi
from epyk.core.js import JsUtils


class MesuredText:
  def __init__(self, varId):
    self.varId = varId

  @property
  def width(self):
    """
    Description:
    ------------

    """
    return JsNumber.JsNumber("%s.width" % self.varId, isPyData=False)


class RadialGradient:
  def __init__(self, varData, varId):
    self.varId, self.varData, self.__set = varId, varData, True
    self._js = []

  def addColorStop(self, stop, color):
    """
    Description:
    ------------
    The addColorStop() method specifies the colors and position in a gradient object.

    The addColorStop() method is used together with createLinearGradient() or createRadialGradient().

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/createRadialGradient

    Attributes:
    ----------
    :param stop: Float. A value between 0.0 and 1.0 that represents the position between start and end in a gradient.
    :param color: String. A CSS color value to display at the stop position.
    """
    self._js.append("%s.addColorStop(%s, %s)" % (self.varId, stop, JsUtils.jsConvertData(color, None)))
    return self

  def toStr(self):
    if self.__set and self.varData is not None:
      self._js = ["var %s = %s" % (self.varId, self.varData)] + self._js
      self.__set = False
    str_fnc = ";".join(self._js)
    self._js = []
    return str_fnc


class Context2D:
  def __init__(self, src):
    self.varId = '%s.getContext("2d")' % src.dom.varId

  def arc(self, x, y, r, sAngle, eAngle, counterclockwise=None):
    """
    Description:
    ------------
    The arc() method creates an arc/curve (used to create circles, or parts of circles).

    Related Pages:

      https://www.w3schools.com/tags/canvas_arc.asp

    Attributes:
    ----------
    :param x: Float. The x-coordinate of the center of the circle.
    :param y: Float. The y-coordinate of the center of the circle.
    :param r: Float. 	The radius of the circle.
    :param sAngle: Float. The starting angle, in radians (0 is at the 3 o'clock position of the arc's circle).
    :param eAngle: Float. The ending angle, in radians.
    :param counterclockwise: Boolean. Optional. Specifies whether the drawing should be counterclockwise or clockwise. False is default, and indicates clockwise, while true indicates counter-clockwise.
    """
    return "%s.arc(%s, %s, %s, %s, %s)" % (self.varId, x, y, r, sAngle, eAngle)

  def beginPath(self):
    """
    Description:
    ------------
    The beginPath() method begins a path, or resets the current path.

    Related Pages:

      https://www.w3schools.com/tags/canvas_beginpath.asp
    """
    return "%s.beginPath()" % self.varId

  def bezierCurveTo(self, cp1x, cp1y, cp2x, cp2y, x, y):
    """
    Description:
    ------------
    The bezierCurveTo() method adds a point to the current path by using the specified control points that represent a
    cubic Bézier curve.

    Related Pages:

      https://www.w3schools.com/tags/canvas_beziercurveto.asp

    Attributes:
    ----------
    :param cp1x: Float. The x-coordinate of the first Bézier control point.
    :param cp1y: Float. The y-coordinate of the first Bézier control point.
    :param cp2x: Float. The x-coordinate of the second Bézier control point.
    :param cp2y: Float. The y-coordinate of the second Bézier control point.
    :param x: Float. The x-coordinate of the ending point.
    :param y: Float. The y-coordinate of the ending point.
    """
    return "%s.bezierCurveTo(%s, %s, %s, %s, %s, %s)" % (self.varId, cp1x, cp1y, cp2x, cp2y, x, y)

  def clearRect(self, x, y, width, height):
    """
    Description:
    ------------
    The clearRect() method clears the specified pixels within a given rectangle.

    Related Pages:

      https://www.w3schools.com/tags/canvas_clearrect.asp

    Attributes:
    ----------
    :param x: Float. The x-coordinate of the upper-left corner of the rectangle to clear.
    :param y: Float. The y-coordinate of the upper-left corner of the rectangle to clear.
    :param width: Float. The width of the rectangle to clear, in pixels.
    :param height: Float. The height of the rectangle to clear, in pixels.
    """
    return "%s.clearRect(%s, %s, %s, %s)" % (self.varId, x, y, width, height)

  def clip(self):
    """
    Description:
    ------------
    The clip() method clips a region of any shape and size from the original canvas.

    Related Pages:

      https://www.w3schools.com/tags/canvas_clip.asp
    """
    return "%s.clip()" % self.varId

  def closePath(self):
    """
    Description:
    ------------
    The closePath() method creates a path from the current point back to the starting point.

    Related Pages:

      https://www.w3schools.com/tags/canvas_closepath.asp
    """
    return "%s.closePath()" % self.varId

  def createPattern(self, image, repeatType):
    """
    Description:
    ------------
    The createPattern() method repeats the specified element in the specified direction.

    The element can be an image, video, or another <canvas> element.

    Related Pages:

      https://www.w3schools.com/tags/canvas_createpattern.asp

    Attributes:
    ----------
    :param image: Specifies the image, canvas, or video element of the pattern to use.
    :param repeatType: Default. The pattern repeats both horizontally and vertically.
    """
    image = JsUtils.jsConvertData(image, None)
    repeatType = JsUtils.jsConvertData(repeatType, None)
    return "%s.createPattern(%s, %s)" % (self.varId, image, repeatType)

  def createRadialGradient(self, x0, y0, r0, x1, y1, r1, varName):
    """
    Description:
    ------------
    The createRadialGradient() method is specified by six parameters, three defining the gradient's start circle,
    and three defining the end circle.

    Related Pages:

      https://www.w3schools.com/tags/canvas_createradialgradient.asp

    Attributes:
    ----------
    :param x0: Float. The x-coordinate of the starting circle of the gradient.
    :param y0: Float. 	The y-coordinate of the starting circle of the gradient.
    :param r0: Float. The radius of the starting circle.
    :param x1: Float. The x-coordinate of the ending circle of the gradient.
    :param y1: Float. The y-coordinate of the ending circle of the gradient.
    :param r1: Float. The radius of the ending circle.
    :param varName: String. The object reference on the Javascript side.
    """
    gradient_id = "%s.createRadialGradient(%s, %s, %s, %s, %s, %s)" % (self.varId, x0, y0, r0, x1, y1, r1)
    return RadialGradient(varData=gradient_id, varId=varName)

  def createLinearGradient(self, x0, y0, x1, y1, varName):
    """
    Description:
    ------------
    The createLinearGradient() method creates a linear gradient object.

    The gradient can be used to fill rectangles, circles, lines, text, etc.

    Usage::

      canvas.ctx.createLinearGradient(0, 0, canvas.dom.width, 0, "test").
      addColorStop("0", "magenta").addColorStop("0.5", "blue").addColorStop("1.0", "red")
      canvas.ctx.strokeStyle(rptObj.js.object("test"))
      canvas.ctx.strokeText("Hello World!", 10, 50)

    Related Pages:

      https://www.w3schools.com/tags/canvas_createlineargradient.asp

    Attributes:
    ----------
    :param x0: Float. The x-coordinate of the start point of the gradient.
    :param y0: Float. The y-coordinate of the start point of the gradient.
    :param x1: Float. The x-coordinate of the end point of the gradient.
    :param y1: Float. The y-coordinate of the end point of the gradient.
    :param varName: String. The object reference on the Javascript side.
    """
    gradient_id = "%s.createLinearGradient(%s, %s, %s, %s)" % (self.varId, x0, y0, x1, y1)
    return RadialGradient(varData=gradient_id, varId=varName)

  def fill(self, color=None):
    """
    Description:
    ------------
    The fill() method fills the current drawing (path). The default color is black.

    Related Pages:

      https://www.w3schools.com/tags/canvas_fill.asp

    Attributes:
    ----------
    :param color: Optional. String the color to be added to the fillStyle
    """
    if color is None:
      return "%s.fill()" % self.varId

    return "%s; %s.fill()" % (self.fillStyle(color), self.varId)

  def fillStyle(self, color):
    """
    Description:
    ------------
    The fillStyle property sets or returns the color, gradient, or pattern used to fill the drawing.

    Related Pages:

      https://www.w3schools.com/tags/canvas_fillstyle.asp

    Attributes:
    ----------
    :param color: String. The colur definition
    """
    color = JsUtils.jsConvertData(color, None)
    return "%s.fillStyle = %s" % (self.varId, color)

  def fillText(self, text, x, y, maxWidth=None, fillStyle=None):
    """
    Description:
    ------------
    The fillText() method draws filled text on the canvas. The default color of the text is black.

    Related Pages:

      https://www.w3schools.com/tags/canvas_filltext.asp

    Attributes:
    ----------
    :param text: String. Specifies the text that will be written on the canvas.
    :param x: Float. The x coordinate where to start painting the text (relative to the canvas).
    :param y: Float. The y coordinate where to start painting the text (relative to the canvas).
    :param maxWidth: Optional. The maximum allowed width of the text, in pixels.
    """
    if isinstance(text, list):
      text = " + ".join([str(JsUtils.jsConvertData(t, None)) for t in text])
    else:
      text = JsUtils.jsConvertData(text, None)
    if fillStyle is not None:
      return "%s; %s.fillText(%s, %s, %s)" % (self.fillStyle(fillStyle), self.varId, text, x, y)

    if maxWidth is not None:
      return "%s.fillText(%s, %s, %s, %s)" % (self.varId, text, x, y, maxWidth)

    return "%s.fillText(%s, %s, %s)" % (self.varId, text, x, y)

  def lineCap(self, value):
    """
    Description:
    ------------
    The lineCap property sets or returns the style of the end caps for a line.

    Related Pages:

      https://www.w3schools.com/tags/canvas_linecap.asp

    Attributes:
    ----------
    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    return "%s.lineCap = %s" % (self.varId, value)

  def lineJoin(self, value):
    """
    Description:
    ------------
    The lineJoin property sets or returns the type of corner created, when two lines meet.

    Related Pages:

      https://www.w3schools.com/tags/canvas_linejoin.asp

    Attributes:
    ----------
    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    return "%s.lineJoin = %s" % (self.varId, value)

  def lineTo(self, x, y):
    """
    Description:
    ------------
    Adds a new point and creates a line to that point from the last specified point in the canvas.

    Related Pages:

      https://www.w3schools.com/tags/canvas_lineto.asp

    Attributes:
    ----------
    :param x: Float. The x-coordinate of where to create the line to
    :param y: Float. The y-coordinate of where to create the line to
    """
    return "%s.lineTo(%s, %s)" % (self.varId, x, y)

  def lineWidth(self, value):
    """
    Description:
    ------------
    The lineWidth property sets or returns the current line width, in pixels.

    Related Pages:

      https://www.w3schools.com/tags/canvas_linewidth.asp

    Attributes:
    ----------
    :param value: Float. The current line width, in pixels.
    """
    return "%s.lineWidth = %s" % (self.varId, value)

  def moveTo(self, x, y):
    """
    Description:
    ------------
    Moves the path to the specified point in the canvas, without creating a line.

    Related Pages:

      https://www.w3schools.com/tags/canvas_moveto.asp

    Attributes:
    ----------
    :param x: Float. The x-coordinate of where to move the path to
    :param y: Float. The y-coordinate of where to move the path to
    """
    return "%s.moveTo(%s, %s)" % (self.varId, x, y)

  def rect(self, x, y, width, height):
    """
    Description:
    ------------
    The rect() method creates a rectangle.

    Related Pages:

      https://www.w3schools.com/tags/canvas_rect.asp

    Attributes:
    ----------
    :param x: Float. The x-coordinate of the upper-left corner of the rectangle
    :param y: Float. The y-coordinate of the upper-left corner of the rectangle
    :param width: Float. The width of the rectangle, in pixels
    :param height: Float. 	The height of the rectangle, in pixels
    """
    return "%s.rect(%s, %s, %s, %s)" % (self.varId, x, y, width, height)

  def fillRect(self, x, y, width, height):
    """
    Description:
    ------------
    The rect() method creates a rectangle.

    Related Pages:

      https://www.w3schools.com/tags/canvas_rect.asp

    Attributes:
    ----------
    :param x: Float. The x-coordinate of the upper-left corner of the rectangle
    :param y: Float. The y-coordinate of the upper-left corner of the rectangle
    :param width: Float. The width of the rectangle, in pixels
    :param height: Float. 	The height of the rectangle, in pixels
    """
    return "%s.fillRect(%s, %s, %s, %s)" % (self.varId, x, y, width, height)

  def font(self, fontStyle):
    """
    Description:
    ------------
    The font property sets or returns the current font properties for text content on the canvas.

    Related Pages:

      https://www.w3schools.com/tags/canvas_font.asp

    Attributes:
    ----------
    :param fontStyle: String. The font properties
    """
    fontStyle = JsUtils.jsConvertData(fontStyle, None)
    return "%s.font = %s" % (self.varId, fontStyle)

  def globalAlpha(self, number):
    """
    Description:
    ------------
    The globalAlpha property sets or returns the current alpha or transparency value of the drawing.

    The globalAlpha property value must be a number between 0.0 (fully transparent) and 1.0 (no transparancy).

    Related Pages:

      https://www.w3schools.com/tags/canvas_globalalpha.asp

    Attributes:
    ----------
    :param number: Float. The transparency value. Must be a number between 0.0 (fully transparent) and 1.0 (no transparancy)
    """
    return "%s.globalAlpha = %s" % (self.varId, number)

  def isPointInPath(self, x, y):
    """
    Description:
    ------------
    The isPointInPath() method returns true if the specified point is in the current path, otherwise false.

    Related Pages:

      https://www.w3schools.com/tags/canvas_ispointinpath.asp

    Attributes:
    ----------
    :param x: Float. The x-coordinate to test
    :param y: Float. The y-coordinate to test
    """
    return JsBoolean.JsBoolean("%s.isPointInPath(%s, %s)" % (self.varId, x, y), isPyData=False)

  def measureText(self, text):
    """
    Description:
    ------------
    The measureText() method returns an object that contains the width of the specified text, in pixels.

    Related Pages:

      https://www.w3schools.com/tags/canvas_measuretext.asp

    Attributes:
    ----------
    :param text: String. The text
    """
    if isinstance(text, list):
      text = " + ".join([str(JsUtils.jsConvertData(t, None)) for t in text])
    else:
      text = JsUtils.jsConvertData(text, None)
    return MesuredText("%s.measureText(%s)" % (self.varId, text))

  def rotate(self, angle):
    """
    Description:
    ------------
    The rotate() method rotates the current drawing.

    Related Pages:

      https://www.w3schools.com/tags/canvas_rotate.asp

    Attributes:
    ----------
    :param angle: Float. The angle number
    """
    return "%s.rotate(%s)" % (self.varId, angle)

  def scale(self, scalewidth, scaleheight):
    """
    Description:
    ------------
    The scale() method scales the current drawing, bigger or smaller.

    Related Pages:

      https://www.w3schools.com/tags/canvas_scale.asp

    Attributes:
    ----------
    :param scalewidth: Float. Scales the width of the current drawing (1=100%, 0.5=50%, 2=200%, etc.)
    :param scaleheight: Float. Scales the height of the current drawing (1=100%, 0.5=50%, 2=200%, etc.)
    """
    return "%s.scale(%s, %s)" % (self.varId, scalewidth, scaleheight)

  def shadowBlur(self, value):
    """
    Description:
    ------------
    The shadowBlur property sets or returns the blur level for shadows.

    Related Pages:

      https://www.w3schools.com/tags/canvas_shadowblur.asp

    Attributes:
    ----------
    :param value: Float. The blur level for the shadow
    """
    return "%s.shadowBlur = %s" % (self.varId, value)

  def shadowColor(self, color):
    """
    Description:
    ------------
    The shadowColor property sets or returns the color to use for shadows.

    Related Pages:

      https://www.w3schools.com/tags/canvas_shadowcolor.asp

    Attributes:
    ----------
    :param color: String. the color code
    """
    color = JsUtils.jsConvertData(color, None)
    return "%s.shadowColor = %s" % (self.varId, color)

  def shadowOffsetX(self, value):
    """
    Description:
    ------------
    The shadowOffsetX property sets or returns the horizontal distance of the shadow from the shape.

    Related Pages:

      https://www.w3schools.com/tags/canvas_shadowoffsetx.asp

    Attributes:
    ----------
    :param value: Float. A positive or negative number that defines the horizontal distance of the shadow from the shape
    """
    return "%s.shadowOffsetX = %s" % (self.varId, value)

  def shadowOffsetY(self, value):
    """
    Description:
    ------------
    The shadowOffsetY property sets or returns the vertical distance of the shadow from the shape.

    Related Pages:

      https://www.w3schools.com/tags/canvas_shadowoffsety.asp

    Attributes:
    ----------
    :param value: A positive or negative number that defines the vertical distance of the shadow from the shape
    """
    return "%s.shadowOffsetY = %s" % (self.varId, value)

  def stroke(self):
    """
    Description:
    ------------
    The stroke() method actually draws the path you have defined with all those moveTo() and lineTo() methods.
    The default color is black.
    """
    return "%s.stroke()" % self.varId

  def strokeWeight(self, val):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param val:
    """
    return "%s.strokeWeight = %s" % (self.varId, val)

  def strokeStyle(self, color="#000000"):
    """
    Description:
    ------------
    The strokeStyle property sets or returns the color, gradient, or pattern used for strokes.

    Related Pages:

      https://www.w3schools.com/tags/canvas_strokestyle.asp

    Attributes:
    ----------
    :param color: A CSS color value that indicates the stroke color of the drawing. Default value is #000000
    """
    return "%s.strokeStyle = %s" % (self.varId, JsUtils.jsConvertData(color, None))

  def strokeRect(self):
    """
    Description:
    ------------
    The strokeRect() method draws a rectangle (no fill). The default color of the stroke is black.

    Related Pages:

      https://www.w3schools.com/tags/canvas_strokestyle.asp
    """

  def strokeText(self, text, x, y, maxWidth=None):
    """
    Description:
    ------------
    The strokeText() method draws text (with no fill) on the canvas. The default color of the text is black.

    Related Pages:

      https://www.w3schools.com/tags/canvas_stroketext.asp

    Attributes:
    ----------
    :param text: String. Specifies the text that will be written on the canvas
    :param x: Float. The x coordinate where to start painting the text (relative to the canvas)
    :param y: Float. The y coordinate where to start painting the text (relative to the canvas)
    :param maxWidth: Optional. The maximum allowed width of the text, in pixels
    """
    if isinstance(text, list):
      text = " + ".join([str(JsUtils.jsConvertData(t, None)) for t in text])
    else:
      text = JsUtils.jsConvertData(text, None)
    return "%s.strokeText(%s, %s, %s)" % (self.varId, text, x, y)

  def textAlign(self, position):
    """
    Description:
    ------------
    The textAlign property sets or returns the current alignment for text content, according to the anchor point.

    Related Pages:

      https://www.w3schools.com/tags/canvas_textalign.asp

    Attributes:
    ----------
    :param position: String. The context align
    """
    return "%s.textAlign = %s" % (self.varId, JsUtils.jsConvertData(position, None))

  def translate(self, x, y):
    """
    Description:
    ------------
    The translate() method remaps the (0,0) position on the canvas.

    Related Pages:

      https://www.w3schools.com/tags/canvas_translate.asp

    Attributes:
    ----------
    :param x: Float. The value to add to horizontal (x) coordinates
    :param y: Float. The value to add to vertical (y) coordinates
    """
    return "%s.translate(%s, %s)" % (self.varId, x, y)

  def textBaseline(self, position):
    """
    Description:
    ------------
    The textBaseline property sets or returns the current text baseline used when drawing text.

    Related Pages:

      https://www.w3schools.com/tags/canvas_textbaseline.asp

    Attributes:
    ----------
    :param position: String. The context baseline
    """
    return "%s.textBaseline = %s" % (self.varId, JsUtils.jsConvertData(position, None))

  def drawImage(self, img, x, y, width, height):
    """
    Description:
    ------------
    The drawImage() method draws an image, canvas, or video onto the canvas.

    Related Pages:

      https://www.w3schools.com/tags/canvas_drawimage.asp

    Attributes:
    ----------
    :param img: String. Specifies the image, canvas, or video element to use
    :param x: Float. Optional. The x coordinate where to place the image on the canvas
    :param y: Float. Optional. The y coordinate where to place the image on the canvas
    :param width: Float. Optional. The width of the image to use (stretch or reduce the image)
    :param height: Float. Optional. The height of the image to use (stretch or reduce the image)
    """
    pass

  def getImageData(self, x, y, width, height):
    """
    Description:
    ------------
    The getImageData() method returns an ImageData object that copies the pixel data for the specified rectangle
    on a canvas..

    Related Pages:

      https://www.w3schools.com/tags/canvas_getimagedata.asp

    Attributes:
    ----------
    :param x: Float. The x coordinate (in pixels) of the upper-left corner to start copy from.
    :param y: Float. The y coordinate (in pixels) of the upper-left corner to start copy from.
    :param width: Float. The width of the rectangular area you will copy.
    :param height: Float. The height of the rectangular area you will copy.
    """
    return "%s.getImageData(%s, %s, %s, %s)" % (self.varId, x, y, width, height)


class Canvas(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlCode = varName if varName is not None else htmlObj.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self._src, self._report = htmlObj, report
    self._js, self.__2d_context = [], None
    self._jquery, self._jquery_ui = None, None

  @property
  def width(self):
    """
    Description:
    -----------

    """
    return JsNumber.JsNumber("%s.width" % self.varId)

  @property
  def getContext2D(self):
    """
    Description:
    ------------
    The HTMLCanvasElement.getContext() method returns a drawing context on the canvas, or null if the context
    identifier is not supported.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext

    :rtype: Context2D
    """
    if self.__2d_context is None:
      self.__2d_context = Context2D(self._src)
    return self.__2d_context

  @property
  def val(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.value, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.varName))

  @property
  def events(self):
    """
    Description:
    ------------

    :rtype: JsNodeDom.JsDomEvents
    """
    return JsNodeDom.JsDomEvents(self._src)

  @property
  def jquery(self):
    """
    Description:
    ------------

    :rtype: JsQuery.JQuery
    """
    if self._jquery is None:
      self._jquery = JsQuery.JQuery(src=self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlCode))
    return self._jquery

  @property
  def jquery_ui(self):
    """
    Description:
    ------------

    :rtype: JsQueryUi.JQueryUI
    """
    if self._jquery_ui is None:
      self._jquery_ui = JsQueryUi.JQueryUI(self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlCode))
    return self._jquery_ui

  def toDataURL(self, format: str = 'image/jpeg'):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/tags/ref_canvas.asp

    Attributes:
    ----------
    :param format:
    """
    return JsObjects.JsObjects.get("%s.toDataURL(%s)" % (self.varName, JsUtils.jsConvertData(format, None)))

  def save(self):
    """
    Description:
    ------------
    Saves the state of the current context.

    Related Pages:

      https://www.w3schools.com/tags/ref_canvas.asp
    """
    return JsObjects.JsObjects.get("%s.save()" % self.varName)

  def restore(self):
    """
    Description:
    ------------
    Returns previously saved path state and attributes.

    Related Pages:

      https://www.w3schools.com/tags/ref_canvas.asp
    """
    return JsObjects.JsObjects.get("%s.restore()" % self.varName)

