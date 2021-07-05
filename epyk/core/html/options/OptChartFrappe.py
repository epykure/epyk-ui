#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options
from epyk.core.js import JsUtils
from epyk.core.js.packages import packageImport
from epyk.core.html.options import OptChart


class OptionsChartSharedFrappe(OptChart.OptionsChartShared):

  def x_format(self, jsFncs, profile=None):
    pass

  def x_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    pass

  def x_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    pass

  def x_label(self, value):
    """
    Description:
    -----------
    Set the label of the x axis.

    Not yet available.

    Related Pages:

      https://github.com/frappe/charts/issues/219

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    pass

  def x_tick_count(self, num):
    return self

  def y_label(self, value):
    """
    Description:
    -----------
    Set the label of the y axis.

    Not yet available.

    Related Pages:

      https://github.com/frappe/charts/issues/219

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    pass

  def y_format(self, jsFncs, profile=None):
    pass

  def y_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    pass

  def y_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    pass

  def y_tick_count(self, num):
    return self


class OptionFormatters(Options):

  def __init__(self, options, name):
    self.__option = options
    self._report = options._report
    self.__name = name

  @packageImport("accounting")
  def toNumber(self, digit=0, thousand_sep="."):
    """

    :param digit:
    :param thousand_sep:
    """
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    self.__option._config("function (value){return accounting.formatNumber(value, %s, %s)}" % (
      digit, thousand_sep), self.__name, True)

  @packageImport("accounting")
  def scale(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    """
    Description:
    -----------

    Usage::

      chart.options.tooltipOptions.y_formatters.scale(1/1000)

    Attributes:
    ----------
    :param factor:
    :param alias:
    :param digits:
    :param thousand_sep:
    """
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    alias = alias or {1000: "k", 1000000: "m"}.get(factor, "")
    self.__option._config(
      "function(value) {var pointVal = value/%s; return accounting.formatNumber(pointVal, %s, %s) + '%s'}" % (
        factor, digits, thousand_sep, alias), self.__name, True)


class FrappeTooltipOptions(Options):

  def formatTooltipX(self, jsFncs, profile=None):
    self._config("function (value){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)

  def formatTooltipY(self, jsFncs, profile=None):
    """
    Description:
    ------------

    Usage::

      l2.options.tooltipOptions.formatTooltipY(["return 'test: '+ value "])

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    self._config("function (value){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)

  @property
  def x_formatters(self):
    return OptionFormatters(self, "formatTooltipX")

  @property
  def y_formatters(self):
    return OptionFormatters(self, "formatTooltipY")


class FrappeMarkersOptions(Options):

  @property
  def labelPos(self):
    """
    Description:
    ------------

    https://frappe.io/charts/docs/basic/annotations
    """
    return self._config_get()

  @labelPos.setter
  def labelPos(self, colors):
    self._config(colors)


class FrappeMarkers(Options):
  @property
  def label(self):
    """
    Description:
    ------------

    https://frappe.io/charts/docs/basic/annotations
    """
    return self._config_get()

  @label.setter
  def label(self, colors):
    self._config(colors)

  @property
  def value(self):
    """
    Description:
    ------------

    https://frappe.io/charts/docs/basic/annotations
    """
    return self._config_get()

  @value.setter
  def value(self, num):
    self._config(num)

  @property
  def options(self):
    """
    Description:
    ------------
    Can be used to set various properties on bar plot.

    Related Pages:

      https://frappe.io/charts/docs/basic/basic_chart
    """
    return self._config_sub_data("options", FrappeMarkersOptions)


class FrappeRegions(Options):
  @property
  def label(self):
    """
    Description:
    ------------

    https://frappe.io/charts/docs/basic/annotations
    """
    return self._config_get()

  @label.setter
  def label(self, colors):
    self._config(colors)

  @property
  def start(self):
    """
    Description:
    ------------

    https://frappe.io/charts/docs/basic/annotations
    """
    return self._config_get()

  @start.setter
  def start(self, num):
    self._config(num)

  @property
  def end(self):
    """
    Description:
    ------------

    https://frappe.io/charts/docs/basic/annotations
    """
    return self._config_get()

  @end.setter
  def end(self, num):
    self._config(num)

  @property
  def options(self):
    """
    Description:
    ------------
    Can be used to set various properties on bar plot.

    Related Pages:

      https://frappe.io/charts/docs/basic/basic_chart
    """
    return self._config_sub_data("options", FrappeMarkersOptions)


class FrappeDataset(Options):

  @property
  def kind(self):
    """
    Description:
    ------------

    """
    return self._config_get(name="chartType")

  @kind.setter
  def kind(self, value):
    self._config(value, name="chartType")

  @property
  def name(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @name.setter
  def name(self, value):
    self._config(value)

  @property
  def values(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @values.setter
  def values(self, vals):
    self._config(vals)


class FrappeData(Options):

  def add_data(self, data, name, kind):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param name:
    :param kind:
    """
    dataset = self._config_sub_data_enum("datasets", FrappeDataset)
    dataset.name = name
    dataset.values = data
    dataset.kind = kind
    return dataset

  @property
  def labels(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @labels.setter
  def labels(self, colors):
    self._config(colors)


class LineOptions(Options):

  @property
  def dotSize(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @dotSize.setter
  def dotSize(self, num):
    self._config(num)

  @property
  def regionFill(self):
    """
    Description:
    ------------


    Related Pages:

      https://frappe.io/charts/docs/basic/trends_regions
    """
    return self._config_get()

  @regionFill.setter
  def regionFill(self, num):
    self._config(num)

  @property
  def hideDots(self):
    """
    Description:
    ------------


    Related Pages:

      https://frappe.io/charts/docs/basic/trends_regions
    """
    return self._config_get()

  @hideDots.setter
  def hideDots(self, num):
    self._config(num)

  @property
  def heatline(self):
    """
    Description:
    ------------


    Related Pages:

      https://frappe.io/charts/docs/basic/trends_regions
    """
    return self._config_get()

  @heatline.setter
  def heatline(self, num):
    self._config(num)

  @property
  def spline(self):
    """
    Description:
    ------------


    Related Pages:

      https://frappe.io/charts/docs/basic/trends_regions
    """
    return self._config_get()

  @spline.setter
  def spline(self, num):
    self._config(num)


class BarOptions(Options):

  @property
  def spaceRatio(self):
    """
    Description:
    ------------
    In order to set the bar width, instead of defining it and the space between the bars independently,
    we simply define the ratio of the space between bars to the bar width.

    Related Pages:

      https://frappe.io/charts/docs/reference/configuration
    """
    return self._config_get()

  @spaceRatio.setter
  def spaceRatio(self, num):
    if num < 0 or num > 1:
      raise Exception("Ratio must be between 0 and 1")

    self._config(num)

  @property
  def stacked(self):
    """
    Description:
    ------------
    Renders multiple bar datasets in a stacked configuration, rather than the default adjacent.

    Related Pages:


    """
    return self._config_get()

  @stacked.setter
  def stacked(self, num):
    self._config(num)

  @property
  def height(self):
    return self._config_get()

  @height.setter
  def height(self, num):
    self._config(num)

  @property
  def depth(self):
    return self._config_get()

  @depth.setter
  def depth(self, num):
    self._config(num)


class AxisOptions(Options):

  @property
  def xAxisMode(self):
    return self._config_get()

  @xAxisMode.setter
  def xAxisMode(self, text):
    self._config(text)

  @property
  def xIsSeries(self):
    """
    Description:
    ------------
    We can skip X labels by setting the xIsSeries property in axisOptions to true.

    Related Pages:

      https://frappe.io/charts/docs/basic/trends_regions
    """
    return self._config_get()

  @xIsSeries.setter
  def xIsSeries(self, flag):
    self._config(flag)


class FrappeLine(Options):

  @property
  def animate(self):
    """
    Description:
    ------------
    Enable or disable animation.

    Related Pages:

      https://frappe.io/charts/docs/reference/configuration
    """
    return self._config_get()

  @animate.setter
  def animate(self, num):
    self._config(num)

  @property
  def truncateLegends(self):
    """
    Description:
    ------------
    Sometimes long legends would overlap with neighboring legends, this option truncates it to a fixed length.

    Related Pages:

      https://frappe.io/charts/docs/reference/configuration
    """
    return self._config_get()

  @truncateLegends.setter
  def truncateLegends(self, flag):
    self._config(flag)

  @property
  def xAxisMode(self):
    """
    Description:
    ------------
    Display axis points as short ticks or long spanning lines.

    Related Pages:

      https://frappe.io/charts/docs/reference/configuration

    """
    return self._config_get()

  @xAxisMode.setter
  def xAxisMode(self, flag):
    self._config(flag)

  @property
  def yAxisMode(self):
    """
    Description:
    ------------
    Display axis points as short ticks or long spanning lines.

    Related Pages:

      https://frappe.io/charts/docs/reference/configuration

    """
    return self._config_get()

  @yAxisMode.setter
  def yAxisMode(self, flag):
    self._config(flag)

  @property
  def xIsSeries(self):
    """
    Description:
    ------------
    The X axis (often the time axis) is usually continuous.

    Related Pages:

      https://frappe.io/charts/docs/reference/configuration

    """
    return self._config_get()

  @xIsSeries.setter
  def xIsSeries(self, flag):
    self._config(flag)

  @property
  def valuesOverPoints(self):
    """
    Description:
    ------------
    To display data values over bars or dots in an axis graph.

    Related Pages:

      https://frappe.io/charts/docs/reference/configuration
      https://frappe.io/charts/docs/basic/annotations
    """
    return self._config_get()

  @valuesOverPoints.setter
  def valuesOverPoints(self, flag):
    self._config(flag)

  @property
  def colors(self):
    return self._config_get()

  @colors.setter
  def colors(self, values):
    self._config(values)

  @property
  def title(self):
    """
    Description:
    ------------
    Add a title to the Chart.

    Related Pages:

      https://frappe.io/charts/docs/reference/configuration
    """
    return self._config_get()

  @title.setter
  def title(self, text):
    self._config(text)

  @property
  def type(self):
    """
    Description:
    ------------
    Let the chart know what type to render.

    Related Pages:

      https://frappe.io/charts/docs/reference/configuration
    """
    return self._config_get()

  @type.setter
  def type(self, value):
    self._config(value)

  @property
  def height(self):
    """
    Description:
    ------------
    Set the height of the chart in pixels.

    Related Pages:

      https://frappe.io/charts/docs/reference/configuration
    """
    return self._config_get()

  @height.setter
  def height(self, num):
    self._config(num)

  @property
  def isNavigable(self):
    """
    Description:
    ------------
    Makes the chart interactive with arrow keys and highlights the current active data point.

    Related Pages:

      https://frappe.io/charts/docs/update_state/navigation
    """
    return self._config_get()

  @isNavigable.setter
  def isNavigable(self, flag):
    self._config(flag)

  @property
  def axisOptions(self):
    """
    Description:
    ------------

    Related Pages:

      https://frappe.io/charts/docs/basic/basic_chart

    """
    return self._config_sub_data("axisOptions", AxisOptions)

  @property
  def lineOptions(self):
    """
    Description:
    ------------
    Can be used to set various properties on line plots, turn them into Area Charts and so on.

    Related Pages:

      https://frappe.io/charts/docs/basic/basic_chart

    """
    return self._config_sub_data("lineOptions", LineOptions)

  @property
  def barOptions(self):
    """
    Description:
    ------------
    Can be used to set various properties on bar plot.

    Related Pages:

      https://frappe.io/charts/docs/basic/basic_chart
    """
    return self._config_sub_data("barOptions", BarOptions)

  @property
  def data(self):
    """
    Description:
    ------------
    Contains an array of labels and an array of datasets, each a value for the 2-dimensional data points.

    Related Pages:

      https://frappe.io/charts/docs/reference/configuration
    """
    return self._config_sub_data("data", FrappeData)

  @property
  def stacked(self):
    """
    Description:
    ------------
    Renders multiple bar datasets in a stacked configuration, rather than the default adjacent.

    Related Pages:


    """
    return self._config_get()

  @stacked.setter
  def stacked(self, num):
    self._config(num)

  def add_marker(self, label, value):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param label:
    :param value:
    """
    dataset = self._config_sub_data_enum("yMarkers", FrappeMarkers)
    dataset.label = label
    dataset.value = value
    return dataset

  def add_region(self, label, start, end):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param label:
    :param start:
    :param end:
    """
    dataset = self._config_sub_data_enum("yRegions", FrappeRegions)
    dataset.label = label
    dataset.start = start
    dataset.end = end
    return dataset

  @property
  def tooltipOptions(self):
    """
    Description:
    ------------
    Frappe Charts are known for their awesome tooltips.
    """
    return self._config_sub_data("tooltipOptions", FrappeTooltipOptions)
