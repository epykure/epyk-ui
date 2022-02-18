
from typing import Union
from epyk.core.html import geo
from epyk.core.html import Defaults_html


class Plotly:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Plotly"

  @property
  def choropleths(self):
    """
    Description:
    -----------
    Plotly Choropleth charts

    Related Pages:

      https://plotly.com/javascript/mapbox-county-choropleth/
    """
    return PlotlyChoropleth(self)

  @property
  def bubbles(self):
    """
    Description:
    -----------
    Plotly Bubble charts

    Related Pages:

      https://plotly.com/javascript/bubble-maps/
    """
    return PlotlyBubble(self)

  def scattermapbox(self, record, lon_columns: list = None, lat_columns: list = None, text_columns: list = None,
                    profile: Union[dict, bool] = None, options: dict = None,  width: Union[int, tuple] = (100, "%"),
                    height: Union[int, tuple] = (430, "px"), html_code: str = None):
    """
    Description:
    -----------

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.Scatter`

    Related Pages:

      https://plot.ly/javascript/mapbox-layers/

    Attributes:
    ----------
    :param record:
    :param lon_columns:
    :param lat_columns:
    :param text_columns:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    series = []
    if lon_columns is not None:
      for i, l in enumerate(lon_columns):
        series.append({'lon': [], 'lat': [], 'text': []})
        for rec in record:
          series[-1]['lon'].append(rec.get(l, 0))
          series[-1]['lat'].append(rec.get(lat_columns[i], 0))
          if text_columns is not None:
            series[-1]['text'].append(rec.get(text_columns[i], 0))
    line_chart = geo.GeoPlotly.Scatter(
      self.page, width, height, options or {}, html_code, profile)
    line_chart.options.responsive = True
    for i, s in enumerate(series):
      line_chart.add_trace(s)
      line_chart.data.marker.color = self.page.theme.colors[::-1][i]
    line_chart.layout.mapbox.style = "open-street-map"
    # line_chart.data.marker.size = 4
    # line_chart.layout.mapbox.style = "open-street-map"
    # line_chart.layout.mapbox.center.lat = 38
    # line_chart.layout.mapbox.center.lon = -90
    # line_chart.layout.dragmode = 'zoom'
    # line_chart.layout.mapbox.zoom = 3
    return line_chart

  def density(self, record, y_columns: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
              options: dict = None, width=(100, "%"), height=(330, "px"), html_code=None):
    """
    Description:
    -----------

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.Scatter`

    Related Pages:

      https://plot.ly/javascript/mapbox-density-heatmaps/

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    line_chart = geo.GeoPlotly.Scatter(self.page, width, height, options or {}, html_code, profile)
    line_chart.options.responsive = True
    line_chart.add_trace({"lon": [-112.8352], 'lat': [48.4113], 'z': [20], 'text': [0.0875]}, type="densitymapbox")
    line_chart.data.marker.color = "fuchsia"
    line_chart.data.marker.size = 4
    line_chart.layout.mapbox.style = "stamen-terrain"
    line_chart.layout.mapbox.center.lat = 38
    line_chart.layout.mapbox.center.lon = -90
    line_chart.layout.dragmode = 'zoom'
    line_chart.layout.zoom = 3
    return line_chart

  def chorolet(self, record, y_columns: list = None, x_axis: str = None, title: str = None,
               options: dict = None, width: Union[int, tuple] = (100, "%"), height: Union[int, tuple] = (330, "px"),
               html_code: str = None, profile: Union[dict, bool] = None):
    """
    Description:
    -----------

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.Chorolet`

    Related Pages:

      https://plotly.com/javascript/mapbox-county-choropleth/

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    data = {"locations": ["NY", "MA", "VT"], "z": [-50, -10, -20]}
    line_chart = geo.GeoPlotly.Chorolet(self.page, width, height, options or {}, html_code, profile)
    line_chart.options.responsive = True
    data['geojson'] = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json"
    line_chart.add_trace(data)
    line_chart.layout.mapbox.center.lat = 38
    line_chart.layout.mapbox.center.lon = -90
    line_chart.layout.dragmode = 'zoom'
    line_chart.layout.zoom = 3
    return line_chart

  def mapbox(self, record, lon_columns: list = None, lat_columns: list = None, text_columns: list = None,
             profile: Union[dict, bool] = None, options: dict = None,
             width: Union[int, tuple] = (100, "%"), height: Union[int, tuple] = (None, "px"), html_code: str = None):
    series = []
    if lon_columns is not None:
      for i, l in enumerate(lon_columns):
        series.append({'lon': [], 'lat': [], 'text': []})
        for rec in record:
          series[-1]['lon'].append(rec.get(l, 0))
          series[-1]['lat'].append(rec.get(lat_columns[i], 0))
          if text_columns is not None:
            series[-1]['text'].append(rec.get(text_columns[i], 0))
    line_chart = geo.GeoPlotly.Scatter(
      self.page, width, height, options or {}, html_code, profile)
    line_chart.options.responsive = True
    line_chart.layout.dragmode = "zoom"
    line_chart.layout.mapbox.style = "white-bg"
    line_chart.layout.mapbox.add_layers("raster",
                                 [
                                   "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"])
    for i, s in enumerate(series):
      line_chart.add_trace(s)
      line_chart.data.marker.color = self.page.theme.colors[::-1][i]
      line_chart.data.marker.size = 4
    line_chart.layout.mapbox.style = "open-street-map"
    line_chart.layout.no_margin()
    return line_chart


