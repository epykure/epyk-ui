
from epyk.core.js.Js import JsConsole
from epyk.core.js.Js import JsWindow
from epyk.core.js.Js import JsBase
from epyk.core.js.Js import JsMaths

from epyk.core.css import Selector

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects

from epyk.core.js.objects.JsNodeDom import JsDoms
from epyk.core.js.objects.JsNodeDom import JsDomsList
from epyk.core.js.objects.JsEvents import Event


def selector(component=None):
  """
  Description:
  -----------
  CSS Selectors

  Related Pages:

      https://www.w3schools.com/cssref/css_selectors.asp

  Attributes:
  ----------
  :param component:
  """
  return Selector.Selector(component)


initEvent = Event().initEvent
createEvent = Event().createEvent
getEvent = Event().getEvent

console = JsConsole()

window = JsWindow.JsWindow()

alert = JsWindow.JsWindow().alert


def querySelectorAll(selector):
  """
  Description:
  ------------
  The querySelectorAll() method returns all elements in the document that matches a specified CSS selector(s),
  as a static NodeList object.

  Related Pages:

      https://www.w3schools.com/jsref/met_document_queryselectorall.asp

  Attributes:
  ----------
  :param selector: String. CSS selectors
  """
  return JsDomsList("document.querySelectorAll(%s)" % JsUtils.jsConvertData(selector, None), isPyData=False)


def querySelector(selector):
  """
  Description:
  ------------
  The querySelector() method returns the first element that matches a specified CSS selector(s) in the document.

  Related Pages:

      https://www.w3schools.com/jsref/met_document_queryselector.asp

  Attributes:
  ----------
  :param selector: String. CSS selectors
  """
  return JsDoms.get("document.querySelector(%s)" % JsUtils.jsConvertData(selector, None))


getElementById = JsBase.getElementById
getElementsByName = JsBase.getElementsByName
getElementsByTagName = JsBase.getElementsByTagName
getElementsByClassName = JsBase.getElementsByClassName

parseFloat = JsBase.parseFloat
parseInt = JsBase.parseInt
parseDate = JsBase.parseDate
typeof = JsBase.typeof

maths = JsMaths.JsMaths()


def comment(value):
  """
  Description:
  ------------
  Javascript Comment section.

  Related Pages:

      https://www.w3schools.com/js/js_comments.asp

  Attributes:
  ----------
  :param value: String. the Value
  """
  return JsObjects.JsVoid("/*%s*/" % value)


def var(name, value=None, global_scope=False):
  """
  Description:
  ------------
  Hoisting is JavaScript's default behavior of moving declarations to the top.

  Attributes:
  ----------
  :param name: String. The variable name
  :param value: Object. Optional. The object
  :param global_scope: Boolean. Optional. The variable scope
  """
  if global_scope:
    name = "window['%s']" % name
  if value is None:
    return JsObjects.JsObject.JsObject.get(name)

  if global_scope:
    return JsObjects.JsVoid("%s = %s" % (name, JsUtils.jsConvertData(value, None)))

  return JsObjects.JsVoid("var %s = %s" % (name, JsUtils.jsConvertData(value, None)))


def recordset(name, value=None, global_scope=False):
  """
  Description:
  ------------
  Hoisting is JavaScript's default behavior of moving declarations to the top.
  Create a recordset variable on the JavaScript side (a list of dictionaries).

  Attributes:
  ----------
  :param name: String. The variable name
  :param value: Object. Optional. The object
  :param global_scope: Boolean. Optional. The variable scope
  """
  if global_scope:
    name = "window['%s']" % name
  if value is None:
    return JsObjects.JsArray.JsRecordSet.get(name)

  if global_scope:
    return JsObjects.JsVoid("%s = %s" % (name, JsUtils.jsConvertData(value, None)))

  return JsObjects.JsVoid("var %s = %s" % (name, JsUtils.jsConvertData(value, None)))


def let(name, value):
  """
  Description:
  ------------
  Redeclaring a variable using the let keyword can solve this problem.

  Redeclaring a variable inside a block will not redeclare the variable outside the block:

  Redeclaring a var variable with let, in the same scope, or in the same block, is not allowed:

  https://www.w3schools.com/js/js_let.asp

  Attributes:
  ----------
  :param name:
  :param value:
  """
  return JsObjects.JsVoid("let %s = %s" % (name, JsUtils.jsConvertData(value, None)))


def const(name, value=None):
  """
  Description:
  ------------
  The keyword const is a little misleading.

  It does NOT define a constant value. It defines a constant reference to a value.

  Redeclaring or reassigning an existing const variable, in the same scope, or in the same block, is not allowed:

  https://www.w3schools.com/js/js_const.asp

  Attributes:
  ----------
  :param name:
  :param value:
  """
  return JsObjects.JsVoid("const %s = %s" % (name, JsUtils.jsConvertData(value, None)))


debugger = JsObjects.JsVoid("debugger")


