#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsNvd3
from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name = 'NVD3 Chart'
  requirements = ('nvd3', )

  def __init__(self,  report, width, height, options, htmlCode, profile):
    self.seriesProperties, self.__chartJsEvents, self.height = {'static': {}, 'dynamic': {}}, {}, height[0]
    super(Chart, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self.html_items, self._datasets = None, [], []
    self._options_init = options

  @property
  def chartId(self):
    """
    Description:
    ------------
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlCode

  @property
  def data(self):
    """
    Description:
    -----------
    Property to the last dataset added to the NVD3 chart.
    Use the function traces to get a specific series from the chart object
    """
    return self._datasets[-1]

  def traces(self, i=None):
    """
    Description:
    ------------
    Get a specific series from the datasets attributes in the NVD3 chart.
    """
    if i is None:
      return self._datasets[-1]

    return self._datasets[i]

  def click(self, jsFnc, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFnc:
    :param profile:
    :param source_event:
    :param onReady:
    """
    raise Exception("Not implemented for this chart !")

  def add_trace(self, data, name=""):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param name:
    """
    dataset = {"values": data, 'key': name}
    next_index = len(self._datasets)
    if len(self._report.theme.colors) > next_index:
      dataset['color'] = self._report.theme.colors[next_index]
    self._datasets.append(dataset)
    return self

  @property
  def d3(self):
    """
    Description:
    ------------

    :rtype: JsD3.D3Select
    """
    if self._d3 is None:
      self._d3 = JsD3.D3Select(self._report, selector="d3.select('#%s')" % self.htmlCode, setVar=False)
    return self._d3

  def convert(self, data, options, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param options:
    :param profile:
    """
    mod_name = __name__.split(".")[-1]
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors[self.builder_name] = "function %s%sConvert(data, options){%s; return result}" % (
      mod_name, self.builder_name, self._js__convertor__)
    if isinstance(data, dict):
      # check if there is no nested HTML components in the data
      tmp_data = ["%s: %s" % (JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)) for k, v in data.items()]
      js_data = "{%s}" % ",".join(tmp_data)
    else:
      js_data = JsUtils.jsConvertData(data, None)
    options, js_options = options or self._options_init, []
    for k, v in options.items():
      if isinstance(v, dict):
        row = ["'%s': %s" % (s_k, JsUtils.jsConvertData(s_v, None)) for s_k, s_v in v.items()]
        js_options.append("'%s': {%s}" % (k, ", ".join(row)))
      else:
        if str(v).strip().startswith("function"):
          js_options.append("%s: %s" % (k, v))
        else:
          js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
    return "%s%sConvert(%s, %s)" % (mod_name, self.builder_name, js_data, "{%s}" % ",".join(js_options))

  def build(self, data=None, options=None, profile=False):
    if data:
      return "d3.select('#%(htmlCode)s').datum(%(data)s).transition().duration(500).call(%(chart)s); nv.utils.windowResize(%(chart)s.update)" % {'htmlCode': self.htmlCode, 'data': self.convert(data, options, profile), 'chart': self.dom.var}

    return JsUtils.jsConvertFncs([self.dom.set_var(True), self.dom.xAxis, self.d3.datum(self._datasets).call(self.dom.var),
                "nv.utils.windowResize(function() { %s.update() })" % self.dom.var], toStr=True)[4:]

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    str_items = "".join([h.html() for h in self.html_items])
    return '%s<svg %s></svg>' % (str_items, self.get_attrs(pyClassNames=self.style.get_classes()))


class ChartLine(Chart):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3Line
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Line(self._report, varName=self.chartId)
    return self._dom

  @property
  def _js__convertor__(self):
    return '''
      if(data.python){
        result = [];
        data.datasets.forEach(function(rec, i){
          result.push( {key: data.series[i], values: rec, labels: data.labels} )})
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}}) ;
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_column] in uniqLabels)){labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
              temp[name][rec[options.x_column]] = rec[name]}})
        }); result = [];
        options.y_columns.forEach(function(series){
          dataSet = {key: series, values: [], labels: labels};
          labels.forEach(function(x, i){
            var value = temp[series][x]; 
            if (isNaN(value)) { value = null};
            if (value !== undefined) {dataSet.values.push({y: value, x: i, label: x})}
          }); result.push(dataSet)})
      }'''


