#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import graph
from epyk.core.py import types
from epyk.core.js import JsUtils


class CompChartFrappe:

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
    if y is not None and not isinstance(y, list) and not JsUtils.isJsData(y):
      y = [y]
    return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def line(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphFrappe.Frappe:
    """Create a line chart from Frappe Chart libraries.

    Usage::

      c = page.ui.charts.frappe.line(y_columns=["Value"], x_axis="Year", height=(500, "px"))
      text = page.ui.input("Italy")
      slider = page.ui.sliders.range(minimum=1990, maximum=2020)
      page.ui.button("Click").click([
      page.js.d3.csv(data_urls.DEMO_COUNTRY).filterCol("Country Name", text.dom.content).cast(["Year", "Value"]).
         filterCol("Year", slider.dom.min_select, ">").filterCol("Year", slider.dom.max_select, "<").get(
           [#"data = data.slice(1)",
          c.build(pk.events.data)])
      ])

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.Frappe(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart

  def bar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
          width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
          options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphFrappe.FrappeBar:
    """Create a bar chart from Frappe Chart libraries.

    Usage::

      c = page.ui.charts.frappe.bar(y_columns=["Value"], x_axis="Year", height=(500, "px"))
      text = page.ui.input("Italy")
      slider = page.ui.sliders.range(minimum=1990, maximum=2020)
      page.ui.button("Click").click([
      page.js.d3.csv(data_urls.DEMO_COUNTRY).filterCol("Country Name", text.dom.content).cast(["Year", "Value"]).
         filterCol("Year", slider.dom.min_select, ">").filterCol("Year", slider.dom.max_select, "<").get(
           [#"data = data.slice(1)",
          c.build(pk.events.data)])
      ])

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.FrappeBar(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i], kind='bar')
    return line_chart

  def percentage(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
                 width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
                 options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphFrappe.FrappePercentage:
    """

    Usage::

      c = page.ui.charts.frappe.percentage(y_columns=["Value"], x_axis="Year", height=(500, "px"))
      text = page.ui.input("Italy")
      slider = page.ui.sliders.range(minimum=1990, maximum=2020)
      page.ui.button("Click").click([
        page.js.fetch(data_urls.DEMO_COUNTRY).csvtoRecords().filterCol(
            "Country Name", text.dom.content).cast(["Year", "Value"]).
          filterCol("Year", slider.dom.min_select, ">").filterCol("Year", slider.dom.max_select, "<").
          get([
            c.build(pk.events.data),
        ])
      ])

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.FrappePercentage(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart

  def donut(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
            options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphFrappe.FrappeDonut:
    """


    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.FrappeDonut(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart

  def pie(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
          width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
          options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphFrappe.FrappePie:
    """

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.FrappePie(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart

  def heatmap(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
              options: types.OPTION_TYPE = None, html_code: str = None) -> graph.GraphFrappe.FrappeHeatmap:
    """

    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.FrappeHeatmap(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart
