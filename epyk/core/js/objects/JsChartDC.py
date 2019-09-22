"""
Interface to the Javascript DC Chart library

https://dc-js.github.io/dc.js/docs/html/

Example
https://bl.ocks.org/jun9/raw/5631952/

"""


from epyk.core.js.configs import JsConfig


class JsBase(JsConfig.JsConfig):
  """
  Base Class for the DC Charts
  """
  listAttributes = []
  jsCls = None

  def version(self, no=None):
    """
    Return or change the underlying Javascript package version

    :param no: Optional. The new package version to force

    :return: The package version used
    """
    if no is not None:
      self

    return

  def addFilterHandler(self, addFilterHandler):
    """
    Set or get the add filter handler. The add filter handler is a function that adds a filter to the chart's filter list.
    Using a custom add filter handler allows you to change the way filters are added or perform additional work when adding a filter, e.g.
    when using a filter server other than crossfilter.

    :param addFilterHandler:

    :return:
    """
    self._js.append("addFilterHandler(%s)" % addFilterHandler)
    return self

  def chartGroup(self, groupId=None):
    """
    Get or set the chart group to which this chart belongs.
    Chart groups are rendered or redrawn together since it is expected they share the same underlying crossfilter data set.

    Documentation
    https://dc-js.github.io/dc.js/docs/html/dc.baseMixin.html

    :param groupId: Optional. The group ID

    :return:
    """
    return

  def data(self, callback):
    """
    Set the data callback or retrieve the chart's data set.
    The data callback is passed the chart's group and by default will return group.all. This behavior may be modified to, for instance, return only the top 5 groups.

    :param callback: Optinal

    :return:
    """

  def chartID(self):
    """
    Returns the internal numeric ID of the chart.

    Documentation
    https://dc-js.github.io/dc.js/docs/html/dc.baseMixin.html

    :return:
    """

  def x(self, xScale):
    """

    :return:
    """
    self._js.append("x(%s)" % xScale)
    return self

  def y(self, yScale):
    """
    Get or set the y scale. The y scale is typically automatically determined by the chart implementation.

    :return:
    """
    self._js.append("y(%s)" % yScale)
    return self

  def yAxis(self, yAxis=None):
    """
    Set or get the y axis used by the coordinate grid chart instance. This function is most useful when y axis customization is required.
    Depending on useRightYAxis the y axis in dc.js is an instance of either d3.axisLeft or d3.axisRight; therefore it supports any valid d3 axis manipulation.

    :return:
    """
    self._js.append("yAxis(%s)" % yAxis)
    return self

  def xUnits(self, unit=None):
    """
    Set or get the xUnits function.
    The coordinate grid chart uses the xUnits function to calculate the number of data projections on the x axis such as the number of bars for a bar chart or the number of dots for a line chart.

    :return:
    """
    self._js.append("xUnits(%s)" % unit)
    return self

  def brushOn(self, brushOn=True):
    """
    urn on/off the brush-based range filter.
    When brushing is on then user can drag the mouse across a chart with a quantitative scale to perform range filtering based on the extent of the brush, or click on the bars of an ordinal bar chart or slices of a pie chart to filter and un-filter them.

    Documentation
    https://dc-js.github.io/dc.js/docs/html/dc.coordinateGridMixin.html

    :param brushOn:
    :return:
    """
    self._js.append("brushOn(%s)")
    return self

  def dimension(self, dimension):
    """
    Set or get the dimension attribute of a chart. In dc, a dimension can be any valid crossfilter dimension

    :param: A Cross filter dimension
    :return:
    """

  def expireCache(self):
    """
    Expire the internal chart cache. dc charts cache some data internally on a per chart basis to speed up rendering and avoid unnecessary calculation

    :return:
    """

  def filter(self, filter):
    """
    Filter the chart by the given parameter, or return the current filter if no input parameter is given.

    :param filter: Filter can be an Array, a single value or a DC filter object

    :return:
    """

  def filterAll(self):
    """
    Clear all filters associated with this chart. The same effect can be achieved by calling chart.filter(null).

    :return:
    """

  def filterHandler(self, filterHandler):
    """
    Set or get the filter handler.
    The filter handler is a function that performs the filter action on a specific dimension.
    Using a custom filter handler allows you to perform additional logic before or after filtering.

    :return:
    """

  def filterPrinter(self, filterPrinter):
    """
    Set or get the filter printer function.
    The filter printer function is used to generate human friendly text for filter value(s) associated with the chart instance.
    The text will get shown in the `.filter element; see turnOnControls.

    :param filterPrinter:
    :return:
    """

  def filters(self):
    """
    Returns all current filters.
    This method does not perform defensive cloning of the internal filter array before returning, therefore any modification of the returned array will effect the chart's internal filter storage.

    :return:
    """

  def group(self):
    """
    Set or get the group attribute of a chart.
    In dc a group is a crossfilter group.
    Usually the group should be created from the particular dimension associated with the same chart. If a value is given, then it will be used as the new group.

    :return:
    """

  def hasFilter(self, filter=None):
    """
    Check whether any active filter or a specific filter is associated with particular chart instance. This function is not

    :param filter:
    :return:
    """

  def height(self, height=None):
    """
    Set or get the height attribute of a chart.
    The height is applied to the SVGElement generated by the chart when rendered (or re-rendered).
    If a value is given, then it will be used to calculate the new height and the chart returned for method chaining.
    The value can either be a numeric, a function, or falsy.

    :param height:

    :return:
    """
    self._js.append("height(%s)" % height)
    return self

  def width(self, width=None):
    """

    :param width:
    :return:
    """
    self._js.append("width(%s)" % width)
    return self

  def label(self):
    """
    Set or get the label function. The chart class will use this function to render labels for each child element in the chart, e.g. slices in a pie chart or bubbles in a bubble chart.
    Not every chart supports the label function, for example line chart does not use this function at all. By default, enables labels; pass false for the second parameter if this is not desired.

    :return:
    """

  def render(self):
    """
    Invoking this method will force the chart to re-render everything from scratch.
    Generally it should only be used to render the chart for the first time on the page or if you want to make sure everything is redrawn from scratch instead of relying on the default incremental redrawing behaviour.

    :return:
    """
    self._js.append("render()")
    return self

  def toStr(self):
    """
    Returns the Javascript String representation

    :return:
    """
    ctx = []
    self.resolveDict(dict([(key, val) for key, val in self.items() if val]), ctx)
    return "{%s}" % ", ".join(ctx)



