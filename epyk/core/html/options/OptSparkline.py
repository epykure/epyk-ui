#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import OptChart


class OptionsSpark(OptChart.OptionsChart):
  component_properties = ("width", )

  @property
  def width(self):
    """
    Description:
    ------------
    Width of the chart - Defaults to 'auto' - May be any valid css width - 1.5em, 20px, etc (using a number without
    a unit specifier won't do what you want) - This option does nothing for bar and tristate chars (see barWidth)/

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get("100%")

  @width.setter
  def width(self, value):
    self._config(value)

  @property
  def height(self):
    """
    Description:
    ------------
    Height of the chart - Defaults to 'auto' (line height of the containing tag).

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get("100%")

  @height.setter
  def height(self, value):
    self._config(value)

  @property
  def chartRangeMin(self):
    """
    Description:
    ------------
    Specify the minimum value to use for the range of Y values of the chart - Defaults to the minimum value supplied.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get(None)

  @chartRangeMin.setter
  def chartRangeMin(self, value):
    self._config(value)

  @property
  def chartRangeMax(self):
    """
    Description:
    ------------
    Specify the maximum value to use for the range of Y values of the chart - Defaults to the maximum value supplied.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get(1)

  @chartRangeMax.setter
  def chartRangeMax(self, value):
    self._config(value)

  @property
  def composite(self):
    """
    Description:
    ------------
    If true then don't erase any existing chart attached to the tag, but draw another chart over the top.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get(False)

  @composite.setter
  def composite(self, flag):
    self._config(flag)

  @property
  def lineWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get(1)

  @lineWidth.setter
  def lineWidth(self, value):
    self._config(value)

  @property
  def lineColor(self):
    """
    Description:
    ------------
    Used by line and discrete charts to specify the colour of the line drawn as a CSS values string.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get("")

  @lineColor.setter
  def lineColor(self, value):
    self._config(value)

  @property
  def fillColor(self):
    """
    Description:
    ------------
    Specify the colour used to fill the area under the graph as a CSS value. Set to false to disable fill.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get("")

  @fillColor.setter
  def fillColor(self, value):
    self._config(value)

  @property
  def enableTagOptions(self):
    """
    Description:
    ------------
    If true then options can be specified as attributes on each tag to be transformed into a sparkline,
    as well as passed to the sparkline() function. See also tagOptionPrefix.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get(self.component.page.theme.danger[1])

  @enableTagOptions.setter
  def enableTagOptions(self, color):
    self._config(color)

  @property
  def tagOptionPrefix(self):
    """
    Description:
    ------------
    String that each option passed as an attribute on a tag must begin with. Defaults to 'spark'.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get(self.component.page.theme.danger[1])

  @tagOptionPrefix.setter
  def tagOptionPrefix(self, color):
    self._config(color)

  @property
  def tagValuesAttribute(self):
    """
    Description:
    ------------
    The name of the tag attribute to fetch values from, if present - Defaults to 'values'.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get(self.component.page.theme.danger[1])

  @tagValuesAttribute.setter
  def tagValuesAttribute(self, color):
    self._config(color)

  @property
  def disableHiddenCheck(self):
    """
    Description:
    ------------
    Set to true to disable checking for hidden sparklines.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get(self.component.page.theme.danger[1])

  @disableHiddenCheck.setter
  def disableHiddenCheck(self, color):
    self._config(color)


class OptionsSparkLine(OptionsSpark):

  @property
  def defaultPixelsPerValue(self):
    """
    Description:
    ------------
    Defaults to 3 pixels of width for each value in the chart.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-docs
    """
    return self._config_get(3)

  @defaultPixelsPerValue.setter
  def defaultPixelsPerValue(self, color):
    self._config(color)

  @property
  def minSpotColor(self):
    """
    Description:
    ------------
    The CSS colour of the marker displayed for the minimum value. Set to false or an empty string to hide it.

    Usage::

    """
    return self._config_get("")

  @minSpotColor.setter
  def minSpotColor(self, color):
    self._config(color)

  @property
  def maxSpotColor(self):
    """
    Description:
    ------------
    The CSS colour of the marker displayed for the maximum value. Set to false or an empty string to hide it.

    Usage::

    """
    return self._config_get("")

  @maxSpotColor.setter
  def maxSpotColor(self, color):
    self._config(color)

  @property
  def highlightSpotColor(self):
    """
    Description:
    ------------
    Specifies a colour for the spot that appears on a value when moused over. Set to null to disable.

    Usage::

    """
    return self._config_get("")

  @highlightSpotColor.setter
  def highlightSpotColor(self, color):
    self._config(color)

  @property
  def highlightLineColor(self):
    """
    Description:
    ------------
    Specifies a colour for the vertical line that appears through a value when moused over. Set to null to disable.

    Usage::

    """
    return self._config_get("")

  @highlightLineColor.setter
  def highlightLineColor(self, color):
    self._config(color)

  @property
  def lineWidth(self):
    """
    Description:
    ------------
    In pixels (default: 1) - Integer.

    Usage::

    """
    return self._config_get(1)

  @lineWidth.setter
  def lineWidth(self, color):
    self._config(color)

  @property
  def normalRangeMin(self):
    """
    Description:
    ------------
    Specify threshold values between which to draw a bar to denote the "normal" or expected range of values.

    Usage::

    """
    return self._config_get("")

  @normalRangeMin.setter
  def normalRangeMin(self, color):
    self._config(color)

  @property
  def normalRangeMax(self):
    """
    Description:
    ------------
    Specify threshold values between which to draw a bar to denote the "normal" or expected range of values.

    Usage::

    """
    return self._config_get("")

  @normalRangeMax.setter
  def normalRangeMax(self, color):
    self._config(color)

  @property
  def spotRadius(self):
    """
    Description:
    ------------
    Radius of all spot markers, In pixels (default: 1.5) - Integer.

    Usage::

    """
    return self._config_get(1.5)

  @spotRadius.setter
  def spotRadius(self, num):
    self._config(num)

  @property
  def spotColor(self):
    """
    Description:
    ------------
    The CSS colour of the final value marker. Set to false or an empty string to hide it.

    Usage::

    """
    return self._config_get("")

  @spotColor.setter
  def spotColor(self, color):
    self._config(color)

  @property
  def valueSpots(self):
    """
    Description:
    ------------
    Specifies which points to draw spots on, and with which colour. Accepts a range.

    Usage::

    """
    return self._config_get({})

  @valueSpots.setter
  def valueSpots(self, color):
    self._config(color)

  @property
  def drawNormalOnTop(self):
    """
    Description:
    ------------
    By default the normal range is drawn behind the fill area of the chart.

    Usage::

    """
    return self._config_get(False)

  @drawNormalOnTop.setter
  def drawNormalOnTop(self, flag):
    self._config(flag)

  @property
  def xvalues(self):
    """
    Description:
    ------------
    By default the normal range is drawn behind the fill area of the chart.

    Usage::

    """
    return self._config_get(None)

  @xvalues.setter
  def xvalues(self, values):
    self._config(values)

  @property
  def chartRangeMinX(self):
    """
    Description:
    ------------
    Specifies the minimum value to use for the X value of the chart.

    Usage::

    """
    return self._config_get(None)

  @chartRangeMinX.setter
  def chartRangeMinX(self, values):
    self._config(values)

  @property
  def chartRangeMaxX(self):
    """
    Description:
    ------------
    Specifies the maximum value to use for the X value of the chart.

    Usage::

    """
    return self._config_get(None)

  @chartRangeMaxX.setter
  def chartRangeMaxX(self, values):
    self._config(values)


class OptionsSparkLineBar(OptionsSpark):

  @property
  def barColor(self):
    """
    Description:
    ------------
    CSS colour used for postive values.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(4)

  @barColor.setter
  def barColor(self, value):
    self._config(value)

  @property
  def zeroColor(self):
    """
    Description:
    ------------
    CSS colour used for values equal to zero.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @zeroColor.setter
  def zeroColor(self, color):
    self._config(color)

  @property
  def nullColor(self):
    """
    Description:
    ------------
    CSS colour used for values equal to null.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @nullColor.setter
  def nullColor(self, color):
    self._config(color)

  @property
  def barWidth(self):
    """
    Description:
    ------------
    Width of each bar, in pixels (integer).

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(4)

  @barWidth.setter
  def barWidth(self, value):
    self._config(value)

  @property
  def barSpacing(self):
    """
    Description:
    ------------
    Space between each bar, in pixels (integer).

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(1)

  @barSpacing.setter
  def barSpacing(self, value):
    self._config(value)

  @property
  def negBarColor(self):
    """
    Description:
    ------------
    CSS colour used for negative values.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(self.component.page.theme.danger[1])

  @negBarColor.setter
  def negBarColor(self, color):
    self._config(color)

  @property
  def zeroAxis(self):
    """
    Description:
    ------------
    Centers the y-axis at zero if true (default).

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(True)

  @zeroAxis.setter
  def zeroAxis(self, value):
    self._config(value)

  @property
  def colorMap(self):
    """
    Description:
    ------------
    A range map to map specific values to selected colours.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @colorMap.setter
  def colorMap(self, colors):
    self._config(colors)

  @property
  def stackedBarColor(self):
    """
    Description:
    ------------
    An array of colours to use for stacked bar charts.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @stackedBarColor.setter
  def stackedBarColor(self, colors):
    self._config(colors)


