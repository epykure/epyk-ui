#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.interfaces.mt import MtButtons
from epyk.interfaces.mt import MtInputs
from epyk.interfaces.mt import MtIcons
from epyk.interfaces.mt import MtSliders
from epyk.interfaces.mt import MtNavigation
from epyk.interfaces.mt import MtTexts
from epyk.interfaces.mt import MtLists
from epyk.interfaces.mt import MtMenus
from epyk.interfaces.mt import MtSelects

from epyk.fwk.mt.html import MdcHtml


class Materials(object):

  def __init__(self, rptObj):
    self.rptObj = rptObj
    self.navbar = self.navigation.top_bar #: shortcut for bar :func:`epyk.interfaces.components.CompNavigation.Navigation.bar`

    # Shortcut for the main components
    self.icon = self.icons.icon
    self.fab = self.fabs.button
    self.button = self.buttons.button
    self.select = self.selects.filled
    self.list = self.lists.list
    self.menu = self.menus.anchor
    self.switch = self.buttons.toggle
    self.radio = self.inputs.radio
    self.slider = self.sliders.slider
    self.tabs = self.navigation.tabs
    self.drawers = self.navigation.drawers
    self.new_line = self.rptObj.web.std.layouts.new_line

  @property
  def selects(self):
    """
    Description:
    ------------
    MDC Select provides Material Design single-option select menus, using the MDC menu. The Select component is fully accessible, and supports RTL rendering.

    Related Pages:

      https://material.io/develop/web/components/input-controls/select-menus/
    """
    return MtSelects.Select(self)

  @property
  def menus(self):
    """
    Description:
    ------------
    A menu displays a list of choices on a temporary surface. They appear when users interact with a button, action, or other control.

    Related Pages:

      https://material.io/develop/web/components/menus/
    """
    return MtMenus.Menu(self)

  @property
  def lists(self):
    """
    Description:
    ------------
    Lists are continuous, vertical indexes of text or images.

    Related Pages:

      https://material.io/develop/web/components/lists/
    """
    return MtLists.List(self)

  @property
  def texts(self):
    """
    Description:
    ------------
    MDC Form Field aligns an MDC Web form field (for example, a checkbox) with its label and makes it RTL-aware.
    It also activates a ripple effect upon interacting with the label.

    Related Pages:

      https://material.io/develop/web/components/input-controls/form-fields/
    """
    return MtTexts.Text(self)

  @property
  def navigation(self):
    """
    Description:
    ------------
    The MDC Linear Progress component is a spec-aligned linear progress indicator component adhering to the Material Design progress & activity requirements.

    Related Pages:

      https://material.io/develop/web/components/linear-progress/
    """
    return MtNavigation.Navigation(self)

  @property
  def fabs(self):
    """
    Description:
    ------------
    A floating action button represents the primary action in an application.

    Related Pages:

      https://material.io/develop/web/components/buttons/floating-action-buttons/
    """
    return MtButtons.FloatingButton(self)

  @property
  def buttons(self):
    """
    Description:
    ------------
    Buttons allow users to take actions, and make choices, with a single tap.

    Related Pages:

      https://material.io/develop/web/components/buttons/
    """
    return MtButtons.Buttons(self)

  @property
  def inputs(self):
    """
    Description:
    ------------
    """
    return MtInputs.Inputs(self)

  @property
  def icons(self):
    """
    Description:
    ------------
    MDC Form Field aligns an MDC Web form field (for example, a checkbox) with its label and makes it RTL-aware.
    It also activates a ripple effect upon interacting with the label.

    Related Pages:

      https://material.io/develop/web/components/input-controls/form-fields/
    """
    return MtIcons.Icon(self)

  @property
  def sliders(self):
    """
    Description:
    ------------
    MDC Slider provides an implementation of the Material Design slider component.
    It is modeled after the browser’s <input type="range"> element. Sliders are fully RTL-aware, and conform to the WAI-ARIA slider authoring practices.

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/
    """
    return MtSliders.Slider(self)

  def composite(self, schema, width=(None, "%"), height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Composite bespoke object.

    This object will be built based on its schema. No specific CSS Style and class will be added to this object.
    The full definition will be done in the nested dictionary schema.

    Usage::

      schema = {'type': 'div', 'css': {}, 'class': , 'attrs': {} 'arias': {},  'children': [
          {'type': : {...}}
          ...
      ]}

    Attributes:
    ----------
    :param schema: Dictionary. The schema of the composite item with the different sub items
    :param width: Optional. Tuple. The component width in pixel or percentage
    :param height: Optional. Tuple. The component height in pixel or percentage
    :param htmlCode: Optional. String. The component identifier code (for both Python and Javascript)
    :param helper: Optional. String. Optional. The helper message
    :param options: Optional. Dictionary. the component specific items
    :param profile: Optional. Not yet available
    """
    html_help = MdcHtml.MdcComposite(self.rptObj, schema, width=width, height=height, htmlCode=htmlCode,
                                     profile=profile, options=options or {}, helper=helper)
    return html_help
