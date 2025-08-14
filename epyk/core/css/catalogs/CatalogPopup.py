from . import Catalog
from ..styles.classes import CssStylesPopup


class CatalogPopup(Catalog.CatalogGroup):
    def table(self):
        """  """
        return self._set_class(CssStylesPopup.CssPopupTable)

    def table_title(self):
        """  """
        return self._set_class(CssStylesPopup.CssPopupTableTitle)

    def table_content(self):
        """  """
        return self._set_class(CssStylesPopup.CssPopupTableTitleContent)

    def loading(self):
        """  """
        return self._set_class(CssStylesPopup.CssEventLoading)
