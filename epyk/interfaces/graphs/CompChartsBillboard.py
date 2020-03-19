
from epyk.core.html import graph


class Billboard(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "C3"

  def line(self, record, y_columns=None, x_axis=None, title=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
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
        series.append(y)
      data.append(series)

    line_chart = graph.GraphBillboard.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(sorted(list(labels)))
    for i, y in enumerate(y_columns):
      line_chart.add_dataset(y, data[i])
    self.parent.context.register(line_chart)
    return line_chart

  def line_range(self, record, y_columns=None, x_axis=None, range=5, title=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
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
        series.append([y+range, y, y-range])
      data.append(series)

    line_chart = graph.GraphBillboard.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = "area-line-range"
    line_chart.labels(sorted(list(labels)))
    for i, y in enumerate(y_columns):
      line_chart.add_dataset(y, data[i])
    self.parent.context.register(line_chart)
    return line_chart

  def bubble(self, record, y_columns=None, x_axis=None, title=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
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
        series.append(y)
      data.append(series)

    bubble_chart = graph.GraphBillboard.ChartBubble(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bubble_chart.labels(sorted(list(labels)))
    for i, y in enumerate(y_columns):
      bubble_chart.add_dataset(y, data[i])
      bubble_chart.data.labels = True
    self.parent.context.register(bubble_chart)
    return bubble_chart

  def radar(self, record, y_columns=None, x_axis=None, title=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
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
        series.append(y)
      data.append(series)

    radar_chart = graph.GraphBillboard.ChartRadar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    radar_chart.labels(sorted(list(labels)))
    for i, y in enumerate(y_columns):
      radar_chart.add_dataset(y, data[i])
      radar_chart.data.labels = True
    self.parent.context.register(radar_chart)
    return radar_chart

  def spline(self, record, y_columns=None, x_axis=None, title=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
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
        series.append(y)
      data.append(series)

    line_chart = graph.GraphBillboard.ChartSpline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(sorted(list(labels)))
    for i, y in enumerate(y_columns):
      line_chart.add_dataset(y, data[i])
    self.parent.context.register(line_chart)
    return line_chart

  def step(self, record, y_columns=None, x_axis=None, title=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
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
        series.append(y)
      data.append(series)

    line_chart = graph.GraphBillboard.ChartSpline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = 'step'
    line_chart.labels(sorted(list(labels)))
    for i, y in enumerate(y_columns):
      line_chart.add_dataset(y, data[i])
    self.parent.context.register(line_chart)
    return line_chart

  def area(self, record, y_columns=None, x_axis=None, title=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
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
        series.append(y)
      data.append(series)

    line_chart = graph.GraphBillboard.ChartArea(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(sorted(list(labels)))
    for i, y in enumerate(y_columns):
      line_chart.add_dataset(y, data[i])
    self.parent.context.register(line_chart)
    return line_chart

  def area_step(self, record, y_columns=None, x_axis=None, title=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
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
        series.append(y)
      data.append(series)

    line_chart = graph.GraphBillboard.ChartArea(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart._type = "area-step"
    line_chart.labels(sorted(list(labels)))
    for i, y in enumerate(y_columns):
      line_chart.add_dataset(y, data[i])
    self.parent.context.register(line_chart)
    return line_chart

  def timeseries(self, record, y_columns=None, x_axis=None, title=None, profile=None, options=None,
                 width=(100, "%"), height=(330, "px"), htmlCode=None):
    line = self.line(record, y_columns, x_axis, title, profile, options, width, height, htmlCode)
    line.axis.x.type = "timeseries"
    line.axis.x.tick.format = "%Y-%m-%d"
    return line

  def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    labels, data = set(), []
    for c in y_columns:
      series = []
      for x, y in agg_data[c].items():
        labels.add(x)
        series.append(y)
      data.append(series)

    line_chart = graph.GraphBillboard.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(sorted(list(labels)))
    for i, y in enumerate(y_columns):
      line_chart.add_dataset(y, data[i])
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
        series.append(y)
      data.append(series)

    line_chart = graph.GraphBillboard.ChartScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(sorted(list(labels)))
    for i, y in enumerate(y_columns):
      line_chart.add_dataset(y, data[i])
    self.parent.context.register(line_chart)
    return line_chart

  def pie(self, record, y_column=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param record:
    :param y_column:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      if y_column in rec:
        agg_data[rec[x_axis]] = agg_data.get(rec[x_axis],  0) + float(rec[y_column])

    pie_chart = graph.GraphBillboard.ChartPie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    for k, value in agg_data.items():
      pie_chart.add_dataset(k, value)
    self.parent.context.register(pie_chart)
    return pie_chart

  def donut(self, record, y_column=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    agg_data = {}
    for rec in record:
      if y_column in rec:
        agg_data[rec[x_axis]] = agg_data.get(rec[x_axis],  0) + float(rec[y_column])

    pie_chart = graph.GraphBillboard.ChartDonut(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    for k, value in agg_data.items():
      pie_chart.add_dataset(k, value)
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
