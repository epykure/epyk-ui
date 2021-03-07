#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css import Colors
from epyk.core.html import Html
from epyk.core.html.options import OptChartApex
from epyk.core.js.packages import JsApexChart
from epyk.core.js import JsUtils


class Chart(Html.Html):
  name = 'ApexCharts'
  requirements = ('apexcharts', )
  _option_cls = OptChartApex.OptionsLine

  def __init__(self,  report, width, height, html_code, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, [], html_code=html_code, profile=profile, options=options,
                                css_attrs={"width": width, "height": height})
    self.options.chart.height = height[0]
    self.options.yaxis.labels.formatters.toNumber()
    self.style.css.margin_top = 10
    self.chartId = "%s_obj" % self.htmlCode

  def click(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs:
    :param profile:
    :param source_event:
    :param on_ready:
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.options.chart.events.click(js_funcs)
    return self

  def zoomable(self, flag=True):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param flag:
    """
    if flag:
      self.options.chart.zoom.type = "x"
      self.options.chart.zoom.enabled = True
      self.options.chart.zoom.autoScaleYaxis = True
    else:
      self.options.chart.zoom.enabled = False

  def colors(self, hex_values):
    """
    Description:
    -----------
    Set the colors of the chart.

    hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
    If the background colors are not specified they will be deduced from the colors list changing the opacity.

    Usage:
    -----

    Attributes:
    ----------
    :param hex_values: List. An array of hexadecimal color codes.
    """
    line_colors, bg_colors = [], []
    for h in hex_values:
      if not isinstance(h, tuple):
        line_colors.append(h)
        bg_colors.append("rgba(%s, %s, %s, %s" % (
          Colors.getHexToRgb(h)[0], Colors.getHexToRgb(h)[1],
          Colors.getHexToRgb(h)[2], self.options.opacity))
      else:
        line_colors.append(h[0])
        bg_colors.append(h[0])
    self.options.colors = line_colors
    self.options.background_colors = bg_colors
    for i, rec in enumerate(self.options.all_series):
      rec.backgroundColor = self.options.background_colors[i]
      rec.borderColor = self.options.colors[i]
      rec.borderWidth = 1

  @property
  def js(self):
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    Usage:
    -----

    :return: A Javascript Dom object functions.

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
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartApex.OptionsLine
    """
    return super().options

  _js__builder__ = '''
      if(data.python){
        result = {series: [], labels: data.labels};
        data.datasets.forEach(function(rec, i){
          result.series.push({label: data.series[i], data: rec})})}
      else{
        var temp = {}; var labels = []; var uniqLabels = {}; 
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){ 
          if(rec[name] !== undefined){
            if (!(rec[options.x_axis] in uniqLabels)){labels.push(rec[options.x_axis]); 
            uniqLabels[rec[options.x_axis]] = true}; 
            temp[name][rec[options.x_axis]] = rec[name]}})
        });
        result = {series: [], labels: labels, xaxis: {}};
        options.y_columns.forEach(function(series, i){
            dataSet = {label: series, data: []};
            if ((typeof options.attrs !== 'undefined') && (typeof options.attrs[series] !== 'undefined')){
              for(var attr in options.attrs[series]){dataSet[attr] = options.attrs[series][attr]}}
            else if(typeof options.commons !== 'undefined'){
              for(var attr in options.commons){dataSet[attr] = options.commons[attr]}}
              labels.forEach(function(x){
                if (typeof temp[series][x] === "undefined"){dataSet.data.push(null)} 
                else {dataSet.data.push({x: x, y: temp[series][x]})}}); 
          result.series.push(dataSet)})
      };
      return result;
      '''

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    """
    if data is not None:
      js_convertor = "%s%s" % (self.name, self.__class__.name)
      self.page.properties.js.add_constructor(
        js_convertor, "function %s(data, options){%s}" % (js_convertor, self._js__builder__))
      profile = self.with_profile(profile, event="Builder", element_id=self.chartId)
      if profile:
        js_func_builder = JsUtils.jsConvertFncs(
          ["var result = %s(data, options)" % js_convertor], toStr=True, profile=profile)
        js_convertor = "(function(data, options){%s; return result})" % js_func_builder
      return "%s.updateOptions(%s(%s, %s))" % (
        "window['%s']" % self.chartId, js_convertor, JsUtils.jsConvertData(data, None), self.options.config_js(options).toStr())

    return JsUtils.jsConvertFncs([self.js.new(
      self.dom.varId, self.options.config_js(options), "window['%s']" % self.chartId), self.js.render()],
      toStr=True, profile=profile)

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class Bar(Chart):
  _option_cls = OptChartApex.OptionsBar

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartApex.OptionsBar
    """
    return super().options


class Area(Chart):
  _option_cls = OptChartApex.OptionsArea

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartApex.OptionFill
    """
    return super().options


class Pie(Chart):
  _option_cls = OptChartApex.OptionsPie

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartApex.OptionsPie
    """
    return super().options
