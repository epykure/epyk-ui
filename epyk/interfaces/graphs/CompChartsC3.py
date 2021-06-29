#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import graph


class C3:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "C3"

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
    Display a line chart from C3.

    :tags:
    :categories:

    Usage::

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
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
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

  def spline(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
    """
    Description:
    ------------
    Display a spline line chart from C3.

    :tags:
    :categories:

    Usage::

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
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
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

  def step(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Display a step line chart from C3.

    :tags:
    :categories:

    Usage::

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
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
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

  def area(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Display a area line chart from C3.

    :tags:
    :categories:

    Usage::

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
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
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

  def area_step(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
                options=None, html_code=None):
    """
    Description:
    ------------
    Display a area step line chart from C3.

    :tags:
    :categories:

    Usage::

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
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
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

  def timeseries(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
                 height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a timeseries chart from C3.

    :tags:
    :categories:

    Usage::

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
    Display a bar chart from C3.

    :tags:
    :categories:

    Usage::

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
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
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

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Display a horizontal bar chart from C3.

    :tags:
    :categories:

    Usage::

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
    Display a Scatter chart from C3.

    :tags:
    :categories:

    Usage::

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
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
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

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """
    Description:
    ------------
    Display a pie chart from C3.

    :tags:
    :categories:

    Usage::

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
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
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

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """
    Description:
    ------------
    Display a donut chart from C3.

    :tags:
    :categories:

    Usage::

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
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
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

  def gauge(self, value=0, text="", profile=None, options=None, width=(100, "%"), height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a gauge chart from C3.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://c3js.org/samples/chart_gauge.html

    Attributes:
    ----------
    :param value: Number. Optional. The value.
    :param text: String. Optional. The gauge text.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    g_chart = graph.GraphC3.ChartGauge(self.page, width, height, html_code, options or {}, profile)
    g_chart.colors(self.page.theme.charts)
    g_chart.add_dataset(value, text)
    return g_chart

  def stanford(self, record=None, y_columns=None, x_axis=None, epoch_col=None, profile=None, width=(100, "%"),
               height=(330, "px"), options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Related Pages:

      https://c3js.org/samples/chart_stanford.html

    Usage::

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param epoch_col: String. Optional. The column corresponding to a key.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
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
