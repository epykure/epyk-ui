#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import graph


class C3(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "C3"

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a line chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/reference.html#line-connectNull

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    data = self.parent.context.rptObj.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def spline(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a spline line chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/samples/chart_spline.html

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartSpline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def step(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a step line chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/samples/chart_step.html

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartSpline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = 'step'
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def area(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a area line chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/samples/chart_step.html

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartArea(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def area_step(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a area step line chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/samples/chart_step.html

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartArea(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = "area-step"
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def timeseries(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a timeseries chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/samples/timeseries.html

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
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

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a bar chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/samples/chart_bar.html

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a horizontal bar chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/samples/axes_rotated.html

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    h_bar = self.bar(record, y_columns, x_axis, profile, width, height, options, htmlCode)
    h_bar.axis.rotated = True
    return h_bar

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a Scatter chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/samples/axes_rotated.html

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.c3.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphC3.ChartScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    return line_chart

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a pie chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/samples/chart_pie.html
      https://c3js.org/reference.html#pie-label-show

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.c3.y(record or [], y_columns, x_axis)
    pie_chart = graph.GraphC3.ChartPie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    pie_chart.labels(data['labels'])
    pie_chart.add_dataset(data['series'][0], data['labels'])
    return pie_chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a donut chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/samples/chart_donut.html

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.c3.y(record or [], y_columns, x_axis)
    pie_chart = graph.GraphC3.ChartDonut(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    pie_chart.labels(data['labels'])
    pie_chart.add_dataset(data['series'][0], data['labels'])
    return pie_chart

  def gauge(self, value=0, text="", profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a gauge chart from C3.

    Usage:
    -----

    Related Pages:

      https://c3js.org/samples/chart_gauge.html

    Attributes:
    ----------
    :param value:
    :param text:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    g_chart = graph.GraphC3.ChartGauge(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    g_chart.add_dataset(text, value)
    return g_chart

  def stanford(self, record=None, y_columns=None, x_axis=None, epoch_col=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns:
    :param x_axis:
    :param epoch_col:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    epoch, labels, series = [], [], []
    for rec in record:
      epoch.append(rec[epoch_col])
      labels.append(rec[x_axis])
      series.append([rec.get(c)for c in y_columns])

    line_chart = graph.GraphC3.ChartStanford(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(labels)
    line_chart.epoch(epoch, epoch_col)
    for i, y in enumerate(y_columns):
      line_chart.add_dataset(y, series[i])
    return line_chart
