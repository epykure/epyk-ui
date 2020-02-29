
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsNumber

from epyk.core.js.objects.JsData import JsDataTransfer


class Event(object):
  def cancelBubble(self):
    """
    Description:
    ------------
    The cancelBubble() method prevents the event-flow from bubbling up to parent elements.

    Related Pages:
    --------------
    https://www.w3schools.com/jsref/event_cancelbubble.asp
    """
    return JsString.JsString("event.cancelBubble = true")

  def target(self):
    """
    Description:
    ------------
    Returns the element that triggered the event

    Related Pages:
    --------------
    https://www.w3schools.com/jsref/event_target.asp
    """
    return JsString.JsString("event.target")

  @property
  def dataTransfer(self):
    """
    Description:
    ------------
    The DataTransfer object is used to hold the data that is being dragged during a drag and drop operation.
    It may hold one or more data items, each of one or more data types. For more information about drag and drop, see HTML Drag and Drop API.

    This object is available from the dataTransfer property of all drag events.

    Related Pages:
    --------------
    https://developer.mozilla.org/fr/docs/Web/API/DataTransfer
    """
    return JsDataTransfer("event.dataTransfer")

  @property
  def timeStamp(self):
    """
    Description:
    ------------
    Returns the time (in milliseconds relative to the epoch) at which the event was created

    Related Pages:
    --------------
    https://www.w3schools.com/jsref/event_timestamp.asp
    """
    return JsString.JsString("event.timeStamp", isPyData=False)

  @property
  def defaultPrevented(self):
    """
    Description:
    ------------
    The defaultPrevented event property checks whether the preventDefault() method was called for the event.

    Related Pages:
    --------------
    https://www.w3schools.com/jsref/event_defaultprevented.asp
    """
    return JsString.JsString("event.defaultPrevented", isPyData=False)

  def preventDefault(self):
    """
    Description:
    ------------
    Cancels the event if it is cancelable, meaning that the default action that belongs to the event will not occur

    Related Pages:
    --------------
    https://www.w3schools.com/jsref/event_preventdefault.asp
    """
    return JsString.JsString("event.preventDefault()", isPyData=False)

  def stopImmediatePropagation(self):
    """
    Description:
    ------------
    The stopImmediatePropagation() method of the Event interface prevents other listeners of the same event from being called.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/Event/stopImmediatePropagation
    """
    return JsString.JsString("event.stopImmediatePropagation()", isPyData=False)

  def stopPropagation(self):
    """
    Description:
    ------------
    Prevents further propagation of an event during event flow

    Related Pages:
    --------------
    https://www.w3schools.com/jsref/event_stoppropagation.asp
    """
    return JsString.JsString("event.stopPropagation()", isPyData=False)


class KeyboardEvent(object):
  pass


class MouseEvent(object):
  @property
  def isTrusted(self):
    """

    :return:
    """
    return JsBoolean.JsBoolean.get(varName="event.isTrusted")

  @property
  def clientX(self):
    """
    Description:
    ------------
    Returns the horizontal coordinate of the mouse pointer, relative to the current window, when the mouse event was triggered

    Related Pages:
    --------------
    https://www.w3schools.com/jsref/event_clientx.asp
    """
    return JsNumber.JsNumber.get(varName="event.clientX")

  @property
  def clientY(self):
    """
    Description:
    ------------
    The clientY property returns the vertical coordinate (according to the client area) of the mouse pointer when a mouse event was triggered.

    Related Pages:
    --------------
    https://www.w3schools.com/jsref/event_clienty.asp
    """
    return JsNumber.JsNumber.get(varName="event.clientY")

  @property
  def offsetX(self):
    """
    Description:
    ------------
    Returns the horizontal coordinate of the mouse pointer relative to the position of the edge of the target element
    """
    return JsNumber.JsNumber.get(varName="event.offsetX")

  def getField(self, fieldName):
    return JsObject.JsObject.get("event.%s" % fieldName)

  def toStr(self):
    return JsObject.JsObject.get("event")
