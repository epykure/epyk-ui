#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options

from epyk.core.js.packages import packageImport
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class OptionHover(Options):

  @property
  def sizeOffset(self):
    return self._config_get()

  @sizeOffset.setter
  def sizeOffset(self, num):
    self._config(num)

  @property
  def size(self):
    return self._config_get()

  @size.setter
  def size(self, num):
    self._config(num)


class OptionMarkers(Options):

  @property
  def size(self):
    return self._config_get()

  @size.setter
  def size(self, num):
    self._config(num)

  @property
  def colors(self):
    return self._config_get()

  @colors.setter
  def colors(self, values):
    self._config(values)

  @property
  def strokeColors(self):
    return self._config_get()

  @strokeColors.setter
  def strokeColors(self, value):
    self._config(value)

  @property
  def strokeWidth(self):
    return self._config_get()

  @strokeWidth.setter
  def strokeWidth(self, num):
    self._config(num)

  @property
  def hover(self):
    return self._config_sub_data("hover", OptionHover)


class OptionToolbar(Options):

  @property
  def show(self):
    return self._config_get()

  @show.setter
  def show(self, flag):
    self._config(flag)

  @property
  def autoSelected(self):
    return self._config_get()

  @autoSelected.setter
  def autoSelected(self, value):
    self._config(value)


class OptionDropShadow(Options):

  @property
  def enabled(self):
    return self._config_get()

  @enabled.setter
  def enabled(self, flag):
    self._config(flag)

  @property
  def color(self):
    return self._config_get()

  @color.setter
  def color(self, value):
    self._config(value)

  @property
  def top(self):
    return self._config_get()

  @top.setter
  def top(self, num):
    self._config(num)

  @property
  def left(self):
    return self._config_get()

  @left.setter
  def left(self, num):
    self._config(num)

  @property
  def blur(self):
    return self._config_get()

  @blur.setter
  def blur(self, num):
    self._config(num)

  @property
  def opacity(self):
    return self._config_get()

  @opacity.setter
  def opacity(self, num):
    self._config(num)


