"""

"""


from epyk.core.js.configs import JsConfig
from epyk.core.css import Color


class JsBase(JsConfig.JsConfig):
  """
  Base Class for the ChartJs Charts
  """
  listAttributes = ['yAxes', 'xAxes', 'datasets']
  jsCls = 'Chart'
  jsType = None


# ---------------------------------------------------------------------------------------------------------
#                                          CHARTJS Configurations
# ---------------------------------------------------------------------------------------------------------
class JsPie(JsBase):
  """

  Documentation
  https://www.chartjs.org/docs/latest/charts/doughnut.html
  """
  alias = 'pie'
  name = 'Pie Chart'
  _attrs = {
    'type': 'pie',
    'options': {'maintainAspectRatio': False, 'responsive': True, 'legend': {'display': True}, 'scaleShowLabels': False,
                'plugins': {'labels': {'render': 'label', 'position': 'outside', 'fontColor': 'red'}},
                'scales': {
                 'yAxes': [{'ticks': {'display': False}, 'gridLines': {'display': False, 'drawBorder': False}}],
                 'xAxes': [{'ticks': {'display': False}, 'gridLines': {'display': False, 'drawBorder': False}}]}}}

  def config(self):
    pass
    # self._report.jsImports.add('chartjs-pie-labels')

  def _colors(self, cList, index=None, borderColors=None):
    """

    :param cList:
    :param index:
    :param borderColors:
    :return:
    """
    if index is None:
      for i in range(len(self.data._schema['values'])):
        if len(cList) > i:
          self.seriesProperties['dynamic'].setdefault(i, {})['backgroundColor'] = cList
    else:
      self.seriesProperties['dynamic'].setdefault(index, {})['backgroundColor'] = cList


class JsDonut(JsPie):
  """

  Documentation
  https://www.chartjs.org/docs/latest/charts/doughnut.html
  """
  alias = 'donut'
  name = 'Donut Chart'
  _attrs = {
    'type': 'doughnut',
    'options': {'maintainAspectRatio': False, 'responsive': True, 'legend': {'display': True},
                'scaleShowLabels': False,
                'scales': {
                  'yAxes': [{'ticks': {'display': False}, 'gridLines': {'display': False, 'drawBorder': False}}],
                  'xAxes': [{'ticks': {'display': False}, 'gridLines': {'display': False, 'drawBorder': False}}]}}}


class JsLine(JsBase):
  """

  Documentation
  https://www.chartjs.org/docs/latest/charts/line.html
  """
  alias = 'line'
  name = 'Basic Line Chart'
  _statics = {'fill': False}
  _attrs = {
    'type': 'line',
    'options':
      {'maintainAspectRatio': False, 'responsive': True, 'legend': {'display': True},
          'scaleShowLabels': True,
          'scales': {
            'yAxes': [{'ticks': {'display': True, 'beginAtZero': True}, 'gridLines': {'display': True}}],
            'xAxes': [{'ticks': {'display': True, 'beginAtZero': True}, 'gridLines': {'display': True}}]}}}

  def _colors(self, cList, index=None, borderColors=None):
    """

    :param cList:
    :param index:
    :param borderColors:
    :return:
    """
    if index is None:
      for i in range(len(self.data._schema['values'])):
        if len(cList) > i:
          self.seriesProperties['dynamic'].setdefault(i, {})['backgroundColor'] = cList[i]
          self.seriesProperties['dynamic'].setdefault(i, {})['borderColor'] = cList[i]
    else:
      self.seriesProperties['dynamic'].setdefault(index, {})['backgroundColor'] = cList
      self.seriesProperties['dynamic'].setdefault(index, {})['borderColor'] = cList

      
class JsArea(JsBase):
  """

  Documentation
  https://www.chartjs.org/docs/latest/charts/area.html
  """
  alias = 'area'
  name = 'Line (Fill Start)'
  _statics = {'fill': True}
  _attrs = {
    'type': 'line',
    'options':
      {'maintainAspectRatio': False, 'responsive': True, 'legend': {'display': True},
          'scaleShowLabels': True,
          'scales': {
            'yAxes': [{'ticks': {'display': True, 'beginAtZero': True}, 'gridLines': {'display': True}}],
            'xAxes': [{'ticks': {'display': True, 'beginAtZero': True}, 'gridLines': {'display': True}}]}}}

  def _colors(self, cList, index=None, borderColors=None):
    """

    :param cList:
    :param index:
    :param borderColors:

    :return:
    """
    gbList = ["rgba(%s,%s,%s,0.3)" % tuple(Color.ColorMaker.getHexToRgb(val)) for val in cList]
    if index is None:
      for i in range(len(self.data._schema['out']['params'][0])):
        if len(cList) > i:
          self.seriesProperties['dynamic'].setdefault(i, {})['backgroundColor'] = gbList[i]
          self.seriesProperties['dynamic'].setdefault(i, {})['borderColor'] = cList[i]
    else:
      self.seriesProperties['dynamic'].setdefault(index, {})['backgroundColor'] = gbList
      self.seriesProperties['dynamic'].setdefault(index, {})['borderColor'] = cList


