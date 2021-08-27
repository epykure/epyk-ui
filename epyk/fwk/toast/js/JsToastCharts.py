#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class Charts(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.varName, self.varData, self.__var_def = varName, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def addData(self, data, category=None):
    """
    Description:
    -----------
    Add data.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#addData

    Attributes:
    ----------
    :param data: Array. Array of data to be added.
    :param category:
    """
    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.addData(%s)" % (self._src.var, data))

  def addSeries(self, data):
    """
    Description:
    -----------
    Add series.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#addSeries

    Attributes:
    ----------
    :param data: String. Data to be added.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.addSeries(%s)" % (self._src.var, data))

  def hideTooltip(self):
    """
    Description:
    -----------
    Hide tooltip.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#hideTooltip
    """
    return JsUtils.jsWrap("%s.hideTooltip(%s)" % self._src.var)

  def setData(self, data):
    """
    Description:
    -----------
    Convert the chart data to new data.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#setData

    Attributes:
    ----------
    :param data: Array. Data to be set.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.setData(%s)" % (self._src.var, data))

  def setOptions(self, options):
    """
    Description:
    -----------
    Convert the chart options to new options.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#setOptions

    Attributes:
    ----------
    :param options: Dictionary. Chart options.
    """
    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.setOptions(%s)" % (self._src.var, options))

  def showTooltip(self, seriesInfo):
    """
    Description:
    -----------
    Show tooltip.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#showTooltip

    Attributes:
    ----------
    :param seriesInfo: Dictionary. Information of the series for the tooltip to be displayed.
    """
    options = JsUtils.jsConvertData(seriesInfo, None)
    return JsUtils.jsWrap("%s.showTooltip(%s)" % (self._src.var, seriesInfo))

  def updateOptions(self, options):
    """
    Description:
    -----------
    Update chart options.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/BubbleChart#updateOptions

    Attributes:
    ----------
    :param options: Dictionary. Chart options.
    """
    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.updateOptions(%s)" % (self._src.var, options))

  def destroy(self):
    """
    Description:
    -----------
    Destroys the instance.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/Chart#destroy
    """
    return JsUtils.jsWrap("%s.destroy()" % self._src.var)
