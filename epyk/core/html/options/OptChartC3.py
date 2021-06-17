#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from epyk.core.html.options import Options
from epyk.core.html.options import Enums
from epyk.core.js import JsUtils
from epyk.core.html.options import OptChart


class EnumAxisTypes(Enums):

  def timeseries(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.TimeseriesChart
    """
    self._set_value()

  def log(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Axis.LogScales
    """
    self._set_value()

  def indexed(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Axis.LogScales
    """
    self._set_value()

  def category(self, categories=None):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Axis.CategoryAxis
    """
    self._set_value()
    if categories is not None:
      self.__option._config(categories, "categories")


class EnumTickFormat(Enums):

  def yy_mm_dd(self):
    """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.TimeseriesChart
    """
    self._set_value(value="%Y-%m-%d")

  def e_b_y(self):
    """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Axis.XAxisTickFitting
    """
    self._set_value(value="%e %b %y")

  def timestamp(self):
    """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Axis.XAxisTickAutorotate
    """
    self._set_value(value="%m-%d-%Y %H:%M:%S")


class EnumStepTypes(Enums):

  def linear(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://c3js.org/reference.html#spline-interpolation-type
    """
    self._set_value()

  def linear_closed(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://c3js.org/reference.html#spline-interpolation-type
    """
    self._set_value("linear-closed")

  def basis(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://c3js.org/reference.html#spline-interpolation-type
    """
    self._set_value()

  def basis_open(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://c3js.org/reference.html#spline-interpolation-type
    """
    self._set_value("basis-open")

  def basis_closed(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://c3js.org/reference.html#spline-interpolation-type
    """
    self._set_value("basis-closed")

  def bundle(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://c3js.org/reference.html#spline-interpolation-type
    """
    self._set_value()

  def cardinal(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://c3js.org/reference.html#spline-interpolation-type
    """
    self._set_value()

  def cardinal_open(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://c3js.org/reference.html#spline-interpolation-type
    """
    self._set_value(value="cardinal-open")

  def cardinal_closed(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://c3js.org/reference.html#spline-interpolation-type
    """
    self._set_value(value="cardinal-closed")

  def monotone(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://c3js.org/reference.html#spline-interpolation-type
    """
    self._set_value()

  def step(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://c3js.org/reference.html#spline-interpolation-type
    """
    self._set_value()

  def step_before(self):
    """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.StepChart
    """
    self._set_value(value="step-before")

  def step_after(self):
    """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.StepChart
    """
    self._set_value(value="step-after")


class EnumTextPosition(Enums):

  def middle(self):
    """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Grid.OptionalXGridLines
    """
    self._set_value()

  def start(self):
    """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Grid.OptionalXGridLines
    """
    self._set_value()


class EnumLegendPosition(Enums):

  def right(self):
    """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Legend.LegendPosition
    """
    self._set_value()

  def left(self):
    """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Legend.LegendPosition
    """
    self._set_value()


class OptionsChartSharedC3(OptChart.OptionsChartShared):

  def x_label(self, value):
    """
    Description:
    -----------
    Set the label of the x axis.

    Related Pages:

      https://c3js.org/reference.html#axis-y-label

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    self.component.options.axis.x.label.text = value

  def y_label(self, value):
    """
    Description:
    -----------
    Set the label of the y axis.

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    self.component.options.axis.y.label.text = value


class OptionPadding(Options):

  @property
  def bottom(self):
    """
    Description:
    ------------
    """
    return self._config_get(None)

  @bottom.setter
  def bottom(self, val):
    self._config(val)


class OptionsGridAxis(Options):

  @property
  def show(self):
    """
    Description:
    ------------
    Show grids along x axis.

    Related Pages:

      https://c3js.org/reference.html#grid-x-show
    """
    return self._config_get(None)

  @show.setter
  def show(self, val):
    self._config(val)

  def add_lines(self, value, css_class=None, text=None, position=None):
    """
    Description:
    ------------
    Add lines to the chart.

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Style.StyleForGrid

    Attributes:
    ----------
    :param value: Number. The coordinate for the line.
    :param css_class: String. Optional. The CSS class reference.
    :param text: String. Optional. The label on the line.
    :param position: String. Optional.

    :rtype: OptionLines
    """
    line = self._config_sub_data_enum("lines", OptionLines)
    line.value = value
    if css_class is not None:
      line.css_class = css_class
    if text is not None:
      line.text = text
    if position is not None:
      line.position = position
    return line


class OptionsGrid(Options):

  @property
  def x(self):
    """
    Description:
    ------------
    Property to the grid x axis.

    :rtype: OptionsGridAxis
    """
    return self._config_sub_data("x", OptionsGridAxis)

  @property
  def y(self):
    """
    Description:
    ------------
    Property to the grid y axis.

    :rtype: OptionsGridAxis
    """
    return self._config_sub_data("y", OptionsGridAxis)


class OptionsLegend(Options):

  @property
  def show(self):
    """
    Description:
    ------------
    Show or hide legend.

    Related Pages:

      https://c3js.org/reference.html#legend-show
    """
    return self._config_get(None)

  @show.setter
  def show(self, val):
    self._config(val)

  @property
  def hide(self):
    """
    Description:
    ------------
    Show or hide legend.

    Related Pages:

      https://c3js.org/reference.html#legend-hide
    """
    return self._config_get(False)

  @hide.setter
  def hide(self, flag):
    self._config(flag)

  @property
  def position(self):
    """
    Description:
    ------------
    Change the position of legend.

    Currently bottom, right and inset are supported.

    Related Pages:

      https://c3js.org/reference.html#legend-position
    """
    return self._config_get(None)

  @position.setter
  def position(self, text):
    self._config(text)

  @property
  def positions(self):
    """

    :return:
    """
    return EnumLegendPosition(self, "position")

  @property
  def inset(self):
    """
    Description:
    ------------
    Change inset legend attributes.

    This option accepts object that has the keys anchor, x, y and step.

    anchor decides the position of the legend. These anchors are available.

    Related Pages:

      https://c3js.org/reference.html#legend-inset
    """
    return self._config_get(None)

  @inset.setter
  def inset(self, text):
    self._config(text)

  @property
  def usePoint(self):
    """
    Description:
    ------------
    Return the point definition to the legend.

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Legend.usePoint
    """
    return self._config_get(False)

  @usePoint.setter
  def usePoint(self, flag):
    self._config(flag)


class OptionsTooltip(Options):

  @property
  def show(self):
    """
    Description:
    ------------
    Show or hide tooltip.

    Related Pages:

      https://c3js.org/reference.html#tooltip-show
    """
    return self._config_get(None)

  @show.setter
  def show(self, val):
    self._config(val)

  @property
  def grouped(self):
    """
    Description:
    ------------
    Set if tooltip is grouped or not for the data points.

    Related Pages:

      https://c3js.org/reference.html#tooltip-grouped
    """
    return self._config_get(True)

  @grouped.setter
  def grouped(self, flag):
    self._config(flag)

  @property
  def position(self):
    """
    Description:
    ------------
    Set custom position for the tooltip.

    This option can be used to modify the tooltip position by returning object that has top and left.

    Related Pages:

      https://c3js.org/reference.html#tooltip-position
    """
    return self._config_get(None)

  @position.setter
  def position(self, val):
    self._config(val)

  @property
  def contents(self):
    """
    Description:
    ------------
    Set custom HTML for the tooltip.

    Specified function receives data, defaultTitleFormat, defaultValueFormat and color of the data point to show.
    If tooltip.grouped is true, data includes multiple data points.

    Related Pages:

      https://c3js.org/reference.html#tooltip-contents
    """
    return self._config_get(None)

  @contents.setter
  def contents(self, val):
    self._config(val)

  @property
  def horizontal(self):
    """
    Description:
    ------------
    Show the tooltips based on the horizontal position of the mouse.

    Related Pages:

      https://c3js.org/reference.html#tooltip-horizontal
    """
    return self._config_get(None)

  @horizontal.setter
  def horizontal(self, flag):
    self._config(flag)


class OptionsSubchart(Options):

  @property
  def show(self):
    """
    Description:
    ------------
    Show sub chart on the bottom of the chart.

    Related Pages:

      https://c3js.org/reference.html#subchart-show
    """
    return self._config_get(None)

  @show.setter
  def show(self, val):
    self._config(val)

  @property
  def axis(self):
    """
    Description:
    ------------

    :rtype: OptionsGrid
    """
    return self._config_sub_data("axis", OptionsGrid)


class OptionsZoom(Options):
  @property
  def enabled(self):
    """
    Description:
    ------------
    Enable zooming.

    Related Pages:

      https://c3js.org/reference.html#zoom-enabled
    """
    return self._config_get(None)

  @enabled.setter
  def enabled(self, val):
    self._config(val)

  @property
  def type(self):
    """
    Description:
    ------------
    There are two types of zoom behavior: 'scroll' and 'drag'.

    Related Pages:

      https://c3js.org/reference.html#zoom-type
    """
    return self._config_get(None)

  @type.setter
  def type(self, val):
    self._config(val)

  @property
  def rescale(self):
    """
    Description:
    ------------
    Enable to rescale after zooming.

    If true set, y domain will be updated according to the zoomed region.

    Related Pages:

      https://c3js.org/reference.html#zoom-rescale
    """
    return self._config_get(None)

  @rescale.setter
  def rescale(self, val):
    self._config(val)

  @property
  def extent(self):
    """
    Description:
    ------------
    Change zoom extent.

    Related Pages:

      https://c3js.org/reference.html#zoom-extent
    """
    return self._config_get(None)

  @extent.setter
  def extent(self, val):
    self._config(val)

  def onzoom(self, jsFncs, profile=None):
    """
    Description:
    ------------
    Set callback that is called when the chart is zooming.

    Specified function receives the zoomed domain.

    Related Pages:

      https://c3js.org/reference.html#zoom-onzoom

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function (value){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)

  def onzoomstart(self, jsFncs, profile=None):
    """
    Description:
    ------------
    Set callback that is called when zooming starts.

    Specified function receives the zoom event.

    Related Pages:

      https://c3js.org/reference.html#zoom-onzoomstart

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function (value){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)

  def onzoomend(self, jsFncs, profile=None):
    """
    Description:
    ------------
    Set callback that is called when zooming ends.

    Specified function receives the zoomed domain.

    Related Pages:

      https://c3js.org/reference.html#zoom-onzoomend

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function (value){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)


class OptionsPoints(Options):

  @property
  def show(self):
    """
    Description:
    ------------
    Whether to show each point in line.

    Related Pages:

      https://c3js.org/reference.html#point-show
    """
    return self._config_get(None)

  @show.setter
  def show(self, flag):
    self._config(flag)

  @property
  def r(self):
    """
    Description:
    ------------
    The radius size of each point.

    Related Pages:

      https://c3js.org/reference.html#point-r
    """
    return self._config_get(None)

  @r.setter
  def r(self, num):
    self._config(num)

  @property
  def focus(self):
    """
    Description:
    ------------

    """
    return self._config_get(None)

  @focus.setter
  def focus(self, val):
    self._attrs["focus"] = {"expand": val, 'enabled': True}

  @property
  def select(self):
    """
    Description:
    ------------

    """
    return self._config_get(None)

  @select.setter
  def select(self, val):
    self._config(val)

  @property
  def pattern(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Point.CombinationPoints
    """
    return self._config_get(None)

  @pattern.setter
  def pattern(self, vals):
    if not self.component.name.startswith("Billboard"):
      logging.critical(
        "Incompatible Option | point.pattern | %s | Not available for this component" % self.component.name)
    else:
      self._config(vals)


class OptionsPadding(Options):

  @property
  def top(self):
    """
    Description:
    ------------
    The padding on the top of the chart.

    Related Pages:

      https://c3js.org/samples/options_padding.html
      https://c3js.org/reference.html#padding-top
    """
    return self._config_get(None)

  @top.setter
  def top(self, num):
    self._config(num)

  @property
  def left(self):
    """
    Description:
    ------------
    Change padding for the chart.

    Related Pages:

      https://c3js.org/samples/options_padding.html
      https://c3js.org/reference.html#padding-left
    """
    return self._config_get(None)

  @left.setter
  def left(self, num):
    self._config(num)

  @property
  def right(self):
    """
    Description:
    ------------
    Change padding for the chart.

    Related Pages:

      https://c3js.org/samples/options_padding.html
      https://c3js.org/reference.html#padding-right
    """
    return self._config_get(None)

  @right.setter
  def right(self, num):
    self._config(num)

  @property
  def bottom(self):
    """
    Description:
    ------------
    Change padding for the chart.

    Related Pages:

      https://c3js.org/samples/options_padding.html
      https://c3js.org/reference.html#padding-bottom
    """
    return self._config_get(None)

  @bottom.setter
  def bottom(self, num):
    self._config(num)


class OptionsSize(Options):

  @property
  def height(self):
    """
    Description:
    ------------
    The desired height of the chart element.

    If this option is not specified, the height of the chart will be calculated by the size of the parent element
    it's appended to.

    Related Pages:

      https://c3js.org/reference.html#size-height
    """
    return self._config_get(None)

  @height.setter
  def height(self, num):
    self._config(num)

  @property
  def width(self):
    """
    Description:
    ------------
    The desired width of the chart element.

    If this option is not specified, the width of the chart will be calculated by the size of the parent element
    it's appended to.

    Related Pages:

      https://c3js.org/reference.html#size-width
    """
    return self._config_get(None)

  @width.setter
  def width(self, num):
    self._config(num)


class OptionsLabel(Options):

  @property
  def text(self):
    """
    Description:
    ------------

    """
    return self._config_get(None)

  @text.setter
  def text(self, text):
    self._config(text)

  @property
  def position(self):
    """
    Description:
    ------------

    """
    return self._config_get(None)

  @position.setter
  def position(self, text):
    self._config(text)

  def format(self, jsFunc, profile=None):
    """
    Set formatter for the label on each donut piece.

    Related Pages:

      https://c3js.org/reference.html#donut-label-format

    :param jsFunc:
    :param profile:
    """
    pass


class OptionsPieLabel(OptionsLabel):
  @property
  def show(self):
    """
    Description:
    ------------
    Show or hide label on each pie piece.

    Related Pages:

      https://c3js.org/reference.html#pie-label-show
    """
    return self._config_get(None)

  @show.setter
  def show(self, flag):
    self._config(flag)

  @property
  def ratio(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.LabelRatio
    """
    return self._config_get(None)

  @ratio.setter
  def ratio(self, num):
    self._config(num)

  @property
  def threshold(self):
    """
    Description:
    ------------
    Set threshold to show/hide labels.

    Related Pages:

      https://c3js.org/reference.html#pie-label-threshold
    """
    return self._config_get(0.05)

  @threshold.setter
  def threshold(self, num):
    self._config(num)


class OptionsDonutLabel(OptionsPieLabel):

  @property
  def ratio(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#DonutChartOptions.LabelRatio
    """
    return self._config_get()

  @ratio.setter
  def ratio(self, num):
    self._config(num)


class OptionLines(Options):

  @property
  def value(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Style.StyleForGrid
    """
    return self._config_get()

  @value.setter
  def value(self, num):
    self._config(num)

  @property
  def css_class(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Style.StyleForGrid
    """
    return self._config_get()

  @css_class.setter
  def css_class(self, css_id):
    self._config(css_id)

  @property
  def text(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Style.StyleForGrid
    """
    return self._config_get()

  @text.setter
  def text(self, value):
    self._config(value)

  @property
  def position(self):
    """
    Description:
    ------------
    Show additional grid lines along x axis.

    Related Pages:

      https://c3js.org/reference.html#grid-x-lines
    """
    return self._config_get(None)

  @position.setter
  def position(self, val):
    self._config(val)

  @property
  def positions(self):
    return EnumTextPosition(self, "position")


class OptionsAxis(Options):

  @property
  def label(self):
    """
    Description:
    ------------

    :rtype: OptionsLabel
    """
    return self._config_sub_data("label", OptionsLabel)

  @property
  def center(self):
    """
    Description:
    ------------

    """
    return self._config_get(0)

  @center.setter
  def center(self, num):
    self._config(num)

  @property
  def categories(self):
    """
    Description:
    ------------
    Set category names on category axis.

    This must be an array that includes category names in string. If category names are included in the date by data.x
    option, this is not required.

    Related Pages:

      https://c3js.org/reference.html#axis-x-categories
    """
    return self._config_get([])

  @categories.setter
  def categories(self, values):
    self._config(values)

  @property
  def inverted(self):
    """
    Description:
    ------------

    """
    return self._config_get(False)

  @inverted.setter
  def inverted(self, flag):
    self._config(flag)

  @property
  def localtime(self):
    """
    Description:
    ------------
    Set how to treat the timezone of x values.

    If true, treat x value as localtime. If false, convert to UTC internally.

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Axis.XAxisTimezone
      https://c3js.org/reference.html#axis-x-localtime
    """
    return self._config_get(True)

  @localtime.setter
  def localtime(self, flag):
    self._config(flag)

  @property
  def type(self):
    """
    Description:
    ------------
    Set type of x axis.

    Related Pages:

      https://c3js.org/reference.html#axis-x-type
    """
    return self._config_get(None)

  @type.setter
  def type(self, val):
    self._config(val)

  @property
  def types(self):
    """
    Description:
    ------------
    Set type of x axis.

    Related Pages:

      https://c3js.org/reference.html#axis-x-type
    """
    return EnumAxisTypes(self, "type")

  @property
  def show(self):
    """
    Description:
    ------------
    Show or hide x axis.

    Related Pages:

      https://c3js.org/reference.html#axis-x-show
    """
    return self._config_get(None)

  @show.setter
  def show(self, val):
    self._config(val)

  @property
  def min(self):
    """
    Description:
    ------------
    Set min value of x axis range.

    Related Pages:

      https://c3js.org/reference.html#axis-x-min
    """
    return self._config_get(None)

  @min.setter
  def min(self, val):
    self._config(val)

  @property
  def max(self):
    """
    Description:
    ------------
    Set max value of x axis range.

    Related Pages:

      https://c3js.org/reference.html#axis-x-max
    """
    return self._config_get(None)

  @max.setter
  def max(self, val):
    self._config(val)

  @property
  def height(self):
    """
    Description:
    ------------
    Set height of x axis.

    Related Pages:

      https://c3js.org/reference.html#axis-x-height
    """
    return self._config_get(None)

  @height.setter
  def height(self, val):
    self._config(val)

  @property
  def extend(self):
    """
    Description:
    ------------
    Set default extent for subchart and zoom. This can be an array or function that returns an array.

    Related Pages:

      https://c3js.org/reference.html#axis-x-extent
    """
    return self._config_get(None)

  @extend.setter
  def extend(self, values):
    self._config(values)

  @property
  def tick(self):
    """
    Description:
    ------------

    :rtype: OptionTick
    """
    return self._config_sub_data("tick", OptionTick)

  @property
  def padding(self):
    """
    Description:
    ------------
    Set padding for the selected axis.

    Related Pages:

      https://c3js.org/reference.html#axis-x-padding

    :rtype: OptionPadding
    """
    return self._config_sub_data("padding", OptionPadding)

  def add_lines(self, value, class_css=None, text=None):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Style.StyleForGrid

    Attributes:
    ----------
    :param value: Number
    :param class_css: String. Optional.
    :param text: String. Optional.

    :rtype: OptionLines
    """
    line = self._config_sub_data_enum("lines", OptionLines)
    line.value = value
    if class_css is not None:
      line.class_css = class_css
    if text is not None:
      line.text = text
    return line

  @property
  def text(self):
    """
    Description:
    ------------

    :rtype: OptionsText
    """
    return self._config_sub_data("text", OptionsText)


class OptionsSelection(Options):
  @property
  def enabled(self):
    """
    Description:
    -----------
    Set data selection enabled.

    If this option is set true, we can select the data points and get/set its state of selection by API (e.g. select,
    unselect, selected).

    Related Pages:

      https://c3js.org/reference.html#data-selection-enabled
    """
    return self._config_get(None)

  @enabled.setter
  def enabled(self, val):
    self._config(val)

  @property
  def grouped(self):
    """
    Description:
    ------------
    Set grouped selection enabled.

    If this option set true, multiple data points that have same x value will be selected by one selection.

    Related Pages:

      https://c3js.org/reference.html#data-selection-grouped
    """
    return self._config_get(False)

  @grouped.setter
  def grouped(self, val):
    self._config(val)

  @property
  def multiple(self):
    """
    Description:
    ------------
    Set multiple data points selection enabled.

    If this option set true, multiple data points can have the selected state at the same time.
    If false set, only one data point can have the selected state and the others will be unselected when the new
    data point is selected.

    Related Pages:

      https://c3js.org/reference.html#data-selection-multiple
    """
    return self._config_get(None)

  @multiple.setter
  def multiple(self, flag):
    self._config(flag)

  @property
  def draggable(self):
    """
    Description:
    ------------
    Enable to select data points by dragging.

    If this option set true, data points can be selected by dragging.

    Related Pages:

      https://c3js.org/reference.html#data-selection-draggable
    """
    return self._config_get(None)

  @draggable.setter
  def draggable(self, val):
    self._config(val)

  def isselectable(self, jsFuncs, profile=None):
    """
    Description:
    ------------
    Set a callback for each data point to determine if it's selectable or not.

    Related Pages:

      https://c3js.org/reference.html#data-selection-isselectable
    """
    pass


class OptionsEmpty(Options):

  @property
  def label(self):
    """
    Description:
    ------------
    Set text displayed when empty data.

    Related Pages:

      https://c3js.org/reference.html#data-empty-label-text

    :rtype: OptionsLabel
    """
    return self._config_sub_data("label", OptionsLabel)


class OptionsStack(Options):
  @property
  def normalize(self):
    """
    Description:
    ------------
    Set the stacking to be normalized

    For stacking, the `data.groups` option should be set and have positive values.
    The yAxis will be set in percentage value (0 ~ 100%).

    Related Pages:

      https://c3js.org/reference.html#data-stack-normalize
    """
    return self._config_get(False)

  @normalize.setter
  def normalize(self, flag):
    self._config(flag)


class OptionsData(Options):
  component_properties = ("columns", "types", 'colors')

  @property
  def x(self):
    """
    Description:
    ------------
    Specify the key of x values in the data.

    Related Pages:

      https://c3js.org/reference.html#data-x
    """
    return self._config_get(None)

  @x.setter
  def x(self, val):
    self._config(val)

  @property
  def xs(self):
    """
    Description:
    ------------
    Specify the keys of the x values for each data.

    Related Pages:

      https://c3js.org/reference.html#data-xs
    """
    return self._config_get(None)

  @xs.setter
  def xs(self, val):
    self._config(val)

  @property
  def xFormat(self):
    """
    Description:
    ------------
    Set a format to parse string specified as x.

    Related Pages:

      https://c3js.org/reference.html#data-xFormat
    """
    return self._config_get(None)

  @xFormat.setter
  def xFormat(self, val):
    self._config(val)

  @property
  def names(self):
    """
    Description:
    ------------
    Set custom data name.

    Related Pages:

      https://c3js.org/reference.html#data-names
    """
    return self._config_get(None)

  @names.setter
  def names(self, val):
    self._config(val)

  @property
  def classes(self):
    """
    Description:
    ------------
    Set custom data class.

    Related Pages:

      https://c3js.org/reference.html#data-classes
    """
    return self._config_get(None)

  @classes.setter
  def classes(self, values):
    self._config(values)

  @property
  def groups(self):
    """
    Description:
    ------------
    Set groups for the data for stacking.

    Related Pages:

      https://c3js.org/reference.html#data-groups
    """
    return self._config_get(None)

  @groups.setter
  def groups(self, val):
    self._config(val)

  @property
  def axes(self):
    """
    Description:
    ------------
    Set y axis the data related to. y and y2 can be used.

    Related Pages:

      https://c3js.org/reference.html#data-axes
    """
    return self._config_get(None)

  @axes.setter
  def axes(self, val):
    self._config(val)

  @property
  def type(self):
    """
    Description:
    ------------
    Set chart type at once.

    Related Pages:

      https://c3js.org/reference.html#data-type
    """
    return self._config_get(None)

  @type.setter
  def type(self, val):
    self._config(val)

  @property
  def types(self):
    """
    Description:
    -----------
    This setting overwrites data.type setting:
    line, spline, step, area...

    Related Pages:

      https://c3js.org/reference.html#data-types
    """
    return self._config_get({})

  @types.setter
  def types(self, val):
    self._config(val)

  @property
  def labels(self):
    """
    Description:
    ------------
    Show labels on each data points.

    Related Pages:

      https://c3js.org/reference.html#data-labels
    """
    return self._config_get(None)

  @labels.setter
  def labels(self, val):
    self._config(val)

  @property
  def order(self):
    """
    Description:
    ------------
    Define the order of the data.

    Related Pages:

      https://c3js.org/reference.html#data-order
    """
    return self._config_get("desc")

  @order.setter
  def order(self, val):
    self._config(val)

  def color(self, jsFunc, profile=None):
    """
    Set color converter function.

    Related Pages:

      https://c3js.org/reference.html#data-color

    :param jsFunc:
    :param profile:
    """
    pass

  @property
  def colors(self):
    """
    Description:
    ------------
    Set color for each data.

    Related Pages:

      https://c3js.org/reference.html#data-colors
    """
    return self._config_get({})

  @colors.setter
  def colors(self, val):
    self._config(val)

  @property
  def columns(self):
    """
    Description:
    ------------
    Load data from a multidimensional array, with each element containing an array consisting of a
    datum name and associated data values.

    Related Pages:

      https://c3js.org/reference.html#data-columns
    """
    return self._config_get([])

  @columns.setter
  def columns(self, values):
    self._config(values)

  @property
  def rows(self):
    """
    Description:
    ------------
    Load data from a multidimensional array, with the first element containing the data names,
    the following containing related data in that order.

    Related Pages:

      https://c3js.org/reference.html#data-rows
    """
    return self._config_get([])

  @rows.setter
  def rows(self, values):
    self._config(values)

  @property
  def hide(self):
    """
    Description:
    ------------
    Hide each data when the chart appears.

    If true specified, all of data will be hidden. If multiple ids specified as an array, those will be hidden.

    Related Pages:

      https://c3js.org/reference.html#data-hide
    """
    return self._config_get(False)

  @hide.setter
  def hide(self, val):
    self._config(val)

  @property
  def selection(self):
    """
    Description:
    ------------

    :rtype: OptionsSelection
    """
    return self._config_sub_data("selection", OptionsSelection)

  @property
  def stack(self):
    """
    Description:
    ------------

    Related Pages:

      https://c3js.org/reference.html#data-stack-normalize

    :rtype: OptionsStack
    """
    return self._config_sub_data("stack", OptionsStack)

  @property
  def empty(self):
    """
    Description:
    ------------

    :rtype: OptionsEmpty
    """
    return self._config_sub_data("empty", OptionsEmpty)

  def onclick(self, jsFuncs, profile=False):
    """
    Description:
    ------------
    Set a callback for click event on each data point.

    Related Pages:

      https://c3js.org/reference.html#data-onclick

    Attributes:
    ----------
    :param jsFuncs: String | List. The Javascript functions
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(){%s}" % JsUtils.jsConvertFncs(jsFuncs, toStr=True, profile=profile), js_type=True)

  def onmouseover(self, jsFuncs, profile=False):
    """
    Description:
    ------------
    Set a callback for mouseover event on each data point.

    Related Pages:

      https://c3js.org/reference.html#data-onmouseover

    Attributes:
    ----------
    :param jsFuncs: String | List. The Javascript functions
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(){%s}" % JsUtils.jsConvertFncs(jsFuncs, toStr=True, profile=profile), js_type=True)

  def onmouseout(self, jsFuncs, profile=False):
    """
    Description:
    ------------
    Set a callback for mouseout event on each data point.

    Related Pages:

      https://c3js.org/reference.html#data-onmouseout

    Attributes:
    ----------
    :param jsFuncs: String | List. The Javascript functions
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(){%s}" % JsUtils.jsConvertFncs(jsFuncs, toStr=True, profile=profile), js_type=True)

  @property
  def url(self):
    """
    Description:
    ------------
    Load a CSV or JSON file from a URL.
    Note that this will not work if loading via the "file://" protocol as the most browsers will block XMLHTTPRequests.

    Related Pages:

      https://c3js.org/reference.html#data-url
    """
    return self._config_get(None)

  @url.setter
  def url(self, val):
    self._config(val)


class OptionEpochs(Options):

  @property
  def epochs(self):
    """
    Description:
    ------------

    """
    return self._config_get(None)

  @epochs.setter
  def epochs(self, val):
    self._config(val)


class OptionCulling(Options):

  @property
  def max(self):
    """
    Description:
    ------------
    The number of tick texts will be adjusted to less than this value.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-culling-max
    """
    return self._config_get(10)

  @max.setter
  def max(self, num):
    self._config(num)


class OptionTick(Options):

  @property
  def centered(self):
    """
    Description:
    ------------
    Centerise ticks on category axis.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-centered
    """
    return self._config_get(True)

  @centered.setter
  def centered(self, flag):
    self._config(flag)

  @property
  def autorotate(self):
    """
    Description:
    ------------

    Related Pages:


    """
    return self._config_get(None)

  @autorotate.setter
  def autorotate(self, flag):
    self._config(flag)

  def format(self, jsFuncs, profile=None):
    """
    A function to format tick value. Format string is also available for timeseries data.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-format

    :param jsFuncs:
    :param profile:
    """
    pass

  @property
  def formats(self):
    return EnumTickFormat(self, "format")

  @property
  def count(self):
    """
    Description:
    ------------
    Set the number of y axis ticks.

    Related Pages:

      https://c3js.org/reference.html#axis-y-tick-count
    """
    return self._config_get(None)

  @count.setter
  def count(self, val):
    self._config(val)

  @property
  def default(self):
    """
    Description:
    ------------
    This option set the default value for y axis when there is no data on init.

    Related Pages:

      https://c3js.org/reference.html#axis-y-default
    """
    return self._config_get(None)

  @default.setter
  def default(self, values):
    self._config(values)

  @property
  def fit(self):
    """
    Description:
    ------------
    Fit x axis ticks.

    If true set, the ticks will be positioned nicely.
    If false set, the ticks will be positioned according to x value of the data points.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-fit
    """
    return self._config_get(True)

  @fit.setter
  def fit(self, flag):
    self._config(flag)

  @property
  def multiline(self):
    """
    Description:
    ------------
    Enable multiline.

    If this option is set true, when a tick's text on the x-axis is too long,
    it splits the text into multiple lines in order to avoid text overlapping.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-multiline
    """
    return self._config_get(True)

  @multiline.setter
  def multiline(self, flag):
    self._config(flag)

  @property
  def multilineMax(self):
    """
    Description:
    ------------
    If this option is set and is above 0, the number of lines will be adjusted to less than this value and
    tick's text is ellipsified.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-multilineMax
    """
    return self._config_get(0)

  @multilineMax.setter
  def multilineMax(self, flag):
    self._config(flag)

  @property
  def rotate(self):
    """
    Description:
    ------------
    Rotate x axis tick text.

    If you set negative value, it will rotate to opposite direction.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-rotate
    """
    return self._config_get(0)

  @rotate.setter
  def rotate(self, num):
    self._config(num)

  @property
  def outer(self):
    """
    Description:
    ------------
    Show x axis outer tick.

    Related Pages:

      https://c3js.org/reference.html#axis-y-tick-outer
    """
    return self._config_get(True)

  @outer.setter
  def outer(self, val):
    self._config(val)

  @property
  def values(self):
    """
    Description:
    ------------
    Set y axis tick values manually.

    Related Pages:

      https://c3js.org/reference.html#axis-y-tick-values
    """
    return self._config_get(None)

  @values.setter
  def values(self, values):
    self._config(values)

  @property
  def culling(self):
    """
    Description:
    ------------
    Setting for culling ticks.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-culling

    :rtype: OptionCulling
    """
    return self._config_sub_data("culling", OptionCulling)

  @property
  def stepSize(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Axis.StepSizeForYAxis
    """
    return self._config_get()

  @stepSize.setter
  def stepSize(self, num):
    self._config(num)

  @property
  def text(self):
    """
    Related Pages:

      https://naver.github.io/billboard.js/demo/#Axis.XAxisTickPosition
    """
    return self._config_sub_data("text", OptionsText)


class OptionX(Options):

  @property
  def tick(self):
    """
    Description:
    ------------

    :rtype: OptionTick
    """
    return self._config_sub_data("tick", OptionTick)


class OptionAxis(Options):

  @property
  def rotated(self):
    """
    Switch x and y axis position.

    Related Pages:

      https://c3js.org/reference.html#axis-rotated
    """
    return self._config_get()

  @rotated.setter
  def rotated(self, val):
    self._config(val)

  @property
  def x(self):
    """
    Description:
    ------------

    Related Pages:

      https://c3js.org/reference.html#axis-y2-show
      https://c3js.org/reference.html#axis-x-show

    :rtype: OptionsAxis
    """
    return self._config_sub_data("x", OptionsAxis)

  @property
  def y(self):
    """
    Description:
    ------------

    Related Pages:

      https://c3js.org/reference.html#axis-y2-show

    :rtype: OptionsAxis
    """
    return self._config_sub_data("y", OptionsAxis)

  @property
  def y2(self):
    """
    Description:
    ------------

    Related Pages:

      https://c3js.org/reference.html#axis-y2-show

    :rtype: OptionsAxis
    """
    return self._config_sub_data("y2", OptionsAxis)


class OptionsRegion(Options):

  @property
  def axis(self):
    return self._config_get()

  @axis.setter
  def axis(self, val):
    self._config(val)

  @property
  def start(self):
    return self._config_get()

  @start.setter
  def start(self, num):
    self._config(num)

  @property
  def end(self):
    return self._config_get()

  @end.setter
  def end(self, num):
    self._config(num)

  @property
  def class_css(self):
    return self._config_get(name="class")

  @class_css.setter
  def class_css(self, val):
    self._config(val, name="class")


class OptionsColor(Options):

  @property
  def pattern(self):
    """
    Description:
    ------------
    Set custom color pattern.

    Related Pages:

      https://naver.github.io/billboard.js/demo/#ChartOptions.ColorPattern
      https://c3js.org/reference.html#color-pattern
    """
    return self._config_get()

  @pattern.setter
  def pattern(self, colors):
    self._config(colors)

  def tiles(self, jsFuncs, profile=None):
    raise Exception("Not yet implemented")


class OptionsPosition(Options):

  @property
  def x(self):
    """
    Description:
    ------------

    """
    return self._config_get([])

  @x.setter
  def x(self, num):
    self._config(num)

  @property
  def y(self):
    """
    Description:
    ------------

    """
    return self._config_get([])

  @y.setter
  def y(self, num):
    self._config(num)


class OptionsText(Options):

  @property
  def show(self):
    """
    Description:
    ------------

    """
    return self._config_get([])

  @show.setter
  def show(self, flag):
    self._config(flag)

  @property
  def position(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Axis.XAxisTickPosition
    """
    return self._config_sub_data("position", OptionsPosition)


class OptionsTitle(Options):

  @property
  def text(self):
    """
    Description:
    ------------

    """
    return self._config_get([])

  @text.setter
  def text(self, value):
    if isinstance(value, list):
      value = "\n".join(value)
    self._config(value)


class OptionsRender(Options):

  @property
  def lazy(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#ChartOptions.LazyRender
    """
    return self._config_get([])

  @lazy.setter
  def lazy(self, flag):
    self._config(flag)

  @property
  def observe(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#ChartOptions.LazyRender
    """
    return self._config_get([])

  @observe.setter
  def observe(self, flag):
    self._config(flag)


class OptionStep(Options):

  @property
  def type(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.StepChart
    """
    return self._config_get()

  @type.setter
  def type(self, value):
    self._config(value)

  @property
  def types(self):
    return EnumStepTypes(self, "type")


class OptionsLine(Options):

  @property
  def classes(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Style.StyleForLines
    """
    return self._config_get([])

  @classes.setter
  def classes(self, values):
    self._config(values)

  @property
  def connectNull(self):
    """
    Description:
    ------------
    Set if null data point will be connected or not.

    If true set, the region of null data will be connected without any data point.
    If false set, the region of null data will not be connected and get empty.

    Related Pages:

      https://c3js.org/reference.html#line-connectNull
    """
    return self._config_get(False)

  @connectNull.setter
  def connectNull(self, flag):
    self._config(flag)

  @property
  def step(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.StepChart
    """
    return self._config_sub_data("step", OptionStep)


class OptionsInteraction(Options):

  @property
  def enabled(self):
    """
    Description:
    ------------
    Indicate if the chart should have interactions.

    If false is set, all of interactions (showing/hiding tooltip, selection, mouse events, etc) will be disabled.

    Related Pages:

      https://c3js.org/reference.html#interaction-enabled
    """
    return self._config_get(True)

  @enabled.setter
  def enabled(self, flag):
    self._config(flag)


class OptionsTransition(Options):

  @property
  def duration(self):
    """
    Description:
    ------------
    Set duration of transition (in milliseconds) for chart animation.

    Related Pages:

      https://c3js.org/reference.html#transition-duration
    """
    return self._config_get(350)

  @duration.setter
  def duration(self, num):
    self._config(num)


class C3(OptChart.OptionsChart):

  @property
  def bindto(self):
    """
    Description:
    ------------
    The CSS selector or the element which the chart will be set to. D3 selection object can be specified.
    If other chart is set already, it will be replaced with the new one (only one chart can be set in one element).

    Related Pages:

      https://c3js.org/reference.html#bindto
    """
    return self._config_get([])

  @bindto.setter
  def bindto(self, cols):
    self._config(cols)

  @property
  def axis(self):
    """
    Description:
    ------------

    :return: OptionAxis
    """
    return self._config_sub_data("axis", OptionAxis)

  @property
  def legend(self):
    """
    Description:
    ------------
    Set visibility of legend.

    Related Pages:

      https://c3js.org/samples/options_legend.html

    :return: OptionsLegend
    """
    return self._config_sub_data("legend", OptionsLegend)

  @property
  def point(self):
    """
    Description:
    ------------

    :rtype: OptionsPoints
    """
    return self._config_sub_data("point", OptionsPoints)

  @property
  def grid(self):
    """
    Description:
    ------------

    :rtype: OptionsGrid
    """
    return self._config_sub_data("grid", OptionsGrid)

  @property
  def zoom(self):
    """
    Description:
    ------------
    Zoom by mouse wheel event and slide by drag.

    Related Pages:

      https://c3js.org/samples/interaction_zoom.html

    :rtype: OptionsZoom
    """
    return self._config_sub_data("zoom", OptionsZoom)

  @property
  def subchart(self):
    """
    Description:
    ------------
    Show sub chart for zoom and selection range.

    Related Pages:

      https://c3js.org/samples/options_subchart.html

    :rtype: OptionsSubchart
    """
    return self._config_sub_data("subchart", OptionsSubchart)

  @property
  def data(self):
    """
    Description:
    ------------

    Related Pages:

      https://c3js.org/reference.html#data-url

    :rtype: OptionsData
    """
    return self._config_sub_data("data", OptionsData)

  def add_region(self, axis, start=None, end=None, class_css=None):
    """
    Description:
    ------------
    Show rectangles inside the chart.

    Related Pages:

      https://c3js.org/samples/region.html
      https://c3js.org/reference.html#regions

    Attributes:
    ----------
    :param axis:
    :param start:
    :param end:
    :param class_css:

    :rtype: OptionsRegion
    """
    region = self._config_sub_data_enum("regions", OptionsRegion)
    region.axis = axis
    if start is not None:
      region.start = start
    if end is not None:
      region.end = end
    if class_css is not None:
      region.class_css = class_css
    return region

  def add_region_per_series(self, name, start=None, end=None, class_css=None):
    """
    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChartWithRegions

    :param name:
    :param start:
    :param end:
    :param class_css:
    """

  def size(self):
    """
    Description:
    ------------
    Set chart size in px.

    Related Pages:

      https://c3js.org/samples/options_size.html

    :rtype: OptionsSize
    """
    return self._config_sub_data("size", OptionsSize)

  def padding(self):
    """
    Description:
    ------------
    Change padding for the chart.

    Related Pages:

      https://c3js.org/samples/options_size.html

    :rtype: OptionsPadding
    """
    return self._config_sub_data("padding", OptionsPadding)

  @property
  def title(self):
    """
    Description:
    ------------
    Add a title to the chart.

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Title.MultilinedTitle

    :rtype: OptionsTitle
    """
    return self._config_sub_data("title", OptionsTitle)

  @property
  def color(self):
    """
    Description:
    ------------
    Add a title to the chart.

    Related Pages:

      https://naver.github.io/billboard.js/demo/#ChartOptions.ColorPattern
      https://naver.github.io/billboard.js/demo/#ChartOptions.ColorTiles3

    :rtype: OptionsTitle
    """
    return self._config_sub_data("color", OptionsColor)

  @property
  def render(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#ChartOptions.LazyRender

    :rtype: OptionsRender
    """
    return self._config_sub_data("render", OptionsRender)

  @property
  def line(self):
    """
    Description:
    ------------

    :rtype: OptionsLine
    """
    return self._config_sub_data("line", OptionsLine)

  @property
  def interaction(self):
    """
    Description:
    ------------
    Configure the interaction on the chart.

    Related Pages:

      https://c3js.org/reference.html#interaction-enabled

    :rtype: OptionsInteraction
    """
    return self._config_sub_data("interaction", OptionsInteraction)

  @property
  def transition(self):
    """
    Description:
    ------------
    Set duration of transition (in milliseconds) for chart animation.

    Related Pages:

      https://c3js.org/reference.html#transition-duration

    :rtype: OptionsTransition
    """
    return self._config_sub_data("transition", OptionsTransition)

  def oninit(self, jsFuncs, profile=None):
    """
    Set a callback to execute when the chart is initialized.

    https://c3js.org/reference.html#oninit

    :param jsFuncs:
    :param profile:
    """
    pass

  def onrendered(self, jsFuncs, profile=None):
    """
    Set a callback which is executed when the chart is rendered.
    Basically, this callback will be called in each time when the chart is redrawed.

    Related Pages:

      https://c3js.org/reference.html#onrendered

    :param jsFuncs:
    :param profile:
    """
    pass

  def onmouseover(self, jsFuncs, profile=None):
    """
    Set a callback to execute when mouse enters the chart.

    Related Pages:

      https://c3js.org/reference.html#onmouseover

    :param jsFuncs:
    :param profile:
    """
    pass

  def onmouseover(self, jsFuncs, profile=None):
    """
    Set a callback to execute when mouse leaves the chart.

    Related Pages:

      https://c3js.org/reference.html#onmouseout

    :param jsFuncs:
    :param profile:
    """
    pass

  def onmouseover(self, jsFuncs, profile=None):
    """
    Set a callback to execute when user resizes the screen.

    Related Pages:

      https://c3js.org/reference.html#onresize

    :param jsFuncs:
    :param profile:
    """
    pass

  def onresized(self, jsFuncs, profile=None):
    """
    Set a callback to execute when screen resize finished.

    Related Pages:

      https://c3js.org/reference.html#onresized

    :param jsFuncs:
    :param profile:
    """
    pass


class OptionsDonut(Options):

  @property
  def title(self):
    """
    Description:
    ------------
    Set title of donut chart.

    Related Pages:

      https://c3js.org/reference.html#donut-title
      https://naver.github.io/billboard.js/demo/#DonutChartOptions.LabelRatio
      https://naver.github.io/billboard.js/demo/#DonutChartOptions.MultilineTitle
    """
    return self._config_get()

  @title.setter
  def title(self, text):
    if isinstance(text, list):
      text = "\n".join(text)
    self._config(text)

  @property
  def label(self):
    """
    Description:
    ------------

    :rtype: OptionsDonutLabel
    """
    return self._config_sub_data("label", OptionsDonutLabel)

  def format(self):
    pass

  @property
  def startingAngle(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#DonutChartOptions.StartingAngle
    """
    return self._config_get()

  @startingAngle.setter
  def startingAngle(self, num):
    self._config(num)

  @property
  def padAngle(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#DonutChartOptions.padAngle
    """
    return self._config_get()

  @padAngle.setter
  def padAngle(self, num):
    self._config(num)

  @property
  def width(self):
    """
    Description:
    ------------
    Set width of donut chart.

    Related Pages:

      https://c3js.org/reference.html#donut-width
    """
    return self._config_get("auto")

  @width.setter
  def width(self, num):
    self._config(num)


class C3Donut(C3):

  @property
  def donut(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#DonutChartOptions.LabelRatio

    :rtype: OptionsDonut
    """
    return self._config_sub_data("donut", OptionsDonut)


class OptionsGauge(Options):

  @property
  def label(self):
    """
    Description:
    ------------

    :rtype: OptionsDonutLabel
    """
    return self._config_sub_data("label", OptionsDonutLabel)

  def format(self):
    pass

  @property
  def units(self):
    """
    Description:
    ------------
    Set width of donut chart.

    Related Pages:

      https://c3js.org/reference.html#gauge-units
    """
    return self._config_get()

  @units.setter
  def units(self, value):
    self._config(value)

  @property
  def max(self):
    """
    Description:
    ------------
    Set max value of the gauge.

    Related Pages:

      https://c3js.org/reference.html#gauge-max
    """
    return self._config_get(100)

  @max.setter
  def max(self, num):
    self._config(num)

  @property
  def min(self):
    """
    Description:
    ------------
    Set min value of the gauge.

    Related Pages:

      https://c3js.org/reference.html#gauge-min
    """
    return self._config_get(0)

  @min.setter
  def min(self, num):
    self._config(num)

  @property
  def width(self):
    """
    Description:
    ------------
    Set width of donut chart.

    Related Pages:

      https://c3js.org/reference.html#donut-width
    """
    return self._config_get("auto")

  @width.setter
  def width(self, num):
    self._config(num)


class C3Gauge(C3):
  @property
  def gauge(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#DonutChartOptions.LabelRatio

    :rtype: OptionsGauge
    """
    return self._config_sub_data("gauge", OptionsGauge)


class OptionsPieExpand(Options):

  @property
  def rate(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.ExpandRate
    """
    return self._config_get()

  @rate.setter
  def rate(self, num):
    self._config(num)


class OptionsPie(Options):

  @property
  def expand(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.ExpandRate

    :rtype: OptionsPieExpand
    """
    return self._config_sub_data("expand", OptionsPieExpand)

  @property
  def innerRadius(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.InnerRadius
    """
    return self._config_get()

  @innerRadius.setter
  def innerRadius(self, value):
    self._config(value)

  @property
  def outerRadius(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.OuterRadius
    """
    return self._config_get()

  @outerRadius.setter
  def outerRadius(self, value):
    self._config(value)

  @property
  def padAngle(self):
    """
    Description:
    ------------


    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.PadAngle
      https://c3js.org/reference.html#pie-padAngle
    """
    return self._config_get(0)

  @padAngle.setter
  def padAngle(self, num):
    self._config(num)

  @property
  def padding(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.Padding
    """
    return self._config_get()

  @padding.setter
  def padding(self, value):
    self._config(value)

  @property
  def startingAngle(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.StartingAngle
    """
    return self._config_get()

  @startingAngle.setter
  def startingAngle(self, value):
    self._config(value)

  @property
  def label(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.LabelRatio

    :rtype: OptionsPieLabel
    """
    return self._config_sub_data("label", OptionsPieLabel)


class C3Pie(C3):

  @property
  def pie(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.ExpandRate

    :rtype: OptionsPie
    """
    return self._config_sub_data("pie", OptionsPie)


class OptionsRadar(Options):

  def axis(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarAxis

    :rtype: OptionsAxis
    """
    return self._config_sub_data("axis", OptionsAxis)

  @property
  def size(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarSize

    :rtype: OptionsSize
    """
    return self._config_sub_data("size", OptionsSize)


class OptionsLevel(Options):

  @property
  def depth(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarLevel
    """
    return self._config_get()

  @depth.setter
  def depth(self, num):
    self._config(num)

  @property
  def text(self):
    return self._config_sub_data("text", OptionsText)

  @property
  def show(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarLevel
    """
    return self._config_get(True)

  @show.setter
  def show(self, flag):
    self._config(flag)

  def format(self, jsFunc, profile=None):
    pass


class OptionsDirection(Options):

  @property
  def clockwise(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.RadarChart
    """
    return self._config_get()

  @clockwise.setter
  def clockwise(self, flag):
    self._config(flag)


class C3Radar(C3):

  @property
  def radar(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarAxis

    :rtype: OptionsRadar
    """
    return self._config_sub_data("radar", OptionsRadar)

  @property
  def level(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarAxis

    :rtype: OptionsLevel
    """
    return self._config_sub_data("level", OptionsLevel)

  @property
  def direction(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.RadarChart

    :rtype: OptionsDirection
    """
    return self._config_sub_data("direction", OptionsDirection)


class OptionsArea(Options):

  @property
  def zerobased(self):
    """
    Description:
    ------------
    Set if min or max value will be 0 on area chart.

    Related Pages:

      https://c3js.org/reference.html#area-zerobased
    """
    return self._config_get(True)

  @zerobased.setter
  def zerobased(self, flag):
    self._config(flag)


class C3Area(C3):

  @property
  def area(self):
    """
    Description:
    ------------

    Related Pages:

      https://c3js.org/reference.html#area-zerobased

    :rtype: OptionsArea
    """
    return self._config_sub_data("area", OptionsArea)


class OptionsBar(Options):

  @property
  def width(self):
    """
    Description:
    ------------

    Related Pages:

      https://c3js.org/reference.html#bar-width
    """
    return self._config_get("auto")

  @width.setter
  def width(self, num):
    self._config(num)

  @property
  def zerobased(self):
    """
    Description:
    ------------
    Set if min or max value will be 0 on bar chart.

    Related Pages:

      https://c3js.org/reference.html#bar-zerobased
    """
    return self._config_get(True)

  @zerobased.setter
  def zerobased(self, flag):
    self._config(flag)


class C3Bar(C3):

  @property
  def bar(self):
    """
    Description:
    ------------

    Related Pages:

      https://c3js.org/reference.html#bar-width

    :rtype: OptionsArea
    """
    return self._config_sub_data("bar", OptionsBar)


class OptionsSpline(Options):

  @property
  def interpolation(self):
    """

    :rtype: OptionStep
    """
    return self._config_sub_data("interpolation", OptionStep)


class C3Spline(C3):

  @property
  def spline(self):
    """

    :rtype: OptionsSpline
    """
    return self._config_sub_data("spline", OptionsSpline)


class OptionsBubble(Options):

  @property
  def maxR(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BubbleDimensionChart
    """
    return self._config_get()

  @maxR.setter
  def maxR(self, num):
    self._config(num)

  @property
  def minR(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BubbleDimensionChart
    """
    return self._config_get()

  @minR.setter
  def minR(self, num):
    self._config(num)


class C3Bubble(C3):

  @property
  def bubble(self):
    """
    Description:
    ------------

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BubbleDimensionChart

    :rtype: OptionsBubble
    """
    return self._config_sub_data("bubble", OptionsBubble)


class C3Stanford(OptChart.OptionsChart):

  @property
  def axis(self):
    """
    Description:
    ------------

    :return: OptionAxis
    """
    return self._config_sub_data("axis", OptionAxis)

  @property
  def point(self):
    """
    Description:
    ------------

    :rtype: OptionsPoints
    """
    return self._config_sub_data("point", OptionsPoints)

  @property
  def grid(self):
    """
    Description:
    ------------

    :rtype: OptionsGrid
    """
    return self._config_sub_data("grid", OptionsGrid)

  @property
  def zoom(self):
    """
    Description:
    ------------

    :rtype: OptionsZoom
    """
    return self._config_sub_data("zoom", OptionsZoom)
