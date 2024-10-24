
from typing import Union
from epyk.core.html import geo
from epyk.core.html import Defaults_html


class GeoGoogle:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "GoogleMaps"

  def maps(self, latitude: float, longitude: float, profile: Union[dict, bool] = None, options: dict = None,
           width: Union[int, tuple] = (100, "%"), height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           html_code: str = None):
    """

    :param latitude:
    :param longitude:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    dflt_options = {"center": (latitude, longitude), 'mapTypeId': 'ROADMAP', 'zoom': 10}
    if options is not None:
      dflt_options.update(options)
    geo_chart = geo.GeoGoogle.ChartGeoGoogle(self.page, width, height, dflt_options, html_code, profile)

    return geo_chart

  def satellite(self, latitude: float, longitude: float, profile: Union[dict, bool] = None, options: dict = None,
                width: Union[int, tuple] = (100, "%"),
                height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
                html_code: str = None):
    """

    :param latitude:
    :param longitude:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    dflt_options = {"center": (latitude, longitude), 'mapTypeId': 'satellite', 'zoom': 10}
    if options is not None:
      dflt_options.update(options)
    geo_chart = geo.GeoGoogle.ChartGeoGoogle(self.page, width, height, dflt_options, html_code, profile)
    return geo_chart

  def terrain(self, latitude: float, longitude: float, profile: Union[dict, bool] = None, options: dict = None,
              width: Union[int, tuple] = (100, "%"),
              height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
              html_code: str = None):
    """

    :param latitude:
    :param longitude:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    dflt_options = {"center": (latitude, longitude), 'mapTypeId': 'terrain', 'zoom': 10}
    if options is not None:
      dflt_options.update(options)
    geo_chart = geo.GeoGoogle.ChartGeoGoogle(self.page, width, height, dflt_options, html_code, profile)
    return geo_chart

  def current(self, profile: Union[dict, bool] = None, options: dict = None, width: Union[int, tuple] = (100, "%"),
              height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    dflt_options = {"center": "navigator.geolocation.getCurrentPosition(function(position){console.log(position.coords.latitude); return (position.coords.latitude, position.coords.longitude)})", 'mapTypeId': 'ROADMAP', 'zoom': 10}
    if options is not None:
      dflt_options.update(options)
    geo_chart = geo.GeoGoogle.ChartGeoGoogle(self.page, width, height, dflt_options, html_code, profile)
    return geo_chart

  def streetview(self):
    pass
