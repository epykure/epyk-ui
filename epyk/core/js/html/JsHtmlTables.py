#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives

from epyk.core.js.html import JsHtml
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects


class JsHtmlTabulatorCell(JsHtml.JsHtml):

  def _init__(self, js_code: str, page: primitives.PageModel, component: primitives.HtmlModel = None):
    self.tableId = js_code
    self.js_code = js_code
    self.page = page
    self.component = component

  def getElement(self):
    """
    Description:
    ------------

    """
    return JsNodeDom.JsDoms.get("cell.getElement()")

  def getColumnField(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObject.JsObject.get("cell.getColumn().getField()")

  def getColumnTitle(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObject.JsObject.get("cell.getColumn().getDefinition().title")

  def getValue(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObject.JsObject.get("cell.getValue()")

  def getRow(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObject.JsObject.get("cell.getRow()")

  def getData(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObject.JsObject.get("cell.getRow().getData()")


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
    return JsHtml.ContentFormatters(self.page, "%s.getData()" % self.component.tableId)

  @property
  def headers(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get("%s.getColumnDefinitions()" % self.component.tableId)

  def empty(self):
    return self.component.js.clearData()


class JsHtmlAggrid(JsHtml.JsHtml):

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(self.page, self.component.js.getRowsData().toStr())
