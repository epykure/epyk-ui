
from epyk.core.html.options import OptChart


class OptionsChartSharedPlotly(OptChart.OptionsChartShared):

  def x_format(self, jsFncs, profile=None):
    pass

  def x_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    pass

  def x_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    pass

  def x_label(self, value):
    """
    Description:
    -----------
    Set the label of the x axis.

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    pass

  def x_tick_count(self, num):
    return self

  def y_format(self, jsFncs, profile=None):
    pass

  def y_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    pass

  def y_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    pass

  def y_label(self, value):
    """
    Description:
    -----------
    Set the label of the y axis.

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    pass

  def y_tick_count(self, num):
    return self


class OptionConfig(OptChart.OptionsChart):

  @property
  def mode(self):
    """
    Description:
    ------------

    Usage::

    """
    return self._config_get(None)

  @mode.setter
  def mode(self, value):
    self._config(value)

  @property
  def responsive(self):
    """
    Description:
    ------------

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self._config_get(True)

  @responsive.setter
  def responsive(self, val):
    self._config(val)

  @property
  def displayModeBar(self):
    """
    Description:
    ------------

    Related Pages:

      https://plotly.com/javascript/configuration-options/
    """
    return self._config_get(True)

  @displayModeBar.setter
  def displayModeBar(self, flag):
    self._config(flag)

  @property
  def editable(self):
    """
    Description:
    ------------

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self._config_get(False)

  @editable.setter
  def editable(self, val):
    self._config(val)

  @property
  def staticPlot(self):
    """
    Description:
    ------------

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self._config_get(None)

  @staticPlot.setter
  def staticPlot(self, val):
    self._config(val)

  @property
  def scrollZoom(self):
    """
    Description:
    ------------

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self._config_get(None)

  @scrollZoom.setter
  def scrollZoom(self, val):
    self._config(val)

  @property
  def mapboxAccessToken(self):
    """
    Description:
    ------------

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self._config_get(None)

  @mapboxAccessToken.setter
  def mapboxAccessToken(self, val):
    self._config(val)
