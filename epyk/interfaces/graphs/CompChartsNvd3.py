#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core.html import graph


class Nvd3:
  
  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "NVD3"

  def plot(self, record=None, y=None, x=None, kind="line", profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

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

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
              height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a scatter chart from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/line.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis, options={"agg":  options.get('agg', 'distinct')})
    line_chart = graph.GraphNVD3.ChartScatter(self.page, width, height, options, html_code, profile)
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a line chart from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/line.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis)
    line_chart = graph.GraphNVD3.ChartLine(self.page, width, height, options, html_code, profile)
    line_chart.dom.useInteractiveGuideline(True)
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def line_cumulative(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
                      height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a Cumulative line chart from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/line.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis)
    line_chart = graph.GraphNVD3.ChartCumulativeLine(self.page, width, height, options, html_code, profile)
    line_chart.dom.useInteractiveGuideline(True)
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def line_focus(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
                 height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a line chart with focus from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/line.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis)
    line_chart = graph.GraphNVD3.ChartFocusLine(self.page, width, height, options, html_code, profile)
    line_chart.dom.useInteractiveGuideline(True)
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
          height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a bars chart from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/discreteBar.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    bar_chart = graph.GraphNVD3.ChartBar(self.page, width, height, options, html_code, profile)
    bar_chart.colors(self.page.theme.charts)
    if y_columns is not None and len(y_columns) > 1:
      bar_chart.dom._selector = "nv.models.multiBarChart()"
    bar_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data['datasets']):
      bar_chart.add_trace(d, data['series'][i])
    return bar_chart

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a bars chart from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/discreteBar.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    bar_chart = graph.GraphNVD3.ChartHorizontalBar(self.page, width, height, options, html_code, profile)
    bar_chart.dom.x(column="label").y(column="y")
    bar_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      bar_chart.add_trace(d, data['labels'][i])
    return bar_chart

  def multi(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
            height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a multi types chart from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/discreteBar.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    bar_chart = graph.GraphNVD3.ChartMultiBar(self.page, width, height, options, html_code, profile)
    bar_chart.colors(self.page.theme.charts)
    if y_columns is not None and len(y_columns) > 1:
      bar_chart.dom._selector = "nv.models.multiBarChart()"
    bar_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data['datasets']):
      bar_chart.add_trace(d, data['labels'][i])
    return bar_chart

  def histo(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
            height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a histo chart from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/discreteBar.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    histo_chart = graph.GraphNVD3.ChartHistoBar(self.page, width, height, options, html_code, profile)
    histo_chart.dom.x(column="label").y(column="y")
    histo_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      histo_chart.add_trace(d, data['labels'][i])
    return histo_chart

  def timeseries(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
                 height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a Timseries chart from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/discreteBar.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    histo_chart = graph.GraphNVD3.ChartHistoBar(self.page, width, height, options, html_code, profile)
    histo_chart.dom.x(column="label").y(column="y")
    histo_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      histo_chart.add_trace(d, data['labels'][i])
    return histo_chart

  def area(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a area chart from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/discreteBar.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    area_chart = graph.GraphNVD3.ChartArea(self.page, width, height, options, html_code, profile)
    area_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      area_chart.add_trace(d, data['labels'][i])
    area_chart.dom.x(column="label").y(column="y")
    return area_chart

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
          height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a pie chart from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/pie.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis)
    pie_chart = graph.GraphNVD3.ChartPie(self.page, width, height, options, html_code, profile)
    pie_chart.colors(self.page.theme.charts)
    pie_chart.dom.x(column="x").y(column="y")
    for i, d in enumerate(data['datasets']):
      pie_chart.add_trace(d, data['labels'][i])
    return pie_chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
            height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a donut chart from NVD3.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/pie.html

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
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis)
    pie_chart = graph.GraphNVD3.ChartPie(self.page, width, height, options, html_code, profile)
    pie_chart.dom.x(column="x").y(column="y").donut(True)
    pie_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      pie_chart.add_trace(d, data['labels'][i])
    return pie_chart

  def gauge(self, value, text=None, total=100, profile=None, options=None, width=(100, "%"), height=(330, "px"),
            html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      http://nvd3.org/examples/pie.html

    Attributes:
    ----------
    :param value:
    :param text:
    :param total:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    if total != 100:
      value = value / total * 100
      total = 100
    pie_chart = graph.GraphNVD3.ChartPie(self.page, width, height, options or {}, html_code, profile)
    pie_chart.colors(self.page.theme.charts)
    pie_chart.dom.x(column="x").y(column="y").donut(True).title(text or "%s%%" % value)
    pie_chart.dom.arcsRadius([
      {"inner": 0.7, "outer": 1},
      {"inner": 0.9, "outer": 1},
    ])

    pie_chart.add_trace([
      {"x": '', "y": value},
      {"x": '', "y": total - value},
    ])
    return pie_chart

  def parallel_coordinates(self, record, dimensions=None, profile=None, options=None, width=(100, "%"),
                           height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param dimensions:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    chart = graph.GraphNVD3.ChartParallelCoord(self.page, width, height, options or {}, html_code, profile)
    chart.set_dimension_names(dimensions)
    chart.colors(self.page.theme.charts)
    chart.add_trace(record)
    return chart

  def sunburst(self, record, name, profile=None, options=None, width=(100, "%"), height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param name:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    chart = graph.GraphNVD3.ChartSunbrust(self.page, width, height, options, html_code, profile)
    chart.colors(self.page.theme.charts)
    chart.add_trace(record, name=name)
    return chart

  def candlestick(self, record, closes, highs, lows, opens, x_axis, profile=None, options=None, width=(100, "%"),
                  height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

      data = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
      sc = page.ui.charts.nvd3.candlestick(data, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"],
          opens=["AAPL.Open"], x_axis='Date')

    Related Pages:


    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param closes:
    :param highs:
    :param lows:
    :param opens:
    :param x_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    all_series = []
    js_date_start = datetime.datetime(1970, 1, 1)
    for i, c in enumerate(closes):
      data_set = []
      for rec in record:
        dt = datetime.datetime.strptime(rec[x_axis], "%Y-%m-%d") - js_date_start
        data_set.append(
          {'date': dt.days, 'close': float(rec[c]), 'high': float(rec[highs[i]]), 'low': float(rec[lows[i]]),
           'open': float(rec[opens[i]])})
      all_series.append(data_set)

    candle_chart = graph.GraphNVD3.ChartCandlestick(self.page, width, height, options, html_code, profile)
    candle_chart.dom.x(column='date').y(column='close')
    candle_chart.colors(self.page.theme.charts)
    candle_chart.dom.xAxis.tickDateFormat()
    for s in all_series:
      candle_chart.add_trace(s)
    return candle_chart

  def ohlc(self, record, closes, highs, lows, opens, x_axis, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param closes:
    :param highs:
    :param lows:
    :param opens:
    :param x_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    all_series = []
    js_date_start = datetime.datetime(1970, 1, 1)
    for i, c in enumerate(closes):
      data_set = []
      for rec in record:
        dt = datetime.datetime.strptime(rec[x_axis], "%Y-%m-%d") - js_date_start
        data_set.append(
          {'date': dt.days, 'close': float(rec[c]), 'high': float(rec[highs[i]]), 'low': float(rec[lows[i]]),
           'open': float(rec[opens[i]])})
      all_series.append(data_set)
    ohlc_chart = graph.GraphNVD3.ChartOhlcBar(self.page, width, height, options or {}, html_code, profile)
    ohlc_chart.dom.x(column='date').y(column='close')
    ohlc_chart.colors(self.page.theme.charts)
    ohlc_chart.dom.xAxis.tickDateFormat()
    for s in all_series:
      ohlc_chart.add_trace(s)
    return ohlc_chart

  def group_box(self, profile=None, options=None, width=(100, "%"), height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Attributes:
    ----------
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    box_chart = graph.GraphNVD3.ChartBoxPlot(self.page, width, height, options or {}, html_code, profile)
    box_chart.colors(self.page.theme.charts)
    box_chart.dom.q1('q1').q2('median').q3('q3').wh(
      'maxRegularValue').wl('minRegularValue').outliers('outliers').staggerLabels(True)
    box_chart.dom.itemColor("seriesColor").x('title')
    return box_chart

  def forceDirected(self, profile=None, options=None, width=(400, "px"), height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Attributes:
    ----------
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    force_chart = graph.GraphNVD3.ChartForceDirected(self.page, width, height, options or {}, html_code, profile)
    force_chart.dom.width(width[0]).height(height[0]).nodeExtras("name").color('color')
    force_chart.colors(self.page.theme.charts)
    return force_chart
