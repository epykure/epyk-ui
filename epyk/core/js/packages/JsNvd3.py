
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage


class JsNvd3Axis(object):

  def __init__(self, id):
    self._selector = id
    self._js = []

  def axisLabel(self, text):
    """
    Chart axis settings

    Example
    chart.xAxis.axisLabel('Time (ms)')

    :param text:
    """
    text = JsUtils.jsConvertData(text, None)
    self._js.append("axisLabel(%s)" % text)
    return self

  def tickFormat(self, jsFnc):
    """
    Chart axis settings

    Example
    chart.xAxis.tickFormat(d3.format(',r'))

    :param jsFnc:
    """
    jsFnc = JsUtils.jsConvertData(jsFnc, None)
    self._js.append("tickFormat(%s)" % jsFnc)
    return self

  def tickValues(self, values):
    """
    Chart axis settings

    Example
    chart.xAxis.tickValues(10)

    :param values:
    """
    values = JsUtils.jsConvertData(values, None)
    self._js.append("tickValues(%s)" % values)
    return self

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._selector

    strData = "%(jqId)s.%(items)s" % {'jqId': self._selector, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return strData


class JsNvd3Utils(object):
  """

  """

  def windowResize(self, jsFnc):
    """
    Update the chart when window resizes.

    :param jsFnc:

    :return:
    """
    return "nv.utils.windowResize(%s)" % jsFnc


class JsNvd3(JsPackage):
  lib_alias = {'js': 'nvd3', 'css': 'nvd3'}

  class __internal(object):
    # By default it will attach eveything to the body
    jqId, jsImports, cssImport = 'd3.select("body")', set([]), set([])

  def __init__(self, src=None, varName=None, setVar=True):
    self.src = src if src is not None else self.__internal()
    self._selector = "nv.models.%s()" % self.chartFnc
    self.varName, self.setVar = varName, setVar
    self.src.jsImports.add(self.lib_alias['js'])
    self.src.cssImport.add(self.lib_alias['css'])
    self._js, self._xaxis, self._yaxis, self._u = [[]], None, None, {}

  def version(self, ver):
    """
    Change the package version number

    Example
    bar.chart.version("1.11.0")

    :param ver: String. The package versions example 1.11.0
    """
    self.src._props.setdefault("packages", {})[self.lib_alias] = ver
    return self

  def set_var(self, flag):
    self.setVar = flag
    return self

  @property
  def varId(self):
    """
    The Javascript and Python reference ID

    :return: The Javascript String of the object variable name
    """
    return self._selector if self.varName is None else self.varName

  def options(self, opts):
    pass

  def width(self, value):
    """
    The width the graph or component created inside the SVG should be made.
    The width of the container element (normally the svg itself)

    Documentation
    https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param value: A python integer

    :return:
    """
    self._js.append("width(%s)" % value)
    return self

  def height(self, value):
    """
    The height the graph or component created inside the SVG should be made.
    The height of the container element (normally the svg itself)

    Documentation
    https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param value:

    :return:
    """
    self._js.append("height(%s)" % value)
    return self

  def margin(self, options):
    """
    Object containing the margins for the chart or component.
    You can specify only certain margins in the object to change just those parts.
    Default options: { "top": 15, "right": 10, "bottom": 50, "left": 60 }

    Documentation
    https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param options: A python dictionary with the options
    """
    options = JsUtils.jsConvertData(options, None)
    self._js.append("margin(%s)" % options)
    return self

  def useInteractiveGuideline(self, flag):
    """
    Tooltips which show all data points.

    :param flag:
    :return:
    """
    flag = JsUtils.jsConvertData(flag, None)
    return self.fnc("useInteractiveGuideline(%s)" % flag)

  def transitionDuration(self, time):
    """

    :param time:
    """
    time = JsUtils.jsConvertData(time, None)
    return self.fnc("transitionDuration(%s)" % time)

  def showLegend(self, flag):
    """

    :param flag:
    """
    flag = JsUtils.jsConvertData(flag, None)
    return self.fnc("showLegend(%s)" % flag)

  @property
  def xAxis(self):
    """

    :return:
    """
    if self._xaxis is None:
      self._xaxis = JsNvd3Axis("%s.xAxis" % self.varName)
    return self._xaxis

  @property
  def yAxis(self):
    """

    :return:
    """
    if self._yaxis is None:
      self._yaxis = JsNvd3Axis("%s.yAxis" % self.varName)
    return self._yaxis

  def showYAxis(self, flag):
    pass

  def showXAxis(self, flag):
    pass

  def update(self):
    pass

  def showControls(self, flag):
    """
    Allow user to choose 'Stacked', 'Stream', 'Expanded' mode.

    :param flag:
    :return:
    """
    flag = JsUtils.jsConvertData(flag, None)
    return self.fnc("showControls(%s)" % flag)

  def color(self, d3ColorScale):
    pass

  def noData(self):
    pass


class JsNvd3Area(JsNvd3):
  chartFnc = "stackedAreaChart"

  def x(self, column=None, jsFnc=None):
    if column is not None:
      return self.fnc("x(function(d){return d.%s})" % column)

    elif jsFnc is not None:
      jsFnc = JsUtils.jsConvertFncs(jsFnc)
      return self.fnc("x(%s)" % jsFnc)

    return self

  def y(self, column=None, jsFnc=None):
    if column is not None:
      return self.fnc("y(function(d){return d.%s})" % column)

    elif jsFnc is not None:
      jsFnc = JsUtils.jsConvertFncs(jsFnc)
      return self.fnc("y(%s)" % jsFnc)

    return self

  def rotateLabels(self, value):
    pass

  def reduceXTicks(self, flag):
    pass

  def rightAlignYAxis(self, flag):
    """
    Move the y-axis to the right side

    :param flag:
    :return:
    """
    flag = JsUtils.jsConvertData(flag, None)
    return self.fnc("rightAlignYAxis(%s)" % flag)

  def clipEdge(self, flag):
    """

    :param flag:
    :return:
    """
    flag = JsUtils.jsConvertData(flag, None)
    return self.fnc("clipEdge(%s)" % flag)

  def controlLabels(self, attrs):
    """

    controlLabels({"stacked": "Stacked"})

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/stackedAreaChart.html

    :param attrs:
    """
    self.fnc("controlLabels(%s)" % JsUtils.jsConvertData(attrs, None))
    return self


class JsNvd3ParallelCoordinates(JsNvd3):
  chartFnc = "parallelCoordinates"

  def dimensionNames(self, categories):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/parallelCoordinates.html

    :param categories:
    """
    self.fnc("dimensionNames(%s)" % JsUtils.jsConvertData(categories, None))
    return self

  def dimensionFormats(self, formats):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/parallelCoordinates.html

    :param formats:
    """
    self.fnc("dimensionFormats(%s)" % JsUtils.jsConvertData(formats, None))
    return self

  def lineTension(self, val):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/parallelCoordinates.html

    :param val:
    """
    self.fnc("lineTension(%s)" % JsUtils.jsConvertData(val, None))
    return self


class JsNvd3CandlestickBar(JsNvd3):
  chartFnc = "candlestickBarChart"


class JsNvd3OhlcBar(JsNvd3):
  chartFnc = "ohlcBarChart"


class JsNvd3Sunburst(JsNvd3):
  chartFnc = "sunburstChart"


class JsNvd3BoxPlot(JsNvd3):
  chartFnc = "boxPlotChart"

  def staggerLabels(self, flag):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlot.html

    :param flag:
    """
    self.fnc("staggerLabels(%s)" % JsUtils.jsConvertData(flag, None))
    return self

  def maxBoxWidth(self, value):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlot.html

    :param value:
    """
    self.fnc("maxBoxWidth(%s)" % JsUtils.jsConvertData(value, None))
    return self

  def yDomain(self, range):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlot.html

    :param range:
    """
    self.fnc("yDomain(%s)" % JsUtils.jsConvertData(range, None))
    return self

  def maxBoxWidth(self, value):
    """
    Prevent boxes from being incredibly wide

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param value:
    """
    self.fnc("maxBoxWidth(%s)" % JsUtils.jsConvertData(value, None))
    return self

  def itemColor(self, seriesColor):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param seriesColor:
    """
    self.fnc("itemColor(function (d) { return d[%s] })" % JsUtils.jsConvertData(seriesColor, None))
    return self

  def outliers(self, outlData):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param outlData:
    """
    self.fnc("outliers(function (d) { return d[%s] })" % JsUtils.jsConvertData(outlData, None))
    return self

  def outlierValue(self, data):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param data:
    """
    self.fnc("outlierValue(function (d) { return d[%s] })" % JsUtils.jsConvertData(data, None))
    return self

  def outlierColor(self, color):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param color:
    """
    self.fnc("outlierColor(function (d) { return d[%s] })" % JsUtils.jsConvertData(color, None))
    return self

  def q1(self, q1_col):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param q1_col:
    """
    self.fnc("q1(function (d) { return d[%s] })" % JsUtils.jsConvertData(q1_col, None))
    return self

  def q2(self, q2_col):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param q2_col:
    """
    self.fnc("q2(function (d) { return d[%s] })" % JsUtils.jsConvertData(q2_col, None))
    return self

  def q3(self, q3_col):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param q3_col:
    """
    self.fnc("q3(function (d) { return d[%s] })" % JsUtils.jsConvertData(q3_col, None))
    return self

  def wl(self, wl_col):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param wl_col:
    """
    self.fnc("wl(function (d) { return d[%s] })" % JsUtils.jsConvertData(wl_col, None))
    return self

  def wh(self, wh_col):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    :param wh_col:
    """
    self.fnc("wh(function (d) { return d[%s] })" % JsUtils.jsConvertData(wh_col, None))
    return self

  def outlierLabel(self):
    pass


class JsNvd3Bar(JsNvd3):
  chartFnc = "discreteBarChart"

  def x(self, column=None, jsFnc=None):
    if column is not None:
      self.fnc("x(function(d){return d.%s})" % column)
    elif jsFnc is not None:
      self.fnc("x(%s)" % JsUtils.jsConvertFncs(jsFnc))
    return self

  def y(self, column=None, jsFnc=None):
    if column is not None:
      self.fnc("y(function(d){return d.%s})" % column)
    elif jsFnc is not None:
      self.fnc("y(%s)" % JsUtils.jsConvertFncs(jsFnc))
    return self

  def color(self, colors):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/TimeSeries.html

    :param colors:
    """
    self.fnc("rotateLabels(%s)" % JsUtils.jsConvertData(colors, None))
    return self

  def rotateLabels(self, value):
    """
    Rotates the X axis labels by the specified degree.

    Documentation
    https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param value:
    """
    self.fnc("rotateLabels(%s)" % value)
    return self

  def reduceXTicks(self, flag):
    pass

  def staggerLabels(self, flag):
    pass

  def tooltips(self, flag):
    pass

  def showValues(self, flag):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/discreteBarChart.html

    :param flag:
    """
    self.fnc("showValues(%s)" % JsUtils.jsConvertData(range, None))
    return self

  def groupSpacing(self, value):
    pass


class JsNvd3MultiBar(JsNvd3):
  chartFnc = "multiBarChart"

  def barColor(self, colors):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/multiBarChart.html

    :param colors:
    """
    self.fnc("barColor(%s)" % JsUtils.jsConvertData(colors, None))
    return self

  def stacked(self, flag):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/multiBarChart2.html

    :param flag:
    """
    self.fnc("stacked(%s)" % JsUtils.jsConvertData(range, None))
    return self


class JsNvd3MultiBarHorizontal(JsNvd3):
  chartFnc = "multiBarHorizontalChart"

  def yErr(self):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/multiBarHorizontalChart.html

    """
    pass

  def barColor(self, colors):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/multiBarHorizontalChart.html

    :param colors:
    """
    self.fnc("barColor(%s)" % JsUtils.jsConvertData(colors, None))
    return self


class JsNvd3Multi(JsNvd3Bar):
  chartFnc = "multiChart"


class JsNvd3Line(JsNvd3Bar):
  chartFnc = "lineChart"


class JsNvd3Scatter(JsNvd3Bar):
  chartFnc = "scatterChart"

  def showDistX(self, flag):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/scatterChart.html

    :param flag:
    """
    self.fnc("showDistX(%s)" % JsUtils.jsConvertData(flag, None))
    return self

  def showDistY(self, flag):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/scatterChart.html

    :param flag:
    """
    self.fnc("showDistY(%s)" % JsUtils.jsConvertData(flag, None))
    return self

  def useVoronoi(self, flag):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/scatterChart.html

    :param flag:
    """
    self.fnc("useVoronoi(%s)" % JsUtils.jsConvertData(flag, None))
    return self


class JsNvd3LineWithFocus(JsNvd3Line):
  chartFnc = "lineWithFocusChart"

  def brushExtent(self, range):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/lineWithFocusChart.html

    :param range:
    """
    self.fnc("brushExtent(%s)" % JsUtils.jsConvertData(range, None))
    return self


class JsNvd3CumulativeLine(JsNvd3Line):
  chartFnc = "cumulativeLineChart"

  def average(self, mean):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/cumulativeLineChart.html

    :param mean: String. The column name corresponding to the mean value
    """
    self.fnc("average(function(d) { return d.[%s] / 100; })" % JsUtils.jsConvertData(mean, None))
    return self

  def clipVoronoi(self, flag):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/cumulativeLineChart.html

    :param flag:
    """
    self.fnc("clipVoronoi(%s)" % JsUtils.jsConvertData(flag, None))
    return self


class JsNvd3LinePlusBar(JsNvd3Bar):
  chartFnc = "linePlusBarChart"

  def legendRightAxisHint(self, text):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/linePlusBarChart.html

    :param text:
    """
    self.fnc("legendRightAxisHint(%s)" % JsUtils.jsConvertData(text, None))
    return self

  def forceY(self, indices):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/linePlusBarChart.html

    :param indices:
    """
    self.fnc("forceY(%s)" % JsUtils.jsConvertData(indices, None))
    return self

  def padData(self, flag):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/linePlusBarChart.html

    :param flag:
    """
    self.fnc("padData(%s)" % JsUtils.jsConvertData(flag, None))
    return self


class JsNvd3HistoricalBar(JsNvd3Bar):
  chartFnc = "historicalBarChart"

  def xScale(self, d3fnc):
    """
    use a time scale instead of plain numbers in order to get nice round default values in the axis

    xScale(d3.time.scale())

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/TimeSeries.html

    :param d3fnc:
    """
    self.fnc("xScale(%s)" % JsUtils.jsConvertData(d3fnc, None))
    return self

  def forceX(self, values):
    """
    fix half-bar problem on the first and last bars

    :param values:
    :return:
    """
    self.fnc("forceX(%s)" % JsUtils.jsConvertData(values, None))
    return self


class JsNvd3Pie(JsNvd3):
  chartFnc = "pieChart"

  def arcsRadius(self, value):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/monitoringChart.html

    :param value:
    """
    self.fnc("arcsRadius(%s)" % JsUtils.jsConvertData(value, None))
    return self

  def x(self, column=None, jsFnc=None):
    if column is not None:
      self.fnc("x(function(d){return d.%s})" % column)
    elif jsFnc is not None:
      self.fnc("x(%s)" % JsUtils.jsConvertFncs(jsFnc))
    return self

  def y(self, column=None, jsFnc=None):
    if column is not None:
      self.fnc("y(function(d){return d.%s})" % column)
    elif jsFnc is not None:
      self.fnc("y(%s)" % JsUtils.jsConvertFncs(jsFnc))
    return self

  def showLabels(self, flag):
    """
    Description:
    ------------
    Display pie labels

    Related Pages:
    --------------
    http://nvd3.org/examples/pie.html

    Attributes:
    ----------
    :param flag:
    """
    self.fnc("showLabels(%s)" % JsUtils.jsConvertData(flag, None))
    return self

  def labelThreshold(self, value):
    """
    Description:
    ------------
    Configure the minimum slice size for labels to show up

    Related Pages:
    --------------
    http://nvd3.org/examples/pie.html

    Attributes:
    ----------
    :param value:
    """
    self.fnc("labelThreshold(%s)" % JsUtils.jsConvertData(value, None))
    return self

  def labelSunbeamLayout(self, flag):
    """
    Change the label orientation for each category

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/monitoringChart.html

    :param flag:
    """
    self.fnc("labelSunbeamLayout(%s)" % JsUtils.jsConvertData(flag, None))
    return self

  def labelType(self, text):
    pass

  def donutLabelsOutside(self, flag):
    """

    :param flag:
    """
    self.fnc("donutLabelsOutside(%s)" % JsUtils.jsConvertData(flag, None))
    return self

  def donut(self, flag):
    """
    Description:
    ------------
    Turn on Donut mode. Makes pie chart look tasty!

    Related Pages:
    --------------
    http://nvd3.org/examples/pie.html

    Attributes:
    ----------
    :param flag:
    """
    value = "donut(%s)" % JsUtils.jsConvertData(flag, None)
    if not value in self._js[-1]:
      self.fnc(value)
    return self

  def startAngle(self, angle):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/donutChart.html
    """
    self.fnc("startAngle(function(d) { return d.startAngle/2 -Math.PI/2; } )")
    return self

  def endAngle(self, angle):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/donutChart.html

    """
    self.fnc("endAngle(function(d) { return d.startAngle/2 -Math.PI/2 })")
    return self

  def half(self):
    pass

  def donutRatio(self, value):
    """
    Description:
    ------------
    Configure how big you want the donut hole size to be.

    Related Pages:
    --------------
    http://nvd3.org/examples/pie.html

    Attributes:
    ----------
    :param flag:
    """
    self.donut(True)
    self.fnc("donutRatio(%s)" % JsUtils.jsConvertData(value, None))
    return self

  def padAngle(self, val):
    """
    Description:
    ------------
    Add a padding (space) between the different categories of the chart

    Related Pages:
    --------------
    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/donutChart.html

    Attributes:
    ----------
    :param val: Float. The padding value
    """
    self.fnc("padAngle(%s)" % JsUtils.jsConvertData(val, None))
    return self

  def cornerRadius(self, val):
    """
    Description:
    ------------
    Change the angle corner radius

    Related Pages:
    --------------
    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/donutChart.html

    Attributes:
    ----------
    :param val: Float. The rounding to be set to the angles
    """
    self.fnc("cornerRadius(%s)" % JsUtils.jsConvertData(val, None))
    return self

  def id(self, classname):
    """
    Description:
    ------------
    allow custom CSS for this one svg

    Attributes:
    ----------
    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/donutChart.html

    Attributes:
    ----------
    :param classname:
    """
    self.fnc("id(%s)" % JsUtils.jsConvertData(classname, None))
    return self

  def growOnHover(self, flag):
    """

    :param flag:
    """
    self.fnc("growOnHover(%s)" % JsUtils.jsConvertData(flag, None))
    return self

  def reduceXTicks(self, flag):
    pass

  def staggerLabels(self, flag):
    pass

  def tooltips(self, flag):
    pass

  def showValues(self, flag):
    pass

  def groupSpacing(self, value):
    pass

  def title(self, text):
    """
    Text to include within the middle of a donut chart

    Documentation
    https://nvd3-community.github.io/nvd3/examples/documentation.html

    :param text:

    :return:
    """
    title = JsUtils.jsConvertData(text, None)
    self._js.append("title(%s)" % title)
    return self

  def titleOffset(self, value):
    pass


class JsNvd3ForceDirectedGraph(JsNvd3Bar):
  chartFnc = "forceDirectedGraph"

  def nodeExtras(self, node):
    """

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/forceDirected.html

    :param node:
    """
    pass
