

from epyk.core.css.styles.classes import CssStyle


class CssAgHead(CssStyle.Style):
  classname = "ag-header-cell-label"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[0], 'background-color': self.rptObj.theme.greys[-1]})


class CssAgOddRow(CssStyle.Style):
  classname = 'ag-row-odd'

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'background-color': self.rptObj.theme.greys[0]}, important=True)


class CssAgEvenRow(CssStyle.Style):
  classname = 'ag-row-even'

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'background-color': self.rptObj.theme.colors[1]}, important=True)


class CssAgCellFocus(CssStyle.Style):
  classname = 'ag-cell-focus'

  def customize(self):
    self.css({'border': '1px solid %s' % self.rptObj.theme.success[1]}, important=True)


class CssAgCell(CssStyle.Style):
  classname = 'ag-cell'

  def customize(self):
    self.css({'line-height': '25px', 'padding': '0 0 0 5px'}, important=True)
