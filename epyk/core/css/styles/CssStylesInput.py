"""
CSS Style module for the Input components
"""

from epyk.core.html import Defaults as Defaults_html
from epyk.core.css import Defaults as Defaults_css

from epyk.core.css.styles import CssStyle


class CssInput(CssStyle.CssCls):
  """
  CSS Base style for the input components
  """
  attrs = {'border': 'none', 'text-align': 'center', 'cursor': 'text', 'margin': '0', 'border-radius': '5px'}
  focus = {'outline': 0}

  def customize(self, style, eventsStyles):
    style.update({"background": self.rptObj.theme.colors[0], "color": self.rptObj.theme.greys[-1],
                  'font-family': Defaults_css.Font.family, 'min-width': '%spx' % Defaults_html.INPUTS_MIN_WIDTH,
                  'line-height': '%spx' % Defaults_html.LINE_HEIGHT, 'border': '1px solid %s' % self.rptObj.theme.colors[0],
                  'font-size': '%spx' % Defaults_css.Font.size})
    eventsStyles['hover'].update({'color': self.rptObj.theme.success[1]})


class CssInputRange(CssStyle.CssCls):
  """
  CSS Style for the input range component
  """
  attrs = {'-webkit-appearance': 'none', 'appearance': 'none', 'outline': 'none', 'opacity': 0.7,
           '-webkit-transition': '.2s', 'transition': 'opacity .2s', 'cursor': 'pointer'}
  hover = {'opacity': 1}

  def customize(self, style, eventsStyles):
    style.update({"background": self.rptObj.theme.colors[0]})


class CssInputRangeThumb(CssStyle.CssCls):
  """
  CSS Style for the thumb of the input range component
  """
  cssId = {'reference': 'input[type=range]::-webkit-slider-thumb'}
  attrs = {'-webkit-appearance': 'none', 'appearance': 'none', 'cursor': 'pointer'}

  def customize(self, style, eventsStyles):
    style.update({"background": self.rptObj.theme.success[1], 'width': '%spx' % Defaults_html.INPUTS_RANGE_THUMB,
                  'height': '%spx' % Defaults_html.INPUTS_RANGE_THUMB})

  @property
  def classname(self):
    return 'input[type=range]::-webkit-slider-thumb'


class CssInputLabel(CssStyle.CssCls):
  """
  CSS Style for the label attached to an input component
  """
  attrs = {'line-height': '1.5', 'margin-left': '10px'}
  cssId = {'child': 'label'}

  def customize(self, style, eventsStyles):
    style.update({'font-family': Defaults_css.Font.family, 'font-size': '%spx' % Defaults_css.Font.size})


class CssInputInteger(CssStyle.CssCls):
  """

  """
  cssId = {'reference': 'input[type=number]::-webkit-inner-spin-button, input[type=number]::-webkit-outer-spin-button'}
  attrs = {"-webkit-appearance": 'none', "margin": 0}


class CssInputInt(CssStyle.CssCls):
  """
  CSS Style for the input integer component
  """
  cssId = {'child': 'input'}


class CssInputText(CssStyle.CssCls):
  """
  CSS Style for the input text component (within a field object)
  """
  attrs = {'margin-left': '10px'}
  cssId = {'child': 'input'}


class CssInputTextArea(CssStyle.CssCls):
  """
  CSS Style for the textarea component.
  """
  attrs = {'resize': 'none', 'margin-bottom': '5px'}
  focus = {'outline': 0}

  def customize(self, style, eventsStyles):
    style.update({"background-color": self.rptObj.theme.colors[0], "color": self.rptObj.theme.greys[-1],
                  'border': '1px solid %s' % self.rptObj.theme.colors[1]})
    eventsStyles['hover'].update({'color': self.rptObj.theme.greys[-1]})
