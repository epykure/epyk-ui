from epyk.core.py import types
from epyk.core.html import graph
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html


import collections.abc


def rupdate(d: dict, u: dict) -> dict:
    """Recursive nested dict update

    :param d: source dictionary
    :param u: dictionary to be merged
    """
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = rupdate(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def clean_opt(inputs: dict, options: dict) -> dict:
    """Clean the ECharts options.

    :param inputs: Input parameters
    :param options: New chart options
    """
    if inputs:
        if "series" in inputs:
            options["_ek"]["series"] = inputs["series"]
            del inputs["series"]

        if "names" in inputs:
            options["_ek"]["names"] = inputs["names"]
            del inputs["names"]

        options.update(inputs)
    return options


def update_series(series, options: dict):
    """Update series object with input chart options.
    This will be used when common series properties are defined or some specific named properties are defined
    for a series.

    :param series:
    :param options:
    """
    if options and "series" in options["_ek"]:
        series.set_attrs(options["_ek"]["series"])
    if "names" in options["_ek"] and series.name in options["_ek"]["names"]:
        series.set_attrs(options["_ek"]["names"][series.name])


class ECharts:

    def __init__(self, ui):
        self.page = ui.page
        self.chartFamily = "ECharts"

    def plot(self, record: list = None, y: list = None, x: str = None, kind: str = "line",
             profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (330, "px"), options: dict = None,
             html_code: str = None, **kwargs
             ) -> graph.GraphECharts.ECharts:
        if y is not None and not isinstance(y, list):
          y = [y]
        if kind and hasattr(self, kind):
            return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                                       options=options, html_code=html_code, **kwargs)

        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = clean_opt(options, {"_ek": {"chart": {"type": kind, "x_axis": x, "y_columns": y}}})
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        chart.builder_name = "EkPlotECharts"
        chart.options.toolbox.feature.saveAsImage = {}
        if record:
            for series in record:
                s = chart.options.series
                s.name = series.get("name")
                s.type = kind
                s.data = series.get("data", [])
                update_series(s, dfl_options)
        return chart

    def line(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
             options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = clean_opt(options, {"_ek": {"chart": {"type": "line", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        chart.options.toolbox.feature.saveAsImage = {}
        chart.options.yAxis.type = 'value'
        chart.options.tooltip.trigger = 'axis'
        if data:
            chart.options.xAxis.data = data["labels"]
            chart.options.xAxis.type = "category"
            for dataset in data['datasets']:
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["_ek"]["chart"]["type"]
                s.data = dataset['data']
                update_series(s, dfl_options)
        return chart

    def bar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
             options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = clean_opt(options, {"_ek": {"chart": {"type": "bar", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        chart.options.yAxis.type = 'value'
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            chart.options.xAxis.data = data["labels"]
            chart.options.xAxis.type = "category"
            for dataset in data['datasets']:
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["_ek"]["chart"]["type"]
                s.data = dataset['data']
                update_series(s, dfl_options)
        return chart

    def pie(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
            html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = clean_opt(options, {"_ek": {"chart": {"type": "pie", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.xy(record, y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "EkPieECharts"
        chart.colors(self.page.theme.charts)
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            for dataset in data['datasets']:
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["_ek"]["chart"]["type"]
                s.data = [{'name': v["x"], 'value': v["y"]} for v in dataset['data']]
                update_series(s, dfl_options)
        return chart

    def donut(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
              html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = clean_opt(options, {"_ek": {
            "chart": {"type": "pie", "x_axis": x_axis, "y_columns": y_columns}, "series": {"radius": ['40%', '70%']}}})
        data = self.page.data.chartJs.xy(record, y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "EkPieECharts"
        chart.colors(self.page.theme.charts)
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            for dataset in data['datasets']:
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["_ek"]["chart"]["type"]
                s.data = [{'name': v["x"], 'value': v["y"]} for v in dataset['data']]
                update_series(s, dfl_options)
        return chart

    def gauge(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
              html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = clean_opt(options, {"_ek": {
            "chart": {"type": "pie", "x_axis": x_axis, "y_columns": y_columns},
            "series": {"radius": ['40%', '70%'], "center": ['50%', '70%'], "startAngle": 180, "endAngle": 360}
        }})
        data = self.page.data.chartJs.xy(record, y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "EkPieECharts"
        chart.colors(self.page.theme.charts)
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            for dataset in data['datasets']:
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["_ek"]["chart"]["type"]
                s.data = [{'name': v["x"], 'value': v["y"]} for v in dataset['data']]
                update_series(s, dfl_options)
        return chart

    def area(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
             html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        if options is None:
            options = {}
        dflt_options = {"smooth": True, "symbol": 'none', "areaStyle": {}}
        for k, v in dflt_options.items():
            if k not in options.get("series", {}):
                options.setdefault("series", {})[k] = v
        return self.line(record, y_columns, x_axis, profile, width, height, options, html_code, **kwargs)

    def step(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
             html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        if options is None:
            options = {}
        if "step" not in options.get("series", {}):
            options.setdefault("series", {})["step"] = "start"
        return self.line(record, y_columns, x_axis, profile, width, height, options, html_code, **kwargs)

    def hbar(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
             html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = clean_opt(options, {"_ek": {"chart": {"type": "bar", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.options.yAxis.type = "category"
        chart.options.xAxis.type = "value"
        chart.options.xAxis.position = "top"
        chart.colors(self.page.theme.charts)
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            chart.options.yAxis.data = data["labels"]
            chart.options.yAxis.axisTick.show = False
            chart.options.yAxis.axisLine.show = False
            chart.options.yAxis.splitLine.show = False
            chart.options.yAxis.axisLabel.show = False
            for dataset in data['datasets']:
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["_ek"]["chart"]["type"]
                s.data = [{"value": d, "label": {"position": "right"}} for d in dataset['data']]
                update_series(s, dfl_options)
        return chart

    def polar(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
              options: dict = None, html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = clean_opt(options, {
            "_ek": {
                "chart": {"type": "pie", "x_axis": x_axis, "y_columns": y_columns},
                "series": {"roseType": "radius", "radius": [20, 140], "center": ['50%', '50%'], "itemStyle": {"borderRadius": 5}}
            }})
        data = self.page.data.chartJs.xy(record, y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "EkPieECharts"
        chart.colors(self.page.theme.charts)
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            for i, dataset in enumerate(data['datasets']):
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["_ek"]["chart"]["type"]
                s.data = [{'name': v["x"], 'value': v["y"]} for v in dataset['data']]
                update_series(s, dfl_options)
        return chart

    def scatter(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
              options: dict = None, html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = clean_opt(options, {"_ek": {"chart": {"type": "scatter", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.xy(record, y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        chart.options.xAxis.type = "value"
        chart.options.yAxis.type = "value"
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            for i, dataset in enumerate(data['datasets']):
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["_ek"]["chart"]["type"]
                s.data = [[v["x"], v["y"]] for v in dataset['data']]
                update_series(s, dfl_options)
        return chart

    def radar(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
              html_code: str = None, **kwargs) -> graph.GraphECharts.EChartsRadar:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = clean_opt(options, {"_ek": {"chart": {"type": "radar", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphECharts.EChartsRadar(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "EkRadarECharts"
        chart.colors(self.page.theme.charts)
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            chart.options.radar.indicator = [{"name": l} for l in data["labels"]]
            s = chart.options.series
            s.type = dfl_options["_ek"]["chart"]["type"]
            s.data = []
            for dataset in data['datasets']:
                new_series = {"value": dataset['data'], "name": dataset['label']}
                if "series" in dfl_options["_ek"]:
                    rupdate(new_series, dfl_options["_ek"]["series"])
                if "names" in dfl_options["_ek"] and new_series["name"] in dfl_options["_ek"]["names"]:
                    rupdate(new_series, dfl_options["_ek"]["names"][new_series["name"]])
                s.data.append(new_series)
        return chart
