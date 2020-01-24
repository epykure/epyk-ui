"""
CSS Style module for the Popup components
"""


from epyk.core.css.styles import CssStyle


class CssPopupTable(CssStyle.CssCls):
  attrs = {'border-spacing': '0', 'border-collapse': 'collapse', 'margin': '0', 'padding': '0', 'width': '100%'}
  cssId = {'child': 'table'}

  def customize(self, style, eventsStyles):
    style.update({"background": self.rptObj.theme.colors[0], "color": self.rptObj.theme.greys[-1],
                  'border': '1px solid %s' % self.rptObj.theme.colors[0],
                  "box-shadow": '0 0 1px 1px %s' % self.rptObj.theme.colors[-1],
                  "-webkit-box-shadow": '0 0 1px 1px %s' % self.rptObj.theme.colors[-1],
                  "-moz-box-shadow": '0 0 1px 1px %s' % self.rptObj.theme.colors[-1]})


class CssPopupTableTitle(CssStyle.CssCls):
  attrs = {'margin': '0', 'padding': '0', 'border-collapse': 'collapse', 'cursor': 'pointer'}
  cssId = {'child': 'table tr:first-child th'}

  def customize(self, style, eventsStyles):
    style.update({"background-color": self.rptObj.theme.colors[-1], "border": "1px solid %s" % self.rptObj.theme.colors[-1],
                  "color": self.rptObj.theme.greys[0]})


class CssPopupTableTitleContent(CssStyle.CssCls):
  attrs = {'vertical-align': 'middle', 'border-collapse': 'collapse', 'text-align': 'right', 'font-weight': 'bold',
           'text-transform': 'uppercase'}
  cssId = {'child': 'table th'}

  def customize(self, style, eventsStyles):
    style.update({"background": self.rptObj.theme.colors[0], "color": self.rptObj.theme.greys[-1],
                  'border': '1px solid %s' % self.rptObj.theme.colors[0]})


class CssEventLoading(CssStyle.CssCls):
  attrs = {'bottom': '5px', 'right': '20px', 'position': 'fixed', 'padding': '5px'}

  def customize(self, style, eventsStyles):
    style.update({"background-color": self.rptObj.theme.greys[0], 'color': self.rptObj.theme.greys[-1]})


