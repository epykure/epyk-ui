
from epyk.core.data.DataClass import DataClass
from epyk.core.data.DataClass import DataEnum


class EnumAlign(DataEnum):

  js_conversion = True

  def left(self):
    return self.set()

  def right(self):
    return self.set()

  def center(self):
    return self.set()


class EnumOrientation(DataEnum):

  js_conversion = True

  def top(self):
    return self.set()

  def bottom(self):
    return self.set()


class Enum3dStyles(DataEnum):
  js_conversion = True

  def bar(self):
    return self.set()

  def bar_color(self):
    return self.set("bar-color")

  def bar_size(self):
    return self.set("bar-size")

  def dot(self):
    return self.set()

  def dot_line(self):
    return self.set("dot-line")

  def dot_color(self):
    return self.set("dot-color")

  def dot_size(self):
    return self.set("dot-size")

  def line(self):
    return self.set()

  def grid(self):
    return self.set()

  def surface(self):
    return self.set()


class EnumNodeShapes(DataEnum):

  js_conversion = True

  def dot(self):
    return self.set()


class EnumPointsStyle(DataEnum):

  js_conversion = True

  def square(self):
    return self.set()

  def circle(self):
    return self.set()


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
    """
    Description:
    -----------
    The chart fill color, as an HTML color string.

    https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["fill"]

  @fill.setter
  def fill(self, val):
    self._attrs["fill"] = val

  @property
  def stroke(self):
    """
    Description:
    -----------
    The color of the chart border, as an HTML color string.

    https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["stroke"]

  @stroke.setter
  def stroke(self, val):
    self._attrs["stroke"] = val

  @property
  def strokeWidth(self):
    """
    Description:
    -----------
    The border width, in pixels.

    https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["strokeWidth"]

  @strokeWidth.setter
  def strokeWidth(self, val):
    self._attrs["strokeWidth"] = val


class OptionAxis(DataClass):

  @property
  def icon(self):
    return self._attrs["icon"]

  @icon.setter
  def icon(self, val):
    self._attrs["icon"] = val

  @property
  def left(self):
    """

    :rtype: OptionRange
    """
    return self.has_attribute(OptionRange)

  @property
  def right(self):
    """

    :rtype: OptionRange
    """
    return self.has_attribute(OptionRange)

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
  def visible(self):
    return self._attrs["visible"]

  @visible.setter
  def visible(self, val):
    self._attrs["visible"] = val


class OptionRange(DataClass):

  @property
  def min(self):
    return self._attrs["min"]

  @min.setter
  def min(self, val):
    self._attrs["min"] = val

  @property
  def max(self):
    return self._attrs["max"]

  @max.setter
  def max(self, val):
    self._attrs["max"] = val


class OptionAxisPosition(DataClass):

  @property
  def range(self):
    """

    :rtype: OptionRange
    """
    return self.has_attribute(OptionRange)


class OptionsCameraPosition(DataClass):

  @property
  def horizontal(self):
    """
    Description:
    -----------
    Value in radians. It can have any value, but is normally in the range of 0 and 2*Pi.

    https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["horizontal"]

  @horizontal.setter
  def horizontal(self, val):
    self._attrs["horizontal"] = val

  @property
  def vertical(self):
    """
    Description:
    -----------
    Value in radians between 0 and 0.5*Pi.

    https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["vertical"]

  @vertical.setter
  def vertical(self, val):
    self._attrs["vertical"] = val

  @property
  def distance(self):
    """
    Description:
    -----------
    The (normalized) distance from the camera to the center of the graph, in the range of 0.71 to 5.0.
    A larger distance puts the graph further away, making it smaller.

    https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["distance"]

  @distance.setter
  def distance(self, val):
    self._attrs["distance"] = val


class OptionsInterpolation(DataClass):

  @property
  def enabled(self):
    """
    Description:
    -----------
    Toggle the interpolation.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def parametrization(self):
    """
    Description:
    -----------
    Define the type of parametrization for the catmullRom interpolation. Example 7 shows the different parametrizations.
    The options are 'centripetal' (best results), 'chordal' and 'uniform'. Uniform is the computationally cheapest
    variant. If interpolation is disabled, linear interpolation is used.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["parametrization"]

  @parametrization.setter
  def parametrization(self, val):
    self._attrs["parametrization"] = val


class OptionContent(DataClass):

  @property
  def background(self):
    return self._attrs["background"]

  @background.setter
  def background(self, val):
    self._attrs["background"] = val

  @property
  def color(self):
    return self._attrs["color"]

  @color.setter
  def color(self, val):
    self._attrs["color"] = val

  @property
  def border(self):
    return self._attrs["border"]

  @border.setter
  def border(self, val):
    self._attrs["border"] = val

  @property
  def borderRadius(self):
    return self._attrs["borderRadius"]

  @borderRadius.setter
  def borderRadius(self, val):
    self._attrs["borderRadius"] = val

  @property
  def padding(self):
    return self._attrs["padding"]

  @padding.setter
  def padding(self, val):
    self._attrs["padding"] = val

  @property
  def boxShadow(self):
    return self._attrs["boxShadow"]

  @boxShadow.setter
  def boxShadow(self, val):
    self._attrs["boxShadow"] = val


class OptionLine(DataClass):

  @property
  def height(self):
    return self._attrs["height"]

  @height.setter
  def height(self, val):
    self._attrs["height"] = val

  @property
  def width(self):
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val

  @property
  def borderLeft(self):
    return self._attrs["borderLeft"]

  @borderLeft.setter
  def borderLeft(self, val):
    self._attrs["borderLeft"] = val


