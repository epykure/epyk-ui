
from epyk.core.html import graph


class Billboard(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "C3"

  def line(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def line_range(self, record, y_columns=None, x_axis=None, range=5, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = "area-line-range"
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def bubble(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    bubble_chart = graph.GraphBillboard.ChartBubble(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bubble_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      bubble_chart.add_dataset(data['series'][i], d)
      bubble_chart.data.labels = True
    self.parent.context.register(bubble_chart)
    return bubble_chart

  def radar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    radar_chart = graph.GraphBillboard.ChartRadar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    radar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      radar_chart.add_dataset(data['series'][i], d)
      radar_chart.data.labels = True
    self.parent.context.register(radar_chart)
    return radar_chart

  def spline(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartSpline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def step(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartSpline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = 'step'
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def area(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartArea(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def area_step(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartArea(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = "area-step"
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def timeseries(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    line = self.line(record, y_columns, x_axis, profile, options, width, height, htmlCode)
    line.axis.x.type = "timeseries"
    line.axis.x.tick.format = "%Y-%m-%d"
    return line

  def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def hbar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    h_bar = self.bar(record, y_columns, x_axis, profile, width, height, options, htmlCode)
    h_bar.axis.rotated = True
    return h_bar

  def scatter(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    line_chart = graph.GraphBillboard.ChartScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def pie(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    pie_chart = graph.GraphBillboard.ChartPie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(pie_chart)
    return pie_chart

  def donut(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).billboard.y(y_columns, x_axis)
    pie_chart = graph.GraphBillboard.ChartDonut(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(pie_chart)
    return pie_chart

  def gauge(self, value, text="", profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    :param value:
    :param text:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    g_chart = graph.GraphBillboard.ChartGauge(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    g_chart.add_dataset(text, value)
    self.parent.context.register(g_chart)
    return g_chart