# ---------------------------------------------------------------------------------------------------------
#                                          DC Configurations
# ---------------------------------------------------------------------------------------------------------
class JsLine(JsBase):
  """
  Configuration for a Lines Chart in DC
  """
  alias = 'line'
  name = 'Bars'
  jsCls = 'lineChart'
  _attrs = {}


class JsBar(JsBase):
  """
  Configuration for a Bars Chart in DC
  """
  alias = 'bar'
  name = 'Bars'
  jsCls = 'barChart'
  _attrs = {}


  def xAxisLabel(self, labelText=None, padding=None):
    """
    Set or get the x axis label. If setting the label, you may optionally include additional padding to the margin to make room for the label.
    By default the padded is set to 12 to accomodate the text height.

    :param labelText:
    :param padding:

    :return:
    """
    self._js.append("xAxisLabel(%s)" % labelText)
    return self

  def yAxisLabel(self, labelText=None, padding=None):
    """
    Set or get the x axis label. If setting the label, you may optionally include additional padding to the margin to make room for the label.
    By default the padded is set to 12 to accomodate the text height.

    :param labelText:
    :param padding:

    :return:
    """
    self._js.append("xAxisLabel(%s)" % labelText)
    return self


class JsPie(JsBase):
  """
  Configuration for a Pies Chart in DC
  """
  alias = 'pie'
  name = 'Pie Chart'
  jsCls = 'pieChart'
  _attrs = {}

  def x(self):
    raise Exception("Does not exist for this chart")


  def emptyTitle(self, title):
    """
    Title to use for the only slice when there is no data.

    Documentation
    https://dc-js.github.io/dc.js/docs/html/dc.pieChart.html

    :param title:

    :return:
    """
    return


class JsBuble(JsBase):
  """
  Configuration for a Pies Chart in DC
  """
  alias = 'bubble'
  name = 'Bubble Chart'
  jsCls = 'bubbleChart'
  _attrs = {}

  def x(self):
    raise Exception("Does not exist for this chart")


class JsRow(JsBase):
  """
  Configuration for a Pies Chart in DC
  """
  alias = 'row'
  name = 'Horizontal Bar Chart'
  jsCls = 'rowChart'
  _attrs = {}


