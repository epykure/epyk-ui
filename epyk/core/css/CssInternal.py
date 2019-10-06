"""
CSS System Definition

THis property will return the pre defined CSS Style and Themes in the framework.
This will return the classes themselves to any changes there will impact the entire framework.

This is a simple and quick hook to apply override and make the environment very specific

"""

import epyk.core.css.themes as themes
import epyk.core.css.styles as css


class DefinedCommonStyles(object):

  def __init__(self, defined_styles):
    self.defined = defined_styles

  def not_selectable(self):
    """
    CSS Class to set the component not selectable
    """
    self.defined.component.style.cssCls("CssNotSelect")
    return self


class DefinedChartStyles(object):
  def __init__(self, defined_styles):
    self.defined = defined_styles
    self._style = None

  def container_border(self):
    """

    """
    self.defined.component.style.cssCls("CssDivChart")
    self._style = "CssDivChart"
    return self

  def remove(self):
    """
    Remove the current CSS class style

    :return:
    """
    self.defined.component.style.cssDelCls(self._style)
    return self


class DefinedDivStyles(object):

  def __init__(self, defined_styles):
    self.defined = defined_styles

  def no_border(self):
    """
    CSS Class to remove the container border
    """
    self.defined.component.style.cssCls("CssDivNoBorder")
    return self

  def mouse_hover_border_bottom(self):
    """
    CSS Class to set a bottom border on move hover
    """
    self.defined.component.style.cssCls("CssDivBottomBorder")
    return self

  def mouse_pointer(self):
    """
    CSS Class to set a pointer when mouse hover
    """
    self.defined.component.style.cssCls("CssDivCursor")
    return self


class DefinedStyles(object):
  def __init__(self, htmlObj):
    self.component = htmlObj
    self.__common, self.__div, self.__chart = None, None, None

  @property
  def commons(self):
    """
    All the defined commons styles
    """
    if self.__common is None:
      self.__common = DefinedCommonStyles(self)
    return self.__common

  @property
  def div(self):
    """
    All the defined Div styles
    """
    if self.__div is None:
      self.__div = DefinedDivStyles(self)
    return self.__div

  @property
  def chart(self):
    """
    All the defined Chart styles
    """
    if self.__chart is None:
      self.__chart = DefinedChartStyles(self)
    return self.__chart
