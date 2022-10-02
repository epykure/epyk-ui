
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
    geo_chart.options.scale.projection = "albersUsa"
    geo_chart.options.geo.colorScale.display = True
    geo_chart.options.geo.colorScale.quantize = 5
    geo_chart.options.geo.colorScale.position = "bottom"
    geo_chart.options.geo.colorScale.legend.position = "bottom-right"
    geo_chart.options.showOutline = True
    geo_chart.options.legend.display = False
    geo_chart.options.showGraticule = True
    return geo_chart

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
    #geo_chart.options.scale.projection = "equalEarth"
    # geo_chart.options.legend.display = False
    geo_chart.options.scales.xy.projection = "equalEarth"
    #geo_chart.options.scale.projection = "equirectangular"
    #geo_chart.options.geo.colorScale.display = True
    geo_chart.options.showOutline = True
    geo_chart.options.plugins.legend.display = False
    geo_chart.options.showGraticule = True
    return geo_chart

  def country(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
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
    geo_chart = geo.GeoChartJs.ChoroplethCountry(self.page, width, height, html_code, options or {}, profile)
    geo_chart.options.scale.projection = "mercator"
#     geo_chart.options.scale.set_projection('''
# d3.geoProjection(function(x, y) {
#   return [x, Math.log(Math.tan(Math.PI / 4 + y / 2))];
#
#   function fitWidth(){}
# });
# ''')
    geo_chart.options.geo.colorScale.display = True
    geo_chart.options.showOutline = True
    geo_chart.options.legend.display = False
    geo_chart.options.showGraticule = False
    return geo_chart

  def fr(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
         options: dict = None, width: Union[int, tuple] = (100, "%"),
         height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    chart = self.country(record, y_columns, x_axis, profile, options, width, height, html_code)
    chart.geo_map = "https://raw.githubusercontent.com/markmarkoh/datamaps/master/src/js/data/fra.json"
    return chart

  def uk(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
         options: dict = None, width: Union[int, tuple] = (100, "%"),
         height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    chart = self.country(record, y_columns, x_axis, profile, options, width, height, html_code)
    chart.geo_map = "https://raw.githubusercontent.com/markmarkoh/datamaps/master/src/js/data/ita.json"
    return chart

  def italy(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
            options: dict = None, width: Union[int, tuple] = (100, "%"),
            height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    chart = self.country(record, y_columns, x_axis, profile, options, width, height, html_code)
    chart.geo_map = "https://raw.githubusercontent.com/markmarkoh/datamaps/master/src/js/data/ita.json"
    chart.options.center = [78.9629, 23.5937]
    return chart

  def india(self, record=None, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
            options: dict = None, width: Union[int, tuple] = (100, "%"),
            height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    chart = self.country(record, y_columns, x_axis, profile, options, width, height, html_code)
    chart.geo_map = "https://rawgit.com/Anujarya300/bubble_maps/master/data/geography-data/india.topo.json"
    return chart
