#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import primitives
from epyk.core.js.packages import JsPackage
from epyk.core.js import JsUtils


class Charts(JsPackage):

  def __init__(self, component, js_code: str = None, set_var: bool = True, is_py_data: bool = True,
               page: primitives.PageModel = None):
    self.varName, self.varData, self.__var_def = js_code, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def addData(self, data: Union[list, primitives.JsDataModel], category: str = None):
    """
    Description:
    -----------
    Add data.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#addData

    Attributes:
    ----------
    :param Union[list, primitives.JsDataModel] data: Array of data to be added.
    :param str category: Optional. The data type.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.addData(%s)" % (self.component.var, data))

  def addSeries(self, data: Union[str, primitives.JsDataModel]):
    """
    Description:
    -----------
    Add series.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#addSeries

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] data: Data to be added.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.addSeries(%s)" % (self.component.var, data))

  def hideTooltip(self):
    """
    Description:
    -----------
    Hide tooltip.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#hideTooltip
    """
    return JsUtils.jsWrap("%s.hideTooltip(%s)" % self.component.var)

  def setData(self, data: Union[list, primitives.JsDataModel]):
    """
    Description:
    -----------
    Convert the chart data to new data.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#setData

    Attributes:
    ----------
    :param Union[list, primitives.JsDataModel] data: Data to be set.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.setData(%s)" % (self.component.var, data))

  def setOptions(self, options: Union[dict, primitives.JsDataModel]):
    """
    Description:
    -----------
    Convert the chart options to new options.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#setOptions

    Attributes:
    ----------
    :param Union[dict, primitives.JsDataModel] options: Chart options.
    """
    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.setOptions(%s)" % (self.component.var, options))

  def showTooltip(self, series_info: Union[dict, primitives.JsDataModel]):
    """
    Description:
    -----------
    Show tooltip.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#showTooltip

    Attributes:
    ----------
    :param Union[dict, primitives.JsDataModel] series_info: Information of the series for the tooltip to be displayed.
    """
    series_info = JsUtils.jsConvertData(series_info, None)
    return JsUtils.jsWrap("%s.showTooltip(%s)" % (self.component.var, series_info))

  def updateOptions(self, options: Union[dict, primitives.JsDataModel]):
    """
    Description:
    -----------
    Update chart options.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#updateOptions

    Attributes:
    ----------
    :param Union[dict, primitives.JsDataModel] options: Chart options.
    """
    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.updateOptions(%s)" % (self.component.var, options))

  def destroy(self):
    """
    Description:
    -----------
    Destroys the instance.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/Chart#destroy
    """
    return JsUtils.jsWrap("%s.destroy()" % self.component.var)
