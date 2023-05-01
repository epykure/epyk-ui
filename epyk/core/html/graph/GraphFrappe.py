#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives
from epyk.core.py import types
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.css import Colors
from epyk.core.js import JsUtils
from epyk.core.html.options import OptChartFrappe
from epyk.core.js.packages import JsFrappe


class Frappe(MixHtmlState.HtmlOverlayStates, Html.Html):
    requirements = ('frappe-charts',)
    name = 'Frappe Mixed'
    _chart__type = 'axis-mixed'
    _option_cls = OptChartFrappe.FrappeLine
    builder_name = "FCharts"

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        super(Frappe, self).__init__(
            page, [], html_code=html_code, profile=profile, options=options,
            css_attrs={"width": width, "height": height})
        self.chartId = "%s_obj" % self.htmlCode
        self.options.type = self._chart__type
        self.__defined_options = None

    @property
    def shared(self) -> OptChartFrappe.OptionsChartSharedFrappe:
        """
        All the common properties shared between all the charts.
        This will ensure a compatibility with the plot method.

        Usage::

          line = page.ui.charts.chartJs.bar()
          line.shared.x_label("x axis")
        """
        return OptChartFrappe.OptionsChartSharedFrappe(self)

    @property
    def js(self) -> JsFrappe.FrappeCharts:
        """
        The Javascript functions defined for this component.
        Those can be specific ones for the module or generic ones from the language.

        Usage::

          btn = page.ui.button("Click").click([
            line.js.addDataPoint("test", [15, 67])
          ])

        :return: A Javascript Dom object functions.
        """
        if self._js is None:
            self._js = JsFrappe.FrappeCharts(selector="window['%s']" % self.chartId, component=self)
        return self._js

    @property
    def options(self) -> OptChartFrappe.FrappeLine:
        """ Chart specific options. """
        return super().options

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
                    Colors.getHexToRgb(h)[2], 0.8))
            else:
                line_colors.append(h[0])
                bg_colors.append(h[0])
        self.options.colors = line_colors
        return self

    def labels(self, values: list):
        """
        Set the series labels.

        :param values: The different values for the x-axis
        """
        self.options.data.labels = values

    def add_dataset(self, data, label, colors=None, opacity=None, kind=None):
        return self.options.data.add_data(data, label, kind or "line")

    @Html.jbuider("frappe")
    def build(self, data: types.JS_DATA_TYPES = None, options: types.JS_DATA_TYPES = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None, stop_state: bool = True):
        """
        Update the chart with context and / or data changes.

        :param data: Optional. The full datasets object expected by ChartJs
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Not used
        :param stop_state: Remove the top panel for the component state (error, loading...)
        """
        if data is not None:
            builder_fnc = JsUtils.jsWrap("%s(%s, %s)" % (
                self.builder_name, JsUtils.jsConvertData(data, None),
                self.__defined_options or self.options.config_js(options).toStr()), profile).toStr()
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(component_id)
            return '%(chartId)s.update(%(builder)s);%(state)s' % {
                'chartId': self.chartId, 'builder': builder_fnc, "state": state_expr}

        return '''%(chartId)s = new frappe.Chart("#%(hmlCode)s", %(config)s)
    ''' % {"chartId": self.chartId, "chartType": self._chart__type, "hmlCode": component_id or self.htmlCode,
           "config": self.options.config_js(options).toStr()}

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
        self.page.properties.js.add_builders(self.build())
        return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())


class FrappeLine(Frappe):
    name = 'Frappe Line'
    _chart__type = 'line'


class FrappeBar(Frappe):
    name = 'Frappe Bar'
    _chart__type = 'bar'


class FrappePie(Frappe):
    name = 'Frappe Pie'
    _chart__type = 'pie'


class FrappeDonut(Frappe):
    name = 'Frappe Donut'
    _chart__type = 'donut'


class FrappePercentage(Frappe):
    name = 'Frappe Percentage'
    _chart__type = 'percentage'


class FrappeHeatmap(Frappe):
    name = 'Frappe Heatmap'
    _chart__type = 'heatmap'
