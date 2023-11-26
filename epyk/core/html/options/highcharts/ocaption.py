from epyk.core.html.options import Options
from typing import Any

        
class OptionCaptionStyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("#666666")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def fontSize(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("0.8em")

    @fontSize.setter
    def fontSize(self, num: float): self._config(num, js_type=False)

        
class OptionCaption(Options):

    @property
    def align(self):
        """The horizontal alignment of the caption.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("left")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def floating(self):
        """When the caption is floating, the plot area will not move to make space for it.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(False)

    @floating.setter
    def floating(self, flag: bool): self._config(flag, js_type=False)

    @property
    def margin(self):
        """The margin between the caption and the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(15)

    @margin.setter
    def margin(self, num: float): self._config(num, js_type=False)

    @property
    def style(self) -> 'OptionCaptionStyle':
        """CSS styles for the caption. """
        return self._config_sub_data("style", OptionCaptionStyle)

    @property
    def text(self):
        """The caption text of the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("")

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
        """The vertical alignment of the caption.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("bottom")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """The x position of the caption relative to the alignment within <code>chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(0)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The y position of the caption relative to the alignment within <code>chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)
