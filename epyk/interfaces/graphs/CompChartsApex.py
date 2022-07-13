#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import types
from epyk.core.html import graph
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html


class ApexChart:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Apex"

  def line(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None):
    """
    Description:
    ------------
    Display a line chart from ApexCharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphApexCharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.xaxis.categories = data['labels']
    for i, d in enumerate(data['datasets']):
      series = chart.options.add_series()
      series.name = d["label"]
      series.data = d["data"]
    chart.options.chart.type = "line"
    return chart

  def plot(self, record=None, y: list = None, x: str = None, kind: str = "line", profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: dict = None, html_code: str = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data.
    :param y: Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x: Optional. The column corresponding to a key in the dictionaries in the record.
    :param kind: Optional. The chart type.
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. The width of the component in the page, default (100, '%').
    :param height: Optional. The height of the component in the page, default (330, "px").
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    if y is not None and not isinstance(y, list):
      y = [y]
    return getattr(self, kind)(records=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def scatter(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
              options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display a scatter chart from Apexchart.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    chart = graph.GraphApexCharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    data = self.page.data.chartJs.xyz(record or [], y_columns, x_axis, None)
    chart.options.xaxis.categories = data['labels']
    if all(isinstance(ele, (int, float)) for ele in data['labels']):
      chart.options.xaxis.type = "numeric"
    for i, d in enumerate(data['datasets']):
      series = chart.options.add_series()
      series.name = d["label"]
      series.data = d["data"]
    chart.options.chart.type = "scatter"
    return chart

  def bar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
          width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
          options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display a bar chart from Apexcharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    chart = graph.GraphApexCharts.Bar(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart.options.xaxis.categories = data['labels']
    for i, d in enumerate(data['datasets']):
      series = chart.options.add_series()
      series.name = d["label"]
      series.data = d["data"]
    chart.options.chart.type = "bar"
    return chart

  def hbar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display a horizontal bars chart from ApexCharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    chart = graph.GraphApexCharts.Bar(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart.options.xaxis.categories = data['labels']
    for i, d in enumerate(data['datasets']):
      series = chart.options.add_series()
      series.name = d["label"]
      series.data = d["data"]
    chart.options.chart.type = "bar"
    chart.options.plotOptions.bar.horizontal = True
    return chart

  def area(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display an area chart from Apexcharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    chart = graph.GraphApexCharts.Area(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart.options.xaxis.categories = data['labels']
    for i, d in enumerate(data['datasets']):
      series = chart.options.add_series()
      series.name = d["label"]
      series.data = d["data"]
    chart.options.chart.type = "area"
    return chart

  def radar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
            options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display a radar chart from Apexcharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    chart = graph.GraphApexCharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.chart.type = "radar"
    responsive = chart.options.add_responsive()
    responsive.breakpoint = 480
    return chart

  def polar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
            options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display a polar chart from ApexCharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    chart = graph.GraphApexCharts.Pie(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.chart.type = "polarArea"
    responsive = chart.options.add_responsive()
    responsive.breakpoint = 480
    return chart

  def pie(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
          width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
          options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display a pie chart from ApexCharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: The column corresponding to a key in the dictionaries in the record.
    :param profile: Optional. A flag to set the component performance storage.
    :param width: The width of the component in the page, default (100, '%').
    :param height: The height of the component in the page, default (330, "px").
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphApexCharts.Pie(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.chart.type = "pie"
    if data["datasets"]:
      chart.options.series = data["datasets"][0]["data"]
      chart.options.labels = data["labels"]
    responsive = chart.options.add_responsive()
    responsive.breakpoint = 480
    return chart

  def donut(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
            options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display a donut chart from ApexCharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphApexCharts.Pie(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.chart.type = "donut"
    if data["datasets"]:
      chart.options.series = data["datasets"][0]["data"]
      chart.options.labels = data["labels"]
    responsive = chart.options.add_responsive()
    responsive.breakpoint = 480
    return chart

  def radial(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
             options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display a radial chart from ApexCharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    chart = graph.GraphApexCharts.Pie(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.chart.type = "radialBar"
    return chart

  def bubble(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
             options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display a bubble chart from ApexCharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": [], 'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}}
    if options is not None:
      dfl_options.update(options)
    chart = graph.GraphApexCharts.Bubble(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.chart.type = "bubble"
    return chart

  def heatmap(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
              options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display a heatmap chart from ApexCharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    if options is not None:
      dfl_options.update(options)
    chart = graph.GraphApexCharts.Area(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.chart.type = "heatmap"
    return chart

  def treemap(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
              options: dict = None, html_code: str = None):
    """
    Description:
    ------------
    Display a treemap chart from ApexCharts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param y_columns: The columns corresponding to keys in the dictionaries in the record
    :param x_axis: The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    if options is not None:
      dfl_options.update(options)
    chart = graph.GraphApexCharts.Area(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.chart.type = "treemap"
    return chart

  def gauge(self, values: float = 0, labels: str = "", profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
            options: types.OPTION_TYPE = None, html_code: str = None):
    """
    Description:
    ------------
    Display a gauge chart from ApexCharts.

    :tags:
    :categories:

    Related Pages:

      https://apexcharts.com/javascript-chart-demos/radialbar-charts/multiple-radialbars/

    Attributes:
    ----------
    :param values: The gauge value.
    :param labels: The gauge label.
    :param profile: Optional. A flag to set the component performance storage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    if options is not None:
      dfl_options.update(options)
    chart = graph.GraphApexCharts.RadialBar(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.chart.type = "radialBar"
    chart.options.height = height[0]
    chart.options.series = [values] if not isinstance(values, list) else values
    chart.options.labels = [labels] if not isinstance(labels, list) else labels
    if dfl_options.get("half", False):
      chart.options.plotOptions.radialBar.startAngle = -90
      chart.options.plotOptions.radialBar.endAngle = 90
    if not labels:
      chart.options.plotOptions.radialBar.dataLabels.name.show = False
    chart.options.plotOptions.radialBar.dataLabels.name.fontSize = self.page.body.style.globals.font.size
    chart.options.plotOptions.radialBar.dataLabels.name.offsetY = 5
    chart.options.plotOptions.radialBar.dataLabels.value.show = True
    chart.options.plotOptions.radialBar.dataLabels.value.offsetY = 0
    chart.options.plotOptions.radialBar.dataLabels.value.fontSize = self.page.body.style.globals.font.header
    chart.options.plotOptions.radialBar.dataLabels.value.formatters.toPercent()
    chart.style.css.margin_top = 0
    return chart
