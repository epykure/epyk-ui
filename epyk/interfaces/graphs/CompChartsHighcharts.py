from epyk.core.py import types
from epyk.core.html import graph
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html


class Highcharts:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Highcharts"

  def plot(self, record: list = None, y: list = None, x: str = None, kind: str = "line",
           profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
           height: types.SIZE_TYPE = (330, "px"), options: dict = None,
           html_code: str = None, **kwargs
           ) -> graph.GraphChartJs.Chart:
    """Generic way to define ChartJs charts.

    :tags:
    :categories:

    `ChartJs <https://www.chartjs.org/>`_

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
    if hasattr(self, kind):
      return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                                 options=options, html_code=html_code)

    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": [], "chart": {"type": kind}, "title": {"text": ""}}
    dfl_options.update({'y_columns': y or [], 'x_axis': x, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y, x)
    chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    return chart

  def line(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": [], "chart": {"type": "line"}, "title": {"text": ""}}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    #chart.colors(self.page.theme.charts)
    #chart.options.xaxis.categories = data['labels']
    #for i, d in enumerate(data['datasets']):
    #  series = chart.options.add_series()
    #  series.name = d["label"]
    #  series.data = d["data"]
    #chart.options.chart.type = "line"
    return chart

  def bar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": [], "chart": {"type": "column"}, "title": {"text": ""}}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    return chart

  def hbar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": [], "chart": {"type": "bar"}, "title": {"text": ""}}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    return chart

  def area(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": [], "chart": {"type": "area"}, "title": {"text": ""}}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    return chart

  def pie(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": [], "chart": {"type": "pie"}, "title": {"text": ""}}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    return chart

  def donut(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": [], "chart": {"type": "pie"}, "title": {"text": ""}}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.plotOptions.pie.innerSize = 50
    return chart

  def gauge(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": [], "chart": {"type": "pie"}, "title": {"text": ""}}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    chart.colors(self.page.theme.charts)
    chart.options.plotOptions.pie.dataLabels.enabled = True
    chart.options.plotOptions.pie.dataLabels.distance = -50
    chart.options.plotOptions.pie.startAngle = -90
    chart.options.plotOptions.pie.endAngle = 90
    chart.options.plotOptions.pie.center = ['50%', '75%']
    return chart