"""
CSS System Definition

THis property will return the pre defined CSS Style and Themes in the framework.
This will return the classes themselves to any changes there will impact the entire framework.

This is a simple and quick hook to apply override and make the environment very specific

"""


class DefinedTagStyles(object):
  def __init__(self, defined_styles):
    self.defined = defined_styles
    self._style = None

  def wrap_style(self, cls_name):
    """
    Function to wrap the class name to a function.
    This module is only dedicated to provide a simple API to the difference CSS Classes

    :param cls_name: The CSS Class name internal to the Framework

    :return: The CSS Style group object
    """
    self.defined.component.style.cssCls(cls_name)
    self._style = cls_name
    return self

  def remove(self):
    """
    Remove the current CSS class style

    :return: The CSS Style group object
    """
    self.defined.component.style.cssDelCls(self._style)
    return self


class DefinedCommonStyles(DefinedTagStyles):

  def not_selectable(self):
    """
    CSS Class to set the component not selectable
    """
    return self.wrap_style("CssNotSelect")


class DefinedChartStyles(DefinedTagStyles):
  def container_border(self):
    """

    """
    return self.wrap_style("CssDivChart")


class DefinedDivStyles(DefinedTagStyles):

  def no_border(self):
    """
    CSS Class to remove the container border
    """
    return self.wrap_style("CssDivNoBorder")

  def mouse_hover_border_bottom(self):
    """
    CSS Class to set a bottom border on move hover
    """
    return self.wrap_style("CssDivBottomBorder")

  def mouse_pointer(self):
    """
    CSS Class to set a pointer when mouse hover
    """
    return self.wrap_style("CssDivCursor")


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
