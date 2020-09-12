
from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsNumber


class Event(object):

  def getEvent(self, varName):
    return JsObject.JsObject.get(varName)

  def createEvent(self, varName, type='Event'):
    """
    Description:
    ------------

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/API/Document/createEvent

    Attributes:
    ----------
    :param type:
    :param varName:
    """
    return "var %s = document.createEvent('%s')" % (varName, type)

  def initEvent(self, name, varName=None, bubbles=True, cancelable=True):
    """
    Description:
    ------------
    The Event.initEvent() method is used to initialize the value of an event created using Document.createEvent().

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Event/initEvent

    Attributes:
    ----------
    :param name:
    :param bubbles:
    :param cancelable:
    """
    name = JsUtils.jsConvertData(name, None)
    bubbles = JsUtils.jsConvertData(bubbles, None)
    cancelable = JsUtils.jsConvertData(cancelable, None)
    varName = varName or "document.createEvent('Event')"
    return JsObject.JsObject.get("%s.initEvent(%s, %s, %s)" % (varName, name, bubbles, cancelable))

  def cancelBubble(self):
    """
    Description:
    ------------
    The cancelBubble() method prevents the event-flow from bubbling up to parent elements.

    Related Pages:

      https://www.w3schools.com/jsref/event_cancelbubble.asp
    """
    return JsString.JsString("event.cancelBubble = true")

  def target(self):
    """
    Description:
    ------------
    Returns the element that triggered the event

    Related Pages:

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

      https://developer.mozilla.org/fr/docs/Web/API/DataTransfer
    """#
    from epyk.core.js.objects.JsData import JsDataTransfer

    return JsDataTransfer("event.dataTransfer")

  @property
  def clipboardData(self):
    """
    Description:
    ------------
    The ClipboardEvent.clipboardData property holds a DataTransfer object, which can be used:

      - to specify what data should be put into the clipboard from the cut and copy event handlers, typically with a setData(format, data) call;
      - to obtain the data to be pasted from the paste event handler, typically with a getData(format) call.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/ClipboardEvent/clipboardData
    """
    from epyk.core.js.objects.JsData import JsClipboardData

    return JsClipboardData("event.clipboardData")

  @property
  def timeStamp(self):
    """
    Description:
    ------------
    Returns the time (in milliseconds relative to the epoch) at which the event was created

    Related Pages:

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

      https://www.w3schools.com/jsref/event_defaultprevented.asp
    """
    return JsString.JsString("event.defaultPrevented", isPyData=False)

  def preventDefault(self):
    """
    Description:
    ------------
    Cancels the event if it is cancelable, meaning that the default action that belongs to the event will not occur

    Related Pages:

      https://www.w3schools.com/jsref/event_preventdefault.asp
    """
    return JsString.JsString("event.preventDefault()", isPyData=False)

  def stopImmediatePropagation(self):
    """
    Description:
    ------------
    The stopImmediatePropagation() method of the Event interface prevents other listeners of the same event from being called.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Event/stopImmediatePropagation
    """
    return JsString.JsString("event.stopImmediatePropagation()", isPyData=False)

  def stopPropagation(self):
    """
    Description:
    ------------
    Prevents further propagation of an event during event flow

    Related Pages:

      https://www.w3schools.com/jsref/event_stoppropagation.asp
    """
    return JsString.JsString("event.stopPropagation()", isPyData=False)

  def toStr(self):
    return "event"


class UIEvent(Event):

  @property
  def detail(self):
    """
    Description:
    ------------
    The detail property returns a number with details about the event.

    Related Pages:

      https://www.w3schools.com/jsref/event_detail.asp
    """
    return JsNumber.JsNumber("event.detail", isPyData=False)

  @property
  def view(self):
    """
    Description:
    ------------
    The view event property returns a reference to the Window object where the event occured.

    Related Pages:

      https://www.w3schools.com/jsref/event_view.asp
    """
    from epyk.core.js.JsWindow import JsWindow

    return JsWindow()


