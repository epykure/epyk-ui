"""
Module in charge of the Basic CSS events
"""


from epyk.core.css.styles import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssDivOnHover(CssStyle.CssCls):
  """ Change the color when the mouse is on the component """
  hover = {"cursor": 'pointer'}

  def customize(self, style, eventsStyles):
    eventsStyles["hover"].update({"color": '%s !IMPORTANT' % self.getColor("colors", 1)})


class CssDivOnHoverBackgroundLight(CssStyle.CssCls):
  """ Change the background color when the mouse is on the component """
  hover = {"cursor": 'pointer'}

  def customize(self, style, eventsStyles):
    eventsStyles["hover"].update({"background-color": self.getColor("greys", 2), "font-weight": 'bold',
      "color": '%s !IMPORTANT' % self.getColor("greys", -1)})
