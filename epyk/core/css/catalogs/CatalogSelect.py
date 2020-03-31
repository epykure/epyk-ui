
from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesSelect


class CatalogSelect(Catalog.CatalogGroup):
  def base(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectStyle)

  def button(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectButton)

  def search_box(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectSearchBox)

  def search_box_input(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectSearchBoxInput)

  def option(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectOption)

  def item(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectOptionItems)

  def menu_hover(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectOptionHover)

  def active(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectOptionActive)

  def option_filter(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectFilterOption)

  def outline(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectOutline)

  def status(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectStatus)

