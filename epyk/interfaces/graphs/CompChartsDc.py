from typing import List, Any

from epyk.core.html.graph import GraphDC
from epyk.core.py import types
from epyk.core.js import JsUtils


class DC:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "DC"

  def plot(self, record=None, y=None, x=None, kind: str = "line", profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None):
    """

    :tags:
    :categories:

    :param record: Optional. The list of dictionaries with the input data
    :param y: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x: Optional. The column corresponding to a key in the dictionaries in the record
    :param kind: Optional. The chart type
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    if not isinstance(y, list) and not JsUtils.isJsData(y):
      y = [y]
    return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def set_crossfilter(self, record, y_columns, x_axis: List[str], var_name: str, extra_cols: List[Any] = None) -> dict:
    """Set a crossfilter object and add the dimensions which will be added to a chart.

    :tags:
    :categories:

    :param record: The Python list of dictionaries
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param var_name:
    :param extra_cols: Optional.
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]

    if not isinstance(x_axis, tuple):
      x_axis = (x_axis, str)
    crossfilter = self.page.js.data.crossfilter(record, "%s_xf" % var_name)
    if len(y_columns) == 1:
      dimension = crossfilter.dimension([x_axis] + (extra_cols or []), '%s_xf_dim' % var_name)
      group = dimension.group('%s_xf_group' % var_name).reduceSum(y_columns[0])
    else:
      dimension = crossfilter.dimension(
        [x_axis] + (extra_cols or []) + [(y, int) for y in y_columns], '%s_xf_dim' % var_name)
      group = dimension.group('%s_xf_group' % var_name)
    self.page._props.setdefault('js', {}).setdefault('datasets', {})["%s_xf" % var_name] = crossfilter.toStr()
    self.page._props.setdefault('js', {}).setdefault('datasets', {})["%s_xf_dim" % var_name] = dimension.toStr()
    self.page._props.setdefault('js', {}).setdefault('datasets', {})["%s_xf_group" % var_name] = group.toStr()
    return {"crossfilter": crossfilter, 'dimension': dimension, 'group': group}

  def line(self, record=None, y_columns=None, x_axis: str = None, title: str = None,
           profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), html_code: str = None
           ) -> GraphDC.ChartLine:
    """

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 30)
      line = page.ui.charts.dc.line(data, y_columns=[1, 2], x_axis='x')

    `Crossfilter <https://square.github.io/crossfilter/>`_
    `DC <https://dc-js.github.io/dc.js/>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param title: Optional. The chart title
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    if isinstance(y_columns, list):
      line_chart = self.series(
        record or [], y_columns, x_axis, 'line', title, profile, options, width, height, html_code)
    else:
      line_chart = GraphDC.ChartLine(self.page, width, height, title, options or {}, html_code, profile)
      line_chart.dom.height(height[0]).x().yAxisLabel(y_columns).renderArea(True)
      if record is not None:
        self.set_crossfilter(record, y_columns, x_axis)
        cross_filter = self.set_crossfilter(record, y_columns, x_axis, line_chart.htmlCode)
        line_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    return line_chart

  def series(self, record=None, y_columns=None, x_axis=None, series_type: str = 'line', title: str = None,
             profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), html_code: str = None
             ) -> GraphDC.ChartSeries:
    """

    :tags:
    :categories:

    `Crossfilter <https://square.github.io/crossfilter/>`_
    `DC <https://dc-js.github.io/dc.js/>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param series_type: Optional.
    :param title: Optional. The chart title
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    pivot_rec = []
    for rec in record:
      pivot_rec.extend([{'x': rec[x_axis], "name": "Series %s" % y, "y": rec[y]} for y in y_columns])

    line_chart = GraphDC.ChartSeries(self.page, width, height, title, options or {}, html_code, profile)
    cross_filter = self.set_crossfilter(pivot_rec, ["y"], "x", line_chart.htmlCode, extra_cols=[('name', str)])
    #self.page._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return [d.name, +d.x]})" % {'cId': line_id, 'data': pivot_rec}
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
    return line_chart

  def scatter(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
              height=(330, "px"), html_code=None) -> GraphDC.ChartScatter:
    """

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 30)
      scatter = page.ui.charts.dc.scatter(data, y_columns=[2, 4], x_axis='x')

    `Crossfilter <https://square.github.io/crossfilter/>`_
    `DC <https://dc-js.github.io/dc.js/>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param title: Optional. The chart title
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    if isinstance(y_columns, list):
      line_chart = self.series(record, y_columns, x_axis, 'scatter', title, profile, options, width, height, html_code)
    else:
      line_chart = GraphDC.ChartScatter(self.page, width, height, title, options or {}, html_code, profile)
      line_chart.dom.height(height[0]).x().yAxisLabel(y_columns)
      if record is not None:
        cross_filter = self.set_crossfilter(record, y_columns, x_axis, line_chart.htmlCode)
        line_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    return line_chart

  def step(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), html_code=None) -> GraphDC.ChartLine:
    """

    :tags:
    :categories:

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param title: Optional. The chart title
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """

    if isinstance(y_columns, list):
      line_chart = self.series(record, y_columns, x_axis, 'step', title, profile, options, width, height, html_code)
    else:
      line_chart = GraphDC.ChartLine(self.page, width, height, title, options or {}, html_code, profile)
      line_chart.dom.height(height[0]).x().yAxisLabel(y_columns).renderArea(True).curveStepBefore()
      if record is not None:
        cross_filter = self.set_crossfilter(record, y_columns, x_axis, line_chart.htmlCode)
        line_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
          height=(330, "px"), html_code=None) -> GraphDC.ChartBar:
    """

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 30)
      bar = page.ui.charts.dc.hbar(data[:10], y_columns=4, x_axis='x')

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param title: Optional. The chart title
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    if isinstance(y_columns, list):
      bar_chart = self.series(record, y_columns, x_axis, 'bar', title, profile, options, width, height, html_code)
    else:
      bar_chart = GraphDC.ChartBar(self.page, width, height, title, options or {}, html_code, profile)
      bar_chart.dom.height(height[0]).x().controlsUseVisibility(True).yAxisLabel(y_columns)
      if record is not None:
        cross_filter = self.set_crossfilter(record, y_columns, x_axis, bar_chart.htmlCode)
        bar_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    return bar_chart

  def hbar(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), html_code=None) -> GraphDC.ChartRow:
    """

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 30)
      hbar = page.ui.charts.dc.hbar(data[:10], y_columns=4, x_axis='x')

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param title: Optional. The chart title
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    bar_chart = GraphDC.ChartRow(self.page, width, height, title, options or {}, html_code, profile)
    line_id = bar_chart.htmlCode
    bar_chart.dom.height(height[0]).x().chartGroup(line_id).elasticX(True)
    if record is not None:
      cross_filter = self.set_crossfilter(record, y_columns, x_axis, bar_chart.htmlCode)
      bar_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    return bar_chart

  def pie(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
          height=(330, "px"), html_code=None) -> GraphDC.ChartPie:
    """

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 30)
      pie = page.ui.charts.dc.pie(data[:5], y_columns=3, x_axis='x')

    `Crossfilter <https://square.github.io/crossfilter/>`_
    `DC <https://dc-js.github.io/dc.js/>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param title: Optional. The chart title
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    pie_chart = GraphDC.ChartPie(self.page, width, height, title, options or {}, html_code, profile)
    pie_chart.dom.height(height[0])
    if record is not None:
      cross_filter = self.set_crossfilter(record, y_columns, x_axis, pie_chart.htmlCode)
      pie_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    return pie_chart

  def sunburst(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None, width=(100, "%"),
               height=(330, "px"), html_code=None) -> GraphDC.ChartSunburst:
    """

    :tags:
    :categories:

    `Crossfilter <https://square.github.io/crossfilter/>`_
    `DC <https://dc-js.github.io/dc.js/>`_

    :param record:
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param title: Optional. The chart title
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    pie_chart = GraphDC.ChartSunburst(self.page, width, height, title, options or {}, html_code, profile)
    line_id = pie_chart.htmlCode
    self.page._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return +d['%(x)s'];})" % {'cId': line_id, 'data': record, 'x': x_axis}
    pie_chart.dom.dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d['%(y)s'] ;})" % {'cId': line_id, 'y': y_columns})
    return pie_chart

  def bubble(self, record=None, y_columns=None, x_axis=None, r_axis=None, title=None, profile=None, options=None,
             width=(100, "%"), height=(330, "px"), html_code=None) -> GraphDC.ChartBubble:
    """

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 30)
      bubble = page.ui.charts.dc.bubble(data, y_columns=3, x_axis='x', r_axis=4, options={'statc_factor': '/10'})

    `Crossfilter <https://square.github.io/crossfilter/>`_
    `DC <https://dc-js.github.io/dc.js/>`_
    `Bubble <https://www.tutorialspoint.com/dcjs/dcjs_bubble_chart.htm/>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param r_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param title: Optional. The chart title
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    if isinstance(y_columns, list):
      bubble_chart = self.series(record, y_columns, x_axis, 'bubble', title, profile, options, width, height, html_code)
    else:
      bubble_chart = GraphDC.ChartBubble(self.page, width, height, title, options or {}, html_code, profile)
      bubble_chart.dom.height(height[0]).x().yAxisLabel(y_columns).keyAccessor(0).radiusValueAccessorByKey(
        1, statc_factor=options.get('statc_factor'))
      if record is not None:
        cross_filter = self.set_crossfilter(
          record, y_columns, x_axis, bubble_chart.htmlCode, extra_cols=[(r_axis, int)])
        bubble_chart.dom.dimension(cross_filter['dimension'].varId).group(cross_filter['group'].varId)
    return bubble_chart
