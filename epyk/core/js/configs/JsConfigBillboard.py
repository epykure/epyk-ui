"""

"""


from epyk.core.js.configs import JsConfig


class JsBase(JsConfig.JsConfig):
  """
  Base Class for the C3 Charts
  """
  listAttributes = []
  jsCls = 'Chart'

  def toJs(self, options=None):
    """
    Returns the Javascript String representation

    :param options:

    :return:
    """
    ctx = []
    self.resolveDict(dict([(key, val) for key, val in self.items() if val]), ctx)
    return ctx


# ---------------------------------------------------------------------------------------------------------
#                                          C3 Configurations
# ---------------------------------------------------------------------------------------------------------
class JsBar(JsBase):
  """
  Configuration for a Bars Chart in C3

  Documentation
  https://c3js.org/samples/chart_bar.html
  """
  alias = 'bar'
  name = 'Bars'
  _attrs = {
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'data': {'x': 'x', 'type': 'bar'},
    'regions': [],
    'axis': {'x': {'type': '"category"'}},
    'subchart': {'show': False},
    'legend': {'show': True},
    'zoom': {'enabled': False},
    'tooltip': {}
  }


class JsHBar(JsBase):
  """
  Configuration for a Horizontal Bars Chart in C3

  Documentation
  https://c3js.org/samples/chart_bar.html
  """
  alias = 'hbar'
  name = 'Horizontal Bars'
  _attrs = {
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'data': {'x': 'x', 'type': 'bar'},
    'regions': [],
    'axis': {'x': {'type': 'category'}, 'rotated': True},
    'subchart': {'show': False},
    'legend': {'show': True},
    'zoom': {'enabled': False},
    'tooltip': {}
  }


class JsScatter(JsBase):
  """
  Configuration for a Basic line Chart in C3

  Documentation
  https://c3js.org/samples/chart_scatter.html
  """
  alias = 'scatter'
  name = 'Scatter Chart'
  _attrs = {
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'data': {'type': 'scatter'},
    'regions': [], 'area': {},
    'axis': {'x': {'tick': {'culling': {'max': 10}}}},
    'subchart': {'show': False}, 'legend': {'show': True}, 'zoom': {'enabled': False},
    'tooltip': {}, 'point': {},
    'fill': False
  }


class JsLine(JsBase):
  """
  Configuration for a Basic line Chart in C3

  Documentation
  https://c3js.org/samples/simple_multiple.html
  """
  alias = 'line'
  name = 'Line Chart'
  _attrs = {
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'data': {'x': 'x'},
    'regions': [],
    'area': {},
    'axis': {
      'y': {}, #'tick': {'count': 5}
      'x': {'tick': {'multiline': False, 'culling': {'max': 14}}, 'type': 'category'}},
    'subchart': {'show': True},
    'legend': {'show': True, 'position': 'inset'},
    'zoom': {'enabled': False},
    'tooltip': {},
    'fill': None
  }


class JsSpline(JsBase):
  """
  Configuration for a Basic line Chart in C3

  Documentation
  https://c3js.org/samples/chart_spline.html
  """
  alias = 'spline'
  name = 'Spline Chart'
  _attrs = {
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'data': {'x': 'x', 'type': 'spline'},
    'regions': [],
    'area': {},
    'axis': {'x': {'tick': {'culling': {'max': 10}}, 'type': 'category'}},
    'subchart': {'show': False},
    'legend': {'show': True},
    'zoom': {'enabled': False},
    'tooltip': {},
    'fill': None
  }


class JsStep(JsBase):
  """
  Configuration for a Basic line Chart in C3

  Documentation
  https://c3js.org/samples/chart_step.html
  """
  alias = 'step'
  name = 'Step Chart'
  _attrs = {
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'data': {'x': 'x', 'type': 'step'},
    'regions': [],
    'area': {},
    'axis': {'x': {'tick': {'culling': {'max': 10}}, 'type': 'category'}},
    'subchart': {'show': False},
    'legend': {'show': True},
    'zoom': {'enabled': False},
    'tooltip': {},
    'fill': None
  }