class JsAreaEnd(JsArea):
  """

  Documentation
  https://www.chartjs.org/docs/latest/charts/area.html
  """
  alias = 'area-end'
  name = 'Line (Fill End)'
  _statics = {'fill': 'end'}


class JsSteppedLine(JsBase):
  """

  Documentation
  https://www.chartjs.org/docs/latest/charts/line.html
  """
  alias = 'step'
  name = 'Stepped Line Chart'
  _statics = {'fill': False, 'steppedLine': True}
  _attrs = {
    'type': 'line',
    'options':
      {'maintainAspectRatio': False, 'responsive': True, 'legend': {'display': True},
          'scaleShowLabels': True,
          'scales': {
            'yAxes': [{'ticks': {'display': True, 'beginAtZero': True}, 'gridLines': {'display': True}}],
            'xAxes': [{'ticks': {'display': True, 'beginAtZero': True}, 'gridLines': {'display': True}}]}}}


class JsBar(JsBase):
  """
  Configuration for a Bars Chart in ChartJs

  Documentation
  https://www.chartjs.org/docs/latest/charts/bar.html
  """
  alias = 'bar'
  name = 'Bars'
  _attrs = {
    'type': 'bar',
    'options': {
        'maintainAspectRatio': False,
        'responsive': True,
        'legend': {'display': True},
                   'scales': {
                      'yAxes': [{'ticks': {'display': True, 'beginAtZero': True}}],
                      'xAxes': [{'ticks': {'display': True}}]}}
  }


class JsBarStacked(JsBase):
  """
  Configuration for a Bars Chart in ChartJs

  Documentation
  https://www.chartjs.org/docs/latest/charts/bar.html
  """
  alias = 'bar-stacked'
  name = 'Bars'
  _attrs = {
    'type': 'bar',
    'options': {
        'maintainAspectRatio': False,
        'responsive': True,
        'legend': {'display': True},
                   'scales': {
                      'yAxes': [{'stacked': True, 'ticks': {'display': True, 'beginAtZero': True}}],
                      'xAxes': [{'stacked': True, 'ticks': {'display': True}}]}}
  }


class JsHBar(JsBase):
  """
  Configuration for a Horizontal Bars Chart in ChartJs

  Documentation
  https://www.chartjs.org/docs/latest/charts/bar.html
  """
  alias = 'hbar'
  name = 'Horizontal Bars'
  _attrs = {
      'type': 'horizontalBar',
      'options':
        {'maintainAspectRatio': False, 'responsive': True, 'legend': {'display': True},
            'scales': {
                'yAxes': [{'ticks': {'display': True, 'beginAtZero': True}}],
                'xAxes': [{'ticks': {'display': True, 'beginAtZero': True}}]}}}


class JsMultiBar(JsBase):
  """

  Documentation
  https://www.chartjs.org/docs/latest/charts/mixed.html
  """
  alias = 'multi'
  name = 'Multi Bars Chart'
  _attrs = {'type': 'bar', 'options': {
      'maintainAspectRatio': False, 'responsive': True, 'legend': {'display': True},
      'scales': {
        'yAxes': [{'ticks': {'display': True, 'beginAtZero': True}}],
        'xAxes': [{'ticks': {'display': True}}]}}}

  #def dataSetType(self, chartType, seriesId):
  #  self.seriesProperties['dynamic'][seriesId] = {'type': chartType, 'fill': False}


class JsScatter(JsBase):
  """

  Documentation
  https://www.chartjs.org/docs/latest/charts/scatter.html
  """
  alias = 'scatter'
  name = 'Scatter Chart'
  jsType = 'scatter'
  _statics = {'pointStyle': 'circle'}
  _attrs = {
    'type': 'scatter',
    'options':
      {'maintainAspectRatio': False, 'responsive': True, 'legend': {'display': True},
       'scales': {
         'yAxes': [{'ticks': {'display': True, 'beginAtZero': True}, 'gridLines': {'display': True}}],
         'xAxes': [{'ticks': {'display': True, 'beginAtZero': True}, 'gridLines': {'display': True}}]}}}

  def _colors(self, cList, index=None, borderColors=None):
    """

    :param cList:
    :param index:
    :param borderColors:

    :return:
    """
    if borderColors is None:
      borderColors = cList
    if index is None:
      for i in range(len(self.data._schema['values'])):
        if len(cList) > i:
          self.seriesProperties['dynamic'].setdefault(i, {})['backgroundColor'] = cList[i]
          self.seriesProperties['dynamic'][i]['borderColor'] = borderColors[i]
    else:
      self.seriesProperties['dynamic'].setdefault(index, {})['backgroundColor'] = cList
      self.seriesProperties['dynamic'][index]['borderColor'] = borderColors


