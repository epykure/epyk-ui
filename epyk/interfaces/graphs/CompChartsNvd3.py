"""

"""

from epyk.core.html import graph


class Nvd3(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "NVD3"

  def line(self, data=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
           width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/line.html

    :param data:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    line_chart = graph.GraphNVD3.ChartLine(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(line_chart)
    line_chart._data = self.parent.context.rptObj.js.data.records(data).to.nvd3.line(y_columns, x_axis, profile or False)
    return line_chart

  def bar(self, data=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
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
    bar_chart = graph.GraphNVD3.ChartBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    if len(y_columns) > 1:
      # Change automatically the underlying chart object to add a multibars chart
      bar_chart.chart._selector = "nv.models.multiBarChart()"
    self.parent.context.register(bar_chart)
    bar_chart._data = self.parent.context.rptObj.js.data.records(data).to.nvd3.bar(y_columns, x_axis, profile or False)
    return bar_chart

  def pie(self, data=None, y_column=None, x_axis=None, title=None, filters=None, profile=None, options=None,
          width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/pie.html

    :param data:
    :param y_column:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:

    """
    pie_chart = graph.GraphNVD3.ChartPie(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(pie_chart)
    pie_chart._data = self.parent.context.rptObj.js.data.records(data).to.nvd3.pie(y_column, x_axis, profile or False)
    return pie_chart
