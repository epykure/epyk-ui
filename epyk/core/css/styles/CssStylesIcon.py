"""
CSS Style module for the Icons components
"""


from epyk.core.css.styles import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssIcon(CssStyle.Style):
  _attrs = {'margin': '4px 10px', 'cursor': 'pointer'}

  def customize(self):
    self.hover.css({"color": self.rptObj.theme.colors[5]})


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
  attrs = {'display': 'inline-block', 'margin': '0 5px 0 0', 'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.rptObj.theme.danger[1],
              'font-size': '%s%s' % (Defaults_css.Icon.small, Defaults_css.Icon.unit)})
    self.hover.css({"color": self.rptObj.theme.danger[1]})


class CssOutIcon(CssStyle.Style):
  attrs = {'display': 'inline-block', 'margin': '0 0 0 20px', 'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.rptObj.theme.danger[1],
              'font-size': '%s%s' % (Defaults_css.Icon.normal, Defaults_css.Icon.unit)})
    self.hover.css({"color": self.rptObj.theme.danger[1]})


class CssBigIcon(CssStyle.Style):
  attrs = {'display': 'inline-block', 'margin': '0 10px 0 10px', 'cursor': 'pointer'}

  def customize(self):
    self.css({"color": self.rptObj.theme.danger[1],
              'font-size': '%s%s' % (Defaults_css.Icon.big, Defaults_css.Icon.unit)})
    self.hover.css({"color": self.rptObj.theme.danger[1]})
