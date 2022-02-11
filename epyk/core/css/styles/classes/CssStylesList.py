#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.css.styles.classes import CssStyle


class CssBasicList(CssStyle.Style):
  _attrs = {'padding': '15px', 'font-size': '16px', 'font-weight': 'bold'}
  _selectors = {'child': 'ul li:first-child'}

  def customize(self):
    self.css({"background": self.page.theme.notch(2), "color": self.page.theme.greys[0]})


class CssBasicListItems(CssStyle.Style):
  _attrs = {'padding': '15px 0 0 0', 'display': 'block'}

  def customize(self):
    self.css({"color": self.page.theme.greys[-1], "border-bottom": "1px solid %s" % self.page.theme.notch(2)})
    self.hover.css({'color': self.page.theme.notch(3)})


class CssBasicListItemsSelected(CssStyle.Style):

  def customize(self):
    self.css({"color": self.page.theme.success[1]})


class CssBasicListItemsDisabled(CssStyle.Style):
  _attrs = {'padding': '15px 0 0 0', 'display': 'block', 'cursor': 'not-allowed'}

  def customize(self):
    self.css({"background-color": self.page.theme.notch(2), "color": self.page.theme.greys[4]})


class CssSquareList(CssStyle.Style):
  _attrs = {'list-style': 'none', 'text-align': 'justify'}
  _before = {'content': "'\\f0c8'", 'font-family': "'Font Awesome 5 Free'", 'padding': '0 5px 0 0'}
  _selectors = {'child': 'li'}

  def customize(self):
    self.before.css({"color": self.page.theme.notch(2)})


class CssListBase(CssStyle.Style):
  _attrs = {'width': '142px', 'min-height': '20px', 'list-style-type': 'none', 'margin': 0, 'padding': '5px 0 0 0',
            'float': 'left', 'margin-right': '10px'}

  def customize(self):
    self.hover.css({"border": "1px solid %s" % self.page.theme.greys[9]})


class CssListLiBase(CssStyle.Style):
  _attrs = {'margin': '0 5px 5px 5px', 'padding': '5px', 'width': '120px'}


class CssListNoDecoration(CssStyle.Style):
  _attrs = {'list-style': 'none', 'padding': '0 0 0 5px'}


class CssListLiUlContainer(CssStyle.Style):
  _attrs = {'display': 'none', 'width': '100%', 'padding': 0, 'margin': 0, 'overflow': 'hidden',
            'transition': 'height .2s ease-in-out'}
  cssId = {'direct': 'ul'}


class CssListLiSubItem(CssStyle.Style):
  _attrs = {'display': 'table', 'width': '100%', 'height': '30px', 'vertical-align': 'middle',
            'list-style-type': 'none', 'float': 'left', 'font-size': '12px', 'margin': 0}

  def customize(self):
    self.hover.css({"background": self.page.theme.greys[2]})


class CssListItemsBorder(CssStyle.Style):
  _selectors = {'child': 'li'}

  def customize(self):
    self.css({"border": "1px solid %s" % self.page.theme.greys[0], "padding-left": '5px'})
    self.hover.css({
      "border-bottom": "1px solid %s" % self.page.theme.colors[2],
      "border-top": "1px solid %s" % self.page.theme.colors[2],
    })


class CssListItemsBackground(CssStyle.Style):
  _selectors = {'child': 'li'}

  def customize(self):
    self.hover.css({
      "background": self.page.theme.colors[0],
      "color": "%s !IMPORTANT" % self.page.theme.colors[-1]})
