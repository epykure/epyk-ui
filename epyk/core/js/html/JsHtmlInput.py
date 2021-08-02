#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class Inputs(JsHtml.JsHtml):

  def autocomplete(self, jsData=None):
    """
    Description:
    ------------
    Sets or returns the value of the autocomplete attribute of a text field.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_autocomplete.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    """
    if jsData is None:
      return JsObjects.JsString.JsString.get("%s.autocomplete" % self._src.dom.varName)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsUtils.jsWrap("%s.autocomplete = %s" % (self._src.dom.varName, jsData))

  def autofocus(self, jsData=None):
    """
    Description:
    ------------
    Sets or returns whether a text field should automatically get focus when the page loads.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_autofocus.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    """
    if jsData is None:
      return JsObjects.JsString.JsString.get("%s.autofocus" % self._src.dom.varName)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsUtils.jsWrap("%s.autofocus = %s" % (self._src.dom.varName, jsData))

  def defaultValue(self, jsData=None):
    """
    Description:
    ------------
    Sets or returns the default value of a text field.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_defaultvalue.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    """
    if jsData is None:
      return JsObjects.JsString.JsString.get("%s.defaultValue" % self._src.dom.varName)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsUtils.jsWrap("%s.defaultValue = %s" % (self._src.dom.varName, jsData))

  def disabled(self, jsData=None):
    """
    Description:
    ------------
    Sets or returns whether the text field is disabled, or not.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_disabled.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    """
    if jsData is None:
      return JsObjects.JsString.JsString.get("%s.disabled" % self._src.dom.varName)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsUtils.jsWrap("%s.disabled = %s" % (self._src.dom.varName, jsData))

  def maxLength(self, jsData=None):
    """
    Description:
    ------------
    Sets or returns the value of the maxlength attribute of a text field.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_maxlength.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    """
    if jsData is None:
      return JsObjects.JsString.JsString.get("%s.maxLength" % self._src.dom.varName)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsUtils.jsWrap("%s.maxLength = %s" % (self._src.dom.varName, jsData))

  def pattern(self, jsData=None):
    """
    Description:
    ------------
    Sets or returns the value of the pattern attribute of a text field.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_pattern.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    """
    if jsData is None:
      return JsObjects.JsString.JsString.get("%s.pattern" % self._src.dom.varName)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsUtils.jsWrap("%s.pattern = %s" % (self._src.dom.varName, jsData))

  def placeholder(self, jsData=None):
    """
    Description:
    ------------
    Set or get the placeholder for an HTML component.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_placeholder.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    """
    if jsData is None:
      return JsObjects.JsString.JsString.get("%s.placeholder" % self._src.dom.varName)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsUtils.jsWrap("%s.placeholder = %s" % (self._src.dom.varName, jsData))

  def readOnly(self, jsData=None):
    """
    Description:
    ------------
    Sets or returns whether a text field is read-only, or not.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_readonly.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    """
    if jsData is None:
      return JsObjects.JsString.JsString.get("%s.readOnly" % self._src.dom.varName)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsUtils.jsWrap("%s.readOnly = %s" % (self._src.dom.varName, jsData))

  def required(self, jsData=None):
    """
    Description:
    ------------
    Sets or returns whether the text field must be filled out before submitting a form.

    Related Pages:

      https://www.w3schools.com/jsref/prop_text_required.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    """
    if jsData is None:
      return JsObjects.JsString.JsString.get("%s.required" % self._src.dom.varName)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsUtils.jsWrap("%s.required = %s" % (self._src.dom.varName, jsData))

  def size(self, jsData=None):
    """
    Description:
    ------------
    Sets or returns the value of the size attribute of a text field.

    Related Pages:

      https://www.w3schools.com/jsref/prop_text_size.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    """
    if jsData is None:
      return JsObjects.JsString.JsString.get("%s.size" % self._src.dom.varName)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsUtils.jsWrap("%s.size = %s" % (self._src.dom.varName, jsData))

  def name(self, jsData=None):
    """
    Description:
    ------------
    Set or get the placeholder for an HTML component.

    Related Pages:

      https://www.w3schools.com/jsref/prop_text_name.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    """
    if jsData is None:
      return JsObjects.JsString.JsString.get("%s.name" % self._src.dom.varName)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsUtils.jsWrap("%s.name = %s" % (self._src.dom.varName, jsData))
