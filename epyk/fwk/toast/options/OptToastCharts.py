
from epyk.core.html.options import Options
from epyk.core.html.options import Enums
from epyk.core.html.options import OptChart


class OptToastChartsShared(OptChart.OptionsChartShared):

  def x_format(self, js_funcs, profile=None):
    return self

  def x_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    return self

  def x_format_number(self, factor=1, alias=None, digits=0, thousand_sep="."):
    return self

  def x_tick_count(self, num):
    self.component.config.xAxis.tick.interval = num
    return self

  def x_label(self, value):
    self.component.config.xAxis.title.text = value
    return self

  def y_format(self, js_funcs, profile=None):
    return self

  def y_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    return self

  def y_format_number(self, factor=1, alias=None, digits=0, thousand_sep="."):
    return self

  def y_tick_count(self, num):
    """
    Description:
    -----------
    Set the interval between the ticks.

    Attributes:
    ----------
    :param num:
    """
    self.component.config.yAxis.tick.interval = num
    return self

  def y_label(self, value):
    self.component.config.yAxis.title.text = value
    return self


class EnumStackTypes(Enums):

  def normal(self):
    """
    Description:
    ------------
    Set the stack type.

    Related Pages:

      https://github.com/nhn/tui.chart/blob/main/docs/en/chart-area.md
    """
    self._set_value()

  def percent(self):
    """
    Description:
    ------------
    Set the stack type.

    Related Pages:

      https://github.com/nhn/tui.chart/blob/main/docs/en/chart-area.md
    """
    self._set_value()


class EnumEventDetectTypes(Enums):

  def grouped(self):
    """
    Description:
    ------------
    Set the stack type.

    Related Pages:

      https://github.com/nhn/tui.chart/blob/main/docs/en/chart-area.md
    """
    self._set_value()


