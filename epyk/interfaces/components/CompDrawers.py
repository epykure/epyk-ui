#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments
from epyk.core.py import types


class Drawers:

  def __init__(self, ui):
    self.page = ui.page

  def drawer(self, width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (100, '%'),
             options: dict = None, profile: types.PROFILE_TYPE = None,
             helper: str = None) -> html.HtmlDrawer.Drawer:
    """  
    Bespoke drawer with handle on the right.

    :tags:
    :categories:

    Usage::

      d1 = page.ui.drawer()
      d1.add_panel(page.ui.button("Test"), "ok")
      d1.drawers[0].click([d1.panels[0].dom.css({"display": 'block'})])

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/drawers.py
 -
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. A dictionary with the components properties
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlDrawer.Drawer(self.page, width, height, options, helper, profile)
    component.style.css.min_height = 200
    html.Html.set_component_skin(component)
    return component

  def left(self, width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (200, 'px'),
           options: dict = None, profile: types.PROFILE_TYPE = None,
           helper: str = None) -> html.HtmlDrawer.Drawer:
    """  
    Bespoke drawer with handle on the left.

    :tags:
    :categories:

    Usage::
 -
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. A dictionary with the components properties
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"side": "left"}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlDrawer.Drawer(self.page, width, height, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def right(self, width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (200, 'px'),
            options: dict = None, profile: types.PROFILE_TYPE = None,
            helper: str = None) -> html.HtmlDrawer.Drawer:
    """  
    Bespoke drawer with handle on the left.

    :tags:
    :categories:

    Usage::

        button = page.ui.button("Test")

        d = page.ui.drawers.right()
        d.add_panel(page.ui.button("Test1"), "ok1")
        d.set_handle(button)

        d.drawers[0].click([
          d.dom.hide(),
          d.panels[0].dom.css({"display": 'block'}).r,
          page.js.console.log(d.dom.content)
        ])
 -
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. A dictionary with the components properties
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"side": "right"}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlDrawer.Drawer(self.page, width, height, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def multi(self, component: html.Html.Html, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (200, 'px'), options: dict = None,
            profile: dict = None, helper: str = None) -> html.HtmlDrawer.DrawerMulti:
    """  

    :tags:
    :categories:

    Usage::

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/multi_drawers.py
 -
    :param component: Object in charge of managing the panel display
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. A dictionary with the components properties
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"side": "right"}
    if options is not None:
      dfl_options.update(options)
    drawer = html.HtmlDrawer.DrawerMulti(self.page, component, width, height, dfl_options, helper, profile)
    html.Html.set_component_skin(drawer)
    return drawer

  def no_handle(self, component: html.Html.Html, width: types.SIZE_TYPE = (100, '%'),
                height: types.SIZE_TYPE = (200, 'px'), options: dict = None,
                profile: types.PROFILE_TYPE = None,
                helper: str = None) -> html.HtmlDrawer.Drawer:
    """  
    Bespoke drawer without handle.
    The event to display the panel will be attached to the component.

    :tags:
    :categories:

    Usage::

      page.ui.drawers.no_handle(page.ui.button("No Handle"))
 -
    :param component: Object in charge of managing the panel display
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. A dictionary with the components properties
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options["side"] = 'right'
    drawer = html.HtmlDrawer.Drawer(self.page, width, height, options, helper, profile)
    drawer.set_handle(component)
    html.Html.set_component_skin(drawer)
    return drawer
