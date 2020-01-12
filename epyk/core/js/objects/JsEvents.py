"""

"""

from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsNumber

from epyk.core.js.objects.JsData import JsDataTransfer


class Event(object):
  def cancelBubble(self):
    """
    The cancelBubble() method prevents the event-flow from bubbling up to parent elements.

    Documentation
    https://www.w3schools.com/jsref/event_cancelbubble.asp

    :return:
    """
    return JsString.JsString("event.cancelBubble = true")

  def target(self):
    """
    Returns the element that triggered the event

    Documentation
    https://www.w3schools.com/jsref/event_target.asp

    :return:
    """
    return JsString.JsString("event.target")

  @property
  def dataTransfer(self):
    """
    The DataTransfer object is used to hold the data that is being dragged during a drag and drop operation.
    It may hold one or more data items, each of one or more data types. For more information about drag and drop, see HTML Drag and Drop API.

    This object is available from the dataTransfer property of all drag events.

    Example

    Documentation
    https://developer.mozilla.org/fr/docs/Web/API/DataTransfer

    :return:
    """
    return JsDataTransfer("event.dataTransfer")

  @property
  def timeStamp(self):
    """
    Returns the time (in milliseconds relative to the epoch) at which the event was created

    Documentation
    https://www.w3schools.com/jsref/event_timestamp.asp

    :return:
    """
    return JsString.JsString("event.timeStamp", isPyData=False)

  @property
  def defaultPrevented(self):
    """
    The defaultPrevented event property checks whether the preventDefault() method was called for the event.

    Documentation
    https://www.w3schools.com/jsref/event_defaultprevented.asp

    :return:
    """
    return JsString.JsString("event.defaultPrevented", isPyData=False)

  def preventDefault(self):
    """
    Cancels the event if it is cancelable, meaning that the default action that belongs to the event will not occur

    Documentation
    https://www.w3schools.com/jsref/event_preventdefault.asp

    :return:
    """
    return JsString.JsString("event.preventDefault()", isPyData=False)

  def stopImmediatePropagation(self):
    """

    :return:
    """
    return JsString.JsString("event.stopImmediatePropagation()", isPyData=False)

  def stopPropagation(self):
    """
    Prevents further propagation of an event during event flow

    :return:
    """
    return JsString.JsString("event.stopPropagation()", isPyData=False)


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
