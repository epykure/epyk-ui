
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
