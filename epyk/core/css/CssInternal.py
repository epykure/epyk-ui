"""
CSS System Definition

THis property will return the pre defined CSS Style and Themes in the framework.
This will return the classes themselves to any changes there will impact the entire framework.

This is a simple and quick hook to apply override and make the environment very specific

"""


class DefinedTagStyles(object):
  def __init__(self, defined_styles):
    self._defined = defined_styles
    self._style = None

  def wrap_style(self, cls_name):
    """
    Function to wrap the class name to a function.
    This module is only dedicated to provide a simple API to the difference CSS Classes

    :param cls_name: The CSS Class name internal to the Framework

    :return: The CSS Style group object
    """
    self._defined.style.cssCls(cls_name)
    self._style = cls_name
    return self

  def remove(self):
    """
    Remove the current CSS class style

    :return: The CSS Style group object
    """
    self._defined.style.cssDelCls(self._style)
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
