"""

"""

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesButton


class CatalogButton(Catalog.CatalogGroup):
  """

  """
  def basic(self):
    """ Basic style for a button """
    return self._set_class(CssStylesButton.CssButtonBasic)

  def border_rounded(self):
    pass

  def reset(self):
    """ """
    return self._set_class(CssStylesButton.CssButtonReset)

  def success(self):
    """ """
    return self._set_class(CssStylesButton.CssButtonSuccess)
