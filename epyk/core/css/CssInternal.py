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


class DefinedStyles(object):
  def __init__(self, htmlObj):
    self.component = htmlObj
    self.__common = None

  @property
  def commons(self):
    """
    All the defined commons styles
    """
    if self.__common is None:
      self.__common = DefinedCommonStyles(self)
    return self.__common

