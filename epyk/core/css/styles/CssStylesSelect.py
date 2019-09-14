"""
CSS Styles for all the select components
"""


from epyk.core.css.styles import CssStyle


class CssSelectStyle(CssStyle.CssCls):
  cssId = {'reference': '.class_select'}
  attrs = {'font-size': '12px', 'font-family': 'Calibri', 'height': '23px', 'padding-top': '2px', 'display': 'inline-block !IMPORTANT',
           'margin': '0 !IMPORTANT'}
  focus = {'outline': '0 !IMPORTANT'}

  def customize(self, style, eventsStyles):
    style.update({"background": self.getColor('colors', 0), "color": self.getColor('greys', -1)})
    eventsStyles['hover'].update({'color': self.getColor('success', 1)})


class CssSelectButton(CssStyle.CssCls):
  focus = {'outline': '0 !IMPORTANT', 'box-shadow': 'none !IMPORTANT'}
  cssId = {'child': ".btn"}


class CssSelectOption(CssStyle.CssCls):
  cssId = {'child': ".dropdown-menu"}
  attrs = {'font-size': '12px !IMPORTANT'}

  def customize(self, style, eventsStyles):
    style.update({"background": self.getColor('colors', 2)})


class CssSelectOptionHover(CssStyle.CssCls):
  cssId = {'child': ".dropdown-menu li a"}

  def customize(self, style, eventsStyles):
    style.update({"color": self.getColor('greys', -1)})
    eventsStyles['hover'].update({'background': self.getColor('success', 0), "color": "black"})


class CssSelectOptionActive(CssStyle.CssCls):
  cssId = {'child': ".active"}

  def customize(self, style, eventsStyles):
    style.update({'background': self.getColor('success', 0), "color": self.getColor('success', 1)})


class CssSelectFilterOption(CssStyle.CssCls):
  attrs = {'text-align': 'center !IMPORTANT'}
  cssId = {'child': ".filter-option"}

