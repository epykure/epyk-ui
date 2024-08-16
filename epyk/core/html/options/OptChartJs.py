#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from typing import List, Optional, Union
from epyk.core.py import types as etypes
from epyk.core.html.options import Options
from epyk.core.js.packages import packageImport, until_version, from_version
from epyk.core.js import JsUtils
from epyk.core.html.options import OptChart

# ChartJs extensions
from epyk.core.html.graph.exts import ChartJsLabels
from epyk.core.html.graph.exts import ChartJsStacked
from epyk.core.html.graph.exts import ChartJsDragData
from epyk.core.html.graph.exts import ChartJsHierarchical
from epyk.core.html.graph.exts import ChartJsDeferred
from epyk.core.html.graph.exts import ChartJsZoom
from epyk.core.html.graph.exts import ChartJsDataLabels
from epyk.core.html.graph.exts import ChartJsCrosshair
from epyk.core.html.graph.exts import ChartJsAnnotation
from epyk.core.html.options import OptChartJsDataSets


class OptionsChartSharedChartJs(OptChart.OptionsChartShared):

    def x_format(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        self.component.options.xAxes.ticks.callback(js_funcs, profile)
        return self

    def x_format_money(self, symbol: etypes.JS_DATA_TYPES = "", digit: int = 0,
                       thousand_sep: etypes.JS_DATA_TYPES = ".",
                       decimal_sep: etypes.JS_DATA_TYPES = ",", fmt: etypes.JS_DATA_TYPES = "%v %s",
                       factor: int = None, alias: str = ""):
        self.component.options.scales.xAxes.ticks.toMoney(symbol, digit, thousand_sep, decimal_sep, fmt, factor, alias)
        return self

    def x_format_number(self, factor: int = 1, alias: str = None, digits: int = 0,
                        thousand_sep: etypes.JS_DATA_TYPES = "."):
        self.component.options.scales.xAxes.ticks.scale(factor, alias, digits, thousand_sep)
        return self

    def x_label(self, value: etypes.JS_DATA_TYPES):
        """ Set the label of the x-axis.

    :param value: The axis label.
    """
        if min(self.component.page.imports.pkgs.chart_js.version) > '3.0.0':
            self.component.options.scales.xAxes.title.text = value
            self.component.options.scales.xAxes.title.display = True
        else:
            self.component.options.scales.xAxes.scaleLabel.label(value)
        return self

    def x_tick_count(self, num: int):
        self.component.options.scales.xAxes.ticks.maxTicksLimit = num
        return self

    def y_format(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        self.component.options.yAxes.ticks.callback(js_funcs, profile)
        return self

    def y_format_money(self, symbol: etypes.JS_DATA_TYPES = "", digit: int = 0,
                       thousand_sep: etypes.JS_DATA_TYPES = ".",
                       decimal_sep: int = ",", fmt: etypes.JS_DATA_TYPES = "%v %s", factor: int = None,
                       alias: str = ""):
        self.component.options.scales.yAxes.ticks.toMoney(symbol, digit, thousand_sep, decimal_sep, fmt, factor, alias)
        return self

    def y_format_number(self, factor: int = 1, alias: str = None, digits: int = 0,
                        thousand_sep: etypes.JS_DATA_TYPES = "."):
        self.component.options.scales.yAxes.ticks.scale(factor, alias, digits, thousand_sep)
        return self

    def y_label(self, value: etypes.JS_DATA_TYPES):
        """
        Set the label of the y-axis.

        :param value: The axis label.
        """
        if min(self.component.page.imports.pkgs.chart_js.version) > '3.0.0':
            self.component.options.scales.yAxes.title.text = value
            self.component.options.scales.yAxes.title.display = True
        else:
            self.component.options.scales.yAxes.scaleLabel.label(value)
        return self

    def y_tick_count(self, num: int):
        self.component.options.scales.yAxes.ticks.maxTicksLimit = num
        return self


class OptionLabelFont(Options):

    @property
    def size(self):
        """ Change the font-size. """
        return self._config_get()

    @size.setter
    def size(self, num: int):
        self._config(num)

    @property
    def family(self):
        """
        Change the font family.

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/subtitle/basic.html
        """
        return self._config_get()

    @family.setter
    def family(self, text: int):
        self._config(text)

    @property
    def weight(self):
        """
        Change the font weight.

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/subtitle/basic.html
        """
        return self._config_get()

    @weight.setter
    def weight(self, text: int):
        self._config(text)

    @property
    def style(self):
        """
        Change the CSS font style property.

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/subtitle/basic.html
        """
        return self._config_get()

    @style.setter
    def style(self, text: int):
        self._config(text)


class OptionAxesTicksMajor(Options):
    @property
    def fontColor(self):
        """
        Change the font color.

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @fontColor.setter
    def fontColor(self, val: str):
        self._config(val)


class OptionAxesTicks(Options):

    @property
    def color(self):
        """
        Change the font color.

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @color.setter
    def color(self, val: str):
        self._config(val)

    @property
    def fontColor(self):
        """
        Change the font color.

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @fontColor.setter
    def fontColor(self, val: str):
        self._config(val)

    @property
    def textStrokeColor(self):
        """
        Change the font color.

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @textStrokeColor.setter
    def textStrokeColor(self, val: str):
        self._config(val)

    @property
    def backdropColor(self):
        """
        Change the font color.

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @backdropColor.setter
    def backdropColor(self, val: str):
        self._config(val)

    @property
    def fontSize(self):
        """
        Change the labels CSS font size.

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @fontSize.setter
    def fontSize(self, val: int):
        self._config(val)

    @property
    def beginAtZero(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @beginAtZero.setter
    def beginAtZero(self, flag: bool):
        self._config(flag)

    @property
    def major(self) -> OptionAxesTicksMajor:
        """ """
        return self._config_sub_data("major", OptionAxesTicksMajor)

    @property
    def minor(self) -> OptionAxesTicksMajor:
        """ """
        return self._config_sub_data("minor", OptionAxesTicksMajor)

    @property
    def max(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @max.setter
    def max(self, val):
        self._config(val)

    @property
    def min(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @min.setter
    def min(self, val):
        self._config(val)

    @property
    def mirror(self):
        """
        Flips tick labels around axis, displaying the labels inside the chart instead of outside.
        Note: Only applicable to vertical scales.

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @mirror.setter
    def mirror(self, val):
        self._config(val)

    @property
    def maxTicksLimit(self):
        """
        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @maxTicksLimit.setter
    def maxTicksLimit(self, val):
        self._config(val)

    @property
    def suggestedMin(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @suggestedMin.setter
    def suggestedMin(self, val):
        self._config(val)

    @property
    def suggestedMax(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @suggestedMax.setter
    def suggestedMax(self, val):
        self._config(val)

    @property
    def stepSize(self):
        """
        Force the step size.

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
          https://www.chartjs.org/docs/3.7.0/samples/scales/linear-step-size.html
        """
        return self._config_get()

    @stepSize.setter
    def stepSize(self, val: int):
        self._config(val)

    @packageImport("accounting")
    def scale(self, factor: int = 1000, alias: str = None, digits: int = 0, thousand_sep: etypes.JS_DATA_TYPES = "."):
        """

        :param factor:
        :param alias:
        :param digits:
        :param thousand_sep:
        """
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        alias = alias or {1000: "k", 1000000: "m"}.get(factor, "")
        self._config('''function(label, index, labels){
var pointVal = label/%s; return accounting.formatNumber(pointVal, %s, %s) + '%s'}''' % (
            factor, digits, thousand_sep, alias), name="callback", js_type=True)
        return self

    @packageImport("accounting")
    def toMoney(self, symbol: etypes.JS_DATA_TYPES = "", digit: int = 0, thousand_sep: etypes.JS_DATA_TYPES = ".",
                decimal_sep: etypes.JS_DATA_TYPES = ",", fmt: etypes.JS_DATA_TYPES = "%v %s", factor: float = None,
                alias: str = ""):
        """

        :param symbol:
        :param digit:
        :param thousand_sep:
        :param decimal_sep:
        :param fmt:
        :param factor:
        :param alias:
        """
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
        fmt = JsUtils.jsConvertData(fmt, None)
        if not alias:
            alias = {1000: "k", 1000000: "m"}.get(factor, alias)
        self._config("function(label, index, labels) {return accounting.formatMoney(label, %s, %s, %s, %s, %s)}" % (
            "'%s'+ %s" % (alias, symbol), digit, thousand_sep, decimal_sep, fmt), name="callback", js_type=True)
        return self

    @packageImport("accounting")
    def toNumber(self, digit: int = 0, thousand_sep: etypes.JS_DATA_TYPES = "."):
        """
        Convert to number using the accounting Javascript module-

        Related Pages:

          https://openexchangerates.github.io/accounting.js/

        :param digit: Optional. The number of digit to be displayed
        :param thousand_sep: Optional. The thousand symbol separator
        """
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        self._config("function(label, index, labels) {return accounting.formatNumber(label, %s, %s)}" % (
            digit, thousand_sep), name="callback", js_type=True)
        return self

    def fcallback(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        """


        Related Pages:

          https://www.chartjs.org/docs/latest/samples/scale-options/ticks.html

        :param js_funcs:
        :param profile:
        """
        self._config('''function(val, index) {return (
function(obj){return new Date(obj.getLabelForValue(val))})(this).toISOString().split('T')[0]}''', js_type=True)
        return self

    @property
    def callback(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/latest/samples/scale-options/ticks.html

        :param js_funcs:
        :param profile:
        """
        return self._config_get()

    @callback.setter
    def callback(self, val: str):
        self._config(val)

    def userCallback(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        """
        Convert to number using the accounting Javascript module-

        Related Pages:

          https://openexchangerates.github.io/accounting.js/

        :param js_funcs:
        :param profile:
        """
        self._config("function(label, index, labels) {return 1}", js_type=True)
        return self

    def mapTo(self, mapping: dict):
        """
        Map the values to a static dictionary.

        :param mapping: The mapping table.
        """
        self._config(
            "function(label, index, labels) {var mapping = %s; if (labels in mapping){return mapping[labels]}; return labels}" % mapping,
            name="callback", js_type=True)
        return self


class OptionLabels(Options):

    @property
    def fontColor(self):
        """ Change the color. """
        return self._config_get()

    @fontColor.setter
    def fontColor(self, val: str):
        self._config(val)


class OptionAxesBorder(Options):

    @property
    def display(self):
        """
        If false, do not display grid lines for this axis.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @display.setter
    def display(self, flag: bool):
        self._config(flag)

    @property
    def color(self):
        """
        The color of the grid lines. If specified as an array, the first color applies to the first grid line, the second
        to the second grid line and so on.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @color.setter
    def color(self, val: str):
        self._config(val)

    @property
    def dash(self):
        """
        Length and spacing of dashes on grid lines.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @dash.setter
    def dash(self, val: List[int]):
        self._config(val)

    @property
    def dashOffset(self):
        """
        Offset for line dashes.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @dashOffset.setter
    def dashOffset(self, val):
        self._config(val)

    @property
    def width(self):
        """
        Offset for line dashes.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @width.setter
    def width(self, val):
        self._config(val)


class OptionAxesGridLine(Options):

    @property
    def display(self):
        """
        If false, do not display grid lines for this axis.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @display.setter
    def display(self, flag: bool):
        self._config(flag)

    @property
    def circular(self):
        """
        If true, gridlines are circular (on radar chart only).

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @circular.setter
    def circular(self, val):
        self._config(val)

    @property
    def color(self):
        """
        The color of the grid lines. If specified as an array, the first color applies to the first grid line, the second
        to the second grid line and so on.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @color.setter
    def color(self, val: str):
        self._config(val)

    @property
    def borderColor(self):
        """
        The color of the grid lines. If specified as an array, the first color applies to the first grid line, the second
        to the second grid line and so on.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @borderColor.setter
    def borderColor(self, val: str):
        is_valid, msg = until_version(self.page.imports.pkgs.chart_js.version, "4")
        if not is_valid:
            raise ValueError("grid.borderColor %s of ChartJs - must use border.color instead" % msg)

        self._config(val)

    @property
    def borderDash(self):
        """
        Length and spacing of dashes on grid lines.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @borderDash.setter
    def borderDash(self, val: List[int]):
        is_valid, msg = until_version(self.page.imports.pkgs.chart_js.version, "4")
        if not is_valid:
            raise ValueError("grid.borderDash %s of ChartJs - must use border.dash instead" % msg)

        self._config(val)

    @property
    def borderDashOffset(self):
        """
        Offset for line dashes.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @borderDashOffset.setter
    def borderDashOffset(self, val):
        is_valid, msg = until_version(self.page.imports.pkgs.chart_js.version, "4")
        if not is_valid:
            raise ValueError("grid.borderDashOffset %s of ChartJs - must use border.dashOffset instead" % msg)

        self._config(val)

    @property
    def borderWidth(self):
        """
        Offset for line dashes.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @borderWidth.setter
    def borderWidth(self, val):
        is_valid, msg = until_version(self.page.imports.pkgs.chart_js.version, "4")
        if not is_valid:
            raise ValueError("grid.borderWidth %s of ChartJs - must use border.width instead" % msg)

        self._config(val)

    @property
    def lineWidth(self):
        """
        Stroke width of grid lines.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @lineWidth.setter
    def lineWidth(self, val: int):
        self._config(val)

    @property
    def drawBorder(self):
        """
        If true, draw border at the edge between the axis and the chart area.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @drawBorder.setter
    def drawBorder(self, flag: bool):
        self._config(flag)

    @property
    def drawOnChartArea(self):
        """
        If true, draw lines on the chart area inside the axis lines.
        This is useful when there are multiple axes and you need to control which grid lines are drawn.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @drawOnChartArea.setter
    def drawOnChartArea(self, val):
        self._config(val)

    @property
    def drawTicks(self):
        """
        If true, draw lines beside the ticks in the axis area beside the chart.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @drawTicks.setter
    def drawTicks(self, val):
        self._config(val)

    @property
    def tickMarkLength(self):
        """
        Length in pixels that the grid lines will draw into the axis area.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @tickMarkLength.setter
    def tickMarkLength(self, val):
        self._config(val)

    @property
    def tickColor(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html
        """
        return self._config_get()

    @tickColor.setter
    def tickColor(self, val):
        self._config(val)

    @property
    def zeroLineWidth(self):
        """
        Stroke width of the grid line for the first index (index 0).

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @zeroLineWidth.setter
    def zeroLineWidth(self, val):
        self._config(val)

    @property
    def zeroLineColor(self):
        """
        Stroke color of the grid line for the first index (index 0).

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @zeroLineColor.setter
    def zeroLineColor(self, val: str):
        self._config(val)

    @property
    def zeroLineBorderDash(self):
        """
        Length and spacing of dashes of the grid line for the first index (index 0).

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @zeroLineBorderDash.setter
    def zeroLineBorderDash(self, val):
        self._config(val)

    @property
    def zeroLineBorderDashOffset(self):
        """
        Offset for line dashes of the grid line for the first index (index 0).

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @zeroLineBorderDashOffset.setter
    def zeroLineBorderDashOffset(self, val):
        self._config(val)

    @property
    def offsetGridLines(self):
        """
        If true, grid lines will be shifted to be between labels. This is set to true for a bar chart by default.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @offsetGridLines.setter
    def offsetGridLines(self, val):
        self._config(val)

    @property
    def z(self):
        """
        z-index of gridline layer. Values <= 0 are drawn under datasets, > 0 on top.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
        """
        return self._config_get()

    @z.setter
    def z(self, val):
        self._config(val)


class OptionAxesScaleLabel(Options):

    @property
    def display(self):
        return self._config_get()

    @display.setter
    def display(self, flag: bool):
        self._config(flag)

    @property
    def fontColor(self):
        return self._config_get()

    @fontColor.setter
    def fontColor(self, val: str):
        self._config(val)

    @property
    def labelString(self):
        return self._config_get()

    @labelString.setter
    def labelString(self, val: str):
        self._config(val)

    def label(self, value: str):
        """
        Shortcut to the labelString and display property.

        :param value: The label value.
        """
        self.labelString = value
        self.display = True


class OptionDisplayFormats(Options):

    @property
    def quarter(self):
        return self._config_get()

    @quarter.setter
    def quarter(self, val: str):
        self._config(val)


class OptionAxesTime(Options):

    @property
    def displayFormats(self) -> OptionDisplayFormats:
        """ """
        return self._config_sub_data("displayFormats", OptionDisplayFormats)


class OptionTitle(Options):

    @property
    def align(self):
        """
        Alignment of the title

        Related Pages:

          https://www.chartjs.org/docs/latest/configuration/title.html
          https://www.chartjs.org/docs/latest/samples/title/alignment.html
        """
        return self._config_get('center')

    @align.setter
    def align(self, text: str):
        self._config(text)

    @property
    def display(self):
        """
        Is the title shown?

        Related Pages:

          https://www.chartjs.org/docs/latest/configuration/title.html
          https://www.chartjs.org/docs/latest/samples/other-charts/pie.html
        """
        return self._config_get(False)

    @display.setter
    def display(self, flag: bool):
        self._config(flag)

    @property
    def fullSize(self):
        """
        Marks that this box should take the full width/height of the canvas.
        If false, the box is sized and placed above/beside the chart area.

        Related Pages:

          https://www.chartjs.org/docs/latest/configuration/title.html
        """
        return self._config_get(True)

    @fullSize.setter
    def fullSize(self, flag: bool):
        self._config(flag)

    @property
    def text(self):
        """
        Set the Chart title.

        Usage::

          bar = page.ui.charts.chartJs.bar()
          bar.options.plugins.title.text = pk.js_callback("function(){return Math.random()}")
          bar.options.plugins.title.display = True

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/other-charts/pie.html
        """
        return self._config_get('')

    @text.setter
    def text(self, val: Union[str, List[str]]):
        self._config(val)

    @property
    def color(self):
        """
        Color of text.

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/other-charts/pie.html
        """
        return self._config_get()

    @color.setter
    def color(self, val: str):
        self._config(val)

    @property
    def position(self):
        """
        Position of title

        Related Pages:

          https://www.chartjs.org/docs/latest/configuration/title.html
        """
        return self._config_get("top")

    @position.setter
    def position(self, val: str):
        self._config(val)

    @property
    def fontSize(self):
        return self._config_get()

    @fontSize.setter
    def fontSize(self, val):
        self._config(val)

    @property
    def fontFamily(self):
        return self._config_get()

    @fontFamily.setter
    def fontFamily(self, val):
        self._config(val)

    @property
    def fontColor(self):
        return self._config_get()

    @fontColor.setter
    def fontColor(self, val):
        self._config(val)

    @property
    def fontStyle(self):
        return self._config_get()

    @fontStyle.setter
    def fontStyle(self, val):
        self._config(val)

    @property
    def padding(self):
        """
        Padding to apply around the title. Only top and bottom are implemented.

        Related Pages:

          https://www.chartjs.org/docs/latest/configuration/title.html
        """
        return self._config_get(10)

    @padding.setter
    def padding(self, val):
        self._config(val)

    @property
    def lineHeight(self):
        return self._config_get()

    @lineHeight.setter
    def lineHeight(self, val):
        self._config(val)

    @property
    def font(self) -> OptionLabelFont:
        """
        Fonts.

        Related Pages:

          https://www.chartjs.org/docs/latest/general/fonts.html
        """
        return self._config_sub_data("font", OptionLabelFont)


class OptionAxes(Options):

    @property
    def attributes(self):
        return self._config_get()

    @attributes.setter
    def attributes(self, values: dict):
        self._config(values)

    @property
    def display(self):
        return self._config_get()

    @display.setter
    def display(self, flag: bool):
        self._config(flag)

    @property
    def distribution(self):
        return self._config_get()

    @distribution.setter
    def distribution(self, val):
        self._config(val)

    @property
    def padding(self):
        """
    """
        return self._config_get()

    @padding.setter
    def padding(self, num: int):
        self._config(num)

    @property
    def reverse(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/other-charts/scatter-multi-axis.html
        """
        return self._config_get()

    @reverse.setter
    def reverse(self, flag: bool):
        self._config(flag)

    @property
    def type(self):
        return self._config_get()

    @type.setter
    def type(self, val: str):
        if val == "time":
            from epyk.core.js import Imports

            Imports.JS_IMPORTS["chart.js"]["req"] = [{'alias': 'moment'}]
            # Add the package moment.js is time is used
            # self._report.jsImports.add("moment")
        self._config(val)

    @property
    def stacked(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @stacked.setter
    def stacked(self, val: bool):
        self._config(val)

    @property
    def static(self):
        """ """
        return self._config_get()

    @static.setter
    def static(self, flag: bool):
        self._config(flag)

    @property
    def id(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @id.setter
    def id(self, val):
        self._config(val)

    @property
    def offset(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @offset.setter
    def offset(self, val):
        self._config(val)

    @property
    def position(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @position.setter
    def position(self, val):
        self._config(val)

    @property
    def suggestedMin(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @suggestedMin.setter
    def suggestedMin(self, val: float):
        self._config(val)

    @property
    def suggestedMax(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @suggestedMax.setter
    def suggestedMax(self, val: float):
        self._config(val)

    @property
    def stepSize(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @stepSize.setter
    def stepSize(self, val: int):
        self._config(val)

    @property
    def ticks(self) -> OptionAxesTicks:
        """ """
        return self._config_sub_data("ticks", OptionAxesTicks)

    @property
    def time(self) -> OptionAxesTime:
        """ """
        return self._config_sub_data("time", OptionAxesTime)

    @property
    def gridLines(self) -> OptionAxesGridLine:
        """ """
        return self._config_sub_data("gridLines", OptionAxesGridLine)

    @property
    def grid(self) -> OptionAxesGridLine:
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/other-charts/scatter-multi-axis.html
          https://www.chartjs.org/docs/latest/migration/v4-migration.html
        """
        return self._config_sub_data("grid", OptionAxesGridLine)

    @property
    def border(self) -> OptionAxesBorder:
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/other-charts/scatter-multi-axis.html
          https://www.chartjs.org/docs/latest/migration/v4-migration.html
        """
        is_valid, msg = from_version(self.page.imports.pkgs.chart_js.version, "4")
        if not is_valid:
            raise ValueError("border %s of ChartJs - must use grid instead" % msg)

        return self._config_sub_data("border", OptionAxesBorder)

    @property
    def title(self) -> OptionTitle:
        """
        Namespace: options.scales[scaleId].title, it defines options for the scale title.
        Note that this only applies to cartesian axes.

        Related Pages:

          https://www.chartjs.org/docs/latest/axes/labelling.html
        """
        return self._config_sub_data("title", OptionTitle)

    @property
    def scaleLabel(self) -> OptionAxesScaleLabel:
        """
    """
        return self._config_sub_data("scaleLabel", OptionAxesScaleLabel)

    def add_label(self, text: str, color: str = None):
        """

        :param text:
        :param color:
        """
        self.scaleLabel.display = True
        self.scaleLabel.labelString = text
        if color is not None:
            self.scaleLabel.fontColor = color
        return self

    def category(self, vals):
        """

        :param vals:
        """
        self.type = "category"
        self.labels = vals


class OptionScalePointLabels(Options):

    @property
    def display(self):
        return self._config_get()

    @display.setter
    def display(self, flag: bool):
        self._config(flag)

    @property
    def centerPointLabels(self):
        return self._config_get()

    @centerPointLabels.setter
    def centerPointLabels(self, flag: bool):
        self._config(flag)

    @property
    def font(self) -> OptionLabelFont:
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/other-charts/polar-area-center-labels.html
        """
        return self._config_sub_data("font", OptionLabelFont)


class OptionScaleR(Options):

    @property
    def pointLabels(self) -> OptionScalePointLabels:
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/other-charts/polar-area-center-labels.html
        """
        return self._config_sub_data("pointLabels", OptionScalePointLabels)


class OptionScales(Options):

    @property
    def xAxes(self) -> OptionAxes:
        """
        Shortcut property to the last x_axes definition.
        Use the function x_axes to be more specific.
        """
        return self.x_axes()

    @property
    def yAxes(self) -> OptionAxes:
        """
        Shortcut property to the last y_axis definition.
        Use the function y_axis to be more specific.

        y_axis is useful when multiple y axes are used for the same chart.
        """
        return self.y_axis()

    def add_axis(self, value: str) -> OptionAxes:
        """
        Add a bespoke series to the chart.

        :param value: The series alias
        """
        return self._config_sub_data(value, OptionAxes)

    def add_y_axis(self) -> OptionAxes:
        """ Add / Get y axis to the chart. """
        return self._config_sub_data("y", OptionAxes)

    def y_axis(self, i: int = None) -> OptionAxes:
        """
        Get a specific y axis.

        :param i: optional. Default take the latest one
        """
        is_valid, msg = from_version(self.page.imports.pkgs.chart_js.version, "3")
        if is_valid:
            return self.add_y_axis()

        if "yAxes" not in self.js_tree:
            self._config_sub_data_enum("yAxes", OptionAxes)

        if i is None:
            return self.js_tree["yAxes"][-1]

        return self.js_tree["yAxes"][i]

    def add_x_axis(self) -> OptionAxes:
        """ Add a X axis to a chart component. """
        return self._config_sub_data("x", OptionAxes)

    def x_axes(self, i: int = None) -> OptionAxes:
        """
        Get a specific x axis.

        :param i: optional. Default take the latest one
        """
        if min(self.component.page.imports.pkgs.chart_js.version) > '3.0.0':
            return self.add_x_axis()

        if "xAxes" not in self.js_tree:
            self._config_sub_data_enum("xAxes", OptionAxes)

        if i is None:
            return self.js_tree["xAxes"][-1]

        return self.js_tree["xAxes"][i]

    @property
    def r(self) -> OptionScaleR:
        """ Add options to the r scale. """
        return self._config_sub_data("r", OptionScaleR)

    @property
    def x(self) -> OptionAxes:
        """ Add options to the x axis. """
        return self._config_sub_data("x", OptionAxes)

    @property
    def y(self) -> OptionAxes:
        """  Add options to the y axis. """
        return self._config_sub_data("y", OptionAxes)

    @property
    def y2(self) -> OptionAxes:
        """  Add options to a y2 axis. """
        return self._config_sub_data("y2", OptionAxes)


class OptionScaleGeo(Options):

    @property
    def projection(self):
        return self._config_get()

    @projection.setter
    def projection(self, val: str):
        self._config(val)

    @property
    def projectionScale(self):
        return self._config_get()

    @projectionScale.setter
    def projectionScale(self, num: int):
        self._config(num)

    def set_projection(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None):
        """

        :param js_funcs:
        :param profile:
        """
        self._config(
            "function (value){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile),
            name="projection", js_type=True)


class OptionScaleProjection(Options):

    @property
    def axis(self):
        return self._config_get()

    @axis.setter
    def axis(self, val: str):
        self._config(val)

    @property
    def center(self):
        return self._config_get()

    @center.setter
    def center(self, values: List[float]):
        self._config(values)

    @property
    def padding(self):
        return self._config_get()

    @padding.setter
    def padding(self, val: int):
        self._config(val)

    @property
    def projection(self):
        return self._config_get()

    @projection.setter
    def projection(self, val: str):
        self._config(val)

    @property
    def projectionScale(self):
        return self._config_get()

    @projectionScale.setter
    def projectionScale(self, val: int):
        self._config(val)

    @property
    def projectionOffset(self):
        return self._config_get()

    @projectionOffset.setter
    def projectionOffset(self, values: List[float]):
        self._config(values)


class OptionScaleColor(Options):

    @property
    def axis(self):
        return self._config_get()

    @axis.setter
    def axis(self, val: str):
        self._config(val)

    @property
    def quantize(self):
        return self._config_get()

    @quantize.setter
    def quantize(self, num: int):
        self._config(num)

    @property
    def legend(self) -> OptionScaleGeo:
        """ """
        return self._config_sub_data("legend", OptionLegend)


class OptionScalesGeo(Options):

    @property
    def xy(self) -> OptionScaleGeo:
        """ """
        return self._config_sub_data("xy", OptionScaleGeo)

    @property
    def projection(self) -> OptionScaleProjection:
        """ """
        return self._config_sub_data("projection", OptionScaleProjection)

    @property
    def color(self) -> OptionScaleColor:
        """ """
        return self._config_sub_data("color", OptionScaleColor)


class OptionPadding(Options):

    @property
    def left(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @left.setter
    def left(self, val):
        self._config(val)

    @property
    def right(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @right.setter
    def right(self, val):
        self._config(val)

    @property
    def top(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @top.setter
    def top(self, val):
        self._config(val)

    @property
    def bottom(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @bottom.setter
    def bottom(self, val):
        self._config(val)


class OptionLayout(Options):

    @property
    def padding(self) -> OptionPadding:
        """ """
        return self._config_sub_data("padding", OptionPadding)

    @property
    def paddings(self):
        """ """
        return self._config_get()

    @paddings.setter
    def paddings(self, values):
        self._config(values, "padding")


class OptionLegend(Options):

    @property
    def labels(self) -> OptionLabels:
        """ """
        return self._config_sub_data("labels", OptionLabels)

    @property
    def title(self) -> OptionTitle:
        """ """
        return self._config_sub_data("title", OptionTitle)

    @property
    def align(self):
        """
        Alignment of the legend.

        Related Pages:

          https://www.chartjs.org/docs/latest/configuration/legend.html

        """
        return self._config_get("center")

    @align.setter
    def align(self, val: str):
        self._config(val)

    @property
    def display(self):
        """
        Is the legend shown?

        Related Pages:

          https://www.chartjs.org/docs/latest/configuration/legend.html

        """
        return self._config_get(True)

    @display.setter
    def display(self, flag: bool):
        self._config(flag)

    @property
    def position(self):
        """
        Position of the legend
        values are top, left, bottom, right

        Related Pages:

          https://www.chartjs.org/docs/latest/configuration/legend.html
        """
        return self._config_get()

    @position.setter
    def position(self, val: str):
        self._config(val)

    @property
    def reverse(self):
        """
        Legend will show datasets in reverse order.

        Related Pages:

          https://www.chartjs.org/docs/latest/configuration/legend.html
        """
        return self._config_get(False)

    @reverse.setter
    def reverse(self, flag: bool):
        self._config(flag)

    @property
    def rtl(self):
        """
        true for rendering the legends from right to left.

        Related Pages:

          https://www.chartjs.org/docs/latest/configuration/legend.html

        """
        return self._config_get(False)

    @rtl.setter
    def rtl(self, flag: bool):
        self._config(flag)


class OptionPoint(Options):

    @property
    def radius(self):
        """ """
        return self._config_get(False)

    @radius.setter
    def radius(self, num: int):
        self._config(num)


class OptionLine(Options):

    @property
    def tension(self):
        """ """
        return self._config_get()

    @tension.setter
    def tension(self, num: int):
        self._config(num)


class OptionInteractionLine(Options):

    @property
    def intersect(self):
        """

        https://www.chartjs.org/docs/latest/samples/line/interpolation.html
        """
        return self._config_get(False)

    @intersect.setter
    def intersect(self, flag: bool):
        self._config(flag)


class OptionElements(Options):

    @property
    def point(self) -> OptionPoint:
        """ """
        return self._config_sub_data("point", OptionPoint)


class OptionElementsLine(OptionElements):

    @property
    def line(self) -> OptionLine:
        """ """
        return self._config_sub_data("line", OptionLine)


class OptionChartJsSize(Options):

    @property
    def height(self):
        """ """
        return self._config_get()

    @height.setter
    def height(self, val: int):
        self._config(val)

    @property
    def width(self):
        """ """
        return self._config_get()

    @width.setter
    def width(self, val: int):
        self._config(val)


class OptionChartAreaBorder(Options):

    @property
    def borderColor(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/plugins/chart-area-border.html
        """
        return self._config_get()

    @borderColor.setter
    def borderColor(self, text: str):
        self._config(text)

    @property
    def borderWidth(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/plugins/chart-area-border.html
        """
        return self._config_get()

    @borderWidth.setter
    def borderWidth(self, num: int):
        self._config(num)

    @property
    def borderDash(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/plugins/chart-area-border.html
        """
        return self._config_get()

    @borderDash.setter
    def borderDash(self, values: List[int]):
        self._config(values)

    @property
    def borderDashOffset(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/plugins/chart-area-border.html
        """
        return self._config_get()

    @borderDashOffset.setter
    def borderDashOffset(self, num: int):
        self._config(num)


class OptionQuadrants(Options):

    @property
    def topLeft(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/plugins/quadrants.html
        """
        return self._config_get()

    @topLeft.setter
    def topLeft(self, text: str):
        self._config(text)

    @property
    def topRight(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/plugins/quadrants.html
        """
        return self._config_get()

    @topRight.setter
    def topRight(self, text: str):
        self._config(text)

    @property
    def bottomRight(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/plugins/quadrants.html
        """
        return self._config_get()

    @bottomRight.setter
    def bottomRight(self, text: str):
        self._config(text)

    @property
    def bottomLeft(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/plugins/quadrants.html
        """
        return self._config_get()

    @bottomLeft.setter
    def bottomLeft(self, text: str):
        self._config(text)


class OptionChartJsPlugins(Options):

    @property
    @packageImport('chartjs-plugin-labels')
    def labels(self) -> ChartJsLabels.Labels:
        """
        Chart.js plugin to display labels on pie, doughnut and polar area chart. Original Chart.PieceLabel.js

        Related Pages:

          https://github.com/emn178/chartjs-plugin-labels
        """
        logging.warning("DEPRECATED module - should use datalabels instead")
        return self._config_sub_data("labels", ChartJsLabels.Labels)

    @property
    def legend(self) -> OptionLegend:
        """

    """
        return self._config_sub_data("legend", OptionLegend)

    @property
    def title(self) -> OptionTitle:
        """
        The chart title defines text to draw at the top of the chart.

        Related Pages:

          https://www.chartjs.org/docs/latest/configuration/title.html
        """
        return self._config_sub_data("title", OptionTitle)

    @property
    def subtitle(self) -> OptionTitle:
        """
        Subtitle is a second title placed under the main title, by default. It has exactly the same configuration options
        with the main title

        Related Pages:

          https://www.chartjs.org/docs/latest/samples/subtitle/basic.html
          https://www.chartjs.org/docs/latest/configuration/subtitle.html
        """
        return self._config_sub_data("subtitle", OptionTitle)

    @property
    def quadrants(self) -> OptionQuadrants:
        return self._config_sub_data("quadrants", OptionQuadrants)

    @property
    @packageImport('chartjs-plugin-datalabels')
    def datalabels(self) -> ChartJsDataLabels.Datalabels:
        """
        Display labels on data for any type of charts.

        Related Pages:

          https://chartjs-plugin-datalabels.netlify.app/
          https://github.com/chartjs/chartjs-plugin-datalabels
        """
        prev_version = from_version(self.page.imports.pkgs.chart_js.version, "3.0.0", included=False)
        if prev_version[0]:
            self.page.imports.pkgs.chart_js_extensions.annotation.version = "0.7.0"
        self.page.properties.js.add_constructor("ChartJsDatalabels", "Chart.register(ChartDataLabels)")
        return self._config_sub_data("datalabels", ChartJsDataLabels.Datalabels)

    @property
    @packageImport('chartjs-plugin-deferred')
    def deferred(self) -> ChartJsDeferred.Deferred:
        """
        Chart.js plugin to defer initial chart updates until the user scrolls and the canvas appears inside the
        viewport, and thus trigger the initial chart animations when the user is likely to see them.

        Related Pages:

          https://github.com/chartjs/awesome#charts
          https://chartjs-plugin-deferred.netlify.app/guide/
        """
        prev_version = from_version(self.page.imports.pkgs.chart_js.version, "3.0.0", included=False)
        if prev_version[0]:
            self.page.imports.pkgs.chart_js_extensions.annotation.version = "1.0.2"
        self.page.properties.js.add_constructor("ChartJsDeferred", "Chart.register(ChartDeferred)")
        return self._config_sub_data("deferred", ChartJsDeferred.Deferred)

    @property
    @packageImport('chartjs-plugin-hierarchical')
    def hierarchical(self) -> ChartJsHierarchical.Hierarchical:
        """
        Adds hierarchical scales that can be collapsed, expanded, and focused

        Related Pages:

          https://github.com/chartjs/awesome#charts
          https://github.com/sgratzl/chartjs-plugin-hierarchical
        """
        self.page.properties.js.add_constructor("ChartJsHierarchical", "Chart.register(HierarchicalScale)")
        return self._config_sub_data("hierarchical", ChartJsHierarchical.Hierarchical)

    @property
    @packageImport('chartjs-plugin-zoom')
    def zoom(self) -> ChartJsZoom.Zoom:
        """
        A zoom and pan plugin for Chart.js. Currently requires Chart.js >= 2.6.0

        Related Pages:

          https://github.com/chartjs/chartjs-plugin-zoom
          https://github.com/chartjs/awesome
          https://www.chartjs.org/chartjs-plugin-zoom/latest/
        """
        prev_version = from_version(self.page.imports.pkgs.chart_js.version, "3.0.0", included=False)
        if prev_version[0]:
            self.page.imports.pkgs.chart_js_extensions.annotation.version = "0.7.7"
        return self._config_sub_data("zoom", ChartJsZoom.Zoom)

    @property
    @packageImport('chartjs-plugin-crosshair')
    def crosshair(self) -> ChartJsCrosshair.Crosshair:
        """
        Adds a data crosshair to line and scatter charts

        Related Pages:

          https://github.com/chartjs/chartjs-plugin-zoom
          https://github.com/chartjs/awesome#charts
        """
        prev_version = from_version(self.page.imports.pkgs.chart_js.version, "3.4.0", included=False)
        if not prev_version[0]:
            logging.warning("Chartjs plugin - crosshair - might not work well with this version of Python")
        return self._config_sub_data("crosshair", ChartJsCrosshair.Crosshair)

    @property
    @packageImport('chartjs-plugin-annotation')
    def annotation(self) -> ChartJsAnnotation.Annotation:
        """
        An annotation plugin for Chart.js >= 2.4.0

        This plugin draws lines and boxes on the chart area.

        Annotations work with line, bar, scatter and bubble charts that use linear, logarithmic, time, or category scales.
        Annotations will not work on any chart that does not have exactly two axes, including pie, radar,
        and polar area charts.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-annotation/latest/
        """
        prev_version = until_version(self.page.imports.pkgs.chart_js.version, "3.0.0", included=False)
        if prev_version[0]:
            self.page.imports.pkgs.chart_js_extensions.annotation.version = "0.5.7"
        else:
            prev_version = until_version(self.page.imports.pkgs.chart_js.version, "3.6.2", included=True)
            if prev_version[0]:
                self.page.imports.pkgs.chart_js_extensions.annotation.version = "1.4.0"
            else:
                self.page.properties.js.add_constructor("ChartJsHierarchical", "Chart.register(annotationPlugin)")
        return self._config_sub_data("annotation", ChartJsAnnotation.Annotation)

    @property
    @packageImport('chartjs-plugin-stacked100')
    def stacked100(self) -> Optional[ChartJsStacked.Stacked100]:
        """
        This plugin for Chart.js that makes your bar chart to 100% stacked bar chart.
        #TODO add check on the chart types.

        Related Pages:

          https://github.com/y-takey/chartjs-plugin-stacked100
        """
        prev_version = from_version(self.page.imports.pkgs.chart_js.version, "3.0.0", included=False)
        if not prev_version[0]:
            logging.warning("Chartjs plugin - stacked100 - Not compatible")
            return None

        self.page.properties.js.add_constructor("ChartJsStacked100", "Chart.register(ChartjsPluginStacked100.default)")
        return self._config_sub_data("stacked100", ChartJsStacked.Stacked100)

    @property
    @packageImport('chartjs-plugin-dragdata')
    def dragdata(self) -> Optional[ChartJsDragData.DragData]:
        """
        This plugin for Chart.js that makes your bar chart to 100% stacked bar chart.

        Related Pages:

          https://github.com/chrispahm/chartjs-plugin-dragdata
        """
        prev_version = from_version(self.page.imports.pkgs.chart_js.version, "3.0.0", included=False)
        if not prev_version[0]:
            logging.warning("Chartjs plugin - dragData - Not compatible")
            return None

        return self._config_sub_data("dragData", ChartJsDragData.DragData)

    @property
    def chartAreaBorder(self) -> OptionChartAreaBorder:
        return self._config_sub_data("chartAreaBorder", OptionChartAreaBorder)


class ChartJsOptions(OptChart.OptionsChart):
    _struct__schema = {
        "elements": {},
        "scales": {},
        "layout": {},
        "title": {},
        "legend": {},
        "plugins": {},
        "size": {}}

    @property
    def data(self):
        return self.component._data_attrs

    @data.setter
    def data(self, values: dict):
        self.component._data_attrs = values
        for d in values.get("datasets", []):
            self.component.add_dataset(**d)

    @property
    def indexAxis(self):
        return self._config_get()

    @indexAxis.setter
    @JsUtils.fromVersion({"chart.js": "3.0.0"})
    def indexAxis(self, flag: bool):
        self._config(flag)

    @property
    def responsive(self):
        return self._config_get()

    @responsive.setter
    def responsive(self, flag: bool):
        self._config(flag)

    @property
    def maintainAspectRatio(self):
        return self._config_get(True)

    @maintainAspectRatio.setter
    def maintainAspectRatio(self, flag: bool):
        self._config(flag)

    @property
    def elements(self) -> OptionElements:
        """
    """
        return self._config_sub_data("elements", OptionElements)

    @property
    def scales(self) -> OptionScales:
        """ """
        return self._config_sub_data("scales", OptionScales)

    @property
    def layout(self) -> OptionLayout:
        """ """
        return self._config_sub_data("layout", OptionLayout)

    @property
    def title(self) -> OptionTitle:
        """ """
        return self._config_sub_data("title", OptionTitle)

    @property
    def legend(self) -> OptionLegend:
        """ """
        return self._config_sub_data("legend", OptionLegend)

    @property
    def plugins(self) -> OptionChartJsPlugins:
        """ """
        return self._config_sub_data("plugins", OptionChartJsPlugins)

    @property
    def tooltips(self):
        """ """
        return self._config_sub_data("tooltips", OptionChartJsTooltips)

    def add_title(self, text: str, color: str = None):
        """

        :param text:
        :param color:
        """
        self.title.display = True
        self.title.text = text
        if color is not None:
            self.title.fontColor = color
        return self

    @property
    def size(self) -> OptionChartJsSize:
        """   """
        return self._config_sub_data("size", OptionChartJsSize)


class OptionPieAnimation(Options):

    @property
    def animateRotate(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @animateRotate.setter
    def animateRotate(self, val):
        self._config(val)

    @property
    def animateScale(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @animateScale.setter
    def animateScale(self, val):
        self._config(val)


class OptionsBar(ChartJsOptions):

    @property
    def stacked(self):
        """

        Related Pages:

          https://www.chartjs.org/samples/latest/charts/bar/stacked.html
        """
        x_stacked = self.scales.x_axes().stacked
        y_stacked = self.scales.y_axis().stacked
        return x_stacked, y_stacked

    @stacked.setter
    def stacked(self, val: bool):
        self.scales.x_axes().stacked = val
        self.scales.y_axis().stacked = val

    @property
    def datasets(self) -> OptChartJsDataSets.Bar:
        """ Common datasets configuration for all series """
        return OptChartJsDataSets.Bar(self.component, page=self.page)


class OptionsRadar(ChartJsOptions):

    @property
    def datasets(self) -> OptChartJsDataSets.Radar:
        """ Common datasets configuration for all series """
        return OptChartJsDataSets.Radar(self.component, page=self.page)


class OptionsPie(ChartJsOptions):

    @property
    def tooltips(self):
        """ """
        return self._config_sub_data("tooltips", OptionChartJsPieTooltips)

    @property
    def cutoutPercentage(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @cutoutPercentage.setter
    def cutoutPercentage(self, val):
        self._config(val)

    @property
    def rotation(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @rotation.setter
    def rotation(self, val: int):
        self._config(val)

    @property
    def circumference(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/line.html
        """
        return self._config_get()

    @circumference.setter
    def circumference(self, val: int):
        self._config(val)

    @property
    def animation(self) -> OptionPieAnimation:
        """ """
        return self._config_sub_data("animation", OptionPieAnimation)

    @property
    def datasets(self) -> OptChartJsDataSets.Pie:
        """ Common datasets configuration for all series """
        return OptChartJsDataSets.Pie(self.component, page=self.page)


class OptionsBubble(ChartJsOptions):
    component_properties = ('r',)

    @property
    def r(self):
        """ The radius value. Default: (v) => 2 """
        return self._config_get(JsUtils.jsWrap("(v) => 2"))

    @r.setter
    def r(self, value):
        self._config(value)

    @property
    def datasets(self) -> OptChartJsDataSets.Bubble:
        """ Common datasets configuration for all series """
        return OptChartJsDataSets.Bubble(self.component, page=self.page)


class OptionsLine(ChartJsOptions):

    @property
    def showLines(self):
        """
        If false, the line is not drawn for this dataset.

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/polar.html
          https://www.chartjs.org/docs/3.7.0/charts/line.html
        """
        return self._config_get()

    @showLines.setter
    def showLines(self, flag: bool):
        self._config(flag)

    @property
    def spanGaps(self):
        """
        If true, lines will be drawn between points with no or null data.
        If false, points with null data will create a break in the line. Can also be a number specifying the maximum gap
        length to span. The unit of the value depends on the scale used.

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/polar.html
          https://www.chartjs.org/docs/3.7.0/charts/line.html
        """
        return self._config_get()

    @spanGaps.setter
    def spanGaps(self, val: Optional[bool]):
        self._config(val)

    @property
    def tension(self):
        """
        Bezier curve tension of the line.
        Set to 0 to draw straightlines. This option is ignored if monotone cubic interpolation is used.

        Related Pages:

          https://www.chartjs.org/docs/3.7.0/charts/line.html
        """
        return self._config_get()

    @tension.setter
    def tension(self, val: int):
        self._config(val)

    @property
    def backgroundColor(self):
        """
        The line fill color.

        Related Pages:

          https://www.chartjs.org/docs/3.7.0/charts/line.html
        """
        return self._config_get()

    @backgroundColor.setter
    def backgroundColor(self, val: str):
        self._config(val)

    @property
    def borderCapStyle(self):
        """
        Cap style of the line.

        Related Pages:

          https://www.chartjs.org/docs/3.7.0/charts/line.html
        """
        return self._config_get()

    @borderCapStyle.setter
    def borderCapStyle(self, val):
        self._config(val)

    @property
    def borderColor(self):
        """
        The line color.

        Related Pages:

          https://www.chartjs.org/docs/3.7.0/charts/line.html
        """
        return self._config_get()

    @borderColor.setter
    def borderColor(self, val: int):
        self._config(val)

    @property
    def borderDash(self):
        """
        Length and spacing of dashes.

        Related Pages:

          https://www.chartjs.org/docs/3.7.0/charts/line.html
        """
        return self._config_get()

    @borderDash.setter
    def borderDash(self, val: int):
        self._config(val)

    @property
    def borderDashOffset(self):
        """
        Offset for line dashes.

        Related Pages:

          https://www.chartjs.org/docs/3.7.0/charts/line.html
        """
        return self._config_get()

    @borderDashOffset.setter
    def borderDashOffset(self, val: int):
        self._config(val)

    @property
    def borderJoinStyle(self):
        """
        Line joint style.

        Related Pages:

          https://www.chartjs.org/docs/3.7.0/charts/line.html
        """
        return self._config_get()

    @borderJoinStyle.setter
    def borderJoinStyle(self, val: str):
        self._config(val)

    @property
    def borderWidth(self):
        """
        The line width (in pixels).

        Related Pages:

          https://www.chartjs.org/docs/3.7.0/charts/line.html
        """
        return self._config_get()

    @borderWidth.setter
    def borderWidth(self, val: int):
        self._config(val)

    @property
    def interaction(self) -> OptionInteractionLine:
        """ """
        return self._config_sub_data("interaction", OptionInteractionLine)

    @property
    def fill(self):
        """
        How to fill the area under the line.

        Related Pages:

          https://www.chartjs.org/docs/3.7.0/charts/line.html
        """
        return self._config_get()

    @fill.setter
    def fill(self, val):
        self._config(val)

    @property
    def elements(self) -> OptionElementsLine:
        """ """
        return self._config_sub_data("elements", OptionElementsLine)

    @property
    def datasets(self) -> OptChartJsDataSets.Line:
        """ Common datasets configuration for all series """
        return OptChartJsDataSets.Line(self.component, page=self.page)


class OptionsPolar(ChartJsOptions):

    @property
    def startAngle(self):
        """
        Starting angle to draw arcs for the first item in a dataset. In degrees, 0 is at top.

        Related Pages:

          https://www.chartjs.org/docs/latest/charts/polar.html
          https://www.chartjs.org/docs/3.7.0/api/interfaces/PolarAreaControllerChartOptions.html
        """
        return self._config_get(0)

    @startAngle.setter
    def startAngle(self, val: int):
        self._config(val)

    @property
    def animation(self) -> OptionPieAnimation:
        """ """
        return self._config_sub_data("animation", OptionPieAnimation)

    @property
    def datasets(self) -> OptChartJsDataSets.Polar:
        """ Common datasets configuration for all series """
        return OptChartJsDataSets.Polar(self.component, page=self.page)


class OptionChartJsTooltipsCallbacks(Options):

    @property
    def label(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get()

    @label.setter
    def label(self, val: etypes.JS_DATA_TYPES):
        val = JsUtils.jsConvertData(val, None)
        self._config("function(tooltipItem, data) { return %s }" % val, js_type=True)

    @packageImport("accounting")
    def labelNumber(self, digit: int = 0, thousand_sep: etypes.JS_DATA_TYPES = ".",
                    decimal_sep: etypes.JS_DATA_TYPES = ","):
        """

        :param digit: Optional. Decimal point separator.
        :param thousand_sep: Optional. thousands separator.
        :param decimal_sep: Optional. Decimal point separator.
        """
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
        if self.component.options.type == 'horizontalBar':
            self._config(
                "function(tooltipItem, data) {return data.datasets[tooltipItem.datasetIndex].label +': '+ accounting.formatNumber(tooltipItem.xLabel, %s, %s, %s) }" % (
                    digit, thousand_sep, decimal_sep), name="label", js_type=True)
        else:
            self._config(
                "function(tooltipItem, data) {return data.datasets[tooltipItem.datasetIndex].label +': '+ accounting.formatNumber(tooltipItem.yLabel, %s, %s, %s) }" % (
                    digit, thousand_sep, decimal_sep), name="label", js_type=True)

    @packageImport("accounting")
    def labelCurrency(self, symbol: etypes.JS_DATA_TYPES = "", digit: int = 0, thousand_sep: etypes.JS_DATA_TYPES = ".",
                      decimal_sep: etypes.JS_DATA_TYPES = ","):
        """

        :param symbol: Optional. Default currency symbol is ''.
        :param digit: Optional. Decimal point separator.
        :param thousand_sep: Optional. thousands separator.
        :param decimal_sep: Optional. Decimal point separator.
        """
        symbol = JsUtils.jsConvertData(symbol, None)
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
        if self.component.options.type == 'horizontalBar':
            self._config('''function(tooltipItem, data) { 
return data.datasets[tooltipItem.datasetIndex].label +': '+ accounting.formatMoney(tooltipItem.xLabel, %s, %s, %s, %s)
}''' % (symbol, digit, thousand_sep, decimal_sep), name="label", js_type=True)
        else:
            self._config('''function(tooltipItem, data) { 
return data.datasets[tooltipItem.datasetIndex].label +': '+ accounting.formatMoney(tooltipItem.yLabel, %s, %s, %s, %s)
}''' % (symbol, digit, thousand_sep, decimal_sep), name="label", js_type=True)

    @property
    def value(self):
        """

        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get()

    @value.setter
    def value(self, val):
        self._config(val)


class OptionChartJsTooltipsPieCallbacks(OptionChartJsTooltipsCallbacks):

    @packageImport("accounting")
    def labelNumber(self, digit: int = 0, thousand_sep: etypes.JS_DATA_TYPES = "."):
        """

        :param digit: Optional. Decimal point separator
        :param thousand_sep: Optional. thousands separator
        """
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        self._config('''
function(tooltipItem, data) {var indice = tooltipItem.index; 
return data.labels[indice] +': '+ accounting.formatNumber(data.datasets[0].data[indice], %s, %s) }''' % (
            digit, thousand_sep), name="label", js_type=True)

    @packageImport("accounting")
    def labelCurrency(self, symbol: etypes.JS_DATA_TYPES = "", digit: int = 0, thousand_sep: etypes.JS_DATA_TYPES = ".",
                      decimal_sep: etypes.JS_DATA_TYPES = ","):
        """

        :param symbol: Optional. Default currency symbol is ''
        :param digit: Optional. Decimal point separator
        :param thousand_sep: Optional. thousands separator
        :param decimal_sep: Optional. Decimal point separator
        """
        symbol = JsUtils.jsConvertData(symbol, None)
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
        self._config('''
function(tooltipItem, data) {var indice = tooltipItem.index; 
return data.labels[indice] +': '+ accounting.formatMoney(data.datasets[0].data[indice], %s, %s, %s, %s) }''' % (
            symbol, digit, thousand_sep, decimal_sep), name="label", js_type=True)


class OptionChartJsTooltips(Options):

    @property
    def enabled(self):
        """

        https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get()

    @enabled.setter
    def enabled(self, flag: bool):
        self._config(flag)

    @property
    def mode(self):
        return self._config_get()

    @mode.setter
    def mode(self, value):
        self._config(value)

    @property
    def intersect(self):
        return self._config_get()

    @intersect.setter
    def intersect(self, flag: bool):
        self._config(flag)

    @property
    def position(self):
        """

        https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get()

    @position.setter
    def position(self, text: str):
        self._config(text)

    @property
    def callbacks(self) -> OptionChartJsTooltipsCallbacks:
        return self._config_sub_data("callbacks", OptionChartJsTooltipsCallbacks)

    def itemSort(self):
        ...

    def filter(self):
        ...

    @property
    def backgroundColor(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get()

    @backgroundColor.setter
    def backgroundColor(self, code: str):
        self._config(code)

    @property
    def titleColor(self):
        """


    Related Pages:

      https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
    """
        return self._config_get('#fff')

    @titleColor.setter
    def titleColor(self, code: str):
        self._config(code)

    @property
    def titleAlign(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get('left')

    @titleAlign.setter
    def titleAlign(self, text: str):
        self._config(text)

    @property
    def titleSpacing(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(2)

    @titleSpacing.setter
    def titleSpacing(self, num: float):
        self._config(num)

    @property
    def titleMarginBottom(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(6)

    @titleMarginBottom.setter
    def titleMarginBottom(self, num: float):
        self._config(num)

    @property
    def bodyColor(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get('#fff')

    @bodyColor.setter
    def bodyColor(self, code: str):
        self._config(code)

    @property
    def bodyAlign(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get('left')

    @bodyAlign.setter
    def bodyAlign(self, text: str):
        self._config(text)

    @property
    def bodySpacing(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(2)

    @bodySpacing.setter
    def bodySpacing(self, num: float):
        self._config(num)

    @property
    def footerColor(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get('#fff')

    @footerColor.setter
    def footerColor(self, code: str):
        self._config(code)

    @property
    def footerAlign(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get('left')

    @footerAlign.setter
    def footerAlign(self, text: str):
        self._config(text)

    @property
    def footerSpacing(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(2)

    @footerSpacing.setter
    def footerSpacing(self, num: float):
        self._config(num)

    @property
    def footerMarginTop(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(6)

    @footerMarginTop.setter
    def footerMarginTop(self, num: float):
        self._config(num)

    @property
    def caretPadding(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(2)

    @caretPadding.setter
    def caretPadding(self, num: float):
        self._config(num)

    @property
    def caretSize(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(5)

    @caretSize.setter
    def caretSize(self, num: float):
        self._config(num)

    @property
    def cornerRadius(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(6)

    @cornerRadius.setter
    def cornerRadius(self, num: float):
        self._config(num)

    @property
    def multiKeyBackground(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get('#fff')

    @multiKeyBackground.setter
    def multiKeyBackground(self, code: str):
        self._config(code)

    @property
    def displayColors(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(True)

    @displayColors.setter
    def displayColors(self, flag: bool):
        self._config(flag)

    @property
    def boxWidth(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get()

    @boxWidth.setter
    def boxWidth(self, num: float):
        self._config(num)

    @property
    def boxHeight(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get()

    @boxHeight.setter
    def boxHeight(self, num: float):
        self._config(num)

    @property
    def boxPadding(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(1)

    @boxPadding.setter
    def boxPadding(self, num: float):
        self._config(num)

    @property
    def usePointStyle(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(False)

    @usePointStyle.setter
    def usePointStyle(self, flag: bool):
        self._config(flag)

    @property
    def borderColor(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get('rgba(0, 0, 0, 0)')

    @borderColor.setter
    def borderColor(self, code: str):
        self._config(code)

    @property
    def borderWidth(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(0)

    @borderWidth.setter
    def borderWidth(self, num: float):
        self._config(num)

    @property
    def rtl(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get()

    @rtl.setter
    def rtl(self, flag: bool):
        self._config(flag)

    @property
    def textDirection(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get()

    @textDirection.setter
    def textDirection(self, text: str):
        self._config(text)

    @property
    def xAlign(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(None)

    @xAlign.setter
    def xAlign(self, text: str):
        self._config(text)

    @property
    def yAlign(self):
        """


        Related Pages:

          https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html
        """
        return self._config_get(None)

    @yAlign.setter
    def yAlign(self, text: str):
        self._config(text)


class OptionChartJsPieTooltips(Options):

    @property
    def callbacks(self) -> OptionChartJsTooltipsPieCallbacks:
        """ """
        return self._config_sub_data("callbacks", OptionChartJsTooltipsPieCallbacks)


class OptionGeoColorScale(Options):

    @property
    def display(self):
        return self._config_get()

    @display.setter
    def display(self, val):
        self._config(val)

    @property
    def quantize(self):
        return self._config_get()

    @quantize.setter
    def quantize(self, val):
        self._config(val)

    @property
    def position(self):
        return self._config_get()

    @position.setter
    def position(self, val: str):
        self._config(val)

    @property
    def legend(self) -> OptionLegend:
        """ """
        return self._config_sub_data("legend", OptionLegend)


class OptionGeoRadiusScale(Options):

    @property
    def display(self):
        return self._config_get()

    @display.setter
    def display(self, val):
        self._config(val)

    @property
    def size(self):
        return self._config_get()

    @size.setter
    def size(self, val):
        self._config(val)


class OptionGeo(Options):

    @property
    def colorScale(self) -> OptionGeoColorScale:
        """ """
        return self._config_sub_data("colorScale", OptionGeoColorScale)

    @property
    def radiusScale(self) -> OptionGeoRadiusScale:
        """ """
        return self._config_sub_data("radiusScale", OptionGeoRadiusScale)


class OptionPlugins(Options):

    @property
    def legend(self) -> OptionLegend:
        """ """
        return self._config_sub_data("legend", OptionLegend)


class OptionsGeo(ChartJsOptions):
    component_properties = ('mapFile',)

    @property
    def mapFile(self):
        return self._config_get(self.component.geo_map, name="_mapFile")

    @mapFile.setter
    def mapFile(self, val: str):
        self._config(val, name="_mapFile")

    @property
    def showOutline(self):
        return self._config_get()

    @showOutline.setter
    def showOutline(self, val: bool):
        self._config(val)

    @property
    def showGraticule(self):
        return self._config_get()

    @showGraticule.setter
    def showGraticule(self, val: bool):
        self._config(val)

    @property
    def scale(self) -> OptionScaleGeo:
        """ """
        return self._config_sub_data("scale", OptionScaleGeo)

    @property
    def scales(self) -> OptionScalesGeo:
        """ """
        return self._config_sub_data("scales", OptionScalesGeo)

    @property
    def geo(self) -> OptionGeo:
        """ """
        return self._config_sub_data("geo", OptionGeo)

    @property
    def plugins(self) -> OptionPlugins:
        """ """
        return self._config_sub_data("plugins", OptionPlugins)


class OptionsTreeMap(ChartJsOptions):
    ...


class OptionChartJsSankeyParsing(Options):

    @property
    def from_(self):
        return self._config_get()

    @from_.setter
    def from_(self, val: str):
        self._config(val, name="from")

    @property
    def to(self):
        return self._config_get()

    @to.setter
    def to(self, val: str):
        self._config(val)

    @property
    def flow(self):
        return self._config_get()

    @flow.setter
    def flow(self, val: str):
        self._config(val)


class OptionsSankey(ChartJsOptions):

    @property
    def parsing(self) -> OptionChartJsSankeyParsing:
        """
        https://github.com/kurkle/chartjs-chart-sankey
        """
        return self._config_sub_data("parsing", OptionChartJsSankeyParsing)
