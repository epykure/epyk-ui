#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.fwk.toast.options import OptToastCharts
from epyk.fwk.toast.js import JsToastCharts
from epyk.core.data.DataPy import SelectionBox


class Chart(Html.Html):
  name = 'ToastCharts'
  requirements = ('@toast-ui/chart', )
  _option_cls = OptToastCharts.OptionsCharts

  def __init__(self, page, width, height, html_code, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(
      page, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.config.usageStatistics = False
    self.style.css.position = "relative"
    self.config.responsive.animation.duration = 300
    self.config.chart.width = "auto"
    self.config.chart.height = "auto"

  _js__builder__ = '''
    options.el = htmlObj; window[htmlObj.id] = new toastui.Chart.lineChart(options)'''

  @property
  def parsers(self):
    """
    Set of functions to parse the data.
    """
    return SelectionBox

  @property
  def shared(self) -> OptToastCharts.OptToastChartsShared:
    """   All the common properties shared between all the charts.
    This will ensure a compatibility with the plot method.

    Usage::

      line = page.ui.charts.chartJs.bar()
      line.shared.x_label("x axis")
    """
    return OptToastCharts.OptToastChartsShared(self)

  @property
  def var(self):
    """   Return the calendar javaScript object reference after the builder.
    """
    return "window['%s']" % self.htmlCode

  @property
  def data(self):
    """   Return the data section from the main python options.
    """
    return self.options.data

  @data.setter
  def data(self, parsed_values):
    self.options.y_columns = self.options.y_columns if self.options.y_columns else ["name"]
    self.options.x_axis = self.options.x_axis if self.options.x_axis is not None else "value"
    result = self.page.data.c3.y(parsed_values or [], self.options.y_columns, self.options.x_axis, self.options)
    if result["series"]:
      for i, s in enumerate(result["series"]):
        self.options.data.add_series(s, result["datasets"][i])
      self.options.data.categories = result["labels"]
    self.config.legend.visible = False

  @property
  def config(self):
    """   Returns the options option for the chart.
    """
    return self.options.config

  @property
  def js(self) -> JsToastCharts.Charts:
    """   Javascript module of the items in the menu.

    :rtype: JsToastCharts.Charts
    """
    if self._js is None:
      self._js = JsToastCharts.Charts(component=self, js_code=self.var, page=self.page)
    return self._js

  @property
  def options(self) -> OptToastCharts.OptionsCharts:
    """   All the component options.

    :rtype: OptToastCharts.OptionsCharts
    """
    return super().options

  def colors(self, hex_values):
    """   Set the colors of the different series.
 
    :param hex_values: Array. The color codes.
    """
    self.config.theme.series.colors = hex_values

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())


class ChartArea(Chart):
  name = 'ToastChartsArea'
  _js__builder__ = '''options.el = htmlObj; window[htmlObj.id] = new toastui.Chart.areaChart(options)'''


class ChartColumn(Chart):
  name = 'ToastChartsColumn'
  _js__builder__ = '''
  options.el = htmlObj; window[htmlObj.id] = new toastui.Chart.columnChart(options)'''


class ChartBar(Chart):
  name = 'ToastChartsBar'
  _js__builder__ = '''options.el = htmlObj; window[htmlObj.id] = new toastui.Chart.barChart(options)'''


class ChartScatter(Chart):
  name = 'ToastChartsScatter'
  _js__builder__ = '''options.el = htmlObj; window[htmlObj.id] = new toastui.Chart.scatterChart(options)'''


class ChartBubble(Chart):
  name = 'ToastChartsBubble'
  _js__builder__ = '''options.el = htmlObj; window[htmlObj.id] = new toastui.Chart.bubbleChart(options)'''


class ChartPie(Chart):
  name = 'ToastChartsPie'
  _option_cls = OptToastCharts.OptionsChartsPie
  _js__builder__ = '''options.el = htmlObj; window[htmlObj.id] = new toastui.Chart.pieChart(options)'''

  @property
  def options(self):
    """   

    :rtype: OptToastCharts.OptionsChartsPie
    """
    return super().options


class ChartRadar(Chart):
  name = 'ToastChartsRadar'
  _js__builder__ = '''options.el = htmlObj; window[htmlObj.id] = new toastui.Chart.radarChart(options)'''


class ChartRadialBar(Chart):
  name = 'ToastChartsRadialBar'
  _js__builder__ = '''options.el = htmlObj; window[htmlObj.id] = new toastui.Chart.radialBarChart(options)'''

