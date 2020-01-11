"""

"""

from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsNumber


class Event(object):
  def preventDefault(self):
    """

    :return:
    """
    return JsString.JsString("event.preventDefault()")

  def stopImmediatePropagation(self):
    """

    :return:
    """
    return JsString.JsString("event.stopImmediatePropagation()")

  def stopPropagation(self):
    """
    Prevents further propagation of an event during event flow

    :return:
    """
    return JsString.JsString("event.stopPropagation()")


class MouseEvent(object):
  @property
  def isTrusted(self):
    """

    :return:
    """
    return JsBoolean.JsBoolean.get(varName="event.isTrusted")

  @property
  def offsetX(self):
    """
    Returns the horizontal coordinate of the mouse pointer relative to the position of the edge of the target element
    """
    return JsNumber.JsNumber.get(varName="event.offsetX")

  def getField(self, fieldName):
    return JsObject.JsObject.get("event.%s" % fieldName)

  def toStr(self):
    return JsObject.JsObject.get("event")
