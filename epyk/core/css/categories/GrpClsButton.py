"""
Group CSS class for all the buttons components
"""

from epyk.core.css.categories import GrpCls
from epyk.core.css.categories.groups import GrpsButton
from epyk.core.css import Properties
from epyk.core.css import Classes


class ClassButton(GrpCls.ClassHtml):
  def __init__(self, htmlObj):
    self.__htmlObj = htmlObj
    self.classList, self.__cls_defined, self.__cls_catalog = {"main": set(), 'other': set()}, None, None
    self.__load()

  def __load(self):
    if self.__cls_defined is None:
      self.__cls_defined = GrpsButton.GrpButton(self.__htmlObj._report, self.classList)
    return self.__cls_defined

  @property
  def defined(self):
    return self.__load()


class ClassButtonCheckBox(Properties.CssMixin):
  def __init__(self, rptObj, classList):
    self.__rptObj = rptObj
    self.__classList = classList
    self.__load()

  @property
  def basic(self): return Classes.CatalogButton(self.__rptObj, self.__classList['main']).basic()

  @property
  def label_disable(self): return Classes.CatalogInput(self.__rptObj, self.__classList['main']).label_disable()


# class CssClassButtonCheckBox(CssGrpCls.CssGrpClass):
#   """
#
#   """
#   css_button_basic = CssStylesLabel.CssLabelContainer
#   css_label_container_disabled = CssStylesLabel.CssLabelContainerDisabled
#   css_label_check_mark_hover = CssStylesLabel.CssLabelCheckMarkHover
#   css_div_no_border = CssStylesDiv.CssDivNoBorder
#   css_check_mark = CssStylesText.CssCheckMark
#   __map, __alt_map = ['CssButtonBasic', 'CssLabelCheckMarkHover', 'CssDivNoBorder', 'CssCheckMark',
#                       'CssLabelContainerDisabled'], []
