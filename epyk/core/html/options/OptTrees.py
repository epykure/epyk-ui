
from epyk.core.html.options import Options


class OptionsTree(Options):
  component_properties = ("icon_close", )

  @property
  def is_root(self):
    """

    :return:
    """
    return self._config_get(True)

  @is_root.setter
  def is_root(self, bool):
    self._config(bool)

  @property
  def icon_open(self):
    """

    :return:
    """
    return self._config_get("fas fa-folder-open")

  @icon_open.setter
  def icon_open(self, icon):
    self._config(icon)

  @property
  def icon_close(self):
    """

    :return:
    """
    return self._config_get("fas fa-folder")

  @icon_close.setter
  def icon_close(self, icon):
    self._config(icon)

  @property
  def expanded(self):
    """

    :return:
    """
    return self._config_get(True)

  @expanded.setter
  def expanded(self, bool):
    self._config(bool)

  @property
  def style(self):
    """

    :return:
    """
    return self._config_get({})

  @style.setter
  def style(self, css):
    self._config(css)


class OptDropDown(Options):

  @property
  def width(self):
    """
    Description:
    ------------
    """
    return self._config_get(False)

  @width.setter
  def width(self, value):
    if isinstance(value, int):
      value = "%spx" % value
    #
    self._config_group_get("a", value)
    self._config_group_get("ul", value, name="left")
