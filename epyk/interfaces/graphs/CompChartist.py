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
    if record:
      chart.options._config(data["labels"], name="labels")
      recordsets = []
      for d in data['datasets']:
        recordsets.append({"name": d["label"], "data": d["data"]})
      chart.options._config(recordsets, name="series")
    return chart

  def bar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphChartist.Chart:
    """

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
    chart = graph.GraphChartist.ChartBar(self.page, width, height, html_code, dfl_options, profile)
    if record:
      chart.options._config(data["labels"], name="labels")
      recordsets = []
      for d in data['datasets']:
        recordsets.append({"name": d["label"], "data": d["data"]})
      chart.options._config(recordsets, name="series")
    return chart

  def hbar(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphChartist.Chart:
    """

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
    chart = graph.GraphChartist.ChartBar(self.page, width, height, html_code, dfl_options, profile)
    chart.options.horizontalBars = True
    if record:
      chart.options._config(data["labels"], name="labels")
      recordsets = []
      for d in data['datasets']:
        recordsets.append({"name": d["label"], "data": d["data"]})
      chart.options._config(recordsets, name="series")
    return chart

  def pie(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphChartist.ChartPie:
    """

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
    chart = graph.GraphChartist.ChartPie(self.page, width, height, html_code, dfl_options, profile)
    if record:
      chart.options._config(data["labels"], name="labels")
      chart.options._config( data['datasets'][0]["data"], name="series")
    return chart

  def donut(self, record=None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
           options: types.OPTION_TYPE = None, html_code: str = None, **kwargs) -> graph.GraphChartist.ChartPie:
    """

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
    chart = graph.GraphChartist.ChartPie(self.page, width, height, html_code, dfl_options, profile)
    chart.options.donut = True
    chart.options.showLabel = True
    if record:
      chart.options._config(data["labels"], name="labels")
      chart.options._config( data['datasets'][0]["data"], name="series")
    return chart
