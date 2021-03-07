#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options
from epyk.core.js.packages import packageImport
from epyk.core.js import JsUtils


class OptionsLi(Options):

  @property
  def max(self):
    """
    """
    return self.get(None)

  @max.setter
  def max(self, value):
    self.set(value)

  @property
  def source(self):
    """
    """
    return self.get(None)

  @source.setter
  def source(self, value):
    self.set(value)

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
  component_properties = ("delete_icon", 'delete_position', 'info_icon', 'li_style', 'click', 'draggable', 'prefix', )

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
  def li_style(self):
    """
    Description:
    ------------
    List Item CSS Style
    """
    return self._config_get({})

  @li_style.setter
  def li_style(self, attrs):
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
    Change the type of items in the dynamic list.
    """
    return self._config_get("text")

  @items_type.setter
  def items_type(self, text):
    self._config(text)
    self._config(text not in ('link', 'badge', 'text', 'icon', 'check'), name="items_space")

  @property
  def items_space(self):
    """
    Description:
    ------------
    Keep the LI margin between the items.
    """
    return self._config_get(True)

  @items_space.setter
  def items_space(self, flag):
    self._config(flag)

  @property
  def info_icon(self):
    """
    Description:
    ------------
    Set the delete icon
    """
    return self._config_get("fas fa-info-circle")

  @info_icon.setter
  def info_icon(self, attrs):
    self._config(attrs)

  @property
  def delete_icon(self):
    """
    Description:
    ------------
    Set the delete icon
    """
    return self._config_get("fas fa-trash-alt")

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

  @property
  def style_select(self):
    """
    Description:
    ------------
    Internal CSS class name to be used when the component is selected.
    """
    return self._config_get(None)

  @style_select.setter
  def style_select(self, value):
    self._config(value)

  @property
  def click(self):
    """
    Description:
    ------------
    Option property to defined click event on list items.
    By default this is None.
    """
    return self._config_get('null')

  @click.setter
  def click(self, value):
    self._config(value, js_type=True)

  @property
  def draggable(self):
    """
    Description:
    ------------
    Property to defined JavaScript draggable events to the list items.
    By default items are not draggable.
    """
    return self._config_get('false')

  @draggable.setter
  def draggable(self, value):
    self._config(value, js_type=True)

  @property
  def prefix(self):
    """
    Description:
    ------------

    """
    return self._config_get("")

  @prefix.setter
  def prefix(self, value):
    self._config(value)


class OptionsTagItems(Options):
  component_properties = ('delete', 'max_height')

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
    return self._config_get('this.parentNode.remove()')

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

  @property
  def max_height(self):
    """
    Description:
    ------------
    Max height property for the filter tags container.
    This will then display a show all and reduce button if the size if above this value.

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get(0)

  @max_height.setter
  def max_height(self, num):
    self._config(num)


class OptionsListBrackets(Options):

  def save(self, js_funcs, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param js_funcs:
    :param profile:
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config("function(){ %s }" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True, name="save")

  def onMatchClick(self, js_funcs, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param js_funcs:
    :param profile:
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config("function(data){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True, name="onMatchClick")

  def onMatchHover(self, js_funcs, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param js_funcs:
    :param profile:
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config("function(data, hover){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True, name="onMatchHover")

  @property
  def centerConnectors(self):
    """
    Description:
    ------------
    route connectors between matches instead of seats.

    Related Pages:

      http://www.aropupu.fi/bracket/

    Attributes:
    ----------
    :param flag: Boolean.
    """
    return self._config_get(False)

  @centerConnectors.setter
  def centerConnectors(self, flag):
    self._config(flag)

  @property
  def disableHighlight(self):
    """
    Description:
    ------------

    Related Pages:

      http://www.aropupu.fi/bracket/

    Attributes:
    ----------
    :param flag: Boolean.
    """
    return self._config_get(False)

  @disableHighlight.setter
  def disableHighlight(self, flag):
    self._config(flag)

  @property
  def skipSecondaryFinal(self):
    """
    Description:
    ------------

    Related Pages:

      http://www.aropupu.fi/bracket/

    Attributes:
    ----------
    :param flag: Boolean.
    """
    return self._config_get(False)

  @skipSecondaryFinal.setter
  def skipSecondaryFinal(self, flag):
    self._config(flag)

  @property
  def skipConsolationRound(self):
    """
    Description:
    ------------

    Related Pages:

      http://www.aropupu.fi/bracket/

    Attributes:
    ----------
    :param flag: Boolean.
    """
    return self._config_get(False)

  @skipConsolationRound.setter
  def skipConsolationRound(self, flag):
    self._config(flag)

  @property
  def skipGrandFinalComeback(self):
    """
    Description:
    ------------

    Related Pages:

      http://www.aropupu.fi/bracket/

    Attributes:
    ----------
    :param flag: Boolean.
    """
    return self._config_get(False)

  @skipGrandFinalComeback.setter
  def skipGrandFinalComeback(self, flag):
    self._config(flag)

  @property
  def dir(self):
    """
    Description:
    ------------

    Related Pages:

      http://www.aropupu.fi/bracket/

    Attributes:
    ----------
    :param value: String.
    """
    return self._config_get("rl")

  @dir.setter
  def dir(self, value):
    self._config(value)

  @property
  def userData(self):
    """
    Description:
    ------------

    Related Pages:

      http://www.aropupu.fi/bracket/

    Attributes:
    ----------
    :param value: String.
    """
    return self._config_get("")

  @userData.setter
  def userData(self, value):
    self._config(value)

  @property
  def teamWidth(self):
    """
    Description:
    ------------

    Related Pages:

      http://www.aropupu.fi/bracket/

    Attributes:
    ----------
    :prop num: String.
    """
    return self._config_get("")

  @teamWidth.setter
  def teamWidth(self, num):
    self._config(num)

  @property
  def scoreWidth(self):
    """
    Description:
    ------------

    Related Pages:

      http://www.aropupu.fi/bracket/

    Attributes:
    ----------
    :prop num: String.
    """
    return self._config_get("")

  @scoreWidth.setter
  def scoreWidth(self, num):
    self._config(num)

  @property
  def matchMargin(self):
    """
    Description:
    ------------

    Related Pages:

      http://www.aropupu.fi/bracket/

    Attributes:
    ----------
    :prop num: String.
    """
    return self._config_get("")

  @matchMargin.setter
  def matchMargin(self, num):
    self._config(num)

  @property
  def roundMargin(self):
    """
    Description:
    ------------

    Related Pages:

      http://www.aropupu.fi/bracket/

    Attributes:
    ----------
    :prop num: String.
    """
    return self._config_get("")

  @roundMargin.setter
  def roundMargin(self, num):
    self._config(num)
