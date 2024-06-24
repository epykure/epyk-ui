from epyk.core.py import types
from epyk.core.html import graph
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html
from epyk.core.js import JsUtils


class ECharts:

    def __init__(self, ui):
        self.page = ui.page
        self.chartFamily = "ECharts"

    def plot(self, record: list = None, y: list = None, x: str = None, kind: str = "line",
             profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (330, "px"), options: dict = None,
             html_code: str = None, **kwargs
             ) -> graph.GraphECharts.ECharts:
        if y is not None and not isinstance(y, list) and not JsUtils.isJsData(y):
          y = [y]
        if kind and hasattr(self, kind):
            return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                                       options=options, html_code=html_code, **kwargs)

        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"ek": {"chart": {"type": kind, "x_axis": x, "y_columns": y}}})
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
                Arguments.update_series(s, dfl_options)
        return chart

    def line(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
             options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"ek": {"chart": {"type": "line", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        chart.options.toolbox.feature.saveAsImage = {}
        chart.options.yAxis.type = dfl_options.get("yAxis", {}).get("type", 'value')
        chart.options.tooltip.trigger = 'axis'
        if data:
            chart.options.xAxis.data = data["labels"]
            chart.options.xAxis.type = "category"
            for dataset in data['datasets']:
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["ek"]["chart"]["type"]
                s.data = dataset['data']
                Arguments.update_series(s, dfl_options)
        return chart

    def bar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
             options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"ek": {"chart": {"type": "bar", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        chart.options.yAxis.type = dfl_options.get("yAxis", {}).get("type", 'value')
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            chart.options.xAxis.data = data["labels"]
            chart.options.xAxis.type = dfl_options.get("xAxis", {}).get("type", 'category')
            for dataset in data['datasets']:
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["ek"]["chart"]["type"]
                s.data = dataset['data']
                Arguments.update_series(s, dfl_options)
        return chart

    def pie(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
            html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"ek": {"chart": {"type": "pie", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.xy(record, y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "EkPieECharts"
        chart.colors(self.page.theme.charts)
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            for dataset in data['datasets']:
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["ek"]["chart"]["type"]
                s.data = [{'name': v["x"], 'value': v["y"]} for v in dataset['data']]
                Arguments.update_series(s, dfl_options)
        return chart

    def donut(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
              html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"ek": {
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
                s.type = dfl_options["ek"]["chart"]["type"]
                s.data = [{'name': v["x"], 'value': v["y"]} for v in dataset['data']]
                Arguments.update_series(s, dfl_options)
        return chart

    def gauge(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
              html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"ek": {
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
                s.type = dfl_options["ek"]["chart"]["type"]
                s.data = [{'name': v["x"], 'value': v["y"]} for v in dataset['data']]
                Arguments.update_series(s, dfl_options)
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
        dfl_options = Arguments.clean_opt(options, {"ek": {"chart": {"type": "bar", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.options.yAxis.type = dfl_options.get("yAxis", {}).get("type", "category")
        chart.options.xAxis.type = dfl_options.get("xAxis", {}).get("type", "value")
        chart.options.xAxis.position = dfl_options.get("xAxis", {}).get("position", "top")
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
                s.type = dfl_options["ek"]["chart"]["type"]
                s.data = [{"value": d, "label": {"position": "right"}} for d in dataset['data']]
                Arguments.update_series(s, dfl_options)
        return chart

    def polar(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
              options: dict = None, html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {
            "ek": {
                "chart": {"type": "pie", "x_axis": x_axis, "y_columns": y_columns},
                "series": {
                    "roseType": "radius", "radius": [20, 140], "center": ['50%', '50%'],
                    "itemStyle": {"borderRadius": 5}}
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
                s.type = dfl_options["ek"]["chart"]["type"]
                s.data = [{'name': v["x"], 'value': v["y"]} for v in dataset['data']]
                Arguments.update_series(s, dfl_options)
        return chart

    def scatter(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
              options: dict = None, html_code: str = None, **kwargs) -> graph.GraphECharts.ECharts:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"ek": {"chart": {"type": "scatter", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.xy(record, y_columns, x_axis)
        chart = graph.GraphECharts.ECharts(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        chart.options.yAxis.type = dfl_options.get("yAxis", {}).get("type", "value")
        chart.options.xAxis.type = dfl_options.get("xAxis", {}).get("type", "value")
        chart.builder_name = "EkScatterECharts"
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            for i, dataset in enumerate(data['datasets']):
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["ek"]["chart"]["type"]
                s.data = [[v["x"], v["y"]] for v in dataset['data']]
                Arguments.update_series(s, dfl_options)
        return chart

    def radar(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
              html_code: str = None, **kwargs) -> graph.GraphECharts.EChartsRadar:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"ek": {"chart": {"type": "radar", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
        chart = graph.GraphECharts.EChartsRadar(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "EkRadarECharts"
        chart.colors(self.page.theme.charts)
        chart.options.toolbox.feature.saveAsImage = {}
        if data:
            chart.options.radar.indicator = [{"name": l} for l in data["labels"]]
            s = chart.options.series
            s.type = dfl_options["ek"]["chart"]["type"]
            s.data = []
            for dataset in data['datasets']:
                new_series = {"value": dataset['data'], "name": dataset['label']}
                if "series" in dfl_options["ek"]:
                    Arguments.rupdate(new_series, dfl_options["ek"]["series"])
                if "names" in dfl_options["ek"] and new_series["name"] in dfl_options["ek"]["names"]:
                    Arguments.rupdate(new_series, dfl_options["ek"]["names"][new_series["name"]])
                s.data.append(new_series)
        return chart

    def sunburst(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
              html_code: str = None, **kwargs) -> graph.GraphECharts.EChartsTreeMap:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"ek": {"chart": {"type": "sunburst", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.to_hyr(record or [], x_axis.split("/"), y_columns)
        chart = graph.GraphECharts.EChartsTreeMap(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "EkTreeECharts"
        chart.colors(self.page.theme.charts)
        if data:
            chart.options.series.type = dfl_options["ek"]["chart"]["type"]
            chart.options.series.radius = [0, '90%']
            chart.options.series.data = data
        chart.options.toolbox.feature.saveAsImage = {}
        return chart

    def treemap(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
              html_code: str = None, **kwargs) -> graph.GraphECharts.EChartsTreeMap:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"ek": {"chart": {"type": "treemap", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.to_hyr(record or [], x_axis.split("/"), y_columns)
        chart = graph.GraphECharts.EChartsTreeMap(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "EkTreeECharts"
        chart.colors(self.page.theme.charts)
        if data:
            chart.options.series.type = dfl_options["ek"]["chart"]["type"]
            chart.options.series.data = data
        chart.options.toolbox.feature.saveAsImage = {}
        return chart

    def tree(self, record: list = None, y_columns: list = None, x_axis: str = None,
                profile: types.PROFILE_TYPE = None,
                width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
                html_code: str = None, **kwargs) -> graph.GraphECharts.EChartsTreeMap:
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {
            "ek": {"chart": {"type": "tree", "x_axis": x_axis, "y_columns": y_columns}}})
        data = self.page.data.to_hyr(record or [], x_axis.split("/"), y_columns)
        chart = graph.GraphECharts.EChartsTreeMap(self.page, width, height, html_code, dfl_options, profile)
        chart.builder_name = "EkTreeECharts"
        chart.colors(self.page.theme.charts)
        if data:
            chart.options.series.type = dfl_options["ek"]["chart"]["type"]
            chart.options.series.data = data
        chart.options.toolbox.feature.saveAsImage = {}
        return chart
