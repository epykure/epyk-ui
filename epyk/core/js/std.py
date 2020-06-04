
from epyk.core.js.Js import JsConsole
from epyk.core.js.Js import JsWindow
from epyk.core.js.Js import JsBase

from epyk.core.js.objects.JsNodeDom import JsDoms
from epyk.core.js.objects.JsEvents import Event


class _Selector(object):

  def __init__(self, component=None):
    self._js = []
    if component is not None:
      self._js.append(component.htmlCode)

  def is_not(self, selector):
    """
    https://www.w3schools.com/cssref/css_selectors.asp

    :param selector:
    """
    self._js.append(":not(selector)")
    return self

  def excluded(self, category, value):
    self._js.append(":not(selector)")
    return self

  def type(self, value):
    return self

  def name(self, value):
    return self

  def toStr(self):
    return "".join(self._js)

  def __str__(self):
    return self.toStr()


dom = JsDoms.new(varName="document", setVar=False)
selector = _Selector

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
