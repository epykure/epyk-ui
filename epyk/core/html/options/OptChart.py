
from epyk.core.html.options import Options


class OptionsChart(Options):
  component_properties = ("opacity", )

  @property
  def opacity(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return self._config_get(0.5)

  @opacity.setter
  def opacity(self, num):
    self._config(num)

  @property
  def type(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return self._config_get(None)

  @type.setter
  def type(self, value):
    self._config(value)

  @property
  def colors(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return self._config_get(None)

  @colors.setter
  def colors(self, colors):
    self._config(colors)

  @property
  def background_colors(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return self._config_get(None)

  @background_colors.setter
  def background_colors(self, colors):
    self._config(colors)

  @property
  def y_columns(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return self._config_get(None)

  @y_columns.setter
  def y_columns(self, cols):
    self._config(cols)

  @property
  def x_axis(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return self._config_get(None)

  @x_axis.setter
  def x_axis(self, col):
    self._config(col)

  @property
  def props(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return self._config_get({})

  @props.setter
  def props(self, values):
    self._config(values)

  @property
  def commons(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return self._config_get({})

  @commons.setter
  def commons(self, values):
    self._config(values)
