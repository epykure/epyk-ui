#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import graph


class ApexChart(object):

  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Apex"

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a line chart from Billboard

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    #data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    chart = graph.GraphApexCharts.Chart(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.chart.type = "line"
    return chart

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a line chart from Billboard

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    #data = self.parent.context.rptObj.data.bb.y(record or [], y_columns, x_axis)
    chart = graph.GraphApexCharts.Chart(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.chart.type = "scatter"
    return chart

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a line chart from Billboard

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    chart = graph.GraphApexCharts.Bar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.chart.type = "bar"
    return chart

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a line chart from Billboard

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    chart = graph.GraphApexCharts.Bar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.chart.type = "bar"
    chart.options.plotOptions.bar.horizontal = True
    return chart

  def area(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a line chart from Billboard

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    chart = graph.GraphApexCharts.Area(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    chart.options.chart.type = "area"
    return chart
