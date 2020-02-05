"""

"""

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles import CssStylesHref


class CatalogLink(Catalog.CatalogGroup):

  def no_decoration(self):
    """  """
    return self._set_class(CssStylesHref.CssHrefNoDecoration)

  def label_dates(self):
    """  """
    return self._set_class(CssStylesHref.CssLabelDates)

  def menu(self):
    """  """
    return self._set_class(CssStylesHref.CssHreftMenu)

  def sub_menu(self):
    """  """
    return self._set_class(CssStylesHref.CssHrefSubMenu)

  def sidebar(self):
    """  """
    return self._set_class(CssStylesHref.CssSideBarLinks)

  def level_1(self):
    """  """
    return self._set_class(CssStylesHref.CssHrefContentLevel1)

  def level_2(self):
    """  """
    return self._set_class(CssStylesHref.CssHrefContentLevel2)

  def level_3(self):
    """  """
    return self._set_class(CssStylesHref.CssHrefContentLevel3)

  def level_4(self):
    """  """
    return self._set_class(CssStylesHref.CssHrefContentLevel4)

  def feedback(self):
    """  """
    return self._set_class(CssStylesHref.CssFeedbackLink)

  def standard(self):
    """  """
    return self._set_class(CssStylesHref.CssStandardLinks)
