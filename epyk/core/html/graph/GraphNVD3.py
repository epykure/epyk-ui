#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Optional

from epyk.core.py import primitives, types
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.css import Colors
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsNvd3
from epyk.core.js.packages import JsD3
from epyk.core.html.options import OptChart
from epyk.core.html.options import OptChartNvd3


class Chart(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'NVD3'
    requirements = ('nvd3',)
    _option_cls = OptChart.OptionsChart

    def __init__(self, page: primitives.PageModel, width, height, options, html_code, profile):
        self.seriesProperties, self.__chartJsEvents, self.height = {'static': {}, 'dynamic': {}}, {}, height[0]
        super(Chart, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
        self._d3, self.html_items, self._datasets, self._labels = None, [], [], None
        self.style.css.margin_left = 10
        self.style.css.margin_right = 10
        self.__defined_options = None

    @property
    def shared(self) -> OptChartNvd3.OptionsChartSharedNVD3:
        """
        All the common properties shared between all the charts.

        This will ensure a compatibility with the plot method.

        Usage::

          line = page.ui.charts.nvd3.bar()
          line.shared.x_label("x axis")
        """
        return OptChartNvd3.OptionsChartSharedNVD3(self)

    @property
    def options(self) -> OptChart.OptionsChart:
        """
        Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def chartId(self) -> str:
        """ Return the Javascript variable of the chart. """
        return "%s_obj" % self.htmlCode

    @property
    def data(self):
        """
        Property to the last dataset added to the NVD3 chart.
        Use the function traces to get a specific series from the chart object.
        """
        return self._datasets[-1]

    def traces(self, i: int = None):
        """
        Get a specific series from the datasets attributes in the NVD3 chart.

        :param i: Optional. An Index number
        """
        if i is None:
            return self._datasets[-1]

        return self._datasets[i]

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False,
              source_event: Optional[str] = None, on_ready: bool = False):
        """
        This function is not implemented.

        :param js_funcs: Required. Javascript functions
        :param profile:  Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        raise NotImplementedError()

    def add_trace(self, data, name: str = ""):
        """

        :param data:
        :param name:
        """
        dataset = {"values": data, 'key': name}
        next_index = len(self._datasets)
        if len(self.options.colors) > next_index:
            dataset['color'] = self.options.colors[next_index]
        self._datasets.append(dataset)
        return self

    def labels(self, values: list):
        """

        :param values: The different values for the x axis
        """
        self._labels = values

    def add_dataset(self, data, label: str, colors: list = None, opacity: float = None, kind: str = None):
        """

        :param data: The list of points (float)
        :param label: Optional. The series label (visible in the legend)
        :param colors: Optional. The color for this series. Default the global definition
        :param opacity: Optional. The opacity factory from 0 to 1
        :param kind: Optional. THe series type. Default to the chart type if not supplied
        """
        return self.add_trace([{"x": l, "y": data[i]} for i, l in enumerate(self._labels)], name=label)

    @property
    def d3(self) -> JsD3.D3Select:
        """ Property to the underlying D3 module. """
        if self._d3 is None:
            self._d3 = JsD3.D3Select(
                page=self.page, selector="d3.select('#%s')" % self.htmlCode, set_var=False, component=self)
        return self._d3

    def colors(self, hex_values: list):
        """
        Set the colors of the chart.

        hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
        If the background colors are not specified they will be deduced from the colors list changing the opacity.

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
        self.dom.color(line_colors)
        for i, rec in enumerate(self._datasets):
            rec['color'] = self.options.colors[i]
        return self

    @Html.jbuider("nvd3")
    def build(self, data: types.JS_DATA_TYPES = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None, component_id: Optional[str] = None, stop_state: bool = True):
        """
        Return the JavaScript fragment to refresh the component content.

        :param data: Optional. Component data
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The object reference ID
        """
        if data is not None:
            builder_fnc = JsUtils.jsWrap("%s(%s, %s)" % (
                self.builder_name, JsUtils.jsConvertData(data, None),
                self.__defined_options or self.options.config_js(options).toStr()), profile).toStr()
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(component_id)
            return '''
        d3.select('#%(htmlCode)s').datum(%(builder)s).transition().duration(500).call(%(chart)s); 
        nv.utils.windowResize(%(chart)s.update);%(state)s''' % {
                'htmlCode': self.htmlCode, 'builder': builder_fnc, "state": state_expr, 'chart': self.dom.var}

        return JsUtils.jsConvertFncs([
            self.dom.set_var(True), self.dom.xAxis, self.dom.yAxis,
            self.d3.datum(self._datasets).call(self.dom.var),
            "nv.utils.windowResize(function() { %s.update() })" % self.dom.var], toStr=True)[4:]

    def define(self, options: types.JS_DATA_TYPES = None) -> str:
        """
        Override the chart settings on the JavaScript side.
        This will allow ot set specific styles for some series or also add commons properties.

        Usage:

          chart.onReady([chart.define({"commons": {"backgroundColor": ["pink"], "label": "Other series"}})])

        :param options: JavaScript of Python attributes
        """
        defined_options = "window.%s_options" % self.html_code
        js_expr = "%s = Object.assign(%s ?? %s, %s)" % (
            defined_options, defined_options, self.options.config_js(), JsUtils.jsConvertData(options, None))
        self.__defined_options = defined_options
        return js_expr

    def __str__(self):
        self.style.css.width = "calc(100%% - %spx)" % (
                int(self.style.css.margin_left[:-2]) + int(self.style.css.margin_right[:-2]))
        self.page.properties.js.add_builders(self.build())
        str_items = "".join([h.html() for h in self.html_items])
        return '<div>%s<svg %s></svg></div>' % (
            str_items, self.get_attrs(css_class_names=self.style.get_classes()))


class ChartLine(Chart):
    builder_name = "ChartLine"

    @property
    def dom(self) -> JsNvd3.JsNvd3Line:
        """ Interface to the Dom element of a NVD3 line chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3Line(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartScatter(ChartLine):

    @property
    def dom(self) -> JsNvd3.JsNvd3Scatter:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3Scatter(page=self.page, js_code=self.chartId, component=self)
        return self._dom

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False,
              source_event: Optional[str] = None, on_ready: bool = False):
        """
        Add click event to the points in the chart.

        :param js_funcs: Required. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.onReady("%s.scatter.dispatch.on('elementClick', function(event){ %s })" % (
            self.dom.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True)))
        return self


class ChartCumulativeLine(ChartLine):

    @property
    def dom(self) -> JsNvd3.JsNvd3CumulativeLine:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3CumulativeLine(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartFocusLine(ChartLine):

    @property
    def dom(self) -> JsNvd3.JsNvd3LineWithFocus:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3LineWithFocus(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartBar(Chart):
    builder_name = "ChartBar"

    @property
    def dom(self) -> JsNvd3.JsNvd3Bar:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3Bar(page=self.page, js_code=self.chartId, component=self)
        return self._dom

    def colors(self, hex_values: list):
        """
        Set the colors of the chart.

        hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
        If the background colors are not specified they will be deduced from the colors list changing the opacity.

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
        self.dom.color(line_colors)
        for i, rec in enumerate(self._datasets):
            rec['color'] = self.options.colors[i]
        return self

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False,
              source_event: Optional[str] = None, on_ready: bool = False):
        """
        Add click event to the points in the chart.

        :param js_funcs: Required. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.onReady("%s.selectAll('.nv-bar').on('click', function(event){%s})" % (
            self.d3.varId, JsUtils.jsConvertFncs(js_funcs, toStr=True)))
        return self

    def add_dataset(self, data, label, colors=None, opacity=None, kind=None):
        return self.add_trace([{"label": l, "y": data[i], "x": l} for i, l in enumerate(self._labels)], name=label)


class ChartHorizontalBar(ChartBar):

    @property
    def dom(self) -> JsNvd3.JsNvd3MultiBarHorizontal:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3MultiBarHorizontal(page=self.page, js_code=self.chartId, component=self)
        return self._dom

    def add_dataset(self, data, label, colors=None, opacity=None, kind=None):
        return self.add_trace([{"label": l, "y": data[i]} for i, l in enumerate(self._labels)], name=label)


class ChartMultiBar(ChartBar):

    @property
    def dom(self) -> JsNvd3.JsNvd3MultiBar:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3MultiBar(page=self.page, js_code=self.chartId, component=self)
        return self._dom

    def colors(self, hex_values: list):
        """
        Set the colors of the chart.

        hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
        If the background colors are not specified they will be deduced from the colors list changing the opacity.

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
        self.dom.barColor(line_colors)
        for i, rec in enumerate(self._datasets):
            rec['color'] = self.options.colors[i]

    def add_dataset(self, data, label, colors=None, opacity=None, kind=None):
        return self.add_trace([{"label": l, "y": data[i]} for i, l in enumerate(self._labels)], name=label)


class ChartPie(Chart):
    builder_name = "ChartPie"

    @property
    def dom(self) -> JsNvd3.JsNvd3Pie:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3Pie(page=self.page, js_code=self.chartId, component=self)
        return self._dom

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False,
              source_event: Optional[str] = None, on_ready: bool = False):
        """
        Add click event to the points in the chart.

        :param js_funcs: Required. Javascript functions
        :param profile:  Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.onReady("%s.pie.dispatch.on('elementClick', function(event){ %s })" % (
            self.dom.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True)))
        return self

    def add_trace(self, data, name: str = ""):
        """

        :param data:
        :param name:
        """
        self.dom.color(self.options.colors)
        self._datasets = data
        return self


class ChartArea(ChartBar):

    @property
    def dom(self) -> JsNvd3.JsNvd3Area:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3Area(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartHistoBar(ChartBar):

    @property
    def dom(self) -> JsNvd3.JsNvd3HistoricalBar:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3HistoricalBar(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartParallelCoord(Chart):

    @property
    def dom(self) -> JsNvd3.JsNvd3ParallelCoordinates:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3ParallelCoordinates(page=self.page, js_code=self.chartId, component=self)
        return self._dom

    def set_dimension_names(self, dimensions):
        """

        :param dimensions:
        """
        self.__dimensions = dimensions
        self.dom.dimensionNames(dimensions)
        return self

    def add_trace(self, data, name: str = ""):
        """

        :param data:
        :param name:
        """
        self._datasets = data
        return self


class ChartSunbrust(Chart):
    builder_name = "ChartSunbrust"

    @property
    def dom(self) -> JsNvd3.JsNvd3Sunburst:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3Sunburst(page=self.page, js_code=self.chartId, component=self)
        return self._dom

    def set_rcolors(self, color: str, data):
        """

        :param color:
        :param data:
        """
        for rec in data:
            rec['color'] = color
            if 'children' in rec:
                self.set_rcolors(color, rec['children'])

    def add_trace(self, data, name: str = ""):
        """

        :param data:
        :param name: Optional.
        """
        for i, rec in enumerate(data):
            rec['color'] = self.page.theme.colors[i + 1]
            self.set_rcolors(rec['color'], rec['children'])
        self._datasets = [{'name': name, 'children': data, 'color': self.options.colors[0]}]
        return self


class ChartBoxPlot(Chart):

    @property
    def dom(self) -> JsNvd3.JsNvd3BoxPlot:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3BoxPlot(page=self.page, js_code=self.chartId, component=self)
        return self._dom

    def add_box(self, q1, q3=None, outliers=None, maxRegularValue=None, mean=None, median=None, minRegularValue=None,
                minOutlier=None, maxOutlier=None, title=None):
        """

        https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

        :param q1:
        :param q3:
        :param outliers:
        :param maxRegularValue:
        :param mean:
        :param median:
        :param minRegularValue:
        :param minOutlier:
        :param maxOutlier:
        """
        names = ['q1', 'median', 'q3', 'outlData', 'maxRegularValue', 'mean', 'minRegularValue', 'minOutlier',
                 'maxOutlier']
        row = {}
        for i, val in enumerate(
                [q1, median, q3, outliers, maxRegularValue, mean, minRegularValue, minOutlier, maxOutlier]):
            if val is not None:
                row[names[i]] = val
            elif names[i] == 'outlData':
                row['outlData'] = []
        series_id = len(self._datasets) - 1
        row['seriesColor'] = self.options.colors[series_id]
        row['title'] = title or "Series %s" % series_id
        self._datasets.append(row)
        return self

    def add_trace(self, data, name: str = ""):
        """


        :param data:
        :param name:
        """
        self._datasets = data
        return self


class ChartCandlestick(Chart):

    @property
    def dom(self) -> JsNvd3.JsNvd3CandlestickBar:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3CandlestickBar(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartOhlcBar(Chart):

    @property
    def dom(self) -> JsNvd3.JsNvd3OhlcBar:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3OhlcBar(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartForceDirected(Chart):

    @property
    def dom(self) -> JsNvd3.JsNvd3ForceDirectedGraph:
        """ Interface to the Dom element of a NVd3 Scatter chart. """
        if self._dom is None:
            self._dom = JsNvd3.JsNvd3ForceDirectedGraph(page=self.page, js_code=self.chartId, component=self)
        return self._dom

    def add_trace(self, data: dict, name: str = ""):
        """

        :param data:
        :param name:
        """
        for d in data.get('nodes', []):
            d['color'] = self.options.colors[d.get('group', 1)]
        self._datasets = data
        return self
