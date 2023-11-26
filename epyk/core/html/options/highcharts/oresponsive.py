from epyk.core.html.options import Options
from typing import Any

        
class OptionResponsiveRulesCondition(Options):

    @property
    def callback(self):
        """A callback function to gain complete control on when the responsive rule applies.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Responsive.ts
        """
        return self._config_get(None)

    @callback.setter
    def callback(self, value: Any): self._config(value, js_type=False)

    @property
    def maxHeight(self):
        """The responsive rule applies if the chart height is less than this.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Responsive.ts
        """
        return self._config_get(None)

    @maxHeight.setter
    def maxHeight(self, num: float): self._config(num, js_type=False)

    @property
    def maxWidth(self):
        """The responsive rule applies if the chart width is less than this.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Responsive.ts
        """
        return self._config_get(None)

    @maxWidth.setter
    def maxWidth(self, num: float): self._config(num, js_type=False)

    @property
    def minHeight(self):
        """The responsive rule applies if the chart height is greater than this.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Responsive.ts
        """
        return self._config_get(0)

    @minHeight.setter
    def minHeight(self, num: float): self._config(num, js_type=False)

    @property
    def minWidth(self):
        """The responsive rule applies if the chart width is greater than this.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Responsive.ts
        """
        return self._config_get(0)

    @minWidth.setter
    def minWidth(self, num: float): self._config(num, js_type=False)

        
class OptionResponsiveRules(Options):

    @property
    def chartOptions(self):
        """A full set of chart options to apply as overrides to the general chart options.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Responsive.ts
        """
        return self._config_get(None)

    @chartOptions.setter
    def chartOptions(self, value: Any): self._config(value, js_type=False)

    @property
    def condition(self) -> 'OptionResponsiveRulesCondition':
        """Under which conditions the rule applies. """
        return self._config_sub_data("condition", OptionResponsiveRulesCondition)

        
class OptionResponsive(Options):

    @property
    def rules(self) -> 'OptionResponsiveRules':
        """A set of rules for responsive settings. """
        return self._config_sub_data_enum("rules", OptionResponsiveRules)
