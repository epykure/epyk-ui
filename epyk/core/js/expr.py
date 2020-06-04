
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects

# All the predefined Javascript Statements
from epyk.core.js.statements import JsIf
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


def switch(self, jsObj):
  """
  Description:
  ------------

  Related Pages:

    https://www.w3schools.com/js/js_switch.asp

  Attributes:
  ----------
  :param jsFnc:
  """
  if not hasattr(jsObj, 'varName'):
    if isinstance(jsObj, list):
      jsObj = JsObjects.JsArray.JsArray(jsObj, setVar=True)
    else:
      jsObj = JsObjects.JsObject.JsObject(jsObj, setVar=True)
  return JsSwitch.JsSwitch(jsObj, self._src)


def while_(self, pivot, jsFnc=None, iterVar='i', start=0, step=1):
  """
  Description:
  ------------

  :param jsCond:
  """
  jsPivot = JsUtils.jsConvertData(pivot, jsFnc)
  if isPyData and isinstance(pivot, (list, range)):
    return JsWhile.JsWhile(jsPivot, ruleType='array', iterVar=iterVar, start=start, step=step,
                                   context=self._context)
  if isPyData and isinstance(pivot, dict):
    return JsWhile.JsWhile(jsPivot, ruleType='dict', iterVar=iterVar, start=start, step=step,
                                   context=self._context)

  return JsWhile.JsWhile(jsPivot, self._context)


def for_(iterable, jsDataKey=None, isPyData=False, jsFnc=None, iterVar='i', start=0, step=1):
  """
  Description:
  ------------

  :param iterable:
  """
  jsIterable = JsUtils.jsConvert(iterable, jsDataKey, isPyData, jsFnc)
  return JsFor.JsFor(jsIterable, iterVar, start, step)


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
    return JsObjects.JsBoolean.JsBoolean("typeof %s" % jsData)

  return JsObjects.JsVoid("typeof %s === '%s'" % (jsData, type))
