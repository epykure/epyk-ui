from epyk.core.html.options import Options
from typing import Any

        
class OptionCreditsStyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("#999999")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def cursor(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("pointer")

    @cursor.setter
    def cursor(self, text: str): self._config(text, js_type=False)

    @property
    def fontSize(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("0.6em")

    @fontSize.setter
    def fontSize(self, num: float): self._config(num, js_type=False)

        
class OptionCreditsPosition(Options):

    @property
    def align(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("right")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def verticalAlign(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("bottom")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(-10)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(-5)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionCredits(Options):

    @property
    def enabled(self):
        """Whether to show the credits text.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def href(self):
        """The URL for the credits label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("https://www.highcharts.com?credits")

    @href.setter
    def href(self, text: str): self._config(text, js_type=False)

    @property
    def position(self) -> 'OptionCreditsPosition':
        """Position configuration for the credits label. """
        return self._config_sub_data("position", OptionCreditsPosition)

    @property
    def style(self) -> 'OptionCreditsStyle':
        """CSS styles for the credits label. """
        return self._config_sub_data("style", OptionCreditsStyle)

    @property
    def text(self):
        """The text for the credits label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("Highcharts.com")

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)
