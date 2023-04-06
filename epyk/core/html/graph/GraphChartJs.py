#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Dict
from epyk.core.py import primitives
from epyk.core.css import Colors
from epyk.core.html import Html
from epyk.core.html.options import OptChartJs

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlCharts
from epyk.core.js.packages import packageImport
from epyk.core.js.primitives import JsObject

from epyk.core.py import types
from epyk.core.js.packages import JsChartJs


class ChartJsActivePoints:

  def __init__(self, chart_id, i, page: primitives.PageModel):
    self.chartId = chart_id
    self.page = page
    self.num = i or self.index

  @property
  def index(self):
    """   Get the index of the clicked series in teh datasets.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().index])

    :return: A javaScript number.
    """
    if min(self.page.imports.pkgs.chart_js.version) > '3.0.0':
      return JsObject.JsObject.get(
        "%s.getElementsAtEventForMode(event, 'nearest', {intersect: true}, true)[0].datasetIndex" % self.chartId)

    return JsObject.JsObject.get("%s.getElementAtEvent(event)[0]._datasetIndex" % self.chartId)

  @property
  def x(self):
    """   Get the name of the selected series.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().x])
    """
    return JsObject.JsObject.get("%s.data.datasets[%s].label" % (self.chartId, self.num))

  @property
  def y(self):
    """   Get the value of the selected series.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().y])
    """
    return JsObject.JsObject.get("%s.data.datasets[%s].data[activePoints[0].index]" % (self.chartId, self.num))

  @property
  def labels(self):
    """   Get the series label name.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().labels])
    """
    return JsObject.JsObject.get("%s.data.labels[activePoints[Math.min(%s, activePoints.length - 1)]]" % (
      self.chartId, self.num))

  @property
  def model(self):
    """   Get the series value.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().model])
    """
    return JsObject.JsObject.get("activePoints[Math.min(%s, activePoints.length - 1)]['_model']" % self.num)

  @property
  def datasetLabel(self):
    """   Get the series name.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().datasetLabel])
    """
    return JsObject.JsObject.get(
      "activePoints[Math.min(%s, activePoints.length - 1)]['_model'].datasetLabel" % self.num)

  @property
  def label(self):
    """   

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().label])
    """
    if min(self.page.imports.pkgs.chart_js.version) > '3.0.0':
      return JsObject.JsObject.get("%s.data.labels[activePoints[Math.min(%s, activePoints.length - 1)].index]" % (
        self.chartId, self.num))

    return JsObject.JsObject.get("%s.data.labels[activePoints[Math.min(%s, activePoints.length - 1)]._index]" % (
      self.chartId, self.num))

  @property
  def dataset(self):
    """   Get the series dataset.

    Usage::

    """
    return JsObject.JsObject.get("activePoints[Math.min(%s, activePoints.length - 1)]['_model'].label" % self.num)

  @property
  def value(self):
    """   Get the point value.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().value])
    """
    return JsObject.JsObject.get("%s.data.datasets[activePoints[Math.min(%s, activePoints.length - 1)]._datasetIndex].data[activePoints[Math.min(%s, activePoints.length - 1)]._index]" % (self.chartId, self.num, self.num))

  def toStr(self):
    """ """
    return JsObject.JsObject.get("activePoints")


