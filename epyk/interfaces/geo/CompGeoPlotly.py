
from epyk.core.html import geo


class Plotly(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Plotly"

  def scattermapbox(self, record, lon_columns=None, lat_columns=None, text_columns=None, title=None, filters=None,
                    profile=None, options=None,  width=(100, "%"), height=(430, "px"), htmlCode=None):
    """

    https://plot.ly/javascript/mapbox-layers/

    :param record:
    :param lon_columns:
    :param lat_columns:
    :param text_columns:
    :param title:
    :param filters:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    series = []
    for i, l in enumerate(lon_columns):
      series.append({'lon': [], 'lat': [], 'text': []})
      for rec in record:
        series[-1]['lon'].append(rec.get(l, 0))
        series[-1]['lat'].append(rec.get(lat_columns[i], 0))
        if text_columns is not None:
          series[-1]['text'].append(rec.get(text_columns[i], 0))
    line_chart = geo.GeoPlotly.Scatter(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                        filters, profile)
    line_chart.options.responsive = True
    self.parent.context.register(line_chart)
    for i, s in enumerate(series):
      line_chart.add_trace(s)
      line_chart.data.marker.color = self.parent.context.rptObj.theme.colors[::-1][i]
    line_chart.layout.mapbox.style = "open-street-map"
    # line_chart.data.marker.size = 4
    # line_chart.layout.mapbox.style = "open-street-map"
    # line_chart.layout.mapbox.center.lat = 38
    # line_chart.layout.mapbox.center.lon = -90
    # line_chart.layout.dragmode = 'zoom'
    # line_chart.layout.mapbox.zoom = 3
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


class PlotlyBubble(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Plotly"

  def bubble(self, scope, record=None, y_column=None, x_axis=None, title=None, profile=None, options=None,
             width=(100, "%"), height=(430, "px"), htmlCode=None):
    map_chart = geo.GeoPlotly.BubbleGeo(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                         profile)
    map_chart.options.responsive = True
    data = {}
    if record is None:
      record = []
    for rec in record:
      if x_axis in rec:
        data[rec[x_axis]] = data.get(x_axis, 0) + float(rec.get(y_column, 0))
    self.parent.context.register(map_chart)
    if record:
      locations = list(data.keys())
      values = [data[k] for k in locations]
      map_chart.add_trace({'locations': locations})
      map_chart.data.marker.colorbar.title = "Test"
      map_chart.data.marker.line.color = "black"
      map_chart.data.marker.size = values
      # map_chart.data.marker.cmin = 0
      # map_chart.data.marker.cmax = max(values)
      map_chart.data.marker.color = values
      map_chart.data.marker.colorscale = 'Reds'
    map_chart.layout.geo.scope = scope
    map_chart.layout.geo.resolution = 150
    if width[1] == 'px':
      map_chart.layout.width = width[0]
    return map_chart

  def usa(self, record=None, lon_columns=None, lat_columns=None, text_columns=None, title=None, profile=None, options=None,
             width=(100, "%"), height=(430, "px"), htmlCode=None):
    map_usa = self.bubble('usa', record, None, None, title, profile, options, width, height, htmlCode)

    series = []
    for i, l in enumerate(lon_columns):
      series.append({'lon': [], 'lat': [], 'text': []})
      for rec in record:
        series[-1]['lon'].append(rec.get(l, 0))
        series[-1]['lat'].append(rec.get(lat_columns[i], 0))
        if text_columns is not None:
          series[-1]['text'].append(rec.get(text_columns[i], 0))
    for i, s in enumerate(series):
      map_usa.add_trace(s)
    map_usa.data.locationmode = 'USA-states'
    map_usa.layout.no_background()
    return map_usa

  def europe(self, record=None, y_column=None, x_axis=None, title=None, profile=None, options=None,
             width=(100, "%"), height=(430, "px"), htmlCode=None):
    return self.bubble('europe', record, y_column, x_axis, title, profile, options, width, height, htmlCode)


class PlotlyScatter(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Plotly"

  def scatter(self, scope, record=None, lon_columns=None, lat_columns=None, text_columns=None, title="", profile=None, options=None,
              width=(100, "%"), height=(430, "px"), htmlCode=None):
    map_chart = geo.GeoPlotly.ScatterGeo(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                         profile)
    map_chart.options.responsive = True

    series = []
    for i, l in enumerate(lon_columns):
      series.append({'lon': [], 'lat': [], 'text': []})
      for rec in record:
        series[-1]['lon'].append(rec.get(l, 0))
        series[-1]['lat'].append(rec.get(lat_columns[i], 0))
        if text_columns is not None:
          series[-1]['text'].append(rec.get(text_columns[i], 0))

    self.parent.context.register(map_chart)
    for i, s in enumerate(series):
      map_chart.add_trace(s)
      map_chart.data.marker.colorbar.title = title
      map_chart.data.marker.line.color = self.parent.context.rptObj.theme.colors[-i]
      #map_chart.data.marker.size = values
      #map_chart.data.marker.cmin = 0
      #map_chart.data.marker.cmax = max(values)
      #map_chart.data.marker.color = values
      map_chart.data.marker.colorscale = 'Reds'
    map_chart.layout.geo.scope = scope
    if width[1] == 'px':
      map_chart.layout.width = width[0]
    return map_chart

  def north_america(self, record=None, lon_columns=None, lat_columns=None, text_columns=None, title=None, profile=None,
                    options=None, width=(100, "%"), height=(430, "px"), htmlCode=None):
    geo_bubble = self.bubble('north america', record, lon_columns, lat_columns, text_columns, title, profile, options, width, height, htmlCode)
    return geo_bubble

  def usa(self, record=None, lon_columns=None, lat_columns=None, text_columns=None, title=None, profile=None,
          options=None, width=(100, "%"), height=(430, "px"), htmlCode=None):
    geo_bubble = self.bubble('usa', record, lon_columns, lat_columns, text_columns, title, profile, options, width, height, htmlCode)
    return geo_bubble


class PlotlyChoropleth(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Plotly"

  def world_map(self, record, y_columns=None, country_column=None, title=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):

    series = []
    for y in y_columns:
      s = {'locations': [], 'z': []}
      for rec in record:
        s['locations'].append(rec[country_column])
        s['z'].append(rec[y])
      series.append(s)
    line_chart = geo.GeoPlotly.Choropleth(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
    line_chart.options.responsive = True
    self.parent.context.register(line_chart)
    for s in series:
      line_chart.add_trace(s)
    line_chart.data.locationmode = 'country names'
    return line_chart

  def europe(self, record, y_column=None, x_axis=None, title=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    map_chart = geo.GeoPlotly.Choropleth(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
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

  def asia(self, record, y_column=None, x_axis=None, title=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    map_chart = geo.GeoPlotly.Choropleth(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
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

  def africa(self, record, y_column=None, x_axis=None, title=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    map_chart = geo.GeoPlotly.Choropleth(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
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

  def usa(self, record, y_column=None, x_axis=None, title=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    map_chart = geo.GeoPlotly.Choropleth(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
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
