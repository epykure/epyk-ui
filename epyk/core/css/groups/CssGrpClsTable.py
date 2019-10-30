"""
Group CSS class for all the Table components
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesTable
from epyk.core.css.styles import CssStylesText
from epyk.core.css.styles import CssStylesPivot
from epyk.core.css.styles import CssStylesTabulator
from epyk.core.css.styles import CssStylesTableExcel


class CssClassTable(CssGrpCls.CssGrpClass):
  """

  """
  css_table_basic = CssStylesTable.CssTableBasic
  css_text = CssStylesText.CssText
  __map, __alt_map = ["CssTableBasic", 'CssText'], []


class CssClassTableContent(CssGrpCls.CssGrpClass):
  """

  """
  css_div_table_content = CssStylesDiv.CssDivTableContent
  __map, __alt_map = ["CssDivTableContent"], []


class CssClassTabulator(CssGrpCls.CssGrpClass):
  """

  """
  css_tabulator = CssStylesTabulator.CssTabulator
  css_tabulator_headers = CssStylesTabulator.CssTabulatorHeaders
  css_tabulator_col = CssStylesTabulator.CssTabulatorCol
  css_tabulator_even_row = CssStylesTabulator.CssTabulatorEvenRow
  css_tabulator_row = CssStylesTabulator.CssTabulatorRow
  css_tabulator_odd_row = CssStylesTabulator.CssTabulatorOddRow
  css_tabulator_groups = CssStylesTabulator.CssTabulatorGroups
  css_tabulator_footer = CssStylesTabulator.CssTabulatorFooter
  css_tabulator_footer_pagination = CssStylesTabulator.CssTabulatorFooterPagination
  css_tabulator_header = CssStylesTabulator.CssTabulatorHeader
  css_tabulator_col_content = CssStylesTabulator.CssTabulatorColContent
  css_tabulator_selected = CssStylesTabulator.CssTabulatorSelected
  css_tabulator_tree_control = CssStylesTabulator.CssTabulatorTreeControl
  css_tabulator_tree_control_expand = CssStylesTabulator.CssTabulatorTreeControlExpand
  css_tabulator_cell = CssStylesTabulator.CssTabulatorCell
  __map, __alt_map = ['CssTabulator', 'CssTabulatorHeaders', 'CssTabulatorCol', 'CssTabulatorEvenRow', 'CssTabulatorRow',
                      'CssTabulatorOddRow', 'CssTabulatorGroups', 'CssTabulatorFooter', 'CssTabulatorFooterPagination',
                      'CssTabulatorHeader', 'CssTabulatorColContent', 'CssTabulatorSelected', 'CssTabulatorTreeControl',
                      'CssTabulatorTreeControlExpand', 'CssTabulatorCell'], []


class CssClassDataTable(CssGrpCls.CssGrpClass):
  """

  """
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  css_div_loading = CssStylesDiv.CssDivLoading
  css_data_table_header = CssStylesTable.CssDataTableHeader
  css_data_table_even = CssStylesTable.CssDataTableEven
  css_data_table_odd = CssStylesTable.CssDataTableOdd
  css_data_table = CssStylesTable.CssDataTable
  css_data_table_footer = CssStylesTable.CssDataTableFooter
  __map, __alt_map = ['CssDivNoBorder', 'CssDivLoading', 'CssDataTableHeader', 'CssDataTableEven', 'CssDataTableOdd',
                      'CssDataTable', 'CssDataTableFooter'], []


class CssClassTablePivot(CssGrpCls.CssGrpClass):
  """

  """
  css_data_table = CssStylesPivot.CssPivotHead
  css_pivot_cells = CssStylesPivot.CssPivotCells
  css_pivot_filter_box = CssStylesPivot.CssPivotFilterBox
  css_pivot_axis = CssStylesPivot.CssPivotAxis
  css_pivot_filter_vals = CssStylesPivot.CssPivotFilterVals
  css_pivot_filter_box_pop_up = CssStylesPivot.CssPivotFilterBoxPopUp
  __map, __alt_map = ['CssPivotHead', 'CssPivotCells', 'CssPivotFilterBox', 'CssPivotAxis', 'CssPivotFilterVals',
                      'CssPivotFilterBoxPopUp'], []


class CssClassTableBespoke(CssGrpCls.CssGrpClass):
  """

  """
  css_data_table = CssStylesTable.CssDataTable
  css_data_table_header = CssStylesTable.CssDataTableHeader
  css_data_table_even = CssStylesTable.CssDataTableEven
  css_data_table_odd = CssStylesTable.CssDataTableOdd
  __map, __alt_map = ['CssDataTable', 'CssDataTableHeader', 'CssDataTableEven', 'CssDataTableOdd'], []


class CssClassTableExcel(CssGrpCls.CssGrpClass):
  """

  """
  css_table_excel = CssStylesTableExcel.CssTableExcel
  css_table_excel_header_cell = CssStylesTableExcel.CssTableExcelHeaderCell
  css_table_excel_td = CssStylesTableExcel.CssTableExcelTd
  __map, __alt_map = ['CssTableExcel', 'CssTableExcelHeaderCell', 'CssTableExcelTd'], []
