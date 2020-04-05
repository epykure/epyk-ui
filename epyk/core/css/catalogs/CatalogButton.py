
from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesButton


class CatalogButton(Catalog.CatalogGroup):

  def basic(self):
    """
    Description:
    -----------
    Basic style for a button
    """
    return self._set_class(CssStylesButton.CssButtonBasic)

  def important(self):
    """
    Description:
    -----------
    Important style for a button
    """
    return self._set_class(CssStylesButton.CssButtonImportant)

  def border_rounded(self):
    """
    Description:
    -----------

    """
    pass

  def reset(self):
    """
    Description:
    -----------
    """
    return self._set_class(CssStylesButton.CssButtonReset)

  def success(self):
    """
    Description:
    -----------
    """
    return self._set_class(CssStylesButton.CssButtonSuccess)

  def content(self):
    """
    Description:
    -----------
    CSS Class for the underlying item panel.
    By default this item is not visible and this will change when the mouse is hover
    """
    return self._set_class(CssStylesButton.CssButtonContentHover)

  def content_link(self):
    """
    Description:
    -----------
    CSS Class for the item link.
    This will set the background color when the mouse is hover.

    The color is deduced from the defined theme
    """
    return self._set_class(CssStylesButton.CssButtonContentAHover)
