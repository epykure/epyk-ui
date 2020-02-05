"""
CSS Style module for the common Div components
"""


from epyk.core.css.styles import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssCommHeader(CssStyle.Style):
  _attrs = {'font-weight': 'bold', 'display': 'block', 'text-align': 'left'}
  _selectors = {'child': 'span'}

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'font-family': Defaults_css.Font.family,
              'font-size': '%s%s' % (Defaults_css.Font.size, Defaults_css.Font.unit)})


class CssCommInput(CssStyle.Style):
  _attrs = {'border': 'none', 'width': '95%', 'margin': 0, 'padding': '5px'}
  _focus = {'outline': 0}

  _selectors = {'child': 'input'}

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'background-color': self.rptObj.theme.greys[0],
              'border-bottom': '1px solid %s' % self.rptObj.theme.success[1], 'font-family': Defaults_css.Font.family,
              'font-size': '%s%s' % (Defaults_css.Font.size, Defaults_css.Font.unit)})


class CssContentEditable(CssStyle.Style):
  classname = False
  _selector = "[contenteditable]"

  def customize(self):
    self.focus.css({'outline': "1px solid %s" % self.rptObj.theme.success[1]})
