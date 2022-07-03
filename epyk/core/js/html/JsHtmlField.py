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
    """
    Description:
    -----------
    Get the user defined values for the component in a dictionary.
    """
    return JsObjects.JsObjects.get(
      '''{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), name: %s, selected: %s}}
        ''' % (self.htmlCode, self.content.toStr(), self.getAttribute('name'), self.selected.toStr()))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """
    Description:
    -----------
    Get the user defined value for the component.
    """
    return JsHtml.ContentFormatters(self.page, "%s.checked" % self.component.input.dom.varName)

  @property
  def selected(self) -> JsHtml.ContentFormatters:
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(
      self.page, "document.body.querySelector('input[name='+%s+']:checked').getAttribute('data-content')" % self.component.input.dom.getAttribute('name'))


class Check(JsHtml.JsHtmlRich):

  @property
  def val(self) -> JsObjects.JsObjects:
    """
    Description:
    -----------
    Get the user defined values for the component in a dictionary.
    """
    return JsObjects.JsObjects.get('''{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), 
name: %s}}''' % (self.htmlCode, self.content.toStr(), self.getAttribute('name')))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """
    Description:
    -----------
    Get the user defined value for the component.
    """
    return JsHtml.ContentFormatters(self.page, "%s.checked" % self.varName)


class InputText(JsHtml.JsHtmlRich):

  def isEmpty(self, js_funcs: types.JS_FUNCS_TYPES):
    """
    Description:
    ------------
    Trigger an event when the input content is emtpy.

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return JsIf.JsIf('%s === ""' % self.component.dom.content.toStr(), js_funcs)

  def hasLength(self, n: int, js_funcs: types.JS_FUNCS_TYPES):
    """
    Description:
    ------------
    Trigger an action only when the length of the input content is above a threshold.

    Attributes:
    ----------
    :param n: The minimum length of the input content.
    :param js_funcs: Javascript functions.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return JsIf.JsIf('%s.length >= %s' % (self.component.dom.content.toStr(), n), js_funcs)

  def if_(self, rule: str, js_funcs: types.JS_FUNCS_TYPES):
    """
    Description:
    ------------
    Generic if statement for an input component.

    Attributes:
    ----------
    :param rule: The javascript expression used as rule
    :param js_funcs: Javascript functions.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return JsIf.JsIf(rule, js_funcs)

  @packages.packageImport('jqueryui', 'jqueryui')
  def autocomplete(self, values: list, options: dict = None):
    """
    Description:
    ------------
    Change the input component to a Jquery autocomplete component.

    Usage::

      input = page.ui.inputs.input("test autocomplete")
      input.js.autocomplete(["AAAAA", "AAABBB", "AAACCC"])

    Related Pages:

      https://jqueryui.com/autocomplete/

    Attributes:
    ----------
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
    Description:
    -----------

    """
    return self.component.input.dom.val

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return self.component.input.dom.content

  def empty(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get('%s = ""' % self.content.toStr())


class Textarea(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(self.page, "%s.value" % self.varName)

  def readonly(self):
    """
    Description:
    -----------

    """
    return "%s.readOnly = true" % self.varName
