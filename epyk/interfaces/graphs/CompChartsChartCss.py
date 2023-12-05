#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import graph
from epyk.core.py import types


class CompChartCss:

  def __init__(self, ui):
    self.page = ui.page

  def plot(self, record=None, y=None, x=None, kind: str = "line", profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None):
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

  def line(self, record=None, y_columns=None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphChartCss.ChartCss:
    """

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    line_chart = graph.GraphChartCss.ChartCss(self.page, width, height, html_code, options, profile)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    if len(data["datasets"]) > 1:
      line_chart.options.multiple()
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
          width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
          options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphChartCss.ChartCssBar:
    """

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    line_chart = graph.GraphChartCss.ChartCssBar(self.page, width, height, html_code, options, profile)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart

  def area(self, record=None, y_columns=None, x_axis=None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphChartCss.ChartCssBarArea:
    """

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    line_chart = graph.GraphChartCss.ChartCssBarArea(self.page, width, height, html_code, options, profile)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart

  def stacked(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
              options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphChartCss.ChartCssBarStacked:
    """

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    line_chart = graph.GraphChartCss.ChartCssBarStacked(self.page, width, height, html_code, options, profile)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart
