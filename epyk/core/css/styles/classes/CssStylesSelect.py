"""
CSS Styles for all the select components
"""

from epyk.core.css.styles.classes import CssStyle
from epyk.core.html import Defaults as Defaults_html
from epyk.core.css import Defaults as Defaults_css


class CssSelectStyle(CssStyle.Style):
  _attrs = {'padding-top': '2px'}
  _focus = {'outline': 0, 'border': 'none', 'box-shadow': 'none'}

  def customize(self):
    self.css({"background": self.rptObj.theme.greys[0], "color": self.rptObj.theme.greys[-1],
              'font-family': Defaults_css.Font.family, 'line-height': '%spx' % Defaults_html.LINE_HEIGHT,
              'font-size': '%spx' % Defaults_css.Font.size, 'min-width': '%spx' % Defaults_html.INPUTS_MIN_WIDTH})
    self.css({'display': 'inline-block', 'margin': 0}, important=True)


class CssSelectButton(CssStyle.Style):
  _attrs = {'padding': '0 5px', 'outline': 'none', 'border-color': 'none', 'box-shadow': 'none'}
  _focus = {'outline': 'none', 'border-color': 'none', 'box-shadow': 'none'}
  classname = 'btn'

  def customize(self):
    self.css({"background-color": self.rptObj.theme.colors[0], "border": 'none', 'color': self.rptObj.theme.colors[-1]})


class CssSelectSearchBox(CssStyle.Style):
  _attrs = {"padding": "0 2px 1px 2px"}
  classname = "bs-searchbox"


class CssSelectSearchBoxInput(CssStyle.Style):
  _attrs = {"outline": 0, "margin-bottom": "10px"}
  _focus = {'outline': 0}

  classname = 'bs-searchbox'
  _selectors = {"child": 'input.form-control'}

  def customize(self):
    self.css({"border-color": self.rptObj.theme.colors[0], "height": "%spx" % Defaults_html.LINE_HEIGHT})
    self.focus.css({"box-shadow": "0 0 0 0.2em %s" % self.rptObj.theme.colors[0]})


class CssSelectOption(CssStyle.Style):
  classname = "dropdown-menu"

  def customize(self):
    self.css({"background": self.rptObj.theme.greys[0],
              'font-size': '%s%s' % (Defaults_css.Font.size, Defaults_css.Font.unit)})


class CssSelectOptionItems(CssStyle.Style):
  attrs = {"margin": 0, "padding": "0 5px"}
  classname = "dropdown-item"


class CssSelectOptionHover(CssStyle.Style):
  classname = "dropdown-menu"
  _selectors = {"child": "li a"}

  def customize(self):
    self.css({"color": self.rptObj.theme.greys[-1]})
    self.css({"border-radius": 0}, important=True)
    self.hover.css({'background': self.rptObj.theme.success[0], "color": "black"})


class CssSelectOptionActive(CssStyle.Style):
  classname = "active"

  def customize(self):
    self.css({'background': self.rptObj.theme.success[0], "color": self.rptObj.theme.success[1]})


class CssSelectFilterOption(CssStyle.Style):
  _attrs = {'text-align': 'center !IMPORTANT'}
  classname = "filter-option"


class CssSelectOutline(CssStyle.Style):
  _focus = {'outline': '0 !important'}
  classnames = ["bootstrap-select", "dropdown-toggle"]


class CssSelectStatus(CssStyle.Style):
  classnames = ["dropdown-menu", "status"]

  def customize(self):
    self.css({"background-color": self.rptObj.theme.greys[0],
              'font-size': '%s%s' % (Defaults_css.Font.size, Defaults_css.Font.unit)})
