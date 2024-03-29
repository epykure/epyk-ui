#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.styles.classes import CssStyle


class CssDivNoMargin(CssStyle.Style):
  _attrs = {'margin': 0, 'padding': 0}


class CssDivNoBorder(CssStyle.Style):
  _attrs = {'margin': 0, 'clear': 'both', 'padding': 0, 'border': 0}

  def customize(self):
    self.focus.css({"outline": '1px solid %s' % self.page.theme.greys[4]})


class CssDivBottomBorder(CssStyle.Style):
  def customize(self):
    self.css({"border-bottom": '2px solid %s' % self.page.theme.colors[0],
              'font-family': self.page.body.style.globals.font.family})
    self.hover.css({"border-bottom": '2px solid %s' % self.page.theme.success.base})


class CssDivWithBorder(CssStyle.Style):
  _attrs = {'margin': '0 0 5px 0', 'padding': '5px', 'outline': 'none'}

  def customize(self):
    self.css({'border': "1px solid %s" % self.page.theme.colors[0],
              'font-family': self.page.body.style.globals.font.family})


class CssDivConsole(CssStyle.Style):
  _attrs = {'margin': 0, 'padding': '5px', 'border': 0, 'outline': 'none'}
  
  def customize(self):
    self.css({'background-color': self.page.theme.greys[9]})


class CssDivCursor(CssStyle.Style):
  _attrs = {'cursor': 'pointer'}


class CsssDivBoxMarginVertical(CssStyle.Style):
  _attrs = {'margin': "5px 0"}


class CsssDivBoxMarginBorder(CssStyle.Style):
  _attrs = {'margin': 0, 'padding': '0 2px 0 2px', 'white-space': 'pre-wrap'}

  def customize(self):
    self.css({"border": '1px solid %s' % self.page.theme.greys[0],
              'font-family': self.page.body.style.globals.font.family})
    self.hover.css({'border': "1px solid %s" % self.page.theme.greys[5]})


class CssDivBoxCenter(CssStyle.Style):
  _attrs = {'width': '100%', 'text-align': 'center'}


class CssDivBoxWithDotBorder(CssStyle.Style):
  _attrs = {'margin': '5px'}

  def customize(self):
    self.css({"border": '1px dashed %s' % self.page.theme.greys[9]})


class CssDivBubble(CssStyle.Style):
  _attrs = {'margin-left': 'auto', 'margin-right': 'auto', 'border-radius': '50%',
            'text-align': 'center'}

  def customize(self):
    self.css({"border": '1px solid %s' % self.page.theme.greys[5]})


class CssDivLeft(CssStyle.Style):
  _attrs = {'float': 'left', 'width': '20%'}


class CssDivRight(CssStyle.Style):
  _attrs = {'float': 'right', 'width': '80%'}


class CssDivBorder(CssStyle.Style):

  def customize(self):
    self.hover.css({"border": "1px solid %s" % self.page.theme.greys[9]})


class CssDivShadow(CssStyle.Style):
  _attrs = {'box-shadow': '10px 10px 8px 10px #888888'}


class CssDivBanner(CssStyle.Style):
  _attrs = {'width': '100%', 'margin': 0, 'overflow-y': 'auto', 'padding': '10px'}

  def customize(self):
    self.css({'background-color': self.page.theme.greys[0]})


class CssDivSubBanner(CssStyle.Style):
  _attrs = {'height': '400px', 'width': '100%', 'overflow-y': 'auto', 'margin-top': '50px', 'padding': 0, 'margin': 0}

  def customize(self):
    self.css({'color': self.page.theme.greys[9], 'background-color': self.page.theme.greys[0]})


class CssDivLabelPoint(CssStyle.Style):
  _attrs = {'padding': '10px', 'margin-top': '20px', 'margin-left': '5px', 'border-radius': '50%', 'cursor': 'pointer',
            'display': 'inline-block'}
  cssId = {'child': 'label'}

  def customize(self):
    self.css({"border": '1px solid %s' % self.page.theme.greys[4], 'background': self.page.theme.greys[0]})
    self.hover.css({"border": '1px solid %s' % self.page.theme.success.base})


class CssDivCommBubble(CssStyle.Style):
  _attrs = {'width': '100%', 'vertical-align': 'top', 'top': 0, 'margin-bottom': '20px', 'margin-left': '20px',
            'display': 'inline-block'}
  _before = {'content': "''", 'width': 0, 'height': 0, 'display': 'inline-block', 'border': '15px solid transparent',
             'margin-left': '-30px'}

  def customize(self):
    self.css({'color': self.page.theme.greys[0]})
    self.before.css({'border-right-color': self.page.theme.colors[9]})


