
from epyk.core.html.options import OptChart


class OptionsChartSharedPlotly(OptChart.OptionsChartShared):

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
    return self.get(True)

  @responsive.setter
  def responsive(self, val):
    self.set(val)

  @property
  def editable(self):
    """
    Description:
    ------------

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self.get(False)

  @editable.setter
  def editable(self, val):
    self.set(val)

  @property
  def staticPlot(self):
    """
    Description:
    ------------

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self.get(None)

  @staticPlot.setter
  def staticPlot(self, val):
    self.set(val)

  @property
  def scrollZoom(self):
    """
    Description:
    ------------

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self.get(None)

  @scrollZoom.setter
  def scrollZoom(self, val):
    self.set(val)

  @property
  def managed(self):
    """
    Description:
    ------------
    """
    return self.get(True)

  @managed.setter
  def managed(self, bool):
    self.set(bool)
