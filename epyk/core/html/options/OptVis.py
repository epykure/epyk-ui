
from epyk.core.data import DataClass


class OptionsTime(DataClass):

  @property
  def scale(self):
    return self._attrs["scale"]

  @scale.setter
  def scale(self, val):
    self._attrs["scale"] = val

  @property
  def step(self):
    return self._attrs["step"]

  @step.setter
  def step(self, val):
    self._attrs["step"] = val


class OptionsBackgroundColor(DataClass):

  @property
  def fill(self):
    return self._attrs["fill"]

  @fill.setter
  def fill(self, val):
    self._attrs["fill"] = val

  @property
  def stroke(self):
    return self._attrs["stroke"]

  @stroke.setter
  def stroke(self, val):
    self._attrs["stroke"] = val

  @property
  def strokeWidth(self):
    return self._attrs["strokeWidth"]

  @strokeWidth.setter
  def strokeWidth(self, val):
    self._attrs["strokeWidth"] = val


class Options2D(DataClass):

  @property
  def autoResize(self):
    """
    If true, the Timeline will automatically detect when its container is resized, and redraw itself accordingly.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["autoResize"]

  @autoResize.setter
  def autoResize(self, val):
    self._attrs["autoResize"] = val

  @property
  def configure(self):
    """
    When true, a configurator is loaded where all configuration options of the Graph2d can be changed live.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["configure"]

  @configure.setter
  def configure(self, val):
    self._attrs["configure"] = val

  @property
  def clickToUse(self):
    return self._attrs["clickToUse"]

  @clickToUse.setter
  def clickToUse(self, val):
    self._attrs["clickToUse"] = val

  @property
  def end(self):
    return self._attrs["end"]

  @end.setter
  def end(self, val):
    self._attrs["end"] = val

  @property
  def height(self):
    return self._attrs["height"]

  @height.setter
  def height(self, val):
    self._attrs["height"] = val

  @property
  def max(self):
    return self._attrs["max"]

  @max.setter
  def max(self, val):
    self._attrs["max"] = val

  @property
  def maxHeight(self):
    return self._attrs["maxHeight"]

  @maxHeight.setter
  def maxHeight(self, val):
    self._attrs["maxHeight"] = val

  @property
  def maxMinorChars(self):
    return self._attrs["maxMinorChars"]

  @maxMinorChars.setter
  def maxMinorChars(self, val):
    self._attrs["maxMinorChars"] = val

  @property
  def min(self):
    return self._attrs["min"]

  @min.setter
  def min(self, val):
    self._attrs["min"] = val

  @property
  def minHeight(self):
    return self._attrs["minHeight"]

  @minHeight.setter
  def minHeight(self, val):
    self._attrs["minHeight"] = val

  @property
  def moveable(self):
    return self._attrs["moveable"]

  @moveable.setter
  def moveable(self, val):
    self._attrs["moveable"] = val

  @property
  def orientation(self):
    return self._attrs["orientation"]

  @orientation.setter
  def orientation(self, val):
    self._attrs["orientation"] = val

  @property
  def showCurrentTime(self):
    return self._attrs["showCurrentTime"]

  @showCurrentTime.setter
  def showCurrentTime(self, val):
    self._attrs["showCurrentTime"] = val

  @property
  def showCustomTime(self):
    return self._attrs["showCustomTime"]

  @showCustomTime.setter
  def showCustomTime(self, val):
    self._attrs["showCustomTime"] = val

  @property
  def showMajorLabels(self):
    return self._attrs["showMajorLabels"]

  @showMajorLabels.setter
  def showMajorLabels(self, val):
    self._attrs["showMajorLabels"] = val

  @property
  def showMinorLabels(self):
    return self._attrs["showMinorLabels"]

  @showMinorLabels.setter
  def showMinorLabels(self, val):
    self._attrs["showMinorLabels"] = val

  @property
  def start(self):
    return self._attrs["start"]

  @start.setter
  def start(self, val):
    self._attrs["start"] = val

  @property
  def width(self):
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val

  @property
  def zoomable(self):
    return self._attrs["zoomable"]

  @zoomable.setter
  def zoomable(self, val):
    self._attrs["zoomable"] = val

  @property
  def zoomMax(self):
    return self._attrs["zoomMax"]

  @zoomMax.setter
  def zoomMax(self, val):
    self._attrs["zoomMax"] = val

  @property
  def zoomMin(self):
    return self._attrs["zoomMin"]

  @zoomMin.setter
  def zoomMin(self, val):
    self._attrs["zoomMin"] = val

  @property
  def timeAxis(self):
    return self.sub_data("timeAxis", OptionsTime)


