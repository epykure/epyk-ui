
from epyk.core.html.options import Options
import abc


class OptionsChart(Options):
  component_properties = ("opacity", )

  @property
  def height(self):
    return self._config_get(None)

  @height.setter
  def height(self, num):
    self._config(num)

  @property
  def opacity(self):
    """
    Description:
    ------------

    Usage::

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

    Usage::

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

    Usage::

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

    Usage::

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

    Usage::

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

    Usage::

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

    Usage::

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

    Usage::

    """
    return self._config_get({})

  @commons.setter
  def commons(self, values):
    self._config(values)


class OptionsChartShared(abc.ABC):

  def __init__(self, component):
    self.component = component

  @abc.abstractmethod
  def x_label(self, value):
    """
    Description:
    -----------
    Set the label of the x axis.

    Attributes:
    ----------
    :param value: String. The axis label.
    """

  @abc.abstractmethod
  def y_label(self, value):
    """
    Description:
    -----------
    Set the label of the y axis.

    Attributes:
    ----------
    :param value: String. The axis label.
    """


class OptionsChartSharedNVD3(OptionsChartShared):

  def x_label(self, value):
    """
    Description:
    -----------
    Set the label of the x axis.

    Related Pages:

      https://c3js.org/reference.html#axis-y-label

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    self.component.dom.xAxis.axisLabel(value)

  def y_label(self, value):
    """
    Description:
    -----------
    Set the label of the y axis.

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    self.component.dom.yAxis.axisLabel(value)
