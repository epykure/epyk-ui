
from epyk.core.html import graph


class Plotly(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Plotly"

  def line(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
           width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    if record is None:
      record = []
      y_columns = y_columns or []
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    line_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    line_chart.options.responsive = True
    self.parent.context.register(line_chart)
    for d in data:
      line_chart.add_trace(d)
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
          width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    if record is None:
      record = []
      y_columns = y_columns or []
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    bar_chart = graph.GraphPlotly.Bar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(bar_chart)
    for d in data:
      bar_chart.add_trace(d)
    return bar_chart

  def hbar(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
          width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

    :param record:
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
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    bar_chart = graph.GraphPlotly.Bar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(bar_chart)
    for d in data:
      bar_chart.add_trace(d, type='bar')
      bar_chart.data.orientation = 'h'
    return bar_chart

  def scatter(self, record=None, y_columns=None, x_axis=None, texts=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    if record is None:
      data = []
    else:
      agg_data, pount_texts = {}, {}
      for rec in record:
        for i, y in enumerate(y_columns):
          if y in rec:
            agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
            if texts is not None:
              pount_texts.setdefault(y, {})[rec[x_axis]] = rec[texts[i]]
      data = []
      for c in y_columns:
        series = {'x': [], 'y': [], 'text': []}
        for x, y in agg_data[c].items():
          series['x'].append(x)
          series['y'].append(y)
          if texts is not None:
            series['text'].append(pount_texts[c][x])
        data.append(series)
    sc_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
    self.parent.context.register(sc_chart)
    for i, d in enumerate(data):
      sc_chart.add_trace(d, mode='markers+text' if texts is not None else 'markers', type="scatter")
      sc_chart.data.marker.color = self.parent.context.rptObj.theme.colors[i]
    sc_chart.layout.no_background()
    return sc_chart

  def timeseries(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
                 width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

        Documentation
        https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
        https://plot.ly/javascript/

        :param record:
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
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    sc_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                      filters, profile)
    self.parent.context.register(sc_chart)
    for d in data:
      sc_chart.add_trace(d, mode='lines', type="scatter")
    return sc_chart

  def scattergl(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param record:
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
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    sc_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(sc_chart)
    for d in data:
      sc_chart.add_trace(d, type="scattergl", mode='markers')
    return sc_chart

  def histogram(self, record, y_columns=None, x_columns=None, title=None, filters=None, profile=None, options=None,
                width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param record:
    :param title:
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
    histo_chart = graph.GraphPlotly.Bar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(histo_chart)

    for d in data:
      histo_chart.add_trace(d, type='histogram')
    return histo_chart

  def pie(self, record=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    if record is None:
      record = []
      y_columns = y_columns or []
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    data = []
    for c in y_columns:
      series = {'labels': [], 'values': []}
      for x, y in agg_data[c].items():
        series['labels'].append(x)
        series['values'].append(y)
      data.append(series)

    pie_chart = graph.GraphPlotly.Pie(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(pie_chart)
    for d in data:
      pie_chart.add_trace(d)
    return pie_chart

  def area(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param record:
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
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    line_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(line_chart)
    for d in data:
      line_chart.add_trace(d)
      line_chart.data.type = "scatter"
      line_chart.data.fill = "tozeroy"
    return line_chart

  def bubble(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param data:
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
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    line_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(line_chart)
    for d in data:
      line_chart.add_trace(d, mode="markers")
    return line_chart

  def ribbon(self, record, y_columns=None, x_axis=None, z_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Create ribbons on the x axis

    https://plot.ly/javascript/ribbon-plots/

    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param title:
    :param filters:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    agg_data, z_data = {}, {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
          z_data.setdefault(y, {})[rec[x_axis]] = rec.get(z_axis)
    data = []
    for c in y_columns:
      series = {'x': [], 'y': [], 'z': []}
      for x, y in agg_data[c].items():
        series['x'].append([x, x+1])
        series['y'].append([y, y])
        series['z'].append([z_data[c][x], z_data[c][x]])
      data.append(series)
    line_chart = graph.GraphPlotly.Surface(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                            filters, profile)
    self.parent.context.register(line_chart)
    for d in data:
      line_chart.add_trace(d)
      line_chart.data.showscale = False
    return line_chart

  def surface(self, record, y_columns=None, x_axis=None, z_axis=None, title=None, filters=None, profile=None,
             options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param title:
    :param filters:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """

    z_a, x_a, agg_y = set(), set(), {}
    for rec in record:
      if z_axis in rec:
        z_a.add(rec[z_axis])
      if x_axis in rec:
        x_a.add(rec[x_axis])
      if z_axis in rec and x_axis in rec:
        agg_key = (rec[x_axis], rec[z_axis])
        for y in y_columns:
          agg_y.setdefault(agg_key, {})[y] = agg_y.get(agg_key, {}).get(y, 0) + float(rec[y])
    z_array = sorted(list(z_a))
    x_array = sorted(list(x_a))
    naps = []
    for y in y_columns:
      nap = []
      for z in z_array:
        row = [agg_y.get((x, z), {}).get(y) for x in x_array]
        nap.append(row)
      naps.append(nap)

    surf_chart = graph.GraphPlotly.Surface(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                           filters, profile)
    self.parent.context.register(surf_chart)
    for d in naps:
      surf_chart.add_trace({'z': d})
      surf_chart.data.showscale = False
    return surf_chart

  def scatter3d(self, record, y_columns=None, x_columns=None, z_columns=None, title=None, filters=None, profile=None,
             options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    https://plot.ly/javascript/3d-line-plots/

    :param record:
    :param y_columns:
    :param x_columns:
    :param z_columns:
    :param title:
    :param filters:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    x_series, y_all_series, z_series = [], [], []
    for i, y in enumerate(y_columns):
      xs, ys, zs = [], [], []
      for rec in record:
        xs.append(rec.get(x_columns[i]))
        zs.append(rec.get(z_columns[i]))
        ys.append(rec.get(y))
      x_series.append(xs)
      y_all_series.append(ys)
      z_series.append(zs)

    sc_chart = graph.GraphPlotly.Scatter3D(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                             filters, profile)
    self.parent.context.register(sc_chart)
    for i, y_series in enumerate(y_all_series):
      sc_chart.add_trace({'x': x_series[i], 'y': y_series, 'z': z_series[i]})
      sc_chart.data.line.color = self.parent.context.rptObj.theme.colors[i]
    return sc_chart

  def maps(self, records, title=None, filters=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):

    surf_chart = graph.GraphPlotly.Surface(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                           filters, profile)
    self.parent.context.register(surf_chart)
    for d in records:
      surf_chart.add_trace({'z': d})
    return surf_chart

  def mesh3d(self, records, intensity, x, y, z, i=None, j=None, k=None, title=None, filters=None, profile=None,
             options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
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
    :param title:
    :param filters:
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
    mesh_chart = graph.GraphPlotly.Mesh3d(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                           filters, profile)
    self.parent.context.register(mesh_chart)
    mesh_chart.add_trace(data)
    return mesh_chart

  def number(self, value, title=None, filters=None, profile=None, options=None, width=(100, "%"), height=(330, "px"),
             htmlCode=None):
    ind = graph.GraphPlotly.Indicator(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(ind)
    ind.add_trace({'value': value}, mode="number")
    return ind

  def number_with_delta(self, value, title=None, filters=None, profile=None, options=None, width=(100, "%"),
                        height=(330, "px"), htmlCode=None):
    ind = graph.GraphPlotly.Indicator(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(ind)
    ind.add_trace({'value': value}, mode="number+delta")
    return ind

  def gauge(self, value, title=None, filters=None, profile=None, options=None, width=(100, "%"),
                        height=(330, "px"), htmlCode=None):
    """

    gauge = rptObj.ui.charts.plotly.gauge(2000)
    gauge.data.gauge.axis.range = [0, 5000]

    https://plot.ly/javascript/indicator/

    :param value:
    :param title:
    :param filters:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    gau = graph.GraphPlotly.Indicator(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(gau)
    gau.add_trace({'value': value}, mode="gauge+number")
    return gau

  def scatterpolar(self, records, r_columns=None, theta_axis=None, title=None, profile=None,
             options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):

    all_series = []
    for c in r_columns:
      series = {"r": [], "theta": []}
      for rec in records:
        series['r'].append(rec[c])
        series['theta'].append(rec[theta_axis])
      all_series.append(series)
    spolar_chart = graph.GraphPlotly.ScatterPolar(self.parent.context.rptObj, width, height, title, options or {},
                                                  htmlCode, profile)
    self.parent.context.register(spolar_chart)
    for d in all_series:
      spolar_chart.add_trace(d, mode="line")
      spolar_chart.data.marker.color = None
    return spolar_chart

  def box(self, records, y_columns=None, x_columns=None, title=None, filters=None, profile=None,
             options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):

    axis, cols = ('y', y_columns) if y_columns is not None else ('x', x_columns)
    series = []
    for c in cols:
      series.append([rec.get(c) for rec in records])

    box_chart = graph.GraphPlotly.Box(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(box_chart)
    for s in series:
      box_chart.add_trace({axis: s})
    return box_chart

  def group_box(self, records, y_columns=None, x_axis=None, title=None, filters=None, profile=None,
             options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):

    """
    https://plot.ly/javascript/box-plots/

    :param records:
    :param y_columns:
    :param x_axis:
    :param title:
    :param filters:
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
    box_chart = graph.GraphPlotly.Box(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(box_chart)
    for s in series:
      box_chart.add_trace({'y': s, 'x': x})
    return box_chart

  def candlestick(self, records, closes, highs, lows, opens, x_axis, title=None, filters=None, profile=None,
                  options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):

    """

    data = rptObj.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
    sc = rptObj.ui.charts.plotly.candlestick(data, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"], opens=["AAPL.Open"], x_axis='Date')

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
    for i, c in enumerate(closes):
      series = {'x': [], 'close': [], 'high': [], 'low': [], 'open': []}
      for rec in records:
        series['x'].append(rec[x_axis])
        series['close'].append(rec[c])
        series['high'].append(rec[highs[i]])
        series['low'].append(rec[lows[i]])
        series['open'].append(rec[opens[i]])
      all_series.append(series)

    candle_chart = graph.GraphPlotly.CandleStick(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                       profile)
    self.parent.context.register(candle_chart)
    for s in all_series:
      candle_chart.add_trace(s)
    candle_chart.layout.no_background()
    return candle_chart
