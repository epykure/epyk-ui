#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.data.DataClass import DataClass
from epyk.core.js.packages import packageImport
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class OptionAxesTicks(DataClass):

  @property
  def fontColor(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["fontColor"]

  @fontColor.setter
  def fontColor(self, val):
    self._attrs["fontColor"] = val

  @property
  def fontSize(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["fontSize"]

  @fontSize.setter
  def fontSize(self, val):
    self._attrs["fontSize"] = val

  @property
  def beginAtZero(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["beginAtZero"]

  @beginAtZero.setter
  def beginAtZero(self, val):
    self._attrs["beginAtZero"] = val

  @property
  def max(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["max"]

  @max.setter
  def max(self, val):
    self._attrs["max"] = val

  @property
  def min(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["min"]

  @min.setter
  def min(self, val):
    self._attrs["min"] = val

  @property
  def suggestedMin(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["suggestedMin"]

  @suggestedMin.setter
  def suggestedMin(self, val):
    self._attrs["suggestedMin"] = val

  @property
  def suggestedMax(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["suggestedMax"]

  @suggestedMax.setter
  def suggestedMax(self, val):
    self._attrs["suggestedMax"] = val

  @property
  def stepSize(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["stepSize"]

  @stepSize.setter
  def stepSize(self, val):
    self._attrs["stepSize"] = val

  def scale(self, factor=1000, alias="k", digits=0):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param factor:
    :param alias:
    :param digits:
    """
    self._attrs["callback"] = JsObjects.JsVoid("function(label, index, labels) {var pointVal = label/%s; return pointVal.toFixed(%s) + '%s';}" % (factor, digits, alias))

  @packageImport("accounting")
  def toMoney(self, symbol="", digit=0, thousand_sep=".", decimal_sep=","):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param symbol:
    :param digit:
    :param thousand_sep:
    :param decimal_sep:
    """
    symbol = JsUtils.jsConvertData(symbol, None)
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
    self._attrs["callback"] = JsObjects.JsVoid("function(label, index, labels) {return accounting.formatMoney(label, %s, %s, %s, %s)}" % (symbol, digit, thousand_sep, decimal_sep))

  @packageImport("accounting")
  def toNumber(self, digit=0, thousand_sep="."):
    """
    Description:
    -----------
    Convert to number using the accounting Javascript module-

    Usage::

      Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param digit: Integer. The number of digit to be displayed
    :param thousand_sep:  The thousand symbol separator
    """
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    self._attrs["callback"] = JsObjects.JsVoid("function(label, index, labels) {return accounting.formatNumber(label, %s, %s)}" % (digit, thousand_sep))


class OptionLabels(DataClass):

  @property
  def fontColor(self):
    """
    """
    return self._attrs["fontColor"]

  @fontColor.setter
  def fontColor(self, val):
    self._attrs["fontColor"] = val


class OptionAxesGridLine(DataClass):

  @property
  def display(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["display"]

  @display.setter
  def display(self, val):
    self._attrs["display"] = val

  @property
  def circular(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["circular"]

  @circular.setter
  def circular(self, val):
    self._attrs["circular"] = val

  @property
  def color(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["color"]

  @color.setter
  def color(self, val):
    self._attrs["color"] = val

  @property
  def borderDash(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["borderDash"]

  @borderDash.setter
  def borderDash(self, val):
    self._attrs["borderDash"] = val

  @property
  def borderDashOffset(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["borderDashOffset"]

  @borderDashOffset.setter
  def borderDashOffset(self, val):
    self._attrs["borderDashOffset"] = val

  @property
  def lineWidth(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["lineWidth"]

  @lineWidth.setter
  def lineWidth(self, val):
    self._attrs["lineWidth"] = val

  @property
  def drawBorder(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["drawBorder"]

  @drawBorder.setter
  def drawBorder(self, val):
    self._attrs["drawBorder"] = val

  @property
  def drawOnChartArea(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["drawOnChartArea"]

  @drawOnChartArea.setter
  def drawOnChartArea(self, val):
    self._attrs["drawOnChartArea"] = val

  @property
  def drawTicks(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["drawTicks"]

  @drawTicks.setter
  def drawTicks(self, val):
    self._attrs["drawTicks"] = val

  @property
  def tickMarkLength(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["tickMarkLength"]

  @tickMarkLength.setter
  def tickMarkLength(self, val):
    self._attrs["tickMarkLength"] = val

  @property
  def zeroLineWidth(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["zeroLineWidth"]

  @zeroLineWidth.setter
  def zeroLineWidth(self, val):
    self._attrs["zeroLineWidth"] = val

  @property
  def zeroLineColor(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["zeroLineColor"]

  @zeroLineColor.setter
  def zeroLineColor(self, val):
    self._attrs["zeroLineColor"] = val

  @property
  def zeroLineBorderDash(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["zeroLineBorderDash"]

  @zeroLineBorderDash.setter
  def zeroLineBorderDash(self, val):
    self._attrs["zeroLineBorderDash"] = val

  @property
  def zeroLineBorderDashOffset(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["zeroLineBorderDashOffset"]

  @zeroLineBorderDashOffset.setter
  def zeroLineBorderDashOffset(self, val):
    self._attrs["zeroLineBorderDashOffset"] = val

  @property
  def offsetGridLines(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["offsetGridLines"]

  @offsetGridLines.setter
  def offsetGridLines(self, val):
    self._attrs["offsetGridLines"] = val

  @property
  def z(self):
    """
    https://www.chartjs.org/docs/latest/axes/styling.html#grid-line-configuration
    """
    return self._attrs["z"]

  @z.setter
  def z(self, val):
    self._attrs["z"] = val


class OptionAxesScaleLabel(DataClass):

  @property
  def display(self):
    return self._attrs["display"]

  @display.setter
  def display(self, val):
    self._attrs["display"] = val

  @property
  def fontColor(self):
    return self._attrs["fontColor"]

  @fontColor.setter
  def fontColor(self, val):
    self._attrs["fontColor"] = val

  @property
  def labelString(self):
    return self._attrs["labelString"]

  @labelString.setter
  def labelString(self, val):
    self._attrs["labelString"] = val


class OptionDisplayFormats(DataClass):

  @property
  def quarter(self):
    return self._attrs["quarter"]

  @quarter.setter
  def quarter(self, val):
    self._attrs["quarter"] = val


class OptionAxesTime(DataClass):

  @property
  def displayFormats(self):
    return self.sub_data("displayFormats", OptionDisplayFormats)


class OptionAxes(DataClass):

  @property
  def display(self):
    return self._attrs["display"]

  @display.setter
  def display(self, val):
    self._attrs["display"] = val

  @property
  def distribution(self):
    return self._attrs["distribution"]

  @distribution.setter
  def distribution(self, val):
    self._attrs["distribution"] = val

  @property
  def type(self):
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    if val == "time":
      from epyk.core.js import Imports

      Imports.JS_IMPORTS["Chart.js"]["req"] = [{'alias': 'moment'}]
      # Add the package moment.js is time is used
      #self._report.jsImports.add("moment")
    self._attrs["type"] = val

  @property
  def stacked(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["stacked"]

  @stacked.setter
  def stacked(self, val):
    self._attrs["stacked"] = val

  @property
  def id(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["id"]

  @id.setter
  def id(self, val):
    self._attrs["id"] = val

  @property
  def offset(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["offset"]

  @offset.setter
  def offset(self, val):
    self._attrs["offset"] = val

  @property
  def position(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["position"]

  @position.setter
  def position(self, val):
    self._attrs["position"] = val

  @property
  def stepSize(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["stepSize"]

  @stepSize.setter
  def stepSize(self, val):
    self._attrs["stepSize"] = val

  @property
  def ticks(self):
    """

    :return:
    """
    return self.sub_data("ticks", OptionAxesTicks)

  @property
  def time(self):
    """

    :return:
    """
    return self.sub_data("time", OptionAxesTime)

  @property
  def gridLines(self):
    return self.sub_data("gridLines", OptionAxesGridLine)

  @property
  def scaleLabel(self):
    return self.sub_data("scaleLabel", OptionAxesScaleLabel)

  def add_label(self, text, color=None):
    self.scaleLabel.display = True
    self.scaleLabel.labelString = text
    if color is not None:
      self.scaleLabel.fontColor = color
    return self

  def category(self, vals):
    """

    :param vals:
    :return:
    """
    self._attrs["type"] = "category"
    self._attrs["labels"] = vals


class OptionScales(DataClass):

  def add_y_axis(self):
    return self.sub_data_enum("yAxes", OptionAxes)

  def y_axis(self, i=None):
    """

    :param i:
    :rtype: OptionAxes
    """
    if "yAxes" not in self._attrs:
      self.add_y_axis()

    if i is None:
      return self._attrs["yAxes"][-1]

    return self._attrs["yAxes"][i]

  def add_x_axis(self):
    return self.sub_data_enum("xAxes", OptionAxes)

  def x_axes(self, i=None):
    if "xAxes" not in self._attrs:
      self.add_x_axis()

    if i is None:
      return self._attrs["xAxes"][-1]

    return self._attrs["xAxes"][i]


class OptionPadding(DataClass):

  @property
  def left(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["left"]

  @left.setter
  def left(self, val):
    self._attrs["left"] = val

  @property
  def right(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["right"]

  @right.setter
  def right(self, val):
    self._attrs["right"] = val

  @property
  def top(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["top"]

  @top.setter
  def top(self, val):
    self._attrs["top"] = val

  @property
  def bottom(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["bottom"]

  @bottom.setter
  def bottom(self, val):
    self._attrs["bottom"] = val


class OptionLayout(DataClass):

  @property
  def padding(self):
    return self.sub_data("padding", OptionPadding)


class OptionLegend(DataClass):

  @property
  def labels(self):
    return self.sub_data("labels", OptionLabels)

  @property
  def align(self):
    """
    Description:
    ------------
    Alignment of the legend.

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/legend.html

    """
    return self._attrs.get("align", "center")

  @align.setter
  def align(self, val):
    self._attrs["align"] = val

  @property
  def display(self):
    """
    Description:
    ------------
    Is the legend shown?

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/legend.html

    """
    return self._attrs.get("display", True)

  @display.setter
  def display(self, bool):
    self._attrs["display"] = bool

  @property
  def position(self):
    """
    Description:
    ------------
    Position of the legend
    values are top, left, bottom, right

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/legend.html

    """
    return self._attrs["position"]

  @position.setter
  def position(self, val):
    self._attrs["position"] = val

  @property
  def reverse(self):
    """
    Description:
    ------------
    Legend will show datasets in reverse order.

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/legend.html

    """
    return self._attrs.get("reverse", False)

  @reverse.setter
  def reverse(self, bool):
    self._attrs["align"] = bool

  @property
  def rtl(self):
    """
    Description:
    ------------
    true for rendering the legends from right to left.

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/legend.html

    """
    return self._attrs.get("rtl", False)

  @rtl.setter
  def rtl(self, bool):
    self._attrs["rtl"] = bool


class OptionPoint(DataClass):

  @property
  def radius(self):
    """
    Description:
    ------------
    """
    return self._attrs.get("radius", False)

  @radius.setter
  def radius(self, num):
    self._attrs["radius"] = num


class OptionElements(DataClass):

  @property
  def point(self):
    return self.sub_data("point", OptionPoint)


class OptionTitle(DataClass):

  @property
  def display(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/title.html

    """
    return self._attrs["display"]

  @display.setter
  def display(self, val):
    self._attrs["display"] = val

  @property
  def text(self):
    return self._attrs["text"]

  @text.setter
  def text(self, val):
    self._attrs["text"] = val

  @property
  def position(self):
    return self._attrs["position"]

  @position.setter
  def position(self, val):
    self._attrs["position"] = val

  @property
  def fontSize(self):
    return self._attrs["fontSize"]

  @fontSize.setter
  def fontSize(self, val):
    self._attrs["fontSize"] = val

  @property
  def fontFamily(self):
    return self._attrs["fontFamily"]

  @fontFamily.setter
  def fontFamily(self, val):
    self._attrs["fontFamily"] = val

  @property
  def fontColor(self):
    return self._attrs["fontColor"]

  @fontColor.setter
  def fontColor(self, val):
    self._attrs["fontColor"] = val

  @property
  def fontStyle(self):
    return self._attrs["fontStyle"]

  @fontStyle.setter
  def fontStyle(self, val):
    self._attrs["fontStyle"] = val

  @property
  def padding(self):
    return self._attrs["padding"]

  @padding.setter
  def padding(self, val):
    self._attrs["padding"] = val

  @property
  def lineHeight(self):
    return self._attrs["lineHeight"]

  @lineHeight.setter
  def lineHeight(self, val):
    self._attrs["lineHeight"] = val


class Options(DataClass):

  @property
  def responsive(self):
    return self._attrs["responsive"]

  @responsive.setter
  def responsive(self, bool):
    self.add("responsive", bool)

  @property
  def maintainAspectRatio(self):
    return self._attrs["maintainAspectRatio"]

  @maintainAspectRatio.setter
  def maintainAspectRatio(self, bool):
    self.add("maintainAspectRatio", bool)

  @property
  def elements(self):
    return self.sub_data("elements", OptionElements)

  @property
  def scales(self):
    return self.sub_data("scales", OptionScales)

  @property
  def layout(self):
    return self.sub_data("layout", OptionLayout)

  @property
  def title(self):
    return self.sub_data("title", OptionTitle)

  @property
  def legend(self):
    return self.sub_data("legend", OptionLegend)

  @property
  def plugins(self):
    return self.sub_data("plugins", OptionChartJsPlugins)

  def add_title(self, text, color=None):
    """

    :param text:
    :param color:
    """
    self.title.display = True
    self.title.text = text
    if color is not None:
      self.title.fontColor = color
    return self

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


class OptionPieAnimation(DataClass):
  @property
  def animateRotate(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["animateRotate"]

  @animateRotate.setter
  def animateRotate(self, val):
    self.attr("animateRotate", val)

  @property
  def animateScale(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["animateScale"]

  @animateScale.setter
  def animateScale(self, val):
    self.attr("animateScale", val)


class OptionsBar(Options):
  pass


class OptionsPie(Options):

  @property
  def cutoutPercentage(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["cutoutPercentage"]

  @cutoutPercentage.setter
  def cutoutPercentage(self, val):
    self._attrs["cutoutPercentage"] = val

  @property
  def rotation(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["rotation"]

  @rotation.setter
  def rotation(self, val):
    self._attrs["rotation"] = val

  @property
  def circumference(self):
    """
    https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs["circumference"]

  @circumference.setter
  def circumference(self, val):
    self._attrs["circumference"] = val

  @property
  def animation(self):
    return self.sub_data("animation", OptionPieAnimation)


class OptionsLine(Options):
  @property
  def showLines(self):
    """
    https://www.chartjs.org/docs/latest/charts/polar.html
    """
    return self._attrs["showLines"]

  @showLines.setter
  def showLines(self, val):
    self._attrs["showLines"] = val

  @property
  def spanGaps(self):
    """
    https://www.chartjs.org/docs/latest/charts/polar.html
    """
    return self._attrs["spanGaps"]

  @spanGaps.setter
  def spanGaps(self, val):
    self._attrs["spanGaps"] = val


class OptionsPolar(Options):

  @property
  def startAngle(self):
    """
    https://www.chartjs.org/docs/latest/charts/polar.html
    """
    return self._attrs["startAngle"]

  @startAngle.setter
  def startAngle(self, val):
    self._attrs["startAngle"] = val

  @property
  def animation(self):
    return self.sub_data("animation", OptionPieAnimation)


class OptionChartJsPlugins(DataClass):

  @property
  @packageImport('chartjs-plugin-zoom')
  def zoom(self):
    """
    Description:
    -----------
    A zoom and pan plugin for Chart.js. Currently requires Chart.js >= 2.6.0

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    from epyk.core.html.graph.exts import ChartJsZoom
    return self.sub_data("zoom", ChartJsZoom.Zoom)

  @property
  @packageImport('chartjs-plugin-crosshair')
  def crosshair(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    from epyk.core.html.graph.exts import ChartJsCrosshair
    return self.sub_data("crosshair", ChartJsCrosshair.Crosshair)

  @property
  @packageImport('chartjs-plugin-annotation')
  def annotation(self):
    """
    Description:
    -----------
    An annotation plugin for Chart.js >= 2.4.0

    This plugin draws lines and boxes on the chart area.

    Annotations work with line, bar, scatter and bubble charts that use linear, logarithmic, time, or category scales.
    Annotations will not work on any chart that does not have exactly two axes, including pie, radar, and polar area charts.

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    from epyk.core.html.graph.exts import ChartJsAnnotation
    return self.sub_data("annotation", ChartJsAnnotation.Annotation)


