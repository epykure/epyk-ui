#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.data import events
from epyk.core.js import JsUtils


class JsFileData(object):

  def __init__(self, varName):
    self.varName = varName

  @property
  def headers(self):
    return JsObjects.JsArray.JsArray.get(self.varName)[0].keys()

  @property
  def records(self):
    return JsObjects.JsArray.JsArray.get(self.varName)

  @property
  def vector(self, name):
    pass

  @property
  def series(self, names):
    pass


class JsHtmlDropFiles(JsHtml.JsHtml):

  @property
  def content(self):
    """
    Description:
    ------------
    Return the values of the items in the list.
    """
    return JsObjects.JsArray.JsArray.get("window['%s_data']" % self._src.htmlCode)

  def store(self, delimiter):
    """

    :param delimiter:
    """
    value = events.data.fileToDict(delimiter)
    return JsObjects.JsVoid("window['%s_data'] = %s" % (self._src.htmlCode, JsUtils.jsConvertData(value, None)))

  @property
  def data(self,):
    return JsFileData("window['%s_data']" % self._src.htmlCode)

