from epyk.core.html.options import Options


class OptionsNumGauge(Options):
    component_properties = ("symbol",)

    @property
    def height(self):
        """Component height with unit - Default in pixel"""
        return self._config_get(None)

    @height.setter
    def height(self, val: str):
        self._config(val)

    @property
    def value(self):
        """Value column name if dictionary """
        return self._config_get(None)

    @value.setter
    def value(self, val: str):
        self._config(val)

    @property
    def symbol(self):
        """Symbol value - Default &"""
        return self._config_get("%")

    @symbol.setter
    def symbol(self, val: str):
        self._config(val)

    @property
    def width(self):
        """Component width with unit - Default in pixel"""
        return self._config_get(None)

    @width.setter
    def width(self, val: str):
        self._config(val)


class OptionsNumCircle(Options):
    @property
    def value(self):
        """Value column name if dictionary """
        return self._config_get(None)

    @value.setter
    def value(self, val: str):
        self._config(val)
