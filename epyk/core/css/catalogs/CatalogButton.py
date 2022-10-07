
from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesButton


class CatalogButton(Catalog.CatalogGroup):
  """
  Pre defined classes for all the Button components.
  """

  def basic(self) -> CssStylesButton.CssButtonBasic:
    """   Basic style for a button.

    :rtype: CssStylesButton.CssButtonBasic
    """
    return self._set_class(CssStylesButton.CssButtonBasic)

  def important(self) -> CssStylesButton.CssButtonImportant:
    """   Important style for a button.

    :rtype: CssStylesButton.CssButtonImportant
    """
    return self._set_class(CssStylesButton.CssButtonImportant)

  def reset(self) -> CssStylesButton.CssButtonReset:
    """

    :rtype: CssStylesButton.CssButtonReset
    """
    return self._set_class(CssStylesButton.CssButtonReset)

  def success(self) -> CssStylesButton.CssButtonSuccess:
    """

    :rtype: CssStylesButton.CssButtonSuccess
    """
    return self._set_class(CssStylesButton.CssButtonSuccess)

  def content(self) -> CssStylesButton.CssButtonContentHover:
    """   CSS Class for the underlying item panel.
    By default this item is not visible and this will change when the mouse is hover.

    :rtype: CssStylesButton.CssButtonContentHover
    """
    return self._set_class(CssStylesButton.CssButtonContentHover)

  def content_link(self) -> CssStylesButton.CssButtonContentAHover:
    """   CSS Class for the item link.
    This will set the background color when the mouse is hover.

    The color is deduced from the defined theme.

    :rtype: CssStylesButton.CssButtonContentAHover
    """
    return self._set_class(CssStylesButton.CssButtonContentAHover)
