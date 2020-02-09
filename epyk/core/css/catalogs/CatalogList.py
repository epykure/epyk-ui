"""

"""

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesList


class CatalogList(Catalog.CatalogGroup):

  def basic(self):
    """  """
    return self._set_class(CssStylesList.CssBasicList)

  def items(self):
    """  """
    return self._set_class(CssStylesList.CssBasicListItems)

  def item_selected(self):
    """ """
    return self._set_class(CssStylesList.CssBasicListItemsSelected)

  def item_no_decoration(self):
    """ """
    return self._set_class(CssStylesList.CssListNoDecoration)

  def item_disabled(self):
    """ """
    return self._set_class(CssStylesList.CssBasicListItemsDisabled)

  def squares(self):
    """  """
    return self._set_class(CssStylesList.CssSquareList)

  def standard(self):
    """  """
    return self._set_class(CssStylesList.CssListBase)

  def items_standard(self):
    """  """
    return self._set_class(CssStylesList.CssListLiBase)

  def sub_list(self):
    """ """
    return self._set_class(CssStylesList.CssListLiUlContainer)

  def sub_item(self):
    """ """
    return self._set_class(CssStylesList.CssListLiSubItem)


