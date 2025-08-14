from . import Catalog
from ..styles.classes import CssStylesMedia


class CatalogMedia(Catalog.CatalogGroup):

    def no_phone(self):
        """ """
        return self._set_class(CssStylesMedia.CssStyleNoSmartphone)

    def font(self):
        """ """
        return self._set_class(CssStylesMedia.CssStyleFont)
