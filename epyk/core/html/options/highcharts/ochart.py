from epyk.core.html.options import Options
from typing import Any
from epyk.core.js import JsUtils
from epyk.core.py import types as etypes

        
class OptionChartZoomingResetbuttonTheme(Options):

    @property
    def zIndex(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(6)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)

        
class OptionChartZoomingResetbuttonPosition(Options):

    @property
    def align(self):
        """The horizontal alignment of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("right")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def verticalAlign(self):
        """The vertical alignment of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("top")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """The horizontal offset of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(-10)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The vertical offset of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(10)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionChartZoomingResetbutton(Options):

    @property
    def position(self) -> 'OptionChartZoomingResetbuttonPosition':
        """The position of the button. """
        return self._config_sub_data("position", OptionChartZoomingResetbuttonPosition)

    @property
    def relativeTo(self):
        """What frame the button placement should be related to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("plot")

    @relativeTo.setter
    def relativeTo(self, text: str): self._config(text, js_type=False)

    @property
    def theme(self) -> 'OptionChartZoomingResetbuttonTheme':
        """A collection of attributes for the button. """
        return self._config_sub_data("theme", OptionChartZoomingResetbuttonTheme)

        
class OptionChartZoomingMousewheel(Options):

    @property
    def enabled(self):
        """Zooming with the mouse wheel can be disabled by setting this option to <code>false</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/MouseWheelZoom/MouseWheelZoom.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def sensitivity(self):
        """Adjust the sensitivity of the zoom.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/MouseWheelZoom/MouseWheelZoom.ts
        """
        return self._config_get(1.1)

    @sensitivity.setter
    def sensitivity(self, num: float): self._config(num, js_type=False)

    @property
    def type(self):
        """Decides in what dimensions the user can zoom scrolling the wheel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/MouseWheelZoom/MouseWheelZoom.ts
        """
        return self._config_get("undefined")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

        
class OptionChartZooming(Options):

    @property
    def key(self):
        """Set a key to hold when dragging to zoom the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("undefined")

    @key.setter
    def key(self, value: Any): self._config(value, js_type=False)

    @property
    def mouseWheel(self) -> 'OptionChartZoomingMousewheel':
        """The mouse wheel zoom is a feature included in Highcharts Stock, but is also available for Highcharts Core as a module. """
        return self._config_sub_data("mouseWheel", OptionChartZoomingMousewheel)

    @property
    def pinchType(self):
        """Equivalent to <a href="#chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("undefined")

    @pinchType.setter
    def pinchType(self, text: str): self._config(text, js_type=False)

    @property
    def resetButton(self) -> 'OptionChartZoomingResetbutton':
        """The button that appears after a selection zoom, allowing the user to reset zoom. """
        return self._config_sub_data("resetButton", OptionChartZoomingResetbutton)

    @property
    def singleTouch(self):
        """Enables zooming by a single touch, in combination with <a href="#chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(False)

    @singleTouch.setter
    def singleTouch(self, flag: bool): self._config(flag, js_type=False)

    @property
    def type(self):
        """Decides in what dimensions the user can zoom by dragging the mouse.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("undefined")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

        
class OptionChartScrollableplotarea(Options):

    @property
    def minHeight(self):
        """The minimum height for the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ScrollablePlotArea.ts
        """
        return self._config_get(None)

    @minHeight.setter
    def minHeight(self, num: float): self._config(num, js_type=False)

    @property
    def minWidth(self):
        """The minimum width for the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ScrollablePlotArea.ts
        """
        return self._config_get(None)

    @minWidth.setter
    def minWidth(self, num: float): self._config(num, js_type=False)

    @property
    def opacity(self):
        """The opacity of mask applied on one of the sides of the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ScrollablePlotArea.ts
        """
        return self._config_get(0.85)

    @opacity.setter
    def opacity(self, num: float): self._config(num, js_type=False)

    @property
    def scrollPositionX(self):
        """The initial scrolling position of the scrollable plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ScrollablePlotArea.ts
        """
        return self._config_get(None)

    @scrollPositionX.setter
    def scrollPositionX(self, num: float): self._config(num, js_type=False)

    @property
    def scrollPositionY(self):
        """The initial scrolling position of the scrollable plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ScrollablePlotArea.ts
        """
        return self._config_get(None)

    @scrollPositionY.setter
    def scrollPositionY(self, num: float): self._config(num, js_type=False)

        
class OptionChartResetzoombuttonTheme(Options):

    @property
    def zIndex(self):
        """zIndex of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)

        
class OptionChartResetzoombuttonPosition(Options):

    @property
    def align(self):
        """The horizontal alignment of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @align.setter
    def align(self, num: float): self._config(num, js_type=False)

    @property
    def verticalAlign(self):
        """The vertical alignment of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """The horizontal offset of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The vertical offset of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionChartResetzoombutton(Options):

    @property
    def position(self) -> 'OptionChartResetzoombuttonPosition':
        """The position of the button. """
        return self._config_sub_data("position", OptionChartResetzoombuttonPosition)

    @property
    def relativeTo(self):
        """What frame the button placement should be related to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @relativeTo.setter
    def relativeTo(self, text: str): self._config(text, js_type=False)

    @property
    def theme(self) -> 'OptionChartResetzoombuttonTheme':
        """A collection of attributes for the button. """
        return self._config_sub_data("theme", OptionChartResetzoombuttonTheme)

        
