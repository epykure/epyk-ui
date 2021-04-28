#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.js.packages import JsPackage
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class ColumnApi:

  def __init__(self, report, varId):
    self.varId = varId
    self._report = report

  def sizeColumnsToFit(self, width):
    """
    Description:
    -----------
    Gets the grid to size the columns to the specified width in pixels, e.g. sizeColumnsToFix(900).
    To have the grid fit the columns to the grid's width, use the Grid API gridApi.sizeColumnsToFit() instead.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    Attributes:
    ----------
    :param width:
    """
    return JsObjects.JsVoid("%s.sizeColumnsToFit(%s)" % (self.varId, JsUtils.jsConvertData(width, None)))

  def getColumnGroup(self, name):
    """
    Description:
    -----------
    Returns the column group with the given name.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    Attributes:
    ----------
    :param name:
    """
    return JsObjects.JsVoid("%s.getColumnGroup(%s)" % (self.varId, JsUtils.jsConvertData(name, None)))

  def getColumn(self, name):
    """
    Description:
    -----------
    Returns the column with the given colKey, which can either be the colId (a string) or the colDef (an object).

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    Attributes:
    ----------
    :param name:
    """
    return JsObjects.JsVoid("%s.getColumn(%s)" % (self.varId, JsUtils.jsConvertData(name, None)))

  def getColumnState(self):
    """
    Description:
    -----------
    Gets the state of the columns. Typically used when saving column state.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.getColumnState()" % self.varId)

  def setColumnState(self, columnState):
    """
    Description:
    -----------
    Sets the state of the columns from a previous state. Returns false if one or more columns could not be found.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.setColumnState(%s)" % (self.varId, JsUtils.jsConvertData(columnState, None)))

  def resetColumnState(self):
    """
    Description:
    -----------
    Sets the state back to match the originally provided column definitions.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.resetColumnState()" % self.varId)

  def isPinning(self):
    """
    Description:
    -----------
    Returns true if pinning left or right, otherwise false.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.isPinning()" % self.varId)

  def isPinningLeft(self):
    """
    Description:
    -----------
    Returns true if pinning left, otherwise false.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.isPinningLeft()" % self.varId)

  def isPinningRight(self):
    """
    Description:
    -----------
    Returns true if pinning right, otherwise false.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.isPinningRight()" % self.varId)

  def setColumnVisible(self, colKey, visible):
    """
    Description:
    -----------
    Sets the visibility of a column. Key can be the column ID or Column object.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    colKey = JsUtils.jsConvertData(colKey, None)
    visible = JsUtils.jsConvertData(visible, None)
    return JsObjects.JsVoid("%s.setColumnVisible(%s. %s)" % (self.varId, colKey, visible))

  def setColumnsVisible(self, colKeys, visible):
    """
    Description:
    -----------
    Same as setColumnVisible, but provide a list of column keys.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    colKeys = JsUtils.jsConvertData(colKeys, None)
    visible = JsUtils.jsConvertData(visible, None)
    return JsObjects.JsVoid("%s.setColumnsVisible(%s. %s)" % (self.varId, colKeys, visible))

  def setColumnPinned(self, colKey, pinned):
    """
    Description:
    -----------
    Sets the column pinned / unpinned. Key can be the column ID, field, ColDef object or Column object.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    colKey = JsUtils.jsConvertData(colKey, None)
    pinned = JsUtils.jsConvertData(pinned, None)
    return JsObjects.JsVoid("%s.setColumnPinned(%s. %s)" % (self.varId, colKey, pinned))

  def setColumnsPinned(self, colKeys, pinned):
    """
    Description:
    -----------
    Sets the column pinned / unpinned. Key can be the column ID, field, ColDef object or Column object.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    colKeys = JsUtils.jsConvertData(colKeys, None)
    pinned = JsUtils.jsConvertData(pinned, None)
    return JsObjects.JsVoid("%s.setColumnsPinned(%s. %s)" % (self.varId, colKeys, pinned))

  def getColumnGroupState(self):
    """
    Description:
    -----------
    Gets the state of the column groups. Typically used when saving column group state.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.getColumnGroupState()" % self.varId)

  def autoSizeColumn(self, colKey):
    """
    Description:
    -----------
    Auto-sizes a column based on its contents.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.autoSizeColumn(%s)" % (self.varId, JsUtils.jsConvertData(colKey, None)))

  def autoSizeColumns(self, colKeys):
    """
    Description:
    -----------
    Same as autoSizeColumn, but provide a list of column keys.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.autoSizeColumns(%s)" % (self.varId, JsUtils.jsConvertData(colKeys, None)))

  def getDisplayNameForColumn(self, name):
    """
    Description:
    -----------
    Returns the display name for a column.
    Useful if you are doing your own header rendering and want the grid to work out if headerValueGetter is used, or
    if you are doing your own column management GUI, to know what to show as the column name.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    Attributes:
    ----------
    :param name:
    """
    return JsObjects.JsVoid("%s.getDisplayNameForColumn(%s)" % (self.varId, JsUtils.jsConvertData(name, None)))

  def getAllColumns(self):
    """
    Description:
    -----------
    Returns all the columns, regardless of visible or not.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.getAllColumns()" % self.varId)

  def getAllGridColumns(self):
    """
    Description:
    -----------
    Returns all the grid columns, same as getAllColumns(), except a) it has the order of the columns that are presented
    in the grid and b) it's after the 'pivot' step, so if pivoting, has the value columns for the pivot.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.getAllGridColumns()" % self.varId)

  def getPrimaryColumns(self):
    """
    Description:
    -----------
    Returns the grid's primary columns.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.getPrimaryColumns()" % self.varId)

  def getSecondaryColumns(self):
    """
    Description:
    -----------
    Returns the grid's secondary columns.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.getSecondaryColumns()" % self.varId)

  def getAllDisplayedVirtualColumns(self):
    """
    Description:
    -----------
    Same as getAllGridColumns(), except only returns rendered columns, i.e. columns that are not within the viewport
    and therefore not rendered, due to column virtualisation, are not displayed.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.getAllDisplayedVirtualColumns()" % self.varId)

  def moveColumn(self, colKey, toIndex):
    """
    Description:
    -----------
    Moves a column to toIndex. The column is first removed, then added at the toIndex location, thus index locations
    will change to the right of the column after the removal.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    Attributes:
    ----------
    :param colKey:
    :param toIndex:
    """
    colKey = JsUtils.jsConvertData(colKey, None)
    toIndex = JsUtils.jsConvertData(toIndex, None)
    return JsObjects.JsVoid("%s.moveColumn(%s, %s)" % (self.varId, colKey, toIndex))

  def moveColumns(self, colKeys, toIndex):
    """
    Description:
    -----------
    Moves a column to toIndex. The column is first removed, then added at the toIndex location, thus index locations
    will change to the right of the column after the removal.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    Attributes:
    ----------
    :param colKeys:
    :param toIndex:
    """
    colKeys = JsUtils.jsConvertData(colKeys, None)
    toIndex = JsUtils.jsConvertData(toIndex, None)
    return JsObjects.JsVoid("%s.moveColumns(%s, %s)" % (self.varId, colKeys, toIndex))

  def setColumnAggFunc(self, column, aggFunc):
    """
    Description:
    -----------
    Sets the agg function for a column. aggFunc can be one of 'min' | 'max' | 'sum'.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    Attributes:
    ----------
    :param column:
    :param aggFunc:
    """
    column = JsUtils.jsConvertData(column, None)
    aggFunc = JsUtils.jsConvertData(aggFunc, None)
    return JsObjects.JsVoid("%s.setColumnAggFunc(%s, %s)" % (self.varId, column, aggFunc))

  def setColumnWidth(self, colKey, newWidth, finished=True):
    """
    Description:
    -----------
    Sets the column width on a single column. The finished flag gets included in the resulting event and not used
    internally by the grid.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    Attributes:
    ----------
    :param colKey:
    :param newWidth:
    :param finished:
    """
    colKey = JsUtils.jsConvertData(colKey, None)
    newWidth = JsUtils.jsConvertData(newWidth, None)
    finished = JsUtils.jsConvertData(finished, None)
    return JsObjects.JsVoid("%s.setColumnWidth(%s, %s, %s)" % (self.varId, colKey, newWidth, finished))

  def setColumnWidths(self, columnWidths, finished=True):
    """
    Description:
    -----------
    Sets the column width on a single column. The finished flag gets included in the resulting event and not used
    internally by the grid.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    Attributes:
    ----------
    :param columnWidths:
    :param finished:
    """
    columnWidths = JsUtils.jsConvertData(columnWidths, None)
    finished = JsUtils.jsConvertData(finished, None)
    return JsObjects.JsVoid("%s.setColumnWidth(%s, %s)" % (self.varId, columnWidths, finished))

  def custom(self, func_nam, *argv):
    """
    Description:
    ------------
    Generic function to call any missing function form a package.
    This will automatically convert the object to JavaScript and also put the right object reference.

    Attributes:
    ----------
    :param func_nam: String. The function name
    :param argv: Objects. Optional. The function arguments on the JavasScript side
    """
    js_args = []
    for arg in argv:
      js_args.append(str(JsUtils.jsConvertData(arg, None)))
    return JsObjects.JsObject.JsObject.get("%s.%s(%s)" % (self.varId, func_nam, ", ".join(js_args)))


