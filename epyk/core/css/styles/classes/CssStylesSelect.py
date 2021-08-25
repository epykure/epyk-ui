#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.css.styles.classes import CssStyle
from epyk.core.html import Defaults as Defaults_html


class CssSelectStyle(CssStyle.Style):
  _attrs = {'padding-top': 0}
  _focus = {'outline': 0, 'border': 'none', 'box-shadow': 'none'}

  def customize(self):
    self.css({
      "background": 'inherit',
      'font-family': self.page.body.style.globals.font.family,
      'line-height': '%spx' % Defaults_html.LINE_HEIGHT,
      'font-size': self.page.body.style.globals.font.normal(), #'min-width': '%spx' % Defaults_html.INPUTS_MIN_WIDTH
    })
    self.css({'display': 'inline-block', 'margin': 0}, important=True)


class CssSelectButton(CssStyle.Style):
  _attrs = {'padding': 0, 'outline': 'none', 'border-color': 'none', 'box-shadow': 'none'}
  _focus = {'outline': 'none', 'border-color': 'none', 'box-shadow': 'none'}

  _selectors = {"child": '.btn'}

  def customize(self):
    self.css({"background-color": 'inherit', "border": 'none'})


class CssSelectSearchBoxInput(CssStyle.Style):
  _attrs = {"outline": 0, "margin-bottom": "5px"}
  _focus = {'outline': 0}

  classname = 'bs-searchbox'
  _selectors = {"child": 'input.form-control'}

  def customize(self):
    self.css({"border-color": self.page.theme.notch(), "height": "%spx" % Defaults_html.LINE_HEIGHT})
    self.focus.css({"box-shadow": "0 0 0 0.2em %s" % self.page.theme.colors[0]})


class CssSelectToggle(CssStyle.Style):

  def customize(self):
    self.css({
      "background-color": 'inherit',
      'font-size': 'inherit'}, important=True)


class CssSelectToggleNoBg(CssStyle.Style):

  def customize(self):
    self.css({'font-size': 'inherit'}, important=True)


class CssSelectOption(CssStyle.Style):
  classname = "dropdown-menu.show"

  def customize(self):
    self.css({
      'font-size': 'inherit',
      'z-index': 260,
      'background-color': self.page.theme.greys[0]}, important=True)


class CssSelectOptionItems(CssStyle.Style):
  _attrs = {"padding": "1px 15px 1px 5px"}
  classname = "dropdown-item"
  _focus = {'outline': 0}

  def customize(self):
    self.css({
      "z-index": 210,
      'line-height': '%spx' % Defaults_html.LINE_HEIGHT,
      'color': "inherit"}, important=True)
    self.hover.css({
      'color': self.page.theme.colors[0],
      "background-color": self.page.theme.notch(2)}, important=True)
    self.active.css({
      "background-color": self.page.theme.colors[-1],
      "color": self.page.theme.greys[0]}, important=True)


class CssSelectOptionActive(CssStyle.Style):
  classname = "active"

  def customize(self):
    self.css({
      'background': self.page.theme.notch(-1),
      "color": self.page.theme.colors[-1]}, important=True)


class CssSelectOptionSelected(CssStyle.Style):
  classname = "dropdown-menu > .active > a, .dropdown-menu > .active > a:hover, .dropdown-menu > .active > a:focus"

  def customize(self):
    self.css({
      'background-color': self.page.theme.notch(-1),
      "color": self.page.theme.greys[0]}, important=True)


class CssSelectFilterOption(CssStyle.Style):
  _attrs = {'text-align': 'center !IMPORTANT', 'padding-top': 0}
  classname = "filter-option"


class CssSelectOutline(CssStyle.Style):
  _focus = {'outline': '0 !important'}
  classnames = ["bootstrap-select", "dropdown-toggle"]


class CssSelectStatus(CssStyle.Style):
  classnames = ["dropdown-menu", "status"]

  def customize(self):
    self.css({
      "background-color": self.page.theme.greys[0],
      'font-size': self.page.body.style.globals.font.normal()})
