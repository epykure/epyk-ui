import logging

from typing import Union, List
from epyk.core.js import JsUtils
from epyk.core.html.options import Options, OptionsWithTemplates
from epyk.core.html.options import Enums
from epyk.core.py import types as etypes


class AgChartsConfig(OptionsWithTemplates):

    @property
    def container(self):
        """
        To have one (the first) grid reflect column changes in another (the second), place the first grid's options in
        alignedGrids property of the second grids.

        `Related Pages <https://www.ag-grid.com/javascript-grid-aligned-grids/>`_
        """
        return self._config_get()

    @container.setter
    def container(self, value):
        self._config(value, js_type=True)

    @property
    def data(self):
        """
        To have one (the first) grid reflect column changes in another (the second), place the first grid's options in
        alignedGrids property of the second grids.

        `Related Pages <https://www.ag-grid.com/javascript-grid-aligned-grids/>`_
        """
        return self._config_get()

    @data.setter
    def data(self, values: list):
        self._config(values)

    @property
    def height(self) -> int:
        """The height of the chart in pixels.

        `Related Pages <https://www.ag-grid.com/charts/options/#reference-AgChartOptions-height/>`_
        """
        return self._config_get()

    @height.setter
    def height(self, value: int):
        self._config(value)

    @property
    def minHeight(self) -> int:
        """Sets the minimum height of the chart. Ignored if height is specified.

        `Related Pages <https://www.ag-grid.com/charts/options/#reference-AgChartOptions-minHeight/>`_
        """
        return self._config_get()

    @minHeight.setter
    def minHeight(self, value: int):
        self._config(value)

    @property
    def minWidth(self) -> int:
        """Sets the minimum width of the chart. Ignored if width is specified.

        `Related Pages <https://www.ag-grid.com/charts/options/#reference-AgChartOptions-minWidth/>`_
        """
        return self._config_get()

    @minWidth.setter
    def minWidth(self, value: int):
        self._config(value)

    @property
    def series(self):
        """
        To have one (the first) grid reflect column changes in another (the second), place the first grid's options in
        alignedGrids property of the second grids.

        `Related Pages <https://www.ag-grid.com/javascript-grid-aligned-grids/>`_
        """
        return self._config_get()

    @series.setter
    def series(self, values: list):
        self._config(values)

    @property
    def theme(self):
        """A predefined theme name or an object containing theme overrides.

        `Related Pages <https://www.ag-grid.com/charts/options/#reference-AgChartOptions-theme/>`_
        `Theme API <https://www.ag-grid.com/charts/themes-api//>`_
        """
        return self._config_get()

    @theme.setter
    def theme(self, value):
        self._config(value)

    @property
    def width(self) -> int:
        """The width of the chart in pixels.

        `Related Pages <https://www.ag-grid.com/charts/options/#reference-AgChartOptions-width/>`_
        """
        return self._config_get()

    @width.setter
    def width(self, value: int):
        self._config(value)
