"""

"""

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesImg


class CatalogImg(Catalog.CatalogGroup):
  def base(self):
    """  """
    return self._set_class(CssStylesImg.CssImgBasic)

  def paragraph(self):
    """  """
    return self._set_class(CssStylesImg.CssImgParagraph)

  def title(self):
    """  """
    return self._set_class(CssStylesImg.CssImgH2)

  def mask(self):
    """
    CSS Class definition to change a div component to a mask which will cover the parent container
    when the mouse is hover
    """
    return self._set_class(CssStylesImg.CssImgMask)

  def info_link(self):
    """
    CSS class definition to add shadow and specific colors to a link href component.
    This is used in the image section for actions on the mask or the animated image
    """
    return self._set_class(CssStylesImg.CssImgAInfo)

  def image(self):
    """  """
    return self._set_class(CssStylesImg.CssImg)

  def content(self):
    """  """
    return self._set_class(CssStylesImg.CssContent)

  def view(self):
    """  """
    return self._set_class(CssStylesImg.CssView)

  def carrousel_item(self):
    """  """
    return self._set_class(CssStylesImg.CssCarrouselLi)

  def carrousel_label(self):
    """  """
    return self._set_class(CssStylesImg.CssCarrouselLabel)

  def carrousel_title(self):
    """  """
    return self._set_class(CssStylesImg.CssCarrouselH2)

  def tns_button(self):
    """ """
    return self._set_class(CssStylesImg.CssTinySliderButton)

  def tns_button_active(self):
    """ """
    return self._set_class(CssStylesImg.CssTinySliderButtonActive)
