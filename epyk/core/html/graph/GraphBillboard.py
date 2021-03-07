#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.data.DataClass import DataClass

from epyk.core.html import Html

from epyk.core.js.packages import JsBillboard
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils

from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name = 'Billboard'
  requirements = ('billboard.js', )

  def __init__(self, report, width, height, html_code, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                profile=profile, options=options)
    self._d3, self._datasets, self._options, self._data_attrs, self._attrs = None, [], None, {}, {}
    self.style.css.margin_top = 10

  @property
  def js(self):
    """
    Description:
    -----------
    JC3 reference API.

    https://c3js.org/reference.html#api-show

    :return: A Javascript object

    :rtype: JsBillboard.Billboard
    """
    if self._js is None:
      self._js = JsBillboard.Billboard(self, varName=self.chartId, report=self._report)
    return self._js

  @property
  def chartId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart.
    """
    return "%s_obj" % self.htmlCode

  def click(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List of Js Functions. A Javascript Python function
    :param profile: A Boolean. Set to true to get the profile for the function on the Javascript console.
    :param source_event: A String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    self.data.onclick(js_funcs, profile)
    return self

  @property
  def d3(self):
    """
    Description:
    -----------
    Property shortcut the the D£ underlying base classes.

    :rtype: JsD3.D3Select
    """
    if self._d3 is None:
      self._d3 = JsD3.D3Select(self._report, selector="d3.select('#%s')" % self.htmlCode, setVar=False)
    return self._d3

  def build(self, data=None, options=None, profile=None, component_id=None):
    if data is not None:
      js_convertor = "%s%s" % (self.name, self.__class__.name)
      self.page.properties.js.add_constructor(
        js_convertor, "function %s(data, options){%s}" % (js_convertor, self._js__builder__))
      profile = self.with_profile(profile, event="Builder", element_id=self.chartId)
      if profile:
        js_func_builder = JsUtils.jsConvertFncs(
          ["var result = %s(data, options)" % js_convertor], toStr=True, profile=profile)
        js_convertor = "(function(data, options){%s; return result})" % js_func_builder
      return '%(chartId)s.unload(); %(chartId)s.load(%(chartFnc)s(%(data)s, %(options)s))' % {
        'chartId': self.chartId, 'chartFnc': js_convertor, "data": JsUtils.jsConvertData(data, None),
        "options": self.options.config_js(options)}

    return '%s = bb.generate(%s)' % (self.chartId, self.getCtx())

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class JsTick(DataClass):

  @property
  def format(self):
    """
    Description:
    -----------
    """
    return self._attrs["format"]

  @format.setter
  def format(self, val):
    self._attrs["format"] = val


class BBAxis(DataClass):

  @property
  def type(self):
    """
    Description:
    -----------
    """
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    self._attrs["type"] = val

  @property
  def show(self):
    """
    Description:
    -----------
    """
    return self._attrs["show"]

  @show.setter
  def show(self, val):
    self._attrs["show"] = val

  @property
  def tick(self):
    """
    Description:
    -----------
    """
    return self.sub_data("x", JsTick)


class BBSelection(DataClass):
  @property
  def enabled(self):
    """
    Description:
    -----------
    Set data selection enabled.

    If this option is set true, we can select the data points and get/set its state of selection by API (e.g. select,
    unselect, selected).

    Related Pages:

      https://c3js.org/reference.html#data-selection-enabled
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def grouped(self):
    """
    Description:
    -----------
    """
    return self._attrs["grouped"]

  @grouped.setter
  def grouped(self, val):
    self._attrs["grouped"] = val

  @property
  def multiple(self):
    """
    Description:
    -----------
    """
    return self._attrs["multiple"]

  @multiple.setter
  def multiple(self, val):
    self._attrs["multiple"] = val

  @property
  def draggable(self):
    """
    Description:
    -----------
    """
    return self._attrs["draggable"]

  @draggable.setter
  def draggable(self, val):
    self._attrs["draggable"] = val

  @property
  def isselectable(self):
    """
    Description:
    -----------
    """
    return self._attrs["isselectable"]

  @isselectable.setter
  def isselectable(self, jsFnc):
    self._attrs["isselectable"] = jsFnc


