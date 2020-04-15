
from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesSelect


class CatalogSelect(Catalog.CatalogGroup):
  def base(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectStyle)

  def button(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectButton)

  def toggle(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectToggle)

  def search_box_input(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectSearchBoxInput)

  def option(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectOption)

  def item(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectOptionItems)

  def active(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectOptionActive)

  def selected(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectOptionSelected)

  def option_filter(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectFilterOption)

  def outline(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectOutline)

  def status(self):
    """  """
    return self._set_class(CssStylesSelect.CssSelectStatus)

