"""
CSS Style module for the HREF / links components
"""


from epyk.core.css.styles import CssStyle
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesList


class CssHrefNoDecoration(CssStyle.CssCls):
  attrs = {'text-decoration': 'none'}
  cssId = {'direct': 'a'}


class CssLabelDates(CssStyle.CssCls):
  attrs = {'background-image': 'none !important'}
  cssId = {'direct': 'a'}

  def customize(self, style, eventsStyles):
    style.update({'background-color': '%s!important' % self.getColor('colors', 5), 'color': '%s!important' % self.getColor('greys', 0)})


class CssHreftMenu(CssStyle.CssCls):
  reqCssCls = [CssStylesDiv.CssDivNoBorder, CssStylesList.CssListNoDecoration, CssHrefNoDecoration]
  attrs = {'display': 'block', 'position': 'relative', 'font-size': '14px', 'height': '32px'}

  hover = []
  directChildrenTag = "a"

  def customize(self, style, eventsStyles):
    style.update({'background': self.getColor('colors', 5), 'color': self.getColor('colors', 4)})


class CssHrefSubMenu(CssStyle.CssCls):
  attrs = {'width': '100%', 'padding-left': '5px', 'color': 'white', 'text-decoration': 'none'}
  cssId = {'direct': 'a'}
  
  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('greys', -1)})
    eventsStyles['hover'].update({'color': self.getColor('colors', 7)})


class CssSideBarLinks(CssStyle.CssCls):
  attrs = {'padding-top': '5px', 'padding-bottom': '5px', 'text-decoration': 'none', 'display': 'block'}
  hover = {'text-decoration': 'none'}

  def customize(self, style, eventsStyles):
    eventsStyles['hover'].update({'background-color': self.getColor('greys', 2)})


class CssHrefContentLevel1(CssStyle.CssCls):
  attrs = {'padding': '0', 'display': 'inline-block', 'margin': '5px 0 0 0', 'font-size': '14px'}


class CssHrefContentLevel2(CssStyle.CssCls):
  attrs = {'padding': '0', 'font-size': '14px', 'display': 'inline-block', 'margin-left': '20px'}


class CssHrefContentLevel3(CssStyle.CssCls):
  attrs = {'padding': '0', 'display': 'inline-block', 'font-size': '14px', 'margin-left': '40px'}


class CssHrefContentLevel4(CssStyle.CssCls):
  attrs = {'padding': '0', 'display': 'inline-block', 'font-size': '14px', 'margin-left': '60px'}


class CssFeedbackLink(CssStyle.CssCls):
  attrs = {'position': 'fixed', 'bottom': '5px', 'cursor': 'pointer', 'right': '25px', 'padding': '0 10px', 'z-index': '1000'}
  hover = {'text-decoration': 'underline'}

  def customize(self, style, eventsStyles):
    style.update({'background-color': self.getColor('greys', 2)})


class CssStandardLinks(CssStyle.CssCls):
  hover = {'text-decoration': 'underline'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('colors', -1)})
    eventsStyles['hover'].update({'color': self.getColor('greys', -1)})

