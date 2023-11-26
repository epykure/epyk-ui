from epyk.core.html.options import Options
from typing import Any

        
class OptionLoading(Options):

    @property
    def hideDuration(self):
        """The duration in milliseconds of the fade out effect.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(100)

    @hideDuration.setter
    def hideDuration(self, num: float): self._config(num, js_type=False)

    @property
    def labelStyle(self):
        """CSS styles for the loading label <code>span</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get({"fontWeight": "bold", "position": "relative", "top": "45%"})

    @labelStyle.setter
    def labelStyle(self, value: Any): self._config(value, js_type=False)

    @property
    def showDuration(self):
        """The duration in milliseconds of the fade in effect.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(100)

    @showDuration.setter
    def showDuration(self, num: float): self._config(num, js_type=False)

    @property
    def style(self):
        """CSS styles for the loading screen that covers the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get({"position": "absolute", "backgroundColor": "#ffffff", "opacity": 0.5, "textAlign": "center"})

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)
