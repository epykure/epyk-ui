"""
CSS Style module for the Tabulator components
"""

from epyk.core.css.styles.classes import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssTabulator(CssStyle.Style):

  def customize(self):
    self.css({'border': '1px solid %s !IMPORTANT' % self.rptObj.theme.greys[3],
              'font-size': '%s%s' % (Defaults_css.Font.header_size, Defaults_css.Font.unit),
              'background-color': self.rptObj.theme.greys[2], 'font-family': Defaults_css.Font.family})


class CssTabulatorFooter(CssStyle.Style):
  classname = "tabulator-footer"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'border': 'none',
              'background': self.rptObj.theme.greys[0]}, important=True)


class CssTabulatorHeader(CssStyle.Style):
  classname = "tabulator-header"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[0], 'border': '1px solid %s' % self.rptObj.theme.greys[2],
              'background': self.rptObj.theme.greys[0]}, important=True)


class CssTabulatorHeaders(CssStyle.Style):
  classname = 'tabulator-headers'

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[0], 'border': 'none',
              'background': self.rptObj.theme.greys[0]}, important=True)


class CssTabulatorSelected(CssStyle.Style):
  classname = 'tabulator-selected'

  def customize(self):
    self.css({'border': '1px solid %s' % self.rptObj.theme.success[1], 'color': 'black',
              'background': self.rptObj.theme.success[0]}, important=True)


class CssTabulatorColContent(CssStyle.Style):
  classname = 'tabulator-col-content'

  def customize(self):
    self.css({'color': "#DEDEDE", 'border': '1px solid #212121', 'background': "#212121"})


class CssTabulatorFooterPagination(CssStyle.Style):
  classname = 'tabulator-page:not(.disabled)'

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'border': 'none',
              'background': self.rptObj.theme.greys[0]}, important=True)
    self.hover.css({'color': self.rptObj.theme.colors[0], 'background': self.rptObj.theme.colors[-1]}, important=True)


class CssTabulatorCol(CssStyle.Style):
  _attrs = {'text-align': 'center !IMPORTANT'}
  classname = 'tabulator-col'

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'border': '1px solid %s' % self.rptObj.theme.greys[3],#'border': 'none !IMPORTANT',
              'background': self.rptObj.theme.greys[0]}, important=True)


class CssTabulatorGroups(CssStyle.Style):
  _attrs = {'text-align': 'center !IMPORTANT'}
  classname = 'tabulator-group'


class CssTabulatorEvenRow(CssStyle.Style):
  classname = 'tabulator-row-even'

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'border': "1px solid %s !IMPORTANT" % self.rptObj.theme.colors[1],
              'background-color': self.rptObj.theme.colors[1]})


class CssTabulatorOddRow(CssStyle.Style):
  classname = 'tabulator-row-odd'

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'border': "1px solid %s" % self.rptObj.theme.greys[0],
              'background-color': self.rptObj.theme.greys[0]})


class CssTabulatorRow(CssStyle.Style):
  _attrs = {'text-align': 'center !IMPORTANT'}
  classname = '.tabulator-row'

  def customize(self):
    self.hover.css({'color': self.rptObj.theme.greys[-1], 'border': "1px solid %s !IMPORTANT" % self.rptObj.theme.success[1],
                    'background-color': self.rptObj.theme.colors[3]})


class CssTabulatorCell(CssStyle.Style):
  classname = 'tabulator-cell'

  def customize(self):
    self.css({'border-right': "1px solid %s" % self.rptObj.theme.greys[3]}, important=True)


class CssTabulatorTreeControl(CssStyle.Style):
  classname = 'tabulator-data-tree-control'

  def customize(self):
    self.css({'border-color': self.rptObj.theme.greys[-1]}, important=True)


class CssTabulatorTreeControlExpand(CssStyle.Style):
  classname = 'tabulator-data-tree-control-expand'

  def customize(self):
    self.css({'background': self.rptObj.theme.greys[-1]}, important=True)