class JsData(DataClass):
  @property
  def x(self):
    """
    Description:
    -----------
    """
    return self._attrs["x"]

  @x.setter
  def x(self, val):
    self._attrs["x"] = val

  @property
  def xs(self): return self._attrs["xs"]

  @xs.setter
  def xs(self, val): self._attrs["xs"] = val

  @property
  def xFormat(self): return self._attrs["xFormat"]

  @xFormat.setter
  def xFormat(self, val): self._attrs["xFormat"] = val

  @property
  def names(self): return self._attrs["names"]

  @names.setter
  def names(self, val): self._attrs["names"] = val

  @property
  def groups(self): return self._attrs["groups"]

  @groups.setter
  def groups(self, val): self._attrs["groups"] = val

  @property
  def axes(self): return self._attrs["axes"]

  @axes.setter
  def axes(self, val): self._attrs["axes"] = val

  @property
  def type(self): return self._attrs["type"]

  @type.setter
  def type(self, val): self._attrs["type"] = val

  def add_type(self, alias, value):
    if "types" not in self._attrs:
      self.types = {}
    self.types[alias] = value
    return self

  @property
  def types(self):
    """
    Description:
    -----------
    This setting overwrites data.type setting:
    line, spline, step, area...

    Related Pages:

      https://c3js.org/reference.html#data-types
    """
    return self._attrs["types"]

  @types.setter
  def types(self, val): self._attrs["types"] = val

  @property
  def labels(self): return self._attrs["labels"]

  @labels.setter
  def labels(self, val): self._attrs["labels"] = val

  @property
  def order(self): return self._attrs["order"]

  @order.setter
  def order(self, val): self._attrs["order"] = val

  @property
  def colors(self):
    if "colors" not in self._attrs:
      self._attrs["colors"] = {}
    return self._attrs["colors"]

  @colors.setter
  def colors(self, val): self._attrs["colors"] = val

  @property
  def columns(self):
    if 'columns' not in self._attrs:
      self._attrs["columns"] = []
    return self._attrs["columns"]

  @columns.setter
  def columns(self, val): self._attrs["columns"] = val

  @property
  def hide(self): return self._attrs["hide"]

  @hide.setter
  def hide(self, val): self._attrs["hide"] = val

  @property
  def selection(self):
    return self.sub_data("selection", BBSelection)

  def onclick(self, js_funcs, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    self._attrs["onclick"] = JsObjects.JsObject.JsObject("function () {%s}" % js_funcs)


class JsScales(DataClass):

  @property
  def rotated(self):
    return self._attrs["rotated"]

  @rotated.setter
  def rotated(self, val):
    self._attrs["rotated"] = val

  @property
  def x(self):
    """
    Description:
    -----------

    Related Pages:

      https://c3js.org/reference.html#axis-y2-show

    :rtype: BBAxis
    """
    return self.sub_data("x", BBAxis)

  @property
  def y(self):
    """
    Description:
    -----------

    https://c3js.org/reference.html#axis-y2-show

    :rtype: BBAxis
    """
    return self.sub_data("y", BBAxis)

  @property
  def y2(self):
    """
    Description:
    -----------

    Related Pages:

      https://c3js.org/reference.html#axis-y2-show

    :rtype: BBAxis
    """
    return self.sub_data("y2", BBAxis)


class BBGridLine(DataClass):

  @property
  def value(self):
    return self._attrs["value"]

  @value.setter
  def value(self, val):
    self._attrs["value"] = val

  @property
  def text(self):
    return self._attrs["text"]

  @text.setter
  def text(self, val):
    self._attrs["text"] = val

  @property
  def css_class(self):
    return self._attrs["class"]

  @css_class.setter
  def css_class(self, val):
    self._attrs["class"] = val

  @property
  def position(self):
    return self._attrs["position"]

  @position.setter
  def position(self, val):
    self._attrs["position"] = val


class C3GridAxis(DataClass):

  @property
  def show(self):
    return self._attrs["show"]

  @show.setter
  def show(self, val):
    self._attrs["show"] = val

  @property
  def lines(self):
    return self.sub_data_enum("lines", BBGridLine)


class BBGrid(DataClass):

  @property
  def x(self):
    return self.sub_data("x", C3GridAxis)

  @property
  def y(self):
    return self.sub_data("y", C3GridAxis)


class JsLegend(DataClass):
  pass


class JsTooltip(DataClass):
  pass


class JsSubchart(DataClass):
  pass


class JsZoom(DataClass):
  @property
  def enabled(self):
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def type(self):
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    self._attrs["type"] = val

  @property
  def rescale(self):
    return self._attrs["rescale"]

  @rescale.setter
  def rescale(self, val):
    self._attrs["rescale"] = val

  @property
  def extent(self):
    return self._attrs["extent"]

  @extent.setter
  def extent(self, val):
    self._attrs["extent"] = val


class BBPoints(DataClass):

  @property
  def show(self):
    return self._attrs["show"]

  @show.setter
  def show(self, val):
    self._attrs["show"] = val

  @property
  def r(self):
    return self._attrs["r"]

  @r.setter
  def r(self, val):
    self._attrs["r"] = val

  @property
  def focus(self):
    return self._attrs["focus"]

  @focus.setter
  def focus(self, val):
    self._attrs["focus"] = {"expand": val, 'enabled': True}

  @property
  def select(self):
    return self._attrs["select"]

  @select.setter
  def select(self, val):
    self._attrs["select"] = val


class ChartLine(Chart):
  _type = 'line'

  def __init__(self, report, width, height, html_code, options, profile):
    super(ChartLine, self).__init__(report, width, height, html_code, options, profile)
    self._attrs["bindto"] = "#%s" % self.htmlCode

  def labels(self, labels, series_id='x'):
    self.data.x = series_id
    self.data.columns.append([series_id] + labels)

  def add_dataset(self, name, data, type=None):
    self.data.columns.append([name] + data)
    self.data.colors[name] = self._report.theme.colors[len(self.data.colors)]
    if type is None:
      self.data.add_type(name, self._type)
    return self._attrs

  _js__builder__ = '''
      if(data.python){ 
        result = {'columns': [], type: options.type};
        result['columns'].push(['x'].concat(data.labels));
        data.series.forEach(function(name, i){
          result['columns'].push([name].concat(data.datasets[i]));
        }); 
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_column] in uniqLabels)){labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
              temp[name][rec[options.x_column]] = rec[name]}})});
        columns = []; columns.push(['x'].concat(labels));
        options.y_columns.forEach(function(series){
          dataSet = [series];
          labels.forEach(function(x){
            if(temp[series][x] == undefined){dataSet.push(null)} else {dataSet.push(temp[series][x])}}); columns.push(dataSet)});
        var result = {columns: columns}
      }; return result'''

  @property
  def axis(self):
    """
    Description:
    -----------

    :rtype: JsScales
    """
    if not'axis' in self._attrs:
      self._attrs['axis'] = JsScales(self._report)
    return self._attrs['axis']

  @property
  def point(self):
    """
    Description:
    -----------

    :rtype: BBPoints
    """
    if 'point' not in self._attrs:
      self._attrs['point'] = BBPoints(self._report)
    return self._attrs['point']

  @property
  def zoom(self):
    """
    Description:
    -----------

    :rtype: JsZoom
    """
    if 'zoom' not in self._attrs:
      self._attrs['zoom'] = JsZoom(self._report)
    return self._attrs['zoom']

  @property
  def data(self):
    """
    Description:
    -----------

    :rtype: JsData

    """
    if 'data' not in self._attrs:
      self._attrs['data'] = JsData(self._report)
    return self._attrs['data']

  @property
  def grid(self):
    """
    Description:
    -----------

    :rtype: BBGrid
    """
    if 'grid' not in self._attrs:
      self._attrs['grid'] = BBGrid(self._report)
    return self._attrs['grid']

  def getCtx(self):
    str_ctx = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items()])
    return str_ctx


