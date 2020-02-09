"""
CSS Style module for the Files Drop components
"""

from epyk.core.css.styles.classes import CssStyle


class CssDropFile(CssStyle.Style):
  _attrs = {'text-align': 'center', 'padding': '5px', 'margin': '5px 0 10px 0'}

  def customize(self):
    self.css({'border': '1px dashed %s' % self.rptObj.theme.colors[1], 'color': self.rptObj.theme.colors[1]})
