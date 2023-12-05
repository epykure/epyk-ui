#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import graph


class Billboard:
  
  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "BB"

  def plot(self, record=None, y=None, x=None, kind="line", profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None, **kwargs):
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
    if y is not None and not isinstance(y, list):
      y = [y]
    return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """Display a line chart from Billboard.

    :tags:
    :categories:

    Usage::

      dataPoints = [
        {'x': 0, 'y': 10, 'y1': 10},
        {'x': 1, 'y': 35, 'y1': 20}]
      chart = page.ui.charts.billboard.line(dataPoints, y_columns=["y", 'y1'], x_axis='x')
      page.ui.button("reset").click([chart.build(dataPoints2)])

    `Line <https://naver.github.io/billboard.js/demo/#Chart.LineChart>`_

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
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartLine(self.page, width, height, html_code, options, profile)
    if data['labels']:
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
    """Display a line range chart from Billboard.

    :tags:
    :categories:

    Usage::

      dataPoints = [
        {'x': 0, 'y': 10, 'y1': 10},
        {'x': 1, 'y': 35, 'y1': 20},
        {'x': 2, 'y': 25, 'y1': 10},
        {'x': 3, 'y': 30, 'y1': 5},
        {'x': 4, 'y': 28, 'y1': 10}]
      c = page.ui.charts.billboard.line_range(dataPoints, y_columns=["y", 'y1'], x_axis='x')

    `Line Range <https://naver.github.io/billboard.js/demo/#Chart.LineChart>`_

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
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartLine(self.page, width, height, html_code, options, profile)
    line_chart.options.type = "area-line-range"
    line_chart.colors(self.page.theme.charts)
    if data['labels']:
      line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def bubble(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
    """Display a bubble chart from Billboard.

    :tags:
    :categories:

    Usage::

      c = page.ui.charts.bb.bubble(y_columns=["Value"], x_axis="Year", height=(500, "px"))
      c.options.axis.y.tick.formats.scale(1000000)

    `Bubble <https://naver.github.io/billboard.js/demo/#Chart.BubbleChart>`_

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
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    bubble_chart = graph.GraphBillboard.ChartBubble(self.page, width, height, html_code, options, profile)
    if data['labels']:
      bubble_chart.labels(data['labels'])
    bubble_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      bubble_chart.add_dataset(d, data['series'][i])
    return bubble_chart

  def radar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """Display a radar chart from Billboard.

    :tags:
    :categories:

    `Radar <https://naver.github.io/billboard.js/demo/#Chart.RadarChart>`_

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
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    radar_chart = graph.GraphBillboard.ChartRadar(self.page, width, height, html_code, options, profile)
    if data['labels']:
      radar_chart.labels(data['labels'])
    radar_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      radar_chart.add_dataset(d, data['series'][i])
    return radar_chart

  def spline(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
    """Display a spline chart from Billboard.

    :tags:
    :categories:

    Usage::

      data = page.py.requests.csv(data_urls.DEMO_COUNTRY)
      c = page.ui.charts.bb.spline(data, y_columns=["Value"], x_axis="Year", height=(500, "px"))
      c.options.axis.y.tick.formats.scale(1000000)

    `Spline <https://naver.github.io/billboard.js/demo/#Chart.SplineChart>`_

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
    data = self.page.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartSpline(self.page, width, height, html_code, options, profile)
    if data['labels']:
      line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def step(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """Display a step chart from Billboard.

    :tags:
    :categories:

    Usage::

      data = page.py.requests.csv(data_urls.DEMO_COUNTRY)
      c = page.ui.charts.bb.step(data, y_columns=["Value"], x_axis="Year", height=(500, "px"))
      c.options.axis.y.tick.formats.scale(1000000)

    `Line Step <https://naver.github.io/billboard.js/demo/#Chart.StepChart>`_

    :param record: Optional. The Python list of dictionaries.
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
    if data['labels']:
      line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def area(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """Display an area chart from Billboard.

    :tags:
    :categories:

    Usage::

      data = page.py.requests.csv(data_urls.DEMO_COUNTRY)
      c = page.ui.charts.bb.area(data, y_columns=["Value"], x_axis="Year", height=(500, "px"))
      c.options.axis.y.tick.formats.scale(1000000)

    `Area <https://naver.github.io/billboard.js/demo/#Chart.AreaChart>`_

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
    if data['labels']:
      line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def area_step(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
                options=None, html_code=None):
    """Display a area step chart from Billboard.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 40)
      area_step = page.ui.charts.billboard.area_step(data, y_columns=list(range(4)), x_axis='x')

    `Area Step <https://naver.github.io/billboard.js/demo/#Chart.AreaChart>`_

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
    if data['labels']:
      line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def timeseries(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
                 height=(330, "px"), html_code=None):
    """Display a timeseries chart from Billboard.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import urls as data_urls

      data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
      ts = page.ui.charts.billboard.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

    `Timeseries <https://naver.github.io/billboard.js/demo/#Chart.LineChart>`_

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
    """Display a bar chart from Billboard.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 40)
      b = page.ui.charts.billboard.bar(data, y_columns=list(range(4)), x_axis='x')

    `Bar <https://naver.github.io/billboard.js/demo/#Chart.BarChart>`_

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
    """Display a stacked bar chart from Billboard.

    :tags:
    :categories:

    Usage::

      data = page.py.requests.csv(data_urls.DEMO_COUNTRY)
      c = page.ui.charts.bb.stacked(data, y_columns=["Value"], x_axis="Year", height=(500, "px"))
      c.options.axis.y.tick.formats.scale(1000000)
      c.options.axis.x.tick.count = 5

    'Stacked <https://naver.github.io/billboard.js/demo/#Chart.StackedBarChart>`_

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
    line_chart.options.data.groups = [data['series']]
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """Display a horizontal bar chart from Billboard.

    :tags:
    :categories:

    Usage::

      data = page.py.requests.csv(data_urls.DEMO_COUNTRY)
      c = page.ui.charts.bb.hbar(data, y_columns=["Value"], x_axis="Year", height=(500, "px"))
      c.options.axis.y.tick.formats.scale(1000000)
      c.options.axis.x.tick.count = 5

    `Horizontal Bar <https://naver.github.io/billboard.js/demo/#Chart.BarChart>`_

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
    """Display a scatter chart from Billboard.

    :tags:
    :categories:

    Usage::

      data = page.py.requests.csv(data_urls.DEMO_COUNTRY)
      c = page.ui.charts.bb.scatter(data, y_columns=["Value"], x_axis="Year", height=(500, "px"))
      c.options.axis.y.tick.formats.scale(1000000)
      c.options.axis.x.tick.count = 5

    `Scatter <https://naver.github.io/billboard.js/demo/#Chart.ScatterPlot>`_

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
    if data['labels']:
      line_chart.labels(data['labels'])
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """Display a pie chart from Billboard.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import urls as data_urls

      data = randoms.getSeries(5, 40)
      p = page.ui.charts.billboard.pie(data, y_columns=[1], x_axis='g')

    `Pie <https://naver.github.io/billboard.js/demo/#Chart.PieChart>`_

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
    if data['labels']:
      pie_chart.labels(data['labels'])
    pie_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d, data['series'])
    return pie_chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """Display a donut chart from Billboard.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import urls as data_urls

      data = randoms.getSeries(5, 40)
      p = page.ui.charts.billboard.donut(data, y_columns=[1], x_axis='g')

    `Donut <https://naver.github.io/billboard.js/demo/#Chart.DonutChart>`_

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
    if data['labels']:
      pie_chart.labels(data['labels'])
    pie_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d, data['series'][i])
    return pie_chart

  def gauge(self, value: int = 0, text: str = "", profile=None, options=None, width=(100, "%"), height=(330, "px"), html_code=None):
    """Display a gauge chart from Billboard.

    :tags:
    :categories:

    Usage::

      g = page.ui.charts.billboard.gauge(60)

    `Gauge <https://naver.github.io/billboard.js/demo/#Chart.GaugeChart`>_

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
