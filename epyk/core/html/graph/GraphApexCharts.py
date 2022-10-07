#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives
from epyk.core.css import Colors
from epyk.core.html import Html
from epyk.core.html.options import OptChartApex
from epyk.core.js.packages import JsApexChart
from epyk.core.js import JsUtils


class ApexActivePoints:

  def __init__(self, chart_id: str, i: int, page: primitives.PageModel):
    self.chartId = chart_id
    self.page = page
    self.num = i or self.index

  @property
  def index(self):
    """   Get the active series index.

    :return: A javaScript number.
    """
    return JsUtils.jsWrap("config.seriesIndex")

  @property
  def config(self):
    """   Get the event / chart detailed configuration.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    :return: A Javascript dictionary.
    """
    return JsUtils.jsWrap("config")

  @property
  def datasetLabel(self):
    """   Return the name of the selected dataset.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    :return: A Javascript string
    """
    return JsUtils.jsWrap("config.config.series[%s].name" % self.num)

  @property
  def dataset(self):
    """   Return the selected dataset.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    :return: A Javascript dictionary
    """
    return JsUtils.jsWrap("config.config.series[%s]" % self.num)

  @property
  def value(self):
    """   Return the value for the selected point of the dataset.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    :return:
    """
    return JsUtils.jsWrap("config.config.series[%s].data[%s]" % (self.num, self.dataPointIndex))

  @property
  def label(self):
    """   Return the x label for the selected point.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    :return: A Javascript object.
    """
    return JsUtils.jsWrap("config.globals.categoryLabels[%s]" % self.dataPointIndex)

  @property
  def dataPointIndex(self):
    """   Get the index of the selected point.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    :return: A Javascript number
    """
    return JsUtils.jsWrap("config.dataPointIndex")

  @property
  def event(self):
    """   Get the original JavaScript event object.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    :return: A JavaScript event object.
    """
    return JsUtils.jsWrap("event")

  @property
  def chartContext(self):
    """   Get the full chart context.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    :return: A Javascript dictionary
    """
    return JsUtils.jsWrap("chartContext")


class Chart(Html.Html):
  name = 'ApexCharts'
  requirements = ('apexcharts', )
  _option_cls = OptChartApex.OptionsLine

  def __init__(self,  page: primitives.PageModel, width, height, html_code, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                css_attrs={"width": width, "height": height})
    self.options.chart.height = height[0]
    self.options.yaxis.labels.formatters.toNumber()
    self.style.css.margin_top = 10
    self.chartId = "%s_obj" % self.htmlCode

  def activePoints(self, i: int = None):
    """   The current active points selected by an event on a chart.

    Usage::

        library = "apex"
        kind = "line"
        c = page.ui.charts.plot(library, data.to_dict('records'), kind=kind, y=["Value"], x="Year", height=(500, "px"))

        c.click([
          page.js.console.log(c.activePoints().label)
        ])

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    :param int i: Optional. The series index. Default it is the series clicked.
    """
    return ApexActivePoints(self.chartId, i, self.page)

  @property
  def shared(self) -> OptChartApex.OptionsChartSharedApex:
    """   All the common properties shared between all the charts.
    This will ensure a compatibility with the plot method.

    Usage::

      line = page.ui.charts.chartJs.bar()
      line.shared.x_label("x axis")
    """
    return OptChartApex.OptionsChartSharedApex(self)

  def click(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """   Add a click event to the Apex chart.

    Related Pages:

      https://apexcharts.com/docs/options/chart/events/

    :param js_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.options.chart.events.click(js_funcs)
    return self

  def zoomable(self, flag: bool = True):
    """   Set the chart zoomable.

    :param bool flag: Optional. Add the zoom option to the chart.
    """
    if flag:
      self.options.chart.zoom.type = "x"
      self.options.chart.zoom.enabled = True
      self.options.chart.zoom.autoScaleYaxis = True
    else:
      self.options.chart.zoom.enabled = False

  def colors(self, hex_values: list):
    """   Set the colors of the chart.

    hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
    If the background colors are not specified they will be deduced from the colors list changing the opacity.

    Usage::

      line = page.ui.charts.apex.line(height=250)
      line.colors(["#FFA500", "#FF7F50"])

    :param list hex_values: An array of hexadecimal color codes.
    """
    line_colors, bg_colors = [], []
    for h in hex_values:
      if h.upper() in Colors.defined:
        h = Colors.defined[h.upper()]['hex']
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
      if hasattr(rec, "backgroundColor"):
        rec.backgroundColor = self.options.background_colors[i]
        rec.borderColor = self.options.colors[i]
        rec.borderWidth = 1

  @property
  def js(self) -> JsApexChart.ApexChart:
    """   The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    Usage::

    :return: A Javascript Dom object functions.

    :rtype: JsApexChart.ApexChart
    """
    if self._js is None:
      self._js = JsApexChart.ApexChart(selector="window['%s']" % self.chartId, component=self, page=self.page)
    return self._js

  @property
  def options(self) -> OptChartApex.OptionsLine:
    """   Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartApex.OptionsLine
    """
    return super().options

  def labels(self, labels):
    """   Set the labels of the different series in the chart.

    Usage::


    :param labels: List. An array of labels.
    """
    self.options.xaxis.categories = labels
    return self

  def add_dataset(self, data, label="", colors=None, opacity=None, kind=None):
    """   

    :param data: List. The list of points (float).
    :param label: List. Optional. The list of points (float).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
    """
    series = self.options.add_series()
    series.name = label
    series.data = data
    return series

  _js__builder__ = '''
      if(data.python){
        result = {series: [], labels: data.labels};
        data.datasets.forEach(function(dataset, i){
          if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
          if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
          if(typeof dataset.hoverBackgroundColor === "undefined"){
            dataset.hoverBackgroundColor = options.background_colors[i]};
          if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
          dataset.name = data.series[i];
          result.series.push(dataset) })
      } else{
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
    Update the chart with context and / or data changes.

    Usage::

    :param data: Dictionary of dictionary. The full datasets object expected by ChartJs.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id: String. Not used.
    """
    if data is not None:
      js_convertor = "%s%s" % (self.name, self.__class__.__name__)
      self.page.properties.js.add_constructor(
        js_convertor, "function %s(data, options){%s}" % (js_convertor, self._js__builder__))
      profile = self.with_profile(profile, event="Builder", element_id=self.chartId)
      if profile:
        js_func_builder = JsUtils.jsConvertFncs(
          ["var result = %s(data, options)" % js_convertor], toStr=True, profile=profile)
        js_convertor = "(function(data, options){%s; return result})" % js_func_builder
      return "%s.updateOptions(%s(%s, %s)); %s.update()" % (
        "window['%s']" % self.chartId, js_convertor, JsUtils.jsConvertData(data, None),
        self.options.config_js(options).toStr(), self.chartId)

    return JsUtils.jsConvertFncs([self.js.new(
      self.dom.varId, self.options.config_js(options), "window['%s']" % self.chartId), self.js.render()],
      toStr=True, profile=profile)

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())


