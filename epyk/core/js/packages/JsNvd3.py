from typing import Any, Union, List
from epyk.core.py import primitives, types as etypes
from epyk.core.js import JsUtils

from epyk.core.js.packages import JsPackage
from epyk.core.js.packages import DataAttrs
from epyk.core.js.packages import packageImport


class JsNvd3Axis:

    def __init__(self, js_code: str, page: primitives.PageModel = None, component: primitives.HtmlModel = None):
        self._selector = js_code
        self._js = []
        self.page, self.component = page, component

    def axisLabel(self, text: str):
        """Chart axis settings.

        Usage::

          chart.xAxis.axisLabel('Time (ms)')

        :param text: String.
        """
        text = JsUtils.jsConvertData(text, None)
        self._js.append("axisLabel(%s)" % text)
        return self

    def tickFormat(self, js_funcs, profile=None):
        """Chart axis settings

        Usage::

          chart.xAxis.tickFormat(d3.format(',r'))

        :param js_funcs:
        """
        self._js.append("tickFormat(tickFormat(function(d,i){ %s })" % JsUtils.jsConvertFncs(
            js_funcs, toStr=True, profile=profile))
        return self

    def tickNumberFormat(self, digit: int = 1):
        """

        :param digit:
        """
        self._js.append("tickFormat(function(d,i){ return d3.format(',.%sf')(d); })" % digit)
        return self

    def tickCurrencyFormat(self, currency):
        """

        :param currency:
        """
        currency = JsUtils.jsConvertData(currency, None)
        self._js.append("tickFormat(function(d,i){ return '%s' + d3.format(',.1f')(d); })" % currency)
        return self

    def tickDateFormat(self):
        """ """
        self._js.append("tickFormat(function(d,i){ return d3.time.format('%x')(new Date(d * 86400000)); })")
        return self

    @packageImport("accounting")
    def tickNumber(self, digit=0, thousand_sep=",", factor=None, alias=None):
        """

        :param digit:
        :param thousand_sep:
        :param factor:
        :param alias:
        """
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        if factor is not None:
            alias = alias or {1000: "k", 1000000: "m"}.get(factor, "")
            alias = JsUtils.jsConvertData(alias, None)
            self._js.append("tickFormat(function(d,i){ return accounting.formatNumber(d/%s, %s, %s)+ %s})" % (
                factor, digit, thousand_sep, alias))
        else:
            self._js.append(
                "tickFormat(function(d,i){ return accounting.formatNumber(d, %s, %s) })" % (digit, thousand_sep))
        return self

    @packageImport("accounting")
    def tickSymbol(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
        """

        :param symbol:
        :param digit:
        :param thousand_sep:
        :param decimal_sep:
        :param factor:
        :param alias:
        """
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
        fmt = JsUtils.jsConvertData(fmt, None)
        if factor is not None:
            alias = alias or {1000: "k", 1000000: "m"}.get(factor, "")
            self._js.append("tickFormat(function(d,i){ return accounting.formatMoney(d/%s, %s, %s, %s, %s, %s) })" % (
                factor, JsUtils.jsConvertData("%s%s" % (alias, symbol), None), digit, thousand_sep, decimal_sep, fmt))
        else:
            self._js.append("tickFormat(function(d,i){ return accounting.formatMoney(d, %s, %s, %s, %s) })" % (
                symbol, digit, thousand_sep, decimal_sep))
        return self

    def tickValues(self, values):
        """Chart axis settings.

        Usage::

           chart.xAxis.tickValues(10)

        :param values:
        """
        values = JsUtils.jsConvertData(values, None)
        self._js.append("tickValues(%s)" % values)
        return self

    def toStr(self):
        """Javascript representation.

        :return: Return the Javascript String
        """
        if self._selector is None:
            raise ValueError("Selector not defined, use this() or new() first")

        if len(self._js) == 0:
            return self._selector

        data = "%(jqId)s.%(items)s" % {'jqId': self._selector, 'items': ".".join(self._js)}
        self._js = []  # empty the stack
        return data


class JsNvd3Utils:

    def windowResize(self, js_funcs, profile=None):
        """Update the chart when window resizes.

        :param js_funcs:
        """
        return "nv.utils.windowResize(%s)" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)


