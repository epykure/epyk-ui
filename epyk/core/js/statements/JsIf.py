#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils
from epyk.core.py import types
from typing import Optional
from epyk.core.py import primitives


class JsIf:

  def __init__(self, condition: str, js_funcs: types.JS_FUNCS_TYPES, context: Optional[primitives.PageModel] = None,
               profile: types.PROFILE_TYPE = False):
    """
    Create a JavaScript If statement.

    Usage::

      JsIf.JsIf(self.input.dom.hasClass("fa-check"), jsFncsTrue)
 
    :param condition: The Javascript condition. Can be a JsBoolean object.
    :param js_funcs: Optional. The Javascript functions.
    :param context: Optional. Metadata concerning the context.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    self._context = context
    js_funcs = JsUtils.jsConvertFncs(js_funcs, False, profile=profile)
    if hasattr(condition, "toStr"):
      condition = condition.toStr()
    self._js = [(condition, js_funcs)]
    self.__js_else = None

  def elif_(self, condition: str, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """
    Add a Javascript elif statement to the loop.
 
    :param condition: The Javascript condition. Can be a JsBoolean object.
    :param js_funcs: The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.

    :return: The If object to allow the chaining.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, False, profile=profile)
    self._js.append((condition, js_funcs))
    return self

  def else_(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """
    Add the Javascript else statement to the loop.

    Usage::

      JsIf.JsIf(self.input.dom.hasClass("fa-check"), jsFncsTrue).else_(jsFncFalse)
 
    :param js_funcs: The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.

    :return: The If object to allow the chaining.
    """
    self.__js_else = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def toStr(self):
    str_data = ["if(%s){%s}" % (self._js[0][0], ";".join(map(lambda x: str(x),  self._js[0][1])))]
    for condition, funcs in self._js[1:]:
      str_data.append("else if(%s){%s}" % (condition, ";".join(funcs)))
    if self.__js_else is not None:
      str_data.append("else {%s}" % self.__js_else)
    # empty the stack
    self._js, self.__js_else = [], None
    return "".join(str_data)
