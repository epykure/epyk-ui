#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml


class JsonFormatter(JsHtml.JsHtmlRich):

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """  
    The Javascript value of the component. This returned only a value corresponding to the state of the component.
    """
    return JsHtml.ContentFormatters(self.page, "JSON.stringify(%s.json)" % self.component.jsonId)

