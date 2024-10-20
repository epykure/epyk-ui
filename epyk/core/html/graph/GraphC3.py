#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from epyk.core.py import types as etypes
from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.html.graph.evts import EvtBillboard
from epyk.core.css import Colors

from epyk.core.js.packages import JsC3
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsD3
from epyk.core.html.options import OptChartC3


class Chart(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'C3'
    tag = "div"
    requirements = ('c3',)
    _option_cls = OptChartC3.C3
    _type = None

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        self.height, self._d3 = height[0], None
        super(Chart, self).__init__(
            page, [], html_code=html_code, css_attrs={"width": width, "height": height}, profile=profile,
            options=options)
        self.style.css.margin_top = 10
        self.style.css.padding = 5
        self.options.type = self._type
        if width[1] == "%":
            self.style.css.width_calc(10, None)
        self.__defined_options = None

    @property
    def events(self) -> EvtBillboard.EvtBillboard:
        """Common Chart events"""
        return EvtBillboard.EvtBillboard(page=self.page, component=self)

    @property
    def options(self) -> OptChartC3.C3:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def dom(self) -> OptChartC3.C3:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = OptChartC3.C3(page=self.page, component=self)
        return self._dom

    @property
    def shared(self) -> OptChartC3.OptionsChartSharedC3:
        """All the common properties shared between all the charts.
        This will ensure a compatibility with the plot method.

        Usage::

          line = page.ui.charts.c3.bar()
          line.shared.x_label("x axis")
        """
        return OptChartC3.OptionsChartSharedC3(self)

    @property
    def js(self) -> JsC3.C3:
        """JavaScript C3 reference API.

        `Related Pages <https://c3js.org/reference.html#api-show>`_

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsC3.C3(js_code=self.js_code, page=self.page, component=self)
        return self._js

    def colors(self, hex_values: List[str]):
        """Set the colors of the chart.
        hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
        If the background colors are not specified they will be deduced from the colors list changing the opacity.

        :param hex_values: An array of hexadecimal color codes.
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
        series_count = 0
        for name in self.options.data.columns:
            if name[0] in self.options.data.colors:
                self.options.data.colors[name[0]] = self.options.colors[series_count]
                series_count += 1
        return self

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = False,
              source_event: str = None, on_ready: bool = False):
        """Set a callback for click event on each data point.

        Usage::

            chart.click([page.js.console.log(chart.js.content)])

        `Related Pages <https://c3js.org/reference.html#data-onclick>`_

        :param js_funcs: List of Js Functions. A Javascript Python function
        :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: String. Optional. The source target for the event
        :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.options.data.onclick(js_funcs, profile)
        return self

    @property
    def d3(self) -> JsD3.D3Select:
        """Property to the D3 library"""
        if self._d3 is None:
            self._d3 = JsD3.D3Select(page=self.page, selector="d3.select('#%s')" % self.htmlCode, set_var=False,
                                     component=self)
        return self._d3

    def _set_js_code(self, html_code: str, js_code: str):
        """Set a different code for the component.
        This method will ensure both HTML and Js references will be properly changed for this component.
        This method is used by the js_code property and should not be used directly.

        :param html_code: The new HTML code
        :param js_code: The new JavaScript code
        """
        self.options._config("'#' + %s" % JsUtils.jsConvertData(html_code, None), name="bindto", js_type=True)

    @Html.jformatter("c3")
    def build(self, data: etypes.JS_DATA_TYPES = None, options: etypes.OPTION_TYPE = None,
              profile: etypes.PROFILE_TYPE = False, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None) -> str:
        """Update the chart with context and / or data changes.

        :param data: Optional. The dataset to be added to the chart
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The component reference (the htmlCode)
        :param stop_state: Remove the top panel for the component state (error, loading...)
        :param dataflows: Chain of data transformations
        """
        self.js_code = component_id
        if data is not None:
            builder_fnc = JsUtils.jsWrap("%s(%s, %s)" % (
                self.builder_name, JsUtils.dataFlows(data, dataflows, self.page),
                self.__defined_options or self.options.config_js(options).toStr()), profile).toStr()
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(component_id)
            return '%(chartId)s.unload({done: function() {%(chartId)s.load(%(builder)s)}});%(state)s' % {
                'chartId': self.js_code, 'builder': builder_fnc, "state": state_expr}

        return '%s = c3.generate(%s)' % (self.js_code, self.options.config_js(options).toStr())

    def define(self, options: etypes.JS_DATA_TYPES = None, dataflows: List[dict] = None, component_id: str = None) -> str:
        """Common JavaScript function to set the table definition.
        If options are defined the definition will be specific to the column definition.

        :param options: Optional. The table API attributes. If None return current definition.
        :param dataflows: Chain of config transformations
        :param component_id: Optional. The object reference ID
        """
        self.js_code = component_id
        defined_options = "window.%s_options" % self.html_code
        js_expr = "%s = Object.assign(%s ?? %s, %s)" % (
            defined_options, defined_options, self.options.config_js(), JsUtils.dataFlows(options, dataflows, self.page))
        self.__defined_options = defined_options
        return js_expr

    @Html.jbuilder("c3")
    def generate(self, data: etypes.JS_DATA_TYPES, options=None,
                 profile: etypes.PROFILE_TYPE = False, dataflows: List[dict] = None) -> str:
        """

        :param data: The dataset to be added to the chart
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param dataflows: Chain of data transformations
        """
        builder_fnc = JsUtils.jsWrap("%s(%s, %s)" % (
            self.builder_name, JsUtils.dataFlows(data, dataflows, self.page),
            self.__defined_options or self.options.config_js(options).toStr()), profile).toStr()

        return '%(chartId)s = c3.generate(Object.assign(%(options)s, {data: %(builder)s}))' % {
            "chartId": self.js_code, 'builder': builder_fnc, "options": self.options.config_js(options).toStr()}

    def __str__(self):
        self.page.properties.js.add_builders(self.build())
        return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


class ChartLine(Chart):
    _type = 'line'
    builder_module = "C3Line"

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        super(ChartLine, self).__init__(page, width, height, html_code, options, profile)
        self.options.bindto = "#%s" % self.htmlCode

    def labels(self, labels: list, series_id: str = 'x'):
        """

        :param labels: The list of labels for the series
        :param series_id: Optional. The series ID
        """
        self.options.data.x = series_id
        self.options.data.columns.append([series_id] + labels)
        if labels and not isinstance(labels[0], (int, float)):
            self.options.axis.x.type = "category"

    def add_dataset(self, data: list, name: str, kind: str = None):
        """Add a new dataset.

        :param data: The series of numbers to be added to the chart
        :param name: The series name
        :param kind: Optional. The chart type
        """
        self.options.data.columns.append([name] + data)
        self.options.data.colors[name] = self.options.colors[len(self.options.data.colors)]
        self.options.data.types[name] = kind or self._type
        return self.options.data

    @property
    def data(self):
        return self.options.data


class ChartSpline(ChartLine):
    _type = 'spline'
    _option_cls = OptChartC3.C3Spline


class ChartArea(ChartLine):
    _type = 'area'
    _option_cls = OptChartC3.C3Area


class ChartBar(ChartLine):
    _type = 'bar'
    _option_cls = OptChartC3.C3Bar


class ChartScatter(ChartLine):
    _type = 'scatter'
    builder_module = "C3Scatter"

    def labels(self, labels: list, series_id: str = 'x'):
        """

        :param labels:
        :param series_id: Optional. The series ID.
        """
        pass


class ChartPie(ChartLine):
    _type = 'pie'
    _option_cls = OptChartC3.C3Pie
    builder_module = "C3Pie"

    def labels(self, labels: list, series_id: str = 'x'):
        """

        :param labels:
        :param series_id:
        """
        self._labels = labels

    def add_dataset(self, values: list, name: str, kind: str = None):
        """Add a dataset to a pie chart.
        If multiple datasets are added the value will be summed up in the resulting pue chart.

        :param values: The series of numbers to be added to the chart
        :param name: The series name
        :param kind: Optional. The chart type
        """
        for i, value in enumerate(values):
            series_index = None
            for j, col in enumerate(self.options.data.columns):
                if col[0] == self._labels[i]:
                    series_index = j
                    break

            if series_index is None:
                self.options.data.columns.append([self._labels[i], value])
            else:
                self.options.data.columns[series_index].append(value)
            if series_index is None:
                series_index = len(self.options.data.columns)
                if series_index < len(self.options.colors):
                    self.options.data.colors[self._labels[i]] = self.options.colors[series_index]
                self.options.data.types[self._labels[i]] = kind or self._type
        return self.options.data


class ChartDonut(ChartPie):
    _type = 'donut'
    _option_cls = OptChartC3.C3Donut


class ChartGauge(ChartPie):
    _type = 'gauge'
    _option_cls = OptChartC3.C3Gauge

    def build(self, data: etypes.JS_DATA_TYPES = None, options: etypes.OPTION_TYPE = None,
              profile: etypes.PROFILE_TYPE = False, component_id: str = None, stop_state: bool = True, **kwargs) -> str:
        """Update the chart with context and / or data changes.

        :param data: Optional. The dataset to be added to the chart
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The component reference (the htmlCode)
        :param stop_state: Remove the top panel for the component state (error, loading...)
        """
        self.js_code = component_id
        if data:
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(component_id)
            return '%(chartId)s.load({columns: [["data", %(value)s]]});%(state)s' % {
                'chartId': self.js_code, 'value': data, "state": state_expr}

        return '%s = c3.generate(%s)' % (self.js_code, self.options.config_js(options).toStr())

    def add_dataset(self, value: list, name: str, kind: str = None):
        """

        :param value: The series of numbers to be added to the chart.
        :param name: The series name.
        :param kind: Optional. The chart type.
        """
        self.options.data.columns.append(["data", value])
        self.options.data.colors["data"] = self.options.colors[len(self.options.data.colors)]
        self.options.data.types["data"] = kind or self._type
        return self.options.data


class ChartStanford(ChartLine):
    _type = 'stanford'
    _option_cls = OptChartC3.C3Stanford
    builder_module = "C3Stanford"

    def epoch(self, series: list, name: str):
        """

        :param series:
        :param name:
        """
        self.options.data.epochs = JsUtils.jsConvertData(str(name), None)
        self.options.data.columns.append([str(name)] + series)

    def add_dataset(self, data: list, name: str, kind: str = None):
        """

        :param data: The series of numbers to be added to the chart
        :param name: The series name
        :param kind: Optional. The chart type
        """
        self.options.data.columns.append([name] + data)
        self.options.data.type = kind or self._type
        return self.options.data
