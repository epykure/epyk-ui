
from epyk.core.html.options import Options
from epyk.core.js import JsUtils
import abc


class OptionsChart(Options):
  component_properties = ("opacity", "get_width", "get_height")

  @property
  def get_width(self):
    """
    Description:
    -----------
    Get the container available with in pixel (including the padding).
    """
    return self._config_get(JsUtils.jsWrap(
      "function(component){return component.clientWidth - (parseFloat(component.style.paddingLeft) + parseFloat(component.style.paddingRight)) }"))

  @get_width.setter
  def get_width(self, num):
    self._config(num)

  @property
  def get_height(self):
    """
    Description:
    -----------
    Get the container available height in pixel (including the padding).
    """
    return self._config_get(JsUtils.jsWrap(
      "function(component){return component.clientHeight - (parseFloat(component.style.paddingTop) + parseFloat(component.style.paddingBottom))}"))

  @get_height.setter
  def get_height(self, num):
    self._config(num)

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
  def x_format(self, jsFncs, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """

  @abc.abstractmethod
  def x_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param symbol:
    :param digit:
    :param thousand_sep:
    :param decimal_sep:
    :param fmt:
    :param factor:
    :param alias:
    """

  @abc.abstractmethod
  def x_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param factor:
    :param alias:
    :param digits:
    :param thousand_sep:
    """

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
  def x_tick_count(self, num):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param num:
    """

  @abc.abstractmethod
  def y_format(self, jsFncs, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """

  @abc.abstractmethod
  def y_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param symbol:
    :param digit:
    :param thousand_sep:
    :param decimal_sep:
    :param fmt:
    :param factor:
    :param alias:
    """

  @abc.abstractmethod
  def y_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param factor:
    :param alias:
    :param digits:
    :param thousand_sep:
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

  @abc.abstractmethod
  def y_tick_count(self, num):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param num:
    """

