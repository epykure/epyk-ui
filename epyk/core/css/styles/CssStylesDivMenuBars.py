"""
CSS Style module for the common Menu Bar components
"""


from epyk.core.css.styles import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssSideBarMenu(CssStyle.CssCls):
  attrs = {'display': 'block', 'width': '100%'}
  hover = {'text-decoration': 'underline'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.rptObj.theme.colors[9]})


class CssSideBarFixed(CssStyle.CssCls):
  attrs = {'height': '100%', 'width': '40px', 'text-align': 'center', 'position': 'fixed', 'padding': '60px 0 0 0',
           'z-index': '5', 'top': '0', 'left': '0', 'overflow-x': 'hidden'}

  def customize(self, style, eventsStyles):
    style.update({'background-color': self.rptObj.theme.colors[9]})


class CssSideBarBubble(CssStyle.CssCls):
  attrs = {'position': 'fixed', 'display': 'none', 'overflow-x': 'hidden', 'text-align': 'left',
           'height': '100%', 'min-width': '200px', 'padding': '10px', 'color': 'black'}

  def customize(self, style, eventsStyles):
    style.update({'background-color': self.rptObj.theme.colors[9], 'font-family': Defaults_css.Font.family,
                  'font-size': '%spx' % Defaults_css.Font.size})


class CssSideBar(CssStyle.CssCls):
  attrs = {'height': '100%', 'position': 'fixed', 'z-index': '5', 'left': '0', 'overflow-x': 'hidden',
           'padding-top': '15px'}


class CssSideBarLiHref(CssStyle.CssCls):
  attrs = {'color': 'white', 'margin': '0', 'padding': '0'}
  cssId = {'child': 'li ul a'}

  def customize(self, style, eventsStyles):
    style.update({'background-color': self.rptObj.theme.colors[9]})


class CssSideBarLi(CssStyle.CssCls):
  attrs = {'color': 'white', 'list-style-type': 'none'}
  cssId = {'child': 'li'}

  def customize(self, style, eventsStyles):
    style.update({'background-color': self.rptObj.theme.colors[9]})


class CssParamsBar(CssStyle.CssCls):
  attrs = {'vertical-align': 'middle', 'white-space': 'nowrap', 'overflow-x': 'auto', 'overflow-y': 'hidden',
           'padding': '2px 10px', 'z-index': 10, 'width': '100%', 'position': 'fixed', 'left': 0, 'margin': 0}

  def customize(self, style, eventsStyles):
    style.update({'border-top': "1px solid %s" % self.rptObj.theme.greys[6]})
    style.update({'background-color': self.rptObj.theme.greys[0]})
