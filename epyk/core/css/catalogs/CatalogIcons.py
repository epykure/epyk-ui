"""

"""

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesIcon


class CatalogIcon(Catalog.CatalogGroup):
  def basic(self):
    """  """
    return self._set_class(CssStylesIcon.CssIcon)

  def standard(self):
    """  """
    return self._set_class(CssStylesIcon.CssStdIcon)

  def small(self):
    """  """
    return self._set_class(CssStylesIcon.CssSmallIcon)

  def small_right(self):
    """  """
    return self._set_class(CssStylesIcon.CssSmallIconRight)

  def small_red(self):
    """  """
    return self._set_class(CssStylesIcon.CssSmallIconRed)

  def out(self):
    """  """
    return self._set_class(CssStylesIcon.CssOutIcon)

  def big(self):
    """  """
    return self._set_class(CssStylesIcon.CssBigIcon)
