#!/usr/bin/env python
# -*- coding: utf-8 -*-


from epyk.core.js import JsUtils


class JsIf(object):
  """

  """

  def __init__(self, jsCondition, jsFncs, context=None):
    """

    :param jsCondition:
    :param jsFncs:
    :param context:
    """
    self._context = context
    jsFncs = JsUtils.jsConvertFncs(jsFncs, False)
    self._js = [(jsCondition, jsFncs)]
    self.__jsElse = None

  def elif_(self, jsCondition, jsFncs):
    """

    :param jsCondition:
    :param jsFncs:
    :return:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, False)
    self._js.append((jsCondition, jsFncs))
    return self

  def else_(self, jsFncs):
    """

    :param jsFncs:
    :return:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, False)
    self.__jsElse = jsFncs
    return self

  def toStr(self):
    """

    :return:
    """
    strData = ["if(%s){%s}" % (self._js[0][0], ";".join(map(lambda x: str(x),  self._js[0][1])))]
    for condition, fncs in self._js[1:]:
      strData.append("else if(%s){%s}" % (condition, ";".join(fncs)))
    if self.__jsElse is not None:
      strData.append("else{%s}" % ";".join(map(lambda x: str(x),  self.__jsElse)))
    self._js, self.__jsElse = [], None # empty the stack
    return "".join(strData)
