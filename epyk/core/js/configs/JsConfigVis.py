"""

"""


from epyk.core.js.configs import JsConfig


class JsBase(JsConfig.JsConfig):
  """
  Base Class for the Plotly Charts
  """
  jsCls = 'Graph2d'
  reference = None  # The main link to get the documentation of this chart
  _statics = None  # Static configuration will be added to each dara set automatically
  jsType = None  # Attach the chart to a family for the data transformation
  _attrs = None
  jsQueryData = '{xaxis: event.time, column: event.value[0], src: event}'

  def __init__(self, report, data, seriesProperties):
    super(JsBase, self).__init__(report, data, seriesProperties)
    self.config()

  def config(self):
    if self._statics is not None:
      self.seriesProperties["static"].update(self._statics)

  @property
  def options(self):
    return self


# ---------------------------------------------------------------------------------------------------------
#                                          VIS Configurations
# ---------------------------------------------------------------------------------------------------------
class JsBar(JsBase):
  """
  Configuration for a Bars Chart in Vis

  Documentation
  http://visjs.org/examples/graph2d/11_barsSideBySideGroups.html
  """
  alias = 'bar'
  name = 'Bars'
  _attrs = {'style': 'bar', 'moveable': False, 'drawPoints': True, 'stack': False, 'orientation': 'top',
            'barChart': {'align': 'center', 'sideBySide': True},
            'dataAxis': {'icons': True}}


class JsLine(JsBase):
  """
  Configuration for a Bars Chart in Vis

  Documentation
  http://visjs.org/examples/graph2d/01_basic.html
  """
  alias = 'line'
  name = 'Line Plot'
  _attrs = {'style': 'line', 'moveable': False, 'drawPoints': False}


class JsScatter(JsBase):
  """
  Configuration for a Bars Chart in Vis

  Documentation
  http://visjs.org/examples/graph2d/18_scatterplot.html
  """
  alias = 'scatter'
  name = 'Scatter Plot'
  _attrs = {'style': 'points', 'sampling': True, 'sort': False, 'defaultGroup': 'Scatterplot', 'moveable': False}


#---------------------------------------------------------------------------------------------------------
#                           3D CHARTS
#
class JsSurface(JsBase):
  """
  Configuration for a Box Chart in Vis

  Documentation
  http://visjs.org/graph3d_examples.html
  """
  jsCls = 'Graph3d'
  alias = 'surface'
  name = 'Surface Plot'
  _attrs = {'style': 'surface', 'keepAspectRatio': True, 'verticalRatio': 0.5, 'showPerspective': True,
            'showGrid': True, 'showShadow': False, #, 'height': '100%'
            #'backgroundColor': {'strokeWidth': 0},
            }


class JsScatter3D(JsBase):
  """

  Documentation
  http://visjs.org/examples/graph3d/07_dot_cloud_colors.html
  """
  jsCls = 'Graph3d'
  alias = 'scatter3d'
  _attrs = {'tooltip': True}


class JsBubble3D(JsBase):
  """

  Documentation
  http://visjs.org/examples/graph3d/07_dot_cloud_colors.html
  """
  jsCls = 'Graph3d'
  alias = 'bubble'
  _attrs = {'style': 'dot-size', 'tooltip': True, 'keepAspectRatio': True, 'showPerspective': True}


class JsGroup3D(JsBase):
  """

  Documentation
  http://visjs.org/examples/graph3d/07_dot_cloud_colors.html
  """
  alias = 'series3d'
  jsType = 'bubble'
  _attrs = {'style': 'dot-color', 'keepAspectRatio': True, 'showPerspective': True, 'verticalRatio': 0.5, 'tooltip': True,
            'showGrid': True, 'showShadow': False, 'legendLabel': 'color value', 'showLegend': False}


class JsLine3D(JsScatter3D):
  """

  Documentation
  http://visjs.org/examples/graph3d/05_line.html
  """
  jsCls = 'Graph3d'
  alias = 'line3d'
  _attrs = {'style': 'line', 'tooltip': True}


class JsBar3D(JsScatter3D):
  """

  Documentation
  http://visjs.org/examples/graph3d/12_custom_labels.html
  """
  jsCls = 'Graph3d'
  alias = 'bar3d'
  _attrs = {'style': 'bar', 'tooltip': True}


class JsBarColor3D(JsScatter3D):
  """

  Documentation
  http://visjs.org/examples/graph3d/12_custom_labels.html
  """
  alias = 'barSeries3d'
  jsType = 'bubble'
  _attrs = {'style': 'bar-color', 'tooltip': True}


#---------------------------------------------------------------------------------------------------------
#                           TIMELINE CHARTS
#
class JsTimeLine(JsBase):
  """

  Documentation
  http://visjs.org/examples/timeline/basicUsage.html
  """
  alias = 'timeline'
  jsCls = 'Timeline'
  name = 'Basic Timeline'


#---------------------------------------------------------------------------------------------------------
#                           NETWORK CHARTS
#
class JsNetwork(JsBase):
  """

  Documentation
  http://visjs.org/examples/network/basicUsage.html
  """
  jsCls = 'Network'
  alias = 'network'
  name = 'Basic Network'
  jsQueryData = '{column: event, src: event}'
