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
              }, important=True)


class CssPivotCells(CssStyle.Style):
  _attrs = {'font-size': '8pt', 'padding': '5px'}
  classname = "pvtTable"
  _selectors = {'child': "tr td"}

  def customize(self):
    self.css({"background": self.rptObj.theme.greys[0], 'color': self.rptObj.theme.greys[-1],
              'border': '1px solid %s' % self.rptObj.theme.colors[0]}, important=True)
    self.hover.css({'border': '1px solid %s' % self.rptObj.theme.colors[3]}, important=True)


class CssPivotLabel(CssStyle.Style):
  classname = "pvtColLabel, .pvtAxisLabel, .pvtRowLabel, .pvtTotalLabel,  th"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'background-color': self.rptObj.theme.colors[1],
              'border': '1px solid %s' % self.rptObj.theme.colors[5]}, important=True)


class CssPivotAxis(CssStyle.Style):
  _attrs = {'background': 'red'}
  classname = "pvtAxisContainer li span.pvtAttr"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'background': self.rptObj.theme.greys[0],
              #'border': '1px solid %s' % self.rptObj.theme.colors[1]
              }, important=True)


class CssPivotFilterBox(CssStyle.Style):
  classname = "pvtAxisContainer"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'background': self.rptObj.theme.greys[0],
              #'border': '1px solid %s' % self.rptObj.theme.colors[1]}
              }, important=True)


class CssPivotFilterVals(CssStyle.Style):
  classname = "pvtVals"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1],#'border': '1px solid %s' % self.rptObj.theme.colors[1]
              }, important=True)


class CssPivotFilterBoxPopUp(CssStyle.Style):
  classname = "pvtFilterBox"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'background-color': self.rptObj.theme.greys[0],
              #'border': '1px solid %s' % self.rptObj.theme.colors[1]
              }, important=True)
