from epyk.core.py import types
from epyk.core.html import geo
from epyk.interfaces import Arguments

from pathlib import Path


#
COUNTRY_MAP = {
    "France": "法国",
    "United_Kingdom": "英国",
}

# Maps will be picked up here by default.
MAP_CDNJS = "https://cdn.jsdelivr.net/npm"


class ECharts:

    def __init__(self, ui):
        self.page = ui.page
        self.chartFamily = "ECharts"

    @property
    def choropleths(self):
        """ """
        return Choropleth(self)

    @property
    def bubbles(self):
        return BubbleMaps(self)


class Choropleth:

    def __init__(self, ui):
        self.page = ui.page
        self.chartFamily = "ECharts"

    def map(self, map_path: str = None, map_alias: str = None, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
              options: dict = None, html_code: str = None, **kwargs) -> geo.GeoECharts.Maps:

        if map_path is None:
            # In this case map will be picked up from echarts-countries based on the alias name
            self.page.imports.addPackage("geojson-%s" % map_alias, {
                'version': '1.0.5',
                'req': [{'alias': 'echarts'}],
                'modules': [
                    {'script': "%s.js" % map_alias, 'path': 'echarts-countries-js@%(version)s/echarts-countries-js/',
                     'cdnjs': MAP_CDNJS}
                ]})
            self.page.jsImports.add("geojson-%s" % map_alias)
            map_alias = COUNTRY_MAP.get(map_alias, map_alias)
        else:
            file_path = Path(map_path)
            if not file_path.exists():
                raise

            self.page.js.customFile(file_path.name, path=str(file_path.parent),
                                    requirements=[{'alias': 'echarts'}], absolute_path=True, authorize=True)

        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"_ek": {"chart": {"x_axis": x_axis, "y_columns": y_columns}}})
        Arguments.set_default(dfl_options, {
            "geo": {"map": map_alias, "roam": True},
            "tooltip": {"triggerOn": "click"},
            "_ek": {"series": {"type": "map", "geoIndex": 0}}
        })
        data = self.page.data.chartJs.xy(record, y_columns, x_axis)
        chart = geo.GeoECharts.Maps(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        if data:
            for i, dataset in enumerate(data['datasets']):
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["_ek"]["chart"]["type"]
                s.data = [[v["x"], v["y"]] for v in dataset['data']]
                Arguments.update_series(s, dfl_options)
        return chart

    def world(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
            options: dict = None, html_code: str = None, map_path: str = None, **kwargs) -> geo.GeoECharts.Maps:
        geo = self.map(record=record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height,
                       options=options, html_code=html_code, map_path=map_path, map_alias="world", **kwargs)
        return geo

    def china(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
            options: dict = None, html_code: str = None, map_path: str = None, **kwargs) -> geo.GeoECharts.Maps:
        geo = self.map(record=record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height,
                       options=options, html_code=html_code, map_path=map_path, map_alias="china", **kwargs)
        return geo

    def country(self, name: str, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
            options: dict = None, html_code: str = None, map_path: str = None, **kwargs) -> geo.GeoECharts.Maps:
        geo = self.map(record=record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height,
                       options=options, html_code=html_code, map_path=map_path, map_alias=name, **kwargs)
        return geo


class BubbleMaps:

    def __init__(self, ui):
        self.page = ui.page
        self.chartFamily = "ECharts"

    def map(self, map_path: str = None, map_alias: str = None, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
              options: dict = None, html_code: str = None, **kwargs) -> geo.GeoECharts.Maps:

        if map_path is None:
            # In this case map will be picked up from echarts-countries based on the alias name
            self.page.imports.addPackage("geojson-%s" % map_alias, {
                'version': '1.0.5',
                'req': [{'alias': 'echarts'}],
                'modules': [
                    {'script': "%s.js" % map_alias, 'path': 'echarts-countries-js@%(version)s/echarts-countries-js/',
                     'cdnjs': MAP_CDNJS}
                ]})
            self.page.jsImports.add("geojson-%s" % map_alias)
            map_alias = COUNTRY_MAP.get(map_alias, map_alias)
        else:
            file_path = Path(map_path)
            if not file_path.exists():
                raise

            self.page.js.customFile(file_path.name, path=str(file_path.parent), requirements=[{'alias': 'echarts'}],
                                    absolute_path=True, authorize=True)

        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = Arguments.clean_opt(options, {"_ek": {"chart": {"x_axis": x_axis, "y_columns": y_columns}}})
        Arguments.set_default(dfl_options, {
            "geo": {"map": map_alias, "roam": True},
            "tooltip": {"triggerOn": "click"},
            "_ek": {"series": {"type": "scatter", "postEffect": {"enable": True},  "large": True, "silent": True,
                               "coordinateSystem": "geo", "blendMode": 'source-over', "symbolSize": 5}}
        })
        data = self.page.data.chartJs.xy(record, y_columns, x_axis)
        chart = geo.GeoECharts.Maps(self.page, width, height, html_code, dfl_options, profile)
        chart.colors(self.page.theme.charts)
        if data:
            for i, dataset in enumerate(data['datasets']):
                s = chart.options.series
                s.name = dataset['label']
                s.type = dfl_options["_ek"]["chart"]["type"]
                s.data = [[v["x"], v["y"]] for v in dataset['data']]
                Arguments.update_series(s, dfl_options)
        return chart

    def world(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
            options: dict = None, html_code: str = None, map_path: str = None, **kwargs) -> geo.GeoECharts.Maps:
        geo = self.map(record=record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height,
                       options=options, html_code=html_code, map_path=map_path, map_alias="world", **kwargs)
        return geo

    def china(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
            options: dict = None, html_code: str = None, map_path: str = None, **kwargs) -> geo.GeoECharts.Maps:
        geo = self.map(record=record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height,
                       options=options, html_code=html_code, map_path=map_path, map_alias="china", **kwargs)
        return geo

    def country(self, name: str, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
            options: dict = None, html_code: str = None, map_path: str = None, **kwargs) -> geo.GeoECharts.Maps:
        geo = self.map(record=record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height,
                       options=options, html_code=html_code, map_path=map_path, map_alias=name, **kwargs)
        return geo