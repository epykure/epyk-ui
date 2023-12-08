from epyk.core.py import types
from epyk.core.html import graph
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html


class Highcharts:

    def __init__(self, ui):
        self.page = ui.page
        self.chartFamily = "Highcharts"

    def plot(self, record: list = None, y: list = None, x: str = None, kind: str = "line",
             profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (330, "px"), options: dict = None,
             html_code: str = None, **kwargs
             ) -> graph.GraphChartJs.Chart:
        """Generic way to define HighCharts charts.

        :tags:
        :categories:

        `ChartJs <https://www.highcharts.com/>`_

        :param record: Optional. The list of dictionaries with the input data
        :param y: Optional. The columns corresponding to keys in the dictionaries in the record
        :param x: Optional. The column corresponding to a key in the dictionaries in the record
        :param kind: Optional. The chart type
        :param profile: Optional. A flag to set the component performance storage
        :param width: Optional. The width of the component in the page, default (100, '%')
        :param height: Optional. The height of the component in the page, default (330, "px")
        :param options: Optional. Specific Python options available for this component
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        """
        if y is not None and not isinstance(y, list):
            y = [y]
        if hasattr(self, kind):
            return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width,
                                       height=height,
                                       options=options, html_code=html_code)

        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"series": [], "chart": {"type": kind}, "title": {"text": ""}}
        dfl_options.update({'y_columns': y or [], 'x_axis': x, 'commons': {'fill': None}})
        if options is not None:
            dfl_options.update(options)
        data = self.page.data.chartJs.y(record or [], y, x)
        chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        return chart

    def line(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
             options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"series": [], "chart": {"type": "line"}, "title": {"text": ""}}
        dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
        if options is not None:
            dfl_options.update(options)
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        if data:
            chart.options.xAxis.categories = data["labels"]
            for dataset in data['datasets']:
                s = chart.options.series_
                s.name = dataset['label']
                s.data = dataset['data']
        return chart

    def bar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
            options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"series": [], "chart": {"type": "column"}, "title": {"text": ""}}
        dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
        if options is not None:
            dfl_options.update(options)
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        chart.builder_name = "HchartsBar"
        if data:
            chart.options.xAxis.categories = data["labels"]
            for dataset in data['datasets']:
                s = chart.options.series_
                s.name = dataset['label']
                s.data = dataset['data']
        return chart

    def hbar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
             options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"series": [], "chart": {"type": "bar"}, "title": {"text": ""}}
        dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
        if options is not None:
            dfl_options.update(options)
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        chart.builder_name = "HchartsBar"
        if data:
            chart.options.xAxis.categories = data["labels"]
            for dataset in data['datasets']:
                s = chart.options.series_
                s.name = dataset['label']
                s.data = dataset['data']
        return chart

    def area(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
             options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"series": [], "chart": {"type": "area"}, "title": {"text": ""}}
        dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
        if options is not None:
            dfl_options.update(options)
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        if data:
            chart.options.xAxis.categories = data["labels"]
            for dataset in data['datasets']:
                s = chart.options.series_
                s.name = dataset['label']
                s.data = dataset['data']
        return chart

    def pie(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
            options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"series": [], "chart": {"type": "pie"}, "title": {"text": ""}}
        dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'colorByPoint': True},
                            'props': {2: {"selected": True, "slice": True}}})
        if options is not None:
            dfl_options.update(options)
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "HchartsPie"
        chart.colors(self.page.theme.charts)
        if data:
            for dataset in data['datasets']:
                s = chart.options.series_
                s.name = dataset['label']
                s.data = [{"name": data["labels"][i], "y": d} for i, d in enumerate(dataset['data'])]
        return chart

    def donut(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
              options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"series": [], "chart": {"type": "pie"}, "title": {"text": ""}}
        dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
        if options is not None:
            dfl_options.update(options)
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "HchartsPie"
        chart.colors(self.page.theme.charts)
        chart.options.plotOptions.pie.innerSize = 50
        if data:
            for dataset in data['datasets']:
                s = chart.options.series_
                s.name = dataset['label']
                s.data = [{"name": data["labels"][i], "y": d} for i, d in enumerate(dataset['data'])]
        return chart

    def gauge(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
              options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"series": [], "chart": {"type": "pie"}, "title": {"text": ""}}
        dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
        if options is not None:
            dfl_options.update(options)
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "HchartsPie"
        chart.colors(self.page.theme.charts)
        chart.options.plotOptions.pie.dataLabels.enabled = True
        chart.options.plotOptions.pie.dataLabels.distance = -50
        chart.options.plotOptions.pie.startAngle = -90
        chart.options.plotOptions.pie.endAngle = 90
        chart.options.plotOptions.pie.center = ['50%', '75%']
        if data:
            for dataset in data['datasets']:
                s = chart.options.series_
                s.name = dataset['label']
                s.data = [{"name": data["labels"][i], "y": d} for i, d in enumerate(dataset['data'])]
        return chart

    def bubble(self, record=None, y_columns: list = None, x_axis: str = None, r_values: list = None,
               profile: types.PROFILE_TYPE = None,
               width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
               options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"series": [], "chart": {"type": "bubble"}, "title": {"text": ""}}
        dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None},
                            'z_columns': None, 'rDim': r_values})
        if options is not None:
            dfl_options.update(options)
        data = self.page.data.chartJs.xyz(record, y_columns, x_axis, r_values)
        chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
        chart.options.chart.zoomType = "xy"
        chart.builder_name = "HchartsBubble"
        chart.colors(self.page.theme.charts)
        if data:
            for dataset in data['datasets']:
                s = chart.options.series_
                s.name = dataset['label']
                s.data = [{"x": d["x"], "y": d["y"], "z": d["r"]} for i, d in enumerate(dataset['data'])]
        return chart
