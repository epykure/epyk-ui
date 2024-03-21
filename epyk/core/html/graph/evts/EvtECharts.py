from . import EvtChart
from epyk.core.py import types as etypes
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class EvtECharts(EvtChart):

    @property
    def point(self):
        """Return the selected point object"""
        return JsObjects.JsObject.JsObject.get("params")

    @property
    def index(self):
        """Return the selected point's index"""
        return JsObjects.JsNumber.JsNumber.get("params.dataIndex")

    @property
    def y(self):
        """Return the value of the selected point"""
        return JsObjects.JsNumber.JsNumber.get("params.value")

    @property
    def label(self):
        """Return the x axis for the selected point"""
        return JsObjects.JsString.JsString.get("params.name")

    @property
    def name(self):
        """Return the selected point's series index"""
        return JsObjects.JsString.JsString.get("params.seriesName")

    @property
    def series_index(self):
        """Return the selected point's series index"""
        return JsObjects.JsNumber.JsNumber.get("params.seriesIndex")

    @property
    def selected(self):
        """Get the selected value"""
        return JsUtils.JsObject.JsObject.get("params.selected")

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user clicks on any area of the chart.

        `Echarts <https://echarts.apache.org/en/api.html#events.Mouse%20events.click>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.onReady([self.component.js.on("click", js_funcs, profile)])

    def dblclick(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user double clicks on any area of the chart.

        `Echarts <https://echarts.apache.org/en/api.html#events.Mouse%20events.dblclick>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.onReady([self.component.js.on("dblclick", js_funcs, profile)])

    def mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user move over on any area of the chart.

        `Echarts <https://echarts.apache.org/en/api.html#events.Mouse%20events.mouseover>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.onReady([self.component.js.on("mouseover", js_funcs, profile)])

    def mouse_out(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user out over on any area of the chart.

        `Echarts <https://echarts.apache.org/en/api.html#events.Mouse%20events.mouseout>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.onReady([self.component.js.on("mouseout", js_funcs, profile)])

    def legend_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user click on a legend.

        `Echarts <https://echarts.apache.org/en/api.html#events.legendselectchanged>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.onReady([self.component.js.on("legendselectchanged", js_funcs, profile)])

    def x_axis_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.chart.events.xAxisLabelClick(js_funcs, profile)

    def select(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user select any area of the chart.

        `Echarts <https://echarts.apache.org/en/api.html#events.selectchanged>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.onReady([self.component.js.on("selectchanged", js_funcs, profile)])

    def unselect(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user select any area of the chart.

        `Echarts <https://echarts.apache.org/en/api.html#events.selectchanged>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.onReady([self.component.js.on("selectchanged", js_funcs, profile)])
