#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html.options import Options
from epyk.core.html.options import OptChart


class OptionsChartSharedGoogle(OptChart.OptionsChartShared):

  def x_label(self, value):
    """
    Description:
    -----------
    Set the label of the x axis.

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    self.component.options.hAxis.title = value

  def y_label(self, value):
    """
    Description:
    -----------
    Set the label of the y axis.

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    self.component.options.vAxis.title = value


class OptionAxis(Options):

  @property
  def title(self):
    return self._config_get()

  @title.setter
  def title(self, value):
    self._config(value)


class OptionGoogle(OptChart.OptionsChart):

  @property
  def vAxis(self):
    return self._config_sub_data("vAxis", OptionAxis)

  @property
  def hAxis(self):
    return self._config_sub_data("hAxis", OptionAxis)

  @property
  def seriesType(self):
    return self._config_get()

  @seriesType.setter
  def seriesType(self, value):
    self._config(value)

  @property
  def title(self):
    return self._config_get()

  @title .setter
  def title(self, value):
    self._config(value)

  @property
  def isStacked(self):
    return self._config_get()

  @isStacked.setter
  def isStacked(self, flag):
    self._config(flag)
