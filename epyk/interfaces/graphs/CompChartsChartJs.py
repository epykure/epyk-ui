
from epyk.core.html import graph
from epyk.core.py import OrderedSet


def y(data, y_columns, x_axis):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param data: List of dict. The Python recordset
  :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
  :param x_axis: String. The column corresponding to a key in the dictionaries in the record
  """
  agg_data = {}
  for rec in data:
    for y in y_columns:
      if y in rec:
        agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
  labels, data = OrderedSet(), []
  for c in y_columns:
    for x, y in agg_data.get(c, {}).items():
      labels.add(x)
  is_data = {"labels": labels, 'datasets': [], 'series': []}
  for i, y in enumerate(y_columns):
    is_data["datasets"].append([agg_data.get(y, {}).get(x) for x in labels])
    is_data["series"].append(y)
  return is_data


def xy(data, y_columns, x_axis):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param data: List of dict. The Python recordset
  :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
  :param x_axis: String. The column corresponding to a key in the dictionaries in the record
  """
  agg_data = {}
  for rec in data:
    for y in y_columns:
      if y in rec:
        agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
  labels, data = set(), []
  for c in y_columns:
    series = []
    for x, y in agg_data[c].items():
      labels.add(x)
      series.append({"x": x, "y": y})
    data.append(series)
  is_data = {"labels": [], 'datasets': [], 'series': []}
  for i, l in enumerate(y_columns):
    is_data["labels"].append(l)
    is_data["datasets"].append(data[i])
    is_data["series"].append(l)
  return is_data


def xyz(data, y_columns, x_axis, z_axis):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param data: List of dict. The Python recordset
  :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
  :param x_axis: String. The column corresponding to a key in the dictionaries in the record
  :param z_axis:
  """
  agg_data, agg_r = {}, {}
  for rec in data:
    for i, y in enumerate(y_columns):
      if y in rec:
        agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
      if z_axis is not None and i < len(z_axis):
        agg_r.setdefault(y, {})[rec[x_axis]] = agg_r.get(y, {}).get(rec[x_axis], 0) + float(rec[z_axis[i]])
  labels, data = OrderedSet(), []
  for c in y_columns:
    series = []
    for x, y in agg_data[c].items():
      labels.add(x)
      series.append({"x": x, "y": y, 'r': agg_r.get(c, {}).get(x, 1)})
    data.append(series)
  is_data = {"labels": labels, 'datasets': [], 'series': []}
  for i, l in enumerate(y_columns):
    is_data["datasets"].append(data[i])
    is_data["series"].append(l)
  return is_data


class ChartJs(object):

  def __init__(self, context):
    self.parent = context
    self.chartFamily = "ChartJs"

  def line(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a line chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/scales/logarithmic/line.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = y(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(line_chart)
    return line_chart

  def timeseries(self, record, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a line chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/scales/logarithmic/line.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    line = self.line(record, y_columns, x_axis, profile, width, height, options, htmlCode)
    return line

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a pie chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/pie.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {}})
    data = y(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartPie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(line_chart)
    return line_chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a donut chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/doughnut.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    data = y(record, y_columns, x_axis)
    dflt_options = {'cutoutPercentage': 50, 'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {}}
    if options is not None:
      dflt_options.update()
    pie_chart = graph.GraphChartJs.ChartPie(self.parent.context.rptObj, width, height, htmlCode, dflt_options, profile)
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(pie_chart)
    return pie_chart

  def area(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a area chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/area/line-stacked.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {"opacity": 0.2}})
    data = y(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i], opacity=0.2)
      line_chart.dataset().fill = True
    self.parent.context.register(line_chart)
    return line_chart

  def step(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a step chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/scales/linear/step-size.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {"fill": None}})
    data = y(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
      line_chart.dataset().steppedLine = 'before'
    self.parent.context.register(line_chart)
    return line_chart

  def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a bar chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/scriptable/bar.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {}})
    data = y(record, y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bar_chart.labels(data['labels'])
    for d in data['datasets']:
      bar_chart.add_dataset(d)
    bar_chart.options.scales.y_axis().ticks.beginAtZero = True
    self.parent.context.register(bar_chart)
    return bar_chart

  def hbar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a horizontal bar chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/scriptable/bar.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {}})
    data = y(record, y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartHBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bar_chart.labels(data['labels'])
    for d in data['datasets']:
      bar_chart.add_dataset(d)
    self.parent.context.register(bar_chart)
    return bar_chart

  def multi(self, type, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------
    Display a multi chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/combo-bar-line.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {}})
    data = y(record, y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bar_chart.labels(data['labels'])
    for d in data['datasets']:
      bar_chart.add_dataset(d)
    bar_chart._attrs['type'] = type
    bar_chart.options.scales.y_axis().ticks.beginAtZero = True
    self.parent.context.register(bar_chart)
    return bar_chart

  def scatter(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a scatter chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/scatter/basic.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'rDim': None, 'attrs': {}})
    data = xy(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(line_chart)
    return line_chart

  def bubble(self, record, y_columns=None, x_axis=None, r_values=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a bubble chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/scriptable/bubble.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'z_columns': r_values, 'colors': self.parent.context.rptObj.theme.charts, 'rDim': None, 'attrs': {}})
    data = xyz(record, y_columns, x_axis, r_values)
    line_chart = graph.GraphChartJs.ChartBubble(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(line_chart)
    return line_chart

  def polar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a bubble chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/polar-area.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {}})
    data = y(record, y_columns, x_axis)
    polar_chart = graph.GraphChartJs.ChartPolar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    polar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      polar_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(polar_chart)
    return polar_chart

  def radar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Display a bubble chart from ChartJs

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/radar.html

    Attributes:
    ----------
    :param record: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param profile:
    :param width: Tuple. The width of the component in the page, default (100, '%')
    :param height: Tuple. The height of the component in the page, default (330, "px")
    :param options:
    :param htmlCode:
    """
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {}})
    data = y(record, y_columns, x_axis)
    radar_chart = graph.GraphChartJs.ChartRadar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    radar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      radar_chart.add_dataset(d, data['series'][i])
    self.parent.context.register(radar_chart)
    return radar_chart
