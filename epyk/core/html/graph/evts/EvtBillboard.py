from . import EvtChart
from epyk.core.py import types as etypes
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class EvtBillboard(EvtChart):

    @property
    def point(self):
        """Return the selected point object"""
        return JsObjects.JsObject.JsObject.get("d")

    @property
    def x(self):
        return JsObjects.JsNumber.JsNumber.get("d.x")

    @property
    def index(self):
        """Return the selected point's index"""
        return JsObjects.JsNumber.JsNumber.get("d.index")

    @property
    def y(self):
        """Return the value of the selected point"""
        return JsUtils.JsObject.JsObject.get("d.value")

    @property
    def name(self):
        """Return the selected point's series name"""
        return JsObjects.JsString.JsString.get("d.name")

    def select(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Set data points to be selected. (data.selection.enabled option should be set true to use this method).

        `Billboard <https://naver.github.io/billboard.js/release/latest/doc/Chart.html#select>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.options.data.onselected(js_funcs, profile)

    def unselect(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Set data points to be un-selected.

        `Billboard <https://naver.github.io/billboard.js/release/latest/doc/Chart.html#unselect>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.options.data.onunselected(js_funcs, profile)

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Set a callback to execute when the chart is initialized.

        `Billboard <https://naver.github.io/billboard.js/release/latest/doc/Options.html#.onclick>`_

        :param js_funcs: Set of Javascript function to trigger on this event
        :param profile: Optional. A flag to set the component performance storage
        """
        self.component.options.data.onclick(js_funcs, profile)

    def mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.data.onmouseover(js_funcs, profile)

    def mouse_out(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.data.onmouseout(js_funcs, profile)
