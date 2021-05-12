#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class FrappeCharts(JsPackage):
  lib_alias = {'js': "frappe-charts", 'css': 'frappe-charts'}

  def __init__(self, htmlCode=None, config=None, src=None, varName=None, selector=None, setVar=False):
    self.src = src if src is not None else self.__internal()
    if selector is None:
      self._selector = self.new(htmlCode, config, varName).toStr()
    else:
      self._selector = selector
    self.varName, self.setVar = varName or self._selector, setVar
    self.src.jsImports.add(self.lib_alias['js'])
    self.src.cssImport.add(self.lib_alias['css'])
    self._js = []

  def new(self, htmlCode, options, varName):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options:
    """
    options = JsUtils.jsConvertData(options, None)
    if varName is not None:
      return JsObjects.JsVoid('%s = new frappe.Chart("#%s", %s)' % (varName, htmlCode, options))

    return JsObjects.JsVoid('new frappe.Chart("#%s", %s)' % (htmlCode, options))

  def addDataPoint(self, label, valueFromEachDataset, position=None):
    """
    Description:
    -----------
    Add a data point to the chart, increasing the length of the dataset.

    Related Pages:

      https://frappe.io/charts/docs/reference/api

    Attributes:
    ----------
    :param label:
    :param valueFromEachDataset:
    :param position:
    """
    label = JsUtils.jsConvertData(label, None)
    valueFromEachDataset = JsUtils.jsConvertData(valueFromEachDataset, None)
    if position is None:
      return JsObjects.JsVoid("%s.addDataPoint(%s, %s)" % (self.varName, label, valueFromEachDataset))

    return JsObjects.JsVoid("%s.addDataPoint(%s, %s, %s)" % (self.varName, label, valueFromEachDataset, position))

  def removeDataPoint(self, n):
    """
    Description:
    -----------
    Remove a data point from the chart, reducing the length of the dataset.

    Related Pages:

      https://frappe.io/charts/docs/reference/api

    Attributes:
    ----------
    :param n: Number. the index of the points to be removed
    """
    return JsObjects.JsVoid("%s.removeDataPoint(%s)" % (self.varName, n))

  def update(self, data):
    """
    Description:
    -----------
    Update the entire data, including annotations, by passing the entire new data object to update.

    Related Pages:

      https://frappe.io/charts/docs/reference/api
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsVoid("%s.update(%s)" % (self.varName, data))

  def export(self):
    """
    Description:
    -----------
    Frappe charts are exportable to an SVG format, in which they are natively rendered.

    Related Pages:

      https://frappe.io/charts/docs/reference/api
    """
    return JsObjects.JsVoid("%s.export()" % self.varName)