class OptionChartParallelaxesTitle(Options):

    @property
    def textAlign(self):
        """Alignment of the text, can be <code>&quot;left&quot;</code>, <code>&quot;right&quot;</code> or <code>&quot;center&quot;</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @textAlign.setter
    def textAlign(self, text: str): self._config(text, js_type=False)

        
class OptionChartParallelaxesStackshadow(Options):

    @property
    def borderColor(self):
        """The color of the <code>stackShadow</code> border.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Pictorial/PictorialSeries.ts
        """
        return self._config_get("transparent")

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderWidth(self):
        """The width of the <code>stackShadow</code> border.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Pictorial/PictorialSeries.ts
        """
        return self._config_get(0)

    @borderWidth.setter
    def borderWidth(self, num: float): self._config(num, js_type=False)

    @property
    def color(self):
        """The color of the <code>stackShadow</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Pictorial/PictorialSeries.ts
        """
        return self._config_get("#dedede")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def enabled(self):
        """Enable or disable <code>stackShadow</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Pictorial/PictorialSeries.ts
        """
        return self._config_get(None)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

        
class OptionChartParallelaxesLabelsStyle(Options):

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

        
class OptionChartParallelaxesLabels(Options):

    @property
    def align(self):
        """What part of the string the given position is anchored to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ParallelCoordinates/ParallelCoordinatesDefaults.ts
        """
        return self._config_get("center")

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

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(15)

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
        """How to handle overflowing labels on horizontal axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
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

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ParallelCoordinates/ParallelCoordinatesDefaults.ts
        """
        return self._config_get(False)

    @reserveSpace.setter
    def reserveSpace(self, flag: bool): self._config(flag, js_type=False)

    @property
    def rotation(self):
        """Rotation of the labels in degrees.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
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
    def style(self) -> 'OptionChartParallelaxesLabelsStyle':
        """CSS styles for the label. """
        return self._config_sub_data("style", OptionChartParallelaxesLabelsStyle)

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

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ParallelCoordinates/ParallelCoordinatesDefaults.ts
        """
        return self._config_get(0)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The y position offset of all labels relative to the tick positions on the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ParallelCoordinates/ParallelCoordinatesDefaults.ts
        """
        return self._config_get(4)

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

        
class OptionChartParallelaxesAccessibility(Options):

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

        
class OptionChartParallelaxesDatetimelabelformatsDay(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%e %b")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionChartParallelaxesDatetimelabelformatsHour(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%H:%M")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

    @property
    def range(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @range.setter
    def range(self, flag: bool): self._config(flag, js_type=False)

        
class OptionChartParallelaxesCrosshair(Options):

    @property
    def className(self):
        """A class name for the crosshair, especially as a hook for styling.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def color(self):
        """The color of the crosshair.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#cccccc")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def dashStyle(self):
        """The dash style for the crosshair.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("Solid")

    @dashStyle.setter
    def dashStyle(self, text: str): self._config(text, js_type=False)

    @property
    def snap(self):
        """Whether the crosshair should snap to the point or follow the pointer independent of points.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @snap.setter
    def snap(self, flag: bool): self._config(flag, js_type=False)

    @property
    def width(self):
        """The pixel width of the crosshair.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(1)

    @width.setter
    def width(self, num: float): self._config(num, js_type=False)

    @property
    def zIndex(self):
        """The Z index of the crosshair.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(2)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)

        
class OptionChartParallelaxesEvents(Options):

    @property
    def afterBreaks(self):
        """An event fired after the breaks have rendered.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @afterBreaks.setter
    def afterBreaks(self, value: Any): self._config(value, js_type=False)

    @property
    def afterSetExtremes(self):
        """As opposed to the <code>setExtremes</code> event, this event fires after the final min and max values are computed and corrected for <code>minRange</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @afterSetExtremes.setter
    def afterSetExtremes(self, value: Any): self._config(value, js_type=False)

    @property
    def pointBreak(self):
        """An event fired when a break from this axis occurs on a point.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @pointBreak.setter
    def pointBreak(self, value: Any): self._config(value, js_type=False)

    @property
    def pointBreakOut(self):
        """An event fired when a point is outside a break after zoom.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @pointBreakOut.setter
    def pointBreakOut(self, value: Any): self._config(value, js_type=False)

    @property
    def pointInBreak(self):
        """An event fired when a point falls inside a break from this axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @pointInBreak.setter
    def pointInBreak(self, value: Any): self._config(value, js_type=False)

    @property
    def setExtremes(self):
        """Fires when the minimum and maximum is set for the axis, either by calling the <code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @setExtremes.setter
    def setExtremes(self, value: Any): self._config(value, js_type=False)

        
