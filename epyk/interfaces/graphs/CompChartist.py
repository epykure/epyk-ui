from epyk.core.py import types
from epyk.core.html import graph
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html


class Chartist:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Chartist"

  def line(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs):
    """
    Display a line chart from ApexCharts.

    :tags:
    :categories:

    Usage::

      chart = page.ui.charts.chartist.line()

    Related Pages:

      https://naver.github.io/billboard.js/demo/#Chart.LineChart

    :param record: The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    chart = graph.GraphChartist.Chart(self.page, width, height, html_code, dfl_options, profile)
    #chart.colors(self.page.theme.charts)
    #chart.options.xaxis.categories = data['labels']
    #for i, d in enumerate(data['datasets']):
    #  series = chart.options.add_series()
    #  series.name = d["label"]
    #  series.data = d["data"]
    #chart.options.chart.type = "line"
    return chart