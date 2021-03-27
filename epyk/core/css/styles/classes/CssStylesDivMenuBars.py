#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.styles.classes import CssStyle


class CssSideBarMenu(CssStyle.Style):
  _attrs = {'display': 'block', 'width': '100%'}
  _hover = {'text-decoration': 'underline'}

  def customize(self):
    self.css({'color': self.page.theme.colors[-1]})


class CssSideBarFixed(CssStyle.Style):
  _attrs = {'height': '100%', 'width': '40px', 'text-align': 'center', 'position': 'fixed', 'padding': '60px 0 0 0',
            'z-index': 5, 'top': 0, 'left': 0, 'overflow-x': 'hidden'}

  def customize(self):
    self.css({'background-color': self.page.theme.colors[-1]})


class CssSideBarBubble(CssStyle.Style):
  _attrs = {'position': 'fixed', 'display': 'none', 'overflow-x': 'hidden', 'text-align': 'left',
            'height': '100%', 'min-width': '200px', 'padding': '10px', 'color': 'black'}

  def customize(self):
    self.css({'background-color': self.page.theme.colors[-1],
              'font-family': self.page.body.style.globals.font.family,
              'font-size': self.page.body.style.globals.font.normal()})


class CssSideBar(CssStyle.Style):
  _attrs = {'height': '100%', 'position': 'fixed', 'z-index': 5, 'left': 0, 'overflow-x': 'hidden',
            'padding-top': '15px'}


class CssSideBarLiHref(CssStyle.Style):
  _attrs = {'color': 'white', 'margin': 0, 'padding': 0}
  _selectors = {'child': 'li ul a'}

  def customize(self):
    self.css({'background-color': self.page.theme.colors[-1]})


class CssSideBarLi(CssStyle.Style):
  _attrs = {'color': 'white', 'list-style-type': 'none'}
  _selectors = {'child': 'li'}

  def customize(self):
    self.css({'background-color': self.page.theme.colors[-1]})


class CssParamsBar(CssStyle.Style):
  _attrs = {'vertical-align': 'middle', 'white-space': 'nowrap', 'overflow-x': 'auto', 'overflow-y': 'hidden',
            'padding': '2px 10px', 'z-index': 10, 'width': '100%', 'position': 'fixed', 'left': 0, 'margin': 0}

  def customize(self):
    self.css({'border-top': "1px solid %s" % self.page.theme.greys[6], 'background-color': self.page.theme.greys[0]})
