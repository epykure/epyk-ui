
from epyk.core.html import Html
from epyk.core.js import JsUtils

# from epyk.core.html.graph import AxisDisplay
from epyk.core.html.graph import GraphFabric
from epyk.core.js.packages import JsChartJs
from epyk.core.js.packages import JsD3

# The list of CSS classes
# from epyk.core.css.styles import CssGrpClsCharts


# Define a set of common standard properties cross charting libraries.
# The below mapping will ensure the correct definition is applied
CHART_ATTRS = {
  # Chart layout
  'bottom': {"key": "bottom", "tree": ['layout', 'padding'], "category": "options"},
  'top': {"key": "top", "tree": ['layout', 'padding'], "category": "options"},

  # Legend
  'legendPosition': {"key": "position", "tree": ['legend'], "category": "options"},
  'legendFontColor': {"key": "fontColor", "tree": ['legend', 'labels'], "category": "options"},

  # Title
  'title': {"key": "text", "tree": ['title'], "category": "options"},
  'titleDisplay': {"key": "display", "tree": ['title'], "category": "options"},
  'titleFontColor': {"key": "fontColor", "tree": ['title'], "category": "options"},

  # Axes
  'grid': [
    {"key": "drawOnChartArea", "tree": ['scales', 'xAxes', 'gridLines'], "category": "options"},
    {"key": "drawOnChartArea", "tree": ['scales', 'yAxes', 'gridLines'], "category": "options"},
  ],
  'xLabel': {"key": "labelString", "tree": ['scales', "xAxes", 'scaleLabel'], "category": "options"},
  'xDisplay': {"key": "display", "tree": ['scales', "xAxes", 'scaleLabel'], "category": "options"},
  'xFontColor': [
    {"key": "fontColor", "tree": ['scales', 'xAxes', 'ticks'], "category": "options"},
    {"key": "color", "tree": ['scales', 'xAxes', 'gridLines'], "category": "options"}
  ],
  'xGrid': {"key": "display", "tree": ['scales', 'xAxes', 'gridLines'], "category": "options"},
  'yLabel': {"key": "labelString", "tree": ['scales', "yAxes", 'scaleLabel'], "category": "options"},
  'yDisplay': {"key": "display", "tree": ['scales', "yAxes", 'scaleLabel'], "category": "options"},
  'precision': {"key": "precision", "tree": ['scales', 'yAxes', 'ticks'], "category": "options"},
  'yFontColor': [
    {"key": "fontColor", "tree": ['scales', 'yAxes', 'ticks'], "category": "options"},
    {"key": "color", "tree": ['scales', 'yAxes', 'gridLines'], "category": "options"}],
  'yGrid': {"key": "display", "tree": ['scales', 'yAxes', 'gridLines'], "category": "options"},

}


class Chart(Html.Html):
  name, category, callFnc = 'ChartJs', 'Charts', 'chartJs'
  # _grpCls = CssGrpClsCharts.CssClassChartsNvd3

  def __init__(self,  report, width, height, title, options, htmlCode, filters, profile):
    self.seriesProperties, self.__chartJsEvents, self.height = {'static': {}, 'dynamic': {}}, {}, height[0]
    super(Chart, self).__init__(report, [], code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self._chart = None, None

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
    return JsUtils.jsConvertFncs([JsChartJs.ChartJs(self.dom.varId, self._chart, varName=self.chartId, src=self._report)], toStr=True)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    strChart = '<div style="height:%spx;margin-top:10px"><canvas id="%s"></canvas></div>' % (self.height-40, self.htmlId)
    return GraphFabric.Chart.html(self, self.get_attrs(withId=False, pyClassNames=self.style.get_classes()), strChart)


class ChartLine(Chart):
  @property
  def chart(self):
    """
    :rtype: JsChartJs.ChartJsTypeBar
    """
    if self._chart is None:
      self._chart = JsChartJs.ChartJsTypeBar(self._report, [])
    return self._chart


class ChartBar(Chart):
  @property
  def chart(self):
    """
    :rtype: JsChartJs.ChartJsTypeBar
    """
    if self._chart is None:
      self._chart = JsChartJs.ChartJsTypeBar(self._report, [])
    return self._chart


class ChartPie(Chart):
  @property
  def chart(self):
    """
    :rtype: JsChartJs.ChartJsTypeBar
    """
    if self._chart is None:
      self._chart = JsChartJs.ChartJsTypeBar(self._report, [])
    return self._chart


class ChartScatter(Chart):
  @property
  def chart(self):
    """
    :rtype: JsChartJs.ChartJsTypeBar
    """
    if self._chart is None:
      self._chart = JsChartJs.ChartJsTypeBar(self._report, [])
    return self._chart
