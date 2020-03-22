
from epyk.core.html import Html

from epyk.core.js.packages import JsDc


class Chart(Html.Html):
  name, category, callFnc = 'DC', 'Charts', 'dc'
  __reqCss, __reqJs = ['dc'], ['dc', 'crossfilter']

  def __init__(self,  report, width, height, title, options, htmlCode, profile):
    super(Chart, self).__init__(report, [], code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)

  @property
  def chartId(self):
    """
    Return the Javascript variable of the chart
    """
    return "chart_%s" % self.htmlId

  def build(self, data=None, options=None, profile=False):
    return self.dom.render().toStr()

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class ChartLine(Chart):
  __reqCss, __reqJs = ['dc'], ['dc', 'crossfilter']

  @property
  def dom(self):
    """
    :rtype: JsChartDC.JsLine
    """
    if self._dom is None:
      self._dom = JsDc.Line(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartBar(Chart):
  __reqCss, __reqJs = ['dc'], ['dc', 'crossfilter']

  @property
  def dom(self):
    """
    :rtype: JsChartDC.JsLine
    """
    if self._dom is None:
      self._dom = JsDc.Bar(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartRow(Chart):
  __reqCss, __reqJs = ['dc'], ['dc', 'crossfilter']

  @property
  def dom(self):
    """
    :rtype: JsChartDC.JsLine
    """
    if self._dom is None:
      self._dom = JsDc.Row(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartScatter(Chart):
  __reqCss, __reqJs = ['dc'], ['dc', 'crossfilter']

  @property
  def dom(self):
    """
    :rtype: JsDc.Scatter
    """
    if self._dom is None:
      self._dom = JsDc.Scatter(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartPie(Chart):
  __reqCss, __reqJs = ['dc'], ['dc', 'crossfilter']

  @property
  def dom(self):
    """
    :rtype: JsDc.Sunburst
    """
    if self._dom is None:
      self._dom = JsDc.Pie(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartSunburst(Chart):
  __reqCss, __reqJs = ['dc'], ['dc', 'crossfilter']

  @property
  def dom(self):
    """
    :rtype: JsDc.Sunburst
    """
    if self._dom is None:
      self._dom = JsDc.Sunburst(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartSeries(Chart):
  __reqCss, __reqJs = ['dc'], ['dc', 'crossfilter']

  @property
  def dom(self):
    """
    :rtype: JsDc.Series
    """
    if self._dom is None:
      self._dom = JsDc.Series(self._report, varName=self.chartId, parent=self)
    return self._dom
