#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.css.styles.classes import CssStyle


class CssTabulator(CssStyle.Style):

  def customize(self):
    self.css({
      "border": "none !IMPORTANT",
      'background-color': self.page.theme.greys[0],
      'font-family': self.page.body.style.globals.font.family})


class CssTabulatorFooter(CssStyle.Style):
  classname = "tabulator-footer"

  def customize(self):
    self.css({
      'color': self.page.theme.greys[-1],
      'border': 'none',
      'background': self.page.theme.greys[0]}, important=True)


class CssTabulatorTable(CssStyle.Style):
  classname = "tabulator-table"
  _attrs = {'width': '100%'}


class CssTabulatorEditing(CssStyle.Style):
  classname = "tabulator-editing input"

  def customize(self):
    self.css({
      'font-family': self.page.body.style.globals.font.family,
      'font-size': "inherit", 'background': 'none', 'border': 'none'}, important=True)
    self.focus.css({'outline-color': self.page.theme.success.base})


class CssTabulatorCellEditing(CssStyle.Style):
  classname = "tabulator-cell.tabulator-editing"

  def customize(self):
    self.css({'border-color': 'none'}, important=True)


class CssTabulatorHeader(CssStyle.Style):
  classname = "tabulator-header"

  def customize(self):
    self.css({'background': 'none'}, important=True)


class CssTabulatorHeaders(CssStyle.Style):
  classname = 'tabulator-headers'

  def customize(self):
    self.css({'border': 'none', 'background': 'none'}, important=True)


class CssTabulatorSelected(CssStyle.Style):
  classname = 'tabulator-selected'

  def customize(self):
    self.css({
      'border': '1px solid %s' % self.page.theme.success.base, 'color': self.page.theme.black,
      'background': None
    }, important=True)


class CssTabulatorCol(CssStyle.Style):
  classname = 'tabulator-col'

  def customize(self):
    self.css({'color': self.page.body.style.globals.table.header_color,
              'border': self.page.body.style.globals.table.header_border,
              'background': self.page.body.style.globals.table.header_background, 'padding': '1px 0',
              "text-align": 'center'}, important=True)


class CssTabulatorColTitle(CssStyle.Style):
  classname = 'tabulator-col-title'

  def customize(self):
    self.css({
      'color': self.page.body.style.globals.table.header_color, 'font-weight': 900,
      'font-size': "{}px".format(self.page.body.style.globals.font.header_size)})


class CssTabulatorColContent(CssStyle.Style):
  classname = 'tabulator-col-content'

  def customize(self):
    self.css({
      'color': self.page.body.style.globals.table.header_color,
      'border': '1px solid %s' % self.page.body.style.globals.table.header_background,
      'background': self.page.body.style.globals.table.header_background})


class CssTabulatorMenu(CssStyle.Style):
  classname = 'tabulator-menu'

  def customize(self):
    self.hover.css({'color': self.page.theme.colors[-1]}, important=True)


class CssTabulatorMenuItem(CssStyle.Style):
  classname = 'tabulator-menu-item'

  def customize(self):
    self.css({
      'background': self.page.theme.greys[1],
      'color': self.page.theme.greys[-1], 'padding': '2px 10px'}, important=True)
    self.hover.css({'color': self.page.theme.colors[-1]}, important=True)


class CssTabulatorFooterPagination(CssStyle.Style):
  classname = 'tabulator-page:not(.disabled)'

  def customize(self):
    self.css({
      'color': self.page.theme.greys[-1], 'border': 'none',
      'background': self.page.theme.greys[0]}, important=True)
    self.hover.css({
      'color': self.page.theme.colors[0],
      'background': self.page.theme.colors[-1]}, important=True)


class CssTabulatorGroups(CssStyle.Style):
  _attrs = {'text-align': 'center !IMPORTANT'}
  classname = 'tabulator-group'


class CssTabulatorHeaderFilterInput(CssStyle.Style):
  _attrs = {'padding': '1px 4px !IMPORTANT', "border": "none !IMPORTANT"}
  _focus = {'outline': 0}
  classname = 'tabulator-header-filter'
  _selectors = {'child': 'input'}


class CssTabulatorEvenRow(CssStyle.Style):
  _selectors = {'child': '.tabulator-row-even'}

  def customize(self):
    self.css({
      'background-color': self.page.theme.colors[0]}, important=True)


class CssTabulatorEvenRowNoStrip(CssStyle.Style):
  _selectors = {'child': '.tabulator-row-even'}

  def customize(self):
    self.css({
      'background-color': self.page.theme.greys[0]}, important=True)


class CssTabulatorOddRow(CssStyle.Style):
  classname = 'tabulator-row-odd'

  def customize(self):
    self.css({
      'background-color': self.page.theme.greys[0]
    })


class CssTabulatorRow(CssStyle.Style):
  classname = 'tabulator-row'

  def customize(self):
    self.css({
      "min-height": "none !IMPORTANT",
      'color': self.page.theme.greys[-1],
      'border': "1px solid %s" % self.page.theme.greys[0]
    })
    self.hover.css({
      'border-bottom': "1px solid %s" % self.page.theme.colors[-1],
      'border-top': "1px solid %s" % self.page.theme.colors[-1],
      'background-color': self.page.theme.colors[1]
    }, important=True)


class CssTabulatorCell(CssStyle.Style):
  classname = 'tabulator-cell'

  def customize(self):
    self.css({
      'padding': 0,
      'border-right': self.page.body.style.globals.table.cell_border_right,
      'border-bottom': self.page.body.style.globals.table.cell_border_bottom #% self.rptObj.theme.greys[3]
              }, important=True)


class CssTabulatorTreeControl(CssStyle.Style):
  classname = 'tabulator-data-tree-control'

  def customize(self):
    self.css({'border-color': self.page.theme.greys[-1]}, important=True)


class CssTabulatorTreeControlExpand(CssStyle.Style):
  classname = 'tabulator-data-tree-control-expand'

  def customize(self):
    self.css({'background': self.page.theme.greys[-1]}, important=True)


class CssTabulatorSortAsc(CssStyle.Style):
  classname = 'tabulator-col.tabulator-sortable[aria-sort=asc] .tabulator-arrow'

  def customize(self):
    self.css({
      'border-bottom': "6px solid %s" % self.page.body.style.globals.table.sorter_arrow_selected}, important=True)


class CssTabulatorSortDesc(CssStyle.Style):
  classname = 'tabulator-col.tabulator-sortable[aria-sort=desc] .tabulator-arrow'

  def customize(self):
    self.css({
      'border-top': "6px solid %s" % self.page.body.style.globals.table.sorter_arrow_selected}, important=True)


class CssTabulatorSortNone(CssStyle.Style):
  classname = 'tabulator-col.tabulator-sortable[aria-sort=none] .tabulator-arrow'

  def customize(self):
    self.css({
      'border-bottom': "6px solid %s" % self.page.body.style.globals.table.sorter_arrow}, important=True)
