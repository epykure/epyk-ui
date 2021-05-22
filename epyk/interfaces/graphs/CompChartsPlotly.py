
from epyk.core.html import graph


class Plotly2D:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Plotly"

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plot.ly/javascript/
      https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

    Attributes:
    ----------
    :param record: List. The Python record.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'type': 'line', 'mode': 'lines+markers'})
    data = self.page.data.plotly.xy(record, y_columns, x_axis)
    line_chart = graph.GraphPlotly.Line(self.page, width, height, options or {}, html_code, profile)
    line_chart.options.responsive = True
    line_chart.colors(self.page.theme.charts)
    for d in data['datasets']:
      line_chart.add_trace(d)
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
          height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plotly.com/javascript/bar-charts/

    Attributes:
    ----------
    :param record: List of dict. The Python record.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'type': 'bar', 'mode': None})
    data = self.page.data.plotly.xy(record, y_columns, x_axis)
    bar_chart = graph.GraphPlotly.Bar(self.page, width, height, options, html_code, profile)
    bar_chart.colors(self.page.theme.charts)
    bar_chart.options.responsive = True
    for d in data['datasets']:
      bar_chart.add_trace(d)
    return bar_chart

  def hbar(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"),
           html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plotly.com/javascript/bar-charts/

    Attributes:
    ----------
    :param record: List of dict. The Python record.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'type': 'bar', 'mode': None,
                    'attrs': {'orientation': 'h'}})
    data = self.page.data.plotly.xy(record, y_columns, x_axis)
    bar_chart = graph.GraphPlotly.Bar(self.page, width, height, options, html_code, profile)
    bar_chart.colors(self.page.theme.charts)
    for d in data['datasets']:
      bar_chart.add_trace(d, type='bar')
      bar_chart.data.orientation = 'h'
    return bar_chart

  def scatter(self, record=None, y_columns=None, x_axis=None, text_column=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plotly.com/javascript/text-and-annotations/

    Attributes:
    ----------
    :param record: List of dict. The Python record.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param text_column: String. Optional.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'text_column': text_column, 'type': 'scatter',
                    'mode': 'markers+text' if text_column is not None else 'markers'})
    data = self.page.data.plotly.xy_text(
      record, y_columns, x_axis, text_column, options={"agg": options.get('agg', 'distinct')})
    sc_chart = graph.GraphPlotly.Line(self.page, width, height, options or {}, html_code, profile)
    sc_chart.colors(self.page.theme.charts)
    sc_chart.options.responsive = True
    for i, d in enumerate(data['datasets']):
      sc_chart.add_trace(d, mode=options['mode'], type=options['type'])
      sc_chart.data.marker.color = self.page.theme.charts[i]
      if text_column is not None:
        sc_chart.data.text = d['text']
    sc_chart.layout.no_background()
    return sc_chart

  def timeseries(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
                 height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plot.ly/javascript/
      https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

    Attributes:
    ----------
    :param record: List of dict. The Python record.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'mode': 'lines', 'type': "scatter"})
    data = self.page.data.plotly.xy(record, y_columns, x_axis)
    sc_chart = graph.GraphPlotly.Line(self.page, width, height, options, html_code, profile)
    sc_chart.colors(self.page.theme.charts)
    for d in data['datasets']:
      sc_chart.add_trace(d)
    return sc_chart

  def scattergl(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
                height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plotly.com/javascript/line-and-scatter/

    Attributes:
    ----------
    :param record: List of dict. The Python record.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'mode': 'markers', 'type': "scattergl"})
    data = self.page.data.plotly.xy(record, y_columns, x_axis)
    sc_chart = graph.GraphPlotly.Line(self.page, width, height, options or {}, html_code, profile)
    sc_chart.colors(self.page.theme.charts)
    for d in data['datasets']:
      sc_chart.add_trace(d, type="scattergl", mode='markers')
    return sc_chart

  def histogram(self, record, y_columns=None, x_columns=None, profile=None, options=None, width=(100, "%"),
                height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
      https://plot.ly/javascript/

    Attributes:
    ----------
    :param record:
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_columns: List. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).

    :rtype: graph.GraphPlotly.Bar
    """
    data = []
    histo_axis = ('y', y_columns) if y_columns is not None else ('x', x_columns)
    for y in histo_axis[1]:
      series = {histo_axis[0]: []}
      for rec in record:
        if y in rec:
          series[histo_axis[0]].append(float(rec[y]))
      data.append(series)
    histo_chart = graph.GraphPlotly.Bar(self.page, width, height, options or {}, html_code, profile)
    histo_chart.colors(self.page.theme.charts)
    for d in data:
      histo_chart.add_trace(d, type='histogram')
    return histo_chart

  def pie(self, record=None, y_columns=None, x_axis=None,  profile=None, options=None, width=(100, "%"),
          height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plotly.com/javascript/pie-charts/

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python records.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'type': 'pie', 'marker': {
      'colors': self.page.theme.charts}, 'mode': None, 'attrs': {'orientation': 'h'}})
    data = self.page.data.plotly.xy(record, y_columns, x_axis)
    pie_chart = graph.GraphPlotly.Pie(self.page, width, height, options or {}, html_code, profile)
    pie_chart.colors(self.page.theme.charts)
    pie_chart.options.responsive = True
    for d in data['datasets']:
      pie_chart.add_trace({"label": d['x'], "values": d['y']})
      pie_chart.data.marker.colors = self.page.theme.charts
    return pie_chart

  def donut(self, record=None, y_columns=None, x_axis=None,  profile=None, options=None, width=(100, "%"),
            height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plotly.com/javascript/pie-charts/

    Attributes:
    ----------
    :param record: List of dict. The Python record.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'type': 'pie', 'marker': {
      'colors': self.page.theme.charts}, 'mode': None, 'attrs': {'orientation': 'h'}})
    data = self.page.data.plotly.xy(record, y_columns, x_axis)
    pie_chart = graph.GraphPlotly.Pie(self.page, width, height, options or {}, html_code, profile)
    pie_chart.colors(self.page.theme.charts)
    pie_chart.options.responsive = True
    for d in data['datasets']:
      pie_chart.add_trace({"label": d['x'], "values": d['y']})
      pie_chart.data.marker.colors = self.page.theme.charts
    pie_chart.data.hole = 0.4
    return pie_chart

  def area(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"),
           html_code=None):
    """
    Description:
    ------------
    How to make a D3.js-based filled area plot in javascript.
    An area chart displays a solid color between the traces of a graph.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plotly.com/javascript/filled-area-plots/

    Attributes:
    ----------
    :param record: List of dict. The Python record.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'type': "scatter", 'attrs': {'fill': "tozeroy"}})
    data = self.page.data.plotly.xy(record, y_columns, x_axis)
    line_chart = graph.GraphPlotly.Line(self.page, width, height, options, html_code, profile)
    line_chart.colors(self.page.theme.charts)
    for d in data['datasets']:
      line_chart.add_trace(d)
      line_chart.data.type = options['type']
      line_chart.data.fill = "tozeroy"
    return line_chart

  def bubble(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
             height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    How to make a D3.js-based filled area plot in javascript.
    An area chart displays a solid color between the traces of a graph.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plotly.com/javascript/bubble-charts/

    Attributes:
    ----------
    :param record: List of dict. The Python record.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'mode': 'markers'})
    data = self.page.data.plotly.xy(record, y_columns, x_axis)
    line_chart = graph.GraphPlotly.Line(self.page, width, height, options, html_code, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.options.responsive = True
    for d in data['datasets']:
      line_chart.add_trace(d, mode=options['mode'])
    return line_chart

  def number(self, value, profile=None, options=None, width=(100, "%"), height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plotly.com/javascript/indicator/

    Attributes:
    ----------
    :param value:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'type': 'indicator', 'mode': "number"})
    ind = graph.GraphPlotly.Indicator(self.page, width, height, options, html_code, profile)
    ind.add_trace({'value': value}, mode=options["mode"])
    return ind

  def number_with_delta(self, value, delta=100, profile=None, options=None, width=(100, "%"), height=(330, "px"),
                        html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plotly.com/javascript/indicator/

    Attributes:
    ----------
    :param value:
    :param delta:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'type': 'indicator', 'mode': "number+delta", "delta": {'reference': delta}})
    ind = graph.GraphPlotly.Indicator(self.page, width, height, options, html_code, profile)
    ind.add_trace({'value': value}, mode=options["mode"])
    ind.data.delta.reference = delta
    return ind

  def gauge(self, value, profile=None, options=None, width=(100, "%"), height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    How to make a D3.js-based gauge chart in javascript.

    :tags:
    :categories:

    Usage::

      gauge = page.ui.charts.plotly.gauge(2000)
      gauge.data.gauge.axis.range = [0, 5000]

    Related Pages:

      https://plotly.com/javascript/gauge-charts/

    Attributes:
    ----------
    :param value:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'type': 'indicator', 'mode': "gauge+number"})
    gau = graph.GraphPlotly.Indicator(self.page, width, height, options or {}, html_code, profile)
    gau.add_trace({'value': value}, mode=options['mode'], type=options['type'])
    return gau

  def scatterpolar(self, record, r_columns=None, theta_axis=None, profile=None, options=None, width=(100, "%"),
                   height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param r_columns:
    :param theta_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    all_series = []
    for c in r_columns:
      series = {"r": [], "theta": []}
      for rec in record:
        series['r'].append(rec[c])
        series['theta'].append(rec[theta_axis])
      all_series.append(series)
    spolar_chart = graph.GraphPlotly.ScatterPolar(self.page, width, height, options or {}, html_code, profile)
    spolar_chart.colors(self.page.theme.charts)
    for d in all_series:
      spolar_chart.add_trace(d, mode="line")
      spolar_chart.data.marker.color = None
    return spolar_chart

  def box(self, record=None, y_columns=None, x_columns=None, profile=None, options=None, width=(100, "%"),
          height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_columns: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    axis, cols = ('y', y_columns) if y_columns is not None else ('x', x_columns)
    series = []
    if cols is not None:
      for c in cols:
        series.append([rec.get(c) for rec in record])
    box_chart = graph.GraphPlotly.Box(self.page, width, height, options or {}, html_code, profile)
    for s in series:
      box_chart.add_trace({axis: s})
    return box_chart

  def group_box(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
                height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://plot.ly/javascript/box-plots/

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    series, x = [[] for _ in range(len(y_columns))], []
    for rec in record:
      for i, c in enumerate(y_columns):
        series[i].append(rec.get(c))
      x.append(rec.get(x_axis))
    box_chart = graph.GraphPlotly.Box(self.page, width, height, options or {}, html_code, profile)
    for s in series:
      box_chart.add_trace({'y': s, 'x': x})
    return box_chart

  def candlestick(self, record, closes, highs, lows, opens, x_axis, profile=None, options=None, width=(100, "%"),
                  height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      data = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
      sc = page.ui.charts.plotly.candlestick(
          data, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"], opens=["AAPL.Open"], x_axis='Date')

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param closes:
    :param highs:
    :param lows:
    :param opens:
    :param x_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    all_series = []
    for i, c in enumerate(closes):
      series = {'x': [], 'close': [], 'high': [], 'low': [], 'open': []}
      for rec in record:
        series['x'].append(rec[x_axis])
        series['close'].append(rec[c])
        series['high'].append(rec[highs[i]])
        series['low'].append(rec[lows[i]])
        series['open'].append(rec[opens[i]])
      all_series.append(series)

    candle_chart = graph.GraphPlotly.CandleStick(self.page, width, height, options or {}, html_code, profile)
    for s in all_series:
      candle_chart.add_trace(s)
    candle_chart.layout.no_background()
    return candle_chart


class Plotly3D:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Plotly"

  def scatter(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
              height=(500, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Related Pages:

      https://plot.ly/javascript/3d-line-plots/

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'z_axis': z_axis, 'type': 'scatter3d',
                    'mode': 'markers'})
    data = self.page.data.plotly.xyz(record, y_columns, x_axis, z_axis)
    sc_chart = graph.GraphPlotly.Scatter3D(self.page, width, height, options or {}, html_code, profile)
    sc_chart.colors(self.page.theme.charts)
    for i, series in enumerate(data['datasets']):
      sc_chart.add_trace({'x': series['x'], 'y': series['y'], 'z': series['z']})
    return sc_chart

  def line(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
           height=(500, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Related Pages:

      https://plot.ly/javascript/3d-line-plots/

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'z_axis': z_axis, 'type': 'scatter3d', 'mode': 'lines'})
    data = self.page.data.plotly.xyz(record, y_columns, x_axis, z_axis)
    sc_chart = graph.GraphPlotly.Scatter3D(self.page, width, height, options or {}, html_code, profile)
    sc_chart.colors(self.page.theme.charts)
    for i, series in enumerate(data['datasets']):
      sc_chart.add_trace({'x': series['x'], 'y': series['y'], 'z': series['z']})
    return sc_chart

  def marker(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
             height=(500, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Related Pages:

      https://plot.ly/javascript/3d-line-plots/

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'z_axis': z_axis, 'type': 'scatter3d',
                    'mode': 'lines+markers'})
    data = self.page.data.plotly.xyz(record, y_columns, x_axis, z_axis)
    sc_chart = graph.GraphPlotly.Scatter3D(self.page, width, height, options or {}, html_code, profile)
    for i, series in enumerate(data['datasets']):
      sc_chart.add_trace({'x': series['x'], 'y': series['y'], 'z': series['z']})
      sc_chart.data.line.color = self.page.theme.colors[i]
    return sc_chart

  def ribbon(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
             height=(500, "px"), html_code=None):
    """
    Description:
    ------------
    Create ribbons on the x axis.

    :tags:
    :categories:

    Related Pages:

      https://plot.ly/javascript/ribbon-plots/

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'delta': {"x": 1, 'y': 1, 'z': 0}}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'z_axis': z_axis, 'type': 'scatter3d',
                    'mode': 'lines+markers'})
    data = self.page.data.plotly.x_yz(
      record, y_columns, x_axis, z_axis, dy=options['delta']['y'], dx=options['delta']['x'], dz=options['delta']['z'])
    line_chart = graph.GraphPlotly.Surface(self.page, width, height, options or {}, html_code,
                                           profile)
    line_chart.colors(self.page.theme.charts)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d)
      line_chart.data.showscale = False
    return line_chart

  def mesh3d(self, record, intensity, x, y, z, i=None, j=None, k=None, profile=None, options=None, width=(100, "%"),
             height=(500, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Related Pages:

      https://plot.ly/javascript/3d-mesh/

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param intensity:
    :param x:
    :param y:
    :param z:
    :param i:
    :param j:
    :param k:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    data = {"intensity": [], 'x': [], 'y': [], 'z': []}
    if i is not None:
      data[i] = []
    if j is not None:
      data[j] = []
    if k is not None:
      data[k] = []
    for rec in record:
      data["intensity"].append(rec[intensity])
      data["x"].append(rec[x])
      data["y"].append(rec[y])
      data["z"].append(rec[z])
      if i is not None:
        data["i"].append(rec[i])
      if j is not None:
        data["j"].append(rec[j])
      if k is not None:
        data["k"].append(rec[k])
    mesh_chart = graph.GraphPlotly.Mesh3d(self.page, width, height, options or {}, html_code, profile)
    mesh_chart.colors(self.page.theme.charts)
    mesh_chart.add_trace(data)
    return mesh_chart

  def surface(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
              height=(500, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'type': 'surface', 'mode': ''})
    naps = self.page.data.plotly.surface(record, y_columns, x_axis, z_axis)
    surf_chart = graph.GraphPlotly.Surface(self.page, width, height, options, html_code, profile)
    surf_chart.colors(self.page.theme.charts)
    for i, d in enumerate(naps['datasets']):
      surf_chart.add_trace({'z': d})
      surf_chart.data.showscale = False
    return surf_chart

  def maps(self, record, profile=None, options=None, width=(100, "%"), height=(500, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    options.update({'type': 'surface', 'mode': ''})
    surf_chart = graph.GraphPlotly.Surface(self.page, width, height, options, html_code, profile)
    for d in record:
      surf_chart.add_trace({'z': d})
    return surf_chart


class Plotly(Plotly2D):

  def __init__(self, ui):
    super(Plotly, self).__init__(ui)
    self._3d = Plotly3D(ui)

  def scatter3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
                height=(400, "px"), html_code=None):
    return self._3d.scatter(
      record, y_columns=y_columns, x_axis=x_axis, z_axis=z_axis, profile=profile, options=options, width=width,
      height=height, html_code=html_code)

  def line3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
             height=(400, "px"), html_code=None):
    return self._3d.line(
      record, y_columns=y_columns, x_axis=x_axis, z_axis=z_axis, profile=profile, options=options,
      width=width, height=height, html_code=html_code)

  def marker3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
               height=(400, "px"), html_code=None):
    return self._3d.marker(
      record, y_columns=y_columns, x_axis=x_axis, z_axis=z_axis, profile=profile, options=options, width=width,
      height=height, html_code=html_code)

  def ribbon(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
             height=(500, "px"), html_code=None):
    return self._3d.ribbon(record, y_columns, x_axis, z_axis, profile, options, width, height, html_code)

  def mesh3d(self, record, intensity, x, y, z, i=None, j=None, k=None, profile=None, options=None, width=(100, "%"),
             height=(500, "px"), html_code=None):
    return self._3d.mesh3d(record, intensity, x, y, z, i, j, k, profile, options, width, height, html_code)

  def surface(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
              height=(500, "px"), html_code=None):
    return self._3d.surface(record, y_columns, x_axis, z_axis, profile, options, width, height, html_code)

  def maps(self, record, profile=None, options=None, width=(100, "%"), height=(500, "px"), html_code=None):
    return self._3d.maps(record, profile, options, width, height, html_code)
