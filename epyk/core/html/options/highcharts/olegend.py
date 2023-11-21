from epyk.core.html.options import Options
from typing import Any

        
class OptionLegendTitle(Options):

    @property
    def style(self):
        """Generic CSS styles for the legend title.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get({"fontSize": "0.75em", "fontWeight": "bold"})

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

    @property
    def text(self):
        """A text or HTML string for the title.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

        
class OptionLegendNavigation(Options):

    @property
    def activeColor(self):
        """The color for the active up or down arrow in the legend page navigation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("#0022ff")

    @activeColor.setter
    def activeColor(self, text: str): self._config(text, js_type=False)

    @property
    def animation(self):
        """How to animate the pages when navigating up or down.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(True)

    @animation.setter
    def animation(self, flag: bool): self._config(flag, js_type=False)

    @property
    def arrowSize(self):
        """The pixel size of the up and down arrows in the legend paging navigation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(12)

    @arrowSize.setter
    def arrowSize(self, num: float): self._config(num, js_type=False)

    @property
    def enabled(self):
        """Whether to enable the legend navigation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def inactiveColor(self):
        """The color of the inactive up or down arrow in the legend page navigation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("#cccccc")

    @inactiveColor.setter
    def inactiveColor(self, text: str): self._config(text, js_type=False)

    @property
    def style(self):
        """Text styles for the legend page navigation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

        
