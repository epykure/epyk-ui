#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.data.DataClass import DataClass

from epyk.core.html import Html
from epyk.core.css import Colors

from epyk.core.js.packages import JsC3
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsD3
from epyk.core.html.options import OptChart


class Chart(Html.Html):
  name = 'C3'
  requirements = ('c3', )
  _option_cls = OptChart.OptionsChart

  def __init__(self, report, width, height, html_code, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(
      report, [], html_code=html_code, css_attrs={"width": width, "height": height}, profile=profile, options=options)
    self._d3, self._datasets, self._options, self._data_attrs, self._attrs = None, [], None, {}, {}
    self.style.css.margin_top = 10

  @property
  def chartId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlCode

  @property
  def js(self):
    """
    Description:
    -----------
    JavaScript C3 reference API.

    Related Pages:

      https://c3js.org/reference.html#api-show

    :return: A Javascript object

    :rtype: JsC3.C3
    """
    if self._js is None:
      self._js = JsC3.C3(self, varName=self.chartId, report=self._report)
    return self._js

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
    series_count = 0
    for name in self.data._attrs.get('columns', []):
      if name[0] in self.data._attrs.get("colors", {}):
        self.data._attrs["colors"][name[0]] = self.options.colors[series_count]
        series_count += 1

  def click(self, js_funcs, profile=False, source_event=None, on_ready=False):
    """
    Description:
    -----------
    Set a callback for click event on each data point.

    Related Pages:

      https://c3js.org/reference.html#data-onclick

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

    :rtype: JsD3.D3Select
    """
    if self._d3 is None:
      self._d3 = JsD3.D3Select(self._report, selector="d3.select('#%s')" % self.htmlCode, setVar=False)
    return self._d3

  def build(self, data=None, options=None, profile=False, component_id=None):
    if data is not None:
      js_convertor = "%s%s" % (self.name, self.__class__.name)
      self.page.properties.js.add_constructor(
        js_convertor, "function %s(data, options){%s}" % (js_convertor, self._js__builder__))
      return '%(chartId)s.unload(); %(chartId)s.load(%(chartFnc)s(%(data)s, %(options)s))' % {
        'chartId': self.chartId, 'chartFnc': js_convertor, "data": JsUtils.jsConvertData(data, None),
        "options":  self.options.config_js(options)}

    return '%s = c3.generate(%s)' % (self.chartId, self.getCtx())

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class JsTick(DataClass):

  @property
  def format(self):
    return self._attrs["format"]

  @format.setter
  def format(self, val):
    self._attrs["format"] = val


class C3Axis(DataClass):

  @property
  def type(self):
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    self._attrs["type"] = val

  @property
  def show(self):
    return self._attrs["show"]

  @show.setter
  def show(self, val):
    self._attrs["show"] = val

  @property
  def tick(self):
    return self.sub_data("x", JsTick)


class C3Selection(DataClass):
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
    """
    return self._attrs["grouped"]

  @grouped.setter
  def grouped(self, val):
    self._attrs["grouped"] = val

  @property
  def multiple(self):
    """
    """
    return self._attrs["multiple"]

  @multiple.setter
  def multiple(self, val):
    self._attrs["multiple"] = val

  @property
  def draggable(self):
    """
    """
    return self._attrs["draggable"]

  @draggable.setter
  def draggable(self, val):
    self._attrs["draggable"] = val

  @property
  def isselectable(self):
    """
    """
    return self._attrs["isselectable"]

  @isselectable.setter
  def isselectable(self, js_funcs):
    self._attrs["isselectable"] = js_funcs


class JsData(DataClass):
  @property
  def x(self):
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

  def add_type(self, alias, name):
    if "types" not in self._attrs:
      self.types = {}
    self.types[alias] = name
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
    return self.sub_data("selection", C3Selection)

  def onclick(self, js_funcs, profile=False):
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    self._attrs["onclick"] = JsObjects.JsObject.JsObject("function () { %s }" % js_funcs)


class JsDataEpochs(JsData):

  @property
  def epochs(self):
    """
    """
    return self._attrs["epochs"]

  @epochs.setter
  def epochs(self, val):
    self._attrs["epochs"] = val


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

    Related Pages:

      https://c3js.org/reference.html#axis-y2-show

    :rtype: C3Axis
    """
    return self.sub_data("x", C3Axis)

  @property
  def y(self):
    """

    Related Pages:

      https://c3js.org/reference.html#axis-y2-show

    :rtype: C3Axis
    """
    return self.sub_data("y", C3Axis)

  @property
  def y2(self):
    """

    Related Pages:

      https://c3js.org/reference.html#axis-y2-show

    :rtype: C3Axis
    """
    return self.sub_data("y2", C3Axis)


class C3GridLine(DataClass):
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
    """

    :rtype: C3GridLine
    """
    return self.sub_data_enum("lines", C3GridLine)


class C3Grid(DataClass):

  @property
  def x(self):
    """

    :rtype: C3GridAxis
    """
    return self.sub_data("x", C3GridAxis)

  @property
  def y(self):
    """

    :rtype: C3GridAxis
    """
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


class C3Points(DataClass):

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
    self.data.colors[name] = self.options.colors[len(self.data.colors)]
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
              if (!(rec[options.x_column] in uniqLabels)){
                labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
              temp[name][rec[options.x_column]] = rec[name]}})});
        columns = []; columns.push(['x'].concat(labels));
        options.y_columns.forEach(function(series){
          dataSet = [series];
          labels.forEach(function(x){
            if(temp[series][x] == undefined){dataSet.push(null)} 
            else {dataSet.push(temp[series][x])}}); columns.push(dataSet)});
        var result = {columns: columns}
      }; return result'''

  @property
  def axis(self):
    """

    :rtype: JsScales
    """
    if not'axis' in self._attrs:
      self._attrs['axis'] = JsScales(self._report)
    return self._attrs['axis']

  @property
  def point(self):
    """

    :rtype: C3Points
    """
    if 'point' not in self._attrs:
      self._attrs['point'] = C3Points(self._report)
    return self._attrs['point']

  @property
  def zoom(self):
    """

    :rtype: JsZoom
    """
    if 'zoom' not in self._attrs:
      self._attrs['zoom'] = JsZoom(self._report)
    return self._attrs['zoom']

  @property
  def data(self):
    """

    :rtype: JsScales
    """
    if 'data' not in self._attrs:
      self._attrs['data'] = JsData(self._report)
    return self._attrs['data']

  @property
  def grid(self):
    """

    :rtype: JsScales
    """
    if 'grid' not in self._attrs:
      self._attrs['grid'] = C3Grid(self._report)
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
              if(!(name in temp[rec[options.x_column]])){
                temp[rec[options.x_column]][name] = rec[name]} 
              else{temp[rec[options.x_column]][name] += rec[name]}}})});
        columns = []; var labels = Object.keys(labels); var count = 0;
        for(var series in temp){
          var values = [count]; count += 1;
          labels.forEach(function(label){
            if(temp[series][label] !== undefined){values.push(temp[series][label])} else{values.push(null)}});
          columns.push(values)};
        var result = {columns: columns}
      }; return result'''

  def labels(self, labels, series_id='x'):
    self._labels = labels

  def add_dataset(self, name, values, type=None):
    for i, value in enumerate(values):
      self.data.columns.append([self._labels[i], value])
      self.data.colors[self._labels[i]] = self.options.colors[i]
      if type is None:
        self.data.add_type(self._labels[i], self._type)
    return self._attrs


class ChartDonut(ChartPie):
  _type = 'donut'


class ChartGauge(ChartPie):
  _type = 'gauge'

  def build(self, data=None, options=None, profile=False, component_id=None):
    if data:
      return '%(chartId)s.load({columns: [["data", %(value)s]]})' % {'chartId': self.chartId, 'value': data}

    return '%s = c3.generate(%s)' % (self.chartId, self.getCtx())

  def add_dataset(self, name, value, type=None):
    self.data.columns.append(["data", value])
    self.data.colors["data"] = self.options.colors[len(self.data.colors)]
    if type is None:
      self.data.add_type("data", self._type)
    return self._attrs


class ChartStanford(ChartPie):
  _type = 'stanford'

  @property
  def data(self):
    """

    :rtype: JsDataEpochs
    """
    if 'data' not in self._attrs:
      self._attrs['data'] = JsDataEpochs(self._report)
    return self._attrs['data']

  def epoch(self, series, name):
    self.data.epochs = JsUtils.jsConvertData(str(name), None)
    self.data.columns.append([str(name)] + series)

  def add_dataset(self, name, data, type=None):
    self.data.columns.append([name] + data)
    self.data.type = type or self._type
    return self._attrs