class KeyboardEvent(UIEvent):

  @property
  def altKey(self):
    """
    Description:
    ------------
    The altKey property returns a Boolean value that indicates whether or not the "ALT" key was pressed when a key event was triggered.

    Related Pages:

      https://www.w3schools.com/jsref/event_key_altkey.asp
    """
    return JsBoolean.JsBoolean.get(varName="event.altKey")

  @property
  def charCode(self):
    """
    Description:
    ------------
    The charCode property returns the Unicode character code of the key that triggered the onkeypress event.

    Related Pages:

      https://www.w3schools.com/jsref/event_key_charcode.asp
    """
    return JsString.JsString.get(varName="event.charCode")

  @property
  @JsUtils.incompatibleBrowser(["Internet Explorer"])
  def code(self):
    """
    Description:
    ------------
    The code property returns the key that triggered the event.

    Related Pages:

      https://www.w3schools.com/jsref/event_key_code.asp
    """
    return JsString.JsString("event.code", isPyData=False)

  @property
  def ctrlKey(self):
    """
    Description:
    ------------
    The ctrlKey property returns a Boolean value that indicates whether or not the "CTRL" key was pressed when a key event was triggered.

    Related Pages:

      https://www.w3schools.com/jsref/event_key_ctrlkey.asp
    """
    return JsBoolean.JsBoolean("event.ctrlKey", isPyData=False)

  @property
  @JsUtils.incompatibleBrowser(["Safari"])
  def key(self):
    """
    Description:
    ------------
    The getModifierState() method returns true if the specified modifier key was pressed, or activated.

    Related Pages:

      https://www.w3schools.com/jsref/event_key_key.asp
    """
    return JsString.JsString("event.key", isPyData=False)

  @property
  def keyCode(self):
    """
    Description:
    ------------
    The keyCode property returns the Unicode character code of the key that triggered the onkeypress event, or the Unicode key code of the key that triggered the onkeydown or onkeyup event.

    Related Pages:

      https://www.w3schools.com/jsref/event_key_keycode.asp
    """
    return JsString.JsString("event.keyCode", isPyData=False)

  @property
  @JsUtils.incompatibleBrowser(["Safari"])
  def location(self):
    """
    Description:
    ------------
    The location property returns a number that indicates the location of a key on the keyboard or device.

    Related Pages:

      https://www.w3schools.com/jsref/event_key_location.asp
    """
    return JsNumber.JsNumber("event.location", isPyData=False)

  @property
  def metaKey(self):
    """
    Description:
    ------------
    The metaKey property returns a Boolean value that indicates whether or not the "META" key was pressed when a key event was triggered.

    Related Pages:

      https://www.w3schools.com/jsref/event_key_metakey.asp
    """
    return JsString.JsString("event.metaKey", isPyData=False)

  @property
  def shiftKey(self):
    """
    Description:
    ------------
    The shiftKey property returns a Boolean value that indicates whether or not the "SHIFT" key was pressed when a key event was triggered.

    Related Pages:

      https://www.w3schools.com/jsref/event_key_shiftkey.asp
    """
    return JsBoolean.JsBoolean.get(varName="event.shiftKey")

  @property
  def which(self):
    """
    Description:
    ------------
    The which property returns the Unicode character code of the key that triggered the onkeypress event, or the Unicode key code of the key that triggered the onkeydown or onkeyup event.

    Related Pages:

      https://www.w3schools.com/jsref/event_key_which.asp
    """
    return JsNumber.JsNumber("event.which", isPyData=False)


