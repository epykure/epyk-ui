#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.css.styles.classes import CssStyle


class CssDefaultTab(CssStyle.Style):
  _attrs = {'margin': 0}

  def customize(self):
    self.css({'background-color': self.page.theme.greys[0], 'color': self.page.theme.colors[-1]})


class CssDefaultTabSelected(CssStyle.Style):

  def customize(self):
    self.css({'background-color': self.page.theme.colors[-1], 'color': self.page.theme.colors[0]})


class CssBorderTab(CssStyle.Style):
  _attrs = {'margin': '0 0 5px 0'}

  def customize(self):
    self.css({
      'border-bottom': 'None', 'background-color': self.page.theme.greys[0],
      'color': self.page.theme.colors[-1]})


class CssBorderTabSelected(CssStyle.Style):

  def customize(self):
    self.css({'border-bottom': "3px solid %s" % self.page.theme.success[1]}, important=True)
