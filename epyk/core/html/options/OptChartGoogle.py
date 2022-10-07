#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html.options import Options
from epyk.core.html.options import OptChart


class OptionsChartSharedGoogle(OptChart.OptionsChartShared):

  def x_format(self, js_funcs, profile=None):
    pass

  def x_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    pass

  def x_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    pass

  def x_label(self, value):
    """   Set the label of the x axis.

    :param value: String. The axis label.
    """
    self.component.options.hAxis.title = value
    return self

  def x_tick_count(self, num):
    return self

  def y_format(self, js_funcs, profile=None):
    pass

  def y_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    pass

  def y_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    pass

  def y_label(self, value):
    """   Set the label of the y axis.

    :param value: String. The axis label.
    """
    self.component.options.vAxis.title = value
    return self

  def y_tick_count(self, num):
    return self


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
    """

    :rtype: OptionAxis
    """
    return self._config_sub_data("vAxis", OptionAxis)

  @property
  def hAxis(self):
    """

    :rtype: OptionAxis
    """
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
