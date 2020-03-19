
import datetime

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

  def hbar(self, record=None, y_columns=None, x_axis=None, title=None, profile=None, options=None,
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

    bar_chart = graph.GraphNVD3.ChartHorizontalBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                                   None, profile)
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

  def gauge(self, value, text=None, title=None, total=100, profile=None, options=None,
          width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/pie.html

    :param text:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:

    """
    if total != 100:
      value = value / total * 100
      total = 100
    pie_chart = graph.GraphNVD3.ChartPie(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, None, profile)
    self.parent.context.register(pie_chart)
    pie_chart.dom.x(column="x").y(column="y").donut(True).title(text or "%s%%" % value)
    pie_chart.dom.arcsRadius([
      {"inner": 0.7, "outer": 1},
      {"inner": 0.9, "outer": 1},
    ])

    pie_chart.add_trace([
      {"x": '', "y": value},
      {"x": '', "y": total - value},
    ])
    return pie_chart

  def parallel_coordinates(self, records, dimensions=None, title=None, profile=None, options=None,
                      width=(100, "%"), height=(330, "px"), htmlCode=None):

    chart = graph.GraphNVD3.ChartParallelCoord(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                         None, profile)
    chart.set_dimension_names(dimensions)
    chart.add_trace(records)
    self.parent.context.register(chart)
    return chart

  def sunburst(self, records, name, title=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    :param records:
    :param title:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    chart = graph.GraphNVD3.ChartSunbrust(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, None, profile)
    chart.add_trace(records, name=name)
    self.parent.context.register(chart)
    return chart

  def candlestick(self, records, closes, highs, lows, opens, x_axis, title=None, profile=None,
                  options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):

    """

    data = rptObj.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
    sc = rptObj.ui.charts.nvd3.candlestick(data, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"], opens=["AAPL.Open"], x_axis='Date')

    :param records:
    :param closes:
    :param highs:
    :param lows:
    :param opens:
    :param x_axis:
    :param title:
    :param filters:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    :return:
    """
    all_series = []
    js_date_start = datetime.datetime(1970, 1, 1)
    for i, c in enumerate(closes):
      data_set = []
      for rec in records:
        dt = datetime.datetime.strptime(rec[x_axis], "%Y-%m-%d") - js_date_start
        data_set.append({'date': dt.days, 'close': float(rec[c]), 'high': float(rec[highs[i]]), 'low': float(rec[lows[i]]), 'open': float(rec[opens[i]])})
      all_series.append(data_set)

    candle_chart = graph.GraphNVD3.ChartCandlestick(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                         None, profile)
    candle_chart.dom.x(column='date').y(column='close')
    candle_chart.dom.xAxis.tickDateFormat()
    self.parent.context.register(candle_chart)
    for s in all_series:
      candle_chart.add_trace(s)
    return candle_chart

  def ohlc(self, records, closes, highs, lows, opens, x_axis, title=None, profile=None,
                  options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):

    all_series = []
    js_date_start = datetime.datetime(1970, 1, 1)
    for i, c in enumerate(closes):
      data_set = []
      for rec in records:
        dt = datetime.datetime.strptime(rec[x_axis], "%Y-%m-%d") - js_date_start
        data_set.append(
          {'date': dt.days, 'close': float(rec[c]), 'high': float(rec[highs[i]]), 'low': float(rec[lows[i]]),
           'open': float(rec[opens[i]])})
      all_series.append(data_set)

    ohlc_chart = graph.GraphNVD3.ChartOhlcBar(self.parent.context.rptObj, width, height, title, options or {},
                                                    htmlCode, None, profile)
    ohlc_chart.dom.x(column='date').y(column='close')
    ohlc_chart.dom.xAxis.tickDateFormat()
    self.parent.context.register(ohlc_chart)
    for s in all_series:
      ohlc_chart.add_trace(s)
    return ohlc_chart

  def group_box(self, title="", profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    :param title:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    box_chart = graph.GraphNVD3.ChartBoxPlot(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, None, profile)
    box_chart.dom.q1('q1').q2('median').q3('q3').wh('maxRegularValue').wl('minRegularValue').outliers('outliers').staggerLabels(True)
    box_chart.dom.itemColor("seriesColor").x('title')
    self.parent.context.register(box_chart)
    return box_chart

  def forceDirected(self, title="", profile=None, options=None, width=(400, "px"), height=(330, "px"), htmlCode=None):
    """

    :param title:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    force_chart = graph.GraphNVD3.ChartForceDirected(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, None, profile)
    force_chart.dom.width(width[0]).height(height[0]).nodeExtras("name").color('color')
    self.parent.context.register(force_chart)
    return force_chart
