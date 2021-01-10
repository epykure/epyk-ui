#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css import Colors
from epyk.core.html import Html
from epyk.core.html.options import OptChartJs

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlCharts
from epyk.core.js.packages import packageImport
from epyk.core.js.primitives import JsObject

from epyk.core.js.packages import JsChartJs
from epyk.core.js.packages import JsD3


class ChartJsActivePoints(object):

  def __init__(self, chartId, i, page):
    self.chartId = chartId
    self.num = i or self.index
    self._report = page

  @property
  def index(self):
    """
    Description:
    -----------
    Get the index of the clicked series in teh datasets.

    Usage:
    -----

    :return: A javaScript number.
    """
    return JsObject.JsObject.get("%s.getElementAtEvent(event)[0]._datasetIndex" % self.chartId) # % (self.chartId, self.num))

  @property
  def x(self):
    """
    Description:
    -----------
    Get the name of the selected series.
    """
    return JsObject.JsObject.get("%s.data.datasets[%s].label" % (self.chartId, self.num))

  @property
  def labels(self):
    """
    Description:
    -----------
    Get the series label name.
    """
    return JsObject.JsObject.get("%s.data.labels[activePoints[%s]]" % (self.chartId, self.num))

  @property
  def model(self):
    """
    Description:
    -----------
    Get the series value.
    """
    return JsObject.JsObject.get("activePoints[%s]['_model']" % self.num)

  @property
  def datasetLabel(self):
    """
    Description:
    -----------
    Get the series name.
    """
    return JsObject.JsObject.get("activePoints[%s]['_model'].datasetLabel" % self.num)

  @property
  def label(self):
    """
    Description:
    -----------

    """
    return JsObject.JsObject.get("%s.data.labels[activePoints[%s]._index]" % (self.chartId, self.num))

  @property
  def dataset(self):
    """
    Description:
    -----------
    Get the series dataset.
    """
    return JsObject.JsObject.get("activePoints[%s]['_model'].label" % self.num)

  @property
  def value(self):
    """
    Description:
    -----------
    Get the point value.
    """
    return JsObject.JsObject.get("%s.data.datasets[activePoints[%s]._datasetIndex].data[activePoints[%s]._index]" % (self.chartId, self.num, self.num))


