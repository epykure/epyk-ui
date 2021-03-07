#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.fwk.mt.js import JsMdcComponents


class Buttons:

  def __init__(self, ui):
    self.page = ui.page

  def button(self, label):
    schema = {
      "type": 'button', 'class': "mdc-button foo-button", 'css': None, 'children': [
        {"type": 'span', 'class': 'mdc-button__ripple', 'css': None},
        {"type": 'span', 'class': 'mdc-button__label', 'css': None, 'args': {"text": label}},
      ]
    }
    button = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Button(button)
    button.style.builder(button.style.varName, dom_obj.instantiate("#%s" % button.htmlCode))
    # Add the specific dom features
    button.dom = dom_obj
    return button

  def icon(self, icon, label=""):
    """
    Description:
    ------------
    The icon button from Materials

    Related Pages:

      https://material.io/develop/web/components/buttons/floating-action-buttons/

    Attributes:
    ----------
    :param icon: String. The icon from Materials Icons
    :param label: String. The label
    """
    self.page.cssImport.add("material-icons")
    if label:
      schema = {"type": 'button', 'class': None, 'css': None, 'arias': {"pressed": False}, 'children': [
        {"type": 'div', 'class': 'mdc-button__ripple', 'css': None},
        {"type": 'span', 'class': 'mdc-button__label', 'css': None, 'args': {"text": label}},
        {"type": 'div', 'class': 'material-icons mdc-button__icon', 'css': None, 'args': {"components": icon}}
      ]}
    else:
      schema = {"type": 'button', 'class': None, 'css': None, 'arias': {"pressed": False}, 'children': [
        {"type": 'div', 'class': 'mdc-fab__ripple', 'css': None},
        {"type": 'span', 'class': 'mdc-fab__icon material-icons', 'css': None, 'args': {"text": icon}}
      ]}
    button = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Button(button)
    button.style.builder(button.style.varName, dom_obj.instantiate("#%s" % button.htmlCode))
    # Add the specific dom features
    button.dom = dom_obj
    return button

  def toggle(self, flag, html_code=None, profile=None):
    """
    Description:
    ------------
    Switches communicate an action a user can take. They are typically placed throughout your UI, in places like dialogs, forms, cards, and toolbars.

    Related Pages:

      https://material-components.github.io/material-components-web-catalog/#/component/switch
      https://material-components.github.io/material-components-web-catalog/#/component/switch

    Attributes:
    ----------
    :param flag: Boolean. The init state of the toggle component.
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    :param profile: Optional. Not yet available
    """
    schema = {"type": 'div', 'css': False, 'children': [
        {"type": 'div', "class": "mdc-switch__track", 'css': False},
        {"type": 'div', "class": "mdc-switch__thumb-underlay", 'css': False, 'children': [
          {"type": 'div', "class": "mdc-switch__thumb", 'css': False},
          {"type": 'checkbox', "class": "mdc-switch__native-control", 'args': {'flag': flag},
           'aria': {'role': 'switch', 'checked': flag}}
    ]}]}

    html_b = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.ButtonSwitch(html_b)
    html_b.style.builder(html_b.style.varName, dom_obj.instantiate("#%s" % html_b.htmlCode))
    # Add the specific dom features
    html_b.dom = dom_obj
    html_b.style.css.margin = 5
    return html_b


class FloatingButton:

  def __init__(self, ui):
    ui.page.jsImports.add("material-components-web")
    ui.page.cssImport.add("material-components-web")
    self.page = ui.page

  def button(self, icon, mini=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param icon: String. The icon from Materials Icons
    """
    self.page.cssImport.add("material-icons")
    schema = {"type": 'button', 'class': None, 'css': None, 'arias': {"pressed": False}, 'children': [
      {"type": 'div', 'class': 'mdc-fab__ripple', 'css': None},
      {"type": 'mdc_icon', 'class-keep': True, 'class': 'mdc-fab__icon', 'css': None, 'args': {"text": icon}},
    ]}

    if mini:
      schema['class'] = "mdc-fab--mini"

    button = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.FAB(button)
    button.style.builder(button.style.varName, dom_obj.instantiate("#%s" % button.htmlCode))
    # Add the specific dom features
    button.dom = dom_obj
    return button

  def extended(self, label, icon=None, mini=False):
    """
    Description:
    ------------
    NOTE: The extended FAB must contain label where as the icon is optional.
    The icon and label may be specified in whichever order is appropriate based on context.

    Attributes:
    ----------
    :param icon: String. The icon from Materials Icons
    """
    schema = {"type": 'button', 'class': "mdc-fab--extended", 'css': None, 'children': [
      {"type": 'div', 'class': 'mdc-fab__ripple', 'css': None},
      {"type": 'span', 'class': 'mdc-fab__label', 'css': None, 'args': {"text": label}},
    ]}
    if mini:
      schema['class'] += " mdc-fab--mini"
    if icon is not None:
      self.page.cssImport.add("material-icons")
      schema['children'].insert(1, {"type": 'mdc_icon', 'class-keep': True, 'class': 'mdc-fab__icon', 'css': None,
                                    'args': {"text": icon}})

    button = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.FAB(button)
    button.style.builder(button.style.varName, dom_obj.instantiate("#%s" % button.htmlCode))
    # Add the specific dom features
    button.dom = dom_obj
    return button