class CssDivComms(CssStyle.Style):
  _attrs = {'margin-top': '10px', 'padding': '5px'}


class CssDivLoading(CssStyle.Style):
  _attrs = {'opacity': 0.5, 'filter': 'alpha(opacity=50)', 'padding': '5px', 'text-align': 'center'}


class CssDivHidden(CssStyle.Style):
  _attrs = {'display': 'none'}


class CssDivTextLeft(CssStyle.Style):
  _attrs = {'text-align': 'left'}


class CssDivTableContent(CssStyle.Style):
  _attrs = {'padding': '5px 10px 5px 10px', 'width': 'auto', 'display': 'inline-block'}

  def customize(self):
    self.css({'border': '1px solid %s' % self.page.theme.greys[3], 'background-color': self.page.theme.greys[0]})


class CssDivPagination(CssStyle.Style):
  _attrs = {'margin': 'auto', 'padding': '8px 16px', 'text-decoration': 'none', 'transition': 'background-color .3s'}
  _selectors = {'child': 'a'}

  def customize(self):
    self.css({'color': self.page.theme.greys[9]})
    self.hover.css({"background-color": self.page.theme.greys[3]})


class CssDivEditor(CssStyle.Style):
  _attrs = {'overflow': 'hidden', 'white-space': 'pre', 'display': 'block', 'padding': '30px 10px 10px 10px',
            'margin-top': '5px', 'text-align': 'left'}

  def customize(self):
    self.css({
      'border': "1px solid %s" % self.page.theme.greys[3],
      'background-color': self.page.theme.greys[2]})
    self.focus.css({
      'background-color': self.page.theme.greys[0],
      'border': "2px solid %s" % self.page.theme.notch()})


class CssDivRow(CssStyle.Style):

  def customize(self):
    self.hover.css({'background-color': self.page.theme.greys[1]})


class CssPanelTitle(CssStyle.Style):
  _attrs = {'padding': '1px 0', 'margin': '0 5px 5px 5px', 'font-weight': 'bold'}

  def customize(self):
    self.css({'border-bottom': "1px solid %s" % self.page.theme.success.base,
              'font-size': self.page.body.style.globals.font.header(),
              'font-family': self.page.body.style.globals.font.family})


class CssDivFilter(CssStyle.Style):
  _attrs = {"padding": "5px"}

  def customize(self):
    self.css({'border': '1px solid %s' % self.page.theme.colors[0]})


class CssDivFilterItems(CssStyle.Style):
  def customize(self):
    self.css({'border': '1px solid %s' % self.page.theme.colors[2]})
    self.hover.css({'border': '1px solid %s' % self.page.theme.success.base})


class CssDivModal(CssStyle.Style):
  _attrs = {'z-index': 100, 'position': 'fixed', 'padding-top': '100px', 'left': 0, 'top': 0,
            'width': '100%', 'height': '100%', 'overflow': 'auto', 'text-align': 'center'}


class CssDivModalContent(CssStyle.Style):
  _attrs = {'margin': '10%', 'padding': '5px 5px 5px 5px', 'border': '1px solid #888', 'width': '75%',
            'box-shadow': '0 19px 38px rgba(0, 0, 0, 0.12), 0 15px 12px rgba(0, 0, 0, 0.22)',
            'display': 'inline-flex', 'flex-direction': 'column'}

  def customize(self):
    self.css({'background-color': self.page.theme.greys[0]})
    self.animation('epyk_modal_animatetop', {
      '0%': {'top': '-300px', 'opacity': '0'}, '100%': {'top': '0px', 'opacity': '1'}}, 0.7, iteration=1)


class CssDivStepper(CssStyle.Style):
  _selectors = {'child': 'li'}

  _attrs = {'float': 'left', 'text-align': 'center'}


class CssDivVerticalRotate(CssStyle.Style):
  _selectors = {'child': '.inner-flip'}

  _hover = {'transform': 'rotateX(180deg)'}


class CssDivHorizontalRotate(CssStyle.Style):
  _selectors = {'child': '.inner-flip'}

  _hover = {'transform': 'rotateY(180deg)'}


class CssDivNoFocusOutline(CssStyle.Style):
  _focus = {'outline': 0}


class CssDivCutCorner(CssStyle.Style):
  _attrs = {"position": 'relative'}
  _before = {'content': "''", 'position': 'absolute', 'top': "-4px",
             'right': "-4px", 'width': 0}

  def customize(self):
    self.before.css({
      'border-top': '20px solid %s' % self.page.theme.greys[0],
      'border-left': '20px solid %s' % self.page.theme.colors[2],
    })
