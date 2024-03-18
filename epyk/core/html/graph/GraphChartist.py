from typing import List
from epyk.core.py import types as etypes

from epyk.core.py import primitives
from epyk.core.css import Colors
from epyk.core.html.options import OptChartist
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.html.graph.evts import EvtChartist
from epyk.core.js.html import JsHtmlCharts
from epyk.core.js import JsUtils


class Chart(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'ChartList'
    tag = "div"
    _option_cls = OptChartist.OptionsChartistLine
    requirements = ('chartist',)
    builder_name = "EkChartist"
    _chart__type = "Line"

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        self.height = height[0]
        super(Chart, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
        self.style.css.margin_top = 10
        self.__defined_options = None

    @property
    def events(self) -> EvtChartist.EvtChartist:
        """Common Chart events"""
        return EvtChartist.EvtChartist(page=self.page, component=self)

    def colors(self, hex_values: list):
        """Set chart colors.

        :param hex_values: Colors list
        """
        line_colors, bg_colors = [], []
        alphabet = list(map(chr, range(97, 123)))
        styles = []
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
        for i, color in enumerate(line_colors):
            if i >= len(alphabet):
                break
            styles.append(".ct-series-%s .ct-line, .ct-series-%s .ct-point {stroke: %s;}" % (alphabet[i], alphabet[i], color))
        self.page.properties.css.add_text(" ".join(styles), "chartist-colors")

    @property
    def options(self) -> OptChartist.OptionsChartistLine:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def dom(self) -> JsHtmlCharts.ChartJs:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtmlCharts.Chartist(page=self.page, component=self, js_code=self.js_code)
        return self._dom

    def define(self, options: etypes.JS_DATA_TYPES = None, dataflows: List[dict] = None, component_id: str = None) -> str:
        """Override the chart settings on the JavaScript side.
        This will allow ot set specific styles for some series or also add commons properties.

        :param options: JavaScript of Python attributes
        :param dataflows: Chain of config transformations:
        """
        self.js_code = component_id
        if options is None:
            if dataflows is not None:
                return "let chartCtx = %(config)s;window['%(chartId)s'].update(null, chartCtx)" % {
                    "config": JsUtils.jsWrap(JsUtils.dataFlows(JsUtils.jsWrap("window['%s']" % self.js_code), dataflows, self.page)),
                    'chartId': self.js_code}

        if dataflows is not None:
            options = JsUtils.jsWrap(JsUtils.dataFlows(options, dataflows, self.page))
        return """window['%(chartId)s'].update(null, %(ctx)s)""" % {
            'chartId': self.js_code, "ctx": JsUtils.jsConvertData(options, None)}

    @Html.jformatter("chartist")
    def build(self, data: etypes.JS_DATA_TYPES = None, options: etypes.JS_DATA_TYPES = None,
              profile: etypes.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """Update the chart with context and / or data changes.

        :param data: Optional. The full datasets object expected by ChartJs
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. Not used
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
            return """%(chartId)s.update(%(builder)s, %(ctx)s);%(state)s""" % {
                'chartId': self.js_code, 'builder': builder_fnc, "state": state_expr,
                "ctx": self.options.config_js(options).toStr()}

        return '%(chartId)s = new Chartist.%(chartType)s("#"+ %(htmlCode)s, %(ctx)s)' % {
            "chartId": self.js_code, "htmlCode": JsUtils.jsConvertData(component_id or self.html_code, None),
            "ctx": self.options.config_js(options).toStr(), "chartType": self._chart__type}

    def __str__(self):
        self.page.properties.js.add_builders(self.build())
        return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


class ChartBar(Chart):
    _chart__type = 'Bar'
    _option_cls = OptChartist.OptionsChartistBar

    @property
    def options(self) -> OptChartist.OptionsChartistBar:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options


class ChartPie(Chart):
    _chart__type = 'Pie'
    builder_name = "EkChartistPie"
    _option_cls = OptChartist.OptionsChartistPie

    @property
    def options(self) -> OptChartist.OptionsChartistPie:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options
