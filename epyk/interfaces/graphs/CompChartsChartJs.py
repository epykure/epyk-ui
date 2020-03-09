
import sys

from epyk.core.html import graph
from epyk.core.js.Imports import requires


class ChartJs(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "ChartJs"

  def line(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    Documentation
    http://www.chartjs.org/

    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
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

    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(sorted(list(labels)))
    for d in data:
      line_chart.add_dataset(d)

    self.parent.context.register(line_chart)
    return line_chart

  def pie(self, record=None, y_column=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param record:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      agg_data[rec[x_axis]] = agg_data.get(rec[x_axis],  0) + float(rec[y_column])
    labels, data = [], []
    for x, y in agg_data.items():
      labels.append(x)
      data.append(y)

    line_chart = graph.GraphChartJs.ChartPie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.add_dataset(data)
    line_chart.labels(labels)
    self.parent.context.register(line_chart)
    return line_chart

  def donut(self, record=None, y_column=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param record:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      agg_data[rec[x_axis]] = agg_data.get(rec[x_axis],  0) + float(rec[y_column])
    labels, data = [], []
    for x, y in agg_data.items():
      labels.append(x)
      data.append(y)

    dflt_options = {'cutoutPercentage': 50}
    if options is not None:
      dflt_options.update()
    pie_chart = graph.GraphChartJs.ChartPie(self.parent.context.rptObj, width, height, htmlCode, dflt_options, profile)
    pie_chart.add_dataset(data)
    pie_chart.labels(labels)

    self.parent.context.register(pie_chart)
    return pie_chart

  def area(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

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

    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(sorted(list(labels)))
    for d in data:
      line_chart.add_dataset(d, opacity=0.2)
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

    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(sorted(list(labels)))
    for d in data:
      line_chart.add_dataset(d)
      line_chart.dataset().steppedLine = 'before'
    self.parent.context.register(line_chart)
    return line_chart

  def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param record:
    :param y_column:
    :param x_axis:
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

    bar_chart = graph.GraphChartJs.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bar_chart.labels(sorted(list(labels)))
    for d in data:
      bar_chart.add_dataset(d)
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
        series.append({"x": y, "y": x})
      data.append(series)

    bar_chart = graph.GraphChartJs.ChartHBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bar_chart.labels(sorted(list(labels)))
    for d in data:
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
    bar_chart = graph.GraphChartJs.ChartBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                              filters, profile)
    bar_chart.chart._data = self.parent.context.rptObj.js.data.records(data).to.chartJs.line(y_columns, x_axis, profile or False)
    self.parent.context.register(bar_chart)
    return bar_chart

  def scatter(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

    :param record:
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

    line_chart = graph.GraphChartJs.ChartScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(sorted(list(labels)))
    for d in data:
      line_chart.add_dataset(d)
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
    agg_data, agg_r = {}, {}
    for rec in record:
      for i, y in enumerate(y_columns):
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis],  0) + float(rec[y])
        if r_values is not None and i < len(r_values):
          agg_r.setdefault(y, {})[rec[x_axis]] = agg_r.get(y, {}).get(rec[x_axis],  0) + float(rec[r_values[i]])
    labels, data = set(), []
    for c in y_columns:
      series = []
      for x, y in agg_data[c].items():
        labels.add(x)
        series.append({"x": x, "y": y, 'r': agg_r.get(c, {}).get(x, 1)})
      data.append(series)

    line_chart = graph.GraphChartJs.ChartBubble(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(sorted(list(labels)))
    for d in data:
      line_chart.add_dataset(d)
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

    polar_chart = graph.GraphChartJs.ChartPolar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    polar_chart.labels(sorted(list(labels)))
    for d in data:
      polar_chart.add_dataset(d)
    self.parent.context.register(polar_chart)
    return polar_chart

  def radar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """

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
        series.append(y)
      data.append(series)

    radar_chart = graph.GraphChartJs.ChartRadar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    radar_chart.labels(sorted(list(labels)))
    for d in data:
      radar_chart.add_dataset(d)
    self.parent.context.register(radar_chart)
    return radar_chart

  def kde(self, aresDf=None, seriesNames=None, otherDims=None, dataFncs=None, title='',
            globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
            width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    """

    Specific options to the chartOptions
      - step      : The number of step used in the gaussian_kde function
      - chartType : The type of display for the result

    :param aresDf:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param title:
    :param globalFilter:
    :param filterSensitive:
    :param profile:
    :param dataSrc:
    :param xAxisOrder:
    :param chartOptions:
    :param width:
    :param widthUnit:
    :param height:
    :param heightUnit:
    :param htmlCode:
    :return: The Python Chart object
    :rtype: graph.GraphChartJs.Chart
    """

    # Those two packages are required for this type of chart
    ares_numpy = requires("numpy", reason='Missing Package', install='numpy', autoImport=True, sourceScript=__file__)
    ares_scipy_stats = requires(name='scipy.stats', reason='Missing Package', install='scipy', autoImport=True, sourceScript=__file__)

    step, chartType = 500, 'line'
    if chartOptions is not None and "step" in chartOptions:
      step = chartOptions["step"]
      del chartOptions["step"]

    if chartOptions is not None and "chartType" in chartOptions:
      chartType = chartOptions["chartType"]
      del chartOptions["chartType"]

    kdeSeries = {}
    for series in seriesNames:
      x = ares_numpy.linspace(min(aresDf[series]), max(aresDf[series]), step)
      kdeSeries[series] = ares_scipy_stats.gaussian_kde(list(aresDf[series]))(x)

    newDff = []
    for i in range(step):
      row = {'x': i}
      for series in seriesNames:
        row[series] = kdeSeries[series][i]
      newDff.append(row)

    return self.parent.context.chart(chartType=chartType, aresDf=newDff, seriesNames=seriesNames,
                                     xAxis="x", otherDims=otherDims, dataFncs=dataFncs, title=title,
                                     chartFamily=self.chartFamily, dataSrc=dataSrc,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)

