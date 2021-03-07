#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.fwk.mt.js import JsMdcComponents


class Select:

  def __init__(self, ui):
    self.page = ui.page

  def filled(self, data, label="", html_code=None):
    """
    Description:
    ------------
    The select uses an MDCMenu component instance to contain the list of options, but uses the data-value attribute
    instead of value to represent the options’ values.

    Related Pages:

      https://material.io/develop/web/components/input-controls/select-menus/

    Attributes:
    ----------
    :param data: Array. The list of data
    :param label: Optional. String. The component label
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'css': False,
      'children': [
          {"type": 'div', "class": "mdc-select__anchor demo-width-class", 'css': False, 'children': [
            {"type": 'icon', "class": "mdc-select__dropdown-icon", 'css': False},
            {"type": 'div', "class": "mdc-select__selected-text", 'css': False},
            {"type": 'mdc_floating', 'class-keep': True, 'css': False, 'args': {"label": label}},
            {"type": 'mdc_line', 'class-keep': True}]},
          {"type": 'div', "class": "mdc-select__menu mdc-menu mdc-menu-surface demo-width-class", 'css': False,
           'children': [
            {"type": 'list', "class": "mdc-list", 'css': False, 'children': [
            ]},
    ]}]}

    for d in data:
      schema['children'][1]['children'][0]['children'].append(
        {"type": 'item', "class": "mdc-list-item", 'css': False, 'args': {"text": d}, 'attrs': {"data-value": d}})
    html_b = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Select(html_b)
    html_b.style.builder(html_b.style.varName, dom_obj.instantiate("#%s" % html_b.htmlCode))
    # Add the specific dom features
    html_b.dom = dom_obj
    return html_b

  def outlined(self, data, label="", html_code=None):
    """
    Description:
    ------------
    MDC Select provides Material Design single-option select menus, using the MDC menu. The Select component is fully
    accessible, and supports RTL rendering.

    Related Pages:

      https://material.io/develop/web/components/input-controls/select-menus/

    Attributes:
    ----------
    :param data: Array. The list of data
    :param label: Optional. String. The component label
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'class': 'mdc-select--outlined', 'css': False, 'children': [
                {"type": 'div', "class": "mdc-select__anchor demo-width-class", 'css': False, 'children': [
                  {"type": 'icon', "class": "mdc-select__dropdown-icon", 'css': False},
                  {"type": 'div', "class": "mdc-select__selected-text", 'css': False},
                  {"type": 'div', "class": "mdc-notched-outline", 'css': False, 'children': [
                    {"type": 'div', "class": "mdc-notched-outline__leading", 'css': False},
                    {"type": 'div', "class": "mdc-notched-outline__notch", 'css': False, 'children': [
                      {"type": 'mdc_floating', 'class-keep': True, 'args': {"label": label}}]},
                    {"type": 'div', "class": "mdc-notched-outline__trailing", 'css': False}]},
                ]},

                {"type": 'div', "class": "mdc-select__menu mdc-menu mdc-menu-surface demo-width-class", 'css': False,
                 'children': [{"type": 'list', "class": "mdc-list", 'css': False, 'children': []}]}]}
    for d in data:
      schema['children'][1]['children'][0]['children'].append(
        {"type": 'item', "class": "mdc-list-item", 'css': False, 'args': {"text": d}, 'attrs': {"data-value": d}})
    html_b = self.page.web.mt.composite(schema, options={"reset_class": True})
    html_b.style.css.margin = 2
    dom_obj = JsMdcComponents.Select(html_b)
    html_b.style.builder(html_b.style.varName, dom_obj.instantiate("#%s" % html_b.htmlCode))
    # Add the specific dom features
    html_b.dom = dom_obj
    return html_b

