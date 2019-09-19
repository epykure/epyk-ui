"""

"""


from epyk.core.js.configs import JsConfig


class JsBase(JsConfig.JsConfig):
  """
  Base Class for the Plotly Charts
  """
  listAttributes = []
  c3d = False
  jsCls = 'Chart'
  reference = None # The main link to get the documentation of this chart
  _statics = None # Static configuration will be added to each dara set automatically
  _layout = None # Change the layout properties of the chart
  jsType = None # Attach the chart to a family for the data transformation

  def __init__(self, report, data, seriesProperties):
    super(JsBase, self).__init__(report, data, seriesProperties)
    for key, val in self._attrs.items():
      self.seriesProperties.setdefault('static', {})[key] = val
    self.config()

  def config(self):
    if self._statics is not None:
      self.seriesProperties["static"].update(self._statics)

  def _colors(self, cList, index=None, borderColors=None):
    """
    Internal function to allow the change of colors of the different series in a Plotly chart.
    Plotly configuration is using the internal variable seriesProperties in order to add the properties once
    the Javascript function has aggregated the different values.
    """
    if index is not None:
      if not "marker" in self.__chart.seriesProperties["static"]:
        self.seriesProperties["static"]["marker"] = {'color': [cList]}
    else:
      for i in range(len(self.data._schema['out']['params'][0])):
        self.seriesProperties["dynamic"].setdefault(i, {})["marker"] = {'color': cList[i]}


# ---------------------------------------------------------------------------------------------------------
#                                          Plotly Configurations
# ---------------------------------------------------------------------------------------------------------
class JsBar(JsBase):
  """
  Configuration for a Bars Chart in Plotly

  Documentation
  https://plot.ly/javascript/bar-charts/
  """
  alias = 'bar'
  name = 'Bars'
  _attrs = {'type': 'bar'}


class JsHBar(JsBase):
  """
  Configuration for a Horizontal Bars Chart in Plotly

  Documentation
  https://plot.ly/javascript/bar-charts/
  """
  alias = 'hbar'
  name = 'Horizontal Bars'
  _attrs = {'orientation': 'h', 'type': 'bar'}


class JsPie(JsBase):
  """
  Configuration for a Pie Chart in Plotly

  Documentation
  https://plot.ly/javascript/pie-charts/
  """
  alias = 'pie'
  name = 'Pie'
  _attrs = {'type': 'pie'}

  def _colors(self, cList, index=None, borderColors=None):
    """

    :param cList:
    :param index:
    :param borderColors:

    :return:
    """
    if index is not None:
      if not "marker" in self.__chart.seriesProperties["static"]:
        self.seriesProperties["static"]["marker"] = {'colors': cList}
    else:
      for i in range(len(self.data._schema['out']['params'][0])):
        self.seriesProperties["dynamic"].setdefault(i, {})["marker"] = {'colors': cList}


class JsDonut(JsPie):
  """
  Configuration for a Donut Chart in Plotly

  Documentation
  https://plot.ly/javascript/pie-charts/
  """
  alias = 'donut'
  name = 'Donut'
  _attrs = {'hole': '.4', 'type': 'pie'}


# ---------------------------------------------------------------------------------------------------------
#                           LINE CHARTS
#
class JsMulti(JsBase):
  """
  Configuration for a Multi Chart in Plotly

  """
  alias = 'multi'
  name = 'Multi Series'
  _attrs = {'type': 'scatter'}


class JsLine(JsBase):
  """
  Configuration for a Linea Chart in Plotly
  """
  alias = 'line'
  name = 'Line Series'
  _attrs = {'type': 'scatter'}


class JsScatter(JsBase):
  """
  Configuration for a Scatter Chart in Plotly
  """
  alias = 'scatter'
  name = 'Scatter Series'
  _attrs = {'mode': 'markers+text', 'type': 'scatter'}
  _layout = {'hovermode': 'closest'}


class JsScatterGl(JsBase):
  """
  Configuration for a ScatterGl Chart in Plotly
  """
  alias = 'scattergl'
  name = 'Scatter Series'
  _attrs = {'mode': 'markers+text', 'type': 'scattergl'}


class JsArea(JsBase):
  """
  Configuration for a Horizontal Bars Chart in Plotly
  """
  alias = 'area'
  name = 'Area Series'
  _attrs = {'fill': 'tonexty', 'mode': 'none'}


class JsBubble(JsBase):
  """
  Configuration for a Bubble Chart in Plotly
  """
  alias = 'bubble'
  name = 'Bubble Chart'
  _attrs = {'mode': 'scatter'}

  def config(self):
    for i in range(len(self.data._schema['out']['params'][0])):
      self.seriesProperties['dynamic'][i] = {'marker': {'size': [1, 4, 50]}, 'mode': 'markers'}


# ---------------------------------------------------------------------------------------------------------
#                           STATISTIC CHARTS
#
class JsBox(JsBase):
  """
  Configuration for a Box Chart in Plotly

  Documentation
  https://plot.ly/javascript/box-plots/
  """
  alias = 'box'
  name = 'Basic Box Series'
  _attrs = {'type': 'box'}
  _statics = {"boxpoints": 'Outliers'}


