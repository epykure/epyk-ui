#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core.py import types
from epyk.core.html import graph
from epyk.interfaces import Arguments
from epyk.core.js import Imports
from epyk.core.css import Colors


class ChartJs:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "ChartJs"
    self.opacity = 0.6

  def set_version(self, v: str):
    """
    Description:
    ------------
    Change the version of the chartJs package.
    Use **self.page.imports.pkgs.chart_js.version** to get the current version.

    Usage::

      page.ui.charts.chartJs.set_version("2.9.4").line(languages, y_columns=['change'], x_axis="name")

    Attributes:
    ----------
    :param v: The version number.
    """
    if v.startswith("2"):
      self.page.imports.setVersion("chart.js", v, js={'register': {
        'alias': 'Chart', 'module': 'Chart.min', 'npm': 'chart.js', 'npm_path': 'dist'}, 'modules': [
        {'script': 'Chart.min.js', 'node_path': 'dist/', 'path': 'Chart.js/%(version)s/', 'cdnjs': Imports.CDNJS_REPO}]},
                                   css={'modules': [
        {'script': 'Chart.min.css', 'node_path': 'dist/', 'path': 'Chart.js/%(version)s/', 'cdnjs': Imports.CDNJS_REPO}]})
    if v.startswith("3"):
      self.page.imports.setVersion("chart.js", v, js={'register': {
        'alias': 'chart', 'module': 'chart.min', 'npm': 'chart.js', 'npm_path': 'dist'}, 'modules': [
        {'script': 'chart.min.js', 'node_path': 'dist/', 'path': 'Chart.js/%(version)s/', 'cdnjs': Imports.CDNJS_REPO}]},
                                   css=False)
    return self

  def plot(self, record: list = None, y: list = None, x: str = None, kind: str = "line",
           profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
           height: types.SIZE_TYPE = (330, "px"), options: dict = None,
           html_code: str = None) -> graph.GraphChartJs.Chart:
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x: Optional. The column corresponding to a key in the dictionaries in the record
    :param kind: Optional. The chart type
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    if y is not None and not isinstance(y, list):
      y = [y]
    return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def line(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
           html_code: str = None) -> graph.GraphChartJs.ChartLine:
    """
    Description:
    ------------
    Display a line chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/scales/logarithmic/line.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
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

  def timeseries(self, record: list = None, y_columns: list = None, x_axis: str = None,
                 profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
                 height: types.SIZE_TYPE = (330, "px"), options: dict = None,
                 html_code: str = None) -> graph.GraphChartJs.ChartLine:
    """
    Description:
    ------------
    Display a line chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/scales/logarithmic/line.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width:  Optional. The width of the component in the page, default (100, '%')
    :param height:  Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    line = self.line(record, y_columns, x_axis, profile, width, height, options, html_code)
    return line

  def pie(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
          width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
          html_code: str = None) -> graph.GraphChartJs.ChartPie:
    """
    Description:
    ------------
    Display a pie chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/pie.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. To set the profiling
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
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

  def donut(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
            html_code: str = None) -> graph.GraphChartJs.ChartPie:
    """
    Description:
    ------------
    Display a donut chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/doughnut.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    dfl_options = {
      'cutoutPercentage': 50, 'y_columns': y_columns or [], 'x_axis': x_axis,
      'commons': {"opacity": self.opacity}}
    if options is not None:
      dfl_options.update()
    pie_chart = graph.GraphChartJs.ChartPie(self.page, width, height, html_code, dfl_options, profile)
    pie_chart.colors(self.page.theme.charts)
    pie_chart.options.type = "doughnut"
    pie_chart._attrs["type"] = "doughnut"
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d["data"], d['label'], opacity=self.opacity)
    return pie_chart

  def area(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
           html_code: str = None) -> graph.GraphChartJs.ChartLine:
    """
    Description:
    ------------
    Display a area chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/area/line-stacked.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
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

  def step(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
           html_code: str = None):
    """
    Description:
    ------------
    Display a step chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/scales/linear/step-size.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
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

  def bar(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
          width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
          html_code: str = None) -> graph.GraphChartJs.ChartBar:
    """
    Description:
    ------------
    Display a bar chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/scriptable/bar.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
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

  def custom(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
             html_code: str = None) -> graph.GraphChartJs.ChartExts:
    """
    Description:
    ------------
    Display a bar chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/scriptable/bar.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
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
          raise ValueError(text % (options['npm_path'].replace("\\", "/"), options['npm']))

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

  def hbar(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
           html_code: str = None) -> graph.GraphChartJs.ChartHBar:
    """
    Description:
    ------------
    Display a horizontal bar chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/scriptable/bar.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {"opacity": self.opacity}})
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    if self.page.imports.pkgs.chart_js.version[0].startswith("2"):
      bar_chart = graph.GraphChartJs.ChartHBar(self.page, width, height, html_code, options, profile)
    else:
      bar_chart = graph.GraphChartJs.ChartBar(self.page, width, height, html_code, options, profile)
      bar_chart.options.indexAxis = 'y'
    bar_chart.colors(self.page.theme.charts)
    bar_chart.labels(data['labels'])
    bar_chart.options.scales.y_axis().ticks.beginAtZero = True
    for i, d in enumerate(data['datasets']):
      bar_chart.add_dataset(d["data"], d['label'])
    return bar_chart

  def multi(self, kind: str, record: list = None, y_columns: list = None, x_axis: str = None,
            profile: types.PROFILE_TYPE = None, options: dict = None, width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (330, "px"), html_code: str = None) -> graph.GraphChartJs.ChartBar:
    """
    Description:
    ------------
    Display a multi chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/combo-bar-line.html

    Attributes:
    ----------
    :param kind: The chart type
    :param record: Optional. The Python list of dictionaries
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
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

  def scatter(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
              html_code: str = None) -> graph.GraphChartJs.ChartScatter:
    """
    Description:
    ------------
    Display a scatter chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/scatter/basic.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
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

  def bubble(self, record: list = None, y_columns: list = None, x_axis: str = None, r_values: list = None,
             profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (330, "px"), options: dict = None,
             html_code: str = None) -> graph.GraphChartJs.ChartBubble:
    """
    Description:
    ------------
    Display a bubble chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/scriptable/bubble.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param r_values: Optional.
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
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

  def polar(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
            options: dict = None, html_code: str = None) -> graph.GraphChartJs.ChartPolar:
    """
    Description:
    ------------
    Display a bubble chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/polar-area.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
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

  def radar(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
            html_code: str = None) -> graph.GraphChartJs.ChartRadar:
    """
    Description:
    ------------
    Display a bubble chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.chartjs.org/samples/latest/charts/radar.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
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

  def fabric(self, profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (330, "px"), options: dict = None,
             html_code: str = None) -> graph.GraphChartJs.Fabric:
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    options = options or {}
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options.update({'y_columns': [], 'x_axis': "", 'commons': {"opacity": self.opacity}})
    component = graph.GraphChartJs.Fabric(self.page, width, height, html_code, options, profile)
    return component

  def treemap(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
              html_code: str = None) -> graph.GraphChartJs.ChartTreeMap:
    """
    Description:
    ------------
    Display a treemap chart from ChartJs.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://chartjs-chart-treemap.pages.dev/usage.html

    Attributes:
    ----------
    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {"opacity": self.opacity}})
    data = self.page.data.chartJs.y(record, y_columns, x_axis)
    treemap_chart = graph.GraphChartJs.ChartTreeMap(self.page, width, height, html_code, options, profile)
    treemap_chart.colors(self.page.theme.charts)
    treemap_chart.labels(data['labels'])
    treemap_chart.options.scales.y_axis().display = False
    for i, d in enumerate(data['datasets']):
      treemap_chart.add_dataset(d["data"], d['label'])
      treemap_chart.datasets[-1].labels.display = True
      treemap_chart.datasets[-1].labels.formatter(data['labels'])
      treemap_chart.datasets[-1].backgrounds(Colors.color_from_raw(self.page.theme.notch(), d["data"]))
    return treemap_chart
