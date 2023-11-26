from epyk.core.html.options import Options
from typing import Any

        
class OptionTooltipStyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("#333333")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def cursor(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("default")

    @cursor.setter
    def cursor(self, text: str): self._config(text, js_type=False)

    @property
    def fontSize(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("0.8em")

    @fontSize.setter
    def fontSize(self, num: float): self._config(num, js_type=False)

        
class OptionTooltipDatetimelabelformats(Options):

    @property
    def day(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("%A, %e %b %Y")

    @day.setter
    def day(self, text: str): self._config(text, js_type=False)

    @property
    def hour(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("%A, %e %b, %H:%M")

    @hour.setter
    def hour(self, text: str): self._config(text, js_type=False)

    @property
    def millisecond(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("%A, %e %b, %H:%M:%S.%L")

    @millisecond.setter
    def millisecond(self, text: str): self._config(text, js_type=False)

    @property
    def minute(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("%A, %e %b, %H:%M")

    @minute.setter
    def minute(self, text: str): self._config(text, js_type=False)

    @property
    def month(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("%B %Y")

    @month.setter
    def month(self, text: str): self._config(text, js_type=False)

    @property
    def second(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("%A, %e %b, %H:%M:%S")

    @second.setter
    def second(self, text: str): self._config(text, js_type=False)

    @property
    def week(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("Week from %A, %e %b %Y")

    @week.setter
    def week(self, text: str): self._config(text, js_type=False)

    @property
    def year(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("%Y")

    @year.setter
    def year(self, text: str): self._config(text, js_type=False)

        
class OptionTooltip(Options):

    @property
    def animation(self):
        """Enable or disable animation of the tooltip.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(True)

    @animation.setter
    def animation(self, flag: bool): self._config(flag, js_type=False)

    @property
    def backgroundColor(self):
        """The background color or gradient for the tooltip.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("#ffffff")

    @backgroundColor.setter
    def backgroundColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderColor(self):
        """The color of the tooltip border.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderRadius(self):
        """The radius of the rounded border corners.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(3)

    @borderRadius.setter
    def borderRadius(self, num: float): self._config(num, js_type=False)

    @property
    def borderWidth(self):
        """The pixel width of the tooltip border.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("undefined")

    @borderWidth.setter
    def borderWidth(self, num: float): self._config(num, js_type=False)

    @property
    def className(self):
        """A CSS class name to apply to the tooltip&#39;s container div, allowing unique CSS styling for each chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def clusterFormat(self):
        """The HTML of the cluster point&#39;s in the tooltip.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/MarkerClusters/MarkerClusterDefaults.ts
        """
        return self._config_get("Clustered points: {point.clusterPointsAmount}")

    @clusterFormat.setter
    def clusterFormat(self, text: str): self._config(text, js_type=False)

    @property
    def crosshairs(self):
        """Since 4.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(True)

    @crosshairs.setter
    def crosshairs(self, value: Any): self._config(value, js_type=False)

    @property
    def dateTimeLabelFormats(self) -> 'OptionTooltipDatetimelabelformats':
        """For series on datetime axes, the date format in the tooltip&#39;s header will by default be guessed based on the closest data points. """
        return self._config_sub_data("dateTimeLabelFormats", OptionTooltipDatetimelabelformats)

    @property
    def distance(self):
        """Distance from point to tooltip in pixels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(16)

    @distance.setter
    def distance(self, num: float): self._config(num, js_type=False)

    @property
    def enabled(self):
        """Enable or disable the tooltip.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def followPointer(self):
        """Whether the tooltip should follow the mouse as it moves across columns, pie slices and other point types with an extent.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @followPointer.setter
    def followPointer(self, flag: bool): self._config(flag, js_type=False)

    @property
    def followTouchMove(self):
        """Whether the tooltip should update as the finger moves on a touch device.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(True)

    @followTouchMove.setter
    def followTouchMove(self, flag: bool): self._config(flag, js_type=False)

    @property
    def footerFormat(self):
        """A string to append to the tooltip format.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("")

    @footerFormat.setter
    def footerFormat(self, text: str): self._config(text, js_type=False)

    @property
    def format(self):
        """A <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("undefined")

    @format.setter
    def format(self, text: str): self._config(text, js_type=False)

    @property
    def formatter(self):
        """Callback function to format the text of the tooltip from scratch.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @formatter.setter
    def formatter(self, value: Any): self._config(value, js_type=False)

    @property
    def headerFormat(self):
        """The HTML of the tooltip header line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @headerFormat.setter
    def headerFormat(self, text: str): self._config(text, js_type=False)

    @property
    def headerShape(self):
        """The name of a symbol to use for the border around the tooltip header.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("callout")

    @headerShape.setter
    def headerShape(self, text: str): self._config(text, js_type=False)

    @property
    def hideDelay(self):
        """The number of milliseconds to wait until the tooltip is hidden when mouse out from a point or chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(500)

    @hideDelay.setter
    def hideDelay(self, num: float): self._config(num, js_type=False)

    @property
    def nullFormat(self):
        """The HTML of the null point&#39;s line in the tooltip.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @nullFormat.setter
    def nullFormat(self, text: str): self._config(text, js_type=False)

    @property
    def nullFormatter(self):
        """Callback function to format the text of the tooltip for visible null points.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @nullFormatter.setter
    def nullFormatter(self, value: Any): self._config(value, js_type=False)

    @property
    def outside(self):
        """Whether to allow the tooltip to render outside the chart&#39;s SVG element box.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @outside.setter
    def outside(self, flag: bool): self._config(flag, js_type=False)

    @property
    def padding(self):
        """Padding inside the tooltip, in pixels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(8)

    @padding.setter
    def padding(self, num: float): self._config(num, js_type=False)

    @property
    def pointFormat(self):
        """The HTML of the point&#39;s line in the tooltip.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @pointFormat.setter
    def pointFormat(self, text: str): self._config(text, js_type=False)

    @property
    def pointFormatter(self):
        """A callback function for formatting the HTML output for a single point in the tooltip.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @pointFormatter.setter
    def pointFormatter(self, value: Any): self._config(value, js_type=False)

    @property
    def positioner(self):
        """A callback function to place the tooltip in a custom position.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @positioner.setter
    def positioner(self, value: Any): self._config(value, js_type=False)

    @property
    def shadow(self):
        """Whether to apply a drop shadow to the tooltip.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(True)

    @shadow.setter
    def shadow(self, flag: bool): self._config(flag, js_type=False)

    @property
    def shape(self):
        """The name of a symbol to use for the border around the tooltip.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("callout")

    @shape.setter
    def shape(self, text: str): self._config(text, js_type=False)

    @property
    def shared(self):
        """When the tooltip is shared, the entire plot area will capture mouse movement or touch events.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @shared.setter
    def shared(self, flag: bool): self._config(flag, js_type=False)

    @property
    def snap(self):
        """Proximity snap for graphs or single points.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(10/25)

    @snap.setter
    def snap(self, num: float): self._config(num, js_type=False)

    @property
    def split(self):
        """Split the tooltip into one label per series, with the header close to the axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @split.setter
    def split(self, flag: bool): self._config(flag, js_type=False)

    @property
    def stickOnContact(self):
        """Prevents the tooltip from switching or closing when touched or pointed.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @stickOnContact.setter
    def stickOnContact(self, flag: bool): self._config(flag, js_type=False)

    @property
    def style(self) -> 'OptionTooltipStyle':
        """CSS styles for the tooltip. """
        return self._config_sub_data("style", OptionTooltipStyle)

    @property
    def useHTML(self):
        """Use HTML to render the contents of the tooltip instead of SVG.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def valueDecimals(self):
        """How many decimals to show in each series&#39; y value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @valueDecimals.setter
    def valueDecimals(self, num: float): self._config(num, js_type=False)

    @property
    def valuePrefix(self):
        """A string to prepend to each series&#39; y value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @valuePrefix.setter
    def valuePrefix(self, text: str): self._config(text, js_type=False)

    @property
    def valueSuffix(self):
        """A string to append to each series&#39; y value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @valueSuffix.setter
    def valueSuffix(self, text: str): self._config(text, js_type=False)

    @property
    def xDateFormat(self):
        """The format for the date in the tooltip header if the X axis is a datetime axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @xDateFormat.setter
    def xDateFormat(self, text: str): self._config(text, js_type=False)
