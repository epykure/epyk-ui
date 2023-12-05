#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core.html import graph
from epyk.core.py import types


class Nvd3:
  
  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "NVD3"

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
    if y is not None and not isinstance(y, list):
      y = [y]
    return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def scatter(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              options: types.OPTION_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
              height: types.SIZE_TYPE = (330, "px"), html_code: str = None) -> graph.GraphNVD3.ChartScatter:
    """Display a scatter chart from NVD3.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 40)
      scatter = page.ui.charts.nvd3.scatter(data, y_columns=[1, 2, 3, 4], x_axis='x')
      scatter.dom.showYAxis(False).showXAxis(False)

    `Line <http://nvd3.org/examples/line.html>`_

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis, options={"agg":  options.get('agg', 'distinct')})
    line_chart = graph.GraphNVD3.ChartScatter(self.page, width, height, options, html_code, profile)
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def line(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           options: types.OPTION_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
           height: types.SIZE_TYPE = (330, "px"), html_code: str = None) -> graph.GraphNVD3.ChartLine:
    """Display a line chart from NVD3.

    :tags:
    :categories:

    Usage::

      c = page.ui.charts.nvd3.line(y_columns=["Value"], x_axis="Year", height=(500, "px"))
      page.ui.button("Click").click([
      text = page.ui.input("Italy")
      slider = page.ui.sliders.range(minimum=1990, maximum=2020)
      page.js.fetch(data_urls.DEMO_COUNTRY).csvtoRecords().filterCol("Country Name", text.dom.content).cast(["Year", "Value"]).
        filterCol("Year", slider.dom.min_select, ">").filterCol("Year", slider.dom.max_select, "<").
        get([
          c.build(pk.events.data)
          #"console.log(row)"
        ])
      ])

    `Line <http://nvd3.org/examples/line.html>`_

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis)
    line_chart = graph.GraphNVD3.ChartLine(self.page, width, height, options, html_code, profile)
    line_chart.dom.useInteractiveGuideline(True)
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def line_cumulative(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
                      options: types.OPTION_TYPE = None,
                      width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
                      html_code: str = None) -> graph.GraphNVD3.ChartCumulativeLine:
    """Display a Cumulative line chart from NVD3.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 40)
      page.ui.charts.nvd3.line_cumulative(data, y_columns=[1, 2, 3, 4], x_axis='x')

    `Line <http://nvd3.org/examples/line.html>`_

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis)
    line_chart = graph.GraphNVD3.ChartCumulativeLine(self.page, width, height, options, html_code, profile)
    line_chart.dom.useInteractiveGuideline(True)
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def line_focus(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
                 options: types.OPTION_TYPE = None,
                 width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
                 html_code: str = None) -> graph.GraphNVD3.ChartFocusLine:
    """Display a line chart with focus from NVD3.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 40)
      page.ui.charts.nvd3.line_focus(data, y_columns=[1, 2, 3, 4], x_axis='x')

    `Line <http://nvd3.org/examples/line.html>`_

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis)
    line_chart = graph.GraphNVD3.ChartFocusLine(self.page, width, height, options, html_code, profile)
    line_chart.dom.useInteractiveGuideline(True)
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def bar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
          options: types.OPTION_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
          height: types.SIZE_TYPE = (330, "px"), html_code: str = None) -> graph.GraphNVD3.ChartBar:
    """Display a bars chart from NVD3.

    :tags:
    :categories:

    Usage::

      c = page.ui.charts.nvd3.bar(y_columns=["Value"], x_axis="Year", height=(500, "px"))
      page.ui.button("Click").click([
      text = page.ui.input("Italy")
      slider = page.ui.sliders.range(minimum=1990, maximum=2020)
      page.js.fetch(data_urls.DEMO_COUNTRY).csvtoRecords().filterCol("Country Name", text.dom.content).cast(["Year", "Value"]).
        filterCol("Year", slider.dom.min_select, ">").filterCol("Year", slider.dom.max_select, "<").
        get([
          c.build(pk.events.data)
          #"console.log(row)"
        ])
      ])

    `Discrete Bar <http://nvd3.org/examples/discreteBar.html>`_

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    bar_chart = graph.GraphNVD3.ChartBar(self.page, width, height, options, html_code, profile)
    bar_chart.colors(self.page.theme.charts)
    if y_columns is not None and len(y_columns) > 1:
      bar_chart.dom._selector = "nv.models.multiBarChart()"
    bar_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data['datasets']):
      bar_chart.add_trace(d, data['series'][i])
    return bar_chart

  def hbar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           options: types.OPTION_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), html_code: str = None):
    """Display a bars chart from NVD3.

    :tags:
    :categories:

    Usage::

      c = page.ui.charts.nvd3.hbar(y_columns=["Value"], x_axis="Year", height=(500, "px"))
      page.ui.button("Click").click([
      text = page.ui.input("Italy")
      slider = page.ui.sliders.range(minimum=1990, maximum=2020)
      page.js.fetch(data_urls.DEMO_COUNTRY).csvtoRecords().filterCol("Country Name", text.dom.content).cast(["Year", "Value"]).
        filterCol("Year", slider.dom.min_select, ">").filterCol("Year", slider.dom.max_select, "<").
        get([
          c.build(pk.events.data)
          #"console.log(row)"
        ])
      ])

    `Horizontal Bar <http://nvd3.org/examples/discreteBar.html>`_

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    bar_chart = graph.GraphNVD3.ChartHorizontalBar(self.page, width, height, options, html_code, profile)
    bar_chart.dom.x(column="label").y(column="y")
    bar_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      bar_chart.add_trace(d, data['labels'][i])
    return bar_chart

  def multi(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            options: types.OPTION_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (330, "px"), html_code: str = None) -> graph.GraphNVD3.ChartMultiBar:
    """Display a multi types chart from NVD3.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 40)
      page.ui.charts.nvd3.multi(data, y_columns=[1, 2], x_axis='x')

    `Multi <http://nvd3.org/examples/discreteBar.html>`_

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    bar_chart = graph.GraphNVD3.ChartMultiBar(self.page, width, height, options, html_code, profile)
    bar_chart.colors(self.page.theme.charts)
    if y_columns is not None and len(y_columns) > 1:
      bar_chart.dom._selector = "nv.models.multiBarChart()"
    bar_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data['datasets']):
      bar_chart.add_trace(d, data['labels'][i])
    return bar_chart

  def histo(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            options: types.OPTION_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
            html_code: str = None) -> graph.GraphNVD3.ChartHistoBar:
    """Display a histo chart from NVD3.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 40)
      page.ui.charts.nvd3.histo(data, y_columns=[1, 2], x_axis='x')

    `histo <http://nvd3.org/examples/discreteBar.html>`_

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    histo_chart = graph.GraphNVD3.ChartHistoBar(self.page, width, height, options, html_code, profile)
    histo_chart.dom.x(column="label").y(column="y")
    histo_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      histo_chart.add_trace(d, data['labels'][i])
    return histo_chart

  def timeseries(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
                 options: types.OPTION_TYPE = None,
                 width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
                 html_code: str = None) -> graph.GraphNVD3.ChartHistoBar:
    """Display a Timseries chart from NVD3.

    :tags:
    :categories:

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    histo_chart = graph.GraphNVD3.ChartHistoBar(self.page, width, height, options, html_code, profile)
    histo_chart.dom.x(column="label").y(column="y")
    histo_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      histo_chart.add_trace(d, data['labels'][i])
    return histo_chart

  def area(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           options: types.OPTION_TYPE = None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
           html_code: str = None) -> graph.GraphNVD3.ChartArea:
    """Display an area chart from NVD3.

    :tags:
    :categories:

    `NVD3 <https://nvd3.org/examples/index.html>`_
    `Area <https://nvd3.org/examples/index.html>`_

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.labely(record or [], y_columns, x_axis)
    area_chart = graph.GraphNVD3.ChartArea(self.page, width, height, options, html_code, profile)
    area_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      area_chart.add_trace(d, data['labels'][i])
    area_chart.dom.x(column="label").y(column="y")
    return area_chart

  def pie(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
          options: types.OPTION_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
          height: types.SIZE_TYPE = (330, "px"), html_code: str = None) -> graph.GraphNVD3.ChartPie:
    """Display a pie chart from NVD3.

    :tags:
    :categories:

    Usage::

      dataPoints = [
        {'x': "Series A", 'y': 10, 'y1': 10},
        {'x': "Series B", 'y': 35, 'y1': 20},
      ]

      dataPoints2 = [
        {'label': "mango", 'x': "Series A", 'y': 30, 'y1': 0},
        {'label': "grape", 'x': "Series B", 'y': 28, 'y1': 0}
      ]

      chart = page.ui.charts.nvd3.pie(dataPoints, y_columns=["y"], x_axis='x')
      page.ui.button("Load").click([c.build(nvd3.xy(dataPoints2, ["y"], "x"))])

    `Pie <http://nvd3.org/examples/pie.html>`_

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis)
    pie_chart = graph.GraphNVD3.ChartPie(self.page, width, height, options, html_code, profile)
    pie_chart.colors(self.page.theme.charts)
    pie_chart.dom.x(column="x").y(column="y")
    for i, d in enumerate(data['datasets']):
      pie_chart.add_trace(d, data['labels'][i])
    return pie_chart

  def donut(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            options: types.OPTION_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (330, "px"), html_code: str = None) -> graph.GraphNVD3.ChartPie:
    """Display a donut chart from NVD3.

    :tags:
    :categories:

    Usage::

      c = page.ui.charts.nvd3.donut(y_columns=["Value"], x_axis="Year", height=(500, "px"))
      donut_s = page.ui.charts.nvd3.donut(data, y_columns=[1], x_axis='g')
      donut_s.dom.padAngle(.08).cornerRadius(5)

    `Pie <http://nvd3.org/examples/pie.html>`_

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
    options.update({'y_columns': y_columns, 'x_axis': x_axis})
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis)
    pie_chart = graph.GraphNVD3.ChartPie(self.page, width, height, options, html_code, profile)
    pie_chart.dom.x(column="x").y(column="y").donut(True)
    pie_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      pie_chart.add_trace(d, data['labels'][i])
    return pie_chart

  def gauge(self, value: float, text: str = None, total: float = 100, profile: types.PROFILE_TYPE = None,
            options: types.OPTION_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (330, "px"), html_code: str = None) -> graph.GraphNVD3.ChartPie:
    """

    :tags:
    :categories:

    Usage::

      page.ui.charts.nvd3.gauge(value=8, text="", total=10)

    `Pie <http://nvd3.org/examples/pie.html>`_

    :param value:
    :param text:
    :param total:
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    if total != 100:
      value = value / total * 100
      total = 100
    options = options or {}
    options.update({'y_columns': []})
    pie_chart = graph.GraphNVD3.ChartPie(self.page, width, height, options, html_code, profile)
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

  def parallel_coordinates(self, record, dimensions=None, profile: types.PROFILE_TYPE = None,
                           options: types.OPTION_TYPE = None,
                           width: types.SIZE_TYPE = (100, "%"),
                           height: types.SIZE_TYPE = (330, "px"),
                           html_code: str = None) -> graph.GraphNVD3.ChartParallelCoord:
    """

    :tags:
    :categories:

    :param record: Optional. The Python list of dictionaries
    :param dimensions: Optional.
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    chart = graph.GraphNVD3.ChartParallelCoord(self.page, width, height, options or {}, html_code, profile)
    chart.set_dimension_names(dimensions)
    chart.colors(self.page.theme.charts)
    chart.add_trace(record)
    return chart

  def sunburst(
          self, record, name: str, profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None,
          width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
          html_code: str = None) -> graph.GraphNVD3.ChartSunbrust:
    """

    :tags:
    :categories:

    Usage::

      records = [
        {'name': 'scripts',
         'children': [
            {"name": "javascript", "size": 10},
            {"name": "python", "size": 5},
            {"name": "ruby", "size": 5},
            {"name": "r", "size": 5}]},
         {"name": "code",
          "children": [
            {"name": "C#", "size": 10},
            {"name": "Java", "size": 5},
          ]
          }
      ]

      page.ui.charts.nvd3.sunburst(records, name='languages')

    :param record: Optional. The Python list of dictionaries
    :param name: Optional.
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    chart = graph.GraphNVD3.ChartSunbrust(self.page, width, height, options, html_code, profile)
    chart.colors(self.page.theme.charts)
    chart.add_trace(record, name=name)
    return chart

  def candlestick(
          self, record, closes, highs, lows, opens, x_axis, profile=None, options=None, width=(100, "%"),
          height=(330, "px"), html_code=None) -> graph.GraphNVD3.ChartCandlestick:
    """

    :tags:
    :categories:

    Usage::

      data = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
      sc = page.ui.charts.nvd3.candlestick(data, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"],
          opens=["AAPL.Open"], x_axis='Date')

      # Example using pandas_datareader
      import pandas_datareader.data as pdr

      btc = pdr.get_data_yahoo("BTC-USD", datetime.strptime(start, '%Y-%m-%d'), datetime.strptime(end, '%Y-%m-%d'))
      btc.reset_index(inplace=True)
      btc["Date"] = btc["Date"].dt.strftime("%Y-%m-%d")

      c1 = page.ui.charts.nvd3.candlestick(
        btc.to_dict("records"), closes=["Adj Close"], highs=["High"], lows=["Low"], opens=["Open"], x_axis="Date")
      c1.shared.y_format_number(factor=1000)
      c1.shared.y_label("$")

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
    candle_chart.dom.xAxis.tickDateFormat()
    candle_chart.colors(self.page.theme.charts)
    for s in all_series:
      candle_chart.add_trace(s)
    return candle_chart

  def ohlc(
          self, record, closes, highs, lows, opens, x_axis, profile=None, options=None, width=(100, "%"),
          height=(330, "px"), html_code=None
  ) -> graph.GraphNVD3.ChartOhlcBar:
    """

    :tags:
    :categories:

    Usage::

      from epyk.mocks import urls as data_urls

      data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
      chart = page.ui.charts.nvd3.ohlc(data_rest, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"], opens=["AAPL.Open"], x_axis='Date')

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
    ohlc_chart.colors(self.page.theme.charts)
    for s in all_series:
      ohlc_chart.add_trace(s)
    return ohlc_chart

  def group_box(
          self, profile=None, options=None, width=(100, "%"), height=(330, "px"), html_code=None
  ) -> graph.GraphNVD3.ChartBoxPlot:
    """

    :tags:
    :categories:

    Usage::

      plot_box = page.ui.charts.nvd3.group_box()
      plot_box.add_box(q1=1.05, q3=2.7, mean=3.365, median=1.3, minRegularValue=0.4, maxRegularValue=4.4, minOutlier=0.4, maxOutlier=6)
      plot_box.add_box(q1=1.05, q3=2.849999996, mean=3.4949999, median=1.5, minRegularValue=0.3, maxRegularValue=4.9, minOutlier=0.3, maxOutlier=4.9)

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

  def forceDirected(
          self, profile=None, options=None, width=(400, "px"), height=(330, "px"), html_code=None
  ) -> graph.GraphNVD3.ChartForceDirected:
    """

    :tags:
    :categories:

    Usage::

      force = page.ui.charts.nvd3.forceDirected()
      force.add_trace({
          "nodes": [
            {"name": "Myriel", "group":1},
            {"name": "Napoleon", "group":1},
            {"name": "Mlle.Baptistine", "group": 5}],
          "links": [
            {"source": 1, "target": 2, "value": 1}
          ]
      })

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
