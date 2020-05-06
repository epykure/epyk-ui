
from epyk.core.html import graph


class C3(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "C3"

  def line(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):

    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).c3.y(y_columns, x_axis)
    line_chart = graph.GraphC3.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def spline(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).c3.y(y_columns, x_axis)
    line_chart = graph.GraphC3.ChartSpline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def step(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).c3.y(y_columns, x_axis)
    line_chart = graph.GraphC3.ChartSpline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = 'step'
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def area(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).c3.y(y_columns, x_axis)
    line_chart = graph.GraphC3.ChartArea(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def area_step(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).c3.y(y_columns, x_axis)
    line_chart = graph.GraphC3.ChartArea(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = "area-step"
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def timeseries(self, record, y_columns=None, x_axis=None, profile=None, options=None,
                 width=(100, "%"), height=(330, "px"), htmlCode=None):
    line = self.line(record, y_columns, x_axis, profile, options, width, height, htmlCode)
    line.axis.x.type = "timeseries"
    line.axis.x.tick.format = "%Y-%m-%d"
    return line

  def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).c3.y(y_columns, x_axis)
    line_chart = graph.GraphC3.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def hbar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    https://c3js.org/samples/axes_rotated.html

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
    data = self.parent.context.rptObj.data.js(record).c3.y(y_columns, x_axis)
    line_chart = graph.GraphC3.ChartScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(data['series'][i], d)
    self.parent.context.register(line_chart)
    return line_chart

  def pie(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    https://c3js.org/samples/chart_pie.html

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
    data = self.parent.context.rptObj.data.js(record).c3.y(y_columns, x_axis)
    pie_chart = graph.GraphC3.ChartPie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    pie_chart.labels(data['labels'])
    pie_chart.add_dataset(data['series'][0], data['labels'])
    self.parent.context.register(pie_chart)
    return pie_chart

  def donut(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.js(record).c3.y(y_columns, x_axis)
    pie_chart = graph.GraphC3.ChartDonut(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    pie_chart.labels(data['labels'])
    pie_chart.add_dataset(data['series'][0], data['labels'])
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
    g_chart = graph.GraphC3.ChartGauge(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    g_chart.add_dataset(text, value)
    self.parent.context.register(g_chart)
    return g_chart

  def stanford(self, record, y_columns=None, x_axis=None, epoch_col=None, title=None, profile=None, width=(100, "%"),
               height=(330, "px"), options=None, htmlCode=None):
    """

    :param record:
    :param y_columns:
    :param x_axis:
    :param epoch_col:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    epoch, labels, series = [], [], []
    for rec in record:
      epoch.append(rec[epoch_col])
      labels.append(rec[x_axis])
      series.append([rec.get(c)for c in y_columns])

    line_chart = graph.GraphC3.ChartStanford(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(labels)
    line_chart.epoch(epoch, epoch_col)
    for i, y in enumerate(y_columns):
      line_chart.add_dataset(y, series[i])
    self.parent.context.register(line_chart)
    return line_chart
