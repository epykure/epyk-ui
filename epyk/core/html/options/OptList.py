#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections

from epyk.core.html.options import Options
from epyk.core.js.packages import packageImport
from epyk.core.js import JsUtils


class OptionsLi(Options):
  component_properties = ("item_type",)

  @property
  def item_type(self):
    """ """
    return self._config_get("li")

  @item_type.setter
  def item_type(self, value):
    self._config(value)

  @property
  def delete(self):
    """ """
    return self.get(True)

  @delete.setter
  def delete(self, value):
    self.set(value)

  @property
  def max(self):
    """ """
    return self.get(None)

  @max.setter
  def max(self, value):
    self.set(value)

  @property
  def source(self):
    """ """
    return self.get(None)

  @source.setter
  def source(self, value):
    self.set(value)

  @property
  def li_css(self):
    """
    """
    return self._config_get({})

  @li_css.setter
  def li_css(self, css):
    self._config(css)

  @property
  def li_class(self):
    """
    """
    return self._config_get([])

  @li_class.setter
  def li_class(self, cls_names):
    self._config(cls_names)


class OptionsItems(Options):
  component_properties = ("delete_icon", 'delete_position', 'info_icon', 'li_style', 'click', 'draggable', 'prefix',
                          'max_selected', 'text_click', "delimiter")

  @property
  def delimiter(self):
    """Value used to aggregate and split string values"""
    return self._config_get(",")

  @delimiter.setter
  def delimiter(self, value: str):
    self._config(value)

  @property
  def inline(self):
    """inline property for the items"""
    return self.li_style.get("display") == "inline-block"

  @inline.setter
  def inline(self, flag: bool):
    if flag:
      self.li_style["display"] = "inline-block"
      self.li_style["margin-left"] = "2px"
      self.li_style["margin-right"] = "2px"
    else:
      self.li_style["display"] = "block"

  @property
  def style(self):
    """Item CSS Style"""
    return self._config_get({})

  @style.setter
  def style(self, attrs):
    self._config(attrs)

  @property
  def li_style(self):
    """List Item CSS Style"""
    return self._config_get({})

  @li_style.setter
  def li_style(self, attrs):
    self._config(attrs)

  @property
  def li_height(self):
    """List Item line height CSS Style"""
    return self.li_style.get("line-height")

  @li_height.setter
  def li_height(self, value):
    styles = dict(self.li_style)
    styles["line-height"] = "%spx" % value
    self.li_style = styles

  @property
  def badge(self):
    """Get the badge style"""
    return self._config_get({})

  @badge.setter
  def badge(self, attrs):
    self._config(attrs)

  @property
  def delete(self):
    """Add a delete icon"""
    return self._config_get(False)

  @delete.setter
  def delete(self, attrs):
    self._config(attrs)

  @property
  def checked(self):
    """Check default value for radio and check lists"""
    return self._config_get(False)

  @checked.setter
  def checked(self, attrs):
    self._config(attrs)

  @property
  def checked_key(self):
    """The key in the data with the boolean to check / uncheck an item.

    Usages::
      its = page.ui.lists.items(["menu %s" % i for i in range(10)])
      its.options.checked_key = "selected"
    """
    return self._config_get("checked")

  @checked_key.setter
  def checked_key(self, value: str):
    self._config(value)

  @property
  def icon(self):
    """Check default value for radio and check lists"""
    return self._config_get("")

  @icon.setter
  def icon(self, attrs):
    self._config(attrs)

  @property
  def text_click(self):
    """Expand the click event to the label for check and radio components.
    This is a way to define if the click event should be done on the full component or not.
    """
    return self._config_get(False)

  @text_click.setter
  def text_click(self, flag: bool):
    self._config(flag)

  @property
  def items_type(self):
    """Change the type of items in the dynamic list"""
    return self._config_get("text")

  @items_type.setter
  def items_type(self, text):
    self._config(text)
    self._config(text not in (
      'link', 'badge', 'text', 'icon', 'timeline', 'check', 'radio', 'logs', 'status'), name="items_space")

  @property
  def items_space(self):
    """Keep the LI margin between the items"""
    return self._config_get(True)

  @items_space.setter
  def items_space(self, flag):
    self._config(flag)

  @property
  def info_icon(self):
    """Set the delete icon"""
    return self._config_get("fas fa-info-circle fa-xs")

  @info_icon.setter
  def info_icon(self, attrs):
    self._config(attrs)

  @property
  def delete_icon(self):
    """Set the delete icon"""
    return self._config_get("fas fa-trash-alt")

  @delete_icon.setter
  def delete_icon(self, attrs):
    self._config(attrs)

  @property
  def delete_position(self):
    """Set the position and CSS attributes of the delete icon"""
    return self._config_get({"float": 'right', 'marginRight': '10px', 'marginTop': '5px'})

  @delete_position.setter
  def delete_position(self, attrs):
    if attrs == "right":
      attrs = {"float": 'right', 'marginRight': '10px', 'marginTop': '5px'}
    self._config(attrs)

  @property
  def markdown(self):
    """Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).
    `showdown <https://github.com/showdownjs/showdown>`_
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
  def max_selected(self):
    """Set a max selected item for a normal list.

    Usages::
      its = page.ui.lists.items(["menu %s" % i for i in range(10)])
      its.options.max_selected = 2
      its.select_type()
      its.click([])
    """
    return self._config_get(None)

  @max_selected.setter
  def max_selected(self, value: int):
    self._config(value)

  @property
  def showdown(self):
    """Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).
    `showdown <https://github.com/showdownjs/showdown>`_
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
    """Internal CSS class name to be used when the component is selected"""
    return self._config_get(None)

  @style_select.setter
  def style_select(self, value):
    self._config(value)

  @property
  def click(self):
    """Option property to defined click event on list items. By default this is None"""
    return self._config_get('null')

  @click.setter
  def click(self, value):
    self._config(value, js_type=True)

  @property
  def draggable(self):
    """Property to defined JavaScript draggable events to the list items. By default items are not draggable"""
    return self._config_get('false')

  @draggable.setter
  def draggable(self, value):
    self._config(value, js_type=True)

  @property
  def prefix(self):
    """ """
    return self._config_get("")

  @prefix.setter
  def prefix(self, value):
    self._config(value)

  @property
  def label(self):
    """A text label use in the design of some components"""
    return self._config_get("")

  @label.setter
  def label(self, value: str):
    self._config(value)

  @property
  def group(self):
    """Set the group name for radio boxes"""
    return self._config_get(None)

  @group.setter
  def group(self, value):
    self._config(value)


