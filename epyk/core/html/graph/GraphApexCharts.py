#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List
from epyk.core.py import types as etypes

from epyk.core.py import primitives
from epyk.core.css import Colors
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.html.options import OptChartApex
from epyk.core.js.packages import JsApexChart
from epyk.core.js import JsUtils


class ApexActivePoints:

    def __init__(self, chart_id: str, i: int, page: primitives.PageModel):
        self.chartId = chart_id
        self.page = page
        self.num = i or self.index

    @property
    def index(self):
        """
        Get the active series index.

        :return: A javaScript number.
        """
        return JsUtils.jsWrap("config.seriesIndex")

    @property
    def config(self) -> JsUtils.jsWrap:
        """
        Get the event / chart detailed configuration.

        Related Pages:

          https://apexcharts.com/docs/options/chart/events/

        :return: A Javascript dictionary.
        """
        return JsUtils.jsWrap("config")

    @property
    def datasetLabel(self) -> JsUtils.jsWrap:
        """
        Return the name of the selected dataset.

        Related Pages:

          https://apexcharts.com/docs/options/chart/events/

        :return: A Javascript string
        """
        return JsUtils.jsWrap("config.config.series[%s].name" % self.num)

    @property
    def dataset(self) -> JsUtils.jsWrap:
        """
        Return the selected dataset.

        Related Pages:

          https://apexcharts.com/docs/options/chart/events/

        :return: A Javascript dictionary
        """
        return JsUtils.jsWrap("config.config.series[%s]" % self.num)

    @property
    def value(self):
        """
        Return the value for the selected point of the dataset.

        Related Pages:

          https://apexcharts.com/docs/options/chart/events/
        """
        return JsUtils.jsWrap("config.config.series[%s].data[%s]" % (self.num, self.dataPointIndex))

    @property
    def label(self):
        """
        Return the x label for the selected point.

        Related Pages:

          https://apexcharts.com/docs/options/chart/events/

        :return: A Javascript object.
        """
        return JsUtils.jsWrap("config.globals.categoryLabels[%s]" % self.dataPointIndex)

    @property
    def dataPointIndex(self) -> JsUtils.jsWrap:
        """
        Get the index of the selected point.

        Related Pages:

          https://apexcharts.com/docs/options/chart/events/

        :return: A Javascript number
        """
        return JsUtils.jsWrap("config.dataPointIndex")

    @property
    def event(self) -> JsUtils.jsWrap:
        """
        Get the original JavaScript event object.

        Related Pages:

          https://apexcharts.com/docs/options/chart/events/

        :return: A JavaScript event object.
        """
        return JsUtils.jsWrap("event")

    @property
    def chartContext(self) -> JsUtils.jsWrap:
        """
        Get the full chart context.

        Related Pages:

          https://apexcharts.com/docs/options/chart/events/

        :return: A Javascript dictionary
        """
        return JsUtils.jsWrap("chartContext")


