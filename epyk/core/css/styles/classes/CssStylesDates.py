#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.styles.classes import CssStyle


class CssDatePickerUI(CssStyle.Style):
  classname = "ui-datepicker"

  def customize(self):
    self.css({"background": self.page.theme.greys[0],
              "font-size": self.page.body.style.globals.font.normal(),
              'z-index': "220 !IMPORTANT", 'width': 'auto'})


class CssDatePicker(CssStyle.Style):
  _attrs = {'font-family': 'inherit', 'border': 'none', 'cursor': 'pointer', 'margin': 0,
            'padding': '2px', 'display': 'inline-block', 'border-radius': '5px', 'text-align': 'center'}
  _focus = {'outline': 0}

  def customize(self):
    self.css({"background": self.page.theme.greys[0],
              "color": self.page.theme.greys[-1],
              'border': '1px solid %s' % self.page.theme.colors[0]})
    self.hover.css({'color': self.page.theme.colors[-1]})


class CssDatesDatePickerHeader(CssStyle.Style):
  classname = "ui-widget-header"

  def customize(self):
    self.css({"background": self.page.theme.colors[0]})


class CssDatesTimePicker(CssStyle.Style):
  _attrs = {'margin': 0}
  classname = "ui-timepicker-standard"

  def customize(self):
    self.css({'color': self.page.theme.greys[-1], "background-color": self.page.theme.greys[0],
              "font-size": self.page.body.style.globals.font.normal()})


class CssDatesTimePickerState(CssStyle.Style):
  classname = "ui-timepicker-standard .ui-state-hover"

  def customize(self):
    self.css({"background-color": self.page.theme.colors[0]})