class OptionChartParallelaxes(Options):

    @property
    def accessibility(self) -> 'OptionChartParallelaxesAccessibility':
        """Accessibility options for an axis. """
        return self._config_sub_data("accessibility", OptionChartParallelaxesAccessibility)

    @property
    def alignTicks(self):
        """When using multiple axis, the ticks of two or more opposite axes will automatically be aligned by adding ticks to the axis or axes with the least ticks, as if <code>tickAmount</code> were specified.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @alignTicks.setter
    def alignTicks(self, flag: bool): self._config(flag, js_type=False)

    @property
    def allowDecimals(self):
        """Whether to allow decimals in this axis&#39; ticks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @allowDecimals.setter
    def allowDecimals(self, flag: bool): self._config(flag, js_type=False)

    @property
    def categories(self):
        """If categories are present for the xAxis, names are used instead of numbers for that axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @categories.setter
    def categories(self, value: Any): self._config(value, js_type=False)

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
    def crosshair(self) -> 'OptionChartParallelaxesCrosshair':
        """Configure a crosshair that follows either the mouse pointer or the hovered point. """
        return self._config_sub_data("crosshair", OptionChartParallelaxesCrosshair)

    @property
    def crossing(self):
        """The value on a perpendicular axis where this axis should cross.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @crossing.setter
    def crossing(self, num: float): self._config(num, js_type=False)

    @property
    def dateTimeLabelFormats(self) -> 'OptionChartParallelaxesDatetimelabelformats':
        """For a datetime axis, the scale will automatically adjust to the appropriate unit. """
        return self._config_sub_data("dateTimeLabelFormats", OptionChartParallelaxesDatetimelabelformats)

    @property
    def endOnTick(self):
        """Whether to force the axis to end on a tick.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @endOnTick.setter
    def endOnTick(self, flag: bool): self._config(flag, js_type=False)

    @property
    def events(self) -> 'OptionChartParallelaxesEvents':
        """Event handlers for the axis. """
        return self._config_sub_data("events", OptionChartParallelaxesEvents)

    @property
    def floor(self):
        """The lowest allowed value for automatically computed axis extremes.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @floor.setter
    def floor(self, num: float): self._config(num, js_type=False)

    @property
    def gridZIndex(self):
        """The Z index of the grid lines.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(1)

    @gridZIndex.setter
    def gridZIndex(self, num: float): self._config(num, js_type=False)

    @property
    def height(self):
        """The height of the Y axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @height.setter
    def height(self, num: float): self._config(num, js_type=False)

    @property
    def labels(self) -> 'OptionChartParallelaxesLabels':
        """The axis labels show the number or category for each tick. """
        return self._config_sub_data("labels", OptionChartParallelaxesLabels)

    @property
    def left(self):
        """The left position as the horizontal axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @left.setter
    def left(self, num: float): self._config(num, js_type=False)

    @property
    def lineColor(self):
        """The color of the line marking the axis itself.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#333333")

    @lineColor.setter
    def lineColor(self, text: str): self._config(text, js_type=False)

    @property
    def lineWidth(self):
        """The width of the line marking the axis itself.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ParallelCoordinates/ParallelCoordinatesDefaults.ts
        """
        return self._config_get(1)

    @lineWidth.setter
    def lineWidth(self, num: float): self._config(num, js_type=False)

    @property
    def linkedTo(self):
        """Index of another axis that this axis is linked to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @linkedTo.setter
    def linkedTo(self, num: float): self._config(num, js_type=False)

    @property
    def margin(self):
        """If there are multiple axes on the same side of the chart, the pixel margin between the axes.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @margin.setter
    def margin(self, num: float): self._config(num, js_type=False)

    @property
    def max(self):
        """The maximum value of the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def maxPadding(self):
        """Padding of the max value relative to the length of the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0.05)

    @maxPadding.setter
    def maxPadding(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value of the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

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

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0.05)

    @minPadding.setter
    def minPadding(self, num: float): self._config(num, js_type=False)

    @property
    def minRange(self):
        """The minimum range to display on this axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @minRange.setter
    def minRange(self, num: float): self._config(num, js_type=False)

    @property
    def minTickInterval(self):
        """The minimum tick interval allowed in axis values.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @minTickInterval.setter
    def minTickInterval(self, num: float): self._config(num, js_type=False)

    @property
    def offset(self):
        """The distance in pixels from the plot area to the axis line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ParallelCoordinates/ParallelCoordinatesDefaults.ts
        """
        return self._config_get(0)

    @offset.setter
    def offset(self, num: float): self._config(num, js_type=False)

    @property
    def opposite(self):
        """Whether to display the axis on the opposite side of the normal.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @opposite.setter
    def opposite(self, flag: bool): self._config(flag, js_type=False)

    @property
    def pane(self):
        """Refers to the index in the <a href="#panes">panes</a> array.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @pane.setter
    def pane(self, num: float): self._config(num, js_type=False)

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

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @reversed.setter
    def reversed(self, flag: bool): self._config(flag, js_type=False)

    @property
    def reversedStacks(self):
        """If <code>true</code>, the first series in a stack will be drawn on top in a positive, non-reversed Y axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @reversedStacks.setter
    def reversedStacks(self, flag: bool): self._config(flag, js_type=False)

    @property
    def showEmpty(self):
        """Whether to show the axis line and title when the axis has no data.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @showEmpty.setter
    def showEmpty(self, flag: bool): self._config(flag, js_type=False)

    @property
    def showFirstLabel(self):
        """Whether to show the first tick label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @showFirstLabel.setter
    def showFirstLabel(self, flag: bool): self._config(flag, js_type=False)

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
    def stackShadow(self) -> 'OptionChartParallelaxesStackshadow':
        """Relevant only for pictorial series. """
        return self._config_sub_data("stackShadow", OptionChartParallelaxesStackshadow)

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

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @startOnTick.setter
    def startOnTick(self, flag: bool): self._config(flag, js_type=False)

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

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @tickInterval.setter
    def tickInterval(self, num: float): self._config(num, js_type=False)

    @property
    def tickLength(self):
        """The pixel length of the main tick marks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(10)

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
        """If tickInterval is <code>null</code> this option sets the approximate pixel interval of the tick marks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
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
        return self._config_get(0)

    @tickWidth.setter
    def tickWidth(self, num: float): self._config(num, js_type=False)

    @property
    def title(self) -> 'OptionChartParallelaxesTitle':
        """Titles for yAxes are taken from <a href="#xAxis. """
        return self._config_sub_data("title", OptionChartParallelaxesTitle)

    @property
    def tooltipValueFormat(self):
        """Parallel coordinates only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ParallelCoordinates/ParallelCoordinatesDefaults.ts
        """
        return self._config_get("undefined")

    @tooltipValueFormat.setter
    def tooltipValueFormat(self, text: str): self._config(text, js_type=False)

    @property
    def top(self):
        """The top position of the Y axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @top.setter
    def top(self, num: float): self._config(num, js_type=False)

    @property
    def type(self):
        """The type of axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
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
    def width(self):
        """The width as the horizontal axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @width.setter
    def width(self, num: float): self._config(num, js_type=False)

    @property
    def zIndex(self):
        """The Z index for the axis group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(2)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)

    @property
    def zoomEnabled(self):
        """Whether to zoom axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @zoomEnabled.setter
    def zoomEnabled(self, flag: bool): self._config(flag, js_type=False)

        
class OptionChartParallelaxesDatetimelabelformatsYear(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%Y")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionChartParallelaxesDatetimelabelformatsWeek(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%e %b")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionChartParallelaxesDatetimelabelformatsSecond(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%H:%M:%S")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

    @property
    def range(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @range.setter
    def range(self, flag: bool): self._config(flag, js_type=False)

        
class OptionChartParallelaxesDatetimelabelformatsMonth(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%b '%y")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionChartParallelaxesDatetimelabelformatsMinute(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%H:%M")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

    @property
    def range(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @range.setter
    def range(self, flag: bool): self._config(flag, js_type=False)

        
class OptionChartParallelaxesDatetimelabelformatsMillisecond(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%H:%M:%S.%L")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

    @property
    def range(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @range.setter
    def range(self, flag: bool): self._config(flag, js_type=False)

        
class OptionChartParallelaxesDatetimelabelformats(Options):

    @property
    def day(self) -> 'OptionChartParallelaxesDatetimelabelformatsDay':
        """. """
        return self._config_sub_data("day", OptionChartParallelaxesDatetimelabelformatsDay)

    @property
    def hour(self) -> 'OptionChartParallelaxesDatetimelabelformatsHour':
        """. """
        return self._config_sub_data("hour", OptionChartParallelaxesDatetimelabelformatsHour)

    @property
    def millisecond(self) -> 'OptionChartParallelaxesDatetimelabelformatsMillisecond':
        """. """
        return self._config_sub_data("millisecond", OptionChartParallelaxesDatetimelabelformatsMillisecond)

    @property
    def minute(self) -> 'OptionChartParallelaxesDatetimelabelformatsMinute':
        """. """
        return self._config_sub_data("minute", OptionChartParallelaxesDatetimelabelformatsMinute)

    @property
    def month(self) -> 'OptionChartParallelaxesDatetimelabelformatsMonth':
        """. """
        return self._config_sub_data("month", OptionChartParallelaxesDatetimelabelformatsMonth)

    @property
    def second(self) -> 'OptionChartParallelaxesDatetimelabelformatsSecond':
        """. """
        return self._config_sub_data("second", OptionChartParallelaxesDatetimelabelformatsSecond)

    @property
    def week(self) -> 'OptionChartParallelaxesDatetimelabelformatsWeek':
        """. """
        return self._config_sub_data("week", OptionChartParallelaxesDatetimelabelformatsWeek)

    @property
    def year(self) -> 'OptionChartParallelaxesDatetimelabelformatsYear':
        """. """
        return self._config_sub_data("year", OptionChartParallelaxesDatetimelabelformatsYear)

        
class OptionChartOptions3dFrameBack(Options):

    @property
    def color(self):
        """The color of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get("transparent")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def size(self):
        """The thickness of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(1)

    @size.setter
    def size(self, num: float): self._config(num, js_type=False)

    @property
    def visible(self):
        """Whether to display the frame.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get('Default')

    @visible.setter
    def visible(self, flag: str): self._config(flag, js_type=False)

        
