from typing import Union
from epyk.core.py import primitives

from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsNumber


class Event(primitives.JsDataModel):

    def getEvent(self, js_code: str):
        """

        :param js_code:
        """
        return JsObject.JsObject.get(js_code)

    def createEvent(self, js_code: str, event_type: Union[str, primitives.JsDataModel] = 'Event'):
        """Create a bespoke JavaScript event.

        Usages::

          div2 = page.ui.div("Trigger Event")
          div2.click([
            # Define the event
            pk.js_std.createEvent('test_event'),
            pk.js_std.initEvent("build", 'test_event', True, True),

            # Dispatch this event to trigger the component div
            div2.dom.dispatchEvent(pk.js_std.getEvent('test_event'))
          ])

        `mozilla <https://developer.mozilla.org/fr/docs/Web/API/Document/createEvent>`_

        :param js_code:
        :param event_type:
        """
        event_type = JsUtils.jsConvertData(event_type, None)
        return "var %s = document.createEvent(%s)" % (js_code, event_type)

    def initEvent(self, name: Union[str, primitives.JsDataModel], js_code: str = None,
                  bubbles: Union[bool, primitives.JsDataModel] = True,
                  cancelable: Union[bool, primitives.JsDataModel] = True):
        """The Event.initEvent() method is used to initialize the value of an event created using
        Document.createEvent().

        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/Event/initEvent>`_

        :param name: Optional.
        :param js_code: Optional.
        :param bubbles: Optional.
        :param cancelable: Optional.
        """
        name = JsUtils.jsConvertData(name, None)
        bubbles = JsUtils.jsConvertData(bubbles, None)
        cancelable = JsUtils.jsConvertData(cancelable, None)
        js_code = js_code or "document.createEvent('Event')"
        return JsObject.JsObject.get("%s.initEvent(%s, %s, %s)" % (js_code, name, bubbles, cancelable))

    def cancelBubble(self):
        """The cancelBubble() method prevents the event-flow from bubbling up to parent elements.

        `w3schools <https://www.w3schools.com/jsref/event_cancelbubble.asp>`_
        """
        return JsString.JsString("event.cancelBubble = true")

    def target(self):
        """Returns the element that triggered the event

        `w3schools <https://www.w3schools.com/jsref/event_target.asp>`_
        """
        return JsString.JsString("event.target")

    @property
    def dataTransfer(self):
        """The DataTransfer object is used to hold the data that is being dragged during a drag and drop operation.
        It may hold one or more data items, each of one or more data types. For more information about drag and drop,
        see HTML Drag and Drop API.

        This object is available from the dataTransfer property of all drag events.

        `mozilla <https://developer.mozilla.org/fr/docs/Web/API/DataTransfer>`_
        """
        from epyk.core.js.objects.JsData import JsDataTransfer

        return JsDataTransfer("event.dataTransfer")

    @property
    def clipboardData(self):
        """The ClipboardEvent.clipboardData property holds a DataTransfer object, which can be used:

          - to specify what data should be put into the clipboard from the cut and copy event handlers, typically with a
            setData(format, data) call;
          - to obtain the data to be pasted from the paste event handler, typically with a getData(format) call.

        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/ClipboardEvent/clipboardData>`_
        """
        from epyk.core.js.objects.JsData import JsClipboardData

        return JsClipboardData("event.clipboardData")

    @property
    def timeStamp(self):
        """Returns the time (in milliseconds relative to the epoch) at which the event was created.

        `w3schools <https://www.w3schools.com/jsref/event_timestamp.asp>`_
        """
        return JsString.JsString("event.timeStamp", is_py_data=False)

    @property
    def defaultPrevented(self):
        """The defaultPrevented event property checks whether the preventDefault() method was called for the event.

        `w3schools <https://www.w3schools.com/jsref/event_defaultprevented.asp>`_
        """
        return JsString.JsString("event.defaultPrevented", is_py_data=False)

    def preventDefault(self):
        """Cancels the event if it is cancelable, meaning that the default action that belongs to the event will not
        occur.

        `w3schools <https://www.w3schools.com/jsref/event_preventdefault.asp>`_
        """
        return JsString.JsString("event.preventDefault()", is_py_data=False)

    def __getitem__(self, items):
        return JsObject.JsObject("event.%s" % items, is_py_data=False)

    def srcElement(self):
        """The deprecated Event.srcElement is an alias for the Event.target property. Use Event.target instead.

        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/Event/srcElement>`_
        """
        return JsObject.JsObject("event.srcElement()", is_py_data=False)

    def stopImmediatePropagation(self) -> JsString.JsString:
        """The stopImmediatePropagation() method of the Event interface prevents other listeners of the same event from
        being called.

        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/Event/stopImmediatePropagation>`_
        """
        return JsString.JsString("event.stopImmediatePropagation()", is_py_data=False)

    def stopPropagation(self) -> JsString.JsString:
        """Prevents further propagation of an event during event flow.

        `w3schools <https://www.w3schools.com/jsref/event_stoppropagation.asp>`_
        """
        return JsString.JsString("event.stopPropagation()", is_py_data=False)

    def toStr(self) -> str:
        return "event"