class OptionLabels(Options):

  def formatter(self, jsFncs):
    self._config("function (value){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  @property
  def style(self):
    return self._config_sub_data("style", OptionStyle)

  @property
  def offsetY(self):
    return self._config_get()

  @offsetY.setter
  def offsetY(self, num):
    self._config(num)

  @property
  def offsetX(self):
    return self._config_get()

  @offsetX.setter
  def offsetX(self, num):
    self._config(num)

  @property
  def useSeriesColors(self):
    return self._config_get()

  @useSeriesColors.setter
  def useSeriesColors(self, flag):
    self._config(flag)

  @property
  def formatters(self):
    return OptionFormatters(self, "formatter")


class OptionAxisTicks(Options):

  @property
  def show(self):
    return self._config_get()

  @show.setter
  def show(self, flag):
    self._config(flag)


class OptionAxisBorder(Options):

  @property
  def show(self):
    return self._config_get()

  @show.setter
  def show(self, flag):
    self._config(flag)


class OptionXaxis(Options):

  @property
  def categories(self):
    return self._config_get()

  @categories.setter
  def categories(self, values):
    self._config(values)

  @property
  def title(self):
    return self._config_sub_data("title", OptionTitle)

  @property
  def labels(self):
    return self._config_sub_data("labels", OptionLabels)

  def axisTicks(self):
    return self._config_sub_data("axisTicks", OptionAxisTicks)

  def axisBorder(self):
    return self._config_sub_data("axisBorder", OptionAxisBorder)

  @property
  def type(self):
    return self._config_get()

  @type.setter
  def type(self, value):
    self._config(value)

  @property
  def min(self):
    return self._config_get()

  @min.setter
  def min(self, num):
    self._config(num)

  @property
  def max(self):
    return self._config_get()

  @max.setter
  def max(self, num):
    self._config(num)

  @property
  def tickAmount(self):
    return self._config_get()

  @tickAmount.setter
  def tickAmount(self, num):
    self._config(num)


class OptionYaxis(Options):

  @property
  def title(self):
    return self._config_sub_data("title", OptionTitle)

  @property
  def labels(self):
    return self._config_sub_data("labels", OptionLabels)

  @property
  def min(self):
    return self._config_get()

  @min.setter
  def min(self, num):
    self._config(num)

  @property
  def max(self):
    return self._config_get()

  @max.setter
  def max(self, num):
    self._config(num)

  @property
  def reversed(self):
    return self._config_get()

  @reversed.setter
  def reversed(self, flag):
    self._config(flag)

  def axisTicks(self):
    return self._config_sub_data("axisTicks", OptionAxisTicks)

  @property
  def tickAmount(self):
    return self._config_get()

  @tickAmount.setter
  def tickAmount(self, num):
    self._config(num)


class OptionRow(Options):

  @property
  def colors(self):
    return self._config_get()

  @colors.setter
  def colors(self, values):
    self._config(values)

  @property
  def opacity(self):
    return self._config_get()

  @opacity.setter
  def opacity(self, num):
    self._config(num)


class OptionPadding(Options):

  @property
  def right(self):
    return self._config_get()

  @right.setter
  def right(self, num):
    self._config(num)

  @property
  def left(self):
    return self._config_get()

  @left.setter
  def left(self, num):
    self._config(num)


class OptionGrid(Options):

  @property
  def borderColor(self):
    return self._config_get()

  @borderColor.setter
  def borderColor(self, value):
    self._config(value)

  @property
  def row(self):
    return self._config_sub_data("row", OptionRow)

  @property
  def padding(self):
    return self._config_sub_data("padding", OptionPadding)


class OptionZoom(Options):

  @property
  def enabled(self):
    return self._config_get()

  @enabled.setter
  def enabled(self, flag):
    self._config(flag)

  @property
  def type(self):
    return self._config_get()

  @type.setter
  def type(self, value):
    self._config(value)

  @property
  def autoScaleYaxis(self):
    return self._config_get()

  @autoScaleYaxis.setter
  def autoScaleYaxis(self, flag):
    self._config(flag)


class OptionSparkline(Options):

  @property
  def enabled(self):
    return self._config_get()

  @enabled.setter
  def enabled(self, value):
    self._config(value)


class OptionDynamicAnimations(Options):

  @property
  def speed(self):
    return self._config_get()

  @speed.setter
  def speed(self, num):
    self._config(num)


class OptionAnimations(Options):

  @property
  def enabled(self):
    return self._config_get()

  @enabled.setter
  def enabled(self, flag):
    self._config(flag)

  @property
  def easing(self):
    return self._config_get()

  @easing.setter
  def easing(self, value):
    self._config(value)

  @property
  def dynamicAnimation(self):
    return self._config_sub_data("dynamicAnimation", OptionDynamicAnimations)


class OptionEvents(Options):

  def click(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Fires when user clicks on any area of the chart.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(event, chartContext, config){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  def mouseMove(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Fires when user moves mouse on any area of the chart.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(event, chartContext, config){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  def legendClick(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Fires when user clicks on legend.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/#legendClick

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(chartContext, seriesIndex, config){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  def markerClick(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Fires when user clicks on the markers.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/#markerClick

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(chartContext, seriesIndex, options){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  def selection(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Fires when user selects rect using the selection tool.
    The second argument contains the yaxis and xaxis coordinates where user made the selection

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/#selection

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(chartContext, options){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  def zoomed(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Fires when user zooms in/out the chart using either the selection zooming tool or zoom in/out buttons.
    The 2nd argument includes information of the new xaxis/yaxis generated after zooming.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/#zoomed

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(chartContext, options){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  def scrolled(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Fires when user drags the brush in a brush chart.
    The 2nd argument includes information of the new axes generated after scrolling the brush.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/#scrolled

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(chartContext, options){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  def animationEnd(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Fires when the chart’s initial animation is finished.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/#animationEnd

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(chartContext, config){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  def updated(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Fires when the chart has been dynamically updated either with updateOptions() or updateSeries() functions.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/#updated

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(chartContext, config){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  def mounted(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Fires after the chart has been drawn on screen.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/#mounted

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(chartContext, config){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  def beforeMount(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Fires before the chart has been drawn on screen.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/#beforeMount

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(chartContext, config){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)


class OptionChart(Options):

  @property
  def height(self):
    return self._config_get()

  @height.setter
  def height(self, num):
    self._config(num)

  @property
  def id(self):
    return self._config_get()

  @id.setter
  def id(self, value):
    self._config(value)

  @property
  def type(self):
    return self._config_get()

  @type.setter
  def type(self, value):
    self._config(value)

  @property
  def zoom(self):
    return self._config_sub_data("zoom", OptionZoom)

  @property
  def events(self):
    return self._config_sub_data("events", OptionEvents)

  @property
  def animations(self):
    return self._config_sub_data("animations", OptionAnimations)

  @property
  def dropShadow(self):
    return self._config_sub_data("dropShadow", OptionDropShadow)

  @property
  def toolbar(self):
    return self._config_sub_data("toolbar", OptionToolbar)

  @property
  def stacked(self):
    return self._config_get()

  @stacked.setter
  def stacked(self, num):
    self._config(num)

  @property
  def sparkline(self):
    return self._config_sub_data("sparkline", OptionSparkline)

  @property
  def stackType(self):
    return self._config_get()

  @stackType.setter
  def stackType(self, num):
    self._config(num)


class OptionName(Options):

  @property
  def show(self):
    return self._config_get()

  @show.setter
  def show(self, flag):
    self._config(flag)

  @property
  def fontSize(self):
    return self._config_get()

  @fontSize.setter
  def fontSize(self, num):
    self._config("%spx" % num)


class OptionValue(Options):

  @property
  def offsetY(self):
    return self._config_get()

  @offsetY.setter
  def offsetY(self, num):
    self._config(num)

  @property
  def fontSize(self):
    return self._config_get()

  @fontSize.setter
  def fontSize(self, num):
    self._config("%spx" % num)


class OptionTotal(Options):

  @property
  def show(self):
    return self._config_get()

  @show.setter
  def show(self, flag):
    self._config(flag)

  @property
  def label(self):
    return self._config_get()

  @label.setter
  def label(self, value):
    self._config(value)

  def formatter(self, jsFncs):
    self._config("function (value){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  @property
  def formatters(self):
    return OptionFormatters(self, "formatter")


class OptionFormatters:
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
    self.__option._config("function (value){return accounting.formatNumber(value, %s, %s)}" % (digit, thousand_sep), self.__name, True)

  @packageImport("accounting")
  def toMoney(self, symbol="", digit=0, thousand_sep=".", decimal_sep=","):
    """

    :param symbol:
    :param digit:
    :param thousand_sep:
    :param decimal_sep:
    """
    symbol = JsUtils.jsConvertData(symbol, None)
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
    self.__option._config("function (value){return accounting.formatMoney(value, %s, %s, %s, %s)}" % (symbol, digit, thousand_sep, decimal_sep), self.__name, True)

  @packageImport("accounting")
  def scale(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    """
    Description:
    -----------

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

  def mapTo(self, mapping):
    self.__option._config("function (value){var mapping = %s; if (value in mapping){return mapping[value]}; return value}" % mapping, self.__name, js_type=True)


class OptionDataLabels(Options):

  @property
  def enabled(self):
    return self._config_get()

  @enabled.setter
  def enabled(self, flag):
    self._config(flag)

  @property
  def textAnchor(self):
    """

    https://apexcharts.com/docs/options/datalabels/
    """
    return self._config_get()

  @textAnchor.setter
  def textAnchor(self, flag):
    self._config(flag)

  @property
  def offsetY(self):
    return self._config_get()

  @offsetY.setter
  def offsetY(self, num):
    self._config(num)

  @property
  def name(self):
    return self._config_sub_data("name", OptionName)

  @property
  def value(self):
    return self._config_sub_data("value", OptionValue)

  @property
  def style(self):
    return self._config_sub_data("style", OptionStyle)

  @property
  def total(self):
    return self._config_sub_data("total", OptionTotal)

  def formatter(self, jsFncs):
    self._config("function (value){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  @property
  def formatters(self):
    return OptionFormatters(self, "formatter")


class OptionStroke(Options):

  @property
  def curve(self):
    return self._config_get()

  @curve.setter
  def curve(self, value):
    self._config(value)

  @property
  def width(self):
    return self._config_get()

  @width.setter
  def width(self, num):
    self._config(num)

  @property
  def dashArray(self):
    return self._config_get()

  @dashArray.setter
  def dashArray(self, values):
    self._config(values)


class OptionStyle(Options):

  @property
  def fontSize(self):
    return self._config_get()

  @fontSize.setter
  def fontSize(self, num):
    self._config("%spx" % num)

  @property
  def color(self):
    return self._config_get()

  @color.setter
  def color(self, value):
    self._config(value)


class OptionTitle(Options):

  @property
  def align(self):
    return self._config_get()

  @align.setter
  def align(self, position):
    self._config(position)

  @property
  def floating(self):
    return self._config_get()

  @floating.setter
  def floating(self, flag):
    self._config(flag)

  @property
  def text(self):
    return self._config_get()

  @text.setter
  def text(self, val):
    self._config(val)

  @property
  def offsetX(self):
    return self._config_get()

  @offsetX.setter
  def offsetX(self, num):
    self._config(num)

  @property
  def style(self):
    return self._config_sub_data("style", OptionStyle)


class OptionLegend(Options):

  @property
  def show(self):
    return self._config_get()

  @show.setter
  def show(self, flag):
    self._config(flag)

  @property
  def position(self):
    return self._config_get()

  @position.setter
  def position(self, value):
    self._config(value)

  @property
  def horizontalAlign(self):
    return self._config_get()

  @horizontalAlign.setter
  def horizontalAlign(self, value):
    self._config(value)

  @property
  def floating(self):
    return self._config_get()

  @floating.setter
  def floating(self, flag):
    self._config(flag)

  @property
  def offsetY(self):
    return self._config_get()

  @offsetY.setter
  def offsetY(self, num):
    self._config(num)

  @property
  def offsetX(self):
    return self._config_get()

  @offsetX.setter
  def offsetX(self, num):
    self._config(num)

  def tooltipHoverFormatter(self, jsFncs):
    pass

  @property
  def labels(self):
    return self._config_sub_data("labels", OptionLabels)


class OptionY(Options):

  def formatter(self, jsFncs):
    self._config("function (value){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), js_type=True)

  @property
  def formatters(self):
    return OptionFormatters(self, "formatter")


class OptionFixed(Options):

  @property
  def enabled(self):
    return self._config_get()

  @enabled.setter
  def enabled(self, flag):
    self._config(flag)

  @property
  def position(self):
    return self._config_get()

  @position.setter
  def position(self, value):
    self._config(value)

  @property
  def offsetY(self):
    return self._config_get()

  @offsetY.setter
  def offsetY(self, num):
    self._config(num)

  @property
  def offsetX(self):
    return self._config_get()

  @offsetX.setter
  def offsetX(self, num):
    self._config(num)


class OptionTooltip(Options):

  @property
  def shared(self):
    return self._config_get()

  @shared.setter
  def shared(self, flag):
    self._config(flag)

  @property
  def y(self):
    return self._config_sub_data("y", OptionY)

  @property
  def fixed(self):
    return self._config_sub_data("fixed", OptionFixed)


class OptionGradient(Options):

  @property
  def type(self):
    return self._config_get()

  @type.setter
  def type(self, value):
    self._config(value)

  @property
  def shadeIntensity(self):
    return self._config_get()

  @shadeIntensity.setter
  def shadeIntensity(self, num):
    self._config(num)

  @property
  def inverseColors(self):
    return self._config_get()

  @inverseColors.setter
  def inverseColors(self, flag):
    self._config(flag)

  @property
  def opacityFrom(self):
    return self._config_get()

  @opacityFrom.setter
  def opacityFrom(self, flag):
    self._config(flag)

  @property
  def opacityTo(self):
    return self._config_get()

  @opacityTo.setter
  def opacityTo(self, flag):
    self._config(flag)

  @property
  def stops(self):
    return self._config_get()

  @stops.setter
  def stops(self, values):
    self._config(values)

  @property
  def gradientToColors(self):
    return self._config_get()

  @gradientToColors.setter
  def gradientToColors(self, values):
    self._config(values)

  @property
  def shade(self):
    return self._config_get()

  @shade.setter
  def shade(self, value):
    self._config(value)


class OptionFill(Options):

  @property
  def type(self):
    return self._config_get()

  @type.setter
  def type(self, value):
    self._config(value)

  @property
  def gradient(self):
    return self._config_sub_data("gradient", OptionGradient)


class OptionSeries(Options):

  @property
  def name(self):
    return self._config_get()

  @name.setter
  def name(self, value):
    self._config(value)

  @property
  def data(self):
    return self._config_get()

  @data.setter
  def data(self, values):
    self._config(values)


class OptionResponsive(Options):

  @property
  def breakpoint(self):
    return self._config_get()

  @breakpoint.setter
  def breakpoint(self, value):
    self._config(value)

  @property
  def opts(self):
    return self._config_sub_data("options", OptionsLine)


class OptionMonochrome(Options):

  @property
  def enabled(self):
    return self._config_get()

  @enabled.setter
  def enabled(self, value):
    self._config(value)


class OptionTheme(Options):

  @property
  def mode(self):
    return self._config_get()

  @mode.setter
  def mode(self, value):
    self._config(value)

  @property
  def palette(self):
    return self._config_get()

  @palette.setter
  def palette(self, value):
    self._config(value)

  @property
  def monochrome(self):
    return self._config_sub_data("monochrome", OptionMonochrome)


class OptionHollow(Options):

  @property
  def size(self):
    return self._config_get()

  @size.setter
  def size(self, value):
    self._config(value)


class OptionPlotOptionsBar(Options):

  @property
  def horizontal(self):
    return self._config_get()

  @horizontal.setter
  def horizontal(self, flag):
    self._config(flag)

  @property
  def barHeight(self):
    return self._config_get()

  @barHeight.setter
  def barHeight(self, value):
    self._config(value)

  @property
  def dataLabels(self):
    return self._config_sub_data("dataLabels", OptionDataLabels)


class plotOptionsRadialBar(Options):

  @property
  def hollow(self):
    return self._config_sub_data("hollow", OptionHollow)

  @property
  def offsetY(self):
    return self._config_get()

  @offsetY.setter
  def offsetY(self, num):
    self._config(num)

  @property
  def startAngle(self):
    return self._config_get()

  @startAngle.setter
  def startAngle(self, num):
    self._config(num)

  @property
  def endAngle(self):
    return self._config_get()

  @endAngle.setter
  def endAngle(self, num):
    self._config(num)


class OptionPlotOptions(Options):

  @property
  def bar(self):
    return self._config_sub_data("bar", OptionPlotOptionsBar)


class plotOptionsRadial(Options):

  @property
  def radialBar(self):
    return self._config_sub_data("radialBar", plotOptionsRadialBar)

  @property
  def dataLabels(self):
    return self._config_sub_data("dataLabels", OptionDataLabels)


class OptionsLine(Options):

  @property
  def chart(self):
    return self._config_sub_data("chart", OptionChart)

  @property
  def colors(self):
    """
    Description:
    ------------

    Related Pages:

      https://apexcharts.com/docs/options/colors/

    Attributes:
    ----------
    :prop values: List. The color codes
    """
    return self._config_get()

  @colors.setter
  def colors(self, valuea):
    self._config(valuea)

  @property
  def grid(self):
    return self._config_sub_data("grid", OptionGrid)

  @property
  def markers(self):
    return self._config_sub_data("markers", OptionMarkers)

  @property
  def title(self):
    return self._config_sub_data("title", OptionTitle)

  @property
  def subtitle(self):
    return self._config_sub_data("subtitle", OptionTitle)

  @property
  def stroke(self):
    return self._config_sub_data("stroke", OptionStroke)

  @property
  def dataLabels(self):
    return self._config_sub_data("dataLabels", OptionDataLabels)

  @property
  def legend(self):
    return self._config_sub_data("legend", OptionLegend)

  @property
  def xaxis(self):
    return self._config_sub_data("xaxis", OptionXaxis)

  @property
  def yaxis(self):
    return self._config_sub_data("yaxis", OptionYaxis)

  @property
  def tooltip(self):
    return self._config_sub_data("tooltip", OptionTooltip)

  @property
  def theme(self):
    """

    https://apexcharts.com/docs/options/theme/
    """
    return self._config_sub_data("theme", OptionTheme)

  def add_series(self):
    return self._config_sub_data_enum("series", OptionSeries)

  def get_series(self, i=0):
    return self.js_tree["series"][i]

  def add_responsive(self):
    return self._config_sub_data_enum("responsive", OptionResponsive)

  def get_responsive(self, i=0):
    return self.js_tree["responsive"][i]


class OptionsArea(OptionsLine):

  @property
  def fill(self):
    return self._config_sub_data("fill", OptionFill)


class OptionsBar(OptionsLine):


  @property
  def plotOptions(self):
    return self._config_sub_data("plotOptions", OptionPlotOptions)


class OptionsPie(OptionsLine):

  @property
  def series(self):
    return self._config_get()

  @series.setter
  def series(self, values):
    self._config(values)

  @property
  def labels(self):
    return self._config_get()

  @labels.setter
  def labels(self, values):
    self._config(values)

  @property
  def plotOptions(self):
    return self._config_sub_data("plotOptions", plotOptionsRadial)