class OptionsSparkLineBoxPlot(OptionsSpark):

  @property
  def raw(self):
    """
    Description:
    ------------
    If set to false (default) then the values supplied are used to caculate the box data points for you.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(False)

  @raw.setter
  def raw(self, values):
    self._config(values)

  @property
  def showOutliers(self):
    """
    Description:
    ------------
    If true (default) then outliers (values > 1.5x the IQR) are marked with circles and the whiskers are placed at Q1
    and Q3 instead of the least and greatest value

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(True)

  @showOutliers.setter
  def showOutliers(self, values):
    self._config(values)

  @property
  def outlierIQR(self):
    """
    Description:
    ------------
    Set the inter-quartile range multipler used to calculate values that qualify as an outlier - Defaults to 1.5.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @outlierIQR.setter
  def outlierIQR(self, values):
    self._config(values)

  @property
  def boxLineColor(self):
    """
    Description:
    ------------
    CSS line colour used to outline the box.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @boxLineColor.setter
  def boxLineColor(self, values):
    self._config(values)

  @property
  def boxFillColor(self):
    """
    Description:
    ------------
    CSS fill colour used for the box.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @boxFillColor.setter
  def boxFillColor(self, values):
    self._config(values)

  @property
  def whiskerColor(self):
    """
    Description:
    ------------
    CSS colour used to draw the whiskers.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @whiskerColor.setter
  def whiskerColor(self, values):
    self._config(values)

  @property
  def outlierLineColor(self):
    """
    Description:
    ------------
    CSS colour used to draw the outlier circles.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @outlierLineColor.setter
  def outlierLineColor(self, values):
    self._config(values)

  @property
  def outlierFillColor(self):
    """
    Description:
    ------------
    CSS colour used to fill the outlier circles.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @outlierFillColor.setter
  def outlierFillColor(self, values):
    self._config(values)

  @property
  def spotRadius(self):
    """
    Description:
    ------------
    Radius in pixels to draw the outlier circles.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @spotRadius.setter
  def spotRadius(self, values):
    self._config(values)

  @property
  def medianColor(self):
    """
    Description:
    ------------
    CSS colour used to draw the median line.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @medianColor.setter
  def medianColor(self, values):
    self._config(values)

  @property
  def target(self):
    """
    Description:
    ------------
    If set to a value, then a small crosshair is drawn at that point to represent a target value.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @target.setter
  def target(self, value):
    self._config(value)

  @property
  def targetColor(self):
    """
    Description:
    ------------
    CSS colour used to draw the target crosshair, if set.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @targetColor.setter
  def targetColor(self, value):
    self._config(value)

  @property
  def minValue(self):
    """
    Description:
    ------------
    If minvalue and maxvalue are set then the scale of the plot is fixed. By default minValue and maxValue are
    deduced from the values supplied.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @minValue.setter
  def minValue(self, value):
    self._config(value)

  @property
  def maxValue(self):
    """
    Description:
    ------------
    If minvalue and maxvalue are set then the scale of the plot is fixed. By default minValue and maxValue are
    deduced from the values supplied.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @maxValue.setter
  def maxValue(self, value):
    self._config(value)