class UIEvent(Event):

    @property
    def detail(self) -> JsNumber.JsNumber:
        """The detail property returns a number with details about the event.

        `w3schools <https://www.w3schools.com/jsref/event_detail.asp>`_
        """
        return JsNumber.JsNumber("event.detail", is_py_data=False)

    @property
    def view(self):
        """The view event property returns a reference to the Window object where the event occured.

        `w3schools <https://www.w3schools.com/jsref/event_view.asp>`_
        """
        from epyk.core.js.JsWindow import JsWindow
        return JsWindow()


class KeyboardEvent(UIEvent):

    @property
    def altKey(self) -> JsBoolean.JsBoolean:
        """The altKey property returns a Boolean value that indicates whether or not the "ALT" key was pressed when a
        key event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_key_altkey.asp>`_
        """
        return JsBoolean.JsBoolean.get(js_code="event.altKey")

    @property
    def charCode(self) -> JsString.JsString:
        """The charCode property returns the Unicode character code of the key that triggered the onkeypress event.

        `w3schools <https://www.w3schools.com/jsref/event_key_charcode.asp>`_
        """
        return JsString.JsString.get(js_code="event.charCode")

    @property
    @JsUtils.incompatibleBrowser(["Internet Explorer"])
    def code(self) -> JsString.JsString:
        """The code property returns the key that triggered the event.

        `w3schools <https://www.w3schools.com/jsref/event_key_code.asp>`_
        """
        return JsString.JsString("event.code", is_py_data=False)

    @property
    def ctrlKey(self) -> JsBoolean.JsBoolean:
        """The ctrlKey property returns a Boolean value that indicates whether or not the "CTRL" key was pressed when a
        key event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_key_ctrlkey.asp>`_
        """
        return JsBoolean.JsBoolean("event.ctrlKey", is_py_data=False)

    @property
    @JsUtils.incompatibleBrowser(["Safari"])
    def key(self) -> JsString.JsString:
        """The getModifierState() method returns true if the specified modifier key was pressed, or activated.

        `w3schools <https://www.w3schools.com/jsref/event_key_key.asp>`_
        """
        return JsString.JsString("event.key", is_py_data=False)

    @property
    def keyCode(self) -> JsString.JsString:
        """The keyCode property returns the Unicode character code of the key that triggered the onkeypress event,
        or the Unicode key code of the key that triggered the onkeydown or onkeyup event.

        `w3schools <https://www.w3schools.com/jsref/event_key_keycode.asp>`_
        """
        return JsString.JsString("event.keyCode", is_py_data=False)

    @property
    @JsUtils.incompatibleBrowser(["Safari"])
    def location(self) -> JsNumber.JsNumber:
        """The location property returns a number that indicates the location of a key on the keyboard or device.

        `w3schools <https://www.w3schools.com/jsref/event_key_location.asp>`_
        """
        return JsNumber.JsNumber("event.location", is_py_data=False)

    @property
    def metaKey(self) -> JsString.JsString:
        """The metaKey property returns a Boolean value that indicates whether or not the "META" key was pressed
        when a key event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_key_metakey.asp>`_
        """
        return JsString.JsString("event.metaKey", is_py_data=False)

    @property
    def shiftKey(self) -> JsBoolean.JsBoolean:
        """The shiftKey property returns a Boolean value that indicates whether or not the "SHIFT" key was pressed when
        a key event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_key_shiftkey.asp>`_
        """
        return JsBoolean.JsBoolean.get(js_code="event.shiftKey")

    @property
    def which(self) -> JsNumber.JsNumber:
        """The which property returns the Unicode character code of the key that triggered the onkeypress event,
        or the Unicode key code of the key that triggered the onkeydown or onkeyup event.

        `w3schools <https://www.w3schools.com/jsref/event_key_which.asp>`_
        """
        return JsNumber.JsNumber("event.which", is_py_data=False)