class Chart(Html.Html):
  name = 'ChartJs Chart'
  requirements = ('chart.js', )

  def __init__(self,  report, width, height, htmlCode, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self._chart, self._datasets, self._options, self._data_attrs, self._attrs = None, None, [], None, {}, {}
    self._options_init = options
    self.style.css.margin_top = 10
    self.chartId = "%s_obj" % self.htmlCode
    if hasattr(self, '_chart__type'):
      self._attrs['type'] = self._chart__type

  def activePoints(self, i=None):
    """
    Description:
    -----------
    The current active points selected by an event on a chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    Attributes:
    ----------
    :param i: Integer. Optional. The series index. Default it is the series clicked.
    """
    return ChartJsActivePoints(self.chartId, i, self._report)

  @property
  def d3(self):
    """
    Description:
    -----------
    Property to the D3 library.

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
  def dom(self):
    """
    Description:
    -----------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlCharts.ChartJs
    """
    if self._dom is None:
      self._dom = JsHtmlCharts.ChartJs(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the series options.

    :rtype: OptChartJs.Options
    """
    if self._options is None:
      self._options = OptChartJs.Options(self._report, attrs=self._options_init)
    return self._options

  @property
  def plugins(self):
    """
    Description:
    -----------
    Shortcut property to all the external plugins defined in the framework.

    Related Pages:

      https://www.chartjs.org/docs/2.7.2/notes/extensions.html
    """
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
    Set the labels of the different series in the chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/axes/labelling.html

    Attributes:
    ----------
    :param labels: List. An array of labels.
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
    The data property of a ChartJs chart.

    Related Pages:

      https://www.chartjs.org/docs/master/general/data-structures

    Attributes:
    ----------
    :param i: Integer. The series index according to the y_columns

    :rtype: JsChartJs.DataSetPie
    """
    if i is None:
      return self._datasets[-1]

    return self._datasets[i]

  @property
  def colors(self):
    """
    Description:
    -----------
    Property to the list of colors used for the border of the series in the chart.

    :return: A list of colors.
    """
    return self._options_init['colors']

  @property
  def bgColors(self):
    """
    Description:
    -----------
    Property to the list of colors used to fill the series in the chart.

    :return: A list of colors.
    """
    return self._options_init['bgColors']

  @colors.setter
  def colors(self, hex_values):
    """
    Description:
    -----------
    Set the colors of the chart.
    hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
    If the background colors are not specified they will be deduced from the colors list changing the opacity.

    Attributes:
    ----------
    :param hex_values: List. An array of hexadecimal color codes.
    """
    line_colors, bg_colors = [], []
    for h in hex_values:
      if not isinstance(h, tuple):
        line_colors.append(h)
        bg_colors.append("rgba(%s, %s, %s, %s" % (Colors.getHexToRgb(h)[0], Colors.getHexToRgb(h)[1],
                                                  Colors.getHexToRgb(h)[2], self._options_init['attrs'].get('opacity', 0)))
      else:
        line_colors.append(h[0])
        bg_colors.append(h[0])
    self._options_init['colors'] = line_colors
    self._options_init['bgColors'] = bg_colors
    self._options._attrs['colors'] = self._options_init['colors']
    self._options._attrs['bgColors'] = self._options_init['colors']
    for i, rec in enumerate(self._datasets):
      rec.backgroundColor = self._options_init['bgColors'][i]
      rec.borderColor = self._options_init['colors'][i]
      rec.borderWidth = 1

  def click(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    -----------
    Add a click event on the chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/general/interactions/events.html

    Attributes:
    ----------
    :param jsFncs: List. Set of Javascript function to trigger on this event
    :param profile: Boolean. To set the profiling.
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    tmpJsFncs = ["var activePoints = %s.getElementsAtEvent(event)" % self.chartId]
    tmpJsFncs.append("if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))
    return super(Chart, self).click(tmpJsFncs, profile)

  def dblclick(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    -----------
    Add a double click event on the chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/general/interactions/events.html

    Attributes:
    ----------
    :param jsFncs: List. Set of Javascript function to trigger on this event
    :param profile: Boolean. To set the profiling.
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    tmpJsFncs = ["var activePoints = %s.getElementsAtEvent(event)" % self.chartId]
    tmpJsFncs.append("if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))
    return super(Chart, self).dblclick(tmpJsFncs, profile)

  def hover(self, jsFncs, profile=False, source_event=None):
    """
    Description:
    -----------
    Add an on mouse hover event on the chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/general/interactions/events.html

    Attributes:
    ----------
    :param jsFncs: List. Set of Javascript function to trigger on this event
    :param profile: Boolean. To set the profiling.
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    """
    tmpJsFncs = ["var activePoints = %s.getElementsAtEvent(event)" % self.chartId]
    tmpJsFncs.append("if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))
    return self.on("mouseover", tmpJsFncs, profile)

  @property
  def datasets(self):
    return self._datasets

  def getCtx(self):
    """
    Description:
    -----------
    Get the ChartJs context. The internal configuration of the chart.
    The context is a dictionary object with javascript fragments.

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/
    """
    obj_datasets = "[%s]" % ", ".join([d.toStr() for d in self._datasets])
    self._data_attrs['datasets'] = JsObject.JsObject.get(obj_datasets)
    obj_data = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._data_attrs.items()])
    self._attrs["data"] = JsObject.JsObject.get(obj_data)
    self._attrs["options"] = JsObject.JsObject.get(str(self.options))
    str_ctx = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items()])
    return str_ctx

  def convert(self, data, options, profile=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. To set the profiling.
    """
    mod_name = __name__.split(".")[-1]
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors[self.builder_name] = "function %s%sConvert(data, options){%s; return result}" % (mod_name, self.builder_name, self._js__convertor__)
    if isinstance(data, dict):
      # check if there is no nested HTML components in the data
      tmp_data = []
      for k, v in data.items():
        if isinstance(v, list):
          row = []
          for i in v:
            if isinstance(i, list):
              sub_row = []
              for j in i:
                if hasattr(j, "toStr"):
                  sub_row.append(j.toStr())
                else:
                  sub_row.append(JsUtils.jsConvertData(j, None).toStr())
              row.append("[%s]" % ", ".join(sub_row))
            else:
              if hasattr(i, "toStr"):
                row.append(i.toStr())
              else:
                row.append(JsUtils.jsConvertData(i, None).toStr())
          tmp_data.append("%s: [%s]" % (JsUtils.jsConvertData(k, None), ", ".join(row)))
        else:
          tmp_data.append("%s: %s" % (JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)))
      js_data = "{%s}" % ",".join(tmp_data)
    else:
      js_data = JsUtils.jsConvertData(data, None)
    options, js_options, js_keys = options or self._options_init, [], set()
    if isinstance(options, dict):
      for k, v in self._options_init.items():
        if k not in options:
          js_keys.add(k)
          if isinstance(v, dict):
            row = ["'%s': %s" % (s_k, JsUtils.jsConvertData(s_v, None)) for s_k, s_v in v.items()]
            js_options.append("'%s': {%s}" % (k, ", ".join(row)))
          else:
            if str(v).strip().startswith("function"):
              js_options.append("%s: %s" % (k, v))
            else:
              js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
      for k, v in options.items():
        js_keys.add(k)
        if isinstance(v, dict):
          row = ["'%s': %s" % (s_k, JsUtils.jsConvertData(s_v, None)) for s_k, s_v in v.items()]
          js_options.append("'%s': {%s}" % (k, ", ".join(row)))
        else:
          if str(v).strip().startswith("function"):
            js_options.append("%s: %s" % (k, v))
          else:
            js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
      if 'colors' not in js_keys:
        js_options.append("colors: %s" % JsUtils.jsConvertData(self._options_init['colors'], None))
      if 'bgColors' not in js_keys and 'bgColors' in self._options_init:
        js_options.append("bgColors: %s" % JsUtils.jsConvertData(self._options_init['bgColors'], None))
      if 'attrs' not in js_keys:
        js_options.append('attrs: %s' % JsUtils.jsConvertData(self._options_init['attrs'], None))
      return "%s%sConvert(%s, %s)" % (mod_name, self.builder_name, js_data, "{%s}" % ",".join(js_options))
    else:
      return "%s%sConvert(%s, Object.assign(%s, %s))" % (mod_name, self.builder_name, js_data, self._options_init, options)

  def build(self, data=None, options=None, profile=False):
    """
    Description:
    ------------
    Update the chart with context and / or data changes.

    Attributes:
    ----------
    :param data:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. To set the profiling.
    """
    if data:
      return "Object.assign(window['%(chartId)s'].data, %(data)s); window['%(chartId)s'].update()" % {'chartId': self.chartId, 'data': self.convert(data, options, profile)}

    return '%s = new Chart(%s.getContext("2d"), %s)' % (self.chartId, self.dom.varId, self.getCtx())

  def loading(self, status=True):
    """
    Description:
    ------------
    Loading component on a chart.

    Attributes:
    ----------
    :param status: Boolean. Optional. Specific the status of the display of the loading component.
    """
    if status:
      return ''' 
        if (typeof window['popup_loading_%(htmlId)s'] === 'undefined'){
          var divLoading = document.createElement("div"); window['popup_loading_%(htmlId)s'] = divLoading; 
          divLoading.style.width = '100%%'; divLoading.style.height = '100%%'; divLoading.style.background = '%(background)s';
          divLoading.style.position = 'absolute'; divLoading.style.top = 0; divLoading.style.left = 0; divLoading.style.zIndex = 200;
          divLoading.style.color = '%(color)s'; divLoading.style.textAlign = 'center'; divLoading.style.paddingTop = '50vh';
          divLoading.innerHTML = "<div style='font-size:50px'><i class='fas fa-spinner fa-spin' style='margin-right:10px'></i>Loading...</div>";
          document.getElementById('%(htmlId)s').parentNode.appendChild(divLoading)
        }''' % {"htmlId": self.htmlCode, 'color': self._report.theme.success[1], 'background': self._report.theme.greys[0]}

    return '''
      if (typeof window['popup_loading_%(htmlId)s'] !== 'undefined'){
        document.getElementById('%(htmlId)s').parentNode.removeChild(window['popup_loading_%(htmlId)s']); 
        window['popup_loading_%(htmlId)s'] = undefined}''' % {"htmlId": self.htmlCode}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<canvas %s></canvas>' % self.get_attrs(pyClassNames=self.style.get_classes())


