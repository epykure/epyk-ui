#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Drawers(object):

  def __init__(self, context):
    self.context = context

  def drawer(self, width=(100, '%'), height=(100, '%'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the right.

    Usage::

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/drawers.py

    Attributes:
    ----------
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. A dictionary with the components properties
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    h_drawer = html.HtmlDrawer.Drawer(self.context.rptObj, width, height, options, helper, profile)
    h_drawer.style.css.min_height = 200
    return h_drawer

  def left(self, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the left.

    Usage::


    Attributes:
    ----------
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"side": "left"}
    if options is not None:
      dflt_options.update(options)
    h_drawer = html.HtmlDrawer.Drawer(self.context.rptObj, width, height, dflt_options, helper, profile)
    return h_drawer

  def right(self, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the left.

    Usage::


    Attributes:
    ----------
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. A dictionary with the components properties
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"side": "right"}
    if options is not None:
      dflt_options.update(options)
    h_drawer = html.HtmlDrawer.Drawer(self.context.rptObj, width, height, dflt_options, helper, profile)
    return h_drawer

  def multi(self, component, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    """
    Description:
    ------------

    Usage::

    Temapltes:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/multi_drawers.py

    Attributes:
    ----------
    :param component:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"side": "right"}
    if options is not None:
      dflt_options.update(options)
    h_drawer = html.HtmlDrawer.DrawerMulti(self.context.rptObj, component, width, height, dflt_options, helper, profile)
    return h_drawer

  def no_handle(self, component, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer without handle.
    The event to display the panel will be attached to the component.

    Usage::


    Attributes:
    ----------
    :param component: Html component. Object in charge of managing the panel display
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
    h_drawer = html.HtmlDrawer.Drawer(self.context.rptObj, width, height, options, helper, profile)
    h_drawer.set_handle(component)
    return h_drawer