class Chart(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'ApexCharts'
    requirements = ('apexcharts',)
    _option_cls = OptChartApex.OptionsLine
    builder_name = "ApCharts"

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        self.height = height[0]
        super(Chart, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
        self.options.chart.height = height[0]
        self.options.yaxis.labels.formatters.toNumber()
        self.style.css.margin_top = 10
        self.chartId = "%s_obj" % self.htmlCode
        self.__defined_options = None

    def activePoints(self, i: int = None) -> ApexActivePoints:
        """
        The current active points selected by an event on a chart.

        Usage::

            library = "apex"
            kind = "line"
            c = page.ui.charts.plot(library, data.to_dict('records'), kind=kind, y=["Value"], x="Year", height=(500, "px"))

            c.click([
              page.js.console.log(c.activePoints().label)
            ])

        Related Pages:

          https://apexcharts.com/docs/options/chart/events/

        :param i: Optional. The series index. Default it is the series clicked
        """
        return ApexActivePoints(self.chartId, i, self.page)

    @property
    def shared(self) -> OptChartApex.OptionsChartSharedApex:
        """
        All the common properties shared between all the charts.
        This will ensure a compatibility with the plot method.

        Usage::

          line = page.ui.charts.chartJs.bar()
          line.shared.x_label("x axis")
        """
        return OptChartApex.OptionsChartSharedApex(self)

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """
        Add a click event to the Apex chart.

        Related Pages:

          https://apexcharts.com/docs/options/chart/events/

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.options.chart.events.click(js_funcs)
        return self

    def zoomable(self, flag: bool = True):
        """
        Set the chart zoomable.

        :param flag: Optional. Add the zoom option to the chart
        """
        if flag:
            self.options.chart.zoom.type = "x"
            self.options.chart.zoom.enabled = True
            self.options.chart.zoom.autoScaleYaxis = True
        else:
            self.options.chart.zoom.enabled = False

    def colors(self, hex_values: List[str]):
        """
        Set the colors of the chart.

        hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
        If the background colors are not specified they will be deduced from the colors list changing the opacity.

        Usage::

          line = page.ui.charts.apex.line(height=250)
          line.colors(["#FFA500", "#FF7F50"])

        :param hex_values: An array of hexadecimal color codes
        """
        line_colors, bg_colors = [], []
        for h in hex_values:
            if h.upper() in Colors.defined:
                h = Colors.defined[h.upper()]['hex']
            if not isinstance(h, tuple):
                line_colors.append(h)
                bg_colors.append("rgba(%s, %s, %s, %s" % (
                    Colors.getHexToRgb(h)[0], Colors.getHexToRgb(h)[1],
                    Colors.getHexToRgb(h)[2], self.options.opacity))
            else:
                line_colors.append(h[0])
                bg_colors.append(h[0])
        self.options.colors = line_colors
        self.options.background_colors = bg_colors
        for i, rec in enumerate(self.options.all_series):
            if hasattr(rec, "backgroundColor"):
                rec.backgroundColor = self.options.background_colors[i]
                rec.borderColor = self.options.colors[i]
                rec.borderWidth = 1
        return self

    @property
    def js(self) -> JsApexChart.ApexChart:
        """
        The Javascript functions defined for this component.
        Those can be specific ones for the module or generic ones from the language.

        :return: A Javascript Dom object functions.
        """
        if self._js is None:
            self._js = JsApexChart.ApexChart(selector="window['%s']" % self.chartId, component=self, page=self.page)
        return self._js

    @property
    def options(self) -> OptChartApex.OptionsLine:
        """
        Property to the component options.

        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def define(self, options: etypes.JS_DATA_TYPES = None, dataflows: List[dict] = None) -> str:
        """
        Set the chart options.

        :param options: The apex chart option
        :param dataflows: Chain of config transformations
        """
        defined_options = "window.%s_options" % self.html_code
        js_expr = "%s = Object.assign(%s ?? %s, %s)" % (
            defined_options, defined_options, self.options.config_js(), JsUtils.dataFlows(options, dataflows, self.page))
        self.__defined_options = defined_options
        return js_expr

    def labels(self, labels: List[str]):
        """
        Set the labels of the different series in the chart.

        :param labels: An array of labels
        """
        self.options.xaxis.categories = labels
        return self

    def add_dataset(self, data: list, label: str = "", colors: List[str] = None, opacity: float = None,
                    kind: str = None):
        """

        :param data: The list of points (float)
        :param label: Optional. The list of points (float)
        :param colors: Not used. Optional. The color for this series. Default the global definition
        :param opacity: Not used. Optional. The opacity level for the content
        :param kind: Not used. Optional. THe series type. Default to the chart type if not supplied
        """
        series = self.options.add_series()
        series.name = label
        series.data = data
        return series

    @Html.jformatter("apex")
    def build(self, data: etypes.JS_DATA_TYPES = None, options: etypes.OPTION_TYPE = None,
              profile: etypes.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """
        Update the chart with context and / or data changes.

        Usage::

            data = []
            component = page.ui.charts.apex.bar([], y_columns=["rating"], x_axis="progress")
            btn1 = page.ui.buttons.refresh("refresh")
            btn1.click([
                component.build(data)
            ])

        :param data: Optional. The full datasets object expected by ChartJs
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Not used
        :param stop_state: Remove the top panel for the component state (error, loading...)
        :param dataflows: Chain of data transformations
        """
        if data is not None:
            builder_fnc = JsUtils.jsWrap("%s(%s, %s)" % (
                self.builder_name, JsUtils.dataFlows(data, dataflows, self.page),
                self.__defined_options or self.options.config_js(options).toStr()), profile).toStr()
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(component_id)
            return "%s.updateOptions(%s); %s.update();%s" % (
                    "window['%s']" % self.chartId, builder_fnc, self.chartId, state_expr)

        return JsUtils.jsConvertFncs([self.js.new(
            self.dom.varId, self.options.config_js(options), "window['%s']" % self.chartId), self.js.render()],
            toStr=True, profile=profile)

    def __str__(self):
        self.page.properties.js.add_builders(self.build())
        return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())


class Bar(Chart):
    _option_cls = OptChartApex.OptionsBar
    name = 'ApexCharts'

    @property
    def options(self) -> OptChartApex.OptionsBar:
        """
        Property to the component options.

        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options


class Area(Chart):
    _option_cls = OptChartApex.OptionsArea

    @property
    def options(self) -> OptChartApex.OptionsArea:
        """
        Property to the component options.

        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options


class Pie(Chart):
    _option_cls = OptChartApex.OptionsPie

    @property
    def options(self) -> OptChartApex.OptionsPie:
        """
        Property to the component options.

        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options


class RadialBar(Chart):
    _option_cls = OptChartApex.OptionsPie
    builder_name = "ApRadialBar"

    @property
    def options(self) -> OptChartApex.OptionsPie:
        """
        Property to the component options.

        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options


class Bubble(Chart):
    _option_cls = OptChartApex.OptionsArea
    builder_name = "ApBubble"

    @property
    def options(self) -> OptChartApex.OptionsArea:
        """
        Property to the component options.

        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options