class JsBubble(JsBase):
  """

  Documentation
  https://www.chartjs.org/docs/latest/charts/bubble.html
  """
  alias = 'bubble'
  name = 'Bubble Chart'
  _attrs = {
    'type': 'bubble',
    'options': {
      'maintainAspectRatio': False, 'responsive': True, 'legend': {'display': True},
      'scales': {
        'yAxes': [{'ticks': {'display': True}, 'gridLines': {'display': False}}],
        'xAxes': [{'ticks': {'display': True}, 'gridLines': {'display': False}}]}}}


class JsPolar(JsBase):
  """

  Documentation
  https://www.chartjs.org/docs/latest/charts/polar.html
  """
  alias = 'polar'
  name = 'Polar Chart'
  _attrs = {
    'type': 'polarArea',
    'options': {
      'maintainAspectRatio': False, 'responsive': True, 'legend': {'display': True},
      'scales': {
        'yAxes': [{'ticks': {'display': False}, 'gridLines': {'display': False, 'drawBorder': False}}],
        'xAxes': [{'ticks': {'display': False}, 'gridLines': {'display': False, 'drawBorder': False}}]}}}

  def _colors(self, cList, index=None, borderColors=None):
    """

    :param cList:
    :param index:
    :param borderColors:

    :return:
    """
    self.addAttr('gridLines', {"color": self._report.getColor("greys", 3)}, ['scale'], category='options')
    rgbList = ["rgba(%s,%s,%s,0.5)" % tuple(Color.ColorMaker.getHexToRgb(val)) for val in cList]
    if index is None:
      for i in range(len(self.data._schema['values'])):
        if len(cList) > i:
          self.seriesProperties['dynamic'].setdefault(i, {})['backgroundColor'] = rgbList
          self.seriesProperties['dynamic'].setdefault(i, {})['borderColor'] = cList
    else:
      self.seriesProperties['dynamic'].setdefault(index, {})['backgroundColor'] = rgbList
      self.seriesProperties['dynamic'].setdefault(index, {})['borderColor'] = cList[index]


class JsRadar(JsBase):
  """

  Documentation
  https://www.chartjs.org/docs/latest/charts/radar.html
  """
  alias = 'radar'
  name = 'Radar Chart'
  _attrs = {
    'type': 'radar',
    'options': {'maintainAspectRatio': False, 'responsive': True, 'legend': {'display': True},
        'scaleShowLabels': False,
        'scale': {'ticks': {'beginAtZero': True}},
        'scales': {
          'yAxes': [{'ticks': {'display': False}, 'gridLines': {'display': False}}],
          'xAxes': [{'ticks': {'display': False}, 'gridLines': {'display': False}}]}}}

  def _colors(self, cList, index=None, borderColors=None):
    """

    :param cList:
    :param index:
    :param borderColors:

    :return:
    """
    self.addAttr('gridLines', {"color": self._report.getColor("greys", 3)}, ['scale'], category='options')
    self.addAttr('angleLines', {"color": self._report.getColor("greys", 3)}, ['scale'], category='options')
    self.addAttr('pointLabels', {"fontColor": self._report.getColor("greys", -1)}, ['scale'], category='options')
    rgbList = ["rgba(%s,%s,%s,0.3)" % tuple(Color.ColorMaker.getHexToRgb(val)) for val in cList]
    if index is None:
      for i in range(len(self.data._schema['out']['params'][0])):
        self.seriesProperties['dynamic'].setdefault(i, {})['backgroundColor'] = rgbList[i]
        self.seriesProperties['dynamic'].setdefault(i, {})['pointBackgroundColor'] = cList[i]
        self.seriesProperties['dynamic'].setdefault(i, {})['borderColor'] = cList[i]
        self.seriesProperties['dynamic'].setdefault(i, {})['borderWidth'] = 1
    else:
      self.seriesProperties['dynamic'].setdefault(index, {})['backgroundColor'] = rgbList[index]
      self.seriesProperties['dynamic'].setdefault(index, {})['pointBackgroundColor'] = cList[index]
      self.seriesProperties['dynamic'].setdefault(index, {})['borderColor'] = cList[index]
      self.seriesProperties['dynamic'].setdefault(index, {})['borderWidth'] = 1
