#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from epyk.core.html import Html
from epyk.core.css import Colors
from epyk.core.html.options import OptPlotly

from epyk.core.py import types

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject

from epyk.core.js.packages import JsPlotly
from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name = 'Plotly'
  tag = "div"
  requirements = ('plotly.js', )
  _option_cls = OptPlotly.OptionConfig

  def __init__(self,  page, width, height, options, html_code, profile):
    self.seriesProperties, self.__chartJsEvents, self.height = {'static': {}, 'dynamic': {}}, {}, height[0]
    super(Chart, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                css_attrs={"width": width, "height": height})
    self._d3, self._attrs, self._traces, self._layout, self._options = None, None, [], None, None
    self.layout.autosize, self._labels = True, None
    if not height[0] is None:
      self.layout.height = height[0]

  @property
  def shared(self) -> OptPlotly.OptionsChartSharedPlotly:
    """All the common properties shared between all the charts.
    This will ensure a compatibility with the plot method.

    Usage::

      line = page.ui.charts.bb.bar()
      line.shared.x_label("x axis")
    """
    return OptPlotly.OptionsChartSharedPlotly(self)

  def click_legend(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """

    `Plotly Doc <https://plotly.com/javascript/plotlyjs-events/>`_

    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
    self.onReady("%s.on('plotly_legendclick', function(data) {%s})" % (
      self.dom.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, source_event: str = None,
            on_ready: bool = False):
    """The onclick event occurs when the user clicks on an element.

    `Plotly Doc <https://plotly.com/javascript/click-events/>`_

    :param js_funcs: A Javascript Python function
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console
    :param source_event: Optional. The source target for the event
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
    """
    self.onReady("%s.on('plotly_click', function(data) {%s})" % (
      self.dom.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def dblclick(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, source_event: str = None,
               on_ready: bool = False):
    """The onDblclick event occurs when the user double clicks on an element.

    `Plotly Doc <https://plotly.com/javascript/click-events/>`_

    :param js_funcs: A Javascript Python function
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console
    :param source_event: Optional. The source target for the event
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
    """
    self.onReady("%s.on('plotly_doubleclick', function(data) {%s})" % (
      self.dom.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def hover(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, source_event: str = None,
            on_ready: bool = False):
    """

    `Plotly Doc <https://plotly.com/javascript/hover-events/>`_

    :param js_funcs: A Javascript Python function
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console
    :param source_event: Optional. The source target for the event
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
    """
    self.onReady("%s.on('plotly_hover', function(data) {%s})" % (
      self.dom.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def unhover(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, source_event: str = None,
              on_ready: bool = False):
    """

    `Plotly Doc <https://plotly.com/javascript/hover-events/>`_

    :param js_funcs: A Javascript Python function
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console
    :param source_event: Optional. The source target for the event
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
    """
    self.onReady("%s.on('plotly_unhover', function(data) {%s})" % (
      self.dom.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  @property
  def data(self) -> OptPlotly.DataChart:
    if not self._traces:
      self.add_trace([])
    return self._traces[-1]

  @property
  def options(self) -> OptPlotly.OptionConfig:
    """Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.
    """
    return super().options

  def traces(self, i: int = None) -> OptPlotly.DataChart:
    if i is None:
      return self._traces[-1]

    return self._traces[i]

  def labels(self, values):
    self._labels = values

  def add_dataset(self, data, label, colors=None, opacity=None, kind=None):
    series = {"x": [], "y": []}
    for i, x in enumerate(self._labels):
      series["x"].append(x)
      series["y"].append(data[i])
    trace = self.add_trace(series, type=kind)
    current_trace = trace.traces()
    current_trace.name = label
    return current_trace

  _js__builder__ = '''
      if(data.python){
        result = [];
        data.datasets.forEach(function(values, i){
          dataSet = {x: [], y: [], name: data.series[i], type: options.type, mode: options.mode, marker: {}};
          if(typeof options.attrs !== undefined){ for(var attr in options.attrs){dataSet[attr] = options.attrs[attr]} };
          if(typeof options.marker !== undefined){
            for(var attr in options.marker){dataSet.marker[attr] = options.marker[attr]} };
          result.push(Object.assign(dataSet, values))
        }); 
      } else {
        var temp = {}; var labels = []; var uniqLabels = {}; var result = [] ;
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if(!(rec[options.x_column] in uniqLabels)){
                labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
              temp[name][rec[options.x_column]] = rec[name]}})});
        options.y_columns.forEach(function(series){
          dataSet = {x: [], y: [], name: series, type: options.type, mode: options.mode, marker: {}};
          if(typeof options.attrs !== undefined){ 
            for(var attr in options.attrs){dataSet[attr] = options.attrs[attr]} };
          if(typeof options.marker !== undefined){
            for(var attr in options.marker){dataSet.marker[attr] = options.marker[attr]} };
          labels.forEach(function(x, i){
            dataSet.x.push(x);
            if(temp[series][x] == undefined){dataSet.y.push(null)} else{dataSet.y.push(temp[series][x])}
          }); result.push(dataSet)})
      }; return result'''

  def colors(self, hex_values: List[str]):
    """Set the colors of the chart.

    hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
    If the background colors are not specified they will be deduced from the colors list changing the opacity.

    :param hex_values: An array of hexadecimal color codes.
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
    for i, rec in enumerate(self._traces):
      rec.fillcolor = self.options.background_colors[i]
      rec.line.color = self.options.colors[i]
      rec.marker.line.color = self.options.colors[i]
      rec.marker.color = self.options.colors[i]

  @property
  def js(self) -> JsPlotly.JsPlotly:
    """Javascript base function.

    Return all the Javascript functions defined in the framework.
    This is an entry point to the full Javascript ecosystem.

    :return: A Javascript object
    """
    if self._js is None:
      self._js = JsPlotly.JsPlotly(selector=self.js_code, component=self, page=self.page)
    return self._js

  @property
  def layout(self) -> OptPlotly.Layout:
    if self._layout is None:
      self._layout = OptPlotly.Layout(page=self.page, component=self)
    return self._layout

  @property
  def d3(self) -> JsD3.D3Select:
    if self._d3 is None:
      self._d3 = JsD3.D3Select(self.page, selector="d3.select('#%s')" % self.htmlCode, setVar=False)
    return self._d3

  def add_trace(self, data, type=None, mode=None):
    """   

    :param data:
    :param type:
    :param mode:
    """
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(OptPlotly.DataChart(component=self, page=self.page, attrs=c_data))
    return self

  def build(self, data=None, options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None,
            component_id: str = None, stop_state: bool = True, dataflows: List[dict] = None):
    """   

    :param data:
    :param options:
    :param profile:
    :param component_id:
    :param dataflows: Chain of data transformations
    """
    self.js_code = component_id
    if data is not None:
      js_convertor = "%s%s" % (self.name, self.__class__.name)
      js_convertor = js_convertor.replace(" ", "")
      self.page.properties.js.add_constructor(
        js_convertor, "function %s(data, options){%s}" % (js_convertor, self._js__builder__))
      profile = self.with_profile(profile, event="Builder", element_id=self.js_code)
      if profile:
        js_func_builder = JsUtils.jsConvertFncs(
          ["var result = %s(data, options)" % js_convertor], toStr=True, profile=profile)
        js_convertor = "(function(data, options){%s; return result})" % js_func_builder
      return JsUtils.jsConvertFncs([
        self.js.react(JsUtils.jsWrap("%(chartFnc)s(%(data)s, %(options)s)" % {
          'chartFnc': js_convertor, "data": JsUtils.dataFlows(data, dataflows, self.page),
          "options":  self.options.config_js(options)}), self.layout, self.options.config_js(options))], toStr=True)

    str_traces = []
    for t in self._traces:
      str_traces.append("{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in t.attrs()]))
    obj_datasets = JsObject.JsObject.get("[%s]" % ", ".join(str_traces))
    return "%s = %s" % (self.js_code, JsUtils.jsConvertFncs([
      self.js.newPlot(obj_datasets, self.layout, self.options, html_code=self.html_code)], toStr=True))

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


class Line(Chart):

  @property
  def dom(self) -> JsPlotly.Line:
    if self._dom is None:
      self._dom = JsPlotly.Line(component=self, js_code=self.js_code, page=self.page)
    return self._dom

  def trace(self, data: types.JS_DATA_TYPES, type: str = None, mode: str = 'lines+markers'):
    """   

    :param data:
    :param type:
    :param mode:
    """
    c_data = dict(data)
    if type is not None:
      c_data['type'] = self.options.type
    if mode is not None:
      c_data['mode'] = self.options.mode or mode
    return OptPlotly.DataXY(page=self.page, attrs=c_data, component=self)

  def add_trace(self, data: types.JS_DATA_TYPES, type: str = None, mode: str = 'lines+markers'):
    """   

    :param data:
    :param type:
    :param mode:
    """
    self._traces.append(self.trace(data, type, mode))
    self.data.line.color = self.options.colors[len(self._traces)-1]
    self.data.marker.color = self.options.colors[len(self._traces)-1]
    return self


class Pie(Chart):

  @property
  def chart(self) -> JsPlotly.Pie:
    if self._chart is None:
      self._chart = JsPlotly.Pie(component=self, page=self.page, js_code=self.js_code)
    return self._chart

  @property
  def data(self) -> OptPlotly.DataPie:
    if not self._traces:
      self._traces.append(OptPlotly.DataPie(page=self.page, component=self))
    return self._traces[-1]

  def add_trace(self, data, type='pie', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = self.options.type
    if mode is not None:
      c_data['mode'] = self.options.mode or mode
    self._traces.append(OptPlotly.DataPie(component=self, page=self.page, attrs=c_data))
    return self

  def add_dataset(self, data, label, colors=None, opacity=None, kind="pie"):
    series = {"label": [], "values": []}
    for i, x in enumerate(self._labels):
      series["label"].append(x)
      series["values"].append(data[i])
    trace = self.add_trace(series, type=kind)
    current_trace = trace.traces()
    current_trace.name = label
    return current_trace

  _js__builder__ = '''if(data.python){
  result = []; 
  dataSet = {label: [], values: [], name: data.series, type: options.type, mode: options.mode, marker: {}};
  if(typeof options.attrs !== undefined){ for(var attr in options.attrs){dataSet[attr] = options.attrs[attr]} };
  if(typeof options.marker !== undefined){
    for(var attr in options.marker){dataSet.marker[attr] = options.marker[attr]}};
  data.datasets.forEach(function(rec, i){
    dataSet.label = rec.x; dataSet.values = rec.y}); result.push(dataSet)
} else {
  var temp = {}; var labels = []; var uniqLabels = {}; var result = [] ;
  options.y_columns.forEach(function(series){temp[series] = {}});
  data.forEach(function(rec){ 
    options.y_columns.forEach(function(name){
      if(rec[name] !== undefined){
        if(!(rec[options.x_column] in uniqLabels)){
          labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
        temp[name][rec[options.x_column]] = rec[name]}})});
  options.y_columns.forEach(function(series){
    dataSet = {label: [], values: [], name: series, type: options.type, mode: options.mode, marker: {}};
    if(typeof options.attrs !== undefined){
      for(var attr in options.attrs){dataSet[attr] = options.attrs[attr]}};
    if(typeof options.marker !== undefined){ 
      for(var attr in options.marker){dataSet.marker[attr] = options.marker[attr]} };
    labels.forEach(function(x, i){
      dataSet.label.push(x);
      if(temp[series][x] == undefined){dataSet.values.push(null)} else{dataSet.values.push(temp[series][x])}
    }); result.push(dataSet)})
}; return result'''


class Surface(Chart):

  @property
  def chart(self) -> JsPlotly.Pie:
    if self._chart is None:
      self._chart = JsPlotly.Pie(page=self.page, js_code=self.js_code, component=self)
    return self._chart

  @property
  def data(self):
    return self._traces[-1]

  def add_trace(self, data, type='surface', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(OptPlotly.DataSurface(page=self.page, component=self, attrs=c_data))
    return self

  _js__builder__ = '''if(data.python){
  result = []; 
  data.datasets.forEach(function(dataset, i){
    result.push( {z: dataset, type: options.type} ) 
  }); console.log(result);
} else {
  var labels = []; var result = [] ;
  data.series.forEach(function(name, i){
    result.push( {z: data.datasets[i], type: options.type} );
  })
}; return result'''


class Scatter3D(Chart):

  @property
  def chart(self) -> JsPlotly.Pie:
    if self._chart is None:
      self._chart = JsPlotly.Pie(page=self.page, component=self, js_code=self.js_code)
    return self._chart

  @property
  def layout(self) -> OptPlotly.Layout3D:
    if self._layout is None:
      self._layout = OptPlotly.Layout3D(page=self.page, component=self)
    return self._layout

  @property
  def data(self):
    return self._traces[-1]

  def add_trace(self, data, type='scatter3d', mode="lines"):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = self.options.type
    if mode is not None:
      c_data['mode'] = self.options.mode or mode
    self._traces.append(OptPlotly.DataSurface(component=self, page=self.page, attrs=c_data))
    return self

  _js__builder__ = '''
var temp = {}; var tempZ = {}; var labels = []; var uniqLabels = {}; var result = [] ;
options.y_columns.forEach(function(series){temp[series] = {}});
options.y_columns.forEach(function(series){tempZ[series] = {}});
data.forEach(function(rec){ 
  options.y_columns.forEach(function(name){
    if(rec[name] !== undefined){
      if(!(rec[options.x_column] in uniqLabels)){
        labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
      temp[name][rec[options.x_column]] = rec[name];
      tempZ[name][rec[options.x_column]] = rec[options.z_axis];
    }})});
options.y_columns.forEach(function(series){
  dataSet = {x: [], y: [], z: [], name: series, type: options.type, mode: options.mode, marker: {}};
  if(typeof options.attrs !== undefined){ for(var attr in options.attrs){dataSet[attr] = options.attrs[attr]} };
  if(typeof options.marker !== undefined){ 
    for(var attr in options.marker){dataSet.marker[attr] = options.marker[attr]} };
  labels.forEach(function(x, i){
    dataSet.x.push(x);
    if(temp[series][x] == undefined){dataSet.y.push(null)} else{dataSet.y.push(temp[series][x])};
    if(tempZ[series][x] == undefined){dataSet.y.push(null)} else{dataSet.z.push(tempZ[series][x])};
  }); result.push(dataSet)});
return result'''


class Mesh3d(Chart):

  @property
  def chart(self) -> JsPlotly.Pie:
    if self._chart is None:
      self._chart = JsPlotly.Pie(page=self.page, component=self, js_code=self.js_code)
    return self._chart

  @property
  def data(self):
    return self._traces[-1]

  def add_trace(self, data, type='mesh3d', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(OptPlotly.DataSurface(component=self, page=self.page, attrs=c_data))
    return self


class Indicator(Chart):

  @property
  def chart(self) -> JsPlotly.Pie:
    if self._chart is None:
      self._chart = JsPlotly.Pie(page=self.page, component=self, js_code=self.js_code)
    return self._chart

  def add_trace(self, data, type='indicator', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(OptPlotly.DataIndicator(page=self.page, component=self, attrs=c_data))
    return self

  _js__builder__ = '''
var dataset = {value: data, type: options.type, mode: options.mode, delta: {}};
if(typeof options.delta !== undefined){
  for(var attr in options.delta){dataset.delta[attr] = options.delta[attr]}};
return [dataset]'''


class ScatterPolar(Chart):

  @property
  def chart(self) -> JsPlotly.Pie:
    """ """
    if self._chart is None:
      self._chart = JsPlotly.Pie(page=self.page, component=self, js_code=self.js_code)
    return self._chart

  def add_trace(self, data, type='scatterpolar', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(OptPlotly.DataChart(page=self.page, component=self, attrs=c_data))
    self.data.fill = 'toself'
    return self


class Box(Chart):

  @property
  def chart(self) -> JsPlotly.Pie:
    """ """
    if self._chart is None:
      self._chart = JsPlotly.Pie(page=self.page, component=self, js_code=self.js_code)
    return self._chart

  @property
  def layout(self) -> OptPlotly.LayoutBox:
    """ """
    if self._layout is None:
      self._layout = OptPlotly.LayoutBox(page=self.page, component=self)
    return self._layout

  def add_trace(self, data, type='box', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(OptPlotly.DataBox(page=self.page, component=self, attrs=c_data))
    return self

  def add_dataset(self, data, label, colors=None, opacity=None, kind="pie"):
    self.add_trace({"x": data})


class CandleStick(Chart):

  @property
  def chart(self) -> JsPlotly.Pie:
    """ """
    if self._chart is None:
      self._chart = JsPlotly.Pie(component=self, page=self.page, js_code=self.js_code)
    return self._chart

  @property
  def layout(self) -> OptPlotly.LayoutBox:
    """ """
    if self._layout is None:
      self._layout = OptPlotly.LayoutBox(component=self, page=self.page)
    return self._layout

  def add_trace(self, data, type='candlestick', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(OptPlotly.DataCandle(page=self.page, component=self, attrs=c_data))
    return self


class Bar(Chart):

  @property
  def chart(self) -> JsPlotly.Bar:
    """ """
    if self._chart is None:
      self._chart = JsPlotly.Bar(page=self.page, js_code=self.js_code, component=self)
    return self._chart

  @property
  def layout(self) -> OptPlotly.LayoutBar:
    if self._layout is None:
      self._layout = OptPlotly.LayoutBar(page=self.page, component=self)
    return self._layout

  def trace(self, data: types.JS_DATA_TYPES, type: str = 'bar', mode: str = None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = self.options.type
    if mode is not None:
      c_data['mode'] = self.options.mode or mode
    return OptPlotly.DataXY(component=self, page=self.page, attrs=c_data)

  def add_trace(self, data, type='bar', mode=None):
    self._traces.append(self.trace(data, type, mode))
    self.data.line.color = self.options.colors[len(self._traces)-1]
    self.data.marker.color = self.options.colors[len(self._traces)-1]
    return self

  def add_dataset(self, data, label, colors=None, opacity=None, kind='bar'):
    return super().add_dataset(data, label, colors, opacity, kind)
