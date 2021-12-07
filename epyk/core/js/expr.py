
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects

# All the predefined Javascript Statements
from epyk.core.js.statements import JsIf
from epyk.core.js.statements import JsErrors
from epyk.core.js.statements import JsFor
from epyk.core.js.statements import JsSwitch
from epyk.core.js.statements import JsWhile


def if_(jsCond, jsFnc):
  """
  Description:
  ------------
  Conditional statements are used to perform different actions based on different conditions.

  Related Pages:

    https://www.w3schools.com/js/js_if_else.asp

  Attributes:
  ----------
  :param jsCond:
  :param jsFnc:
  """
  if isinstance(jsCond, list):
    jsCond = "(%s)" % ")||(".join(JsUtils.jsConvertFncs(jsCond))
  return JsIf.JsIf(jsCond, jsFnc)


def switch(variable):
  """
  Description:
  ------------
  switch statement is used to perform different actions based on different conditions.

  Related Pages:

    https://www.w3schools.com/js/js_switch.asp

  Attributes:
  ----------
  :param variable:
  """
  if hasattr(variable, 'dom'):
    variable = variable.dom.content
  variable = JsUtils.jsConvertData(variable, None)
  return JsSwitch.JsSwitch(variable)


def while_(pivot, jsFnc=None, options=None):
  """
  Description:
  ------------

  Related Pages:

    https://www.w3schools.com/js/js_loop_while.asp

  Attributes:
  ----------
  :param pivot:
  :param jsFnc:
  :param options:
  """
  js_while = JsWhile.JsWhile(pivot, options=options)
  if jsFnc is not None:
    js_while.fncs(jsFnc)
  return js_while


def whileOf(jsIterable, jsFnc=None, options=None):
  """
  Description:
  ------------

  Related Pages:

    https://www.w3schools.com/js/js_loop_while.asp

  Attributes:
  ----------
  :param jsIterable:
  :param jsFnc:
  """
  if hasattr(jsIterable, 'dom'):
    jsIterable = jsIterable.dom.content
  js_for = JsWhile.JsWhileIterable(jsIterable, options=options)
  if jsFnc is not None:
    js_for.fncs(jsFnc)
  return js_for


def for_(end, jsFnc=None, options=None):
  """
  Description:
  ------------
  Loops can execute a block of code a number of times.

  Related Pages:

    https://www.w3schools.com/js/js_loop_for.asp

  Attributes:
  ----------
  :param end:
  :param jsFnc:
  """
  if hasattr(end, 'dom'):
    end = end.dom.content.number
  js_for = JsFor.JsFor(end, options=options)
  if jsFnc is not None:
    js_for.fncs(jsFnc)
  return js_for


def forIn(jsObj, jsFnc=None, options=None):
  """
  The JavaScript for/in statement loops through the properties of an object

  :param jsObj:
  :param jsFnc:
  """
  if hasattr(jsObj, 'dom'):
    jsObj = jsObj.dom.content
  js_for = JsFor.JsIterable(jsObj, options=options)
  if jsFnc is not None:
    js_for.fncs(jsFnc)
  return js_for


def forOf(jsIterable, jsFnc=None, options=None):
  """
  The JavaScript for/of statement loops through the values of an iterable objects

  :param jsIterable:
  :param jsFnc:
  """
  if hasattr(jsIterable, 'dom'):
    jsIterable = jsIterable.dom.content
  dflt_options = {"type": 'of'}
  if options is not None:
    dflt_options.update(options)
  js_for = JsFor.JsIterable(jsIterable, options=dflt_options)
  if jsFnc is not None:
    js_for.fncs(jsFnc)
  return js_for


def typeof(jsData, type=None):
  """
  Description:
  ------------
  The typeof function

  Related Pages:

    https://www.w3schools.com/js/js_datatypes.asp

  Attributes:
  ----------
  :param jsData: String. A String corresponding to a JavaScript object
  :param type: String. The type of object
  """
  if type is None:
    return JsObjects.JsBoolean.JsBoolean("typeof %s" % JsUtils.jsConvertData(jsData, None))

  return JsObjects.JsVoid("typeof %s === %s" % (JsUtils.jsConvertData(jsData, None), JsUtils.jsConvertData(type, None)))


def not_(jsCond):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param jsCond:
  """
  return "!(%s)" % JsUtils.jsConvertData(jsCond, None)


def try_(jsFncs):
  """
  Description:
  ------------
  Block of code to try

  Related Pages:

    https://www.w3schools.com/js/js_errors.asp

  Attributes:
  ----------
  :param jsFncs: List.
  """
  if not isinstance(jsFncs, list):
    jsFncs = [jsFncs]
  return JsErrors.JsTry(jsFncs)


def and_(*args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  return "(%s)" % ") && (".join([JsUtils.jsConvertData(x, None) for x in args])


def throw(value):
  """
  Description:
  ------------
  The throw statement allows you to create a custom error.

  Technically you can throw an exception (throw an error).

  Related Pages:

    https://www.w3schools.com/js/js_errors.asp

  Attributes:
  ----------
  :param value: String. The message displayed with the exception
  """
  return JsObjects.JsObject.JsObject.get("throw %s" % JsUtils.jsConvertData(value, None))


def or_(*args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  return "(%s)" % ") || (".join([JsUtils.jsConvertData(x, None) for x in args])


break_ = JsObjects.JsObject.JsObject.get("break")


continue_ = JsObjects.JsObject.JsObject.get("continue")