class JsNvd3(JsPackage):
    lib_alias = {'js': 'nvd3', 'css': 'nvd3'}
    lib_selector = 'd3.select("body")'

    def __init__(self, component: primitives.HtmlModel = None, page: primitives.PageModel = None, js_code: str = None,
                 selector: str = None, data: Any = None, set_var: bool = None):
        self.component, self.page = component, page
        if page is None and component is not None:
            self.page = component.page
        self._selector = "nv.models.%s()" % self.chartFnc
        self.varName, self.setVar = js_code, set_var
        self.component.jsImports.add(self.lib_alias['js'])
        self.component.cssImport.add(self.lib_alias['css'])
        self._js, self._xaxis, self._yaxis, self._u = [[]], None, None, {}
        self._js_enums, self._container = {}, "%s.parentNode" % self.element

    def set_var(self, flag: bool):
        self.setVar = flag
        return self

    @property
    def varId(self):
        """The Javascript and Python reference ID.

        :return: The Javascript String of the object variable name
        """
        return self._selector if self.varName is None else self.varName

    def options(self, opts):
        raise NotImplementedError()

    def width(self, value):
        """The width the graph or component created inside the SVG should be made.
        The width of the container element (normally the svg itself).

        Related Pages:

          https://nvd3-community.github.io/nvd3/examples/documentation.html

        :param value: A python integer.
        """
        return self.fnc("width(%s)" % value)

    def height(self, value: float):
        """The height the graph or component created inside the SVG should be made.
        The height of the container element (normally the svg itself)

        Related Pages:

          https://nvd3-community.github.io/nvd3/examples/documentation.html

        :param float value:
        """
        return self.fnc("height(%s)" % value)

    def margin(self, options: dict):
        """Object containing the margins for the chart or component.
        You can specify only certain margins in the object to change just those parts.
        Default options: { "top": 15, "right": 10, "bottom": 50, "left": 60 }

        Related Pages:

          https://nvd3-community.github.io/nvd3/examples/documentation.html

        :param dict options: A python dictionary with the options.
        """
        options = JsUtils.jsConvertData(options, None)
        self._js.append("margin(%s)" % options)
        return self

    def useInteractiveGuideline(self, flag: bool):
        """Tooltips which show all data points.

        :param flag:
        """
        flag = JsUtils.jsConvertData(flag, None)
        return self.fnc("useInteractiveGuideline(%s)" % flag)

    def transitionDuration(self, time):
        """

        :param time:
        """
        time = JsUtils.jsConvertData(time, None)
        return self.fnc("transitionDuration(%s)" % time)

    def showLegend(self, flag: bool):
        """

        :param flag:
        """
        flag = JsUtils.jsConvertData(flag, None)
        return self.fnc("showLegend(%s)" % flag)

    @property
    def xAxis(self) -> JsNvd3Axis:
        """ """
        if self._xaxis is None:
            self._xaxis = JsNvd3Axis("%s.xAxis" % self.varName, page=self.page, component=self.component)
        return self._xaxis

    @property
    def yAxis(self) -> JsNvd3Axis:
        """ """
        if self._yaxis is None:
            self._yaxis = JsNvd3Axis("%s.yAxis" % self.varName, page=self.page, component=self.component)
        return self._yaxis

    def showYAxis(self, flag: bool):
        """

        :param bool flag:
        """
        flag = JsUtils.jsConvertData(flag, None)
        return self.fnc("showYAxis(%s)" % flag)

    def showXAxis(self, flag: bool):
        """

        :param bool flag:
        """
        flag = JsUtils.jsConvertData(flag, None)
        return self.fnc("showXAxis(%s)" % flag)

    def update(self):
        pass

    def showControls(self, flag: bool):
        """Allow user to choose 'Stacked', 'Stream', 'Expanded' mode.

        :param bool flag:
        """
        flag = JsUtils.jsConvertData(flag, None)
        return self.fnc("showControls(%s)" % flag)

    def noData(self):
        raise NotImplementedError()

    def color(self, colors):
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
        return JsUtils.jsWrap('''(function(containerId, tag, htmlCode, jsCode, attrs){
const newDiv = document.createElement(tag); 
Object.keys(attrs).forEach(function(key) {newDiv.setAttribute(key, attrs[key]);}); newDiv.id = htmlCode;
if(!containerId){document.body.appendChild(newDiv)} else {document.getElementById(containerId).appendChild(newDiv)};
%(builder)s;return newDiv})(%(container)s, "%(tag)s", %(html_code)s, %(js_code)s, %(attrs)s)''' % {
            "js_code": JsUtils.jsConvertData(self.component.js_code, None),
            "html_code": JsUtils.jsConvertData(html_code or self.component.html_code, None),
            "tag": self.component.tag, "ctx": self.component.options.config_js(options).toStr(),
            "container": JsUtils.jsConvertData(container, None),
            "attrs": self.component.get_attrs(css_class_names=self.component.style.get_classes(), to_str=False),
            "builder": self.component.build(options=options)
        })


