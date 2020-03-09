
from epyk.core.data import DataClass


class OptionAxesTicks(DataClass):

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


class OptionAxes(DataClass):

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
  def ticks(self):
    """

    :return:
    """
    return self.sub_data("ticks", OptionAxesTicks)

  @property
  def gridLines(self):
    return self.sub_data("gridLines", OptionAxesGridLine)

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

  def add_x_axes(self):
    return self.sub_data_enum("xAxes", OptionAxes)

  def x_axes(self, i=None):
    if "xAxes" not in self._attrs:
      self.add_x_axes()

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


class OptionTitle(DataClass):
  @property
  def display(self):
    """
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
  def scales(self):
    return self.sub_data("scales", OptionScales)

  @property
  def layout(self):
    return self.sub_data("layout", OptionLayout)

  @property
  def title(self):
    return self.sub_data("title", OptionTitle)


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

