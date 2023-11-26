from epyk.core.html.options import Options
from typing import Any

        
class OptionNodataPosition(Options):

    @property
    def align(self):
        """Horizontal alignment of the label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/NoDataToDisplay/NoDataDefaults.ts
        """
        return self._config_get("center")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def verticalAlign(self):
        """Vertical alignment of the label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/NoDataToDisplay/NoDataDefaults.ts
        """
        return self._config_get("middle")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """Horizontal offset of the label, in pixels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/NoDataToDisplay/NoDataDefaults.ts
        """
        return self._config_get(0)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """Vertical offset of the label, in pixels.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/NoDataToDisplay/NoDataDefaults.ts
        """
        return self._config_get(0)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionNodata(Options):

    @property
    def attr(self):
        """An object of additional SVG attributes for the no-data label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/NoDataToDisplay/NoDataDefaults.ts
        """
        return self._config_get(None)

    @attr.setter
    def attr(self, value: Any): self._config(value, js_type=False)

    @property
    def position(self) -> 'OptionNodataPosition':
        """The position of the no-data label, relative to the plot area. """
        return self._config_sub_data("position", OptionNodataPosition)

    @property
    def style(self):
        """CSS styles for the no-data label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/NoDataToDisplay/NoDataDefaults.ts
        """
        return self._config_get(None)

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

    @property
    def useHTML(self):
        """Whether to insert the label as HTML, or as pseudo-HTML rendered with SVG.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/NoDataToDisplay/NoDataDefaults.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)
