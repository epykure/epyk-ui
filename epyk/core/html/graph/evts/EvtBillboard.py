from . import EvtChart
from epyk.core.py import types as etypes
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class EvtBillboard(EvtChart):

    @property
    def point(self):
        return JsObjects.JsObject.JsObject.get("d")

    @property
    def x(self):
        return JsObjects.JsNumber.JsNumber.get("d.x")

    @property
    def index(self):
        return JsObjects.JsNumber.JsNumber.get("d.index")

    @property
    def y(self):
        """Get the selected value"""
        return JsUtils.JsObject.JsObject.get("d.value")

    @property
    def name(self):
        return JsObjects.JsString.JsString.get("d.name")

    def select(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.data.onselected(js_funcs, profile)

    def unselect(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.data.onunselected(js_funcs, profile)

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.data.onclick(js_funcs, profile)

    def mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.data.onmouseover(js_funcs, profile)

    def mouse_out(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        self.component.options.data.onmouseout(js_funcs, profile)
