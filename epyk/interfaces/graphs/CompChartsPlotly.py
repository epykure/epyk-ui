
from epyk.core.html import graph


class Plotly2D(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Plotly"

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

			https://plot.ly/javascript/
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'type': 'bar', 'mode': 'lines+markers'})
    data = self.parent.context.rptObj.data.plotly.xy(record, y_columns, x_axis)
    line_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    line_chart.options.responsive = True
    self.parent.context.register(line_chart)
    for d in data['datasets']:
      line_chart.add_trace(d)
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

			https://plotly.com/javascript/bar-charts/

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'type': 'bar', 'mode': None})
    data = self.parent.context.rptObj.data.plotly.xy(record, y_columns, x_axis)
    bar_chart = graph.GraphPlotly.Bar(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    self.parent.context.register(bar_chart)
    for d in data['datasets']:
      bar_chart.add_trace(d)
    return bar_chart

  def hbar(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

			https://plotly.com/javascript/bar-charts/

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'type': 'bar', 'mode': None, 'attrs': {'orientation': 'h'}})
    data = self.parent.context.rptObj.data.plotly.xy(record, y_columns, x_axis)
    bar_chart = graph.GraphPlotly.Bar(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    self.parent.context.register(bar_chart)
    for d in data['datasets']:
      bar_chart.add_trace(d, type='bar')
      bar_chart.data.orientation = 'h'
    return bar_chart

  def scatter(self, record=None, y_columns=None, x_axis=None, text_column=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

			https://plotly.com/javascript/text-and-annotations/

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'text_column': text_column, 'type': 'scatter',
                    'mode': 'markers+text' if text_column is not None else 'markers'})
    data = self.parent.context.rptObj.data.plotly.xy_text(record, y_columns, x_axis, text_column)
    sc_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(sc_chart)
    for i, d in enumerate(data['datasets']):
      sc_chart.add_trace(d, mode=options['mode'], type=options['type'])
      sc_chart.data.marker.color = self.parent.context.rptObj.theme.colors[i]
      if text_column is not None:
        sc_chart.data.text = d['text']
    sc_chart.layout.no_background()
    return sc_chart

  def timeseries(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

			https://plot.ly/javascript/
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'mode': 'lines', 'type': "scatter"})
    data = self.parent.context.rptObj.data.plotly.xy(record, y_columns, x_axis)
    sc_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    self.parent.context.register(sc_chart)
    for d in data['datasets']:
      sc_chart.add_trace(d)
    return sc_chart

  def scattergl(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

			https://plotly.com/javascript/line-and-scatter/

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'mode': 'markers', 'type': "scattergl"})
    data = self.parent.context.rptObj.data.plotly.xy(record, y_columns, x_axis)
    sc_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(sc_chart)
    for d in data['datasets']:
      sc_chart.add_trace(d, type="scattergl", mode='markers')
    return sc_chart

  def histogram(self, record, y_columns=None, x_columns=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Related Pages:

			https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param record:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:

    :return:

    :rtype: graph.GraphPlotly.Chart
    """
    data = []
    histo_axis = ('y', y_columns) if y_columns is not None else ('x', x_columns)
    for rec in record:
      for y in histo_axis[1]:
        series = {histo_axis[0]: []}
        if y in rec:
          series[histo_axis[0]].append(float(rec[y]))
        data.append(series)
    histo_chart = graph.GraphPlotly.Bar(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(histo_chart)
    for d in data:
      histo_chart.add_trace(d, type='histogram')
    return histo_chart

  def pie(self, record=None, y_columns=None, x_axis=None,  profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

			https://plotly.com/javascript/pie-charts/

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'type': 'pie', 'marker': {'colors': self.parent.context.rptObj.theme.charts}, 'mode': None, 'attrs': {'orientation': 'h'}})
    data = self.parent.context.rptObj.data.plotly.xy(record, y_columns, x_axis)
    pie_chart = graph.GraphPlotly.Pie(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(pie_chart)
    for d in data['datasets']:
      pie_chart.add_trace({"label": d['x'], "values": d['y']})
      pie_chart.data.marker.colors = self.parent.context.rptObj.theme.charts
    return pie_chart

  def area(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    How to make a D3.js-based filled area plot in javascript. An area chart displays a solid color between the traces of a graph.

    Related Pages:

			https://plotly.com/javascript/filled-area-plots/

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'type': "scatter", 'attrs': {'fill': "tozeroy"}})
    data = self.parent.context.rptObj.data.plotly.xy(record, y_columns, x_axis)
    line_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    self.parent.context.register(line_chart)
    for d in data['datasets']:
      line_chart.add_trace(d)
      line_chart.data.type = options['type']
      line_chart.data.fill = "tozeroy"
    return line_chart

  def bubble(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    How to make a D3.js-based filled area plot in javascript. An area chart displays a solid color between the traces of a graph.

    Related Pages:

			https://plotly.com/javascript/bubble-charts/

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'mode': 'markers'})
    data = self.parent.context.rptObj.data.plotly.xy(record, y_columns, x_axis)
    line_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    self.parent.context.register(line_chart)
    for d in data['datasets']:
      line_chart.add_trace(d, mode=options['mode'])
    return line_chart

  def number(self, value, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

			https://plotly.com/javascript/indicator/

    Attributes:
    ----------
    :param value:
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'type': 'indicator', 'mode': "number"})
    ind = graph.GraphPlotly.Indicator(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    self.parent.context.register(ind)
    ind.add_trace({'value': value}, mode=options["mode"])
    return ind

  def number_with_delta(self, value, delta=100, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

			https://plotly.com/javascript/indicator/

    Attributes:
    ----------
    :param value:
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'type': 'indicator', 'mode': "number+delta", "delta": {'reference': delta}})
    ind = graph.GraphPlotly.Indicator(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    self.parent.context.register(ind)
    ind.add_trace({'value': value}, mode=options["mode"])
    ind.data.delta.reference = delta
    return ind

  def gauge(self, value, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    How to make a D3.js-based gauge chart in javascript.


    gauge = rptObj.ui.charts.plotly.gauge(2000)
    gauge.data.gauge.axis.range = [0, 5000]

    Related Pages:

			https://plotly.com/javascript/gauge-charts/

    Attributes:
    ----------
    :param value:
    :param profile:
    :param options:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param htmlCode:
    """
    options = options or {}
    options.update({'type': 'indicator', 'mode': "gauge+number"})
    gau = graph.GraphPlotly.Indicator(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(gau)
    gau.add_trace({'value': value}, mode=options['mode'], type=options['type'])
    return gau

  def scatterpolar(self, records, r_columns=None, theta_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    all_series = []
    for c in r_columns:
      series = {"r": [], "theta": []}
      for rec in records:
        series['r'].append(rec[c])
        series['theta'].append(rec[theta_axis])
      all_series.append(series)
    spolar_chart = graph.GraphPlotly.ScatterPolar(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(spolar_chart)
    for d in all_series:
      spolar_chart.add_trace(d, mode="line")
      spolar_chart.data.marker.color = None
    return spolar_chart

  def box(self, records, y_columns=None, x_columns=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):

    axis, cols = ('y', y_columns) if y_columns is not None else ('x', x_columns)
    series = []
    for c in cols:
      series.append([rec.get(c) for rec in records])
    box_chart = graph.GraphPlotly.Box(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(box_chart)
    for s in series:
      box_chart.add_trace({axis: s})
    return box_chart

  def group_box(self, records, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    https://plot.ly/javascript/box-plots/

    :param records:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    series, x = [[] for _ in range(len(y_columns))], []
    for rec in records:
      for i, c in enumerate(y_columns):
        series[i].append(rec.get(c))
      x.append(rec.get(x_axis))
    box_chart = graph.GraphPlotly.Box(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(box_chart)
    for s in series:
      box_chart.add_trace({'y': s, 'x': x})
    return box_chart

  def candlestick(self, records, closes, highs, lows, opens, x_axis, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    data = rptObj.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
    sc = rptObj.ui.charts.plotly.candlestick(data, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"], opens=["AAPL.Open"], x_axis='Date')

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
    for i, c in enumerate(closes):
      series = {'x': [], 'close': [], 'high': [], 'low': [], 'open': []}
      for rec in records:
        series['x'].append(rec[x_axis])
        series['close'].append(rec[c])
        series['high'].append(rec[highs[i]])
        series['low'].append(rec[lows[i]])
        series['open'].append(rec[opens[i]])
      all_series.append(series)

    candle_chart = graph.GraphPlotly.CandleStick(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(candle_chart)
    for s in all_series:
      candle_chart.add_trace(s)
    candle_chart.layout.no_background()
    return candle_chart


class Plotly3D(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Plotly"

  def scatter(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
              height=(500, "px"), htmlCode=None):
    """

    https://plot.ly/javascript/3d-line-plots/

    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'z_axis': z_axis, 'type': 'scatter3d', 'mode': 'markers'})
    data = self.parent.context.rptObj.data.plotly.xyz(record, y_columns, x_axis, z_axis)
    sc_chart = graph.GraphPlotly.Scatter3D(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(sc_chart)
    for i, series in enumerate(data['datasets']):
      sc_chart.add_trace({'x': series['x'], 'y': series['y'], 'z': series['z']})
      sc_chart.data.line.color = self.parent.context.rptObj.theme.colors[i]
    return sc_chart

  def line(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
              height=(500, "px"), htmlCode=None):
    """

    https://plot.ly/javascript/3d-line-plots/

    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'z_axis': z_axis, 'type': 'scatter3d', 'mode': 'lines'})
    data = self.parent.context.rptObj.data.plotly.xyz(record, y_columns, x_axis, z_axis)
    sc_chart = graph.GraphPlotly.Scatter3D(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(sc_chart)
    for i, series in enumerate(data['datasets']):
      sc_chart.add_trace({'x': series['x'], 'y': series['y'], 'z': series['z']})
      #sc_chart.data.line.color = self.parent.context.rptObj.theme.colors[i]
    return sc_chart

  def marker(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
              height=(500, "px"), htmlCode=None):
    """

    https://plot.ly/javascript/3d-line-plots/

    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'z_axis': z_axis, 'type': 'scatter3d', 'mode': 'lines+markers'})
    data = self.parent.context.rptObj.data.plotly.xyz(record, y_columns, x_axis, z_axis)
    sc_chart = graph.GraphPlotly.Scatter3D(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(sc_chart)
    for i, series in enumerate(data['datasets']):
      sc_chart.add_trace({'x': series['x'], 'y': series['y'], 'z': series['z']})
      sc_chart.data.line.color = self.parent.context.rptObj.theme.colors[i]
    return sc_chart

  def ribbon(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
             height=(500, "px"), htmlCode=None):
    """
    Description:
    ------------
    Create ribbons on the x axis

    Related Pages:

      https://plot.ly/javascript/ribbon-plots/

    ttributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {'delta': {"x": 1, 'y': 1, 'z': 0}}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'z_axis': z_axis, 'type': 'scatter3d', 'mode': 'lines+markers'})
    data = self.parent.context.rptObj.data.plotly.x_yz(record, y_columns, x_axis, z_axis, dy=options['delta']['y'], dx=options['delta']['x'], dz=options['delta']['z'])
    line_chart = graph.GraphPlotly.Surface(self.parent.context.rptObj, width, height, options or {}, htmlCode,
                                           profile)
    self.parent.context.register(line_chart)
    for i, d in enumerate(data['datasets']):
      line_chart.add_trace(d)
      line_chart.data.showscale = False
    return line_chart

  def mesh3d(self, records, intensity, x, y, z, i=None, j=None, k=None, profile=None, options=None, width=(100, "%"),
             height=(500, "px"), htmlCode=None):
    """

    https://plot.ly/javascript/3d-mesh/

    :param records:
    :param intensity:
    :param x:
    :param y:
    :param z:
    :param i:
    :param j:
    :param k:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    data = {"intensity": [], 'x': [], 'y': [], 'z': []}
    if i is not None:
      data[i] = []
    if j is not None:
      data[j] = []
    if k is not None:
      data[k] = []
    for rec in records:
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
    mesh_chart = graph.GraphPlotly.Mesh3d(self.parent.context.rptObj, width, height, options or {}, htmlCode, profile)
    self.parent.context.register(mesh_chart)
    mesh_chart.add_trace(data)
    return mesh_chart

  def surface(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"),
              height=(500, "px"), htmlCode=None):
    """

    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    options = options or {}
    options.update({'type': 'surface', 'mode': ''})
    naps = self.parent.context.rptObj.data.plotly.surface(record, y_columns, x_axis, z_axis)
    surf_chart = graph.GraphPlotly.Surface(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    self.parent.context.register(surf_chart)
    for i, d in enumerate(naps['datasets']):
      surf_chart.add_trace({'z': d})
      surf_chart.data.showscale = False
    return surf_chart

  def maps(self, records, profile=None, options=None, width=(100, "%"), height=(500, "px"), htmlCode=None):

    options = options or {}
    options.update({'type': 'surface', 'mode': ''})
    surf_chart = graph.GraphPlotly.Surface(self.parent.context.rptObj, width, height, options, htmlCode, profile)
    self.parent.context.register(surf_chart)
    for d in records:
      surf_chart.add_trace({'z': d})
    return surf_chart


class Plotly(Plotly2D):

  def __init__(self, context):
    super(Plotly, self).__init__(context)
    self._3d = Plotly3D(context)

  def scatter3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"), height=(400, "px"), htmlCode=None):
    return self._3d.scatter(record, y_columns=y_columns, x_axis=x_axis, z_axis=z_axis, profile=profile, options=options, width=width, height=height, htmlCode=htmlCode)

  def line3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"), height=(400, "px"), htmlCode=None):
    return self._3d.line(record, y_columns=y_columns, x_axis=x_axis, z_axis=z_axis, profile=profile, options=options, width=width, height=height, htmlCode=htmlCode)

  def marker3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"), height=(400, "px"), htmlCode=None):
    return self._3d.marker(record, y_columns=y_columns, x_axis=x_axis, z_axis=z_axis, profile=profile, options=options, width=width, height=height, htmlCode=htmlCode)

  def ribbon(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"), height=(500, "px"), htmlCode=None):
    return self._3d.ribbon(record, y_columns, x_axis, z_axis, profile, options, width, height, htmlCode)

  def mesh3d(self, record, intensity, x, y, z, i=None, j=None, k=None, profile=None, options=None, width=(100, "%"), height=(500, "px"), htmlCode=None):
    return self._3d.mesh3d(record, intensity, x, y, z, i, j, k, profile, options, width, height, htmlCode)

  def surface(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, options=None, width=(100, "%"), height=(500, "px"), htmlCode=None):
    return self._3d.surface(record, y_columns, x_axis, z_axis, profile, options, width, height, htmlCode)

  def maps(self, record, profile=None, options=None, width=(100, "%"), height=(500, "px"), htmlCode=None):
    return self._3d.maps(record, profile, options, width, height, htmlCode)
