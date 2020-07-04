#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Module dedicated to wrap the Javascript Boolean

Related Pages:

		https://www.w3schools.com/jsref/jsref_valueof_boolean.asp
"""

import json

from epyk.core.js.primitives import JsObject


class JsBoolean(JsObject.JsObject):
  _jsClass = "Boolean"

  def __init__(self, data, varName=None, setVar=False, isPyData=True, report=None):
    if not hasattr(data, 'varName') and isPyData:
      isPyData = True
      data = json.dumps(data)
    super(JsBoolean, self).__init__(data, varName, setVar, isPyData, report)

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

:
    https://www.w3schools.com/jsref/jsref_valueof_boolean.asp

    :return: A Boolean, either "true" or "false"
    """
    return JsBoolean("%s.valueOf()" % self.varId, isPyData=False)
