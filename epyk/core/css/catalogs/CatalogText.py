
from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesDivComms, CssStylesText


class CatalogText(Catalog.CatalogGroup):
  def bold(self):
    """
    Description:
    ------------
    Basic style for an input component
    """
    return self._set_class(CssStylesText.CssTextBold)

  def formula(self):
    """
    Description:
    ------------
    CSS Style for the formulas component
    """
    return self._set_class(CssStylesText.CssFormula)

  def title_1(self):
    """
    Description:
    ------------

    """
    return self._set_class(CssStylesText.CssTitle1)

  def title_2(self):
    """
    Description:
    ------------

    """
    return self._set_class(CssStylesText.CssTitle2)

  def title_3(self):
    """
    Description:
    ------------

    """
    return self._set_class(CssStylesText.CssTitle3)

  def title_4(self):
    """
    Description:
    ------------
    """
    return self._set_class(CssStylesText.CssTitle4)

  def title(self):
    """
    Description:
    ------------

    """
    return self._set_class(CssStylesText.CssTitle)

  def number(self):
    """
    Description:
    ------------

    """
    return self._set_class(CssStylesText.CssNumberCenter)

  def red(self):
    """
    Description:
    ------------

    """
    return self._set_class(CssStylesText.CssMarkRed)

  def blue(self):
    """
    Description:
    ------------
    """
    return self._set_class(CssStylesText.CssMarkBlue)

  def with_border(self):
    """
    Description:
    ------------
    """
    return self._set_class(CssStylesText.CssTextWithBorder)

  def check_mark(self):
    """
    Description:
    ------------
    """
    return self._set_class(CssStylesText.CssCheckMark)

  def item(self):
    """
    Description:
    ------------
    """
    return self._set_class(CssStylesText.CssTextItem)

  def no_selection(self):
    """
    Description:
    ------------
    Text cannot be selected
    """
    return self._set_class(CssStylesText.CssTextNotSelectable)

  def content_editable(self):
    """
    Description:
    ------------
    """
    return self._set_class(CssStylesDivComms.CssContentEditable)
  

class CatalogComments(Catalog.CatalogGroup):
  def header(self):
    """
    Description:
    ------------
    """
    return self._set_class(CssStylesDivComms.CssCommHeader)

  def input(self):
    """
    Description:
    ------------
    """
    return self._set_class(CssStylesDivComms.CssCommInput)

  def content_editable(self):
    """
    Description:
    ------------
    """
    return self._set_class(CssStylesDivComms.CssContentEditable)
