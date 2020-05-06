
from epyk.core.html import Html
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsNvd3
from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name, category, callFnc = 'NVD3', 'Charts', 'nvd3.chart'

  def __init__(self,  report, width, height, title, options, htmlCode, filters, profile):
    self.seriesProperties, self.__chartJsEvents, self.height = {'static': {}, 'dynamic': {}}, {}, height[0]
    super(Chart, self).__init__(report, [], code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self.html_items = None, []
    if title is not None:
      h_title = report.ui.title(title, level=2).css({"padding-left": '10px'})
      h_title.inReport = False
      self.html_items.append(h_title)

  @property
  def chartId(self):
    """
    Description:
    ------------
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlId

  @property
  def data(self):
    return self._vals[-1]

  def traces(self, i=None):
    """

    :rtype: JsChartJs.DataSetPie
    """
    if i is None:
      return self._vals[-1]

    return self._vals[i]

  def click(self, jsFnc, profile=False):
    raise Exception("Not implemented for this chart ")

  def add_trace(self, data, name=""):
    dataset = {"values": data, 'key': name}
    next_index = len(self._vals)
    if len(self._report.theme.colors) > next_index:
      dataset['color'] = self._report.theme.colors[next_index]
    self._vals.append(dataset)
    return self

  @property
  def d3(self):
    """

    :rtype: JsD3.D3Select
    """
    if self._d3 is None:
      self._d3 = JsD3.D3Select(self._report, selector="d3.select('#%s')" % self.htmlId, setVar=False)
    return self._d3

  def build(self, data=None, options=None, profile=False):
    return JsUtils.jsConvertFncs([self.dom.set_var(True), self.dom.xAxis, self.d3.datum(data).call(self.dom.var),
                "nv.utils.windowResize(function() { %s.update() })" % self.dom.var], toStr=True)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    str_items = "".join([h.html() for h in self.html_items])
    return '%s<svg %s></svg>' % (str_items, self.get_attrs(pyClassNames=self.style.get_classes()))


class ChartLine(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3Line
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Line(self._report, varName=self.chartId)
    return self._dom


class ChartScatter(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3Line
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Scatter(self._report, varName=self.chartId)
    return self._dom


class ChartCumulativeLine(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3CumulativeLine
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3CumulativeLine(self._report, varName=self.chartId)
    return self._dom


class ChartFocusLine(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3CumulativeLine
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3LineWithFocus(self._report, varName=self.chartId)
    return self._dom


class ChartBar(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3Bar
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Bar(self._report, varName=self.chartId)
    return self._dom


class ChartHorizontalBar(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3Bar
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3MultiBarHorizontal(self._report, varName=self.chartId)
    return self._dom


class ChartMultiBar(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3Bar
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3MultiBar(self._report, varName=self.chartId)
    return self._dom


class ChartPie(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3Pie
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Pie(self._report, varName=self.chartId)
    return self._dom

  def click(self, jsFnc, profile=False):
    self.onReady("%s.pie.dispatch.on('elementClick', function(event){ %s })" % (self.dom.varName, JsUtils.jsConvertFncs(jsFnc, toStr=True)))
    return self

  def add_trace(self, data, name=""):
    """

    :param data:
    :param name:
    """
    self.dom.color(self._report.theme.colors)
    self._vals = data
    return self


class ChartArea(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3Area
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Area(self._report, varName=self.chartId)
    return self._dom


class ChartHistoBar(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3Area
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3HistoricalBar(self._report, varName=self.chartId)
    return self._dom


class ChartParallelCoord(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3ParallelCoordinates
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3ParallelCoordinates(self._report, varName=self.chartId)
    return self._dom

  def set_dimension_names(self, dimensions):
    """

    :param dimensions:
    """
    self.__dimensions = dimensions
    self.dom.dimensionNames(dimensions)
    return self

  def add_trace(self, data, name=""):
    """

    :param data:
    :param name:
    """
    self._vals = data
    return self


class ChartSunbrust(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3Sunburst
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Sunburst(self._report, varName=self.chartId)
    return self._dom

  def set_rcolors(self, color, data):
    """

    :param color:
    :param data:
    """
    for rec in data:
      rec['color'] = color
      if 'children' in rec:
        self.set_rcolors(color, rec['children'])

  def add_trace(self, data, name=""):
    """

    :param data:
    :param name:
    """
    for i, rec in enumerate(data):
      rec['color'] = self._report.theme.colors[i+1]
      self.set_rcolors(rec['color'], rec['children'])
    self._vals = [{'name': name, 'children': data, 'color': self._report.theme.colors[0]}]
    return self


class ChartBoxPlot(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3BoxPlot
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3BoxPlot(self._report, varName=self.chartId)
    return self._dom

  def add_box(self, q1, q3=None, outliers=None, maxRegularValue=None, mean=None, median=None, minRegularValue=None,
              minOutlier=None, maxOutlier=None, title=None):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param q1:
    :param q3:
    :param outliers:
    :param maxRegularValue:
    :param mean:
    :param median:
    :param minRegularValue:
    :param minOutlier:
    :param maxOutlier:
    """
    names = ['q1', 'median', 'q3', 'outlData', 'maxRegularValue', 'mean', 'minRegularValue', 'minOutlier', 'maxOutlier']
    row = {}
    for i, val in enumerate([q1, median, q3, outliers, maxRegularValue, mean, minRegularValue, minOutlier, maxOutlier]):
      if val is not None:
        row[names[i]] = val
      elif names[i] == 'outlData':
        row['outlData'] = []
    series_id = len(self._vals) - 1
    row['seriesColor'] = self._report.theme.colors[series_id]
    row['title'] = title or "Series %s" % series_id
    self._vals.append(row)
    return self

  def add_trace(self, data, name=""):
    """

    :param data:
    :param name:
    """
    self._vals = data
    return self


class ChartCandlestick(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3BoxPlot
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3CandlestickBar(self._report, varName=self.chartId)
    return self._dom


class ChartOhlcBar(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3OhlcBar
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3OhlcBar(self._report, varName=self.chartId)
    return self._dom


class ChartForceDirected(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3BoxPlot
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3ForceDirectedGraph(self._report, varName=self.chartId)
    return self._dom

  def add_trace(self, data, name=""):
    """

    :param data:
    :param name:
    """
    for d in data.get('nodes', []):
      d['color'] = self._report.theme.colors[d.get('group', 1)]
    self._vals = data
    return self
