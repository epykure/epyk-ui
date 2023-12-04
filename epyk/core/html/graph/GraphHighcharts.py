
from typing import List
from epyk.core.css import Colors
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlHighCharts
from epyk.core.js.packages import JsHighcharts
from epyk.core.py import primitives
from epyk.core.py import types as etypes
from epyk.core.py import types
from epyk.core.html.mixins import MixHtmlState
from epyk.core.html import Html
from epyk.core.html.options import OptChartHighcharts


class Chart(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'Highcharts'
    tag = "div"
    requirements = ('highcharts',)
    _chart__type = None
    _option_cls = OptChartHighcharts.OptionsHighcharts
    builder_name = "Charts"

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        self.height = height[0]
        super(Chart, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
        self.style.css.margin_top = 10

    @property
    def options(self) -> OptChartHighcharts.OptionsHighcharts:
        """Property to the series options"""
        return super().options

    @property
    def dom(self) -> JsHtmlHighCharts.HighCharts:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtmlHighCharts.HighCharts(page=self.page, component=self)
        return self._dom

    def define(self, options: types.JS_DATA_TYPES = None, dataflows: List[dict] = None) -> str:
        if options is None:
            if dataflows is not None:
                return "%s;%s" % (
                    JsUtils.jsWrap(JsUtils.dataFlows(JsUtils.jsWrap("window['%s']" % self.js_code), dataflows, self.page)),
                    self.js.update())

        if dataflows is not None:
            options = JsUtils.jsWrap(JsUtils.dataFlows(options, dataflows, self.page))
        return self.js.update(options)

    def colors(self, hex_values: list):
        line_colors, bg_colors = [], []
        for h in hex_values:
            if h.upper() in Colors.defined:
                h = Colors.defined[h.upper()]['hex']
            if not isinstance(h, tuple):
                if h.startswith("#"):
                    line_colors.append(h)
                else:
                    line_colors.append(h)
            else:
                line_colors.append(h[0])
        self.options.colors = line_colors
        for i, rec in enumerate(self.options.js_tree.get("series", [])):
            rec.color = line_colors[i]

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False,
              source_event: str = None, on_ready: bool = False):
        js_funcs.insert(0, "let activePoints = [%s]" % self.dom.active())
        self.options.plotOptions.series.point.events.click(js_funcs=js_funcs, profile=profile)

    @property
    def js(self) -> JsHighcharts.Highcharts:
        if self._js is None:
            self._js = JsHighcharts.Highcharts(selector="window['%s']" % self.js_code, component=self, page=self.page)
        return self._js

    @Html.jformatter("highcharts")
    def build(self, data: etypes.JS_DATA_TYPES = None, options: etypes.JS_DATA_TYPES = None,
              profile: etypes.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        self.js_code = component_id
        if data is not None:
            builder_fnc = JsUtils.jsWrap("%s(%s, %s.options)" % (
                self.builder_name, JsUtils.dataFlows(data, dataflows, self.page), self.js_code), profile).toStr()
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(component_id)
            return """%(chartId)s = Highcharts.chart(%(htmlCode)s, %(builder)s)""" % {
                'chartId': self.js_code, "htmlCode": JsUtils.jsConvertData(component_id or self.html_code, None),
                'builder': builder_fnc, "state": state_expr}

        return '%(chartId)s = Highcharts.chart(%(htmlCode)s, %(ctx)s)' % {
            "chartId": self.js_code, "htmlCode": JsUtils.jsConvertData(component_id or self.html_code, None),
            "ctx": self.options.config_js(options)}

    def __str__(self):
        self.page.properties.js.add_builders(self.build())
        return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)
