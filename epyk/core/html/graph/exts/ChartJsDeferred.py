from epyk.core.html.options import Options


class Deferred(Options):

    @property
    def delay(self):
        """
        Number of milliseconds to delay the loading after the chart is considered inside the viewport.

        Related Pages:

          https://chartjs-plugin-deferred.netlify.app/samples/delay.html
        """
        return self._config_get(0)

    @delay.setter
    def delay(self, num: int):
        self._config(num)

    @property
    def xOffset(self):
        """
        Number of pixels (or percent of the canvas width) from which the chart is considered inside the viewport.

        Related Pages:

          https://chartjs-plugin-deferred.netlify.app/samples/delay.html
        """
        return self._config_get(0)

    @xOffset.setter
    def xOffset(self, num: int):
        self._config(num)

    @property
    def yOffset(self):
        """
        Number of pixels (or percent of the canvas height) from which the chart is considered inside the viewport.

        Related Pages:

          https://chartjs-plugin-deferred.netlify.app/samples/delay.html
        """
        return self._config_get(0)

    @yOffset.setter
    def yOffset(self, num: int):
        self._config(num)