class JsHBox(JsBase):
  """
  Configuration for a Box Chart in Plotly

  Documentation
  https://plot.ly/javascript/box-plots/
  """
  alias = 'hbox'
  name = 'Horizontal Box Series'
  _attrs = {'type': 'box'}


class JsSankey(JsBase):
  """
  Configuration for a Sankey Chart in Plotly

  Documentation
  https://plot.ly/javascript/sankey-diagram/
  """
  alias = 'sankey'
  name = 'Sankey Series'
  _attrs = {'type': 'sankey'}


class JsParallelCoordinates(JsBase):
  """
  Configuration for a Box Chart in Plotly

  Documentation
  https://plot.ly/javascript/parallel-coordinates-plot/
  """
  alias = 'parcoords'
  name = 'Parallel Coordinates Series'
  _attrs = {'type': 'parcoords'}


class JsParallelCategory(JsBase):
  """
  Configuration for a Box Chart in Plotly

  Documentation
  https://plot.ly/javascript/parallel-categories-diagram/
  """
  alias = 'parcats'
  name = 'Basic Parallel Categories Diagram'
  _attrs = {'type': 'parcats'}


# ---------------------------------------------------------------------------------------------------------
#                           MAPS / HEATMAPS CHARTS
#
class JsMaps(JsBase):
  """
  Configuration for a Box Chart in Plotly

  Documentation
  https://plot.ly/javascript/choropleth-maps/
  """
  alias = 'choropleth'
  name = 'Country GDP Choropleth Map'
  _attrs = {'type': 'choropleth', "locationmode": 'country names', "autocolorscale": False}


class JsMapsEurope(JsBase):
  """
  Configuration for a Box Chart in Plotly

  Documentation
  https://plot.ly/javascript/choropleth-maps/
  """
  alias = 'europe'
  jsType = 'choropleth'
  name = 'Country GDP Choropleth Map'
  _attrs = {'type': 'choropleth', "locationmode": 'country names', "autocolorscale": False}
  _layout = {"geo": {"showland": True, "projection": {"type": "Mercator"}, "scope": "europe", "showcoastlines": True, "showframe": True}}


class JsHeatMap(JsBase):
  """
  Configuration for a Box Chart in Plotly

  Documentation
  https://plot.ly/javascript/heatmaps/
  """
  alias = 'heatmap'
  name = 'Basic Parallel Categories Diagram'
  _attrs = {'type': 'heatmap', 'showscale': False}


# ---------------------------------------------------------------------------------------------------------
#                           3D CHARTS
#
class JsSurface(JsBase):
  """
  Configuration for a Box Chart in Plotly

  Documentation
  https://plot.ly/javascript/3d-surface-plots/
  """
  alias = 'surface'
  c3d = True
  name = 'Surface Plot'
  _attrs = {'type': 'surface', 'opacity': 0.9}


class JsSurfaceBorder(JsBase):
  """
  Configuration for a Box Chart in Plotly

  Documentation
  https://plot.ly/javascript/3d-surface-plots/
  """
  alias = 'surface-contours'
  name = 'Surface Plot'
  _attrs = {'type': 'surface'}
  _statics = {'contours': {'z': {
      'show': True, 'usecolormap': True, 'highlightcolor': "#42f462", 'project': {'z': True}}}}


class JsScatter3D(JsBase):
  """
  Configuration for a Box Chart in Plotly

  Documentation
  https://plot.ly/javascript/3d-point-clustering/
  """
  alias = 'scatter3d'
  name = '3D Point Clustering'
  _attrs = {'type': 'scatter3d'}
  _layout = {'showlegend': False}

  def _colors(self, cList, indices=None, borderColors=None):
    """

    :param cList:
    :param indices:
    :param borderColors:

    :return:
    """
    if indices is not None:
      if not isinstance(indices, list):
        indices, cList = [indices], [cList]
      for i, index in enumerate(indices):
       self.seriesProperties["dynamic"][index]["marker"].update({'color': cList[i]})
    else:
      for i in range(len(self.data._schema['out']['params'][0])):
        self.seriesProperties["dynamic"].setdefault(i, {})["marker"] = {'color': cList[i]}


class JsLine3D(JsScatter3D):
  """
  Configuration for a Box Chart in Plotly
  """
  alias = 'line3d'
  jsType = 'scatter3d'
  name = '3D Point Clustering'
  _attrs = {'type': 'scatter3d', 'opacity': 1, 'mode': 'lines'}


class JsMesh3D(JsScatter3D):
  """
  Configuration for a Box Chart in Plotly

  Documentation
  https://plot.ly/javascript/3d-point-clustering/
  """
  alias = 'mesh3d'
  name = '3D Clustering'
  _attrs = {'type': 'mesh3d'}
  _layout = {'showlegend': False, 'autosize': True}
  _statics = {'opacity': 0.1}
