"""
CSS Styles for all the select components
"""


from epyk.core.css.styles import CssStyle


class CssSelectStyle(CssStyle.CssCls):
  attrs = {'font-size': '12px', 'font-family': 'Calibri', 'height': '23px', 'padding-top': '2px',
           'display': 'inline-block !IMPORTANT', 'margin': '0 !IMPORTANT', 'min-width': '140px'}
  focus = {'outline': 0, 'border': 'none', 'box-shadow': 'none'}

  def customize(self, style, eventsStyles):
    style.update({"background": self.getColor('greys', 0), "color": self.getColor('greys', -1)})


class CssSelectButton(CssStyle.CssCls):
  attrs = {'padding': '0 5px', 'outline': 'none !IMPORTANT', 'border-color': 'none', 'box-shadow': 'none'}
  focus = {'outline': 'none !IMPORTANT', 'border-color': 'none', 'box-shadow': 'none'}
  cssId = {'reference': ".btn"}


class CssSelectSearchBox(CssStyle.CssCls):
  attrs = {"padding": "0 2px 1px 2px"}
  cssId = {'reference': ".bs-searchbox"}


class CssSelectSearchBoxInput(CssStyle.CssCls):
  attrs = {"height": "23px", "outline": 0, "margin-bottom": "10px"}
  cssId = {'reference': ".bs-searchbox input.form-control"}
  focus = {'outline': 0}

  def customize(self, style, eventsStyles):
    style.update({"border-color": self.getColor('colors', 0)})
    eventsStyles['focus'].update({"box-shadow": "0 0 0 0.2em %s" % self.getColor('colors', 0)})


class CssSelectOption(CssStyle.CssCls):
  cssId = {'reference': ".dropdown-menu"}
  attrs = {'font-size': '12px !IMPORTANT'}

  def customize(self, style, eventsStyles):
    style.update({"background": self.getColor('greys', 0)})


class CssSelectOptionHover(CssStyle.CssCls):
  cssId = {'reference': ".dropdown-menu li a"}

  def customize(self, style, eventsStyles):
    style.update({"color": self.getColor('greys', -1)})
    eventsStyles['hover'].update({'background': self.getColor('success', 0), "color": "black"})


class CssSelectOptionActive(CssStyle.CssCls):
  cssId = {'reference': ".active"}

  def customize(self, style, eventsStyles):
    style.update({'background': self.getColor('success', 0), "color": self.getColor('success', 1)})


class CssSelectFilterOption(CssStyle.CssCls):
  attrs = {'text-align': 'center !IMPORTANT'}
  cssId = {'reference': ".filter-option"}


class CssSelectOutline(CssStyle.CssCls):
  focus = {'outline': '0 !important'}
  cssId = {'reference': ".bootstrap-select .dropdown-toggle"}

