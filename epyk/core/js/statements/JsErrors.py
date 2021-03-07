#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class JsError:

  def __init__(self, val):
    self.__selector = val

  @property
  def message(self):
    """
    Description:
    ------------
    Sets or returns an error message (a string).
    """
    return JsObjects.JsObject.JsObject.get("%s.message" % self.__selector)

  @property
  def name(self):
    """
    Description:
    ------------
    Sets or returns an error name.
    """
    return JsObjects.JsObject.JsObject.get("%s.name" % self.__selector)

  def toStr(self):
    return JsObjects.JsObject.JsObject.get(self.__selector)

  def __str__(self):
    return self.__selector


class JsTry:

  def __init__(self, jsFncs, profile=False):
    self.__try_jsFnc = jsFncs
    self.__fin_jsFnc = None
    self.__catch_jsFnc = None
    self.profile = profile

  @property
  def error(self):
    """
    Description:
    ------------
    The error message object.
    """
    return JsError("err")

  def catch(self, jsFncs, profile=False):
    """
    Description:
    ------------
    Block of code to handle errors.

    The variable to be used is err in this loop.

    Attributes:
    ----------
    :param jsFncs: List | String. The JavaScript logic.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__catch_jsFnc = jsFncs
    self.profile = profile
    return self

  def except_(self, jsFncs, profile=False):
    """
    Description:
    ------------
    Block of code to handle errors (catch in JavaScript).

    The variable to be used is err in this loop.

    Attributes:
    ----------
    :param jsFncs: List | String. The JavaScript logic.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__catch_jsFnc = jsFncs
    self.profile = profile
    return self

  def finally_(self, jsFncs, profile=False):
    """
    Description:
    ------------
    Block of code to be executed regardless of the try / catch result.

    Attributes:
    ----------
    :param jsFncs: List | String. The JavaScript logic.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__fin_jsFnc = jsFncs
    self.profile = profile
    return self

  def toStr(self):
    a = JsUtils.jsConvertFncs(self.__try_jsFnc, toStr=True, profile=self.profile)
    if self.__catch_jsFnc is None:
      raise Exception("Catch must be defined")

    b = JsUtils.jsConvertFncs(self.__catch_jsFnc, toStr=True, profile=self.profile)
    if self.__fin_jsFnc is None:
      return "try{%s} catch(%s){%s}" % (a, self.error, b)

    c = JsUtils.jsConvertFncs(self.__fin_jsFnc, toStr=True, profile=self.profile)
    return "try{%s} catch(%s){%s} finally{%s}" % (a, self.error, b, c)

  def __str__(self):
    return self.toStr()