class OptionDot(DataClass):

  @property
  def height(self):
    return self._attrs["height"]

  @height.setter
  def height(self, val):
    self._attrs["height"] = val

  @height.setter
  def height(self, val):
    self._attrs["height"] = val

  @property
  def width(self):
    return self._attrs["width"]

  @property
  def border(self):
    return self._attrs["border"]

  @border.setter
  def border(self, val):
    self._attrs["border"] = val

  @property
  def borderRadius(self):
    return self._attrs["borderRadius"]

  @borderRadius.setter
  def borderRadius(self, val):
    self._attrs["borderRadius"] = val


class OptionsTooltipStyle(DataClass):

  @property
  def content(self):
    """

    :rtype: OptionContent
    """
    return self.has_attribute(OptionContent)

  @property
  def line(self):
    """

    :rtype: OptionLine
    """
    return self.has_attribute(OptionLine)

  @property
  def dot(self):
    """

    :rtype: OptionDot
    """
    return self.has_attribute(OptionDot)


class OptionsdrawPoints(DataClass):

  @property
  def enabled(self):
    """
    Description:
    -----------
    Toggles the drawing of the datapoints.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def onRender(self):
    """
    Description:
    -----------
    Defines a render function for every datapoint. If a group has no drawPoints.onRender callback,
    the graph2d drawPoints.onRender callback will be used. If neither is defined, the datapoint will be rendered
    according to the group setting of drawPoints.enabled. This callback must return true if the datapoint should be
    rendered, otherwise false.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["onRender"]

  @onRender.setter
  def onRender(self, val):
    self._attrs["onRender"] = val

  @property
  def size(self):
    """
    Description:
    -----------
    Determine the size at which the data points are drawn.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["size"]

  @size.setter
  def size(self, val):
    self._attrs["size"] = val

  @property
  def style(self):
    """

    :rtype: EnumPointsStyle
    """
    return self.has_attribute(EnumPointsStyle)


class OptionBarChart(DataClass):

  @property
  def align(self):
    """
    Description:
    -----------
    The alignment of the bars with regards to the coordinate. The options are 'left', 'right' or 'center'.

    https://visjs.github.io/vis-timeline/docs/graph2d/

    :rtype: EnumAlign
    """
    return self.has_attribute(EnumAlign)

  @property
  def sideBySide(self):
    """
    Description:
    -----------
    If two datapoints of a barchart overlap, they are drawn over eachother by default.
    If sideBySide is set to true, they will be drawn side by side, within the same width as a single bar..
    See example 10 for more information. When using groups, see example 11.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["sideBySide"]

  @sideBySide.setter
  def sideBySide(self, val):
    self._attrs["sideBySide"] = val

  @property
  def width(self):
    """
    Description:
    -----------
    The width of the bars

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val

  @property
  def minWidth(self):
    """
    Description:
    -----------
    The minimum width of the bars in pixels: by default the bars get smaller while zooming out to prevent overlap,
    this value is the minimum width of the bar. Default behavior (when minWidth is not set) is 10% of the bar width.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["minWidth"]

  @minWidth.setter
  def minWidth(self, val):
    self._attrs["minWidth"] = val


class OptionsLegendPosition(DataClass):

  @property
  def visible(self):
    """
    Description:
    -----------
    Both axis, left and right, have a corresponding legend. This toggles the visibility of the legend that is coupled
    with the left axis.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["visible"]

  @visible.setter
  def visible(self, val):
    self._attrs["visible"] = val

  @property
  def position(self):
    """
    Description:
    -----------
    Determine the position of the legend coupled to the left axis. Options are 'top-left', 'top-right',
    'bottom-left' or 'bottom-right'.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["position"]

  @position.setter
  def position(self, val):
    self._attrs["position"] = val


class OptionsLegend(DataClass):

  @property
  def enabled(self):
    """
    Description:
    -----------
    Toggle the legend.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def icons(self):
    """
    Description:
    -----------
    Show automatically generated icons on the legend.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["icons"]

  @icons.setter
  def icons(self, val):
    self._attrs["icons"] = val

  @property
  def left(self):
    """
    Description:
    -----------

    :https://visjs.github.io/vis-timeline/docs/graph2d/

    :rtype: OptionsLegendPosition
    """
    return self.has_attribute(OptionsLegendPosition)

  @property
  def right(self):
    """
    Description:
    -----------

    https://visjs.github.io/vis-timeline/docs/graph2d/

    :rtype: OptionsLegendPosition
    """
    return self.has_attribute(OptionsLegendPosition)


