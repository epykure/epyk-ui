
import datetime

from epyk.core.html import graph


class Nvd3(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "NVD3"

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a scatter chart from NVD3

    Related Pages:

			http://nvd3.org/examples/line.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.xy(record, y_columns, x_axis)
    line_chart = graph.GraphNVD3.ChartScatter(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a line chart from NVD3

    Related Pages:

			http://nvd3.org/examples/line.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.xy(record, y_columns, x_axis)
    line_chart = graph.GraphNVD3.ChartLine(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    line_chart.dom.useInteractiveGuideline(True)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def line_cumulative(self, record=None, y_columns=None, x_axis=None, profile=None, options=None,  width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a Cumulative line chart from NVD3

    Related Pages:

			http://nvd3.org/examples/line.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.xy(record, y_columns, x_axis)
    line_chart = graph.GraphNVD3.ChartCumulativeLine(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    line_chart.dom.useInteractiveGuideline(True)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def line_focus(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a line chart with focus from NVD3

    Related Pages:

			http://nvd3.org/examples/line.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.xy(record, y_columns, x_axis)
    line_chart = graph.GraphNVD3.ChartFocusLine(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    line_chart.dom.useInteractiveGuideline(True)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d, data['labels'][i])
    line_chart.dom.x(column="x").y(column="y")
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a bars chart from NVD3

    Related Pages:

			http://nvd3.org/examples/discreteBar.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.labely(record, y_columns, x_axis)
    bar_chart = graph.GraphNVD3.ChartBar(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    if y_columns is not None and len(y_columns) > 1:
      # Change automatically the underlying chart object to add a multibars chart
      bar_chart.dom._selector = "nv.models.multiBarChart()"
    bar_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data['datasets']):
      bar_chart.add_trace(d, data['labels'][i])
    return bar_chart

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a bars chart from NVD3

    Related Pages:

			http://nvd3.org/examples/discreteBar.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:

    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.labely(record, y_columns, x_axis)
    bar_chart = graph.GraphNVD3.ChartHorizontalBar(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    bar_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data['datasets']):
      bar_chart.add_trace(d, data['labels'][i])
    return bar_chart

  def multi(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a multi types chart from NVD3

    Related Pages:

			http://nvd3.org/examples/discreteBar.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:

    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.labely(record, y_columns, x_axis)
    bar_chart = graph.GraphNVD3.ChartBar(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    if y_columns is not None and len(y_columns) > 1:
      # Change automatically the underlying chart object to add a multibars chart
      bar_chart.dom._selector = "nv.models.multiBarChart()"
    bar_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data['datasets']):
      bar_chart.add_trace(d, data['labels'][i])
    return bar_chart

  def histo(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a histo chart from NVD3

    Related Pages:

			http://nvd3.org/examples/discreteBar.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.labely(record, y_columns, x_axis)
    histo_chart = graph.GraphNVD3.ChartHistoBar(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    histo_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data['datasets']):
      histo_chart.add_trace(d, data['labels'][i])
    return histo_chart

  def timeseries(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a Timseries chart from NVD3

    Related Pages:

			http://nvd3.org/examples/discreteBar.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param x_axis:
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:

    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.labely(record, y_columns, x_axis)
    histo_chart = graph.GraphNVD3.ChartHistoBar(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    histo_chart.dom.x(column="label").y(column="y")
    for i, d in enumerate(data['datasets']):
      histo_chart.add_trace(d, data['labels'][i])
    return histo_chart

  def area(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a area chart from NVD3

    Related Pages:

			http://nvd3.org/examples/discreteBar.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.labely(record, y_columns, x_axis)
    area_chart = graph.GraphNVD3.ChartArea(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    for i, d in enumerate(data['datasets']):
      area_chart.add_trace(d, data['labels'][i])
    area_chart.dom.x(column="label").y(column="y")
    return area_chart

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a pie chart from NVD3

    Related Pages:

			http://nvd3.org/examples/pie.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.xy(record, y_columns, x_axis)
    pie_chart = graph.GraphNVD3.ChartPie(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    pie_chart.dom.x(column="x").y(column="y")
    for i, d in enumerate(data['datasets']):
      pie_chart.add_trace(d, data['labels'][i])
    return pie_chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a donut chart from NVD3

    Related Pages:

			http://nvd3.org/examples/pie.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis})
    data = self.parent.context.rptObj.data.nvd3.xy(record, y_columns, x_axis)
    pie_chart = graph.GraphNVD3.ChartPie(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    pie_chart.dom.x(column="x").y(column="y").donut(True)
    for i, d in enumerate(data['datasets']):
      pie_chart.add_trace(d, data['labels'][i])
    return pie_chart

  def gauge(self, value, text=None, total=100, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

			http://nvd3.org/examples/pie.html

    :param text:
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:

    """
    if total != 100:
      value = value / total * 100
      total = 100
    pie_chart = graph.GraphNVD3.ChartPie(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
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

  def parallel_coordinates(self, records, dimensions=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    :param records:
    :param dimensions:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    chart = graph.GraphNVD3.ChartParallelCoord(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    chart.set_dimension_names(dimensions)
    chart.add_trace(records)
    return chart

  def sunburst(self, records, name, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    :param records:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    #options.update({'y_columns': y_columns, 'x_column': name})
    chart = graph.GraphNVD3.ChartSunbrust(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    chart.add_trace(records, name=name)
    return chart

  def candlestick(self, records, closes, highs, lows, opens, x_axis, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    data = rptObj.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
    sc = rptObj.ui.charts.nvd3.candlestick(data, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"], opens=["AAPL.Open"], x_axis='Date')

    :param records:
    :param closes:
    :param highs:
    :param lows:
    :param opens:
    :param x_axis:
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

    candle_chart = graph.GraphNVD3.ChartCandlestick(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    candle_chart.dom.x(column='date').y(column='close')
    candle_chart.dom.xAxis.tickDateFormat()
    for s in all_series:
      candle_chart.add_trace(s)
    return candle_chart

  def ohlc(self, records, closes, highs, lows, opens, x_axis, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    :param records:
    :param closes:
    :param highs:
    :param lows:
    :param opens:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
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
    ohlc_chart = graph.GraphNVD3.ChartOhlcBar(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    ohlc_chart.dom.x(column='date').y(column='close')
    ohlc_chart.dom.xAxis.tickDateFormat()
    for s in all_series:
      ohlc_chart.add_trace(s)
    return ohlc_chart

  def group_box(self, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    box_chart = graph.GraphNVD3.ChartBoxPlot(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    box_chart.dom.q1('q1').q2('median').q3('q3').wh('maxRegularValue').wl('minRegularValue').outliers('outliers').staggerLabels(True)
    box_chart.dom.itemColor("seriesColor").x('title')
    return box_chart

  def forceDirected(self, profile=None, options=None, width=(400, "px"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    force_chart = graph.GraphNVD3.ChartForceDirected(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    force_chart.dom.width(width[0]).height(height[0]).nodeExtras("name").color('color')
    return force_chart
