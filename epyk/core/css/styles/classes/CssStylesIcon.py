#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.styles.classes import CssStyle


class CssIcon(CssStyle.Style):
  _attrs = {'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.page.theme.colors[-1]})
    self.hover.css({"color": self.page.theme.notch()})


class CssStdIcon(CssStyle.Style):
  _attrs = {'cursor': 'pointer'}

  def customize(self):
    self.hover.css({"color": self.page.theme.success.base})


class CssSmallIcon(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'margin': '0 5px 0 0', 'cursor': 'pointer'}

  def customize(self):
    self.hover.css({"color": self.page.theme.notch(),
                    'font-size': self.page.body.style.globals.icon.small_size()})


class CssSmallIconRight(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'margin': '0 0 0 5px', 'cursor': 'pointer', 'float': 'right'}

  def customize(self):
    self.hover.css({"color": self.page.theme.notch(),
                    'font-size': self.page.body.style.globals.icon.small_size()})


class CssSmallIconRed(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'margin': '0 5px 0 0', 'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.page.theme.danger.base,
              'font-size': self.page.body.style.globals.icon.small_size()})
    self.hover.css({"color": self.page.theme.danger.base})


class CssOutIcon(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'margin': '0 0 0 20px', 'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.page.theme.danger.base,
              'font-size': self.page.body.style.globals.icon.normal_size()})
    self.hover.css({"color": self.page.theme.danger.base})


class CssBigIcon(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'margin': '0 10px 0 10px', 'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.page.theme.danger.base,
              'font-size': self.page.body.style.globals.icon.big_size()})
    self.hover.css({"color": self.page.theme.danger.base})


class CssIconSelected(CssStyle.Style):
  _attrs = {'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.page.theme.greys[-1]})
    self.active.css({"color": self.page.theme.danger.base})
