"""
CSS Style module for the Tabulator components
"""


from epyk.core.css.styles import CssStyle


class CssTabulator(CssStyle.CssCls):

  def customize(self, style, eventsStyles):
    style.update({'border': '1px solid %s !IMPORTANT' % self.getColor('greys', 3), 'font-size': self.fontSize,
                  'background-color': self.getColor('greys', 2), 'font-family': self.fontFamily})


class CssTabulatorFooter(CssStyle.CssCls):
  cssId = {'child': '.tabulator-footer'}

  def customize(self, style, eventsStyles):
    style.update({'color': "%s !IMPORTANT" % self.getColor('greys', -1), 'border': 'none !IMPORTANT',
                  'background': "%s !IMPORTANT" % self.getColor('greys', 0)})


class CssTabulatorHeader(CssStyle.CssCls):
  cssId = {'child': '.tabulator-header'}

  def customize(self, style, eventsStyles):
    style.update({'color': "%s !IMPORTANT" % self.getColor('greys', 0),
                  'border': '1px solid %s !IMPORTANT' % self.getColor('greys', 2),
                  'background': "%s !IMPORTANT" % self.getColor('greys', 0)})


class CssTabulatorHeaders(CssStyle.CssCls):
  cssId = {'child': '.tabulator-headers'}

  def customize(self, style, eventsStyles):
    style.update({'color': "%s !IMPORTANT" % self.getColor('greys', 0), 'border': 'none',
                  'background': "%s !IMPORTANT" % self.getColor('greys', 0)})


class CssTabulatorSelected(CssStyle.CssCls):
  cssId = {'child': '.tabulator-selected'}

  def customize(self, style, eventsStyles):
    style.update({
      'border': '1px solid %s !IMPORTANT' % self.getColor('success', 1), 'color': 'black !IMPORTANT',
      'background': '%s !IMPORTANT' % self.getColor('success', 0)})


class CssTabulatorColContent(CssStyle.CssCls):
  cssId = {'child': '.tabulator-col-content'}

  def customize(self, style, eventsStyles):
    style.update({'color': "#DEDEDE !IMPORTANT", 'border': '1px solid #212121 !IMPORTANT',
                  'background': "#212121 !IMPORTANT"})


class CssTabulatorFooterPagination(CssStyle.CssCls):
  cssId = {'child': '.tabulator-page:not(.disabled)'}

  def customize(self, style, eventsStyles):
    style.update({'color': "%s !IMPORTANT" % self.getColor('greys', -1), 'border': 'none !IMPORTANT', 'background': "%s !IMPORTANT" % self.getColor('greys', 0)})
    eventsStyles['hover'].update({'color':  "%s !IMPORTANT" % self.getColor('colors', 0), 'background':  "%s !IMPORTANT" % self.getColor('colors', -1)})


class CssTabulatorCol(CssStyle.CssCls):
  attrs = {'text-align': 'center !IMPORTANT'}
  cssId = {'child': '.tabulator-col'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('greys', -1), 'border': '1px solid %s !IMPORTANT' % self.getColor('greys', 3),#'border': 'none !IMPORTANT',
                  'background': "%s !IMPORTANT" % self.getColor('greys', 0)})


class CssTabulatorGroups(CssStyle.CssCls):
  attrs = {'text-align': 'center !IMPORTANT'}
  cssId = {'child': '.tabulator-group'}


class CssTabulatorEvenRow(CssStyle.CssCls):
  cssId = {'child': '.tabulator-row-even'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('greys', -1), 'border': "1px solid %s !IMPORTANT" % self.getColor('colors', 1),
                  'background-color': self.getColor('colors', 1)})


class CssTabulatorOddRow(CssStyle.CssCls):
  cssId = {'child': '.tabulator-row-odd'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('greys', -1), 'border': "1px solid %s !IMPORTANT" % self.getColor('greys', 0),
                  'background-color': self.getColor('greys', 0)})


class CssTabulatorRow(CssStyle.CssCls):
  attrs = {'text-align': 'center !IMPORTANT'}
  cssId = {'child': '.tabulator-row'}

  def customize(self, style, eventsStyles):
    eventsStyles['hover'].update({'color': self.getColor('greys', -1), 'border': "1px solid %s !IMPORTANT" % self.getColor('success', 1),
                                  'background-color': self.getColor('colors', 3)})


class CssTabulatorCell(CssStyle.CssCls):
  cssId = {'child': '.tabulator-cell'}

  def customize(self, style, eventsStyles):
    # % self.getColor('greys', -1)
    style.update({'border-right': "1px solid %s !IMPORTANT" % self.getColor('greys', 3)})


class CssTabulatorTreeControl(CssStyle.CssCls):
  cssId = {'child': '.tabulator-data-tree-control'}

  def customize(self, style, eventsStyles):
    style.update({'border-color': "%s !IMPORTANT" % self.getColor('greys', -1)})


class CssTabulatorTreeControlExpand(CssStyle.CssCls):
  cssId = {'child': '.tabulator-data-tree-control-expand'}

  def customize(self, style, eventsStyles):
    style.update({'background': "%s !IMPORTANT" % self.getColor('greys', -1)})

