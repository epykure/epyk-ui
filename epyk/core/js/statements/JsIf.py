#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils


class JsIf:

  def __init__(self, jsCondition, jsFncs, context=None, profile=False):
    """
    Description:
    ------------
    Create a JavaScript If statement

    Usage:
    -----

      JsIf.JsIf(self.input.dom.hasClass("fa-check"), jsFncsTrue)

    Attributes:
    ----------
    :param jsCondition: String. The Javascript condition. Can be a JsBoolean object.
    :param jsFncs: List | String. Optional. The Javascript functions.
    :param context: Page. Optional. Dictionary. Meta data concerning the context.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    self._context = context
    js_funcs = JsUtils.jsConvertFncs(jsFncs, False, profile=profile)
    self._js = [(jsCondition, js_funcs)]
    self.__jsElse = None

  def elif_(self, jsCondition, jsFncs, profile=False):
    """
    Description:
    ------------
    Add a Javascript elif statement to the loop.

    Usage:
    -----

    Attributes:
    ----------
    :param jsCondition: String. The Javascript condition. Can be a JsBoolean object.
    :param jsFncs: List | String. Optional. The Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.

    :return: The If object to allow the chaining.
    """
    js_funcs = JsUtils.jsConvertFncs(jsFncs, False, profile=profile)
    self._js.append((jsCondition, js_funcs))
    return self

  def else_(self, jsFncs, profile=False):
    """
    Description:
    ------------
    Add the Javascript else statement to the loop.

    Usage::

      JsIf.JsIf(self.input.dom.hasClass("fa-check"), jsFncsTrue).else_(jsFncFalse)

    Attributes:
    ----------
    :param jsFncs: List | String. The Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.

    :return: The If object to allow the chaining.
    """
    js_funcs = JsUtils.jsConvertFncs(jsFncs, False, profile=profile)
    self.__jsElse = js_funcs
    return self

  def toStr(self):
    str_data = ["if(%s){%s}" % (self._js[0][0], ";".join(map(lambda x: str(x),  self._js[0][1])))]
    for condition, funcs in self._js[1:]:
      str_data.append("else if(%s){%s}" % (condition, ";".join(funcs)))
    if self.__jsElse is not None:
      str_data.append("else{%s}" % ";".join(map(lambda x: str(x),  self.__jsElse)))
    # empty the stack
    self._js, self.__jsElse = [], None
    return "".join(str_data)
