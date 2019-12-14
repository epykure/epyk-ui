"""
CSS Style module for the Search components
"""


from epyk.core.css.styles import CssStyle


class CssSearchExt(CssStyle.CssCls):
  attrs = {'width': '130px', 'height': '30px', 'box-sizing': 'border-box', 'border-radius': '4px', 'font-size': '12px',
           'background-repeat': 'no-repeat', 'padding': '5px 20px 5px 40px', '-webkit-transition': 'width 0.4s ease-in-out',
           'transition': 'width 0.4s ease-in-out'}
  focus = {'width': '100%', 'outline': 0}

  def customize(self, style, eventsStyles):
    style.update({"background-color": self.getColor('greys', 0), "border": '1px solid %s' % self.getColor('greys', 5)})
    eventsStyles['hover'].update({'color': self.getColor('greys', -1), 'border': '1px solid %s' % self.getColor('success', 1)})


class CssSearch(CssStyle.CssCls):
  attrs = {'width': '100%', 'display': 'inline-block', 'border': 'none', 'font-size': '12px', 'background-repeat': 'no-repeat',
           'padding': '5px 20px 5px 40px'}
  focus = {'outline': 0}

  def customize(self, style, eventsStyles):
    style.update({"background-color": self.getColor('greys', 0), "border-bottom": '1px solid %s' % self.getColor('greys', 3), 'color': self.getColor('greys', -1)})
    eventsStyles['hover'].update({'color': self.getColor('greys', -1), 'border-bottom-color': self.getColor('success', 1)})


class CssSearchButton(CssStyle.CssCls):
  attrs = {'margin-top': '10px', 'margin-left': '10px', 'display': 'block', 'cursor': 'pointer', 'position': 'absolute'}
  cssId = {'child': 'i'}

  def customize(self, style, eventsStyles):
    style.update({"color": self.getColor("greys", 5)})
