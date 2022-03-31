#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.css.styles.classes import CssStyle


class CssTextBold(CssStyle.Style):
  _attrs = {'font-weight': 'bold'}


class CssFormula(CssStyle.Style):
  """
  CSS Style for the formulas component
  """
  _attrs = {'padding': 0, 'margin': 0}
  _focus = {'outline': 0, 'border': 'none', 'box-shadow': 'none'}
  classname = "math"


class CssTitle1(CssStyle.Style):
  _attrs = {'padding': '0 0 5px 0', 'font-weight': 'bold', 'text-transform': 'uppercase',
            'white-space': 'pre-wrap', 'border-bottom': '1px dashed black', 'border-width': '2px',
            'margin-bottom': '5px'}

  def customize(self):
    self.css({"color": self.page.theme.greys[-3], "border-color": self.page.theme.greys[-1]})


class CssTitle2(CssStyle.Style):
  _attrs = {'padding': 0, 'margin-top': '5px', 'font-weight': 'bold', 'text-transform': 'uppercase',
            'white-space': 'pre-wrap'}

  def customize(self):
    self.css({"color": self.page.theme.notch(2)})


class CssTitle3(CssStyle.Style):
  _attrs = {'padding': 0, 'margin-top': '5px', 'font-weight': 'bold', 'text-transform': 'uppercase',
            'white-space': 'pre-wrap'}

  def customize(self):
    self.css({"color": self.page.theme.notch(2), 'font-family': self.page.body.style.globals.font.family})


class CssTitle4(CssStyle.Style):
  _attrs = {'padding': 0, 'margin': '5px 0 0 0', 'font-weight': 'bold', 'width': '100%', 'white-space': 'pre-wrap'}

  def customize(self):
    self.css({"color": self.page.theme.greys[5]})


class CssTitle5(CssStyle.Style):
  _attrs = {'padding': 0, 'margin': '2px 0 0 0', 'font-weight': 'bold', 'width': '100%', 'white-space': 'pre-wrap'}


class CssTitle(CssStyle.Style):
  _attrs = {'padding': 0, 'margin-bottom': 0, 'white-space': 'pre-wrap', 'font-weight': 'bold'}


class CssNumberCenter(CssStyle.Style):
  _attrs = {'width': '100%', 'text-align': 'center', 'padding': 0, 'margin-bottom': 0, 'white-space': 'pre-wrap',
            'font-weight': 'bold'}

  def customize(self):
    self.css({'font-size': self.page.body.style.globals.font.normal(4),
              'font-family': self.page.body.style.globals.font.family})


class CssMarkRed(CssStyle.Style):
  _attrs = {'background': 'none'}

  def customize(self):
    self.css({"color": self.page.theme.danger.base,
              'font-size': self.page.body.style.globals.font.normal()})


class CssMarkBlue(CssStyle.Style):
  _attrs = {'background': 'none', 'font-weight': 'bold'}

  def customize(self):
    self.css({"color": self.page.theme.notch(2),
              'font-size': self.page.body.style.globals.font.normal()})


class CssTextWithBorder(CssStyle.Style):
  _attrs = {'border': '1px solid', 'padding': '5px', 'margin': '10px'}
  _selectors = {'child': 'fieldset'}

  def customize(self):
    self.css({"background-color": self.page.theme.greys[0]})


class CssCheckMark(CssStyle.Style):
  _attrs = {'text-align': 'center', 'display': 'inline-block',
            'font-family': 'FontAwesome', 'height': '18px', 'width': '18px'}

  def customize(self):
    self.css({"background-color": self.page.theme.greys[0], "color": self.page.theme.greys[-1]})
    self.hover.css({'color': 'white', 'background-color': self.page.theme.colors[-1]})


class CssTextItem(CssStyle.Style):
  _attrs = {'cursor': 'pointer', 'width': '200px', 'padding': '5px 5px 5px 20px'}

  def customize(self):
    self.hover.css({"color": self.page.theme.greys[-1], "background": self.page.theme.colors[2]})


class CssTextNotSelectable(CssStyle.Style):
  _attrs = {'-moz-user-select': 'none', "user-select": 'none', '-khtml-user-select': 'none',
            '-webkit-user-select': 'none', '-ms-user-select': 'none', "-o-user-select": 'none'}
