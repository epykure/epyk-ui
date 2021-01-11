#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.fwk.mt.js import JsMdcComponents


class Inputs(object):

  def __init__(self, context):
    self.context = context

  def input(self, value="", label=""):
    """
    Description:
    ------------

    Related Pages:

      https://material-components.github.io/material-components-web-catalog/#/component/text-field?icons=leadingIcon&type=outlined

    Attributes:
    ----------
    :param text:
    :param label:
    """
    schema = {"type": 'mdc_field', 'class-keep': True, 'css': False,
              'children': [
                  {"type": 'div', 'class-keep': True, "class": "mdc-text-field__ripple", 'css': False},
                  {"type": 'input', "class": "mdc-text-field__input", 'css': False, 'args': {'text': value}},
                  {"type": 'mdc_line', 'class-keep': True, 'css': False},
                  {"type": 'mdc_floating', 'class-keep': True, 'css': False, 'args': {'label': label}},
      ]
    }

    html_b = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    return html_b

  def filled(self, value="", label="", leading_icon=None, trailing_icon=None):
    """
    Description:
    ------------

    Usage::

      text_1 = rptObj.materials.inputs.filled("Test", "Title", leading_icon="favorite")
      text_2 = rptObj.materials.inputs.filled("Test", "Title", trailing_icon="visibility")

    Related Pages:

      https://material-components.github.io/material-components-web-catalog/#/component/text-field

    Attributes:
    ----------
    :param value:
    :param label:
    :param leading_icon:
    :param trailing_icon:
    """
    schema = {"type": 'mdc_field', 'class-keep': True, 'css': False,
              'children': [
                  {"type": 'input', "class": "mdc-text-field__input", 'css': False, 'args': {'text': value}},
                  {"type": 'mdc_line', 'class-keep': True, 'css': False},
                  {"type": 'mdc_floating', 'class-keep': True, 'css': False, 'args': {'label': label}},
      ]
    }
    if leading_icon is not None:
      schema['children'] = [{"type": 'icon', 'class-keep': True, 'css': False, 'args': {'text': leading_icon, 'in_text_field': True}}] + schema['children']
    if trailing_icon is not None:
      schema['children'] = [{"type": 'icon', 'class-keep': True, 'css': False, 'args': {'text': trailing_icon, 'in_text_field': True}}] + schema['children']
    html_b = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    if leading_icon is not None:
      html_b.attr['class'].add("mdc-text-field--with-leading-icon")
    if trailing_icon is not None:
      html_b.attr['class'].add("mdc-text-field--with-trailing-icon")
    return html_b

  def outlined(self, value="", label="", leading_icon=None, trailing_icon=None):
    """
    Description:
    ------------

    Usage::

      text_1 = rptObj.materials.inputs.outlined("Test", "Title", leading_icon="favorite")
      text_2 = rptObj.materials.inputs.outlined("Test", "Title", trailing_icon="visibility")

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/

    Attributes:
    ----------
    :param value:
    :param label:
    :param leading_icon:
    :param trailing_icon:
    """
    schema = {"type": 'div', 'css': False, 'children': [
        {"type": 'input', "class": "mdc-text-field__input", 'css': False, 'args': {'text': value}},
        {"type": 'div', "class": "mdc-notched-outline", 'css': False, 'children': [
          {"type": 'div', "class": "mdc-notched-outline__leading", 'css': False},
          {"type": 'div', "class": "mdc-notched-outline__notch", 'css': False, 'children': [
            {"type": 'mdc_floating', 'class-keep': True, 'args': {'label': label}}
          ]},
          {"type": 'div', "class": "mdc-notched-outline__trailing", 'css': False},
        ]},

    ]}

    if leading_icon is not None:
      schema['children'] = [{"type": 'mdc_icon', 'class-keep': True, 'css': False, 'args': {'text': leading_icon, 'in_text_field': True}}] + schema['children']
    if trailing_icon is not None:
      schema['children'] = [{"type": 'mdc_icon', 'class-keep': True, 'css': False, 'args': {'text': trailing_icon, 'in_text_field': True}}] + schema['children']

    html_b = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})

    dom_obj_ripple = JsMdcComponents.TextRipple(html_b)
    html_b.style.builder(html_b.style.varName, dom_obj_ripple.instantiate("#%s" % html_b.htmlCode))

    dom_obj = JsMdcComponents.TextNothedOutline(html_b)
    html_b.style.builder("%s_notch" % html_b.style.varName, dom_obj.instantiate("#%s" % html_b.htmlCode))

    # Add the specific dom features
    html_b.dom = dom_obj_ripple

    if leading_icon is not None:
      html_b.attr['class'].add("mdc-text-field--with-leading-icon")
    if trailing_icon is not None:
      html_b.attr['class'].add("mdc-text-field--with-trailing-icon")
    html_b.css({"margin-top": '5px'})
    return html_b

  def textarea(self, value="", label=""):
    """
    Description:
    ------------

    Usage::

      const lineRipple = new mdc.textField.MDCTextField(document.querySelector('.mdc-text-field'));

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/

    Attributes:
    ----------
    :param value:
    :param label:
    """
    schema = {"type": 'mdc_field', 'class-keep': True, 'class': 'mdc-text-field--textarea', 'css': False, 'children': [
      {"type": 'div', "class": "mdc-text-field-character-counter", 'css': False},
      {"type": 'textarea', "class": "mdc-text-field__input", 'css': False, 'attrs': {"maxlength": 140, 'rows': 8, 'cols': 40}, 'args': {'text': value}},
      {"type": 'div', "class": "mdc-notched-outline", 'css': False, 'children': [
        {"type": 'div', "class": "mdc-notched-outline__leading", 'css': False},
        {"type": 'div', "class": "mdc-notched-outline__notch", 'css': False, 'children': [
          {"type": 'mdc_floating', 'class-keep': True, 'css': False, 'args': {'label': label}},
        ]},
        {"type": 'div', "class": "mdc-notched-outline__trailing", 'css': False},
    ]}]}
    html_r = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    return html_r

  def password(self, value="", label="", required=False, rules=None):
    """
    Description:
    ------------
    MDCTextFieldFoundation provides validity styling by using the :invalid and :required attributes provided by HTML5’s form validation API.

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/

    Attributes:
    ----------
    :param value:
    :param label:
    :param required:
    :param rules:
    """
    schema = {"type": 'mdc_field', 'class-keep': True, 'class': 'mdc-text-field--textarea', 'css': False, 'children': [
      {"type": 'div', "class": "mdc-text-field__ripple", 'css': False},
      {"type": 'input', "class": "mdc-text-field__input", 'attrs': {'type': 'password', 'value': value}, 'css': False},
      {"type": 'span', "class": "mdc-floating-label", 'css': False},
      {"type": 'mdc_line', 'class-keep': True, 'css': False, 'args': {'label': label}},
    ]}
    if required is not None:
      schema['children'][1]['attrs']["required"] = ""
    if rules is not None:
      schema['children'][1]['attrs'].update(rules)
    html_r = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    return html_r

  def html5(self, value="", label="", required=False, rules=None):
    """
    Description:
    ------------
    MDCTextFieldFoundation provides validity styling by using the :invalid and :required attributes provided by HTML5’s form validation API.

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/

    Attributes:
    ----------
    :param value:
    :param label:
    :param required:
    :param rules:
    """
    schema = {"type": 'mdc_field', 'class-keep': True, 'class': 'mdc-text-field--textarea', 'css': False, 'children': [
      {"type": 'div', "class": "mdc-text-field__ripple", 'css': False},
      {"type": 'input', "class": "mdc-text-field__input", 'attrs': {'type': 'text', 'value': value}, 'css': False},
      {"type": 'span', "class": "mdc-floating-label", 'css': False},
      {"type": 'mdc_line', 'class-keep': True, 'css': False, 'args': {'label': label}},
    ]}
    if required:
      schema['children'][1]['attrs']["required"] = ""
    if rules is not None:
      schema['children'][1]['attrs'].update(rules)
    html_r = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    return html_r

  def prefilled(self, value="", label=""):
    """
    Description:
    ------------
    When dealing with JS-driven text fields that already have values, you’ll want to ensure that you render mdc-floating-label with the mdc-floating-label--float-above modifier class.
    This will ensure that the label moves out of the way of the text field’s value and prevents a Flash Of Un-styled Content (FOUC).

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/

    Attributes:
    ----------
    :param value:
    :param label:
    """
    schema = {"type": 'mdc_field', 'class-keep': True, 'class': 'mdc-text-field--textarea', 'css': False, 'children': [
      {"type": 'div', "class": "mdc-text-field__ripple", 'css': False},
      {"type": 'input', "class": "mdc-text-field__input", 'attrs': {'type': 'text', 'value': value}, 'css': False},
      {"type": 'span', "class": "mdc-floating-label", 'css': False},
      {"type": 'mdc_line', 'class-keep': True, 'css': False, 'args': {'label': label}},
    ]}

    html_r = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    return html_r

  def mdc_radio(self, flag=False, value="", group_name=None):
    """
    Description:
    ------------
    Radio buttons allow the user to select one option from a set while seeing all available options.

    Usage::

      rptObj.materials.inputs.radio(True, group_name="group_1")
      rptObj.materials.inputs.radio(False, group_name="group_1")

    Related Pages:

      https://material.io/develop/web/components/input-controls/radio-buttons/

    Attributes:
    ----------
    :param flag:
    :param value:
    :param group_name:
    """
    schema = {"type": 'div', 'css': False, 'children': [
      {"type": 'radio', "class": "mdc-radio__native-control", 'attrs': {"value": value}, 'css': False, 'args': {'flag': flag, 'group_name': group_name}},
      {"type": 'div', "class": "mdc-radio__background", 'css': False, 'children': [
        {"type": 'div', "class": "mdc-radio__outer-circle", 'css': False},
        {"type": 'div', "class": "mdc-radio__inner-circle", 'css': False},
      ]},
      {"type": 'div', "class": "mdc-radio__ripple", 'css': False},
    ]}
    html_r = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})

    dom_obj = JsMdcComponents.Radio(html_r)
    html_r.style.builder(html_r.style.varName, dom_obj.instantiate("#%s" % html_r.htmlCode))
    # Add the specific dom features
    html_r.dom = dom_obj

    html_r.css({"margin": '5px'})
    return html_r

  def radio(self, flag=False, value="", group_name=None):
    """
    Description:
    ------------
    Radio buttons allow the user to select one option from a set while seeing all available options.

    Related Pages:

      https://material.io/develop/web/components/input-controls/radio-buttons/

    Attributes:
    ----------
    :param flag:
    :param flag:
    :param group_name:
    """
    schema = {"type": 'div', 'class': None, 'css': None, 'children': [
      {"type": 'mdc_radio', 'class-keep': True, 'css': None, 'args': {"value": value, 'flag': flag, 'group_name': group_name}}]}

    div = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    div.set_attrs({"class": None, 'css': None})

    dom_obj = JsMdcComponents.Field(div)
    div.style.builder(div.style.varName, dom_obj.instantiate("#%s" % div.htmlCode))
    # Add the specific dom features
    div.dom = dom_obj
    div.onReady([div.dom.input("radio")])
    return div

  def chip(self, text):
    """
    Description:
    ------------
    Chips are compact elements that allow users to enter information, select a choice, filter content, or trigger an action.

    Usage::

      rptObj.materials.inputs.chip(["test %s" % i for i in range(5)])

    Related Pages:

      https://material.io/develop/web/components/chips/

    Attributes:
    ----------
    :param text:
    """
    schema = {"type": 'div', 'class': 'mdc-chip-set mdc-chip-set--input', 'attrs': {'role': 'grid'}, 'children': []}
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
    dom_obj = JsMdcComponents.Chip(html_c)
    html_c.style.builder(html_c.style.varName, dom_obj.instantiate("#%s" % html_c.htmlCode))
    # Add the specific dom features
    html_c.dom = dom_obj
    return html_c

  def checkbox(self, flag, text, width=24, height=24):
    """
    Description:
    ------------
    Checkboxes allow the user to select one or more items from a set.

    Usage::

      rptObj.materials.inputs.checkbox(True, "test")
      rptObj.materials.inputs.checkbox(False, "test2")
      chk3 = rptObj.materials.inputs.checkbox(False, "test3")
      rptObj.js.addOnReady([chk3.dom.setStatus('indeterminate')])

    Related Pages:

        https://material.io/develop/web/components/input-controls/checkboxes/

    Attributes:
    ----------
    :param text:
    """

    schema = {"type": 'div', 'class': 'mdc-form-field', 'css': False, 'children': [
        {"type": 'div', "class": "mdc-checkbox", 'css': False, 'children': [
          {'type': 'checkbox', 'class': 'mdc-checkbox__native-control', 'alias': 'checkbox', 'css': False, 'args': {'flag': flag}},
          {'type': 'div', 'class': 'mdc-checkbox__background', 'css': False, 'children': [
            {'type': 'svg', 'class': 'mdc-checkbox__checkmark', 'css': False, 'attrs': {'viewBox': '0 0 %s %s' % (width, height)}, 'children': [
              {'type': 'path', 'class': 'mdc-checkbox__checkmark-path', 'css': False, 'args': {'bespoke_path': ["M1.73,12.91 8.1,19.28 22.79,4.59"]}}
            ]},
            {'type': 'div', 'class': 'mdc-checkbox__mixedmark', 'css': False}
          ]},
          {'type': 'div', 'class': 'checkbox__ripple', 'css': False}
        ]},
      {'type': 'label', 'css': False, 'args': {'text': text}}
      ]}
    html_chk = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.CheckBox(html_chk)
    if flag:
      self.context.rptObj.body.onReady([dom_obj.setStatus('checked')])
    html_chk.style.builder(html_chk.style.varName, dom_obj.instantiate("#%s" % html_chk.htmlCode))
    html_chk.dom = dom_obj
    return html_chk