class JsArea(JsBase):
  """

  Documentation
  https://c3js.org/samples/chart_area.html
  """
  alias = 'area'
  name = 'Area Chart'
  _attrs = {
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'data': {'x': 'x', 'type': 'area'},
    'regions': [],
    'area': {},
    'axis': {'x': {'tick': {'culling': {'max': 10}}, 'type': 'category'}},
    'subchart': {'show': False},
    'legend': {'show': True},
    'zoom': {'enabled': False},
    'tooltip': {},
    'fill': None
  }


class JsAreaSpline(JsBase):
  """

  Documentation
  https://c3js.org/samples/chart_area.html
  """
  alias = 'area-spline'
  name = 'Area Spline Chart'
  _attrs = {
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'data': {'x': 'x', 'type': 'area-spline'},
    'regions': [],
    'area': {},
    'axis': {'x': {'tick': {'culling': {'max': 10}}, 'type': 'category'}},
    'subchart': {'show': False},
    'legend': {'show': True},
    'zoom': {'enabled': False},
    'tooltip': {},
    'fill': None
  }


class JsAreaStep(JsBase):
  """

  Documentation
  https://c3js.org/samples/chart_area.html
  """
  alias = 'area-step'
  name = 'Area Step Chart'
  _attrs = {
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'data': {'x': 'x', 'type': 'area-step'},
    'regions': [],
    'area': {},
    'axis': {'x': {'tick': {'culling': {'max': 10}}, 'type': 'category'}},
    'subchart': {'show': False},
    'legend': {'show': True},
    'zoom': {'enabled': False},
    'tooltip': {},
    'fill': None
  }


class JsPie(JsBase):
  """
  Configuration for a Pie Chart in C3

  Documentation

  """
  alias = 'pie'
  name = 'Pie Chart'
  _attrs = {
    'data': {'x': 'x', 'type': 'pie'},
    'axis': {'x': {'type': 'category'}},
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'subchart': {'show': False},
    'legend': {'show': True},
    'zoom': {'enabled': False}
  }


class JsDonut(JsBase):
  """
  Configuration for a Donut Chart in C3

  Documentation

  """
  alias = 'donut'
  name = 'Donut Chart'
  _attrs = {
    'data': {'x': 'x', 'type': 'donut'},
    'axis': {'x': {'type': 'category'}},
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'subchart': {'show': False},
    'legend': {'show': True},
    'zoom': {'enabled': False}
  }


class JsGauge(JsBase):
  """
  Configuration for a Donut Chart in C3

  Documentation
  https://c3js.org/samples/chart_pie.html
  """
  alias = 'gauge'
  name = 'Gauge Chart'
  _attrs = {
    'data': {'x': 'x', 'type': 'gauge'},
    'axis': {'x': {'type': 'category'}},
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'subchart': {'show': False},
    'legend': {'show': True},
    'zoom': {'enabled': False}
  }


class JsRadar(JsBase):
  """
  Configuration for a Radar Chart in C3

  Documentation
  https://naver.github.io/billboard.js/demo/#Chart.RadarChart
  """
  alias = 'radar'
  name = 'Radar Chart'
  _attrs = {
    'data': {'x': 'x', 'type': 'radar', 'labels': True},
    'axis': {},
    'grid': {'x': {'show': True}, 'y': {'show': True}, 'enabled': True},
    'subchart': {'show': False},
    'legend': {'show': True},
    'zoom': {'enabled': False}
  }


class JsBubble(JsBase):
  """
  Configuration for a Bubble Chart in C3

  Documentation
  https://naver.github.io/billboard.js/demo/#Chart.BubbleChart
  """
  alias = 'bubble'
  name = 'Bubble Chart'
  _attrs = {
    'data': {'x': 'x', 'type': 'bubble', 'labels': True},
    'axis': {'x': {'type': 'category'}},
    'bubble': {"maxR": 50},
    'subchart': {'show': False},
    'zoom': {'enabled': False},
    'grid': {}
  }
