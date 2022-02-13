#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import primitives

from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class JsFileData:

  def __init__(self, js_code: str):
    self.varName = js_code

  @property
  def raw(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObjects.get(self.varName)

  @property
  def headers(self) -> JsObjects.JsArray.JsArray:
    """
    Description:
    ------------

    """
    return JsObjects.JsArray.JsArray.get(self.varName)[0].keys()

  @property
  def records(self) -> JsObjects.JsArray.JsArray:
    """
    Description:
    ------------

    """
    return JsObjects.JsArray.JsArray.get(self.varName)

  def vector(self, name: str) -> JsObjects.JsArray.JsArray:
    """
    Description:
    ------------

    Attributes:
    ----------
    :param str name:
    """
    name = JsUtils.jsConvertData(name, None)
    return JsObjects.JsArray.JsArray.get('''
      (function(records, col){
        var vector = []; records.forEach(function(rec){vector.push(rec[col])});
        return vector
      })(%s, %s)
      ''' % (self.varName, name))

  def values(self, name: Union[str, primitives.JsDataModel], with_count: bool = False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] name:
    :param bool with_count:
    """
    name = JsUtils.jsConvertData(name, None)
    with_count = JsUtils.jsConvertData(with_count, None)
    return JsObjects.JsObjects.get('''
      (function(records, col){
        var vector = {}; records.forEach(function(rec){
          if(vector[rec[col]] == undefined){vector[rec[col]] = 0};
          vector[rec[col]]++});
        if(%s){return vector}
        else{return Object.keys(vector)}
      })(%s, %s)
      ''' % (with_count, self.varName, name))

  def series(self, names: Union[str, primitives.JsDataModel]) -> JsObjects.JsArray.JsArray:
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] names:
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
  def content(self) -> JsObjects.JsArray.JsArray:
    """
    Description:
    ------------
    Return the values of the items in the list.
    """
    return JsObjects.JsArray.JsArray.get("(function(){if(typeof window['%(htmlCode)s_data'] !== 'undefined'){return window['%(htmlCode)s_data']} else {return []}})()" % {
      "htmlCode": self.component.htmlCode})

  def store(self, delimiter: str = None, data_type: str = None, js_code: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param str delimiter: Optional. The file delimiter.
    :param str data_type: Optional. The data type like json for example.
    :param Union[str, primitives.JsDataModel] js_code: Optional.
    """
    from epyk.core.data import events

    delimiter = delimiter or self.component.options.delimiter
    data_type = data_type or self.component.options.format
    js_code = JsUtils.jsConvertData(js_code or '%s_data' % self.component.htmlCode, None)
    if data_type.endswith("json"):
      value = events.data.jsonParse()
    else:
      value = events.data.fileToDict(delimiter)
    return JsObjects.JsVoid("window[%s] = %s" % (js_code, JsUtils.jsConvertData(value, None)))

  def load(self, data: Union[str, primitives.JsDataModel], js_code: Union[str, primitives.JsDataModel] = None):
    js_code = JsUtils.jsConvertData(js_code or '%s_data' % self.component.htmlCode, None)
    return JsObjects.JsVoid("window[%s] = %s" % (js_code, JsUtils.jsConvertData(data, None)))

  def get_data(self, js_code: Union[str, primitives.JsDataModel] = None):
    js_code = JsUtils.jsConvertData(js_code or '%s_data' % self.component.htmlCode, None)
    return JsObjects.JsObjects.get("window[%s]" % js_code)

  @property
  def code(self):
    """
    Description:
    ------------
    The default data reference.
    """
    return "%s_data" % self.component.htmlCode

  @property
  def data(self):
    return JsFileData("window['%s_data']" % self.component.htmlCode)

