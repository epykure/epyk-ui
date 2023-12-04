#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from epyk.core.py import primitives
from epyk.core.py import types
from epyk.core.html import Html
from epyk.core.js import JsUtils
from epyk.core.html.options import OptChartGoogle


class Chart(Html.Html):
    name = 'Google Chart'
    tag = "div"
    requirements = ('google-charts',)
    _option_cls = OptChartGoogle.OptionGoogle

    def __init__(self, page: primitives.PageModel, data, width, height, html_code, options, profile):
        self.height = height[0]
        super(Chart, self).__init__(page, data, html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
        self._d3, self._chart, self._datasets, self._options, self._data_attrs, self._attrs = None, None, [], None, {}, {}
        self.style.css.margin_top = 10

    @property
    def shared(self) -> OptChartGoogle.OptionsChartSharedGoogle:
        """All the common properties shared between all the charts.
        This will ensure a compatibility with the plot method.

          Usage::

            line = page.ui.charts.bb.bar()
            line.shared.x_label("x axis")
        """
        return OptChartGoogle.OptionsChartSharedGoogle(self)

    @property
    def options(self) -> OptChartGoogle.OptionGoogle:
        """Property to the series options"""
        return super().options

    @property
    def chartId(self):
        """Return the Javascript variable of the chart"""
        return "%s_obj" % self.htmlCode

    def build(self, data: types.JS_DATA_TYPES = None, options: types.JS_DATA_TYPES = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """

        :param data:
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param component_id: String. Optional. A DOM component reference in the page.
        :param stop_state: Remove the top panel for the component state (error, loading...)
        """
        return '''
%(chartId)s = google.charts.setOnLoadCallback( (function(){
var data = new google.visualization.DataTable();
var chartOptions = %(options)s; 
delete chartOptions.type;

var chartData = %(data)s;
data.addColumn('string', chartData.x);
chartData.series.forEach(function(col){data.addColumn('number', col)})
data.addRows(chartData.datasets);
var chart = new google.visualization.%(type)s(%(varId)s);
chart.draw(data, chartOptions);
return chart
}));
''' % {
            'chartId': self.chartId, 'varId': component_id or self.dom.varId,
            'options': self.options.config_js(options), 'data': JsUtils.dataFlows(data, dataflows, self.page),
            'type': self.options.type}

    def define(self, options: types.JS_DATA_TYPES = None, dataflows: List[dict] = None) -> str:
        """Not yet defined for this chart"""
        return ""

    def colors(self, colors):
        raise NotImplementedError()

    def labels(self, values: list):
        """Set the chart labels.

        :param values: The label values.
        """
        self._vals = {"x": [], "datasets": [], "series": []}
        for v in values:
            self._vals["datasets"].append([str(v)])

    def add_dataset(self, data, label, colors=None, opacity=None, kind=None):
        """
 
        :param data:
        :param label:
        :param colors:
        :param opacity:
        :param kind:
        """
        self._vals["x"].append(label)
        self._vals["series"].append(label)
        for i, val in enumerate(data):
            self._vals["datasets"][i].append(val)

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


class ChartLine(Chart):
    pass
