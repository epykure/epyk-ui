
from epyk.core.html.options import OptChart


class OptionsChartSharedNVD3(OptChart.OptionsChartShared):

  def x_format(self, js_funcs, profile=None):
    self.component.dom.xAxis.tickFormat(js_funcs, profile)
    return self

  def x_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    self.component.dom.xAxis.tickSymbol(symbol, digit, thousand_sep, decimal_sep, fmt, factor, alias)
    return self

  def x_format_number(self, factor=1, alias=None, digits=0, thousand_sep="."):
    self.component.dom.xAxis.tickNumber(digits, thousand_sep, factor, alias)
    return self

  def x_label(self, value):
    """   Set the label of the x axis.

    Related Pages:

      https://c3js.org/reference.html#axis-y-label
 
    :param value: String. The axis label.
    """
    self.component.dom.xAxis.axisLabel(value)

  def x_tick_count(self, num):
    return self

  def y_format(self, js_funcs, profile=None):
    self.component.dom.yAxis.tickFormat(js_funcs, profile)
    return self

  def y_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    self.component.dom.yAxis.tickSymbol(symbol, digit, thousand_sep, decimal_sep, fmt, factor, alias)
    return self

  def y_format_number(self, factor=1, alias=None, digits=0, thousand_sep="."):
    self.component.dom.yAxis.tickNumber(digits, thousand_sep, factor, alias)
    return self

  def y_label(self, value):
    """   Set the label of the y axis.
 
    :param value: String. The axis label.
    """
    self.component.dom.yAxis.axisLabel(value)

  def y_tick_count(self, num):
    return self
