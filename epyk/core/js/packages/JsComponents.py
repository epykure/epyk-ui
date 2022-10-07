#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import primitives
from epyk.core.js.packages import JsPackage
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class SkillBar(JsPackage):
  lib_set_var = False

  def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = False,
               page: primitives.PageModel = None):
    super(SkillBar, self).__init__(
      component, js_code=js_code, selector=component.htmlCode, data=None, set_var=set_var, page=page)

  @property
  def labels(self):
    """  

    """
    return JsObjects.JsVoid('''
(function(component){let labels = []; let row;
let r=0; while(row=component.firstChild.rows[r++]){
  labels.push(row.cells[0].innerText)}; return labels})(%(varName)s)
''' % {"varName": self.varName})

  @property
  def records(self):
    """  
    """
    return JsObjects.JsVoid('''
(function(component){let records = []; let row;
let r=0; while(row=component.firstChild.rows[r++]){
  records.push({"label": row.cells[0].innerText, "value": parseFloat(row.cells[1].firstChild.style["width"])}) ;
}; return records})(%(varName)s)''' % {"varName": self.varName})

  def get(self, label: Union[str, primitives.JsDataModel]):
    """  
 
    :param Union[str, primitives.JsDataModel] label:
    """
    label = JsUtils.jsConvertData(label, None)
    return JsObjects.JsVoid('''
(function(component, label){let rowCell = null; let row;
let r=0; while(row=component.firstChild.rows[r++]){
  if(row.cells[0].innerText == label){rowCell = row; break}
}; return rowCell})(%(varName)s, %(label)s)''' % {"varName": self.varName, "label": label})

  def value(self, label: Union[str, primitives.JsDataModel],
            value: Union[str, primitives.JsDataModel] = None, options: dict = None):
    """  
 
    :param Union[str, primitives.JsDataModel] label:
    :param Union[str, primitives.JsDataModel] value:
    :param dict options:
    """
    label = JsUtils.jsConvertData(label, None)
    if value is None:
      return JsObjects.JsVoid('''
(function(){let row = %(row)s; let value = -1;
if (row != null){value = parseFloat(row.cells[1].firstChild.style["width"])}   
return value})() ''' % {"row": self.get(label).toStr()})

    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsVoid('''
(function(){let row = %(row)s; let options = %(options)s;
if (row != null){
  let cellValue = %(value)s;
  row.cells[1].firstChild.style["width"] = cellValue + "%%";
  if( cellValue > options.thresholds[1]){ row.cells[1].firstChild.style.backgroundColor = options.success}
  else if(cellValue > options.thresholds[0]) {row.cells[1].firstChild.style.backgroundColor = options.warning}
  else {row.cells[1].firstChild.style.backgroundColor = options.danger}
  row.title = cellValue + "%%"}})() ''' % {
      "row": self.get(label).toStr(), "value": value, 'options': self.component.options.config_js(options)})

  def load(self, values):
    raise NotImplementedError()

  def remove(self, label: Union[str, primitives.JsDataModel]):
    """  
 
    :param Union[str, primitives.JsDataModel] label:
    """
    label = JsUtils.jsConvertData(label, None)
    return JsObjects.JsVoid('''
(function(){let row = %(row)s; let value = -1;
if (row != null){row.remove()}})() ''' % {"row": self.get(label).toStr()})