class Bar(Chart):
  _option_cls = OptChartApex.OptionsBar
  name = 'ApexCharts'

  @property
  def options(self) -> OptChartApex.OptionsBar:
    """   Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartApex.OptionsBar
    """
    return super().options


class Area(Chart):
  _option_cls = OptChartApex.OptionsArea

  @property
  def options(self) -> OptChartApex.OptionsArea:
    """   Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartApex.OptionsArea
    """
    return super().options


class Pie(Chart):
  _option_cls = OptChartApex.OptionsPie

  @property
  def options(self) -> OptChartApex.OptionsPie:
    """   Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartApex.OptionsPie
    """
    return super().options


class RadialBar(Chart):
  _option_cls = OptChartApex.OptionsPie

  _js__builder__ = '''
    if (typeof data === 'number'){data = {values: [data]}}
    else {
      if (typeof data.values === 'number'){
        data.values = [data.values]; if (typeof data.labels !== 'undefined'){data.labels = [data.labels]}}}
    result = {series: data.values};
    if (typeof data.labels !== 'undefined'){result.labels = data.labels}
    return result'''

  @property
  def options(self) -> OptChartApex.OptionsPie:
    """   Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartApex.OptionsPie
    """
    return super().options


class Bubble(Chart):
  _option_cls = OptChartApex.OptionsArea

  _js__builder__ = '''
       if(data.python){
         result = {series: [], labels: data.labels};
         data.datasets.forEach(function(dataset, i){
           if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
           if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
           if(typeof dataset.hoverBackgroundColor === "undefined"){
             dataset.hoverBackgroundColor = options.background_colors[i]};
           if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
           dataset.name = data.series[i];
           result.series.push(dataset) })
       } else{
         var temp = {}; var labels = []; var uniqLabels = {}; 
         options.y_columns.forEach(function(series){temp[series] = {}});
         data.forEach(function(rec){ 
           options.y_columns.forEach(function(name){ 
           if(rec[name] !== undefined){
             if (!(rec[options.x_axis] in uniqLabels)){labels.push(rec[options.x_axis]); 
             uniqLabels[rec[options.x_axis]] = true}; 
             temp[name][rec[options.x_axis]] = rec[name]}})
         }); 
         result = {series: [], type: options.chart.type };
         options.y_columns.forEach(function(series, i){
             dataSet = {label: series, data: [], color: options.colors[i], type: options.chart.type, borderWidth: 2, backgroundColor: 'rgb(255, 99, 132)'};
             if ((typeof options.attrs !== 'undefined') && (typeof options.attrs[series] !== 'undefined')){
               for(var attr in options.attrs[series]){dataSet[attr] = options.attrs[series][attr]}}
             else if(typeof options.commons !== 'undefined'){
               for(var attr in options.commons){dataSet[attr] = options.commons[attr]}}
               labels.forEach(function(x){
                 if (typeof temp[series][x] === "undefined"){dataSet.data.push(null)} 
                 else {dataSet.data.push({x: x, r: 100, y: temp[series][x]})}}); 
           result.series.push(dataSet)})
       }; return result;
       '''

  @property
  def options(self) -> OptChartApex.OptionsArea:
    """   Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartApex.OptionsArea
    """
    return super().options
