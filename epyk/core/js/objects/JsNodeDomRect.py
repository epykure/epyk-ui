
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsObject


class JsDOMRect:

  def __init__(self, js_code: str):
    self.varId = js_code

  def setVar(self, js_code: str, var_type: str = "var"):
    return JsObject.JsObject("%s %s = %s" % (var_type, js_code, self.varId))

  @property
  def x(self):
    """   The x read-only property of the DOMRectReadOnly interface represents the x coordinate of the DOMRect's origin.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/x
    """
    return JsNumber.JsNumber("%s.x" % self.varId)

  @property
  def y(self):
    """   The y read-only property of the DOMRectReadOnly interface represents the y coordinate of the DOMRect's origin.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/y
    """
    return JsNumber.JsNumber("%s.y" % self.varId)

  @property
  def width(self):
    """   The width read-only property of the DOMRectReadOnly interface represents the width of the DOMRect.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/width
    """
    return JsNumber.JsNumber("%s.width" % self.varId)

  @property
  def height(self):
    """   The height read-only property of the DOMRectReadOnly interface represents the height of the DOMRect.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/height
    """
    return JsNumber.JsNumber("%s.height" % self.varId)

  @property
  def top(self):
    """   The top read-only property of the DOMRectReadOnly interface returns the top coordinate value of the DOMRect.
    (Has the same value as y, or y + height if height is negative.)

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/top
    """
    return JsNumber.JsNumber("%s.top" % self.varId)

  @property
  def right(self):
    """   The right read-only property of the DOMRectReadOnly interface returns the right coordinate value of the DOMRect.
    (Has the same value as x + width, or x if width is negative.)

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/right
    """
    return JsNumber.JsNumber("%s.top" % self.varId)

  @property
  def bottom(self):
    """   The bottom read-only property of the DOMRectReadOnly interface returns the bottom coordinate value of the DOMRect.
    (Has the same value as y + height, or y if height is negative.)

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/bottom
    """
    return JsNumber.JsNumber("%s.top" % self.varId)

  @property
  def left(self):
    """   The left read-only property of the DOMRectReadOnly interface returns the left coordinate value of the DOMRect.
    (Has the same value as x, or x + width if width is negative.)

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/left
    """
    return JsNumber.JsNumber("%s.left" % self.varId)