class MouseEvent(UIEvent):

    @property
    def altKey(self) -> JsBoolean.JsBoolean:
        """The altKey property returns a Boolean value that indicates whether or not the "ALT" key was pressed
        when a key event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_altkey.asp>`_
        """
        return JsBoolean.JsBoolean.get(js_code="event.altKey")

    @property
    def button(self) -> JsNumber.JsNumber:
        """The button property returns a number that indicates which mouse button was pressed when a mouse event was
        triggered.

        `w3schools <https://www.w3schools.com/jsref/event_button.asp>`_
        """
        return JsNumber.JsNumber("event.button", is_py_data=False)

    @property
    @JsUtils.incompatibleBrowser(["Safari"])
    def buttons(self) -> JsNumber.JsNumber:
        """The buttons property returns a number that indicates which mouse button or mouse buttons were pressed
        when a mouse event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_buttons.asp>`_
        """
        return JsNumber.JsNumber("event.buttons", is_py_data=False)

    @property
    def isTrusted(self) -> JsBoolean.JsBoolean:
        """

        :return:
        """
        return JsBoolean.JsBoolean.get(js_code="event.isTrusted")

    @property
    def clientX(self):
        """Returns the horizontal coordinate of the mouse pointer, relative to the current window, when the mouse event
        was triggered

        `w3schools <https://www.w3schools.com/jsref/event_clientx.asp>`_
        """
        return JsNumber.JsNumber.get(js_code="event.clientX")

    @property
    def clientY(self) -> JsNumber.JsNumber:
        """The clientY property returns the vertical coordinate (according to the client area) of the mouse pointer
        when a mouse event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_clienty.asp>`_
        """
        return JsNumber.JsNumber.get(js_code="event.clientY")

    @property
    def pageX(self) -> JsNumber.JsNumber:
        """ """
        return JsNumber.JsNumber.get(js_code="event.pageX")

    @property
    def pageY(self) -> JsNumber.JsNumber:
        """ """
        return JsNumber.JsNumber.get(js_code="event.pageY")

    @property
    def offsetX(self) -> JsNumber.JsNumber:
        """Returns the horizontal coordinate of the mouse pointer relative to the position of the edge of the target
        element"""
        return JsNumber.JsNumber.get(js_code="event.offsetX")

    @property
    def offsetY(self) -> JsNumber.JsNumber:
        """Returns the horizontal coordinate of the mouse pointer relative to the position of the edge of the target
        element"""
        return JsNumber.JsNumber.get(js_code="event.offsetY")

    def getField(self, field_name: str) -> JsObject.JsObject:
        return JsObject.JsObject.get("event.%s" % field_name)

    @property
    def metaKey(self) -> JsString.JsString:
        """The metaKey property returns a Boolean value that indicates whether or not the "META" key was pressed
        when a key event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_metakey.asp>`_
        """
        return JsString.JsString("event.metaKey", is_py_data=False)

    @property
    def shiftKey(self) -> JsBoolean.JsBoolean:
        """The shiftKey property returns a Boolean value that indicates whether or not the "SHIFT" key was pressed
        when a mouse event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_shiftkey.asp>`_
        """
        return JsBoolean.JsBoolean.get(js_code="event.shiftKey")

    @property
    def ctrlKey(self) -> JsBoolean.JsBoolean:
        """The ctrlKey property returns a Boolean value that indicates whether or not the "CTRL" key was pressed
        when a mouse event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_ctrlkey.asp>`_
        """
        return JsBoolean.JsBoolean("event.ctrlKey", is_py_data=False)

    @property
    def which(self) -> JsNumber.JsNumber:
        """The which property returns a number that indicates which mouse button was pressed when a mouse event was
        triggered.

        `w3schools <https://www.w3schools.com/jsref/event_which.asp>`_
        """
        return JsNumber.JsNumber("event.which", is_py_data=False)

    @property
    def movementX(self) -> JsNumber.JsNumber:
        """Returns the horizontal coordinate of the mouse pointer relative to the position of the last mousemove event.

        `w3schools <https://www.w3schools.com/jsref/obj_mouseevent.asp>`_
        """
        return JsNumber.JsNumber.get(js_code="event.movementX")

    @property
    def movementY(self) -> JsNumber.JsNumber:
        """Returns the vertical coordinate of the mouse pointer relative to the position of the last mousemove event.

        `w3schools <https://www.w3schools.com/jsref/obj_mouseevent.asp>`_
        """
        return JsNumber.JsNumber.get(js_code="event.movementY")

    @property
    def screenX(self) -> JsNumber.JsNumber:
        """Returns the horizontal coordinate of the mouse pointer, relative to the screen, when an event was triggered.

        `w3schools <https://www.w3schools.com/jsref/obj_mouseevent.asp>`_
        """
        return JsNumber.JsNumber.get(js_code="event.screenX")

    @property
    def screenY(self) -> JsNumber.JsNumber:
        """Returns the vertical coordinate of the mouse pointer, relative to the screen, when an event was triggered.

        `w3schools <https://www.w3schools.com/jsref/obj_mouseevent.asp>`_
        """
        return JsNumber.JsNumber.get(js_code="event.screenY")

    def toStr(self) -> JsObject.JsObject:
        return JsObject.JsObject.get("event")


