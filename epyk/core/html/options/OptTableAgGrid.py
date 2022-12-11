import logging

from typing import Union
from epyk.core.js import JsUtils
from epyk.core.html.options import Options
from epyk.core.html.options import Enums
from epyk.core.py import types as etypes


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

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/

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


    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._set_value(value=None)

  def sum(self):
    """


    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._set_value()


class ColType(Enums):

  def nonEditableColumn(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions
    """
    return self._set_value()

  def dateColumn(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions
    """
    return self._set_value()

  def numericColumn(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions
    """
    return self._set_value()

  def numberColumn(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions
    """
    return self._set_value()

  def medalColumn(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions
    """
    return self._set_value()

  def rightAligned(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions
    """
    return self._set_value()


class ColumnFilter(Enums):

  def true(self):
    return self._set_value(value='true', js_type=True)

  def false(self):
    return self._set_value(value='false', js_type=True)

  def agTextColumnFilter(self, **kwargs):
    """   A Text Filter for string comparisons.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-filtering/
    """
    if kwargs:
      self._set_value(value=kwargs, name="filterParams")
    return self._set_value()

  def agDateColumnFilter(self, **kwargs):
    """   A Date Filter for date comparisons.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-filter-date/
    """
    if kwargs:
      self._set_value(value=kwargs, name="filterParams")
    return self._set_value()

  def agNumberColumnFilter(self):
    """   A Number Filter for number comparisons.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-filtering/
    """
    return self._set_value()

  def agSetColumnFilter(self, filter_name):
    """   A Set Filter, influenced by how filters work in Microsoft Excel. This is an ag-Grid-Enterprise feature.

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
  def aggFunc(self):
    """   """
    return self._config_get()

  @aggFunc.setter
  def aggFunc(self, val: etypes.JS_DATA_TYPES):
    val = JsUtils.jsConvertData(val, None)
    self._config(val, js_type=True)

  @property
  def cellClassRules(self):
    """   Rules that return true will have the class applied the second time.
    Rules that return false will have the class removed second time.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/cell-styles/
    """
    return self._config_get()

  @cellClassRules.setter
  def cellClassRules(self, value: dict):
    self._config(value)

  @property
  def cellRenderers(self):
    """

    Related Pages:

      https://www.ag-grid.com/archive/27.1.0/javascript-data-grid/component-cell-renderer/
    """
    return self._config_sub_data("cellRenderer", CellRenderer)

  @property
  def cellRenderer(self):
    """   Change the cell rendering.

    Usage::

      c = table.get_column("city")
      c.cellRenderer = ''' function(param){
      return '<span><i class="far fa-comments"></i>Test '+ param.value +'</span>'} '''

    Related Pages:

      https://www.ag-grid.com/archive/27.1.0/javascript-data-grid/component-cell-renderer/
    """
    return self._config_get()

  @cellRenderer.setter
  def cellRenderer(self, value: str):
    self._config(value, js_type=True)

  @property
  def cellRendererParams(self):
    """   On top of the parameters provided by the grid, you can also provide your own parameters.
    This is useful if you want to 'configure' your Cell Renderer. For example, you might have a Cell
    Renderer for formatting currency but you need to provide what currency for your cell renderer to use.

    Related Pages:

      https://www.ag-grid.com/archive/27.1.0/javascript-data-grid/component-cell-renderer/
    """
    return self._config_get()

  @cellRendererParams.setter
  def cellRendererParams(self, values: dict):
    self._config(values)

  @property
  def cellStyle(self):
    """   Rules that return true will have the class applied the second time.
    Rules that return false will have the class removed second time.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/cell-styles/
    """
    return self._config_get()

  @cellStyle.setter
  def cellStyle(self, values: dict):
    self._config(values)

  @property
  def children(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-grid-grouping-headers/
    """
    return self._config_get()

  @children.setter
  def children(self, val):
    self._config(val)

  def add_children(self, attrs: dict):
    """ Integrated way to add children to the header definition.

    :param attrs: The different columns properties to set.
    """
    col = self._config_sub_data_enum("children", Column)
    col.update_config(attrs)
    return col

  @property
  def colId(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-grid-grouping-headers/
    """
    return self._config_get()

  @colId.setter
  def colId(self, val):
    self._config(val)

  @property
  def columnGroupShow(self):
    """   values closed, open.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-grouping-headers/
    """
    return self._config_get()

  @columnGroupShow.setter
  def columnGroupShow(self, val: str):
    self._config(val)

  @property
  def editor(self) -> CellEditor:
    """   Cell editing format

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return CellEditor(self, "cellEditor")

  @property
  def editable(self):
    """   """
    return self._config_get()

  @editable.setter
  def editable(self, val):
    self._config(val)

  @property
  def enableRowGroup(self):
    """   Allow every column to be grouped.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._config_get()

  @enableRowGroup.setter
  def enableRowGroup(self, val):
    self._config(val)

  @property
  def field(self):
    """   """
    return self._config_get()

  @field.setter
  def field(self, val: str):
    self._config(val)

  @property
  def filters(self) -> ColumnFilter:
    """   Set filtering on a column using the column definition property filter. The property can have one of the following
    values:

    Related Pages:

      https://www.ag-grid.com/javascript-grid-filtering/
    """
    return ColumnFilter(self, 'filter')

  @property
  def filterValueGetter(self):
    """   Function or expression. Gets the value for filtering purposes.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/value-getters/
    """
    return self._config_get()

  @filterValueGetter.setter
  def filterValueGetter(self, value: str):
    self._config(value, js_type=True)

  @property
  def groupId(self):
    """   """
    return self._config_get()

  @groupId.setter
  def groupId(self, val: str):
    self._config(val)

  @property
  def groupRowsSticky(self):
    """ To enable sticky groups, set the groupRowsSticky property to true.
    This behaviour applies to all row group levels.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/grouping-sticky-groups/
    """
    return self._config_get()

  @groupRowsSticky.setter
  def groupRowsSticky(self, flag: bool):
    self._config(flag)

  @property
  def groupDisplayType(self):
    """ To display each row group using group rows set groupDisplayType = 'groupRows' as shown below:

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/grouping-sticky-groups/
    """
    return self._config_get()

  @groupDisplayType.setter
  def groupDisplayType(self, val: str):
    self._config(val)

  @property
  def hide(self):
    """   True if the column is hidden, otherwise false.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-definitions/
    """
    return self._config_get()

  @hide.setter
  def hide(self, flag: bool):
    self._config(flag)

  @property
  def headerClass(self):
    """ Similarly to styling cells, the grid will use the result of headerClass
    from the column definition to style the grid headers.

    Related Pages:

      https://ag-grid.com/javascript-data-grid/excel-export-styles/#styling-headers
    """
    return self._config_get()

  @headerClass.setter
  def headerClass(self, val: str):
    self._config(val)

  @property
  def headerName(self):
    """ The name to render in the column header.
    If not specified and field is specified, the field name will be used as the header name.

    Related Pages:

      https://ag-grid.com/javascript-data-grid/column-properties/#reference-header
    """
    return self._config_get()

  @headerName.setter
  def headerName(self, val: str):
    self._config(val)

  @property
  def headerCheckboxSelection(self):
    """ If true or the callback returns true, a 'select all' checkbox will be put into the header.
    See Header Checkbox Selection.

    Related Pages:

      https://ag-grid.com/javascript-data-grid/column-properties/#reference-header
    """
    return self._config_get()

  @headerCheckboxSelection.setter
  def headerCheckboxSelection(self, flag: bool):
    self._config(flag)

  @property
  def headerTooltip(self):
    """ When we want to display a header tooltip, we set the headerTooltip config as a string,
    and that string will be displayed as the tooltip.

    Related Pages:

      https://ag-grid.com/javascript-data-grid/component-tooltip/#header-tooltip-with-custom-tooltip
    """
    return self._config_get()

  @headerTooltip.setter
  def headerTooltip(self, val: str):
    self._config(val)

  @property
  def headerValueGetter(self):
    """   Function or expression. Gets the value for display in the header.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/value-getters/
    """
    return self._config_get()

  @headerValueGetter.setter
  def headerValueGetter(self, value: str):
    self._config(value, js_type=True)

  @property
  def lockPinned(self):
    """   If you do not want the user to be able to pin using the UI, set the property lockPinned=true.
    This will block the UI in the following way:

    Related Pages:

      https://www.ag-grid.com/javascript-grid-pinning/
    """
    return self._config_get()

  @lockPinned.setter
  def lockPinned(self, flag: bool):
    self._config(flag)

  @property
  def marryChildren(self):
    """   Sometimes you want columns of the group to always stick together.
    To achieve this, set the column group property marryChildren=true. The example below demonstrates the following:

    """
    return self._config_get()

  @marryChildren.setter
  def marryChildren(self, val):
    self._config(val)

  @property
  def sortable(self):
    """   """
    return self._config_get()

  @sortable.setter
  def sortable(self, val):
    self._config(val)

  @property
  def suppressColumnsToolPanel(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example
    """
    return self._config_get()

  @suppressColumnsToolPanel.setter
  def suppressColumnsToolPanel(self, flag: bool):
    self._config(flag)

  @property
  def suppressMenu(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/component-floating-filter/
    """
    return self._config_get()

  @suppressMenu.setter
  def suppressMenu(self, flag: bool):
    self._config(flag)

  @property
  def floatingFilterComponent(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/component-floating-filter/
    """
    return self._config_get()

  @floatingFilterComponent.setter
  def floatingFilterComponent(self, data):
    self._config(data, js_type=True)

  @property
  def floatingFilterComponentParams(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/component-floating-filter/
    """
    return self._config_get()

  @floatingFilterComponentParams.setter
  def floatingFilterComponentParams(self, values: dict):
    self._config(values)

  @property
  def tooltipField(self):
    """

    https://www.ag-grid.com/javascript-data-grid/component-tooltip/
    """
    return self._config_get()

  @tooltipField.setter
  def tooltipField(self, val: str):
    self._config(val)

  @property
  def toolPanelClass(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example
    """
    return self._config_get()

  @toolPanelClass.setter
  def toolPanelClass(self, val: str):
    val = JsUtils.jsConvertData(val, None)
    self._config(val, js_type=True)

  @property
  def filter(self):
    """   """
    return self._config_get()

  @filter.setter
  def filter(self, val):
    self._config(val)

  @property
  def flex(self):
    """   It's often required that one or more columns fill the entire available space in the grid. For this scenario,
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
    """   """
    return self._config_get()

  @checkboxSelection.setter
  def checkboxSelection(self, val):
    self._config(val)

  @property
  def suppressMovable(self):
    """   The column property suppressMovable changes whether the column can be dragged.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-column-moving/
    """
    return self._config_get()

  @suppressMovable.setter
  def suppressMovable(self, val):
    self._config(val)

  @property
  def pinned(self):
    """   """
    return self._config_get()

  @pinned.setter
  def pinned(self, val: Union[str, bool]):
    self._config(val)

  @property
  def lockPosition(self):
    """   The column property lockPosition locks columns to the first position in the grid.

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
    """   """
    return self._config_get()

  @maxWidth.setter
  def maxWidth(self, val):
    self._config(val)

  @property
  def minWidth(self):
    """   """
    return self._config_get()

  @minWidth.setter
  def minWidth(self, val):
    self._config(val)

  @property
  def resizable(self):
    """   Turn column resizing on for the grid by setting resizable=true for each column.
    To set resizing for each column, set resizable=true on the default column definition.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._config_get()

  @resizable.setter
  def resizable(self, val):
    self._config(val)

  @property
  def rowDrag(self):
    """   """
    return self._config_get()

  @rowDrag.setter
  def rowDrag(self, val):
    self._config(val)

  @property
  def rowGroup(self):
    """   """
    return self._config_get()

  @rowGroup.setter
  def rowGroup(self, val):
    self._config(val)

  @property
  def rowGroupIndex(self):
    """   The index of the row group. If the column is not grouped, this field is null.
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
    """   """
    return self._config_get()

  @suppressSizeToFit.setter
  def suppressSizeToFit(self, val):
    self._config(val)

  @property
  def types(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions
    """
    return self._config_sub_data("type", ColType)

  @property
  def type(self):
    """   """
    return self._config_get()

  @type.setter
  def type(self, val: str):
    self._config(val)

  @property
  def enableCellChangeFlash(self):
    """

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

    Related Pages:

      https://www.ag-grid.com/javascript-grid-refresh/
    """
    return self._config_get()

  @suppressCellFlash.setter
  def suppressCellFlash(self, val):
    self._config(val)

  @property
  def sortingOrder(self):
    """   It is possible to override this behaviour by providing your own sortingOrder on either the gridOptions or the
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
    """   Cell editing format

    Related Pages:

      https://www.ag-grid.com/javascript-grid-sorting/
    """
    return ColOrder(self, 'sort')

  @property
  def title(self):
    """   """
    return self._config_get(name="headerName")

  @title.setter
  def title(self, val: str):
    self._config(val, name="headerName")

  @property
  def valueGetter(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions
    """
    return self._config_get()

  @valueGetter.setter
  def valueGetter(self, val: etypes.JS_DATA_TYPES):
    self._config(val, js_type=True)

  @property
  def valueSetter(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/value-setters/
    """
    return self._config_get()

  @valueSetter.setter
  def valueSetter(self, val: etypes.JS_DATA_TYPES):
    self._config(val, js_type=True)

  @property
  def valueFormatter(self):
    """ Value formatters allow you to format values for display. This is useful when data is one type (e.g. numeric)
    but needs to be converted for human reading (e.g. putting in currency symbols and number formatting).

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/value-formatters/
    """
    return self._config_get()

  @valueFormatter.setter
  def valueFormatter(self, val: str):
    self._config(val)

  @property
  def volatile(self):
    """   """
    return self._config_get()

  @volatile.setter
  def volatile(self, flag: bool):
    self._config(flag)

  @property
  def width(self):
    """   """
    return self._config_get()

  @width.setter
  def width(self, value: int):
    self._config(value)

  @property
  def wrapHeaderText(self):
    """  If enabled then column header names that are too long for the column width will wrap onto the next line.
    Default false

    Related Pages:

      https://ag-grid.com/javascript-data-grid/column-properties/#reference-header
    """
    return self._config_get(False)

  @wrapHeaderText.setter
  def wrapHeaderText(self, flag: bool):
    self._config(flag)


class DefaultColDef(Options):

  @property
  def filter(self):
    """   set a filter for every columns.
    """
    return self._config_get()

  @filter.setter
  def filter(self, val: str):
    self._config(val)

  @property
  def filters(self):
    """   Set filtering on a column using the column definition property filter. The property can have one of the following
    values:

    Related Pages:

      https://www.ag-grid.com/javascript-grid-filtering/
    """
    return ColumnFilter(self, 'filter')

  @property
  def flex(self):
    """   It's often required that one or more columns fill the entire available space in the grid. For this scenario,
    it is possible to use the flex config.
    Some columns could be set with a regular width config, while other columns would have a flex config.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._config_get()

  @flex.setter
  def flex(self, val: int):
    self._config(val)

  @property
  def floatingFilter(self):
    """   Floating Filter Components allow you to add your own floating filter types to AG Grid. You can create a Custom
    Floating Filter Component to work alongside one of the grid's Provided Filters, or alongside a Custom Filter.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/component-floating-filter/
    """
    return self._config_get()

  @floatingFilter.setter
  def floatingFilter(self, flag: bool):
    self._config(flag)

  @property
  def groupDefaultExpanded(self):
    """   To open all groups down to a given group level use the groupDefaultExpanded grid option as shown below:

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/grouping-opening-groups/#opening-group-levels-by-default
    """
    return self._config_get()

  @groupDefaultExpanded.setter
  def groupDefaultExpanded(self, val: int):
    if self.component.options.verbose and self.page.imports.pkgs.ag_grid.community_version:
      logging.warning("groupDefaultExpanded not available in the community version")
    self._config(val)

  @property
  def minWidth(self):
    """   """
    return self._config_get()

  @minWidth.setter
  def minWidth(self, val: int):
    self._config(val)

  @property
  def editable(self):
    """   make every column editable
    """
    return self._config_get()

  @editable.setter
  def editable(self, flag: bool):
    self._config(flag)

  @property
  def resizable(self):
    """   Turn column resizing on for the grid by setting resizable=true for each column.
    To set resizing for each column, set resizable=true on the default column definition.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-resizing/
    """
    return self._config_get()

  @resizable.setter
  def resizable(self, flag: bool):
    self._config(flag)

  @property
  def sortable(self):
    """   """
    return self._config_get()

  @sortable.setter
  def sortable(self, flag: bool):
    self._config(flag)

  @property
  def treeData(self):
    """

    Related Pages:

      https://www.ag-grid.com/documentation/javascript/tree-data/
    """
    return self._config_get()

  @treeData.setter
  def treeData(self, flag: bool):
    if self.component.options.verbose and self.page.imports.pkgs.ag_grid.community_version:
      logging.warning("treeData not available in the community version")

    self._config(flag)

  @property
  def width(self):
    """   set every column width.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions
    """
    return self._config_get()

  @width.setter
  def width(self, num: int):
    self._config(num)


class TableToolPanelsParams(Options):

  @property
  def suppressSyncLayoutWithGrid(self):
    """   """
    return self._config_get()

  @suppressSyncLayoutWithGrid.setter
  def suppressSyncLayoutWithGrid(self, val):
    self._config(val)


class TableToolPanelsFilters(Options):

  @property
  def id(self):
    """   """
    return self._config_get()

  @id.setter
  def id(self, val):
    self._config(val)

  @property
  def labelDefault(self):
    """   """
    return self._config_get()

  @labelDefault.setter
  def labelDefault(self, val):
    self._config(val)

  @property
  def labelKey(self):
    """   """
    return self._config_get()

  @labelKey.setter
  def labelKey(self, val):
    self._config(val)

  @property
  def iconKey(self):
    """   """
    return self._config_get()

  @iconKey.setter
  def iconKey(self, val):
    self._config(val)

  @property
  def toolPanel(self):
    """   """
    return self._config_get()

  @toolPanel.setter
  def toolPanel(self, val):
    self._config(val)

  def toolPanelParams(self):
    """

    """
    return self.has_attribute(TableToolPanelsParams)


class TableToolPanels(Options):

  def filters(self):
    """

    """
    return self.has_attribute(TableToolPanelsFilters)


class EnumStatusPanelsPanels(Options):
  @property
  def statusPanel(self):
    """   """
    return self._config_get()

  @statusPanel.setter
  def statusPanel(self, val):
    self._config(val)

  @property
  def align(self):
    """   """
    return self._config_get()

  @align.setter
  def align(self, val):
    self._config(val)

  @property
  def key(self):
    """   """
    return self._config_get()

  @key.setter
  def key(self, val):
    self._config(val)


class TableStatusBar(Options):

  def statusPanels(self) -> EnumStatusPanelsPanels:
    """   """
    return self._config_sub_data_enum('statusPanels', EnumStatusPanelsPanels)


class TableConfig(Options):
  _struct__schema = {"autoGroupColumnDef": {}, "defaultColDef": {}, "TableStatusBar": {}, "columns": []}

  @property
  def alignedGrids(self):
    """   To have one (the first) grid reflect column changes in another (the second), place the first grid's options in
    alignedGrids property of the second grids.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-aligned-grids/
    """
    return self._config_get()

  @alignedGrids.setter
  def alignedGrids(self, val):
    self._config(val)

  @property
  def allowContextMenuWithControlKey(self):
    """  If you always want the grid's context menu, even when Ctrl is pressed, then set
    allowContextMenuWithControlKey=true.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/context-menu/
    """
    return self._config_get()

  @allowContextMenuWithControlKey.setter
  def allowContextMenuWithControlKey(self, flag: bool):
    self._config(flag)

  @property
  def animateRows(self):
    """   Row animations occur after filtering, sorting, resizing height and expanding / collapsing a row group.
    Each of these animations is turned OFF by default. They are all turned on using the property animateRows=true.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/row-animation/
    """
    return self._config_get()

  @animateRows.setter
  def animateRows(self, flag: bool):
    self._config(flag)

  @property
  def autoGroupColumnDef(self) -> DefaultColDef:
    return self._config_sub_data("autoGroupColumnDef", DefaultColDef)

  @property
  def colResizeDefault(self):
    """   If you hold 'shift' while dragging the resize handle, the column will take space away from the column adjacent to
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
    """   Set the columnDefs with all the column properties.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-groups/#column-definitions-vs-column-group-definitions
    """
    return self._config_sub_data_enum("columnDefs", Column)

  @property
  def columnTypes(self):
    """   Define a column type (you can define as many as you like.
    Expect a valid Json object.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions
    """
    return self._config_get()

  @columnTypes.setter
  def columnTypes(self, data: str):
    self._config(data, js_type=True)

  @property
  def defaultColDef(self) -> DefaultColDef:
    """   contains properties that all columns will inherit.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#custom-column-types
    """
    return self._config_sub_data("defaultColDef", DefaultColDef)

  @property
  def data(self):
    """   Update the Row Data inside the grid by updating the rowData grid property or by calling the grid API
    setRowData().

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/data-update-row-data/
    """
    return self._config_get(name="rowData")

  @data.setter
  def data(self, val):
    self._config(val, name="rowData")

  @property
  def deltaColumnMode(self):
    """   """
    return self._config_get()

  @deltaColumnMode.setter
  def deltaColumnMode(self, val: str):
    self._config(val)

  @property
  def editType(self):
    """

    Related Pages:

    """
    return self._config_get()

  @editType.setter
  def editType(self, value: str):
    self._config(value)

  @property
  def enablePivot(self):
    """   Allow every column to be pivoted

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example
    """
    return self._config_get()

  @enablePivot.setter
  def enablePivot(self, flag: bool):
    self._config(flag)

  @property
  def enableRangeSelection(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/context-menu/
    """
    return self._config_get()

  @enableRangeSelection.setter
  def enableRangeSelection(self, flag: bool):
    self._config(flag)

  @property
  def enableValue(self):
    """   This means you can drag the columns to the values section, but you cannot drag them to the group or pivot
    sections.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example
    """
    return self._config_get()

  @enableValue.setter
  def enableValue(self, flag: bool):
    self._config(flag)

  @property
  def ensureDomOrder(self):
    """   ensures the rows and columns in the DOM always appear in the same order as displayed in the grid.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._config_get()

  @ensureDomOrder.setter
  def ensureDomOrder(self, val):
    self._config(val)

  @property
  def enterMovesDown(self):
    """   Set to true to have Enter key move focus to the cell below if not editing.
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
    """   Set to true to have Enter key move focus to the cell below after Enter is pressed while editing.
    The default is editing will stop and focus will remain on the editing cell.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._config_get()

  @enterMovesDownAfterEdit.setter
  def enterMovesDownAfterEdit(self, val):
    self._config(val)

  @property
  def functionsReadOnly(self):
    """   By setting the property functionsReadOnly=true, the grid will prevent changes to group, pivot or values
    through the GUI. This is useful if you want to show the user the group, pivot and values panel,
    so they can see which columns are used, but prevent them from making changes to the selection.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._config_get()

  @functionsReadOnly.setter
  def functionsReadOnly(self, flag: bool):
    self._config(flag)

  def getContextMenuItems(self):
    pass

  def getRowClass(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
    """ Callback version of property rowClass to set class(es) for each row individually.
    Function should return either a string (class name), array of strings (array of class names) or undefined
    for no class.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/row-styles/#reference-styling-getRowClass

    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(params)") and not func_ref:
      str_func = "function(params){%s}" % str_func
    self._config(str_func, js_type=True)

  @property
  def groupIncludeFooter(self):
    """  If you want to include a footer with each group, set the property groupIncludeFooter to true.
    It is also possible to include a 'grand' total footer for all groups using the property groupIncludeTotalFooter.

    Related Pages:

      https://www.ag-grid.com/archive/26.0.0/javascript-data-grid/grouping-footers/

    """
    return self._config_get()

  @groupIncludeFooter.setter
  def groupIncludeFooter(self, flag: bool):
    self._config(flag)

  @property
  def groupIncludeTotalFooter(self):
    """

    Related Pages:

      https://www.ag-grid.com/archive/26.0.0/javascript-data-grid/grouping-footers/

    """
    return self._config_get()

  @groupIncludeTotalFooter.setter
  def groupIncludeTotalFooter(self, flag: bool):
    self._config(flag)

  def isGroupOpenByDefault(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                           func_ref: bool = False):
    """

    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(param)") and not func_ref:
      str_func = "function(param){%s}" % str_func
    self._config(str_func, js_type=True)

  def onGridReady(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions

    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(param)") and not func_ref:
      str_func = "function(param){%s}" % str_func
    self._config(str_func, js_type=True)

  def on(self, event_type: str, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
         func_ref: bool = False):
    """

    Related Pages:

      https://ag-grid.com/angular-data-grid/grid-interface/

    :param event_type: The event type
    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(param)") and not func_ref:
      str_func = "function(param){%s}" % str_func
    if not event_type.startswith("on"):
      event_type = "on%s" % event_type.capitalize()
    self._config(str_func, name=event_type, js_type=True)

  def onCellEditingStopped(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                           func_ref: bool = False):
    """   Editing a cell has stopped.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/cell-editing/

    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(param)") and not func_ref:
      str_func = "function(param){%s}" % str_func
    self._config(str_func, js_type=True)

  def onCellValueChanged(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                         func_ref: bool = False):
    """   Value has changed after editing (this event will not fire if editing was cancelled, eg ESC was pressed) or
    if cell value has changed as a result of paste operation.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/cell-editing/

    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(param)") and not func_ref:
      str_func = "function(param){%s}" % str_func
    self._config(str_func, js_type=True)

  def onRowClicked(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                   func_ref: bool = False):
    """

    Related Pages:

      https://ag-grid.com/angular-data-grid/grid-interface/

    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(param)") and not func_ref:
      str_func = "function(param){%s}" % str_func
    self._config(str_func, js_type=True)

  def onColumnResized(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                      func_ref: bool = False):
    """

    Related Pages:

      https://ag-grid.com/angular-data-grid/grid-interface/

    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(param)") and not func_ref:
      str_func = "function(param){%s}" % str_func
    self._config(str_func, js_type=True)

  def onPaginationChanged(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                          func_ref: bool = False):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/row-pagination/

    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(param)") and not func_ref:
      str_func = "function(param){%s}" % str_func
    self._config(str_func, js_type=True)

  @property
  def overlayLoadingTemplate(self):
    """   Provide a plain HTML string to the grid properties overlayLoadingTemplate and overlayNoRowsTemplate.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/overlays/
    """
    return self._config_get()

  @overlayLoadingTemplate.setter
  def overlayLoadingTemplate(self, val: str):
    self._config(val)

  @property
  def overlayNoRowsTemplate(self):
    """   Provide a plain HTML string to the grid properties overlayLoadingTemplate and overlayNoRowsTemplate.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/overlays/
    """
    return self._config_get()

  @overlayNoRowsTemplate.setter
  def overlayNoRowsTemplate(self, val: str):
    self._config(val)

  @property
  def paginateChildRows(self):
    """   Set to true to have pages split children of groups when using Row Grouping or detail rows with Master Detail. See Pagination & Child Rows.
    Default: false

    Related Pages:

      hhttps://www.ag-grid.com/javascript-data-grid/row-pagination/
    """
    return self._config_get(False)

  @paginateChildRows.setter
  def paginateChildRows(self, flag: bool):
    self._config(flag)

  @property
  def pagination(self):
    """   To enable pagination in, set the grid property pagination=true.
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
    """   How many rows to load per page. If paginationAutoPageSize is specified, this property is ignored.
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
    """   If you set paginationAutoPageSize=true the grid will automatically show as many rows in each page as it can fit.
    This is demonstrated below. Note if you resize the display area of the grid, the page size automatically changes.
    To view this, open the example up in a new tab and resize your browser.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._config_get()

  @paginationAutoPageSize.setter
  def paginationAutoPageSize(self, num: int):
    self._config(num)

  def paginationNumberFormatter(self):
    """   Allows user to format the numbers in the pagination panel, i.e. 'row count' and 'page number' labels.
    This is for pagination panel only, to format numbers inside the grid's cells (i.e. your data),
    then use valueFormatter in the column definitions.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/row-pagination/
    """
    pass

  @property
  def popupParent(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/csv-export/
    """
    return self._config_get()

  @popupParent.setter
  def popupParent(self, data: str):
    self._config(data, js_type=True)

  @property
  def pivotMode(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example
    """
    return self._config_get()

  @pivotMode.setter
  def pivotMode(self, flag: bool):
    self._config(flag)

  @property
  def pivotPanelShow(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example
    """
    return self._config_get()

  @pivotPanelShow.setter
  def pivotPanelShow(self, val: str):
    self._config(val)

  @property
  def groupSelectsChildren(self):
    """   Filler groups do not keep their selection state should the filler group be moved.
    For example if you have groups A->B->C, where C is the only row provided
    (so the grid creates groups A and B for you), and then you change the patch to D->B->C,
    group B will not keep it's selection.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/tree-data/#example-selecting-groups-and-children
    """
    return self._config_get()

  @groupSelectsChildren.setter
  def groupSelectsChildren(self, flag: bool):
    self._config(flag)

  @property
  def rowClass(self):
    """ The style properties to apply to all rows. Set to an object of key (style names) and values (style values).

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/row-styles/
    """
    return self._config_get(None)

  @rowClass.setter
  def rowClass(self, values: Union[str, list]):
    self._config(values)

  @property
  def rowClassRules(self):
    """ The following snippet shows rowClassRules applying classes to rows using expressions on an age column value:

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/row-styles/
    """
    return self._config_get(None)

  @rowClassRules.setter
  def rowClassRules(self, values: Union[str, dict]):
    self._config(values)

  @property
  def rowHeight(self):
    """   By default, the grid will display rows with a height of 25px. You can change this for each row individually
    to give each row a different height.

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/row-height/
    """
    return self._config_get(25)

  @rowHeight.setter
  def rowHeight(self, num: int):
    self._config(int(num))

  @property
  def rowStyle(self):
    """  Property to set style for all rows. Set to an object of key (style names) and values (style values).

    Related Pages:

      http://54.222.217.254/javascript-grid-row-styles/#row-style
    """
    return self._config_get(None)

  @rowStyle.setter
  def rowStyle(self, values: Union[dict, str]):
    self._config(values)

  @property
  def singleClickEdit(self):
    """   To change the default so that a single-click starts editing, set the property gridOptions.singleClickEdit = true.
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
    """   The grid configures a cellRenderer with a button to start editing.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-cell-editing/
    """
    return self._config_get()

  @suppressClickEdit.setter
  def suppressClickEdit(self, val):
    self._config(val)

  @property
  def suppressPaginationPanel(self):
    """   If you set suppressPaginationPanel=true, the grid will not show the standard navigation controls for pagination.
    This is useful is you want to provide your own navigation controls.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._config_get(False)

  @suppressPaginationPanel.setter
  def suppressPaginationPanel(self, flag: bool):
    self._config(flag)

  @property
  def suppressScrollOnNewData(self):
    """   The example also sets property suppressScrollOnNewData=true, which tells the grid to NOT scroll to the top when the
    page changes.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-pagination/
    """
    return self._config_get()

  @suppressScrollOnNewData.setter
  def suppressScrollOnNewData(self, val):
    self._config(val)

  @property
  def suppressColumnVirtualisation(self):
    """   Ensures all columns are rendered, i.e. appears in the DOM.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-accessibility/
    """
    return self._config_get()

  @suppressColumnVirtualisation.setter
  def suppressColumnVirtualisation(self, val):
    self._config(val)

  @property
  def suppressDragLeaveHidesColumns(self):
    """   Column animations happen when you move a column. The default is for animations to be turned on.
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
  def suppressExcelExport(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/csv-export/
    """
    return self._config_get()

  @suppressExcelExport.setter
  def suppressExcelExport(self, flag: bool):
    self._config(flag)

  @property
  def rowMultiSelectWithClick(self):
    """   Set to true to allow multiple rows to be selected with clicks.
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
    """   Set to true to allow rows to be deselected if you hold down Ctrl and click the row.
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
    """   Type of row selection, set to either 'single' or 'multiple' to enable selection.
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
    """   Sets the number of rows rendered outside of the scrollable viewable area.

    Related Pages:

      https://www.ag-grid.com/javascript-grid-accessibility/
    """
    return self._config_get()

  @rowBuffer.setter
  def rowBuffer(self, val):
    self._config(val)

  @property
  def rowGroupPanelShow(self):
    """

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example
    """
    return self._config_get()

  @rowGroupPanelShow.setter
  def rowGroupPanelShow(self, val: str):
    if self.component.options.verbose and self.page.imports.pkgs.ag_grid.community_version:
      logging.warning("rowGroupPanelShow not available in the community version")
    self._config(val)

  @property
  def rowTotal(self):
    """ Predefined way to add a row total attached to the table.
    """
    return self._config_get(False)

  @rowTotal.setter
  def rowTotal(self, flag: bool):
    self._config(flag)

  @property
  def suppressRowClickSelection(self):
    """   If true, rows won't be selected when clicked. Use, for example, when you want checkbox selection, and don't want to
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
    """   It is possible to override this behaviour by providing your own sortingOrder on either the gridOptions or the
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
  def sideBar(self):
    """

    """
    return self._config_get()

  @sideBar.setter
  def sideBar(self, val: Union[str, dict]):
    self._config(val)

  @property
  def sideBars(self):
    return EnumSidebar(self, "sideBar")

  def statusBar(self) -> TableStatusBar:
    """

    """
    return self._config_sub_data("statusBar", TableStatusBar)

  @property
  def valueCache(self):
    """ Set to true to turn on the value cache.
    Default: false

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/value-getters/
    """
    return self._config_get(False)

  @valueCache.setter
  def valueCache(self, flag: bool):
    self._config(flag)

  @property
  def valueCacheNeverExpires(self):
    """ Set to true to configure the value cache to not expire after data updates.
    Default: false

    Related Pages:

      https://www.ag-grid.com/javascript-data-grid/value-getters/
    """
    return self._config_get(False)

  @valueCacheNeverExpires.setter
  def valueCacheNeverExpires(self, flag: bool):
    self._config(flag)