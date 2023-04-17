#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.graph import GraphChartJs
from epyk.core.html.options import OptChartJs
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsChartJs

from epyk.core.py import types


class Choropleth(GraphChartJs.Chart):
    name = 'ChartJs Choropleth'
    requirements = ('chartjs-chart-geo',)
    geo_map = "https://unpkg.com/world-atlas/countries-50m.json"
    # geo_map = "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-10m.json"
    _option_cls = OptChartJs.OptionsGeo
    _chart__type = "choropleth"
    builder_name = "GeoChoropleth"

    @property
    def options(self) -> OptChartJs.OptionsGeo:
        """
        Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @Html.jbuider("chartjs")
    def build(self, data: types.JS_DATA_TYPES = None, options: types.JS_DATA_TYPES = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None, stop_state: bool = True):
        """
        Update the chart with context and / or data changes.

        :param data: Optional. The full datasets object expected by ChartJs
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. Not used
        :param stop_state: Remove the top panel for the component state (error, loading...)
        """
        callbacks = "(function(){})"
        if stop_state:
            callbacks = "(function(){%s})" % self.hide_state(component_id)
        return "%(builder)s(%(htmlObj)s, %(data)s, %(options)s, %(map)s, %(callbacks)s)" % {
            "data": data, "options": self.getCtx(),
            "builder": self.builder_name,
            "callbacks": callbacks,
            "htmlObj": component_id or self.dom.varId,
            'map': JsUtils.jsConvertData(self.geo_map, None)
        }

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<div><canvas %s></canvas></div>' % self.get_attrs(css_class_names=self.style.get_classes())


class ChoroplethUs(Choropleth):
    name = 'ChartJs Choropleth US'
    geo_map = "https://unpkg.com/us-atlas/states-10m.json"
    _option_cls = OptChartJs.OptionsGeo
    builder_name = "GeoChoroplethUs"

    @property
    def options(self) -> OptChartJs.OptionsGeo:
        """
        Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def add_dataset(self, data, label, kind=None, colors=None, opacity=None, alias=None):
        """
        Add a new Dataset to the chart list of Datasets.

        Related Pages:

          https://www.chartjs.org/docs/latest/developers/updates.html

        :param data: List. The list of points (float).
        :param label: String. The series label (visible in the legend).
        :param colors: List. Optional. The color for this series. Default the global definition.
        :param opacity: Float. Optional. The opacity level for the content.
        :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
        :param alias: String. The chart alias name visible in the legend. Default the label.
        """
        data = JsChartJs.DataSetBar(self.page, attrs={})
        self._datasets.append(data)
        alias = alias or label
        # if alias not in self.options.y_columns:
        #  self.options.y_columns.append(alias)
        #  self.options.props[alias] = {"type": kind or self.options.type, 'fill': False}
        if kind == "line":
            data.fill = None
        return data


class ChoroplethCountry(Choropleth):
    name = 'ChartJs Choropleth Country'
    geo_map = "https://raw.githubusercontent.com/markmarkoh/datamaps/master/src/js/data/fra.json"
    _option_cls = OptChartJs.OptionsGeo
    builder_name = "GeoChoroplethCountry"

    @property
    def options(self) -> OptChartJs.OptionsGeo:
        """
        Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options
