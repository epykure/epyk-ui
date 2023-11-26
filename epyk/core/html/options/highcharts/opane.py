from epyk.core.html.options import Options
from typing import Any

        
class OptionPaneBackground(Options):

    @property
    def backgroundColor(self):
        """The background color or gradient for the pane.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get("{ linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 }, stops: [[0, #ffffff], [1, #e6e6e6]] }")

    @backgroundColor.setter
    def backgroundColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderColor(self):
        """The pane background border color.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get("#cccccc")

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderWidth(self):
        """The pixel border width of the pane background.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get(1)

    @borderWidth.setter
    def borderWidth(self, num: float): self._config(num, js_type=False)

    @property
    def className(self):
        """The class name for this background.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get(None)

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def innerRadius(self):
        """The inner radius of the pane background.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get(0)

    @innerRadius.setter
    def innerRadius(self, num: float): self._config(num, js_type=False)

    @property
    def outerRadius(self):
        """The outer radius of the circular pane background.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get("105%")

    @outerRadius.setter
    def outerRadius(self, num: float): self._config(num, js_type=False)

    @property
    def shape(self):
        """The shape of the pane background.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get("circle")

    @shape.setter
    def shape(self, text: str): self._config(text, js_type=False)

        
class OptionPane(Options):

    @property
    def background(self) -> 'OptionPaneBackground':
        """An array of background items for the pane. """
        return self._config_sub_data("background", OptionPaneBackground)

    @property
    def center(self):
        """The center of a polar chart or angular gauge, given as an array of [x, y] positions.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get(["50%", "50%"])

    @center.setter
    def center(self, value: Any): self._config(value, js_type=False)

    @property
    def endAngle(self):
        """The end angle of the polar X axis or gauge value axis, given in degrees where 0 is north.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get(None)

    @endAngle.setter
    def endAngle(self, num: float): self._config(num, js_type=False)

    @property
    def innerSize(self):
        """The inner size of the pane, either as a number defining pixels, or a percentage defining a percentage of the pane&#39;s size.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get("0%")

    @innerSize.setter
    def innerSize(self, num: float): self._config(num, js_type=False)

    @property
    def size(self):
        """The size of the pane, either as a number defining pixels, or a percentage defining a percentage of the available plot area (the smallest of the plot height or plot width).

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get("85%")

    @size.setter
    def size(self, num: float): self._config(num, js_type=False)

    @property
    def startAngle(self):
        """The start angle of the polar X axis or gauge axis, given in degrees where 0 is north.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Pane.ts
        """
        return self._config_get(0)

    @startAngle.setter
    def startAngle(self, num: float): self._config(num, js_type=False)
