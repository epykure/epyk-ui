
import logging

from epyk.core.html.options import Options
from epyk.core.html.options import Enums


class EnumSidebar(Enums):

  def filters(self):
    return self._set_value()

  def columns(self):
    return self._set_value()


class CellEditor(Enums):

  def datePicker(self):
    return self._set_value()

  def numericCellEditor(self):
    return self._set_value()

  def agLargeTextCellEditor(self):
    return self._set_value()

  def agRichSelectCellEditor(self, values, **kwargs):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/

    Attributes:
    ----------
    :param values:
    """
    cell_editor_params = {'values': values}
    if kwargs:
      cell_editor_params.update(kwargs)
    self._set_value(value=cell_editor_params, name="cellEditorParams")
    return self._set_value()


class CellRenderer(Enums):

  def singleClickEditRenderer(self):
    return self._set_value()

  def agGroupCellRenderer(self):
    return self._set_value()


class AggFnc(Enums):

  def null(self):
    """
    Description:
    -----------


    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._set_value(value=None)

  def sum(self):
    """
    Description:
    -----------


    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._set_value()


class ColType(Enums):

  def nonEditableColumn(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._set_value()

  def dateColumn(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._set_value()

  def numericColumn(self):
    """
    Description:
    -----------

    """
    return self._set_value()

  def numberColumn(self):
    """
    Description:
    -----------

    """
    return self._set_value()

  def medalColumn(self):
    """
    Description:
    -----------

    """
    return self._set_value()


class ColumnFilter(Enums):

  def true(self):
    return self._set_value(value='true', js_type=True)

  def false(self):
    return self._set_value(value='false', js_type=True)

  def agTextColumnFilter(self, **kwargs):
    """
    Description:
    -----------
    A Text Filter for string comparisons.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-filtering/
    """
    if kwargs:
      self._set_value(value=kwargs, name="filterParams")
    return self._set_value()

  def agDateColumnFilter(self, **kwargs):
    """
    Description:
    -----------
    A Date Filter for date comparisons.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-filter-date/
    """
    if kwargs:
      self._set_value(value=kwargs, name="filterParams")
    return self._set_value()

  def agNumberColumnFilter(self):
    """
    Description:
    -----------
    A Number Filter for number comparisons.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-filtering/
    """
    return self._set_value()

  def agSetColumnFilter(self, filter_name):
    """
    Description:
    -----------
    A Set Filter, influenced by how filters work in Microsoft Excel. This is an ag-Grid-Enterprise feature.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-filter-component/
    """
    return self._set_value(value=filter_name)


class ColOrder(Enums):

  def asc(self):
    return self._set_value()

  def desc(self):
    return self._set_value()


class Column(Options):

  @property
  def children(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/javascript-grid-grouping-headers/
    """
    return self._config_get()

  @children.setter
  def children(self, val):
    self._config(val)

  @property
  def colId(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/javascript-grid-grouping-headers/
    """
    return self._config_get()

  @colId.setter
  def colId(self, val):
    self._config(val)

  @property
  def columnGroupShow(self):
    """
    Description:
    -----------
    values closed, open.

    https://www.ag-grid.com/javascript-grid-grouping-headers/
    """
    return self._config_get()

  @columnGroupShow.setter
  def columnGroupShow(self, val):
    self._config(val)

  @property
  def editor(self):
    """
    Description:
    -----------
    Cell editing format

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/

    :rtype: CellEditor
    """
    return CellEditor(self, "cellEditor")

  @property
  def editable(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @editable.setter
  def editable(self, val):
    self._config(val)

  @property
  def enableRowGroup(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._config_get()

  @enableRowGroup.setter
  def enableRowGroup(self, val):
    self._config(val)

  @property
  def field(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @field.setter
  def field(self, val: str):
    self._config(val)

  @property
  def filters(self):
    """
    Description:
    -----------
    Set filtering on a column using the column definition property filter. The property can have one of the following
    values:

    Related Pages:

      https://www.ag-grid.com/javascript-grid-filtering/
    """
    return ColumnFilter(self, 'filter')

  @property
  def hide(self):
    """
    Description:
    -----------
    True if the column is hidden, otherwise false.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._config_get()

  @hide.setter
  def hide(self, val):
    self._config(val)

  @property
  def headerName(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @headerName.setter
  def headerName(self, val: str):
    self._config(val)

  @property
  def lockPinned(self):
    """
    Description:
    -----------
    If you do not want the user to be able to pin using the UI, set the property lockPinned=true.
    This will block the UI in the following way:

    Related Pages:

      https://www.ag-grid.com/javascript-grid-pinning/
    """
    return self._config_get()

  @lockPinned.setter
  def lockPinned(self, val):
    self._config(val)

  @property
  def marryChildren(self):
    """
    Description:
    -----------
    Sometimes you want columns of the group to always stick together.
    To achieve this, set the column group property marryChildren=true. The example below demonstrates the following:

    """
    return self._config_get()

  @marryChildren.setter
  def marryChildren(self, val):
    self._config(val)

  @property
  def sortable(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @sortable.setter
  def sortable(self, val):
    self._config(val)

  @property
  def filter(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @filter.setter
  def filter(self, val):
    self._config(val)

  @property
  def flex(self):
    """
    Description:
    -----------
    It's often required that one or more columns fill the entire available space in the grid. For this scenario,
    it is possible to use the flex config.
    Some columns could be set with a regular width config, while other columns would have a flex config.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._config_get()

  @flex.setter
  def flex(self, val):
    self._config(val)

  @property
  def checkboxSelection(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @checkboxSelection.setter
  def checkboxSelection(self, val):
    self._config(val)

  @property
  def suppressMovable(self):
    """
    Description:
    -----------
    The column property suppressMovable changes whether the column can be dragged.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-moving/
    """
    return self._config_get()

  @suppressMovable.setter
  def suppressMovable(self, val):
    self._config(val)

  @property
  def pinned(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @pinned.setter
  def pinned(self, val):
    self._config(val)

  @property
  def lockPosition(self):
    """
    Description:
    -----------
    The column property lockPosition locks columns to the first position in the grid.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-moving/
    """
    return self._config_get()

  @lockPosition.setter
  def lockPosition(self, val):
    self._config('locked-col', name="cellClass")
    self._config(val)

  @property
  def maxWidth(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @maxWidth.setter
  def maxWidth(self, val):
    self._config(val)

  @property
  def minWidth(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @minWidth.setter
  def minWidth(self, val):
    self._config(val)

  @property
  def resizable(self):
    """
    Description:
    -----------
    Turn column resizing on for the grid by setting resizable=true for each column.
    To set resizing for each column, set resizable=true on the default column definition.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._config_get()

  @resizable.setter
  def resizable(self, val):
    self._config(val)

  @property
  def rowGroup(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @rowGroup.setter
  def rowGroup(self, val):
    self._config(val)

  @property
  def rowGroupIndex(self):
    """
    Description:
    -----------
    The index of the row group. If the column is not grouped, this field is null.
    If multiple columns are used to group, this index provides the order of the grouping.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._config_get()

  @rowGroupIndex.setter
  def rowGroupIndex(self, val):
    self._config(val)

  @property
  def suppressSizeToFit(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @suppressSizeToFit.setter
  def suppressSizeToFit(self, val):
    self._config(val)

  @property
  def type(self):
    """
    Description:
    -----------

    """
    return ColType(self, self._attrs)

  @property
  def enableCellChangeFlash(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/javascript-grid-refresh/
    """
    return self._config_get()

  @enableCellChangeFlash.setter
  def enableCellChangeFlash(self, val):
    self._config(val)

  @property
  def suppressCellFlash(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/javascript-grid-refresh/
    """
    return self._config_get()

  @suppressCellFlash.setter
  def suppressCellFlash(self, val):
    self._config(val)

  @property
  def sortingOrder(self):
    """
    Description:
    -----------
    It is possible to override this behaviour by providing your own sortingOrder on either the gridOptions or the
    colDef.
    If defined both in colDef and gridOptions, the colDef will get preference, allowing you to defined a common default,
    and then tailoring per column.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-sorting/
    """
    return self._config_get()

  @sortingOrder.setter
  def sortingOrder(self, val):
    self._config(val)

  @property
  def sort(self):
    """
    Description:
    -----------
    Cell editing format

    Related Pages:

      https://www.ag-grid.com/javascript-grid-sorting/
    """
    return ColOrder(self, 'sort')


class DefaultColDef(Options):

  @property
  def filter(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @filter.setter
  def filter(self, val):
    self._config(val)

  @property
  def flex(self):
    """
    Description:
    -----------
    It's often required that one or more columns fill the entire available space in the grid. For this scenario,
    it is possible to use the flex config.
    Some columns could be set with a regular width config, while other columns would have a flex config.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._config_get()

  @flex.setter
  def flex(self, val):
    self._config(val)

  @property
  def minWidth(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @minWidth.setter
  def minWidth(self, val):
    self._config(val)

  @property
  def editable(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @editable.setter
  def editable(self, val):
    self._config(val)

  @property
  def resizable(self):
    """
    Description:
    -----------
    Turn column resizing on for the grid by setting resizable=true for each column.
    To set resizing for each column, set resizable=true on the default column definition.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._config_get()

  @resizable.setter
  def resizable(self, val):
    self._config(val)

  @property
  def sortable(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @sortable.setter
  def sortable(self, val):
    self._config(val)

  @property
  def treeData(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.ag-grid.com/documentation/javascript/tree-data/
    """
    return self._config_get()

  @treeData.setter
  def treeData(self, val):
    if 'ag-grid-community' in self.component.jsImports and self.component.verbose:
      logging.warning("treeData not available in the community version")

    self._config(val)


class TableToolPanelsParams(Options):

  @property
  def suppressSyncLayoutWithGrid(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @suppressSyncLayoutWithGrid.setter
  def suppressSyncLayoutWithGrid(self, val):
    self._config(val)


class TableToolPanelsFilters(Options):

  @property
  def id(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @id.setter
  def id(self, val):
    self._config(val)

  @property
  def labelDefault(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @labelDefault.setter
  def labelDefault(self, val):
    self._config(val)

  @property
  def labelKey(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @labelKey.setter
  def labelKey(self, val):
    self._config(val)

  @property
  def iconKey(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @iconKey.setter
  def iconKey(self, val):
    self._config(val)

  @property
  def toolPanel(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @toolPanel.setter
  def toolPanel(self, val):
    self._config(val)

  def toolPanelParams(self):
    """
    Description:
    -----------

    """
    return self.has_attribute(TableToolPanelsParams)


class TableToolPanels(Options):

  def filters(self):
    """
    Description:
    -----------

    :return:
    """
    return self.has_attribute(TableToolPanelsFilters)


class TableSideBar(Options):

  def toolPanelsColumn(self):
    self._config(["columns"], name="toolPanels")
    return self


class EnumStatusPanelsPanels(Options):
  @property
  def statusPanel(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @statusPanel.setter
  def statusPanel(self, val):
    self._config(val)

  @property
  def align(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @align.setter
  def align(self, val):
    self._config(val)

  @property
  def key(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @key.setter
  def key(self, val):
    self._config(val)


class TableStatusBar(Options):

  def statusPanels(self):
    """
    Description:
    -----------

    :rtype: EnumStatusPanelsPanels
    """
    return self._config_sub_data_enum('statusPanels', EnumStatusPanelsPanels)


class TableConfig(Options):

  @property
  def alignedGrids(self):
    """
    Description:
    -----------
    To have one (the first) grid reflect column changes in another (the second), place the first grid's options in
    alignedGrids property of the second grids.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-aligned-grids/
    """
    return self._config_get()

  @alignedGrids.setter
  def alignedGrids(self, val):
    self._config(val)

  @property
  def animateRows(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @animateRows.setter
  def animateRows(self, val):
    self._config(val)

  @property
  def colResizeDefault(self):
    """
    Description:
    -----------
    If you hold 'shift' while dragging the resize handle, the column will take space away from the column adjacent to
    it. This means the total width for all columns will be constant.

    You can also change the default behaviour for resizing.
    Set grid property colResizeDefault='shift' to have shift resizing as default and normal resizing to happen when
    shift key is pressed.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._config_get()

  @colResizeDefault.setter
  def colResizeDefault(self, val):
    self._config(val)

  @property
  def columns(self) -> Column:
    """
    Description:
    -----------

    """
    return self._config_sub_data_enum("columnDefs", Column)

  @property
  def defaultColDef(self) -> DefaultColDef:
    """
    Description:
    -----------

    """
    return self._config_sub_data("defaultColDef", DefaultColDef)

  @property
  def data(self):
    """
    Description:
    -----------
    """
    return self._config_get(name="rowData")

  @data.setter
  def data(self, val):
    self._config(val, name="rowData")

  @property
  def deltaColumnMode(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @deltaColumnMode.setter
  def deltaColumnMode(self, val: str):
    self._config(val)

  @property
  def enablePivot(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @enablePivot.setter
  def enablePivot(self, flag: bool):
    self._config(flag)

  @property
  def enableValue(self):
    """
    Description:
    -----------
    """
    return self._config_get()

  @enableValue.setter
  def enableValue(self, flag: bool):
    self._config(flag)

  @property
  def enterMovesDown(self):
    """
    Description:
    -----------
    Set to true to have Enter key move focus to the cell below if not editing.
    The default is Enter key starts editing the currently focused cell.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._config_get()

  @enterMovesDown.setter
  def enterMovesDown(self, val):
    self._config(val)

  @property
  def enterMovesDownAfterEdit(self):
    """
    Description:
    -----------
    Set to true to have Enter key move focus to the cell below after Enter is pressed while editing.
    The default is editing will stop and focus will remain on the editing cell.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._config_get()

  @enterMovesDownAfterEdit.setter
  def enterMovesDownAfterEdit(self, val):
    self._config(val)

  @property
  def pagination(self):
    """
    Description:
    -----------
    To enable pagination in, set the grid property pagination=true.
    The following simple example shows this, the only difference to this and previous examples is the pagination=true
    property.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._config_get()

  @pagination.setter
  def pagination(self, val):
    self._config(val)

  @property
  def paginationPageSize(self):
    """
    Description:
    -----------
    How many rows to load per page. If paginationAutoPageSize is specified, this property is ignored.
    See Customising Pagination.
    Default: 100

    Related Pages:

      https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._config_get(100)

  @paginationPageSize.setter
  def paginationPageSize(self, num: int):
    self.pagination = num > 0
    self._config(num)

  @property
  def paginationAutoPageSize(self):
    """
    Description:
    -----------
    If you set paginationAutoPageSize=true the grid will automatically show as many rows in each page as it can fit.
    This is demonstrated below. Note if you resize the display area of the grid, the page size automatically changes.
    To view this, open the example up in a new tab and resize your browser.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._config_get()

  @paginationAutoPageSize.setter
  def paginationAutoPageSize(self, num: int):
    self._config(num)

  @property
  def groupSelectsChildren(self):
    """
    Description:
    -----------


    Related Pages:

      https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._config_get()

  @groupSelectsChildren.setter
  def groupSelectsChildren(self, val):
    self._config(val)

  @property
  def rowHeight(self):
    """
    Description:
    -----------
    By default, the grid will display rows with a height of 25px. You can change this for each row individually
    to give each row a different height.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/row-height/
    """
    return self._config_get(25)

  @rowHeight.setter
  def rowHeight(self, num: int):
    self._config(int(num))

  @property
  def singleClickEdit(self):
    """
    Description:
    -----------
    To change the default so that a single-click starts editing, set the property gridOptions.singleClickEdit = true.
    This is useful when you want a cell to enter edit mode as soon as you click on it, similar to the experience you
    get when inside Excel.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._config_get()

  @singleClickEdit.setter
  def singleClickEdit(self, val):
    self._config(val)

  @property
  def suppressClickEdit(self):
    """
    Description:
    -----------
    The grid configures a cellRenderer with a button to start editing.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._config_get()

  @suppressClickEdit.setter
  def suppressClickEdit(self, val):
    self._config(val)

  @property
  def suppressPaginationPanel(self):
    """
    Description:
    -----------
    If you set suppressPaginationPanel=true, the grid will not show the standard navigation controls for pagination.
    This is useful is you want to provide your own navigation controls.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._config_get()

  @suppressPaginationPanel.setter
  def suppressPaginationPanel(self, val):
    self._config(val)

  @property
  def suppressScrollOnNewData(self):
    """
    Description:
    -----------
    The example also sets property suppressScrollOnNewData=true, which tells the grid to NOT scroll to the top when the
    page changes.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._config_get()

  @suppressScrollOnNewData.setter
  def suppressScrollOnNewData(self, val):
    self._config(val)

  @property
  def ensureDomOrder(self):
    """
    Description:
    -----------
    ensures the rows and columns in the DOM always appear in the same order as displayed in the grid.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._config_get()

  @ensureDomOrder.setter
  def ensureDomOrder(self, val):
    self._config(val)

  @property
  def suppressColumnVirtualisation(self):
    """
    Description:
    -----------
    Ensures all columns are rendered, i.e. appears in the DOM.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-accessibility/
    """
    return self._config_get()

  @suppressColumnVirtualisation.setter
  def suppressColumnVirtualisation(self, val):
    self._config(val)

  @property
  def suppressDragLeaveHidesColumns(self):
    """
    Description:
    -----------
    Column animations happen when you move a column. The default is for animations to be turned on.
    It is recommended that you leave the column move animations on unless your target platform (browser and hardware)
    is to slow to manage the animations.
    To turn OFF column animations, set the grid property suppressColumnMoveAnimation=true.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-moving/
    """
    return self._config_get()

  @suppressDragLeaveHidesColumns.setter
  def suppressDragLeaveHidesColumns(self, val):
    self._config(val)

  @property
  def rowMultiSelectWithClick(self):
    """
    Description:
    -----------
    Set to true to allow multiple rows to be selected with clicks.
    For example, if you click to select one row and then click to select another row, the first row will stay selected
    as well.
    Clicking a selected row in this mode will deselect the row.
    This is useful for touch devices where Ctrl and Shift clicking is not an option.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-selection/
    """
    return self._config_get()

  @rowMultiSelectWithClick.setter
  def rowMultiSelectWithClick(self, val):
    self._config(val)

  @property
  def rowDeselection(self):
    """
    Description:
    -----------
    Set to true to allow rows to be deselected if you hold down Ctrl and click the row.
    By default, the grid disallows deselection of rows (i.e. once a row is selected, it remains selected until another
    row is selected in its place).

    Related Pages:

      https://www.ag-grid.com/javascript-grid-selection/
    """
    return self._config_get()

  @rowDeselection.setter
  def rowDeselection(self, val):
    self._config(val)

  @property
  def rowSelection(self):
    """
    Description:
    -----------
    Type of row selection, set to either 'single' or 'multiple' to enable selection.
    'single' will use single row selection, such that when you select a row, any previously selected row gets
    unselected.
    'multiple' allows multiple rows to be selected.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-selection/
    """
    return self._config_get()

  @rowSelection.setter
  def rowSelection(self, val):
    self._config(val)

  @property
  def rowBuffer(self):
    """
    Description:
    -----------
    Sets the number of rows rendered outside of the scrollable viewable area.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-accessibility/
    """
    return self._config_get()

  @rowBuffer.setter
  def rowBuffer(self, val):
    self._config(val)

  @property
  def suppressRowClickSelection(self):
    """
    Description:
    -----------
    If true, rows won't be selected when clicked. Use, for example, when you want checkbox selection, and don't want to
    also select the row when the row is clicked.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-selection/
    """
    return self._config_get()

  @suppressRowClickSelection.setter
  def suppressRowClickSelection(self, val):
    self._config(val)

  @property
  def sortingOrder(self):
    """
    Description:
    -----------
    It is possible to override this behaviour by providing your own sortingOrder on either the gridOptions or the
    colDef.
    If defined both in colDef and gridOptions, the colDef will get preference, allowing you to defined a common
    default, and then tailoring per column.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-sorting/
    """
    return self._config_get()

  @sortingOrder.setter
  def sortingOrder(self, val):
    self._config(val)

  @property
  def sideBar(self) -> TableSideBar:
    """
    Description:
    -----------

    """
    return self._config_sub_data("sideBar", TableSideBar)

  @property
  def sideBars(self):
    return EnumSidebar(self, "sideBar")

  def statusBar(self) -> TableStatusBar:
    """
    Description:
    -----------

    """
    return self._config_sub_data("statusBar", TableStatusBar)