class PlotlyBubble:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Plotly"

  def bubble(self, scope, record=None, size_col=None, country_col=None, long_col=None, lat_col=None, profile=None,
             options=None, width=(100, "%"), height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    How to make a D3.js-based bubble map in JavaScript. A bubble map overlays a bubble chart on a map.

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.BubbleGeo`

    Related Pages:

      https://plotly.com/javascript/bubble-maps/

    Attributes:
    ----------
    :param scope: String. The scope of the chart
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param long_col: String. The column in the recordset used to retrieve the longitude (optional if country codes)
    :param lat_col: String. The column in the recordset used to retrieve the latitude (optional if country codes)
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    dftl_options = {'type': 'scattergeo'}
    if options is not None:
      dftl_options.update(options)
    map_chart = geo.GeoPlotly.BubbleGeo(self.page, width, height, dftl_options, html_code, profile)
    map_chart.options.responsive = True

    records = []
    if country_col is not None:
      records = self.page.data.plotly.countries(record, country_col, size_col, dftl_options.get('scale', False))
      points = ['locations']
    elif long_col is not None and lat_col is not None:
      records = self.page.data.plotly.locations(record, long_col, lat_col, size_col, dftl_options.get('scale', False))
      points = ['lon', 'lat']
    for record in records:
      map_chart.add_trace({p: record[p] for p in points})
      #map_chart.data.marker.colorbar.title = "Test"
      #map_chart.data.marker.line.color = "black"
      map_chart.data.marker.size = record['marker'].get('size', [])
      # map_chart.data.marker.cmin = 0
      # map_chart.data.marker.cmax = max(values)
      map_chart.data.marker.color = record['marker'].get('color', 'black')
      map_chart.data.marker.colorscale = 'Reds'
    map_chart.layout.geo.scope = scope
    map_chart.layout.geo.resolution = 150
    return map_chart

  def usa(self, record=None, size_col=None, country_col=None, long_col=None, lat_col=None,
          profile=None, options=None, width=(100, "%"), height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A bubble chart for the USA.

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.BubbleGeo`

    Related Pages:

      https://plotly.com/javascript/bubble-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param long_col: String. The column in the recordset used to retrieve the longitude (optional if country codes)
    :param lat_col: String. The column in the recordset used to retrieve the latitude (optional if country codes)
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    map_usa = self.bubble('usa', record, size_col=size_col, country_col=country_col, long_col=long_col, lat_col=lat_col,
                          profile=profile, options=options, width=width, height=height, html_code=html_code)
    map_usa.data.locationmode = 'USA-states'
    map_usa.data.locationmode = 'usa'
    map_usa.layout.no_background()
    return map_usa

  def europe(self, record=None, size_col=None, country_col=None, long_col=None, lat_col=None, profile=None,
             options=None, width=(100, "%"), height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A bubble chart for Europe

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.BubbleGeo`

    Related Pages:

      https://plotly.com/javascript/bubble-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param long_col: String. The column in the recordset used to retrieve the longitude (optional if country codes)
    :param lat_col: String. The column in the recordset used to retrieve the latitude (optional if country codes)
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    return self.bubble('europe', record, size_col=size_col, country_col=country_col, long_col=long_col, lat_col=lat_col,
                       profile=profile, options=options, width=width, height=height, html_code=html_code)

  def asia(self, record=None, size_col=None, country_col=None, long_col=None, lat_col=None, profile=None, options=None,
           width=(100, "%"), height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A bubble chart for Asia

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.BubbleGeo`

    Related Pages:

      https://plotly.com/javascript/bubble-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param long_col: String. The column in the recordset used to retrieve the longitude (optional if country codes)
    :param lat_col: String. The column in the recordset used to retrieve the latitude (optional if country codes)
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    return self.bubble('asia', record, size_col=size_col, country_col=country_col, long_col=long_col, lat_col=lat_col,
                       profile=profile, options=options, width=width, height=height, html_code=html_code)

  def africa(self, record=None, size_col=None, country_col=None, long_col=None, lat_col=None, profile=None,
             options=None, width=(100, "%"), height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A bubble chart for Africa

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.BubbleGeo`

    Related Pages:

      https://plotly.com/javascript/bubble-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param long_col: String. The column in the recordset used to retrieve the longitude (optional if country codes)
    :param lat_col: String. The column in the recordset used to retrieve the latitude (optional if country codes)
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    return self.bubble('africa', record, size_col=size_col, country_col=country_col, long_col=long_col, lat_col=lat_col,
                       profile=profile, options=options, width=width, height=height, html_code=html_code)

  def south_america(self, record=None, size_col=None, country_col=None, long_col=None, lat_col=None, profile=None,
                    options=None, width=(100, "%"), height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A bubble chart for South America

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.BubbleGeo`

    Related Pages:

      https://plotly.com/javascript/bubble-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param long_col: String. The column in the recordset used to retrieve the longitude (optional if country codes)
    :param lat_col: String. The column in the recordset used to retrieve the latitude (optional if country codes)
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    return self.bubble(
      'south america', record, size_col=size_col, country_col=country_col, long_col=long_col, lat_col=lat_col,
      profile=profile, options=options, width=width, height=height, html_code=html_code)

  def north_america(self, record=None, size_col=None, country_col=None, long_col=None, lat_col=None, profile=None,
                    options=None, width=(100, "%"), height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A bubble chart for North America

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.BubbleGeo`

    Related Pages:

      https://plotly.com/javascript/bubble-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param long_col: String. The column in the recordset used to retrieve the longitude (optional if country codes)
    :param lat_col: String. The column in the recordset used to retrieve the latitude (optional if country codes)
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    return self.bubble(
      'north america', record, size_col=size_col, country_col=country_col, long_col=long_col, lat_col=lat_col,
      profile=profile, options=options, width=width, height=height, html_code=html_code)

  def world(self, record=None, size_col=None, country_col=None, long_col=None, lat_col=None, profile=None, options=None,
            width=(100, "%"), height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A world bubble chart

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.BubbleGeo`

    Related Pages:

      https://plotly.com/javascript/bubble-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param long_col: String. The column in the recordset used to retrieve the longitude (optional if country codes)
    :param lat_col: String. The column in the recordset used to retrieve the latitude (optional if country codes)
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    """
    map_world = self.bubble('world', record, size_col=size_col, country_col=country_col, long_col=long_col, lat_col=lat_col,
                            profile=profile, options=options, width=width, height=height, html_code=html_code)
    map_world.layout.geo.showland = True
    map_world.layout.geo.subunitwidth = 1
    map_world.layout.geo.countrywidth = 1
    map_world.layout.geo.projection.type = "earth"
    map_world.layout.geo.landcolor = 'rgb(217, 217, 217)'
    return map_world


class PlotlyChoropleth:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Plotly"

  def world(self, record, size_col=None, country_col=None, profile=None, options=None, width=(100, "%"),
            height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A world Choropleth Chart

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.Choropleth`

    Related Pages:

      https://plotly.com/javascript/choropleth-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    dftl_options = {'type': 'choropleth', 'mode': ''}
    if options is not None:
      dftl_options.update(options)

    records = self.page.data.plotly.choropleth(record, country_col, size_col, dftl_options.get('scale', False))
    line_chart = geo.GeoPlotly.Choropleth(self.page, width, height, dftl_options, html_code, profile)
    line_chart.options.responsive = True
    for record in records:
      line_chart.add_trace(record)
    return line_chart

  def europe(self, record=None, size_col=None, country_col=None, profile=None, options=None, width=(100, "%"),
             height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A Choropleth Chart for European countries

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.Choropleth`

    Related Pages:

      https://plotly.com/javascript/choropleth-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    map_chart = self.world(record or [], size_col, country_col, profile, options, width, height, html_code)
    map_chart.layout.geo.scope = 'europe'
    return map_chart

  def asia(self, record, size_col=None, country_col=None, profile=None, options=None, width=(100, "%"),
           height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A Choropleth Chart for asian countries

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.Choropleth`

    Related Pages:

      https://plotly.com/javascript/choropleth-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    map_chart = self.world(record, size_col, country_col, profile, options, width, height, html_code)
    map_chart.layout.geo.scope = 'asia'
    return map_chart

  def africa(self, record, size_col=None, country_col=None, profile=None, options=None, width=(100, "%"),
             height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A Choropleth Chart for african countries

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.Choropleth`

    Related Pages:

      https://plotly.com/javascript/choropleth-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    map_chart = self.world(record, size_col, country_col, profile, options, width, height, html_code)
    map_chart.layout.geo.scope = 'africa'
    return map_chart

  def south_america(self, record, size_col=None, country_col=None, profile=None, options=None, width=(100, "%"),
                    height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A Choropleth Chart for south american countries

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.Choropleth`

    Related Pages:

      https://plotly.com/javascript/choropleth-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    map_chart = self.world(record, size_col, country_col, profile, options, width, height, html_code)
    map_chart.layout.geo.scope = 'south america'
    return map_chart

  def north_america(self, record, size_col=None, country_col=None, profile=None, options=None, width=(100, "%"),
                    height=(430, "px"), html_code=None):
    """
    Description:
    -----------
    A Choropleth Chart for north american countries

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.Choropleth`

    Related Pages:

      https://plotly.com/javascript/choropleth-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    map_chart = self.world(record, size_col, country_col, profile, options, width, height, html_code)
    map_chart.layout.geo.scope = 'north america'
    return map_chart

  def usa(self, record, y_column=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"),
          html_code=None):
    """
    Description:
    -----------

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoPlotly.Choropleth`

    Related Pages:

      https://plotly.com/javascript/choropleth-maps/

    Attributes:
    ----------
    :param record: Data. The recordset
    :param size_col: String. The column in the recordset used for the values
    :param country_col: String. The column in the recordset used to retrieve country code
    :param profile: A flag to set the component performance storage
    :param options: Dictionary. The charts options
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    """
    map_chart = geo.GeoPlotly.Choropleth(self.page, width, height, options or {}, html_code, profile)
    map_chart.options.responsive = True
    data = {}
    for rec in record:
      if x_axis in rec:
        data[rec[x_axis]] = data.get(x_axis, 0) + float(rec.get(y_column, 0))
    locations = list(data.keys())
    map_chart.add_trace({'locations': locations, 'z': [data[k] for k in locations]})
    map_chart.data.locationmode = 'USA-states'
    map_chart.layout.geo.scope = 'usa'
    map_chart.layout.geo.showlakes = True
    map_chart.layout.geo.showland = True
    return map_chart
