"""
CSS Style module for the Radio components
"""


from epyk.core.css.styles import CssStyle


class CssRadioButton(CssStyle.CssCls):
  attrs = {'padding': '2px 5px', 'cursor': 'pointer', 'vertical-align': 'middle', 'font-size': '12px'}

  def customize(self, style, eventsStyles):
    style.update({'border': '1px solid %s' % self.getColor("colors", 3)})


class CssRadioButtonSelected(CssStyle.CssCls):
  attrs = {'padding': '2px 5px', 'cursor': 'pointer', 'vertical-align': 'middle', 'font-size': '12px'}

  def customize(self, style, eventsStyles):
    style.update({'border': '1px solid %s' % self.getColor("success", 1), 'color': self.getColor('success', 1)})


class CssRadioSwitch(CssStyle.CssCls):
  attrs = {'height': '0', 'width': '0', 'visibility': 'hidden'}
  cssId = {'tag': 'input'}


class CssRadioSwitchLabel(CssStyle.CssCls):
  attrs = {'cursor': 'pointer', 'margin': '2px', 'text-indent': '-9999px', 'display': 'block', 'border-radius': '100px', 'position': 'relative'}
  after = {'content': "''", 'position': 'absolute', 'left': '5px', 'width': '20px', 'height': '100%', 'border-radius': '20px', 'transition': '0.3s'}
  cssId = {'tag': 'label'}

  def customize(self, style, eventsStyles):
    style.update({'background': self.getColor('greys', 3)})
    eventsStyles['after'].update({'background-color': self.getColor('colors', 5)})


class CssRadioSwitchChecked(CssStyle.CssCls):
  after = {'left': 'calc(100% - 5px)', 'transform': 'translateX(-100%)'}
  cssId = {'tag': 'input:checked + label'}

