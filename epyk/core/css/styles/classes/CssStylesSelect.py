#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.styles.classes import CssStyle
from epyk.core.html import Defaults as Defaults_html
from epyk.core.css import Defaults as Defaults_css


class CssSelectStyle(CssStyle.Style):
  _attrs = {'padding-top': '2px'}
  _focus = {'outline': 0, 'border': 'none', 'box-shadow': 'none'}

  def customize(self):
    self.css({"background": self.rptObj.theme.greys[0], "color": self.rptObj.theme.greys[-1],
              'font-family': Defaults_css.Font.family, 'line-height': '%spx' % Defaults_html.LINE_HEIGHT,
              'font-size': '%spx' % Defaults_css.Font.size, #'min-width': '%spx' % Defaults_html.INPUTS_MIN_WIDTH
              })
    self.css({'display': 'inline-block', 'margin': 0}, important=True)


class CssSelectButton(CssStyle.Style):
  _attrs = {'padding': '0 5px', 'outline': 'none', 'border-color': 'none', 'box-shadow': 'none'}
  _focus = {'outline': 'none', 'border-color': 'none', 'box-shadow': 'none'}

  _selectors = {"child": '.btn'}

  def customize(self):
    self.css({"background-color": self.rptObj.theme.colors[0], "border": 'none', 'color': self.rptObj.theme.colors[-1]})


class CssSelectSearchBoxInput(CssStyle.Style):
  _attrs = {"outline": 0, "margin-bottom": "5px"}
  _focus = {'outline': 0}

  classname = 'bs-searchbox'
  _selectors = {"child": 'input.form-control'}

  def customize(self):
    self.css({"border-color": self.rptObj.theme.colors[5], "height": "%spx" % Defaults_html.LINE_HEIGHT})
    self.focus.css({"box-shadow": "0 0 0 0.2em %s" % self.rptObj.theme.colors[0]})


class CssSelectToggle(CssStyle.Style):

  def customize(self):
    self.css({"background-color": self.rptObj.theme.colors[0], 'font-size': '%s%s' % (Defaults_css.Font.size, Defaults_css.Font.unit)}, important=True)


class CssSelectToggleNoBg(CssStyle.Style):

  def customize(self):
    self.css({'font-size': '%s%s' % (Defaults_css.Font.size, Defaults_css.Font.unit)}, important=True)


class CssSelectOption(CssStyle.Style):
  classname = "dropdown-menu"

  def customize(self):
    self.css({'font-size': '%s%s' % (Defaults_css.Font.size, Defaults_css.Font.unit)}, important=True)


class CssSelectOptionItems(CssStyle.Style):
  _attrs = {"margin": 0, "padding": "0 5px"}
  classname = "dropdown-item"
  _focus = {'outline': 0}

  def customize(self):
    self.css({'line-height': '%spx' % Defaults_html.LINE_HEIGHT, 'color': self.rptObj.theme.greys[-1]}, important=True)
    self.hover.css({'color': self.rptObj.theme.success[1]}, important=True)
    self.active.css({"background-color": self.rptObj.theme.success[1]})


class CssSelectOptionActive(CssStyle.Style):
  classname = "active"

  def customize(self):
    self.css({'background': self.rptObj.theme.success[0], "color": self.rptObj.theme.success[1]}, important=True)


class CssSelectOptionSelected(CssStyle.Style):
  classname = "selected"

  def customize(self):
    self.css({'background': self.rptObj.theme.success[0], "color": self.rptObj.theme.success[1]}, important=True)


class CssSelectFilterOption(CssStyle.Style):
  _attrs = {'text-align': 'center !IMPORTANT'}
  classname = "filter-option"


class CssSelectOutline(CssStyle.Style):
  _focus = {'outline': '0 !important'}
  classnames = ["bootstrap-select", "dropdown-toggle"]


class CssSelectStatus(CssStyle.Style):
  classnames = ["dropdown-menu", "status"]

  def customize(self):
    self.css({"background-color": self.rptObj.theme.greys[0], 'font-size': '%s%s' % (Defaults_css.Font.size, Defaults_css.Font.unit)})