class ChartScatter(ChartLine):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3Scatter
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Scatter(self._report, varName=self.chartId)
    return self._dom

  def click(self, jsFncs, profile=False, source_event=None, onReady=False):
    """

    Attributes:
    ----------
    :param jsFncs: List of Js Functions. A Javascript Python function
    :param profile: A Boolean. Set to true to get the profile for the function on the Javascript console.
    :param source_event: A String. Optional. The source target for the event.
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    self.onReady("%s.scatter.dispatch.on('elementClick', function(event){ %s })" % (self.dom.varName, JsUtils.jsConvertFncs(jsFncs, toStr=True)))
    return self


class ChartCumulativeLine(ChartLine):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3CumulativeLine
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3CumulativeLine(self._report, varName=self.chartId)
    return self._dom


class ChartFocusLine(Chart):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3LineWithFocus
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3LineWithFocus(self._report, varName=self.chartId)
    return self._dom


class ChartBar(Chart):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3Bar
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Bar(self._report, varName=self.chartId)
    return self._dom

  def click(self, jsFnc, profile=False, source_event=None, onReady=False):
    """

    :param jsFnc:
    :param profile:
    :param source_event:
    :param onReady:
    """
    self.onReady("%s.selectAll('.nv-bar').on('click', function(event){ %s })" % (self.d3.varId, JsUtils.jsConvertFncs(jsFnc, toStr=True)))
    return self

  @property
  def _js__convertor__(self):
    return '''
      if(data.python){
        result = [];
        data.datasets.forEach(function(rec, i){
          result.push( {key: data.series[i], values: rec, labels: data.labels} )})
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}}) ;
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_column] in uniqLabels)){labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
              temp[name][rec[options.x_column]] = rec[name]}})
        }); var result = [];
        options.y_columns.forEach(function(series){
          dataSet = {key: series, values: [], labels: labels};
          labels.forEach(function(x, i){
            var value = temp[series][x]; 
            if (isNaN(value)) { value = null};
            if (value !== undefined) {dataSet.values.push({y: value, x: i, label: x})}
          }); result.push(dataSet)})
      }'''


class ChartHorizontalBar(ChartBar):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3MultiBarHorizontal
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3MultiBarHorizontal(self._report, varName=self.chartId)
    return self._dom


class ChartMultiBar(Chart):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3MultiBar
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3MultiBar(self._report, varName=self.chartId)
    return self._dom


class ChartPie(Chart):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3Pie
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Pie(self._report, varName=self.chartId)
    return self._dom

  @property
  def _js__convertor__(self):
    return '''
      if(data.python){
        data.datasets.forEach(function(dataset, i){console.log(dataset);
          result = dataset;  
        }); console.log(result)
      } else {
        var temp = {}; var labels = {};
        data.forEach(function(rec){ 
          if(!(rec[options.x_column] in temp)){temp[rec[options.x_column]] = {}};
          options.y_columns.forEach(function(name){
            labels[name] = true; if(rec[name] !== undefined) {if (!(name in temp[rec[options.x_column]])){temp[rec[options.x_column]][name] = rec[name]} else {temp[rec[options.x_column]][name] += rec[name]}}  }) ;
        });
        var labels = Object.keys(labels); result = [];
        for(var series in temp){
          var values = {y: 0, x: series};
          labels.forEach(function(label){
            if(temp[series][label] !== undefined){values.y = temp[series][label]}});
          result.push(values)}
      }'''

  def click(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    :param source_event:
    :param onReady:
    """
    self.onReady("%s.pie.dispatch.on('elementClick', function(event){ %s })" % (self.dom.varName, JsUtils.jsConvertFncs(jsFncs, toStr=True)))
    return self

  def add_trace(self, data, name=""):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param name:
    """
    self.dom.color(self._report.theme.colors)
    self._datasets = data
    return self


class ChartArea(ChartBar):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3Area
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Area(self._report, varName=self.chartId)
    return self._dom


class ChartHistoBar(ChartBar):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3HistoricalBar
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3HistoricalBar(self._report, varName=self.chartId)
    return self._dom


class ChartParallelCoord(Chart):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3ParallelCoordinates
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3ParallelCoordinates(self._report, varName=self.chartId)
    return self._dom

  def set_dimension_names(self, dimensions):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param dimensions:
    """
    self.__dimensions = dimensions
    self.dom.dimensionNames(dimensions)
    return self

  def add_trace(self, data, name=""):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param name:
    """
    self._datasets = data
    return self


class ChartSunbrust(Chart):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3Sunburst
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3Sunburst(self._report, varName=self.chartId)
    return self._dom

  def set_rcolors(self, color, data):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param color:
    :param data:
    """
    for rec in data:
      rec['color'] = color
      if 'children' in rec:
        self.set_rcolors(color, rec['children'])

  def add_trace(self, data, name=""):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param name:
    """
    for i, rec in enumerate(data):
      rec['color'] = self._report.theme.colors[i+1]
      self.set_rcolors(rec['color'], rec['children'])
    self._datasets = [{'name': name, 'children': data, 'color': self._report.theme.colors[0]}]
    return self

  @property
  def _js__convertor__(self):
    return '''
      var result = [{name: options.x_column, children: []}]; var sizeTree = options.y_columns.length-1;
      data.forEach(function(rec){
        var path = []; var tmpResultLevel = result[0].children; var branchVal = 0;
        options.y_columns.forEach(function(s, i){
          var treeLevel = -1; 
          tmpResultLevel.forEach(function(l, j){if(l.name == rec[s]){treeLevel = j}});
          if(i == sizeTree){
            if(treeLevel >= 0){
              tmpResultLevel[treeLevel].size += rec[options.x_column]}else{tmpResultLevel.push({name: rec[s], size: rec[options.x_column]})}
          }else{
            if(treeLevel < 0 ){
              tmpResultLevel.push({name: rec[s], children: []}); treeLevel = tmpResultLevel.length - 1};
              tmpResultLevel = tmpResultLevel[treeLevel].children}
        })})'''


class ChartBoxPlot(Chart):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3BoxPlot
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3BoxPlot(self._report, varName=self.chartId)
    return self._dom

  def add_box(self, q1, q3=None, outliers=None, maxRegularValue=None, mean=None, median=None, minRegularValue=None,
              minOutlier=None, maxOutlier=None, title=None):
    """
    Description:
    ------------

    https://github.com/nvd3-community/nvd3/blob/gh-pages/examples/boxPlotCustomModel.html

    Attributes:
    ----------
    :param q1:
    :param q3:
    :param outliers:
    :param maxRegularValue:
    :param mean:
    :param median:
    :param minRegularValue:
    :param minOutlier:
    :param maxOutlier:
    """
    names = ['q1', 'median', 'q3', 'outlData', 'maxRegularValue', 'mean', 'minRegularValue', 'minOutlier', 'maxOutlier']
    row = {}
    for i, val in enumerate([q1, median, q3, outliers, maxRegularValue, mean, minRegularValue, minOutlier, maxOutlier]):
      if val is not None:
        row[names[i]] = val
      elif names[i] == 'outlData':
        row['outlData'] = []
    series_id = len(self._datasets) - 1
    row['seriesColor'] = self._report.theme.colors[series_id]
    row['title'] = title or "Series %s" % series_id
    self._datasets.append(row)
    return self

  def add_trace(self, data, name=""):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param name:
    """
    self._datasets = data
    return self


class ChartCandlestick(Chart):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3CandlestickBar
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3CandlestickBar(self._report, varName=self.chartId)
    return self._dom


class ChartOhlcBar(Chart):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3OhlcBar
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3OhlcBar(self._report, varName=self.chartId)
    return self._dom


class ChartForceDirected(Chart):

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsNvd3.JsNvd3ForceDirectedGraph
    """
    if self._dom is None:
      self._dom = JsNvd3.JsNvd3ForceDirectedGraph(self._report, varName=self.chartId)
    return self._dom

  def add_trace(self, data, name=""):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param name:
    """
    for d in data.get('nodes', []):
      d['color'] = self._report.theme.colors[d.get('group', 1)]
    self._datasets = data
    return self
