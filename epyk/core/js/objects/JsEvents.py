"""

"""

from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsObject


class MouseEvent(object):

  @property
  def isTrusted(self):
    return JsBoolean.JsBoolean.get(varName="event.isTrusted")

  def getField(self, fieldName):
    return JsObject.JsObject.get("event.%s" % fieldName)

  def toStr(self):
    return JsObject.JsObject.get("event")
