
from epyk.core.js.Js import JsConsole
from epyk.core.js.Js import JsWindow
from epyk.core.js.Js import JsBase

from epyk.core.js.objects.JsNodeDom import JsDoms
from epyk.core.js.objects.JsEvents import Event


class Selector(object):

  def excluded(self, category, value):
    pass

  def type(self, value):
    pass

  def name(self, value):
    pass

  def toStr(self):
    pass

  def __str__(self):
    return self.toStr()


dom = JsDoms.new(varName="document", setVar=False)
selector = Selector()

initEvent = Event().initEvent
createEvent = Event().createEvent
getEvent = Event().getEvent

console = JsConsole()

window = JsWindow.JsWindow()

alert = JsWindow.JsWindow().alert

getElementById = JsBase.getElementById
getElementsByName = JsBase.getElementsByName
getElementsByTagName = JsBase.getElementsByTagName
getElementsByClassName = JsBase.getElementsByClassName

parseFloat = JsBase.parseFloat
parseInt = JsBase.parseInt
parseDate = JsBase.parseDate
typeof = JsBase.typeof