class OptionsTagItems(Options):
  component_properties = ('delete', 'max_height', "clear", "show_all", "reduce")

  @property
  def clear(self):
    """

    :prop css:
    """
    return self._config_get(True)

  @clear.setter
  def clear(self, flag: bool):
    if flag and not self.component.clear:
      self.component.clear = self.page.ui.text("&#215;clear", html_code=self.component.sub_html_code("clear"))
      self.component.clear.classList.add(self.component.style_refs["html-filters-clear"])
      self.component.clear.options.managed = False
      self.component.clear.click([self.component.dom.clear()])
    elif not flag:
      #TODO review _browser_data for removed components
      self.component.clear._browser_data['mouse'] = collections.OrderedDict()
      self.component.clear = None
    self._config(flag)

  @property
  def visible(self):
    """

    :prop css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get(False)

  @visible.setter
  def visible(self, attrs: dict):
    self._config(attrs)

  @property
  def delete(self):
    """Display the deleted icon on the different items

    :prop attrs: Dictionary or False. The deleted icon properties
    """
    return self._config_get('this.parentNode.remove()')

  @delete.setter
  def delete(self, attrs: dict):
    self._config(attrs)

  @property
  def category_css(self):
    """

    :prop css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @category_css.setter
  def category_css(self, attrs: dict):
    self._config(attrs)

  @property
  def value_css(self):
    """

    :prop css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @value_css.setter
  def value_css(self, attrs: dict):
    self._config(attrs)

  @property
  def item_css(self):
    """

    :prop css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @item_css.setter
  def item_css(self, attrs: dict):
    self._config(attrs)

  @property
  def category(self):
    """

    :prop css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @category.setter
  def category(self, attrs: dict):
    self._config(attrs)

  @property
  def icon_css(self):
    """

    :prop css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @icon_css.setter
  def icon_css(self, attrs: dict):
    self._config(attrs)

  @property
  def max_height(self):
    """Max height property for the filter tags container.
    This will then display a show all and reduce button if the size if above this value.

    :prop int css: All the CSS attributes to add the any items
    """
    return self._config_get(0)

  @max_height.setter
  def max_height(self, num: int):
    if num:
      self.component.classList.add(self.component.style_refs["html-filters"])
    self._config(num)

  @property
  def draggable(self):
    """Set the component draggable and define JavaScript events.

    :prop js_funcs: String. The JavaScript functions.
    """
    return self._config_get()

  @draggable.setter
  def draggable(self, js_funcs):
    self._config(js_funcs, js_type=True)

  @property
  def reduce(self):
    """Set the component draggable and define JavaScript events.

    :prop js_funcs: String. The JavaScript functions.
    """
    return self._config_get("reduce")

  @reduce.setter
  def reduce(self, value):
    self._config(value)

  @property
  def show_all(self):
    """Set the component draggable and define JavaScript events.

    :prop js_funcs: String. The JavaScript functions.
    """
    return self._config_get("show all")

  @show_all.setter
  def show_all(self, value):
    self._config(value)


