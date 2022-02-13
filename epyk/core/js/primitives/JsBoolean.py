#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional
from epyk.core.py import primitives

import json

from epyk.core.js.primitives import JsObject


class JsBoolean(JsObject.JsObject):
  _jsClass = "Boolean"

  def __init__(self, data, js_code: Optional[str] = None, set_var: bool = False, is_py_data: bool = True,
               page: Optional[primitives.PageModel] = None, component: primitives.HtmlModel = None):
    if not hasattr(data, 'varName') and is_py_data:
      is_py_data = True
      data = json.dumps(data)
    super(JsBoolean, self).__init__(data, js_code, set_var, is_py_data, page=page, component=component)

  @property
  def not_(self):
    """
    Description:
    -----------
    Add the Symbol (!) for the boolean negation.
    This feature is also available directly to the JsObj

    Usage::

      jsObj.objects.boolean.get("weekend").not_

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Op%C3%A9rateurs/Op%C3%A9rateurs_logiques

    :return: The Python Javascript Boolean Object
    """
    self.varName = "!%s" % self.varId
    return self

  def valueOf(self):
    """
    Description:
    -----------
    The valueOf() method returns the primitive value of a boolean.

    Usage::

      jsObj.objects.boolean.new(False, "testBool")
      jsObj.objects.boolean.get("testBool").valueOf()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_valueof_boolean.asp

    :return: A Boolean, either "true" or "false"
    """
    return JsBoolean("%s.valueOf()" % self.varId, is_py_data=False)
