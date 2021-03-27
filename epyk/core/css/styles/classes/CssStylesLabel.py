#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.css.styles.classes import CssStyle


class CssLabelContainerDisabled(CssStyle.Style):
  _attrs = {'color': 'red', 'cursor': 'not-allowed'}

  def customize(self):
    self.css({'color': self.page.theme.danger[1]})


class CssLabelCheckMarkHover(CssStyle.Style):
  _selectors = {'child': "label"}

  def customize(self):
    self.hover.css({'background-color': self.page.theme.notch()})
