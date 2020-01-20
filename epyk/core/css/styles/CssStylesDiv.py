"""
CSS Style module for the Div components
"""


from epyk.core.css.styles import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssDivNoBorder(CssStyle.CssCls):
  attrs = {'margin': '0', 'clear': 'both', 'padding': '0', 'border': '0'}


class CssDivBottomBorder(CssStyle.CssCls):
  def customize(self, style, eventsStyles):
    style.update({"border-bottom": '2px solid %s' % self.getColor("colors", 0), 'font-family': Defaults_css.Font.family})
    eventsStyles['hover'].update({"border-bottom": '2px solid %s' % self.getColor("success", -1)})


class CssDivWithBorder(CssStyle.CssCls):
  attrs = {'margin': '0 0 5px 0', 'padding': '5px', 'outline': 'none'}

  def customize(self, style, eventsStyles):
    style.update({'border': "1px solid %s" % self.getColor('colors', 0), 'font-family': Defaults_css.Font.family})


class CssDivConsole(CssStyle.CssCls):
  attrs = {'margin': '0', 'padding': '5px', 'border': '0', 'outline': 'none'}
  
  before = [{'attr': 'content', 'value': r"'C:\Users\LONDON>'"}]
  
  def customize(self, style, eventsStyles):
    style.update({'background-color': self.getColor('greys', 9)})


class CssDivCursor(CssStyle.CssCls):
  attrs = {'cursor': 'cursor'}
  hover = {'cursor': 'pointer'}


class CsssDivBoxMargin(CssStyle.CssCls):
  attrs = {'margin': '0', 'padding': '0 2px 0 2px', 'white-space': 'pre-wrap'}

  def customize(self, style, eventsStyles):
    style.update({"border": '1px solid %s' % self.getColor('greys', 0), 'font-family': Defaults_css.Font.family})
    eventsStyles['hover'].update({'border': "1px solid %s" % self.getColor('greys', 5)})


class CssDivBoxCenter(CssStyle.CssCls):
  attrs = {'width': '100%', 'text-align': 'center'}


class CssDivBoxWithDotBorder(CssStyle.CssCls):
  attrs = {'margin': '5px'}

  def customize(self, style, eventsStyles):
    style.update({"border": '1px dashed %s' % self.getColor('greys', 9)})


class CssDivBubble(CssStyle.CssCls):
  attrs = {'margin-left': 'auto', 'margin-right': 'auto', 'border-radius': '50%',
           'text-align': 'center'}

  def customize(self, style, eventsStyles):
    style.update({"border": '1px solid %s' % self.getColor('greys', 5)})


class CssDivBox(CssStyle.CssCls):
  attrs = {'width': '100%'}

  def customize(self, style, eventsStyles):
    eventsStyles['hover'].update({"border-left": "4px solid %s" % self.getColor('greys', 0), 'background-color': self.getColor('colors', 9)})


class CssDivLeft(CssStyle.CssCls):
  attrs = {'float': 'left', 'width': '20%'}


class CssDivRight(CssStyle.CssCls):
  attrs = {'float': 'right', 'width': '80%'}


class CssDivBorder(CssStyle.CssCls):

  def customize(self, style, eventsStyles):
    eventsStyles['hover'].update({"border": "1px solid %s" % self.getColor('greys', 9)})


class CssDivShadow(CssStyle.CssCls):
  attrs = {'box-shadow': '10px 10px 8px 10px #888888'}


class CssDivWhitePage(CssStyle.CssCls):
  reqCss = [CssDivShadow, CssDivBorder]
  attrs = {'height': '80%', 'min-height': '600px', 'margin': '0 10px 0 10px'}

  def customize(self, style, eventsStyles):
    eventsStyles['hover'].update({'background-color': self.getColor('greys', 0)})


class CssDivBanner(CssStyle.CssCls):
  attrs = {'width': '100%', 'margin': '0', 'overflow-y': 'auto', 'padding': '10px'}

  def customize(self, style, eventsStyles):
    style.update({'background-color': self.getColor('greys', 0)})


class CssDivSubBanner(CssStyle.CssCls):
  attrs = {'height': '400px', 'width': '100%', 'overflow-y': 'auto', 'margin-top': '50px', 'padding': '0', 'margin': '0'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('greys', 9), 'background-color': self.getColor('greys', 0)})


