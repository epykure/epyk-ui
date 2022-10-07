
from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStyleDropdown


class CatalogDropDown(Catalog.CatalogGroup):

  def base(self):
    """
    """
    return self._set_class(CssStyleDropdown.CssDropDownSubMenu)

  def menu(self):
    """
    """
    return self._set_class(CssStyleDropdown.CssDropDownMenu)

  def menu_li(self):
    """
    """
    return self._set_class(CssStyleDropdown.CssDropDownMenuHLi)

  def menu_after(self):
    """
    """
    return self._set_class(CssStyleDropdown.CssDropDownAfterMenu)

  def menu_hover(self):
    """
    """
    return self._set_class(CssStyleDropdown.CssDropDownMenuHoverAAfter)

  def menu_pull_left(self):
    """
    """
    return self._set_class(CssStyleDropdown.CssDropDownSubMenuPullLeft)

  def menu_caret(self):
    """
    """
    return self._set_class(CssStyleDropdown.CssDropDownCaret)
