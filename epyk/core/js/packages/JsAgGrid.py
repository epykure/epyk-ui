#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Any, Union, Optional, List, Tuple
from epyk.core.py import primitives, types
from epyk.core.js.packages import JsPackage
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class ColumnComponent(JsPackage):
    lib_alias = {"js": "ag-grid-community", "css": "ag-grid-community"}
    lib_selector = "column"

    @property
    def field(self):
        return JsObjects.JsObject.JsObject("%s.colDef.field" % self.varId)

    def getId(self):
        return JsObjects.JsString.JsString("%s.getId()" % self.varId)

    def cellStyle(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
        """This sub function will use p as sub parameter to not corrupt the main event.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if not str_func.startswith("function(p)") and not func_ref:
            str_func = "function(p){%s}" % str_func
        return JsUtils.jsWrap(str_func)


class DataComponent(JsPackage):
    lib_alias = {"js": "ag-grid-community", "css": "ag-grid-community"}
    lib_selector = "data"


class NodeComponent(JsPackage):
    lib_alias = {"js": "ag-grid-community", "css": "ag-grid-community"}
    lib_selector = "node"

    @property
    def id(self):
        return JsObjects.JsString.JsString("%s.id" % self.varId)


class _Export:

    @property
    def column(self):
        return ColumnComponent(selector="param.column")

    @property
    def data(self):
        return DataComponent(selector="param.data")

    @property
    def node(self):
        return NodeComponent(selector="param.node")

    @property
    def param(self):
        """ Variable received in the aggrid methods. """
        return JsObjects.JsObject.JsObject("param")

    @property
    def newValue(self):
        """  """
        return JsObjects.JsObject.JsObject("param.newValue")

    @property
    def oldValue(self):
        """ """
        return JsObjects.JsObject.JsObject("param.oldValue")

    def rowIndex(self, js_code: str = "param"):
        return JsObjects.JsNumber.JsNumber("%s.rowIndex" % js_code)


class ColumnApi:

    def __init__(self, page: primitives.PageModel, js_code: str):
        self.varId = js_code
        self.page = page

    def sizeColumnsToFit(self, width):
        """Gets the grid to size the columns to the specified width in pixels, e.g. sizeColumnsToFix(900).
        To have the grid fit the columns to the grid's width, use the Grid API gridApi.sizeColumnsToFit() instead.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_

        :param width:
        """
        return JsObjects.JsVoid("%s.sizeColumnsToFit(%s)" % (self.varId, JsUtils.jsConvertData(width, None)))

    def getColumnGroup(self, name: str):
        """Returns the column group with the given name.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_

        :param name:
        """
        return JsObjects.JsVoid("%s.getColumnGroup(%s)" % (self.varId, JsUtils.jsConvertData(name, None)))

    def getColumn(self, name: str):
        """Returns the column with the given colKey, which can either be the colId (a string) or the colDef (an object).
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_

        :param name:
        """
        return JsObjects.JsVoid("%s.getColumn(%s)" % (self.varId, JsUtils.jsConvertData(name, None)))

    def getColumnState(self):
        """Gets the state of the columns. It is used when saving column state.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.getColumnState()" % self.varId)

    def setColumnState(self, column_state):
        """Sets the state of the columns from a previous state. Returns false if one or more columns could not be found.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.setColumnState(%s)" % (self.varId, JsUtils.jsConvertData(column_state, None)))

    def resetColumnState(self):
        """Sets the state back to match the originally provided column definitions.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.resetColumnState()" % self.varId)

    def isPinning(self):
        """Returns true if pinning left or right, otherwise false.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.isPinning()" % self.varId)

    def isPinningLeft(self):
        """Returns true if pinning left, otherwise false.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.isPinningLeft()" % self.varId)

    def isPinningRight(self):
        """Returns true if pinning right, otherwise false.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.isPinningRight()" % self.varId)

    def setColumnVisible(self, col_name: str, visible: bool):
        """Sets the visibility of a column. Key can be the column ID or Column object.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_

        :param col_name: The column name
        :param visible:
        """
        col_name = JsUtils.jsConvertData(col_name, None)
        visible = JsUtils.jsConvertData(visible, None)
        return JsObjects.JsVoid("%s.setColumnVisible(%s. %s)" % (self.varId, col_name, visible))

    def setColumnsVisible(self, col_names, visible):
        """Same as setColumnVisible, but provide a list of column keys.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        col_names = JsUtils.jsConvertData(col_names, None)
        visible = JsUtils.jsConvertData(visible, None)
        return JsObjects.JsVoid("%s.setColumnsVisible(%s. %s)" % (self.varId, col_names, visible))

    def setColumnPinned(self, col_name: str, pinned: bool):
        """Sets the column pinned / unpinned. Key can be the column ID, field, ColDef object or Column object.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        col_name = JsUtils.jsConvertData(col_name, None)
        pinned = JsUtils.jsConvertData(pinned, None)
        return JsObjects.JsVoid("%s.setColumnPinned(%s. %s)" % (self.varId, col_name, pinned))

    def setColumnsPinned(self, col_names, pinned):
        """Sets the column pinned / unpinned. Key can be the column ID, field, ColDef object or Column object.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        col_names = JsUtils.jsConvertData(col_names, None)
        pinned = JsUtils.jsConvertData(pinned, None)
        return JsObjects.JsVoid("%s.setColumnsPinned(%s. %s)" % (self.varId, col_names, pinned))

    def getColumnGroupState(self):
        """Gets the state of the column groups. Typically used when saving column group state.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.getColumnGroupState()" % self.varId)

    def autoSizeColumn(self, col_name: str):
        """Auto-sizes a column based on its contents.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.autoSizeColumn(%s)" % (self.varId, JsUtils.jsConvertData(col_name, None)))

    def autoSizeColumns(self, col_names: list):
        """Same as autoSizeColumn, but provide a list of column keys.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.autoSizeColumns(%s)" % (self.varId, JsUtils.jsConvertData(col_names, None)))

    def getDisplayNameForColumn(self, name: str):
        """Returns the display name for a column.
        Useful if you are doing your own header rendering and want the grid to work out if headerValueGetter is used, or
        if you are doing your own column management GUI, to know what to show as the column name.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_

        :param name:
        """
        return JsObjects.JsVoid("%s.getDisplayNameForColumn(%s)" % (self.varId, JsUtils.jsConvertData(name, None)))

    def getAllColumns(self):
        """Returns all the columns, regardless of visible or not.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.getAllColumns()" % self.varId)

    def getAllGridColumns(self):
        """Returns all the grid columns, same as getAllColumns(), except a) it has the order of the columns that are
        presented in the grid and b) it's after the 'pivot' step, so if pivoting, has the value columns for the pivot.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.getAllGridColumns()" % self.varId)

    def getPrimaryColumns(self):
        """Returns the grid's primary columns.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.getPrimaryColumns()" % self.varId)

    def getSecondaryColumns(self):
        """Returns the grid's secondary columns.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.getSecondaryColumns()" % self.varId)

    def getAllDisplayedVirtualColumns(self):
        """Same as getAllGridColumns(), except only returns rendered columns, i.e. columns that are not within the
        viewport and therefore not rendered, due to column virtualization, are not displayed.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.getAllDisplayedVirtualColumns()" % self.varId)

    def moveColumn(self, col_name, to_index):
        """Moves a column to toIndex. The column is first removed, then added at the toIndex location, thus index
        locations will change to the right of the column after the removal.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_

        :param col_name:
        :param to_index:
        """
        col_name = JsUtils.jsConvertData(col_name, None)
        to_index = JsUtils.jsConvertData(to_index, None)
        return JsObjects.JsVoid("%s.moveColumn(%s, %s)" % (self.varId, col_name, to_index))

    def moveColumns(self, col_names, to_index):
        """Moves a column to toIndex. The column is first removed, then added at the toIndex location, thus index
        locations will change to the right of the column after the removal.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_

        :param col_names:
        :param to_index:
        """
        col_names = JsUtils.jsConvertData(col_names, None)
        to_index = JsUtils.jsConvertData(to_index, None)
        return JsObjects.JsVoid("%s.moveColumns(%s, %s)" % (self.varId, col_names, to_index))

    def setColumnAggFunc(self, column, agg_func):
        """Sets the agg function for a column. aggFunc can be one of 'min' | 'max' | 'sum'.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_

        :param column:
        :param agg_func:
        """
        column = JsUtils.jsConvertData(column, None)
        agg_func = JsUtils.jsConvertData(agg_func, None)
        return JsObjects.JsVoid("%s.setColumnAggFunc(%s, %s)" % (self.varId, column, agg_func))

    def setColumnWidth(self, col_name, new_width, finished=True):
        """Sets the column width on a single column. The finished flag gets included in the resulting event and not used
        internally by the grid.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_

        :param col_name:
        :param new_width:
        :param finished:
        """
        col_name = JsUtils.jsConvertData(col_name, None)
        new_width = JsUtils.jsConvertData(new_width, None)
        finished = JsUtils.jsConvertData(finished, None)
        return JsObjects.JsVoid("%s.setColumnWidth(%s, %s, %s)" % (self.varId, col_name, new_width, finished))

    def setColumnWidths(self, column_widths, finished=True):
        """Sets the column width on a single column. The finished flag gets included in the resulting event and not used
        internally by the grid.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_

        :param column_widths:
        :param finished:
        """
        column_widths = JsUtils.jsConvertData(column_widths, None)
        finished = JsUtils.jsConvertData(finished, None)
        return JsObjects.JsVoid("%s.setColumnWidth(%s, %s)" % (self.varId, column_widths, finished))

    def custom(self, func_nam: str, *argv):
        """Generic function to call any missing function form a package.
        This will automatically convert the object to JavaScript and also put the right object reference.

        :param func_nam: The function name
        :param argv: Objects. Optional. The function arguments on the JavasScript side
        """
        js_args = []
        for arg in argv:
            js_args.append(str(JsUtils.jsConvertData(arg, None)))
        return JsObjects.JsObject.JsObject.get("%s.%s(%s)" % (self.varId, func_nam, ", ".join(js_args)))


class AgGrid(JsPackage):
    lib_alias = {"js": "ag-grid-community", "css": "ag-grid-community"}

    #  -----------------------------------------
    #  Common table javascript interface
    #  -----------------------------------------

    @property
    def api(self):
        """Switch JavaScript definition to the appropriate api"""
        if self.component.options.useCreateGrid:
            return JsObjects.JsObject.JsObject.get(self.varId)

        return JsObjects.JsObject.JsObject.get("%s.api" % self.varId)

    def add_row(self, data, flag: Union[types.JS_DATA_TYPES, bool] = False, dataflows: List[dict] = None):
        row = JsUtils.dataFlows(data, dataflows, self.page)
        return JsObjects.JsVoid(
            "%(tableId)s.gridOptions.rowData.push(%(row)s); %(tableId)s.gridApi.setRowData(this.gridOptions.rowData)" % {
                "tableId": self.varId, "row": row})

    def empty(self):
        """ Empty the table """
        return self.setRowData([])

    def download(self, filename: str = None, options: dict = None, *args, **kwargs):
        """Common download feature for tables.
        `Related Pages <http://tabulator.info/docs/4.0/download>`_

        :param filename: Filename
        :param options: Download option
        """
        if filename and filename.endswith(".xls"):
            if not options:
                options = {}
            options["fileName"] = filename
            return self.exportDataAsExcel(options)

        else:
            filename = filename or "%s.csv" % self.component.html_code
            if not options:
                options = {}
            options["fileName"] = filename
            return self.exportDataAsCsv(options)

    def show_column(self, column: str):
        return self.columnApi.setColumnVisible(column, False)

    def hide_column(self, column: str):
        return self.columnApi.setColumnVisible(column, True)

    def redraw(self, flag: bool = False):
        return ""

    #  -----------------------------------------
    #  Specific table javascript interface
    #  -----------------------------------------

    def applyTransaction(self, transaction):
        """Update row data. Pass a transaction object with lists for add, remove and update.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_

        :param transaction:
        """
        return JsObjects.JsVoid("%s.applyTransaction(%s)" % (self.api, JsUtils.jsConvertData(transaction, None)))

    def applyTransactionAsync(self, transaction, callback):
        """Same as applyTransaction except executes asynchronous for efficiency.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_

        :param transaction:
        :param callback:
        """
        return JsObjects.JsVoid("%s.applyTransaction(%s, %s)" % (
            self.api, JsUtils.jsConvertData(transaction, None), callback))

    def collapseAll(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grouping-opening-groups/#opening-group-levels-by-default>`_
        """
        return ColumnApi(self.page, "%s.collapseAll" % self.api)

    @property
    def columnApi(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-definitions/>`_
        """
        return ColumnApi(self.page, "%s.columnApi" % self.varId)

    def expandAll(self):
        """

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grouping-opening-groups/#opening-group-levels-by-default>`_
        """
        return ColumnApi(self.page, "%s.expandAll" % self.api)

    def exportDataAsCsv(self, csv_export_params: dict = None):
        """The grid data can be exported to CSV with an API call, or using the right-click context menu
        (Enterprise only) on the Grid.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/csv-export/>`_
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/csv-export/#csvexportparams>`_

        :param csv_export_params: CSV export options
        """
        if csv_export_params is not None:
            return JsObjects.JsVoid(
                "%s.exportDataAsCsv(%s)" % (self.api, JsUtils.jsConvertData(csv_export_params, None)))

        return JsObjects.JsVoid("%s.exportDataAsCsv()" % self.api)

    def exportDataAsExcel(self, excel_export_params: dict = None):
        """Downloads an Excel export of the grid's data.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/excel-export-api/#excelexportparams>`_

        :param excel_export_params: CSV export options
        """
        if excel_export_params is not None:
            return JsObjects.JsVoid(
                "%s.exportDataAsExcel(%s)" % (self.api, JsUtils.jsConvertData(excel_export_params, None)))

        return JsObjects.JsVoid("%s.exportDataAsExcel()" % self.api)

    def getColumnDefs(self):
        """Call to set new column definitions. The grid will redraw all the column headers, and then redraw all of the rows.
        `Related Pages <https://www.ag-grid.com/documentation/javascript/column-updating-definitions/>`_
        """
        return JsObjects.JsObject.JsObject("%s.getColumnDefs()" % self.api)

    def getDataAsCsv(self, params: dict = None) -> JsObjects.JsString.JsString:
        """Similar to exportDataAsCsv, except returns the result as a string rather than download it.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-api/>`_

        :param params
        """
        if not params:
            return JsObjects.JsString.JsString.get("%s.getDataAsCsv(%s)" % (
                self.api, JsUtils.jsConvertData(params, None)))

        return JsObjects.JsString.JsString.get("%s.getDataAsCsv()" % self.api)

    def getDataAsExcel(self, params: dict = None) -> JsObjects.JsString.JsString:
        """Similar to exportDataAsExcel, except instead of downloading a file, it will return a Blob to be processed by the user.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-api/>`_

        :param params
        """
        if not params:
            return JsObjects.JsString.JsString.get("%s.getDataAsExcel(%s)" % (
                self.api, JsUtils.jsConvertData(params, None)))

        return JsObjects.JsString.JsString.get("%s.getDataAsExcel()" % self.api)

    def getDisplayedRowAtIndex(self, index):
        """Returns the displayed rowNode at the given index.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_

        :param index:
        """
        index = JsUtils.jsConvertData(index, None)
        return JsObjects.JsVoid("%s.getRowNode(%s)" % (self.api, index))

    def getDisplayedRowCount(self):
        """Returns the total number of displayed rows.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.getDisplayedRowCount()" % self.api)

    def getFilteredRowData(self):
        return JsObjects.JsArray.JsArray.get(
            "(function(){let rowData = [];%s.forEachNodeAfterFilter(node => {rowData.push(node.data);}); return rowData})()" % self.api)

    def getFirstDisplayedRow(self):
        """Get the index of the first displayed row due to scrolling (includes invisible rendered rows in the buffer).
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.getFirstDisplayedRow()" % self.api)

    def getLastDisplayedRow(self):
        """Get the index of the last displayed row due to scrolling (includes invisible rendered rows in the buffer).
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.getLastDisplayedRow()" % self.api)

    def getQuickFilter(self):
        """Get the current Quick Filter text from the grid, or undefined if none is set.
        `Related Pages <https://ag-grid.com/javascript-data-grid/filter-quick//>`_
        """
        return JsObjects.JsVoid("%s.getQuickFilter()" % self.api)

    def getRowNode(self, row_id):
        """Returns the row node with the given ID. The row node ID is the one you provide with the callback
        getRowNodeId(data), otherwise the ID is a number auto generated by the grid when the row data is set.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_

        :param row_id:
        """
        row_id = JsUtils.jsConvertData(row_id, None)
        return JsObjects.JsVoid("%s.getRowNode(%s)" % (self.api, row_id))

    def hideColumn(self, column):
        """
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-definitions/>`_

        :param column:
        """
        return JsObjects.JsVoid("%(varId)s.columnApi.setColumnVisible(%(cols)s, false)" % {
            'varId': self.varId, 'cols': JsUtils.jsConvertData(column, None)})

    def hideColumns(self, columns):
        """

        :param columns:
        """
        return JsObjects.JsVoid("%(varId)s.columnApi.setColumnsVisible(%(cols)s, false)" % {
            'varId': self.varId, 'cols': JsUtils.jsConvertData(columns, None)})

    def isQuickFilterPresent(self):
        """Returns true if the Quick Filter is set, otherwise false.
        `Aggrid <https://ag-grid.com/javascript-data-grid/filter-quick//>`_
        """
        return JsObjects.JsVoid("%s.isQuickFilterPresent()" % self.api)

    def purgeServerSideCache(self, route):
        """

        `Related Pages <http://54.222.217.254/javascript-grid-server-side-model-tree-data/>`_

        :param route:
        """
        return JsObjects.JsVoid("%s.purgeServerSideCache(%s)" % (self.api, JsUtils.jsConvertData(route, None)))

    def setAutoHeight(self):
        """Gets columns to adjust automatically height.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.setDomLayout('autoHeight')" % self.api)

    def setColumnDefs(self, col_defs: Any):
        """Call to set new column definitions. The grid will redraw all the column headers, and then redraw all of the
        rows. `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_

        :param col_defs: The new table definition. If None update the existing ones.
        """
        if min(self.page.imports.pkgs.ag_grid.version) > '31.0.0':
            if col_defs is None:
                return JsObjects.JsVoid("%s.setGridOption('columnDefs', %s)" % (
                    self.api, JsUtils.jsConvertData(self.getColumnDefs(), None)))

            return JsObjects.JsVoid(
                "%s.setGridOption('columnDefs', %s)" % (self.api, JsUtils.jsConvertData(col_defs, None)))

        else:
            if col_defs is None:
                return JsObjects.JsVoid("%s.setColumnDefs(%s)" % (
                    self.api, JsUtils.jsConvertData(self.getColumnDefs(), None)))

            return JsObjects.JsVoid("%s.setColumnDefs(%s)" % (self.api, JsUtils.jsConvertData(col_defs, None)))

    def setDomLayout(self, data: types.JS_DATA_TYPES):
        """Gets columns to adjust in size to fit the grid horizontally
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_

        :param data: The layout properties
        """
        data = JsUtils.jsConvertData(data, None)
        return JsObjects.JsVoid("%s.setDomLayout(%s)" % (self.api, data))

    def setGridOption(self, name: types.JS_DATA_TYPES, value: types.JS_DATA_TYPES):
        name = JsUtils.jsConvertData(name, None)
        value = JsUtils.jsConvertData(value, None)
        return JsUtils.jsWrap("%s.setGridOption(%s, %s)" % (self.api, name, value))

    def setRowData(self, rows: types.JS_DATA_TYPES, dataflows: List[dict] = None):
        """Set rows.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_

        :param rows:
        :param dataflows: Chain of data transformations
        """
        if min(self.page.imports.pkgs.ag_grid.version) > '31.0.0':
            if self.component.options.rowTotal:
                return JsObjects.JsVoid("%s.setGridOption('rowData', %s); %s" % (
                    self.api, JsUtils.dataFlows(rows, dataflows, self.page),
                    self.setTotalRow(rows, self.component.options.rowTotal).toStr()))

            return JsObjects.JsVoid("%s.setGridOption('rowData', %s)" % (
                self.api, JsUtils.dataFlows(rows, dataflows, self.page)))

        else:
            if self.component.options.rowTotal:
                return JsObjects.JsVoid("%s.setRowData(%s); %s" % (
                    self.api, JsUtils.dataFlows(rows, dataflows, self.page),
                    self.setTotalRow(rows, self.component.options.rowTotal).toStr()))

            return JsObjects.JsVoid("%s.setRowData(%s)" % (
                self.api, JsUtils.dataFlows(rows, dataflows, self.page)))

    def showColumn(self, column):
        """
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-definitions/>`_

        :param column:
        """
        return JsObjects.JsVoid("%(varId)s.columnApi.setColumnVisible(%(cols)s, true)" % {
            'varId': self.varId, 'cols': JsUtils.jsConvertData(column, None)})

    def showColumns(self, columns):
        """

        :param columns:
        """
        return JsObjects.JsVoid("%(varId)s.columnApi.setColumnsVisible(%(cols)s, true)" % {
            'varId': self.varId, 'cols': JsUtils.jsConvertData(columns, None)})

    def sizeColumnsToFit(self):
        """Gets columns to adjust in size to fit the grid horizontally
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.sizeColumnsToFit()" % self.api)

    def stopEditing(self, cancel: bool = None):
        """The callback stopEditing (from the params above) gets called by the editor.
        This is how your cell editor informs the grid to stop editing.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/cell-editing-start-stop/>`_

        :param cancel: Optional. If a cell is editing, it stops the editing. Pass true if you want to cancel the editing
        """
        if cancel is None:
            return JsObjects.JsVoid("%s.stopEditing()" % self.api)

        cancel = JsUtils.jsConvertData(cancel, None)
        return JsObjects.JsVoid("%s.stopEditing(%s)" % (self.api, cancel))

    def selectAll(self):
        """Select all rows (even rows that are not visible due to grouping being enabled and their groups not expanded).
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.selectAll()" % self.api)

    def deselectAll(self):
        """Clear all row selections.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.deselectAll()" % self.api)

    def selectAllFiltered(self):
        """Select all filtered rows.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.selectAllFiltered()" % self.api)

    def deselectAllFiltered(self):
        """Clear all filtered selections.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.deselectAllFiltered()" % self.api)

    def getSelectedNodes(self):
        """Returns a list of selected nodes. Getting the underlying node (rather than the data) is useful when
        working with tree / aggregated data, as the node can be traversed.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.getSelectedNodes()" % self.api)

    def getFocusedCell(self):
        """Returns the focused cell (or the last focused cell if the grid lost focus).
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-api/
        """
        return JsObjects.JsVoid("%s.getFocusedCell()" % self.api)

    def getFilterModel(self):
        """It is possible to get the state of all filters using the grid API method getFilterModel(), and to set the state
        using setFilterModel().
        These methods manage the filters states via the getModel() and setModel() methods of the individual filters.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/filter-api/#get--set-all-filter-models>`_
        """
        return JsObjects.JsObject.JsObject("%s.getFilterModel()" % self.api)

    def getAdvancedFilterModel(self):
        """Get the state of the Advanced Filter. Used for saving Advanced Filter state.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/filter-advanced/>`_
        """
        return JsObjects.JsObject.JsObject("%s.getAdvancedFilterModel()" % self.api)

    def setColumnFilterModel(self, column, data: types.JS_DATA_TYPES, dataflows: List[dict] = None):
        """Sets the filter model for the specified column. Setting a model of null will reset the filter (make inactive).
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/filter-api/>`_

        :param column:
        :param data:
        :param dataflows: Chain of config transformations
        """
        column = JsUtils.jsConvertData(column, None)
        if dataflows:
            return JsObjects.JsObject.JsObject("%s.setColumnFilterModel(%s, %s)" % (
                self.api, column, JsUtils.dataFlows(data, dataflows, self.page)))

        data = JsUtils.jsConvertData(data, None)
        return JsObjects.JsObject.JsObject("%s.setColumnFilterModel(%s, %s)" % (self.api, column, data))

    def setFocusedCell(self, rowIndex: types.JS_DATA_TYPES, colKey: types.JS_DATA_TYPES,
                       RowPinnedType: types.JS_DATA_TYPES = None):
        """Sets the focus to the specified cell. rowPinned can be either 'top', 'bottom' or null (for not pinned).

        :param rowIndex: Row index value
        :param colKey: Column alias
        :param RowPinnedType:
        """
        rowIndex = JsUtils.jsConvertData(rowIndex, None)
        colKey = JsUtils.jsConvertData(colKey, None)
        RowPinnedType = JsUtils.jsConvertData(RowPinnedType, None)
        return JsObjects.JsObject.JsObject("%s.setFocusedCell(%s, %s, %s)" % (self.api, rowIndex, colKey, RowPinnedType))

    def setFocusedHeader(self, colKey: types.JS_DATA_TYPES, floatingFilter: types.JS_DATA_TYPES = False):
        """Sets the focus to the specified header. If floatingFilter is true, the Column's floatingFilter element will
        be focused.

        :param colKey: Column alias
        :param floatingFilter:
        """
        colKey = JsUtils.jsConvertData(colKey, None)
        floatingFilter = JsUtils.jsConvertData(floatingFilter, None)
        return JsObjects.JsObject.JsObject("%s.setFocusedHeader(%s, %s)" % (self.api, colKey, floatingFilter))

    def startEditingCell(self, rowIndex: types.JS_DATA_TYPES, colKey: types.JS_DATA_TYPES,
                       RowPinnedType: types.JS_DATA_TYPES = None):
        """Start editing the provided cell. If another cell is editing, the editing will be stopped in that other cell.

        :param rowIndex: Row index value
        :param colKey: Column alias
        :param RowPinnedType:
        """
        rowIndex = JsUtils.jsConvertData(rowIndex, None)
        colKey = JsUtils.jsConvertData(colKey, None)
        RowPinnedType = JsUtils.jsConvertData(RowPinnedType, None)
        return JsObjects.JsObject.JsObject(
            "%s.startEditingCell({rowIndex: %s, colKey: %s, RowPinnedType: %s})" % (
                self.api, rowIndex, colKey, RowPinnedType))

    def getColumnFilterModel(self, column, dataflows: List[dict] = None):
        """Gets the current filter model for the specified column. Will return null if no active filter.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/filter-api/>`_

        :param column:
        :param dataflows: Chain of config transformations
        """
        if dataflows:
            return JsObjects.JsObject.JsObject("%s.getColumnFilterModel(%s)" % (
                self.api, JsUtils.dataFlows(column, dataflows, self.page)))

        column = JsUtils.jsConvertData(column, None)
        return JsObjects.JsObject.JsObject("%s.getColumnFilterModel(%s)" % (self.api, column))

    def setFilterModel(self, data: types.JS_DATA_TYPES, dataflows: List[dict] = None):
        """Sets the state of all the advanced filters.
        Provide it with what you get from getFilterModel() to restore filter state.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/filter-api/#get--set-all-filter-models>`_

        :param data:
        :param dataflows: Chain of config transformations
        """
        if dataflows:
            return JsObjects.JsObject.JsObject("%s.setFilterModel(%s)" % (
                self.api, JsUtils.dataFlows(data, dataflows, self.page)))

        data = JsUtils.jsConvertData(data, None)
        return JsObjects.JsObject.JsObject("%s.setFilterModel(%s)" % (self.api, data))

    def setAdvancedFilterModel(self, data: types.JS_DATA_TYPES, dataflows: List[dict] = None):
        """Set the state of the Advanced Filter. Used for restoring Advanced Filter state
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/filter-advanced/>`_

        :param data:
        :param dataflows: Chain of config transformations
        """
        if dataflows:
            return JsObjects.JsObject.JsObject("%s.setAdvancedFilterModel(%s)" % (
                self.api, JsUtils.dataFlows(data, dataflows, self.page)))

        data = JsUtils.jsConvertData(data, None)
        return JsObjects.JsObject.JsObject("%s.setAdvancedFilterModel(%s)" % (self.api, data))

    def destroyFilter(self):
        """Sets the state of all the advanced filters.
        Provide it with what you get from getFilterModel() to restore filter state.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/filter-api/#get--set-all-filter-models>`_
        """
        return JsObjects.JsObject.JsObject("%s.destroyFilter()" % self.api)

    def getFilterInstance(self, data: types.JS_DATA_TYPES):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/filter-api/#get--set-all-filter-models>`_

        :param data:
        """
        raise NotImplementedError("Not yet available")

    def getModel(self):
        """Get table model.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/filter-api/#get--set-all-filter-models>`_
        """
        return JsObjects.JsObject.JsObject("%s.getModel()" % self.api)

    def getRowsData(self) -> JsObjects.JsArray.JsArray:
        """Get all the data in the table.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/accessing-data/>`_
        """
        return JsObjects.JsArray.JsArray.get('''
(function(table) {let rowData = []; table.forEachNode(node => rowData.push(node.data)); return rowData})(%s)''' % self.api)

    def getSelectedRows(self) -> JsObjects.JsArray.JsArray:
        """Returns a list of selected rows (i.e. row data that you provided).
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsArray.JsArray.get("%s.getSelectedRows()" % self.api)

    def getCellRanges(self):
        """Returns the list of selected cell ranges.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.getCellRanges()" % self.api)

    def clearRangeSelection(self):
        """Clears the selected range.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.clearRangeSelection()" % self.api)

    def refreshCells(self, params):
        """Performs change detection on all cells, refreshing cells where required.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        params = JsUtils.jsConvertData(params, None)
        return JsObjects.JsVoid("%s.refreshCells(%s)" % (self.api, params))

    def redrawRows(self, params):
        """Remove a row from the DOM and recreate it again from scratch.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        params = JsUtils.jsConvertData(params, None)
        return JsObjects.JsVoid("%s.redrawRows(%s)" % (self.api, params))

    def refreshHeader(self):
        """Redraws the header. Useful if a column name changes, or something else that changes how the column header is
        displayed.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.refreshHeader()" % self.api)

    def flashCells(self, params):
        """Flash rows, columns or individual cells. See Flashing Cells.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        `Related Pages <https://www.ag-grid.com/angular-data-grid/flashing-cells/>`_
        """
        params = JsUtils.jsConvertData(params, None)
        return JsObjects.JsVoid("%s.flashCells(%s)" % (self.api, params))

    def clearFocusedCell(self):
        """Clears the focused cell.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.clearFocusedCell()" % self.api)

    def tabToNextCell(self):
        """Navigates the grid focus to the next cell, as if tabbing.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.tabToNextCell()" % self.api)

    def tabToPreviousCell(self):
        """Navigates the grid focus to the previous cell, as if shift-tabbing.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.tabToPreviousCell()" % self.api)

    def overlayLoadingTemplate(self, js_data: types.JS_DATA_TYPES) -> JsObjects.JsVoid:
        """Set the template for loading overlay.

        :param js_data: String or HTML string
        """
        js_data = JsUtils.jsConvertData(js_data, None)
        return JsObjects.JsVoid("%s.overlayLoadingTemplate = %s" % (self.varId, js_data))

    def overlayNoRowsTemplate(self, js_data: types.JS_DATA_TYPES) -> JsObjects.JsVoid:
        """Set the template for No Rows overlay

        :param js_data: String or HTML string
        """
        js_data = JsUtils.jsConvertData(js_data, None)
        return JsObjects.JsVoid("%s.overlayNoRowsTemplate = %s" % (self.varId, js_data))

    def showLoadingOverlay(self) -> JsObjects.JsVoid:
        """Show the 'loading' overlay.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.showLoadingOverlay()" % self.api)

    def showNoRowsOverlay(self):
        """Show the 'no rows' overlay.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.showNoRowsOverlay()" % self.api)

    def hideOverlay(self) -> JsObjects.JsVoid:
        """Hides the overlay if showing.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.hideOverlay()" % self.api)

    def destroy(self) -> JsObjects.JsVoid:
        """Will destroy the grid and release resources.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.destroy()" % self.api)

    def resetRowHeights(self) -> JsObjects.JsVoid:
        """Tells the grid to recalculate the row heights.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.resetRowHeights()" % self.api)

    def paginationIsLastPageFound(self) -> JsObjects.JsVoid:
        """Returns true when the last page is known; this will always be the case if you are using the Client-Side
        Row Model for pagination.
        Returns false when the last page is not known; this only happens when using Infinite Scrolling Row Model.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.paginationIsLastPageFound()" % self.api)

    def copySelectedRangeToClipboard(self, include_headers) -> JsObjects.JsVoid:
        """Copies the selected ranges to the clipboard.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        include_headers = JsUtils.jsConvertData(include_headers, None)
        return JsObjects.JsVoid("%s.copySelectedRangeToClipboard(%s)" % (self.api, include_headers))

    def copySelectedRangeDown(self) -> JsObjects.JsVoid:
        """Copies the selected range down, similar to Ctrl + D in Excel.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.copySelectedRangeDown()" % self.api)

    def paginationGetPageSize(self) -> JsObjects.JsVoid:
        """Returns how many rows are being shown per page.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.paginationGetPageSize()" % self.api)

    def paginationSetPageSize(self, new_page_size) -> JsObjects.JsVoid:
        """Sets the paginationPageSize to newPageSize, then re-paginates the grid so the changes are applied immediately.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        new_page_size = JsUtils.jsConvertData(new_page_size, None)
        return JsObjects.JsVoid("%s.paginationSetPageSize(%s)" % (self.api, new_page_size))

    def paginationGetCurrentPage(self) -> JsObjects.JsVoid:
        """Returns the 0-based index of the page which is showing.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.paginationGetCurrentPage()" % self.api)

    def paginationGetTotalPages(self) -> JsObjects.JsVoid:
        """Returns the total number of pages. Returns null if paginationIsLastPageFound() == false.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.paginationGetTotalPages()" % self.api)

    def paginationGetRowCount(self) -> JsObjects.JsVoid:
        """The total number of rows. Returns null if paginationIsLastPageFound() == false.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.paginationGetRowCount()" % self.api)

    def paginationGoToPage(self, page_number: types.JS_DATA_TYPES) -> JsObjects.JsVoid:
        """Goes to the specified page. If the page requested doesn't exist, it will go to the last page.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_

        :param page_number: Page index
        """
        page_number = JsUtils.jsConvertData(page_number, None)
        return JsObjects.JsVoid("%s.paginationGoToPage(%s)" % (self.api, page_number))

    def paginationGoToNextPage(self) -> JsObjects.JsVoid:
        """Shorthands for goToPage(relevantPageNumber).
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.paginationGoToNextPage()" % self.api)

    def paginationGoToPreviousPage(self) -> JsObjects.JsVoid:
        """Shorthands for goToPage(relevantPageNumber).
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.paginationGoToPreviousPage()" % self.api)

    def paginationGoToFirstPage(self) -> JsObjects.JsVoid:
        """Shorthands for goToPage(relevantPageNumber).
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.paginationGoToFirstPage()" % self.api)

    def paginationGoToLastPage(self) -> JsObjects.JsVoid:
        """Shorthands for goToPage(relevantPageNumber).
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        return JsObjects.JsVoid("%s.paginationGoToLastPage()" % self.api)

    def setSideBarVisible(self, show) -> JsObjects.JsVoid:
        """Tells the grid to recalculate the row heights.
        `Related Pages <https://www.ag-grid.com/javascript-grid-api/>`_
        """
        show = JsUtils.jsConvertData(show, None)
        return JsObjects.JsVoid("%s.setSideBarVisible(%s)" % (self.api, show))

    def getSortModel(self) -> JsObjects.JsVoid:
        """Returns the sort state.
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-api/>`_
        """
        return JsObjects.JsVoid("%s.getSortModel()" % self.api)

    def setPinnedBottomRowData(self, rowData) -> JsObjects.JsVoid:
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-pinning/>`_

        :param rowData:
        """
        return JsObjects.JsVoid(
            "%s.setPinnedBottomRowData(%s)" % (self.api, JsUtils.jsConvertData(rowData, None)))

    def setPinnedTopRowData(self, rowData) -> JsObjects.JsVoid:
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-pinning/>`_

        :param rowData:
        """
        return JsObjects.JsVoid("%s.setPinnedTopRowData(%s)" % (self.api, JsUtils.jsConvertData(rowData, None)))

    def setTotalRow(self, rowData, cols: types.JS_DATA_TYPES = None) -> JsObjects.JsVoid:
        """

        :param rowData:
        :param cols:
        :return:
        """
        return JsObjects.JsVoid('''
const calcTotalCols = %s; const totalRow = function(api) {
      let result = [{}]; calcTotalCols.forEach(function (params){result[0][params] = 0});
      calcTotalCols.forEach(function (params){%s.forEach(function (line) {result[0][params] += line[params];})});
      api.setPinnedBottomRowData(result);
  }; totalRow(%s)''' % (JsUtils.jsConvertData(cols, None), JsUtils.jsConvertData(rowData, None), self.api))

    def setServerSideDatasource(self, data) -> JsObjects.JsVoid:
        """Set new datasource for Server-Side Row Model.
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-api/#reference-serverSideRowModel>`_

        :param data:
        """
        return JsObjects.JsVoid("%s.setServerSideDatasource(%s)" % (self.api, JsUtils.jsConvertData(data, None)))

    @property
    def fields(self) -> JsObjects.JsArray.JsArray:
        """Get the table's header fields"""
        return JsObjects.JsArray.JsArray.get(
            "(function(colsDef){let res = []; colsDef.forEach(function(r){res.push(r.field)}); return res})(%s)" % self.getColumnDefs())

    @property
    def titles(self) -> JsObjects.JsArray.JsArray:
        """Get the table's header titles"""
        return JsObjects.JsArray.JsArray.get(
            "(function(colsDef){let res = []; colsDef.forEach(function(r){res.push(r.title)}); return res})(%s)" % self.getColumnDefs())

    def fetch(self, url: Union[str, primitives.JsDataModel], data: Optional[dict] = None, js_code: str = "response",
              is_json: bool = True,
              components: Optional[List[Union[Tuple[primitives.HtmlModel, str], primitives.HtmlModel]]] = None,
              profile: Optional[Union[dict, bool]] = None, headers: Optional[dict] = None,
              asynchronous: bool = False, stringify: bool = True, method: str = "GET") -> JsObjects.XMLHttpRequest:
        rest_call = self.page.js.rest(
            method, url, data, js_code, is_json=is_json, components=components, profile=profile, headers=headers,
            asynchronous=asynchronous, stringify=stringify)
        rest_call.onSuccess(['''
var fakeServer = {
    getData: (request) => {
      const requestedRows = %s.response.slice(request.startRow, request.endRow);
      return {success: true, rows: requestedRows};},
};
%s.api.setServerSideDatasource({
  getRows: (params) => {
    const response = fakeServer.getData(params.request);
    setTimeout(function () {
      if (response.success) {params.success({ rowData: response.rows })} else {params.fail();}
    }, 500);
  }});''' % (js_code, self.varId)])
        return rest_call

    def onFilterChanged(self):
        return JsObjects.JsVoid("%s.onFilterChanged()" % self.api)

    @property
    def _(self):
        """Aggrid standard components (mainly for events).

        Usage::
          table.js._
        """
        return _Export()