class OptionChartOptions3dFrameBottom(Options):

    @property
    def color(self):
        """The color of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get("transparent")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def size(self):
        """The thickness of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(1)

    @size.setter
    def size(self, num: float): self._config(num, js_type=False)

    @property
    def visible(self):
        """Whether to display the frame.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get('Default')

    @visible.setter
    def visible(self, flag: str): self._config(flag, js_type=False)

        
class OptionChartOptions3dFrameFront(Options):

    @property
    def color(self):
        """The color of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get("transparent")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def size(self):
        """The thickness of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(1)

    @size.setter
    def size(self, num: float): self._config(num, js_type=False)

    @property
    def visible(self):
        """Whether to display the frame.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get('Default')

    @visible.setter
    def visible(self, flag: str): self._config(flag, js_type=False)

        
class OptionChartPanning(Options):

    @property
    def enabled(self):
        """Enable or disable chart panning.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(False)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def type(self):
        """Decides in what dimensions the user can pan the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("x")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

        
class OptionChartOptions3d(Options):

    @property
    def alpha(self):
        """One of the two rotation angles for the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(0)

    @alpha.setter
    def alpha(self, num: float): self._config(num, js_type=False)

    @property
    def axisLabelPosition(self):
        """Set it to <code>&quot;auto&quot;</code> to automatically move the labels to the best edge.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(None)

    @axisLabelPosition.setter
    def axisLabelPosition(self, value: Any): self._config(value, js_type=False)

    @property
    def beta(self):
        """One of the two rotation angles for the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(0)

    @beta.setter
    def beta(self, num: float): self._config(num, js_type=False)

    @property
    def depth(self):
        """The total depth of the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(100)

    @depth.setter
    def depth(self, num: float): self._config(num, js_type=False)

    @property
    def enabled(self):
        """Whether to render the chart using the 3D functionality.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(False)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def fitToPlot(self):
        """Whether the 3d box should automatically adjust to the chart plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(True)

    @fitToPlot.setter
    def fitToPlot(self, flag: bool): self._config(flag, js_type=False)

    @property
    def frame(self) -> 'OptionChartOptions3dFrame':
        """Provides the option to draw a frame around the charts by defining a bottom, front and back panel. """
        return self._config_sub_data("frame", OptionChartOptions3dFrame)

    @property
    def viewDistance(self):
        """Defines the distance the viewer is standing in front of the chart, this setting is important to calculate the perspective effect in column and scatter charts.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(25)

    @viewDistance.setter
    def viewDistance(self, num: float): self._config(num, js_type=False)

        
class OptionChartOptions3dFrameTop(Options):

    @property
    def color(self):
        """The color of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get("transparent")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def size(self):
        """The thickness of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(1)

    @size.setter
    def size(self, num: float): self._config(num, js_type=False)

    @property
    def visible(self):
        """Whether to display the frame.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get('Default')

    @visible.setter
    def visible(self, flag: str): self._config(flag, js_type=False)

        