class CssDivLabelPoint(CssStyle.CssCls):
  attrs = {'padding': '10px', 'margin-top': '20px', 'margin-left': '5px', 'border-radius': '50%', 'cursor': 'pointer',
           'display': 'inline-block'}
  cssId = {'child': 'label'}

  def customize(self, style, eventsStyles):
    style.update({"border": '1px solid %s' % self.getColor("greys", 4), 'background': self.getColor('greys', 0)})
    eventsStyles['hover'].update({"border": '1px solid %s' % self.getColor("success", 1)})


class CssDivCommBubble(CssStyle.CssCls):
  attrs = {'width': '100%', 'vertical-align': 'top', 'top': '0', 'margin-bottom': '20px', 'margin-left': '20px',
           'display': 'inline-block'}
  before = {'content': "''", 'width': 0, 'height': 0, 'display': 'inline-block', 'border': '15px solid transparent', 'margin-left': '-30px'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('greys', 0)})
    eventsStyles['before'].update({'border-right-color': self.getColor('colors', 9)})


class CssDivComms(CssStyle.CssCls):
  attrs = {'margin-top': '10px', 'padding': '5px'}


class CssDivLoading(CssStyle.CssCls):
  attrs = {'opacity': 0.5, 'filter': 'alpha(opacity=50)', 'padding': '5px', 'text-align': 'center'}


class CssDivHidden(CssStyle.CssCls):
  attrs = {'display': 'none'}


class CssDivTextLeft(CssStyle.CssCls):
  attrs = {'text-align': 'left'}


class CssDivTableContent(CssStyle.CssCls):
  attrs = {'padding': '5px 10px 5px 10px', 'width': 'auto', 'display': 'inline-block'}

  def customize(self, style, eventsStyles):
    style.update({'border': '1px solid %s' % self.getColor('greys', 3), 'background-color': self.getColor('greys', 1)})


class CssDivPagination(CssStyle.CssCls):
  attrs = {'margin': 'auto', 'padding': '8px 16px', 'text-decoration': 'none', 'transition': 'background-color .3s'}
  cssId = {'child': 'a'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.getColor('greys', 9)})
    eventsStyles['hover'].update({"background-color": self.getColor('greys', 3)})


class CssDivEditor(CssStyle.CssCls):
  attrs = {'overflow': 'hidden', 'white-space': 'pre', 'display': 'block', 'padding': '30px 10px 10px 10px',
           'margin-top': '5px', 'text-align': 'left'}

  def customize(self, style, eventsStyles):
    style.update({'border': "1px solid %s" % self.getColor('greys', 3), 'background-color': self.getColor('greys', 2)})
    eventsStyles['focus'].update({'background-color': self.getColor('greys', 0), 'border': "2px solid %s" % self.getColor('colors', 5)})


class CssDivRow(CssStyle.CssCls):

  def customize(self, style, eventsStyles):
    eventsStyles['hover'].update({'background-color': self.getColor('greys', 1)})


class CssPanelTitle(CssStyle.CssCls):
  attrs = {'padding': '1px 0', 'margin': '0 5px 5px 5px', 'font-weight': 'bold'}

  def customize(self, style, eventsStyles):
    style.update({'border-bottom': "1px solid %s" % self.getColor('success', 1), "font-size": self.headerFontSize,
                  'font-family': Defaults_css.Font.family})


class CssDivFilter(CssStyle.CssCls):
  attrs = {"padding": "5px"}

  def customize(self, style, eventsStyles):
    style.update({'border': '1px solid %s' % self.getColor('colors', 0)})


class CssDivFilterItems(CssStyle.CssCls):

  def customize(self, style, eventsStyles):
    style.update({'border': '1px solid %s' % self.getColor('colors', 2)})
    eventsStyles['hover'].update({'border': '1px solid %s' % self.getColor('success', 1)})

class CssDivModal(CssStyle.CssCls):

  attrs = {'display': 'none', 'z-index': 1, 'position': 'fixed', 'padding-top': '100px', 'left': 0, 'top': 0,
           'width': '100%', 'height': '100%', 'overflow': 'auto', 'background-color': 'rgb(0,0,0,0.4)'}

class CssDivModalContent(CssStyle.CssCls):

  attrs = {'margin': 'auto', 'padding': '20px', 'border': '1px solid #888', 'width': '80%'}

  def customize(self, style, eventsStyles):
    style.update({'background-color': self.getColor('greys', 0)})