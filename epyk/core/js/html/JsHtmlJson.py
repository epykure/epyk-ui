#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml


class JsonFormatter(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    ------------
    The Javascript value of the component. This returned only a value corresponding to the state of the component.

    Usage::
    """
    return JsHtml.ContentFormatters(self._report, "JSON.stringify(%s.json)" % self._src.jsonId)