class OptionLegend(Options):

    @property
    def accessibility(self) -> 'OptionLegendAccessibility':
        """Accessibility options for the legend. """
        return self._config_sub_data("accessibility", OptionLegendAccessibility)

    @property
    def align(self):
        """The horizontal alignment of the legend box within the chart area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("center")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def alignColumns(self):
        """If the <a href="legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(True)

    @alignColumns.setter
    def alignColumns(self, flag: bool): self._config(flag, js_type=False)

    @property
    def backgroundColor(self):
        """The background color of the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @backgroundColor.setter
    def backgroundColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderColor(self):
        """The color of the drawn border around the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("#999999")

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderRadius(self):
        """The border corner radius of the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(0)

    @borderRadius.setter
    def borderRadius(self, num: float): self._config(num, js_type=False)

    @property
    def borderWidth(self):
        """The width of the drawn border around the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(0)

    @borderWidth.setter
    def borderWidth(self, num: float): self._config(num, js_type=False)

    @property
    def bubbleLegend(self) -> 'OptionLegendBubblelegend':
        """The bubble legend is an additional element in legend which presents the scale of the bubble series. """
        return self._config_sub_data("bubbleLegend", OptionLegendBubblelegend)

    @property
    def className(self):
        """A CSS class name to apply to the legend group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("highcharts-no-tooltip")

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def enabled(self):
        """Enable or disable the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def floating(self):
        """When the legend is floating, the plot area ignores it and is allowed to be placed below it.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @floating.setter
    def floating(self, flag: bool): self._config(flag, js_type=False)

    @property
    def itemCheckboxStyle(self):
        """Default styling for the checkbox next to a legend item when <code>showCheckbox</code> is true.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get({"width": "13px", "height": "13px", "position":"absolute"})

    @itemCheckboxStyle.setter
    def itemCheckboxStyle(self, value: Any): self._config(value, js_type=False)

    @property
    def itemDistance(self):
        """In a legend with horizontal layout, the itemDistance defines the pixel distance between each item.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(20)

    @itemDistance.setter
    def itemDistance(self, num: float): self._config(num, js_type=False)

    @property
    def itemHiddenStyle(self):
        """CSS styles for each legend item when the corresponding series or point is hidden.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get({"color": "#cccccc"})

    @itemHiddenStyle.setter
    def itemHiddenStyle(self, value: Any): self._config(value, js_type=False)

    @property
    def itemHoverStyle(self):
        """CSS styles for each legend item in hover mode.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get({"color": "#000000"})

    @itemHoverStyle.setter
    def itemHoverStyle(self, value: Any): self._config(value, js_type=False)

    @property
    def itemMarginBottom(self):
        """The pixel bottom margin for each legend item.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(2)

    @itemMarginBottom.setter
    def itemMarginBottom(self, num: float): self._config(num, js_type=False)

    @property
    def itemMarginTop(self):
        """The pixel top margin for each legend item.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(2)

    @itemMarginTop.setter
    def itemMarginTop(self, num: float): self._config(num, js_type=False)

    @property
    def itemStyle(self):
        """CSS styles for each legend item.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get({"color": "#333333", "cursor": "pointer", "fontSize": "0.75em", "fontWeight": "bold", "textOverflow": "ellipsis"})

    @itemStyle.setter
    def itemStyle(self, value: Any): self._config(value, js_type=False)

    @property
    def itemWidth(self):
        """The width for each legend item.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @itemWidth.setter
    def itemWidth(self, num: float): self._config(num, js_type=False)

    @property
    def labelFormat(self):
        """A <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("{name}")

    @labelFormat.setter
    def labelFormat(self, text: str): self._config(text, js_type=False)

    @property
    def labelFormatter(self):
        """Callback function to format each of the series&#39; labels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @labelFormatter.setter
    def labelFormatter(self, value: Any): self._config(value, js_type=False)

    @property
    def layout(self):
        """The layout of the legend items.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("horizontal")

    @layout.setter
    def layout(self, text: str): self._config(text, js_type=False)

    @property
    def lineHeight(self):
        """Line height for the legend items.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(16)

    @lineHeight.setter
    def lineHeight(self, num: float): self._config(num, js_type=False)

    @property
    def margin(self):
        """If the plot area sized is calculated automatically and the legend is not floating, the legend margin is the space between the legend and the axis labels or plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(12)

    @margin.setter
    def margin(self, num: float): self._config(num, js_type=False)

    @property
    def maxHeight(self):
        """Maximum pixel height for the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @maxHeight.setter
    def maxHeight(self, num: float): self._config(num, js_type=False)

    @property
    def navigation(self) -> 'OptionLegendNavigation':
        """Options for the paging or navigation appearing when the legend is overflown. """
        return self._config_sub_data("navigation", OptionLegendNavigation)

    @property
    def padding(self):
        """The inner padding of the legend box.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(8)

    @padding.setter
    def padding(self, num: float): self._config(num, js_type=False)

    @property
    def reversed(self):
        """Whether to reverse the order of the legend items compared to the order of the series or points as defined in the configuration object.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @reversed.setter
    def reversed(self, flag: bool): self._config(flag, js_type=False)

    @property
    def rtl(self):
        """Whether to show the symbol on the right side of the text rather than the left side.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @rtl.setter
    def rtl(self, flag: bool): self._config(flag, js_type=False)

    @property
    def shadow(self):
        """Whether to apply a drop shadow to the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @shadow.setter
    def shadow(self, flag: bool): self._config(flag, js_type=False)

    @property
    def squareSymbol(self):
        """When this is true, the legend symbol width will be the same as the symbol height, which in turn defaults to the font size of the legend items.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(True)

    @squareSymbol.setter
    def squareSymbol(self, flag: bool): self._config(flag, js_type=False)

    @property
    def style(self):
        """CSS styles for the legend area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

    @property
    def symbolHeight(self):
        """The pixel height of the symbol for series types that use a rectangle in the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @symbolHeight.setter
    def symbolHeight(self, num: float): self._config(num, js_type=False)

    @property
    def symbolPadding(self):
        """The pixel padding between the legend item symbol and the legend item text.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(5)

    @symbolPadding.setter
    def symbolPadding(self, num: float): self._config(num, js_type=False)

    @property
    def symbolRadius(self):
        """The border radius of the symbol for series types that use a rectangle in the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @symbolRadius.setter
    def symbolRadius(self, num: float): self._config(num, js_type=False)

    @property
    def symbolWidth(self):
        """The pixel width of the legend item symbol.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @symbolWidth.setter
    def symbolWidth(self, num: float): self._config(num, js_type=False)

    @property
    def title(self) -> 'OptionLegendTitle':
        """A title to be added on top of the legend. """
        return self._config_sub_data("title", OptionLegendTitle)

    @property
    def useHTML(self):
        """Whether to <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def valueDecimals(self):
        """For a color axis with data classes, how many decimals to render in the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(-1)

    @valueDecimals.setter
    def valueDecimals(self, num: float): self._config(num, js_type=False)

    @property
    def valueSuffix(self):
        """For a color axis with data classes, a suffix for the range numbers in the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("''")

    @valueSuffix.setter
    def valueSuffix(self, text: str): self._config(text, js_type=False)

    @property
    def verticalAlign(self):
        """The vertical alignment of the legend box.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("bottom")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def width(self):
        """The width of the legend box.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @width.setter
    def width(self, num: float): self._config(num, js_type=False)

    @property
    def x(self):
        """The x offset of the legend relative to its horizontal alignment <code>align</code> within chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(0)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The vertical offset of the legend relative to it&#39;s vertical alignment <code>verticalAlign</code> within chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(0)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionLegendBubblelegendRanges(Options):

    @property
    def borderColor(self):
        """The color of the border for individual range.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("undefined")

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def color(self):
        """The color of the bubble for individual range.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("undefined")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def connectorColor(self):
        """The color of the connector for individual range.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("undefined")

    @connectorColor.setter
    def connectorColor(self, text: str): self._config(text, js_type=False)

    @property
    def value(self):
        """Range size value, similar to bubble Z data.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("undefined")

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

        
class OptionLegendBubblelegendLabels(Options):

    @property
    def align(self):
        """The alignment of the labels compared to the bubble legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("right")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def allowOverlap(self):
        """Whether to allow data labels to overlap.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(False)

    @allowOverlap.setter
    def allowOverlap(self, flag: bool): self._config(flag, js_type=False)

    @property
    def className(self):
        """An additional class name to apply to the bubble legend label graphical elements.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("undefined")

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def format(self):
        """A format string for the bubble legend labels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("")

    @format.setter
    def format(self, text: str): self._config(text, js_type=False)

    @property
    def formatter(self):
        """Available <code>this</code> properties are: <ul> <li><code>this.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("undefined")

    @formatter.setter
    def formatter(self, text: str): self._config(text, js_type=False)

    @property
    def style(self):
        """CSS styles for the labels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(None)

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

    @property
    def x(self):
        """The x position offset of the label relative to the connector.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(0)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The y position offset of the label relative to the connector.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(0)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionLegendBubblelegend(Options):

    @property
    def borderColor(self):
        """The color of the ranges borders, can be also defined for an individual range.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("undefined")

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderWidth(self):
        """The width of the ranges borders in pixels, can be also defined for an individual range.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(2)

    @borderWidth.setter
    def borderWidth(self, num: float): self._config(num, js_type=False)

    @property
    def className(self):
        """An additional class name to apply to the bubble legend&#39; circle graphical elements.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("undefined")

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def color(self):
        """The main color of the bubble legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("undefined")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def connectorClassName(self):
        """An additional class name to apply to the bubble legend&#39;s connector graphical elements.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("undefined")

    @connectorClassName.setter
    def connectorClassName(self, text: str): self._config(text, js_type=False)

    @property
    def connectorColor(self):
        """The color of the connector, can be also defined for an individual range.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("undefined")

    @connectorColor.setter
    def connectorColor(self, text: str): self._config(text, js_type=False)

    @property
    def connectorDistance(self):
        """The length of the connectors in pixels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(60)

    @connectorDistance.setter
    def connectorDistance(self, num: float): self._config(num, js_type=False)

    @property
    def connectorWidth(self):
        """The width of the connectors in pixels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(1)

    @connectorWidth.setter
    def connectorWidth(self, num: float): self._config(num, js_type=False)

    @property
    def enabled(self):
        """Enable or disable the bubble legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(False)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def labels(self) -> 'OptionLegendBubblelegendLabels':
        """Options for the bubble legend labels. """
        return self._config_sub_data("labels", OptionLegendBubblelegendLabels)

    @property
    def legendIndex(self):
        """The position of the bubble legend in the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(0)

    @legendIndex.setter
    def legendIndex(self, num: float): self._config(num, js_type=False)

    @property
    def maxSize(self):
        """Miximum bubble legend range size.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(60)

    @maxSize.setter
    def maxSize(self, num: float): self._config(num, js_type=False)

    @property
    def minSize(self):
        """Minimum bubble legend range size.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(10)

    @minSize.setter
    def minSize(self, num: float): self._config(num, js_type=False)

    @property
    def ranges(self) -> 'OptionLegendBubblelegendRanges':
        """Options for specific range. """
        return self._config_sub_data("ranges", OptionLegendBubblelegendRanges)

    @property
    def sizeBy(self):
        """Whether the bubble legend range value should be represented by the area or the width of the bubble.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get("area")

    @sizeBy.setter
    def sizeBy(self, text: str): self._config(text, js_type=False)

    @property
    def sizeByAbsoluteValue(self):
        """When this is true, the absolute value of z determines the size of the bubble.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(False)

    @sizeByAbsoluteValue.setter
    def sizeByAbsoluteValue(self, flag: bool): self._config(flag, js_type=False)

    @property
    def zIndex(self):
        """Define the visual z index of the bubble legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(1)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)

    @property
    def zThreshold(self):
        """Ranges with with lower value than zThreshold, are skipped.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Series/Bubble/BubbleLegendDefaults.ts
        """
        return self._config_get(0)

    @zThreshold.setter
    def zThreshold(self, num: float): self._config(num, js_type=False)

        
class OptionLegendAccessibilityKeyboardnavigation(Options):

    @property
    def enabled(self):
        """Enable keyboard navigation for the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

        
class OptionLegendAccessibility(Options):

    @property
    def enabled(self):
        """Enable accessibility support for the legend.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def keyboardNavigation(self) -> 'OptionLegendAccessibilityKeyboardnavigation':
        """Options for keyboard navigation for the legend. """
        return self._config_sub_data("keyboardNavigation", OptionLegendAccessibilityKeyboardnavigation)
