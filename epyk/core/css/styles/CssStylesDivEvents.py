"""
Module in charge of the Basic CSS events
"""


from epyk.core.css.styles import CssStyle

from epyk.core.css import Defaults as Defaults_css


class CssDivOnHover(CssStyle.CssCls):
  """ Change the color when the mouse is on the component """
  hover = {"cursor": 'pointer'}

  def customize(self, style, eventsStyles):
    eventsStyles["hover"].update({"color": '%s !IMPORTANT' % self.rptObj.theme.colors[1]})


class CssDivOnHoverBackgroundLight(CssStyle.CssCls):
  """ Change the background color when the mouse is on the component """
  attrs = {"background-color": "inherit"}
  hover = {"cursor": 'pointer'}

  def customize(self, style, eventsStyles):
    eventsStyles["hover"].update({"background-color": self.rptObj.theme.greys[2], "font-weight": 'bold',
      "color": '%s !IMPORTANT' % self.rptObj.theme.greys[-1]})


class CssDivOnHoverWidth(CssStyle.CssCls):
  """ Change the background color when the mouse is on the component """
  attrs = {"align": 'right', "background-color": "inherit",
           #"-o-transition": "width 1s ease-out",
           #"transition": "width 1s ease-out",
           #"-moz-transition": "width 1s ease-out",
           #"-webkit-transition": "width 1s ease-out",
           #'width': '50px'
  }
  hover = {"cursor": 'pointer', 'width': '150px'}

  def customize(self, style, eventsStyles):
    eventsStyles["hover"].update({"background-color": self.rptObj.theme.greys[2], "font-weight": 'bold',
      "color": '%s !IMPORTANT' % self.rptObj.theme.greys[-1]})
