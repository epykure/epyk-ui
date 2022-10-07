
from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesDivComms, CssStylesText, CssStylesCode


class CatalogText(Catalog.CatalogGroup):
  def bold(self):
    """
    Basic style for an input component
    """
    return self._set_class(CssStylesText.CssTextBold)

  def formula(self):
    """
    CSS Style for the formulas component
    """
    return self._set_class(CssStylesText.CssFormula)

  def title_1(self):
    """

    """
    return self._set_class(CssStylesText.CssTitle1)

  def title_2(self):
    """

    """
    return self._set_class(CssStylesText.CssTitle2)

  def title_3(self):
    """

    """
    return self._set_class(CssStylesText.CssTitle3)

  def title_4(self):
    """
    """
    return self._set_class(CssStylesText.CssTitle4)

  def title_5(self):
    """
    """
    return self._set_class(CssStylesText.CssTitle5)

  def title(self):
    """

    """
    return self._set_class(CssStylesText.CssTitle)

  def number(self):
    """

    """
    return self._set_class(CssStylesText.CssNumberCenter)

  def red(self):
    """

    """
    return self._set_class(CssStylesText.CssMarkRed)

  def colored(self):
    """
    This class will change the font color to the 7th color of the colors theme.
    The font weight will be set to bold also.
    """
    return self._set_class(CssStylesText.CssMarkBlue)

  def with_border(self):
    """
    """
    return self._set_class(CssStylesText.CssTextWithBorder)

  def check_mark(self):
    """
    """
    return self._set_class(CssStylesText.CssCheckMark)

  def item(self):
    """
    """
    return self._set_class(CssStylesText.CssTextItem)

  def no_selection(self):
    """
    Text cannot be selected
    """
    return self._set_class(CssStylesText.CssTextNotSelectable)

  def content_editable(self):
    """
    """
    return self._set_class(CssStylesDivComms.CssContentEditable)
  

class CatalogComments(Catalog.CatalogGroup):
  def header(self):
    """
    """
    return self._set_class(CssStylesDivComms.CssCommHeader)

  def input(self):
    """
    """
    return self._set_class(CssStylesDivComms.CssCommInput)

  def content_editable(self):
    """
    """
    return self._set_class(CssStylesDivComms.CssContentEditable)


class CatalogEditor(Catalog.CatalogGroup):

  def cm(self):
    """
    Group for the CSS Class for the codemirror container.
    """
    return self._set_class(CssStylesCode.CMEditor)

  def cm_gutter(self):
    """
    Group for the CSS Class for the gutter panel.

    :return:
    """
    return self._set_class(CssStylesCode.CMEditorGutters)

  def cm_activeline(self):
    """
    Group for he CSS Class for the active line background.

    :return:
    """
    return self._set_class(CssStylesCode.CMEditorActiveLine)


class CatalogFormulas(Catalog.CatalogGroup):

  def mjx(self):
    """
    Group for the CSS Class for the Mathjax container.
    """
    return self._set_class(CssStylesCode.Mjx)

  def container(self):
    """
    Group for the CSS Class for the Mathjax container.
    """
    return self._set_class(CssStylesCode.MjxContainer)

  def display(self):
    """
    Group for the CSS Class for the Mathjax display.
    """
    return self._set_class(CssStylesCode.MjxDisplay)
