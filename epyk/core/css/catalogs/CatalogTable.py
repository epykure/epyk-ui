
from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesPivot, CssStylesTableExcel, CssStylesTable, CssStylesTabulator, CssStylesDiv, CssStylesTableAgGrid


class CatalogTable(Catalog.CatalogGroup):

  def table(self):
    """  """
    return self._set_class(CssStylesTable.CssTableBasic)

  def row_hover(self):
    """  """
    return self._set_class(CssStylesTable.CssTrHover)

  def new_row(self):
    """  """
    return self._set_class(CssStylesTable.CssTableNewRow)

  def selected(self):
    """  """
    return self._set_class(CssStylesTable.CssTableSelected)

  def cell_comment(self):
    """  """
    return self._set_class(CssStylesTable.CssCellComment)

  def cell_save(self):
    """  """
    return self._set_class(CssStylesTable.CssCellSave)

  def editable(self):
    """  """
    return self._set_class(CssStylesTable.CssTdEditor)

  def row_details(self):
    """  """
    return self._set_class(CssStylesTable.CssTdDetails)

  def row_details_shown(self):
    """  """
    return self._set_class(CssStylesTable.CssTdDetailsShown)

  def grid_headers(self):
    """  """
    return self._set_class(CssStylesTable.CssTdGridHeaderCols)

  def grid_no_header(self):
    """  """
    return self._set_class(CssStylesTable.CssTdGridNoHeaderCols)

  def grid_row_header(self):
    """  """
    return self._set_class(CssStylesTable.CssTdGridHeaderRows)

  def grid_vals(self):
    """  """
    return self._set_class(CssStylesTable.CssTdGridVals)

  def pivot_head(self):
    """  """
    return self._set_class(CssStylesPivot.CssPivotHead)

  def datatable(self):
    """  """
    return self._set_class(CssStylesTable.CssDataTable)

  def datatable_header(self):
    """  """
    return self._set_class(CssStylesTable.CssDataTableHeader)

  def datatable_footer(self):
    """  """
    return self._set_class(CssStylesTable.CssDataTableFooter)

  def datatable_even(self):
    """  """
    return self._set_class(CssStylesTable.CssDataTableEven)

  def datatable_odd(self):
    """  """
    return self._set_class(CssStylesTable.CssDataTableOdd)

  def pivot_cell(self):
    """  """
    return self._set_class(CssStylesPivot.CssPivotCells)

  def pivot_axis(self):
    """  """
    return self._set_class(CssStylesPivot.CssPivotAxis)

  def pivot_filter_box(self):
    """  """
    return self._set_class(CssStylesPivot.CssPivotFilterBox)

  def pivot_filter_val(self):
    """  """
    return self._set_class(CssStylesPivot.CssPivotFilterVals)

  def pivot_filter_label(self):
    """  """
    return self._set_class(CssStylesPivot.CssPivotLabel)

  def pivot_filter_popup(self):
    """  """
    return self._set_class(CssStylesPivot.CssPivotFilterBoxPopUp)

  def excel(self):
    """  """
    return self._set_class(CssStylesTableExcel.CssTableExcel)

  def excel_header_cell(self):
    """  """
    return self._set_class(CssStylesTableExcel.CssTableExcelHeaderCell)

  def excel_row(self):
    """  """
    return self._set_class(CssStylesTableExcel.CssTableExcelTd)

  def excel_cell(self):
    """  """
    return self._set_class(CssStylesTableExcel.CssTableExcelCell)

  def excel_title(self):
    """  """
    return self._set_class(CssStylesTableExcel.CssTableExcelTitle)

  def excel_selected_row(self):
    """  """
    return self._set_class(CssStylesTableExcel.CssTableExcelSelectedRow)

  def excel_selected_cell(self):
    """  """
    return self._set_class(CssStylesTableExcel.CssTableExcelSelected)

  def excel_red_cell(self):
    """  """
    return self._set_class(CssStylesTableExcel.CssTableRedCells)

  def excel_red_cell_background(self):
    """  """
    return self._set_class(CssStylesTableExcel.CssTableBackGroundRedCells)

  def tabulator(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulator)

  def tabulator_footer(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorFooter)

  def tabulator_footer_pagination(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorFooterPagination)

  def tabulator_header(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorHeader)

  def tabulator_headers(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorHeaders)

  def tabulator_selected(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorSelected)

  def tabulator_col_content(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorColContent)

  def tabulator_menu(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorMenu)

  def tabulator_menu_item(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorMenuItem)

  def tabulator_col(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorCol)

  def tabulator_groups(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorGroups)

  def tabulator_even_rows(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorEvenRow)

  def tabulator_even_rows_no_strop(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorEvenRowNoStrip)

  def tabulator_odd_rows(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorOddRow)

  def tabulator_rows(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorRow)

  def tabulator_cell(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorCell)

  def tabulator_tree_control(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorTreeControl)

  def tabulator_tree_control_expand(self):
    """  """
    return self._set_class(CssStylesTabulator.CssTabulatorTreeControlExpand)

  def table_content(self):
    """ """
    return self._set_class(CssStylesDiv.CssDivTableContent)

  def ag_head(self):
    """  """
    return self._set_class(CssStylesTableAgGrid.CssAgHead)

  def ag_row_odd(self):
    """  """
    return self._set_class(CssStylesTableAgGrid.CssAgOddRow)

  def ag_row_even(self):
    """  """
    return self._set_class(CssStylesTableAgGrid.CssAgEvenRow)

  def ag_row(self):
    """  """
    return self._set_class(CssStylesTableAgGrid.CssAgRow)

  def ag_cell_focus(self):
    """  """
    return self._set_class(CssStylesTableAgGrid.CssAgCellFocus)

  def ag_cell(self):
    """  """
    return self._set_class(CssStylesTableAgGrid.CssAgCell)
