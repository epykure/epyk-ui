"""
CSS Style module for the common Div components
"""


from epyk.core.css.styles import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssCommHeader(CssStyle.CssCls):
  attrs = {'font-weight': 'bold', 'display': 'block', 'text-align': 'left'}
  cssId = {'child': 'span'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor("greys", -1), 'font-family': Defaults_css.Font.family,
                  'font-size': '%spx' % Defaults_css.Font.size})


class CssCommInput(CssStyle.CssCls):
  attrs = {'border': 'none', 'width': '95%', 'margin': '0', 'padding': '5px'}
  focus = {'outline': 0}
  cssId = {'child': 'input'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor("greys", -1), 'background-color': self.getColor("greys", 0),
                  'border-bottom': '1px solid %s' % self.getColor("success", 1), 'font-family': Defaults_css.Font.family,
                  'font-size': '%spx' % Defaults_css.Font.size})


class CssContentEditable(CssStyle.CssCls):
  """

  """
  focus = {}
  cssId = {'reference': '[contenteditable]'}

  def customize(self, style, eventsStyles):
    eventsStyles['focus'].update({'outline': "1px solid %s" % self.getColor("success", 1)})