class Fabric(Html.Html):
  name = 'ChartJs Fabric'
  requirements = ('chart.js', )

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(Fabric, self).__init__(report, [], htmlCode=htmlCode, options=options, profile=profile)
    self.attr["data-counter"] = 0
    self.attr["data-next"] = 1
    self.attr["data-current"] = 0
    self.chart = ChartBar(report, width, height, None, options, profile)
    self.chart.options.scales.y_axis().ticks.toNumber()
    self.chart.options.managed = False
    self.chart.chartId = "window['%s_' + %s]" % (self.htmlCode, self.dom.getAttribute("data-current"))

  def new(self):
    return self.dom.appendChild(JsObject.JsObject.get('''(function(htmlObj){
      var comp = document.createElement('canvas'); comp.id = htmlObj.id + "_" + htmlObj.getAttribute("data-next"); 
      htmlObj.setAttribute("data-counter", parseInt(htmlObj.getAttribute("data-counter")) + 1);
      htmlObj.setAttribute("data-current", htmlObj.getAttribute("data-next"));
      htmlObj.setAttribute("data-next", parseInt(htmlObj.getAttribute("data-next")) + 1);
      return comp})(%(htmlId)s)''' % {"htmlId": self.dom.varId}))

  def build(self, data=None, options=None, profile=False):
    return '''%(chartId)s = new Chart(%(chartId)s.getContext('2d'), {type: 'bar'}); 
      Object.assign(%(chartId)s.data, %(data)s); %(chartId)s.update()''' % {"chartId": self.chart.chartId, "data": self.chart.convert(data, options, profile)}

  def create(self, data=None, options=None, attrs=None, profile=False):
    return self.dom.appendChild(JsObject.JsObject.get('''(function(htmlObj){
      var comp = document.createElement('canvas'); comp.id = htmlObj.id + "_" + htmlObj.getAttribute("data-next"); 
      htmlObj.setAttribute("data-counter", parseInt(htmlObj.getAttribute("data-counter")) + 1);
      htmlObj.setAttribute("data-current", htmlObj.getAttribute("data-next"));
      htmlObj.setAttribute("data-next", parseInt(htmlObj.getAttribute("data-next")) + 1);
      %(chartId)s = new Chart(comp.getContext('2d'), %(options)s); 
      Object.assign(%(chartId)s.data, %(data)s); %(chartId)s.update()
      return comp})(%(htmlId)s)
      ''' % {"htmlId": self.dom.varId, "options": options, "chartId": self.chart.chartId, "data": self.chart.convert(data, attrs, profile)}))

  def __str__(self):
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class Datasets(object):

  def __init__(self, report):
    self._report, self.__data = report, []

  def add(self, data):
    """
    Description:
    ------------
    Add a series to an existing dataset.

    Attributes:
    ----------
    :param data: List. A list of numbers.
    """
    self.__data.append(data)
    return self


