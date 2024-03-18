
from typing import List

from epyk.core.css import Colors
from epyk.core.py import types
from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.html.options import OptChartECharts
from epyk.core.html.graph.evts import EvtECharts
from epyk.core.html.mixins import MixHtmlState
from epyk.core.js import JsUtils


class ECharts(MixHtmlState.HtmlOverlayStates, Html.Html):
    requirements = ('echarts',)
    name = 'ECharts'
    tag = "div"
    _option_cls = OptChartECharts.EChartOptions
    builder_name = "EkECharts"

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        super(ECharts, self).__init__(
            page, [], html_code=html_code, profile=profile, options=options,
            css_attrs={"width": width, "height": height})

    def _set_js_code(self, html_code: str, js_code: str):
        """Set a different code for the component.
        This method will ensure both HTML and Js references will be properly changed for this component.
        This method is used by the js_code property and should not be used directly.

        :param html_code: The new HTML code
        :param js_code: The new JavaScript code
        """
        self.js.varName = js_code
        self.dom.varName = "document.getElementById(%s)" % JsUtils.jsConvertData(html_code, None)

    def colors(self, hex_values: list):
        """Set the colors of the chart.

        hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
        If the background colors are not specified they will be deduced from the colors list changing the opacity.

        Usage::

            from epyk.mocks import randoms

            chart = page.ui.charts.chartJs.line(randoms.languages, y_columns=["rating", 'change'], x_axis='name')
            chart.colors(["#FFFF00", "#FFA500"])

        :param hex_values: An array of hexadecimal color codes
        """
        line_colors, bg_colors = [], []
        for h in hex_values:
            if h.upper() in Colors.defined:
                h = Colors.defined[h.upper()]['hex']
            if not isinstance(h, tuple):
                if h.startswith("#"):
                    line_colors.append(h)
                    bg_colors.append("rgb(%s, %s, %s)" % (
                        Colors.getHexToRgb(h)[0], Colors.getHexToRgb(h)[1],
                        Colors.getHexToRgb(h)[2]))
                else:
                    line_colors.append(h)
                    bg_colors.append(h)
            else:
                line_colors.append(h[0])
                bg_colors.append(h[0])
        self.options.js_tree["_ek"]["colors"] = line_colors
        self.options.js_tree["_ek"]["background_colors"] = bg_colors
        for i, rec in enumerate(self.options.js_tree.get("series", [])):
            if self.options.js_tree["_ek"]["chart"]["type"] in ["pie", "polarArea"]:
                rec.color = self.options.colors
            else:
                rec.color = self.options.colors[i]
            rec.borderWidth = 1

    def define(self, options: types.JS_DATA_TYPES = None, dataflows: List[dict] = None, component_id: str = None) -> str:
        """Override the chart settings on the JavaScript side.
        This will allow ot set specific styles for some series or also add commons properties.

        Usage:

          chart.onReady([chart.define({"commons": {"backgroundColor": ["pink"], "label": "Other series"}})])

        :param options: JavaScript of Python attributes
        :param dataflows: Chain of config transformations
        """
        defined_options = "window.%s_options" % self.html_code
        js_expr = "%s = Object.assign(%s ?? %s, %s)" % (
            defined_options, defined_options, self.options.config_js(), JsUtils.dataFlows(options, dataflows, self.page))
        self.__defined_options = defined_options
        return js_expr

    @Html.jformatter("echarts")
    def build(self, data: types.JS_DATA_TYPES = None, options: types.JS_DATA_TYPES = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """

        """
        self.js_code = component_id
        builder_fnc = JsUtils.jsWrap("%s(%s, %s)" % (
            self.builder_name, JsUtils.dataFlows(data or [], dataflows, self.page),
            self.options.config_js(options).toStr()), profile).toStr()

        if data is not None:
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(self.html_code)
            return '%(chartId)s.setOption(%(builder)s);%(state)s' % {
                'chartId': self.js_code, 'builder': builder_fnc, "state": state_expr}

        return '''%(chartId)s = window.echarts.init(document.getElementById(%(hmlCode)s)); %(chartId)s.setOption(%(builder)s);
        ''' % {"chartId": self.js_code, "hmlCode": JsUtils.jsConvertData(component_id or self.htmlCode, None),
               'builder': builder_fnc}

    @property
    def events(self) -> EvtECharts.EvtECharts:
        """Common Chart events"""
        return EvtECharts.EvtECharts(page=self.page, component=self)

    def __str__(self):
        self.page.properties.js.add_builders(self.build())
        return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)
