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
    """  """
    return self._set_class(CssStylesImg.CssImgMask)

  def info_link(self):
    """  """
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

