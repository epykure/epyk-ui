"""
CSS Style module for the Input components
"""


from epyk.core.css.styles import CssStyle


class CssInput(CssStyle.CssCls):
  attrs = {'font-size': '12px', 'font-family': 'Calibri', 'border': 'none', 'text-align': 'center', 'cursor': 'text',
           'margin': '0', 'border-radius': '5px', "line-height": "20px"}
  focus = {'outline': 0}

  def customize(self, style, eventsStyles):
    style.update({"background": self.getColor('colors', 0), "color": self.getColor('greys', -1), 'border': '1px solid %s' % self.getColor('colors', 0)})
    eventsStyles['hover'].update({'color': self.getColor('success', 1)})


class CssInputInteger(CssStyle.CssCls):
  cssId = {'reference': 'input[type=number]::-webkit-inner-spin-button, input[type=number]::-webkit-outer-spin-button'}
  attrs = {"-webkit-appearance": 'none', "margin": 0}


class CssInputRange(CssStyle.CssCls):
  attrs = {'-webkit-appearance': 'none', 'appearance': 'none', 'outline': 'none', 'opacity': 0.7,
           '-webkit-transition': '.2s', 'transition': 'opacity .2s', 'cursor': 'pointer'}
  hover = {'opacity': 1}

  def customize(self, style, eventsStyles):
    style.update({"background": self.getColor('colors', 0)})


class CssInputRangeThumb(CssStyle.CssCls):
  cssId = {'reference': 'input[type=range]::-webkit-slider-thumb'}
  attrs = {'-webkit-appearance': 'none', 'appearance': 'none', 'cursor': 'pointer',
           'width': '10px', 'height': '10px'}

  def customize(self, style, eventsStyles):
    style.update({"background": self.getColor('success', 1)})

  @property
  def classname(self):
    return 'input[type=range]::-webkit-slider-thumb'


class CssInputLabel(CssStyle.CssCls):
  attrs = {'font-size': '12px', 'line-height': '1.5', 'margin-left': '10px'}
  cssId = {'child': 'label'}


class CssInputInt(CssStyle.CssCls):
  cssId = {'child': 'input'}


class CssInputText(CssStyle.CssCls):
  attrs = {'margin-left': '10px'}
  cssId = {'child': 'input'}


class CssInputTextArea(CssStyle.CssCls):
  attrs = {'resize': 'none', 'margin-bottom': '5px'}
  focus = {'outline': 0}

  def customize(self, style, eventsStyles):
    style.update({"background-color": self.getColor('colors', 0), "color": self.getColor('greys', -1),
                  'border': '1px solid %s' % self.getColor('greys', 3)})
    eventsStyles['hover'].update({'color': self.getColor('greys', -1), 'border': '1px solid %s' % self.getColor('success', 1)})
