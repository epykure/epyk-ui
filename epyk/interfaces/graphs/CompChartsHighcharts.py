from epyk.core.py import types
from epyk.core.html import graph
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html


class Highcharts:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Highcharts"

  def line(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphHighcharts.Chart:
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphHighcharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    #chart.colors(self.page.theme.charts)
    #chart.options.xaxis.categories = data['labels']
    #for i, d in enumerate(data['datasets']):
    #  series = chart.options.add_series()
    #  series.name = d["label"]
    #  series.data = d["data"]
    #chart.options.chart.type = "line"
    return chart
