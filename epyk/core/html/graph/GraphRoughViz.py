#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.js.packages import JsD3
from epyk.core.js import JsUtils
from epyk.core.html.options import OptChartRoughViz
from epyk.core.py import types as etypes


class RoughViz(MixHtmlState.HtmlOverlayStates, Html.Html):
    requirements = ('rough-viz',)
    name = 'rough_viz'
    _chart__type = 'Line'
    _option_cls = OptChartRoughViz.RoughVizLine
    builder_name = "RvCharts"

    def __init__(self, page, width, height, html_code, options, profile):
        super(RoughViz, self).__init__(
            page, [], html_code=html_code, profile=profile, options=options,
            css_attrs={"width": width, "height": height})
        self._d3, self._chart, self._datasets, self._data_attrs, self._attrs = None, None, [], {}, {}
        self.chartId = "%s_obj" % self.htmlCode
        self.options.element = "#%s" % self.htmlCode

    @property
    def shared(self) -> OptChartRoughViz.OptionsChartSharedRoughViz:
        """
        All the common properties shared between all the charts.
        This will ensure a compatibility with the plot method.

        Usage::

          b = page.ui.charts.roughviz.plot(languages, y=["rating", 'change'], x='name', width=300)
          b.shared.x_label("Test X")
          b.shared.y_label("Test Y")
        """
        return OptChartRoughViz.OptionsChartSharedRoughViz(self)

    @property
    def options(self) -> OptChartRoughViz.RoughVizLine:
        """ Chart specific options. """
        return super().options

    @property
    def datasets(self):
        """ Chart datasets """
        return self._datasets

    @property
    def d3(self) -> JsD3.D3Select:
        """ Property to the D3 library. """
        if self._d3 is None:
            self._d3 = JsD3.D3Select(
                page=self.page, component=self, selector="d3.select('#%s')" % self.htmlCode, set_var=False)
        return self._d3

    def add_dataset(self, data: list, label: str = "", colors: list = None, opacity: float = None, kind: float = None):
        """
        Add a new Dataset to the chart list of Datasets.

        Related Pages:

          https://www.chartjs.org/docs/latest/developers/updates.html

        :param data: The list of points (float)
        :param label: Optional. The list of points (float)
        :param colors: Optional. The color for this series. Default the global definition
        :param opacity: Optional. The opacity level for the content
        """
        dataset = self.options.data.add(label, data)
        return dataset

    @Html.jformatter("roughviz")
    def build(self, data: etypes.JS_DATA_TYPES = None, options: etypes.OPTION_TYPE = None,
              profile: etypes.PROFILE_TYPE = False, component_id: str = None, stop_state: bool = True):
        """
        Update the chart with context and / or data changes.

        :param data: Optional. The full datasets object expected by ChartJs
        :param options: Optional. Specific Python options available for this component
        :param profile:Optional. A flag to set the component performance storage
        :param component_id: Not used
        :param stop_state: Remove the top panel for the component state (error, loading...)
        """
        if data is not None:
            builder_fnc = JsUtils.jsWrap("%s(%s, %s)" % (
                self.builder_name, JsUtils.jsConvertData(data, None),
                self.options.config_js(options).toStr()), profile).toStr()
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(component_id)
            options = options or {}
            options["data"] = data
            return '''%(chartId)s.data = %(builder)s; %(state)s''' % {
                "chartId": self.chartId, 'builder': builder_fnc, "state": state_expr}

        return '''%(chartId)s = new roughViz.%(chartType)s(%(config)s)''' % {
            "chartId": self.chartId, "chartType": self._chart__type, "hmlCode": component_id or self.htmlCode,
            'config': self.options.config_js(options)}

    def colors(self, hex_values: List[str]):
        ...

    def labels(self, labels: list, series_id: str = None):
        ...

    def define(self, options: etypes.JS_DATA_TYPES = None) -> str:
        """ Not yet defined for this chart """
        return ""

    def __str__(self):
        self.page.properties.js.add_builders(self.build())
        return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())


class RoughVizBar(RoughViz):
    _chart__type = 'Bar'
    _option_cls = OptChartRoughViz.RoughVizBar


class RoughVizPie(RoughViz):
    _chart__type = 'Pie'
    _option_cls = OptChartRoughViz.RoughVizPie


class RoughVizDonut(RoughViz):
    _chart__type = 'Donut'
    _option_cls = OptChartRoughViz.RoughVizPie


class RoughVizBarH(RoughViz):
    _chart__type = 'BarH'
    _option_cls = OptChartRoughViz.RoughVizBar


class RoughVizScatter(RoughViz):
    _chart__type = 'Scatter'
    _option_cls = OptChartRoughViz.RoughVizScatter
