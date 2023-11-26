from epyk.core.html.options import Options
from typing import Any

        
class OptionXaxisTitleStyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#666666")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def fontSize(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("0.8em")

    @fontSize.setter
    def fontSize(self, num: float): self._config(num, js_type=False)

        
class OptionXaxisTitle(Options):

    @property
    def align(self):
        """Alignment of the title relative to the axis values.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("middle")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def enabled(self):
        """Deprecated.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def margin(self):
        """The pixel distance between the axis labels or line and the title.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @margin.setter
    def margin(self, num: float): self._config(num, js_type=False)

    @property
    def offset(self):
        """The distance of the axis title from the axis line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @offset.setter
    def offset(self, num: float): self._config(num, js_type=False)

    @property
    def position3d(self):
        """Defines how the title is repositioned according to the 3D chart orientation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Axis3DDefaults.ts
        """
        return self._config_get(None)

    @position3d.setter
    def position3d(self, value: Any): self._config(value, js_type=False)

    @property
    def reserveSpace(self):
        """Whether to reserve space for the title when laying out the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @reserveSpace.setter
    def reserveSpace(self, flag: bool): self._config(flag, js_type=False)

    @property
    def rotation(self):
        """The rotation of the text in degrees.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0)

    @rotation.setter
    def rotation(self, num: float): self._config(num, js_type=False)

    @property
    def skew3d(self):
        """If enabled, the axis title will skewed to follow the perspective.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/Axis3DDefaults.ts
        """
        return self._config_get(None)

    @skew3d.setter
    def skew3d(self, flag: bool): self._config(flag, js_type=False)

    @property
    def style(self) -> 'OptionXaxisTitleStyle':
        """CSS styles for the title. """
        return self._config_sub_data("style", OptionXaxisTitleStyle)

    @property
    def text(self):
        """The actual text of the axis title.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

    @property
    def textAlign(self):
        """Alignment of the text, can be <code>&quot;left&quot;</code>, <code>&quot;right&quot;</code> or <code>&quot;center&quot;</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @textAlign.setter
    def textAlign(self, text: str): self._config(text, js_type=False)

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
        """Horizontal pixel offset of the title position.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """Vertical pixel offset of the title position.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionXaxisPlotlinesLabels(Options):

    @property
    def clip(self):
        """Whether to hide labels that are outside the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(False)

    @clip.setter
    def clip(self, flag: bool): self._config(flag, js_type=False)

        
class OptionXaxisPlotlinesLabel(Options):

    @property
    def align(self):
        """Horizontal alignment of the label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get("left")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def formatter(self):
        """Callback JavaScript function to format the label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @formatter.setter
    def formatter(self, value: Any): self._config(value, js_type=False)

    @property
    def rotation(self):
        """Rotation of the text label in degrees.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @rotation.setter
    def rotation(self, num: float): self._config(num, js_type=False)

    @property
    def style(self):
        """CSS styles for the text label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

    @property
    def text(self):
        """The text itself.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

    @property
    def textAlign(self):
        """The text alignment for the label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @textAlign.setter
    def textAlign(self, text: str): self._config(text, js_type=False)

    @property
    def useHTML(self):
        """Whether to <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def verticalAlign(self):
        """Vertical alignment of the label relative to the plot line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get("top")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """Horizontal position relative the alignment.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """Vertical position of the text baseline relative to the alignment.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionXaxisPlotlinesEvents(Options):

    @property
    def click(self):
        """Click event on a plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @click.setter
    def click(self, value: Any): self._config(value, js_type=False)

    @property
    def mousemove(self):
        """Mouse move event on a plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @mousemove.setter
    def mousemove(self, value: Any): self._config(value, js_type=False)

    @property
    def mouseout(self):
        """Mouse out event on the corner of a plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @mouseout.setter
    def mouseout(self, value: Any): self._config(value, js_type=False)

    @property
    def mouseover(self):
        """Mouse over event on a plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @mouseover.setter
    def mouseover(self, value: Any): self._config(value, js_type=False)

        
class OptionXaxisPlotlines(Options):

    @property
    def className(self):
        """A custom class name, in addition to the default <code>highcharts-plot-line</code>, to apply to each individual line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def color(self):
        """The color of the line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get("#999999")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def dashStyle(self):
        """The dashing or dot style for the plot line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get("Solid")

    @dashStyle.setter
    def dashStyle(self, text: str): self._config(text, js_type=False)

    @property
    def events(self) -> 'OptionXaxisPlotlinesEvents':
        """An object defining mouse events for the plot line. """
        return self._config_sub_data("events", OptionXaxisPlotlinesEvents)

    @property
    def id(self):
        """An id used for identifying the plot line in Axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @id.setter
    def id(self, text: str): self._config(text, js_type=False)

    @property
    def label(self) -> 'OptionXaxisPlotlinesLabel':
        """Text labels for the plot bands. """
        return self._config_sub_data("label", OptionXaxisPlotlinesLabel)

    @property
    def labels(self) -> 'OptionXaxisPlotlinesLabels':
        """. """
        return self._config_sub_data("labels", OptionXaxisPlotlinesLabels)

    @property
    def value(self):
        """The position of the line in axis units.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def width(self):
        """The width or thickness of the plot line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(2)

    @width.setter
    def width(self, num: float): self._config(num, js_type=False)

    @property
    def zIndex(self):
        """The z index of the plot line within the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)

        
