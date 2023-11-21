from epyk.core.html.options import Options
from typing import Any

        
class OptionColoraxisMarkerAnimation(Options):

    @property
    def duration(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(50)

    @duration.setter
    def duration(self, num: float): self._config(num, js_type=False)

        
class OptionColoraxisMarker(Options):

    @property
    def animation(self) -> 'OptionColoraxisMarkerAnimation':
        """Animation for the marker as it moves between values. """
        return self._config_sub_data("animation", OptionColoraxisMarkerAnimation)

    @property
    def color(self):
        """The color of the marker.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get("#999999")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def width(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(0.01)

    @width.setter
    def width(self, num: float): self._config(num, js_type=False)

        
class OptionColoraxisLabelsStyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#333333")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def cursor(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("default")

    @cursor.setter
    def cursor(self, text: str): self._config(text, js_type=False)

    @property
    def fontSize(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("0.8em")

    @fontSize.setter
    def fontSize(self, num: float): self._config(num, js_type=False)

        
class OptionColoraxisLabels(Options):

    @property
    def align(self):
        """What part of the string the given position is anchored to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def allowOverlap(self):
        """Whether to allow the axis labels to overlap.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @allowOverlap.setter
    def allowOverlap(self, flag: bool): self._config(flag, js_type=False)

    @property
    def autoRotation(self):
        """For horizontal axes, the allowed degrees of label rotation to prevent overlapping labels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("undefined")

    @autoRotation.setter
    def autoRotation(self, value: Any): self._config(value, js_type=False)

    @property
    def autoRotationLimit(self):
        """When each category width is more than this many pixels, we don&#39;t apply auto rotation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(80)

    @autoRotationLimit.setter
    def autoRotationLimit(self, num: float): self._config(num, js_type=False)

    @property
    def distance(self):
        """The label&#39;s pixel distance from the perimeter of the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(8)

    @distance.setter
    def distance(self, num: float): self._config(num, js_type=False)

    @property
    def enabled(self):
        """Enable or disable the axis labels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def format(self):
        """A format string for the axis label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @format.setter
    def format(self, text: str): self._config(text, js_type=False)

    @property
    def formatter(self):
        """Callback JavaScript function to format the label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @formatter.setter
    def formatter(self, value: Any): self._config(value, js_type=False)

    @property
    def maxStaggerLines(self):
        """Horizontal axis only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(5)

    @maxStaggerLines.setter
    def maxStaggerLines(self, num: float): self._config(num, js_type=False)

    @property
    def overflow(self):
        """How to handle overflowing labels on horizontal color axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get("justify")

    @overflow.setter
    def overflow(self, text: str): self._config(text, js_type=False)

    @property
    def padding(self):
        """The pixel padding for axis labels, to ensure white space between them.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(5)

    @padding.setter
    def padding(self, num: float): self._config(num, js_type=False)

    @property
    def position3d(self):
        """Defines how the labels are be repositioned according to the 3D chart orientation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Axis3DDefaults.ts
        """
        return self._config_get("offset")

    @position3d.setter
    def position3d(self, text: str): self._config(text, js_type=False)

    @property
    def reserveSpace(self):
        """Whether to reserve space for the labels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @reserveSpace.setter
    def reserveSpace(self, flag: bool): self._config(flag, js_type=False)

    @property
    def rotation(self):
        """Rotation of the labels in degrees.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(0)

    @rotation.setter
    def rotation(self, num: float): self._config(num, js_type=False)

    @property
    def skew3d(self):
        """If enabled, the axis labels will skewed to follow the perspective.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Axis3DDefaults.ts
        """
        return self._config_get(False)

    @skew3d.setter
    def skew3d(self, flag: bool): self._config(flag, js_type=False)

    @property
    def staggerLines(self):
        """Horizontal axes only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0)

    @staggerLines.setter
    def staggerLines(self, num: float): self._config(num, js_type=False)

    @property
    def step(self):
        """To show only every <em>n</em>&#39;th label on the axis, set the step to <em>n</em>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0)

    @step.setter
    def step(self, num: float): self._config(num, js_type=False)

    @property
    def style(self) -> 'OptionColoraxisLabelsStyle':
        """CSS styles for the label. """
        return self._config_sub_data("style", OptionColoraxisLabelsStyle)

    @property
    def useHTML(self):
        """Whether to <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def x(self):
        """The x position offset of all labels relative to the tick positions on the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The y position offset of all labels relative to the tick positions on the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

    @property
    def zIndex(self):
        """The Z index for the axis labels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(7)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)

        
class OptionColoraxisAccessibility(Options):

    @property
    def description(self):
        """Description for an axis to expose to screen reader users.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @description.setter
    def description(self, text: str): self._config(text, js_type=False)

    @property
    def enabled(self):
        """Enable axis accessibility features, including axis information in the screen reader information region.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def rangeDescription(self):
        """Range description for an axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @rangeDescription.setter
    def rangeDescription(self, text: str): self._config(text, js_type=False)

        
class OptionColoraxisDataclasses(Options):

    @property
    def color(self):
        """The color of each data class.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(None)

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def from_(self):
        """The start of the value range that the data class represents, relating to the point value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(None)

    @from_.setter
    def from_(self, num: float): self._config(num, js_type=False)

    @property
    def name(self):
        """The name of the data class as it appears in the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(None)

    @name.setter
    def name(self, text: str): self._config(text, js_type=False)

    @property
    def to(self):
        """The end of the value range that the data class represents, relating to the point value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(None)

    @to.setter
    def to(self, num: float): self._config(num, js_type=False)

        
class OptionColoraxisEvents(Options):

    @property
    def afterSetExtremes(self):
        """As opposed to the <code>setExtremes</code> event, this event fires after the final min and max values are computed and corrected for <code>minRange</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @afterSetExtremes.setter
    def afterSetExtremes(self, value: Any): self._config(value, js_type=False)

    @property
    def legendItemClick(self):
        """Fires when the legend item belonging to the colorAxis is clicked.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(None)

    @legendItemClick.setter
    def legendItemClick(self, value: Any): self._config(value, js_type=False)

    @property
    def pointBreakOut(self):
        """An event fired when a point is outside a break after zoom.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @pointBreakOut.setter
    def pointBreakOut(self, value: Any): self._config(value, js_type=False)

    @property
    def setExtremes(self):
        """Fires when the minimum and maximum is set for the axis, either by calling the <code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @setExtremes.setter
    def setExtremes(self, value: Any): self._config(value, js_type=False)

        
class OptionColoraxis(Options):

    @property
    def accessibility(self) -> 'OptionColoraxisAccessibility':
        """Accessibility options for an axis. """
        return self._config_sub_data("accessibility", OptionColoraxisAccessibility)

    @property
    def angle(self):
        """In a polar chart, this is the angle of the Y axis in degrees, where 0 is up and 90 is right.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/RadialAxis.ts
        """
        return self._config_get(0)

    @angle.setter
    def angle(self, num: float): self._config(num, js_type=False)

    @property
    def ceiling(self):
        """The highest allowed value for automatically computed axis extremes.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @ceiling.setter
    def ceiling(self, num: float): self._config(num, js_type=False)

    @property
    def className(self):
        """A class name that opens for styling the axis by CSS, especially in Highcharts styled mode.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def crossing(self):
        """The value on a perpendicular axis where this axis should cross.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @crossing.setter
    def crossing(self, num: float): self._config(num, js_type=False)

    @property
    def dataClassColor(self):
        """Determines how to set each data class&#39; color if no individual color is set.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get("tween")

    @dataClassColor.setter
    def dataClassColor(self, text: str): self._config(text, js_type=False)

    @property
    def dataClasses(self) -> 'OptionColoraxisDataclasses':
        """An array of data classes or ranges for the choropleth map. """
        return self._config_sub_data("dataClasses", OptionColoraxisDataclasses)

    @property
    def endOnTick(self):
        """Whether to force the axis to end on a tick.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(True)

    @endOnTick.setter
    def endOnTick(self, flag: bool): self._config(flag, js_type=False)

    @property
    def events(self) -> 'OptionColoraxisEvents':
        """Event handlers for the axis. """
        return self._config_sub_data("events", OptionColoraxisEvents)

    @property
    def floor(self):
        """The lowest allowed value for automatically computed axis extremes.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @floor.setter
    def floor(self, num: float): self._config(num, js_type=False)

    @property
    def gridLineColor(self):
        """Color of the grid lines extending from the axis across the gradient.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get("#ffffff")

    @gridLineColor.setter
    def gridLineColor(self, text: str): self._config(text, js_type=False)

    @property
    def gridLineDashStyle(self):
        """The dash or dot style of the grid lines.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("Solid")

    @gridLineDashStyle.setter
    def gridLineDashStyle(self, text: str): self._config(text, js_type=False)

    @property
    def gridLineInterpolation(self):
        """Polar charts only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/RadialAxis.ts
        """
        return self._config_get(None)

    @gridLineInterpolation.setter
    def gridLineInterpolation(self, value: Any): self._config(value, js_type=False)

    @property
    def gridLineWidth(self):
        """The width of the grid lines extending from the axis across the gradient of a scalar color axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(1)

    @gridLineWidth.setter
    def gridLineWidth(self, num: float): self._config(num, js_type=False)

    @property
    def gridZIndex(self):
        """The Z index of the grid lines.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(1)

    @gridZIndex.setter
    def gridZIndex(self, num: float): self._config(num, js_type=False)

    @property
    def id(self):
        """An id for the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @id.setter
    def id(self, text: str): self._config(text, js_type=False)

    @property
    def labels(self) -> 'OptionColoraxisLabels':
        """The axis labels show the number for each tick. """
        return self._config_sub_data("labels", OptionColoraxisLabels)

    @property
    def layout(self):
        """The layout of the color axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(None)

    @layout.setter
    def layout(self, text: str): self._config(text, js_type=False)

    @property
    def lineColor(self):
        """The color of the line marking the axis itself.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#333333")

    @lineColor.setter
    def lineColor(self, text: str): self._config(text, js_type=False)

    @property
    def margin(self):
        """If there are multiple axes on the same side of the chart, the pixel margin between the axes.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @margin.setter
    def margin(self, num: float): self._config(num, js_type=False)

    @property
    def marker(self) -> 'OptionColoraxisMarker':
        """The triangular marker on a scalar color axis that points to the value of the hovered area. """
        return self._config_sub_data("marker", OptionColoraxisMarker)

    @property
    def max(self):
        """The maximum value of the axis in terms of map point values.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def maxColor(self):
        """The color to represent the maximum of the color axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get("#0022ff")

    @maxColor.setter
    def maxColor(self, text: str): self._config(text, js_type=False)

    @property
    def maxPadding(self):
        """Padding of the max value relative to the length of the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(0)

    @maxPadding.setter
    def maxPadding(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value of the axis in terms of map point values.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def minColor(self):
        """The color to represent the minimum of the color axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get("#e6e9ff")

    @minColor.setter
    def minColor(self, text: str): self._config(text, js_type=False)

    @property
    def minorGridLineColor(self):
        """Color of the minor, secondary grid lines.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#f2f2f2")

    @minorGridLineColor.setter
    def minorGridLineColor(self, text: str): self._config(text, js_type=False)

    @property
    def minorGridLineDashStyle(self):
        """The dash or dot style of the minor grid lines.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("Solid")

    @minorGridLineDashStyle.setter
    def minorGridLineDashStyle(self, text: str): self._config(text, js_type=False)

    @property
    def minorGridLineWidth(self):
        """Width of the minor, secondary grid lines.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(1)

    @minorGridLineWidth.setter
    def minorGridLineWidth(self, num: float): self._config(num, js_type=False)

    @property
    def minorTickColor(self):
        """Color for the minor tick marks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#999999")

    @minorTickColor.setter
    def minorTickColor(self, text: str): self._config(text, js_type=False)

    @property
    def minorTickInterval(self):
        """Specific tick interval in axis units for the minor ticks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @minorTickInterval.setter
    def minorTickInterval(self, num: float): self._config(num, js_type=False)

    @property
    def minorTickLength(self):
        """The pixel length of the minor tick marks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(2)

    @minorTickLength.setter
    def minorTickLength(self, num: float): self._config(num, js_type=False)

    @property
    def minorTickPosition(self):
        """The position of the minor tick marks relative to the axis line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("outside")

    @minorTickPosition.setter
    def minorTickPosition(self, text: str): self._config(text, js_type=False)

    @property
    def minorTicks(self):
        """Enable or disable minor ticks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @minorTicks.setter
    def minorTicks(self, flag: bool): self._config(flag, js_type=False)

    @property
    def minorTicksPerMajor(self):
        """The number of minor ticks per major tick.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(5)

    @minorTicksPerMajor.setter
    def minorTicksPerMajor(self, num: float): self._config(num, js_type=False)

    @property
    def minorTickWidth(self):
        """The pixel width of the minor tick mark.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0)

    @minorTickWidth.setter
    def minorTickWidth(self, num: float): self._config(num, js_type=False)

    @property
    def minPadding(self):
        """Padding of the min value relative to the length of the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(0)

    @minPadding.setter
    def minPadding(self, num: float): self._config(num, js_type=False)

    @property
    def panningEnabled(self):
        """Whether to pan axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @panningEnabled.setter
    def panningEnabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def reversed(self):
        """Whether to reverse the axis so that the highest number is closest to the origin.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(None)

    @reversed.setter
    def reversed(self, flag: bool): self._config(flag, js_type=False)

    @property
    def showFirstLabel(self):
        """Whether to show the first tick label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @showFirstLabel.setter
    def showFirstLabel(self, flag: bool): self._config(flag, js_type=False)

    @property
    def showInLegend(self):
        """Whether to display the colorAxis in the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(True)

    @showInLegend.setter
    def showInLegend(self, flag: bool): self._config(flag, js_type=False)

    @property
    def showLastLabel(self):
        """Whether to show the last tick label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @showLastLabel.setter
    def showLastLabel(self, flag: bool): self._config(flag, js_type=False)

    @property
    def softMax(self):
        """A soft maximum for the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @softMax.setter
    def softMax(self, num: float): self._config(num, js_type=False)

    @property
    def softMin(self):
        """A soft minimum for the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @softMin.setter
    def softMin(self, num: float): self._config(num, js_type=False)

    @property
    def startOfWeek(self):
        """For datetime axes, this decides where to put the tick between weeks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(1)

    @startOfWeek.setter
    def startOfWeek(self, num: float): self._config(num, js_type=False)

    @property
    def startOnTick(self):
        """Whether to force the axis to start on a tick.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(True)

    @startOnTick.setter
    def startOnTick(self, flag: bool): self._config(flag, js_type=False)

    @property
    def stops(self):
        """Color stops for the gradient of a scalar color axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(None)

    @stops.setter
    def stops(self, value: Any): self._config(value, js_type=False)

    @property
    def tickAmount(self):
        """The amount of ticks to draw on the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @tickAmount.setter
    def tickAmount(self, num: float): self._config(num, js_type=False)

    @property
    def tickColor(self):
        """Color for the main tick marks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#333333")

    @tickColor.setter
    def tickColor(self, text: str): self._config(text, js_type=False)

    @property
    def tickInterval(self):
        """The interval of the tick marks in axis units.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(None)

    @tickInterval.setter
    def tickInterval(self, num: float): self._config(num, js_type=False)

    @property
    def tickLength(self):
        """The pixel length of the main tick marks on the color axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(5)

    @tickLength.setter
    def tickLength(self, num: float): self._config(num, js_type=False)

    @property
    def tickmarkPlacement(self):
        """For categorized axes only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("between")

    @tickmarkPlacement.setter
    def tickmarkPlacement(self, text: str): self._config(text, js_type=False)

    @property
    def tickPixelInterval(self):
        """If <a href="#colorAxis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get(72)

    @tickPixelInterval.setter
    def tickPixelInterval(self, num: float): self._config(num, js_type=False)

    @property
    def tickPosition(self):
        """The position of the major tick marks relative to the axis line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("outside")

    @tickPosition.setter
    def tickPosition(self, text: str): self._config(text, js_type=False)

    @property
    def tickPositioner(self):
        """A callback function returning array defining where the ticks are laid out on the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @tickPositioner.setter
    def tickPositioner(self, value: Any): self._config(value, js_type=False)

    @property
    def tickPositions(self):
        """An array defining where the ticks are laid out on the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @tickPositions.setter
    def tickPositions(self, value: Any): self._config(value, js_type=False)

    @property
    def tickWidth(self):
        """The pixel width of the major tick marks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @tickWidth.setter
    def tickWidth(self, value: Any): self._config(value, js_type=False)

    @property
    def type(self):
        """The type of interpolation to use for the color axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Color/ColorAxisDefaults.ts
        """
        return self._config_get("linear")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

    @property
    def uniqueNames(self):
        """Applies only when the axis <code>type</code> is <code>category</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @uniqueNames.setter
    def uniqueNames(self, flag: bool): self._config(flag, js_type=False)

    @property
    def units(self):
        """Datetime axis only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @units.setter
    def units(self, value: Any): self._config(value, js_type=False)

    @property
    def visible(self):
        """Whether axis, including axis title, line, ticks and labels, should be visible.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @visible.setter
    def visible(self, flag: bool): self._config(flag, js_type=False)

    @property
    def zIndex(self):
        """The Z index for the axis group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(2)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)
