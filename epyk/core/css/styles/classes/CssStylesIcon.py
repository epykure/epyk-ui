"""
CSS Style module for the Icons components
"""

from epyk.core.css.styles.classes import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssIcon(CssStyle.Style):
  _attrs = {'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.rptObj.theme.success[1]})
    self.hover.css({"color": self.rptObj.theme.colors[-1]})


class CssStdIcon(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'margin': '0 0 0 20px', 'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.rptObj.theme.colors[5],
              'font-size': '%s%s' % (Defaults_css.Icon.big, Defaults_css.Icon.unit)})
    self.hover.css({"color": self.rptObj.theme.colors[5]})


class CssSmallIcon(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'margin': '0 5px 0 0', 'cursor': 'pointer'}

  def customize(self):
    self.hover.css({"color": self.rptObj.theme.colors[5],
                    'font-size': '%s%s' % (Defaults_css.Icon.small, Defaults_css.Icon.unit)})


class CssSmallIconRight(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'margin': '0 0 0 5px', 'cursor': 'pointer', 'float': 'right'}

  def customize(self):
    self.hover.css({"color": self.rptObj.theme.colors[5],
                    'font-size': '%s%s' % (Defaults_css.Icon.small, Defaults_css.Icon.unit)})


class CssSmallIconRed(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'margin': '0 5px 0 0', 'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.rptObj.theme.danger[1],
              'font-size': '%s%s' % (Defaults_css.Icon.small, Defaults_css.Icon.unit)})
    self.hover.css({"color": self.rptObj.theme.danger[1]})


class CssOutIcon(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'margin': '0 0 0 20px', 'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.rptObj.theme.danger[1],
              'font-size': '%s%s' % (Defaults_css.Icon.normal, Defaults_css.Icon.unit)})
    self.hover.css({"color": self.rptObj.theme.danger[1]})


class CssBigIcon(CssStyle.Style):
  _attrs = {'display': 'inline-block', 'margin': '0 10px 0 10px', 'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.rptObj.theme.danger[1],
              'font-size': '%s%s' % (Defaults_css.Icon.big, Defaults_css.Icon.unit)})
    self.hover.css({"color": self.rptObj.theme.danger[1]})