class ChartSpline(ChartLine):
  _type = 'spline'


class ChartArea(ChartLine):
  _type = 'area'


class ChartBar(ChartLine):
  _type = 'bar'


class ChartScatter(ChartLine):
  _type = 'scatter'

  _js__builder__ = '''
      if(data.python){ 
        result = {'columns': [], type: options.type};
        result['columns'].push(['x'].concat(data.labels));
        data.series.forEach(function(name, i){
          result['columns'].push([name].concat(data.datasets[i]));
        });
      } else {
        var tempVal = {}; var tempX = {}; var labels = []; 
        options.y_columns.forEach(function(series){tempVal[series] = []; tempX[series +"_x"] = []});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if(!(rec[options.x_column] in tempVal[name])){
                tempVal[name] = [name, rec[name]]; tempX[name +"_x"] = [name +"_x", rec[options.x_column]]}
              else {tempVal[name].push(rec[name]); tempX[name +"_x"].push(rec[options.x_column])}}})});
        result = {'columns': [], 'xs': {}};
        options.y_columns.forEach(function(series){
          result.columns.push(tempVal[series]); result.columns.push(tempX[series +"_x"]); 
          result.xs[series] = series +"_x"})
      }; return result'''


class ChartPie(ChartLine):
  _type = 'pie'

  _js__builder__ = '''
      if(data.python){ 
        result = {'columns': [], type: options.type};
        result['columns'].push(['x'].concat(data.labels));
        data.series.forEach(function(name, i){
          result['columns'].push([name].concat(data.datasets[i]));
        }); 
      } else {
        var temp = {}; var labels = {};
        data.forEach(function(rec){ 
          if(!(rec[options.x_column] in temp)){temp[rec[options.x_column]] = {}};
          options.y_columns.forEach(function(name){
            labels[name] = true; 
            if(rec[name] !== undefined){
              if(!(name in temp[rec[options.x_column]])){temp[rec[options.x_column]][name] = rec[name]} 
              else{temp[rec[options.x_column]][name] += rec[name]}}})});
        columns = []; var labels = Object.keys(labels); var count = 0;
        for(var series in temp){
          var values = [count]; count += 1;
          labels.forEach(function(label){
            if(temp[series][label] !== undefined){
              values.push(temp[series][label])} else{values.push(null)}});
          columns.push(values)};
        var result = {columns: columns};
      }; return result'''

  def labels(self, labels, series_id='x'):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param labels:
    :param series_id:
    """
    self._labels = labels

  def add_dataset(self, name, values, type=None):
    for i, value in enumerate(values):
      self.data.columns.append([self._labels[i], value])
      self.data.colors[self._labels[i]] = self._report.theme.colors[i]
      self.data.add_type(self._labels[i], type or self._type)
    return self._attrs


class ChartDonut(ChartPie):
  _type = 'donut'


class ChartGauge(ChartPie):
  _type = 'gauge'

  def build(self, data=None, options=None, profile=None, component_id=None):
    if data:
      return '%(chartId)s.load({columns: [["data", %(value)s]]})' % {'chartId': self.chartId, 'value': data}

    return '%s = bb.generate(%s)' % (self.chartId, self.getCtx())

  def add_dataset(self, name, value, type=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param name:
    :param value:
    :param type:
    """
    self.data.columns.append(["data", value])
    self.data.colors["data"] = self._report.theme.colors[len(self.data.colors)]
    if type is None:
      self.data.add_type("data", self._type)
    return self._attrs


class ChartBubble(ChartLine):
  _type = 'bubble'


class ChartRadar(ChartLine):
  _type = 'radar'

