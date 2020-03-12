
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

  def world_map(self, record, y_column=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    data = {"locations": ["NY", "MA", "VT"], "z": [-50, -10, -20]}
    line_chart = geo.GeoPlotly.Choropleth(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                          filters, profile)
    line_chart.options.responsive = True
    self.parent.context.register(line_chart)
    line_chart.add_trace({'locations': ['France'], 'z': ['50']})
    line_chart.data.locationmode = 'country names'
    return line_chart

  def europe(self, record, y_column=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    map_chart = geo.GeoPlotly.Choropleth(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                          filters, profile)
    map_chart.options.responsive = True
    data = {}
    for rec in record:
      if x_axis in rec:
        data[rec[x_axis]] = data.get(x_axis, 0) + float(rec.get(y_column, 0))
    self.parent.context.register(map_chart)
    locations = list(data.keys())
    map_chart.add_trace({'locations': locations, 'z': [data[k] for k in locations]})
    map_chart.data.locationmode = 'country names'
    map_chart.data.autocolorscale = True
    map_chart.layout.geo.scope = 'europe'
    map_chart.layout.geo.showlakes = True
    map_chart.layout.geo.showland = True
    return map_chart

  def asia(self, record, y_column=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    map_chart = geo.GeoPlotly.Choropleth(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                          filters, profile)
    map_chart.options.responsive = True
    data = {}
    for rec in record:
      if x_axis in rec:
        data[rec[x_axis]] = data.get(x_axis, 0) + float(rec.get(y_column, 0))

    map_chart.options.responsive = True
    self.parent.context.register(map_chart)
    locations = list(data.keys())
    map_chart.add_trace({'locations': locations, 'z': [data[k] for k in locations]})
    map_chart.data.locationmode = 'country names'
    map_chart.layout.geo.scope = 'asia'
    map_chart.layout.geo.showlakes = True
    map_chart.layout.geo.showland = True
    return map_chart

  def africa(self, record, y_column=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    map_chart = geo.GeoPlotly.Choropleth(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                          filters, profile)
    map_chart.options.responsive = True
    data = {}
    for rec in record:
      if x_axis in rec:
        data[rec[x_axis]] = data.get(x_axis, 0) + float(rec.get(y_column, 0))
    self.parent.context.register(map_chart)
    locations = list(data.keys())
    map_chart.add_trace({'locations': locations, 'z': [data[k] for k in locations]})
    map_chart.data.locationmode = 'country names'
    map_chart.layout.geo.scope = 'africa'
    map_chart.layout.geo.showlakes = True
    map_chart.layout.geo.showland = True
    return map_chart

  def usa(self, record, y_column=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    map_chart = geo.GeoPlotly.Choropleth(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                          filters, profile)
    map_chart.options.responsive = True
    data = {}
    for rec in record:
      if x_axis in rec:
        data[rec[x_axis]] = data.get(x_axis, 0) + float(rec.get(y_column, 0))
    self.parent.context.register(map_chart)
    locations = list(data.keys())
    map_chart.add_trace({'locations': locations, 'z': [data[k] for k in locations]})
    map_chart.data.locationmode = 'USA-states'
    map_chart.layout.geo.scope = 'usa'
    map_chart.layout.geo.showlakes = True
    map_chart.layout.geo.showland = True
    return map_chart

  def scatter_europe(self, record, y_column=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    map_chart = geo.GeoPlotly.ScatterGeo(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                         filters, profile)
    map_chart.options.responsive = True
    data = {}
    for rec in record:
      if x_axis in rec:
        data[rec[x_axis]] = data.get(x_axis, 0) + float(rec.get(y_column, 0))
    self.parent.context.register(map_chart)
    locations = list(data.keys())
    map_chart.add_trace({'locations': locations, 'z': [data[k] for k in locations]})
    map_chart.data.locationmode = 'country names'
    map_chart.data.autocolorscale = True
    map_chart.layout.geo.scope = 'europe'
    map_chart.layout.geo.showlakes = True
    map_chart.layout.geo.showland = True
    return map_chart