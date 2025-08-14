from . import Catalog
from ..styles.classes import CssStylesIcon


class CatalogIcon(Catalog.CatalogGroup):
    def basic(self) -> CssStylesIcon.CssIcon:
        """  """
        return self._set_class(CssStylesIcon.CssIcon)

    def standard(self) -> CssStylesIcon.CssStdIcon:
        """  """
        return self._set_class(CssStylesIcon.CssStdIcon)

    def small(self) -> CssStylesIcon.CssSmallIcon:
        """  """
        return self._set_class(CssStylesIcon.CssSmallIcon)

    def small_right(self) -> CssStylesIcon.CssSmallIconRight:
        """  """
        return self._set_class(CssStylesIcon.CssSmallIconRight)

    def small_red(self) -> CssStylesIcon.CssSmallIconRed:
        """  """
        return self._set_class(CssStylesIcon.CssSmallIconRed)

    def out(self) -> CssStylesIcon.CssOutIcon:
        """  """
        return self._set_class(CssStylesIcon.CssOutIcon)

    def big(self) -> CssStylesIcon.CssBigIcon:
        """  """
        return self._set_class(CssStylesIcon.CssBigIcon)

    def selected(self) -> CssStylesIcon.CssIconSelected:
        """  """
        return self._set_class(CssStylesIcon.CssIconSelected)
