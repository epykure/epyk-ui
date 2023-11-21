from epyk.core.html.options import Options
from typing import Any

        
class OptionTitleStyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("#333333")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def fontWeight(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("bold")

    @fontWeight.setter
    def fontWeight(self, text: str): self._config(text, js_type=False)

        
class OptionTitle(Options):

    @property
    def align(self):
        """The horizontal alignment of the title.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("center")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def floating(self):
        """When the title is floating, the plot area will not move to make space for it.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @floating.setter
    def floating(self, flag: bool): self._config(flag, js_type=False)

    @property
    def margin(self):
        """The margin between the title and the plot area, or if a subtitle is present, the margin between the subtitle and the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(15)

    @margin.setter
    def margin(self, num: float): self._config(num, js_type=False)

    @property
    def style(self) -> 'OptionTitleStyle':
        """CSS styles for the title. """
        return self._config_sub_data("style", OptionTitleStyle)

    @property
    def text(self):
        """The title of the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("Chart title")

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

    @property
    def useHTML(self):
        """Whether to <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def verticalAlign(self):
        """The vertical alignment of the title.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def widthAdjust(self):
        """Adjustment made to the title width, normally to reserve space for the exporting burger menu.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(-44)

    @widthAdjust.setter
    def widthAdjust(self, num: float): self._config(num, js_type=False)

    @property
    def x(self):
        """The x position of the title relative to the alignment within <code>chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(0)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The y position of the title relative to the alignment within <a href="#chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)
