#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from typing import Dict, List

from epyk.core.py import types
from epyk.core.html import graph
from epyk.interfaces import Arguments
from epyk.core.js import Imports
from epyk.core.css import Colors
from epyk.core.js.packages import until_version


class ChartJs:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "ChartJs"
    self.opacity = 0.6

  def set_version(self, v: str):
    """Change the version of the chartJs package.
    Use **self.page.imports.pkgs.chart_js.version** to get the current version.

    Usage::

      page.ui.charts.chartJs.set_version("2.9.4").line(languages, y_columns=['change'], x_axis="name")

    :param v: The version number
    """
    if v.startswith("2"):
      self.page.imports.setVersion("chart.js", v, js={'register': {
        'alias': 'Chart', 'module': 'Chart.min', 'npm': 'chart.js', 'npm_path': 'dist'}, 'modules': [
        {'script': 'Chart.min.js', 'node_path': 'dist/', 'path': 'Chart.js/%(version)s/',
         'cdnjs': Imports.CDNJS_REPO}]}, css={'modules': [
        {'script': 'Chart.min.css', 'node_path': 'dist/', 'path': 'Chart.js/%(version)s/',
         'cdnjs': Imports.CDNJS_REPO}]})
    elif v.startswith("3") or v.startswith("4"):
      self.page.imports.setVersion("chart.js", v, js={'register': {
        'alias': 'chart', 'module': 'chart.min', 'npm': 'chart.js', 'npm_path': 'dist'}, 'modules': [
        {'script': 'chart.min.js', 'node_path': 'dist/', 'path': 'Chart.js/%(version)s/',
         'cdnjs': Imports.CDNJS_REPO}]}, css=False)
    return self

  def plot(self, record: list = None, y: list = None, x: str = None, kind: str = "line",
           profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
           height: types.SIZE_TYPE = (330, "px"), options: dict = None,
           html_code: str = None, **kwargs
           ) -> graph.GraphChartJs.Chart:
    """Generic way to define ChartJs charts.

    :tags:
    :categories:

    `ChartJs <https://www.chartjs.org/>`_

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
           html_code: str = None, **kwargs
           ) -> graph.GraphChartJs.ChartLine:
    """Display a line chart from ChartJs.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 30)
      chart = page.ui.charts.chartJs.line(data, y_columns=[3, 4], x_axis='x')

    `ChartJs <https://www.chartjs.org/>`_
    `Line <https://www.chartjs.org/samples/latest/scales/logarithmic/line.html>`_

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
                 html_code: str = None, **kwargs
                 ) -> graph.GraphChartJs.ChartLine:
    """Display a line chart from ChartJs.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import urls as data_urls

      data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
      ts = page.ui.charts.chartJs.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

    `ChartJs <https://www.chartjs.org/>`_
    `Line <https://www.chartjs.org/samples/latest/scales/logarithmic/line.html>`_

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
    """Display a pie chart from ChartJs.

    :tags:
    :categories:

    Usage::

      page = pk.Page()
      df = pd.DataFrame({'Sales': [5000, 1222, 2000], 'Other': [500, 122, 200]}, index=['TV', 'Smartphones', 'DVD'])
      chart1 = page.ui.charts.chartJs.pie(df.to_dict("records"), y_columns=['Sales'], x_axis="Other")
      chart1.click([
        page.js.console.log(chart1.dom.active()),
        chart1.build([{"Sales": 10, "Other": "A"}, {"Sales": 15, "Other": "B"}])])

    `Pie <https://www.chartjs.org/samples/latest/charts/pie.html>`_

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
            html_code: str = None, **kwargs
            ) -> graph.GraphChartJs.ChartPie:
    """Display a donut chart from ChartJs.

    :tags:
    :categories:

    Usage::

      page = pk.Page()
      df = pd.DataFrame({'Sales': [5000, 1222, 2000], 'Other': [500, 122, 200]}, index=['TV', 'Smartphones', 'DVD'])
      chart1 = page.ui.charts.chartJs.donut(df.to_dict("records"), y_columns=['Sales'], x_axis="Other")
      chart1.click([
        page.js.console.log(chart1.dom.active()),
        chart1.build([{"Sales": 10, "Other": "A"}, {"Sales": 15, "Other": "B"}])])

    `Doughnut <https://www.chartjs.org/samples/latest/charts/doughnut.html>`_

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
    pie_chart.type = "doughnut"
    pie_chart.labels(data['labels'])
    for i, d in enumerate(data['datasets']):
      pie_chart.add_dataset(d["data"], d['label'], opacity=self.opacity)
    return pie_chart

  def area(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"), options: dict = None,
           html_code: str = None, **kwargs
           ) -> graph.GraphChartJs.ChartLine:
    """Display a area chart from ChartJs.

    :tags:
    :categories:

    `Line Stacked <https://www.chartjs.org/samples/latest/charts/area/line-stacked.html>`_

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
           html_code: str = None, **kwargs
           ):
    """Display a step chart from ChartJs.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 30)
      chart = page.ui.charts.chartJs.step(data, y_columns=list(range(4)), x_axis='x')
      chart.options.showLines = True

    `Step size <https://www.chartjs.org/samples/latest/scales/linear/step-size.html>`_

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
    """Display a bar chart from ChartJs.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 30)
      page.ui.charts.chartJs.bar(data, y_columns=[1, 2, 3], x_axis='x')

    `Bar <https://www.chartjs.org/samples/latest/scriptable/bar.html>`_

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
             html_code: str = None, **kwargs
             ) -> graph.GraphChartJs.ChartExts:
    """Display a bespoke chart from ChartJs.
    It is important to get a NodeJs with the extra packages installed to use this interface.
    This will not download the external required resources and it will rely on the setup of the Node server.

    :tags:
    :categories:

    Usage::

      c = page.ui.charts.chartJs.custom(randoms.languages, y_columns=["rating", 'change'], x_axis='name',
                options={"type": 'sankey', 'npm': 'chartjs-chart-sankey',
                         'npm_path': '../NodeJs/node_modules'})

    `Custom <https://www.chartjs.org/samples/latest/scriptable/bar.html>`_

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
           html_code: str = None, **kwargs
           ) -> graph.GraphChartJs.ChartHBar:
    """Display a horizontal bar chart from ChartJs.

    :tags:
    :categories:

    Usage::

      from epyk.mocks import randoms

      data = randoms.getSeries(5, 30)
      chart = page.ui.charts.chartJs.hbar(data[:5], y_columns=list(range(4)), x_axis='x')
      chart.click([page.js.console.log(chart.js.value)])

    `Horizontal Bar <https://www.chartjs.org/samples/latest/scriptable/bar.html>`_

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
            height: types.SIZE_TYPE = (330, "px"), html_code: str = None, **kwargs
            ) -> graph.GraphChartJs.ChartBar:
    """Display a multi chart from ChartJs.

    :tags:
    :categories:

    `Combo Bar Line <https://www.chartjs.org/samples/latest/charts/combo-bar-line.html>`_

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
              html_code: str = None, **kwargs
              ) -> graph.GraphChartJs.ChartScatter:
    """Display a scatter chart from ChartJs.

    :tags:
    :categories:

    `Basic <https://www.chartjs.org/samples/latest/charts/scatter/basic.html>`_

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
             html_code: str = None
             ) -> graph.GraphChartJs.ChartBubble:
    """Display a bubble chart from ChartJs.

    :tags:
    :categories:

    `Bubble <https://www.chartjs.org/samples/latest/scriptable/bubble.html>`_

    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param r_values: Optional. Set the r for the points on the chart
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'z_columns': None, 'rDim': r_values,
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
            options: dict = None, html_code: str = None, **kwargs
            ) -> graph.GraphChartJs.ChartPolar:
    """Display a bubble chart from ChartJs.

    :tags:
    :categories:

    `Polar Area <https://www.chartjs.org/samples/latest/charts/polar-area.html>`_

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
            html_code: str = None, **kwargs
            ) -> graph.GraphChartJs.ChartRadar:
    """Display a bubble chart from ChartJs.

    :tags:
    :categories:

    `Radar <https://www.chartjs.org/samples/latest/charts/radar.html>`_

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
             html_code: str = None, **kwargs
             ) -> graph.GraphChartJs.Fabric:
    """

    :tags:
    :categories:

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

  def treemap(self, record: list = None, y_columns: list = None, x_axis: str = None, groups: list = None,
              profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
              height: types.SIZE_TYPE = (330, "px"), options: dict = None,
              html_code: str = None, **kwargs
              ) -> graph.GraphChartJs.ChartTreeMap:
    """Display a treemap chart from ChartJs.

    :tags:
    :categories:

    `Usage <https://chartjs-chart-treemap.pages.dev/usage.html>`_

    :param record: Optional. The list of dictionaries with the input data
    :param y_columns: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param groups: Optional. The columns corresponding to a key in the dictionaries in the record
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    prev_version = until_version(self.page.imports.pkgs.chart_js.version, "3.8.0", included=False)
    if prev_version[0]:
      self.page.imports.pkgs.chart_js_extensions.treemap.version = "2.0.1"
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options.update({'y_columns': y_columns or [], "groups": groups,
      'commons': {
        "opacity": self.opacity, "colors": {"base": self.page.theme.notch(), "light": self.page.theme.notch(-3)}}})
    groups = groups or x_axis
    if groups is not None:
      if len(groups) == 1:
        options["x_axis"] = groups[0]
      else:
        options["groups"] = groups
    data = self.page.data.chartJs.y(record, y_columns, None)
    treemap_chart = graph.GraphChartJs.ChartTreeMap(self.page, width, height, html_code, options, profile)
    treemap_chart.colors(self.page.theme.charts)
    treemap_chart.labels(data['labels'])
    treemap_chart.options.scales.y_axis().display = False
    for i, d in enumerate(data['datasets']):
      if "data" not in d:
        treemap_chart.add_dataset(d, data['labels'][0], kind="tree")
        treemap_chart.datasets[-1].labels.display = True
        treemap_chart.datasets[-1].groups = groups
        treemap_chart.datasets[-1].backgroundColor = '''function(ctx) {var item = ctx.dataset.data[ctx.dataIndex];
if (item){
  var a = item.v / (item.gs || item.s) / 2 + 0.5;
  if(item.l === 0){return Chart.helpers.color("%s").alpha(a).rgbString()}
  if(item.l === 1){return Chart.helpers.color("white").alpha(0.3).rgbString()}
  else{return Chart.helpers.color("%s").alpha(a).rgbString()}}
}''' % (options['commons']["colors"]["light"], options['commons']["colors"]["base"])
        treemap_chart.plugins.legend.display = False
      else:
        treemap_chart.add_dataset(d["data"], d['label'])
        treemap_chart.datasets[-1].labels.display = True
        treemap_chart.datasets[-1].labels.formatter(data['labels'])
        treemap_chart.datasets[-1].backgrounds(Colors.color_from_raw(self.page.theme.notch(), d["data"]))
    return treemap_chart

  def sankey(self, record: List[dict] = None, label: str = "", profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
             options: dict = None, html_code: str = None, **kwargs
  ) -> graph.GraphChartJs.ChartSankey:
    """To create a sankey chart, include chartjs-chart-sankey.js after chart.js and then create the chart by setting the
    type attribute to 'sankey'

    Usage::

      data = [{"from": 'a', "to": 'b', "flow": 10},
              {"from": 'a', "to": 'c', "flow": 5},]
      chart = page.ui.charts.chartJs.sankey(data, label="series")
      chart.click(chart.build([{"from": 'a', "to": 'b', "flow": 10}]))

    `Sankey <https://npm.io/package/chartjs-chart-sankey>`_
    """
    sankey_chart = graph.GraphChartJs.ChartSankey(self.page, width, height, html_code, options, profile)
    sankey_chart.colors(self.page.theme.charts)
    sankey_chart.add_dataset(record, label)
    sankey_chart.options.responsive = True
    return sankey_chart

  def venn(self):
    raise NotImplementedError()

  def matrix(self, record: list = None, y_columns: list = None, x_axis: str = None, profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
             options: dict = None, html_code: str = None, **kwargs
             ) -> graph.GraphChartJs.ChartMatrix:
    """Display a matrix chart from ChartJs.

    :tags:
    :categories:

    `Matrix >https://github.com/kurkle/chartjs-chart-matrix>`_
    `ChartJs <https://chartjs-chart-matrix.pages.dev/>`_

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
    matrix_chart = graph.GraphChartJs.ChartMatrix(self.page, width, height, html_code, options, profile)
    matrix_chart.options.scales.x.display = False
    matrix_chart.options.scales.x.offset = False
    matrix_chart.options.scales.x.min = 0.5
    matrix_chart.options.scales.x.max = 0.5
    matrix_chart.options.scales.y.display = False
    matrix_chart.options.scales.y.offset = False
    matrix_chart.options.scales.y.min = 0.5
    matrix_chart.options.scales.y.max = 0.5
    matrix_chart.colors(self.page.theme.charts)
    matrix_chart.labels(data['labels'])
    matrix_chart.options.scales.y_axis().display = False
    for i, d in enumerate(data['datasets']):
      matrix_chart.add_dataset(d["data"], d['label'])
    return matrix_chart

  def wordcloud(self, record: list = None, y_columns: list = None, x_axis: str = None,
                profile: types.PROFILE_TYPE = None,
                width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
                options: dict = None, html_code: str = None, **kwargs
                ) -> graph.GraphChartJs.ChartWordCloud:
    """Chart.js module for charting word or tag clouds. Adding new chart type: wordCloud.

    :tags:
    :categories:

    Usage::

      fake = Faker()
      rec = [{"Sales": random.randint(1, 100), "Other": fake.name()} for _ in range(40)]
      chart1 = page.ui.charts.chartJs.wordcloud(rec, y_columns=['Sales'], x_axis="Other")
      page.ui.button("click").click([
        chart1.build([{"Sales": 40, "Other": 30}, {"Sales": 1, "Other": 1}, {"Sales": 15, "Other": 5}])])

    `WordCloud <https://github.com/sgratzl/chartjs-chart-wordcloud>`_

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
    wc_chart = graph.GraphChartJs.ChartWordCloud(self.page, width, height, html_code, options, profile)
    wc_chart.colors(self.page.theme.charts)
    wc_chart.labels(data['labels'])
    wc_chart.options.scales.y_axis().display = False
    for i, d in enumerate(data['datasets']):
      wc_chart.add_dataset(d["data"], d['label'])
    return wc_chart

  def hierarchical(self, record: list = None, labels: list = None, profile: types.PROFILE_TYPE = None,
                   width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
                   options: dict = None, horizontal: bool = False, kind: str = "bar",
                   html_code: str = None, **kwargs
                   ) -> graph.GraphChartJs.ChartHyr:
    """Chart.js module for adding a new categorical scale which mimics a hierarchical tree.

    `Hierarchical <https://github.com/sgratzl/chartjs-plugin-hierarchical>`_
    `Deep Hierarchical <https://github.com/sgratzl/chartjs-plugin-hierarchical/blob/main/samples/deep_hierarchy.html>`_

    :param record: Optional. The list of dictionaries with the input data
    :param labels:
    :param profile: Optional. A flag to set the component performance storage
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param horizontal: Optional.
    :param kind: Optional.
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    hyr_chart = graph.GraphChartJs.ChartHyr(self.page, width, height, html_code, options, profile)
    hyr_chart._attrs["type"] = kind
    hyr_chart.colors(self.page.theme.charts)
    hyr_chart._data_attrs['labels'] = labels
    hyr_chart._datasets = record or []
    if horizontal:
      hyr_chart.options.scales.y.type = "hierarchical"
      hyr_chart.options.scales.y.padding = 0
      hyr_chart.options.scales.y.attributes = {"backgroundColor": 'gray'}
      hyr_chart.options.layout.paddings = {"left": 50}
    else:
      hyr_chart.options.scales.x.type = "hierarchical"
      hyr_chart.options.scales.x.attributes = {"backgroundColor": 'gray'}
      hyr_chart.options.layout.paddings = {"bottom": 60}
    hyr_chart.options.responsive = True
    return hyr_chart

