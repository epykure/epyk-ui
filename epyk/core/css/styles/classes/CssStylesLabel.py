"""
CSS Style module for the Label components
"""

from epyk.core.css.styles.classes import CssStyle


# class CssLabelContainer(CssStyle.Style):
#   _attrs = {'display': 'block', 'position': 'relative', 'cursor': 'pointer', '-webkit-user-select': 'none',
#             '-moz-user-select': 'none', '-ms-user-select': 'none', 'user-select': 'none'}
#
#   def customize(self):
#     self.css({'font-family': Defaults_css.Font.family,
#               'font-size': '%s%s' % (Defaults_css.Font.size, Defaults_css.Font.unit)})
#

class CssLabelContainerDisabled(CssStyle.Style):
  _attrs = {'color': 'red', 'cursor': 'not-allowed'}

  def customize(self):
    self.css({'color': self.rptObj.theme.danger[1]})


class CssLabelCheckMarkHover(CssStyle.Style):
  _selectors = {'child': "label"}

  def customize(self):
    self.hover.css({'background-color': self.rptObj.theme.colors[5]})
