"""
CSS Style module for the Radio components
"""

from epyk.core.css.styles.classes import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssRadioButton(CssStyle.Style):
  _attrs = {'padding': '2px 5px', 'cursor': 'pointer', 'vertical-align': 'middle'}

  def customize(self):
    self.css({'border': '1px solid %s' % self.rptObj.theme.colors[3], 'font-size': '%spx' % Defaults_css.Font.size})


class CssRadioButtonSelected(CssStyle.Style):
  _attrs = {'padding': '2px 5px', 'cursor': 'pointer', 'vertical-align': 'middle'}

  def customize(self):
    self.css({'border': '1px solid %s' % self.rptObj.theme.success[1], 'color': self.rptObj.theme.success[1],
              'font-size': '%spx' % Defaults_css.Font.size})


class CssRadioSwitch(CssStyle.Style):
  _attrs = {'height': 0, 'width': 0, 'visibility': 'hidden'}


class CssRadioSwitchLabel(CssStyle.Style):
  _attrs = {'cursor': 'pointer', 'margin': '2px', 'text-indent': '-9999px', 'display': 'block', 'border-radius': '50px',
            'position': 'relative', 'top': '5px'}
  _after = {'content': "''", 'position': 'absolute', 'left': '5px', 'width': '15px', 'height': '15px',
            'border-radius': '20px', 'transition': '0.3s', 'margin': 'auto', 'top': '-2.5px'}

  def customize(self):
    self.css({'background': self.rptObj.theme.greys[3]})
    self.after.css({'background-color': self.rptObj.theme.colors[-1]})


class CssRadioSwitchChecked(CssStyle.Style):
  _after = {'left': 'calc(100% - 5px)', 'transform': 'translateX(-100%)'}
  _selectors = {'child': 'input:checked + label'}
