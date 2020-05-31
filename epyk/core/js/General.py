
from epyk.core.js.Js import JsConsole
from epyk.core.js.Js import JsWindow

from epyk.core.js.objects.JsEvents import Event


initEvent = Event().initEvent
createEvent = Event().createEvent
getEvent = Event().getEvent

console = JsConsole()

window = JsWindow.JsWindow()

alert = JsWindow.JsWindow().alert