class OptionsSparkLinePie(OptionsSpark):

  @property
  def sliceColors(self):
    """
    Description:
    ------------
    An array of CSS colors to use for pie slices.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @sliceColors.setter
  def sliceColors(self, values):
    self._config(values)

  @property
  def offset(self):
    """
    Description:
    ------------
    Angle in degrees to offset the first slice.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @offset.setter
  def offset(self, value):
    self._config(value)

  @property
  def borderWidth(self):
    """
    Description:
    ------------
    Width of the border to draw around the whole pie chart, in pixels.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @borderWidth.setter
  def borderWidth(self, value):
    self._config(value)

  @property
  def borderColor(self):
    """
    Description:
    ------------
    CSS color to use to draw the pie border.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get("#000")

  @borderColor.setter
  def borderColor(self, value):
    self._config(value)


class OptionsSparkLineBullet(OptionsSpark):

  @property
  def targetColor(self):
    """
    Description:
    ------------
    The CSS colour of the vertical target market.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @targetColor.setter
  def targetColor(self, value):
    self._config(value)

  @property
  def targetWidth(self):
    """
    Description:
    ------------
    The width of the target marker in pixels (integer).

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @targetWidth.setter
  def targetWidth(self, value):
    self._config(value)

  @property
  def performanceColor(self):
    """
    Description:
    ------------
    The CSS color of the performance measure horizontal bar.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @performanceColor.setter
  def performanceColor(self, value):
    self._config(value)

  @property
  def rangeColors(self):
    """
    Description:
    ------------
    Colors to use for each qualitative range background color.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @rangeColors.setter
  def rangeColors(self, values):
    self._config(values)


