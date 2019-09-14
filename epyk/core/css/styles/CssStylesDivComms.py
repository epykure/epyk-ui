"""
CSS Style module for the common Div components
"""


from epyk.core.css.styles import CssStyle


class CssCommHeader(CssStyle.CssCls):
  attrs = {'font-size': '12px', 'font-family': 'Calibri', 'font-weight': 'bold', 'display': 'block', 'text-align': 'left'}
  cssId = {'child': 'span'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor("greys", -1),})


class CssCommInput(CssStyle.CssCls):
  attrs = {'font-size': '12px', 'font-family': 'Calibri', 'border': 'none', 'width': '95%', 'margin': '0', 'padding': '5px'}
  focus = {'outline': 0}
  cssId = {'child': 'input'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor("greys", -1), 'background-color': self.getColor("greys", 0),
                  'border-bottom': '1px solid %s' % self.getColor("success", 1)})
