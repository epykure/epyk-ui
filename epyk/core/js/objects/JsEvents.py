"""

"""

from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsNumber


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
