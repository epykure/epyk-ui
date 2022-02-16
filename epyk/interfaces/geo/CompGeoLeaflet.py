import logging

from typing import Union
from epyk.core.html import geo
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html


class GeoLeaflet:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Leaflet"

  def map(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
          options: dict = None, width: Union[int, tuple] = (100, "%"),
          height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
          html_code: str = None):
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    return geo.GeoLeaflet.GeoLeaflet(self.page, width, height, html_code, options or {}, profile)

  def europe(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
             options: dict = None, width: Union[int, tuple] = (100, "%"),
             height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
             html_code: str = None):
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    geo_chart = geo.GeoLeaflet.GeoLeaflet(self.page, width, height, html_code, options or {}, profile)
    return geo_chart
