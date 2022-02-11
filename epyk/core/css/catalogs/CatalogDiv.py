#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesDrop
from epyk.core.css.styles.classes import CssStylesDivEvents
from epyk.core.css.styles.classes import CssStylesDiv
from epyk.core.css.styles.classes import CssStylesDivShape
from epyk.core.css.styles.classes import CssStylesCommon
from epyk.core.css.styles.classes import CssStylesDivComms
from epyk.core.css.styles.classes import CssStylesDivDrawers


class CatalogDiv(Catalog.CatalogGroup):
  def basic(self) -> CssStylesDrop.CssDropFile:
    """  """
    return self._set_class(CssStylesDrop.CssDropFile)

  def bubble(self) -> CssStylesDiv.CssDivBubble:
    """  """
    return self._set_class(CssStylesDiv.CssDivBubble)

  def bubble_comment(self) -> CssStylesDiv.CssDivCommBubble:
    """  """
    return self._set_class(CssStylesDiv.CssDivCommBubble)

  def left(self) -> CssStylesDiv.CssDivLeft:
    """  """
    return self._set_class(CssStylesDiv.CssDivLeft)

  def right(self) -> CssStylesDiv.CssDivRight:
    """  """
    return self._set_class(CssStylesDiv.CssDivRight)

  def pointer(self) -> CssStylesDiv.CssDivCursor:
    """  """
    return self._set_class(CssStylesDiv.CssDivCursor)

  def banner(self) -> CssStylesDiv.CssDivBanner:
    """  """
    return self._set_class(CssStylesDiv.CssDivBanner)

  def sub_banner(self) -> CssStylesDiv.CssDivSubBanner:
    """  """
    return self._set_class(CssStylesDiv.CssDivSubBanner)

  def sub_label(self) -> CssStylesDiv.CssDivLabelPoint:
    """ """
    return self._set_class(CssStylesDiv.CssDivLabelPoint)

  def no_border(self) -> CssStylesDiv.CssDivNoBorder:
    """  """
    return self._set_class(CssStylesDiv.CssDivNoBorder)

  def border(self) -> CssStylesDiv.CssDivWithBorder:
    """  """
    return self._set_class(CssStylesDiv.CssDivWithBorder)

  def border_shadow(self) -> CssStylesDiv.CssDivShadow:
    """  """
    return self._set_class(CssStylesDiv.CssDivShadow)

  def border_dot(self) -> CssStylesDiv.CssDivBoxWithDotBorder:
    """  """
    return self._set_class(CssStylesDiv.CssDivBoxWithDotBorder)

  def border_bottom(self) -> CssStylesDiv.CssDivBottomBorder:
    """  """
    return self._set_class(CssStylesDiv.CssDivBottomBorder)

  def console(self) -> CssStylesDiv.CssDivConsole:
    """  """
    return self._set_class(CssStylesDiv.CssDivConsole)

  def margin_with_border(self) -> CssStylesDiv.CsssDivBoxMarginBorder:
    """  """
    return self._set_class(CssStylesDiv.CsssDivBoxMarginBorder)

  def no_margin(self) -> CssStylesDiv.CssDivNoMargin:
    """  """
    return self._set_class(CssStylesDiv.CssDivNoMargin)

  def margin_vertical(self) -> CssStylesDiv.CsssDivBoxMarginVertical:
    """  """
    return self._set_class(CssStylesDiv.CsssDivBoxMarginVertical)

  def content_center(self) -> CssStylesDiv.CssDivBoxCenter:
    """  """
    return self._set_class(CssStylesDiv.CssDivBoxCenter)

  def color_hover(self) -> CssStylesDivEvents.CssDivOnHover:
    """ Change the color when the mouse is on the component """
    return self._set_class(CssStylesDivEvents.CssDivOnHover)

  def danger_hover(self):
    """ Change the color when the mouse is on the component """
    return self._set_class(CssStylesDivEvents.CssDivOnDangerHover)

  def background_hover(self) -> CssStylesDivEvents.CssDivOnHoverBackgroundLight:
    """ Change the background color when the mouse is on the component """
    return self._set_class(CssStylesDivEvents.CssDivOnHoverBackgroundLight)

  def color_background_hover(self) -> CssStylesDivEvents.CssDivOnHoverColor:
    """ Change the background color when the mouse is on the component """
    return self._set_class(CssStylesDivEvents.CssDivOnHoverColor)

  def color_light_background_hover(self) -> CssStylesDivEvents.CssDivOnHoverLightColor:
    """ Change the background color when the mouse is on the component """
    return self._set_class(CssStylesDivEvents.CssDivOnHoverLightColor)

  def width_hover(self) -> CssStylesDivEvents.CssDivOnHoverWidth:
    """ Change the background color when the mouse is on the component """
    return self._set_class(CssStylesDivEvents.CssDivOnHoverWidth)

  def border_hover(self) -> CssStylesDivEvents.CssDivOnHoverBorder:
    """ Change the background color when the mouse is on the component """
    return self._set_class(CssStylesDivEvents.CssDivOnHoverBorder)

  def span_close(self) -> CssStylesCommon.CssCloseSpan:
    """Change the font size and location of the close button - generally used for the modal components"""
    return self._set_class(CssStylesCommon.CssCloseSpan)

  def modal(self) -> CssStylesDiv.CssDivModal:
    """  """
    return self._set_class(CssStylesDiv.CssDivModal)

  def modal_content(self) -> CssStylesDiv.CssDivModalContent:
    """  """
    return self._set_class(CssStylesDiv.CssDivModalContent)

  def stepper(self) -> CssStylesDiv.CssDivStepper:
    """  """
    return self._set_class(CssStylesDiv.CssDivStepper)

  def bubble_container(self) -> CssStylesDivComms.CssSpeechBubble:
    """  """
    return self._set_class(CssStylesDivComms.CssSpeechBubble)

  def bubble_content(self) -> CssStylesDivComms.CssSpeechBubbleContent:
    """  """
    return self._set_class(CssStylesDivComms.CssSpeechBubbleContent)

  def bubble_arrow(self) -> CssStylesDivComms.CssSpeechBubbleArrow:
    """  """
    return self._set_class(CssStylesDivComms.CssSpeechBubbleArrow)

  def rotate_vertical(self) -> CssStylesDiv.CssDivVerticalRotate:
    """  """
    return self._set_class(CssStylesDiv.CssDivVerticalRotate)

  def rotate_horizontal(self) -> CssStylesDiv.CssDivHorizontalRotate:
    """"""
    return self._set_class(CssStylesDiv.CssDivHorizontalRotate)

  def no_focus_outline(self) -> CssStylesDiv.CssDivNoFocusOutline:
    """"""
    return self._set_class(CssStylesDiv.CssDivNoFocusOutline)

  def cut_corner(self) -> CssStylesDiv.CssDivCutCorner:
    """"""
    return self._set_class(CssStylesDiv.CssDivCutCorner)


