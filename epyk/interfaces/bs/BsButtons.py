#!/usr/bin/python
# -*- coding: utf-8 -*-


class Buttons(object):

  def __init__(self, context):
    self.context = context

  def block(self, text, category="primary", format='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param category:
    :param format:
    """
    schema = {"type": 'button', 'class': 'btn', 'arias': {'pressed': False}, 'css': None, 'args': {'text': text}}
    button = self.context.rptObj.web.bs.composite(schema, options={"reset_class": True})
    button.attr['class'].add("btn-%s" % category)
    button.attr['class'].add("btn-%s" % format)
    button.attr['class'].add("btn-block")
    button.attr['data-toggle'] = "button"
    return button

  def small(self, text, category="primary"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param category:
    """
    schema = {"type": 'button', 'class': 'btn btn-sm', 'arias': {'pressed': False}, 'css': None, 'args': {'text': text}}
    button = self.context.rptObj.web.bs.composite(schema, options={"reset_class": True})
    button.attr['class'].add("btn-%s" % category)
    button.attr['data-toggle'] = "button"
    return button

  def long(self, text, category="primary"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param category:
    """
    schema = {"type": 'button', 'class': 'btn btn-lg', 'arias': {'pressed': False}, 'css': None, 'args': {'text': text}}
    button = self.context.rptObj.web.bs.composite(schema, options={"reset_class": True})
    button.attr['class'].add("btn-%s" % category)
    button.attr['data-toggle'] = "button"
    return button

  def button(self, text, category="primary", format='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param category:
    :param format:
    """
    schema = {"type": 'button', 'class': 'btn', 'arias': {'pressed': False}, 'css': None, 'args': {'text': text}}
    button = self.context.rptObj.web.bs.composite(schema, options={"reset_class": True})
    button.attr['class'].add("btn-%s" % category)
    button.attr['class'].add("btn-%s" % format)
    button.attr['data-toggle'] = "button"
    return button

  def checked(self, text, category="primary"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param category:
    """
    schema = {"type": 'div', 'class': 'btn-group-toggle', 'arias': {'pressed': False}, 'css': None, 'children': [
      {"type": 'label', 'css': None, 'class': 'btn btn-%s active' % category, 'children': [
        {'type': 'checkbox', 'css': None, 'args': {'flag': True, 'label': text}}
      ]}
    ]}
    button = self.context.rptObj.web.bs.composite(schema, options={"reset_class": True})
    button.attr['data-toggle'] = "button"
    return button

  def toolbar(self):
    """
    Description:
    ------------
    Combine sets of button groups into button toolbars for more complex components. Use utility classes as needed to space out groups, buttons, and more.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/button-group/
    """
    container = self.context.rptObj.web.std.div()
    container.attr['class'].add('btn-toolbar')
    container.attr['role'] = 'toolbar'
    return container

  def group(self, vertical=False):
    """
    Description:
    ------------
    Wrap a series of buttons with .btn in .btn-group. Add on optional JavaScript radio and checkbox style behavior with our buttons plugin.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/button-group/

    Attributes:
    ----------
    :param vertical:
    """
    container = self.context.rptObj.web.std.div()
    if vertical:
      container.attr['class'].add('btn-group-vertical')
    else:
      container.attr['class'].add('btn-group')
    return container

  def dropdown(self, text, values, category="primary"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param values:
    :param category:
    """
    schema = {"type": 'div', 'class': 'btn-group', 'attrs': {'role': 'group'}, 'css': None, 'children': [
      {'type': 'button', 'css': None, 'class': 'btn btn-%s dropdown-toggle' % category, 'attrs': {'data-toggle': 'dropdown'}, 'args': {'text': text}},
      {"type": 'div', 'css': None, 'class': 'dropdown-menu', 'children': []}
    ]}

    for v in values:
      schema['children'][1]['children'].append({'type': 'link', 'css': None, 'class': 'dropdown-item', 'args': {'text': v, 'url': '#'}})
    button = self.context.rptObj.web.bs.composite(schema, options={"reset_class": True})
    button.attr['data-toggle'] = "button"
    return button

  def primary(self, text, format='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param format:
    """
    button = self.button(text, category="primary", format=format)
    return button

  def secondary(self, text, format='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param format:
    """
    button = self.button(text, category="secondary", format=format)
    return button

  def success(self, text, format='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param format:
    """
    button = self.button(text, category="success", format=format)
    return button

  def danger(self, text, format='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param format:
    """
    button = self.button(text, category="danger", format=format)
    return button

  def warning(self, text, format='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param format:
    """
    button = self.button(text, category="warning", format=format)
    return button

  def info(self, text, format='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param format:
    """
    button = self.button(text, category="info", format=format)
    return button

  def light(self, text, format='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param format:
    """
    button = self.button(text, category="light", format=format)
    return button

  def dark(self, text, format='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param format:
    """
    button = self.button(text, category="dark", format=format)
    return button

  def link(self, text, format='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param format:
    """
    button = self.button(text, category="link", format=format)
    return button

  def close(self, dismiss=""):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param dismiss:
    """
    schema = {"type": 'button', 'class': 'close', 'attrs': {'data-dismiss': dismiss}, 'arias': {'label': 'Close'}, 'css': None, 'children': [
      {"type": 'span', 'css': None, 'arias': {"hidden": True}, 'args': {"text": '&times;'}}]}
    button = self.context.rptObj.web.bs.composite(schema, options={"reset_class": True})
    return button
