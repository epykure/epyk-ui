
from epyk.core.html import graph
from epyk.core.js.packages import JsNvd3


class Nvd3(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "NVD3"

  def line(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
           width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/line.html

    :param record:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis],  0) + float(rec[y])

    labels, data = set(), []
    for c in y_columns:
      series = []
      for x, y in agg_data[c].items():
        labels.add(x)
        series.append({"x": x, "y": y})
      data.append(series)

    line_chart = graph.GraphNVD3.ChartLine(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    line_chart.dom.useInteractiveGuideline(True)
    for i, d in enumerate(data):
      line_chart.add_trace(d, y_columns[i])
    self.parent.context.register(line_chart)
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def bar(self, data=None, y_columns=None, x_axis='labels', title=None, filters=None, profile=None, options=None,
          width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/discreteBar.html

    :param data:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:

    """
    if y_columns is None:
      y_columns = ['y']
    bar_chart = graph.GraphNVD3.ChartBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    if y_columns is not None and len(y_columns) > 1:
      # Change automatically the underlying chart object to add a multibars chart
      bar_chart.dom._selector = "nv.models.multiBarChart()"
    self.parent.context.register(bar_chart)
    bar_chart.dom.x(column="label").y(column="y")
    bar_chart._vals = self.parent.context.rptObj.js.data.records(data).to.nvd3.bar(y_columns, x_axis, profile or False)
    return bar_chart

  def histo(self, data=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
            width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/discreteBar.html

    :param data:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:

    """
    bar_chart = graph.GraphNVD3.Chart(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    bar_chart.chart = JsNvd3.JsNvd3Histo(bar_chart._report, varName=bar_chart.chartId)
    bar_chart._data = self.parent.context.rptObj.js.data.records(data).to.nvd3.bar(y_columns, x_axis, profile or False)
    bar_chart.dom.x(column="label").y(column="y")
    self.parent.context.register(bar_chart)
    return bar_chart

  def area(self, data=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
            width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/discreteBar.html

    :param data:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:

    """
    area_chart = graph.GraphNVD3.ChartArea(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    area_chart._vals = self.parent.context.rptObj.js.data.records(data).to.nvd3.bar(y_columns, x_axis, profile or False)
    area_chart.dom.x(column="label").y(column="y")
    self.parent.context.register(area_chart)
    return area_chart

  def pie(self, record=None, y_column=None, x_axis=None, title=None, filters=None, profile=None, options=None,
          width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/pie.html

    :param record:
    :param y_column:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:

    """
    agg_data = {}
    for rec in record:
      if y_column in rec:
        agg_data.setdefault(y_column, {})[rec[x_axis]] = agg_data.get(y_column, {}).get(rec[x_axis],  0) + float(rec[y_column])

    series = []
    for x, y in agg_data[y_column].items():
      series.append({"x": x, "y": y})

    pie_chart = graph.GraphNVD3.ChartPie(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(pie_chart)
    pie_chart.dom.x(column="x").y(column="y")
    pie_chart.add_trace(series, y_column)
    return pie_chart
