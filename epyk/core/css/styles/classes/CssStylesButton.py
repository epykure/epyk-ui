
from epyk.core.css.styles.classes import CssStyle
from epyk.core.html import Defaults


class CssBorderRadius(CssStyle.Style):
  _attrs = {'border-radius': '5px'}


class CssButtonBasic(CssStyle.Style):
  _attrs = {'font-weight': 'bold', 'padding': '4px', 'margin': '2px 0 2px 0', 'text-decoration': 'none',
            'border-radius': '4px', 'white-space': 'nowrap', 'display': 'inline-block',
            '-webkit-appearance': 'none', '-moz-appearance': 'none'}
  _hover = {'text-decoration': 'none', 'cursor': 'pointer'}
  _focus = {'outline': 0}
  _disabled = {'cursor': 'none'}

  def customize(self):
    self.css({'border': '1px solid %s' % self.page.theme.colors[0], 'color': 'inherit'})
    self.hover.css(
      {"background-color": self.page.theme.notch(), 'color': self.page.theme.greys[0],
          'border': '1px solid %s' % self.page.theme.notch()}, important=True)
    self.disabled.css({
        'background-color': self.page.theme.greys[0],
        'border-color': self.page.theme.greys[0],
        'color': self.page.theme.greys[self.page.theme.index],
        "cursor": "not-allowed",
        'font-style': 'italic'}, important=True)


class CssButtonImportant(CssStyle.Style):
  _attrs = {'font-weight': 'bold', 'padding': '2px 20px', 'margin': '2px 0 2px 0', 'text-decoration': 'none',
            'border-radius': '4px', 'white-space': 'nowrap', 'display': 'inline-block', 'line-height': '30px',
            '-webkit-appearance': 'none', '-moz-appearance': 'none'}
  _hover = {'text-decoration': 'none', 'cursor': 'pointer'}
  _focus = {'outline': 0}
  _disabled = {'cursor': 'none'}

  def customize(self):
    self.css({'border': '1px solid', 'color': self.page.theme.greys[0],
              'background-color': self.page.theme.colors[-2]})
    self.hover.css({'background-color': self.page.theme.colors[-1], 'color': self.page.theme.greys[0]})
    self.disabled.css({
      'background-color': self.page.theme.colors[-1], 'color': self.page.theme.notch(1), 'font-style': 'italic'})


class CssButtonReset(CssStyle.Style):
  _attrs = {'font-weight': 'bold', 'padding': '5px 10px 5px 10px', 'margin-top': '5px', 'text-decoration': 'none',
            'border-radius': '5px', 'display': 'inline-block', 'text-transform': 'uppercase'}
  _hover = {'text-decoration': 'none', 'cursor': 'pointer'}
  _focus = {'outline': 0}

  def customize(self):
    self.css({'border': '1px solid %s' % self.page.theme.danger.dark, 'color': self.page.theme.danger.dark,
              'background-color': "white"})
    self.hover.css({'background-color': self.page.theme.danger.dark, 'color': "white"})


class CssButtonSuccess(CssStyle.Style):
  _attrs = {'font-weight': 'bold', 'padding': '10px 10px 10px 10px', 'margin': '10px 0px 10px 5px',
            'text-decoration': 'none', 'border-radius': '5px', 'display': 'inline-block', 'text-transform': 'uppercase'}
  _hover = {'text-decoration': 'none', 'cursor': 'pointer'}

  def customize(self):
    self.css({'color': self.page.theme.colors[-1], 'background-color': self.page.theme.greys[0],
              'border': '1px solid %s' % self.page.theme.colors[-1]})
    self.hover.css({'color': self.page.theme.greys[0], 'background-color': self.page.theme.colors[-1]})


class CssButtonContentHover(CssStyle.Style):
  _hover = {'display': 'block !IMPORTANT'}
  _selectors = {'suffix': ".dropdown-content"}


class CssButtonContentAHover(CssStyle.Style):
  _selectors = {'child': ".dropdown-content a"}

  def customize(self):
    self.hover.css({'background-color': self.page.theme.success.light})
