#!/usr/bin/python
# -*- coding: utf-8 -*-

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
    return JsObjects.JsObjects.get('''{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), name: %s, selected: %s}}
        ''' % (self.htmlCode, self.content.toStr(), self.getAttribute('name'), self.selected.toStr()))

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(self._report, "%s.checked" % self._src.input.dom.varName)

  @property
  def selected(self):
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(self._report, "document.body.querySelector('input[name='+%s+']:checked').getAttribute('data-content')" % self._src.input.dom.getAttribute('name'))


class Check(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get('''{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), name: %s}}
        ''' % (self.htmlCode, self.content.toStr(), self.getAttribute('name')))

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(self._report, "%s.checked" % self.varName)


class InputText:

  def __init__(self, component, page):
    self._component = component
    self._page = page

  def isEmpty(self, jsFncs):
    """
    Description:
    ------------
    Trigger an event when the input content is emtpy.

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return JsIf.JsIf('%s === ""' % self._component.dom.content.toStr(), jsFncs)

  def hasLength(self, n, jsFncs):
    """
    Description:
    ------------
    Trigger an action only when the length of the input content is above a threshold.

    Attributes:
    ----------
    :param n: Integer. The minimum length of the input content.
    :param jsFncs: List | String. Javascript functions.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return JsIf.JsIf('%s.length >= %s' % (self._component.dom.content.toStr(), n), jsFncs)

  def if_(self, jsRule, jsFncs):
    """
    Description:
    ------------
    Generic if statement for an input component.

    Attributes:
    ----------
    :param jsRule: String.
    :param jsFncs: List | String. Javascript functions.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return JsIf.JsIf(jsRule, jsFncs)


class JsHtmlFields(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    -----------

    """
    return self._src.input.dom.val

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return self._src.input.dom.content

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
    return JsHtml.ContentFormatters(self._report, "%s.value" % self.varName)
