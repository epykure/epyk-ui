"""
CSS Style module for the Table components
"""

from epyk.core.css.styles.classes import CssStyle


class CssDataTable(CssStyle.Style):
  _attrs = {'border-collapse': 'collapse !IMPORTANT'}

  def customize(self):
    self.css({'border': "1px solid %s" % self.page.theme.greys[3]}, important=True)


class CssDataTableHeader(CssStyle.Style):
  _selectors = {'child': 'thead'}

  def customize(self):
    self.css({
      'color': self.page.theme.greys[0],
      "background": self.page.theme.greys[-1], 'white-space': 'nowrap'})


class CssDataTableFooter(CssStyle.Style):
  _selector = 'paginate_button'
  classname = False

  def customize(self):
    self.css({
      "color": "red",
      'background-color': "%s" % self.page.theme.notch(-3)}, important=True)


class CssDataTableEven(CssStyle.Style):
  _selectors = {'child': 'tbody tr:nth-child(even)'}

  def customize(self):
    self.css({'color': self.page.theme.greys[-1], 'background-color': self.page.theme.greys[0],
              'border-top': "1px solid %s !IMPORTANT" % self.page.theme.greys[0]})
    self.hover.css({
      'border': "1px solid %s !IMPORTANT" % self.page.theme.success[1],
      'color': self.page.theme.greys[-1], 'background-color': self.page.theme.notch(-2)})


class CssDataTableOdd(CssStyle.Style):
  _selectors = {'child': 'tbody tr:nth-child(odd)'}

  def customize(self):
    self.css({
      'color': self.page.theme.greys[-1],
      'background-color': self.page.theme.colors[1],
      'border-top': "1px solid %s !IMPORTANT" % self.page.theme.colors[1]})
    self.hover.css({
      'border': "1px solid %s !IMPORTANT" % self.page.theme.success[1],
      'color': self.page.theme.greys[-1],
      'background-color': self.page.theme.notch(-2)})


class CssTableBasic(CssStyle.Style):
  _attrs = {'margin': '5px', 'border-collapse': 'collapse'}


# class CssTableColumnFixed(CssStyle.Style):
#   _attrs = {'margin': '5px', 'text-align': 'left', 'font-weight': 'bold'}
#

class CssTableNewRow(CssStyle.Style):
  _attrs = {'color': '#546472'}


class CssTableSelected(CssStyle.Style):
  _attrs = {'background-color': '#AEDAF8 !important'}


class CssCellComment(CssStyle.Style):
  _attrs = {'margin': '0!important', 'padding': '2px 0 0 2px!important'}


class CssCellSave(CssStyle.Style):
  _attrs = {'color': '#293846!important'}


class CssTdEditor(CssStyle.Style):
  _attrs = {'border-width': '1px', 'border-style': 'solid', 'text-align': 'left', 'height': '30px', 'padding': '5px',
            'vertical-align': 'middle'}

  def customize(self):
    self.css({
      "color": self.page.theme.notch(),
      'border-color': self.page.theme.greys[5]})


class CssTdDetails(CssStyle.Style):
  _before = {'content': "'\\f0fe'", 'font-family': "'Font Awesome 5 Free'", 'cursor': 'pointer', 'padding': '0 5px 0 0'}
  _selectors = {'child': 'td'}


class CssTdDetailsShown(CssStyle.Style):
  _before = {'content': "'\\f146'", 'font-family': "'Font Awesome 5 Free'", 'cursor': 'pointer', 'padding': '0 5px 0 0'}
  _selectors = {'child': 'td'}


class CssTdGridHeaderCols(CssStyle.Style):
  _attrs = {"border-bottom": '1px solid black', "margin": '0 1px'}
  _selectors = {'child': 'th:not(:first-child)'}


class CssTdGridNoHeaderCols(CssStyle.Style):
  _attrs = {"display": 'none'}
  _selectors = {'child': 'th:not(:first-child)'}


class CssTdGridHeaderRows(CssStyle.Style):
  _attrs = {"text-align": 'left'}
  _selectors = {'child': 'td[name="row_header"]'}


class CssTdGridVals(CssStyle.Style):
  _selectors = {'child': 'td:not([name="row_header"])'}
  _attrs = {"padding": '3px'}
  _focus = {"outline": "0px solid transparent"}

  def customize(self):
    self.css({
      "background-color": self.page.theme.colors[0],
      "border-bottom": '1px solid %s' % self.page.theme.greys[4]})
    self.focus.css({
      "border-bottom": '1px solid %s' % self.page.theme.success[1]})


class CssTrHover(CssStyle.Style):

  def customize(self):
    self.hover.css({"background": self.page.theme.notch(-3)})
