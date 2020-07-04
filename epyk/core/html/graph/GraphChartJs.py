#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.options import OptChartJs

from epyk.core.js import JsUtils
from epyk.core.js.packages import packageImport
from epyk.core.js.primitives import JsObject

from epyk.core.js.packages import JsChartJs
from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name = 'ChartJs Chart'
  requirements = ('Chart.js', )

  def __init__(self,  report, width, height, htmlCode, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self._chart, self._datasets, self._options, self._data_attrs, self._attrs = None, None, [], None, {}, {}
    self._options_init = options
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
  def d3(self):
    """

    :rtype: JsD3.D3Select
    """
    if self._d3 is None:
      self._d3 = JsD3.D3Select(self._report, selector="d3.select('#%s')" % self.htmlCode, setVar=False)
    return self._d3

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript base function

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    :return: A Javascript object

    :rtype: JsChartJs.ChartJs
    """
    if self._js is None:
      self._js = JsChartJs.ChartJs(selector="window['%s']" % self.chartId, src=self)
    return self._js

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptChartJs.Options
    """
    if self._options is None:
      self._options = OptChartJs.Options(self._report, attrs=self._options_init)
    return self._options

  @property
  def plugins(self):
    return self.options.plugins

  @packageImport('chartjs-plugin-dragdata')
  def dragData(self):
    """
    Description:
    -----------
    A plugin for Chart.js >= 2.4.0

    Makes data points draggable. Supports touch events.

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata
    """
    self.options._attrs['dragData'] = True
    return self.options

  def labels(self, labels):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param labels:
    """
    self._data_attrs['labels'] = labels
    return self

  def label(self, i, name):
    """
    Description:
    -----------
    Change the series name

    Attributes:
    ----------
    :param i: Integer. The series index according to the y_columns
    :param name: String. The new name to be set
    """
    self.dataset(i).label = name
    return self

  def dataset(self, i=None):
    """
    Description:
    -----------

    :rtype: JsChartJs.DataSetPie
    """
    if i is None:
      return self._datasets[-1]

    return self._datasets[i]

  def click(self, jsFncs, profile=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    if self._attrs.get('type') in ['pie']:
      tmpJsFncs = ["var activePoints = %s.getSegmentsAtEvent(event)" % self.chartId]
      tmpJsFncs.append("if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))
    else:
      tmpJsFncs = ["var activePoints = %s.getElementsAtEvent(event)" % self.chartId]
      tmpJsFncs.append("if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))
    return super(Chart, self).click(tmpJsFncs, profile)

  def hover(self, jsFncs, profile=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    tmpJsFncs = ["var activePoints = %s.getElementsAtEvent(event)" % self.chartId]
    tmpJsFncs.append("if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))
    return self.on("mouseover", tmpJsFncs, profile)

  @property
  def datasets(self):
    return self._datasets

  def getCtx(self):
    obj_datasets = "[%s]" % ", ".join([d.toStr() for d in self._datasets])
    self._data_attrs['datasets'] = JsObject.JsObject.get(obj_datasets)
    obj_data = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._data_attrs.items()])
    self._attrs["data"] = JsObject.JsObject.get(obj_data)
    self._attrs["options"] = JsObject.JsObject.get(str(self.options))
    str_ctx = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items()])
    return str_ctx

  def convert(self, data, options, profile=False):
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
      return "Object.assign(window['%(chartId)s'].data, %(data)s); window['%(chartId)s'].update()" % {'chartId': self.chartId, 'data': self.convert(data, options, profile)}
      #return "window['%(chartId)s'].data.labels = %(labels)s; window['%(chartId)s'].data.datasets = [%(recordsset)s]; window['%(chartId)s'].update()" % {'labels': js_data['labels'], 'recordsset': ",".join(recordsset),  'chartId': self.chartId}

    return '%s = new Chart(%s.getContext("2d"), %s)' % (self.chartId, self.dom.varId, self.getCtx())

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<canvas %s></canvas>' % self.get_attrs(pyClassNames=self.style.get_classes())


class Datasets(object):

  def __init__(self, report):
    self._report, self.__data = report, []

  def add(self, data):
    self.__data.append(data)
    return self


class ChartLine(Chart):

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartLine, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'line'

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptChartJs.OptionsLine
    """
    if self._options is None:
      self._options = OptChartJs.OptionsLine(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label, colors=None, opacity=0.8, type=None):
    data = JsChartJs.DataSetScatterLine(self._report, attrs={"data": data})
    data.fill = False
    data.label = label
    if colors is None:
      data.borderColor = self._report.theme.charts[id]
      data.backgroundColor = self._report.theme.charts[id]
    data.borderWidth = 1
    data.pointRadius = 3
    if opacity is not None:
      data.fillOpacity = opacity
    return data

  def add_dataset(self, data, label="", colors=None, opacity=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param label:
    :param colors:
    :param opacity:
    """
    data = self.new_dataset(len(self._datasets), data, label, colors=colors, opacity=opacity, type=None)
    self._datasets.append(data)
    return data

  @property
  def _js__convertor__(self):
    return ''' 
      if(data.python){
          result = {datasets: [], labels: data.series};
          data.datasets.forEach(function(rec, i){
            result.datasets.push( {label: data.series[i], data: rec, backgroundColor: options.colors[i], borderColor: options.colors[i]} )
          })}
      else{
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_column] in uniqLabels)){labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
              temp[name][rec[options.x_column]] = rec[name]}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.colors[i], borderColor: options.colors[i]};
          for(var attr in options.attrs){dataSet[attr] = options.attrs[attr]};
          labels.forEach(function(x){
            if (temp[series][x] == undefined) {dataSet.data.push(null)} else{dataSet.data.push(temp[series][x])}
          }); result.datasets.push(dataSet)})
      }'''


class ChartBubble(Chart):

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartBubble, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'bubble'

  def new_dataset(self, id, data, label, colors=None, opacity=0.8, type=None):
    data = JsChartJs.DataSetBubble(self._report, attrs={"data": data})
    data.fill = False
    data.label = label
    if colors is None:
      data.borderColor = self._report.theme.charts[id]
      data.backgroundColor = self._report.theme.charts[id]
      data.fillOpacity = opacity
    return data

  def add_dataset(self, data, label, colors=None, opacity=0.8):
    """

    """
    data = self.new_dataset(len(self._datasets), data, label, colors, opacity=opacity)
    self._datasets.append(data)
    return data

  @property
  def _js__convertor__(self):
    return '''
      if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(rec, i){
          result.datasets.push( {label: data.series[i], data: rec, backgroundColor: options.colors[i]} )
        })
      } else {
        var temp = {}; var labels = [];
        options.y_columns.forEach(function(series){temp[series] = []});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              labels.push(rec[options.x_column]); var r = 2; if((options.rDim != undefined) && (rec[options.rDim] != undefined)){r = rec[options.rDim]};
              temp[name].push({y: rec[name], x: rec[options.x_column], r: r})}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.colors[i]};
          labels.forEach(function(x, i){dataSet.data = temp[series]}); 
        result.datasets.push(dataSet)})
      }'''


class ChartBar(ChartLine):

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartBar, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'bar'

  @property
  def options(self):
    """

    :rtype: OptChartJs.OptionsBar
    """
    if self._options is None:
      self._options = OptChartJs.OptionsBar(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label, colors=None, opacity=0.8, type=None):
    if type is not None:
      data = JsChartJs.DataSetBar(self._report, attrs={"data": data, 'type': self._attrs['type']})
    else:
      data = JsChartJs.DataSetBar(self._report, attrs={"data": data})
    data.label = label
    if colors is None:
      data.backgroundColor = self._report.theme.charts[id]
      data.fillOpacity = opacity
    return data

  def add_dataset(self, data, label, type=None, colors=None, opacity=0.8):
    """

    """
    data = self.new_dataset(len(self._datasets), data, label, colors, opacity=opacity, type=type)
    self._datasets.append(data)
    return data


class ChartPolar(Chart):

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartPolar, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'polarArea'

  @property
  def options(self):
    """

    :rtype: OptChartJs.OptionsPolar
    """
    if self._options is None:
      self._options = OptChartJs.OptionsPolar(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label, colors=None, type=None):
    if type is not None:
      data = JsChartJs.DataSetPolar(self._report, attrs={"data": data, 'type': type})
    else:
      data = JsChartJs.DataSetPolar(self._report, attrs={"data": data})
    data.label = label
    data.backgroundColor = self._report.theme.charts
    return data

  def add_dataset(self, data, label, colors=None, opacity=0.4, type=None):
    """

    :return:
    """
    data = self.new_dataset(len(self._datasets), data, label, colors)
    self._datasets.append(data)
    return data

  @property
  def _js__convertor__(self):
    return '''
      if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(rec, i){
          var dataset = {label: data.series[i], data: rec, backgroundColor: options.colors, borderColor: options.colors};
          for(var attr in options.attrs){dataset[attr] = options.attrs[attr]};
          result.datasets.push(dataset)
        })
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_column] in uniqLabels)){labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
              temp[name][rec[options.x_column]] = rec[name]}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.colors, borderColor: options.colors};
          for(var attr in options.attrs){dataSet[attr] = options.attrs[attr]};
          labels.forEach(function(x){
            if (temp[series][x] == undefined) {dataSet.data.push(null)} else{dataSet.data.push(temp[series][x])}
          }); result.datasets.push(dataSet)})
      }'''


class ChartHBar(ChartBar):

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartBar, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'horizontalBar'


class ChartPie(Chart):

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartPie, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'pie'

  @property
  def options(self):
    """

    :rtype: OptChartJs.OptionsPie
    """
    if self._options is None:
      self._options = OptChartJs.OptionsPie(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label="", colors=None, opacity=0.8, type=None):
    data = JsChartJs.DataSetPie(self._report, attrs={"data": data})
    if colors is None:
      data.backgroundColor = self._report.theme.charts
      data.fillOpacity = opacity
    return data

  def add_dataset(self, data, label="", colors=None, opacity=0.8):
    """

    :return:
    """
    data = self.new_dataset(len(self._datasets), data, label, colors=colors, opacity=opacity)
    self._datasets.append(data)
    return data

  @property
  def _js__convertor__(self):
    return ''' 
      if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(rec, i){
          result.datasets.push( {label: data.series[i], data: rec, backgroundColor: options.colors} ) })
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_column] in uniqLabels)){labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
              temp[name][rec[options.x_column]] = rec[name]}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series){
          dataSet = {label: series, data: [], backgroundColor: []};
          labels.forEach(function(x, i){
            dataSet.backgroundColor.push(options.colors[i]);
            if(temp[series][x] == undefined) {dataSet.data.push(null)} else{dataSet.data.push(temp[series][x])}
          }); result.datasets.push(dataSet)})
      }
      '''


class ChartRadar(Chart):

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartRadar, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'radar'

  def new_dataset(self, id, data, label, colors=None, opacity=0.8, type=None):
    data = JsChartJs.DataSetRadar(self._report, attrs={"data": data})
    data.label = label
    if colors is None:
      data.backgroundColor = self._report.theme.charts[id]
      data.borderColor = self._report.theme.charts[id]
      data.borderWidth = 0.2
      data.fillOpacity = opacity
    return data

  def add_dataset(self, data, label, colors=None, opacity=0.4):
    """

    """
    data = self.new_dataset(len(self._datasets), data, label, colors, opacity)
    self._datasets.append(data)
    return data

  @property
  def _js__convertor__(self):
    return '''
      if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(rec, i){
          var dataset = {label: data.series[i], data: rec, backgroundColor: options.colors, borderColor: options.colors[i]};
          for(var attr in options.attrs){dataset[attr] = options.attrs[attr]};
          result.datasets.push(dataset)
        })
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_column] in uniqLabels)){labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
              temp[name][rec[options.x_column]] = rec[name]}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.colors, borderColor: options.colors[i]};
          for(var attr in options.attrs){dataSet[attr] = options.attrs[attr]};
          labels.forEach(function(x){
            if (temp[series][x] == undefined) {dataSet.data.push(null)} else{dataSet.data.push(temp[series][x])}
          }); result.datasets.push(dataSet)})
      }'''


class ChartScatter(Chart):

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartScatter, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'scatter'

  def new_dataset(self, id, data, label, colors=None, type=None):
    data = JsChartJs.DataSetScatterLine(self._report, attrs={"data": data})
    data.fill = False
    data.label = label
    if colors is None:
      data.backgroundColor = self._report.theme.charts[id]
      data.borderColor = self._report.theme.charts[id]
    return data

  def add_dataset(self, data, label, colors=None):
    """

    :return:
    """
    data = self.new_dataset(len(self._datasets), data, label, colors)
    self._datasets.append(data)
    return data

  @property
  def _js__convertor__(self):
    return ''' 
      if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(rec, i){
          result.datasets.push( {label: data.series[i], data: rec, backgroundColor: options.colors[i]} )
        })
      } else {
        var temp = {}; var labels = [];
        options.y_columns.forEach(function(series){temp[series] = []});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              labels.push(rec[options.x_column]); var r = 2; if((options.rDim != undefined) && (rec[options.rDim] != undefined)){r = rec[options.rDim]};
              temp[name].push({y: rec[name], x: rec[options.x_column], r: r})}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.colors[i]};
          labels.forEach(function(x, i){dataSet.data = temp[series]}); 
        result.datasets.push(dataSet)})
      
      }
    '''


class ChartExts(ChartPie):

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartExts, self).__init__(report, width, height, htmlCode, options, profile)
    self.jsImports.add(options['npm'])
    self._attrs['type'] = options['type']

