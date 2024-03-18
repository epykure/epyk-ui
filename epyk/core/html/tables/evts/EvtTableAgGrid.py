from . import EvtTable
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.py import types as etypes


class EvtAggrid(EvtTable):

    @property
    def value(self):
        """Get the selected value"""
        return JsUtils.JsObject.JsObject.get("param.value")

    @property
    def data(self):
        """Get the selected data"""
        return JsUtils.JsObject.JsObject.get("param")

    @property
    def column_clicked(self):
        """Get the selected column definition"""
        return JsUtils.JsObject.JsObject.get("param.column")

    @property
    def column_clicked_id(self):
        """Get the selected column ID"""
        return JsObjects.JsString.JsString.get("param.column.colId")

    @property
    def row_clicked(self):
        """Get the selected row"""
        return JsUtils.JsObject.JsObject.get("param.data")

    @property
    def row_clicked_index(self):
        """Get the selected row index"""
        return JsObjects.JsNumber.JsNumber.get("param.rowIndex")

    def header_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                     func_ref: bool = False):
        """A click is performed on a column header.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/cell-editing/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onColumnHeaderClicked(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def header_mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                          func_ref: bool = False):
        """A mouse cursor is initially moved over a column header.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/#reference-columns-columnHeaderClicked>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onColumnHeaderMouseOver(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def header_mouse_leave(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                           func_ref: bool = False):
        """A mouse cursor is moved out of a column header.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/#reference-columns-columnHeaderClicked>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onColumnHeaderMouseLeave(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def row_editing_start(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                          func_ref: bool = False):
        """Editing a row has started (when row editing is enabled). When row editing, this event will be fired once and
        cellEditingStarted will be fired for each individual cell. Only fires when doing Full Row Editing.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/#reference-columns-columnHeaderClicked>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onRowEditingStarted(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def row_editing_stop(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                         func_ref: bool = False):
        """Editing a row has stopped (when row editing is enabled). When row editing, this event will be fired once
        and cellEditingStopped will be fired for each individual cell. Only fires when doing Full Row Editing.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/#reference-columns-columnHeaderClicked>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onRowEditingStopped(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def row_changed(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                    func_ref: bool = False):
        """Row selection is changed. Use the grid API getSelectedNodes() or getSelectedRows() to get the new list of
        selected nodes / row data.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-selection/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onRowValueChanged(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def row_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                  func_ref: bool = False):
        """Row is clicked.

        `Related Pages <https://ag-grid.com/angular-data-grid/grid-interface/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onRowClicked(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def row_double_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                         func_ref: bool = False):
        """Row is double clicked.

        `Related Pages <https://ag-grid.com/angular-data-grid/grid-interface/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onRowDoubleClicked(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def row_selected(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                     func_ref: bool = False):
        """Row is selected or deselected. The event contains the node in question, so call the node's isSelected()
        method to see if it was just selected or deselected.

        `Related Pages <https://ag-grid.com/angular-data-grid/grid-interface/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onRowSelected(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def cell_editing_start(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                           func_ref: bool = False):
        """Editing a cell has started..

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/cell-editing/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onCellEditingStarted(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def cell_editing_stop(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                          func_ref: bool = False):
        """Editing a cell has stopped.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/cell-editing/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onCellEditingStopped(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def cell_changed(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                     func_ref: bool = False):
        """Value has changed after editing (this event will not fire if editing was cancelled, eg ESC was pressed) or
        if cell value has changed as a result of paste operation.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/cell-editing/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onCellValueChanged(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def cell_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                   func_ref: bool = False):
        """Cell is clicked.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onCellClicked(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def cell_double_click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                          func_ref: bool = False):
        """Cell is double clicked.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onCellDoubleClicked(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def cell_focused(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                     func_ref: bool = False):
        """Cell is focused.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onCellFocused(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def cell_mouse_over(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                        func_ref: bool = False):
        """Mouse entered cell.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onCellMouseOver(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def cell_mouse_out(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                       func_ref: bool = False):
        """Mouse left cell.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onCellMouseOut(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def cell_mouse_down(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                        func_ref: bool = False):
        """Mouse down on cell.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        return self.component.options.onCellMouseDown(js_funcs=js_funcs, profile=profile, func_ref=func_ref)
