#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.styles.classes import CssStyle


class CssSearchExt(CssStyle.Style):
  _attrs = {'box-sizing': 'border-box', 'border-radius': '4px', 'width': '40px', 'background-repeat': 'no-repeat',
            'padding': '5px 0px', '-webkit-transition': 'width 0.4s ease-in-out', 'color': 'inherit',
            'transition': 'width 0.4s ease-in-out'}
  _focus = {'width': '350px', 'outline': 0}

  def customize(self):
    self.hover.css({
      'color': self.page.theme.greys[-1],
      'border-bottom-color': self.page.theme.notch(1)})


class CssSearch(CssStyle.Style):
  _attrs = {'width': 'auto', 'display': 'inline-block', 'border': 'none', 'background-repeat': 'no-repeat',
            'padding': '5px 0px'}
  _focus = {'outline': 0}

  def customize(self):
    self.css({
      "border-bottom-color": self.page.theme.greys[3],
      'color': self.page.theme.greys[-1]})
    self.hover.css({
      'color': self.page.theme.greys[-1],
      'border-bottom-color': self.page.theme.notch(1)})


class CssSearchButton(CssStyle.Style):
  _attrs = {'margin-top': '10px', 'margin-left': '10px', 'display': 'block', 'cursor': 'pointer',
            'position': 'absolute'}
  _selectors = {'child': 'i'}

  def customize(self):
    self.css({"color": self.page.theme.greys[5]})
