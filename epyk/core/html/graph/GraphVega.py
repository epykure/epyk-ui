from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsVega
from epyk.core.html.options import OptChartVega
from epyk.core.py import types as etypes

from typing import List


class VegaEmdedCharts(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'Vega-Lite charts'
    tag = "div"
    requirements = ('vega-embed',)
    _option_cls = OptChartVega.OptionsChart
    _chart__type = "VegaChart"
    builder_module = "VCharts"

    def __init__(self, report, data, width, height, html_code, options, profile):
        super(VegaEmdedCharts, self).__init__(
            report, data, html_code=html_code, profile=profile, options=options,
            css_attrs={"width": width, "height": height})
        self.style.css.padding = "5px 50px"
        self.options.schema = "https://vega.github.io/schema/vega-lite/v5.json"

    @property
    def vega(self) -> JsVega.Vega:
        """JavaScript Vega Chart reference API.

        `Vega Doc <https://c3js.org/reference.html#api-show>`_

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsVega.Vega(self, js_code=self.js_code, page=self.page)
        return self._js

    @property
    def js(self) -> JsVega.VegaChart:
        """JavaScript Vega Chart reference API.

        `Vega Doc <https://c3js.org/reference.html#api-show>`_

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsVega.VegaChart(self, js_code=self.js_code, page=self.page)
        return self._js

    @Html.jformatter("vega")
    def build(self, data: etypes.JS_DATA_TYPES = None, options: etypes.OPTION_TYPE = None,
              profile: etypes.PROFILE_TYPE = False, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None) -> str:
        """Update the chart with context and / or data changes.

        :param data: List. Optional. The full datasets object expected by ChartJs.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param component_id: String. Not used.
        :param stop_state: Remove the top panel for the component state (error, loading...)
        :param dataflows: Chain of data transformations
        """
        self.js_code = component_id
        if data is not None:
            builder_fnc = JsUtils.jsWrap("%s(%s, %s)" % (
                self.builder_name, JsUtils.dataFlows(data, dataflows, self.page),
                self.options.config_js(options).toStr()), profile).toStr()
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(self.html_code)
            return """var changeSet = vega.changeset().remove(vega.truthy).insert(%(builder)s);
%(chartId)s.then(function (res) {res.view.change('table', changeSet).run();%(state)s})""" % {
                'chartId': self.js_code, 'builder': builder_fnc, "state": state_expr}

        return '%(chartId)s = vegaEmbed("#" + %(htmlCode)s, %(options)s)' % {
            "chartId": self.js_code, "htmlCode": JsUtils.jsConvertData(component_id or self.html_code, None),
            "options": self.options.config_js(options)}

    def colors(self, hex_values: List[str]):
        ...

    def labels(self, labels: list, series_id: str = None):
        ...

    def define(self, options: etypes.JS_DATA_TYPES = None, dataflows: List[dict] = None) -> str:
        """Not yet defined for this chart"""
        return ""

    def __str__(self):
        self.page.properties.js.add_builders(self.build())
        return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)
