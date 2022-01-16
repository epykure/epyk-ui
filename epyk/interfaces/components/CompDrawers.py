#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core import html
from epyk.interfaces import Arguments


class Drawers:

  def __init__(self, ui):
    self.page = ui.page

  def drawer(self, width: Union[tuple, int] = (100, '%'), height: Union[tuple, int] = (100, '%'),
             options: Optional[Union[dict, bool]] = None, profile: Optional[Union[dict, bool]] = None,
             helper: Optional[str] = None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the right.

    :tags:
    :categories:

    Usage::

      d1 = page.ui.drawer()
      d1.add_panel(page.ui.button("Test"), "ok")
      d1.drawers[0].click([d1.panels[0].dom.css({"display": 'block'})])

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/drawers.py

    Attributes:
    ----------
    :param Union[tuple, int] width: Optional. A tuple with the integer for the component width and its unit.
    :param Union[tuple, int] height: Optional. A tuple with the integer for the component height and its unit.
    :param Optional[Union[dict, bool]] options: Optional. A dictionary with the components properties.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] helper: Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlDrawer.Drawer(self.page, width, height, options, helper, profile)
    component.style.css.min_height = 200
    html.Html.set_component_skin(component)
    return component

  def left(self, width: Union[tuple, int] = (100, '%'), height: Union[tuple, int] = (200, 'px'),
           options: Optional[Union[dict, bool]] = None, profile: Optional[Union[dict, bool]] = None,
           helper: Optional[str] = None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the left.

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param Union[tuple, int] width: Optional. A tuple with the integer for the component width and its unit.
    :param Union[tuple, int] height: Optional. A tuple with the integer for the component height and its unit.
    :param Optional[Union[dict, bool]] options: Optional. A dictionary with the components properties.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] helper: Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"side": "left"}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlDrawer.Drawer(self.page, width, height, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def right(self, width: Union[tuple, int] = (100, '%'), height: Union[tuple, int] = (200, 'px'),
            options: Optional[Union[dict, bool]] = None, profile: Optional[Union[dict, bool]] = None,
            helper: Optional[str] = None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the left.

    :tags:
    :categories:

    Usage::

        button = page.ui.button("Test")

        d = page.ui.drawers.right()
        d.add_panel(page.ui.button("Test1"), "ok1")
        d.set_handle(button)

    Attributes:
    ----------
    :param Union[tuple, int] width: Optional. A tuple with the integer for the component width and its unit.
    :param Union[tuple, int] height: Optional. A tuple with the integer for the component height and its unit.
    :param Optional[Union[dict, bool]] options: Optional. A dictionary with the components properties.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] helper: Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"side": "right"}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlDrawer.Drawer(self.page, width, height, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def multi(self, component, width: Union[tuple, int] = (100, '%'), height: Union[tuple, int] = (200, 'px'),
            options: Optional[Union[dict, bool]] = None, profile: Optional[Union[dict, bool]] = None,
            helper: Optional[str] = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/multi_drawers.py

    Attributes:
    ----------
    :param component: Html component. Object in charge of managing the panel display..
    :param Union[tuple, int] width: Optional. A tuple with the integer for the component width and its unit.
    :param Union[tuple, int] height: Optional. A tuple with the integer for the component height and its unit.
    :param Optional[Union[dict, bool]] options: Optional. A dictionary with the components properties.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] helper: Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"side": "right"}
    if options is not None:
      dfl_options.update(options)
    drawer = html.HtmlDrawer.DrawerMulti(self.page, component, width, height, dfl_options, helper, profile)
    html.Html.set_component_skin(drawer)
    return drawer

  def no_handle(self, component, width: Union[tuple, int] = (100, '%'), height: Union[tuple, int] = (200, 'px'),
                options: Optional[Union[dict, bool]] = None, profile: Optional[Union[dict, bool]] = None,
                helper: Optional[str] = None):
    """
    Description:
    ------------
    Bespoke drawer without handle.
    The event to display the panel will be attached to the component.

    :tags:
    :categories:

    Usage::

      page.ui.drawers.no_handle(page.ui.button("No Handle"))

    Attributes:
    ----------
    :param component: Html component. Object in charge of managing the panel display.
    :param Union[tuple, int] width: Optional. A tuple with the integer for the component width and its unit.
    :param Union[tuple, int] height: Optional. A tuple with the integer for the component height and its unit.
    :param Optional[Union[dict, bool]] options: Optional. A dictionary with the components properties.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] helper: Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options["side"] = 'right'
    drawer = html.HtmlDrawer.Drawer(self.page, width, height, options, helper, profile)
    drawer.set_handle(component)
    html.Html.set_component_skin(drawer)
    return drawer
