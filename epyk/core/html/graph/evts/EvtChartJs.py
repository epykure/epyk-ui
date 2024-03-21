from . import EvtChart
from epyk.core.py import types as etypes
from epyk.core.js.primitives import JsObjects


class EvtChartJs(EvtChart):

    @property
    def point(self):
        """Return the selected point object"""
        return JsObjects.JsObject.JsObject.get(
            "%s.getElementsAtEventForMode(event, 'nearest', { intersect: true }, true)[0]" % self.component.js_code)

    @property
    def index(self):
        """Return the selected point's index"""
        return JsObjects.JsNumber.JsNumber.get(self.point.get_value(["index"]))

    @property
    def series_index(self):
        """Return the selected point's series index"""
        return JsObjects.JsNumber.JsNumber.get(self.point.get_value(["datasetIndex"]))

    @property
    def y(self):
        """Return the value of the selected point"""
        return JsObjects.JsObject.JsObject.get("%s.data.datasets[%s].data[%s]" % (self.component.js_code, self.series_index, self.index))

    @property
    def label(self):
        """Return the x axis for the selected point"""
        return JsObjects.JsObject.JsObject.get("%s.data.labels[%s]" % (self.component.js_code, self.index))

    @property
    def name(self):
        """Return the selected point's series name"""
        return JsObjects.JsObject.JsObject.get("%s.data.datasets[%s].label" % (self.component.js_code, self.series_index))

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Called if the event is of type 'mouseup', 'click' or ''contextmenu' over chartArea. Passed the event,
        an array of active elements, and the chart.

        `Billboard <https://www.chartjs.org/docs/latest/configuration/interactions.html>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.on("click", js_funcs, profile)

