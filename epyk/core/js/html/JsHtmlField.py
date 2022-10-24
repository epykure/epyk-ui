#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import types
from epyk.core.js.packages import JsQuery

from epyk.core.js.html import JsHtml

from epyk.core.js import packages
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.statements import JsIf


class Radio(JsHtml.JsHtmlRich):

  @property
  def val(self) -> JsObjects.JsObjects:
    """   Get the user defined values for the component in a dictionary.
    """
    return JsObjects.JsObjects.get(
      '''{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), name: %s, selected: %s}}
        ''' % (self.htmlCode, self.content.toStr(), self.getAttribute('name'), self.selected.toStr()))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """   Get the user defined value for the component.
    """
    return JsHtml.ContentFormatters(self.page, "%s.checked" % self.component.input.dom.varName)

  @property
  def selected(self) -> JsHtml.ContentFormatters:
    """   

    """
    return JsHtml.ContentFormatters(
      self.page, "document.body.querySelector('input[name='+%s+']:checked').getAttribute('data-content')" % self.component.input.dom.getAttribute('name'))


class Check(JsHtml.JsHtmlRich):

  @property
  def val(self) -> JsObjects.JsObjects:
    """   Get the user defined values for the component in a dictionary.
    """
    return JsObjects.JsObjects.get('''{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), 
name: %s}}''' % (self.htmlCode, self.content.toStr(), self.getAttribute('name')))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """   Get the user defined value for the component.
    """
    return JsHtml.ContentFormatters(self.page, "%s.checked" % self.varName)


class InputText(JsHtml.JsHtmlRich):

  def isEmpty(self, js_funcs: types.JS_FUNCS_TYPES):
    """
    Trigger an event when the input content is emtpy.

    :param js_funcs: Javascript functions.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return JsIf.JsIf('%s === ""' % self.component.dom.content.toStr(), js_funcs)

  def hasLength(self, n: int, js_funcs: types.JS_FUNCS_TYPES):
    """
    Trigger an action only when the length of the input content is above a threshold.

    :param n: The minimum length of the input content.
    :param js_funcs: Javascript functions.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return JsIf.JsIf('%s.length >= %s' % (self.component.dom.content.toStr(), n), js_funcs)

  def if_(self, rule: str, js_funcs: types.JS_FUNCS_TYPES):
    """
    Generic if statement for an input component.

    :param rule: The javascript expression used as rule
    :param js_funcs: Javascript functions.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return JsIf.JsIf(rule, js_funcs)

  @packages.packageImport('jqueryui', 'jqueryui')
  def autocomplete(self, values: list, options: dict = None):
    """
    Change the input component to a Jquery autocomplete component.

    Usage::

      input = page.ui.inputs.input("test autocomplete")
      input.js.autocomplete(["AAAAA", "AAABBB", "AAACCC"])

    Related Pages:

      https://jqueryui.com/autocomplete/

    :param values: The list of values to be added to the component
    :param options: The extra properties for this autocomplete module
    """
    if self.component.attr["type"] != "text":
      raise ValueError("Autocomplete can only be used with input text components")

    values = JsUtils.jsConvertData(values, None)
    options = options or {}
    return JsUtils.jsWrap('''
%s.autocomplete(Object.assign({source: %s}, %s))
''' % (JsQuery.decorate_var(self.varId, convert_var=False), values, options))


class JsHtmlFields(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """   

    """
    return self.component.input.dom.val

  @property
  def content(self):
    """   

    """
    return self.component.input.dom.content

  def empty(self):
    """   

    """
    return JsObjects.JsObjects.get('%s = ""' % self.content.toStr())


class Textarea(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """   

    """
    return JsHtml.ContentFormatters(self.page, "%s.value" % self.varName)

  def isEmpty(self, js_funcs: types.JS_FUNCS_TYPES):
    """
    Trigger an event when the textarea content is emtpy.

    :param js_funcs: Javascript functions.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return JsIf.JsIf('%s === ""' % self.component.dom.content.toStr(), js_funcs)

  def disabled(self, data: types.JS_DATA_TYPES = None):
    """
    Sets or returns whether the text field is disabled, or not.

    Usages::

      auto_srv = page.ui.textarea()
      btn.click([
        auto_srv.dom.disabled(True)
      ])

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_disabled.asp

    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.disabled" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.disabled = %s" % (self.component.dom.varName, data))

  def placeholder(self, data: types.JS_DATA_TYPES = None):
    """
    Set or get the placeholder for an HTML component.

    Usages::

      auto_srv = page.ui.textarea()
      btn.click([
        auto_srv.dom.placeholder("Test")
      ])

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_placeholder.asp

    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.placeholder" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.placeholder = %s" % (self.component.dom.varName, data))

  def readOnly(self, data: types.JS_DATA_TYPES = None):
    """
    Sets or returns whether a text field is read-only, or not.

    Usages::

      auto_srv = page.ui.textarea()
      btn.click([
        auto_srv.dom.readOnly(True)
      ])

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_readonly.asp

    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.readOnly" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.readOnly = %s" % (self.component.dom.varName, data))

  def required(self, data: types.JS_DATA_TYPES = None):
    """
    Sets or returns whether the text field must be filled out before submitting a form.

    Related Pages:

      https://www.w3schools.com/jsref/prop_text_required.asp

    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.required" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.required = %s" % (self.component.dom.varName, data))

  def autofocus(self, data: types.JS_DATA_TYPES = None):
    """
    Sets or returns whether a text field should automatically get focus when the page loads.

    Related Pages:

        https://www.w3schools.com/jsref/prop_text_autofocus.asp

    :param data: A String corresponding to a JavaScript object.
    """
    if data is None:
      return JsObjects.JsString.JsString.get("%s.autofocus" % self.component.dom.varName)

    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.autofocus = %s" % (self.component.dom.varName, data))

  def empty(self):
    """ Empty the content of the HTML component using the innerHTML JavaScript property.
    """
    return JsUtils.jsWrap('%s.value = ""' % self.varName)
