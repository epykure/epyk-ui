#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.styles.classes import CssStyle


class CssImgBasic(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'position': 'relative', 'height': 'auto', 'max-height': '100%',
            'max-width': '100%'}
  _selectors = {'child': 'img'}


class CssImgParagraph(CssStyle.Style):
  _attrs = {'transform': 'scale(1.1)', 'font-style': 'italic', 'padding': '10px', 'position': 'relative'}
  _hover = {'transition': 'all 0.2s linear'}
  _selectors = {'child': 'p'}

  def customize(self):
    self.css({'color': self.page.theme.colors[0]})


class CssImgH2(CssStyle.Style):
  _attrs = {'opacity': 0, 'transition': 'all 0.2s ease-in-out', 'text-transform': 'uppercase', 'text-align': 'center',
            'position': 'relative', 'padding': '10px', 'margin': '20px 0 0 0'}
  _hover = {'opacity': 1, 'transform': 'translateY(0px)'}
  _selectors = {'child': 'h2'}

  def customize(self):
    self.css({'color': self.page.theme.colors[0]})


class CssImgMask(CssStyle.Style):
  _attrs = {'opacity': 0, 'transition': 'all 0.4s ease-in-out', 'height': 'inherit', 'left': 1,
            'position': 'absolute'}
  _hover = {'opacity': 0.8}

  def customize(self):
    self.css({
      'background-color': self.page.theme.success[0],
      'border': '1px solid %s' % self.page.theme.success[1]})


class CssImgAInfo(CssStyle.Style):
  _attrs = {'opacity': 1, 'transition': 'all 0.2s ease-in-out', 'display': 'block', 'text-decoration': 'none',
            'padding': '7px 14px', 'text-transform': 'uppercase', 'box-shadow': '0 0 1px #000', "margin": '10px auto',
            'text-align': "center"}
  _hover = {'transform': 'translateY(0px)', 'box-shadow': '0 0 5px #000', 'transition-delay': '0.2s'}

  def customize(self):
    self.css({'background-color': self.page.theme.colors[0], 'color': self.page.theme.colors[-1]})


class CssImg(CssStyle.Style):
  _attrs = {'transition': 'all 0.2s linear', 'display': 'block', 'height': 'auto', 'margin': 'auto',
            'max-height': '100%', 'max-width': '100%', 'position': 'relative'}
  _hover = {'transform': 'scale(1.1)'}
  _selectors = {'child': 'img'}


class CssContent(CssStyle.Style):
  _attrs = {'width': '100%', 'height': '70%', 'position': 'absolute', 'overflow': 'hidden', 'top': '20%', 'left': 0}
  classname = 'content'


class CssView(CssStyle.Style):
  _attrs = {'height': '70%', 'margin': '10px', 'float': 'left', 'overflow': 'hidden', 'position': 'relative',
            'text-align': 'center', 'cursor': 'default'}

  def customize(self):
    self.css({'border': '1px solid %s' % self.page.theme.greys[5]})
    self.hover.css({'border': "1px solid %s" % self.page.theme.success[1]})


class CssCarrouselLi(CssStyle.Style):
  _attrs = {'list-style': 'none', 'display': 'none', 'padding': 0, 'margin': 0}
  _selectors = {'child': 'li'}


class CssCarrouselLabel(CssStyle.Style):
  _attrs = {'background': 'black', 'padding': '10px', 'border-radius': '50%', 'display': 'inline-block',
            'text-align': 'center'}
  _selectors = {'child': 'label'}


class CssCarrouselH2(CssStyle.Style):
  _attrs = {'position': 'absolute', 'top': '10px', 'padding': '10px'}
  _selectors = {'child': 'h2'}
