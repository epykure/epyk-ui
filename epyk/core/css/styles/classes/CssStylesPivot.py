"""
CSS Style module for the Pivot components
"""

from epyk.core.css.styles.classes import CssStyle


class CssPivotHead(CssStyle.Style):
  _attrs = {'font-size': '8pt', 'padding': '5px'}
  classname = "pvtTable"
  _selectors = {'child': "tr th"}

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'background-color': self.rptObj.theme.colors[0],
              #'border': '1px solid %s' % self.rptObj.theme.colors[3]
              })


class CssPivotCells(CssStyle.Style):
  _attrs = {'font-size': '8pt', 'padding': '5px'}
  classname = "pvtTable"
  _selectors = {'child': "tr td"}

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'border': '1px solid %s' % self.rptObj.theme.colors[3]}, important=True)
    self.hover.css({'color': self.rptObj.theme.greys[-1], 'background-color': self.rptObj.theme.colors[2]}, important=True)


class CssPivotLabel(CssStyle.Style):
  classname = "pvtColLabel, .pvtAxisLabel, .pvtRowLabel, .pvtTotalLabel,  th"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'background-color': self.rptObj.theme.colors[1],
              'border': '1px solid %s' % self.rptObj.theme.colors[5]}, important=True)


class CssPivotAxis(CssStyle.Style):
  _attrs = {'background': 'red'}
  classname = "pvtAxisContainer"
  _selectors = {"child": "li span.pvtAttr"}

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], #'background-color': self.rptObj.theme.colors[1],
              #'border': '1px solid %s' % self.rptObj.theme.colors[1]
              }, important=True)


class CssPivotFilterBox(CssStyle.Style):
  classname = "pvtAxisContainer"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[1], #'background-color': self.rptObj.theme.colors[3],
              #'border': '1px solid %s' % self.rptObj.theme.colors[1]}
              })


class CssPivotFilterVals(CssStyle.Style):
  classname = "pvtVals"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1],#'border': '1px solid %s' % self.rptObj.theme.colors[1]
              })


class CssPivotFilterBoxPopUp(CssStyle.Style):
  classname = "pvtFilterBox"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[1],
              #'border': '1px solid %s' % self.rptObj.theme.colors[1]
              })
