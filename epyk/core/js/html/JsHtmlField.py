#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import primitives

from epyk.core.js.html import JsHtml

from epyk.core.js.primitives import JsObjects
from epyk.core.js.statements import JsIf


class Radio(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get(
      '''{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), name: %s, selected: %s}}
        ''' % (self.htmlCode, self.content.toStr(), self.getAttribute('name'), self.selected.toStr()))

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(self.page, "%s.checked" % self.component.input.dom.varName)

  @property
  def selected(self):
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(
      self.page, "document.body.querySelector('input[name='+%s+']:checked').getAttribute('data-content')" % self.component.input.dom.getAttribute('name'))


class Check(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get('''{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), 
name: %s}}''' % (self.htmlCode, self.content.toStr(), self.getAttribute('name')))

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(self.page, "%s.checked" % self.varName)


class InputText(JsHtml.JsHtmlRich):

  def isEmpty(self, js_funcs: Union[str, list]):
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

  def hasLength(self, n: int, js_funcs: Union[str, list]):
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

  def if_(self, rule: str, js_funcs: Union[str, list]):
    """
    Description:
    ------------
    Generic if statement for an input component.

    Attributes:
    ----------
    :param rule:
    :param js_funcs: Javascript functions.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return JsIf.JsIf(rule, js_funcs)


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
    return "%s.readOnly = true" % self.varName
