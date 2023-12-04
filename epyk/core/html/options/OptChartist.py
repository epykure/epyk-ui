from typing import List
from epyk.core.html.options import Options

class OptionsAxisY(Options):

    @property
    def onlyInteger(self):
        """"""
        return self._config_get()

    @onlyInteger.setter
    def onlyInteger(self, flag: bool):
        self._config(flag)

    @property
    def offset(self):
        """"""
        return self._config_get()

    @offset.setter
    def offset(self, value: int):
        self._config(value)


class OptionsChartPadding(Options):

    @property
    def right(self):
        """"""
        return self._config_get()

    @right.setter
    def right(self, value: int):
        self._config(value)


class OptionsChartistLine(Options):

    @property
    def high(self):
        """If high is specified then the axis will display values explicitly up to this value and the computed maximum
        from the data is ignored

        Related Pages:

          https://gionkunz.github.io/chartist-js/api-documentation.html
        """
        return self._config_get()

    @high.setter
    def high(self, value: int):
        self._config(value)

    @property
    def low(self):
        """If low is specified then the axis will display values explicitly down to this value and the computed minimum
        from the data is ignored
        """
        return self._config_get()

    @low.setter
    def low(self, value: int):
        self._config(value)

    @property
    def scaleMinSpace(self):
        """This option will be used when finding the right scale division settings.
        The amount of ticks on the scale will be determined so that as many ticks as possible will be displayed,
        while not violating this minimum required space (in pixel).
        """
        return self._config_get()

    @scaleMinSpace.setter
    def scaleMinSpace(self, value: int):
        self._config(value)

    @property
    def onlyInteger(self):
        """Can be set to true or false. If set to true, the scale will be generated with whole numbers only"""
        return self._config_get()

    @onlyInteger.setter
    def onlyInteger(self, flag: bool):
        self._config(flag)

    @property
    def referenceValue(self):
        """The reference value can be used to make sure that this value will always be on the chart.
        This is especially useful on bipolar charts where the bipolar center always needs to be part of the chart.
        """
        return self._config_get()

    @referenceValue.setter
    def referenceValue(self, value: int):
        self._config(value)

    @property
    def divisor(self):
        """If specified then the value range determined from minimum to maximum (or low and high) will be divided by this
        number and ticks will be generated at those division points. The default divisor is 1.
        """
        return self._config_get()

    @divisor.setter
    def divisor(self, value: int):
        self._config(value)

    @property
    def ticks(self):
        """If ticks is explicitly set, then the axis will not compute the ticks with the divisor,
        but directly use the data in ticks to determine at what points on the axis a tick need to be generated.
        """
        return self._config_get()

    @ticks.setter
    def ticks(self, values: List[int]):
        self._config(values)


    @property
    def stretch(self):
        """If set to true the full width will be used to distribute the values where the last value will be at the
        maximum of the axis length. If false the spaces between the ticks will be evenly distributed instead.
        """
        return self._config_get()

    @stretch.setter
    def stretch(self, flag: bool):
        self._config(flag)


class OptionsChartistBar(OptionsChartistLine):

    @property
    def seriesBarDistance(self):
        """ """
        return self._config_get()

    @seriesBarDistance.setter
    def seriesBarDistance(self, num: int):
        self._config(num)

    @property
    def reverseData(self):
        """ """
        return self._config_get()

    @reverseData.setter
    def reverseData(self, flag: bool):
        self._config(flag)

    @property
    def horizontalBars(self):
        """ """
        return self._config_get()

    @horizontalBars.setter
    def horizontalBars(self, flag: bool):
        self._config(flag)


class OptionsChartistPie(Options):

    @property
    def donut(self):
        """"""
        return self._config_get()

    @donut.setter
    def donut(self, flag: bool):
        self._config(flag)

    @property
    def donutWidth(self):
        """"""
        return self._config_get()

    @donutWidth.setter
    def donutWidth(self, value: int):
        self._config(value)

    @property
    def donutSolid(self):
        """"""
        return self._config_get()

    @donutSolid.setter
    def donutSolid(self, flag: bool):
        self._config(flag)

    @property
    def startAngle(self):
        """"""
        return self._config_get()

    @startAngle.setter
    def startAngle(self, value: int):
        self._config(value)

    @property
    def showLabel(self):
        """"""
        return self._config_get()

    @showLabel.setter
    def showLabel(self, flag: bool):
        self._config(flag)