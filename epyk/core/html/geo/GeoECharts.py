#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.graph import GraphECharts
from epyk.core.html.options import OptChartECharts
from epyk.core.js.packages import packageImport


class Maps(GraphECharts.ECharts):
    name = 'ECharts Geo'
    _option_cls = OptChartECharts.EChartGeoOptions
    builder_module = "EkMapECharts"

    @property
    def options(self) -> OptChartECharts.EChartGeoOptions:
        """Property to the component options.

        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

