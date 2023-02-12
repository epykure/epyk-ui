
from epyk.core.html.options import Options
from epyk.core.js import JsUtils
from epyk.core.py import types as etypes


class OptionsTree(Options):
  component_properties = ("icon_close", "with_badge", "is_root", "click_node", "icon_style")

  @property
  def is_root(self):
    """
 
    :prop flag:
    """
    return self._config_get(True)

  @is_root.setter
  def is_root(self, flag: bool):
    self._config(flag)

  @property
  def icon_open(self):
    """ Set the icon when the node is open.
 
    :prop icon: The icon reference from font-awesome
    """
    return self._config_get("fas fa-folder-open")

  @icon_open.setter
  def icon_open(self, icon: str):
    self._config(icon)

  @property
  def icon_close(self):
    """ Set the icon when the node is closed.
 
    :prop icon: The icon reference from font-awesome
    """
    return self._config_get("fas fa-folder")

  @icon_close.setter
  def icon_close(self, icon: str):
    self._config(icon)

  @property
  def icon_style(self):
    """ Set the CSS attributes to each node and leaf in the tree.
 
    :prop css: The CSS Style to be used
    """
    return self._config_get({"margin-right": "5px"})

  @icon_style.setter
  def icon_style(self, css: dict):
    i_style = dict(self.icon_style)
    i_style.update(css)
    self._config(i_style)

  @property
  def expanded(self):
    """ Flag to set the initial state of the tree.
 
    :prop flag: A flag to specify the state of the tree
    """
    return self._config_get(True)

  @expanded.setter
  def expanded(self, flag: bool):
    self._config(flag)

  @property
  def style(self):
    """ Set the CSS attributes to each node and leaf in the tree.
 
    :prop css: The CSS Style to be used
    """
    return self._config_get({})

  @style.setter
  def style(self, css: dict):
    self._config(css)

  @property
  def with_badge(self):
    """ Display a badge with the count of leaves in the tree for a given node.
 
    :prop flag: A flag to specify if the badge with the count of leaves is visible
    """
    return self._config_get(False)

  @with_badge.setter
  def with_badge(self, flag: bool):
    self._config(flag)

  @property
  def with_icon(self):
    """
 
    :prop key: The key in the data used to display an icon
    """
    return self._config_get(None)

  @with_icon.setter
  def with_icon(self, key: bool):
    self._config(key)

  @property
  def filter_on(self):
    """
 
    :prop key: The sub string to filter the tree result
    """
    return self._config_get(None)

  @filter_on.setter
  def filter_on(self, text: str):
    self._config(text)

  def click_node(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
    """ Add event on the node label.
 
    :param js_funcs: A Javascript Python function
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config(
      "function(event, value, data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile),
      js_type=True, name="clickNode")

  def click_leaf(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
    """ Add a specific event on the leaf nodes in the hierarchy view.
 
    :param js_funcs: A Javascript Python function
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config(
      "function(event, value, data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile),
      js_type=True, name="clickLeaf")


class OptDropDown(Options):

  @property
  def width(self):
    """ Set the width of the dropdown item.
 
    :prop number: The width of the item in pixel
    """
    return self._config_get(False)

  @width.setter
  def width(self, value: int):
    if isinstance(value, int):
      value = "%spx" % value
    #
    self._config_group_get("a", value)
    self._config_group_get("ul", value, name="left")

  @property
  def a(self):
    """

    """
    return self._config_get({})

  @a.setter
  def a(self, css: dict):
    self._config(css)

  @property
  def ul(self):
    """

    """
    return self._config_get({})

  @ul.setter
  def ul(self, css: dict):
    self._config(css)

  def onClick(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
    """
 
    :param js_funcs: A Javascript Python function
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config(
      "function(event, value){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile),
      js_type=True, name="click")
