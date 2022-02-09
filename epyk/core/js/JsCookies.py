#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.js import Js
from epyk.core.js import JsUtils


class JsCookies:

  def __init__(self, src: Optional[primitives.PageModel]):
    self.page = src

  def set(self, key: str, data, data_key: str = None, python_data=True, js_funcs: Optional[Union[list, str]] = None):
    """
    Description:
    ------------

    Related Pages:

      https//www.w3schools.com/js/js_cookies.asp

    Attributes:
    ----------
    :param key:
    :param data:
    :param data_key:
    :param python_data:
    :param Optional[Union[list, str]] js_funcs: The Javascript functions.
    """
    data = JsUtils.jsConvert(data, data_key, python_data, js_funcs)
    if self.page._context.get('cookies') is None:
      self.page._context['cookies'] = True
      return "document.cookies = {'%s': %s}" % (key, data)

    return "document.cookies['%s'] = %s" % (key, data)

  def get(self, data: Union[str, primitives.JsDataModel] = None, js_conv_func: Optional[Union[str, list]] = True,
          js_result_func: Optional[str] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] data: Optional. A String corresponding to a JavaScript object.
    :param Optional[Union[str, list]] js_conv_func: Optional. A specific JavaScript data conversion function.
    :param Optional[str] js_result_func: Optional. A function used to transform the result.
    """
    if data is None:
      return Js.JsJson().parse("decodeURIComponent(document.cookies)", js_result_func=js_result_func)

    data = JsUtils.jsConvertData(data, js_conv_func)
    return Js.JsJson().parse("decodeURIComponent(document.cookies)['%s']" % data, js_result_func=js_result_func)
