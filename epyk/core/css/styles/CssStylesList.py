"""
CSS Style module for the List components
"""


from epyk.core.css.styles import CssStyle


class CssBasicList(CssStyle.Style):
  _attrs = {'padding': '15px', 'font-size': '16px', 'font-weight': 'bold'}
  _selectors = {'child': 'ul li:first-child'}

  def customize(self):
    self.css({"background": self.rptObj.theme.colors[7], "color": self.rptObj.theme.greys[0]})


class CssBasicListItems(CssStyle.Style):
  _attrs = {'padding': '15px 0 0 0', 'display': 'block'}

  def customize(self):
    self.css({"color": self.rptObj.theme.greys[-1], "border-bottom": "1px solid %s" % self.rptObj.theme.colors[7]})
    self.hover.css({'color': self.rptObj.theme.colors[8]})


class CssBasicListItemsSelected(CssStyle.Style):

  def customize(self):
    self.css({"color": self.rptObj.theme.success[1]})


class CssBasicListItemsDisabled(CssStyle.Style):
  _attrs = {'padding': '15px 0 0 0', 'display': 'block', 'cursor': 'not-allowed'}

  def customize(self):
    self.css({"background-color": self.rptObj.theme.greys[7], "color": self.rptObj.theme.greys[4]})


class CssSquareList(CssStyle.Style):
  _attrs = {'list-style': 'none', 'text-align': 'justify'}
  _before = {'content': "'\\f0c8'", 'font-family': "'Font Awesome 5 Free'", 'padding': '0 5px 0 0'}
  _selectors = {'child': 'li'}

  def customize(self):
    self.before.cess({"color": self.rptObj.theme.colors[7]})


class CssListBase(CssStyle.Style):
  _attrs = {'width': '142px', 'min-height': '20px', 'list-style-type': 'none', 'margin': 0, 'padding': '5px 0 0 0',
            'float': 'left', 'margin-right': '10px'}

  def customize(self):
    self.hover.css({"border": "1px solid %s" % self.rptObj.theme.greys[9]})


class CssListLiBase(CssStyle.Style):
  _attrs = {'margin': '0 5px 5px 5px', 'padding': '5px', 'width': '120px'}


class CssListNoDecoration(CssStyle.Style):
  _attrs = {'list-style': 'none', 'padding': '0 0 0 5px'}


class CssListLiUlContainer(CssStyle.Style):
  _attrs = {'display': 'none', 'width': '100%', 'padding': 0, 'margin': 0, 'overflow': 'hidden',
            'transition': 'height .2s ease-in-out'}
  cssId = {'direct': 'ul'}


class CssListLiSubItem(CssStyle.Style):
  _attrs = {'display': 'table', 'width': '100%', 'height': '30px', 'vertical-align': 'middle',
            'list-style-type': 'none', 'float': 'left', 'font-size': '12px', 'margin': 0}

  def customize(self):
    self.hover.css({"background": self.rptObj.theme.greys[2]})
