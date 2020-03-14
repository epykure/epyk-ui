
from epyk.core.html import Html
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsNvd3
from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name, category, callFnc = 'NVD3', 'Charts', 'nvd3.chart'

  def __init__(self,  report, width, height, title, options, htmlCode, filters, profile):
    self.seriesProperties, self.__chartJsEvents, self.height = {'static': {}, 'dynamic': {}}, {}, height[0]
    super(Chart, self).__init__(report, [], code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3 = None

  @property
  def chartId(self):
    """
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

  def add_trace(self, data, name=""):
    dataset = {"values": data, 'key': name}
    next_index = len(self._vals)
    if len(self._report.theme.colors) > next_index:
      dataset['color'] = self._report.theme.colors[next_index]
    self._vals.append(dataset)
    return self

  @property
  def d3(self):
    if self._d3 is None:
      self._d3 = JsD3.D3Select(self._report, id="#%s" % self.htmlId)
    return self._d3

  def build(self, data=None, options=None, profile=False):
    return JsUtils.jsConvertFncs([self.dom.set_var(True), self.dom.xAxis, self.d3.datum(data).call(self.dom.var),
                "nv.utils.windowResize(function() { %s.update() })" % self.dom.var], toStr=True)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<svg %s></svg>' % self.get_attrs(pyClassNames=self.style.get_classes())


class ChartLine(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3Line
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Line(self._report, varName=self.chartId)
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


class ChartPie(Chart):

  @property
  def dom(self):
    """
    :rtype: JsNvd3.JsNvd3Pie
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Pie(self._report, varName=self.chartId)
    return self._dom

  def add_trace(self, data, name=""):
    #next_index = len(self._vals)
    #if len(self._report.theme.colors) > next_index:
    #  dataset['color'] = self._report.theme.colors[next_index]
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
