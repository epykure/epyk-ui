"""
CSS Style module for the Popup components
"""

from epyk.core.css.styles.classes import CssStyle


class CssPopupTable(CssStyle.Style):
  _attrs = {'border-spacing': 0, 'border-collapse': 'collapse', 'margin': 0, 'padding': 0, 'width': '100%'}
  _selectors = {'child': 'table'}

  def customize(self):
    self.css({"background": self.page.theme.colors[0], "color": self.page.theme.greys[-1],
              'border': '1px solid %s' % self.page.theme.colors[0],
              "box-shadow": '0 0 1px 1px %s' % self.page.theme.colors[-1],
              "-webkit-box-shadow": '0 0 1px 1px %s' % self.page.theme.colors[-1],
              "-moz-box-shadow": '0 0 1px 1px %s' % self.page.theme.colors[-1]})


class CssPopupTableTitle(CssStyle.Style):
  _attrs = {'margin': 0, 'padding': 0, 'border-collapse': 'collapse', 'cursor': 'pointer'}
  _selectors = {'child': 'table tr:first-child th'}

  def customize(self):
    self.css({"background-color": self.page.theme.colors[-1], "border": "1px solid %s" % self.page.theme.colors[-1],
              "color": self.page.theme.greys[0]})


class CssPopupTableTitleContent(CssStyle.Style):
  _attrs = {'vertical-align': 'middle', 'border-collapse': 'collapse', 'text-align': 'right', 'font-weight': 'bold',
            'text-transform': 'uppercase'}
  _selectors = {'child': 'table th'}

  def customize(self):
    self.css({
      "background": self.page.theme.colors[0], "color": self.page.theme.greys[-1],
      'border': '1px solid %s' % self.page.theme.colors[0]})


class CssEventLoading(CssStyle.Style):
  _attrs = {'bottom': '5px', 'right': '20px', 'position': 'fixed', 'padding': '5px'}

  def customize(self):
    self.css({"background-color": self.page.theme.greys[0], 'color': self.page.theme.greys[-1]})
