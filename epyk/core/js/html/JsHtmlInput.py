#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import primitives

from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class Inputs(JsHtml.JsHtml):

  def autocomplete(self, data: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Sets or returns the value of the autocomplete attribute of a text field.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_autocomplete.asp

    Attributes:
    ----------
    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.autocomplete" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.autocomplete = %s" % (self.component.dom.varName, data))

  def autofocus(self, data: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Sets or returns whether a text field should automatically get focus when the page loads.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_autofocus.asp

    Attributes:
    ----------
    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.autofocus" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.autofocus = %s" % (self.component.dom.varName, data))

  def defaultValue(self, data: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Sets or returns the default value of a text field.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_defaultvalue.asp

    Attributes:
    ----------
    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.defaultValue" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.defaultValue = %s" % (self.component.dom.varName, data))

  def disabled(self, data: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Sets or returns whether the text field is disabled, or not.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_disabled.asp

    Attributes:
    ----------
    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.disabled" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.disabled = %s" % (self.component.dom.varName, data))

  def maxLength(self, data: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Sets or returns the value of the maxlength attribute of a text field.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_maxlength.asp

    Attributes:
    ----------
    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.maxLength" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.maxLength = %s" % (self.component.dom.varName, data))

  def pattern(self, data: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Sets or returns the value of the pattern attribute of a text field.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_pattern.asp

    Attributes:
    ----------
    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.pattern" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.pattern = %s" % (self.component.dom.varName, data))

  def placeholder(self, data: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Set or get the placeholder for an HTML component.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_placeholder.asp

    Attributes:
    ----------
    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.placeholder" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.placeholder = %s" % (self.component.dom.varName, data))

  def readOnly(self, data: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Sets or returns whether a text field is read-only, or not.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_readonly.asp

    Attributes:
    ----------
    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.readOnly" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.readOnly = %s" % (self.component.dom.varName, data))

  def required(self, data: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Sets or returns whether the text field must be filled out before submitting a form.

    Related Pages:

      https://www.w3schools.com/jsref/prop_text_required.asp

    Attributes:
    ----------
    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.required" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.required = %s" % (self.component.dom.varName, data))

  def size(self, data: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Sets or returns the value of the size attribute of a text field.

    Related Pages:

      https://www.w3schools.com/jsref/prop_text_size.asp

    Attributes:
    ----------
    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.size" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.size = %s" % (self.component.dom.varName, data))

  def name(self, data: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Set or get the placeholder for an HTML component.

    Related Pages:

      https://www.w3schools.com/jsref/prop_text_name.asp

    Attributes:
    ----------
    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.name" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.name = %s" % (self.component.dom.varName, data))
