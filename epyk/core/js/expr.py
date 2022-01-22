
from typing import Union, Optional, List
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects

# All the predefined Javascript Statements
from epyk.core.js.statements import JsIf
from epyk.core.js.statements import JsErrors
from epyk.core.js.statements import JsFor
from epyk.core.js.statements import JsSwitch
from epyk.core.js.statements import JsWhile


def if_(condition: Union[List[Union[str, primitives.JsDataModel]], bool, str], js_funcs: Union[list, str]):
  """
  Description:
  ------------
  Conditional statements are used to perform different actions based on different conditions.

  Related Pages:

    https://www.w3schools.com/js/js_if_else.asp

  Attributes:
  ----------
  :param Union[list[Union[str, primitives.JsDataModel]], str] condition: The JavaScript conditions.
  :param Union[list, str] js_funcs: The Javascript functions.
  """
  if isinstance(condition, list):
    condition = "(%s)" % ")||(".join(JsUtils.jsConvertFncs(condition))
  return JsIf.JsIf(condition, js_funcs)


def switch(variable: Union[primitives.JsDataModel, str]):
  """
  Description:
  ------------
  switch statement is used to perform different actions based on different conditions.

  Related Pages:

    https://www.w3schools.com/js/js_switch.asp

  Attributes:
  ----------
  :param Union[primitives.JsDataModel, str] variable:
  """
  if hasattr(variable, 'dom'):
    variable = variable.dom.content
  variable = JsUtils.jsConvertData(variable, None)
  return JsSwitch.JsSwitch(variable)


def while_(pivot, js_funcs: Optional[Union[list, str]] = None, options: Optional[dict] = None,
           profile: Optional[Union[dict, bool]] = False):
  """
  Description:
  ------------

  Related Pages:

    https://www.w3schools.com/js/js_loop_while.asp

  Attributes:
  ----------
  :param str pivot: The JavaScript expression.
  :param Optional[Union[list, str]] js_funcs: The Javascript functions.
  :param Optional[dict] options: Optional. Specific Python options available for this component.
  :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
  """
  js_while = JsWhile.JsWhile(pivot, options=options, profile=profile)
  if js_funcs is not None:
    js_while.fncs(js_funcs)
  return js_while


def whileOf(iterable, js_funcs: Optional[Union[list, str]] = None, options: Optional[dict] = None,
            profile: Optional[Union[dict, bool]] = None):
  """
  Description:
  ------------

  Related Pages:

    https://www.w3schools.com/js/js_loop_while.asp

  Attributes:
  ----------
  :param iterable:
  :param Optional[Union[list, str]] js_funcs: The Javascript functions.
  :param Optional[dict] options: Optional. Specific Python options available for this component.
  :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
  """
  if hasattr(iterable, 'dom'):
    iterable = iterable.dom.content
  js_for = JsWhile.JsWhileIterable(iterable, options=options, profile=profile)
  if js_funcs is not None:
    js_for.fncs(js_funcs)
  return js_for


def for_(end, js_funcs: Optional[Union[list, str]] = None, options: Optional[dict] = None,
         profile: Optional[Union[dict, bool]] = None):
  """
  Description:
  ------------
  Loops can execute a block of code a number of times.

  Related Pages:

    https://www.w3schools.com/js/js_loop_for.asp

  Attributes:
  ----------
  :param end:
  :param Optional[Union[list, str]] js_funcs: The Javascript functions.
  :param Optional[dict] options: Optional. Specific Python options available for this component.
  :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
  """
  if hasattr(end, 'dom'):
    end = end.dom.content.number
  js_for = JsFor.JsFor(end, options=options, profile=profile)
  if js_funcs is not None:
    js_for.fncs(js_funcs)
  return js_for


