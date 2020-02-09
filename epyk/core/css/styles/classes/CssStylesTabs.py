"""
CSS Style module for the Tabs components
"""

from epyk.core.css.styles.classes import CssStyle


class CssDefaultTab(CssStyle.Style):
  _attrs = {'margin': 0}

  def customize(self):
    self.css({'background-color': self.rptObj.theme.greys[0], 'color': self.rptObj.theme.colors[-1]})


class CssDefaultTabSelected(CssStyle.Style):

  def customize(self):
    self.css({'background-color': self.rptObj.theme.colors[-1], 'color': self.rptObj.theme.colors[0]})


class CssBorderTab(CssStyle.Style):
  _attrs = {'margin': '0 0 5px 0'}

  def customize(self):
    self.css({'border-bottom': 'None', 'background-color': self.rptObj.theme.greys[0],
              'color': self.rptObj.theme.colors[-1]})


class CssBorderTabSelected(CssStyle.Style):

  def customize(self):
    self.css({'border-bottom': "3px solid %s" % self.rptObj.theme.success[1]}, important=True)
