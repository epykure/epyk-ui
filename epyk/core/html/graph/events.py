from epyk.core.js.primitives import JsObjects
from epyk.core.py import types as etypes


class EvtChart:

    def __init__(self, page, component):
        self.page = page
        self.component = component

    @property
    def params(self):
        return JsObjects.JsObjects.get("params")

    def select(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("select() not yet available for chart: %s" % self.component.name)

    def unselect(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("unselect() not yet available for chart: %s" % self.component.name)

    def change(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("change() not yet available for chart: %s" % self.component.name)

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("click() not yet available for chart: %s" % self.component.name)

    def double_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("double_click() not yet available for chart: %s" % self.component.name)

    def mouse_down(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("mouse_down() not yet available for chart: %s" % self.component.name)

    def mouse_up(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("mouse_up() not yet available for chart: %s" % self.component.name)

    def mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("mouse_over() not yet available for chart: %s" % self.component.name)

    def mouse_out(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("mouse_out() not yet available for chart: %s" % self.component.name)

    def legend_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("legend_click() not yet available for chart: %s" % self.component.name)

    def marker_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("marker_click() not yet available for chart: %s" % self.component.name)

    def x_axis_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("x_axis_click() not yet available for chart: %s" % self.component.name)
