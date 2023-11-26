from epyk.core.html.options import Options
from typing import Any

        
class OptionGlobal(Options):

    @property
    def canvasToolsURL(self):
        """<em>Canvg rendering for Android 2.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @canvasToolsURL.setter
    def canvasToolsURL(self, text: str): self._config(text, js_type=False)

    @property
    def Date(self):
        """This option is deprecated since v6.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @Date.setter
    def Date(self, value: Any): self._config(value, js_type=False)

    @property
    def getTimezoneOffset(self):
        """This option is deprecated since v6.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @getTimezoneOffset.setter
    def getTimezoneOffset(self, value: Any): self._config(value, js_type=False)

    @property
    def timezone(self):
        """This option is deprecated since v6.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @timezone.setter
    def timezone(self, text: str): self._config(text, js_type=False)

    @property
    def timezoneOffset(self):
        """This option is deprecated since v6.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @timezoneOffset.setter
    def timezoneOffset(self, num: float): self._config(num, js_type=False)

    @property
    def useUTC(self):
        """This option is deprecated since v6.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @useUTC.setter
    def useUTC(self, flag: bool): self._config(flag, js_type=False)
