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
    self.clsMap = set(self.__map) # Main CSS Classes loaded and added to the container
    self.clsAltMap = set(self.__alt_map) # Alternate CSS classes not loaded automatically at component level
    self.src = htmlObj

  def __contains__(self, key):
    return key in self.clsMap

  def add(self, clsName): self.clsMap.add(clsName)

  def remove(self, clsName):
    if not isinstance(clsName, list):
      clsName = [clsName]
    for c in clsName:
      self.clsMap.remove(c)

  def clear(self, all=True):
    self.clsMap = set([])
    if all:
      self.clsAltMap = set([])


class CssGrpClassBase(CssGrpClass):
  """
  Default style for most of the components.

  This will remove the border and the different margin and padding of the container.
  """
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  __map, __alt_map = ['CssDivNoBorder'], []


class CssGrpClassBox(CssGrpClass):
  CsssDivBoxMargin = CssStylesDiv.CsssDivBoxMargin
  __map, __alt_map = ['CsssDivBoxMargin'], []


class CssGrpClassBaseCursor(CssGrpClass):
  """
  Default style for most of the components.

  This will remove the border and the different margin and padding of the container.
  """
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssDivCursor = CssStylesDiv.CssDivCursor
  __map, __alt_map = ['CssDivNoBorder', 'CssDivCursor'], []


class CssClassHr(CssGrpClass):
  CssHr = CssStylesHr.CssHr
  __map, __alt_map = ['CssHr'], []


class CssClassLoading(CssGrpClass):
  CssDivLoading = CssStylesDiv.CssDivLoading
  __map, __alt_map = ['CssDivLoading'], []


class CssClassSideBarFixed(CssGrpClass):
  CssSideBarFixed = CssStylesDivMenuBars.CssSideBarFixed
  __map, __alt_map = ['CssSideBarFixed'], []
