#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List
from epyk.core.py import types as etypes

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class FrappeCharts(JsPackage):
  lib_alias = {'js': "frappe-charts", 'css': 'frappe-charts'}

  def __init__(self, html_code=None, config=None, component=None, js_code=None, selector=None, set_var=False,
               page = None):
    self.component, self.page = component, page
    if page is None and component is not None:
      self.page = component.page
    if selector is None:
      self._selector = self.new(html_code, config, js_code).toStr()
    else:
      self._selector = selector
    self.varName, self.setVar = js_code or self._selector, set_var
    self.component.jsImports.add(self.lib_alias['js'])
    self.component.cssImport.add(self.lib_alias['css'])
    self._js = []

  def new(self, html_code, options, js_code):
    """   
 
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options:
    :param js_code:
    """
    options = JsUtils.jsConvertData(options, None)
    if js_code is not None:
      return JsObjects.JsVoid('%s = new frappe.Chart("#%s", %s)' % (js_code, html_code, options))

    return JsObjects.JsVoid('new frappe.Chart("#%s", %s)' % (html_code, options))

  def addDataPoint(self, label, value_from_each_dataset, position=None):
    """   Add a data point to the chart, increasing the length of the dataset.

    Related Pages:

      https://frappe.io/charts/docs/reference/api
 
    :param label:
    :param value_from_each_dataset:
    :param position:
    """
    label = JsUtils.jsConvertData(label, None)
    value_from_each_dataset = JsUtils.jsConvertData(value_from_each_dataset, None)
    if position is None:
      return JsObjects.JsVoid("%s.addDataPoint(%s, %s)" % (self.varName, label, value_from_each_dataset))

    return JsObjects.JsVoid("%s.addDataPoint(%s, %s, %s)" % (self.varName, label, value_from_each_dataset, position))

  def removeDataPoint(self, n):
    """   Remove a data point from the chart, reducing the length of the dataset.

    Related Pages:

      https://frappe.io/charts/docs/reference/api
 
    :param n: Number. the index of the points to be removed
    """
    return JsObjects.JsVoid("%s.removeDataPoint(%s)" % (self.varName, n))

  def update(self, data: etypes.JS_DATA_TYPES, dataflows: List[dict] = None):
    """
    Update the entire data, including annotations, by passing the entire new data object to update.

    Related Pages:

      https://frappe.io/charts/docs/reference/api

    :param data: Optional. The full datasets object expected by Frappe Chart
    :param dataflows: Chain of data transformations
    """
    data = JsUtils.dataFlows(data, dataflows, self.page)
    return JsObjects.JsVoid("%s.update(%s)" % (self.varName, data))

  def export(self):
    """
    Frappe charts are exportable to an SVG format, in which they are natively rendered.

    Related Pages:

      https://frappe.io/charts/docs/reference/api
    """
    return JsObjects.JsVoid("%s.export()" % self.varName)
