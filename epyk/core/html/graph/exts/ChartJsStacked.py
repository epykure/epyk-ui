from epyk.core.html.options import Options


class Stacked100(Options):

    @property
    def enable(self):
        """
        Enable chart.

        Related Pages:

          https://github.com/y-takey/chartjs-plugin-stacked100
        """
        return self._config_get(True)

    @enable.setter
    def enable(self, flag: bool):
        self._config(flag)

    @property
    def replaceTooltipLabel(self):
        """
        Replace tooltip label automatically.

        Related Pages:

          https://github.com/y-takey/chartjs-plugin-stacked100
        """
        return self._config_get(True)

    @replaceTooltipLabel.setter
    def replaceTooltipLabel(self, flag: bool):
        self._config(flag)

    @property
    def fixNegativeScale(self):
        """
        FixNegativeScale is false, the negative scale is variable. (the range is between -100 and -1)

        Related Pages:

          https://github.com/y-takey/chartjs-plugin-stacked100
        """
        return self._config_get(True)

    @fixNegativeScale.setter
    def fixNegativeScale(self, flag: bool):
        self._config(flag)

    @property
    def individual(self):
        """
        Scale the highest bar to 100%, and the rest would be proportional to the highest bar of a stack.

        Related Pages:

          https://github.com/y-takey/chartjs-plugin-stacked100
        """
        return self._config_get(False)

    @individual.setter
    def individual(self, flag: bool):
        self._config(flag)

    @property
    def precision(self):
        """
        Precision of percentage. the range is between 0 and 16

        Related Pages:

          https://github.com/y-takey/chartjs-plugin-stacked100
        """
        return self._config_get(1)

    @precision.setter
    def precision(self, num: int):
        self._config(num)
