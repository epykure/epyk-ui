"""
Module in charge of the CSS Standard modules
"""

from epyk.core.css.styles.classes import CssStyle
from epyk.core.css import Defaults


class CssBody(CssStyle.Style):
  _attrs = {'top': 0, 'margin': '0 20px 0 20px'}
  cssId = {'tag': 'body'}

  def customize(self):
    if isinstance(Defaults.BACKGROUND, tuple):
      bg_color = self.rptObj.theme.greys[0]
      if bg_color != '#000000':
        bg_color = self.rptObj.theme.greys[2]
    else:
      bg_color = Defaults.BACKGROUND
    self.css({"background-color": bg_color, "color": self.rptObj.theme.greys[9], 'font-family':
      Defaults.Font.family, 'font-size': "%s%s" % (Defaults.Font.size, Defaults.Font.unit)})


class CssTextSelection(CssStyle.Style):
  def customize(self):
    self.css({"background": self.rptObj.theme.success[0]})


class CssBodyContent(CssStyle.Style):
  _attrs = {'margin-top': '10px', 'padding': '5px'}

  def customize(self):
    self.css({"background-color": self.rptObj.theme.greys[0], "border-radius": "5px",
              "border": '1px solid %s' % self.rptObj.theme.greys[3]})
    if Defaults.BODY_CONTAINER is not None:
      self.css(Defaults.BODY_CONTAINER)


class CssBodyLoadingBack(CssStyle.Style):
  _attrs = {'text-align': 'center', 'top': 0, 'left': 0, 'width': '100%', 'padding-top': '20%', 'height': '100%',
            'z-index': 295, 'position': 'fixed', 'opacity': 0.5, 'filter': 'alpha(opacity=50)'}

  def customize(self):
    self.css({"background-color": self.rptObj.theme.greys[5]})


class CssBodyLoading(CssStyle.Style):
  _attrs = {'text-align': 'center', 'top': 0, 'left': 0, 'width': '100%', 'position': 'fixed', 'padding-top': '10%',
            'height': '100%', 'display': 'none', 'z-index': 300}

  def customize(self):
    self.css({"color": self.rptObj.theme.greys[9]})


class CssNotSelect(CssStyle.Style):
  _attrs = {"-webkit-touch-callout": 'none', "user-select": 'none', "-webkit-user-select": 'none',
            "-khtml-user-select": 'none', "-moz-user-select": 'none', "-ms-user-select": 'none'}


class CssCloseSpan(CssStyle.Style):
  _attrs = {'float': 'right', 'text-align': 'right', 'font-size': '32px', 'z-index': 10, 'color': 'red',
            'position': 'relative', 'top': '-10px'}


class CssHoverReduce(CssStyle.Style):
  _hover = {"transform": 'scale(0.9)'}


class CssHoverZoom(CssStyle.Style):
  _hover = {"transform": 'scale(1.1)', 'z-index': 10}


class CssHoverRotate(CssStyle.Style):
  _hover = {"transform": 'rotate(10deg)', 'z-index': 10}