class CatalogDrawer(Catalog.CatalogGroup):

  def drawer(self) -> CssStylesDivDrawers.CssDrawer:
    """  The main layout for the drawer component """
    return self._set_class(CssStylesDivDrawers.CssDrawer)

  def nav(self) -> CssStylesDivDrawers.CssDrawerNav:
    """   """
    return self._set_class(CssStylesDivDrawers.CssDrawerNav)

  def handle(self) -> CssStylesDivDrawers.CssDrawerHandle:
    """  """
    return self._set_class(CssStylesDivDrawers.CssDrawerHandle)

  def content(self) -> CssStylesDivDrawers.CssDrawerContent:
    """  """
    return self._set_class(CssStylesDivDrawers.CssDrawerContent)


class CatalogShapes(Catalog.CatalogGroup):

  def page(self) -> CssStylesDivShape.CssDivPage:
    """
    Description:
    -----------
    Create a file look and feel display for a container.
    """
    return self._set_class(CssStylesDivShape.CssDivPage)

  def circle(self) -> CssStylesDivShape.CssDivCircle:
    """
    Description:
    -----------
    Create a circle look and feel display for a container.

    Related Pages:

      https://css-tricks.com/the-shapes-of-css/
    """
    return self._set_class(CssStylesDivShape.CssDivCircle)

  def parallelogram(self) -> CssStylesDivShape.Parallelogram:
    """
    Description:
    -----------
    Create a parallelogram look and feel display for a container.

    Related Pages:

      https://css-tricks.com/the-shapes-of-css/
    """
    return self._set_class(CssStylesDivShape.Parallelogram)

  def octagon(self) -> CssStylesDivShape.Octagon:
    """
    Description:
    -----------
    Create a Octagon and feel display for a container.

    Related Pages:

      https://css-tricks.com/the-shapes-of-css/
    """
    return self._set_class(CssStylesDivShape.Octagon)