class TouchEvent(UIEvent):

    @property
    def altKey(self) -> JsBoolean.JsBoolean:
        """The altKey property returns a Boolean value that indicates whether or not the "ALT" key was pressed
        when a touch event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_touch_altkey.asp>`_
        """
        return JsBoolean.JsBoolean.get(js_code="event.altKey")

    @property
    def ctrlKey(self) -> JsBoolean.JsBoolean:
        """The ctrlKey property returns a Boolean value that indicates whether or not the "CTRL" key was pressed
        when a touch event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_touch_ctrlkey.asp>`_
        """
        return JsBoolean.JsBoolean("event.ctrlKey", is_py_data=False)

    @property
    def metaKey(self) -> JsString.JsString:
        """The metaKey property returns a Boolean value that indicates whether or not the "META" key was pressed
        when a touch event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_touch_metakey.asp>`_
        """
        return JsString.JsString("event.metaKey", is_py_data=False)

    @property
    def shiftKey(self) -> JsBoolean.JsBoolean:
        """The shiftKey property returns a Boolean value that indicates whether or not the "SHIFT" key was pressed
        when a touch event was triggered.

        `w3schools <https://www.w3schools.com/jsref/event_touch_shiftkey.asp>`_
        """
        return JsBoolean.JsBoolean.get(js_code="event.shiftKey")

    @property
    def targetTouches(self) -> JsArray.JsArray:
        """The targetTouches property returns an array of Touch objects, one for each finger that is touching the
        current target element.

        `w3schools <https://www.w3schools.com/jsref/event_touch_targettouches.asp>`_
        """
        return JsArray.JsArray("event.shiftKey", is_py_data=False)

    @property
    def touches(self) -> JsArray.JsArray:
        """The touches property returns an array of Touch objects, one for each finger that is currently touching the
        surface.

        `w3schools <https://www.w3schools.com/jsref/event_touch_touches.asp>`_
        """
        return JsArray.JsArray("event.shiftKey", is_py_data=False)

    def ontouchcancel(self):
        raise NotImplementedError()

    def ontouchend(self):
        raise NotImplementedError()

    def ontouchmove(self):
        raise NotImplementedError()

    def ontouchstart(self):
        raise NotImplementedError()
