#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject


class JsWhile:

  def __init__(self, jsPivot, options=None, context=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsPivot:
    :param options:
    :param context:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._context = context
    self.options = {"var": 'i'}
    if options is not None:
      self.options.update(options)
    self.__jsFncs, self.__next = [], None
    self.__pivot = jsPivot
    self.profile = profile

  def next(self, rule):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param rule:
    """
    self.__next = rule
    return self

  def fncs(self, jsFncs, reset=True, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param reset:
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if reset:
      self.__jsFncs = jsFncs
    else:
      self.__jsFncs.extend(jsFncs)
    self.profile = profile
    return self

  def toStr(self):
    if self.__next is None:
      raise Exception("next() function must be used to avoid infinite loops !!")

    fncs = JsUtils.jsConvertFncs(self.__jsFncs, toStr=True, profile=self.profile)
    return "while(%s){%s; %s}" % (self.__pivot, fncs, self.__next)


class JsWhileIterable:

  def __init__(self, jsIterable, options=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsIterable:
    :param options: Dictionary. Optional. While options.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self.__js_it = jsIterable
    self.options = {"var": 'x'}
    if options is not None:
      self.options.update(options)
    self.options['it'] = JsUtils.jsConvertData(self.__js_it, None)
    self.profile = profile

  @property
  def var(self):
    """
    Description:
    -----------
`   Return the variable reference for this loop.
    """
    return self.options['var']

  @var.setter
  def var(self, value):
    """
    Description:
    -----------
`   Return the variable reference for this loop.

    Attributes:
    ----------
    :param value: String. The value reference for the JavaScript variable.
    """
    self.options['var'] = value

  @property
  def value(self):
    """
    Description:
    -----------
    return the value during the while loop
    """
    return JsObject.JsObject.get("%(it)s[%(var)s]" % self.options)

  def fncs(self, jsFncs, reset=True, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs: Array. The PyJs functions.
    :param reset: Boolean. Optional. Reset the JavaScript functions for this loop.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if reset:
      self.__jsFncs = jsFncs
    else:
      self.__jsFncs.extend(jsFncs)
    self.profile = profile
    return self

  def toStr(self):
    self.options['jsFncs'] = JsUtils.jsConvertFncs(self.__jsFncs, toStr=True, profile=self.profile)
    return "var %(var)s = 0; while(%(it)s[%(var)s]){%(jsFncs)s; %(var)s++}" % self.options
