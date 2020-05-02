
from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesDrop
from epyk.core.css.styles.classes import CssStylesDivEvents
from epyk.core.css.styles.classes import CssStylesDiv
from epyk.core.css.styles.classes import CssStylesCommon
from epyk.core.css.styles.classes import CssStylesDivDrawers


class CatalogDiv(Catalog.CatalogGroup):
  def basic(self):
    """  """
    return self._set_class(CssStylesDrop.CssDropFile)

  def bubble(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivBubble)

  def bubble_comment(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivCommBubble)

  def left(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivLeft)

  def right(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivRight)

  def pointer(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivCursor)

  def banner(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivBanner)

  def sub_banner(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivSubBanner)

  def sub_label(self):
    """ """
    return self._set_class(CssStylesDiv.CssDivLabelPoint)

  def no_border(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivNoBorder)

  def border(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivWithBorder)

  def border_shadow(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivShadow)

  def border_dot(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivBoxWithDotBorder)

  def border_bottom(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivBottomBorder)

  def console(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivConsole)

  def margin_with_border(self):
    """  """
    return self._set_class(CssStylesDiv.CsssDivBoxMarginBorder)

  def no_margin(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivNoMargin)

  def margin_vertical(self):
    """  """
    return self._set_class(CssStylesDiv.CsssDivBoxMarginVertical)

  def content_center(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivBoxCenter)

  def color_hover(self):
    """ Change the color when the mouse is on the component """
    return self._set_class(CssStylesDivEvents.CssDivOnHover)

  def background_hover(self):
    """ Change the background color when the mouse is on the component """
    return self._set_class(CssStylesDivEvents.CssDivOnHoverBackgroundLight)

  def width_hover(self):
    """ Change the background color when the mouse is on the component """
    return self._set_class(CssStylesDivEvents.CssDivOnHoverWidth)

  def span_close(self):
    """Change the font size and location of the close button - generally used for the modal components"""
    return self._set_class(CssStylesCommon.CssCloseSpan)

  def modal(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivModal)

  def modal_content(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivModalContent)

  def stepper(self):
    """  """
    return self._set_class(CssStylesDiv.CssDivStepper)


class CatalogDrawer(Catalog.CatalogGroup):

  def drawer(self):
    """  The main layout for the drawer compenent """
    return self._set_class(CssStylesDivDrawers.CssDrawer)

  def nav(self):
    """   """
    return self._set_class(CssStylesDivDrawers.CssDrawerNav)

  def handle(self):
    """  """
    return self._set_class(CssStylesDivDrawers.CssDrawerHandle)

  def content(self):
    """  """
    return self._set_class(CssStylesDivDrawers.CssDrawerContent)
