from typing import Optional, List
from epyk.core.py import types as etypes

from epyk.core.py import primitives
from epyk.core.css import Colors
from epyk.core.html.options import OptChartist
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.js import JsUtils


class Chart(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'ChartList'
    _option_cls = OptChartist.OptionsChartistLine
    requirements = ('chartist',)
    builder_name = "EkChartist"
    _chart__type = "Line"

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        self.height = height[0]
        super(Chart, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
        self.style.css.margin_top = 10
        self.chartId = "%s_obj" % self.htmlCode
        self.__defined_options = None

    @Html.jformatter("chartist")
    def build(self, data: etypes.JS_DATA_TYPES = None, options: etypes.JS_DATA_TYPES = None,
              profile: etypes.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """
        Update the chart with context and / or data changes.

        :param data: Optional. The full datasets object expected by ChartJs
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. Not used
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
            return """window['%(chartId)s'].update(%(builder)s);%(state)s""" % {
                'chartId': self.chartId, 'builder': builder_fnc, "state": state_expr}

        return '%(chartId)s = new Chartist.%(chartType)s("#%(htmlCode)s", {}, %(ctx)s)' % {
            "chartId": self.chartId, "htmlCode": self.html_code, "ctx": {}, "chartType": self._chart__type}

    def __str__(self):
        self.page.properties.js.add_builders(self.build())
        return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())


class ChartBar(Chart):
    _chart__type = 'Bar'


class ChartPie(Chart):
    _chart__type = 'Pie'
