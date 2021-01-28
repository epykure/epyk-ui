
from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesDivComms, CssStylesText, CssStylesCode


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

  def colored(self):
    """
    Description:
    ------------
    This class will change the font color to the 7th color of the colors theme.
    The font weight will be set to bold also.
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


class CatalogEditor(Catalog.CatalogGroup):

  def cm(self):
    """
    Description:
    ------------
    Group for the CSS Class for the codemirror container.
    """
    return self._set_class(CssStylesCode.CMEditor)

  def cm_gutter(self):
    """
    Description:
    ------------
    Group for the CSS Class for the gutter panel.

    :return:
    """
    return self._set_class(CssStylesCode.CMEditorGutters)

  def cm_activeline(self):
    """
    Description:
    ------------
    Group for he CSS Class for the active line background.

    :return:
    """
    return self._set_class(CssStylesCode.CMEditorActiveLine)