class Options3D(DataClass):

  @property
  def animationInterval(self):
    return self._attrs["animationInterval"]

  @animationInterval.setter
  def animationInterval(self, val):
    self._attrs["animationInterval"] = val

  @property
  def animationPreload(self):
    return self._attrs["animationPreload"]

  @animationPreload.setter
  def animationPreload(self, val):
    self._attrs["animationPreload"] = val

  @property
  def animationAutoStart(self):
    return self._attrs["animationAutoStart"]

  @animationAutoStart.setter
  def animationAutoStart(self, val):
    self._attrs["animationAutoStart"] = val

  @property
  def axisColor(self):
    return self._attrs["axisColor"]

  @axisColor.setter
  def axisColor(self, val):
    self._attrs["axisColor"] = val

  @property
  def autoResize(self):
    return self._attrs["autoResize"]

  @autoResize.setter
  def autoResize(self, val):
    self._attrs["autoResize"] = val

  @property
  def backgroundColor(self):
    return self.sub_data("backgroundColor", OptionsBackgroundColor)

  @property
  def dataColor(self):
    return self.sub_data("dataColor", OptionsBackgroundColor)

  @property
  def dotSizeRatio(self):
    return self._attrs["dotSizeRatio"]

  @dotSizeRatio.setter
  def dotSizeRatio(self, val):
    self._attrs["dotSizeRatio"] = val

  @property
  def dotSizeMinFraction(self):
    return self._attrs["dotSizeMinFraction"]

  @dotSizeMinFraction.setter
  def dotSizeMinFraction(self, val):
    self._attrs["dotSizeMinFraction"] = val

  @property
  def dotSizeMaxFraction(self):
    return self._attrs["dotSizeMaxFraction"]

  @dotSizeMaxFraction.setter
  def dotSizeMaxFraction(self, val):
    self._attrs["dotSizeMaxFraction"] = val

  @property
  def gridColor(self):
    return self._attrs["gridColor"]

  @gridColor.setter
  def gridColor(self, val):
    self._attrs["gridColor"] = val

  @property
  def height(self):
    return self._attrs["height"]

  @height.setter
  def height(self, val):
    if isinstance(val, float):
      val = "%spx" % val
    self._attrs["height"] = val

  @property
  def keepAspectRatio(self):
    return self._attrs["keepAspectRatio"]

  @keepAspectRatio.setter
  def keepAspectRatio(self, val):
    self._attrs["keepAspectRatio"] = val

  @property
  def rotateAxisLabels(self):
    return self._attrs["rotateAxisLabels"]

  @rotateAxisLabels.setter
  def rotateAxisLabels(self, val):
    self._attrs["rotateAxisLabels"] = val

  @property
  def showAnimationControls(self):
    return self._attrs["showAnimationControls"]

  @showAnimationControls.setter
  def showAnimationControls(self, val):
    self._attrs["showAnimationControls"] = val

  @property
  def showGrid(self):
    return self._attrs["showGrid"]

  @showGrid.setter
  def showGrid(self, val):
    self._attrs["showGrid"] = val

  @property
  def showXAxis(self):
    return self._attrs["showXAxis"]

  @showXAxis.setter
  def showXAxis(self, val):
    self._attrs["showXAxis"] = val

  @property
  def showYAxis(self):
    return self._attrs["showYAxis"]

  @showYAxis.setter
  def showYAxis(self, val):
    self._attrs["showYAxis"] = val

  @property
  def showZAxis(self):
    return self._attrs["showZAxis"]

  @showZAxis.setter
  def showZAxis(self, val):
    self._attrs["showZAxis"] = val

  @property
  def showPerspective(self):
    return self._attrs["showPerspective"]

  @showPerspective.setter
  def showPerspective(self, val):
    self._attrs["showPerspective"] = val

  @property
  def showLegend(self):
    return self._attrs["showLegend"]

  @showLegend.setter
  def showLegend(self, val):
    self._attrs["showLegend"] = val

  @property
  def showShadow(self):
    return self._attrs["showShadow"]

  @showShadow.setter
  def showShadow(self, val):
    self._attrs["showShadow"] = val

  @property
  def style(self):
    return self._attrs["style"]

  @style.setter
  def style(self, val):
    self._attrs["style"] = val

  @property
  def tooltip(self):
    return self._attrs["tooltip"]

  @tooltip.setter
  def tooltip(self, val):
    self._attrs["tooltip"] = val

  @property
  def tooltipDelay(self):
    return self._attrs["tooltipDelay"]

  @tooltipDelay.setter
  def tooltipDelay(self, val):
    self._attrs["tooltipDelay"] = val

  @property
  def valueMax(self):
    return self._attrs["valueMax"]

  @valueMax.setter
  def valueMax(self, val):
    self._attrs["valueMax"] = val

  @property
  def valueMin(self):
    return self._attrs["valueMin"]

  @valueMin.setter
  def valueMin(self, val):
    self._attrs["valueMin"] = val

  @property
  def verticalRatio(self):
    return self._attrs["verticalRatio"]

  @verticalRatio.setter
  def verticalRatio(self, val):
    self._attrs["verticalRatio"] = val

  @property
  def width(self):
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    if isinstance(val, float):
      val = "%spx" % val
    self._attrs["width"] = val
