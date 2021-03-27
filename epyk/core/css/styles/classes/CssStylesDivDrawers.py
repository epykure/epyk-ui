#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.styles.classes import CssStyle


class CssDrawer(CssStyle.Style):
  _selectors = {'child': 'div[name="drawer"]'}

  _attrs = {"position": "absolute", 'top': 0, 'height': '100%', 'overflow-x': 'hidden'}


class CssDrawerNav(CssStyle.Style):
  _selectors = {'child': 'div[name="drawer_nav"]'}

  _attrs = {"width": '100%', 'height': '30px', "background": 'blue', 'display': 'block'}


class CssDrawerHandle(CssStyle.Style):
  _selectors = {'child': 'div[name="drawer_handle"]'}

  _attrs = {"width": "10px", 'height': '100%', 'display': 'inline-block'}
  _after = {'position': 'absolute', 'top': '50%', 'padding': '2px', 'height': '100%'}

  def customize(self):
    self.css({'background-color': self.page.theme.colors[-1]})


class CssDrawerContent(CssStyle.Style):
  _selectors = {'child': 'div[name="drawer_content"]'}

  _attrs = {'height': '100%', 'display': 'inline-block'}

  def customize(self):
    self.css({'background-color': self.page.theme.colors[0]})
