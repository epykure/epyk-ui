"""
CSS Style module for the Bespoke Excel components
"""

from epyk.core.css.styles.classes import CssStyle


class CssTableExcel(CssStyle.Style):
  _attrs = {'border-collapse': 'collapse', 'border-spacing': 0, 'margin': 0, 'border': '1px solid #e5e0e0'}
  _selectors = {'child': 'table'}


class CssTableExcelHeaderCell(CssStyle.Style):
  _attrs = {'border': '1px solid #cecece', 'padding': '1px 5px', 'text-align': 'center', 'background-color': '#DCDCDC'}
  _selectors = {'child': 'table th'}


class CssTableExcelTd(CssStyle.Style):
  _attrs = {'padding': '0', 'margin': 0}
  _selectors = {'child': 'table td'}


class CssTableExcelCell(CssStyle.Style):
  _attrs = {'border': '2px solid white', 'background-color': 'white', 'height': '100%', 'width': '100%'}
  _selectors = {'child': 'td > div'}
  _active = {'border': '2px solid #8EB0E7'}


class CssTableExcelTitle(CssStyle.Style):
  _attrs = {
    'border': '1px solid #cecece', 'cursor': 'pointer', 'padding': '1px 20px 1px 20px',
    'background-color': '#F3F3F3'}
  _hover, _active = {'cursor': 'pointer'}, {'background-color': '#8EB0E7'}
  _selectors = {'child': 'td.rows'}


# -------------------------------------------------------------------------------------------
# CSS Style for the selected rows
# -------------------------------------------------------------------------------------------
class CssTableExcelSelectedRow(CssStyle.Style):
  _attrs = {'background-color': '#E6EFFF'}
  _selectors = {'child': 'tr.blue td > div'}


class CssTableExcelSelected(CssStyle.Style):
  _attrs = {'background-color': '#8EB0E7', 'border': '1px dotted #5292F7'}
  _selectors = {'child': 'tr.blue td:first-child'}


class CssTableRedCells(CssStyle.Style):
  _attrs = {'color': 'red'}
  _after = {'content': '" $"'}


class CssTableBackGroundRedCells(CssStyle.Style):
  _attrs = {'color': 'red'}
