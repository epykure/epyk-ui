"""
CSS Style module for the Radio components
"""


from epyk.core.css.styles import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssRadioButton(CssStyle.CssCls):
  attrs = {'padding': '2px 5px', 'cursor': 'pointer', 'vertical-align': 'middle'}

  def customize(self, style, eventsStyles):
    style.update({'border': '1px solid %s' % self.rptObj.theme.colors[3], 'font-size': '%spx' % Defaults_css.Font.size})


class CssRadioButtonSelected(CssStyle.CssCls):
  attrs = {'padding': '2px 5px', 'cursor': 'pointer', 'vertical-align': 'middle'}

  def customize(self, style, eventsStyles):
    style.update({'border': '1px solid %s' % self.rptObj.theme.success[1], 'color': self.rptObj.theme.success[1],
                  'font-size': '%spx' % Defaults_css.Font.size})


class CssRadioSwitch(CssStyle.CssCls):
  attrs = {'height': '0', 'width': '0', 'visibility': 'hidden'}
  cssId = {'child': 'input'}


class CssRadioSwitchLabel(CssStyle.CssCls):
  attrs = {'cursor': 'pointer', 'margin': '2px', 'text-indent': '-9999px', 'display': 'block', 'border-radius': '100px',
           'position': 'relative'}
  after = {'content': "''", 'position': 'absolute', 'left': '5px', 'width': '20px', 'height': '100%',
           'border-radius': '20px', 'transition': '0.3s'}
  cssId = {'child': 'label'}

  def customize(self, style, eventsStyles):
    style.update({'background': self.rptObj.theme.greys[3]})
    eventsStyles['after'].update({'background-color': self.rptObj.theme.success[1]})


class CssRadioSwitchChecked(CssStyle.CssCls):
  after = {'left': 'calc(100% - 5px)', 'transform': 'translateX(-100%)'}
  cssId = {'child': 'input:checked + label'}

