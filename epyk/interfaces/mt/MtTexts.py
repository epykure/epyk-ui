#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.fwk.mt.js import JsMdcComponents


class Text(object):

  def __init__(self, context):
    self.context = context

  def field(self, htmlCode=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param htmlCode: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'label', 'css': None}
    label = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.TextRipple(label)
    label.style.builder(label.style.varName, dom_obj.instantiate("#%s" % label.htmlCode))
    # Add the specific dom features
    label.dom = dom_obj
    return label

  def icon(self, value, htmlCode=None):
    """
    Description:
    ------------

    Usage::

      rptObj.materials.texts.icon("favorite")

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param value:
    :param htmlCode: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'label', 'class': 'mdc-text-field mdc-text-field--with-leading-icon',
              'children': [
                {"type": 'icon', "class": "material-icons mdc-text-field__icon mdc-text-field__icon--leading",
                 'attrs': {'tabindex': 0}, 'arias': {'role': 'button'}, 'css': False, 'args': {'text': value}},
                {"type": 'input', 'class': 'mdc-text-field__input'},
                {"type": 'span', 'class': 'mdc-floating-label'},
                {"type": 'div', 'class': 'mdc-line-ripple'},
              ]
    }
    html_t = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Icon(html_t)
    html_t.style.builder(html_t.style.varName, dom_obj.instantiate("#%s" % html_t.htmlCode))
    # Add the specific dom features
    html_t.dom = dom_obj
    return html_t

  def line(self, label="", htmlCode=None):
    """
    Description:
    ------------
    Floating labels display the type of input a field requires.
    Every Text Field and Select should have a label, except for full-width text fields, which use the input’s placeholder attribute instead.

    Related Pages:

      https://material.io/develop/web/components/input-controls/floating-label/

    Attributes:
    ----------
    :param label:
    :param htmlCode: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'class': None, 'css': None, 'args': {"components": label}}
    span = self.context.rptObj.web.mt.composite(schema)
    dom_obj = JsMdcComponents.Line(span)
    span.style.builder(span.style.varName, dom_obj.instantiate("#%s" % span.htmlCode))
    # Add the specific dom features
    span.dom = dom_obj
    return span

  def floating(self, label, htmlCode=None):
    """
    Description:
    ------------
    Floating labels display the type of input a field requires.
    Every Text Field and Select should have a label, except for full-width text fields, which use the input’s placeholder attribute instead.

    Usage::

      rptObj.materials.texts.floating("Hello")

    Related Pages:

      https://material.io/develop/web/components/input-controls/floating-label/

    Attributes:
    ----------
    :param label:
    :param htmlCode: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'span', 'class': None, 'css': False, 'args': {"text": label}}
    span = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.TextFloating(span)
    span.style.builder(span.style.varName, dom_obj.instantiate("#%s" % span.htmlCode))
    # Add the specific dom features
    span.dom = dom_obj
    return span

  def chip(self, text, choice=False, htmlCode=None):
    """
    Description:
    ------------
    Chips are compact elements that allow users to enter information, select a choice, filter content, or trigger an action.

    Related Pages:

      https://material.io/develop/web/components/chips/

    Attributes:
    ----------
    :param text:
    :param choice:
    :param htmlCode: Optional. String. The component identifier code (for both Python and Javascript)
    """
    if choice:
      schema = {"type": 'div', 'class': 'mdc-chip-set--choice', 'attrs': {'role': 'grid'}, 'children': []}
    else:
      schema = {"type": 'div', 'attrs': {'role': 'grid'}, 'children': []}
    if not isinstance(text, list):
      text = [text]

    for t in text:
      schema['children'].append({"type": 'div', "class": "mdc-chip", 'css': False, 'attrs': {'role': 'row'}, 'children': [
        {"type": 'div', "class": "mdc-chip__ripple", 'css': False},
        {"type": 'icon', "class": "material-icons mdc-chip__icon mdc-chip__icon--leading", 'css': False, 'args': {'text': 'event'}},
        {"type": 'div',  'attrs': {'role': 'gridcell'}, 'css': False, 'children': [
          {"type": 'div', "class": "mdc-chip__primary-action", 'attrs': {'role': 'button'}, 'css': False, 'children': [
            {"type": 'span', "class": "mdc-chip__text", 'css': False, 'args': {'text': t}},
          ]},
        ]},
      ]})

    html_c = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Chip(html_c, html_c.style.varName)
    html_c.style.builder(html_c.style.varName, dom_obj.instantiate("#%s" % html_c.htmlCode))
    # Add the specific dom features
    html_c.dom = dom_obj
    return html_c

  def snackbar(self, text, btn_label='RETRY', btn_action=None, type='NORMAL', dismiss=True):
    """
    Description:
    ------------
    Snackbars provide brief messages about app processes at the bottom of the screen.

    Usage::

      rptObj.materials.text.checkbox(True, "test")
      rptObj.materials.inputs.checkbox(False, "test2")
      chk3 = rptObj.materials.inputs.checkbox(False, "test3")
      rptObj.js.addOnReady([chk3.dom.setStatus('indeterminate')])

    Related Pages:

        https://material.io/develop/web/components/snackbars/

    Attributes:
    ----------
    :param text: text to appear in the bar
    :param btn_label: Label to be applied to the snackbar
    :param btn_action: Action to trigger on click
    :param type: Normal, Leading or Stacked
    """
    display_map = {'NORMAL': 'mdc-snackbar', 'STACKED': 'mdc-snackbar mdc-snackbar--stacked', 'LEADING': 'mdc-snackbar mdc-snackbar--leading'}
    if dismiss:
      schema = {"type": 'div', 'class': display_map.get(type.upper(), 'mdc-snackbar'), 'css': False, 'children': [
        {"type": 'div', "class": "mdc-snackbar__surface", 'css': False, 'children': [
          {'type': 'div', 'class': 'mdc-snackbar__label', 'css': False, 'attrs': {'role': 'status'}, 'arias': {'live': 'polite'}, 'args': {'components': text}},
          {'type': 'div', 'class': 'mdc-snackbar__actions', 'css': False, 'children': [
            {'type': 'button', 'class': 'mdc-button mdc-snackbar__action', 'css': False, 'attrs': {'type': 'button'}, 'children': [
              {'type': 'div', 'class': 'mdc-button__ripple', 'css': False},
              {'type': 'span', 'class': 'mdc-button__label', 'css': False, 'args': {'text': btn_label}}
            ]},
            {'type': 'button', 'class': 'mdc-icon-button mdc-snackbar__dismiss material-icons', 'css': False, 'attrs': {'title': 'Dismiss'}, 'args': {'text': 'close'}},
          ]},
        ]},
      ]}
    else:
      schema = {"type": 'div', 'class': display_map.get(type.upper(), 'mdc-snackbar'), 'css': False, 'children': [
        {"type": 'div', "class": "mdc-snackbar__surface", 'css': False, 'children': [
          {'type': 'div', 'class': 'mdc-snackbar__label', 'css': False, 'attrs': {'role': 'status'}, 'arias': {'live': 'polite'}, 'args': {'components': text}},
          {'type': 'div', 'class': 'mdc-snackbar__actions', 'css': False, 'children': [
            {'type': 'button', 'class': 'mdc-button mdc-snackbar__action', 'css': False, 'attrs': {'type': 'button'}, 'children': [
              {'type': 'div', 'class': 'mdc-button__ripple', 'css': False},
              {'type': 'span', 'class': 'mdc-button__label', 'css': False, 'args': {'text': btn_label}}
            ]},
          ]},
        ]},
      ]}
    html_snackbar = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.SnackBar(html_snackbar)
    html_snackbar.style.builder(html_snackbar.style.varName, dom_obj.instantiate("#%s" % html_snackbar.htmlCode))
    html_snackbar.dom = dom_obj
    return html_snackbar
