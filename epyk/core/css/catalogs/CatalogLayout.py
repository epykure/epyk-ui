#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesHr, CssStylesScrollBar
from epyk.core.css.styles.classes import CssStylesSearch, CssStylesCommon, CssStylesDivMenuBars, CssStylesPanel


class CatalogLayout(Catalog.CatalogGroup):
  def hr(self):
    """  """
    return self._set_class(CssStylesHr.CssHr)

  def body(self):
    """  """
    return self._set_class(CssStylesCommon.CssBody)

  def body_content(self):
    """  """
    return self._set_class(CssStylesCommon.CssBodyContent)

  def loading(self):
    """  """
    return self._set_class(CssStylesCommon.CssBodyLoadingBack)

  def selection(self):
    """  """
    return self._set_class(CssStylesCommon.CssTextSelection)

  def panel_arrow_down(self):
    """  """
    return self._set_class(CssStylesPanel.CssPanelArrowDown)

  def panel_arrow_up(self):
    """  """
    return self._set_class(CssStylesPanel.CssPanelArrowUp)

  def menubar(self):
    """  """
    return self._set_class(CssStylesDivMenuBars.CssSideBarMenu)

  def menubar_fixed(self):
    """  """
    return self._set_class(CssStylesDivMenuBars.CssSideBarFixed)

  def menubar_bubble(self):
    """  """
    return self._set_class(CssStylesDivMenuBars.CssSideBarBubble)

  def menubar_side(self):
    """  """
    return self._set_class(CssStylesDivMenuBars.CssSideBar)

  def menubar_link(self):
    """  """
    return self._set_class(CssStylesDivMenuBars.CssSideBarLiHref)

  def menubar_item(self):
    """  """
    return self._set_class(CssStylesDivMenuBars.CssSideBarLi)

  def menubar_params(self):
    """  """
    return self._set_class(CssStylesDivMenuBars.CssParamsBar)

  def search(self):
    """  """
    return self._set_class(CssStylesSearch.CssSearch)

  def search_extension(self, max_width=(100, '%')):
    """
    Description:
    -----------
    Attached the div extension class to the component.

    :param max_width: Tuple. Optional. The maximum with for the component. Default 100%.
    """
    cssObj = CssStylesSearch.CssSearchExt(self.page, html_id=self._html_id)
    cssObj.classname = "%s_%s%s" % (cssObj.classname, max_width[0], max_width[1])
    cssObj.hover.css({"width": "%s%s" % (max_width[0], max_width[1])})
    return self._add_class(cssObj)

  def search_button(self):
    """  """
    return self._set_class(CssStylesSearch.CssSearchButton)

  def scrollbar(self):
    """  """
    return self._set_class(CssStylesScrollBar.CssScrollBar)

  def scrollbar_track(self):
    """  """
    return self._set_class(CssStylesScrollBar.CssScrollBarTrack)

  def scrollbar_track_thumb(self):
    """  """
    return self._set_class(CssStylesScrollBar.CssScrollBarTrackThumb)

  def hover_reduce(self):
    """  """
    return self._set_class(CssStylesCommon.CssHoverReduce)

  def hover_colored(self):
    """  """
    return self._set_class(CssStylesCommon.CssHoverColored)

  def hover_zoom(self):
    """  """
    return self._set_class(CssStylesCommon.CssHoverZoom)

  def hover_large_zoom(self):
    """  """
    return self._set_class(CssStylesCommon.CssHoverLargeZoom)

  def hover_rotate(self):
    """  """
    return self._set_class(CssStylesCommon.CssHoverRotate)
