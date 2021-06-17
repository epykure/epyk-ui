#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import graph


class Billboard:
  
  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "BB"

  def plot(self, record=None, y=None, x=None, kind="line", profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y: List | String. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param kind: String. Optional. The chart type.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    if y is not None and not isinstance(y, list):
      y = [y]
    return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Display a line chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartLine(self.page, width, height, html_code, options, profile)
    line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    line_chart.options.axis.x.tick.count = 5
    line_chart.options.axis.x.tick.rotate = 0
    line_chart.options.axis.x.tick.multiline = False
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def line_range(self, record=None, y_columns=None, x_axis=None, range=5, profile=None, width=(100, "%"),
                 height=(330, "px"), options=None, html_code=None):
    """
    Description:
    ------------
    Display a line range chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartLine(self.page, width, height, html_code, options, profile)
    line_chart.options.type = "area-line-range"
    line_chart.colors(self.page.theme.charts)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def bubble(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
    """
    Description:
    ------------
    Display a bubble chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BubbleChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    bubble_chart = graph.GraphBillboard.ChartBubble(self.page, width, height, html_code, options, profile)
    bubble_chart.labels(data['labels'])
    bubble_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      bubble_chart.add_dataset(d, data['series'][i])
    return bubble_chart

  def radar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """
    Description:
    ------------
    Display a radar chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.RadarChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    radar_chart = graph.GraphBillboard.ChartRadar(self.page, width, height, html_code, options, profile)
    radar_chart.labels(data['labels'])
    radar_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      radar_chart.add_dataset(d, data['series'][i])
    return radar_chart

  def spline(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
    """
    Description:
    ------------
    Display a spline chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.SplineChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartSpline(self.page, width, height, html_code, options, profile)
    line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def step(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Display a step chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.StepChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartSpline(self.page, width, height, html_code, options, profile)
    line_chart.options.type = 'step'
    line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def area(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Display a area chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.AreaChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartArea(self.page, width, height, html_code, options, profile)
    line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def area_step(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
                options=None, html_code=None):
    """
    Description:
    ------------
    Display a area step chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.AreaChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartArea(self.page, width, height, html_code, options, profile)
    line_chart.options.type = "area-step"
    line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def timeseries(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
                 height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a timeseries chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    line = self.line(record, y_columns, x_axis, profile, width, height, options, html_code)
    line.options.axis.x.type = "timeseries"
    line.options.axis.x.tick.format = "%Y-%m-%d"
    return line

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """
    Description:
    ------------
    Display a bar chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BarChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartBar(self.page, width, height, html_code, options, profile)
    if data['labels']:
      line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    line_chart.options.axis.x.tick.count = 5
    line_chart.options.axis.x.tick.rotate = 0
    line_chart.options.axis.x.tick.multiline = False
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def stacked(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    """
    Description:
    ------------
    Display a stacked bar chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.StackedBarChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartBar(self.page, width, height, html_code, options, profile)
    line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    line_chart.options.data.groups = [data['series']]
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Display a horizontal bar chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BarChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    h_bar = self.bar(record, y_columns, x_axis, profile, width, height, options, html_code)
    h_bar.options.axis.rotated = True
    return h_bar

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    """
    Description:
    ------------
    Display a scatter chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.ScatterPlot

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis, options={"agg":  options.get('agg', 'distinct')})
    line_chart = graph.GraphBillboard.ChartScatter(self.page, width, height, html_code, options, profile)
    line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """
    Description:
    ------------
    Display a pie chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.PieChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    pie_chart = graph.GraphBillboard.ChartPie(self.page, width, height, html_code, options, profile)
    pie_chart.labels(data['labels'])
    pie_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d, data['series'])
    return pie_chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """
    Description:
    ------------
    Display a donut chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.DonutChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    pie_chart = graph.GraphBillboard.ChartDonut(self.page, width, height, html_code, options, profile)
    pie_chart.labels(data['labels'])
    pie_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d, data['series'][i])
    return pie_chart

  def gauge(self, value=0, text="", profile=None, options=None, width=(100, "%"), height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a gauge chart from Billboard.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.GaugeChart

    Attributes:
    ----------
    :param value: Integer. Optional. The gauge chart value.
    :param text: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    g_chart = graph.GraphBillboard.ChartGauge(self.page, width, height, html_code, options, profile)
    g_chart.colors(self.page.theme.charts)
    g_chart.add_dataset(value, text)
    return g_chart