def forIn(jsObj, js_funcs: Optional[Union[list, str]] = None, options: Optional[dict] = None,
          profile: Optional[Union[dict, bool]] = None):
  """
  Description:
  ------------
  The JavaScript for/in statement loops through the properties of an object

  Attributes:
  ----------
  :param jsObj:
  :param Optional[Union[list, str]] js_funcs: The Javascript functions.
  :param Optional[dict] options: Optional. Specific Python options available for this component.
  :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
  """
  if hasattr(jsObj, 'dom'):
    jsObj = jsObj.dom.content
  js_for = JsFor.JsIterable(jsObj, options=options, profile=profile)
  if js_funcs is not None:
    js_for.fncs(js_funcs)
  return js_for


def forOf(iterable, js_funcs: Optional[Union[list, str]] = None, options: Optional[dict] = None,
          profile: Optional[Union[dict, bool]] = None):
  """
  Description:
  ------------
  The JavaScript for/of statement loops through the values of an iterable objects.

  Attributes:
  ----------
  :param iterable:
  :param Optional[Union[list, str]] js_funcs: The Javascript functions.
  :param Optional[dict] options: Optional. Specific Python options available for this component.
  :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
  """
  if hasattr(iterable, 'dom'):
    iterable = iterable.dom.content
  dfl_options = {"type": 'of'}
  if options is not None:
    dfl_options.update(options)
  js_for = JsFor.JsIterable(iterable, options=dfl_options, profile=profile)
  if js_funcs is not None:
    js_for.fncs(js_funcs)
  return js_for


def typeof(jsData: Union[primitives.JsDataModel, str], type: Optional[Union[primitives.JsDataModel, str]] = None):
  """
  Description:
  ------------
  The typeof function

  Related Pages:

    https://www.w3schools.com/js/js_datatypes.asp

  Attributes:
  ----------
  :param Union[primitives.JsDataModel, str] jsData: A String corresponding to a JavaScript object.
  :param Optional[Union[primitives.JsDataModel, str]] type: The type of object.
  """
  if type is None:
    return JsObjects.JsBoolean.JsBoolean("typeof %s" % JsUtils.jsConvertData(jsData, None))

  return JsObjects.JsVoid("typeof %s === %s" % (JsUtils.jsConvertData(jsData, None), JsUtils.jsConvertData(type, None)))


def not_(condition: Union[primitives.JsDataModel, str]):
  """
  Description:
  ------------
  Add a not JavaScript expression to a JavaScript string.

  Attributes:
  ----------
  :param Union[primitives.JsDataModel, str] condition: The JavaScript expression.
  """
  return "!(%s)" % JsUtils.jsConvertData(condition, None)


def try_(js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
  """
  Description:
  ------------
  Block of code to try.

  Related Pages:

    https://www.w3schools.com/js/js_errors.asp

  Attributes:
  ----------
  :param Union[list, str] js_funcs: The PyJs functions.
  :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
  """
  if not isinstance(js_funcs, list):
    js_funcs = [js_funcs]
  return JsErrors.JsTry(js_funcs, profile=profile)


def and_(*args):
  """
  Description:
  ------------
  Add a and expression to a JavaScript chain.

  Attributes:
  ----------
  :param args:
  """
  return "(%s)" % ") && (".join([JsUtils.jsConvertData(x, None) for x in args])


def throw(value: Union[primitives.JsDataModel, str]):
  """
  Description:
  ------------
  The throw statement allows you to create a custom error.

  Technically you can throw an exception (throw an error).

  Related Pages:

    https://www.w3schools.com/js/js_errors.asp

  Attributes:
  ----------
  :param Union[primitives.JsDataModel, str] value: The message displayed with the exception.
  """
  return JsObjects.JsObject.JsObject.get("throw %s" % JsUtils.jsConvertData(value, None))


def or_(*args):
  """
  Description:
  ------------
  Add a Or expression to a JavaScript chain.

  Attributes:
  ----------
  :param args:
  """
  return "(%s)" % ") || (".join([JsUtils.jsConvertData(x, None) for x in args])


break_ = JsObjects.JsObject.JsObject.get("break")


continue_ = JsObjects.JsObject.JsObject.get("continue")
