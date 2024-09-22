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
