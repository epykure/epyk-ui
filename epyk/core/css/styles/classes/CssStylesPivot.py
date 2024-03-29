#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.css.styles.classes import CssStyle


class CssPivotHead(CssStyle.Style):
  classname = "pvtTable"
  _selectors = {'child': "tr th"}

  def customize(self):
    self.css({'color': self.page.theme.greys[-1], 'background-color': self.page.theme.colors[1]}, important=True)


class CssPivotCells(CssStyle.Style):
  classname = "pvtRows, .pvtCols"

  def customize(self):
    self.css({"background-color": self.page.theme.colors[0], 'color': self.page.theme.greys[-1],
              'border': '1px solid %s' % self.page.theme.colors[0]}, important=True)


class CssPivotLabel(CssStyle.Style):
  classname = "pvtColLabel, .pvtAxisLabel, .pvtRowLabel, .pvtTotalLabel,  th"

  def customize(self):
    self.css({'color': self.page.theme.greys[-1], 'background-color': self.page.theme.colors[1],
              'border': '1px solid %s' % self.page.theme.colors[1]}, important=True)


class CssPivotAxis(CssStyle.Style):
  _attrs = {'background': 'red'}
  classname = "pvtAxisContainer li span.pvtAttr, .c3-tooltip"

  def customize(self):
    self.css({
      'color': self.page.theme.greys[-1], 'background': self.page.theme.greys[0]}, important=True)


class CssPivotFilterBox(CssStyle.Style):
  classname = "pvtAxisContainer"

  def customize(self):
    self.css({
      'color': self.page.theme.greys[-1], 'border': '1px solid %s' % self.page.theme.colors[1]}, important=True)


class CssPivotFilterVals(CssStyle.Style):
  classname = "pvtVals, .pvtUiCell"

  def customize(self):
    self.css({
      'color': self.page.theme.greys[-1], 'background-color': self.page.theme.greys[0],
      'border': "1px solid %s" % self.page.theme.colors[1]})


class CssPivotFilterBoxPopUp(CssStyle.Style):
  classname = "pvtFilterBox"

  def customize(self):
    self.css({'color': self.page.theme.greys[-1], 'background-color': self.page.theme.greys[0]}, important=True)


class CssPivotFilterBoxPopUpHeader(CssStyle.Style):
  classname = "pvtFilterBox h4"

  def customize(self):
    self.css({'font-size': self.page.body.style.globals.font.normal(5), "margin": "2px 0"}, important=True)


class CssPivotFilterBoxPopUpButton(CssStyle.Style):
  classname = "pvtFilterBox button"

  _attrs = {'font-weight': 'bold', 'padding': '0 20px', 'margin': 0, 'text-decoration': 'none',
            'border-radius': '4px', 'white-space': 'nowrap', 'display': 'inline-block', 'line-height': '20px',
            '-webkit-appearance': 'none', '-moz-appearance': 'none'}
  _hover = {'text-decoration': 'none', 'cursor': 'pointer'}
  _focus = {'outline': 0}
  _disabled = {'cursor': 'none'}

  def customize(self):
    self.css({'border': '1px solid %s' % self.page.theme.greys[4], 'color': 'white',
              'background-color': self.page.theme.colors[-1]})
    self.hover.css({
      'background-color': self.page.theme.colors[0], 'color': self.page.theme.colors[-1]}, important=True)


class CssPivotFilterBoxPopUpCheck(CssStyle.Style):
  classname = "pvtCheckContainer p"
  _attrs = {"margin": 0}

  def customize(self):
    self.css({"font-size": self.page.body.style.globals.font.normal(), "vertical-align": "middle", "padding-bottom": 0})


class CssPivotFilterBoxPopUpCheckLabel(CssStyle.Style):
  classname = "pvtCheckContainer p label"
  _attrs = {"margin": 0}

  def customize(self):
    self.css({"font-size": self.page.body.style.globals.font.normal()})
