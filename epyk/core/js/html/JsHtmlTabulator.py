#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects


class JsHtmlTabulatorCell(JsHtml.JsHtml):

  def _init__(self, tableId, page):
    self.tableId = tableId
    self.page = page

  def getElement(self):
    """

    :return:
    """
    return JsNodeDom.JsDoms.get("cell.getElement()")

  def getColumnField(self):
    """

    :return:
    """
    return JsObjects.JsObject.JsObject.get("cell.getColumn().getField()")

  def getColumnTitle(self):
    """

    :return:
    """
    return JsObjects.JsObject.JsObject.get("cell.getColumn().getDefinition().title")

  def getValue(self):
    """

    :return:
    """
    return JsObjects.JsObject.JsObject.get("cell.getValue()")

  def getRow(self):
    """

    :return:
    """
    return JsObjects.JsObject.JsObject.get("cell.getRow()")

  def getData(self):
    """

    :return:
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
    return JsHtml.ContentFormatters(self._report, "%s.getData()" % self._src.tableId)

  @property
  def headers(self):
    """
    Description:
    -----------


    """
    return JsObjects.JsObjects.get("%s.getColumnDefinitions()" % self._src.tableId)
