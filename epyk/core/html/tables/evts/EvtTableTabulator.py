from . import EvtTable

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.py import types as etypes


class EvtTabulator(EvtTable):

    @property
    def cell(self):
        """Get the selected cell"""
        return JsUtils.JsObject.JsObject.get("cell._cell")

    @property
    def value(self):
        """Get the selected value"""
        return JsUtils.JsObject.JsObject.get("cell._cell.value")

    @property
    def row(self):
        """Get the selected row"""
        return JsUtils.JsObject.JsObject.get("row._row.data")

    @property
    def column_clicked_id(self):
        """Get the selected column ID"""
        return JsObjects.JsString.JsString.get("column._column.field")

    @property
    def column_clicked(self):
        """Get the selected column"""
        return JsUtils.JsObject.JsObject.get("column._column")

    def header_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The headerClick event is triggered when a user left clicks on a column or group header.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("headerClick", js_funcs, profile=profile, data_ref="column")
        ])

    def header_double_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The headerDblClick event is triggered when a user double clicks on a column or group header.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("headerDblClick", js_funcs, profile=profile, data_ref="column")
        ])

    def header_mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The headerMouseOver event is triggered when the mouse pointer moves over a column header, or any of its
        children.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("headerMouseOver", js_funcs, profile=profile, data_ref="column")
        ])

    def header_mouse_leave(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The headerMouseLeave event is triggered when the mouse pointer leaves a column header.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("headerMouseLeave", js_funcs, profile=profile, data_ref="column")
        ])

    def row_editing_start(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("row_editing_start() not yet available for table: %s" % self.component.name)

    def row_editing_stop(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("row_editing_stop() not yet available for table: %s" % self.component.name)

    def row_changed(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The rowUpdated event is triggered when a row is updated by the updateRow, updateOrAddRow,
        updateData or updateOrAddData, functions.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("rowUpdated", js_funcs, profile=profile, data_ref="row")
        ])

    def row_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The rowClick event is triggered when a user clicks on a row.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("rowClick", js_funcs, profile=profile, data_ref="row")
        ])

    def row_double_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The rowDblClick event is triggered when a user double clicks on a row.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("rowDblClick", js_funcs, profile=profile, data_ref="row")
        ])

    def row_selected(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The rowClick event is triggered when a user clicks on a row.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("rowClick", js_funcs, profile=profile, data_ref="cell")
        ])

    def cell_editing_start(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_editing_start() not yet available for table: %s" % self.component.name)

    def cell_editing_stop(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_editing_stop() not yet available for table: %s" % self.component.name)

    def cell_changed(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The rowUpdated event is triggered when a row is updated by the updateRow, updateOrAddRow,
        updateData or updateOrAddData, functions.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("rowUpdated", js_funcs, profile=profile, data_ref="row")
        ])

    def cell_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The cellClick event is triggered when a user left clicks on a cell.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("cellClick", js_funcs, profile=profile, data_ref="cell")
        ])

    def cell_double_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The cellDblClick event is triggered when a user double clicks on a cell

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("cellDblClick", js_funcs, profile=profile, data_ref="cell")
        ])

    def cell_focused(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        raise NotImplementedError("cell_focused() not yet available for table: %s" % self.component.name)

    def cell_mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The cellMouseOver event is triggered when the mouse pointer enters a cell or one of its child element.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("cellMouseOver", js_funcs, profile=profile, data_ref="cell")
        ])

    def cell_mouse_out(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The cellMouseOut event is triggered when the mouse pointer leaves a cell or one of its child element.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("cellMouseOut", js_funcs, profile=profile, data_ref="cell")
        ])

    def cell_mouse_down(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """The cellMouseDown event is triggered when the left mouse button is pressed with the cursor over a cell.

        `Tabulator <https://tabulator.info/docs/6.0/events>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self.component.onReady([
            self.component.js.on("cellMouseDown", js_funcs, profile=profile, data_ref="cell")
        ])
