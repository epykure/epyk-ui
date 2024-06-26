#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Defaults as Defaults_html
from epyk.core.css.styles.classes import CssStyle


BORDER_1PX_EXPR = '1px solid {}'


class CssInput(CssStyle.Style):
  """  CSS Base style for the input components.
  """
  _attrs = {'border': 'none', 'cursor': 'text', 'margin': 0}
  _focus = {'outline': 0}

  def customize(self):
    self.attrs.css({'color': 'inherit',
                    'font-family': self.page.body.style.globals.font.family,
                    'line-height': '%spx' % Defaults_html.LINE_HEIGHT,
                    'text-align': Defaults_html.INPUTS_POSITION,
                    'border': BORDER_1PX_EXPR.format(self.page.theme.colors[0]),
                    'font-size': self.page.body.style.globals.font.normal()})
    self.hover.css({
      'color': self.page.theme.notch(1),
      'border': '1px solid %s' % self.page.theme.notch(-3),
    })


class CssInputBottom(CssStyle.Style):
  """  CSS Base style for the input components.
  """
  _attrs = {'border': 'none', 'text-align': 'center', 'cursor': 'text', 'margin': 0}
  _focus = {'outline': 0}

  def customize(self):
    self.attrs.css({'color': 'inherit',
                    'font-family': self.page.body.style.globals.font.family,
                    'line-height': '%spx' % Defaults_html.LINE_HEIGHT,
                    'border-bottom': BORDER_1PX_EXPR.format(self.page.theme.colors[0]),
                    'font-size': self.page.body.style.globals.font.normal()})
    self.hover.css({
      'color': self.page.theme.notch(1),
      'border-bottom': '1px solid %s' % self.page.theme.notch(1),
    })


class CssInputNoBorder(CssStyle.Style):
  """  CSS Base style for the input components.
  """
  _attrs = {'border': 'none', 'text-align': 'center', 'cursor': 'text', 'margin': 0}
  _focus = {'outline': 0}

  def customize(self):
    self.attrs.css({'color': 'inherit',
                    'font-family': self.page.body.style.globals.font.family,
                    'line-height': '%spx' % Defaults_html.LINE_HEIGHT,
                    'font-size': self.page.body.style.globals.font.normal()})
    self.hover.css({
      'color': self.page.theme.notch(1),
    })


class CssInputRange(CssStyle.Style):
  """  CSS Style for the input range component.
  """
  _attrs = {'-webkit-appearance': 'none', 'appearance': 'none', 'outline': 'none', 'opacity': 0.7,
            '-webkit-transition': '.2s', 'transition': 'opacity .2s', 'cursor': 'pointer'}
  _hover = {'opacity': 1}
  _selectors = {'child': 'input'}

  def customize(self):
    self.attrs.css({"background": self.page.theme.colors[0]})


class CssInputNumberNoInnerScroll(CssStyle.Style):
  """
  Description:
  ------------

  """
  _attrs = {'-webkit-appearance': 'none', "margin": 0}
  _selectors = {'child': 'input::-webkit-inner-spin-button'}


class CssInputNumberNoOuterScroll(CssStyle.Style):
  """
  Description:
  ------------

  """
  _attrs = {'-webkit-appearance': 'none', "margin": 0}
  _selectors = {'child': 'input::-webkit-outer-spin-button'}


class CssInputNumberNoScroll(CssStyle.Style):
  """
  Description:
  ------------

  """
  _attrs = {'-moz-appearance': 'textfield'}
  _selectors = {'child': 'input[type=number]'}


class CssInputRangeThumb(CssStyle.Style):
  """  CSS Style for the thumb of the input range component.
  """
  _attrs = {'-webkit-appearance': 'none', 'appearance': 'none', 'cursor': 'pointer'}
  _webkit_slider_thumb = {'-webkit-appearance': 'none', 'appearance': 'none', 'cursor': 'pointer'}
  _selectors = {'child': 'input'}

  def customize(self):
    self.webkit_slider_thumb.css({
      "background": self.page.theme.colors[-1],
      'width': '%spx' % Defaults_html.INPUTS_RANGE_THUMB,
      'height': '%spx' % Defaults_html.INPUTS_RANGE_THUMB})


class CssInputLabel(CssStyle.Style):
  """  CSS Style for the label attached to an input component.
  """
  _attrs = {'line-height': '1.5', 'margin-left': '10px'}
  _selectors = {'child': 'label'}

  def customize(self):
    self.attrs.css({'font-family': self.page.body.style.globals.font.family,
                    'font-size': self.page.body.style.globals.font.normal()})


class CssInputInteger(CssStyle.Style):
  """
  Description:
  ------------

  """
  cssId = {'reference': 'input[type=number]::-webkit-inner-spin-button, input[type=number]::-webkit-outer-spin-button'}
  _attrs = {"-webkit-appearance": 'none', "margin": 0}


class CssInputText(CssStyle.Style):
  """  CSS Style for the input text component (within a field object).
  """
  _attrs = {'margin-left': '10px'}
  _selectors = {'child': 'input'}


class CssInputTextArea(CssStyle.Style):
  """  CSS Style for the textarea component.
  """
  _attrs = {'resize': 'none', 'margin-bottom': '5px', 'padding': '5px'}
  _focus = {'outline': 0}

  def customize(self):
    self.css({"background-color": self.page.theme.greys[1], "color": self.page.theme.greys[-1],
              'border': BORDER_1PX_EXPR.format(self.page.theme.colors[4])})
    self.hover.css({'color': self.page.theme.greys[-1]})


class CssInputValid(CssStyle.Style):

  def customize(self):
    self.valid.css({"color": self.page.theme.success.base})
    self.invalid.css({"color": self.page.theme.danger.base, "border": "1px solid %s" % self.page.theme.danger.base})


class CssUIActive(CssStyle.Style):
  classname = "ui-state-active"

  def customize(self):
    self.css({"border": BORDER_1PX_EXPR.format(self.page.theme.notch(-3)),
              'background-color': self.page.theme.notch()}, important=True)
    self.hover.css({"border": BORDER_1PX_EXPR.format(self.page.theme.notch(-1)),
                    'background-color': self.page.theme.notch()})


class CssUISlider(CssStyle.Style):
  classname = "ui-slider-handle"
  _focus = {'outline': 0}


class CssUIWidgetHeader(CssStyle.Style):
  classname = "ui-widget-header"

  def customize(self):
    self.css({'background': self.page.theme.notch()}, important=True)


class CssUIMenuActive(CssStyle.Style):
  classname = "ui-state-active"

  def customize(self):
    self.css({"border": BORDER_1PX_EXPR.format(self.page.theme.notch()),
              'background-color': self.page.theme.notch()}, important=True)
    self.hover.css({"border": BORDER_1PX_EXPR.format(self.page.theme.notch()),
                    'background-color': self.page.theme.notch()})


class CssAutocomplete(CssStyle.Style):
  classname = "ui-autocomplete"

  def customize(self):
    self.css({
      "z-index": 220, 'background-color': self.page.theme.colors[0], 'color': self.page.theme.greys[5]}, important=True)


class CssAutocompleteMenu(CssStyle.Style):
  classname = "ui-menu"

  def customize(self):
    self.css({'border': self.page.theme.greys[0]}, important=True)


class CssAutocompleteItemActive(CssStyle.Style):
  classname = "ui-menu .ui-state-active"

  def customize(self):
    self.css({
      'border': BORDER_1PX_EXPR.format(self.page.theme.greys[4]),
      'background': self.page.theme.notch(2),
      "color":  self.page.theme.greys[0]}, important=True)
