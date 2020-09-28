

from epyk.core.css.styles.classes import CssStyle


class CssAgHead(CssStyle.Style):
  classname = "ag-header-cell-label"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'font-weight': 'bold', 'padding': '0 0 0 5px', 'background-color': self.rptObj.theme.greys[2]})


class CssAgOddRow(CssStyle.Style):
  classname = 'ag-row-odd'

  def customize(self):
    self.css({'background-color': self.rptObj.theme.greys[0]}, important=True)


class CssAgEvenRow(CssStyle.Style):
  classname = 'ag-row-even'

  def customize(self):
    self.css({'background-color': self.rptObj.theme.colors[0]}, important=True)


class CssAgCellFocus(CssStyle.Style):
  classname = 'ag-cell-focus'

  def customize(self):
    self.css({'border': '2px solid %s' % self.rptObj.theme.success[1]}, important=True)


class CssAgRow(CssStyle.Style):
  classname = 'ag-row'

  def customize(self):
    self.css({"align-items": 'center', 'display': 'flex'}, important=True)


class CssAgCell(CssStyle.Style):
  classname = 'ag-cell'

  def customize(self):
    self.css({"align-items": 'center', 'display': 'flex', 'padding': '0 0 0 5px'}, important=True)