class MouseEvent(UIEvent):

  @property
  def altKey(self):
    """
    Description:
    ------------
    The altKey property returns a Boolean value that indicates whether or not the "ALT" key was pressed when a key event was triggered.

    Related Pages:

      https://www.w3schools.com/jsref/event_altkey.asp
    """
    return JsBoolean.JsBoolean.get(varName="event.altKey")

  @property
  def button(self):
    """
    The button property returns a number that indicates which mouse button was pressed when a mouse event was triggered.

    Related Pages:

      https://www.w3schools.com/jsref/event_button.asp
    """
    return JsNumber.JsNumber("event.button", isPyData=False)

  @property
  @JsUtils.incompatibleBrowser(["Safari"])
  def buttons(self):
    """
    The buttons property returns a number that indicates which mouse button or mouse buttons were pressed when a mouse event was triggered.

    Related Pages:

      https://www.w3schools.com/jsref/event_buttons.asp
    """
    return JsNumber.JsNumber("event.buttons", isPyData=False)

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

      https://www.w3schools.com/jsref/event_clienty.asp
    """
    return JsNumber.JsNumber.get(varName="event.clientY")

  @property
  def pageX(self):
    """

    :return:
    """
    return JsNumber.JsNumber.get(varName="event.pageX")

  @property
  def pageY(self):
    """

    :return:
    """
    return JsNumber.JsNumber.get(varName="event.pageY")

  @property
  def offsetX(self):
    """
    Description:
    ------------
    Returns the horizontal coordinate of the mouse pointer relative to the position of the edge of the target element
    """
    return JsNumber.JsNumber.get(varName="event.offsetX")

  @property
  def offsetY(self):
    """
    Description:
    ------------
    Returns the horizontal coordinate of the mouse pointer relative to the position of the edge of the target element
    """
    return JsNumber.JsNumber.get(varName="event.offsetY")

  def getField(self, fieldName):
    return JsObject.JsObject.get("event.%s" % fieldName)

  @property
  def metaKey(self):
    """
    The metaKey property returns a Boolean value that indicates whether or not the "META" key was pressed when a key event was triggered.

    https://www.w3schools.com/jsref/event_metakey.asp
    """
    return JsString.JsString("event.metaKey", isPyData=False)

  @property
  def shiftKey(self):
    """
    The shiftKey property returns a Boolean value that indicates whether or not the "SHIFT" key was pressed when a mouse event was triggered.

    https://www.w3schools.com/jsref/event_shiftkey.asp
    """
    return JsBoolean.JsBoolean.get(varName="event.shiftKey")

  @property
  def ctrlKey(self):
    """
    The ctrlKey property returns a Boolean value that indicates whether or not the "CTRL" key was pressed when a mouse event was triggered.

    https://www.w3schools.com/jsref/event_ctrlkey.asp
    """
    return JsBoolean.JsBoolean("event.ctrlKey", isPyData=False)

  @property
  def which(self):
    """
    The which property returns a number that indicates which mouse button was pressed when a mouse event was triggered.

    https://www.w3schools.com/jsref/event_which.asp
    """
    return JsNumber.JsNumber("event.which", isPyData=False)

  @property
  def movementX(self):
    """
    Description:
    ------------
    Returns the horizontal coordinate of the mouse pointer relative to the position of the last mousemove event

    Related Pages:

      https://www.w3schools.com/jsref/obj_mouseevent.asp
    """
    return JsNumber.JsNumber.get(varName="event.movementX")

  @property
  def movementY(self):
    """
    Description:
    ------------
    Returns the vertical coordinate of the mouse pointer relative to the position of the last mousemove event

    Related Pages:

      https://www.w3schools.com/jsref/obj_mouseevent.asp
    """
    return JsNumber.JsNumber.get(varName="event.movementY")

  @property
  def screenX(self):
    """
    Description:
    ------------
    Returns the horizontal coordinate of the mouse pointer, relative to the screen, when an event was triggered

    Related Pages:

      https://www.w3schools.com/jsref/obj_mouseevent.asp
    """
    return JsNumber.JsNumber.get(varName="event.screenX")

  @property
  def screenY(self):
    """
    Description:
    ------------
    Returns the vertical coordinate of the mouse pointer, relative to the screen, when an event was triggered

    Related Pages:

      https://www.w3schools.com/jsref/obj_mouseevent.asp
    """
    return JsNumber.JsNumber.get(varName="event.screenY")

  def toStr(self):
    return JsObject.JsObject.get("event")


class TouchEvent(UIEvent):

  @property
  def altKey(self):
    """
    Description:
    ------------
    The altKey property returns a Boolean value that indicates whether or not the "ALT" key was pressed when a touch event was triggered.

    Related Pages:

      https://www.w3schools.com/jsref/event_touch_altkey.asp
    """
    return JsBoolean.JsBoolean.get(varName="event.altKey")

  @property
  def ctrlKey(self):
    """
    Description:
    ------------
    The ctrlKey property returns a Boolean value that indicates whether or not the "CTRL" key was pressed when a touch event was triggered.

    Related Pages:

      https://www.w3schools.com/jsref/event_touch_ctrlkey.asp
    """
    return JsBoolean.JsBoolean("event.ctrlKey", isPyData=False)

  @property
  def metaKey(self):
    """
    Description:
    ------------
    The metaKey property returns a Boolean value that indicates whether or not the "META" key was pressed when a touch event was triggered.

    Related Pages:

      https://www.w3schools.com/jsref/event_touch_metakey.asp
    """
    return JsString.JsString("event.metaKey", isPyData=False)

  @property
  def shiftKey(self):
    """
    Description:
    ------------
    The shiftKey property returns a Boolean value that indicates whether or not the "SHIFT" key was pressed when a touch event was triggered.

    Related Pages:

      https://www.w3schools.com/jsref/event_touch_shiftkey.asp
    """
    return JsBoolean.JsBoolean.get(varName="event.shiftKey")

  @property
  def targetTouches(self):
    """
    Description:
    ------------
    The targetTouches property returns an array of Touch objects, one for each finger that is touching the current target element.

    Related Pages:

      https://www.w3schools.com/jsref/event_touch_targettouches.asp
    """
    return JsArray.JsArray("event.shiftKey", isPyData=False)

  @property
  def touches(self):
    """
    Description:
    ------------
    The touches property returns an array of Touch objects, one for each finger that is currently touching the surface.

    Related Pages:

      https://www.w3schools.com/jsref/event_touch_touches.asp
    """
    return JsArray.JsArray("event.shiftKey", isPyData=False)

  def ontouchcancel(self):
    pass

  def ontouchend(self):
    pass

  def ontouchmove(self):
    pass

  def ontouchstart(self):
    pass