class Chart(Html.Html):
  name = 'ChartJs'
  requirements = ('chart.js', )
  _option_cls = OptChartJs.ChartJsOptions
  _chart__type = None

  def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(
      page, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self._chart, self._datasets, self._data_attrs, self._attrs = None, [], {}, {}
    self.style.css.margin_top = 10
    self.style.css.position = "relative"
    self.chartId = "%s_obj" % self.htmlCode
    self.options.type = self._chart__type
    self.options.maintainAspectRatio = False
    self._attrs["type"] = self._chart__type
    self.attr["class"].add("chart-container")
    self.__defined_options = None

  def activePoints(self, i: int = None) -> ChartJsActivePoints:
    """   The current active points selected by an event on a chart.

    Usage::

        activePoints

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    :param i: Optional. The series index. Default it is the series clicked.
    """
    return ChartJsActivePoints(self.chartId, i, self.page)

  @property
  def type(self):
    return self._attrs["type"]

  @type.setter
  def type(self, value: str):
    self._attrs["type"] = value

  @property
  def shared(self):
    """   All the common properties shared between all the charts.
    This will ensure a compatibility with the plot method.

    Usage::

      line = page.ui.charts.chartJs.bar()
      line.shared.x_label("x axis")
    """
    return OptChartJs.OptionsChartSharedChartJs(component=self)

  @property
  def js(self) -> JsChartJs.ChartJs:
    """   Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    Usage::

      line = page.ui.charts.chartJs.bar()
      page.ui.button("Load").click([line.js.add(6, {"test 2": 34})])

    :return: A Javascript object.
    """
    if self._js is None:
      self._js = JsChartJs.ChartJs(selector="window['%s']" % self.chartId, component=self, page=self.page)
    return self._js

  @property
  def dom(self) -> JsHtmlCharts.ChartJs:
    """   Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage::

    :return: A Javascript Dom object.
    """
    if self._dom is None:
      self._dom = JsHtmlCharts.ChartJs(page=self.page, component=self)
    return self._dom

  @property
  def options(self) -> OptChartJs.ChartJsOptions:
    """   Property to the series options.

    Usage::

    """
    return super().options

  @property
  def plugins(self):
    """ Shortcut property to all the external plugins defined in the framework.

    Related Pages:

      https://www.chartjs.org/docs/2.7.2/notes/extensions.html
      https://github.com/chartjs/awesome#charts
    """
    return self.options.plugins

  @packageImport('chartjs-plugin-dragdata')
  def dragData(self):
    """   A plugin for Chart.js >= 2.4.0.

    Makes data points draggable. Supports touch events.

    Usage::

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata
    """
    self.options._attrs['dragData'] = True
    return self.options

  def labels(self, labels: list):
    """ Set the labels of the different series in the chart.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/axes/labelling.html

    :param labels: An array of labels
    """
    self._data_attrs['labels'] = labels
    return self

  def label(self, i: int, name: str):
    """ Change the series name.

    Usage::

    :param i: The series index according to the y_columns
    :param name: The new name to be set
    """
    self.dataset(i).label = name
    return self

  def dataset(self, i: int = None) -> JsChartJs.DataSetPie:
    """   The data property of a ChartJs chart.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/master/general/data-structures

    :param i: Optional. The series index according to the y_columns
    """
    if i is None:
      return self._datasets[-1]

    return self._datasets[i]

  def colors(self, hex_values: list):
    """   Set the colors of the chart.

    hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
    If the background colors are not specified they will be deduced from the colors list changing the opacity.

    Usage::

    :param hex_values: An array of hexadecimal color codes
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
    for i, rec in enumerate(self._datasets):
      if self._chart__type in ["pie", "polarArea"]:
        rec.backgroundColor = self.options.background_colors
        rec.borderColor = self.options.colors
      else:
        rec.backgroundColor = self.options.background_colors[i]
        rec.borderColor = self.options.colors[i]
      rec.borderWidth = 1

  def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False,
            source_event: str = None, on_ready: bool = False):
    """   Add a click event on the chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/general/interactions/events.html

    :param js_funcs: Set of Javascript function to trigger on this event
    :param profile: Optional. A flag to set the component performance storage
    :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    if min(self.page.imports.pkgs.chart_js.version) > '3.0.0':
      tmp_js_funcs = [
        "var activePoints = %s.getElementsAtEventForMode(event, 'nearest', { intersect: true }, true)" % self.chartId,
        "if(activePoints.length > 0){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True)]
    else:
      tmp_js_funcs = [
        "var activePoints = %s.getElementsAtEvent(event)" % self.chartId,
        "if(activePoints.length > 0){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True)]
    return super(Chart, self).click(tmp_js_funcs, profile)

  def dblclick(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False, source_event: str = None,
               on_ready: bool = False):
    """   Add a double click event on the chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/general/interactions/events.html

    :param js_funcs: Set of Javascript function to trigger on this event
    :param profile: Optional. A flag to set the component performance storage
    :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
    """
    if min(self.page.imports.pkgs.chart_js.version) > '3.0.0':
      tmp_js_funcs = [
        "var activePoints = %s.getElementsAtEventForMode(event, 'nearest', { intersect: true }, true)" % self.chartId,
        "if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(js_funcs, toStr=True)]
    else:
      tmp_js_funcs = [
        "var activePoints = %s.getElementsAtEvent(event)" % self.chartId,
        "if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(js_funcs, toStr=True)]
    return super(Chart, self).dblclick(tmp_js_funcs, profile)

  def hover(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False, source_event: str = None):
    """   Add an on mouse hover event on the chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/general/interactions/events.html

    :param js_funcs: Set of Javascript function to trigger on this event
    :param profile: Optional. A flag to set the component performance storage
    :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
    """
    if min(self.page.imports.pkgs.chart_js.version) > '3.0.0':
      tmp_js_funcs = [
        "var activePoints = %s.getElementsAtEventForMode(event, 'nearest', { intersect: true }, true)" % self.chartId,
        "if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(js_funcs, toStr=True)]
    else:
      tmp_js_funcs = [
        "var activePoints = %s.getElementsAtEvent(event)" % self.chartId,
        "if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(js_funcs, toStr=True)]
    return self.on("mouseover", tmp_js_funcs, profile)

  @property
  def datasets(self):
    """ Get all the datasets defined for a chart.
    """
    return self._datasets

  def getCtx(self, options: dict = None):
    """   Get the ChartJs context. The internal configuration of the chart.
    The context is a dictionary object with javascript fragments.

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/

    :param options: Optional. The chart options
    """
    obj_datasets = "[%s]" % ", ".join([d.toStr() for d in self._datasets])
    self._data_attrs['datasets'] = JsObject.JsObject.get(obj_datasets)
    obj_data = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._data_attrs.items()])
    self._attrs["data"] = JsObject.JsObject.get(obj_data)
    self._attrs["options"] = self.options.config_js(options)
    str_ctx = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items()])
    return str_ctx

  def define(self, options: types.JS_DATA_TYPES = None) -> str:
    """ Override the chart settings on the JavaScript side.
    This will allow ot set specific styles for some series or also add commons properties.

    Usage:

      chart.onReady([chart.define({"commons": {"backgroundColor": ["pink"], "label": "Other series"}})])

    :param options: JavaScript of Python attributes
    """
    defined_options = "window.%s_options" % self.html_code
    js_expr = "%s = Object.assign(%s ?? %s, %s)" % (
      defined_options, defined_options, self.options.config_js(), JsUtils.jsConvertData(options, None))
    self.__defined_options = defined_options
    return js_expr

  def build(self, data: types.JS_DATA_TYPES = None, options: types.JS_DATA_TYPES = None,
            profile: types.PROFILE_TYPE = None, component_id: str = None):
    """ Update the chart with context and / or data changes.

    :param data: Optional. The full datasets object expected by ChartJs
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    :param component_id: Optional. Not used
    """
    if data is not None:
      js_convertor = "%s%s" % (self.name, self._chart__type)
      self.page.properties.js.add_constructor(
        js_convertor, "function %s(data, options){%s}" % (js_convertor, self._js__builder__))
      profile = self.with_profile(profile, event="Builder", element_id=self.chartId)
      if profile:
        js_func_builder = JsUtils.jsConvertFncs([
          "var result = %s(data, options)" % js_convertor], toStr=True, profile=profile)
        js_convertor = "(function(data, options){%s; return result})" % js_func_builder
      return """Object.assign(window['%(chartId)s'].data, %(chartFnc)s(%(data)s, %(options)s)); 
        window['%(chartId)s'].update()""" % {
        'chartId': self.chartId, 'chartFnc': js_convertor, "data": JsUtils.jsConvertData(data, None),
        "options": self.__defined_options or self.options.config_js(options)}
    return '%(chartId)s = new Chart(%(component)s.getContext("2d"), %(ctx)s)' % {
      "chartId": self.chartId, "component": component_id or self.dom.varId, "ctx": self.getCtx(options)}

  def loading(self, status: bool = True, z_index: int = 500, label: str = "Loading...."):
    """ Loading component on a chart.

    Usage::

        chart_obj.loading()
        ....
        chart_obj.loading(False)

    :param status: Optional. Specific the status of the display of the loading component
    :param label: Optional.
    :param z_index: Optional. Specifies the stack order of an element
    """
    if status:
      try:
        loading_height = "%spx" % int(self.height / 2)
      except:
        loading_height = "30%"
      return ''' 
if (typeof window['popup_loading_%(htmlId)s'] === 'undefined'){
  var divLoading = document.createElement("div"); window['popup_loading_%(htmlId)s'] = divLoading; 
  divLoading.style.width = '100%%'; divLoading.style.height = '100%%'; divLoading.style.background = '%(background)s';
  divLoading.style.position = 'absolute'; divLoading.style.top = 0; divLoading.style.left = 0;
  divLoading.style.zIndex = %(z_index)s; divLoading.style.color = '%(color)s'; divLoading.style.textAlign = 'center'; 
  divLoading.style.display = 'block'; 
  var divLoadingContainer = document.createElement("p"); divLoadingContainer.style.marginTop = '%(height)s'; 
  var divLoadingIcon = document.createElement("i"); divLoadingIcon.classList.add("fas", "fa-spinner", "fa-spin");
  divLoadingIcon.style.marginRight = "5px"; divLoadingContainer.appendChild(divLoadingIcon); 
  var divLoadingContent = document.createElement("span"); divLoadingContent.innerHTML = %(label)s;
  divLoadingContainer.appendChild(divLoadingContent);
  divLoading.appendChild(divLoadingContainer); document.getElementById('%(htmlId)s').parentNode.appendChild(divLoading)
}''' % {"htmlId": self.htmlCode, 'color': self.page.theme.greys[-3], 'background': self.page.theme.greys[0],
        'label': JsUtils.jsConvertData(label, None), "z_index": z_index, "height": loading_height}

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s><canvas id="%s"></canvas></div>' % (
      self.get_attrs(css_class_names=self.style.get_classes(), with_id=False), self.htmlCode)


class Fabric(Html.Html):
  name = 'ChartJs Fabric'
  requirements = ('chart.js', )

  def __init__(self, page, width, height, html_code, options, profile):
    super(Fabric, self).__init__(page, [], html_code=html_code, options=options, profile=profile)
    self.attr.update({"data-counter": 0, "data-next": 1, "data-current": 0})
    self.chart = ChartBar(page, width, height, None, options, profile)
    self.chart.colors(self.page.theme.charts)
    self.chart.options.scales.y_axis().ticks.toNumber()
    self.chart.options.managed = False
    self.chart.chartId = "window['%s_' + %s]" % (self.htmlCode, self.dom.getAttribute("data-current"))

  def new(self):
    """

    Usage::

    """
    return self.dom.appendChild(JsObject.JsObject.get('''(function(htmlObj){
      var comp = document.createElement('canvas'); comp.id = htmlObj.id + "_" + htmlObj.getAttribute("data-next"); 
      htmlObj.setAttribute("data-counter", parseInt(htmlObj.getAttribute("data-counter")) + 1);
      htmlObj.setAttribute("data-current", htmlObj.getAttribute("data-next"));
      htmlObj.setAttribute("data-next", parseInt(htmlObj.getAttribute("data-next")) + 1);
      return comp})(%(htmlId)s)''' % {"htmlId": self.dom.varId}))

  def build(self, data=None, options: dict = None, profile=False, component_id=None):
    """

    Usage::

    :param data:
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    :param component_id:
    """
    return '''%(chartId)s = new Chart(%(dom)s.getContext('2d'), {type: 'bar'}); 
      Object.assign(%(chartId)s.data, %(data)s); %(chartId)s.update()''' % {
      "chartId": self.chart.chartId, "dom": component_id or self.chart.chartId,
      "data": self.chart.build(data, options, profile)}

  def create(self, data=None, options=None, attrs=None, profile=False):
    """

    Usage::

    :param data:
    :param options: Optional. Specific Python options available for this component
    :param attrs: Optional.
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.dom.appendChild(JsObject.JsObject.get('''(function(htmlObj){
      var comp = document.createElement('canvas'); comp.id = htmlObj.id + "_" + htmlObj.getAttribute("data-next"); 
      htmlObj.setAttribute("data-counter", parseInt(htmlObj.getAttribute("data-counter")) + 1);
      htmlObj.setAttribute("data-current", htmlObj.getAttribute("data-next"));
      htmlObj.setAttribute("data-next", parseInt(htmlObj.getAttribute("data-next")) + 1);
      %(chartId)s = new Chart(comp.getContext('2d'), %(options)s); 
      Object.assign(%(chartId)s.data, %(data)s); %(chartId)s.update()
      return comp})(%(htmlId)s)
      ''' % {"htmlId": self.dom.varId, "options": options, "chartId": self.chart.chartId,
             "data": self.chart.build(data, attrs, profile)}))

  def __str__(self):
    return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())


class Datasets:

  def __init__(self, page):
    self.page, self.__data = page, []

  def add(self, data):
    """ Add a series to an existing dataset.

    Usage::

    :param data: A list of numbers
    """
    self.__data.append(data)
    return self


class ChartLine(Chart):
  _chart__type = 'line'
  _option_cls = OptChartJs.OptionsLine

  @property
  def options(self) -> OptChartJs.OptionsLine:
    """ Property to the specific ChartJs Line chart.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return super().options

  def new_dataset(self, index, data, label, colors=None, opacity=None, kind=None, **kwargs):
    """ Add a new series to the chart datasets.
    The dataset structure of a chart is a list of dataset.

    For a chart line the default Opacity is None which will set the fill to attribute to False.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/elements.html

    :param index: The index of the dataset in the chart list of datasets
    :param data: The list of points (float)
    :param label: The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity level for the content
    :param kind: Optional. THe series type. Default to the chart type if not supplied
    """
    data = JsChartJs.DataSetScatterLine(self.page, attrs={"data": data})
    if opacity is None:
      data.fill = False
    data.label = label
    opacity = opacity or self.options.opacity
    if not opacity:
      self.options.props[label] = {"fill": False}
    data.set_style(background_color=self.options.background_colors[index], fill_opacity=opacity or self.options.opacity,
                   border_width=1, border_color=colors or self.options.colors[index])
    for k, v in kwargs.items():
      if hasattr(data, k):
        setattr(data, k, v)
      else:
        data._attrs[k] = v
    return data

  def add_dataset(self, data, label: str = "", colors=None, opacity=None, kind=None, **kwargs):
    """ Add a new Dataset to the chart list of Datasets.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    :param data: The list of points (float)
    :param label: Optional. The list of points (float)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity level for the content
    :param kind: Optional. The chart type
    """
    data = self.new_dataset(len(self._datasets), data, label, colors=colors, opacity=opacity, kind=None, **kwargs)
    self._datasets.append(data)
    return data

  _js__builder__ = '''
      if(data.python){
        result = {datasets: [], labels: data.labels};
        data.datasets.forEach(function(dataset, i){
          if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
          if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
          if(typeof dataset.hoverBackgroundColor === "undefined"){
            dataset.hoverBackgroundColor = options.background_colors[i]};
          if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
          result.datasets.push(dataset) })
      } else{
        var temp = {}; var labels = []; var uniqLabels = {}; 
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){ 
          if(rec[name] !== undefined){
            if (!(rec[options.x_axis] in uniqLabels)){
              labels.push(rec[options.x_axis]); uniqLabels[rec[options.x_axis]] = true}; 
            temp[name][rec[options.x_axis]] = rec[name]}})
        }); 
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
            dataSet = {label: series, data: [], backgroundColor: options.background_colors[i], type: options.type, 
                 hoverBackgroundColor: options.colors[i], borderColor: options.colors[i], 
                 borderColor: options.colors[i], borderWidth: 1, hoverBorderColor: options.colors[i]};
            if ((typeof options.props !== 'undefined') && (typeof options.props[series] !== 'undefined')){
              for(var attr in options.props[series]){dataSet[attr] = options.props[series][attr]}}
            else if(typeof options.commons !== 'undefined'){
              for(var attr in options.commons){dataSet[attr] = options.commons[attr]}}
              labels.forEach(function(x){
                if (temp[series][x] == undefined){dataSet.data.push(null)} else {dataSet.data.push(temp[series][x])}}); 
            if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
              dataSet = Object.assign(dataSet, options.datasets[series])}
          result.datasets.push(dataSet)});
          if (typeof options.labels !== "undefined"){ result.labels = options.labels}
      }; return result'''


class ChartBubble(Chart):
  _chart__type = 'bubble'
  _option_cls = OptChartJs.OptionsBubble

  def new_dataset(self, index, data, label, colors=None, opacity=None, kind=None, **kwargs):
    """ Add a new series to the chart datasets.
    The dataset structure of a chart is a list of dataset.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/elements.html

    :param index: The index of the dataset in the chart list of datasets
    :param data: The list of points (float)
    :param label: The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity level for the content
    :param kind: Optional. THe series type. Default to the chart type if not supplied
    """
    data = JsChartJs.DataSetBubble(self.page, attrs={"data": data})
    data.fill = False
    data.label = label
    data.set_style(background_color=self.options.background_colors[index],
                   fill_opacity=opacity or self.options.opacity,
                   border_width=1, border_color=colors or self.options.colors[index])
    for k, v in kwargs.items():
      if hasattr(data, k):
        setattr(data, k, v)
      else:
        data._attrs[k] = v
    return data

  def add_dataset(self, data, label, colors=None, opacity=None, **kwargs):
    """ Add a new Dataset to the chart list of Datasets.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    :param data: The list of points (float)
    :param label: The list of points (float)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity level for the content
    """
    data = self.new_dataset(len(self._datasets), data, label, colors, opacity=opacity, **kwargs)
    self._datasets.append(data)
    return data

  _js__builder__ = '''
      if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(dataset, i){
          if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
          if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
          if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
          result.datasets.push(dataset) })
      } else {
        var temp = {}; var labels = [];
        options.y_columns.forEach(function(series){temp[series] = []});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[options.x_axis] !== undefined){
              labels.push(rec[options.x_axis]); var r = 2; 
              if((options.rDim != undefined) && (rec[options.rDim] != undefined)){r = rec[options.rDim]};
              temp[name].push({y: rec[name], x: rec[options.x_axis], r: r})}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, type: options.type, data: [], backgroundColor: options.colors[i]};
          if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x, i){dataSet.data = temp[series]}); 
          if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
              dataSet = Object.assign(dataSet, options.datasets[series])}
        result.datasets.push(dataSet)});
        if (typeof options.labels !== "undefined"){ result.labels = options.labels} 
      }; return result'''


class ChartBar(ChartLine):
  _chart__type = 'bar'
  _option_cls = OptChartJs.OptionsBar

  @property
  def options(self):
    """ Property to the bar chart options.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html

    :rtype: OptChartJs.OptionsBar
    """
    return super().options

  def new_dataset(self, index, data, label, colors=None, opacity=None, kind=None, **kwargs):
    """ Add a new series to the chart datasets.
    The dataset structure of a chart is a list of dataset.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/elements.html

    :param index: The index of the dataset in the chart list of datasets
    :param data: The list of points (float)
    :param label: The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity level for the content
    :param kind: Optional. THe series type. Default to the chart type if not supplied
    """
    series_attrs = {"data": data, 'type': kind or self.options.type}
    if series_attrs['type'] == 'line':
      data = JsChartJs.DataSetScatterLine(self.page, attrs=series_attrs)
    else:
      data = JsChartJs.DataSetBar(self.page, attrs=series_attrs)
    data.label = label
    data.set_style(background_color=self.options.background_colors[index], fill_opacity=opacity or self.options.opacity,
                   border_width=1, border_color=colors or self.options.colors[index])
    for k, v in kwargs.items():
      if hasattr(data, k):
        setattr(data, k, v)
      else:
        data._attrs[k] = v
    return data

  def add_dataset(self, data, label: str, kind: str = None, colors: List[str] = None, opacity: float = None,
                  alias: str = None, **kwargs) -> JsChartJs.DataSetScatterLine:
    """ Add a new Dataset to the chart list of Datasets.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    :param data: The list of points (float)
    :param label: The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity level for the content
    :param kind: Optional. THe series type. Default to the chart type if not supplied
    :param alias: The chart alias name visible in the legend. Default the label
    """
    data = self.new_dataset(len(self._datasets), data, label, colors, opacity=opacity, kind=kind, **kwargs)
    self._datasets.append(data)
    alias = alias or label
    if alias not in self.options.y_columns:
      self.options.y_columns.append(alias)
      self.options.props[alias] = {"type": kind or self.options.type, 'fill': False}
    if kind == "line":
      data.fill = None
    return data


class ChartPolar(Chart):
  _chart__type = 'polarArea'
  _option_cls = OptChartJs.OptionsPolar

  @property
  def options(self) -> OptChartJs.OptionsPolar:
    """ Property to the Polar chart options.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/polar.html
    """
    return super().options

  def new_dataset(self, index: int, data, label: str, colors: List[str] = None,
                  kind: str = None, **kwargs) -> JsChartJs.DataSetPolar:
    """Add anew dataset.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    :param index: The index of the dataset in the chart list of datasets
    :param data: The list of points (float)
    :param label: The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param kind: Optional. The series type. Default to the chart type if not supplied
    """
    if kind is not None:
      data = JsChartJs.DataSetPolar(self.page, attrs={"data": data, 'type': kind})
    else:
      data = JsChartJs.DataSetPolar(self.page, attrs={"data": data})
    data.set_style(
      background_color=self.options.background_colors,
      fill_opacity=self.options.opacity, border_width=1,
      border_color=colors or self.options.colors)
    data.label = label
    for k, v in kwargs.items():
      if hasattr(data, k):
        setattr(data, k, v)
      else:
        data._attrs[k] = v
    return data

  def add_dataset(self, data, label: str, colors: List[str] = None, opacity: float = None,
                  kind: str = None, **kwargs) -> JsChartJs.DataSetPolar:
    """

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    :param data: The list of points (float)
    :param label: The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity factory from 0 to 1
    :param kind: Optional. The series type. Default to the chart type if not supplied
    """
    data = self.new_dataset(len(self._datasets), data, label, colors, **kwargs)
    self._datasets.append(data)
    return data

  _js__builder__ = '''
      if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(dataset, i){
          if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors};
          if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors};
          if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
          for(var attr in options.attrs){dataset[attr] = options.attrs[attr]};
          result.datasets.push(dataset)})
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_axis] in uniqLabels)){
                labels.push(rec[options.x_axis]); uniqLabels[rec[options.x_axis]] = true};
              temp[name][rec[options.x_axis]] = rec[name]}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, type: options.type, data: [], backgroundColor: options.background_colors, 
                     borderColor: options.colors, hoverBackgroundColor: options.colors};
          for(var attr in options.props){dataSet[attr] = options.props[attr]};
          if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x){
            if (temp[series][x] == undefined) {dataSet.data.push(null)} else{dataSet.data.push(temp[series][x])}
          }); 
          if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
              dataSet = Object.assign(dataSet, options.datasets[series])}
          result.datasets.push(dataSet)});
          if (typeof options.labels !== "undefined"){ result.labels = options.labels} 
      }; return result'''


class ChartHBar(ChartBar):
  _chart__type = 'horizontalBar'


class ChartPie(Chart):
  _chart__type = 'pie'
  _option_cls = OptChartJs.OptionsPie

  @property
  def options(self) -> OptChartJs.OptionsPie:
    """   Property to the Pie Chart options.

    Usage::

    """
    return super().options

  def new_dataset(self, index: int, data, label: str = "", colors: List[str] = None, opacity: float = None,
                  kind: str = None, **kwargs) -> JsChartJs.DataSetPie:
    """

    Usage::

    :param index:
    :param data: The list of points (float)
    :param label: Optional. The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity factory from 0 to 1
    :param kind: Optional. THe series type. Default to the chart type if not supplied
    """
    data = JsChartJs.DataSetPie(self.page, attrs={"data": data})
    if colors is None:
      data.set_style(
        background_colors=self.options.background_colors,
        fill_opacity=opacity or self.options.opacity, border_width=1,
        border_colors=self.options.colors)
    for k, v in kwargs.items():
      if hasattr(data, k):
        setattr(data, k, v)
      else:
        data._attrs[k] = v
    return data

  def add_dataset(self, data, label: str = "", colors: List[str] = None,
                  opacity: float = None, **kwargs) -> JsChartJs.DataSetPie:
    """

    Usage::

    :param data: The list of points (float)
    :param label: Optional. The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity factory from 0 to 1
    """
    data = self.new_dataset(len(self._datasets), data, label, colors=colors, opacity=opacity, **kwargs)
    self._datasets.append(data)
    return data

  _js__builder__ = '''
      if(data.python){
        result = {datasets: [], labels: data.labels};
        data.datasets.forEach(function(dataset, i){
          if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors};
          if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors};
          if(typeof dataset.hoverBackgroundColor === "undefined"){
            dataset.hoverBackgroundColor = options.background_colors};
          if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)};
          result.datasets.push(dataset)})
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_axis] in uniqLabels)){
                labels.push(rec[options.x_axis]); uniqLabels[rec[options.x_axis]] = true};
              temp[name][rec[options.x_axis]] = rec[name]}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series){
          dataSet = {label: series, data: [], backgroundColor: options.background_colors, type: options.type,
                     borderColor: options.colors, hoverBackgroundColor: options.colors};
          if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x, i){
            dataSet.backgroundColor.push(options.colors);
            if(temp[series][x] == undefined) {dataSet.data.push(null)} else{dataSet.data.push(temp[series][x])}
          }); 
          if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
              dataSet = Object.assign(dataSet, options.datasets[series])}
          result.datasets.push(dataSet)});
          if (typeof options.labels !== "undefined"){ result.labels = options.labels}
      }; return result'''


class ChartRadar(Chart):
  _chart__type = 'radar'
  _option_cls = OptChartJs.OptionsRadar

  def new_dataset(self, index: int, data, label: str, colors: List[str] = None, opacity: float = None,
                  kind: str = None, **kwargs) -> JsChartJs.DataSetRadar:
    """

    Usage::

    :param index:
    :param data: The list of points (float)
    :param label: Optional. The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity factory from 0 to 1
    :param kind: Optional. The series type. Default to the chart type if not supplied
    """
    data = JsChartJs.DataSetRadar(self.page, attrs={"data": data})
    data.label = label
    if colors is None:
      data.backgroundColor = self.options.colors[index]
      data.borderColor = self.options.colors[index]
      data.borderWidth = 0.2
      data.fillOpacity = opacity or self.options.props.get("opacity", 0)
    for k, v in kwargs.items():
      if hasattr(data, k):
        setattr(data, k, v)
      else:
        data._attrs[k] = v
    return data

  def add_dataset(self, data, label: str, colors: List[str] = None,
                  opacity: float = None, **kwargs) -> JsChartJs.DataSetRadar:
    """

    Usage::

    :param data: The list of points (float)
    :param label: Optional. The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity factory from 0 to 1
    """
    dataset = self.new_dataset(len(self._datasets), data, label, colors, opacity, **kwargs)
    self._datasets.append(dataset)
    return dataset

  _js__builder__ = '''
      if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(dataset, i){
          if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
          if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
          if(typeof dataset.borderWidth === "undefined"){dataset.borderWidth  = 1};
          if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
          result.datasets.push(dataset) })
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_axis] in uniqLabels)){
                labels.push(rec[options.x_axis]); uniqLabels[rec[options.x_axis]] = true}; 
              temp[name][rec[options.x_axis]] = rec[name]}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.background_colors[i], fill: true, type: options.type,
                     borderColor: options.colors[i]};
          for(var attr in options.props){dataSet[attr] = options.props[attr]};
          if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x){
            if (temp[series][x] == undefined) {dataSet.data.push(null)} else {dataSet.data.push(temp[series][x])}
          }); 
          if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
              dataSet = Object.assign(dataSet, options.datasets[series])}
          result.datasets.push(dataSet)}); if (typeof options.labels !== "undefined"){ result.labels = options.labels} 
      }; return result'''


class ChartScatter(Chart):
  _chart__type = 'scatter'

  def new_dataset(self, index: int, data, label: str, colors: List[str] = None,
                  kind: str = None, **kwargs) -> JsChartJs.DataSetScatterLine:
    """

    Usage::

    :param index:
    :param data: The list of points (float)
    :param label: Optional. The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param kind: Optional. THe series type. Default to the chart type if not supplied
    """
    data = JsChartJs.DataSetScatterLine(self.page, attrs={"data": data})
    data.fill = False
    data.label = label
    if colors is None:
      data.backgroundColor = self.options.colors[index]
      data.borderColor = self.options.colors[index]
    for k, v in kwargs.items():
      if hasattr(data, k):
        setattr(data, k, v)
      else:
        data._attrs[k] = v
    return data

  def add_dataset(self, data, label: str, colors: List[str] = None, **kwargs) -> JsChartJs.DataSetScatterLine:
    """

    Usage::

    :param data: The list of points (float)
    :param label: Optional. The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    """
    data = self.new_dataset(len(self._datasets), data, label, colors, **kwargs)
    self._datasets.append(data)
    return data

  _js__builder__ = '''
      if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(dataset, i){
          if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
          if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
          if(typeof dataset.hoverBackgroundColor === "undefined"){dataset.hoverBackgroundColor = options.colors[i]};
          if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
          result.datasets.push(dataset)})
      } else {
        var temp = {}; var labels = [];
        options.y_columns.forEach(function(series){temp[series] = []});
        data.forEach(function(rec){ 
          options.y_columns.forEach(function(name){
            if(rec[options.x_axis] !== undefined){
              labels.push(rec[options.x_axis]); var r = 2; 
              if((options.rDim != undefined) && (rec[options.rDim] != undefined)){r = rec[options.rDim]};
              temp[name].push({y: rec[name], x: rec[options.x_axis], r: r})}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.colors[i], type: options.type};
          if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x, i){dataSet.data = temp[series]});
        if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
              dataSet = Object.assign(dataSet, options.datasets[series])} 
        result.datasets.push(dataSet)}); if (typeof options.labels !== "undefined"){ result.labels = options.labels} 
    }; return result'''


class ChartTreeMap(Chart):
  requirements = ('chart.js', 'chartjs-chart-treemap')
  _chart__type = 'treemap'
  _option_cls = OptChartJs.OptionsTreeMap

  def add_dataset(self, tree: List[dict], label: str, colors: List[str] = None, **kwargs) -> JsChartJs.DataSetTreeMap:
    """ Add a dataset for the tree map.

    Usage::

    :param tree: The list of points (float)
    :param label: Optional. The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    """
    if "kind" not in kwargs:
      kwargs["kind"] = "data"
    data = self.new_dataset(len(self._datasets), tree, label, colors, **kwargs)
    self._datasets.append(data)
    return data

  def new_dataset(self, index: int, data, label: str, colors: List[str] = None, kind: str = None,
                  **kwargs) -> JsChartJs.DataSetTreeMap:
    """ Override an existing dataset.

    Usage::

    :param index: The series index
    :param data: The list of points (float)
    :param label: Optional. The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param kind: Optional. THe series type. Default to the chart type if not supplied
    """
    data = JsChartJs.DataSetTreeMap(self.page, attrs={kind: data})
    if kind == "tree":
      data.key = label
    else:
      data.label = label
    if colors is None:
      data.backgroundColor = self.options.colors[index]
      data.borderColor = self.options.colors[index]
    for k, v in kwargs.items():
      if hasattr(data, k):
        setattr(data, k, v)
      else:
        data._attrs[k] = v
    return data

  def backgrounds(self, colors: Dict[str, str]):
    """ Specific mapping rules for the background colors.

    :param colors: The color mapping based on the section label
    """
    self.options.commons["backgroundColorMaps"] = colors
    self.dataset().custom("backgroundColor", JsUtils.jsWrap('''function(ctx){var item = ctx.dataset.data[ctx.dataIndex];
if (item){
  var a = item.v / (item.gs || item.s) / 2 + 0.5;
  var colorsMaps = %s; if(colorsMaps[item.g]){return colorsMaps[item.g]}
  if(item.l === 0){return Chart.helpers.color("%s").alpha(a).rgbString()}
  if(item.l === 1){return Chart.helpers.color("white").alpha(0.3).rgbString()}
  else{return Chart.helpers.color("%s").alpha(a).rgbString()}}
}''' % (
      colors, self.options['commons']["colors"]["light"], self.options['commons']["colors"]["base"])
    ))

  _js__builder__ = '''
    if(data.python){
      result = {datasets: [], labels: data.labels};
      data.datasets.forEach(function(dataset, i){
        if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors};
        if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors};
        if(typeof dataset.hoverBackgroundColor === "undefined"){
          dataset.hoverBackgroundColor = options.background_colors};
        if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)};
        result.datasets.push(dataset)})
    } else {
      result = {datasets: [], labels: []};
      result.datasets.push({
        tree: data, key: options.y_columns[0], groups: options.groups, labels: {display: true}});
      result.datasets.forEach(function(dataset, i){
        if (options.commons.backgroundColorMaps){
          dataset.backgroundColor = function(ctx) {var item = ctx.dataset.data[ctx.dataIndex];
              if (item){
                var a = item.v / (item.gs || item.s) / 2 + 0.5;
                var colorsMaps = options.commons.backgroundColorMaps; if(colorsMaps[item.g]){return colorsMaps[item.g]}
                if(item.l === 0){return Chart.helpers.color(options.commons.colors.light).alpha(a).rgbString()}
                if(item.l === 1){return Chart.helpers.color("white").alpha(0.3).rgbString()}
                else{return Chart.helpers.color(options.commons.colors.base).alpha(a).rgbString()}}}
        } else {  
          dataset.backgroundColor = options.colors[i];
        }
      })
    }; return result'''


class ChartMatrix(Chart):
  requirements = ('chart.js', 'chartjs-chart-matrix')
  _chart__type = 'matrix'

  def new_dataset(self, index: int, data, label: str = "", colors: List[str] = None, opacity: float = None,
                  kind: str = None, **kwargs) -> JsChartJs.DataSetPie:
    """

    Usage::

    :param index:
    :param data: The list of points (float)
    :param label: Optional. The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity factory from 0 to 1
    :param kind: Optional. THe series type. Default to the chart type if not supplied
    """
    data = JsChartJs.DataSetPie(self.page, attrs={"data": data})
    if colors is None:
      data.set_style(
        background_colors=self.options.background_colors,
        fill_opacity=opacity or self.options.opacity, border_width=1,
        border_colors=self.options.colors)
    for k, v in kwargs.items():
      if hasattr(data, k):
        setattr(data, k, v)
      else:
        data._attrs[k] = v
    return data

  def add_dataset(self, data, label: str = "", colors: List[str] = None,
                  opacity: float = None, **kwargs) -> JsChartJs.DataSetPie:
    """

    Usage::

    :param data: The list of points (float)
    :param label: Optional. The series label (visible in the legend)
    :param colors: Optional. The color for this series. Default the global definition
    :param opacity: Optional. The opacity factory from 0 to 1
    """
    data = self.new_dataset(len(self._datasets), data, label, colors=colors, opacity=opacity, **kwargs)
    self._datasets.append(data)
    return data

  _js__builder__ = '''
        if(data.python){
          result = {datasets: [], labels: data.series};
          data.datasets.forEach(function(dataset, i){
            if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
            if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
            if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
            result.datasets.push(dataset) })
        } else {
          var temp = {}; var labels = [];
          options.y_columns.forEach(function(series){temp[series] = []});
          data.forEach(function(rec){ 
            options.y_columns.forEach(function(name){
              if(rec[options.x_axis] !== undefined){
                labels.push(rec[options.x_axis]);
                temp[name].push({y: rec[name], x: rec[options.x_axis]})}})});
          result = {datasets: [], labels: labels};
          options.y_columns.forEach(function(series, i){
            dataSet = {label: series, type: options.type, data: [], backgroundColor: options.colors[i]};
            if(typeof options.commons !== 'undefined'){
              for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
            labels.forEach(function(x, i){dataSet.data = temp[series]}); 
            if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
                dataSet = Object.assign(dataSet, options.datasets[series])}
          result.datasets.push(dataSet)});
          if (typeof options.labels !== "undefined"){ result.labels = options.labels} 
        }; console.log(result); return result'''


class ChartSankey(Chart):
  requirements = ('chart.js', 'chartjs-chart-sankey')
  _chart__type = 'sankey'


class ChartWordCloud(ChartPolar):
  requirements = ('chart.js', 'chartjs-chart-wordcloud')
  _chart__type = 'wordCloud'


class ChartVenn(Chart):
  requirements = ('chart.js', 'chartjs-chart-venn')
  _chart__type = 'venn'


class ChartHyr(Chart):
  requirements = ('chart.js', 'chartjs-plugin-hierarchical')
  _chart__type = 'bar'

  _js__builder__ = '''return data'''


class ChartExts(ChartPie):

  def __init__(self, page, width, height, html_code, options, profile):
    super(ChartExts, self).__init__(page, width, height, html_code, options, profile)
    self.jsImports.add(options['npm'])
    self.options.type = options['type']

