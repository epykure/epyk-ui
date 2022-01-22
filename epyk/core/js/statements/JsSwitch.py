#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class JsSwitch:
  """
  Description:
  ------------

  Documentation:
    - https://www.w3schools.com/js/js_switch.asp

  """

  def __init__(self, variable: str, profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param str variable: the variable name.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self.__selector = variable
    self.__js, self.__default = [], None
    self.profile = profile

  def case(self, value, js_funcs: Union[list, str], strict: bool = False, profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value: Object. The pivot value.
    :param Union[list, str] js_funcs: The JavaScript functions.
    :param bool strict:
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if strict:
      self.__js.append((JsObjects.JsVoid("(%s === %s)" % (self.__selector, value)), js_funcs))
    else:
      self.__js.append((JsObjects.JsVoid("(%s == %s)" % (self.__selector, value)), js_funcs))
    self.profile = profile
    return self

  def caseRange(self, min: Union[int, primitives.JsDataModel], max: Union[int, primitives.JsDataModel],
                js_funcs: Union[list, str], include_value: bool = True):
    """
    Description:
    ------------
    Range case. The value should be within the range [min, max].

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] max: The min value for this range.
    :param Union[int, primitives.JsDataModel] min: The max value for this range.
    :param Union[list, str] js_funcs: The JavaScript functions.
    :param bool include_value: Optional. To specify if the pivot value is included.
    """
    max = JsUtils.jsConvertData(max, None)
    min = JsUtils.jsConvertData(min, None)
    if include_value:
      self.__js.append((JsObjects.JsVoid(
        "(%s <= %s) && (%s <= %s)" % (min, self.__selector, self.__selector, max)), js_funcs))
    else:
      self.__js.append((JsObjects.JsVoid(
        "(%s < %s) && (%s < %s)" % (min, self.__selector, self.__selector, max)), js_funcs))
    return self

  def caseBelow(self, value: Union[int, primitives.JsDataModel], js_funcs: Union[list, str],
                include_value: bool = True):
    """
    Description:
    ------------
    Below case. The switch value should be below the value.

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] value: Number. The pivot value.
    :param Union[list, str] js_funcs: The JavaScript functions.
    :param bool include_value: Optional. To specify if the pivot value is included.
    """
    value = JsUtils.jsConvertData(value, None)
    if include_value:
      self.__js.append((JsObjects.JsVoid("(%s <= %s)" % (self.__selector, value)), js_funcs))
    else:
      self.__js.append((JsObjects.JsVoid("(%s < %s)" % (self.__selector, value)), js_funcs))
    return self

  def caseAbove(self, value: Union[int, primitives.JsDataModel], js_funcs: Union[list, str],
                include_value: bool = True):
    """
    Description:
    ------------
    Above case. The switch value should be above the value.

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] value: The pivot value.
    :param Union[list, str] js_funcs: The JavaScript functions.
    :param bool include_value: Optional. To specify if the pivot value is included.
    """
    value = JsUtils.jsConvertData(value, None)
    if include_value:
      self.__js.append((JsObjects.JsVoid("(%s >= %s)" % (self.__selector, value)), js_funcs))
    else:
      self.__js.append((JsObjects.JsVoid("(%s > %s)" % (self.__selector, value)), js_funcs))
    return self

  def default_(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    Default case value

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript functions.
    """
    self.__default = js_funcs
    return self

  def toStr(self):
    str_data = []
    for var, js_funcs in self.__js:
      str_data.append("case %s: {%s; break}" % (
        JsUtils.jsConvertData(var, None), JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=self.profile)))
    if self.__default is not None:
      str_data.append("default: {%s}" % JsUtils.jsConvertFncs(self.__default, toStr=True, profile=self.profile))
    # empty the stack
    self.__js_funcs, self.__default = [], None
    return "switch (true){%s}" % ("".join(str_data))

  def __str__(self):
    return self.toStr()
