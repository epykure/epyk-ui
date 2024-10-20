#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.css.styles.classes import CssStyle


class CssAgHead(CssStyle.Style):
  classname = "ag-header-cell-label"

  def customize(self):
    self.css({
      'color': self.page.body.style.globals.table.header_color,
      'font-weight': 'bold',
      'padding': '0 0 0 5px',
      'background-color': self.page.body.style.globals.table.header_background})


class CssAgOddRow(CssStyle.Style):
  classname = 'ag-row-odd'

  def customize(self):
    self.css({'background-color': self.page.theme.greys[0]}, important=True)


class CssAgEvenRow(CssStyle.Style):
  classname = 'ag-row-even'

  def customize(self):
    self.css({'background-color': self.page.theme.colors[0]}, important=True)


class CssAgCellFocus(CssStyle.Style):
  classname = 'ag-cell-focus'

  def customize(self):
    self.css({'border': '1px solid %s' % self.page.theme.notch()}, important=True)


class CssAgRow(CssStyle.Style):
  classname = 'ag-row'

  def customize(self):
    self.css({"align-items": 'center', 'display': 'flex'}, important=True)


class CssAgCell(CssStyle.Style):
  classname = 'ag-cell'

  def customize(self):
    self.css({"align-items": 'center', 'display': 'flex', 'padding': '0 0 0 5px'}, important=True)


class CssAgFilter(CssStyle.Style):
  classname = 'ag-filter'

  def customize(self):
    self.css({
      "border": '1px solid %s' % self.page.theme.greys[3],
      'background-color': self.page.theme.greys[1], 'padding': '2px'})


class CssAgHeaderLabel(CssStyle.Style):
  classname = 'ag-cell-label-container'

  def customize(self):
    self.css({'background-color': self.page.theme.greys[2]},  important=True)


class CssAgMFilterPopup(CssStyle.Style):
  classname = 'ag-popup-child'

  def customize(self):
    self.css({'background-color': self.page.theme.greys[0]},  important=True)
