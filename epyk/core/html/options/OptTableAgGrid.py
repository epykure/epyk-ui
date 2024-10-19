import logging

from typing import Union, List
from epyk.core.js import JsUtils
from epyk.core.html.options import Options, OptionsWithTemplates
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
        `Related Pages <https://www.ag-grid.com/javascript-grid-cell-editing/>`_

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
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-definitions/>`_
        """
        return self._set_value(value=None)

    def sum(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-grid-column-definitions/>`_
        """
        return self._set_value()


class ColType(Enums):

    def nonEditableColumn(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_
        """
        return self._set_value()

    def dateColumn(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_
        """
        return self._set_value()

    def numericColumn(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_
        """
        return self._set_value()

    def numberColumn(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_
        """
        return self._set_value()

    def medalColumn(self):
        """

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_
        """
        return self._set_value()

    def rightAligned(self):
        """

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_
        """
        return self._set_value()


class ColumnFilter(Enums):

    def true(self):
        return self._set_value(value='true', js_type=True)

    def false(self):
        return self._set_value(value='false', js_type=True)

    def agTextColumnFilter(self, **kwargs):
        """A Text Filter for string comparisons.

        `Related Pages <https://www.ag-grid.com/javascript-grid-filtering/>`_
        """
        if kwargs:
            self._set_value(value=kwargs, name="filterParams")
        return self._set_value()

    def agDateColumnFilter(self, **kwargs):
        """A Date Filter for date comparisons.

        `Related Pages <https://www.ag-grid.com/javascript-grid-filter-date/>`_
        """
        if kwargs:
            self._set_value(value=kwargs, name="filterParams")
        return self._set_value()

    def agNumberColumnFilter(self):
        """A Number Filter for number comparisons.

        `Related Pages <https://www.ag-grid.com/javascript-grid-filtering/>`_
        """
        return self._set_value()

    def agSetColumnFilter(self, filter_name):
        """A Set Filter, influenced by how filters work in Microsoft Excel. This is an ag-Grid-Enterprise feature.

        `Related Pages <https://www.ag-grid.com/javascript-grid-filter-component/>`_
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
        """Rules that return true will have the class applied the second time.
        Rules that return false will have the class removed second time.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/cell-styles/>`_
        """
        return self._config_get()

    @cellClassRules.setter
    def cellClassRules(self, value: dict):
        self._config(value)

    @property
    def cellEditor(self):
        return self._config_get()

    @cellEditor.setter
    def cellEditor(self, value: dict):
        self._config(value)

    @property
    def cellEditorPopup(self):
        return self._config_get()

    @cellEditorPopup.setter
    def cellEditorPopup(self, flag: bool):
        self._config(flag)

    @property
    def cellEditorParams(self):
        return self._config_get()

    @cellEditorParams.setter
    def cellEditorParams(self, values: dict):
        self._config(values)

    @property
    def cellRenderers(self) -> CellRenderer:
        """
        `Related Pages <https://www.ag-grid.com/archive/27.1.0/javascript-data-grid/component-cell-renderer/>`_
        """
        return CellRenderer(self, "cellRenderer")

    @property
    def cellRenderer(self):
        """Change the cell rendering.

        Usage::

          c = table.get_column("city")
          c.cellRenderer = ''' function(param){
          return '<span><i class="far fa-comments"></i>Test '+ param.value +'</span>'} '''

        `Related Pages <https://www.ag-grid.com/archive/27.1.0/javascript-data-grid/component-cell-renderer/>`_
        """
        return self._config_get()

    @cellRenderer.setter
    def cellRenderer(self, value: str):
        self._config(value, js_type=True)

    @property
    def cellRendererParams(self):
        """On top of the parameters provided by the grid, you can also provide your own parameters.
        This is useful if you want to 'configure' your Cell Renderer. For example, you might have a Cell
        Renderer for formatting currency but you need to provide what currency for your cell renderer to use.

        `Related Pages <https://www.ag-grid.com/archive/27.1.0/javascript-data-grid/component-cell-renderer/>`_
        """
        return self._config_get()

    @cellRendererParams.setter
    def cellRendererParams(self, values: dict):
        if not isinstance(values, dict):
            self._config(values, js_type=True)
        else:
            self._config(values, js_type=False)

    @property
    def cellStyle(self):
        """Rules that return true will have the class applied the second time.
        Rules that return false will have the class removed second time.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/cell-styles/>`_
        """
        return self._config_get()

    @cellStyle.setter
    def cellStyle(self, values: dict):
        if not isinstance(values, dict):
            self._config(values, js_type=True)
        else:
            self._config(values, js_type=False)

    @property
    def children(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-grid-grouping-headers/>`_
        """
        return self._config_get()

    @children.setter
    def children(self, val):
        self._config(val)

    def add_children(self, attrs: dict):
        """Integrated way to add children to the header definition.

        :param attrs: The different columns properties to set.
        """
        col = self._config_sub_data_enum("children", Column)
        col.update_config(attrs)
        return col

    @property
    def colId(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-grid-grouping-headers/>`_
        """
        return self._config_get()

    @colId.setter
    def colId(self, val: str):
        self._config(val)

    @property
    def columnGroupShow(self):
        """values closed, open.

        `Related Pages <https://www.ag-grid.com/javascript-grid-grouping-headers/>`_
        """
        return self._config_get()

    @columnGroupShow.setter
    def columnGroupShow(self, val: str):
        self._config(val)

    @property
    def editor(self) -> CellEditor:
        """Cell editing format

        `Related Pages <https://www.ag-grid.com/javascript-grid-cell-editing/>`_
        """
        return CellEditor(self, "cellEditor")

    @property
    def editable(self):
        """   """
        return self._config_get()

    @editable.setter
    def editable(self, val: bool):
        self._config(val)

    @property
    def enableRowGroup(self):
        """Allow every column to be grouped.

        `Related Pages <https://www.ag-grid.com/javascript-grid-column-definitions/>`_
        """
        return self._config_get()

    @enableRowGroup.setter
    def enableRowGroup(self, val: bool):
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
        """Set filtering on a column using the column definition property filter. The property can have one of the
        following values:

        `Related Pages <https://www.ag-grid.com/javascript-grid-filtering/>`_
        """
        return ColumnFilter(self, 'filter')

    @property
    def filterValueGetter(self):
        """Function or expression. Gets the value for filtering purposes.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/value-getters/>`_
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
        """To enable sticky groups, set the groupRowsSticky property to true.
        This behaviour applies to all row group levels.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grouping-sticky-groups/>`_
        """
        return self._config_get()

    @groupRowsSticky.setter
    def groupRowsSticky(self, flag: bool):
        self._config(flag)

    @property
    def groupDisplayType(self):
        """To display each row group using group rows set groupDisplayType = 'groupRows' as shown below:

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grouping-sticky-groups/>`_
        """
        return self._config_get()

    @groupDisplayType.setter
    def groupDisplayType(self, val: str):
        self._config(val)

    @property
    def hide(self) -> bool:
        """True if the column is hidden, otherwise false.

        `Related Pages <https://www.ag-grid.com/javascript-grid-column-definitions/>`_
        """
        return self._config_get()

    @hide.setter
    def hide(self, flag: bool):
        self._config(flag)

    @property
    def headerClass(self):
        """Similarly to styling cells, the grid will use the result of headerClass
        from the column definition to style the grid headers.

        `Related Pages <https://ag-grid.com/javascript-data-grid/excel-export-styles/#styling-headers>`_
        """
        return self._config_get()

    @headerClass.setter
    def headerClass(self, val: str):
        self._config(val)

    @property
    def headerName(self):
        """The name to render in the column header.
        If not specified and field is specified, the field name will be used as the header name.

        `Related Pages <https://ag-grid.com/javascript-data-grid/column-properties/#reference-header>`_
        """
        return self._config_get()

    @headerName.setter
    def headerName(self, val: str):
        self._config(val)

    @property
    def headerCheckboxSelection(self) -> bool:
        """If true or the callback returns true, a 'select all' checkbox will be put into the header.
        See Header Checkbox Selection.

        `Related Pages <https://ag-grid.com/javascript-data-grid/column-properties/#reference-header>`_
        """
        return self._config_get()

    @headerCheckboxSelection.setter
    def headerCheckboxSelection(self, flag: bool):
        self._config(flag)

    @property
    def headerCheckboxSelectionCurrentPageOnly(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-selection/>`_
        """
        return self._config_get()

    @headerCheckboxSelectionCurrentPageOnly.setter
    def headerCheckboxSelectionCurrentPageOnly(self, flag: bool):
        self._config(flag)

    @property
    def headerTooltip(self):
        """When we want to display a header tooltip, we set the headerTooltip config as a string,
        and that string will be displayed as the tooltip.

        `Related Pages <https://ag-grid.com/javascript-data-grid/component-tooltip/#header-tooltip-with-custom-tooltip>`_
        """
        return self._config_get()

    @headerTooltip.setter
    def headerTooltip(self, val: str):
        self._config(val)

    @property
    def headerValueGetter(self):
        """Function or expression. Gets the value for display in the header.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/value-getters/>`_
        """
        return self._config_get()

    @headerValueGetter.setter
    def headerValueGetter(self, value: str):
        self._config(value, js_type=True)

    @property
    def lockPinned(self):
        """If you do not want the user to be able to pin using the UI, set the property lockPinned=true.
        This will block the UI in the following way:

        `Related Pages <https://www.ag-grid.com/javascript-grid-pinning/>`_
        """
        return self._config_get()

    @lockPinned.setter
    def lockPinned(self, flag: bool):
        self._config(flag)

    @property
    def marryChildren(self):
        """Sometimes you want columns of the group to always stick together.
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
    def sortable(self, val: bool):
        self._config(val)

    @property
    def suppressColumnsToolPanel(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example>`_
        """
        return self._config_get()

    @suppressColumnsToolPanel.setter
    def suppressColumnsToolPanel(self, flag: bool):
        self._config(flag)

    @property
    def suppressMenu(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/component-floating-filter/>`_
        """
        return self._config_get()

    @suppressMenu.setter
    def suppressMenu(self, flag: bool):
        self._config(flag)

    @property
    def floatingFilterComponent(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/component-floating-filter/>`_
        """
        return self._config_get()

    @floatingFilterComponent.setter
    def floatingFilterComponent(self, data):
        self._config(data, js_type=True)

    @property
    def floatingFilterComponentParams(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/component-floating-filter/>`_
        """
        return self._config_get()

    @floatingFilterComponentParams.setter
    def floatingFilterComponentParams(self, values: dict):
        self._config(values)

    @property
    def tooltipField(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/component-tooltip/>`_
        """
        return self._config_get()

    @tooltipField.setter
    def tooltipField(self, val: str):
        self._config(val)

    @property
    def toolPanelClass(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example>`_
        """
        return self._config_get()

    @toolPanelClass.setter
    def toolPanelClass(self, val: str):
        val = JsUtils.jsConvertData(val, None)
        self._config(val, js_type=True)

    @property
    def type(self):
        """Use columnTypes to define a set of Column properties to be applied together. The properties in a column
        type are applied to a Column by setting its type property.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#column-types>`_
        """
        return self._config_get()

    @type.setter
    def type(self, val: str):
        self._config(val)

    @property
    def filter(self):
        """   """
        return self._config_get()

    @filter.setter
    def filter(self, val):
        self._config(val)

    @property
    def filterParams(self):
        """   """
        return self._config_get()

    @filterParams.setter
    def filterParams(self, values: dict):
        self._config(values)

    @property
    def flex(self):
        """It's often required that one or more columns fill the entire available space in the grid. For this scenario,
        it is possible to use the flex config.
        Some columns could be set with a regular width config, while other columns would have a flex config.

        `Related Pages <https://www.ag-grid.com/javascript-grid-resizing/>`_
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
        """The column property suppressMovable changes whether the column can be dragged.

        `Related Pages <https://www.ag-grid.com/javascript-grid-column-moving/>`_
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
        """The column property lockPosition locks columns to the first position in the grid.

        `Related Pages <https://www.ag-grid.com/javascript-grid-column-moving/>`_
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
        """Turn column resizing on for the grid by setting resizable=true for each column.
        To set resizing for each column, set resizable=true on the default column definition.

        `Related Pages <https://www.ag-grid.com/javascript-grid-resizing/>`_
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
        """The index of the row group. If the column is not grouped, this field is null.
        If multiple columns are used to group, this index provides the order of the grouping.

        `Related Pages <https://www.ag-grid.com/javascript-grid-column-definitions/>`_
        """
        return self._config_get()

    @rowGroupIndex.setter
    def rowGroupIndex(self, val):
        self._config(val)

    @property
    def rowSpan(self):
        """By default, each cell will take up the height of one row. You can change this behaviour to allow cells to
        span multiple rows. This feature is similar to 'cell merging' in Excel or 'row spanning' in HTML tables.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-spanning/>`_
        """
        return self._config_get()

    @rowSpan.setter
    def rowSpan(self, val: Union[str, int]):
        self._config(val)

    def rowSpanFunc(self, data: etypes.JS_DATA_TYPES):
        """Set a rowSpan function. This can be a callback function or even a string pointing to a
        JavaScript function.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-spanning/>`_

        :param data: JavaScript expression
        """
        self._config(data, name="rowSpan", js_type=True)

    @property
    def suppressSizeToFit(self):
        """If you don't want a particular column to be included in the auto resize, then set the column definition
        suppressSizeToFit=true. This is helpful if, for example, you want the first column to remain fixed width,
        but all other columns to fill the width of the table.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-sizing/
        """
        return self._config_get()

    @suppressSizeToFit.setter
    def suppressSizeToFit(self, flag: bool):
        self._config(flag)

    @property
    def types(self) -> ColType:
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_
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
        """The grid can flash cells to highlight data changes. This is a great visual indicator to users of the grid who
        want data changes to be noticed.

        `Related Pages <https://www.ag-grid.com/javascript-grid-refresh/>`_
        `Related Pages <https://www.ag-grid.com/angular-data-grid/flashing-cells/>`_
        """
        return self._config_get()

    @enableCellChangeFlash.setter
    def enableCellChangeFlash(self, flag: bool):
        self._config(flag)

    @property
    def suppressCellFlash(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-grid-refresh/>`_
        """
        return self._config_get()

    @suppressCellFlash.setter
    def suppressCellFlash(self, val):
        self._config(val)

    @property
    def sortingOrder(self):
        """It is possible to override this behaviour by providing your own sortingOrder on either the gridOptions or the
        colDef.
        If defined both in colDef and gridOptions, the colDef will get preference, allowing you to defined a common
        default, and then tailoring per column.

        `Related Pages <https://www.ag-grid.com/javascript-grid-sorting/>`_
        """
        return self._config_get()

    @sortingOrder.setter
    def sortingOrder(self, val):
        self._config(val)

    @property
    def sorts(self):
        """
        Cell editing format

        `Related Pages <https://www.ag-grid.com/javascript-grid-sorting/>`_
        """
        return ColOrder(self, 'sort')

    @property
    def comparator(self):
        """Custom sorting is provided at a column level by configuring a comparator on the column definition.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-sorting/>`_
        """
        return self._config_get()

    @comparator.setter
    def comparator(self, val: str):
        self._config(val)

    @property
    def showDisabledCheckboxes(self):
        """
        `Related Pages <https://ag-grid.com/javascript-data-grid/row-selection//>`_
        """
        return self._config_get()

    @showDisabledCheckboxes.setter
    def showDisabledCheckboxes(self, val):
        self._config(val)

    @property
    def sort(self):
        """Custom sorting is provided at a column level.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-sorting/>`_
        """
        return self._config_get()

    @sort.setter
    def sort(self, val: str):
        self._config(val)

    @property
    def unSortIcon(self):
        """Custom sorting is provided at a column level.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-sorting/>`_
        """
        return self._config_get()

    @unSortIcon.setter
    def unSortIcon(self, flag: bool):
        self._config(flag)

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
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_
        """
        return self._config_get()

    @valueGetter.setter
    def valueGetter(self, val: etypes.JS_DATA_TYPES):
        self._config(val, js_type=True)

    @property
    def valueSetter(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/value-setters/>`_
        """
        return self._config_get()

    @valueSetter.setter
    def valueSetter(self, val: etypes.JS_DATA_TYPES):
        self._config(val, js_type=True)

    @property
    def valueFormatter(self):
        """Value formatters allow you to format values for display. This is useful when data is one type (e.g. numeric)
        but needs to be converted for human reading (e.g. putting in currency symbols and number formatting).

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/value-formatters/>`_
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
        """If enabled then column header names that are too long for the column width will wrap onto the next line.
        Default false

        `Related Pages <https://ag-grid.com/javascript-data-grid/column-properties/#reference-header>`_
        """
        return self._config_get(False)

    @wrapHeaderText.setter
    def wrapHeaderText(self, flag: bool):
        self._config(flag)


class CellRendererParams(Options):

    @property
    def checkbox(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tree-data/>`_
        """
        return self._config_get()

    @checkbox.setter
    def checkbox(self, flag: bool):
        self._config(flag)

    @property
    def suppressCount(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tree-data/>`_
        """
        return self._config_get()

    @suppressCount.setter
    def suppressCount(self, flag: bool):
        self._config(flag)

    def innerRenderer(self, js_func: etypes.JS_DATA_TYPES):
        self._config(js_func, "innerRenderer", js_type=True)


class DefaultColDef(Options):

    @property
    def cellRenderers(self) -> CellRenderer:
        """
        `Related Pages <https://www.ag-grid.com/archive/27.1.0/javascript-data-grid/component-cell-renderer/>`_
        """
        return CellRenderer(self, "cellRenderer")

    @property
    def cellRenderer(self):
        """Change the cell rendering.

        Usage::

          c = table.get_column("city")
          c.cellRenderer = ''' function(param){
          return '<span><i class="far fa-comments"></i>Test '+ param.value +'</span>'} '''

        `Related Pages <https://www.ag-grid.com/archive/27.1.0/javascript-data-grid/component-cell-renderer/>`_
        """
        return self._config_get()

    @cellRenderer.setter
    def cellRenderer(self, value: str):
        self._config(value, js_type=True)

    @property
    def cellRendererParams(self) -> CellRendererParams:
        """ """
        return self._config_sub_data("cellRendererParams", CellRendererParams)

    @property
    def cellStyle(self) -> dict:
        """Use defaultColDef to set properties across ALL Columns."""
        return self._config_get()

    @cellStyle.setter
    def cellStyle(self, values: dict):
        self._config(values)

    @property
    def enablePivot(self) -> bool:
        """"""
        return self._config_get()

    @enablePivot.setter
    def enablePivot(self, val: bool):
        self._config(val)

    @property
    def enableRowGroup(self) -> bool:
        """"""
        return self._config_get()

    @enableRowGroup.setter
    def enableRowGroup(self, val: bool):
        self._config(val)

    @property
    def enableValue(self) -> bool:
        """"""
        return self._config_get()

    @enableValue.setter
    def enableValue(self, val: bool):
        self._config(val)

    @property
    def filter(self):
        """  set a filter for every columns. """
        return self._config_get()

    @filter.setter
    def filter(self, val: str):
        self._config(val)

    @property
    def filters(self):
        """Set filtering on a column using the column definition property filter. The property can have one of the
        following values:

        `Related Pages <https://www.ag-grid.com/javascript-grid-filtering/>`_
        """
        return ColumnFilter(self, 'filter')

    @property
    def filterParams(self):
        """  set a filter for every columns. """
        return self._config_get()

    @filterParams.setter
    def filterParams(self, values: dict):
        self._config(values)

    @property
    def field(self):
        """

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/component-floating-filter/
        """
        return self._config_get()

    @field.setter
    def field(self, name: str):
        self._config(name)

    @property
    def flex(self):
        """It's often required that one or more columns fill the entire available space in the grid. For this scenario,
        it is possible to use the flex config.
        Some columns could be set with a regular width config, while other columns would have a flex config.

        `Related Pages <https://www.ag-grid.com/javascript-grid-resizing/>`_
        """
        return self._config_get()

    @flex.setter
    def flex(self, val: int):
        self._config(val)

    @property
    def floatingFilter(self):
        """Floating Filter Components allow you to add your own floating filter types to AG Grid. You can create a Custom
        Floating Filter Component to work alongside one of the grid's Provided Filters, or alongside a Custom Filter.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/component-floating-filter/>`_
        """
        return self._config_get()

    @floatingFilter.setter
    def floatingFilter(self, flag: bool):
        self._config(flag)

    @property
    def groupDefaultExpanded(self):
        """To open all groups down to a given group level use the groupDefaultExpanded grid option as shown below:

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grouping-opening-groups/#opening-group-levels-by-default>`_
        """
        return self._config_get()

    @groupDefaultExpanded.setter
    def groupDefaultExpanded(self, val: int):
        if self.component.options.verbose and self.page.imports.pkgs.ag_grid.community_version:
            logging.warning("groupDefaultExpanded not available in the community version")
        self._config(val)

    @property
    def headerName(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/component-floating-filter/>`_
        """
        return self._config_get()

    @headerName.setter
    def headerName(self, name: str):
        self._config(name)

    @property
    def minWidth(self):
        """   """
        return self._config_get()

    @minWidth.setter
    def minWidth(self, val: int):
        self._config(val)

    @property
    def editable(self):
        """ make every column editable """
        return self._config_get()

    @editable.setter
    def editable(self, flag: bool):
        self._config(flag)

    @property
    def resizable(self):
        """Turn column resizing on for the grid by setting resizable=true for each column.
        To set resizing for each column, set resizable=true on the default column definition.

        `Related Pages <https://www.ag-grid.com/javascript-grid-resizing/>`_
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
    def suppressMovable(self):
        """The column property suppressMovable changes whether the column can be dragged.

        `Related Pages <https://www.ag-grid.com/javascript-grid-column-moving/>`_
        """
        return self._config_get()

    @suppressMovable.setter
    def suppressMovable(self, flag: bool):
        self._config(flag)

    @property
    def treeData(self):
        """
        `Related Pages <https://www.ag-grid.com/documentation/javascript/tree-data/>`_
        """
        return self._config_get()

    @treeData.setter
    def treeData(self, flag: bool):
        if self.component.options.verbose and self.page.imports.pkgs.ag_grid.community_version:
            logging.warning("treeData not available in the community version")

        self._config(flag)

    @property
    def width(self):
        """set every column width.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_
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
        """ """
        return self.has_attribute(TableToolPanelsParams)


class TableToolPanels(Options):

    def filters(self):
        """ """
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
    def statusPanelParams(self) -> dict:
        """

        `Doc <https://www.ag-grid.com/javascript-data-grid/status-bar/>`_
        """
        return self._config_get()

    @statusPanelParams.setter
    def statusPanelParams(self, values: dict):
        self._config(values)

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


class TableConfig(OptionsWithTemplates):
    _struct__schema = {"autoGroupColumnDef": {}, "defaultColDef": {}, "TableStatusBar": {}, "columns": []}

    @property
    def alignedGrids(self):
        """
        To have one (the first) grid reflect column changes in another (the second), place the first grid's options in
        alignedGrids property of the second grids.

        `Related Pages <https://www.ag-grid.com/javascript-grid-aligned-grids/>`_
        """
        return self._config_get()

    @alignedGrids.setter
    def alignedGrids(self, val):
        self._config(val)

    @property
    def allowContextMenuWithControlKey(self):
        """
        If you always want the grid's context menu, even when Ctrl is pressed, then set
        allowContextMenuWithControlKey=true.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/context-menu/>`_
        """
        return self._config_get()

    @allowContextMenuWithControlKey.setter
    def allowContextMenuWithControlKey(self, flag: bool):
        self._config(flag)

    @property
    def animateRows(self):
        """
        Row animations occur after filtering, sorting, resizing height and expanding / collapsing a row group.
        Each of these animations is turned OFF by default. They are all turned on using the property animateRows=true.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-animation/>`_
        """
        return self._config_get()

    @animateRows.setter
    def animateRows(self, flag: bool):
        self._config(flag)

    @property
    def autoGroupColumnDef(self) -> DefaultColDef:
        return self._config_sub_data("autoGroupColumnDef", DefaultColDef)

    @property
    def cacheBlockSize(self):
        """
        `Related Pages <http://54.222.217.254/javascript-grid-server-side-model-tree-data/>`_
        """
        return self._config_get()

    @cacheBlockSize.setter
    def cacheBlockSize(self, num: int):
        self._config(num)

    @property
    def cacheQuickFilter(self):
        """Set to true to turn on the Quick Filter cache, used to improve performance when using the Quick Filter.

        `Aggrid <https://ag-grid.com/javascript-data-grid/filter-quick//>`_
        """
        return self._config_get()

    @cacheQuickFilter.setter
    def cacheQuickFilter(self, num: int):
        self._config(num)

    @property
    def cellSelection(self) -> bool:
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/context-menu/>`_
        """
        return self._config_get()

    @cellSelection.setter
    def cellSelection(self, flag: bool):
        self._config(flag)

    @property
    def colResizeDefault(self):
        """
        If you hold 'shift' while dragging the resize handle, the column will take space away from the column adjacent
        to it. This means the total width for all columns will be constant.

        You can also change the default behaviour for resizing.
        Set grid property colResizeDefault='shift' to have shift resizing as default and normal resizing to happen when
        shift key is pressed.

        `Related Pages <https://www.ag-grid.com/javascript-grid-resizing/>`_
        """
        return self._config_get()

    @colResizeDefault.setter
    def colResizeDefault(self, val):
        self._config(val)

    @property
    def columns(self) -> Column:
        """
        Set the columnDefs with all the column properties.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-groups/#column-definitions-vs-column-group-definitions>`_
        """
        return self._config_sub_data_enum("columnDefs", Column)

    @property
    def columnMenu(self):
        """
        Define a column type (you can define as many as you like.
        Expect a valid Json object.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_
        """
        return self._config_get()

    @columnMenu.setter
    def columnMenu(self, val: str):
        self._config(val)

    @property
    def columnTypes(self):
        """
        Define a column type (you can define as many as you like.
        Expect a valid Json object.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_
        """
        return self._config_get()

    @columnTypes.setter
    def columnTypes(self, data: Union[str, dict]):
        if isinstance(data, dict):
            self._config(data)
        else:
            self._config(data, js_type=True)

    @property
    def components(self):
        return self._config_get()

    @components.setter
    def components(self, values: dict):
        self._config(values, js_type=True)

    @property
    def defaultColDef(self) -> DefaultColDef:
        """
        Contains properties that all columns will inherit.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#custom-column-types>`_
        """
        return self._config_sub_data("defaultColDef", DefaultColDef)

    @property
    def data(self):
        """
        Update the Row Data inside the grid by updating the rowData grid property or by calling the grid API
        setRowData().

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/data-update-row-data/>`_
        """
        return self._config_get(name="rowData")

    @data.setter
    def data(self, val):
        self._config(val, name="rowData")

    @property
    def debug(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/data-update-row-data/>`_
        """
        return self._config_get()

    @debug.setter
    def debug(self, flag: bool):
        self._config(flag)

    @property
    def deltaColumnMode(self):
        """   """
        return self._config_get()

    @deltaColumnMode.setter
    def deltaColumnMode(self, val: str):
        self._config(val)

    @property
    def deltaRowDataMode(self):
        """ """
        return self._config_get()

    @deltaRowDataMode.setter
    def deltaRowDataMode(self, flag: bool):
        self._config(flag)

    @property
    def editType(self):
        """ """
        return self._config_get()

    @editType.setter
    def editType(self, value: str):
        self._config(value)

    @property
    def enableAdvancedFilter(self):
        """The Advanced Filter allows for complex filter conditions to be entered across columns in a
        single type-ahead input, as well as within a hierarchical visual builder.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/filter-advanced/>`_
        """
        return self._config_get()

    @enableAdvancedFilter.setter
    def enableAdvancedFilter(self, flag: bool):
        self._config(flag)

    @property
    def enableColResize(self):
        """
        `Related Pages <http://54.222.217.254/javascript-grid-server-side-model-tree-data/>`_
        """
        return self._config_get()

    @enableColResize.setter
    def enableColResize(self, flag: bool):
        self._config(flag)

    @property
    def enablePivot(self):
        """
        Allow every column to be pivoted

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example>`_
        """
        return self._config_get()

    @enablePivot.setter
    def enablePivot(self, flag: bool):
        self._config(flag)

    @property
    def enableRangeSelection(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/context-menu/>`_
        """
        return self._config_get()

    @enableRangeSelection.setter
    def enableRangeSelection(self, flag: bool):
        self._config(flag)

    @property
    def enableValue(self):
        """
        This means you can drag the columns to the values section, but you cannot drag them to the group or pivot
        sections.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example>`_
        """
        return self._config_get()

    @enableValue.setter
    def enableValue(self, flag: bool):
        self._config(flag)

    @property
    def ensureDomOrder(self):
        """
        Ensures the rows and columns in the DOM always appear in the same order as displayed in the grid.

        `Related Pages <https://www.ag-grid.com/javascript-grid-cell-editing/>`_
        """
        return self._config_get()

    @ensureDomOrder.setter
    def ensureDomOrder(self, val):
        self._config(val)

    @property
    def enterMovesDown(self):
        """
        Set to true to have Enter key move focus to the cell below if not editing.
        The default is Enter key starts editing the currently focused cell.

        `Related Pages <https://www.ag-grid.com/javascript-grid-cell-editing/>`_
        """
        return self._config_get()

    @enterMovesDown.setter
    def enterMovesDown(self, val):
        self._config(val)

    @property
    def enterMovesDownAfterEdit(self):
        """
        Set to true to have Enter key move focus to the cell below after Enter is pressed while editing.
        The default is editing will stop and focus will remain on the editing cell.

        `Related Pages <https://www.ag-grid.com/javascript-grid-cell-editing/>`_
        """
        return self._config_get()

    @enterMovesDownAfterEdit.setter
    def enterMovesDownAfterEdit(self, val):
        self._config(val)

    @property
    def functionsReadOnly(self):
        """
        By setting the property functionsReadOnly=true, the grid will prevent changes to group, pivot or values
        through the GUI. This is useful if you want to show the user the group, pivot and values panel,
        so they can see which columns are used, but prevent them from making changes to the selection.

        `Related Pages <https://www.ag-grid.com/javascript-grid-cell-editing/>`_
        """
        return self._config_get()

    @functionsReadOnly.setter
    def functionsReadOnly(self, flag: bool):
        self._config(flag)

    def getServerSideGroupKey(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                              func_ref: bool = False):
        """

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if not str_func.startswith("function(dataItem)") and not func_ref:
            if "return " not in str_func:
                str_func = "return %s" % str_func
            str_func = "function(dataItem){%s}" % str_func
        self._config(str_func, js_type=True)

    def getContextMenuItems(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Set table context menu.

        `Context Menu <https://www.ag-grid.com/javascript-data-grid/context-menu/>`_
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if not str_func.startswith("function(params)") and not func_ref:
            str_func = "function(params){%s}" % str_func
        self._config(str_func, js_type=True)

    def getRowClass(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """
        Callback version of property rowClass to set class(es) for each row individually.
        Function should return either a string (class name), array of strings (array of class names) or undefined
        for no class.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-styles/#reference-styling-getRowClass>`_

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
    def groupAggFiltering(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tree-data/>`_
        """
        return self._config_get()

    @groupAggFiltering.setter
    def groupAggFiltering(self, flag: bool):
        self._config(flag)

    @property
    def groupAllowUnbalanced(self):
        """This section covers Unbalanced Groups - when grouping by rows that can contain null or undefined group
        values.

        `Related Pages <https://www.ag-grid.com/angular-data-grid/grouping-unbalanced-groups//>`_
        """
        return self._config_get()

    @groupAllowUnbalanced.setter
    def groupAllowUnbalanced(self, flag: bool):
        self._config(flag)

    @property
    def groupIncludeFooter(self):
        """
        If you want to include a footer with each group, set the property groupIncludeFooter to true.
        It is also possible to include a 'grand' total footer for all groups using the property groupIncludeTotalFooter.

        `Related Pages <https://www.ag-grid.com/archive/26.0.0/javascript-data-grid/grouping-footers/>`_
        """
        return self._config_get()

    @groupIncludeFooter.setter
    def groupIncludeFooter(self, flag: bool):
        self._config(flag)

    @property
    def groupIncludeTotalFooter(self):
        """
        `Related Pages <https://www.ag-grid.com/archive/26.0.0/javascript-data-grid/grouping-footers/>`_
        """
        return self._config_get()

    @groupIncludeTotalFooter.setter
    def groupIncludeTotalFooter(self, flag: bool):
        self._config(flag)

    @property
    def includeHiddenColumnsInQuickFilter(self) -> bool:
        """Hidden columns are excluded from the Quick Filter by default. To include hidden columns, set to true.

        `Ag-grid <https://ag-grid.com/javascript-data-grid/filter-quick//>`_
        """
        return self._config_get()

    @includeHiddenColumnsInQuickFilter.setter
    def includeHiddenColumnsInQuickFilter(self, flag: bool):
        self._config(flag)

    def isGroupOpenByDefault(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                             func_ref: bool = False):
        """

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def isServerSideGroup(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                          func_ref: bool = False):
        """

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if not str_func.startswith("function(dataItem)") and not func_ref:
            if "return " not in str_func:
                str_func = "return %s" % str_func
            str_func = "function(dataItem){%s}" % str_func
        self._config(str_func, js_type=True)

    def isRowSelectable(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if not str_func.startswith("function(row)") and not func_ref:
            if "return " not in str_func:
                str_func = "return %s" % str_func
            str_func = "function(row){%s}" % str_func
        self._config(str_func, js_type=True)

    @property
    def maxBlocksInCache(self):
        """
        `Related Pages <http://54.222.217.254/javascript-grid-server-side-model-tree-data/>`_
        """
        return self._config_get()

    @maxBlocksInCache.setter
    def maxBlocksInCache(self, num: int):
        self._config(num)

    def onGridReady(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/column-definitions/#default-column-definitions>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def on(self, event_type: str, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
           func_ref: bool = False):
        """

        `Related Pages <https://ag-grid.com/angular-data-grid/grid-interface/>`_

        :param event_type: The event type
        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        if not event_type.startswith("on"):
            event_type = "on%s" % event_type.capitalize()
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref, name=event_type)

    def onColumnHeaderClicked(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """A click is performed on a column header.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/#reference-columns-columnHeaderClicked>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onColumnHeaderMouseOver(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """A mouse cursor is initially moved over a column header.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/#reference-columns-columnHeaderClicked>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onColumnHeaderMouseLeave(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """A mouse cursor is moved out of a column header.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/#reference-columns-columnHeaderClicked>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onCellEditingStarted(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                             func_ref: bool = False):
        """Editing a cell has stopped.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/cell-editing/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onCellEditingStopped(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                             func_ref: bool = False):
        """Editing a cell has stopped.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/cell-editing/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onCellValueChanged(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                           func_ref: bool = False):
        """Value has changed after editing (this event will not fire if editing was cancelled, eg ESC was pressed) or
        if cell value has changed as a result of paste operation.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/cell-editing/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onCellClicked(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                     func_ref: bool = False):
        """Cell is clicked.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onCellDoubleClicked(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                     func_ref: bool = False):
        """Cell is double clicked.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onCellFocused(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                     func_ref: bool = False):
        """Cell is focused.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onCellMouseOver(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                        func_ref: bool = False):
        """Mouse entered cell.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onCellMouseOut(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                        func_ref: bool = False):
        """Mouse left cell.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onCellMouseDown(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                        func_ref: bool = False):
        """Mouse down on cell.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onFilterChanged(
            self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Filter has been modified and applied.

        `Related Pages <https://ag-grid.com/javascript-data-grid/grid-events//>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onRowClicked(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                     func_ref: bool = False):
        """Row is clicked.

        `Related Pages <https://ag-grid.com/angular-data-grid/grid-interface/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onRowDoubleClicked(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Row is double clicked.

        `Related Pages <https://ag-grid.com/angular-data-grid/grid-interface/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onRowEditingStarted(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                            func_ref: bool = False):
        """Editing a row has started (when row editing is enabled). When row editing, this event will be fired once and
        cellEditingStarted will be fired for each individual cell. Only fires when doing Full Row Editing.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/#reference-columns-columnHeaderClicked>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onRowEditingStopped(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                            func_ref: bool = False):
        """Editing a row has stopped (when row editing is enabled). When row editing, this event will be fired once
        and cellEditingStopped will be fired for each individual cell. Only fires when doing Full Row Editing.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/#reference-columns-columnHeaderClicked>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onRowValueChanged(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                          func_ref: bool = False):
        """A cell's value within a row has changed. This event corresponds to Full Row Editing only.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grid-events/#reference-columns-columnHeaderClicked>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onRowSelected(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                     func_ref: bool = False):
        """Row is selected or deselected. The event contains the node in question, so call the node's isSelected()
        method to see if it was just selected or deselected.

        `Related Pages <https://ag-grid.com/angular-data-grid/grid-interface/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onSelectionChanged(
            self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Row selection is changed. Use the grid API getSelectedNodes() or getSelectedRows() to get the new list of
        selected nodes / row data.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-selection/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        if self.rowSelection is None:
            self.rowSelection = 'single'
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onRowDataUpdated(
            self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Row selection is changed. Use the grid API getSelectedNodes() or getSelectedRows() to get the new list of
        selected nodes / row data.

        `Related Pages <https://ag-grid.com/javascript-data-grid/grid-lifecycle/#row-data-updated/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onColumnResized(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                        func_ref: bool = False):
        """

        `Related Pages <https://ag-grid.com/angular-data-grid/grid-interface/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def onPaginationChanged(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                            func_ref: bool = False):
        """

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-pagination/>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    @property
    def overlayLoadingTemplate(self):
        """Provide a plain HTML string to the grid properties overlayLoadingTemplate and overlayNoRowsTemplate.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/overlays/>`_
        """
        return self._config_get()

    @overlayLoadingTemplate.setter
    def overlayLoadingTemplate(self, val: str):
        self._config(val)

    @property
    def overlayNoRowsTemplate(self):
        """Provide a plain HTML string to the grid properties overlayLoadingTemplate and overlayNoRowsTemplate.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/overlays/>`_
        """
        return self._config_get()

    @overlayNoRowsTemplate.setter
    def overlayNoRowsTemplate(self, val: str):
        self._config(val)

    @property
    def paginateChildRows(self):
        """Set to true to have pages split children of groups when using Row Grouping or detail rows with Master Detail.
        See Pagination & Child Rows.

        Default: false

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-pagination/>`_
        """
        return self._config_get(False)

    @paginateChildRows.setter
    def paginateChildRows(self, flag: bool):
        self._config(flag)

    @property
    def pagination(self):
        """To enable pagination in, set the grid property pagination=true.
        The following simple example shows this, the only difference to this and previous examples is the pagination=true
        property.

        `Related Pages <https://www.ag-grid.com/javascript-grid-pagination/>`_
        """
        return self._config_get()

    @pagination.setter
    def pagination(self, val):
        self._config(val)

    @property
    def paginationPageSize(self):
        """How many rows to load per page. If paginationAutoPageSize is specified, this property is ignored.
        See Customising Pagination.
        Default: 100

        `Related Pages <https://www.ag-grid.com/javascript-grid-pagination/>`_
        """
        return self._config_get(100)

    @paginationPageSize.setter
    def paginationPageSize(self, num: int):
        self.pagination = num > 0
        self._config(num)

    @property
    def paginationPageSizeSelector(self):
        """

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-pagination/#customising-pagination>`_
        """
        return self._config_get([200, 500, 1000])

    @paginationPageSizeSelector.setter
    def paginationPageSizeSelector(self, values: List[int]):
        self._config(values)

    @property
    def paginationAutoPageSize(self):
        """If you set paginationAutoPageSize=true the grid will automatically show as many rows in each page as it can
        fit. This is demonstrated below. Note if you resize the display area of the grid, the page size automatically
        changes. To view this, open the example up in a new tab and resize your browser.

        `Related Pages <https://www.ag-grid.com/javascript-grid-pagination/>`_
        """
        return self._config_get()

    @paginationAutoPageSize.setter
    def paginationAutoPageSize(self, num: int):
        self._config(num)

    def paginationNumberFormatter(self):
        """Allows user to format the numbers in the pagination panel, i.e. 'row count' and 'page number' labels.
        This is for pagination panel only, to format numbers inside the grid's cells (i.e. your data),
        then use valueFormatter in the column definitions.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-pagination/>`_
        """
        pass

    @property
    def popupParent(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/csv-export/>`_
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/context-menu/>`_
        """
        return self._config_get()

    @popupParent.setter
    def popupParent(self, data: str):
        self._config(data, js_type=True)

    @property
    def pivotMode(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example>`_
        """
        return self._config_get()

    @pivotMode.setter
    def pivotMode(self, flag: bool):
        self._config(flag)

    @property
    def pivotPanelShow(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example>`_
        """
        return self._config_get()

    @pivotPanelShow.setter
    def pivotPanelShow(self, val: str):
        self._config(val)

    @property
    def groupDefaultExpanded(self):
        """To open all groups down to a given group level use the groupDefaultExpanded grid option as shown below:

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/grouping-opening-groups/#opening-group-levels-by-default>`_
        """
        return self._config_get()

    @groupDefaultExpanded.setter
    def groupDefaultExpanded(self, val: int):
        if self.component.options.verbose and self.page.imports.pkgs.ag_grid.community_version:
            logging.warning("groupDefaultExpanded not available in the community version")
        self._config(val)

    @property
    def groupSelectsChildren(self):
        """Filler groups do not keep their selection state should the filler group be moved.

        For example if you have groups A->B->C, where C is the only row provided
        (so the grid creates groups A and B for you), and then you change the patch to D->B->C,
        group B will not keep it's selection.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tree-data/#example-selecting-groups-and-children>`_
        """
        return self._config_get()

    @groupSelectsChildren.setter
    def groupSelectsChildren(self, flag: bool):
        self._config(flag)

    def quickFilterMatcher(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                             func_ref: bool = False):
        """Changes the matching logic for whether a row passes the Quick Filter.

        `ag-grid <https://ag-grid.com/javascript-data-grid/filter-quick//>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    def quickFilterParser(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
                             func_ref: bool = False):
        """Changes how the Quick Filter splits the Quick Filter text into search terms.

        `ag-grid <https://ag-grid.com/javascript-data-grid/filter-quick//>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        """
        self._config_func(js_funcs=js_funcs, profile=profile, func_ref=func_ref)

    @property
    def quickFilterText(self) -> str:
        """Rows are filtered using this text as a Quick Filter.

        `Related Pages <https://ag-grid.com/javascript-data-grid/filter-quick//>`_
        """
        return self._config_get()

    @quickFilterText.setter
    def quickFilterText(self, val: str):
        self._config(val)

    @property
    def rowModelType(self):
        """
        `Related Pages <http://54.222.217.254/javascript-grid-server-side-model-tree-data/>`_
        """
        return self._config_get()

    @rowModelType.setter
    def rowModelType(self, value: str):
        self._config(value)

    @property
    def rowClass(self):
        """The style properties to apply to all rows. Set to an object of key (style names) and values (style values).

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-styles/>`_
        """
        return self._config_get(None)

    @rowClass.setter
    def rowClass(self, values: Union[str, list]):
        self._config(values)

    @property
    def rowClassRules(self):
        """The following snippet shows rowClassRules applying classes to rows using expressions on an age column value:

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-styles/>`_
        """
        return self._config_get(None)

    @rowClassRules.setter
    def rowClassRules(self, values: Union[str, dict]):
        if isinstance(values, dict):
            r = ["%s: %s" % (JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)) for k, v in values.items()]
            self._config("{%s}" % ",".join(r), js_type=True)
        else:
            self._config(values)

    @property
    def rowHeight(self):
        """By default, the grid will display rows with a height of 25px. You can change this for each row individually
        to give each row a different height.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-height/>`_
        """
        return self._config_get(42)

    @rowHeight.setter
    def rowHeight(self, num: Union[bool, int]):
        if not num:
            self.remove()
            self.page.properties.css.remove_text('aggrid_row_height')
            theme = self.component.style.theme_name or "alpine"
            self.page.properties.css.remove_text('aggrid_row_height_%s' % theme)
        else:
            row_height_px = int(num)
            if row_height_px < 42:
                theme = self.component.style.theme_name or "alpine"
                # Theme requiring specific CSS
                self.page.properties.css.add_text('''
.ag-theme-%s .ag-cell {
    line-height: %spx !important; 
}''' % (theme, row_height_px), map_id='aggrid_row_height_%s' % theme, replace=True)
                self.page.properties.css.add_text('''
.ag-theme-%s {
  --ag-grid-size: 3px;
  --ag-list-item-height: %spx;
} ''' % (theme, row_height_px), map_id='aggrid_row_height', replace=True)
            self._config(row_height_px)

    @property
    def rowStyle(self):
        """Property to set style for all rows. Set to an object of key (style names) and values (style values).

        `Related Pages <http://54.222.217.254/javascript-grid-row-styles/#row-style>`_
        """
        return self._config_get(None)

    @rowStyle.setter
    def rowStyle(self, values: Union[dict, str]):
        self._config(values)

    @property
    def sideBar(self):
        """

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/filter-api//>`_
        """
        return self._config_get()

    @sideBar.setter
    def sideBar(self, val):
        self._config(val)

    @property
    def singleClickEdit(self):
        """To change the default so that a single-click starts editing, set the property gridOptions.singleClickEdit = true.
        This is useful when you want a cell to enter edit mode as soon as you click on it, similar to the experience you
        get when inside Excel.

        `Related Pages <https://www.ag-grid.com/javascript-grid-cell-editing/>`_
        """
        return self._config_get()

    @singleClickEdit.setter
    def singleClickEdit(self, val):
        self._config(val)

    @property
    def suppressAggFilteredOnly(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tree-data/>`_
        """
        return self._config_get()

    @suppressAggFilteredOnly.setter
    def suppressAggFilteredOnly(self, flag: bool):
        self._config(flag)

    @property
    def suppressClickEdit(self):
        """The grid configures a cellRenderer with a button to start editing.

        `Related Pages <https://www.ag-grid.com/javascript-grid-cell-editing/>`_
        """
        return self._config_get()

    @suppressClickEdit.setter
    def suppressClickEdit(self, val):
        self._config(val)

    @property
    def suppressCutToClipboard(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/clipboard/>`_
        """
        return self._config_get()

    @suppressCutToClipboard.setter
    def suppressCutToClipboard(self, val):
        self._config(val)

    @property
    def suppressPaginationPanel(self):
        """If you set suppressPaginationPanel=true, the grid will not show the standard navigation controls for pagination.
        This is useful is you want to provide your own navigation controls.

        `Related Pages <https://www.ag-grid.com/javascript-grid-pagination/>`_
        """
        return self._config_get(False)

    @suppressPaginationPanel.setter
    def suppressPaginationPanel(self, flag: bool):
        self._config(flag)

    @property
    def suppressPaste(self):
        """Pasting is on by default as long as cells are editable (non-editable cells cannot be modified,
        even with a paste operation). Set to true turn paste operations off.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/clipboard/>`_
        """
        return self._config_get()

    @suppressPaste.setter
    def suppressPaste(self, flag: bool):
        self._config(flag)

    @property
    def suppressCopySingleCellRanges(self):
        """Set to true to copy rows instead of ranges when a range with only a single cell is selected.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/clipboard/>`_
        """
        return self._config_get()

    @suppressCopySingleCellRanges.setter
    def suppressCopySingleCellRanges(self, flag: bool):
        self._config(flag)

    @property
    def suppressRowHoverHighlight(self):
        """Highlighting Rows is on by default. To turn it off, set the grid property.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-styles/>`_
        """
        return self._config_get()

    @suppressRowHoverHighlight.setter
    def suppressRowHoverHighlight(self, flag: bool):
        self._config(flag)

    @property
    def columnHoverHighlight(self):
        """Highlighting Columns is off by default. To turn it on, set the grid property.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-styles/>`_
        """
        return self._config_get()

    @columnHoverHighlight.setter
    def columnHoverHighlight(self, flag: bool):
        self._config(flag)

    @property
    def suppressScrollOnNewData(self):
        """The example also sets property suppressScrollOnNewData=true, which tells the grid to NOT scroll to the top
        when the page changes.

        `Related Pages <https://www.ag-grid.com/javascript-grid-pagination/>`_
        """
        return self._config_get()

    @suppressScrollOnNewData.setter
    def suppressScrollOnNewData(self, val):
        self._config(val)

    @property
    def suppressColumnVirtualisation(self):
        """Ensures all columns are rendered, i.e. appears in the DOM.

        `Related Pages <https://www.ag-grid.com/javascript-grid-accessibility/>`_
        """
        return self._config_get()

    @suppressColumnVirtualisation.setter
    def suppressColumnVirtualisation(self, val):
        self._config(val)

    @property
    def suppressDragLeaveHidesColumns(self):
        """Column animations happen when you move a column. The default is for animations to be turned on.

        It is recommended that you leave the column move animations on unless your target platform (browser and hardware)
        is to slow to manage the animations.
        To turn OFF column animations, set the grid property suppressColumnMoveAnimation=true.

        `Related Pages <https://www.ag-grid.com/javascript-grid-column-moving/>`_
        """
        return self._config_get()

    @suppressDragLeaveHidesColumns.setter
    def suppressDragLeaveHidesColumns(self, val):
        self._config(val)

    @property
    def suppressExcelExport(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/csv-export/>`_
        """
        return self._config_get()

    @suppressExcelExport.setter
    def suppressExcelExport(self, flag: bool):
        self._config(flag)

    @property
    def suppressPropertyNamesCheck(self):
        """ """
        return self._config_get()

    @suppressPropertyNamesCheck.setter
    def suppressPropertyNamesCheck(self, flag: bool):
        self._config(flag)

    @property
    def rowMultiSelectWithClick(self):
        """Set to true to allow multiple rows to be selected with clicks.

        For example, if you click to select one row and then click to select another row, the first row will stay
        selected as well.
        Clicking a selected row in this mode will deselect the row.
        This is useful for touch devices where Ctrl and Shift clicking is not an option.

        `Related Pages <https://www.ag-grid.com/javascript-grid-selection/>`_
        """
        return self._config_get()

    @rowMultiSelectWithClick.setter
    def rowMultiSelectWithClick(self, val):
        self._config(val)

    @property
    def rowDeselection(self):
        """Set to true to allow rows to be deselected if you hold down Ctrl and click the row.
        By default, the grid disallows deselection of rows (i.e. once a row is selected, it remains selected until another
        row is selected in its place).

        `Related Pages <https://www.ag-grid.com/javascript-grid-selection/>`_
        """
        return self._config_get()

    @rowDeselection.setter
    def rowDeselection(self, val):
        self._config(val)

    @property
    def rowSelection(self):
        """Type of row selection, set to either 'single' or 'multiple' to enable selection.
        'single' will use single row selection, such that when you select a row, any previously selected row gets
        unselected.
        'multiple' allows multiple rows to be selected.

        `Related Pages <https://www.ag-grid.com/javascript-grid-selection/>`_
        """
        return self._config_get()

    @rowSelection.setter
    def rowSelection(self, val):
        self._config(val)

    @property
    def rowBuffer(self):
        """Sets the number of rows rendered outside of the scrollable viewable area.

        `Related Pages <https://www.ag-grid.com/javascript-grid-accessibility/>`_
        """
        return self._config_get()

    @rowBuffer.setter
    def rowBuffer(self, val):
        self._config(val)

    @property
    def rowGroupPanelShow(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/tool-panel-columns/#column-tool-panel-example>`_
        """
        return self._config_get()

    @rowGroupPanelShow.setter
    def rowGroupPanelShow(self, val: str):
        if self.component.options.verbose and self.page.imports.pkgs.ag_grid.community_version:
            logging.warning("rowGroupPanelShow not available in the community version")
        self._config(val)

    @property
    def rowTotal(self):
        """ Predefined way to add a row total attached to the table. """
        return self._config_get(False)

    @rowTotal.setter
    def rowTotal(self, flag: bool):
        self._config(flag)

    @property
    def suppressRowClickSelection(self):
        """If true, rows won't be selected when clicked. Use, for example, when you want checkbox selection, and don't
        want to also select the row when the row is clicked.

        `Related Pages <https://www.ag-grid.com/javascript-grid-selection/>`_
        """
        return self._config_get()

    @suppressRowClickSelection.setter
    def suppressRowClickSelection(self, flag: bool):
        self._config(flag)

    @property
    def suppressAggFuncInHeader(self):
        """
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-selection/>`_
        """
        return self._config_get()

    @suppressAggFuncInHeader.setter
    def suppressAggFuncInHeader(self, flag: bool):
        self._config(flag)

    @property
    def suppressRowTransform(self):
        """The property suppressRowTransform=true is used to stop the grid positioning rows using CSS transform and
        instead the grid will use CSS top.

        `Related Pages <https://www.ag-grid.com/angular-data-grid/row-spanning/>`_
        """
        return self._config_get()

    @suppressRowTransform.setter
    def suppressRowTransform(self, flag: bool):
        self._config(flag)

    @property
    def sortingOrder(self):
        """It is possible to override this behaviour by providing your own sortingOrder on either the gridOptions or the
        colDef.
        If defined both in colDef and gridOptions, the colDef will get preference, allowing you to define a common
        default, and then tailoring per column.

        `Related Pages <https://www.ag-grid.com/javascript-grid-sorting/>`_
        """
        return self._config_get()

    @sortingOrder.setter
    def sortingOrder(self, val):
        self._config(val)

    @property
    def sideBar(self):
        """ """
        return self._config_get()

    @sideBar.setter
    def sideBar(self, val: Union[str, dict]):
        self._config(val)

    @property
    def sideBars(self):
        return EnumSidebar(self, "sideBar")

    def statusBar(self) -> TableStatusBar:
        """ """
        return self._config_sub_data("statusBar", TableStatusBar)

    @property
    def treeData(self):
        """
        `Related Pages <https://www.ag-grid.com/documentation/javascript/tree-data/>`_
        """
        return self._config_get()

    @treeData.setter
    def treeData(self, flag: bool):
        if self.component.options.verbose and self.page.imports.pkgs.ag_grid.community_version:
            logging.warning("treeData not available in the community version")

        self._config(flag)

    @property
    def useCreateGrid(self) -> bool:
        """ """
        return self.get(False)

    @useCreateGrid.setter
    def useCreateGrid(self, flag: bool):
        if self.page.imports.pkgs.ag_grid.version[0] < "31.0.0":
            logging.warning(
                "Aggrid version %s might not be component with createGrid definition" % self.page.imports.pkgs.ag_grid.version[0])
        return self.set(flag)

    @property
    def valueCache(self):
        """Set to true to turn on the value cache.

        Default: false

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/value-getters/>`_
        """
        return self._config_get(False)

    @valueCache.setter
    def valueCache(self, flag: bool):
        self._config(flag)

    @property
    def valueCacheNeverExpires(self):
        """Set to true to configure the value cache to not expire after data updates.

        Default: false

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/value-getters/>`_
        """
        return self._config_get(False)

    @valueCacheNeverExpires.setter
    def valueCacheNeverExpires(self, flag: bool):
        self._config(flag)
