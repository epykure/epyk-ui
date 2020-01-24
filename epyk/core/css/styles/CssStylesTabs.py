"""
CSS Style module for the Tabs components
"""


from epyk.core.css.styles import CssStyle


class CssDefaultTab(CssStyle.CssCls):
  attrs = {'margin': 0}

  def customize(self, style, eventsStyles):
    style.update({'background-color': self.rptObj.theme.greys[0], 'color': self.rptObj.theme.colors[-1]})


class CssDefaultTabSelected(CssStyle.CssCls):

  def customize(self, style, eventsStyles):
    style.update({'background-color': self.rptObj.theme.colors[-1], 'color': self.rptObj.theme.colors[0]})


class CssBorderTab(CssStyle.CssCls):
  attrs = {'margin': '0 0 5px 0'}

  def customize(self, style, eventsStyles):
    style.update({'border-bottom': 'None', 'background-color': self.rptObj.theme.greys[0],
                  'color': self.rptObj.theme.colors[-1]})


class CssBorderTabSelected(CssStyle.CssCls):

  def customize(self, style, eventsStyles):
    style.update({'border-bottom': "3px solid %s !IMPORTANT" % self.rptObj.theme.success[1]})