class ChartLine(Chart):
  _chart__type = 'line'

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the specific ChartJs Line chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html

    :rtype: OptChartJs.OptionsLine
    """
    if self._options is None:
      self._options = OptChartJs.OptionsLine(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label, colors=None, opacity=None, type=None):
    """
    Description:
    ------------
    Add a new series to the chart datasets.
    The dataset structure of a chart is a list of dataset.

    For a chart line the default Opacity is None which will set the fill to attribute to False.

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/elements.html

    Attributes:
    ----------
    :param id: Integer. The index of the dataset in the chart list of datasets.
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color definition to be used to set the color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    :param type: String. Optional. THe series type. Default to the chart type if not supplied.
    """
    data = JsChartJs.DataSetScatterLine(self._report, attrs={"data": data})
    if opacity is None:
      data.fill = False
    data.label = label
    opacity = opacity or self.options['attrs'].get("opacity", 0)
    if not opacity:
      self.options['attrs'][label] = {"fill": False}
    data.set_style(backgroundColor=self.bgColors[id], fillOpacity=opacity, borderWidth=1, borderColor=colors or self.colors[id])
    return data

  def add_dataset(self, data, label="", colors=None, opacity=None):
    """
    Description:
    ------------
    Add a new Dataset to the chart list of Datasets.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: List. The list of points (float).
    :param colors: List. Optional. The color definition to be used to set the color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    """
    data = self.new_dataset(len(self._datasets), data, label, colors=colors, opacity=opacity, type=None)
    self._datasets.append(data)
    return data

  @property
  def _js__convertor__(self):
    return '''
      if(data.python){
        result = {datasets: [], labels: data.labels};
        data.datasets.forEach(function(rec, i){
          result.datasets.push({label: data.series[i], data: rec, backgroundColor: options.colors[i], borderColor: options.colors[i]})})}
      else{
        var temp = {}; var labels = []; var uniqLabels = {}; 
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){ 
          if(rec[name] !== undefined){
            if (!(rec[options.x_axis] in uniqLabels)){labels.push(rec[options.x_axis]); uniqLabels[rec[options.x_axis]] = true}; 
            temp[name][rec[options.x_axis]] = rec[name]}})
        }); 
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
            dataSet = {label: series, data: [], backgroundColor: options.bgColors[i], hoverBackgroundColor: options.colors[i], 
                       borderColor: options.colors[i], borderColor: options.colors[i], borderWidth: 1,
                       hoverBorderColor: options.colors[i]};
            if (typeof options.attrs[series] !== 'undefined'){
            for(var attr in options.attrs[series]){dataSet[attr] = options.attrs[series][attr]}}
            else if(typeof options.commons !== 'undefined'){
              for(var attr in options.commons){dataSet[attr] = options.commons[attr]}}
              labels.forEach(function(x){
                if (temp[series][x] == undefined){dataSet.data.push(null)} else {dataSet.data.push(temp[series][x])}}); 
          result.datasets.push(dataSet)})
      }'''


class ChartBubble(Chart):
  _chart__type = 'bubble'

  def new_dataset(self, id, data, label, colors=None, opacity=None, type=None):
    """
    Description:
    ------------
    Add a new series to the chart datasets.
    The dataset structure of a chart is a list of dataset.

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/elements.html

    Attributes:
    ----------
    :param id: Integer. The index of the dataset in the chart list of datasets.
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color definition to be used to set the color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    :param type: String. Optional. THe series type. Default to the chart type if not supplied.
    """
    data = JsChartJs.DataSetBubble(self._report, attrs={"data": data})
    data.fill = False
    data.label = label
    data.set_style(backgroundColor=self.bgColors[id], fillOpacity=opacity or self.options['attrs'].get("opacity", 0),
                   borderWidth=1, borderColor=colors or self.colors[id])
    return data

  def add_dataset(self, data, label, colors=None, opacity=None):
    """
    Description:
    ------------
    Add a new Dataset to the chart list of Datasets.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: List. The list of points (float).
    :param colors: List. Optional. The color definition to be used to set the color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
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
          result.datasets.push( {label: data.series[i], data: rec, backgroundColor: options.colors[i]})})
      } else {
        var temp = {}; var labels = [];
        options.y_columns.forEach(function(series){temp[series] = []});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[options.x_axis] !== undefined){
              labels.push(rec[options.x_axis]); var r = 2; if((options.rDim != undefined) && (rec[options.rDim] != undefined)){r = rec[options.rDim]};
              temp[name].push({y: rec[name], x: rec[options.x_axis], r: r})}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.colors[i]};
          if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x, i){dataSet.data = temp[series]}); 
        result.datasets.push(dataSet)})
      }'''


class ChartBar(ChartLine):
  _chart__type = 'bar'

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the bar chart options.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html

    :rtype: OptChartJs.OptionsBar
    """
    if self._options is None:
      self._options = OptChartJs.OptionsBar(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label, colors=None, opacity=None, type=None):
    """
    Description:
    ------------
    Add a new series to the chart datasets.
    The dataset structure of a chart is a list of dataset.

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/elements.html

    Attributes:
    ----------
    :param id: Integer. The index of the dataset in the chart list of datasets.
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color definition to be used to set the color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    :param type: String. Optional. THe series type. Default to the chart type if not supplied.
    """
    series_attrs = {"data": data, 'type': type or self._attrs['type']}
    if series_attrs['type'] == 'line':
      data = JsChartJs.DataSetScatterLine(self._report, attrs=series_attrs)
    else:
      data = JsChartJs.DataSetBar(self._report, attrs=series_attrs)
    data.label = label
    data.set_style(backgroundColor=self.bgColors[id], fillOpacity=opacity or self.options['attrs'].get("opacity", 0),
                   borderWidth=1, borderColor=colors or self.colors[id])
    return data

  def add_dataset(self, data, label, type=None, colors=None, opacity=None, alias=None):
    """
    Description:
    ------------
    Add a new Dataset to the chart list of Datasets.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color definition to be used to set the color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    :param type: String. Optional. THe series type. Default to the chart type if not supplied.
    :param alias: String. The chart alias name visible in the legend. Default the label.
    """
    data = self.new_dataset(len(self._datasets), data, label, colors, opacity=opacity, type=type)
    self._datasets.append(data)
    alias = alias or label
    if alias not in self.options['y_columns']:
      self.options['y_columns'].append(alias)
      self.options['attrs'][alias] = {"type": type or self._attrs['type'], 'fill': False}
    return data


class ChartPolar(Chart):
  _chart__type = 'polarArea'

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the Polar chart options.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/polar.html

    :rtype: OptChartJs.OptionsPolar
    """
    if self._options is None:
      self._options = OptChartJs.OptionsPolar(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label, colors=None, type=None):
    """
    Description:
    -----------

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param id: Integer. The index of the dataset in the chart list of datasets.
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color definition to be used to set the color for this series. Default the global definition.
    :param type: String. Optional. THe series type. Default to the chart type if not supplied.
    """
    if type is not None:
      data = JsChartJs.DataSetPolar(self._report, attrs={"data": data, 'type': type})
    else:
      data = JsChartJs.DataSetPolar(self._report, attrs={"data": data})
    data.set_style(backgroundColor=self.bgColors[id], fillOpacity=self.options['attrs'].get("opacity", 0), borderWidth=1,
                   borderColor=colors or self.colors[id])
    data.label = label
    return data

  def add_dataset(self, data, label, colors=None, opacity=None, type=None):
    """
    Description:
    -----------

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color definition to be used to set the color for this series. Default the global definition.
    :param opacity:
    :param type: String. Optional. THe series type. Default to the chart type if not supplied.
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
          result.datasets.push(dataset)})
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_axis] in uniqLabels)){labels.push(rec[options.x_axis]); uniqLabels[rec[options.x_axis]] = true};
              temp[name][rec[options.x_axis]] = rec[name]}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.bgColors, borderColor: options.colors};
          for(var attr in options.attrs){dataSet[attr] = options.attrs[attr]};
          if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x){
            if (temp[series][x] == undefined) {dataSet.data.push(null)} else{dataSet.data.push(temp[series][x])}
          }); result.datasets.push(dataSet)})
      }'''


