
from epyk.core.html import geo


class GeoGoogle(object):

  def __init__(self, context):
    self.parent = context
    self.chartFamily = "GoogleMaps"

  def maps(self, lattitude, longitude, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    :param lattitude:
    :param longitude:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    dflt_options = {"center": (lattitude, longitude), 'mapTypeId': 'ROADMAP', 'zoom': 10}
    if options is not None:
      dflt_options.update(options)
    geo_chart = geo.GeoGoogle.ChartGeoGoogle(self.parent.context.rptObj, width, height, dflt_options, htmlCode, profile)

    return geo_chart

  def satellite(self, lattitude, longitude, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    :param lattitude:
    :param longitude:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    dflt_options = {"center": (lattitude, longitude), 'mapTypeId': 'satellite', 'zoom': 10}
    if options is not None:
      dflt_options.update(options)
    geo_chart = geo.GeoGoogle.ChartGeoGoogle(self.parent.context.rptObj, width, height, dflt_options, htmlCode, profile)
    return geo_chart

  def terrain(self, lattitude, longitude, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    :param lattitude:
    :param longitude:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    dflt_options = {"center": (lattitude, longitude), 'mapTypeId': 'terrain', 'zoom': 10}
    if options is not None:
      dflt_options.update(options)
    geo_chart = geo.GeoGoogle.ChartGeoGoogle(self.parent.context.rptObj, width, height, dflt_options, htmlCode, profile)
    return geo_chart

  def current(self, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    dflt_options = {"center": "navigator.geolocation.getCurrentPosition(function(position){console.log(position.coords.latitude); return (position.coords.latitude, position.coords.longitude)})", 'mapTypeId': 'ROADMAP', 'zoom': 10}
    if options is not None:
      dflt_options.update(options)
    geo_chart = geo.GeoGoogle.ChartGeoGoogle(self.parent.context.rptObj, width, height, dflt_options, htmlCode, profile)
    return geo_chart

  def streetview(self):
    pass
