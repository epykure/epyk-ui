
from epyk.core.html.graph import GraphDC
from epyk.core.js.objects import JsChartDC


class DC(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "DC"

  def line(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://square.github.io/crossfilter/
    https://dc-js.github.io/dc.js/

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
      line_id = line_chart.htmlId
      self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return +d['%(x)s'];})" % {'cId': line_id, 'data': record, 'x': x_axis}
      line_chart.dom.height(height[0]).x().yAxisLabel("This is the Y Axis!").renderArea(True).dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d['%(y)s'] ;})" % {'cId': line_id, 'y': y_columns})
      self.parent.context.register(line_chart)
    return line_chart

  def series(self, record=None, y_columns=None, x_axis=None, series_type='line', title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://square.github.io/crossfilter/
    https://dc-js.github.io/dc.js/

    :param record:
    :param y_column:
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
    line_id = line_chart.htmlId
    self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return [d.name, +d.x]})" % {'cId': line_id, 'data': pivot_rec}
    if series_type == 'line':
      line_chart.dom.line().height(height[0]).x().seriesAccessorByKey(0).keyAccessor(1).valueAccessor().elasticY(True).dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d.y ;})" % {'cId': line_id})
    elif series_type in ['scatter', 'point']:
      line_chart.dom.scatter().height(height[0]).x().seriesAccessorByKey(0).keyAccessor(1).valueAccessor().dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d.y ;})" % {'cId': line_id})
    elif series_type == 'bar':
      line_chart.dom.bar().height(height[0]).x().seriesAccessorByKey(0).keyAccessor(1).valueAccessor().dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d.y ;})" % {'cId': line_id})
    self.parent.context.register(line_chart)
    return line_chart

  def scatter(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://square.github.io/crossfilter/
    https://dc-js.github.io/dc.js/

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
      line_chart = self.series(record, y_columns, x_axis, 'scatter', title, profile, options, width, height, htmlCode)
    else:
      line_chart = GraphDC.ChartScatter(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
      line_id = line_chart.htmlId
      self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return [+d['%(x)s'], +d['%(y)s']];})" % {'cId': line_id, 'data': record, 'x': x_axis, 'y': y_columns}
      line_chart.dom.height(height[0]).x().yAxisLabel("This is the Y Axis!").dimension("%s_dim" % line_id).group("%(cId)s_dim.group()" % {'cId': line_id})
      self.parent.context.register(line_chart)
    return line_chart

  def step(self, record=None, y_column=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """

    :param record:
    :param y_column:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    line_chart = GraphDC.ChartLine(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
    line_id = line_chart.htmlId
    self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return +d['%(x)s'];})" % {'cId': line_id, 'data': record, 'x': x_axis}
    line_chart.dom.height(height[0]).x().yAxisLabel("This is the Y Axis!").renderArea(True).curveStepBefore().dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d['%(y)s'] ;})" % {'cId': line_id, 'y': y_column})
    self.parent.context.register(line_chart)
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """

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
      bar_chart = self.series(record, y_columns, x_axis, 'bar', title, profile, options, width, height, htmlCode)
    else:
      bar_chart = GraphDC.ChartBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
      line_id = bar_chart.htmlId
      self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return +d['%(x)s'];})" % {'cId': line_id, 'data': record, 'x': x_axis}
      bar_chart.dom.height(height[0]).x().controlsUseVisibility(True).yAxisLabel("This is the Y Axis!").dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d['%(y)s'] ;})" % {'cId': line_id, 'y': y_columns})
      self.parent.context.register(bar_chart)
    return bar_chart

  def hbar(self, record=None, y_column=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """

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
    self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return +d['%(x)s'];})" % {'cId': line_id, 'data': record, 'x': x_axis}
    bar_chart.dom.height(height[0]).x().chartGroup(line_id).elasticX(True).dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d['%(y)s'] ;})" % {'cId': line_id, 'y': y_column})
    self.parent.context.register(bar_chart)
    return bar_chart

  def pie(self, record=None, y_column=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """

    Documentation
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
    pie_chart = GraphDC.ChartPie(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
    line_id = pie_chart.htmlId
    self.parent.context.rptObj._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return +d['%(x)s'];})" % {'cId': line_id, 'data': record, 'x': x_axis}
    pie_chart.dom.dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d['%(y)s'] ;})" % {'cId': line_id, 'y': y_column})
    self.parent.context.register(pie_chart)
    return pie_chart

  def sunburst(self, record=None, y_column=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """

    Documentation
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

  def bubble(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None, filters=None, profile=None,
        xAxisOrder=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
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

    :return:

    :rtype: GraphDC.Chart
    """
    chart_obj = JsChartDC.JsBuble(self.parent.context.rptObj, data, {'static': {}, 'dynamic': {}})
    return self.parent.context.register(GraphDC.Chart(self.parent.context.rptObj, chart_obj, width, height, title,
                                                      options or {}, htmlCode, filters, profile))
