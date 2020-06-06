
from epyk.core.html import Html

from epyk.core.data.DataClass import DataClass
from epyk.core.js.packages import JsAgGrid
from epyk.core.data.DataClass import DataGroup

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class Table(Html.Html):
  name = 'Ag Grid Table'
  requirements = ('ag-grid', )

  def __init__(self, report, records, width, height, htmlCode, options, profile):
    data, columns, self.__config = [], [], None
    super(Table, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.config.update(options)
    if records is not None:
      self.config.data = records

  def headers(self, colsDef):
    """

    :param colsDef:
    """
    for col in self.config['columnDefs']:
      if col['colId'] in colsDef:
        col.update(colsDef[col['colId']])

  @property
  def style(self):
    if self._styleObj is None:
      self._styleObj = GrpClsTable.Aggrid(self)
    return self._styleObj

  @property
  def config(self):
    if self.__config is None:
      self.__config = TableConfig(self._report)
    return self.__config

  @property
  def js(self):
    """
    Return the Javascript internal object

    :return: A Javascript object

    :rtype: JsAgGrid.AgGrid
    """
    if self._js is None:
      self._js = JsAgGrid.AgGrid(self._report, selector=self.tableId, setVar=False, parent=self)
    return self._js

  def add_column(self, field, title=None):
    """

    :param field:
    :param title:
    """
    col_def = self.config.columns
    col_def.field = field
    col_def.colId = field
    col_def.headerName = field if title is None else title
    # col_def.filter = True
    return col_def

  @property
  def tableId(self):
    """
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlCode

  def build(self, data=None, options=None, profile=False):
    if data:
      return self.js.setRowData(data)

    return 'var %(tableId)s = %(config)s; new agGrid.Grid(%(htmlCode)s, %(tableId)s)' % {'tableId': self.tableId, 'config': self.config, 'htmlCode': self.dom.varName}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "<div %s></div>" % (self.get_attrs(pyClassNames=self.style.get_classes()))


class CellEditor(DataGroup):

  def datePicker(self):
    self._attrs["cellEditor"] = "'datePicker'"

  def numericCellEditor(self):
    self._attrs["cellEditor"] = "'numericCellEditor'"

  def agLargeTextCellEditor(self):
    self._attrs["cellEditor"] = "'agLargeTextCellEditor'"

  def agRichSelectCellEditor(self, values, **kwargs):
    """

    https://www.ag-grid.com/javascript-grid-cell-editing/

    :param values:
    :param kwargs:
    """
    self._attrs["cellEditor"] = "'agRichSelectCellEditor'"
    self._attrs["cellEditorParams"] = {'values': values}
    if kwargs:
      self._attrs["cellEditorParams"].update(kwargs)
    return self


class CellRenderer(DataClass):
  def singleClickEditRenderer(self):
    self._attrs["renderer"] = "singleClickEditRenderer"
    return self

  def agGroupCellRenderer(self):
    self._attrs["renderer"] = "agGroupCellRenderer"
    return self


class AggFnc(DataGroup):

  def null(self):
    """
    https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    self._attrs["renderer"] = None

  def sum(self):
    """
    https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    self._attrs["renderer"] = "sum"


class ColType(DataGroup):

  def nonEditableColumn(self):
    """

    https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    self._attrs["type"] = 'nonEditableColumn'

  def dateColumn(self):
    """

    https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    self._attrs["type"] = 'dateColumn'

  def numericColumn(self):
    self._attrs["type"] = 'numericColumn'

  def numberColumn(self):
    self._attrs["type"] = 'numberColumn'

  def medalColumn(self):
    self._attrs["type"] = 'medalColumn'


class ColumnFilter(DataGroup):

  def true(self):
    self._attrs["filter"] = 'true'
    return self

  def false(self):
    self._attrs["filter"] = 'false'
    return self

  def agTextColumnFilter(self, **kwargs):
    """
    A Text Filter for string comparisons.

    https://www.ag-grid.com/javascript-grid-filtering/

    :param kwargs:
    """
    self._attrs["filter"] = "'agTextColumnFilter'"
    if kwargs:
      self._attrs["filterParams"] = kwargs
    return self

  def agDateColumnFilter(self, **kwargs):
    """
    A Date Filter for date comparisons.

    https://www.ag-grid.com/javascript-grid-filter-date/

    :param kwargs:
    """
    self._attrs["filter"] = "'agDateColumnFilter'"
    if kwargs:
      self._attrs["filterParams"] = kwargs
    return self

  def agNumberColumnFilter(self):
    """
    A Number Filter for number comparisons.

    https://www.ag-grid.com/javascript-grid-filtering/
    """
    self._attrs["filter"] = "'agNumberColumnFilter'"
    return self

  def agSetColumnFilter(self, filterName):
    """
    A Set Filter, influenced by how filters work in Microsoft Excel. This is an ag-Grid-Enterprise feature.

    https://www.ag-grid.com/javascript-grid-filter-component/
    :return:
    """
    self._attrs["filter"] = filterName
    return self


class ColOrder(DataGroup):

  def asc(self):
    self._attrs["sort"] = 'asc'
    return self

  def desc(self):
    self._attrs["sort"] = 'desc'
    return self


class Column(DataClass):

  @property
  def children(self):
    """
    Description:
    -----------

    https://www.ag-grid.com/javascript-grid-grouping-headers/
    """
    return self._attrs["children"]

  @children.setter
  def children(self, val):
    self._attrs["children"] = val

  @property
  def colId(self):
    """
    Description:
    -----------

    https://www.ag-grid.com/javascript-grid-grouping-headers/
    """
    return self._attrs["colId"]

  @colId.setter
  def colId(self, val):
    self._attrs["colId"] = val

  @property
  def columnGroupShow(self):
    """
    Description:
    -----------
    values closed, open

    https://www.ag-grid.com/javascript-grid-grouping-headers/
    """
    return self._attrs["columnGroupShow"]

  @columnGroupShow.setter
  def columnGroupShow(self, val):
    self._attrs["columnGroupShow"] = val

  @property
  def editor(self):
    """
    Description:
    -----------
    Cell editing format

    https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return CellEditor(self, self._attrs)

  @property
  def editable(self):
    """
    Description:
    -----------
    """
    return self._attrs["editable"]

  @editable.setter
  def editable(self, val):
    self._attrs["editable"] = val

  @property
  def enableRowGroup(self):
    """
    Description:
    -----------

    https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._attrs["enableRowGroup"]

  @enableRowGroup.setter
  def enableRowGroup(self, val):
    self._attrs["enableRowGroup"] = val

  @property
  def field(self):
    """
    Description:
    -----------
    """
    return self._attrs["field"]

  @field.setter
  def field(self, val):
    self._attrs["field"] = val

  @property
  def filter(self):
    """
    Description:
    -----------
    Set filtering on a column using the column definition property filter. The property can have one of the following values:

    https://www.ag-grid.com/javascript-grid-filtering/
    """
    return ColumnFilter(self, self._attrs)

  @property
  def hide(self):
    """
    Description:
    -----------
    True if the column is hidden, otherwise false.

    https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._attrs["hide"]

  @hide.setter
  def hide(self, val):
    self._attrs["hide"] = val

  @property
  def headerName(self):
    """
    Description:
    -----------
    """
    return self._attrs["headerName"]

  @headerName.setter
  def headerName(self, val):
    self._attrs["headerName"] = val

  @property
  def lockPinned(self):
    """
    Description:
    -----------
    If you do not want the user to be able to pin using the UI, set the property lockPinned=true.
    This will block the UI in the following way:

    https://www.ag-grid.com/javascript-grid-pinning/
    """
    return self._attrs["lockPinned"]

  @lockPinned.setter
  def lockPinned(self, val):
    self._attrs["lockPinned"] = val

  @property
  def marryChildren(self):
    """
    Description:
    -----------
    Sometimes you want columns of the group to always stick together.
    To achieve this, set the column group property marryChildren=true. The example below demonstrates the following:

    """
    return self._attrs["marryChildren"]

  @marryChildren.setter
  def marryChildren(self, val):
    self._attrs["marryChildren"] = val

  @property
  def sortable(self):
    """
    Description:
    -----------
    """
    return self._attrs["sortable"]

  @sortable.setter
  def sortable(self, val):
    self._attrs["sortable"] = val

  @property
  def filter(self):
    """
    Description:
    -----------
    """
    return self._attrs["filter"]

  @filter.setter
  def filter(self, val):
    self._attrs["filter"] = val

  @property
  def flex(self):
    """
    Description:
    -----------
    It's often required that one or more columns fill the entire available space in the grid. For this scenario,
    it is possible to use the flex config.
    Some columns could be set with a regular width config, while other columns would have a flex config.

    https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._attrs["flex"]

  @flex.setter
  def flex(self, val):
    self._attrs["flex"] = val

  @property
  def checkboxSelection(self):
    """
    Description:
    -----------
    """
    return self._attrs["checkboxSelection"]

  @checkboxSelection.setter
  def checkboxSelection(self, val):
    self._attrs["checkboxSelection"] = val

  @property
  def suppressMovable(self):
    """
    Description:
    -----------
    The column property suppressMovable changes whether the column can be dragged.

    https://www.ag-grid.com/javascript-grid-column-moving/
    """
    return self._attrs["suppressMovable"]

  @suppressMovable.setter
  def suppressMovable(self, val):
    self._attrs["suppressMovable"] = val

  @property
  def pinned(self):
    """
    Description:
    -----------
    """
    return self._attrs["pinned"]

  @pinned.setter
  def pinned(self, val):
    self._attrs["pinned"] = val

  @property
  def lockPosition(self):
    """
    Description:
    -----------
    The column property lockPosition locks columns to the first position in the grid.

    https://www.ag-grid.com/javascript-grid-column-moving/

    """
    return self._attrs["lockPosition"]

  @lockPosition.setter
  def lockPosition(self, val):
    self._attrs["cellClass"] = 'locked-col'
    self._attrs["lockPosition"] = val

  @property
  def maxWidth(self):
    """
    Description:
    -----------
    """
    return self._attrs["maxWidth"]

  @maxWidth.setter
  def maxWidth(self, val):
    self._attrs["maxWidth"] = val

  @property
  def minWidth(self):
    """
    Description:
    -----------
    """
    return self._attrs["minWidth"]

  @minWidth.setter
  def minWidth(self, val):
    self._attrs["minWidth"] = val

  @property
  def resizable(self):
    """
    Description:
    -----------
    Turn column resizing on for the grid by setting resizable=true for each column.
    To set resizing for each column, set resizable=true on the default column definition.

    https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._attrs["resizable"]

  @resizable.setter
  def resizable(self, val):
    self._attrs["resizable"] = val

  @property
  def rowGroup(self):
    """
    Description:
    -----------
    """
    return self._attrs["rowGroup"]

  @rowGroup.setter
  def rowGroup(self, val):
    self._attrs["rowGroup"] = val

  @property
  def rowGroupIndex(self):
    """
    Description:
    -----------
    The index of the row group. If the column is not grouped, this field is null.
    If multiple columns are used to group, this index provides the order of the grouping.

    https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._attrs["rowGroupIndex"]

  @rowGroupIndex.setter
  def rowGroupIndex(self, val):
    self._attrs["rowGroupIndex"] = val

  @property
  def suppressSizeToFit(self):
    """
    Description:
    -----------
    """
    return self._attrs["suppressSizeToFit"]

  @suppressSizeToFit.setter
  def suppressSizeToFit(self, val):
    self._attrs["suppressSizeToFit"] = val

  @property
  def type(self):
    """
    Description:
    -----------

    :return:
    """
    return ColType(self, self._attrs)

  @property
  def enableCellChangeFlash(self):
    """
    Description:
    -----------

    https://www.ag-grid.com/javascript-grid-refresh/
    """
    return self._attrs["enableCellChangeFlash"]

  @enableCellChangeFlash.setter
  def enableCellChangeFlash(self, val):
    self._attrs["enableCellChangeFlash"] = val

  @property
  def suppressCellFlash(self):
    """
    Description:
    -----------

    https://www.ag-grid.com/javascript-grid-refresh/
    """
    return self._attrs["suppressCellFlash"]

  @suppressCellFlash.setter
  def suppressCellFlash(self, val):
    self._attrs["suppressCellFlash"] = val

  @property
  def sortingOrder(self):
    """
    Description:
    -----------
    It is possible to override this behaviour by providing your own sortingOrder on either the gridOptions or the colDef.
    If defined both in colDef and gridOptions, the colDef will get preference, allowing you to defined a common default, and then tailoring per column.

    https://www.ag-grid.com/javascript-grid-sorting/
    """
    return self._attrs["sortingOrder"]

  @sortingOrder.setter
  def sortingOrder(self, val):
    self._attrs["sortingOrder"] = val

  @property
  def sort(self):
    """
    Description:
    -----------
    Cell editing format

    https://www.ag-grid.com/javascript-grid-sorting/
    """
    return ColOrder(self, self._attrs)


class DefaultColDef(DataClass):

  @property
  def filter(self):
    """
    Description:
    -----------
    """
    return self._attrs["filter"]

  @filter.setter
  def filter(self, val):
    self._attrs["filter"] = val

  @property
  def flex(self):
    """
    Description:
    -----------
    It's often required that one or more columns fill the entire available space in the grid. For this scenario,
    it is possible to use the flex config.
    Some columns could be set with a regular width config, while other columns would have a flex config.

    https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._attrs["flex"]

  @flex.setter
  def flex(self, val):
    self._attrs["flex"] = val

  @property
  def minWidth(self):
    """
    Description:
    -----------
    """
    return self._attrs["minWidth"]

  @minWidth.setter
  def minWidth(self, val):
    self._attrs["minWidth"] = val

  @property
  def editable(self):
    """
    Description:
    -----------
    """
    return self._attrs["editable"]

  @editable.setter
  def editable(self, val):
    self._attrs["editable"] = val

  @property
  def resizable(self):
    """
    Description:
    -----------
    Turn column resizing on for the grid by setting resizable=true for each column.
    To set resizing for each column, set resizable=true on the default column definition.

    https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._attrs["resizable"]

  @resizable.setter
  def resizable(self, val):
    self._attrs["resizable"] = val

  @property
  def sortable(self):
    """
    Description:
    -----------
    """
    return self._attrs["sortable"]

  @sortable.setter
  def sortable(self, val):
    self._attrs["sortable"] = val


class TableToolPanelsParams(DataClass):

  @property
  def suppressSyncLayoutWithGrid(self):
    """
    Description:
    -----------
    """
    return self._attrs["suppressSyncLayoutWithGrid"]

  @suppressSyncLayoutWithGrid.setter
  def suppressSyncLayoutWithGrid(self, val):
    self._attrs["suppressSyncLayoutWithGrid"] = val


class TableToolPanelsFilters(DataClass):

  @property
  def id(self):
    """
    Description:
    -----------
    """
    return self._attrs["id"]

  @id.setter
  def id(self, val):
    self._attrs["id"] = val

  @property
  def labelDefault(self):
    """
    Description:
    -----------
    """
    return self._attrs["labelDefault"]

  @labelDefault.setter
  def labelDefault(self, val):
    self._attrs["labelDefault"] = val

  @property
  def labelKey(self):
    """
    Description:
    -----------
    """
    return self._attrs["labelKey"]

  @labelKey.setter
  def labelKey(self, val):
    self._attrs["labelKey"] = val

  @property
  def iconKey(self):
    """
    Description:
    -----------
    """
    return self._attrs["iconKey"]

  @iconKey.setter
  def iconKey(self, val):
    self._attrs["iconKey"] = val

  @property
  def toolPanel(self):
    """
    Description:
    -----------
    """
    return self._attrs["toolPanel"]

  @toolPanel.setter
  def toolPanel(self, val):
    self._attrs["toolPanel"] = val

  def toolPanelParams(self):
    """

    :return:
    """
    return self.has_attribute(TableToolPanelsParams)


class TableToolPanels(DataClass):

  def filters(self):
    """

    :return:
    """
    return self.has_attribute(TableToolPanelsFilters)


class TableSideBar(DataClass):

  def toolPanelsColumn(self):
    self._attrs["toolPanels"] = ["columns"]
    return self


class EnumStatusPanelsPanels(DataClass):
  @property
  def statusPanel(self):
    """
    Description:
    -----------
    """
    return self._attrs["statusPanel"]

  @statusPanel.setter
  def statusPanel(self, val):
    self._attrs["statusPanel"] = val

  @property
  def align(self):
    """
    Description:
    -----------
    """
    return self._attrs["align"]

  @align.setter
  def align(self, val):
    self._attrs["align"] = val

  @property
  def key(self):
    """
    Description:
    -----------
    """
    return self._attrs["key"]

  @key.setter
  def key(self, val):
    self._attrs["key"] = val


class TableStatusBar(DataClass):

  def statusPanels(self):
    return self.sub_data_enum('statusPanels', EnumStatusPanelsPanels)


class TableConfig(DataClass):

  @property
  def alignedGrids(self):
    """
    Description:
    -----------
    To have one (the first) grid reflect column changes in another (the second), place the first grid's options in alignedGrids property of the second grids.

    https://www.ag-grid.com/javascript-grid-aligned-grids/
    """
    return self._attrs["alignedGrids"]

  @alignedGrids.setter
  def alignedGrids(self, val):
    self._attrs["alignedGrids"] = val

  @property
  def animateRows(self):
    """
    Description:
    -----------
    """
    return self._attrs["animateRows"]

  @animateRows.setter
  def animateRows(self, val):
    self._attrs["animateRows"] = val

  @property
  def colResizeDefault(self):
    """
    Description:
    -----------
    If you hold 'shift' while dragging the resize handle, the column will take space away from the column adjacent to it.
    This means the total width for all columns will be constant.

    You can also change the default behaviour for resizing.
    Set grid property colResizeDefault='shift' to have shift resizing as default and normal resizing to happen when shift key is pressed.

    https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._attrs["colResizeDefault"]

  @colResizeDefault.setter
  def colResizeDefault(self, val):
    self._attrs["colResizeDefault"] = val

  @property
  def columns(self):
    """
    Description:
    -----------
    """
    return self.sub_data_enum("columnDefs", Column)

  @property
  def defaultColDef(self):
    """
    Description:
    -----------
    """
    return self.sub_data("defaultColDef", DefaultColDef)

  @property
  def data(self):
    """
    Description:
    -----------
    """
    return self._attrs["rowData"]

  @data.setter
  def data(self, val):
    self._attrs["rowData"] = val

  @property
  def deltaColumnMode(self):
    """
    Description:
    -----------
    """
    return self._attrs["deltaColumnMode"]

  @deltaColumnMode.setter
  def deltaColumnMode(self, val):
    self._attrs["deltaColumnMode"] = val

  @property
  def enablePivot(self):
    """
    Description:
    -----------
    """
    return self._attrs["enablePivot"]

  @enablePivot.setter
  def enablePivot(self, val):
    self._attrs["enablePivot"] = val

  @property
  def enableValue(self):
    """
    Description:
    -----------
    """
    return self._attrs["enableValue"]

  @enableValue.setter
  def enableValue(self, val):
    self._attrs["enableValue"] = val

  @property
  def enterMovesDown(self):
    """
    Description:
    -----------
    Set to true to have Enter key move focus to the cell below if not editing. The default is Enter key starts editing the currently focused cell.

    https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._attrs["enterMovesDown"]

  @enterMovesDown.setter
  def enterMovesDown(self, val):
    self._attrs["enterMovesDown"] = val

  @property
  def enterMovesDownAfterEdit(self):
    """
    Description:
    -----------
    Set to true to have Enter key move focus to the cell below after Enter is pressed while editing. The default is editing will stop and focus will remain on the editing cell.

    https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._attrs["enterMovesDownAfterEdit"]

  @enterMovesDownAfterEdit.setter
  def enterMovesDownAfterEdit(self, val):
    self._attrs["enterMovesDownAfterEdit"] = val

  @property
  def pagination(self):
    """
    Description:
    -----------
    To enable pagination in, set the grid property pagination=true.
    The following simple example shows this, the only difference to this and previous examples is the pagination=true property.

    https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._attrs["pagination"]

  @pagination.setter
  def pagination(self, val):
    self._attrs["pagination"] = val

  @property
  def paginationPageSize(self):
    """
    Description:
    -----------
    How many rows to load per page. If paginationAutoPageSize is specified, this property is ignored. See Customising Pagination.
    Default: 100

    https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._attrs.get("paginationPageSize", 100)

  @paginationPageSize.setter
  def paginationPageSize(self, val):
    self._attrs["paginationPageSize"] = val

  @property
  def paginationAutoPageSize(self):
    """
    Description:
    -----------
    If you set paginationAutoPageSize=true the grid will automatically show as many rows in each page as it can fit.
    This is demonstrated below. Note if you resize the display area of the grid, the page size automatically changes.
    To view this, open the example up in a new tab and resize your browser.

    https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._attrs["paginationAutoPageSize"]

  @paginationAutoPageSize.setter
  def paginationAutoPageSize(self, val):
    self._attrs["paginationAutoPageSize"] = val

  @property
  def groupSelectsChildren(self):
    """
    Description:
    -----------


    https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._attrs["groupSelectsChildren"]

  @groupSelectsChildren.setter
  def groupSelectsChildren(self, val):
    self._attrs["groupSelectsChildren "] = val

  @property
  def singleClickEdit(self):
    """
    Description:
    -----------
    To change the default so that a single-click starts editing, set the property gridOptions.singleClickEdit = true.
    This is useful when you want a cell to enter edit mode as soon as you click on it, similar to the experience you get when inside Excel.

    https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._attrs["singleClickEdit"]

  @singleClickEdit.setter
  def singleClickEdit(self, val):
    self._attrs["singleClickEdit "] = val

  @property
  def suppressClickEdit(self):
    """
    Description:
    -----------
    The grid configures a cellRenderer with a button to start editing.

    https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._attrs["suppressClickEdit"]

  @suppressClickEdit.setter
  def suppressClickEdit(self, val):
    self._attrs["suppressClickEdit "] = val

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
    return self._attrs["suppressPaginationPanel"]

  @suppressPaginationPanel.setter
  def suppressPaginationPanel(self, val):
    self._attrs["suppressPaginationPanel "] = val

  @property
  def suppressScrollOnNewData(self):
    """
    Description:
    -----------
    The example also sets property suppressScrollOnNewData=true, which tells the grid to NOT scroll to the top when the page changes.

    Related Pages:

			https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._attrs["suppressScrollOnNewData"]

  @suppressScrollOnNewData.setter
  def suppressScrollOnNewData(self, val):
    self._attrs["suppressScrollOnNewData "] = val

  @property
  def ensureDomOrder(self):
    """
    Description:
    -----------
    ensures the rows and columns in the DOM always appear in the same order as displayed in the grid.

    Related Pages:

			https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._attrs["ensureDomOrder"]

  @ensureDomOrder.setter
  def ensureDomOrder(self, val):
    self._attrs["ensureDomOrder "] = val

  @property
  def suppressColumnVirtualisation(self):
    """
    Description:
    -----------
    Ensures all columns are rendered, i.e. appears in the DOM.

    Related Pages:

			https://www.ag-grid.com/javascript-grid-accessibility/
    """
    return self._attrs["suppressColumnVirtualisation"]

  @suppressColumnVirtualisation.setter
  def suppressColumnVirtualisation(self, val):
    self._attrs["suppressColumnVirtualisation "] = val

  @property
  def suppressDragLeaveHidesColumns(self):
    """
    Description:
    -----------
    Column animations happen when you move a column. The default is for animations to be turned on.
    It is recommended that you leave the column move animations on unless your target platform (browser and hardware) is to slow to manage the animations.
    To turn OFF column animations, set the grid property suppressColumnMoveAnimation=true.

    Related Pages:

			https://www.ag-grid.com/javascript-grid-column-moving/
    """
    return self._attrs["suppressDragLeaveHidesColumns"]

  @suppressDragLeaveHidesColumns.setter
  def suppressDragLeaveHidesColumns(self, val):
    self._attrs["suppressDragLeaveHidesColumns "] = val

  @property
  def rowMultiSelectWithClick(self):
    """
    Description:
    -----------
    Set to true to allow multiple rows to be selected with clicks.
    For example, if you click to select one row and then click to select another row, the first row will stay selected as well.
    Clicking a selected row in this mode will deselect the row.
    This is useful for touch devices where Ctrl and Shift clicking is not an option.

    Related Pages:

			https://www.ag-grid.com/javascript-grid-selection/
    """
    return self._attrs["rowMultiSelectWithClick"]

  @rowMultiSelectWithClick.setter
  def rowMultiSelectWithClick(self, val):
    self._attrs["rowMultiSelectWithClick "] = val

  @property
  def rowDeselection(self):
    """
    Description:
    -----------
    Set to true to allow rows to be deselected if you hold down Ctrl and click the row.
    By default the grid disallows deselection of rows (i.e. once a row is selected, it remains selected until another row is selected in its place).

    Related Pages:

			https://www.ag-grid.com/javascript-grid-selection/
    """
    return self._attrs["rowDeselection"]

  @rowDeselection.setter
  def rowDeselection(self, val):
    self._attrs["rowDeselection "] = val

  @property
  def rowSelection(self):
    """
    Description:
    -----------
    Type of row selection, set to either 'single' or 'multiple' to enable selection.
    'single' will use single row selection, such that when you select a row, any previously selected row gets unselected.
    'multiple' allows multiple rows to be selected.

    Related Pages:

			https://www.ag-grid.com/javascript-grid-selection/
    """
    return self._attrs["rowSelection"]

  @rowSelection.setter
  def rowSelection(self, val):
    self._attrs["rowSelection "] = val

  @property
  def rowBuffer(self):
    """
    Description:
    -----------
    Sets the number of rows rendered outside of the scrollable viewable area.

    Related Pages:

			https://www.ag-grid.com/javascript-grid-accessibility/
    """
    return self._attrs["rowBuffer"]

  @rowBuffer.setter
  def rowBuffer(self, val):
    self._attrs["rowBuffer "] = val

  @property
  def suppressRowClickSelection(self):
    """
    Description:
    -----------
    If true, rows won't be selected when clicked. Use, for example, when you want checkbox selection, and don't want to also select the row when the row is clicked.

    Related Pages:

			https://www.ag-grid.com/javascript-grid-selection/
    """
    return self._attrs["suppressRowClickSelection"]

  @suppressRowClickSelection.setter
  def suppressRowClickSelection(self, val):
    self._attrs["suppressRowClickSelection "] = val

  @property
  def sortingOrder(self):
    """
    Description:
    -----------
    It is possible to override this behaviour by providing your own sortingOrder on either the gridOptions or the colDef.
    If defined both in colDef and gridOptions, the colDef will get preference, allowing you to defined a common default, and then tailoring per column.

    https://www.ag-grid.com/javascript-grid-sorting/
    """
    return self._attrs["sortingOrder"]

  @sortingOrder.setter
  def sortingOrder(self, val):
    self._attrs["sortingOrder"] = val

  @property
  def sideBar(self):
    """

    :return:
    """
    return self.sub_data("sideBar", TableSideBar)

  def statusBar(self):
    """

    :return:
    """
    return self.sub_data("statusBar", TableStatusBar)
