
import os

from epyk.core.html import graph


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
    data = self.parent.context.rptObj.data.chartJs.y(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
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
    data = self.parent.context.rptObj.data.chartJs.y(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartPie(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
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
    data = self.parent.context.rptObj.data.chartJs.y(record, y_columns, x_axis)
    dflt_options = {'cutoutPercentage': 50, 'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {}}
    if options is not None:
      dflt_options.update()
    pie_chart = graph.GraphChartJs.ChartPie(self.parent.context.rptObj, width, height, htmlCode, dflt_options, profile)
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d, data['series'][i])
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
    data = self.parent.context.rptObj.data.chartJs.y(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i], opacity=0.2)
      line_chart.dataset().fill = True
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
    data = self.parent.context.rptObj.data.chartJs.y(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
      line_chart.dataset().steppedLine = 'before'
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
    data = self.parent.context.rptObj.data.chartJs.y(record, y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      bar_chart.add_dataset(d, data['series'][i])
    bar_chart.options.scales.y_axis().ticks.beginAtZero = True
    return bar_chart

  def custom(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
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
    if self.parent.context.rptObj.ext_packages is None:
      self.parent.context.rptObj.ext_packages = {}
    chartjs_defined_package = {
      'funnel-chart-js': {
        'version': '1.1.2',
        'req': [{'alias': 'Chart.js'}],
        'website': 'https://www.npmjs.com/package/chartjs-plugin-funnel',
        'modules': [
          {'script': 'chart.funnel.min.js', 'path': '', 'cdnjs': '%s/funnel-chart-js/dist/' % options['npm_path'].replace("\\", "/")},
        ]},
      'chartjs-chart-sankey': {
        'version': '0.1.3',
        'website': 'https://www.npmjs.com/package/chartjs-chart-sankey',
        'req': [{'alias': 'Chart.js'}],
        'modules': [
          {'script': 'chartjs-chart-sankey.min.js', 'path': '', 'cdnjs': '%s/chartjs-chart-sankey/dist/' % options['npm_path'].replace("\\", "/")}
        ]}
    }
    if options.get('npm') is not None and options['npm'] not in chartjs_defined_package:
      folder = "dist"
      if not os.path.exists('%s/%s/%s' % (options['npm_path'].replace("\\", "/"), options['npm'], folder)):
        folder = 'build'
        if not os.path.exists('%s/%s/%s' % (options['npm_path'].replace("\\", "/"), options['npm'], folder)):
          raise Exception("Missing module %s/%s/dist or build in the package - use web npm feature to install package to your app " % (options['npm_path'].replace("\\", "/"), options['npm']))

      chartjs_defined_package[options['npm']] = {
        'req': [{'alias': 'Chart.js'}], 'version': 'N/A',
        'modules': [
          {'script': '%s.min.js' % options.get('script', options['npm']), 'path': '', 'cdnjs': '%s/%s/%s' % (options['npm_path'].replace("\\", "/"), options['npm'], folder) },
      ]}

      del options['npm_path']
      if 'script' in options:
        del options['script']

    self.parent.context.rptObj.ext_packages.update(chartjs_defined_package)
    options = options or {}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {}})
    data = self.parent.context.rptObj.data.chartJs.y(record, y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartExts(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      bar_chart.add_dataset(d, data['series'][i])
    bar_chart.options.scales.y_axis().ticks.beginAtZero = True
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
    data = self.parent.context.rptObj.data.chartJs.y(record, y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartHBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      bar_chart.add_dataset(d, data['series'][i])
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
    data = self.parent.context.rptObj.data.chartJs.y(record, y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    bar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      bar_chart.add_dataset(d, data['series'][i])
    bar_chart._attrs['type'] = type
    bar_chart.options.scales.y_axis().ticks.beginAtZero = True
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
    data = self.parent.context.rptObj.data.chartJs.xyz(record, y_columns, x_axis, None)
    line_chart = graph.GraphChartJs.ChartScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
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
    data = self.parent.context.rptObj.data.chartJs.xyz(record, y_columns, x_axis, r_values)
    line_chart = graph.GraphChartJs.ChartBubble(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
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
    data = self.parent.context.rptObj.data.chartJs.y(record, y_columns, x_axis)
    polar_chart = graph.GraphChartJs.ChartPolar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    polar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      polar_chart.add_dataset(d, data['series'][i])
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
    data = self.parent.context.rptObj.data.chartJs.y(record, y_columns, x_axis)
    radar_chart = graph.GraphChartJs.ChartRadar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    radar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      radar_chart.add_dataset(d, data['series'][i])
    return radar_chart
