"""

"""

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles import CssStylesText
from epyk.core.css.styles import CssStylesDivComms


class CatalogText(Catalog.CatalogGroup):
  def bold(self):
    """ Basic style for an input component """
    return self._set_class(CssStylesText.CssTextBold)

  def formula(self):
    """ CSS Style for the formulas component """
    return self._set_class(CssStylesText.CssFormula)

  def title_1(self):
    """  """
    return self._set_class(CssStylesText.CssTitle1)

  def title_2(self):
    """  """
    return self._set_class(CssStylesText.CssTitle2)

  def title_3(self):
    """  """
    return self._set_class(CssStylesText.CssTitle3)

  def title_4(self):
    """  """
    return self._set_class(CssStylesText.CssTitle4)

  def title(self):
    """  """
    return self._set_class(CssStylesText.CssTitle)

  def number(self):
    """  """
    return self._set_class(CssStylesText.CssNumberCenter)

  def red(self):
    """  """
    return self._set_class(CssStylesText.CssMarkRed)

  def blue(self):
    """  """
    return self._set_class(CssStylesText.CssMarkBlue)

  def with_border(self):
    """ """
    return self._set_class(CssStylesText.CssTextWithBorder)

  def check_mark(self):
    """ """
    return self._set_class(CssStylesText.CssCheckMark)

  def item(self):
    """ """
    return self._set_class(CssStylesText.CssTextItem)

  def no_selection(self):
    """ Text cannot be selected """
    return self._set_class(CssStylesText.CssTextNotSelectable)


class CatalogComments(Catalog.CatalogGroup):
  def header(self):
    """  """
    return self._set_class(CssStylesDivComms.CssCommHeader)

  def input(self):
    """  """
    return self._set_class(CssStylesDivComms.CssCommInput)

  def content_editable(self):
    """  """
    return self._set_class(CssStylesDivComms.CssContentEditable)
