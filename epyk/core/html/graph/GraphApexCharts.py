#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.options import OptChartApex
from epyk.core.js.packages import JsApexChart
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class Chart(Html.Html):
  name = 'ApexCharts'
  requirements = ('apexcharts', )
  _options_type_cls = OptChartApex.OptionsLine

  def __init__(self,  report, width, height, htmlCode, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._options = self._options_type_cls(self, options)
    self.options.chart.height = height[0]
    self.options.yaxis.labels.formatters.toNumber()
    self.style.css.margin_top = 10
    self.chartId = "%s_obj" % self.htmlCode

  def click(self, js_funcs, profile=False, source_event=None, onReady=False):
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.options.chart.events.click(js_funcs)
    return self

  def zoomable(self, flag=True):
    if flag:
      self.options.chart.zoom.type = "x"
      self.options.chart.zoom.enabled = True
      self.options.chart.zoom.autoScaleYaxis = True
    else:
      self.options.chart.zoom.enabled = False

  @property
  def js(self):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsApexChart.ApexChart
    """
    if self._js is None:
      self._js = JsApexChart.ApexChart(selector="window['%s']" % self.chartId, src=self)
    return self._js

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptChartApex.OptionsLine
    """
    return self._options

  def build(self, data=None, options=None, profile=False):
    """
    """
    if options is not None:
      return self.js.updateOptions(self.options.config_js(options))

    if data is not None:
      return self.js.updateSeries(data)

    return JsUtils.jsConvertFncs([self.js.new(self.dom.varId, self.options.config_js(options), "window['%s']" % self.chartId), self.js.render()], toStr=True)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.build())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class Bar(Chart):
  _options_type_cls = OptChartApex.OptionsBar

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptChartApex.OptionsBar
    """
    return self._options


class Area(Chart):
  _options_type_cls = OptChartApex.OptionsArea

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptChartApex.OptionFill
    """
    return self._options


class Pie(Chart):
  _options_type_cls = OptChartApex.OptionsPie

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptChartApex.OptionsPie
    """
    return self._options
