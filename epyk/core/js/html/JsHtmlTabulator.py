#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects


class JsHtmlTabulator(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    -----------
    Return a Javascript val object
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlCode, self.content.toStr()))

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(self._report, "%s.getData()" % self._src.tableId)
