#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.styles.classes import CssStylesLoadings
from epyk.core.py import types
from epyk.core import html


class Animations:

  def __init__(self, ui):
    self.page = ui.page

  def loading_line(self, height: types.PROFILE_TYPE = (3, "px"), profile: types.PROFILE_TYPE = None,
                   html_code: str = None, options: dict = None) -> html.HtmlContainer.Div:
    """
    Description:
    -----------
    Add a loading line component.

    Related Pages:

      https://codepen.io/ziafatali/pen/mxVwpq

    Attributes:
    ----------
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    """
    component = self.page.ui.div(html_code=html_code, height=height, options=options, profile=profile)
    component.style.css.background_color = "#ddd"
    component.style.css.margin = 0
    component.style.add_classes.custom(CssStylesLoadings.CssLoadingLine)

    def stop():
      """ Stop the loading animation """
      return component.dom.removeClass("cssloadingline").r

    def start():
      """ Start the loading animation """
      return component.dom.addClass("cssloadingline").r

    component.stop = stop
    component.start = start
    return component

  def progress_cursor(self) -> html.HtmlContainer.Div:
    """
    Description:
    -----------

    Related Pages:

    """
    cursor = self.page.body.style.css.cursor
    component = self.page.ui.div()

    def stop():
      return self.page.body.dom.css("cursor", cursor or "default").r

    def start():
      return self.page.body.dom.css("cursor", "progress").r

    component.stop = stop
    component.start = start
    return component
