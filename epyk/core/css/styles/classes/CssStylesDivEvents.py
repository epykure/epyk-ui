"""
Module in charge of the Basic CSS events
"""

from epyk.core.css.styles.classes import CssStyle


class CssDivOnHover(CssStyle.Style):
  """
  Change the color when the mouse is on the component
  """
  _hover = {"cursor": 'pointer'}

  def customize(self):
    self.hover.css({"color": self.page.theme.colors[-1]}, important=True)


class CssDivOnDangerHover(CssStyle.Style):
  """
  Change the color when the mouse is on the component
  """
  _hover = {"cursor": 'pointer'}

  def customize(self):
    self.hover.css({"color": self.page.theme.danger[1]}, important=True)


class CssDivOnHoverBackgroundLight(CssStyle.Style):
  """
  Change the background color when the mouse is on the component
  """
  _attrs = {"background-color": "inherit"}
  _hover = {"cursor": 'pointer'}

  def customize(self):
    self.css({'border': "1px solid %s" % self.page.theme.greys[0]})
    self.hover.css({
      'border': "1px solid %s" % self.page.theme.colors[1],
      "background-color": self.page.theme.colors[0], "text-decoration": 'underline'})
    self.hover.css('color', self.page.theme.greys[-1], important=True)


class CssDivOnHoverColor(CssStyle.Style):
  """
  Change the background color when the mouse is on the component
  """
  _attrs = {"background-color": "inherit"}
  _hover = {"cursor": 'pointer'}

  def customize(self):
    self.hover.css({"background-color": self.page.theme.colors[-3]}, important=True)
    self.hover.css('color', self.page.theme.colors[0], important=True)


class CssDivOnHoverLightColor(CssStyle.Style):
  """
  Change the background color when the mouse is on the component
  """
  _attrs = {"background-color": "inherit"}
  _hover = {"cursor": 'pointer'}

  def customize(self):
    self.hover.css({"background-color": self.page.theme.colors[1]}, important=True)


class CssDivOnHoverWidth(CssStyle.Style):
  """
  Change the background color when the mouse is on the component
  """
  _attrs = {"align": 'right', "background-color": "inherit"}
  _hover = {"cursor": 'pointer', 'width': '150px'}

  def customize(self):
    self.hover.css({"background-color": self.page.theme.greys[2], "font-weight": 'bold'})
    self.hover.css('color', self.page.theme.greys[-1], important=True)


class CssDivOnHoverBorder(CssStyle.Style):
  def customize(self):
    self.css({"border": "2px solid %s" % self.page.theme.colors[0]})
    self.hover.css({'border': "2px solid %s" % self.page.theme.colors[-1]})
