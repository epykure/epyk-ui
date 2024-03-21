from . import EvtChart
from epyk.core.py import types as etypes
from epyk.core.js.primitives import JsObjects


class EvtApexCharts(EvtChart):

    @property
    def point(self):
        """Return the selected point object"""
        return JsObjects.JsObject.JsObject.get("config")

    @property
    def y(self):
        """Return the value of the selected point"""
        return JsObjects.JsNumber.JsNumber.get("config.config.series[config.seriesIndex].data[config.dataPointIndex]")

    @property
    def index(self):
        """Return the selected point's index"""
        return JsObjects.JsNumber.JsNumber.get("config.dataPointIndex")

    @property
    def series_index(self):
        """Return the selected point's series index"""
        return JsObjects.JsNumber.JsNumber.get("config.seriesIndex")

    @property
    def name(self):
        """Return the selected point's series name"""
        return JsObjects.JsString.JsString.get("config.config.series[config.seriesIndex].name")

    @property
    def label(self):
        """Return the x axis for the selected point"""
        return JsObjects.JsNumber.JsNumber.get("config.config.xaxis.categories[config.dataPointIndex]")

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user clicks on any area of the chart.

        `ApexChart <https://apexcharts.com/docs/options/chart/events/>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.options.chart.events.click(js_funcs, profile)

    def mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user moves mouse on any area of the chart.

        `ApexChart <https://apexcharts.com/docs/options/chart/events/>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.options.chart.events.mouseMove(js_funcs, profile)

    def mouse_out(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user moves mouse outside chart area (exclusing axis).

        `ApexChart <https://apexcharts.com/docs/options/chart/events/>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.options.chart.events.mouseLeave(js_funcs, profile)

    def legend_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user clicks on legend.

        `ApexChart <https://apexcharts.com/docs/options/chart/events/>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.options.chart.events.legendClick(js_funcs, profile)

    def marker_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user clicks on the markers.

        `ApexChart <https://apexcharts.com/docs/options/chart/events/>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.options.chart.events.markerClick(js_funcs, profile)

    def x_axis_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when user clicks on the x-axis labels.

        `ApexChart <https://apexcharts.com/docs/options/chart/events/>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.options.chart.events.xAxisLabelClick(js_funcs, profile)
