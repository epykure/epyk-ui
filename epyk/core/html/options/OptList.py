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
    self._config(True, 'markdown')
    self._config(values)


class OptionsTagItems(Options):

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