class OptionsListBrackets(Options):

  def save(self, js_funcs, profile=None):
    """

    :param js_funcs:
    :param profile:
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config("function(){ %s }" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True, name="save")

  def onMatchClick(self, js_funcs, profile=None):
    """

    :param js_funcs:
    :param profile:
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config("function(data){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True, name="onMatchClick")

  def onMatchHover(self, js_funcs, profile=None):
    """

    :param js_funcs:
    :param profile:
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config("function(data, hover){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True, name="onMatchHover")

  @property
  def centerConnectors(self):
    """route connectors between matches instead of seats.

    Related Pages:

      http://www.aropupu.fi/bracket/

    :prop flag: Boolean.
    """
    return self._config_get(False)

  @centerConnectors.setter
  def centerConnectors(self, flag: bool):
    self._config(flag)

  @property
  def disableHighlight(self):
    """
    `bracket <http://www.aropupu.fi/bracket/>`_

    :prop flag: Boolean.
    """
    return self._config_get(False)

  @disableHighlight.setter
  def disableHighlight(self, flag: bool):
    self._config(flag)

  @property
  def skipSecondaryFinal(self):
    """

    `bracket <http://www.aropupu.fi/bracket/>`_

    :prop flag: Boolean.
    """
    return self._config_get(False)

  @skipSecondaryFinal.setter
  def skipSecondaryFinal(self, flag: bool):
    self._config(flag)

  @property
  def skipConsolationRound(self):
    """

    `bracket <http://www.aropupu.fi/bracket/>`_

    :prop flag: Boolean.
    """
    return self._config_get(False)

  @skipConsolationRound.setter
  def skipConsolationRound(self, flag: bool):
    self._config(flag)

  @property
  def skipGrandFinalComeback(self):
    """

    `bracket <http://www.aropupu.fi/bracket/>`_

    :prop flag: Boolean.
    """
    return self._config_get(False)

  @skipGrandFinalComeback.setter
  def skipGrandFinalComeback(self, flag: bool):
    self._config(flag)

  @property
  def dir(self):
    """

    `bracket <http://www.aropupu.fi/bracket/>`_

    :prop value: String.
    """
    return self._config_get("rl")

  @dir.setter
  def dir(self, value: str):
    self._config(value)

  @property
  def userData(self):
    """

    `bracket <http://www.aropupu.fi/bracket/>`_

    :prop value: String.
    """
    return self._config_get("")

  @userData.setter
  def userData(self, value: str):
    self._config(value)

  @property
  def teamWidth(self):
    """

    `bracket <http://www.aropupu.fi/bracket/>`_

    :prop num: String.
    """
    return self._config_get("")

  @teamWidth.setter
  def teamWidth(self, num):
    self._config(num)

  @property
  def scoreWidth(self):
    """

    `bracket <http://www.aropupu.fi/bracket/>`_

    :prop num: String.
    """
    return self._config_get("")

  @scoreWidth.setter
  def scoreWidth(self, num: int):
    self._config(num)

  @property
  def matchMargin(self):
    """

    `bracket <http://www.aropupu.fi/bracket/>`_

    :prop num: String.
    """
    return self._config_get("")

  @matchMargin.setter
  def matchMargin(self, num: str):
    self._config(num)

  @property
  def roundMargin(self):
    """

    `bracket <http://www.aropupu.fi/bracket/>`_

    :prop num: String.
    """
    return self._config_get("")

  @roundMargin.setter
  def roundMargin(self, num):
    self._config(num)
