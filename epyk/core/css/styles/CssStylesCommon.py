"""
Module in charge of the CSS Standard modules
"""


from epyk.core.css.styles import CssStyle


class CssBody(CssStyle.CssCls):
  attrs = {'top': '0', 'margin': '0 20px 0 20px'}
  cssId = {'tag': 'body'}

  def customize(self, style, eventsStyles):
    if self.getColor('greys', 0) == '#000000':
      style.update({"background-color": self.getColor('greys', 0), "color": self.getColor('greys', 9),
                    'font-family': self.fontFamily, 'font-size': self.fontSize})
    else:
      style.update({"background-color": self.getColor('greys', 2), "color": self.getColor('greys', 9),
                    'font-family': self.fontFamily, 'font-size': self.fontSize})


class CssTextSelection(CssStyle.CssCls):
  def customize(self, style, eventsStyles):
    style.update({"background": self.getColor("success", 0)})


class CssBodyContent(CssStyle.CssCls):
  attrs = {'margin-top': '10px', 'padding': '5px'}

  def customize(self, style, eventsStyles):
    style.update({"background-color": self.getColor('greys', 0), "border-radius": "5px",
                  "border": '1px solid %s' % self.getColor('greys', 3)})


class CssBodyLoadingBack(CssStyle.CssCls):
  attrs = {'text-align': 'center', 'top': '0', 'left': '0', 'width': '100%', 'padding-top': '20%', 'height': '100%',
           'z-index': '295', 'position': 'fixed', 'opacity': '0.5', 'filter': 'alpha(opacity=50)'}

  def customize(self, style, eventsStyles):
    style.update({"background-color": self.getColor('greys', 5)})


class CssBodyLoading(CssStyle.CssCls):
  attrs = {'text-align': 'center', 'top': '0', 'left': '0', 'width': '100%', 'position': 'fixed', 'padding-top': '10%',
           'height': '100%', 'display': 'none', 'z-index': '300'}

  def customize(self, style, eventsStyles):
    style.update({"color": self.getColor('greys', 9)})


class CssNotSelect(CssStyle.CssCls):
  attrs = {"-webkit-touch-callout": 'none', "user-select": 'none',
           "-webkit-user-select": 'none', "-khtml-user-select": 'none',
           "-moz-user-select": 'none', "-ms-user-select": 'none'}
