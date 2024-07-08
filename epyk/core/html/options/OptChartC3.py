#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from epyk.core.py import types as etypes

from epyk.core.html.options import Options
from epyk.core.html.options import Enums
from epyk.core.js.packages import packageImport
from epyk.core.js import JsUtils
from epyk.core.html.options import OptChart


class OptionsChartSharedC3(OptChart.OptionsChartShared):

    def x_format(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        raise NotImplementedError()

    def x_format_money(self, symbol: str = "", digit: int = 0, thousand_sep: str = ".", decimal_sep: str = ",",
                       fmt: str = "%v %s", factor: float = None, alias: str = ""):
        self.component.options.axis.x.tick.formats.toMoney(symbol, digit, thousand_sep, decimal_sep, fmt, factor, alias)
        return self

    def x_format_number(self, factor: float = 1, alias: str = None, digits: int = 0, thousand_sep: str = "."):
        self.component.options.axis.x.tick.formats.scale(factor, alias, digits, thousand_sep)
        return self

    def x_label(self, value: str):
        """Set the label of the x-axis.

    `Package Doc <https://c3js.org/reference.html#axis-y-label>`_

    :param value: The axis label
    """
        self.component.options.axis.x.label.text = value
        return self

    def x_tick_count(self, num: int):
        self.component.options.axis.x.tick.count = num
        return self

    def y_format(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        raise NotImplementedError()

    def y_format_money(self, symbol: str = "", digit: int = 0, thousand_sep: str = ".", decimal_sep: str = ",",
                       fmt: str = "%v %s", factor: float = None, alias: str = ""):
        self.component.options.axis.y.tick.formats.toMoney(symbol, digit, thousand_sep, decimal_sep, fmt, factor, alias)
        return self

    def y_format_number(self, factor: float = 1, alias: str = None, digits: int = 0, thousand_sep: str = "."):
        self.component.options.axis.x.tick.formats.scale(factor, alias, digits, thousand_sep)
        return self

    def y_label(self, value: str):
        """Set the label of the y-axis.

    :param value: The axis label.
    """
        self.component.options.axis.y.label.text = value
        return self

    def y_tick_count(self, num: int):
        self.component.options.axis.y.tick.count = num
        return self


class EnumAxisTypes(Enums):

    def timeseries(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Chart.TimeseriesChart>`_
    """
        self._set_value()

    def log(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Axis.LogScales>`_
    """
        self._set_value()

    def indexed(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Axis.LogScales>`_
    """
        self._set_value()

    def category(self, categories: list = None):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Axis.CategoryAxis>`_
    """
        self._set_value()
        if categories is not None:
            self.__option._config(categories, "categories")


class EnumTickFormat(Enums):

    def format(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Chart.TimeseriesChart>`_
    """
        self._set_value(value='''
      function(index, categoryName){var label = new Date(categoryName);
        return label.getFullYear() +"-"+ (label.getMonth() + 1) +"-"+ label.getDate()}''', js_type=True)

    @packageImport("accounting")
    def toNumber(self, digit: int = 0, thousand_sep: str = "."):
        """Convert to number using the accounting Javascript module.

    `Package Doc <https://openexchangerates.github.io/accounting.js/>`_

    :param digit: The number of digit to be displayed
    :param thousand_sep: The thousand symbol separator
    """
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        self._set_value(value="function(value) {return accounting.formatNumber(value, %s, %s)}" % (
            digit, thousand_sep), js_type=True)
        return self

    @packageImport("accounting")
    def toMoney(self, symbol: str = "", digit: int = 0, thousand_sep: str = ".", decimal_sep: str = ",",
                fmt: str = "%v %s", factor: float = None, alias: str = ""):
        """

    :param symbol: Optional.
    :param digit: Optional.
    :param thousand_sep: Optional.
    :param decimal_sep: Optional.
    :param fmt: Optional.
    :param factor: Optional.
    :param alias: Optional.
    """
        symbol = JsUtils.jsConvertData(symbol, None)
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
        if not alias:
            alias = {1000: "k", 1000000: "m"}.get(factor, alias)
        self._set_value(value="function (value){return accounting.formatMoney(value/%s, %s, %s, %s, %s, '%s')}" % (
            factor or 1, "'%s'+ %s" % (alias, symbol), digit, thousand_sep, decimal_sep, fmt), js_type=True)

    @packageImport("accounting")
    def scale(self, factor: float = 1000, alias: str = None, digits: int = 0, thousand_sep: str = "."):
        """

    :param factor:
    :param alias:
    :param digits:
    :param thousand_sep:
    """
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        alias = alias or {1000: "k", 1000000: "m"}.get(factor, "")
        self._set_value(value="function(value) {return accounting.formatNumber(value/%s, %s, %s) + '%s'}" % (
            factor, digits, thousand_sep, alias), js_type=True)
        return self

    def yy_mm_dd(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Chart.TimeseriesChart>`_
    """
        self._set_value(value="%Y-%m-%d")

    def e_b_y(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Axis.XAxisTickFitting>`_
    """
        self._set_value(value="%e %b %y")

    def timestamp(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Axis.XAxisTickAutorotate>`_
    """
        self._set_value(value="%m-%d-%Y %H:%M:%S")


class EnumStepTypes(Enums):

    def linear(self):
        """Set type of curve interpolation.

    `Package Doc <https://c3js.org/reference.html#spline-interpolation-type>`_
    """
        self._set_value()

    def linear_closed(self):
        """Set type of curve interpolation.

    `Package Doc <https://c3js.org/reference.html#spline-interpolation-type>`_
    """
        self._set_value("linear-closed")

    def basis(self):
        """ Set type of curve interpolation.

    `Package Doc <https://c3js.org/reference.html#spline-interpolation-type>`_
    """
        self._set_value()

    def basis_open(self):
        """Set type of curve interpolation.

    `Package Doc <https://c3js.org/reference.html#spline-interpolation-type>`_
    """
        self._set_value("basis-open")

    def basis_closed(self):
        """Set type of curve interpolation.

    `Package Doc <https://c3js.org/reference.html#spline-interpolation-type>`_
    """
        self._set_value("basis-closed")

    def bundle(self):
        """Set type of curve interpolation.

    `Package Doc <https://c3js.org/reference.html#spline-interpolation-type>`_
    """
        self._set_value()

    def cardinal(self):
        """Set type of curve interpolation.

    `Package Doc <https://c3js.org/reference.html#spline-interpolation-type>`_
    """
        self._set_value()

    def cardinal_open(self):
        """Set type of curve interpolation.

    `Package Doc <https://c3js.org/reference.html#spline-interpolation-type>`_
    """
        self._set_value(value="cardinal-open")

    def cardinal_closed(self):
        """Set type of curve interpolation.

    `Package Doc <https://c3js.org/reference.html#spline-interpolation-type>`_
    """
        self._set_value(value="cardinal-closed")

    def monotone(self):
        """Set type of curve interpolation.

    `Package Doc <https://c3js.org/reference.html#spline-interpolation-type>`_
    """
        self._set_value()

    def step(self):
        """Set type of curve interpolation.

    `Package Doc <https://c3js.org/reference.html#spline-interpolation-type>`_
    """
        self._set_value()

    def step_before(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Chart.StepChart>`_
    """
        self._set_value(value="step-before")

    def step_after(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Chart.StepChart>`_
    """
        self._set_value(value="step-after")


class EnumTextPosition(Enums):

    def middle(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Grid.OptionalXGridLines>`_
    """
        self._set_value()

    def start(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Grid.OptionalXGridLines>`_
    """
        self._set_value()


class EnumLegendPosition(Enums):

    def right(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Legend.LegendPosition>`_
    """
        self._set_value()

    def left(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Legend.LegendPosition>`_
    """
        self._set_value()


class OptionPadding(Options):

    @property
    def bottom(self):
        return self._config_get(None)

    @bottom.setter
    def bottom(self, val):
        self._config(val)


class OptionLines(Options):

    @property
    def value(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Style.StyleForGrid>`_
    """
        return self._config_get()

    @value.setter
    def value(self, num):
        self._config(num)

    @property
    def css_class(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Style.StyleForGrid>`_
    """
        return self._config_get()

    @css_class.setter
    def css_class(self, css_id):
        self._config(css_id)

    @property
    def text(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Style.StyleForGrid>`_
    """
        return self._config_get()

    @text.setter
    def text(self, value):
        self._config(value)

    @property
    def position(self):
        """Show additional grid lines along x axis.

    `Package Doc <https://c3js.org/reference.html#grid-x-lines>`_
    """
        return self._config_get(None)

    @position.setter
    def position(self, val):
        self._config(val)

    @property
    def positions(self) -> EnumTextPosition:
        return EnumTextPosition(self, "position")


class OptionsGridAxis(Options):

    @property
    def show(self):
        """Show grids along x axis.

    `Package Doc <https://c3js.org/reference.html#grid-x-show>`_
    """
        return self._config_get(None)

    @show.setter
    def show(self, val):
        self._config(val)

    def add_lines(self, value, css_class=None, text=None, position=None) -> OptionLines:
        """Add lines to the chart.

    `Package Doc <https://naver.github.io/billboard.js/demo/#Style.StyleForGrid>`_

    :param value: Number. The coordinate for the line.
    :param css_class: String. Optional. The CSS class reference.
    :param text: String. Optional. The label on the line.
    :param position: String. Optional.
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
    def x(self) -> OptionsGridAxis:
        """Property to the grid x axis"""
        return self._config_sub_data("x", OptionsGridAxis)

    @property
    def y(self) -> OptionsGridAxis:
        """Property to the grid y axis"""
        return self._config_sub_data("y", OptionsGridAxis)


class OptionsLegend(Options):

    @property
    def show(self):
        """Show or hide legend.

    `Package Doc <https://c3js.org/reference.html#legend-show>`_
    """
        return self._config_get(None)

    @show.setter
    def show(self, val):
        self._config(val)

    @property
    def hide(self):
        """Show or hide legend.

    `Package Doc <https://c3js.org/reference.html#legend-hide>`_
    """
        return self._config_get(False)

    @hide.setter
    def hide(self, flag: bool):
        self._config(flag)

    @property
    def position(self):
        """Change the position of legend.
    Currently bottom, right and inset are supported.

    `Package Doc <https://c3js.org/reference.html#legend-position>`_
    """
        return self._config_get(None)

    @position.setter
    def position(self, text):
        self._config(text)

    @property
    def positions(self) -> EnumLegendPosition:
        """

    :return:
    """
        return EnumLegendPosition(self, "position")

    @property
    def inset(self):
        """Change inset legend attributes.
    This option accepts object that has the keys anchor, x, y and step.
    anchor decides the position of the legend. These anchors are available.

    `Package Doc <https://c3js.org/reference.html#legend-inset>`_
    """
        return self._config_get(None)

    @inset.setter
    def inset(self, text):
        self._config(text)

    @property
    def usePoint(self):
        """Return the point definition to the legend.

    `Package Doc <https://naver.github.io/billboard.js/demo/#Legend.usePoint>`_
    """
        return self._config_get(False)

    @usePoint.setter
    def usePoint(self, flag):
        self._config(flag)


class OptionsTooltip(Options):

    @property
    def show(self):
        """Show or hide tooltip.

    `Package Doc <https://c3js.org/reference.html#tooltip-show>`_
    """
        return self._config_get(None)

    @show.setter
    def show(self, val):
        self._config(val)

    @property
    def grouped(self):
        """Set if tooltip is grouped or not for the data points.

    `Package Doc <https://c3js.org/reference.html#tooltip-grouped>`_
    """
        return self._config_get(True)

    @grouped.setter
    def grouped(self, flag):
        self._config(flag)

    @property
    def position(self):
        """Set custom position for the tooltip.
    This option can be used to modify the tooltip position by returning object that has top and left.

    `Package Doc <https://c3js.org/reference.html#tooltip-position>`_
    """
        return self._config_get(None)

    @position.setter
    def position(self, val):
        self._config(val)

    @property
    def contents(self):
        """Set custom HTML for the tooltip.
    Specified function receives data, defaultTitleFormat, defaultValueFormat and color of the data point to show.
    If tooltip.grouped is true, data includes multiple data points.

    `Package Doc <https://c3js.org/reference.html#tooltip-contents>`_
    """
        return self._config_get(None)

    @contents.setter
    def contents(self, val):
        self._config(val)

    @property
    def horizontal(self):
        """Show the tooltips based on the horizontal position of the mouse.

    `Package Doc <https://c3js.org/reference.html#tooltip-horizontal>`_
    """
        return self._config_get(None)

    @horizontal.setter
    def horizontal(self, flag: bool):
        self._config(flag)


class OptionsSubchart(Options):

    @property
    def show(self):
        """Show sub chart on the bottom of the chart.

    `Package Doc <https://c3js.org/reference.html#subchart-show>`_
    """
        return self._config_get(None)

    @show.setter
    def show(self, val):
        self._config(val)

    @property
    def axis(self) -> OptionsGrid:
        """

    """
        return self._config_sub_data("axis", OptionsGrid)


class OptionsZoom(Options):

    @property
    def enabled(self):
        """Enable zooming.

    `Package Doc <https://c3js.org/reference.html#zoom-enabled>`_
    """
        return self._config_get(None)

    @enabled.setter
    def enabled(self, val):
        self._config(val)

    @property
    def type(self):
        """There are two types of zoom behavior: 'scroll' and 'drag'.

    `Package Doc <https://c3js.org/reference.html#zoom-type>`_
    """
        return self._config_get(None)

    @type.setter
    def type(self, val):
        self._config(val)

    @property
    def rescale(self):
        """Enable to rescale after zooming.
    If true set, y domain will be updated according to the zoomed region.

    `Package Doc <https://c3js.org/reference.html#zoom-rescale>`_
    """
        return self._config_get(None)

    @rescale.setter
    def rescale(self, val):
        self._config(val)

    @property
    def extent(self):
        """Change zoom extent.

    `Package Doc <https://c3js.org/reference.html#zoom-extent>`_
    """
        return self._config_get(None)

    @extent.setter
    def extent(self, val):
        self._config(val)

    def onzoom(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        """Set callback that is called when the chart is zooming.
    Specified function receives the zoomed domain.

    `Package Doc <https://c3js.org/reference.html#zoom-onzoom>`_

    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
        self._config("function (value){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile),
                     js_type=True)

    def onzoomstart(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        """Set callback that is called when zooming starts.
    Specified function receives the zoom event.

    `Package Doc <https://c3js.org/reference.html#zoom-onzoomstart>`_

    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
        self._config("function (value){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile),
                     js_type=True)

    def onzoomend(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        """Set callback that is called when zooming ends.
    Specified function receives the zoomed domain.

    `Package Doc <https://c3js.org/reference.html#zoom-onzoomend>`_

    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
        self._config("function (value){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile),
                     js_type=True)


class OptionsPoints(Options):

    @property
    def show(self):
        """Whether to show each point in line.

    `Package Doc <https://c3js.org/reference.html#point-show>`_
    """
        return self._config_get(None)

    @show.setter
    def show(self, flag: bool):
        self._config(flag)

    @property
    def r(self):
        """The radius size of each point.

    `Package Doc <https://c3js.org/reference.html#point-r>`_
    """
        return self._config_get(None)

    @r.setter
    def r(self, num: float):
        self._config(num)

    @property
    def focus(self):
        """

    """
        return self._config_get(None)

    @focus.setter
    def focus(self, val):
        self._attrs["focus"] = {"expand": val, 'enabled': True}

    @property
    def select(self):
        """

    """
        return self._config_get(None)

    @select.setter
    def select(self, val):
        self._config(val)

    @property
    def pattern(self):
        """

    `Package Doc <https://naver.github.io/billboard.js/demo/#Point.CombinationPoints>`_
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
        """The padding on the top of the chart.

    `Package Doc <https://c3js.org/samples/options_padding.html>`_
    `Padding Doc <https://c3js.org/reference.html#padding-top>`_
    """
        return self._config_get(None)

    @top.setter
    def top(self, num):
        self._config(num)

    @property
    def left(self):
        """Change padding for the chart.

    `Package Doc <https://c3js.org/samples/options_padding.html>`_
    `Padding Doc <https://c3js.org/reference.html#padding-left>`_
    """
        return self._config_get(None)

    @left.setter
    def left(self, num):
        self._config(num)

    @property
    def right(self):
        """Change padding for the chart.

    `Package Doc <https://c3js.org/samples/options_padding.html>`_
    `Padding Doc <https://c3js.org/reference.html#padding-right>`_
    """
        return self._config_get(None)

    @right.setter
    def right(self, num):
        self._config(num)

    @property
    def bottom(self):
        """Change padding for the chart.

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
        """The desired height of the chart element.
    If this option is not specified, the height of the chart will be calculated by the size of the parent element
    it's appended to.

    `Package Doc <https://c3js.org/reference.html#size-height>`_
    """
        return self._config_get(None)

    @height.setter
    def height(self, num):
        self._config(num)

    @property
    def width(self):
        """The desired width of the chart element.
    If this option is not specified, the width of the chart will be calculated by the size of the parent element
    it's appended to.

    `Package Doc <https://c3js.org/reference.html#size-width>`_
    """
        return self._config_get(None)

    @width.setter
    def width(self, num):
        self._config(num)


class OptionsLabel(Options):

    @property
    def text(self):
        """

    """
        return self._config_get(None)

    @text.setter
    def text(self, text):
        self._config(text)

    @property
    def position(self):
        """

    """
        return self._config_get(None)

    @position.setter
    def position(self, text):
        self._config(text)

    def format(self, js_funcs, profile=None):
        """ Set formatter for the label on each donut piece.

    Related Pages:

      https://c3js.org/reference.html#donut-label-format

    :param js_funcs:
    :param profile:
    """
        pass


class OptionsPieLabel(OptionsLabel):
    @property
    def show(self):
        """ Show or hide label on each pie piece.

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

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.LabelRatio
    """
        return self._config_get(None)

    @ratio.setter
    def ratio(self, num):
        self._config(num)

    @property
    def threshold(self):
        """ Set threshold to show/hide labels.

    Related Pages:

      https://c3js.org/reference.html#pie-label-threshold
    """
        return self._config_get(0.05)

    @threshold.setter
    def threshold(self, num: float):
        self._config(num)


class OptionsDonutLabel(OptionsPieLabel):

    @property
    def ratio(self):
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#DonutChartOptions.LabelRatio
    """
        return self._config_get()

    @ratio.setter
    def ratio(self, num):
        self._config(num)


class OptionCulling(Options):

    @property
    def max(self):
        """ The number of tick texts will be adjusted to less than this value.

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
        """ Centerise ticks on category axis.

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

    Related Pages:


    """
        return self._config_get(None)

    @autorotate.setter
    def autorotate(self, flag):
        self._config(flag)

    def format(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        """
    A function to format tick value. Format string is also available for timeseries data.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-format

    :param js_funcs:
    :param profile:
    """
        pass

    @property
    def formats(self):
        return EnumTickFormat(self, "format")

    @property
    def count(self):
        """ Set the number of y axis ticks.

    Related Pages:

      https://c3js.org/reference.html#axis-y-tick-count
    """
        return self._config_get(None)

    @count.setter
    def count(self, val):
        self._config(val)

    @property
    def default(self):
        """ This option set the default value for y axis when there is no data on init.

    Related Pages:

      https://c3js.org/reference.html#axis-y-default
    """
        return self._config_get(None)

    @default.setter
    def default(self, values):
        self._config(values)

    @property
    def fit(self):
        """ Fit x axis ticks.

    If true set, the ticks will be positioned nicely.
    If false set, the ticks will be positioned according to x value of the data points.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-fit
    """
        return self._config_get(True)

    @fit.setter
    def fit(self, flag: bool):
        self._config(flag)

    @property
    def multiline(self):
        """ Enable multiline.

    If this option is set true, when a tick's text on the x-axis is too long,
    it splits the text into multiple lines in order to avoid text overlapping.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-multiline
    """
        return self._config_get(True)

    @multiline.setter
    def multiline(self, flag: bool):
        self._config(flag)

    @property
    def multilineMax(self):
        """ If this option is set and is above 0, the number of lines will be adjusted to less than this value and
    tick's text is ellipsified.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-multilineMax
    """
        return self._config_get(0)

    @multilineMax.setter
    def multilineMax(self, flag: bool):
        self._config(flag)

    @property
    def rotate(self):
        """ Rotate x-axis tick text.

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
        """ Show x-axis outer tick.

    Related Pages:

      https://c3js.org/reference.html#axis-y-tick-outer
    """
        return self._config_get(True)

    @outer.setter
    def outer(self, val: bool):
        self._config(val)

    @property
    def values(self):
        """ Set y-axis tick values manually.

    Related Pages:

      https://c3js.org/reference.html#axis-y-tick-values
    """
        return self._config_get(None)

    @values.setter
    def values(self, values):
        self._config(values)

    @property
    def culling(self) -> OptionCulling:
        """ Setting for culling ticks.

    Related Pages:

      https://c3js.org/reference.html#axis-x-tick-culling
    """
        return self._config_sub_data("culling", OptionCulling)

    @property
    def stepSize(self):
        """

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


class OptionsAxis(Options):

    @property
    def label(self) -> OptionsLabel:
        """
    """
        return self._config_sub_data("label", OptionsLabel)

    @property
    def center(self):
        """

    """
        return self._config_get(0)

    @center.setter
    def center(self, num: float):
        self._config(num)

    @property
    def categories(self):
        """ Set category names on category axis.

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

    """
        return self._config_get(False)

    @inverted.setter
    def inverted(self, flag: bool):
        self._config(flag)

    @property
    def localtime(self):
        """ Set how to treat the timezone of x values.

    If true, treat x value as localtime. If false, convert to UTC internally.

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Axis.XAxisTimezone
      https://c3js.org/reference.html#axis-x-localtime
    """
        return self._config_get(True)

    @localtime.setter
    def localtime(self, flag: bool):
        self._config(flag)

    @property
    def type(self):
        """ Set type of x-axis.

    Related Pages:

      https://c3js.org/reference.html#axis-x-type
    """
        return self._config_get(None)

    @type.setter
    def type(self, val):
        self._config(val)

    @property
    def types(self):
        """ Set type of x-axis.

    Related Pages:

      https://c3js.org/reference.html#axis-x-type
    """
        return EnumAxisTypes(self, "type")

    @property
    def show(self):
        """ Show or hide x-axis.

    Related Pages:

      https://c3js.org/reference.html#axis-x-show
    """
        return self._config_get(None)

    @show.setter
    def show(self, val):
        self._config(val)

    @property
    def min(self):
        """ Set min value of x-axis range.

    Related Pages:

      https://c3js.org/reference.html#axis-x-min
    """
        return self._config_get(None)

    @min.setter
    def min(self, val):
        self._config(val)

    @property
    def max(self):
        """ Set max value of x-axis range.

    Related Pages:

      https://c3js.org/reference.html#axis-x-max
    """
        return self._config_get(None)

    @max.setter
    def max(self, val):
        self._config(val)

    @property
    def height(self):
        """ Set height of x-axis.

    Related Pages:

      https://c3js.org/reference.html#axis-x-height
    """
        return self._config_get(None)

    @height.setter
    def height(self, val):
        self._config(val)

    @property
    def extend(self):
        """ Set default extent for subchart and zoom. This can be an array or function that returns an array.

    Related Pages:

      https://c3js.org/reference.html#axis-x-extent
    """
        return self._config_get(None)

    @extend.setter
    def extend(self, values):
        self._config(values)

    @property
    def tick(self) -> OptionTick:
        """

    """
        return self._config_sub_data("tick", OptionTick)

    @property
    def padding(self) -> OptionPadding:
        """ Set padding for the selected axis.

    Related Pages:

      https://c3js.org/reference.html#axis-x-padding
    """
        return self._config_sub_data("padding", OptionPadding)

    def add_lines(self, value, class_css=None, text=None) -> OptionLines:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Style.StyleForGrid

    :param value: Number
    :param class_css: String. Optional.
    :param text: String. Optional.
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

    :rtype: OptionsText
    """
        return self._config_sub_data("text", OptionsText)


class OptionsSelection(Options):

    @property
    def enabled(self):
        """  Set data selection enabled.

    If this option is set true, we can select the data points and get/set its state of selection by API (e.g. select,
    unselect, selected).

    Related Pages:

      https://c3js.org/reference.html#data-selection-enabled
    """
        return self._config_get(None)

    @enabled.setter
    def enabled(self, val: bool):
        self._config(val)

    @property
    def grouped(self):
        """ Set grouped selection enabled.

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
        """ Set multiple data points selection enabled.

    If this option set true, multiple data points can have the selected state at the same time.
    If false set, only one data point can have the selected state and the others will be unselected when the new
    data point is selected.

    Related Pages:

      https://c3js.org/reference.html#data-selection-multiple
    """
        return self._config_get(None)

    @multiple.setter
    def multiple(self, flag: bool):
        self._config(flag)

    @property
    def draggable(self):
        """ Enable to select data points by dragging.

    If this option set true, data points can be selected by dragging.

    Related Pages:

      https://c3js.org/reference.html#data-selection-draggable
    """
        return self._config_get(None)

    @draggable.setter
    def draggable(self, val: bool):
        self._config(val)

    def isselectable(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        """Set a callback for each data point to determine if it's selectable or not.

        Related Pages:

          https://c3js.org/reference.html#data-selection-isselectable
        """
        pass


class OptionsEmpty(Options):

    @property
    def label(self) -> OptionsLabel:
        """Set text displayed when empty data.

        Related Pages:

          https://c3js.org/reference.html#data-empty-label-text
        """
        return self._config_sub_data("label", OptionsLabel)


class OptionsStack(Options):

    @property
    def normalize(self):
        """Set the stacking to be normalized.
        For stacking, the `data.groups` option should be set and have positive values.
        The yAxis will be set in percentage value (0 ~ 100%).

        Related Pages:

          https://c3js.org/reference.html#data-stack-normalize
        """
        return self._config_get(False)

    @normalize.setter
    def normalize(self, flag: bool):
        self._config(flag)


class OptionsData(Options):
    component_properties = ("columns", "types", 'colors')

    @property
    def x(self):
        """Specify the key of x values in the data.

        Related Pages:

          https://c3js.org/reference.html#data-x
        """
        return self._config_get(None)

    @x.setter
    def x(self, val):
        self._config(val)

    @property
    def xs(self):
        """Specify the keys of the x values for each data.

        `Package Doc <https://c3js.org/reference.html#data-xs>`_
        """
        return self._config_get(None)

    @xs.setter
    def xs(self, val):
        self._config(val)

    @property
    def xFormat(self):
        """Set a format to parse string specified as x.

        `Package Doc <https://c3js.org/reference.html#data-xFormat>`_
        """
        return self._config_get(None)

    @xFormat.setter
    def xFormat(self, val):
        self._config(val)

    @property
    def names(self):
        """Set custom data name.

        `Package Doc <https://c3js.org/reference.html#data-names>`_
        """
        return self._config_get(None)

    @names.setter
    def names(self, val):
        self._config(val)

    @property
    def classes(self):
        """Set custom data class.

        `Package Doc <https://c3js.org/reference.html#data-classes>`_
        """
        return self._config_get(None)

    @classes.setter
    def classes(self, values):
        self._config(values)

    @property
    def groups(self):
        """Set groups for the data for stacking.

        `Package Doc <https://c3js.org/reference.html#data-groups>`_
        """
        return self._config_get(None)

    @groups.setter
    def groups(self, val):
        self._config(val)

    @property
    def axes(self):
        """Set y-axis the data related to. y and y2 can be used.

        `Package Doc <https://c3js.org/reference.html#data-axes>`_
        """
        return self._config_get(None)

    @axes.setter
    def axes(self, val):
        self._config(val)

    @property
    def type(self):
        """Set chart type at once.

        `Package Doc <https://c3js.org/reference.html#data-type>`_
        """
        return self._config_get(None)

    @type.setter
    def type(self, val):
        self._config(val)

    @property
    def types(self):
        """This setting overwrites data.type setting: line, spline, step, area...

        `Package Doc <https://c3js.org/reference.html#data-types>`_
        """
        return self._config_get({})

    @types.setter
    def types(self, val):
        self._config(val)

    @property
    def labels(self):
        """Show labels on each data points.

        `Package Doc <https://c3js.org/reference.html#data-labels>`_
        """
        return self._config_get(None)

    @labels.setter
    def labels(self, val):
        self._config(val)

    @property
    def order(self):
        """ Define the order of the data.

        `Package Doc <https://c3js.org/reference.html#data-order>`_
        """
        return self._config_get("desc")

    @order.setter
    def order(self, val):
        self._config(val)

    def color(self, js_funcs, profile=None):
        """Set color converter function.

        `Package Doc <https://c3js.org/reference.html#data-color>`_

        :param js_funcs:
        :param profile:
        """
        pass

    @property
    def colors(self):
        """Set color for each data.

        `Package Doc <https://c3js.org/reference.html#data-colors>`_
        """
        return self._config_get({})

    @colors.setter
    def colors(self, val):
        self._config(val)

    @property
    def columns(self):
        """Load data from a multidimensional array, with each element containing an array consisting of a
        datum name and associated data values.

        `Package Doc <https://c3js.org/reference.html#data-columns>`_
        """
        return self._config_get([])

    @columns.setter
    def columns(self, values):
        self._config(values)

    @property
    def rows(self):
        """Load data from a multidimensional array, with the first element containing the data names,
        the following containing related data in that order.

        `Package Doc <https://c3js.org/reference.html#data-rows>`_
        """
        return self._config_get([])

    @rows.setter
    def rows(self, values):
        self._config(values)

    @property
    def hide(self):
        """ Hide each data when the chart appears.
        If true specified, all of data will be hidden. If multiple ids specified as an array, those will be hidden.

        `Package Doc <https://c3js.org/reference.html#data-hide>`_
        """
        return self._config_get(False)

    @hide.setter
    def hide(self, val: bool):
        self._config(val)

    @property
    def selection(self) -> OptionsSelection:
        """ """
        return self._config_sub_data("selection", OptionsSelection)

    @property
    def stack(self) -> OptionsStack:
        """

        `Package Doc <https://c3js.org/reference.html#data-stack-normalize>`_
        """
        return self._config_sub_data("stack", OptionsStack)

    @property
    def empty(self) -> OptionsEmpty:
        """ """
        return self._config_sub_data("empty", OptionsEmpty)

    def onclick(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = False):
        """Set a callback for click event on each data point.

        `Package Doc <https://c3js.org/reference.html#data-onclick>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        self._config("function(d, element){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

    def onmouseover(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = False):
        """Set a callback for mouse/touch over event on each data point.

        `Package Doc <https://c3js.org/reference.html#data-onmouseover>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        self._config("function(d, element){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile),
                     name="onover", js_type=True)

    def onmouseout(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = False):
        """ Set a callback for mouse/touch out event on each data point.

        `Package Doc <https://c3js.org/reference.html#data-onmouseout>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        self._config("function(d, element){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile),
                     name="onout", js_type=True)

    def onselected(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = False):
        """Set a callback for on data selection.

        `Package Doc <https://c3js.org/reference.html#data-onmouseout>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        self.selection.enabled = True
        self._config("function(d, element){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

    def onunselected(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = False):
        """Set a callback for on data selection.

        `Package Doc <https://c3js.org/reference.html#data-onmouseout>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        self.selection.enabled = True
        self._config("function(d, element){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

    @property
    def url(self):
        """ Load a CSV or JSON file from a URL.
        Note that this will not work if loading via the "file://" protocol as the most browsers will block XMLHTTPRequests.

        `Package Doc <https://c3js.org/reference.html#data-url>`_
        """
        return self._config_get(None)

    @url.setter
    def url(self, val: str):
        self._config(val)


class OptionEpochs(Options):

    @property
    def epochs(self):
        """ """
        return self._config_get(None)

    @epochs.setter
    def epochs(self, val):
        self._config(val)


class OptionX(Options):

    @property
    def tick(self) -> OptionTick:
        """ """
        return self._config_sub_data("tick", OptionTick)


class OptionAxis(Options):

    @property
    def rotated(self):
        """Switch x and y-axis position.

        `Package Doc <https://c3js.org/reference.html#axis-rotated>`_
        """
        return self._config_get()

    @rotated.setter
    def rotated(self, val):
        self._config(val)

    @property
    def x(self) -> OptionsAxis:
        """

        Related Pages:

          https://c3js.org/reference.html#axis-y2-show
          https://c3js.org/reference.html#axis-x-show
        """
        return self._config_sub_data("x", OptionsAxis)

    @property
    def y(self) -> OptionsAxis:
        """

        `Package Doc <https://c3js.org/reference.html#axis-y2-show>`_
        """
        return self._config_sub_data("y", OptionsAxis)

    @property
    def y2(self) -> OptionsAxis:
        """

        `Package Doc <https://c3js.org/reference.html#axis-y2-show>`_
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
        """Set custom color pattern.

        Related Pages:

          https://naver.github.io/billboard.js/demo/#ChartOptions.ColorPattern
          https://c3js.org/reference.html#color-pattern
        """
        return self._config_get()

    @pattern.setter
    def pattern(self, colors):
        self._config(colors)

    def tiles(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        raise NotImplementedError()


class OptionsPosition(Options):

    @property
    def x(self):
        """  """
        return self._config_get([])

    @x.setter
    def x(self, num):
        self._config(num)

    @property
    def y(self):
        """  """
        return self._config_get([])

    @y.setter
    def y(self, num):
        self._config(num)


class OptionsText(Options):

    @property
    def show(self):
        """ """
        return self._config_get([])

    @show.setter
    def show(self, flag: bool):
        self._config(flag)

    @property
    def position(self) -> OptionsPosition:
        """

        `Package Doc <https://naver.github.io/billboard.js/demo/#Axis.XAxisTickPosition>`_
        """
        return self._config_sub_data("position", OptionsPosition)


class OptionsTitle(Options):

    @property
    def text(self):
        """  """
        return self._config_get([])

    @text.setter
    def text(self, value: str):
        if isinstance(value, list):
            value = "\n".join(value)
        self._config(value)


class OptionsRender(Options):

    @property
    def lazy(self):
        """

        `Package Doc <https://naver.github.io/billboard.js/demo/#ChartOptions.LazyRender>`_
        """
        return self._config_get([])

    @lazy.setter
    def lazy(self, flag: bool):
        self._config(flag)

    @property
    def observe(self):
        """

        `Package Doc <https://naver.github.io/billboard.js/demo/#ChartOptions.LazyRender>`_
        """
        return self._config_get([])

    @observe.setter
    def observe(self, flag: bool):
        self._config(flag)


class OptionStep(Options):

    @property
    def type(self):
        """

        `Package Doc <https://naver.github.io/billboard.js/demo/#Chart.StepChart>`_
        """
        return self._config_get()

    @type.setter
    def type(self, value: str):
        self._config(value)

    @property
    def types(self):
        return EnumStepTypes(self, "type")


class OptionsLine(Options):

    @property
    def classes(self):
        """

        `Package Doc <https://naver.github.io/billboard.js/demo/#Style.StyleForLines>`_
        """
        return self._config_get([])

    @classes.setter
    def classes(self, values):
        self._config(values)

    @property
    def connectNull(self):
        """Set if null data point will be connected or not.
        If true set, the region of null data will be connected without any data point.
        If false set, the region of null data will not be connected and get empty.

        `Package Doc <https://c3js.org/reference.html#line-connectNull>`_
        """
        return self._config_get(False)

    @connectNull.setter
    def connectNull(self, flag: bool):
        self._config(flag)

    @property
    def step(self) -> OptionStep:
        """

        `Package Doc <https://naver.github.io/billboard.js/demo/#Chart.StepChart>`_
        """
        return self._config_sub_data("step", OptionStep)


class OptionsInteraction(Options):

    @property
    def enabled(self):
        """Indicate if the chart should have interactions.
        If false is set, all of interactions (showing/hiding tooltip, selection, mouse events, etc) will be disabled.

        `Package Doc <https://c3js.org/reference.html#interaction-enabled>`_
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool):
        self._config(flag)


class OptionsTransition(Options):

    @property
    def duration(self):
        """Set duration of transition (in milliseconds) for chart animation.

        `Package Doc <https://c3js.org/reference.html#transition-duration>`_
        """
        return self._config_get(350)

    @duration.setter
    def duration(self, num: int):
        self._config(num)


class C3(OptChart.OptionsChart):

    @property
    def container(self):
        """Return always the container DOM element"""
        if self.component is not None:
            return self.element

    @property
    def element(self):
        """Return always the real DOM element"""
        if self.component is not None:
            return "document.getElementById('%s')" % self.component.html_code

    @property
    def bindto(self):
        """The CSS selector or the element which the chart will be set to. D3 selection object can be specified.
        If other chart is set already, it will be replaced with the new one (only one chart can be set in one element).

        `Package Doc <https://c3js.org/reference.html#bindto>`_
        """
        return self._config_get([])

    @bindto.setter
    def bindto(self, cols):
        self._config(JsUtils.jsConvertData(cols, None), js_type=True)

    @property
    def axis(self) -> OptionAxis:
        """ """
        return self._config_sub_data("axis", OptionAxis)

    @property
    def legend(self) -> OptionsLegend:
        """Set visibility of legend.

        `Package Doc <https://c3js.org/sampl>`_
        """
        return self._config_sub_data("legend", OptionsLegend)

    @property
    def point(self) -> OptionsPoints:
        """ """
        return self._config_sub_data("point", OptionsPoints)

    @property
    def grid(self):
        """ """
        return self._config_sub_data("grid", OptionsGrid)

    @property
    def zoom(self):
        """Zoom by mouse wheel event and slide by drag.

        `Package Doc <https://c3js.org/samples/interaction_zoom.html>`_
        """
        return self._config_sub_data("zoom", OptionsZoom)

    @property
    def subchart(self):
        """Show sub chart for zoom and selection range.

        `Package Doc <https://c3js.org/samples/options_subchart.html>`_
        """
        return self._config_sub_data("subchart", OptionsSubchart)

    @property
    def data(self) -> OptionsData:
        """

        `Package Doc <https://c3js.org/reference.html#data-url>`_
        """
        return self._config_sub_data("data", OptionsData)

    def add_region(self, axis, start=None, end=None, class_css=None) -> OptionsRegion:
        """Show rectangles inside the chart.

        Related Pages:

          https://c3js.org/samples/region.html
          https://c3js.org/reference.html#regions

        :param axis:
        :param start:
        :param end:
        :param class_css:
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
        `Package Doc <https://naver.github.io/billboard.js/demo/#Chart.LineChartWithRegions>`_

        :param name:
        :param start:
        :param end:
        :param class_css:
        """

    def size(self) -> OptionsSize:
        """Set chart size in px.

        `Package Doc <https://c3js.org/samples/options_size.html>`_
        """
        return self._config_sub_data("size", OptionsSize)

    def padding(self) -> OptionsPadding:
        """Change padding for the chart.

        `Package Doc <https://c3js.org/samples/options_size.html>`_
        """
        return self._config_sub_data("padding", OptionsPadding)

    @property
    def title(self) -> OptionsTitle:
        """Add a title to the chart.

        `Package Doc <https://naver.github.io/billboard.js/demo/#Title.MultilinedTitle>`_
        """
        return self._config_sub_data("title", OptionsTitle)

    @property
    def color(self) -> OptionsColor:
        """Add a title to the chart.

        Related Pages:

          https://naver.github.io/billboard.js/demo/#ChartOptions.ColorPattern
          https://naver.github.io/billboard.js/demo/#ChartOptions.ColorTiles3
        """
        return self._config_sub_data("color", OptionsColor)

    @property
    def render(self) -> OptionsRender:
        """

        `Package Doc <https://naver.github.io/billboard.js/demo/#ChartOptions.LazyRender>`_
        """
        return self._config_sub_data("render", OptionsRender)

    @property
    def line(self) -> OptionsLine:
        """ """
        return self._config_sub_data("line", OptionsLine)

    @property
    def interaction(self) -> OptionsInteraction:
        """Configure the interaction on the chart.

        `Package Doc <https://c3js.org/reference.html#interaction-enabled>`_
        """
        return self._config_sub_data("interaction", OptionsInteraction)

    @property
    def transition(self) -> OptionsTransition:
        """Set duration of transition (in milliseconds) for chart animation.

        `Package Doc <https://c3js.org/reference.html#transition-duration>`_
        """
        return self._config_sub_data("transition", OptionsTransition)

    def oninit(self, js_funcs, profile=None):
        """Set a callback to execute when the chart is initialized.

        `Package Doc <https://c3js.org/reference.html#oninit>`_

        :param js_funcs:
        :param profile:
        """
        pass

    def onrendered(self, js_funcs, profile=None):
        """Set a callback which is executed when the chart is rendered.
        Basically, this callback will be called in each time when the chart is redrawed.

        `Package Doc <https://c3js.org/reference.html#onrendered>`_

        :param js_funcs:
        :param profile:
        """
        pass

    def onmouseover(self, js_funcs, profile=None):
        """Set a callback to execute when mouse enters the chart.

        `Package Doc <https://c3js.org/reference.html#onmouseover>`_

        :param js_funcs:
        :param profile:
        """
        pass

    def onmouseover(self, js_funcs, profile=None):
        """Set a callback to execute when mouse leaves the chart.

        `Package Doc <https://c3js.org/reference.html#onmouseout>`_

        :param js_funcs:
        :param profile:
        """
        pass

    def onmouseover(self, js_funcs, profile=None):
        """Set a callback to execute when user resizes the screen.

        `Package Doc <https://c3js.org/reference.html#onresize>`_

        :param js_funcs:
        :param profile:
        """
        pass

    def onresized(self, js_funcs, profile=None):
        """Set a callback to execute when screen resize finished.

        `Package Doc <https://c3js.org/reference.html#onresized>`_

        :param js_funcs:
        :param profile:
        """
        pass

    def createWidget(self, html_code: str, container: str = None, options: etypes.JS_DATA_TYPES = None):
        """Create a new widget derived from an existing one.
        Using this method will make the main object as a template namely it will be removed from the page scope.

        :param html_code: The widget HTML code
        :param container: The widget container. Default the body
        :param options: The specific widget options
        """
        self.component.options.managed = False
        self.component.js_code = html_code
        lib = "bb" if self.component.name == "Billboard" else 'c3'
        js_code = JsUtils.jsConvertData(self.component.js_code, None).toStr()
        if js_code.startswith("window"):
            js_code = js_code[7:-1]
        return JsUtils.jsWrap('''
(function(containerId, tag, htmlCode, jsCode, ctx, attrs){
    const newDiv = document.createElement(tag);
    Object.keys(attrs).forEach(function(key) {newDiv.setAttribute(key, attrs[key]);}); newDiv.id = htmlCode;
    if(!containerId){document.body.appendChild(newDiv)} else {document.getElementById(containerId).appendChild(newDiv)};
    window[jsCode] = %(lib)s.generate(ctx); return newDiv
})(%(container)s, "%(tag)s", %(html_code)s, %(js_code)s, %(ctx)s, %(attrs)s)''' % {
            "js_code": js_code,
            "attrs": self.component.get_attrs(css_class_names=self.component.style.get_classes(), to_str=False),
            "html_code": JsUtils.jsConvertData(html_code or self.component.html_code, None),
            "tag": self.component.tag, "ctx": self.component.options.config_js(options).toStr(), "lib": lib,
            "container": JsUtils.jsConvertData(container, None)
        })


class OptionsDonut(Options):

    @property
    def title(self):
        """Set title of donut chart.

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
    def label(self) -> OptionsDonutLabel:
        """
    """
        return self._config_sub_data("label", OptionsDonutLabel)

    def format(self):
        pass

    @property
    def startingAngle(self):
        """

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

    Related Pages:

      https://naver.github.io/billboard.js/demo/#DonutChartOptions.padAngle
    """
        return self._config_get()

    @padAngle.setter
    def padAngle(self, num):
        self._config(num)

    @property
    def width(self):
        """ Set width of donut chart.

    Related Pages:

      https://c3js.org/reference.html#donut-width
    """
        return self._config_get("auto")

    @width.setter
    def width(self, num):
        self._config(num)


class C3Donut(C3):

    @property
    def donut(self) -> OptionsDonut:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#DonutChartOptions.LabelRatio
    """
        return self._config_sub_data("donut", OptionsDonut)


class OptionsGauge(Options):

    @property
    def label(self) -> OptionsDonutLabel:
        """
    """
        return self._config_sub_data("label", OptionsDonutLabel)

    def format(self):
        pass

    @property
    def units(self):
        """ Set width of donut chart.

    Related Pages:

      https://c3js.org/reference.html#gauge-units
    """
        return self._config_get()

    @units.setter
    def units(self, value):
        self._config(value)

    @property
    def max(self):
        """ Set max value of the gauge.

    Related Pages:

      https://c3js.org/reference.html#gauge-max
    """
        return self._config_get(100)

    @max.setter
    def max(self, num):
        self._config(num)

    @property
    def min(self):
        """ Set min value of the gauge.

    Related Pages:

      https://c3js.org/reference.html#gauge-min
    """
        return self._config_get(0)

    @min.setter
    def min(self, num):
        self._config(num)

    @property
    def width(self):
        """ Set width of donut chart.

    Related Pages:

      https://c3js.org/reference.html#donut-width
    """
        return self._config_get("auto")

    @width.setter
    def width(self, num):
        self._config(num)


class C3Gauge(C3):
    @property
    def gauge(self) -> OptionsGauge:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#DonutChartOptions.LabelRatio
    """
        return self._config_sub_data("gauge", OptionsGauge)


class OptionsPieExpand(Options):

    @property
    def rate(self):
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.ExpandRate
    """
        return self._config_get()

    @rate.setter
    def rate(self, num):
        self._config(num)


class OptionsPie(Options):

    @property
    def expand(self) -> OptionsPieExpand:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.ExpandRate
    """
        return self._config_sub_data("expand", OptionsPieExpand)

    @property
    def innerRadius(self):
        """

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

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.StartingAngle
    """
        return self._config_get()

    @startingAngle.setter
    def startingAngle(self, value):
        self._config(value)

    @property
    def label(self) -> OptionsPieLabel:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.LabelRatio
    """
        return self._config_sub_data("label", OptionsPieLabel)


class C3Pie(C3):

    @property
    def pie(self) -> OptionsPie:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#PieChartOptions.ExpandRate
    """
        return self._config_sub_data("pie", OptionsPie)


class OptionsRadar(Options):

    def axis(self) -> OptionsAxis:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarAxis
    """
        return self._config_sub_data("axis", OptionsAxis)

    @property
    def size(self) -> OptionsSize:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarSize
    """
        return self._config_sub_data("size", OptionsSize)


class OptionsLevel(Options):

    @property
    def depth(self):
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarLevel
    """
        return self._config_get()

    @depth.setter
    def depth(self, num):
        self._config(num)

    @property
    def text(self) -> OptionsText:
        return self._config_sub_data("text", OptionsText)

    @property
    def show(self):
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarLevel
    """
        return self._config_get(True)

    @show.setter
    def show(self, flag: bool):
        self._config(flag)

    def format(self, js_func, profile=None):
        raise NotImplementedError()


class OptionsDirection(Options):

    @property
    def clockwise(self):
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.RadarChart
    """
        return self._config_get()

    @clockwise.setter
    def clockwise(self, flag):
        self._config(flag)


class C3Radar(C3):

    @property
    def radar(self) -> OptionsRadar:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarAxis
    """
        return self._config_sub_data("radar", OptionsRadar)

    @property
    def level(self) -> OptionsLevel:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarAxis
    """
        return self._config_sub_data("level", OptionsLevel)

    @property
    def direction(self) -> OptionsDirection:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.RadarChart
    """
        return self._config_sub_data("direction", OptionsDirection)


class OptionsArea(Options):

    @property
    def zerobased(self):
        """
    Set if min or max value will be 0 on area chart.

    Related Pages:

      https://c3js.org/reference.html#area-zerobased
    """
        return self._config_get(True)

    @zerobased.setter
    def zerobased(self, flag: bool):
        self._config(flag)


class C3Area(C3):

    @property
    def area(self) -> OptionsArea:
        """

    Related Pages:

      https://c3js.org/reference.html#area-zerobased
    """
        return self._config_sub_data("area", OptionsArea)


class OptionsBar(Options):

    @property
    def width(self):
        """

    Related Pages:

      https://c3js.org/reference.html#bar-width
    """
        return self._config_get("auto")

    @width.setter
    def width(self, num: bool):
        self._config(num)

    @property
    def zerobased(self):
        """ Set if min or max value will be 0 on bar chart.

    Related Pages:

      https://c3js.org/reference.html#bar-zerobased
    """
        return self._config_get(True)

    @zerobased.setter
    def zerobased(self, flag: bool):
        self._config(flag)


class C3Bar(C3):

    @property
    def bar(self) -> OptionsBar:
        """

    Related Pages:

      https://c3js.org/reference.html#bar-width
    """
        return self._config_sub_data("bar", OptionsBar)


class OptionsSpline(Options):

    @property
    def interpolation(self) -> OptionStep:
        """
    """
        return self._config_sub_data("interpolation", OptionStep)


class C3Spline(C3):

    @property
    def spline(self) -> OptionsSpline:
        """
    """
        return self._config_sub_data("spline", OptionsSpline)


class OptionsBubble(Options):

    @property
    def maxR(self):
        """

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

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BubbleDimensionChart
    """
        return self._config_get()

    @minR.setter
    def minR(self, num):
        self._config(num)


class C3Bubble(C3):

    @property
    def bubble(self) -> OptionsBubble:
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BubbleDimensionChart
    """
        return self._config_sub_data("bubble", OptionsBubble)


class C3StanfordData(OptionsData):

    @property
    def epochs(self):
        """

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BubbleDimensionChart
    """
        return self._config_get()

    @epochs.setter
    def epochs(self, value):
        self._config(value)


class C3Stanford(OptChart.OptionsChart):

    @property
    def axis(self) -> OptionAxis:
        """
    """
        return self._config_sub_data("axis", OptionAxis)

    @property
    def point(self) -> OptionsPoints:
        """
    """
        return self._config_sub_data("point", OptionsPoints)

    @property
    def data(self) -> C3StanfordData:
        """
    """
        return self._config_sub_data("data", C3StanfordData)

    @property
    def grid(self) -> OptionsGrid:
        """
    """
        return self._config_sub_data("grid", OptionsGrid)

    @property
    def zoom(self) -> OptionsZoom:
        """
    """
        return self._config_sub_data("zoom", OptionsZoom)
