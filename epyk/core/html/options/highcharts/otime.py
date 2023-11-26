from epyk.core.html.options import Options
from typing import Any

        
class OptionTime(Options):

    @property
    def Date(self):
        """A custom <code>Date</code> class for advanced date handling.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("undefined")

    @Date.setter
    def Date(self, value: Any): self._config(value, js_type=False)

    @property
    def getTimezoneOffset(self):
        """A callback to return the time zone offset for a given datetime.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("undefined")

    @getTimezoneOffset.setter
    def getTimezoneOffset(self, value: Any): self._config(value, js_type=False)

    @property
    def moment(self):
        """Allows to manually load the <code>moment.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Time.ts
        """
        return self._config_get(None)

    @moment.setter
    def moment(self, value: Any): self._config(value, js_type=False)

    @property
    def timezone(self):
        """Requires <a href="https://momentjs.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("undefined")

    @timezone.setter
    def timezone(self, text: str): self._config(text, js_type=False)

    @property
    def timezoneOffset(self):
        """The timezone offset in minutes.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(0)

    @timezoneOffset.setter
    def timezoneOffset(self, num: float): self._config(num, js_type=False)

    @property
    def useUTC(self):
        """Whether to use UTC time for axis scaling, tickmark placement and time display in <code>Highcharts.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(True)

    @useUTC.setter
    def useUTC(self, flag: bool): self._config(flag, js_type=False)