class JsNvd3Area(JsNvd3):
    chartFnc = "stackedAreaChart"

    def x(self, column=None, js_funcs=None, profile=False):
        """

        :param column: String.
        :param js_funcs: List | String. Javascript functions.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        """
        if column is not None:
            return self.fnc("x(function(d){return d.%s})" % column)

        elif js_funcs is not None:
            js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
            return self.fnc("x(%s)" % js_funcs)

        return self

    def y(self, column=None, js_funcs=None, profile=False):
        """

        :param column:
        :param js_funcs: List | String. Javascript functions.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        """
        if column is not None:
            return self.fnc("y(function(d){return d.%s})" % column)

        elif js_funcs is not None:
            js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
            return self.fnc("y(%s)" % js_funcs)

        return self

    def rotateLabels(self, value):
        pass

    def reduceXTicks(self, flag):
        pass

    def rightAlignYAxis(self, flag: bool):
        """Move the y-axis to the right side.

        :param flag:
        """
        flag = JsUtils.jsConvertData(flag, None)
        return self.fnc("rightAlignYAxis(%s)" % flag)

    def clipEdge(self, flag: bool):
        """

        :param flag:
        """
        flag = JsUtils.jsConvertData(flag, None)
        return self.fnc("clipEdge(%s)" % flag)

    def controlLabels(self, attrs: dict):
        """

        Usage::

          controlLabels({"stacked": "Stacked"})

        Related Pages:

          https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/stackedAreaChart.html

        :param dict attrs:
        """
        self.fnc("controlLabels(%s)" % JsUtils.jsConvertData(attrs, None))
        return self


class JsNvd3ParallelCoordinates(JsNvd3):
    chartFnc = "parallelCoordinates"

    def dimensionNames(self, categories: list):
        """

        Related Pages:

          https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/parallelCoordinates.html

        :param list categories:
        """
        self.fnc("dimensionNames(%s)" % JsUtils.jsConvertData(categories, None))
        return self

    def dimensionFormats(self, formats):
        """

        Related Pages:

          https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/parallelCoordinates.html

        :param formats:
        """
        self.fnc("dimensionFormats(%s)" % JsUtils.jsConvertData(formats, None))
        return self

    def lineTension(self, val):
        """

        Related Pages:

          https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/parallelCoordinates.html

        :param val:
        """
        self.fnc("lineTension(%s)" % JsUtils.jsConvertData(val, None))
        return self