class OptionsChartDataSeries(Options):
  @property
  def name(self):
    """
    Description:
    ------------

    Related Pages:


    """
    return self._config_get()

  @name.setter
  def name(self, text):
    self._config(text)

  @property
  def data(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @data.setter
  def data(self, values):
    self._config(values)

  @property
  def visible(self):
    """
    Description:
    ------------

    Related Pages:


    """
    return self._config_get()

  @visible.setter
  def visible(self, flag):
    self._config(flag)

  @property
  def stackGroup(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-17-bar-groupStack-chart-basic
    """
    return self._config_get()

  @stackGroup.setter
  def stackGroup(self, text):
    self._config(text)


class OptionsChartData(Options):

  @property
  def categories(self):
    """
    Description:
    ------------

    Related Pages:


    """
    return self._config_get()

  @categories.setter
  def categories(self, values):
    self._config(values)

  def add_series(self, name, data) -> OptionsChartDataSeries:
    """
    Description:
    -----------

    Related Pages:



    :rtype: OptionsChartDataSeries
    """
    new_series = self._config_sub_data_enum("series", OptionsChartDataSeries)
    new_series.name = name
    new_series.data = data
    return new_series


class OptionsChartAttrs(Options):

  @property
  def title(self):
    """
    Description:
    ------------

    Related Pages:


    """
    return self._config_get()

  @title.setter
  def title(self, values):
    self._config(values)

  @property
  def width(self):
    """
    Description:
    ------------

    Related Pages:


    """
    return self._config_get()

  @width.setter
  def width(self, num):
    self._config(num)

  @property
  def height(self):
    """
    Description:
    ------------

    Related Pages:


    """
    return self._config_get()

  @height.setter
  def height(self, num):
    self._config(num)


class OptionsTitle(Options):
  @property
  def text(self):
    """
    Description:
    ------------

    Related Pages:


    """
    return self._config_get()

  @text.setter
  def text(self, value):
    self._config(value)


class OptionsAxisLabel(Options):

  @property
  def interval(self):
    """
    Description:
    ------------
    Set the tick interval on the axis.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/ColumnChart
    """
    return self._config_get()

  @interval.setter
  def interval(self, num):
    self._config(num)


class OptionsScale(Options):

  @property
  def min(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-15-bar-stack-chart-dataLabels
    """
    return self._config_get()

  @min.setter
  def min(self, num):
    self._config(num)

  @property
  def max(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-15-bar-stack-chart-dataLabels
    """
    return self._config_get()

  @max.setter
  def max(self, num):
    self._config(num)

  @property
  def stepSize(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example17-03-scale
    """
    return self._config_get()

  @stepSize.setter
  def stepSize(self, num):
    self._config(num)

  @property
  def step(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example17-03-scale
    """
    return self._config_get()

  @step.setter
  def step(self, num):
    self._config(num)


class OptionsAxis(Options):

  @property
  def label(self) -> OptionsAxisLabel:
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-06-bar-chart-centerYAxis

    :rtype: OptionsAxisLabel
    """
    return self._config_sub_data("label", OptionsAxisLabel)

  @property
  def tick(self) -> OptionsAxisLabel:
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example17-04-tick-label-interval
    
    :rtype: OptionsAxisLabel
    """
    return self._config_sub_data("tick", OptionsAxisLabel)

  @property
  def scale(self) -> OptionsScale:
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-06-bar-chart-centerYAxis

    :rtype: OptionsScale
    """
    return self._config_sub_data("scale", OptionsScale)

  @property
  def title(self) -> OptionsTitle:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsTitle
    """
    return self._config_sub_data("title", OptionsTitle)

  def add_title(self, text: str) -> OptionsTitle:
    """
    Description:
    ------------

    Related Pages:

    Attributes:
    ----------
    :param str text:

    :rtype: OptionsTitle
    """
    title = self._config_sub_data("title", OptionsTitle)
    title.text = text
    return title

  @property
  def align(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-06-bar-chart-centerYAxis
    """
    return self._config_get()

  @align.setter
  def align(self, text):
    self._config(text)

  @property
  def pointOnColumn(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @pointOnColumn.setter
  def pointOnColumn(self, flag):
    self._config(flag)


class OptionsDataLabels(Options):

  @property
  def visible(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @visible.setter
  def visible(self, flag):
    self._config(flag)

  @property
  def offsetY(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @offsetY.setter
  def offsetY(self, num):
    self._config(num)


class OptionsChartStack(Options):

  @property
  def type(self):
    """
    Description:
    ------------

    # normal, percent
    """
    return self._config_get()

  @type.setter
  def type(self, text):
    self._config(text)

  @property
  def types(self):
    return EnumStackTypes(self, "type")

  @property
  def connector(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-14-bar-stack-chart-connector
    """
    return self._config_get()

  @connector.setter
  def connector(self, flag):
    self._config(flag)


class OptionsChartSeries(Options):


  @property
  def dataLabels(self) -> OptionsDataLabels:
    """

    Related Pages:


    :rtype: OptionsDataLabels
    """
    return self._config_sub_data("dataLabels", OptionsDataLabels)

  @property
  def diverging(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-05-bar-chart-diverging
    """
    return self._config_get()

  @diverging.setter
  def diverging(self, flag):
    self._config(flag)

  @property
  def eventDetectType(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @eventDetectType.setter
  def eventDetectType(self, text):
    self._config(text)

  @property
  def eventDetectTypes(self):
    return EnumEventDetectTypes(self, "eventDetectType")

  @property
  def selectable(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @selectable.setter
  def selectable(self, flag):
    self._config(flag)

  @property
  def shift(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example06-02-column-chart-liveUpdate
    """
    return self._config_get()

  @shift.setter
  def shift(self, flag):
    self._config(flag)

  @property
  def stack(self) -> OptionsChartStack:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsChartStack
    """
    return self._config_sub_data("stack", OptionsChartStack)

  def stacked(self):
    self.stack.types.normal()

  @property
  def spline(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @spline.setter
  def spline(self, flag):
    self._config(flag)

  @property
  def showDot(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @showDot.setter
  def showDot(self, flag):
    self._config(flag)

  @property
  def zoomable(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example01-09-area-chart-zoomable
    """
    return self._config_get()

  @zoomable.setter
  def zoomable(self, flag):
    self._config(flag)


class OptionsDot(Options):

  @property
  def radius(self):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/nhn/tui.chart/blob/main/docs/en/chart-line.md
    """
    return self._config_get()

  @radius.setter
  def radius(self, num):
    self._config(num)


class OptionsThemeSeries(Options):

  @property
  def areaOpacity(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example01-12-area-chart-theme
    """
    return self._config_get()

  @areaOpacity.setter
  def areaOpacity(self, num):
    self._config(num)

  @property
  def barWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-10-bar-chart-theme
    """
    return self._config_get()

  @barWidth.setter
  def barWidth(self, num):
    self._config(num)

  @property
  def colors(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example01-12-area-chart-theme
    """
    return self._config_get()

  @colors.setter
  def colors(self, values):
    self._config(values)

  @property
  def dashSegments(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example01-12-area-chart-theme
    """
    return self._config_get()

  @dashSegments.setter
  def dashSegments(self, array):
    self._config(array)

  @property
  def fillColor(self):
    """
    Description:
    ------------
    The background color of the series.

    Related Pages:

      https://github.com/nhn/tui.chart/blob/main/docs/en/chart-scatter.md
    """
    return self._config_get()

  @fillColor.setter
  def fillColor(self, value):
    self._config(value)

  @property
  def lineWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example01-12-area-chart-theme
    """
    return self._config_get()

  @lineWidth.setter
  def lineWidth(self, num):
    self._config(num)

  @property
  def iconTypes(self):
    """
    Description:
    ------------

    Related Pages:

      http://nhn.github.io/tui.chart/latest/tutorial-example11-05-scatter-chart-iconType
    """
    return self._config_get()

  @iconTypes.setter
  def iconTypes(self, values):
    self._config(values)

  @property
  def dot(self) -> OptionsDot:
    """

    Related Pages:

      https://github.com/nhn/tui.chart/blob/main/docs/en/chart-line.md

    :rtype: OptionsDot
    """
    return self._config_sub_data("dot", OptionsDot)


class OptionsTheme(Options):

  @property
  def series(self) -> OptionsThemeSeries:
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example01-12-area-chart-theme

    :rtype: OptionsThemeSeries
    """
    return self._config_sub_data("series", OptionsThemeSeries)


class OptionsLegendItem(Options):

  @property
  def overflow(self):
    """
    Description:
    ------------

    Related Pages:

      http://nhn.github.io/tui.chart/latest/tutorial-example17-06-legend-ellipsis
    """
    return self._config_get()

  @overflow.setter
  def overflow(self, text):
    self._config(text)

  @property
  def width(self):
    """
    Description:
    ------------

    Related Pages:

      http://nhn.github.io/tui.chart/latest/tutorial-example17-06-legend-ellipsis
    """
    return self._config_get()

  @width.setter
  def width(self, num):
    self._config(num)


class OptionsLegend(Options):

  @property
  def align(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-10-bar-chart-theme
    """
    return self._config_get()

  @align.setter
  def align(self, text):
    self._config(text)

  @property
  def item(self) -> OptionsLegendItem:
    """
    Description:
    ------------

    Related Pages:

      http://nhn.github.io/tui.chart/latest/tutorial-example17-06-legend-ellipsis

    :rtype: OptionsLegendItem
    """
    return self._config_sub_data("item", OptionsLegendItem)

  @property
  def visible(self):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/nhn/tui.chart/blob/main/docs/en/common-legend.md
    """
    return self._config_get()

  @visible.setter
  def visible(self, flag):
    self._config(flag)


class OptionsTooltip(Options):
  def formatter(self):
    """
    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example08-04-line-chart-spline

    """
    pass


class OptionsChartPlotLine(Options):

  @property
  def value(self):
    """
    Description:
    ------------
    Value that corresponds to the x axis.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-10-bar-chart-theme
      https://github.com/nhn/tui.chart/blob/main/docs/en/common-plot.md
    """
    return self._config_get()

  @value.setter
  def value(self, text):
    self._config(text)

  @property
  def color(self):
    """
    Description:
    ------------
    Line color.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-10-bar-chart-theme
      https://github.com/nhn/tui.chart/blob/main/docs/en/common-plot.md
    """
    return self._config_get()

  @color.setter
  def color(self, text):
    self._config(text)

  @property
  def opacity(self):
    """
    Description:
    ------------
    Line opacity

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-10-bar-chart-theme
      https://github.com/nhn/tui.chart/blob/main/docs/en/common-plot.md
    """
    return self._config_get()

  @opacity.setter
  def opacity(self, num):
    self._config(num)


class OptionsChartPlotBand(Options):

  @property
  def color(self):
    """
    Description:
    ------------
    Box color.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-10-bar-chart-theme
      https://github.com/nhn/tui.chart/blob/main/docs/en/common-plot.md
    """
    return self._config_get()

  @color.setter
  def color(self, text):
    self._config(text)

  @property
  def range(self):
    """
    Description:
    ------------
    Values that correspond to the x-axis; entered in the array in the order of starting value and ending value.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example08-15-line-chart-plot-bands-lines
      https://github.com/nhn/tui.chart/blob/main/docs/en/common-plot.md
    """
    return self._config_get()

  @range.setter
  def range(self, values):
    self._config(values)

  @property
  def opacity(self):
    """
    Description:
    ------------
    Box color opacity

    Related Pages:

      https://nhn.github.io/tui.chart/latest/tutorial-example02-10-bar-chart-theme
      https://github.com/nhn/tui.chart/blob/main/docs/en/common-plot.md
    """
    return self._config_get()

  @opacity.setter
  def opacity(self, num):
    self._config(num)

  @property
  def mergeOverlappingRanges(self):
    """
    Description:
    ------------
    Determines whether to display overlapping bands when there are overlapping values in the range (default: false)

    Related Pages:

      https://github.com/nhn/tui.chart/blob/main/docs/en/common-plot.md
    """
    return self._config_get()

  @mergeOverlappingRanges.setter
  def mergeOverlappingRanges(self, flag):
    self._config(flag)


class OptionsChartPlot(Options):

  def add_lines(self, value, color='#fa2828'):
    """
    Description:
    -----------
    Line, Area, LineArea, LineScatter, ColumnLine.

    Related Pages:

      https://github.com/nhn/tui.chart/blob/main/docs/en/common-plot.md

    :rtype: OptionsChartPlotLine
    """
    line = self._config_sub_data_enum("lines", OptionsChartPlotLine)
    line.value = value
    line.color = color
    return line

  def add_band(self, values, color: str = '#ff5722', opacity: float = 0.1) -> OptionsChartPlotBand:
    """
    Description:
    -----------
    Line, Area, LineArea, LineScatter, ColumnLine

    Related Pages:

      https://github.com/nhn/tui.chart/blob/main/docs/en/common-plot.md

    :rtype: OptionsChartPlotBand
    """
    band = self._config_sub_data_enum("bands", OptionsChartPlotBand)
    band.range = [values]
    band.color = color
    band.opacity = opacity
    return band


class OptionsAnimation(Options):

  @property
  def duration(self):
    """
    Description:
    ------------
    Box color opacity

    Related Pages:

      http://nhn.github.io/tui.chart/latest/tutorial-example02-08-bar-chart-responsive
    """
    return self._config_get()

  @duration.setter
  def duration(self, num):
    self._config(num)


class OptionsResponsive(Options):

  @property
  def animation(self) -> OptionsAnimation:
    """
    Description:
    ------------

    :rtype: OptionsAnimation
    """
    return self._config_sub_data("animation", OptionsAnimation)


class OptionsChartOpts(Options):

  @property
  def chart(self) -> OptionsChartAttrs:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsChartAttrs
    """
    return self._config_sub_data("chart", OptionsChartAttrs)

  @property
  def legend(self) -> OptionsLegend:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsLegend
    """
    return self._config_sub_data("legend", OptionsLegend)

  @property
  def tooltip(self) -> OptionsTooltip:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsTooltip
    """
    return self._config_sub_data("tooltip", OptionsTooltip)

  @property
  def theme(self) -> OptionsTheme:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsTheme
    """
    return self._config_sub_data("theme", OptionsTheme)

  @property
  def series(self) -> OptionsChartSeries:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsChartSeries
    """
    return self._config_sub_data("series", OptionsChartSeries)

  @property
  def plot(self) -> OptionsChartPlot:
    """
    Description:
    ------------

    :rtype: OptionsChartPlot
    """
    return self._config_sub_data("plot", OptionsChartPlot)

  @property
  def xAxis(self) -> OptionsAxis:
    """
    Related Pages:


    :rtype: OptionsAxis
    """
    return self._config_sub_data("xAxis", OptionsAxis)

  @property
  def yAxis(self) -> OptionsAxis:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsAxis
    """
    return self._config_sub_data("yAxis", OptionsAxis)

  @property
  def usageStatistics(self):
    """
    Description:
    ------------

    """
    return self._config_get(False)

  @usageStatistics.setter
  def usageStatistics(self, flag):
    self._config(flag)

  @property
  def responsive(self) -> OptionsResponsive:
    """
    Description:
    ------------

    :rtype: OptionsResponsive
    """
    return self._config_sub_data("responsive", OptionsResponsive)


class OptionsCharts(Options):

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
  def config(self) -> OptionsChartOpts:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsChartOpts
    """
    return self._config_sub_data("options", OptionsChartOpts)

  @property
  def data(self) -> OptionsChartData:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsChartData
    """
    return self._config_sub_data("data", OptionsChartData)


class OptionsChartRadiusRange(Options):

  @property
  def inner(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @inner.setter
  def inner(self, value):
    self._config(value)

  @property
  def outer(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @outer.setter
  def outer(self, value):
    self._config(value)


class OptionsChartSeriesPie(Options):

  @property
  def radiusRange(self) -> OptionsChartRadiusRange:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsChartRadiusRange
    """
    return self._config_sub_data("radiusRange", OptionsChartRadiusRange)


class OptionsChartPieOpts(OptionsChartOpts):

  @property
  def series(self) -> OptionsChartSeriesPie:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsChartSeriesPie
    """
    return self._config_sub_data("series", OptionsChartSeriesPie)


class OptionsChartsPie(OptionsCharts):

  @property
  def config(self) -> OptionsChartPieOpts:
    """
    Description:
    ------------

    Related Pages:


    :rtype: OptionsChartPieOpts
    """
    return self._config_sub_data("options", OptionsChartPieOpts)
