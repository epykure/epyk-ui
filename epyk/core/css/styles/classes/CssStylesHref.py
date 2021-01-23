
from epyk.core.css.styles.classes import CssStyle


class CssHrefNoDecoration(CssStyle.Style):
  _attrs = {'text-decoration': 'none', 'color': 'inherit'}

  def customize(self):
    self.hover.css({'color': self.rptObj.theme.colors[4]})


class CssLabelDates(CssStyle.Style):
  _selectors = {'child': 'a'}

  def customize(self):
    self.css({'background-color': self.rptObj.theme.colors[5], 'background-image': 'none',
              'color': self.rptObj.theme.greys[0]}, important=True)


class CssHreftMenu(CssStyle.Style):
  _attrs = {'margin': 0, 'clear': 'both', 'border': 0, 'display': 'block', 'position': 'relative', 'color': 'inherit',
            'height': '32px', 'list-style': 'none', 'padding': '0 0 0 5px', 'text-decoration': 'none'}
  _selectors = {'child': 'a'}

  def customize(self):
    self.css({'background': self.rptObj.theme.colors[5], 'color': self.rptObj.theme.colors[4]})


class CssHrefSubMenu(CssStyle.Style):
  _attrs = {'width': '100%', 'padding-left': '5px', 'color': 'white', 'text-decoration': 'none'}
  _selectors = {'child': 'a'}
  
  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1]})
    self.hover.css({'color': self.rptObj.theme.colors[7]})


class CssSideBarLinks(CssStyle.Style):
  _attrs = {'padding-top': '5px', 'padding-bottom': '5px', 'text-decoration': 'none', 'display': 'block'}
  _hover = {'text-decoration': 'none'}

  def customize(self):
    self.hover.css({'background-color': self.rptObj.theme.greys[2]})


class CssHrefContentLevel1(CssStyle.Style):
  _attrs = {'padding': 0, 'display': 'inline-block', 'margin': 0}


class CssHrefContentLevel2(CssStyle.Style):
  _attrs = {'padding': 0, 'display': 'inline-block', 'margin-left': '20px'}


class CssHrefContentLevel3(CssStyle.Style):
  attrs = {'padding': 0, 'display': 'inline-block', 'margin-left': '40px'}


class CssHrefContentLevel4(CssStyle.Style):
  _attrs = {'padding': 0, 'display': 'inline-block', 'margin-left': '60px'}


class CssFeedbackLink(CssStyle.Style):
  _attrs = {'position': 'fixed', 'bottom': '5px', 'cursor': 'pointer', 'right': '25px', 'padding': '0 10px',
            'z-index': 1000}
  _hover = {'text-decoration': 'underline'}

  def customize(self):
    self.css({'background-color': self.rptObj.theme.greys[2]})


class CssStandardLinks(CssStyle.Style):
  _hover = {'text-decoration': 'underline'}

  def customize(self):
    self.css({'color': self.rptObj.theme.colors[-1]})
    self.hover.css({'color': self.rptObj.theme.colors[-1]})

