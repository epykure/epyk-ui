
from epyk.core.html import graph
from epyk.core.js.packages import JsNvd3


class Nvd3(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "NVD3"

  def scatter(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
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

    line_chart = graph.GraphNVD3.ChartScatter(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    for i, d in enumerate(data):
      line_chart.add_trace(d, y_columns[i])
    self.parent.context.register(line_chart)
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

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

  def line_cumulative(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
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

    line_chart = graph.GraphNVD3.ChartCumulativeLine(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    line_chart.dom.useInteractiveGuideline(True)
    for i, d in enumerate(data):
      line_chart.add_trace(d, y_columns[i])
    self.parent.context.register(line_chart)
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def line_focus(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
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

    line_chart = graph.GraphNVD3.ChartFocusLine(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    line_chart.dom.useInteractiveGuideline(True)
    for i, d in enumerate(data):
      line_chart.add_trace(d, y_columns[i])
    self.parent.context.register(line_chart)
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
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
        series.append({"label": x, "y": y})
      data.append(series)

    bar_chart = graph.GraphNVD3.ChartBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    if y_columns is not None and len(y_columns) > 1:
      # Change automatically the underlying chart object to add a multibars chart
      bar_chart.dom._selector = "nv.models.multiBarChart()"
    self.parent.context.register(bar_chart)
    bar_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data):
      bar_chart.add_trace(d, y_columns[i])
    return bar_chart

  def multi(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
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
        series.append({"label": x, "y": y})
      data.append(series)

    bar_chart = graph.GraphNVD3.ChartBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    if y_columns is not None and len(y_columns) > 1:
      # Change automatically the underlying chart object to add a multibars chart
      bar_chart.dom._selector = "nv.models.multiBarChart()"
    self.parent.context.register(bar_chart)
    bar_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data):
      bar_chart.add_trace(d, y_columns[i])
    return bar_chart

  def histo(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
            width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/discreteBar.html

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
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])

    labels, data = set(), []
    for c in y_columns:
      series = []
      for x, y in agg_data[c].items():
        labels.add(x)
        series.append({"label": x, "y": y})
      data.append(series)

    histo_chart = graph.GraphNVD3.ChartHistoBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    histo_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data):
      histo_chart.add_trace(d, y_columns[i])
    self.parent.context.register(histo_chart)
    return histo_chart

  def timeseries(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
            width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/discreteBar.html

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
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])

    labels, data = set(), []
    for c in y_columns:
      series = []
      for x, y in agg_data[c].items():
        labels.add(x)
        series.append({"label": x, "y": y})
      data.append(series)

    histo_chart = graph.GraphNVD3.ChartHistoBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    histo_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data):
      histo_chart.add_trace(d, y_columns[i])
    self.parent.context.register(histo_chart)
    return histo_chart

  def area(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
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
        series.append({"label": x, "y": y})
      data.append(series)

    area_chart = graph.GraphNVD3.ChartArea(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    for i, d in enumerate(data):
      area_chart.add_trace(d, y_columns[i])
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

  def donut(self, record=None, y_column=None, x_axis=None, title=None, filters=None, profile=None, options=None,
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
    pie_chart.dom.x(column="x").y(column="y").donut(True)
    pie_chart.add_trace(series, y_column)
    return pie_chart

  def gauge(self, record=None, y_column=None, x_axis=None, text='', title=None, filters=None, profile=None, options=None,
          width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/pie.html

    :param record:
    :param y_column:
    :param x_axis:
    :param text:
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
    pie_chart.dom.x(column="x").y(column="y").donut(True).title(text)
    pie_chart.add_trace(series, y_column)
    return pie_chart
