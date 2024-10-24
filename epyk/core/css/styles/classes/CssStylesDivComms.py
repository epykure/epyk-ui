#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.styles.classes import CssStyle


class CssCommHeader(CssStyle.Style):
  _attrs = {'font-weight': 'bold', 'display': 'block', 'text-align': 'left'}
  _selectors = {'child': 'span'}

  def customize(self):
    self.css({'color': self.page.theme.greys[-1],
              'font-family': self.page.body.style.globals.font.family,
              'font-size': self.page.body.style.globals.font.normal()})


class CssCommInput(CssStyle.Style):
  _attrs = {'border': 'none', 'width': '95%', 'margin': 0, 'padding': '5px'}
  _focus = {'outline': 0}

  _selectors = {'child': 'input'}

  def customize(self):
    self.css({'color': self.page.theme.greys[-1], 'background-color': self.page.theme.greys[0],
              'border-bottom': '1px solid %s' % self.page.theme.success.base,
              'font-family': self.page.body.style.globals.font.family,
              'font-size': self.page.body.style.globals.font.normal()})


class CssContentEditable(CssStyle.Style):
  classname = False
  _selector = "[contenteditable]"

  def customize(self):
    self.focus.css({'outline': "1px solid %s" % self.page.theme.notch()})


class CssSpeechBubble(CssStyle.Style):
  classname = "speech-bubble"
  _attrs = {"border-radius": '4px', 'margin': '0 auto 10px', 'padding': '5px', 'position': 'relative'}


class CssSpeechBubbleContent(CssStyle.Style):
  classname = "speech-bubble-ds"
  _attrs = {"border": '1px solid #a7a7a7', 'border-radius': '4px', 'box-shadow': '4px 4px 0 rgba(0, 0, 0, 0.2)',
            'display': 'inline-block', 'margin': '0 auto 40px', 'padding': '0 5px', 'position': 'relative'}


class CssSpeechBubbleArrow(CssStyle.Style):
  classname = "speech-bubble-ds__arrow"
  _attrs = {"border-left": '21px solid transparent', "border-top": '20px solid rgba(0, 0, 0, 0.2)',
            'bottom': '-25px', 'position': 'absolute', 'right': '10px'}