class OptionChartOptions3dFrameSide(Options):

    @property
    def color(self):
        """The color of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get("transparent")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def size(self):
        """The thickness of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(1)

    @size.setter
    def size(self, num: float): self._config(num, js_type=False)

        
class OptionChartOptions3dFrameRight(Options):

    @property
    def color(self):
        """The color of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get("transparent")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def size(self):
        """The thickness of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(1)

    @size.setter
    def size(self, num: float): self._config(num, js_type=False)

    @property
    def visible(self):
        """Whether to display the frame.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get('Default')

    @visible.setter
    def visible(self, flag: str): self._config(flag, js_type=False)

        
class OptionChartOptions3dFrameLeft(Options):

    @property
    def color(self):
        """The color of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get("transparent")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def size(self):
        """The thickness of the panel.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(1)

    @size.setter
    def size(self, num: float): self._config(num, js_type=False)

    @property
    def visible(self):
        """Whether to display the frame.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get('Default')

    @visible.setter
    def visible(self, flag: str): self._config(flag, js_type=False)

        
class OptionChartOptions3dFrame(Options):

    @property
    def back(self) -> 'OptionChartOptions3dFrameBack':
        """The back side of the frame around a 3D chart. """
        return self._config_sub_data("back", OptionChartOptions3dFrameBack)

    @property
    def bottom(self) -> 'OptionChartOptions3dFrameBottom':
        """The bottom of the frame around a 3D chart. """
        return self._config_sub_data("bottom", OptionChartOptions3dFrameBottom)

    @property
    def front(self) -> 'OptionChartOptions3dFrameFront':
        """The front of the frame around a 3D chart. """
        return self._config_sub_data("front", OptionChartOptions3dFrameFront)

    @property
    def left(self) -> 'OptionChartOptions3dFrameLeft':
        """The left side of the frame around a 3D chart. """
        return self._config_sub_data("left", OptionChartOptions3dFrameLeft)

    @property
    def right(self) -> 'OptionChartOptions3dFrameRight':
        """The right of the frame around a 3D chart. """
        return self._config_sub_data("right", OptionChartOptions3dFrameRight)

    @property
    def side(self) -> 'OptionChartOptions3dFrameSide':
        """Note: As of v5. """
        return self._config_sub_data("side", OptionChartOptions3dFrameSide)

    @property
    def size(self):
        """General pixel thickness for the frame faces.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get(1)

    @size.setter
    def size(self, num: float): self._config(num, js_type=False)

    @property
    def top(self) -> 'OptionChartOptions3dFrameTop':
        """The top of the frame around a 3D chart. """
        return self._config_sub_data("top", OptionChartOptions3dFrameTop)

    @property
    def visible(self):
        """Whether the frames are visible.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/Chart3D.ts
        """
        return self._config_get("default")

    @visible.setter
    def visible(self, text: str): self._config(text, js_type=False)

        
class OptionChartEvents(Options):

    @property
    def addSeries(self):
        """Fires when a series is added to the chart after load time, using the <code>addSeries</code> method.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @addSeries.setter
    def addSeries(self, value: Any): self._config(value, js_type=False)

    @property
    def afterPrint(self):
        """Fires after a chart is printed through the context menu item or the <code>Chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/Exporting.ts
        """
        return self._config_get(None)

    @afterPrint.setter
    def afterPrint(self, value: Any): self._config(value, js_type=False)

    @property
    def beforePrint(self):
        """Fires before a chart is printed through the context menu item or the <code>Chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/Exporting.ts
        """
        return self._config_get(None)

    @beforePrint.setter
    def beforePrint(self, value: Any): self._config(value, js_type=False)

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """ Fires when clicking on the plot background. One parameter, event, is passed to the function, containing common event information.

        :linK: https://api.highcharts.com/highcharts/chart.events.click

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
    """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if not str_func.startswith("function(event)") and not func_ref:
            str_func = "function(event){%s}" % str_func
        self._config(str_func, js_type=True)

    def drilldown(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when a drilldown point is clicked, before the new series is added.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if not str_func.startswith("function(event)") and not func_ref:
            str_func = "function(event){%s}" % str_func
        self._config(str_func, js_type=True)

    def drillup(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Fires when drilling up from a drilldown series.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if not str_func.startswith("function(event)") and not func_ref:
            str_func = "function(event){%s}" % str_func
        self._config(str_func, js_type=True)

    @property
    def drillupall(self):
        """In a chart with multiple drilldown series, this event fires after all the series have been drilled up.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get(None)

    @drillupall.setter
    def drillupall(self, value: Any): self._config(value, js_type=False)

    @property
    def exportData(self):
        """Callback that fires while exporting data.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get(None)

    @exportData.setter
    def exportData(self, value: Any): self._config(value, js_type=False)

    @property
    def fullscreenClose(self):
        """Fires when a fullscreen is closed through the context menu item, or a fullscreen is closed on the <code>Escape</code> button click, or the <code>Chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/Fullscreen.ts
        """
        return self._config_get(None)

    @fullscreenClose.setter
    def fullscreenClose(self, value: Any): self._config(value, js_type=False)

    @property
    def fullscreenOpen(self):
        """Fires when a fullscreen is opened through the context menu item, or the <code>Chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/Fullscreen.ts
        """
        return self._config_get(None)

    @fullscreenOpen.setter
    def fullscreenOpen(self, value: Any): self._config(value, js_type=False)

    @property
    def load(self):
        """Fires when the chart is finished loading.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @load.setter
    def load(self, value: Any): self._config(value, js_type=False)

    @property
    def redraw(self):
        """Fires when the chart is redrawn, either after a call to <code>chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @redraw.setter
    def redraw(self, value: Any): self._config(value, js_type=False)

    @property
    def render(self):
        """Fires after initial load of the chart (directly after the <code>load</code> event), and after each redraw (directly after the <code>redraw</code> event).

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @render.setter
    def render(self, value: Any): self._config(value, js_type=False)

    @property
    def selection(self):
        """Fires when an area of the chart has been selected.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @selection.setter
    def selection(self, value: Any): self._config(value, js_type=False)

        
class OptionChart(Options):

    @property
    def alignThresholds(self):
        """When using multiple axes, align the thresholds.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(False)

    @alignThresholds.setter
    def alignThresholds(self, flag: bool): self._config(flag, js_type=False)

    @property
    def alignTicks(self):
        """When using multiple axes, the ticks of two or more opposite axes will automatically be aligned by adding ticks to the axis or axes with the least ticks, as if <code>tickAmount</code> were specified.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(True)

    @alignTicks.setter
    def alignTicks(self, flag: bool): self._config(flag, js_type=False)

    @property
    def allowMutatingData(self):
        """By default, (because of memory and performance reasons) the chart does not copy the data but keeps it as a reference.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(True)

    @allowMutatingData.setter
    def allowMutatingData(self, flag: bool): self._config(flag, js_type=False)

    @property
    def animation(self):
        """Set the overall animation for all chart updating.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(True)

    @animation.setter
    def animation(self, flag: bool): self._config(flag, js_type=False)

    @property
    def backgroundColor(self):
        """The background color or gradient for the outer chart area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("#ffffff")

    @backgroundColor.setter
    def backgroundColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderColor(self):
        """The color of the outer chart border.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("#334eff")

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderRadius(self):
        """The corner radius of the outer chart border.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(0)

    @borderRadius.setter
    def borderRadius(self, num: float): self._config(num, js_type=False)

    @property
    def borderWidth(self):
        """The pixel width of the outer chart border.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(0)

    @borderWidth.setter
    def borderWidth(self, num: float): self._config(num, js_type=False)

    @property
    def className(self):
        """A CSS class name to apply to the charts container <code>div</code>, allowing unique CSS styling for each chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def colorCount(self):
        """In styled mode, this sets how many colors the class names should rotate between.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(10)

    @colorCount.setter
    def colorCount(self, num: float): self._config(num, js_type=False)

    @property
    def displayErrors(self):
        """Whether to display errors on the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Debugger/Debugger.ts
        """
        return self._config_get(True)

    @displayErrors.setter
    def displayErrors(self, flag: bool): self._config(flag, js_type=False)

    @property
    def events(self) -> 'OptionChartEvents':
        """Event listeners for the chart. """
        return self._config_sub_data("events", OptionChartEvents)

    @property
    def height(self):
        """An explicit height for the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @height.setter
    def height(self, value: Any): self._config(value, js_type=False)

    @property
    def ignoreHiddenSeries(self):
        """If true, the axes will scale to the remaining visible series once one series is hidden.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(True)

    @ignoreHiddenSeries.setter
    def ignoreHiddenSeries(self, flag: bool): self._config(flag, js_type=False)

    @property
    def inverted(self):
        """Whether to invert the axes so that the x axis is vertical and y axis is horizontal.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(False)

    @inverted.setter
    def inverted(self, flag: bool): self._config(flag, js_type=False)

    @property
    def margin(self):
        """The margin between the outer edge of the chart and the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @margin.setter
    def margin(self, num: float): self._config(num, js_type=False)

    @property
    def marginBottom(self):
        """The margin between the bottom outer edge of the chart and the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @marginBottom.setter
    def marginBottom(self, num: float): self._config(num, js_type=False)

    @property
    def marginLeft(self):
        """The margin between the left outer edge of the chart and the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @marginLeft.setter
    def marginLeft(self, num: float): self._config(num, js_type=False)

    @property
    def marginRight(self):
        """The margin between the right outer edge of the chart and the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @marginRight.setter
    def marginRight(self, num: float): self._config(num, js_type=False)

    @property
    def marginTop(self):
        """The margin between the top outer edge of the chart and the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @marginTop.setter
    def marginTop(self, num: float): self._config(num, js_type=False)

    @property
    def numberFormatter(self):
        """Callback function to override the default function that formats all the numbers in the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @numberFormatter.setter
    def numberFormatter(self, value: Any): self._config(value, js_type=False)

    @property
    def options3d(self) -> 'OptionChartOptions3d':
        """Options to render charts in 3 dimensions. """
        return self._config_sub_data("options3d", OptionChartOptions3d)

    @property
    def panKey(self):
        """Allows setting a key to switch between zooming and panning.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @panKey.setter
    def panKey(self, value: Any): self._config(value, js_type=False)

    @property
    def panning(self) -> 'OptionChartPanning':
        """Allow panning in a chart. """
        return self._config_sub_data("panning", OptionChartPanning)

    @property
    def parallelAxes(self) -> 'OptionChartParallelaxes':
        """Common options for all yAxes rendered in a parallel coordinates plot. """
        return self._config_sub_data("parallelAxes", OptionChartParallelaxes)

    @property
    def parallelCoordinates(self):
        """Flag to render charts as a parallel coordinates plot.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ParallelCoordinates/ParallelCoordinatesDefaults.ts
        """
        return self._config_get(False)

    @parallelCoordinates.setter
    def parallelCoordinates(self, flag: bool): self._config(flag, js_type=False)

    @property
    def pinchType(self):
        """Equivalent to <a href="#chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("undefined")

    @pinchType.setter
    def pinchType(self, text: str): self._config(text, js_type=False)

    @property
    def plotBackgroundColor(self):
        """The background color or gradient for the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @plotBackgroundColor.setter
    def plotBackgroundColor(self, text: str): self._config(text, js_type=False)

    @property
    def plotBackgroundImage(self):
        """The URL for an image to use as the plot background.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @plotBackgroundImage.setter
    def plotBackgroundImage(self, text: str): self._config(text, js_type=False)

    @property
    def plotBorderColor(self):
        """The color of the inner chart or plot area border.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("#cccccc")

    @plotBorderColor.setter
    def plotBorderColor(self, text: str): self._config(text, js_type=False)

    @property
    def plotBorderWidth(self):
        """The pixel width of the plot area border.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(0)

    @plotBorderWidth.setter
    def plotBorderWidth(self, num: float): self._config(num, js_type=False)

    @property
    def plotShadow(self):
        """Whether to apply a drop shadow to the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(False)

    @plotShadow.setter
    def plotShadow(self, flag: bool): self._config(flag, js_type=False)

    @property
    def polar(self):
        """When true, cartesian charts like line, spline, area and column are transformed into the polar coordinate system.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(False)

    @polar.setter
    def polar(self, flag: bool): self._config(flag, js_type=False)

    @property
    def reflow(self):
        """Whether to reflow the chart to fit the width of the container div on resizing the window.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(True)

    @reflow.setter
    def reflow(self, flag: bool): self._config(flag, js_type=False)

    @property
    def renderTo(self):
        """The HTML element where the chart will be rendered.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @renderTo.setter
    def renderTo(self, text: str): self._config(text, js_type=False)

    @property
    def resetZoomButton(self) -> 'OptionChartResetzoombutton':
        """The button that appears after a selection zoom, allowing the user to reset zoom. """
        return self._config_sub_data("resetZoomButton", OptionChartResetzoombutton)

    @property
    def scrollablePlotArea(self) -> 'OptionChartScrollableplotarea':
        """Options for a scrollable plot area. """
        return self._config_sub_data("scrollablePlotArea", OptionChartScrollableplotarea)

    @property
    def selectionMarkerFill(self):
        """The background color of the marker square when selecting (zooming in on) an area of the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("rgba(51,92,173,0.25)")

    @selectionMarkerFill.setter
    def selectionMarkerFill(self, text: str): self._config(text, js_type=False)

    @property
    def shadow(self):
        """Whether to apply a drop shadow to the outer chart area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(False)

    @shadow.setter
    def shadow(self, flag: bool): self._config(flag, js_type=False)

    @property
    def showAxes(self):
        """Whether to show the axes initially.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @showAxes.setter
    def showAxes(self, flag: bool): self._config(flag, js_type=False)

    @property
    def spacing(self):
        """The distance between the outer edge of the chart and the content, like title or legend, or axis title and labels if present.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get([10, 10, 15, 10])

    @spacing.setter
    def spacing(self, value: Any): self._config(value, js_type=False)

    @property
    def spacingBottom(self):
        """The space between the bottom edge of the chart and the content (plot area, axis title and labels, title, subtitle or legend in top position).

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(15)

    @spacingBottom.setter
    def spacingBottom(self, num: float): self._config(num, js_type=False)

    @property
    def spacingLeft(self):
        """The space between the left edge of the chart and the content (plot area, axis title and labels, title, subtitle or legend in top position).

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(10)

    @spacingLeft.setter
    def spacingLeft(self, num: float): self._config(num, js_type=False)

    @property
    def spacingRight(self):
        """The space between the right edge of the chart and the content (plot area, axis title and labels, title, subtitle or legend in top position).

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(10)

    @spacingRight.setter
    def spacingRight(self, num: float): self._config(num, js_type=False)

    @property
    def spacingTop(self):
        """The space between the top edge of the chart and the content (plot area, axis title and labels, title, subtitle or legend in top position).

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(10)

    @spacingTop.setter
    def spacingTop(self, num: float): self._config(num, js_type=False)

    @property
    def style(self):
        """Additional CSS styles to apply inline to the container <code>div</code> and the root SVG.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get({"fontFamily": "Helvetica, Arial, sans-serif", "fontSize": "1rem"})

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

    @property
    def styledMode(self):
        """Whether to apply styled mode.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(False)

    @styledMode.setter
    def styledMode(self, flag: bool): self._config(flag, js_type=False)

    @property
    def type(self):
        """The default series type for the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get("line")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

    @property
    def width(self):
        """An explicit width for the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @width.setter
    def width(self, value: Any): self._config(value, js_type=False)

    @property
    def zooming(self) -> 'OptionChartZooming':
        """Chart zooming options. """
        return self._config_sub_data("zooming", OptionChartZooming)

    @property
    def zoomKey(self):
        """Set a key to hold when dragging to zoom the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/DraggablePoints/DragDropDefaults.ts
        """
        return self._config_get(None)

    @zoomKey.setter
    def zoomKey(self, value: Any): self._config(value, js_type=False)

    @property
    def zoomType(self):
        """Decides in what dimensions the user can zoom by dragging the mouse.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Chart/ChartDefaults.ts
        """
        return self._config_get(None)

    @zoomType.setter
    def zoomType(self, text: str): self._config(text, js_type=False)
