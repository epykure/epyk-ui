from epyk.core.html.options import Options
from typing import Any

        
class OptionDrilldownBreadcrumbsEvents(Options):

    @property
    def click(self):
        """Fires when clicking on the breadcrumbs button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(None)

    @click.setter
    def click(self, value: Any): self._config(value, js_type=False)

        
class OptionDrilldownActivedatalabelstyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get("#0022ff")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def cursor(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get("pointer")

    @cursor.setter
    def cursor(self, text: str): self._config(text, js_type=False)

    @property
    def fontWeight(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get("bold")

    @fontWeight.setter
    def fontWeight(self, text: str): self._config(text, js_type=False)

    @property
    def textDecoration(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get("underline")

    @textDecoration.setter
    def textDecoration(self, text: str): self._config(text, js_type=False)

        
class OptionDrilldown(Options):

    @property
    def activeAxisLabelStyle(self):
        """Additional styles to apply to the X axis label for a point that has drilldown data.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get({ "cursor": "pointer", "color": "#003399", "fontWeight": "bold", "textDecoration": "underline" })

    @activeAxisLabelStyle.setter
    def activeAxisLabelStyle(self, value: Any): self._config(value, js_type=False)

    @property
    def activeDataLabelStyle(self) -> 'OptionDrilldownActivedatalabelstyle':
        """Additional styles to apply to the data label of a point that has drilldown data. """
        return self._config_sub_data("activeDataLabelStyle", OptionDrilldownActivedatalabelstyle)

    @property
    def allowPointDrilldown(self):
        """When this option is false, clicking a single point will drill down all points in the same category, equivalent to clicking the X axis label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get(True)

    @allowPointDrilldown.setter
    def allowPointDrilldown(self, flag: bool): self._config(flag, js_type=False)

    @property
    def animation(self):
        """Set the animation for all drilldown animations.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get(None)

    @animation.setter
    def animation(self, flag: bool): self._config(flag, js_type=False)

    @property
    def breadcrumbs(self) -> 'OptionDrilldownBreadcrumbs':
        """Options for the breadcrumbs, the navigation at the top leading the way up through the drilldown levels. """
        return self._config_sub_data("breadcrumbs", OptionDrilldownBreadcrumbs)

    @property
    def drillUpButton(self) -> 'OptionDrilldownDrillupbutton':
        """Options for the drill up button that appears when drilling down on a series. """
        return self._config_sub_data("drillUpButton", OptionDrilldownDrillupbutton)

    @property
    def series(self):
        """An array of series configurations for the drill down.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get(None)

    @series.setter
    def series(self, value: Any): self._config(value, js_type=False)

        
class OptionDrilldownDrillupbuttonPosition(Options):

    @property
    def align(self):
        """Horizontal alignment.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get("right")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def verticalAlign(self):
        """Vertical alignment of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get("top")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """The X offset of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get(-10)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The Y offset of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get(10)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionDrilldownDrillupbutton(Options):

    @property
    def position(self) -> 'OptionDrilldownDrillupbuttonPosition':
        """Positioning options for the button within the <code>relativeTo</code> box. """
        return self._config_sub_data("position", OptionDrilldownDrillupbuttonPosition)

    @property
    def relativeTo(self):
        """What box to align the button to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get("plotBox")

    @relativeTo.setter
    def relativeTo(self, text: str): self._config(text, js_type=False)

    @property
    def theme(self):
        """A collection of attributes for the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get(None)

    @theme.setter
    def theme(self, value: Any): self._config(value, js_type=False)

        
class OptionDrilldownBreadcrumbsSeparatorStyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("#666666")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def fontSize(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("0.8em")

    @fontSize.setter
    def fontSize(self, num: float): self._config(num, js_type=False)

        
class OptionDrilldownBreadcrumbsSeparator(Options):

    @property
    def style(self) -> 'OptionDrilldownBreadcrumbsSeparatorStyle':
        """CSS styles for the breadcrumbs separator. """
        return self._config_sub_data("style", OptionDrilldownBreadcrumbsSeparatorStyle)

    @property
    def text(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("/")

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

        
class OptionDrilldownBreadcrumbsPosition(Options):

    @property
    def align(self):
        """Horizontal alignment of the breadcrumbs buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("left")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def verticalAlign(self):
        """Vertical alignment of the breadcrumbs buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("top")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """The X offset of the breadcrumbs button group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(0)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The Y offset of the breadcrumbs button group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("undefined")

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionDrilldownBreadcrumbs(Options):

    @property
    def buttonSpacing(self):
        """The default padding for each button and separator in each direction.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(5)

    @buttonSpacing.setter
    def buttonSpacing(self, num: float): self._config(num, js_type=False)

    @property
    def buttonTheme(self) -> 'OptionDrilldownBreadcrumbsButtontheme':
        """A collection of attributes for the buttons. """
        return self._config_sub_data("buttonTheme", OptionDrilldownBreadcrumbsButtontheme)

    @property
    def events(self) -> 'OptionDrilldownBreadcrumbsEvents':
        """. """
        return self._config_sub_data("events", OptionDrilldownBreadcrumbsEvents)

    @property
    def floating(self):
        """When the breadcrumbs are floating, the plot area will not move to make space for it.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(False)

    @floating.setter
    def floating(self, flag: bool): self._config(flag, js_type=False)

    @property
    def format(self):
        """A format string for the breadcrumbs button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("undefined")

    @format.setter
    def format(self, text: str): self._config(text, js_type=False)

    @property
    def formatter(self):
        """Callback function to format the breadcrumb text from scratch.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("undefined")

    @formatter.setter
    def formatter(self, text: str): self._config(text, js_type=False)

    @property
    def position(self) -> 'OptionDrilldownBreadcrumbsPosition':
        """Positioning for the button row. """
        return self._config_sub_data("position", OptionDrilldownBreadcrumbsPosition)

    @property
    def relativeTo(self):
        """What box to align the button to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("plotBox")

    @relativeTo.setter
    def relativeTo(self, text: str): self._config(text, js_type=False)

    @property
    def rtl(self):
        """Whether to reverse the order of buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(False)

    @rtl.setter
    def rtl(self, flag: bool): self._config(flag, js_type=False)

    @property
    def separator(self) -> 'OptionDrilldownBreadcrumbsSeparator':
        """Options object for Breadcrumbs separator. """
        return self._config_sub_data("separator", OptionDrilldownBreadcrumbsSeparator)

    @property
    def showFullPath(self):
        """Show full path or only a single button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(True)

    @showFullPath.setter
    def showFullPath(self, flag: bool): self._config(flag, js_type=False)

    @property
    def style(self):
        """CSS styles for all breadcrumbs.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(None)

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

    @property
    def useHTML(self):
        """Whether to use HTML to render the breadcrumbs items texts.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def zIndex(self):
        """The z index of the breadcrumbs group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(7)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)

        
class OptionDrilldownBreadcrumbsButtonthemeStyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("#334eff")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

        
class OptionDrilldownBreadcrumbsButtontheme(Options):

    @property
    def style(self) -> 'OptionDrilldownBreadcrumbsButtonthemeStyle':
        """. """
        return self._config_sub_data("style", OptionDrilldownBreadcrumbsButtonthemeStyle)
