"""
CSS Style module for the Label components
"""


from epyk.core.css.styles import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssLabelContainer(CssStyle.CssCls):
  attrs = {'display': 'block', 'position': 'relative', 'cursor': 'pointer', '-webkit-user-select': 'none',
           '-moz-user-select': 'none', '-ms-user-select': 'none', 'user-select': 'none'}

  def customize(self, style, eventsStyles):
    style.update({'font-family': Defaults_css.Font.family, 'font-size': '%spx' % Defaults_css.Font.size})


class CssLabelContainerDisabled(CssStyle.CssCls):
  attrs = {'color': 'red', 'cursor': 'not-allowed'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor("danger", 1)})


class CssLabelCheckMarkHover(CssStyle.CssCls):
  cssId = {'child': "label"}

  def customize(self, style, eventsStyles):
    eventsStyles['hover'].update({'background-color': self.getColor('colors', 5)})
