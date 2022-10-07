#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import primitives

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi
from epyk.core.js import JsUtils


class MesuredText:
  def __init__(self, js_code: str):
    self.varId = js_code

  @property
  def width(self):
    """  

    """
    return JsNumber.JsNumber("%s.width" % self.varId, is_py_data=False)


class RadialGradient:
  def __init__(self, data, js_code: str):
    self.varId, self.varData, self.__set = js_code, data, True
    self._js = []

  def addColorStop(self, stop: float, color: str):
    """  
    The addColorStop() method specifies the colors and position in a gradient object.

    The addColorStop() method is used together with createLinearGradient() or createRadialGradient().

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/createRadialGradient

    :param stop: A value between 0.0 and 1.0 that represents the position between start and end in a gradient.
    :param color: A CSS color value to display at the stop position.
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
  def __init__(self, component: primitives.HtmlModel):
    self.varId = '%s.getContext("2d")' % component.dom.varId

  def arc(self, x: float, y: float, r: float, start_angle: float, end_angle: float, counterclockwise: bool = None):
    """  
    The arc() method creates an arc/curve (used to create circles, or parts of circles).

    Related Pages:

      https://www.w3schools.com/tags/canvas_arc.asp

    :param x: The x-coordinate of the center of the circle.
    :param y: The y-coordinate of the center of the circle.
    :param r: The radius of the circle.
    :param start_angle: The starting angle, in radians (0 is at the 3 o'clock position of the arc's circle).
    :param end_angle: The ending angle, in radians.
    :param counterclockwise: Optional. Specifies whether the drawing should be counterclockwise or clockwise.
      False is default, and indicates clockwise, while true indicates counter-clockwise.
    """
    return "%s.arc(%s, %s, %s, %s, %s)" % (self.varId, x, y, r, start_angle, end_angle)

  def beginPath(self):
    """  
    The beginPath() method begins a path, or resets the current path.

    Related Pages:

      https://www.w3schools.com/tags/canvas_beginpath.asp
    """
    return "%s.beginPath()" % self.varId

  def bezierCurveTo(self, cp1x: float, cp1y: float, cp2x: float, cp2y: float, x: float, y: float):
    """  
    The bezierCurveTo() method adds a point to the current path by using the specified control points that represent a
    cubic Bézier curve.

    Related Pages:

      https://www.w3schools.com/tags/canvas_beziercurveto.asp

    :param cp1x: The x-coordinate of the first Bézier control point.
    :param cp1y: The y-coordinate of the first Bézier control point.
    :param cp2x: The x-coordinate of the second Bézier control point.
    :param cp2y: The y-coordinate of the second Bézier control point.
    :param x: The x-coordinate of the ending point.
    :param y: The y-coordinate of the ending point.
    """
    return "%s.bezierCurveTo(%s, %s, %s, %s, %s, %s)" % (self.varId, cp1x, cp1y, cp2x, cp2y, x, y)

  def clearRect(self, x: float, y: float, width: float, height: float):
    """  
    The clearRect() method clears the specified pixels within a given rectangle.

    Related Pages:

      https://www.w3schools.com/tags/canvas_clearrect.asp

    :param x: The x-coordinate of the upper-left corner of the rectangle to clear.
    :param y: The y-coordinate of the upper-left corner of the rectangle to clear.
    :param width: The width of the rectangle to clear, in pixels.
    :param height: The height of the rectangle to clear, in pixels.
    """
    return "%s.clearRect(%s, %s, %s, %s)" % (self.varId, x, y, width, height)

  def clip(self):
    """  
    The clip() method clips a region of any shape and size from the original canvas.

    Related Pages:

      https://www.w3schools.com/tags/canvas_clip.asp
    """
    return "%s.clip()" % self.varId

  def closePath(self):
    """  
    The closePath() method creates a path from the current point back to the starting point.

    Related Pages:

      https://www.w3schools.com/tags/canvas_closepath.asp
    """
    return "%s.closePath()" % self.varId

  def createPattern(self, image: Union[str, primitives.JsDataModel], repeat_type: Union[str, primitives.JsDataModel]):
    """  
    The createPattern() method repeats the specified element in the specified direction.

    The element can be an image, video, or another <canvas> element.

    Related Pages:

      https://www.w3schools.com/tags/canvas_createpattern.asp

    :param image: Specifies the image, canvas, or video element of the pattern to use.
    :param repeat_type: Default. The pattern repeats both horizontally and vertically.
    """
    image = JsUtils.jsConvertData(image, None)
    repeat_type = JsUtils.jsConvertData(repeat_type, None)
    return "%s.createPattern(%s, %s)" % (self.varId, image, repeat_type)

  def createRadialGradient(self, x0: float, y0: float, r0: float, x1: float, y1: float, r1: float, js_code: str):
    """  
    The createRadialGradient() method is specified by six parameters, three defining the gradient's start circle,
    and three defining the end circle.

    Related Pages:

      https://www.w3schools.com/tags/canvas_createradialgradient.asp

    :param x0: The x-coordinate of the starting circle of the gradient.
    :param y0: The y-coordinate of the starting circle of the gradient.
    :param r0: The radius of the starting circle.
    :param x1: The x-coordinate of the ending circle of the gradient.
    :param y1: The y-coordinate of the ending circle of the gradient.
    :param r1: The radius of the ending circle.
    :param js_code: The object reference on the Javascript side.
    """
    gradient_id = "%s.createRadialGradient(%s, %s, %s, %s, %s, %s)" % (self.varId, x0, y0, r0, x1, y1, r1)
    return RadialGradient(data=gradient_id, js_code=js_code)

  def createLinearGradient(self, x0: float, y0: float, x1: float, y1: float, js_code: str):
    """  
    The createLinearGradient() method creates a linear gradient object.

    The gradient can be used to fill rectangles, circles, lines, text, etc.

    Usage::

      canvas.ctx.createLinearGradient(0, 0, canvas.dom.width, 0, "test").
      addColorStop("0", "magenta").addColorStop("0.5", "blue").addColorStop("1.0", "red")
      canvas.ctx.strokeStyle(rptObj.js.object("test"))
      canvas.ctx.strokeText("Hello World!", 10, 50)

    Related Pages:

      https://www.w3schools.com/tags/canvas_createlineargradient.asp

    :param x0: The x-coordinate of the start point of the gradient.
    :param y0: The y-coordinate of the start point of the gradient.
    :param x1: The x-coordinate of the end point of the gradient.
    :param y1: The y-coordinate of the end point of the gradient.
    :param js_code: The object reference on the Javascript side.
    """
    gradient_id = "%s.createLinearGradient(%s, %s, %s, %s)" % (self.varId, x0, y0, x1, y1)
    return RadialGradient(data=gradient_id, js_code=js_code)

  def fill(self, color: Union[str, primitives.JsDataModel] = None):
    """  
    The fill() method fills the current drawing (path). The default color is black.

    Related Pages:

      https://www.w3schools.com/tags/canvas_fill.asp

    :param color: Optional. String the color to be added to the fillStyle.
    """
    if color is None:
      return "%s.fill()" % self.varId

    return "%s; %s.fill()" % (self.fillStyle(color), self.varId)

  def fillStyle(self, color: Union[str, primitives.JsDataModel]):
    """  
    The fillStyle property sets or returns the color, gradient, or pattern used to fill the drawing.

    Related Pages:

      https://www.w3schools.com/tags/canvas_fillstyle.asp

    :param color: The color definition.
    """
    return "%s.fillStyle = %s" % (self.varId, JsUtils.jsConvertData(color, None))

  def fillText(self, text, x, y, max_width: int = None, fill_style: Union[str, primitives.JsDataModel] = None):
    """  
    The fillText() method draws filled text on the canvas. The default color of the text is black.

    Related Pages:

      https://www.w3schools.com/tags/canvas_filltext.asp

    :param text: Specifies the text that will be written on the canvas.
    :param x: The x coordinate where to start painting the text (relative to the canvas).
    :param y: The y coordinate where to start painting the text (relative to the canvas).
    :param max_width: Optional. The maximum allowed width of the text, in pixels.
    :param fill_style:
    """
    if isinstance(text, list):
      text = " + ".join([str(JsUtils.jsConvertData(t, None)) for t in text])
    else:
      text = JsUtils.jsConvertData(text, None)
    if fill_style is not None:
      return "%s; %s.fillText(%s, %s, %s)" % (self.fillStyle(fill_style), self.varId, text, x, y)

    if max_width is not None:
      return "%s.fillText(%s, %s, %s, %s)" % (self.varId, text, x, y, max_width)

    return "%s.fillText(%s, %s, %s)" % (self.varId, text, x, y)

  def lineCap(self, value: Union[str, primitives.JsDataModel]):
    """  
    The lineCap property sets or returns the style of the end caps for a line.

    Related Pages:

      https://www.w3schools.com/tags/canvas_linecap.asp

    :param value:
    """
    return "%s.lineCap = %s" % (self.varId, JsUtils.jsConvertData(value, None))

  def lineJoin(self, value: Union[str, primitives.JsDataModel]):
    """  
    The lineJoin property sets or returns the type of corner created, when two lines meet.

    Related Pages:

      https://www.w3schools.com/tags/canvas_linejoin.asp

    :param value:
    """
    return "%s.lineJoin = %s" % (self.varId, JsUtils.jsConvertData(value, None))

  def lineTo(self, x: float, y: float):
    """  
    Adds a new point and creates a line to that point from the last specified point in the canvas.

    Related Pages:

      https://www.w3schools.com/tags/canvas_lineto.asp

    :param x: The x-coordinate of where to create the line to
    :param y: The y-coordinate of where to create the line to
    """
    return "%s.lineTo(%s, %s)" % (self.varId, x, y)

  def lineWidth(self, value: float):
    """  
    The lineWidth property sets or returns the current line width, in pixels.

    Related Pages:

      https://www.w3schools.com/tags/canvas_linewidth.asp

    :param value: The current line width, in pixels.
    """
    return "%s.lineWidth = %s" % (self.varId, value)

  def moveTo(self, x: float, y: float):
    """  
    Moves the path to the specified point in the canvas, without creating a line.

    Related Pages:

      https://www.w3schools.com/tags/canvas_moveto.asp

    :param x: The x-coordinate of where to move the path to
    :param y: The y-coordinate of where to move the path to
    """
    return "%s.moveTo(%s, %s)" % (self.varId, x, y)

  def rect(self, x: float, y: float, width: float, height: float):
    """  
    The rect() method creates a rectangle.

    Related Pages:

      https://www.w3schools.com/tags/canvas_rect.asp

    :param x: The x-coordinate of the upper-left corner of the rectangle
    :param y: The y-coordinate of the upper-left corner of the rectangle
    :param width: The width of the rectangle, in pixels
    :param height: The height of the rectangle, in pixels
    """
    return "%s.rect(%s, %s, %s, %s)" % (self.varId, x, y, width, height)

  def fillRect(self, x: float, y: float, width: float, height: float):
    """  
    The rect() method creates a rectangle.

    Related Pages:

      https://www.w3schools.com/tags/canvas_rect.asp

    :param x: The x-coordinate of the upper-left corner of the rectangle
    :param y: float The y-coordinate of the upper-left corner of the rectangle
    :param width: The width of the rectangle, in pixels
    :param height: The height of the rectangle, in pixels
    """
    return "%s.fillRect(%s, %s, %s, %s)" % (self.varId, x, y, width, height)

  def font(self, font_style: Union[str, primitives.JsDataModel]):
    """  
    The font property sets or returns the current font properties for text content on the canvas.

    Related Pages:

      https://www.w3schools.com/tags/canvas_font.asp

    :param font_style: The font properties.
    """
    return "%s.font = %s" % (self.varId, JsUtils.jsConvertData(font_style, None))

  def globalAlpha(self, number: float):
    """  
    The globalAlpha property sets or returns the current alpha or transparency value of the drawing.

    The globalAlpha property value must be a number between 0.0 (fully transparent) and 1.0 (no transparency).

    Related Pages:

      https://www.w3schools.com/tags/canvas_globalalpha.asp

    :param number: The transparency value. Must be a number between 0.0 (fully transparent) and 1.0 (no transparency)
    """
    return "%s.globalAlpha = %s" % (self.varId, number)

  def isPointInPath(self, x: float, y: float):
    """  
    The isPointInPath() method returns true if the specified point is in the current path, otherwise false.

    Related Pages:

      https://www.w3schools.com/tags/canvas_ispointinpath.asp

    :param x: The x-coordinate to test.
    :param y: The y-coordinate to test.
    """
    return JsBoolean.JsBoolean("%s.isPointInPath(%s, %s)" % (self.varId, x, y), is_py_data=False)

  def measureText(self, text: Union[str, list, primitives.JsDataModel]):
    """  
    The measureText() method returns an object that contains the width of the specified text, in pixels.

    Related Pages:

      https://www.w3schools.com/tags/canvas_measuretext.asp

    :param text: The text.
    """
    if isinstance(text, list):
      text = " + ".join([str(JsUtils.jsConvertData(t, None)) for t in text])
    else:
      text = JsUtils.jsConvertData(text, None)
    return MesuredText("%s.measureText(%s)" % (self.varId, text))

  def rotate(self, angle: float):
    """  
    The rotate() method rotates the current drawing.

    Related Pages:

      https://www.w3schools.com/tags/canvas_rotate.asp

    :param angle: The angle number
    """
    return "%s.rotate(%s)" % (self.varId, angle)

  def scale(self, scale_width: float, scale_height: float):
    """  
    The scale() method scales the current drawing, bigger or smaller.

    Related Pages:

      https://www.w3schools.com/tags/canvas_scale.asp

    :param scale_width: Scales the width of the current drawing (1=100%, 0.5=50%, 2=200%, etc.)
    :param scale_height: Scales the height of the current drawing (1=100%, 0.5=50%, 2=200%, etc.)
    """
    return "%s.scale(%s, %s)" % (self.varId, scale_width, scale_height)

  def shadowBlur(self, value: float):
    """  
    The shadowBlur property sets or returns the blur level for shadows.

    Related Pages:

      https://www.w3schools.com/tags/canvas_shadowblur.asp

    :param value: The blur level for the shadow.
    """
    return "%s.shadowBlur = %s" % (self.varId, value)

  def shadowColor(self, color: Union[str, primitives.JsDataModel]):
    """  
    The shadowColor property sets or returns the color to use for shadows.

    Related Pages:

      https://www.w3schools.com/tags/canvas_shadowcolor.asp

    :param color: the color code.
    """
    return "%s.shadowColor = %s" % (self.varId, JsUtils.jsConvertData(color, None))

  def shadowOffsetX(self, value: float):
    """  
    The shadowOffsetX property sets or returns the horizontal distance of the shadow from the shape.

    Related Pages:

      https://www.w3schools.com/tags/canvas_shadowoffsetx.asp

    :param value: A positive or negative number that defines the horizontal distance of the shadow from the shape
    """
    return "%s.shadowOffsetX = %s" % (self.varId, value)

  def shadowOffsetY(self, value: float):
    """  
    The shadowOffsetY property sets or returns the vertical distance of the shadow from the shape.

    Related Pages:

      https://www.w3schools.com/tags/canvas_shadowoffsety.asp

    :param value: A positive or negative number that defines the vertical distance of the shadow from the shape
    """
    return "%s.shadowOffsetY = %s" % (self.varId, value)

  def stroke(self):
    """  
    The stroke() method actually draws the path you have defined with all those moveTo() and lineTo() methods.
    The default color is black.
    """
    return "%s.stroke()" % self.varId

  def strokeWeight(self, val: float):
    """  

    :param val:
    """
    return "%s.strokeWeight = %s" % (self.varId, val)

  def strokeStyle(self, color: Union[str, primitives.JsDataModel] = "#000000"):
    """  
    The strokeStyle property sets or returns the color, gradient, or pattern used for strokes.

    Related Pages:

      https://www.w3schools.com/tags/canvas_strokestyle.asp

    :param color: A CSS color value that indicates the stroke color of the drawing.
      Default value is #000000
    """
    return "%s.strokeStyle = %s" % (self.varId, JsUtils.jsConvertData(color, None))

  def strokeRect(self):
    """  
    The strokeRect() method draws a rectangle (no fill). The default color of the stroke is black.

    Related Pages:

      https://www.w3schools.com/tags/canvas_strokestyle.asp
    """

  def strokeText(self, text: Union[str, list, primitives.JsDataModel], x: float, y: float, max_width: float = None):
    """  
    The strokeText() method draws text (with no fill) on the canvas. The default color of the text is black.

    Related Pages:

      https://www.w3schools.com/tags/canvas_stroketext.asp

    :param text: Specifies the text that will be written on the canvas.
    :param x: The x coordinate where to start painting the text (relative to the canvas).
    :param y: The y coordinate where to start painting the text (relative to the canvas).
    :param max_width: Optional. The maximum allowed width of the text, in pixels.
    """
    if isinstance(text, list):
      text = " + ".join([str(JsUtils.jsConvertData(t, None)) for t in text])
    else:
      text = JsUtils.jsConvertData(text, None)
    return "%s.strokeText(%s, %s, %s)" % (self.varId, text, x, y)

  def textAlign(self, position: Union[str, primitives.JsDataModel]):
    """  
    The textAlign property sets or returns the current alignment for text content, according to the anchor point.

    Related Pages:

      https://www.w3schools.com/tags/canvas_textalign.asp

    :param position: The context align
    """
    return "%s.textAlign = %s" % (self.varId, JsUtils.jsConvertData(position, None))

  def translate(self, x: float, y: float):
    """  
    The translate() method remaps the (0,0) position on the canvas.

    Related Pages:

      https://www.w3schools.com/tags/canvas_translate.asp

    :param x: The value to add to horizontal (x) coordinates
    :param y: The value to add to vertical (y) coordinates
    """
    return "%s.translate(%s, %s)" % (self.varId, x, y)

  def textBaseline(self, position: Union[str, primitives.JsDataModel]):
    """  
    The textBaseline property sets or returns the current text baseline used when drawing text.

    Related Pages:

      https://www.w3schools.com/tags/canvas_textbaseline.asp

    :param position: The context baseline.
    """
    return "%s.textBaseline = %s" % (self.varId, JsUtils.jsConvertData(position, None))

  def drawImage(self, img, x: float, y: float, width: float, height: float):
    """  
    The drawImage() method draws an image, canvas, or video onto the canvas.

    Related Pages:

      https://www.w3schools.com/tags/canvas_drawimage.asp

    :param img: Specifies the image, canvas, or video element to use.
    :param x: Optional. The x coordinate where to place the image on the canvas.
    :param y: Optional. The y coordinate where to place the image on the canvas.
    :param width: Optional. The width of the image to use (stretch or reduce the image).
    :param height: Optional. The height of the image to use (stretch or reduce the image).
    """
    pass

  def getImageData(self, x: float, y: float, width: float, height: float):
    """  
    The getImageData() method returns an ImageData object that copies the pixel data for the specified rectangle
    on a canvas.

    Related Pages:

      https://www.w3schools.com/tags/canvas_getimagedata.asp

    :param x: The x coordinate (in pixels) of the upper-left corner to start copy from.
    :param y: The y coordinate (in pixels) of the upper-left corner to start copy from.
    :param width: The width of the rectangular area you will copy.
    :param height: The height of the rectangular area you will copy.
    """
    return "%s.getImageData(%s, %s, %s, %s)" % (self.varId, x, y, width, height)


class Canvas(JsNodeDom.JsDoms):

  def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
               is_py_data: bool = True, page: primitives.PageModel = None):
    self.htmlCode = js_code if js_code is not None else component.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self.component, self.page = component, page
    self._js, self.__2d_context = [], None
    self._jquery, self._jquery_ui = None, None

  @property
  def width(self):
    """   

    """
    return JsNumber.JsNumber("%s.width" % self.varId)

  @property
  def getContext2D(self) -> Context2D:
    """  
    The HTMLCanvasElement.getContext() method returns a drawing context on the canvas, or null if the context
    identifier is not supported.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext

    :rtype: Context2D
    """
    if self.__2d_context is None:
      self.__2d_context = Context2D(self.component)
    return self.__2d_context

  @property
  def val(self):
    """  

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.value, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.varName))

  @property
  def events(self) -> JsNodeDom.JsDomEvents:
    """  

    """
    return JsNodeDom.JsDomEvents(self.component)

  @property
  def jquery(self) -> JsQuery.JQuery:
    """  

    """
    if self._jquery is None:
      self._jquery = JsQuery.JQuery(
        component=self.component, selector=JsQuery.decorate_var("#%s" % self.component.htmlCode))
    return self._jquery

  @property
  def jquery_ui(self) -> JsQueryUi.JQueryUI:
    """  

    """
    if self._jquery_ui is None:
      self._jquery_ui = JsQueryUi.JQueryUI(
        self.component, selector=JsQuery.decorate_var("#%s" % self.component.htmlCode))
    return self._jquery_ui

  def toDataURL(self, format: str = 'image/jpeg'):
    """  

    Related Pages:

      https://www.w3schools.com/tags/ref_canvas.asp

    :param format:
    """
    return JsObjects.JsObjects.get("%s.toDataURL(%s)" % (self.varName, JsUtils.jsConvertData(format, None)))

  def save(self):
    """  
    Saves the state of the current context.

    Related Pages:

      https://www.w3schools.com/tags/ref_canvas.asp
    """
    return JsObjects.JsObjects.get("%s.save()" % self.varName)

  def restore(self):
    """  
    Returns previously saved path state and attributes.

    Related Pages:

      https://www.w3schools.com/tags/ref_canvas.asp
    """
    return JsObjects.JsObjects.get("%s.restore()" % self.varName)

