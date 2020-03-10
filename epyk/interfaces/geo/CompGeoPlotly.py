
from epyk.core.html import geo


class Plotly(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Plotly"

  def pane(self):
    pass

  def scatter(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    https://plot.ly/javascript/mapbox-layers/

    :param record:
    :param y_columns:
    :param x_axis:
    :param title:
    :param filters:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    line_chart = geo.GeoPlotly.Scatter(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                        filters, profile)
    line_chart.options.responsive = True
    self.parent.context.register(line_chart)
    line_chart.add_trace({"lon": [-112.8352], 'lat': [48.4113], 'text': [0.0875]})
    line_chart.data.marker.color = "fuchsia"
    line_chart.data.marker.size = 4
    line_chart.layout.mapbox.style = "open-street-map"
    line_chart.layout.mapbox.center.lat = 38
    line_chart.layout.mapbox.center.lon = -90
    line_chart.layout.dragmode = 'zoom'
    line_chart.layout.zoom = 3
    return line_chart

  def density(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    https://plot.ly/javascript/mapbox-density-heatmaps/

    :param record:
    :param y_columns:
    :param x_axis:
    :param title:
    :param filters:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    line_chart = geo.GeoPlotly.Scatter(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                       filters, profile)
    line_chart.options.responsive = True
    self.parent.context.register(line_chart)
    line_chart.add_trace({"lon": [-112.8352], 'lat': [48.4113], 'z': [20], 'text': [0.0875]}, type="densitymapbox")
    line_chart.data.marker.color = "fuchsia"
    line_chart.data.marker.size = 4
    line_chart.layout.mapbox.style = "stamen-terrain"
    line_chart.layout.mapbox.center.lat = 38
    line_chart.layout.mapbox.center.lon = -90
    line_chart.layout.dragmode = 'zoom'
    line_chart.layout.zoom = 3
    return line_chart

  def chorolet(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    data = {"locations": ["NY", "MA", "VT"], "z": [-50, -10, -20]}
    line_chart = geo.GeoPlotly.Chorolet(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                       filters, profile)
    line_chart.options.responsive = True
    self.parent.context.register(line_chart)
    data['geojson'] = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json"
    line_chart.add_trace(data)
    line_chart.layout.mapbox.center.lat = 38
    line_chart.layout.mapbox.center.lon = -90
    line_chart.layout.dragmode = 'zoom'
    line_chart.layout.zoom = 3
    return line_chart