class Options2D(DataClass):

  @property
  def barChart(self):
    """

    :rtype: OptionBarChart
    """
    return self.has_attribute(OptionBarChart)

  @property
  def configure(self):
    """
    Description:
    -----------
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
  def defaultGroup(self):
    """
    Description:
    -----------
    This is the label for the default, ungrouped items when shown in a legend.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["defaultGroup"]

  @defaultGroup.setter
  def defaultGroup(self, val):
    self._attrs["defaultGroup"] = val

  @property
  def drawPoints(self) -> OptionsdrawPoints:
    """
    Description:
    -----------

    https://visjs.github.io/vis-timeline/docs/graph2d/

    :rtype: OptionsdrawPoints
    """
    return self.has_attribute(OptionsdrawPoints)

  @property
  def dataAxis(self) -> OptionAxis:
    """
    Description:
    -----------

    https://visjs.github.io/vis-timeline/docs/graph2d/

    :rtype: OptionAxis
    """
    return self.has_attribute(OptionAxis)

  @property
  def interpolation(self) -> OptionsInterpolation:
    """

    https://visjs.github.io/vis-timeline/docs/graph2d/

    :rtype: OptionsInterpolation
    """
    return self.has_attribute(OptionsInterpolation)

  @property
  def end(self):
    return self._attrs["end"]

  @end.setter
  def end(self, val):
    self._attrs["end"] = val

  @property
  def graphHeight(self):
    """
    Description:
    -----------
    This is the height of the graph SVG canvas.
    If it is larger than the height of the outer frame, you can drag up and down the vertical direction as well as the
    usual horizontal direction.

    https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["graphHeight"]

  @graphHeight.setter
  def graphHeight(self, val):
    self._attrs["graphHeight"] = val

  @property
  def height(self):
    """

    :return:
    """
    return self._attrs["height"]

  @height.setter
  def height(self, val):
    if isinstance(val, int):
      val = "%spx" % val
    # self.graphHeight = val
    self._attrs["height"] = val

  @property
  def legend(self) -> OptionsLegend:
    """

    :rtype: OptionsLegend
    """
    return self.has_attribute[OptionsLegend]

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
  def orientation(self) -> EnumOrientation:
    """

    :rtype: EnumOrientation
    """
    return self.has_attribute(EnumOrientation)

  @property
  def shaded(self) -> EnumOrientation:
    """

    :rtype: EnumOrientation
    """
    return self.has_attribute(EnumOrientation)

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
  def sort(self):
    return self._attrs["sort"]

  @sort.setter
  def sort(self, val):
    self._attrs["sort"] = val

  @property
  def start(self):
    return self._attrs["start"]

  @start.setter
  def start(self, val):
    self._attrs["start"] = val

  @property
  def style(self):
    return self._attrs["style"]

  @style.setter
  def style(self, val):
    self._attrs["style"] = val

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
  def timeAxis(self) -> OptionsTime:
    return self.sub_data("timeAxis", OptionsTime)

  @property
  def managed(self):
    """
    Description:
    ------------
    """
    return self.get(True)

  @managed.setter
  def managed(self, flag: bool):
    self.set(flag)


class Options3D(DataClass):

  @property
  def animationInterval(self):
    """
    Description:
    -----------
    The animation interval in milliseconds. This determines how fast the animation runs.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["animationInterval"]

  @animationInterval.setter
  def animationInterval(self, val):
    self._attrs["animationInterval"] = val

  @property
  def animationPreload(self):
    """
    Description:
    -----------
    If false, the animation frames are loaded as soon as they are requested.
    if animationPreload is true, the graph will automatically load all frames in the background, resulting in a
    smoother animation as soon as all frames are loaded. The load progress is shown on screen.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["animationPreload"]

  @animationPreload.setter
  def animationPreload(self, val):
    self._attrs["animationPreload"] = val

  @property
  def animationAutoStart(self):
    """
    Description:
    -----------
    If true, the animation starts playing automatically after the graph is created.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["animationAutoStart"]

  @animationAutoStart.setter
  def animationAutoStart(self, val):
    self._attrs["animationAutoStart"] = val

  @property
  def axisColor(self):
    """
    Description:
    -----------
    The color of the axis lines and the text along the axis.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
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
  def backgroundColor(self) -> OptionsBackgroundColor:
    return self.sub_data("backgroundColor", OptionsBackgroundColor)

  @property
  def cameraPosition(self) -> OptionsCameraPosition:
    """

    :rtype: OptionsCameraPosition
    """
    return self.has_attribute(OptionsCameraPosition)

  @property
  def ctrlToZoom(self):
    return self._attrs["ctrlToZoom"]

  @ctrlToZoom.setter
  def ctrlToZoom(self, val):
    self._attrs["ctrlToZoom"] = val

  @property
  def dataColor(self) -> OptionsBackgroundColor:
    return self.sub_data("dataColor", OptionsBackgroundColor)

  @property
  def dotSizeRatio(self):
    """
    Description:
    -----------
    Ratio of the size of the dots with respect to the width of the graph.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["dotSizeRatio"]

  @dotSizeRatio.setter
  def dotSizeRatio(self, val):
    self._attrs["dotSizeRatio"] = val

  @property
  def dotSizeMinFraction(self):
    """
    Description:
    -----------
    Size of minimum-value dot as a fraction of dotSizeRatio. Applicable when using style dot-size.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["dotSizeMinFraction"]

  @dotSizeMinFraction.setter
  def dotSizeMinFraction(self, val):
    self._attrs["dotSizeMinFraction"] = val

  @property
  def dotSizeMaxFraction(self):
    """
    Description:
    -----------
    Size of maximum-value dot as a fraction of dotSizeRatio. Applicable when using style dot-size.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["dotSizeMaxFraction"]

  @dotSizeMaxFraction.setter
  def dotSizeMaxFraction(self, val):
    self._attrs["dotSizeMaxFraction"] = val

  @property
  def filterLabel(self):
    return self._attrs["filterLabel"]

  @filterLabel.setter
  def filterLabel(self, val):
    self._attrs["filterLabel"] = val

  @property
  def gridColor(self):
    """
    Description:
    -----------
    The color of the grid lines.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["gridColor"]

  @gridColor.setter
  def gridColor(self, val):
    self._attrs["gridColor"] = val

  @property
  def height(self):
    """
    Description:
    -----------
    The height of the graph in pixels or as a percentage.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["height"]

  @height.setter
  def height(self, val):
    if isinstance(val, float):
      val = "%spx" % val
    self._attrs["height"] = val

  @property
  def keepAspectRatio(self):
    """
    Description:
    -----------
    If keepAspectRatio is true, the x-axis and the y-axis keep their aspect ratio.
    If false, the axes are scaled such that they both have the same, maximum width.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["keepAspectRatio"]

  @keepAspectRatio.setter
  def keepAspectRatio(self, val):
    self._attrs["keepAspectRatio"] = val

  @property
  def rotateAxisLabels(self):
    """
    Description:
    -----------
    If rotateAxisLabels is true, the x-axis and y-axis labels will rotate with the graph. Useful with long label values.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["rotateAxisLabels"]

  @rotateAxisLabels.setter
  def rotateAxisLabels(self, val):
    self._attrs["rotateAxisLabels"] = val

  @property
  def showAnimationControls(self):
    """
    Description:
    -----------
    If true, animation controls are created at the bottom of the Graph.
    The animation controls consists of buttons previous, start/stop, next, and a slider showing the current frame.
    Only applicable when the provided data contains an animation.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["showAnimationControls"]

  @showAnimationControls.setter
  def showAnimationControls(self, val):
    self._attrs["showAnimationControls"] = val

  @property
  def showGrayBottom(self):
    """
    Description:
    -----------
    If true, draw the bottom side of the surface in gray.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["showGrayBottom"]

  @showGrayBottom.setter
  def showGrayBottom(self, val):
    self._attrs["showGrayBottom"] = val

  @property
  def showGrid(self):
    """
    Description:
    -----------
    If true, grid lines are drawn in the x-y surface (the bottom of the 3d graph).

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["showGrid"]

  @showGrid.setter
  def showGrid(self, val):
    self._attrs["showGrid"] = val

  @property
  def showXAxis(self):
    """
    Description:
    -----------
    If true, X axis and X axis labels are drawn

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["showXAxis"]

  @showXAxis.setter
  def showXAxis(self, val):
    self._attrs["showXAxis"] = val

  @property
  def showYAxis(self):
    """
    Description:
    -----------
    If true, Y axis and Y axis labels are drawn.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["showYAxis"]

  @showYAxis.setter
  def showYAxis(self, val):
    self._attrs["showYAxis"] = val

  @property
  def showZAxis(self):
    """
    Description:
    -----------
    If true, Z axis and Z axis labels are drawn.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["showZAxis"]

  @showZAxis.setter
  def showZAxis(self, val):
    self._attrs["showZAxis"] = val

  @property
  def showPerspective(self):
    """
    Description:
    -----------
    If true, the graph is drawn in perspective: points and lines which are further away are drawn smaller.
    Note that the graph currently does not support a gray colored bottom side when drawn in perspective.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["showPerspective"]

  @showPerspective.setter
  def showPerspective(self, val):
    self._attrs["showPerspective"] = val

  @property
  def showLegend(self):
    """
    Description:
    -----------
    If true, a legend is drawn for the graph (if the graph type supports it).
    By default a legend is drawn for dot and dot-color style graphs.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["showLegend"]

  @showLegend.setter
  def showLegend(self, val):
    self._attrs["showLegend"] = val

  @property
  def showShadow(self):
    """
    Description:
    -----------
    Show shadow on the graph.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["showShadow"]

  @showShadow.setter
  def showShadow(self, val):
    self._attrs["showShadow"] = val

  @property
  def showSurfaceGrid(self):
    """
    Description:
    -----------
    If true, grid lines are drawn on the surface of the graph itself (only effective if style: 'surface'.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["showSurfaceGrid"]

  @showSurfaceGrid.setter
  def showSurfaceGrid(self, val):
    self._attrs["showSurfaceGrid"] = val

  @property
  def style(self) -> Enum3dStyles:
    """
    Description:
    -----------
    The style of the 3d graph

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html

    :rtype: Enum3dStyles
    """
    return self.has_attribute(Enum3dStyles)

  @property
  def tooltip(self):
    """
    Description:
    -----------
    Show a tooltip showing the values of the hovered data point.
    The contents of the tooltip can be customized by providing a callback function as tooltip.
    In this case the function is called with an object containing parameters x, y, z, and data
    (the source JS object for the point) as an argument, and must return a string which may contain HTML.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["tooltip"]

  @tooltip.setter
  def tooltip(self, val):
    self._attrs["tooltip"] = val

  @property
  def tooltipDelay(self):
    """
    Description:
    -----------
    The delay time (in ms) for the tooltip to appear when the mouse cursor hovers over an x-y grid tile.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["tooltipDelay"]

  @tooltipDelay.setter
  def tooltipDelay(self, val):
    self._attrs["tooltipDelay"] = val

  @property
  def tooltipStyle(self) -> OptionsTooltipStyle:
    """

    :rtype: OptionsTooltipStyle
    """
    return self.has_attribute(OptionsTooltipStyle)

  @property
  def valueMax(self):
    """
    Description:
    -----------
    The maximum value for the value-axis. Only available in combination with the styles dot-color and dot-size.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["valueMax"]

  @valueMax.setter
  def valueMax(self, val):
    self._attrs["valueMax"] = val

  @property
  def valueMin(self):
    """
    Description:
    -----------
    The minimum value for the value-axis. Only available in combination with the styles dot-color and dot-size.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["valueMin"]

  @valueMin.setter
  def valueMin(self, val):
    self._attrs["valueMin"] = val

  @property
  def verticalRatio(self):
    """
    Description:
    -----------
    A value between 0.1 and 1.0.
    This scales the vertical size of the graph When keepAspectRatio is set to false, and verticalRatio is set to 1.0,
    the graph will be a cube.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["verticalRatio"]

  @verticalRatio.setter
  def verticalRatio(self, val):
    self._attrs["verticalRatio"] = val

  @property
  def width(self):
    """
    Description:
    -----------
    The width of the graph in pixels or as a percentage.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    if isinstance(val, float):
      val = "%spx" % val
    self._attrs["width"] = val

  @property
  def xCenter(self):
    """
    Description:
    -----------
    The horizontal center position of the graph, as a percentage or in pixels.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["xCenter"]

  @xCenter.setter
  def xCenter(self, val):
    self._attrs["xCenter"] = val

  @property
  def xMax(self):
    """
    Description:
    -----------
    The maximum value for the x-axis. If not set, the largest value for x in the data set is used.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["xMax"]

  @xMax.setter
  def xMax(self, val):
    self._attrs["xMax"] = val

  @property
  def xMin(self):
    """
    Description:
    -----------
    The minimum value for the x-axis. If not set, the smallest value for x in the data set is used.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["xMin"]

  @xMin.setter
  def xMin(self, val):
    self._attrs["xMin"] = val

  @property
  def xBarWidth(self):
    """
    Description:
    -----------
    The width of bars in x direction. By default, the width is equal to the smallest distance between the data points.
    Only applicable for styles 'bar' and 'bar-color'.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["xBarWidth"]

  @xBarWidth.setter
  def xBarWidth(self, val):
    self._attrs["xBarWidth"] = val

  @property
  def xValueLabel(self):
    """
    Description:
    -----------
    A function for custom formatting of the labels along the x-axis, for example function (x) {return (x * 100) + '%'}.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["xValueLabel"]

  @xValueLabel.setter
  def xValueLabel(self, val):
    self._attrs["xValueLabel"] = val

  @property
  def xStep(self):
    """
    Description:
    -----------
    Step size for the grid on the x-axis.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["xStep"]

  @xStep.setter
  def xStep(self, val):
    self._attrs["xStep"] = val

  @property
  def yBarWidth(self):
    """
    Description:
    -----------
    The width of bars in y direction. By default, the width is equal to the smallest distance between the data points.
    Only applicable for styles 'bar' and 'bar-color'.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["yBarWidth"]

  @yBarWidth.setter
  def yBarWidth(self, val):
    self._attrs["yBarWidth"] = val

  @property
  def yCenter(self):
    """
    Description:
    -----------
    The vertical center position of the graph, as a percentage or in pixels.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["yCenter"]

  @yCenter.setter
  def yCenter(self, val):
    self._attrs["yCenter"] = val

  @property
  def yMax(self):
    """
    Description:
    -----------
    The maximum value for the y-axis. If not set, the largest value for y in the data set is used.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["yMax"]

  @yMax.setter
  def yMax(self, val):
    self._attrs["yMax"] = val

  @property
  def yMin(self):
    """
    Description:
    -----------
    The minimum value for the y-axis. If not set, the smallest value for y in the data set is used.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["yMin"]

  @yMin.setter
  def yMin(self, val):
    self._attrs["yMin"] = val

  @property
  def yValueLabel(self):
    """
    Description:
    -----------
    A function for custom formatting of the labels along the y-axis, for example function (y) {return (y * 100) + '%'}.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["yValueLabel"]

  @yValueLabel.setter
  def yValueLabel(self, val):
    self._attrs["yValueLabel"] = val

  @property
  def yStep(self):
    """
    Description:
    -----------
    Step size for the grid on the y-axis.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["yStep"]

  @yStep.setter
  def yStep(self, val):
    self._attrs["yStep"] = val

  @property
  def zValueLabel(self):
    """
    Description:
    -----------
    A function for custom formatting of the labels along the z-axis, for example function (z) {return (z * 100) + '%'}

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["zValueLabel"]

  @zValueLabel.setter
  def zValueLabel(self, val):
    self._attrs["zValueLabel"] = val

  @property
  def zMax(self):
    """
    Description:
    -----------
    The maximum value for the z-axis. If not set, the largest value for z in the data set is used.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["zMax"]

  @zMax.setter
  def zMax(self, val):
    self._attrs["zMax"] = val

  @property
  def zMin(self):
    """
    Description:
    -----------
    The minimum value for the z-axis. If not set, the smallest value for z in the data set is used.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/index.html
    """
    return self._attrs["zMin"]

  @zMin.setter
  def zMin(self, val):
    self._attrs["zMin"] = val

  @property
  def managed(self):
    """
    Description:
    ------------
    """
    return self.get(True)

  @managed.setter
  def managed(self, flag: bool):
    self.set(flag)


class OptionsEditable(DataClass):

  @property
  def add(self):
    """
    Description:
    -----------
    If true, new items can be created by double tapping an empty space in the Timeline. See section Editing Items for
    a detailed explanation.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/
    """
    return self._attrs["add"]

  @add.setter
  def add(self, val):
    self._attrs["add"] = val

  @property
  def remove(self):
    """
    Description:
    -----------
    If true, items can be deleted by first selecting them, and then clicking the delete button on the top right of the
    item. See section Editing Items for a detailed explanation.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/
    """
    return self._attrs["remove"]

  @remove.setter
  def remove(self, val):
    self._attrs["remove"] = val

  @property
  def updateGroup(self):
    """
    Description:
    -----------
    If true, items can be dragged from one group to another. Only applicable when the Timeline has groups.
    See section Editing Items for a detailed explanation.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/
    """
    return self._attrs["updateGroup"]

  @updateGroup.setter
  def updateGroup(self, val):
    self._attrs["updateGroup"] = val

  @property
  def updateTime(self):
    """
    Description:
    -----------
    If true, items can be dragged to another moment in time. See section Editing Items for a detailed explanation.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/
    """
    return self._attrs["updateTime"]

  @updateTime.setter
  def updateTime(self, val):
    self._attrs["updateTime"] = val

  @property
  def overrideItems(self):
    """
    Description:
    -----------
    If true, item specific editable properties are overridden by timeline settings

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/
    """
    return self._attrs["overrideItems"]

  @overrideItems.setter
  def overrideItems(self, val):
    self._attrs["overrideItems"] = val


class OptionsTimeline(DataClass):

  @property
  def autoResize(self):
    """
    Description:
    -----------
    If true, the Timeline will automatically detect when its container is resized, and redraw itself accordingly.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["autoResize"]

  @autoResize.setter
  def autoResize(self, val):
    self._attrs["autoResize"] = val

  @property
  def editable(self):
    """

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/

    :rtype: OptionsEditable
    """
    return self.has_attribute(OptionsEditable)

  @editable.setter
  def editable(self, val):
    self._attrs["editable"] = val

  @property
  def end(self):
    """
    Description:
    -----------
    The initial end date for the axis of the timeline. If not provided, the latest date present in the items set is
    taken as end date.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return self._attrs["end"]

  @end.setter
  def end(self, val):
    self._attrs["end"] = val

  @property
  def clickToUse(self):
    """
    Description:
    -----------
    When a Timeline is configured to be clickToUse, it will react to mouse and touch events only when active.
    When active, a blue shadow border is displayed around the Timeline. The Timeline is set active by clicking on it,
    and is changed to inactive again by clicking outside the Timeline or by pressing the ESC key.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/
    """
    return self._attrs["clickToUse"]

  @clickToUse.setter
  def clickToUse(self, val):
    self._attrs["clickToUse"] = val

  @property
  def start(self):
    """
    Description:
    -----------
    The initial start date for the axis of the timeline. If not provided, the earliest date present in the events is
    taken as start date.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/
    """
    return self._attrs["start"]

  @start.setter
  def start(self, val):
    self._attrs["start"] = val

  @property
  def stack(self):
    """
    Description:
    -----------
    If true (default), items will be stacked on top of each other such that they do not overlap.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/
    """
    return self._attrs["stack"]

  @stack.setter
  def stack(self, val):
    self._attrs["stack"] = val

  @property
  def stackSubgroups(self):
    """
    Description:
    -----------
    If true (default), subgroups will be stacked on top of each other such that they do not overlap.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/
    """
    return self._attrs["stackSubgroups"]

  @stackSubgroups.setter
  def stackSubgroups(self, val):
    self._attrs["stackSubgroups"] = val

  @property
  def multiselect(self):
    """
    Description:
    -----------
    If true, multiple items can be selected using ctrl+click, shift+click, or by holding items.
    Only applicable when option selectable is true.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/
    """
    return self._attrs["multiselect"]

  @multiselect.setter
  def multiselect(self, val):
    self._attrs["multiselect"] = val

  @property
  def sequentialSelection(self):
    """
    Description:
    -----------
    If true, then only sequential items are allowed to be selected (no gaps) when multiselect is true

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/
    """
    return self._attrs["sequentialSelection"]

  @sequentialSelection.setter
  def sequentialSelection(self, val):
    self._attrs["sequentialSelection"] = val

  @property
  def managed(self):
    """
    Description:
    ------------
    """
    return self.get(True)

  @managed.setter
  def managed(self, flag: bool):
    self.set(flag)


class OptionLabel(DataClass):

  @property
  def enabled(self):
    """
    Description:
    -----------
    Toggle the scaling of the label on or off. If this option is not defined, it is set to true if any of the
    properties in this object are defined.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/edges.html
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def min(self):
    """
    Description:
    -----------
    The minimum font-size used for labels when scaling.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/edges.html
    """
    return self._attrs["min"]

  @min.setter
  def min(self, val):
    self._attrs["min"] = val

  @property
  def max(self):
    """
    Description:
    -----------
    The maximum font-size used for labels when scaling.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/edges.html
    """
    return self._attrs["max"]

  @max.setter
  def max(self, val):
    self._attrs["max"] = val

  @property
  def maxVisible(self):
    """
    Description:
    -----------
    When zooming in, the font is drawn larger as well.
    You can limit the perceived font size using this option.
    If set to 30, the font will never look larger than size 30 zoomed at 100%.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/edges.html
    """
    return self._attrs["maxVisible"]

  @maxVisible.setter
  def maxVisible(self, val):
    self._attrs["maxVisible"] = val

  @property
  def drawThreshold(self):
    """
    Description:
    -----------
    When zooming out, the font will be drawn smaller. This defines a lower limit for when the font is drawn.
    When using font scaling, you can use this together with the maxVisible to first show labels of important edges when
    zoomed out and only show the rest when zooming in.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/edges.html
    """
    return self._attrs["drawThreshold"]

  @drawThreshold.setter
  def drawThreshold(self, val):
    self._attrs["drawThreshold"] = val


class OptionNodeScaling(DataClass):

  @property
  def min(self):
    return self._attrs["min"]

  @min.setter
  def min(self, val):
    self._attrs["min"] = val

  @property
  def max(self):
    return self._attrs["max"]

  @max.setter
  def max(self, val):
    self._attrs["max"] = val

  @property
  def label(self) -> OptionLabel:
    """

    :rtype: OptionLabel
    """
    return self.has_attribute(OptionLabel)


class OptionFont(DataClass):

  @property
  def size(self):
    return self._attrs["size"]

  @size.setter
  def size(self, val):
    self._attrs["size"] = val

  @property
  def face(self):
    return self._attrs["face"]

  @face.setter
  def face(self, val):
    self._attrs["face"] = val


class OptionNode(DataClass):

  @property
  def shape(self) -> EnumNodeShapes:
    """

    :rtype: EnumNodeShapes
    """
    return self.has_attribute(EnumNodeShapes)

  @property
  def scaling(self) -> OptionNodeScaling:
    """

    :rtype: OptionNodeScaling
    """
    return self.has_attribute(OptionNodeScaling)

  @property
  def font(self) -> OptionFont:
    """

    :rtype: OptionFont
    """
    return self.has_attribute(OptionFont)


class OptionPhysicsBarnesHut(DataClass):

  @property
  def springLength(self):
    return self._attrs["springLength"]

  @springLength.setter
  def springLength(self, val):
    self._attrs["springLength"] = val


class OptionPhysics(DataClass):

  @property
  def stabilization(self):
    return self._attrs["stabilization"]

  @stabilization.setter
  def stabilization(self, val):
    self._attrs["stabilization"] = val

  @property
  def physics(self):
    """

    :rtype: OptionPhysicsBarnesHut
    """
    return self.has_attribute(OptionPhysicsBarnesHut)


class OptionColor(DataClass):

  @property
  def color(self):
    return self._attrs["color"]

  @color.setter
  def color(self, val):
    self._attrs["color"] = val

  @property
  def highlight(self):
    return self._attrs["highlight"]

  @highlight.setter
  def highlight(self, val):
    self._attrs["highlight"] = val

  @property
  def hover(self):
    return self._attrs["hover"]

  @hover.setter
  def hover(self, val):
    self._attrs["hover"] = val


class OptionInteraction(DataClass):

  @property
  def hover(self):
    return self._attrs["hover"]

  @hover.setter
  def hover(self, val):
    self._attrs["hover"] = val

  @property
  def hideEdgesOnDrag(self):
    return self._attrs["hideEdgesOnDrag"]

  @hideEdgesOnDrag.setter
  def hideEdgesOnDrag(self, val):
    self._attrs["hideEdgesOnDrag"] = val

  @property
  def tooltipDelay(self):
    return self._attrs["tooltipDelay"]

  @tooltipDelay.setter
  def tooltipDelay(self, val):
    self._attrs["tooltipDelay"] = val


class OptionSmooth(DataEnum):

  def continuous(self):
    return self.set()

  def cubicBezier(self):
    return self.set()


class OptionShadow(DataClass):

  @property
  def enabled(self):
    """
    Description:
    -----------
    Toggle the casting of shadows. If this option is not defined, it is set to true if any of the properties in
    this object are defined.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/edges.html
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def color(self):
    """
    Description:
    -----------
    The color size of the shadow as a string. Supported formats are 'rgb(255,255,255)', 'rgba(255,255,255,1)'
    and '#FFFFFF'.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/edges.html
    """
    return self._attrs["color"]

  @color.setter
  def color(self, val):
    self._attrs["color"] = val

  @property
  def size(self):
    """
    Description:
    -----------
    The blur size of the shadow.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/edges.html
    """
    return self._attrs["size"]

  @size.setter
  def size(self, val):
    self._attrs["size"] = val

  @property
  def x(self):
    """
    Description:
    -----------
    The x offset.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/edges.html
    """
    return self._attrs["x"]

  @x.setter
  def x(self, val):
    self._attrs["x"] = val

  @property
  def y(self):
    """
    Description:
    -----------
    The y offset.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/edges.html
    """
    return self._attrs["y"]

  @y.setter
  def y(self, val):
    self._attrs["y"] = val


class OptionEdge(DataClass):

  @property
  def color(self) -> OptionColor:
    """

    :rtype: OptionColor
    """
    return self.has_attribute(OptionColor)

  @property
  def hoverWidth(self):
    return self._attrs["hoverWidth"]

  @hoverWidth.setter
  def hoverWidth(self, val):
    self._attrs["hoverWidth"] = val

  @property
  def interaction(self) -> OptionInteraction:
    """

    :rtype: OptionInteraction
    """
    return self.has_attribute(OptionInteraction)

  @property
  def width(self):
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val

  @property
  def smooth(self) -> OptionSmooth:
    """

    :rtype: OptionSmooth
    """
    return self.has_attribute(OptionSmooth)

  @property
  def shadow(self) -> OptionShadow:
    """

    :rtype: OptionShadow
    """
    return self.has_attribute(OptionShadow)


class OPtionsHierarchical(DataClass):

  @property
  def enabled(self):
    """
    Description:
    -----------
    Toggle the usage of the hierarchical layout system.
    If this option is not defined, it is set to true if any of the properties in this object are defined.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/layout.html#
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def levelSeparation(self):
    """
    Description:
    -----------
    The distance between the different levels.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/layout.html#
    """
    return self._attrs["levelSeparation"]

  @levelSeparation.setter
  def levelSeparation(self, val):
    self._attrs["levelSeparation"] = val

  @property
  def nodeSpacing(self):
    """
    Description:
    -----------
    Minimum distance between nodes on the free axis. This is only for the initial layout.
    If you enable physics, the node distance there will be the effective node distance

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/layout.html#
    """
    return self._attrs["nodeSpacing"]

  @nodeSpacing.setter
  def nodeSpacing(self, val):
    self._attrs["nodeSpacing"] = val

  @property
  def treeSpacing(self):
    """
    Description:
    -----------
    Distance between different trees (independent networks). This is only for the initial layout.
    If you enable physics, the repulsion model will denote the distance between the trees.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/layout.html#
    """
    return self._attrs["treeSpacing"]

  @treeSpacing.setter
  def treeSpacing(self, val):
    self._attrs["treeSpacing"] = val

  @property
  def blockShifting(self):
    """
    Description:
    -----------
    Method for reducing whitespace. Can be used alone or together with edge minimization.
    Each node will check for whitespace and will shift it's branch along with it for as far as it can, respecting the nodeSpacing on any level.
    This is mainly for the initial layout. If you enable physics, the layout will be determined by the physics. This will greatly speed up the stabilization time though!

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/layout.html#
    """
    return self._attrs["blockShifting"]

  @blockShifting.setter
  def blockShifting(self, val):
    self._attrs["blockShifting"] = val

  @property
  def edgeMinimization(self):
    """
    Description:
    -----------
    Method for reducing whitespace. Can be used alone or together with block shifting.
    Enabling block shifting will usually speed up the layout process.
    Each node will try to move along its free axis to reduce the total length of it's edges.
    This is mainly for the initial layout. If you enable physics, the layout will be determined by the physics.
    This will greatly speed up the stabilization time though!

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/layout.html#
    """
    return self._attrs["edgeMinimization"]

  @edgeMinimization.setter
  def edgeMinimization(self, val):
    self._attrs["edgeMinimization"] = val

  @property
  def parentCentralization(self):
    """
    Description:
    -----------
    When true, the parents nodes will be centered again after the layout algorithm has been finished.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/layout.html#
    """
    return self._attrs["parentCentralization"]

  @parentCentralization.setter
  def parentCentralization(self, val):
    self._attrs["parentCentralization"] = val


class OptionLayout(DataClass):

  @property
  def randomSeed(self):
    """
    Description:
    -----------
    When NOT using the hierarchical layout, the nodes are randomly positioned initially.
    This means that the settled result is different every time. If you provide a random seed manually,
    the layout will be the same every time.
    Ideally you try with an undefined seed, reload until you are happy with the layout and use the getSeed() method to
    ascertain the seed.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/layout.html#
    """
    return self._attrs["randomSeed"]

  @randomSeed.setter
  def randomSeed(self, val):
    self._attrs["randomSeed"] = val

  @property
  def improvedLayout(self):
    """
    Description:
    -----------
    When enabled, the network will use the Kamada Kawai algorithm for initial layout.
    For networks larger than 100 nodes, clustering will be performed automatically to reduce the amount of nodes.
    This can greatly improve the stabilization times. If the network is very interconnected (no or few leaf nodes),
    this may not work and it will revert back to the old method. Performance will be improved in the future

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/layout.html#
    """
    return self._attrs["improvedLayout"]

  @improvedLayout.setter
  def improvedLayout(self, val):
    self._attrs["improvedLayout"] = val

  @property
  def clusterThreshold(self):
    """
    Description:
    -----------
    Cluster threshold to which improvedLayout applies.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/layout.html#
    """
    return self._attrs["clusterThreshold"]

  @clusterThreshold.setter
  def clusterThreshold(self, val):
    self._attrs["clusterThreshold"] = val

  @property
  def hierarchical(self) -> OPtionsHierarchical:
    """
    Description:
    -----------

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/layout.html#

    :rtype: OPtionsHierarchical
    """
    return self.has_attribute(OPtionsHierarchical)


class OptionManipulation(DataClass):

  @property
  def enabled(self):
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val


class OptionsNetwork(DataClass):

  @property
  def autoResize(self):
    """
    Description:
    -----------
    If true, the Network will automatically detect when its container is resized, and redraw itself accordingly.
    If false, the Network can be forced to repaint after its container has been resized using the function redraw()
    and setSize().

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/
    """
    return self._attrs["autoResize"]

  @autoResize.setter
  def autoResize(self, val):
    self._attrs["autoResize"] = val

  @property
  def width(self):
    """
    Description:
    -----------
    the width of the canvas. Can be in percentages or pixels (ie. '400px').

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/
    """
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val

  @property
  def height(self):
    """
    Description:
    -----------
    the height of the canvas. Can be in percentages or pixels (ie. '400px').

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/
    """
    return self._attrs["height"]

  @height.setter
  def height(self, val):
    self._attrs["height"] = val

  @property
  def locale(self):
    """
    Description:
    -----------
    Select the locale. By default, the language is English

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/
    """
    return self._attrs["locale"]

  @locale.setter
  def locale(self, val):
    self._attrs["locale"] = val

  @property
  def nodes(self) -> OptionNode:
    """
    Description:
    -----------
    All options in this object are explained in the nodes module.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/

    :rtype: OptionNode
    """
    return self.has_attribute(OptionNode)

  @property
  def edges(self) -> OptionEdge:
    """
    Description:
    -----------
    All options in this object are explained in the edges module.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/

    :rtype: OptionEdge
    """
    return self.has_attribute(OptionEdge)

  @property
  def layout(self) -> OptionLayout:
    """
    Description:
    -----------

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/

    All options in this object are explained in the layout module.

    :rtype: OptionLayout
    """
    return self.has_attribute(OptionLayout)

  @property
  def physics(self) -> OptionPhysics:
    """
    Description:
    -----------
    All options in this object are explained in the physics module.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/

    :rtype: OptionPhysics
    """
    return self.has_attribute(OptionPhysics)

  @property
  def interaction(self) -> OptionInteraction:
    """
    Description:
    -----------
    All options in this object are explained in the interaction module.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/

    :rtype: OptionInteraction
    """
    return self.has_attribute(OptionInteraction)

  @property
  def manipulation(self) -> OptionManipulation:
    """
    Description:
    -----------
    All options in this object are explained in the manipulation module.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/

    :rtype: OptionManipulation
    """
    return self.has_attribute(OptionManipulation)

  @property
  def managed(self):
    """
    Description:
    ------------
    """
    return self.get(True)

  @managed.setter
  def managed(self, flag: bool):
    self.set(flag)