class AgGrid(JsPackage):
  lib_alias = {"js": "ag-grid-community", "css": "ag-grid-community"}

  def sizeColumnsToFit(self):
    """
    Description:
    -----------
    Gets columns to adjust in size to fit the grid horizontally

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/
    """
    return JsObjects.JsVoid("%s.api.sizeColumnsToFit()" % self.varId)

  @property
  def columnApi(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return ColumnApi(self.src, "%s.columnApi" % self.varId)

  def setColumnDefs(self, colDefs):
    """
    Description:
    -----------
    Call to set new column definitions. The grid will redraw all the column headers, and then redraw all of the rows.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/

    Attributes:
    ----------
    :param colDefs:
    """
    return JsObjects.JsVoid("%s.api.setColumnDefs(%s)" % (self.varId, JsUtils.jsConvertData(colDefs, None)))

  def getColumnDefs(self):
    """
    Description:
    -----------
    Call to set new column definitions. The grid will redraw all the column headers, and then redraw all of the rows.

    Related Pages:

      https://www.ag-grid.com/documentation/javascript/column-updating-definitions/
    """
    return JsObjects.JsVoid("%s.api.getColumnDefs()" % self.varId)

  def setRowData(self, rows):
    """
    Description:
    -----------
    Set rows.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/

		Attributes:
    ----------
    :param rows:
    """
    return JsObjects.JsVoid("%s.api.setRowData(%s)" % (self.varId, JsUtils.jsConvertData(rows, None)))

  def applyTransaction(self, transaction):
    """
    Description:
    -----------
    Update row data. Pass a transaction object with lists for add, remove and update.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/

    Attributes:
    ----------
    :param transaction:
    """
    return JsObjects.JsVoid("%s.api.applyTransaction(%s)" % (self.varId, JsUtils.jsConvertData(transaction, None)))

  def applyTransactionAsync(self, transaction, callback):
    """
    Description:
    -----------
    Same as applyTransaction except executes asynchronous for efficiency.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/

    Attributes:
    ----------
    :param transaction:
    :param callback:
    """
    return JsObjects.JsVoid("%s.api.applyTransaction(%s, %s)" % (
      self.varId, JsUtils.jsConvertData(transaction, None), callback))

  def getDisplayedRowCount(self):
    """
    Description:
    -----------
    Returns the total number of displayed rows.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.getDisplayedRowCount()" % self.varId)

  def getFirstDisplayedRow(self):
    """
    Description:
    -----------
    Get the index of the first displayed row due to scrolling (includes invisible rendered rows in the buffer).

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.getFirstDisplayedRow()" % self.varId)

  def getLastDisplayedRow(self):
    """
    Description:
    -----------
    Get the index of the last displayed row due to scrolling (includes invisible rendered rows in the buffer).

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.getLastDisplayedRow()" % self.varId)

  def hideColumns(self, columns):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param columns:
    """
    return JsObjects.JsVoid("%(varId)s.columnApi.setColumnsVisible(%(cols)s, false)" % {
      'varId': self.varId, 'cols': JsUtils.jsConvertData(columns, None)})

  def showColumns(self, columns):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param columns:
    """
    return JsObjects.JsVoid("%(varId)s.columnApi.setColumnsVisible(%(cols)s, true)" % {
      'varId': self.varId, 'cols': JsUtils.jsConvertData(columns, None)})

  def hideColumn(self, column):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/

    Attributes:
    ----------
    :param columns:
    """
    return JsObjects.JsVoid("%(varId)s.columnApi.setColumnVisible(%(cols)s, false)" % {
      'varId': self.varId, 'cols': JsUtils.jsConvertData(column, None)})

  def showColumn(self, column):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/

    Attributes:
    ----------
    :param column:
    """
    return JsObjects.JsVoid("%(varId)s.columnApi.setColumnVisible(%(cols)s, true)" % {
      'varId': self.varId, 'cols': JsUtils.jsConvertData(column, None)})

  def getRowNode(self, row_id):
    """
    Description:
    -----------
    Returns the row node with the given ID. The row node ID is the one you provide with the callback getRowNodeId(data),
    otherwise the ID is a number auto generated by the grid when the row data is set.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/

    Attributes:
    ----------
    :param row_id:
    """
    row_id = JsUtils.jsConvertData(row_id, None)
    return JsObjects.JsVoid("%s.api.getRowNode(%s)" % (self.varId, row_id))

  def getDisplayedRowAtIndex(self, index):
    """
    Description:
    -----------
    Returns the displayed rowNode at the given index.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/

    Attributes:
    ----------
    :param index:
    """
    index = JsUtils.jsConvertData(index, None)
    return JsObjects.JsVoid("%s.api.getRowNode(%s)" % (self.varId, index))

  def selectAll(self):
    """
    Description:
    -----------
    Select all rows (even rows that are not visible due to grouping being enabled and their groups not expanded).

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.selectAll()" % self.varId)

  def deselectAll(self):
    """
    Description:
    -----------
    Clear all row selections.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.deselectAll()" % self.varId)

  def selectAllFiltered(self):
    """
    Description:
    -----------
    Select all filtered rows.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.selectAllFiltered()" % self.varId)

  def deselectAllFiltered(self):
    """
    Description:
    -----------
    Clear all filtered selections.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.deselectAllFiltered()" % self.varId)

  def getSelectedNodes(self):
    """
    Description:
    -----------
    Returns a list of selected nodes. Getting the underlying node (rather than the data) is useful when working with
    tree / aggregated data, as the node can be traversed.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.getSelectedNodes()" % self.varId)

  def getSelectedRows(self):
    """
    Description:
    -----------
    Returns a list of selected rows (i.e. row data that you provided).

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.getSelectedRows()" % self.varId)

  def getCellRanges(self):
    """
    Description:
    -----------
    Returns the list of selected cell ranges.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.getCellRanges()" % self.varId)

  def clearRangeSelection(self):
    """
    Description:
    -----------
    Clears the selected range.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.clearRangeSelection()" % self.varId)

  def refreshCells(self, params):
    """
    Description:
    -----------
    Performs change detection on all cells, refreshing cells where required.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    params = JsUtils.jsConvertData(params, None)
    return JsObjects.JsVoid("%s.api.refreshCells(%s)" % (self.varId, params))

  def redrawRows(self, params):
    """
    Description:
    -----------
    Remove a row from the DOM and recreate it again from scratch.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    params = JsUtils.jsConvertData(params, None)
    return JsObjects.JsVoid("%s.api.redrawRows(%s)" % (self.varId, params))

  def refreshHeader(self):
    """
    Description:
    -----------
    Redraws the header. Useful if a column name changes, or something else that changes how the column header
    is displayed.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.refreshHeader(%s)" % (self.varId))

  def flashCells(self, params):
    """
    Description:
    -----------
    Flash rows, columns or individual cells. See Flashing Cells.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    params = JsUtils.jsConvertData(params, None)
    return JsObjects.JsVoid("%s.api.flashCells(%s)" % (self.varId, params))

  def clearFocusedCell(self):
    """
    Description:
    -----------
    Clears the focused cell.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.clearFocusedCell()" % (self.varId))

  def tabToNextCell(self):
    """
    Description:
    -----------
    Navigates the grid focus to the next cell, as if tabbing.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.tabToNextCell()" % (self.varId))

  def tabToPreviousCell(self):
    """
    Description:
    -----------
    Navigates the grid focus to the previous cell, as if shift-tabbing.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.tabToPreviousCell()" % (self.varId))

  def showLoadingOverlay(self):
    """
    Description:
    -----------
    Show the 'loading' overlay.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.showLoadingOverlay()" % (self.varId))

  def showNoRowsOverlay(self):
    """
    Description:
    -----------
    Show the 'no rows' overlay.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.showNoRowsOverlay()" % (self.varId))

  def hideOverlay(self):
    """
    Description:
    -----------
    Hides the overlay if showing.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.hideOverlay()" % (self.varId))

  def destroy(self):
    """
    Description:
    -----------
    Will destroy the grid and release resources.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.destroy()" % (self.varId))

  def resetRowHeights(self):
    """
    Description:
    -----------
    Tells the grid to recalculate the row heights.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.resetRowHeights()" % (self.varId))

  def paginationIsLastPageFound(self):
    """
    Description:
    -----------
    Returns true when the last page is known; this will always be the case if you are using the Client-Side Row Model
    for pagination.
    Returns false when the last page is not known; this only happens when using Infinite Scrolling Row Model.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.paginationIsLastPageFound()" % (self.varId))

  def copySelectedRangeToClipboard(self, includeHeaders):
    """
    Description:
    -----------
    Copies the selected ranges to the clipboard.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    includeHeaders = JsUtils.jsConvertData(includeHeaders, None)
    return JsObjects.JsVoid("%s.api.copySelectedRangeToClipboard(%s)" % (self.varId, includeHeaders))

  def copySelectedRangeDown(self):
    """
    Description:
    -----------
    Copies the selected range down, similar to Ctrl + D in Excel.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.copySelectedRangeDown()" % self.varId)

  def paginationGetPageSize(self):
    """
    Description:
    -----------
    Returns how many rows are being shown per page.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.paginationGetPageSize()" % (self.varId))

  def paginationSetPageSize(self, newPageSize):
    """
    Description:
    -----------
    Sets the paginationPageSize to newPageSize, then re-paginates the grid so the changes are applied immediately.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    newPageSize = JsUtils.jsConvertData(newPageSize, None)
    return JsObjects.JsVoid("%s.api.paginationSetPageSize(%s)" % (self.varId, newPageSize))

  def paginationGetCurrentPage(self):
    """
    Description:
    -----------
    Returns the 0-based index of the page which is showing.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.paginationGetCurrentPage()" % (self.varId))

  def paginationGetTotalPages(self):
    """
    Description:
    -----------
    Returns the total number of pages. Returns null if paginationIsLastPageFound() == false.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.paginationGetTotalPages()" % (self.varId))

  def paginationGetRowCount(self):
    """
    Description:
    -----------
    The total number of rows. Returns null if paginationIsLastPageFound() == false.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.paginationGetRowCount()" % (self.varId))

  def paginationGoToPage(self, pageNumber):
    """
    Description:
    -----------
    Goes to the specified page. If the page requested doesn't exist, it will go to the last page.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    pageNumber = JsUtils.jsConvertData(pageNumber, None)
    return JsObjects.JsVoid("%s.api.paginationGoToPage(%s)" % (self.varId, pageNumber))

  def paginationGoToNextPage(self):
    """
    Description:
    -----------
    Shorthands for goToPage(relevantPageNumber).

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.paginationGoToNextPage()" % self.varId)

  def paginationGoToPreviousPage(self):
    """
    Description:
    -----------
    Shorthands for goToPage(relevantPageNumber).

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.paginationGoToPreviousPage()" % self.varId)

  def paginationGoToFirstPage(self):
    """
    Description:
    -----------
    Shorthands for goToPage(relevantPageNumber).

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.paginationGoToFirstPage()" % self.varId)

  def paginationGoToLastPage(self):
    """
    Description:
    -----------
    Shorthands for goToPage(relevantPageNumber).

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    return JsObjects.JsVoid("%s.api.paginationGoToLastPage()" % self.varId)

  def setSideBarVisible(self, show):
    """
    Description:
    -----------
    Tells the grid to recalculate the row heights.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-api/
    """
    show = JsUtils.jsConvertData(show, None)
    return JsObjects.JsVoid("%s.api.setSideBarVisible(%s)" % (self.varId, show))

  def getSortModel(self):
    """
    Description:
    -----------
    Returns the sort state.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-api/

    """
    return JsObjects.JsVoid("%s.api.getSortModel()" % self.varId)
