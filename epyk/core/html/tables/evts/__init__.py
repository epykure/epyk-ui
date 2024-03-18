from epyk.core.py import types as etypes


class EvtTable:

    def __init__(self, page, component):
        self.page = page
        self.component = component

    def header_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("header_click() not yet available for table: %s" % self.component.name)

    def header_mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("header_mouse_over() not yet available for table: %s" % self.component.name)

    def header_mouse_leave(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("header_mouse_leave() not yet available for table: %s" % self.component.name)

    def row_editing_start(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("row_editing_start() not yet available for table: %s" % self.component.name)

    def row_editing_stop(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("row_editing_stop() not yet available for table: %s" % self.component.name)

    def row_changed(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("row_changed() not yet available for table: %s" % self.component.name)

    def row_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("row_click() not yet available for table: %s" % self.component.name)

    def row_double_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("row_double_click() not yet available for table: %s" % self.component.name)

    def row_selected(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("row_selected() not yet available for table: %s" % self.component.name)

    def cell_editing_start(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_editing_start() not yet available for table: %s" % self.component.name)

    def cell_editing_stop(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_editing_stop() not yet available for table: %s" % self.component.name)

    def cell_changed(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_changed() not yet available for table: %s" % self.component.name)

    def cell_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_click() not yet available for table: %s" % self.component.name)

    def cell_double_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_double_click() not yet available for table: %s" % self.component.name)

    def cell_focused(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_focused() not yet available for table: %s" % self.component.name)

    def cell_mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_mouse_over() not yet available for table: %s" % self.component.name)

    def cell_mouse_out(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_mouse_out() not yet available for table: %s" % self.component.name)

    def cell_mouse_down(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_mouse_down() not yet available for table: %s" % self.component.name)
