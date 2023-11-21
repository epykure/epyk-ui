from epyk.core.html.options import Options
from typing import Any

        
class OptionYaxisTitleStyle(Options):

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

        
class OptionYaxisTitle(Options):

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
        """The pixel distance between the axis labels and the title.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(40)

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
        return self._config_get(270)

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
    def style(self) -> 'OptionYaxisTitleStyle':
        """CSS styles for the title. """
        return self._config_sub_data("style", OptionYaxisTitleStyle)

    @property
    def text(self):
        """The actual text of the axis title.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("Values")

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

        
class OptionYaxisStackshadow(Options):

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

        
class OptionYaxisStacklabelsStyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#000000")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def fontSize(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("0.7em")

    @fontSize.setter
    def fontSize(self, num: float): self._config(num, js_type=False)

    @property
    def fontWeight(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("bold")

    @fontWeight.setter
    def fontWeight(self, text: str): self._config(text, js_type=False)

    @property
    def textOutline(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("1px contrast")

    @textOutline.setter
    def textOutline(self, num: float): self._config(num, js_type=False)

        
class OptionYaxisStacklabelsAnimation(Options):

    @property
    def defer(self):
        """The animation delay time in milliseconds.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @defer.setter
    def defer(self, num: float): self._config(num, js_type=False)

        
class OptionYaxisStacklabels(Options):

    @property
    def align(self):
        """Defines the horizontal alignment of the stack total label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def allowOverlap(self):
        """Allow the stack labels to overlap.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @allowOverlap.setter
    def allowOverlap(self, flag: bool): self._config(flag, js_type=False)

    @property
    def animation(self) -> 'OptionYaxisStacklabelsAnimation':
        """Enable or disable the initial animation when a series is displayed for the <code>stackLabels</code>. """
        return self._config_sub_data("animation", OptionYaxisStacklabelsAnimation)

    @property
    def backgroundColor(self):
        """The background color or gradient for the stack label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @backgroundColor.setter
    def backgroundColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderColor(self):
        """The border color for the stack label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderRadius(self):
        """The border radius in pixels for the stack label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0)

    @borderRadius.setter
    def borderRadius(self, num: float): self._config(num, js_type=False)

    @property
    def borderWidth(self):
        """The border width in pixels for the stack label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0)

    @borderWidth.setter
    def borderWidth(self, num: float): self._config(num, js_type=False)

    @property
    def crop(self):
        """Whether to hide stack labels that are outside the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @crop.setter
    def crop(self, flag: bool): self._config(flag, js_type=False)

    @property
    def enabled(self):
        """Enable or disable the stack total labels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(False)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def format(self):
        """A format string for the data label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("{total}")

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
    def overflow(self):
        """How to handle stack total labels that flow outside the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("justify")

    @overflow.setter
    def overflow(self, text: str): self._config(text, js_type=False)

    @property
    def rotation(self):
        """Rotation of the labels in degrees.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0)

    @rotation.setter
    def rotation(self, num: float): self._config(num, js_type=False)

    @property
    def style(self) -> 'OptionYaxisStacklabelsStyle':
        """CSS styles for the label. """
        return self._config_sub_data("style", OptionYaxisStacklabelsStyle)

    @property
    def textAlign(self):
        """The text alignment for the label.

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
    def verticalAlign(self):
        """Defines the vertical alignment of the stack total label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """The x position offset of the label relative to the left of the stacked bar.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The y position offset of the label relative to the tick position on the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionYaxisPlotlinesLabels(Options):

    @property
    def clip(self):
        """Whether to hide labels that are outside the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(False)

    @clip.setter
    def clip(self, flag: bool): self._config(flag, js_type=False)

        