class JsNvd3CandlestickBar(JsNvd3):
    chartFnc = "candlestickBarChart"

    def x(self, column=None, jsFnc=None, profile=False):
        """

        :param column:
        :param jsFnc: Optional. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if column is not None:
            self.fnc("x(function(d){return d.%s})" % column)
        elif jsFnc is not None:
            self.fnc("x(%s)" % JsUtils.jsConvertFncs(jsFnc, toStr=True, profile=profile))
        return self

    def y(self, column=None, js_funcs=None, profile=False):
        """

        :param column:
        :param js_funcs: Optional. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if column is not None:
            self.fnc("y(function(d){return d.%s})" % column)
        elif js_funcs is not None:
            self.fnc("y(%s)" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self


class JsNvd3OhlcBar(JsNvd3):
    chartFnc = "ohlcBarChart"

    def x(self, column=None, js_funcs=None, profile=False):
        """

        :param column:
        :param js_funcs: Optional. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if column is not None:
            self.fnc("x(function(d){return d.%s})" % column)
        elif js_funcs is not None:
            self.fnc("x(%s)" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self

    def y(self, column=None, js_funcs=None, profile=False):
        """

        :param column:
        :param js_funcs: Optional. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if column is not None:
            self.fnc("y(function(d){return d.%s})" % column)
        elif js_funcs is not None:
            self.fnc("y(%s)" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self


class JsNvd3Sunburst(JsNvd3):
    chartFnc = "sunburstChart"


class JsNvd3BoxPlot(JsNvd3):
    chartFnc = "boxPlotChart"

    def x(self, column=None, js_funcs=None, profile=False):
        """

    :param column:
    :param js_funcs: Optional. Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
        if column is not None:
            self.fnc("x(function(d){return d.%s})" % column)
        elif js_funcs is not None:
            self.fnc("x(%s)" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self

    def staggerLabels(self, flag):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlot.html

    :param flag:
    """
        self.fnc("staggerLabels(%s)" % JsUtils.jsConvertData(flag, None))
        return self

    def yDomain(self, values):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlot.html

    :param values:
    """
        self.fnc("yDomain(%s)" % JsUtils.jsConvertData(values, None))
        return self

    def maxBoxWidth(self, value):
        """
    Prevent boxes from being incredibly wide.

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param value:
    """
        self.fnc("maxBoxWidth(%s)" % JsUtils.jsConvertData(value, None))
        return self

    def itemColor(self, series_color):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param series_color:
    """
        self.fnc("itemColor(function (d) { return d[%s] })" % JsUtils.jsConvertData(series_color, None))
        return self

    def outliers(self, outlData):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param outlData:
    """
        self.fnc("outliers(function (d) { return d[%s] })" % JsUtils.jsConvertData(outlData, None))
        return self

    def outlierValue(self, data):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param data:
    """
        self.fnc("outlierValue(function (d) { return d[%s] })" % JsUtils.jsConvertData(data, None))
        return self

    def outlierColor(self, color: str):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param color:
    """
        self.fnc("outlierColor(function (d) { return d[%s] })" % JsUtils.jsConvertData(color, None))
        return self

    def q1(self, q1_col):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param q1_col:
    """
        self.fnc("q1(function (d) { return d[%s] })" % JsUtils.jsConvertData(q1_col, None))
        return self

    def q2(self, q2_col):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param q2_col:
    """
        self.fnc("q2(function (d) { return d[%s] })" % JsUtils.jsConvertData(q2_col, None))
        return self

    def q3(self, q3_col):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param q3_col:
    """
        self.fnc("q3(function (d) { return d[%s] })" % JsUtils.jsConvertData(q3_col, None))
        return self

    def wl(self, wl_col):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param wl_col:
    """
        self.fnc("wl(function (d) { return d[%s] })" % JsUtils.jsConvertData(wl_col, None))
        return self

    def wh(self, wh_col):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param wh_col:
    """
        self.fnc("wh(function (d) { return d[%s] })" % JsUtils.jsConvertData(wh_col, None))
        return self

    def outlierLabel(self):
        pass


class JsNvd3Bar(JsNvd3):
    chartFnc = "discreteBarChart"

    def x(self, column=None, js_funcs=None, profile=False):
        """

    :param column:
    :param js_funcs: Optional. Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
        if column is not None:
            self.fnc("x(function(d){return d.%s})" % column)
        elif js_funcs is not None:
            self.fnc("x(%s)" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self

    def y(self, column=None, js_funcs=None, profile=False):
        """

    :param column:
    :param js_funcs: Optional. Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
        if column is not None:
            self.fnc("y(function(d){return d.%s})" % column)
        elif js_funcs is not None:
            self.fnc("y(%s)" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self

    def color(self, colors: list):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/TimeSeries.html

    :param colors:
    """
        self.fnc("color(%s)" % JsUtils.jsConvertData(colors, None))
        return self

    def rotateLabels(self, value):
        """
    Rotates the X axis labels by the specified degree.

    Related Pages:

      https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param value:
    """
        self.fnc("rotateLabels(%s)" % value)
        return self

    def reduceXTicks(self, flag: bool):
        """

    :param flag:
    """

    def staggerLabels(self, flag: bool):
        """

    :param flag:
    """

    def tooltips(self, flag: bool):
        """

    :param flag:
    """

    def showValues(self, flag: bool):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/discreteBarChart.html

    :param flag:
    """
        self.fnc("showValues(%s)" % JsUtils.jsConvertData(flag, None))
        return self

    def groupSpacing(self, value):
        raise NotImplementedError()


class JsNvd3MultiBar(JsNvd3):
    chartFnc = "multiBarChart"

    def x(self, column=None, js_funcs=None, profile=False):
        """

    :param column:
    :param js_funcs: Optional. Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
        if column is not None:
            self.fnc("x(function(d){return d.%s})" % column)
        elif js_funcs is not None:
            self.fnc("x(%s)" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self

    def y(self, column=None, js_funcs=None, profile=False):
        """

    :param column:
    :param js_funcs: Optional. Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
        if column is not None:
            self.fnc("y(function(d){return d.%s})" % column)
        elif js_funcs is not None:
            self.fnc("y(%s)" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self

    def barColor(self, colors: list):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/multiBarChart.html

    :param colors:
    """
        self.fnc("barColor(%s)" % JsUtils.jsConvertData(colors, None))
        return self

    def stacked(self, flag: bool):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/multiBarChart2.html

    :param flag: Stack the series in the chart
    """
        self.fnc("stacked(%s)" % JsUtils.jsConvertData(flag, None))
        return self


class JsNvd3MultiBarHorizontal(JsNvd3Bar):
    chartFnc = "multiBarHorizontalChart"

    def yErr(self):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/multiBarHorizontalChart.html
    """
        raise NotImplementedError()

    def barColor(self, colors: list):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/multiBarHorizontalChart.html

    :param colors: The list of color for the bar series.
    """
        self.fnc("barColor(%s)" % JsUtils.jsConvertData(colors, None))
        return self


class JsNvd3Multi(JsNvd3Bar):
    chartFnc = "multiChart"


class JsNvd3Line(JsNvd3Bar):
    chartFnc = "lineChart"


class JsNvd3Scatter(JsNvd3Bar):
    chartFnc = "scatterChart"

    def showDistX(self, flag: bool):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/scatterChart.html

    :param flag:
    """
        self.fnc("showDistX(%s)" % JsUtils.jsConvertData(flag, None))
        return self

    def showDistY(self, flag: bool):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/scatterChart.html

    :param flag:
    """
        self.fnc("showDistY(%s)" % JsUtils.jsConvertData(flag, None))
        return self

    def useVoronoi(self, flag: bool):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/scatterChart.html

    :param flag:
    """
        self.fnc("useVoronoi(%s)" % JsUtils.jsConvertData(flag, None))
        return self


class JsNvd3LineWithFocus(JsNvd3Line):
    chartFnc = "lineWithFocusChart"

    def brushExtent(self, values: list):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/lineWithFocusChart.html

    :param values:
    """
        self.fnc("brushExtent(%s)" % JsUtils.jsConvertData(values, None))
        return self


class JsNvd3CumulativeLine(JsNvd3Line):
    chartFnc = "cumulativeLineChart"

    def average(self, mean: str):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/cumulativeLineChart.html

    :param mean: The column name corresponding to the mean value
    """
        self.fnc("average(function(d) { return d.[%s] / 100; })" % JsUtils.jsConvertData(mean, None))
        return self

    def clipVoronoi(self, flag: bool):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/cumulativeLineChart.html

    :param flag:
    """
        self.fnc("clipVoronoi(%s)" % JsUtils.jsConvertData(flag, None))
        return self


class JsNvd3LinePlusBar(JsNvd3Bar):
    chartFnc = "linePlusBarChart"

    def legendRightAxisHint(self, text: str):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/linePlusBarChart.html

    :param text:
    """
        self.fnc("legendRightAxisHint(%s)" % JsUtils.jsConvertData(text, None))
        return self

    def forceY(self, indices):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/linePlusBarChart.html

    :param indices:
    """
        self.fnc("forceY(%s)" % JsUtils.jsConvertData(indices, None))
        return self

    def padData(self, flag: bool):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/linePlusBarChart.html

    :param flag:
    """
        self.fnc("padData(%s)" % JsUtils.jsConvertData(flag, None))
        return self


class JsNvd3HistoricalBar(JsNvd3Bar):
    chartFnc = "historicalBarChart"

    def xScale(self, d3_func):
        """
    Use a time scale instead of plain numbers in order to get nice round default values in the axis.

    Usage::

      xScale(d3.time.scale())

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/TimeSeries.html

    :param d3_func:
    """
        self.fnc("xScale(%s)" % JsUtils.jsConvertData(d3_func, None))
        return self

    def forceX(self, values: list):
        """
    fix half-bar problem on the first and last bars.

    :param values:
    """
        self.fnc("forceX(%s)" % JsUtils.jsConvertData(values, None))
        return self


class JsDataArcRadius(DataAttrs):

    @property
    def inner(self):
        """
    """
        return self._attrs["inner"]

    @inner.setter
    def inner(self, time):
        self._attrs["inner"] = time

    @property
    def outer(self):
        """
    """
        return self._attrs["outer"]

    @outer.setter
    def outer(self, time):
        self._attrs["outer"] = time


class JsNvd3Pie(JsNvd3):
    chartFnc = "pieChart"

    def arcsRadius(self, values=None):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/monitoringChart.html
      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/monitoringChart.html

    :param values: Optional.
    """
        if values is not None:
            for a in values:
                arc = self.fnc_enum('arcsRadius', JsDataArcRadius)
                for k, v in a.items():
                    setattr(arc, k, v)
            return self

        return self.fnc_enum('arcsRadius', JsDataArcRadius)

    def x(self, column=None, js_funcs=None, profile=False):
        """

    :param column:
    :param js_funcs: Optional. Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
        if column is not None:
            self.fnc("x(function(d){return d.%s})" % column)
        elif js_funcs is not None:
            self.fnc("x(%s)" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self

    def y(self, column=None, js_funcs=None, profile=False):
        """

    :param column:
    :param js_funcs: Optional. Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
        if column is not None:
            self.fnc("y(function(d){return d.%s})" % column)
        elif js_funcs is not None:
            self.fnc("y(%s)" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self

    def showLabels(self, flag: bool):
        """
    Display pie labels.

    Related Pages:

      http://nvd3.org/examples/pie.html

    :param flag:
    """
        self.fnc("showLabels(%s)" % JsUtils.jsConvertData(flag, None))
        return self

    def labelThreshold(self, value):
        """
    Configure the minimum slice size for labels to show up.

    Related Pages:

      http://nvd3.org/examples/pie.html

    :param value:
    """
        self.fnc("labelThreshold(%s)" % JsUtils.jsConvertData(value, None))
        return self

    def labelSunbeamLayout(self, flag: bool):
        """
    Change the label orientation for each category.

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/monitoringChart.html

    :param flag:
    """
        self.fnc("labelSunbeamLayout(%s)" % JsUtils.jsConvertData(flag, None))
        return self

    def labelType(self, text):
        raise NotImplementedError()

    def donutLabelsOutside(self, flag: bool):
        """

    :param flag:
    """
        self.fnc("donutLabelsOutside(%s)" % JsUtils.jsConvertData(flag, None))
        return self

    def color(self, colors: list):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/TimeSeries.html

    :param colors:
    """
        self.fnc("color(%s)" % JsUtils.jsConvertData(colors, None))
        return self

    def donut(self, flag: bool):
        """
    Turn on Donut mode. Makes pie chart look tasty!

    Related Pages:

      http://nvd3.org/examples/pie.html

    :param flag:
    """
        value = "donut(%s)" % JsUtils.jsConvertData(flag, None)
        if value not in self._js[-1]:
            self.fnc(value)
        return self

    def startAngle(self, angle: str):
        """

    Usage::

      startAngle("d.startAngle/2 -Math.PI/2")

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/donutChart.html

    :param angle: The javaScript expression
    """
        self.fnc("startAngle(function(d) { return %s; } )" % angle)
        return self

    def endAngle(self, angle: str):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/donutChart.html

    :param str angle:
    """
        self.fnc("endAngle(function(d) { return %s })" % angle)
        return self

    def half(self):
        pass

    def donutRatio(self, value: float):
        """
    Configure how big you want the donut hole size to be.

    Related Pages:

      http://nvd3.org/examples/pie.html

    :param value:
    """
        self.donut(True)
        self.fnc("donutRatio(%s)" % JsUtils.jsConvertData(value, None))
        return self

    def padAngle(self, val: float):
        """
    Add a padding (space) between the different categories of the chart.

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/donutChart.html

    :param val: The padding value.
    """
        self.fnc("padAngle(%s)" % JsUtils.jsConvertData(val, None))
        return self

    def cornerRadius(self, val: float):
        """
    Change the angle corner radius

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/donutChart.html

    :param val: The rounding to be set to the angles
    """
        self.fnc("cornerRadius(%s)" % JsUtils.jsConvertData(val, None))
        return self

    def id(self, class_name: str):
        """
    allow custom CSS for this one svg.

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/donutChart.html

    :param class_name:
    """
        self.fnc("id(%s)" % JsUtils.jsConvertData(class_name, None))
        return self

    def growOnHover(self, flag: bool):
        """

    :param bool flag:
    """
        self.fnc("growOnHover(%s)" % JsUtils.jsConvertData(flag, None))
        return self

    def reduceXTicks(self, flag: bool):
        pass

    def staggerLabels(self, flag: bool):
        pass

    def tooltips(self, flag):
        pass

    def showValues(self, flag):
        pass

    def groupSpacing(self, value):
        pass

    def title(self, text: Union[str, primitives.JsDataModel]):
        """
    Text to include within the middle of a donut chart.

    Related Pages:

      https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param Union[str, primitives.JsDataModel] text:
    """
        self.fnc("title(%s)" % JsUtils.jsConvertData(JsUtils.jsConvertData(text, None), None))
        return self

    def titleOffset(self, value):
        pass


class JsNvd3ForceDirectedGraph(JsNvd3Bar):
    chartFnc = "forceDirectedGraph"

    def color(self, colors: List[str]):
        """

    :param colors:
    """
        self.fnc("color(function(d) {return %(colors)s[d.index]})" % {"colors": colors})
        return self

    def nodeExtras(self, text: str):
        """

    Related Pages:

      https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/forceDirected.html

    :param text:
    """
        self.fnc(
            "nodeExtras(function(node) {node.append('text').attr('dx', 12).attr('dy', '.35em').text(function(d) { return d.%s }) })" % text)
        return self
