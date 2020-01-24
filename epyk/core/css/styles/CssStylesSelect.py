"""
CSS Styles for all the select components
"""

from epyk.core.css.styles import CssStyle
from epyk.core.html import Defaults as Defaults_html
from epyk.core.css import Defaults as Defaults_css


class CssSelectStyle(CssStyle.CssCls):
  attrs = {'padding-top': '2px', 'display': 'inline-block !IMPORTANT', 'margin': '0 !IMPORTANT'}
  focus = {'outline': 0, 'border': 'none', 'box-shadow': 'none'}

  def customize(self, style, eventsStyles):
    style.update({"background": self.rptObj.theme.greys[0], "color": self.rptObj.theme.greys[-1],
                  'font-family': Defaults_css.Font.family, 'line-height': '%spx' % Defaults_html.LINE_HEIGHT,
                  'font-size': '%spx' % Defaults_css.Font.size, 'min-width': '%spx' % Defaults_html.INPUTS_MIN_WIDTH})


class CssSelectButton(CssStyle.CssCls):
  attrs = {'padding': '0 5px', 'outline': 'none !IMPORTANT', 'border-color': 'none', 'box-shadow': 'none'}
  focus = {'outline': 'none !IMPORTANT', 'border-color': 'none', 'box-shadow': 'none'}
  cssId = {'reference': ".btn"}

  def customize(self, style, eventsStyles):
    style.update({"background-color": self.rptObj.theme.colors[0], "border": 'none',
                  'color': self.rptObj.theme.colors[-1]})


class CssSelectSearchBox(CssStyle.CssCls):
  attrs = {"padding": "0 2px 1px 2px"}
  cssId = {'reference': ".bs-searchbox"}


class CssSelectSearchBoxInput(CssStyle.CssCls):
  attrs = {"outline": 0, "margin-bottom": "10px"}
  cssId = {'reference': ".bs-searchbox input.form-control"}
  focus = {'outline': 0}

  def customize(self, style, eventsStyles):
    style.update({"border-color": self.rptObj.theme.colors[0], "height": "%spx" % Defaults_html.LINE_HEIGHT})
    eventsStyles['focus'].update({"box-shadow": "0 0 0 0.2em %s" % self.rptObj.theme.colors[0]})


class CssSelectOption(CssStyle.CssCls):
  cssId = {'reference': ".dropdown-menu"}

  def customize(self, style, eventsStyles):
    style.update({"background": self.rptObj.theme.greys[0], 'font-size': '%spx' % Defaults_css.Font.size})


class CssSelectOptionItems(CssStyle.CssCls):
  attrs = {"margin": 0, "padding": "0 5px", "border-radius": '0 !IMPORTANT'}
  cssId = {'reference': ".dropdown-item"}


class CssSelectOptionHover(CssStyle.CssCls):
  cssId = {'reference': ".dropdown-menu li a"}

  def customize(self, style, eventsStyles):
    style.update({"color": self.rptObj.theme.greys[-1]})
    eventsStyles['hover'].update({'background': self.rptObj.theme.success[0], "color": "black"})


class CssSelectOptionActive(CssStyle.CssCls):
  cssId = {'reference': ".active"}

  def customize(self, style, eventsStyles):
    style.update({'background': self.rptObj.theme.success[0], "color": self.rptObj.theme.success[1]})


class CssSelectFilterOption(CssStyle.CssCls):
  attrs = {'text-align': 'center !IMPORTANT'}
  cssId = {'reference': ".filter-option"}


class CssSelectOutline(CssStyle.CssCls):
  focus = {'outline': '0 !important'}
  cssId = {'reference': ".bootstrap-select .dropdown-toggle"}


class CssSelectStatus(CssStyle.CssCls):
  cssId = {'reference': ".dropdown-menu .status"}

  def customize(self, style, eventsStyles):
    style.update({"background-color": self.rptObj.theme.greys[0], 'font-size': '%spx' % Defaults_css.Font.size})
