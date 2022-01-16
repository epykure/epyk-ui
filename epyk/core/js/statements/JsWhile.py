#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject


class JsWhile:

  def __init__(self, pivot: str, options: Optional[dict] = None, context=None,
               profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    -----------
    Create a JavaScript while statement.

    Attributes:
    ----------
    :param str pivot: The JavaScript expression.
    :param Optional[dict] options:
    :param context:
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self._context = context
    self.options = {"var": 'i'}
    if options is not None:
      self.options.update(options)
    self.__js_funcs, self.__next = [], None
    self.__pivot = pivot
    self.profile = profile

  def next(self, rule: str):
    """
    Description:
    -----------
    Set the way the while will increment the cursor.

    Attributes:
    ----------
    :param str rule: The JavaScript fragment for the next statement,
    """
    self.__next = rule
    return self

  def fncs(self, js_funcs: Union[list, str], reset: bool = True, profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    -----------
    Set the functions, event to be trigger during the while loop.

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param bool reset: Reset the defined javascript functions or append to them.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    if reset:
      self.__js_funcs = js_funcs
    else:
      self.__js_funcs.extend(js_funcs)
    self.profile = profile
    return self

  def toStr(self):
    if self.__next is None:
      raise ValueError("next() function must be used to avoid infinite loops !!")

    funcs = JsUtils.jsConvertFncs(self.__js_funcs, toStr=True, profile=self.profile)
    return "while(%s){%s; %s}" % (self.__pivot, funcs, self.__next)


class JsWhileIterable:

  def __init__(self, iterable, options: Optional[dict] = None, profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param iterable:
    :param Optional[dict] options: Optional. While options.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self.__js_it = iterable
    self.options = {"var": 'x'}
    if options is not None:
      self.options.update(options)
    self.options['it'] = JsUtils.jsConvertData(self.__js_it, None)
    self.profile = profile

  @property
  def var(self) -> str:
    """
    Description:
    -----------
`   Return the variable reference for this loop.
    """
    return self.options['var']

  @var.setter
  def var(self, value: str):
    """
    Description:
    -----------
`   Return the variable reference for this loop.

    Attributes:
    ----------
    :param str value: The value reference for the JavaScript variable.
    """
    self.options['var'] = value

  @property
  def value(self):
    """
    Description:
    -----------
    return the value during the while loop.
    """
    return JsObject.JsObject.get("%(it)s[%(var)s]" % self.options)

  def fncs(self, js_funcs: Union[list, str], reset: bool = True, profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The PyJs functions.
    :param bool reset: Optional. Reset the JavaScript functions for this loop.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    if reset:
      self.__js_funcs = js_funcs
    else:
      self.__js_funcs.extend(js_funcs)
    self.profile = profile
    return self

  def toStr(self):
    self.options['jsFncs'] = JsUtils.jsConvertFncs(self.__js_funcs, toStr=True, profile=self.profile)
    return "var %(var)s = 0; while(%(it)s[%(var)s]){%(jsFncs)s; %(var)s++}" % self.options
