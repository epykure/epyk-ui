#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from epyk.core.html import Html
from epyk.core.html.graph import GraphChartJs
from epyk.core.html.options import OptChartJs
from epyk.core.js import JsUtils

from epyk.core.py import types


class Choropleth(GraphChartJs.Chart):
    name = 'ChartJs Choropleth'
    tag = "canvas"
    requirements = ('chartjs-chart-geo',)
    geo_map = "https://unpkg.com/world-atlas/countries-50m.json"
    # geo_map = "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-10m.json"
    _option_cls = OptChartJs.OptionsGeo
    _chart__type = "choropleth"
    builder_module = "GeoChoropleth"

    @property
    def options(self) -> OptChartJs.OptionsGeo:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @Html.jbuilder("chartjs")
    def build(self, data: types.JS_DATA_TYPES = None, options: types.JS_DATA_TYPES = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """Update the chart with context and / or data changes.

        :param data: Optional. The full datasets object expected by ChartJs
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. Not used
        :param stop_state: Remove the top panel for the component state (error, loading...)
        :param dataflows: Chain of data transformations
        """
        self.js_code = component_id
        callbacks = "(function(){})"
        if stop_state:
            callbacks = "(function(){%s})" % self.hide_state(self.html_code)
        return "%(builder)s(%(htmlObj)s, %(data)s, %(options)s, %(callbacks)s)" % {
            "data": JsUtils.dataFlows(data, dataflows, self.page), "options": self.getCtx(),
            "builder": self.builder_name, "callbacks": callbacks, "htmlObj": component_id or self.dom.varId
        }

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<div><%s %s></%s></div>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


class ChoroplethUs(Choropleth):
    name = 'ChartJs Choropleth US'
    geo_map = "https://unpkg.com/us-atlas/states-10m.json"
    _option_cls = OptChartJs.OptionsGeo
    builder_module = "GeoChoroplethUs"

    @property
    def options(self) -> OptChartJs.OptionsGeo:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options


class ChoroplethCountry(Choropleth):
    name = 'ChartJs Choropleth Country'
    geo_map = "https://raw.githubusercontent.com/markmarkoh/datamaps/master/src/js/data/fra.json"
    _option_cls = OptChartJs.OptionsGeo
    builder_module = "GeoChoroplethCountry"

    @property
    def options(self) -> OptChartJs.OptionsGeo:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options