class ChartHBar(ChartBar):
  _chart__type = 'horizontalBar'


class ChartPie(Chart):
  _chart__type = 'pie'

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the Pie Chart options.

    :rtype: OptChartJs.OptionsPie
    """
    if self._options is None:
      self._options = OptChartJs.OptionsPie(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label="", colors=None, opacity=None, type=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param id:
    :param data:
    :param label:
    :param colors:
    :param opacity:
    :param type:
    """
    data = JsChartJs.DataSetPie(self._report, attrs={"data": data})
    if colors is None:
      data.set_style(backgroundColors=self.bgColors, fillOpacity=opacity, borderWidth=1, borderColors=self.colors)
    return data

  def add_dataset(self, data, label="", colors=None, opacity=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param label:
    :param colors:
    :param opacity:
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
              if (!(rec[options.x_axis] in uniqLabels)){labels.push(rec[options.x_axis]); uniqLabels[rec[options.x_axis]] = true};
              temp[name][rec[options.x_axis]] = rec[name]}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series){
          dataSet = {label: series, data: [], backgroundColor: options.bgColors, borderColor: options.colors};
          if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x, i){
            dataSet.backgroundColor.push(options.colors);
            if(temp[series][x] == undefined) {dataSet.data.push(null)} else{dataSet.data.push(temp[series][x])}
          }); result.datasets.push(dataSet)})}
      '''


class ChartRadar(Chart):
  _chart__type = 'radar'

  def new_dataset(self, id, data, label, colors=None, opacity=None, type=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param id:
    :param data:
    :param label:
    :param colors:
    :param opacity:
    :param type:
    """
    data = JsChartJs.DataSetRadar(self._report, attrs={"data": data})
    data.label = label
    if colors is None:
      data.backgroundColor = self.colors[id]
      data.borderColor = self.colors[id]
      data.borderWidth = 0.2
      data.fillOpacity = opacity or self.options['attrs'].get("opacity", 0)
    return data

  def add_dataset(self, data, label, colors=None, opacity=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param label:
    :param colors:
    :param opacity:
    """
    dataset = self.new_dataset(len(self._datasets), data, label, colors, opacity)
    self._datasets.append(dataset)
    return dataset

  @property
  def _js__convertor__(self):
    return '''
      if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(rec, i){
          var dataset = {label: data.series[i], data: rec, backgroundColor: options.colors, borderColor: options.colors[i]};
          for(var attr in options.attrs){dataset[attr] = options.attrs[attr]};
          result.datasets.push(dataset)})
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_axis] in uniqLabels)){labels.push(rec[options.x_axis]); uniqLabels[rec[options.x_axis]] = true}; 
              temp[name][rec[options.x_axis]] = rec[name]}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.colors, borderColor: options.colors[i]};
          for(var attr in options.attrs){dataSet[attr] = options.attrs[attr]};
          if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x){
            if (temp[series][x] == undefined) {dataSet.data.push(null)} else{dataSet.data.push(temp[series][x])}
          }); result.datasets.push(dataSet)})}
      '''


class ChartScatter(Chart):
  _chart__type = 'scatter'

  def new_dataset(self, id, data, label, colors=None, type=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param id:
    :param data:
    :param label:
    :param colors:
    :param type:
    """
    data = JsChartJs.DataSetScatterLine(self._report, attrs={"data": data})
    data.fill = False
    data.label = label
    if colors is None:
      data.backgroundColor = self.colors[id]
      data.borderColor = self.colors[id]
    return data

  def add_dataset(self, data, label, colors=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param label:
    :param colors:
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
          result.datasets.push( {label: data.series[i], data: rec, backgroundColor: options.colors[i]})})
      } else {
        var temp = {}; var labels = [];
        options.y_columns.forEach(function(series){temp[series] = []});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[options.x_axis] !== undefined){
              labels.push(rec[options.x_axis]); var r = 2; if((options.rDim != undefined) && (rec[options.rDim] != undefined)){r = rec[options.rDim]};
              temp[name].push({y: rec[name], x: rec[options.x_axis], r: r})}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.colors[i]};
          if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x, i){dataSet.data = temp[series]}); 
        result.datasets.push(dataSet)})}
    '''


class ChartExts(ChartPie):

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartExts, self).__init__(report, width, height, htmlCode, options, profile)
    self.jsImports.add(options['npm'])
    self._attrs['type'] = options['type']

