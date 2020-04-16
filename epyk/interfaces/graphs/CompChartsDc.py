
from epyk.core.html.graph import GraphDC


class DC(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "DC"

  def set_crossfilter(self, record, y_columns, x_axis, varName, extra_cols=None):
    """
    Description:
    -----------
    Set a crossfilter object and add the dimensions which will be added to a chart.

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    """
    #
    if not isinstance(y_columns, list):
      y_columns = [y_columns]

    if not isinstance(x_axis, tuple):
      x_axis = (x_axis, str)
    crossfilter = self.parent.context.rptObj.js.data.crossfilter(record, "%s_xf" % varName)
    if len(y_columns) == 1:
      dimension = crossfilter.dimension([x_axis] + (extra_cols or []), '%s_xf_dim' % varName)
      group = dimension.group('%s_xf_group' % varName).reduceSum(y_columns[0])
    else:
      dimension = crossfilter.dimension([x_axis] + (extra_cols or []) + [(y, int) for y in y_columns], '%s_xf_dim' % varName)
      group = dimension.group('%s_xf_group' % varName)

    #
    self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})["%s_xf" % varName] = crossfilter.toStr()
    self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})["%s_xf_dim" % varName] = dimension.toStr()
    self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})["%s_xf_group" % varName] = group.toStr()

    return {"crossfilter": crossfilter, 'dimension': dimension, 'group': group}

  def line(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    -----------

    Related Pages:

			https://square.github.io/crossfilter/
    https://dc-js.github.io/dc.js/

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    if isinstance(y_columns, list):
      line_chart = self.series(record, y_columns, x_axis, 'line', title, profile, options, width, height, htmlCode)
    else:
      line_chart = GraphDC.ChartLine(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
      line_chart.dom.height(height[0]).x().yAxisLabel(y_columns).renderArea(True)
      if record is not None:
        self.set_crossfilter(record, y_columns, x_axis)
        cross_filter = self.set_crossfilter(record, y_columns, x_axis, line_chart.htmlId)
        line_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    self.parent.context.register(line_chart)
    return line_chart

  def series(self, record=None, y_columns=None, x_axis=None, series_type='line', title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    -----------

    Related Pages:

			https://square.github.io/crossfilter/
    https://dc-js.github.io/dc.js/

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    pivot_rec = []
    for rec in record:
      pivot_rec.extend([{'x': rec[x_axis], "name": "Series %s" % y, "y": rec[y]} for y in y_columns])

    line_chart = GraphDC.ChartSeries(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
    cross_filter = self.set_crossfilter(pivot_rec, ["y"], "x", line_chart.htmlId, extra_cols=[('name', str)])
    #self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return [d.name, +d.x]})" % {'cId': line_id, 'data': pivot_rec}
    if series_type == 'line':
      line_chart.dom.line().height(height[0]).x().seriesAccessorByKey(1).keyAccessor(0).valueAccessor().elasticY(True) # .dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d.y ;})" % {'cId': line_id})
      line_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    elif series_type == 'step':
      line_chart.dom.line().height(height[0]).x().seriesAccessorByKey(1).keyAccessor(0).valueAccessor().elasticY(True) # .dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d.y ;})" % {'cId': line_id})
      line_chart.dom._sub_chart.renderArea(True).curveStepBefore()
      line_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    elif series_type == 'bubble':
      line_chart.dom.bubble().height(height[0]).x().seriesAccessorByKey(1).keyAccessor(0).valueAccessor().radiusValueAccessorByKey()
      line_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    elif series_type in ['scatter', 'point']:
      line_chart.dom.scatter().height(height[0]).x().seriesAccessorByKey(1).keyAccessor(0).valueAccessor()
      line_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    elif series_type == 'bar':
      line_chart.dom.bar().height(height[0]).x().seriesAccessorByKey(1).keyAccessor(0).valueAccessor()# .dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d.y ;})" % {'cId': line_id})
      line_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    self.parent.context.register(line_chart)
    return line_chart

  def scatter(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    -----------

    Related Pages:

			https://square.github.io/crossfilter/
    https://dc-js.github.io/dc.js/

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    if isinstance(y_columns, list):
      line_chart = self.series(record, y_columns, x_axis, 'scatter', title, profile, options, width, height, htmlCode)
    else:
      line_chart = GraphDC.ChartScatter(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
      line_chart.dom.height(height[0]).x().yAxisLabel(y_columns)
      if record is not None:
        cross_filter = self.set_crossfilter(record, y_columns, x_axis, line_chart.htmlId)
        line_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    self.parent.context.register(line_chart)
    return line_chart

  def step(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    -----------

    Related Pages:
Attributes:
    ----------
    :param record:
    :param y_column:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """

    if isinstance(y_columns, list):
      line_chart = self.series(record, y_columns, x_axis, 'step', title, profile, options, width, height, htmlCode)
    else:
      line_chart = GraphDC.ChartLine(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
      line_chart.dom.height(height[0]).x().yAxisLabel(y_columns).renderArea(True).curveStepBefore()
      if record is not None:
        cross_filter = self.set_crossfilter(record, y_columns, x_axis, line_chart.htmlId)
        line_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
      self.parent.context.register(line_chart)
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    -----------

    Related Pages:
Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    if isinstance(y_columns, list):
      bar_chart = self.series(record, y_columns, x_axis, 'bar', title, profile, options, width, height, htmlCode)
    else:
      bar_chart = GraphDC.ChartBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
      bar_chart.dom.height(height[0]).x().controlsUseVisibility(True).yAxisLabel(y_columns)
      if record is not None:
        cross_filter = self.set_crossfilter(record, y_columns, x_axis, bar_chart.htmlId)
        bar_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    self.parent.context.register(bar_chart)
    return bar_chart

  def hbar(self, record=None, y_column=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    -----------

    Related Pages:
Attributes:
    ----------
    :param record:
    :param y_column:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    bar_chart = GraphDC.ChartRow(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
    line_id = bar_chart.htmlId
    bar_chart.dom.height(height[0]).x().chartGroup(line_id).elasticX(True)
    if record is not None:
      cross_filter = self.set_crossfilter(record, y_column, x_axis, bar_chart.htmlId)
      bar_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    self.parent.context.register(bar_chart)
    return bar_chart

  def pie(self, record=None, y_column=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    -----------

    Related Pages:

			https://square.github.io/crossfilter/
    https://dc-js.github.io/dc.js/

    Attributes:
    ----------
    :param record:
    :param y_column:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    pie_chart = GraphDC.ChartPie(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
    pie_chart.dom.height(height[0])
    if record is not None:
      cross_filter = self.set_crossfilter(record, y_column, x_axis, pie_chart.htmlId)
      pie_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    self.parent.context.register(pie_chart)
    return pie_chart

  def sunburst(self, record=None, y_column=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """

    Related Pages:

			https://square.github.io/crossfilter/
    https://dc-js.github.io/dc.js/

    :param data:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param title:
    :param profile:
    :param xAxisOrder:
    :param width:
    :param height:
    :param htmlCode:
    """
    pie_chart = GraphDC.ChartSunburst(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
    line_id = pie_chart.htmlId
    self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return +d['%(x)s'];})" % {'cId': line_id, 'data': record, 'x': x_axis}
    pie_chart.dom.dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d['%(y)s'] ;})" % {'cId': line_id, 'y': y_column})
    self.parent.context.register(pie_chart)
    return pie_chart

  def bubble(self, record=None, y_columns=None, x_axis=None, r_axis=None, title=None, profile=None, options=None, width=(100, "%"),
             height=(330, "px"), htmlCode=None):
    """
    Description:
    -----------

    Related Pages:

			https://square.github.io/crossfilter/
    https://dc-js.github.io/dc.js/
    https://www.tutorialspoint.com/dcjs/dcjs_bubble_chart.htm

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    if isinstance(y_columns, list):
      bubble_chart = self.series(record, y_columns, x_axis, 'bubble', title, profile, options, width, height, htmlCode)
    else:
      bubble_chart = GraphDC.ChartBubble(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
      bubble_chart.dom.height(height[0]).x().yAxisLabel(y_columns).keyAccessor(0).radiusValueAccessorByKey(1, statc_factor=options.get('statc_factor'))
      if record is not None:
        cross_filter = self.set_crossfilter(record, y_columns, x_axis, bubble_chart.htmlId, extra_cols=[(r_axis, int)])
        bubble_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    self.parent.context.register(bubble_chart)
    return bubble_chart
