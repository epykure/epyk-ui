
from typing import Union
from epyk.core.html import geo
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html


class ChartJs:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "ChartJs"

  @property
  def choropleths(self):
    """ """
    return Choropleth(self)

  @property
  def bubbleMap(self):
    return BubbleMaps(self)


class BubbleMaps:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "ChartJs"

  def world(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
            options: dict = None, width: Union[int, tuple] = (100, "%"),
            height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoChartJs.Choropleth`

    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    geo_chart = geo.GeoChartJs.Choropleth(self.page, width, height, html_code, options or {}, profile)
    geo_chart._attrs['type'] = "bubbleMap"

    geo_chart.options.scale.projection = "mercator"
    geo_chart.options.geo.radiusScale.display = True
    geo_chart.options.geo.radiusScale.size = [1, 20]
    geo_chart.options.showOutline = True
    geo_chart.options.legend.display = False
    geo_chart.options.showGraticule = True
    return geo_chart

  def us(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
         options: dict = None, width: Union[int, tuple] = (100, "%"),
         height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoChartJs.Choropleth`

    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    geo_chart = geo.GeoChartJs.ChoroplethUs(
      self.page, width, height, html_code, options or {}, profile)
    geo_chart._attrs['type'] = "bubbleMap"
    geo_chart.options.scale.projection = "albersUsa"
    geo_chart.options.geo.radiusScale.display = True
    geo_chart.options.geo.radiusScale.size = [1, 20]
    geo_chart.options.showOutline = True
    geo_chart.options.legend.display = False
    geo_chart.options.showGraticule = True
    return geo_chart


class Choropleth:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "ChartJs"

  def us(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
         options: dict = None, width: Union[int, tuple] = (100, "%"),
         height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Usage::

      records = [{"name": "Nevada", "value": 23}, {"name": "Texas", "value": 60}]
      us = page.ui.geo.chartJs.choropleths.us(records, y_columns=["value"], x_axis="name")
      page.ui.button("Click").click([us.build({"Louisiana": 40})])

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoChartJs.Choropleth`

    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    geo_chart = geo.GeoChartJs.ChoroplethUs(
      self.page, width, height, html_code, options or {}, profile)
    geo_chart.options.geo.colorScale.display = True
    geo_chart.options.geo.colorScale.quantize = 5
    geo_chart.options.geo.colorScale.position = "bottom"
    geo_chart.options.geo.colorScale.legend.position = "bottom-right"
    geo_chart.options.showOutline = True
    geo_chart.options.legend.display = False
    geo_chart.options.showGraticule = True

    if record is not None:
      geo_chart._vals = {rec[x_axis]: rec[y_columns[0]] for rec in record}
    else:
      geo_chart._vals = {}

    if self.page.imports.pkgs.chart_js_extensions.geo.version[0].startswith("3."):
      geo_chart.options.scale.projection = "albersUsa"
    else:
      geo_chart.options.scales.projection.axis = "x"
      geo_chart.options.maintainAspectRatio = True
      geo_chart.options.scales.projection.projection = "albersUsa"

    return geo_chart

  def world(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
            options: dict = None, width: Union[int, tuple] = (100, "%"),
            height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Usage::

      records = [{"name": "Italy", "value": 23}]
      wl = page.ui.geo.chartJs.choropleths.world(records, y_columns=["value"], x_axis="name")
      page.ui.button("Click").click([
        wl.build({"Germany": 23, "Spain": 40, "Italy": 23}),
        us.build({"Louisiana": 40}),
        uk.build({"Birmingham": 40}),
      ])

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoChartJs.Choropleth`

    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    geo_chart = geo.GeoChartJs.Choropleth(self.page, width, height, html_code, options or {}, profile)
    if record is not None:
      geo_chart._vals = {rec[x_axis]: rec[y_columns[0]] for rec in record}
    else:
      geo_chart._vals = {}

    if self.page.imports.pkgs.chart_js_extensions.geo.version[0].startswith("3."):
      geo_chart.options.scales.xy.projection = "equalEarth"
    else:
      geo_chart.options.scales.projection.axis = "x"
      geo_chart.options.maintainAspectRatio = True
      geo_chart.options.scales.projection.projection = "equalEarth"

    geo_chart.options.showOutline = True
    geo_chart.options.plugins.legend.display = False
    geo_chart.options.showGraticule = True
    return geo_chart

  def country(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
              options: dict = None, width: Union[int, tuple] = (100, "%"),
              height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Usage::

      records = [{"name": "Liverpool", "value": 23}, {"name": "Leeds", "value": 60}]
      uk = page.ui.geo.chartJs.choropleths.uk(records, y_columns=["value"], x_axis="name")
      page.ui.button("Click").click([
        uk.build({"Birmingham": 40}),
      ])

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoChartJs.Choropleth`

    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    geo_chart = geo.GeoChartJs.ChoroplethCountry(self.page, width, height, html_code, options or {}, profile)

    if self.page.imports.pkgs.chart_js_extensions.geo.version[0].startswith("3."):
      geo_chart.options.scales.xy.projection = "mercator"
    else:
      geo_chart.options.scales.projection.axis = "x"
      geo_chart.options.maintainAspectRatio = True
      geo_chart.options.scales.projection.projection = "mercator"

    if record is not None:
      geo_chart._vals = {rec[x_axis]: rec[y_columns[0]] for rec in record}
    else:
      geo_chart._vals = {}

    geo_chart.options.geo.colorScale.display = True
    geo_chart.options.showOutline = True
    geo_chart.options.legend.display = False
    geo_chart.options.showGraticule = False
    return geo_chart

  def fr(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
         options: dict = None, width: Union[int, tuple] = (100, "%"),
         height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    chart = self.country(record, y_columns, x_axis, profile, options, width, height, html_code)
    chart.options.mapFile = "https://raw.githubusercontent.com/markmarkoh/datamaps/master/src/js/data/fra.json"
    if self.page.imports.pkgs.chart_js_extensions.geo.version[0].startswith("4."):
      chart.options.scales.projection.projectionScale = 24
      chart.options.scales.projection.projectionOffset = [-80, 1050]
    return chart

  def uk(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
         options: dict = None, width: Union[int, tuple] = (100, "%"),
         height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Usage::

      records = [{"name": "Liverpool", "value": 23}, {"name": "Leeds", "value": 60}]
      uk = page.ui.geo.chartJs.choropleths.uk(records, y_columns=["value"], x_axis="name")
      page.ui.button("Click").click([
        uk.build({"Birmingham": 40}),
      ])

    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    :return:
    """
    chart = self.country(record, y_columns, x_axis, profile, options, width, height, html_code)
    chart.options.mapFile = "https://raw.githubusercontent.com/markmarkoh/datamaps/master/src/js/data/gbr.json"
    if self.page.imports.pkgs.chart_js_extensions.geo.version[0].startswith("4."):
      chart.options.scales.projection.projectionScale = 20
      chart.options.scales.projection.projectionOffset = [0, 1100]
    return chart

  def italy(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
            options: dict = None, width: Union[int, tuple] = (100, "%"),
            height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    chart = self.country(record, y_columns, x_axis, profile, options, width, height, html_code)
    chart.options.mapFile = "https://raw.githubusercontent.com/markmarkoh/datamaps/master/src/js/data/ita.json"
    if self.page.imports.pkgs.chart_js_extensions.geo.version[0].startswith("3."):
      chart.options.scales.projection.center = [78.9629, 23.5937]
      chart.options.scales.projection.padding = 10
    else:
      chart.options.scales.projection.projectionScale = 23
      chart.options.scales.projection.projectionOffset = [-220, 900]
    return chart

  def india(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
            options: dict = None, width: Union[int, tuple] = (100, "%"),
            height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    chart = self.country(record, y_columns, x_axis, profile, options, width, height, html_code)
    chart.options.mapFile = "https://rawgit.com/Anujarya300/bubble_maps/master/data/geography-data/india.topo.json"
    return chart
