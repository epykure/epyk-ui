
from epyk.core.html.options import Options


class OptionsTree(Options):
  component_properties = ("icon_close", "with_badge")

  @property
  def is_root(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :prop flag:
    """
    return self._config_get(True)

  @is_root.setter
  def is_root(self, flag):
    self._config(flag)

  @property
  def icon_open(self):
    """
    Description:
    ------------
    Set the icon when the node is open.

    Attributes:
    ----------
    :prop icon: String. The icon reference from font-awesome.
    """
    return self._config_get("fas fa-folder-open")

  @icon_open.setter
  def icon_open(self, icon):
    self._config(icon)

  @property
  def icon_close(self):
    """
    Description:
    ------------
    Set the icon when the node is closed.

    Attributes:
    ----------
    :prop icon: String. The icon reference from font-awesome.
    """
    return self._config_get("fas fa-folder")

  @icon_close.setter
  def icon_close(self, icon):
    self._config(icon)

  @property
  def expanded(self):
    """
    Description:
    ------------
    Flag to set the initial state of the tree.

    Attributes:
    ----------
    :prop flag: Boolean. A flag to specify the state of the tree.
    """
    return self._config_get(True)

  @expanded.setter
  def expanded(self, flag):
    self._config(flag)

  @property
  def style(self):
    """
    Description:
    ------------
    Set the CSS attributes to each node and leaf in the tree.

    Attributes:
    ----------
    :prop css: Dictionary. The CSS Style to be used.
    """
    return self._config_get({})

  @style.setter
  def style(self, css):
    self._config(css)

  @property
  def with_badge(self):
    """
    Description:
    ------------
    Display a badge with the count of leaves in the tree for a given node.

    Attributes:
    ----------
    :prop flag: Boolean. A flag to specify if the badge with the count of leaves is visible.
    """
    return self._config_get(False)

  @with_badge.setter
  def with_badge(self, flag):
    self._config(flag)


class OptDropDown(Options):

  @property
  def width(self):
    """
    Description:
    ------------
    Set the width of the dropdown item.

    Attributes:
    ----------
    :prop number: Integer. The width of the item in pixel.
    """
    return self._config_get(False)

  @width.setter
  def width(self, value):
    if isinstance(value, int):
      value = "%spx" % value
    #
    self._config_group_get("a", value)
    self._config_group_get("ul", value, name="left")
