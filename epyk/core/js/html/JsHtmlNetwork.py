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
  def raw(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObjects.get(self.varName)

  @property
  def headers(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsArray.JsArray.get(self.varName)[0].keys()

  @property
  def records(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsArray.JsArray.get(self.varName)

  def vector(self, name):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    """
    name = JsUtils.jsConvertData(name, None)
    return JsObjects.JsArray.JsArray.get('''
      (function(records, col){
        var vector = []; records.forEach(function(rec){vector.push(rec[col])});
        return vector
      })(%s, %s)
      ''' % (self.varName, name))

  def values(self, name):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    """
    name = JsUtils.jsConvertData(name, None)
    return JsObjects.JsObjects.get('''
      (function(records, col){
        var vector = {}; records.forEach(function(rec){
          if(vector[rec[col]] == undefined){vector[rec[col]] = 0};
          vector[rec[col]]++});
        return vector
      })(%s, %s)
      ''' % (self.varName, name))

  def series(self, names):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param names:
    """
    names = JsUtils.jsConvertData(names, None)
    return JsObjects.JsArray.JsArray.get('''
      (function(records, cols){
        var vector = []; records.forEach(function(rec){
          var row = []; cols.forEach(function(r){row.push(rec[r])}); vector.push(row)});
        return vector
      })(%s, %s)
      ''' % (self.varName, names))


class JsHtmlDropFiles(JsHtml.JsHtml):

  @property
  def content(self):
    """
    Description:
    ------------
    Return the values of the items in the list.
    """
    return JsObjects.JsArray.JsArray.get("window['%s_data']" % self._src.htmlCode)

  def store(self, delimiter=None, format=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param delimiter: String. Optional. The file delimiter
    """
    delimiter = delimiter or self._src.options.delimiter
    format = format or self._src.options.format
    print(format)
    if format.endswith("json"):
      value = events.data.jsonParse()
    else:
      value = events.data.fileToDict(delimiter)
    return JsObjects.JsVoid("window['%s_data'] = %s" % (self._src.htmlCode, JsUtils.jsConvertData(value, None)))

  @property
  def data(self,):
    return JsFileData("window['%s_data']" % self._src.htmlCode)

