
from epyk.core.html import graph


class ChartJs(object):

  def __init__(self, context):
    self.parent = context
    self.chartFamily = "ChartJs"

  def line(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    Documentation
    http://www.chartjs.org/

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).chartjs.y(y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(line_chart)
    return line_chart

  def timeseries(self, record, y_columns=None, x_axis=None, title=None, profile=None, options=None,
                 width=(100, "%"), height=(330, "px"), htmlCode=None):
    line = self.line(record, y_columns, x_axis, profile, width, height, options, htmlCode)
    return line

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param record:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).chartjs.y(y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartPie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(line_chart)
    return line_chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param record:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    data = self.parent.context.rptObj.data.js(record).chartjs.y(y_columns, x_axis)
    dflt_options = {'cutoutPercentage': 50, 'y_columns': y_columns, 'x_column': x_axis}
    if options is not None:
      dflt_options.update()
    pie_chart = graph.GraphChartJs.ChartPie(self.parent.context.rptObj, width, height, htmlCode, dflt_options, profile)
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(pie_chart)
    return pie_chart

  def area(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).chartjs.y(y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i], opacity=0.2)
      line_chart.dataset().fill = True
    self.parent.context.register(line_chart)
    return line_chart

  def step(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    data = self.parent.context.rptObj.data.js(record).chartjs.y(y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
      line_chart.dataset().steppedLine = 'before'
    self.parent.context.register(line_chart)
    return line_chart

  def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param record: Array.
    :param y_column: String.
    :param x_axis: String.
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).chartjs.y(y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bar_chart.labels(data['labels'])
    for d in data['datasets']:
      bar_chart.add_dataset(d)
    bar_chart.options.scales.y_axis().ticks.beginAtZero = True
    self.parent.context.register(bar_chart)
    return bar_chart

  def hbar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param record:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).chartjs.y(y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartHBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bar_chart.labels(data['labels'])
    for d in data['datasets']:
      bar_chart.add_dataset(d)
    self.parent.context.register(bar_chart)
    return bar_chart

  def multi(self, data=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
           width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    bar_chart = graph.GraphChartJs.ChartBar(self.parent.context.rptObj, width, height, title, options, htmlCode, filters, profile)
    bar_chart.chart._data = self.parent.context.rptObj.js.data.records(data).to.chartJs.line(y_columns, x_axis, profile or False)
    self.parent.context.register(bar_chart)
    return bar_chart

  def scatter(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------

    Attributes:
    ----------

    :param record:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).chartjs.xy(y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(line_chart)
    return line_chart

  def bubble(self, record, y_columns=None, x_axis=None, r_values=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'z_columns': r_values})
    data = self.parent.context.rptObj.data.js(record).chartjs.xyz(y_columns, x_axis, r_values)
    line_chart = graph.GraphChartJs.ChartBubble(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(line_chart)
    return line_chart

  def polar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).chartjs.y(y_columns, x_axis)
    polar_chart = graph.GraphChartJs.ChartPolar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    polar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      polar_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(polar_chart)
    return polar_chart

  def radar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    A radar chart is a way of showing multiple data points and the variation between them.

    https://www.chartjs.org/docs/latest/charts/radar.html

    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """

    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).chartjs.y(y_columns, x_axis)
    radar_chart = graph.GraphChartJs.ChartRadar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    radar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      radar_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(radar_chart)
    return radar_chart
