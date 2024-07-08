#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Optional

from epyk.core.py import types as etypes
from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.html.graph.evts import EvtBillboard
from epyk.core.css import Colors

from epyk.core.js.packages import JsBillboard
from epyk.core.js import JsUtils
from epyk.core.html.options import OptChartC3

from epyk.core.js.packages import JsD3


class Chart(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'Billboard'
    tag = "div"
    requirements = ('billboard.js',)
    _option_cls = OptChartC3.C3
    _type = None

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        self.height, self._d3 = height[0], None
        super(Chart, self).__init__(page, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                    profile=profile, options=options)
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

          line = page.ui.charts.bb.bar()
          line.shared.x_label("x axis")
        """
        return OptChartC3.OptionsChartSharedC3(component=self)

    @property
    def js(self) -> JsBillboard.Billboard:
        """C3 reference API.

        `Related Pages <https://c3js.org/reference.html#api-show>`_

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsBillboard.Billboard(js_code=self.js_code, page=self.page, component=self)
        return self._js

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """Add a click event on a chart.

        :param js_funcs: A Javascript Python function
        :param profile: Set to true to get the profile for the function on the Javascript console.
        :param source_event: Optional. The source target for the event.
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
        """
        self.options.data.onclick(js_funcs, profile)
        return self

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

    @property
    def d3(self) -> JsD3.D3Select:
        """Property shortcut the D3 underlying base classes"""
        if self._d3 is None:
            self._d3 = JsD3.D3Select(
                page=self.page, selector="d3.select('#%s')" % self.html_code, set_var=False, component=self)
        return self._d3

    def _set_js_code(self, html_code: str, js_code: str):
        """Set a different code for the component.
        This method will ensure both HTML and Js references will be properly changed for this component.
        This method is used by the js_code property and should not be used directly.

        :param html_code: The new HTML code
        :param js_code: The new JavaScript code
        """
        self.options._config("'#' + %s" % JsUtils.jsConvertData(html_code, None), name="bindto", js_type=True)

    @Html.jformatter("bb")
    def build(self, data: etypes.JS_DATA_TYPES = None, options: etypes.OPTION_TYPE = None,
              profile: etypes.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None) -> str:
        """Build / Update the chart.

        :param data: Optional. Dataset
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The component reference (the htmlCode)
        :param stop_state: Remove the top panel for the component state (error, loading...)
        :param dataflows: Chain of data transformations
        """
        self.js_code = component_id
        if data is not None:
            state_expr = ""
            builder_func = JsUtils.jsWrap("%s(%s, %s)" % (
                self.builder_name, JsUtils.dataFlows(data, dataflows, self.page),
                self.__defined_options or self.options.config_js(options).toStr()), profile).toStr()
            if stop_state:
                state_expr = ";%s" % self.hide_state(component_id)
            return '%(chartId)s.unload({done: function(){%(chartId)s.load(%(builder)s)}});%(state)s' % {
                'chartId': self.js_code, 'builder': builder_func, "state": state_expr}

        return '%s = bb.generate(%s)' % (self.js_code, self.options.config_js(options).toStr())

    def define(self, options: etypes.JS_DATA_TYPES = None, dataflows: List[dict] = None, component_id: str = None) -> str:
        """

        :param options:
        :param dataflows: Chain of config transformations:
        :param component_id: Optional. The component reference (the htmlCode)
        """
        self.js_code = component_id
        defined_options = "window.%s_options" % self.html_code
        js_expr = "%s = Object.assign(%s ?? %s, %s)" % (
            defined_options, defined_options, self.options.config_js(), JsUtils.dataFlows(options, dataflows, self.page))
        self.__defined_options = defined_options
        return js_expr

    def __str__(self):
        self.page.properties.js.add_builders(self.build())
        return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


class ChartLine(Chart):
    _type = 'line'
    builder_name = "BBLine"

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        super(ChartLine, self).__init__(page, width, height, html_code, options, profile)
        self.options.bindto = "#%s" % self.htmlCode

    def labels(self, labels: list, series_id: str = 'x'):
        """Set the series labels.

        :param labels: List of labels
        :param series_id: The series key
        """
        self.options.data.x = series_id
        self.options.data.columns.append([series_id] + labels)
        if labels and not isinstance(labels[0], (int, float)):
            self.options.axis.x.type = "category"
        return self

    def add_dataset(self, data: list, name: str, kind: str = None) -> OptChartC3.OptionsData:
        """Add a dataset to the chart.

        :param data: The dataset to be added to the chart
        :param name: The name (alias) of the dataset
        :param kind: Optional. The type of chart
        """
        self.options.data.columns.append([name] + data)
        self.options.data.colors[name] = self.options.colors[len(self.options.data.colors)]
        self.options.data.types[name] = kind or self._type
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
    builder_name = "BBScatter"

    def labels(self, labels: list, series_id: str = 'x'):
        """
 
        :param labels:
        :param series_id: Optional. The series ID.
        """
        pass


class ChartPie(ChartLine):
    _type = 'pie'
    _option_cls = OptChartC3.C3Pie
    builder_name = "BBPie"

    def labels(self, labels: list, series_id: str = 'x'):
        """
 
        :param labels:
        :param series_id: Optional.
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
              profile: etypes.PROFILE_TYPE = None, component_id: str = None, **kwargs) -> str:
        """
 
        :param data: Optional. The dataset to be added to the chart
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The component reference (the htmlCode)
        """
        self.js_code = component_id
        if data:
            return '%(chartId)s.load({columns: [["data", %(value)s]]})' % {'chartId': self.js_code, 'value': data}

        return '%s = bb.generate(%s)' % (self.js_code, self.options.config_js(options).toStr())

    def add_dataset(self, value: list, name: str, kind: str = None):
        """
 
        :param value: The series of numbers to be added to the chart
        :param name: The series name
        :param kind: Optional. The chart type
        """
        self.options.data.columns.append(["data", value])
        self.options.data.colors["data"] = self.options.colors[len(self.options.data.colors)]
        self.options.data.types["data"] = kind or self._type
        return self.options.data


class ChartBubble(ChartLine):
    _type = 'bubble'


class ChartRadar(ChartPie):
    _type = 'radar'
    _option_cls = OptChartC3.C3Radar
