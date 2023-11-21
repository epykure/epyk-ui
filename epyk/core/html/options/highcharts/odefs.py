from epyk.core.html.options import Options
from typing import Any

        
class OptionDefsReverseArrowAttributes(Options):

    @property
    def id(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get("reverse-arrow")

    @id.setter
    def id(self, text: str): self._config(text, js_type=False)

    @property
    def markerHeight(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get(10)

    @markerHeight.setter
    def markerHeight(self, num: float): self._config(num, js_type=False)

    @property
    def markerWidth(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get(10)

    @markerWidth.setter
    def markerWidth(self, num: float): self._config(num, js_type=False)

    @property
    def refX(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get(1)

    @refX.setter
    def refX(self, num: float): self._config(num, js_type=False)

    @property
    def refY(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get(5)

    @refY.setter
    def refY(self, num: float): self._config(num, js_type=False)

        
class OptionDefsArrowAttributes(Options):

    @property
    def id(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get("arrow")

    @id.setter
    def id(self, text: str): self._config(text, js_type=False)

    @property
    def markerHeight(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get(10)

    @markerHeight.setter
    def markerHeight(self, num: float): self._config(num, js_type=False)

    @property
    def markerWidth(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get(10)

    @markerWidth.setter
    def markerWidth(self, num: float): self._config(num, js_type=False)

    @property
    def refX(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get(9)

    @refX.setter
    def refX(self, num: float): self._config(num, js_type=False)

    @property
    def refY(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get(5)

    @refY.setter
    def refY(self, num: float): self._config(num, js_type=False)

        
class OptionDefsReverseArrow(Options):

    @property
    def attributes(self) -> 'OptionDefsReverseArrowAttributes':
        """. """
        return self._config_sub_data("attributes", OptionDefsReverseArrowAttributes)

    @property
    def tagName(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get("marker")

    @tagName.setter
    def tagName(self, text: str): self._config(text, js_type=False)

        
class OptionDefsArrow(Options):

    @property
    def attributes(self) -> 'OptionDefsArrowAttributes':
        """. """
        return self._config_sub_data("attributes", OptionDefsArrowAttributes)

    @property
    def children(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get(None)

    @children.setter
    def children(self, value: Any): self._config(value, js_type=False)

    @property
    def tagName(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/Controllables/ControllableDefaults.ts
        """
        return self._config_get("marker")

    @tagName.setter
    def tagName(self, text: str): self._config(text, js_type=False)

        
class OptionDefs(Options):

    @property
    def arrow(self) -> 'OptionDefsArrow':
        """. """
        return self._config_sub_data("arrow", OptionDefsArrow)

    @property
    def reverse_arrow(self) -> 'OptionDefsReverseArrow':
        """. """
        return self._config_sub_data("reverse-arrow", OptionDefsReverseArrow)
