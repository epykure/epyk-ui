"""
CSS Style module for the Bespoke Excel components
"""


from epyk.core.css.styles import CssStyle


class CssTableExcel(CssStyle.CssCls):
  attrs = {'border-collapse': 'collapse', 'border-spacing': '0', 'margin': '0', 'border': '1px solid #e5e0e0'}
  cssId = {'child': 'table'}


class CssTableExcelHeaderCell(CssStyle.CssCls):
  attrs = {'border': '1px solid #cecece', 'padding': '1px 5px', 'text-align': 'center', 'background-color': '#DCDCDC'}
  cssId = {'child': 'table th'}


class CssTableExcelTd(CssStyle.CssCls):
  attrs = {'padding': '0', 'margin': '0'}
  cssId = {'child': 'table td'}


class CssTableExcelCell(CssStyle.CssCls):
  attrs = {'border': '2px solid white', 'background-color': 'white', 'height': '100%', 'width': '100%'}
  cssId = {'child': 'td > div'}
  active = {'border': '2px solid #8EB0E7'}


class CssTableExcelTitle(CssStyle.CssCls):
  attrs = {'border': '1px solid #cecece', 'cursor': 'pointer', 'padding': '1px 20px 1px 20px',
           'background-color': '#F3F3F3'}
  hover, active = {'cursor': 'pointer'}, {'background-color': '#8EB0E7'}
  cssId = {'child': 'td.rows'}


# -------------------------------------------------------------------------------------------
# CSS Style for the selected rows
# -------------------------------------------------------------------------------------------
class CssTableExcelSelectedRow(CssStyle.CssCls):
  attrs = {'background-color': '#E6EFFF'}
  cssId = {'child': 'tr.blue td > div'}


class CssTableExcelSelected(CssStyle.CssCls):
  attrs = {'background-color': '#8EB0E7', 'border': '1px dotted #5292F7'}
  cssId = {'chld': 'tr.blue td:first-child'}


class CssTableRedCells(CssStyle.CssCls):
  attrs = {'color': 'red'}
  after = {'content': '" $"'}


class CssTableBackGroundRedCells(CssStyle.CssCls):
  attrs = {'color': 'red'}
