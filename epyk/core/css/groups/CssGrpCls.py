"""
Group CSS class for all the Layouts components
"""

# The list of CSS classes
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesDivMenuBars
from epyk.core.css.styles import CssStylesHr


class CssGrpClass(object):
  __map, __alt_map = [], []

  def __init__(self, htmlObj):
    # TODO: Rwmove those __ list
    self.clsMap = set(getattr(self, "_%s__map" % self.__class__.__name__)) # Main CSS Classes loaded and added to the container
    self.clsAltMap = set(getattr(self, "_%s__alt_map" % self.__class__.__name__)) # Alternate CSS classes not loaded automatically at component level
    self.src = htmlObj

  def __contains__(self, key):
    return key in self.clsMap

  def add(self, clsName): self.clsMap.add(clsName)

  def remove(self, clsName):
    if not isinstance(clsName, list):
      clsName = [clsName]
    for c in clsName:
      self.clsMap.remove(c)

  def ovr(self, clsName, attrs=None, eventAttrs=None, all_important=True):
    """
    Create a derived CSS Class from the base one predefined within the framework

    Example
    button.defined.ovr("CssButtonBasic", eventAttrs={'hover': {"cursor": "cell"}})

    :param clsName: The existing CSS Python Class Name
    :param attrs: Optional. A python dictionary with the attributes to be updated
    :param eventAttrs: Optional. A nested Python dictionary with the attributes to be updated
    :param all_important: Optional. A boolean flag to set the attributes to important
    """
    if clsName in self:
      self.remove(clsName)
    dervfCls = self.src._report.style.cssDerivCls(self.src.htmlId, clsName, attrs, event_attrs=eventAttrs,
                                                  force_reload=True, all_important=all_important)
    self.src._report.style.add(dervfCls.classname)
    self.add(dervfCls.classname)

  def clear(self, all=True):
    self.clsMap = set([])
    if all:
      self.clsAltMap = set([])

  def __str__(self):
    return str({"clsMap": self.clsMap, "clsAltMap": self.clsAltMap})


class CssGrpClassBase(CssGrpClass):
  """
  Default style for most of the components.

  This will remove the border and the different margin and padding of the container.
  """
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  __map, __alt_map = ['CssDivNoBorder'], []


class CssGrpClassBox(CssGrpClass):
  """

  """
  css_div_box_margin = CssStylesDiv.CsssDivBoxMargin
  __map, __alt_map = ['CsssDivBoxMargin'], []


class CssGrpClassBaseCursor(CssGrpClass):
  """

  """
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  css_div_cursor = CssStylesDiv.CssDivCursor
  __map, __alt_map = ['CssDivNoBorder', 'CssDivCursor'], []


class CssClassHr(CssGrpClass):
  """

  """
  css_hr = CssStylesHr.CssHr
  __map, __alt_map = ['CssHr'], []


class CssClassLoading(CssGrpClass):
  """

  """
  css_div_loading = CssStylesDiv.CssDivLoading
  __map, __alt_map = ['CssDivLoading'], []


class CssClassSideBarFixed(CssGrpClass):
  """

  """
  css_side_bar_fixed = CssStylesDivMenuBars.CssSideBarFixed
  __map, __alt_map = ['CssSideBarFixed'], []
