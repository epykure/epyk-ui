#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import graph


class Billboard(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "BB"

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a line chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def line_range(self, record=None, y_columns=None, x_axis=None, range=5, profile=None, width=(100, "%"),
                 height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a line range chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = "area-line-range"
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def bubble(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a bubble chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BubbleChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    bubble_chart = graph.GraphBillboard.ChartBubble(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bubble_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      bubble_chart.add_dataset(data['series'][i], d)
      bubble_chart.data.labels = True
    return bubble_chart

  def radar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a radar chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.RadarChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    radar_chart = graph.GraphBillboard.ChartRadar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    radar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      radar_chart.add_dataset(data['series'][i], d)
      radar_chart.data.labels = True
    return radar_chart

  def spline(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a spline chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.SplineChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartSpline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def step(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a step chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.StepChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartSpline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = 'step'
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def area(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a area chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.AreaChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartArea(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def area_step(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
                options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a area step chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.AreaChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartArea(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = "area-step"
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def timeseries(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
                 height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a timeseries chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    line = self.line(record, y_columns, x_axis, profile, width, height, options, htmlCode)
    line.axis.x.type = "timeseries"
    line.axis.x.tick.format = "%Y-%m-%d"
    return line

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a bar chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BarChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def stacked(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a stacked bar chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.StackedBarChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    line_chart.data.groups = [data['series']]
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a horizontal bar chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.BarChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    h_bar = self.bar(record, y_columns, x_axis, profile, width, height, options, htmlCode)
    h_bar.axis.rotated = True
    return h_bar

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a scatter chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.ScatterPlot

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a pie chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.PieChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    pie_chart = graph.GraphBillboard.ChartPie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(data['series'][i], d)
    return pie_chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a donut chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.DonutChart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    pie_chart = graph.GraphBillboard.ChartDonut(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(data['series'][i], d)
    return pie_chart

  def gauge(self, value=0, text="", profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a gauge chart from Billboard.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.GaugeChart

    Attributes:
    ----------
    :param value: Integer. Optional. The gauge chart value.
    :param text: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    g_chart = graph.GraphBillboard.ChartGauge(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    g_chart.add_dataset(text, value)
    return g_chart