class OptionYaxisPlotlinesLabel(Options):

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

        
class OptionYaxisPlotlinesEvents(Options):

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

        
class OptionYaxisPlotlines(Options):

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
    def events(self) -> 'OptionYaxisPlotlinesEvents':
        """An object defining mouse events for the plot line. """
        return self._config_sub_data("events", OptionYaxisPlotlinesEvents)

    @property
    def id(self):
        """An id used for identifying the plot line in Axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @id.setter
    def id(self, text: str): self._config(text, js_type=False)

    @property
    def label(self) -> 'OptionYaxisPlotlinesLabel':
        """Text labels for the plot bands. """
        return self._config_sub_data("label", OptionYaxisPlotlinesLabel)

    @property
    def labels(self) -> 'OptionYaxisPlotlinesLabels':
        """. """
        return self._config_sub_data("labels", OptionYaxisPlotlinesLabels)

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

        
class OptionYaxisPlotbandsLabel(Options):

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

        
class OptionYaxisPlotbandsEvents(Options):

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

        
class OptionYaxisPlotbands(Options):

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
    def events(self) -> 'OptionYaxisPlotbandsEvents':
        """An object defining mouse events for the plot band. """
        return self._config_sub_data("events", OptionYaxisPlotbandsEvents)

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
    def innerRadius(self):
        """In a gauge chart, this option determines the inner radius of the plot band that stretches along the perimeter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(None)

    @innerRadius.setter
    def innerRadius(self, num: float): self._config(num, js_type=False)

    @property
    def label(self) -> 'OptionYaxisPlotbandsLabel':
        """Text labels for the plot bands. """
        return self._config_sub_data("label", OptionYaxisPlotbandsLabel)

    @property
    def outerRadius(self):
        """In a gauge chart, this option determines the outer radius of the plot band that stretches along the perimeter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get("100%")

    @outerRadius.setter
    def outerRadius(self, num: float): self._config(num, js_type=False)

    @property
    def thickness(self):
        """In a gauge chart, this option sets the width of the plot band stretching along the perimeter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/PlotLineOrBand/PlotLineOrBand.ts
        """
        return self._config_get(10)

    @thickness.setter
    def thickness(self, num: float): self._config(num, js_type=False)

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

        
class OptionYaxisLabelsStyle(Options):

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

        
class OptionYaxisLabels(Options):

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
    def style(self) -> 'OptionYaxisLabelsStyle':
        """CSS styles for the label. """
        return self._config_sub_data("style", OptionYaxisLabelsStyle)

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
        return self._config_get("undefined")

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The y position offset of all labels relative to the tick positions on the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(3)

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

        
class OptionYaxisAccessibility(Options):

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

        
class OptionYaxisBreaks(Options):

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

        
class OptionYaxisDatetimelabelformatsDay(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%e %b")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionYaxisDatetimelabelformatsHour(Options):

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

        
class OptionYaxisCrosshair(Options):

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

        
class OptionYaxisEvents(Options):

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

        
class OptionYaxis(Options):

    @property
    def accessibility(self) -> 'OptionYaxisAccessibility':
        """Accessibility options for an axis. """
        return self._config_sub_data("accessibility", OptionYaxisAccessibility)

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
    def breaks(self) -> 'OptionYaxisBreaks':
        """An array defining breaks in the axis, the sections defined will be left out and all the points shifted closer to each other. """
        return self._config_sub_data("breaks", OptionYaxisBreaks)

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
    def crosshair(self) -> 'OptionYaxisCrosshair':
        """Configure a crosshair that follows either the mouse pointer or the hovered point. """
        return self._config_sub_data("crosshair", OptionYaxisCrosshair)

    @property
    def crossing(self):
        """The value on a perpendicular axis where this axis should cross.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(None)

    @crossing.setter
    def crossing(self, num: float): self._config(num, js_type=False)

    @property
    def dateTimeLabelFormats(self) -> 'OptionYaxisDatetimelabelformats':
        """For a datetime axis, the scale will automatically adjust to the appropriate unit. """
        return self._config_sub_data("dateTimeLabelFormats", OptionYaxisDatetimelabelformats)

    @property
    def endOnTick(self):
        """Whether to force the axis to end on a tick.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(True)

    @endOnTick.setter
    def endOnTick(self, flag: bool): self._config(flag, js_type=False)

    @property
    def events(self) -> 'OptionYaxisEvents':
        """Event handlers for the axis. """
        return self._config_sub_data("events", OptionYaxisEvents)

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
    def height(self):
        """The height of the Y axis.

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
    def labels(self) -> 'OptionYaxisLabels':
        """The axis labels show the number or category for each tick. """
        return self._config_sub_data("labels", OptionYaxisLabels)

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
        return self._config_get(0)

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
    def maxColor(self):
        """Solid gauge only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#003399")

    @maxColor.setter
    def maxColor(self, text: str): self._config(text, js_type=False)

    @property
    def maxPadding(self):
        """Padding of the max value relative to the length of the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get(0.05)

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
    def minColor(self):
        """Solid gauge only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("#e6ebf5")

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
    def plotBands(self) -> 'OptionYaxisPlotbands':
        """An array of colored bands stretching across the plot area marking an interval on the axis. """
        return self._config_sub_data("plotBands", OptionYaxisPlotbands)

    @property
    def plotLines(self) -> 'OptionYaxisPlotlines':
        """An array of lines stretching across the plot area, marking a specific value on one of the axes. """
        return self._config_sub_data("plotLines", OptionYaxisPlotlines)

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
    def stackLabels(self) -> 'OptionYaxisStacklabels':
        """The stack labels show the total value for each bar in a stacked column or bar chart. """
        return self._config_sub_data("stackLabels", OptionYaxisStacklabels)

    @property
    def stackShadow(self) -> 'OptionYaxisStackshadow':
        """Relevant only for pictorial series. """
        return self._config_sub_data("stackShadow", OptionYaxisStackshadow)

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
    def stops(self):
        """Solid gauge series only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
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
    def title(self) -> 'OptionYaxisTitle':
        """The axis title, showing next to the axis line. """
        return self._config_sub_data("title", OptionYaxisTitle)

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

        
class OptionYaxisDatetimelabelformatsYear(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%Y")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionYaxisDatetimelabelformatsWeek(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%e %b")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionYaxisDatetimelabelformatsSecond(Options):

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

        
class OptionYaxisDatetimelabelformatsMonth(Options):

    @property
    def main(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Axis/AxisDefaults.ts
        """
        return self._config_get("%b '%y")

    @main.setter
    def main(self, text: str): self._config(text, js_type=False)

        
class OptionYaxisDatetimelabelformatsMinute(Options):

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

        
class OptionYaxisDatetimelabelformatsMillisecond(Options):

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

        
class OptionYaxisDatetimelabelformats(Options):

    @property
    def day(self) -> 'OptionYaxisDatetimelabelformatsDay':
        """. """
        return self._config_sub_data("day", OptionYaxisDatetimelabelformatsDay)

    @property
    def hour(self) -> 'OptionYaxisDatetimelabelformatsHour':
        """. """
        return self._config_sub_data("hour", OptionYaxisDatetimelabelformatsHour)

    @property
    def millisecond(self) -> 'OptionYaxisDatetimelabelformatsMillisecond':
        """. """
        return self._config_sub_data("millisecond", OptionYaxisDatetimelabelformatsMillisecond)

    @property
    def minute(self) -> 'OptionYaxisDatetimelabelformatsMinute':
        """. """
        return self._config_sub_data("minute", OptionYaxisDatetimelabelformatsMinute)

    @property
    def month(self) -> 'OptionYaxisDatetimelabelformatsMonth':
        """. """
        return self._config_sub_data("month", OptionYaxisDatetimelabelformatsMonth)

    @property
    def second(self) -> 'OptionYaxisDatetimelabelformatsSecond':
        """. """
        return self._config_sub_data("second", OptionYaxisDatetimelabelformatsSecond)

    @property
    def week(self) -> 'OptionYaxisDatetimelabelformatsWeek':
        """. """
        return self._config_sub_data("week", OptionYaxisDatetimelabelformatsWeek)

    @property
    def year(self) -> 'OptionYaxisDatetimelabelformatsYear':
        """. """
        return self._config_sub_data("year", OptionYaxisDatetimelabelformatsYear)
