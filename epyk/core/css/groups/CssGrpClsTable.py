"""
Group CSS class for all the Table components
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesTable
from epyk.core.css.styles import CssStylesPivot
from epyk.core.css.styles import CssStylesTabulator
from epyk.core.css.styles import CssStylesTableExcel


class CssClassTableContent(CssGrpCls.CssGrpClass):
  CssDivTableContent = CssStylesDiv.CssDivTableContent
  __map, __alt_map = ["CssDivTableContent"], []


class CssClassTabulator(CssGrpCls.CssGrpClass):
  CssTabulator = CssStylesTabulator.CssTabulator
  CssTabulatorHeaders = CssStylesTabulator.CssTabulatorHeaders
  CssTabulatorCol = CssStylesTabulator.CssTabulatorCol
  CssTabulatorEvenRow = CssStylesTabulator.CssTabulatorEvenRow
  CssTabulatorRow = CssStylesTabulator.CssTabulatorRow
  CssTabulatorOddRow = CssStylesTabulator.CssTabulatorOddRow
  CssTabulatorGroups = CssStylesTabulator.CssTabulatorGroups
  CssTabulatorFooter = CssStylesTabulator.CssTabulatorFooter
  CssTabulatorFooterPagination = CssStylesTabulator.CssTabulatorFooterPagination
  CssTabulatorHeader = CssStylesTabulator.CssTabulatorHeader
  CssTabulatorColContent = CssStylesTabulator.CssTabulatorColContent
  CssTabulatorSelected = CssStylesTabulator.CssTabulatorSelected
  CssTabulatorTreeControl = CssStylesTabulator.CssTabulatorTreeControl
  CssTabulatorTreeControlExpand = CssStylesTabulator.CssTabulatorTreeControlExpand
  CssTabulatorCell = CssStylesTabulator.CssTabulatorCell
  __map, __alt_map = ['CssTabulator', 'CssTabulatorHeaders', 'CssTabulatorCol', 'CssTabulatorEvenRow', 'CssTabulatorRow',
                      'CssTabulatorOddRow', 'CssTabulatorGroups', 'CssTabulatorFooter', 'CssTabulatorFooterPagination',
                      'CssTabulatorHeader', 'CssTabulatorColContent', 'CssTabulatorSelected', 'CssTabulatorTreeControl',
                      'CssTabulatorTreeControlExpand', 'CssTabulatorCell'], []


class CssClassDataTable(CssGrpCls.CssGrpClass):
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssDivLoading = CssStylesDiv.CssDivLoading
  CssDataTableHeader = CssStylesTable.CssDataTableHeader
  CssDataTableEven = CssStylesTable.CssDataTableEven
  CssDataTableOdd = CssStylesTable.CssDataTableOdd
  CssDataTable = CssStylesTable.CssDataTable
  CssDataTableFooter = CssStylesTable.CssDataTableFooter
  __map, __alt_map = ['CssDivNoBorder', 'CssDivLoading', 'CssDataTableHeader', 'CssDataTableEven', 'CssDataTableOdd',
                      'CssDataTable', 'CssDataTableFooter'], []


class CssClassTablePivot(CssGrpCls.CssGrpClass):
  CssDataTable = CssStylesPivot.CssPivotHead
  CssPivotCells = CssStylesPivot.CssPivotCells
  CssPivotFilterBox = CssStylesPivot.CssPivotFilterBox
  CssPivotAxis = CssStylesPivot.CssPivotAxis
  CssPivotFilterVals = CssStylesPivot.CssPivotFilterVals
  CssPivotFilterBoxPopUp = CssStylesPivot.CssPivotFilterBoxPopUp
  __map, __alt_map = ['CssPivotHead', 'CssPivotCells', 'CssPivotFilterBox', 'CssPivotAxis', 'CssPivotFilterVals',
                      'CssPivotFilterBoxPopUp'], []


class CssClassTableBespoke(CssGrpCls.CssGrpClass):
  CssDataTable = CssStylesTable.CssDataTable
  CssDataTableHeader = CssStylesTable.CssDataTableHeader
  CssDataTableEven = CssStylesTable.CssDataTableEven
  CssDataTableOdd = CssStylesTable.CssDataTableOdd
  __map, __alt_map = ['CssDataTable', 'CssDataTableHeader', 'CssDataTableEven', 'CssDataTableOdd'], []


class CssClassTableExcel(CssGrpCls.CssGrpClass):
  CssTableExcel = CssStylesTableExcel.CssTableExcel
  CssTableExcelHeaderCell = CssStylesTableExcel.CssTableExcelHeaderCell
  CssTableExcelTd = CssStylesTableExcel.CssTableExcelTd
  __map, __alt_map = ['CssTableExcel', 'CssTableExcelHeaderCell', 'CssTableExcelTd'], []
