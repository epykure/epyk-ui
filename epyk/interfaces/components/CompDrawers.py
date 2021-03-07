#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Drawers:

  def __init__(self, ui):
    self.page = ui.page

  def drawer(self, width=(100, '%'), height=(100, '%'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the right.

    Usage:
    -----

      d1 = page.ui.drawer()
      d1.add_panel(page.ui.button("Test"), "ok")
      d1.drawers[0].click([d1.panels[0].dom.css({"display": 'block'})])

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/drawers.py

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. A dictionary with the components properties.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param helper: String. Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    h_drawer = html.HtmlDrawer.Drawer(self.page, width, height, options, helper, profile)
    h_drawer.style.css.min_height = 200
    return h_drawer

  def left(self, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the left.

    Usage:
    -----

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param helper: String. Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"side": "left"}
    if options is not None:
      dflt_options.update(options)
    h_drawer = html.HtmlDrawer.Drawer(self.page, width, height, dflt_options, helper, profile)
    return h_drawer

  def right(self, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the left.

    Usage:
    -----

        button = page.ui.button("Test")

        d = page.ui.drawers.right()
        d.add_panel(page.ui.button("Test1"), "ok1")
        d.set_handle(button)

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. A dictionary with the components properties.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param helper: String. Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"side": "right"}
    if options is not None:
      dflt_options.update(options)
    h_drawer = html.HtmlDrawer.Drawer(self.page, width, height, dflt_options, helper, profile)
    return h_drawer

  def multi(self, component, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    """
    Description:
    ------------

    Usage:
    -----

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/multi_drawers.py

    Attributes:
    ----------
    :param component: Html component. Object in charge of managing the panel display..
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param helper: String. Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"side": "right"}
    if options is not None:
      dflt_options.update(options)
    h_drawer = html.HtmlDrawer.DrawerMulti(self.page, component, width, height, dflt_options, helper, profile)
    return h_drawer

  def no_handle(self, component, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer without handle.
    The event to display the panel will be attached to the component.

    Usage:
    -----

      page.ui.drawers.no_handle(page.ui.button("No Handle"))

    Attributes:
    ----------
    :param component: Html component. Object in charge of managing the panel display.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. A dictionary with the components properties.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param helper: String. Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options["side"] = 'right'
    h_drawer = html.HtmlDrawer.Drawer(self.page, width, height, options, helper, profile)
    h_drawer.set_handle(component)
    return h_drawer
