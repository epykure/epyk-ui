#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils
from typing import Union, Optional
from epyk.core.py import primitives


class JsIf:

  def __init__(self, condition: str, js_funcs: Union[list, str], context: Optional[primitives.PageModel] = None,
               profile: Optional[Union[dict, bool]] = False):
    """
    Description:
    ------------
    Create a JavaScript If statement.

    Usage::

      JsIf.JsIf(self.input.dom.hasClass("fa-check"), jsFncsTrue)

    Attributes:
    ----------
    :param str condition: The Javascript condition. Can be a JsBoolean object.
    :param Union[list, str] js_funcs: Optional. The Javascript functions.
    :param Optional[primitives.PageModel] context: Optional. Meta data concerning the context.
    :param Optional[Union[dict, bool]] profile: Boolean. Optional. A flag to set the component performance storage.
    """
    self._context = context
    js_funcs = JsUtils.jsConvertFncs(js_funcs, False, profile=profile)
    if hasattr(condition, "toStr"):
      condition = condition.toStr()
    self._js = [(condition, js_funcs)]
    self.__jsElse = None

  def elif_(self, condition: str, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Add a Javascript elif statement to the loop.

    Attributes:
    ----------
    :param str condition: The Javascript condition. Can be a JsBoolean object.
    :param Union[list, str] js_funcs: The Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.

    :return: The If object to allow the chaining.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, False, profile=profile)
    self._js.append((condition, js_funcs))
    return self

  def else_(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Add the Javascript else statement to the loop.

    Usage::

      JsIf.JsIf(self.input.dom.hasClass("fa-check"), jsFncsTrue).else_(jsFncFalse)

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.

    :return: The If object to allow the chaining.
    """
    self.__jsElse = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def toStr(self):
    str_data = ["if(%s){%s}" % (self._js[0][0], ";".join(map(lambda x: str(x),  self._js[0][1])))]
    for condition, funcs in self._js[1:]:
      str_data.append("else if(%s){%s}" % (condition, ";".join(funcs)))
    if self.__jsElse is not None:
      str_data.append("else {%s}" % self.__jsElse)
    # empty the stack
    self._js, self.__jsElse = [], None
    return "".join(str_data)
