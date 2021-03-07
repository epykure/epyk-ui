#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.js import Js
from epyk.core.js import JsUtils


class JsCookies:
  class __internal(object):
    _context = {}

  def __init__(self, src=None):
    self.src = src if src is not None else self.__internal()

  def set(self, jsKey, jsData, jsDataKey=None, isPyData=True, jsFnc=None):
    """
    Description:
    ------------

    Related Pages:

      https//www.w3schools.com/js/js_cookies.asp

    Attributes:
    ----------
    :param jsKey:
    :param jsData:
    :param jsDataKey:
    :param isPyData:
    :param jsFnc:
    """
    jsData = JsUtils.jsConvert(jsData, jsDataKey, isPyData, jsFnc)
    if self.src._context.get('cookies') is None:
      self.src._context['cookies'] = True
      return "document.cookies = {'%s': %s}" % (jsKey, jsData)

    return "document.cookies['%s'] = %s" % (jsKey, jsData)

  def get(self, jsData=None, jsConvFnc=True, jsResultFnc=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    :param jsResultFnc: Optional. A function used to transform the result.
    """
    if jsData is None:
      return Js.JsJson().parse("decodeURIComponent(document.cookies)", jsResultFnc=jsResultFnc)

    jsData = JsUtils.jsConvertData(jsData, jsConvFnc)
    return Js.JsJson().parse("decodeURIComponent(document.cookies)['%s']" % jsData, jsResultFnc=jsResultFnc)
