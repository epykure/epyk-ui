import logging

from epyk.core.html import geo
from epyk.interfaces import Arguments


class GeoLeaflet:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Leaflet"

  def map(self, record=None, y_column=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), html_code=None):
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    return geo.GeoLeaflet.GeoLeaflet(self.page, width, height, html_code, options or {}, profile)

  def europe(self, record=None, y_column=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), html_code=None):
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    geo_chart = geo.GeoLeaflet.GeoLeaflet(self.page, width, height, html_code, options or {}, profile)

    return geo_chart
