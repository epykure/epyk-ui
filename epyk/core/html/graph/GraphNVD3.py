
from epyk.core.html import Html

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject
from epyk.core.js.html import JsHtmlD3

from epyk.core.html.graph import GraphFabric
from epyk.core.js.packages import JsNvd3
from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name, category, callFnc = 'NVD3', 'Charts', 'nvd3.chart'
  # _grpCls = CssGrpClsCharts.CssClassChartsNvd3

  def __init__(self,  report, width, height, title, options, htmlCode, filters, profile):
    self.seriesProperties, self.__chartJsEvents, self.height = {'static': {}, 'dynamic': {}}, {}, height[0]
    super(Chart, self).__init__(report, [], code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self._chart = None, None

  @property
  def dom(self):
    """
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlD3.JsHtmlD3
    """
    if self._dom is None:
      self._dom = JsHtmlD3.JsHtmlD3(self, report=self._report)
    return self._dom

  @property
  def chartId(self):
    """
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlId

  @property
  def d3(self):
    if self._d3 is None:
      self._d3 = JsD3.D3Select(self._report, id="#%s" % self.htmlId)
    return self._d3

  @property
  def chart(self):
    raise Exception("Chart object should be defined in the configuration")

  @property
  def _js__builder__(self):
    return JsUtils.jsConvertFncs([
      self.chart.set_var(True), self.chart.xAxis, self.d3.datum(JsObject.JsObject.get('data')).call(self.chart.var)], toStr=True)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    strChart = '<svg id="%s"></svg>' % self.htmlId
    return GraphFabric.Chart.html(self, self.get_attrs(withId=False, pyClassNames=self.style.get_classes()), strChart)


class ChartLine(Chart):
  @property
  def chart(self):
    """
    :rtype: JsNvd3.JsNvd3Line
    """
    if self._chart is None:
      self._chart = JsNvd3.JsNvd3Line(self._report, varName=self.chartId)
    return self._chart


class ChartBar(Chart):
  @property
  def chart(self):
    """
    :rtype: JsNvd3.JsNvd3Bar
    """
    if self._chart is None:
      self._chart = JsNvd3.JsNvd3Bar(self._report, varName=self.chartId)
    return self._chart


class ChartPie(Chart):
  @property
  def chart(self):
    """
    :rtype: JsNvd3.JsNvd3Pie
    """
    if self._chart is None:
      self._chart = JsNvd3.JsNvd3Pie(self._report, varName=self.chartId)
    return self._chart


class ChartArea(Chart):
  @property
  def chart(self):
    """
    :rtype: JsNvd3.JsNvd3Area
    """
    if self._chart is None:
      self._chart = JsNvd3.JsNvd3Area(self._report, varName=self.chartId)
    return self._chart