class OptionsSparkLineDiscrete(OptionsSpark):

  @property
  def lineHeight(self):
    """
    Description:
    ------------
    Height of each line in pixels.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @lineHeight.setter
  def lineHeight(self, value):
    self._config(value)

  @property
  def thresholdValue(self):
    """
    Description:
    ------------
    Height of each line in pixels.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @thresholdValue.setter
  def thresholdValue(self, value):
    self._config(value)

  @property
  def thresholdColor(self):
    """
    Description:
    ------------
    Height of each line in pixels.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @thresholdColor.setter
  def thresholdColor(self, value):
    self._config(value)


class OptionsSparkLineTristate(OptionsSpark):

  @property
  def posBarColor(self):
    """
    Description:
    ------------
    CSS colour for positive (win) values.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @posBarColor.setter
  def posBarColor(self, value):
    self._config(value)

  @property
  def negBarColor(self):
    """
    Description:
    ------------
    CSS colour for negative (lose) values.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @negBarColor.setter
  def negBarColor(self, value):
    self._config(value)

  @property
  def zeroBarColor(self):
    """
    Description:
    ------------
    CSS colour for zero (draw) values.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @zeroBarColor.setter
  def zeroBarColor(self, value):
    self._config(value)

  @property
  def barWidth(self):
    """
    Description:
    ------------
    Width of each bar, in pixels (integer).

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @barWidth.setter
  def barWidth(self, value):
    self._config(value)

  @property
  def barSpacing(self):
    """
    Description:
    ------------
    Space between each bar, in pixels (integer).

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @barSpacing.setter
  def barSpacing(self, value):
    self._config(value)

  @property
  def colorMap(self):
    """
    Description:
    ------------
    A range map to map specific values to selected colours.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about
    """
    return self._config_get(None)

  @colorMap.setter
  def colorMap(self, colors):
    self._config(colors)
