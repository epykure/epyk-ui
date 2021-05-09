#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options
from epyk.core.js import JsUtils
from epyk.core.html.options import OptChart


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


class OptionsGridLine(Options):
  @property
  def value(self):
    """
    Description:
    ------------
    Show additional grid lines along x axis.

    Related Pages:

      https://c3js.org/reference.html#grid-x-lines
    """
    return self._config_get(None)

  @value.setter
  def value(self, val):
    self._config(val)

  @property
  def text(self):
    """
    Description:
    ------------
    Show additional grid lines along x axis.

    Related Pages:

      https://c3js.org/reference.html#grid-x-lines
    """
    return self._config_get(None)

  @text.setter
  def text(self, text):
    self._config(text)

  @property
  def css_class(self):
    """
    Description:
    ------------
    Show additional grid lines along x axis.

    Related Pages:

      https://c3js.org/reference.html#grid-x-lines
    """
    return self._config_get(None, name="class")

  @css_class.setter
  def css_class(self, val):
    self._config(val, name="class")

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

  @property
  def lines(self):
    """
    Description:
    ------------
    Show additional grid lines along x axis.

    Related Pages:

      https://c3js.org/reference.html#grid-x-lines

    :rtype: OptionsGridLine
    """
    return self.sub_data_enum("lines", OptionsGridLine)


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
  def type(self):
    """
    Description:
    ------------

    """
    return self._config_get(None)

  @type.setter
  def type(self, val):
    self._config(val)

  @property
  def show(self):
    """
    Description:
    ------------

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

    """
    return self._config_get(None)

  @min.setter
  def min(self, val):
    self._config(val)

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

    :rtype: OptionTick
    """
    return self._config_sub_data("padding", OptionPadding)


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

    """
    return self._config_get(None)

  @grouped.setter
  def grouped(self, val):
    self._config(val)

  @property
  def multiple(self):
    """
    Description:
    ------------

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

    """
    return self._config_get(None)

  @draggable.setter
  def draggable(self, val):
    self._config(val)

  @property
  def isselectable(self):
    """
    Description:
    ------------

    """
    return self._config_get(None)

  @isselectable.setter
  def isselectable(self, js_funcs):
    self._attrs["isselectable"] = js_funcs


class OptionsData(Options):
  component_properties = ("columns", "types", 'colors')

  @property
  def x(self):
    """
    Description:
    ------------

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

    """
    return self._config_get(None)

  @names.setter
  def names(self, val):
    self._config(val)

  @property
  def groups(self):
    """
    Description:
    ------------

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

    """
    return self._config_get(None)

  @order.setter
  def order(self, val):
    self._config(val)

  @property
  def colors(self):
    """
    Description:
    ------------

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

    """
    return self._config_get([])

  @columns.setter
  def columns(self, values):
    self._config(values)

  @property
  def hide(self):
    """
    Description:
    ------------
    """
    return self._config_get(None)

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

  def onclick(self, jsFncs, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs: String | List. The Javascript functions
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function(){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)


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

    """
    return self._config_get(None)

  @max.setter
  def max(self, num):
    self._config(num)


class OptionTick(Options):

  @property
  def format(self):
    """
    Description:
    ------------
    Set formatter for y axis tick text.

    This option accepts d3.format object as well as a function you define.

    Related Pages:

      https://c3js.org/reference.html#axis-y-tick-format
    """
    return self._config_get(None)

  @format.setter
  def format(self, val):
    self._config(val)

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
    return self._config_get(None)

  @fit.setter
  def fit(self, flag):
    self._config(flag)

  @property
  def multiline(self):
    """
    Description:
    ------------

    Related Pages:


    """
    return self._config_get(None)

  @multiline.setter
  def multiline(self, flag):
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
    return self._config_get(None)

  @rotate.setter
  def rotate(self, num):
    self._config(num)

  @property
  def outer(self):
    """
    Description:
    ------------

    Related Pages:

      https://c3js.org/reference.html#axis-y-tick-outer
    """
    return self._config_get(None)

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


class C3(OptChart.OptionsChart):

  @property
  def bindto(self):
    """
    Description:
    ------------

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

  @property
  def data(self):
    """
    Description:
    ------------

    :rtype: OptionsData
    """
    return self._config_sub_data("data", OptionsData)


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
