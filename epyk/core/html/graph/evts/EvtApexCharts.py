from . import EvtChart
from epyk.core.py import types as etypes
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class EvtApexCharts(EvtChart):

    @property
    def point(self):
        return JsObjects.JsObject.JsObject.get("config")

    @property
    def y(self):
        return JsObjects.JsNumber.JsNumber.get("config.config.series[config.seriesIndex].data[config.dataPointIndex]")

    @property
    def index(self):
        return JsObjects.JsNumber.JsNumber.get("config.dataPointIndex")

    @property
    def series_index(self):
        return JsObjects.JsNumber.JsNumber.get("config.seriesIndex")

    @property
    def name(self):
        return JsObjects.JsString.JsString.get("config.config.series[config.seriesIndex].name")

    @property
    def label(self):
        return JsObjects.JsNumber.JsNumber.get("config.config.xaxis.categories[config.dataPointIndex]")

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.chart.events.click(js_funcs, profile)

    def mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.chart.events.mouseMove(js_funcs, profile)

    def mouse_out(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.chart.events.mouseLeave(js_funcs, profile)

    def legend_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.chart.events.legendClick(js_funcs, profile)

    def marker_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.chart.events.markerClick(js_funcs, profile)

    def x_axis_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.chart.events.xAxisLabelClick(js_funcs, profile)
