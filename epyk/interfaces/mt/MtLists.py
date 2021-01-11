#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.fwk.mt.js import JsMdcComponents


class List(object):

  def __init__(self, context):
    self.context = context

  def images(self):
    """
    Description:
    ------------

    Related Pages:

      https://material.io/develop/web/components/image-lists/

    """
    pass

  def list(self, data):
    """
    Description:
    ------------

    Related Pages:

      https://material.io/develop/web/components/lists/

    Attributes:
    ----------
    :param data:
    """
    schema = {"type": 'div', 'css': False, 'children': []}
    for i, d in enumerate(data):
      schema[ 'children'].append({'type': 'item', 'class': "mdc-list-item", 'css': False, 'attrs': {"tabindex": i}, 'children': [
        {"type": 'span', 'class': "mdc-list-item__text", 'css': False, 'args': {"text": d}}
      ]})
    html_l = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.List(html_l)
    html_l.style.builder(html_l.style.varName, dom_obj.instantiate("#%s" % html_l.htmlCode))
    # Add the specific dom features
    html_l.dom = dom_obj
    return html_l

  def selections(self, data):
    """
    Description:
    ------------
    MDC List can handle selecting/deselecting list elements based on click or keyboard actions.
    When enabled, the space and enter keys (or click event) will trigger a single list item to become selected and any other previously selected element to become deselected.

    Related Pages:

      https://material.io/develop/web/components/lists/

    Attributes:
    ----------
    :param data:
    """
    schema = {"type": 'div', 'css': False, 'attrs': {'role': 'listbox'}, 'children': []}
    for i, d in enumerate(data):
      schema[ 'children'].append({'type': 'item', 'class': "mdc-list-item", 'css': False, 'attrs': {"tabindex": i, 'role': 'option'}, 'children': [
        {"type": 'span', 'class': "mdc-list-item__text", 'css': False, 'args': {"text": d}}
      ]})
    html_l = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})

    dom_obj = JsMdcComponents.List(html_l)
    html_l.style.builder(html_l.style.varName, dom_obj.instantiate("#%s" % html_l.htmlCode))
    # Add the specific dom features
    html_l.dom = dom_obj
    html_l.onReady([html_l.dom.singleSelection(True)])
    return html_l

  def radios(self, data, group_name=None):
    """
    Description:
    ------------
    When rendering list radio group with pre-selected radio button the selected list item should contain aria-checked set to true and the native radio input element contains checked attribute, all other list items should have aria-checked set to false.
    The list root contains role="radiogroup" whereas each list item within radio group contains role="radio".

    Related Pages:

      https://material.io/develop/web/components/lists/

    Attributes:
    ----------
    :param data:
    :param group_name:
    """
    if group_name is None:
      group_name = "radios_%s" % id(data)
    schema = {"type": 'list', 'css': False, 'attrs': {'role': 'radiogroup'}, 'children': []}
    for i, d in enumerate(data):
      schema['children'].append({'type': 'item', 'class': "mdc-list-item", 'css': False, 'attrs': {"tabindex": i, 'role': 'radio'}, 'arias': {'checked': False}, 'children': [
        {"type": 'div', 'class': "mdc-list-item__graphic", 'css': False, 'children': [
          {"type": 'div', "class": "mdc-radio", 'css': False, 'children': [
            {"type": 'radio', "class": "mdc-radio__native-control", 'css': False, 'attrs': {"value": d}, 'args': {'group_name': group_name}},
            {"type": 'div', "class": "mdc-radio__background", 'css': False, 'children': [
              {"type": 'div', "class": "mdc-radio__outer-circle", 'css': False},
              {"type": 'div', "class": "mdc-radio__inner-circle", 'css': False},
            ]}
          ]},
        ]},
        {"type": 'label', "class": "mdc-list-item__text", 'css': False, 'args': {"text": d}},
      ]})
    html_l = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.List(html_l)
    html_l.style.builder(html_l.style.varName, dom_obj.instantiate("#%s" % html_l.htmlCode))
    # Add the specific dom features
    html_l.dom = dom_obj
    return html_l

  def checkbox(self, data, group_name=None):
    """
    Description:
    ------------
    When rendering list with checkbox items all pre-selected list items should contain aria-checked set to true and the native checkbox input element should contain checked attribute, all other list items should have aria-checked set to false.
    Each list item in checkbox list contains role="checkbox" attribute and the list root should contain role="group" and aria-label attributes.

    Related Pages:

      https://material.io/develop/web/components/lists/

    Attributes:
    ----------
    :param data:
    :param group_name:
    """
    if group_name is None:
      group_name = "radios_%s" % id(data)
    schema = {"type": 'list', 'css': False, 'arias': {'label': 'List with checkbox items'}, 'attrs': {'role': 'group'}, 'children': []}
    for i, d in enumerate(data):
      schema[ 'children'].append({'type': 'item', 'class': "mdc-list-item", 'css': False, 'attrs': {"tabindex": i, 'role': 'checkbox'}, 'arias': {'checked': False}, 'children': [
        {"type": 'div', 'class': "mdc-list-item__graphic", 'css': False, 'children': [
          {"type": 'div', "class": "mdc-checkbox", 'css': False, 'children': [
            {"type": 'checkbox', "class": "mdc-checkbox__native-control", 'css': False, 'attrs': {"value": d}, 'args': {'flag': False}},
            {"type": 'div', "class": "mdc-checkbox__background", 'css': False}
          ]},
        ]},
        {"type": 'label', "class": "mdc-list-item__text", 'css': False, 'args': {"text": d}},
      ]})
    html_l = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.List(html_l)
    html_l.style.builder(html_l.style.varName, dom_obj.instantiate("#%s" % html_l.htmlCode))
    # Add the specific dom features
    html_l.dom = dom_obj
    return html_l
