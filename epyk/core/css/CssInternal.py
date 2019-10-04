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


class DefinedStyles(object):
  def __init__(self, htmlObj):
    self.component = htmlObj
    self.__common, self.__div = None, None

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