class OptionXaxisPlotbandsLabel(Options):

    @property
    def align(self):
        """Horizontal alignment of the label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get("center")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def rotation(self):
        """Rotation of the text label in degrees .

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(0)

    @rotation.setter
    def rotation(self, num: float): self._config(num, js_type=False)

    @property
    def style(self):
        """CSS styles for the text label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

    @property
    def text(self):
        """The string text itself.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

    @property
    def textAlign(self):
        """The text alignment for the label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @textAlign.setter
    def textAlign(self, text: str): self._config(text, js_type=False)

    @property
    def useHTML(self):
        """Whether to <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def verticalAlign(self):
        """Vertical alignment of the label relative to the plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get("top")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """Horizontal position relative the alignment.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """Vertical position of the text baseline relative to the alignment.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionXaxisPlotbandsEvents(Options):

    @property
    def click(self):
        """Click event on a plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @click.setter
    def click(self, value: Any): self._config(value, js_type=False)

    @property
    def mousemove(self):
        """Mouse move event on a plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @mousemove.setter
    def mousemove(self, value: Any): self._config(value, js_type=False)

    @property
    def mouseout(self):
        """Mouse out event on the corner of a plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @mouseout.setter
    def mouseout(self, value: Any): self._config(value, js_type=False)

    @property
    def mouseover(self):
        """Mouse over event on a plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @mouseover.setter
    def mouseover(self, value: Any): self._config(value, js_type=False)

        
class OptionXaxisPlotbands(Options):

    @property
    def borderColor(self):
        """Border color for the plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderWidth(self):
        """Border width for the plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(0)

    @borderWidth.setter
    def borderWidth(self, num: float): self._config(num, js_type=False)

    @property
    def className(self):
        """A custom class name, in addition to the default <code>highcharts-plot-band</code>, to apply to each individual band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def color(self):
        """The color of the plot band.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get("#e6e9ff")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def events(self) -> 'OptionXaxisPlotbandsEvents':
        """An object defining mouse events for the plot band. """
        return self._config_sub_data("events", OptionXaxisPlotbandsEvents)

    @property
    def from_(self):
        """The start position of the plot band in axis units.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @from_.setter
    def from_(self, num: float): self._config(num, js_type=False)

    @property
    def id(self):
        """An id used for identifying the plot band in Axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @id.setter
    def id(self, text: str): self._config(text, js_type=False)

    @property
    def label(self) -> 'OptionXaxisPlotbandsLabel':
        """Text labels for the plot bands. """
        return self._config_sub_data("label", OptionXaxisPlotbandsLabel)

    @property
    def to(self):
        """The end position of the plot band in axis units.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @to.setter
    def to(self, num: float): self._config(num, js_type=False)

    @property
    def zIndex(self):
        """The z index of the plot band within the chart, relative to other elements.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)

        
class OptionXaxisLabelsStyle(Options):

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

        
class OptionXaxisLabels(Options):

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

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

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
    def style(self) -> 'OptionXaxisLabelsStyle':
        """CSS styles for the label. """
        return self._config_sub_data("style", OptionXaxisLabelsStyle)

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

        
class OptionXaxisAccessibility(Options):

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

        
class OptionXaxisBreaks(Options):

    @property
    def breakSize(self):
        """A number indicating how much space should be left between the start and the end of the break.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0)

    @breakSize.setter
    def breakSize(self, num: float): self._config(num, js_type=False)

    @property
    def from_(self):
        """The point where the break starts.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @from_.setter
    def from_(self, num: float): self._config(num, js_type=False)

    @property
    def repeat(self):
        """Defines an interval after which the break appears again.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0)

    @repeat.setter
    def repeat(self, num: float): self._config(num, js_type=False)

    @property
    def to(self):
        """The point where the break ends.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @to.setter
    def to(self, num: float): self._config(num, js_type=False)

        
class OptionXaxisDatetimelabelformatsDay(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%e %b")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionXaxisDatetimelabelformatsHour(Options):

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

        
class OptionXaxisCrosshair(Options):

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

        
class OptionXaxisEvents(Options):

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

        
class OptionXaxis(Options):

    @property
    def accessibility(self) -> 'OptionXaxisAccessibility':
        """Accessibility options for an axis. """
        return self._config_sub_data("accessibility", OptionXaxisAccessibility)

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
    def alternateGridColor(self):
        """When using an alternate grid color, a band is painted across the plot area between every other grid line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @alternateGridColor.setter
    def alternateGridColor(self, text: str): self._config(text, js_type=False)

    @property
    def angle(self):
        """In a polar chart, this is the angle of the Y axis in degrees, where 0 is up and 90 is right.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/RadialAxis.ts
        """
        return self._config_get(0)

    @angle.setter
    def angle(self, num: float): self._config(num, js_type=False)

    @property
    def breaks(self) -> 'OptionXaxisBreaks':
        """An array defining breaks in the axis, the sections defined will be left out and all the points shifted closer to each other. """
        return self._config_sub_data("breaks", OptionXaxisBreaks)

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
    def crosshair(self) -> 'OptionXaxisCrosshair':
        """Configure a crosshair that follows either the mouse pointer or the hovered point. """
        return self._config_sub_data("crosshair", OptionXaxisCrosshair)

    @property
    def crossing(self):
        """The value on a perpendicular axis where this axis should cross.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @crossing.setter
    def crossing(self, num: float): self._config(num, js_type=False)

    @property
    def dateTimeLabelFormats(self) -> 'OptionXaxisDatetimelabelformats':
        """For a datetime axis, the scale will automatically adjust to the appropriate unit. """
        return self._config_sub_data("dateTimeLabelFormats", OptionXaxisDatetimelabelformats)

    @property
    def endOnTick(self):
        """Whether to force the axis to end on a tick.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @endOnTick.setter
    def endOnTick(self, flag: bool): self._config(flag, js_type=False)

    @property
    def events(self) -> 'OptionXaxisEvents':
        """Event handlers for the axis. """
        return self._config_sub_data("events", OptionXaxisEvents)

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
        """Color of the grid lines extending the ticks across the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#e6e6e6")

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
        """The width of the grid lines extending the ticks across the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

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
    def height(self):
        """The height as the vertical axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @height.setter
    def height(self, num: float): self._config(num, js_type=False)

    @property
    def id(self):
        """An id for the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @id.setter
    def id(self, text: str): self._config(text, js_type=False)

    @property
    def labels(self) -> 'OptionXaxisLabels':
        """The axis labels show the number or category for each tick. """
        return self._config_sub_data("labels", OptionXaxisLabels)

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

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
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
        return self._config_get(0.01)

    @maxPadding.setter
    def maxPadding(self, num: float): self._config(num, js_type=False)

    @property
    def maxZoom(self):
        """Deprecated.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @maxZoom.setter
    def maxZoom(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value of the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

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

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0.01)

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

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("undefined")

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
    def plotBands(self) -> 'OptionXaxisPlotbands':
        """An array of colored bands stretching across the plot area marking an interval on the axis. """
        return self._config_sub_data("plotBands", OptionXaxisPlotbands)

    @property
    def plotLines(self) -> 'OptionXaxisPlotlines':
        """An array of lines stretching across the plot area, marking a specific value on one of the axes. """
        return self._config_sub_data("plotLines", OptionXaxisPlotlines)

    @property
    def reversed(self):
        """Whether to reverse the axis so that the highest number is closest to the origin.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @reversed.setter
    def reversed(self, flag: bool): self._config(flag, js_type=False)

    @property
    def reversedStacks(self):
        """This option determines how stacks should be ordered within a group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

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
        return self._config_get(False)

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
        return self._config_get(100)

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
    def title(self) -> 'OptionXaxisTitle':
        """The axis title, showing next to the axis line. """
        return self._config_sub_data("title", OptionXaxisTitle)

    @property
    def top(self):
        """The top position as the vertical axis.

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

        
class OptionXaxisDatetimelabelformatsYear(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%Y")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionXaxisDatetimelabelformatsWeek(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%e %b")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionXaxisDatetimelabelformatsSecond(Options):

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

        
class OptionXaxisDatetimelabelformatsMonth(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%b '%y")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionXaxisDatetimelabelformatsMinute(Options):

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

        
class OptionXaxisDatetimelabelformatsMillisecond(Options):

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

        
class OptionXaxisDatetimelabelformats(Options):

    @property
    def day(self) -> 'OptionXaxisDatetimelabelformatsDay':
        """. """
        return self._config_sub_data("day", OptionXaxisDatetimelabelformatsDay)

    @property
    def hour(self) -> 'OptionXaxisDatetimelabelformatsHour':
        """. """
        return self._config_sub_data("hour", OptionXaxisDatetimelabelformatsHour)

    @property
    def millisecond(self) -> 'OptionXaxisDatetimelabelformatsMillisecond':
        """. """
        return self._config_sub_data("millisecond", OptionXaxisDatetimelabelformatsMillisecond)

    @property
    def minute(self) -> 'OptionXaxisDatetimelabelformatsMinute':
        """. """
        return self._config_sub_data("minute", OptionXaxisDatetimelabelformatsMinute)

    @property
    def month(self) -> 'OptionXaxisDatetimelabelformatsMonth':
        """. """
        return self._config_sub_data("month", OptionXaxisDatetimelabelformatsMonth)

    @property
    def second(self) -> 'OptionXaxisDatetimelabelformatsSecond':
        """. """
        return self._config_sub_data("second", OptionXaxisDatetimelabelformatsSecond)

    @property
    def week(self) -> 'OptionXaxisDatetimelabelformatsWeek':
        """. """
        return self._config_sub_data("week", OptionXaxisDatetimelabelformatsWeek)

    @property
    def year(self) -> 'OptionXaxisDatetimelabelformatsYear':
        """. """
        return self._config_sub_data("year", OptionXaxisDatetimelabelformatsYear)
