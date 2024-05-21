#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import graph
from epyk.core.py import types
from epyk.core.js import JsUtils


class C3:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "C3"

  def plot(self, record=None, y=None, x=None, kind: str = "line", profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs):
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
    if y is not None and not isinstance(y, list) and not JsUtils.isJsData(y):
      y = [y]
    return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def line(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphC3.ChartLine:
    """Display a line chart from C3.

    :tags:
    :categories:

    Usage::

      dataPoints = [
        {'x': 0, 'y': 10, 'y1': 10},
        {'x': 1, 'y': 35, 'y1': 20},
        {'x': 2, 'y': 25, 'y1': 10},
        {'x': 3, 'y': 30, 'y1': 5},
        {'x': 4, 'y': 28, 'y1': 10}]
      c = page.ui.charts.c3.line(dataPoints2, y_columns=["y", 'y1'], x_axis='x') #dataPoints, y_columns=["y", 'y1'], x_axis='x')

    `Line <https://c3js.org/>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartLine(self.page, width, height, html_code, options, profile)
    line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    #line_chart.options.axis.x.tick.count = 5
    #line_chart.options.axis.x.tick.rotate = 0
    #line_chart.options.axis.x.tick.multiline = False
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def spline(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
             options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphC3.ChartSpline:
    """Display a spline line chart from C3.

    :tags:
    :categories:

    `Spline <https://c3js.org/samples/chart_spline.html>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartSpline(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def step(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphC3.ChartSpline:
    """Display a step line chart from C3.

    :tags:
    :categories:

    `Step <https://c3js.org/samples/chart_step.html>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartSpline(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.options.type = 'step'
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def area(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphC3.ChartArea:
    """Display an area line chart from C3.

    :tags:
    :categories:

    `Area <https://c3js.org/samples/chart_area.html>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartArea(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def area_step(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
                width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
                options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphC3.ChartArea:
    """Display a area step line chart from C3.

    :tags:
    :categories:

   `Area <https://c3js.org/samples/chart_area.html>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartArea(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart._type = "area-step"
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def timeseries(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
                 options: types.OPTION_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
                 height: types.SIZE_TYPE = (330, "px"), html_code: str = None) -> graph.GraphC3.ChartLine:
    """Display a timeseries chart from C3.

    :tags:
    :categories:

    `Time series <https://c3js.org/samples/timeseries.html>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    line = self.line(record, y_columns, x_axis, profile, width, height, options, html_code)
    line.options.axis.x.type = "timeseries"
    line.options.axis.x.tick.format = "%Y-%m-%d"
    return line

  def bar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
          width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
          options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphC3.ChartBar:
    """Display a bar chart from C3.

    :tags:
    :categories:

    Related Pages:

      https://c3js.org/samples/chart_bar.html

    :param record: Optional. The Python list of dictionaries.
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartBar(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.labels(data['labels'])
    line_chart.options.axis.x.tick.rotate = 0
    line_chart.options.axis.x.tick.multiline = False
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def hbar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphC3.ChartBar:
    """Display a horizontal bar chart from C3.

    :tags:
    :categories:

    `Axes <https://c3js.org/samples/axes_rotated.html>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    h_bar = self.bar(record, y_columns, x_axis, profile, width, height, options, html_code)
    h_bar.options.axis.rotated = True
    return h_bar

  def scatter(self, record=None, y_columns=None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
              options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphC3.ChartScatter:
    """Display a Scatter chart from C3.

    :tags:
    :categories:

    `Scatter <https://c3js.org/samples/chart_scatter.html>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.c3.y(record or [], y_columns, x_axis, options={"agg": options.get('agg', 'distinct')})
    line_chart = graph.GraphC3.ChartScatter(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def pie(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
          width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
          options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphC3.ChartPie:
    """Display a pie chart from C3.

    :tags:
    :categories:

    `Pie <https://c3js.org/samples/chart_pie.html>`_
    `Pie Labels <https://c3js.org/reference.html#pie-label-show>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    pie_chart = graph.GraphC3.ChartPie(self.page, width, height, html_code, options, profile)
    pie_chart.colors(self.page.theme.charts)
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d, data['series'][i])
    return pie_chart

  def donut(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
            options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphC3.ChartDonut:
    """Display a donut chart from C3.

    :tags:
    :categories:

    `Donut <https://c3js.org/samples/chart_donut.html>`_

    :param record: Optional. The Python list of dictionaries.
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    pie_chart = graph.GraphC3.ChartDonut(self.page, width, height, html_code, options, profile)
    pie_chart.colors(self.page.theme.charts)
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d, data['series'][i])
    return pie_chart

  def gauge(self, value: float = 0, text: str = "", profile: types.PROFILE_TYPE = None,
            options: types.OPTION_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (330, "px"), html_code: str = None) -> graph.GraphC3.ChartGauge:
    """Display a gauge chart from C3.

    :tags:
    :categories:

    Usage::

      c = page.ui.charts.c3.gauge(45)
      page.ui.button("Update").click([c.build(10)])

    `Gauge <https://c3js.org/samples/chart_gauge.html>`_

    :param value: Optional. The value
    :param text: Optional. The gauge text
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    g_chart = graph.GraphC3.ChartGauge(self.page, width, height, html_code, options or {}, profile)
    g_chart.colors(self.page.theme.charts)
    g_chart.add_dataset(value, text)
    return g_chart

  def stanford(self, record=None, y_columns: list = None, x_axis: str = None, epoch_col=None,
               profile: types.PROFILE_TYPE = None,
               width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
               options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphC3.ChartStanford:
    """

    :tags:
    :categories:

    `Stanford https://c3js.org/samples/chart_stanford.html>`_

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param epoch_col: Optional. The column corresponding to a key
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    epoch, labels, series = [], [], []
    if record:
      for rec in record:
        epoch.append(rec[epoch_col])
        labels.append(rec[x_axis])
        series.append([rec.get(c)for c in y_columns])
    line_chart = graph.GraphC3.ChartStanford(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.options.point.r = 2
    if record:
      line_chart.labels(labels)
      line_chart.epoch(epoch, epoch_col)
      for i, y in enumerate(y_columns):
        line_chart.add_dataset(series[i], y)
    return line_chart
