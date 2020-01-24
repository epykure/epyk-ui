"""
CSS Style module for the List components
"""


from epyk.core.css.styles import CssStyle
from epyk.core.css.styles import CssStylesDiv


class CssBasicList(CssStyle.CssCls):
  attrs = {'padding': '15px', 'font-size': '16px', 'font-weight': 'bold'}
  cssId = {'child': 'ul li:first-child'}

  def customize(self, style, eventsStyles):
    style.update({"background": self.rptObj.theme.colors[7]})
    style.update({"color": self.rptObj.theme.greys[0]})


class CssBasicListItems(CssStyle.CssCls):
  attrs = {'padding': '15px 0 0 0', 'display': 'block'}

  def customize(self, style, eventsStyles):
    style.update({"color": self.rptObj.theme.greys[-1]})
    style.update({"border-bottom": "1px solid %s" % self.rptObj.theme.colors[7]})
    eventsStyles['hover'].update({'color': self.rptObj.theme.colors[8]})


class CssBasicListItemsSelected(CssStyle.CssCls):

  def customize(self, style, eventsStyles):
    style.update({"color": self.rptObj.theme.success[1]})


class CssBasicListItemsDisabled(CssStyle.CssCls):
  attrs = {'padding': '15px 0 0 0', 'display': 'block', 'cursor': 'not-allowed'}

  def customize(self, style, eventsStyles):
    style.update({"background-color": self.rptObj.theme.greys[7], "color": self.rptObj.theme.greys[4]})


class CssSquareList(CssStyle.CssCls):
  attrs = {'list-style': 'none', 'text-align': 'justify'}
  before = {'content': "'\\f0c8'", 'font-family': "'Font Awesome 5 Free'", 'padding': '0 5px 0 0'}
  cssId = {'child': 'li'}

  def customize(self, style, eventsStyles):
    eventsStyles['before'].update({"color": self.rptObj.theme.colors[7]})


class CssListBase(CssStyle.CssCls):
  reqCss = [CssStylesDiv.CssDivBorder]
  attrs = {'width': '142px', 'min-height': '20px', 'list-style-type': 'none', 'margin': '0', 'padding': '5px 0 0 0',
           'float': 'left', 'margin-right': '10px'}


class CssListLiBase(CssStyle.CssCls):
  attrs = {'margin': '0 5px 5px 5px', 'padding': '5px', 'width': '120px'}


class CssListNoDecoration(CssStyle.CssCls):
  attrs = {'list-style': 'none', 'padding': '0 0 0 5px'}


class CssListLiUlContainer(CssStyle.CssCls):
  attrs = {'display': 'none', 'width': '100%', 'padding': '0', 'margin': '0', 'overflow': 'hidden',
           'transition': 'height .2s ease-in-out'}
  cssId = {'direct': 'ul'}


class CssListLiSubItem(CssStyle.CssCls):
  attrs = {'display': 'table', 'width': '100%', 'height': '30px', 'vertical-align': 'middle', 'list-style-type': 'none',
           'float': 'left', 'font-size': '12px', 'margin': 0}

  def customize(self, style, eventsStyles):
    eventsStyles['hover'].update({"background": self.rptObj.theme.greys[2]})
