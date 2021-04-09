#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core.html import graph
from epyk.interfaces import Arguments


class ChartJs:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "ChartJs"
    self.opacity = 0.6

  def plot(self, record=None, y=None, x=None, kind="line", profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y: List | String. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param kind: String. Optional. The chart type.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    if y is not None and not isinstance(y, list):
      y = [y]
    return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Display a line chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/scales/logarithmic/line.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    data = self.page.data.chartJs.y(record or [], y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d["data"], d['label'])
    line_chart.options.scales.y_axis().ticks.beginAtZero = True
    return line_chart

  def timeseries(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
                 height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a line chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/scales/logarithmic/line.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    line = self.line(record, y_columns, x_axis, profile, width, height, options, html_code)
    return line

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """
    Description:
    ------------
    Display a pie chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/pie.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. To set the profiling.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {"opacity": self.opacity}})
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartPie(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d["data"], d['label'], opacity=self.opacity)
    return line_chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """
    Description:
    ------------
    Display a donut chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/doughnut.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    dflt_options = {'cutoutPercentage': 50, 'y_columns': y_columns or [], 'x_axis': x_axis,
                    'commons': {"opacity": self.opacity}}
    if options is not None:
      dflt_options.update()
    pie_chart = graph.GraphChartJs.ChartPie(self.page, width, height, html_code, dflt_options, profile)
    pie_chart.colors(self.page.theme.charts)
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d["data"], d['label'], opacity=self.opacity)
    return pie_chart

  def area(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Display a area chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/area/line-stacked.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px")
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {"opacity": self.opacity}})
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d["data"], d['label'], opacity=self.opacity)
      line_chart.dataset().fill = True
    return line_chart

  def step(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Display a step chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/scales/linear/step-size.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%')
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px")
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {"fill": None}})
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    line_chart = graph.GraphChartJs.ChartLine(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d["data"], d['label'])
      line_chart.dataset().steppedLine = 'before'
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """
    Description:
    ------------
    Display a bar chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/scriptable/bar.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%')
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px")
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {"opacity": self.opacity}})
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartBar(self.page, width, height, html_code, options, profile)
    bar_chart.colors(self.page.theme.charts)
    bar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      bar_chart.add_dataset(d["data"], d['label'], opacity=self.opacity)
    bar_chart.options.scales.y_axis().ticks.beginAtZero = True
    bar_chart.options.scales.y_axis().ticks.toNumber()
    bar_chart.options.tooltips.callbacks.labelNumber()
    bar_chart.options.scales.x_axes().offset = True
    return bar_chart

  def custom(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
    """
    Description:
    ------------
    Display a bar chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/scriptable/bar.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    chartjs_defined_package = {
      'funnel-chart-js': {
        'version': '1.1.2',
        'req': [{'alias': 'chart.js'}],
        'website': 'https://www.npmjs.com/package/chartjs-plugin-funnel',
        'modules': [
          {'script': 'chart.funnel.min.js', 'path': '',
           'cdnjs': '%s/funnel-chart-js/dist/' % options['npm_path'].replace("\\", "/")},
        ]},
      'chartjs-chart-sankey': {
        'version': '0.1.3',
        'website': 'https://www.npmjs.com/package/chartjs-chart-sankey',
        'req': [{'alias': 'chart.js'}],
        'modules': [
          {'script': 'chartjs-chart-sankey.min.js', 'path': '',
           'cdnjs': '%s/chartjs-chart-sankey/dist/' % options['npm_path'].replace("\\", "/")}
        ]}
    }
    if options.get('npm') is not None and options['npm'] not in chartjs_defined_package:
      folder = "dist"
      if not os.path.exists('%s/%s/%s' % (options['npm_path'].replace("\\", "/"), options['npm'], folder)):
        folder = 'build'
        if not os.path.exists('%s/%s/%s' % (options['npm_path'].replace("\\", "/"), options['npm'], folder)):
          text = "Missing module %s/%s/dist or build in the package - use web npm to install package to your app"
          raise Exception(text % (options['npm_path'].replace("\\", "/"), options['npm']))

      chartjs_defined_package[options['npm']] = {
        'req': [{'alias': 'chart.js'}], 'version': 'N/A',
        'modules': [
          {'script': '%s.min.js' % options.get('script', options['npm']), 'path': '',
           'cdnjs': '%s/%s/%s' % (options['npm_path'].replace("\\", "/"), options['npm'], folder)},
        ]}

      del options['npm_path']
      if 'script' in options:
        del options['script']

    self.page.ext_packages.update(chartjs_defined_package)
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {"opacity": self.opacity}})
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartExts(self.page, width, height, html_code, options, profile)
    bar_chart.colors(self.page.theme.charts)
    bar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      bar_chart.add_dataset(d["data"], d['label'])
    bar_chart.options.scales.y_axis().ticks.beginAtZero = True
    return bar_chart

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Display a horizontal bar chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/scriptable/bar.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {"opacity": self.opacity}})
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartHBar(self.page, width, height, html_code, options, profile)
    bar_chart.colors(self.page.theme.charts)
    bar_chart.labels(data['labels'])
    bar_chart.options.scales.y_axis().ticks.beginAtZero = True
    for i, d in enumerate(data['datasets']):
      bar_chart.add_dataset(d["data"], d['label'])
    return bar_chart

  def multi(self, kind, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
            height=(330, "px"), html_code=None):
    """
    Description:
    ------------
    Display a multi chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/combo-bar-line.html

    Attributes:
    ----------
    :param kind: String. The chart type.
    :param record: List. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {"opacity": self.opacity}})
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    bar_chart = graph.GraphChartJs.ChartBar(self.page, width, height, html_code, options, profile)
    bar_chart.colors(self.page.theme.charts)
    bar_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      bar_chart.add_dataset(d["data"], d['label'])
    bar_chart.options.type = kind
    bar_chart.options.scales.y_axis().ticks.beginAtZero = True
    return bar_chart

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    """
    Description:
    ------------
    Display a scatter chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/scatter/basic.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'rDim': None, 'commons': {}})
    data = self.page.data.chartJs.xyz(record, y_columns, x_axis, None)
    line_chart = graph.GraphChartJs.ChartScatter(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d["data"], data['series'][i])
    return line_chart

  def bubble(self, record=None, y_columns=None, x_axis=None, r_values=None, profile=None, width=(100, "%"),
             height=(330, "px"), options=None, html_code=None):
    """
    Description:
    ------------
    Display a bubble chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/scriptable/bubble.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param r_values: List
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'z_columns': r_values, 'rDim': None,
                    'commons': {"opacity": self.opacity}})
    data = self.page.data.chartJs.xyz(record, y_columns, x_axis, r_values)
    line_chart = graph.GraphChartJs.ChartBubble(self.page, width, height, html_code, options, profile)
    line_chart.colors(self.page.theme.charts)
    line_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      line_chart.add_dataset(d, data['series'][i])
    return line_chart

  def polar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """
    Description:
    ------------
    Display a bubble chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/polar-area.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {"opacity": self.opacity}})
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    polar_chart = graph.GraphChartJs.ChartPolar(self.page, width, height, html_code, options, profile)
    polar_chart.colors(self.page.theme.charts)
    polar_chart.labels(data['labels'])
    polar_chart.options.scales.y_axis().display = False
    for i, d in enumerate(data['datasets']):
      polar_chart.add_dataset(d["data"], d['label'])
    return polar_chart

  def radar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """
    Description:
    ------------
    Display a bubble chart from ChartJs.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/radar.html

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {"opacity": self.opacity}})
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    radar_chart = graph.GraphChartJs.ChartRadar(self.page, width, height, html_code, options, profile)
    radar_chart.colors(self.page.theme.charts)
    radar_chart.labels(data['labels'])
    radar_chart.options.scales.y_axis().display = False
    for i, d in enumerate(data['datasets']):
      radar_chart.add_dataset(d["data"], d['label'])
    return radar_chart

  def fabric(self, profile=None, width=(100, "%"), height=(330, "px"), options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options.update({'y_columns': [], 'x_axis': "", 'commons': {"opacity": self.opacity}})
    component = graph.GraphChartJs.Fabric(self.page, width, height, html_code, options, profile)
    return component
