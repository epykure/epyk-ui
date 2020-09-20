#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options
from epyk.core.js.packages import packageImport


class OptionsLi(Options):

  @property
  def li_css(self):
    """
    """
    return self.get({})

  @li_css.setter
  def li_css(self, css):
    self.set(css)

  @property
  def li_class(self):
    """
    """
    return self.get([])

  @li_class.setter
  def li_class(self, cls_names):
    self.set(cls_names)


class OptionsItems(Options):
  component_properies = ("delete_icon", 'delete_position')

  @property
  def style(self):
    """
    Description:
    ------------
    Item CSS Style
    """
    return self._config_get({})

  @style.setter
  def style(self, attrs):
    self._config(attrs)

  @property
  def badge(self):
    """
    Description:
    ------------
    Get the badge style
    """
    return self._config_get({})

  @badge.setter
  def badge(self, attrs):
    self._config(attrs)

  @property
  def delete(self):
    """
    Description:
    ------------
    Add a delete icon
    """
    return self._config_get(False)

  @delete.setter
  def delete(self, attrs):
    self._config(attrs)

  @property
  def checked(self):
    """
    Description:
    ------------
    Check default value for radio and check lists
    """
    return self._config_get(False)

  @checked.setter
  def checked(self, attrs):
    self._config(attrs)

  @property
  def icon(self):
    """
    Description:
    ------------
    Check default value for radio and check lists
    """
    return self._config_get("")

  @icon.setter
  def icon(self, attrs):
    self._config(attrs)

  @property
  def items_type(self):
    """
    Description:
    ------------
    Change the type of items in the dynamic list
    """
    return self._config_get("text")

  @items_type.setter
  def items_type(self, text):
    self._config(text)

  @property
  def delete_icon(self):
    """
    Description:
    ------------
    Set the delete icon
    """
    return self._config_get("fa-trash-alt")

  @delete_icon.setter
  def delete_icon(self, attrs):
    self._config(attrs)

  @property
  def delete_position(self):
    """
    Description:
    ------------
    Set the position and CSS attributes of the delete icon
    """
    return self._config_get({"float": 'right', 'marginRight': '10px', 'marginTop': '5px'})

  @delete_position.setter
  def delete_position(self, attrs):
    if attrs == "right":
      attrs = {"float": 'right', 'marginRight': '10px', 'marginTop': '5px'}
    self._config(attrs)

  @property
  def markdown(self):
    """
    Description:
    ------------
    Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return self._config_get(False)

  @markdown.setter
  @packageImport("showdown")
  def markdown(self, values):
    if values is True:
      values = {}
    if isinstance(values, bool):
      self._config(values)
      self._config({} if values is True else values, 'showdown')
    else:
      self._config(True)
      self._config(values, 'showdown')

  @property
  def showdown(self):
    """
    Description:
    ------------
    Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return self._config_get(False)

  @showdown.setter
  @packageImport("showdown")
  def showdown(self, values):
    if values is True:
      values = {}
    self._config(True, 'markdown')
    self._config(values)


class OptionsTagItems(Options):
  component_properies = ('delete', )

  @property
  def visible(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get(False)

  @visible.setter
  def visible(self, attrs):
    self._config(attrs)

  @property
  def delete(self):
    """
    Description:
    ------------
    Display the deleted icon on the different items

    Attributes:
    ----------
    :param attrs: Dictionary or False. The deleted icon properties
    """
    return self._config_get('function(){this.parentNode.remove()}')

  @delete.setter
  def delete(self, attrs):
    self._config(attrs)

  @property
  def category_css(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @category_css.setter
  def category_css(self, attrs):
    self._config(attrs)

  @property
  def value_css(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @value_css.setter
  def value_css(self, attrs):
    self._config(attrs)

  @property
  def item_css(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @item_css.setter
  def item_css(self, attrs):
    self._config(attrs)

  @property
  def category(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @category.setter
  def category(self, attrs):
    self._config(attrs)

  @property
  def icon_css(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @icon_css.setter
  def icon_css(self, attrs):
    self._config(attrs)
