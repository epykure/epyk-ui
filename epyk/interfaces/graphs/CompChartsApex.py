#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import graph
from epyk.interfaces import Arguments


class ApexChart(object):

  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Apex"

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a line chart from ApexCharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    data = self.parent.context.rptObj.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphApexCharts.Chart(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    chart.options.xaxis.categories = data['labels']
    for i, d in enumerate(data['datasets']):
      series = chart.options.add_series()
      series.name = d["label"]
      series.data = d
    chart.options.chart.type = "line"
    return chart

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a scatter chart from Apexchart.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    chart = graph.GraphApexCharts.Chart(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    data = self.parent.context.rptObj.data.chartJs.y(record or [], y_columns, x_axis)
    chart.options.xaxis.categories = data['labels']
    for i, d in enumerate(data['datasets']):
      series = chart.options.add_series()
      series.name = d["label"]
      series.data = d
    chart.options.chart.type = "scatter"
    return chart

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a bar chart from Apexcharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    chart = graph.GraphApexCharts.Bar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    data = self.parent.context.rptObj.data.chartJs.y(record or [], y_columns, x_axis)
    chart.options.xaxis.categories = data['labels']
    for i, d in enumerate(data['datasets']):
      series = chart.options.add_series()
      series.name = d["label"]
      series.data = d
    chart.options.chart.type = "bar"
    return chart

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a horizontal bars chart from ApexCharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    chart = graph.GraphApexCharts.Bar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    data = self.parent.context.rptObj.data.chartJs.y(record or [], y_columns, x_axis)
    chart.options.xaxis.categories = data['labels']
    for i, d in enumerate(data['datasets']):
      series = chart.options.add_series()
      series.name = d["label"]
      series.data = d
    chart.options.chart.type = "bar"
    chart.options.plotOptions.bar.horizontal = True
    return chart

  def area(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display an area chart from Apexcharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    chart = graph.GraphApexCharts.Area(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    data = self.parent.context.rptObj.data.chartJs.y(record or [], y_columns, x_axis)
    chart.options.xaxis.categories = data['labels']
    for i, d in enumerate(data['datasets']):
      series = chart.options.add_series()
      series.name = d["label"]
      series.data = d
    chart.options.chart.type = "area"
    return chart

  def radar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a radar chart from Apexcharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    chart = graph.GraphApexCharts.Chart(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    chart.options.chart.type = "radar"
    responsive = chart.options.add_responsive()
    responsive.breakpoint = 480
    return chart

  def polar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a polar chart from ApexCharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    chart = graph.GraphApexCharts.Pie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    chart.options.chart.type = "polarArea"
    responsive = chart.options.add_responsive()
    responsive.breakpoint = 480
    return chart

  def pie(self, record=None, y_column=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a pie chart from ApexCharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_column: String. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. The width of the component in the page, default (100, '%').
    :param height: Tuple. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    data = self.parent.context.rptObj.data.chartJs.y(record or [], [y_column], x_axis)
    chart = graph.GraphApexCharts.Pie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    chart.options.chart.type = "pie"
    chart.options.series = data["datasets"][0]
    chart.options.labels = data["labels"]
    responsive = chart.options.add_responsive()
    responsive.breakpoint = 480
    return chart

  def donut(self, record=None, y_column=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a donut chart from ApexCharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_column: String. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    data = self.parent.context.rptObj.data.chartJs.y(record or [], [y_column], x_axis)
    chart = graph.GraphApexCharts.Pie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    chart.options.chart.type = "donut"
    chart.options.series = data["datasets"][0]
    chart.options.labels = data["labels"]
    responsive = chart.options.add_responsive()
    responsive.breakpoint = 480
    return chart

  def radial(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a radial chart from ApexCharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    chart = graph.GraphApexCharts.Pie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    chart.options.chart.type = "radialBar"
    return chart

  def bubble(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a bubble chart from ApexCharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    chart = graph.GraphApexCharts.Area(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    chart.options.chart.type = "bubble"
    return chart

  def heatmap(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a heatmap chart from ApexCharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    chart = graph.GraphApexCharts.Area(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    chart.options.chart.type = "heatmap"
    return chart

  def treemap(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a treemap chart from ApexCharts.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    chart = graph.GraphApexCharts.Area(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.colors = self.parent.context.rptObj.theme.charts
    chart.options.chart.type = "treemap"
    return chart
