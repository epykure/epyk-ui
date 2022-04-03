#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives
from epyk.core.css import Colors
from epyk.core.html import Html
from epyk.core.html.options import OptChartJs

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlCharts
from epyk.core.js.packages import packageImport
from epyk.core.js.primitives import JsObject

from epyk.core.js.packages import JsChartJs


class ChartJsActivePoints:

  def __init__(self, chart_id, i, page: primitives.PageModel):
    self.chartId = chart_id
    self.page = page
    self.num = i or self.index

  @property
  def index(self):
    """
    Description:
    -----------
    Get the index of the clicked series in teh datasets.

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
    """
    Description:
    -----------
    Get the name of the selected series.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().x])
    """
    return JsObject.JsObject.get("%s.data.datasets[%s].label" % (self.chartId, self.num))

  @property
  def labels(self):
    """
    Description:
    -----------
    Get the series label name.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().labels])
    """
    return JsObject.JsObject.get("%s.data.labels[activePoints[Math.min(%s, activePoints.length - 1)]]" % (
      self.chartId, self.num))

  @property
  def model(self):
    """
    Description:
    -----------
    Get the series value.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().model])
    """
    return JsObject.JsObject.get("activePoints[Math.min(%s, activePoints.length - 1)]['_model']" % self.num)

  @property
  def datasetLabel(self):
    """
    Description:
    -----------
    Get the series name.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().datasetLabel])
    """
    return JsObject.JsObject.get(
      "activePoints[Math.min(%s, activePoints.length - 1)]['_model'].datasetLabel" % self.num)

  @property
  def label(self):
    """
    Description:
    -----------

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
    """
    Description:
    -----------
    Get the series dataset.

    Usage::

    """
    return JsObject.JsObject.get("activePoints[Math.min(%s, activePoints.length - 1)]['_model'].label" % self.num)

  @property
  def value(self):
    """
    Description:
    -----------
    Get the point value.

    Usage::

      line = page.ui.charts.chartJs.line()
      line.click([line.activePoints().value])
    """
    return JsObject.JsObject.get("%s.data.datasets[activePoints[Math.min(%s, activePoints.length - 1)]._datasetIndex].data[activePoints[Math.min(%s, activePoints.length - 1)]._index]" % (self.chartId, self.num, self.num))


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

  def activePoints(self, i: int = None):
    """
    Description:
    -----------
    The current active points selected by an event on a chart.

    Usage::

        activePoints

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    Attributes:
    ----------
    :param i: Integer. Optional. The series index. Default it is the series clicked.
    """
    return ChartJsActivePoints(self.chartId, i, self.page)

  @property
  def shared(self):
    """
    Description:
    -----------
    All the common properties shared between all the charts.
    This will ensure a compatibility with the plot method.

    Usage::

      line = page.ui.charts.chartJs.bar()
      line.shared.x_label("x axis")
    """
    return OptChartJs.OptionsChartSharedChartJs(component=self)

  @property
  def js(self) -> JsChartJs.ChartJs:
    """
    Description:
    -----------
    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    Usage::

      line = page.ui.charts.chartJs.bar()
      page.ui.button("Load").click([line.js.add(6, {"test 2": 34})])

    :return: A Javascript object.

    :rtype: JsChartJs.ChartJs
    """
    if self._js is None:
      self._js = JsChartJs.ChartJs(selector="window['%s']" % self.chartId, component=self, page=self.page)
    return self._js

  @property
  def dom(self) -> JsHtmlCharts.ChartJs:
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage::

    :return: A Javascript Dom object.

    :rtype: JsHtmlCharts.ChartJs
    """
    if self._dom is None:
      self._dom = JsHtmlCharts.ChartJs(page=self.page, component=self)
    return self._dom

  @property
  def options(self) -> OptChartJs.ChartJsOptions:
    """
    Description:
    -----------
    Property to the series options.

    Usage::

    :rtype: OptChartJs.ChartJsOptions
    """
    return super().options

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
    A plugin for Chart.js >= 2.4.0.

    Makes data points draggable. Supports touch events.

    Usage::

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

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/axes/labelling.html

    Attributes:
    ----------
    :param labels: List. An array of labels.
    """
    self._data_attrs['labels'] = labels
    return self

  def label(self, i: int, name: str):
    """
    Description:
    -----------
    Change the series name.

    Usage::

    Attributes:
    ----------
    :param i: Integer. The series index according to the y_columns.
    :param name: String. The new name to be set.
    """
    self.dataset(i).label = name
    return self

  def dataset(self, i: int = None) -> JsChartJs.DataSetPie:
    """
    Description:
    -----------
    The data property of a ChartJs chart.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/master/general/data-structures

    Attributes:
    ----------
    :param i: Integer. Optional. The series index according to the y_columns.

    :rtype: JsChartJs.DataSetPie
    """
    if i is None:
      return self._datasets[-1]

    return self._datasets[i]

  def colors(self, hex_values):
    """
    Description:
    -----------
    Set the colors of the chart.

    hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
    If the background colors are not specified they will be deduced from the colors list changing the opacity.

    Usage::

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
    for i, rec in enumerate(self._datasets):
      if self._chart__type in ["pie", "polarArea"]:
        rec.backgroundColor = self.options.background_colors
        rec.borderColor = self.options.colors
      else:
        rec.backgroundColor = self.options.background_colors[i]
        rec.borderColor = self.options.colors[i]
      rec.borderWidth = 1

  def click(self, js_funcs, profile=False, source_event=None, on_ready=False):
    """
    Description:
    -----------
    Add a click event on the chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/general/interactions/events.html

    Attributes:
    ----------
    :param js_funcs: List. Set of Javascript function to trigger on this event.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The JavaScript DOM source for the event (can be a sug item).
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if min(self.page.imports.pkgs.chart_js.version) > '3.0.0':
      tmp_js_funcs = [
        "var activePoints = %s.getElementsAtEventForMode(event, 'nearest', { intersect: true }, true)" % self.chartId,
        "if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(js_funcs, toStr=True)]
    else:
      tmp_js_funcs = [
        "var activePoints = %s.getElementsAtEvent(event)" % self.chartId,
        "if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(js_funcs, toStr=True)]
    return super(Chart, self).click(tmp_js_funcs, profile)

  def dblclick(self, js_funcs, profile=False, source_event=None, on_ready=False):
    """
    Description:
    -----------
    Add a double click event on the chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/general/interactions/events.html

    Attributes:
    ----------
    :param js_funcs: List. Set of Javascript function to trigger on this event.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The JavaScript DOM source for the event (can be a sug item).
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
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

  def hover(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    -----------
    Add an on mouse hover event on the chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/general/interactions/events.html

    Attributes:
    ----------
    :param js_funcs: List. Set of Javascript function to trigger on this event.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The JavaScript DOM source for the event (can be a sug item).
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
    """
    Description:
    -----------

    """
    return self._datasets

  def getCtx(self, options=None):
    """
    Description:
    -----------
    Get the ChartJs context. The internal configuration of the chart.
    The context is a dictionary object with javascript fragments.

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/

    Attributes:
    ----------
    :param options: Dictionary. Optional. The chart options.
    """
    obj_datasets = "[%s]" % ", ".join([d.toStr() for d in self._datasets])
    self._data_attrs['datasets'] = JsObject.JsObject.get(obj_datasets)
    obj_data = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._data_attrs.items()])
    self._attrs["data"] = JsObject.JsObject.get(obj_data)
    self._attrs["options"] = self.options.config_js(options)
    str_ctx = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items()])
    return str_ctx

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    Description:
    ------------
    Update the chart with context and / or data changes.

    Attributes:
    ----------
    :param data: List. Optional. The full datasets object expected by ChartJs.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id: String. Not used.
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
        "options": self.options.config_js(options)}
    return '%(chartId)s = new Chart(%(component)s.getContext("2d"), %(ctx)s)' % {
      "chartId": self.chartId, "component": component_id or self.dom.varId, "ctx": self.getCtx(options)}

  def loading(self, status=True):
    """
    Description:
    ------------
    Loading component on a chart.

    Usage::

        chart_obj.loading()
        ....
        chart_obj.loading(False)

    Attributes:
    ----------
    :param status: Boolean. Optional. Specific the status of the display of the loading component.
    """
    if status:
      return ''' 
        if (typeof window['popup_loading_%(htmlId)s'] === 'undefined'){
          var divLoading = document.createElement("div"); window['popup_loading_%(htmlId)s'] = divLoading; 
          divLoading.style.width = '100%%'; divLoading.style.height = '100%%'; 
          divLoading.style.background = '%(background)s';
          divLoading.style.position = 'absolute'; divLoading.style.top = 0; divLoading.style.left = 0; 
          divLoading.style.zIndex = 200;
          divLoading.style.color = '%(color)s'; divLoading.style.textAlign = 'center'; 
          divLoading.style.paddingTop = '50vh';
          divLoading.innerHTML = "<div style='font-size:50px'><i class='fas fa-spinner fa-spin' style='margin-right:10px'></i>Loading...</div>";
          document.getElementById('%(htmlId)s').parentNode.appendChild(divLoading)
        }''' % {
        "htmlId": self.htmlCode, 'color': self.page.theme.success[1], 'background': self.page.theme.greys[0]}

    return '''
      if (typeof window['popup_loading_%(htmlId)s'] !== 'undefined'){
        document.getElementById('%(htmlId)s').parentNode.removeChild(window['popup_loading_%(htmlId)s']); 
        window['popup_loading_%(htmlId)s'] = undefined}''' % {"htmlId": self.htmlCode}

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
    Description:
    ------------

    Usage::

    """
    return self.dom.appendChild(JsObject.JsObject.get('''(function(htmlObj){
      var comp = document.createElement('canvas'); comp.id = htmlObj.id + "_" + htmlObj.getAttribute("data-next"); 
      htmlObj.setAttribute("data-counter", parseInt(htmlObj.getAttribute("data-counter")) + 1);
      htmlObj.setAttribute("data-current", htmlObj.getAttribute("data-next"));
      htmlObj.setAttribute("data-next", parseInt(htmlObj.getAttribute("data-next")) + 1);
      return comp})(%(htmlId)s)''' % {"htmlId": self.dom.varId}))

  def build(self, data=None, options=None, profile=False, component_id=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param data:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id:
    """
    return '''%(chartId)s = new Chart(%(dom)s.getContext('2d'), {type: 'bar'}); 
      Object.assign(%(chartId)s.data, %(data)s); %(chartId)s.update()''' % {
      "chartId": self.chart.chartId, "dom": component_id or self.chart.chartId,
      "data": self.chart.build(data, options, profile)}

  def create(self, data=None, options=None, attrs=None, profile=False):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param data:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
    """
    Description:
    ------------
    Add a series to an existing dataset.

    Usage::

    Attributes:
    ----------
    :param data: List. A list of numbers.
    """
    self.__data.append(data)
    return self


class ChartLine(Chart):
  _chart__type = 'line'
  _option_cls = OptChartJs.OptionsLine

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the specific ChartJs Line chart.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html

    :rtype: OptChartJs.OptionsLine
    """
    return super().options

  def new_dataset(self, index, data, label, colors=None, opacity=None, kind=None, **kwargs):
    """
    Description:
    ------------
    Add a new series to the chart datasets.
    The dataset structure of a chart is a list of dataset.

    For a chart line the default Opacity is None which will set the fill to attribute to False.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/elements.html

    Attributes:
    ----------
    :param index: Integer. The index of the dataset in the chart list of datasets.
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
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

  def add_dataset(self, data, label="", colors=None, opacity=None, kind=None, **kwargs):
    """
    Description:
    ------------
    Add a new Dataset to the chart list of Datasets.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: List. Optional. The list of points (float).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    :param kind: String. Optional. The chart type.
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
          result.datasets.push(dataSet)})
      }; return result'''


class ChartBubble(Chart):
  _chart__type = 'bubble'

  def new_dataset(self, index, data, label, colors=None, opacity=None, kind=None, **kwargs):
    """
    Description:
    ------------
    Add a new series to the chart datasets.
    The dataset structure of a chart is a list of dataset.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/elements.html

    Attributes:
    ----------
    :param index: Integer. The index of the dataset in the chart list of datasets.
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
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
    """
    Description:
    ------------
    Add a new Dataset to the chart list of Datasets.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: List. The list of points (float).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
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
        result.datasets.push(dataSet)})
      }; return result'''


class ChartBar(ChartLine):
  _chart__type = 'bar'
  _option_cls = OptChartJs.OptionsBar

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the bar chart options.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html

    :rtype: OptChartJs.OptionsBar
    """
    return super().options

  def new_dataset(self, index, data, label, colors=None, opacity=None, kind=None, **kwargs):
    """
    Description:
    ------------
    Add a new series to the chart datasets.
    The dataset structure of a chart is a list of dataset.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/elements.html

    Attributes:
    ----------
    :param index: Integer. The index of the dataset in the chart list of datasets.
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
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

  def add_dataset(self, data, label, kind=None, colors=None, opacity=None, alias=None, **kwargs):
    """
    Description:
    ------------
    Add a new Dataset to the chart list of Datasets.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
    :param alias: String. The chart alias name visible in the legend. Default the label.
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
  def options(self):
    """
    Description:
    ------------
    Property to the Polar chart options.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/polar.html

    :rtype: OptChartJs.OptionsPolar
    """
    return super().options

  def new_dataset(self, index, data, label, colors=None, kind=None, **kwargs):
    """
    Description:
    -----------

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param index: Integer. The index of the dataset in the chart list of datasets.
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
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

  def add_dataset(self, data, label, colors=None, opacity=None, kind=None, **kwargs):
    """
    Description:
    -----------

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Number. Optional. The opacity factory from 0 to 1.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
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
          }); result.datasets.push(dataSet)})
      }; return result'''


class ChartHBar(ChartBar):
  _chart__type = 'horizontalBar'


class ChartPie(Chart):
  _chart__type = 'pie'
  _option_cls = OptChartJs.OptionsPie

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the Pie Chart options.

    Usage::

    :rtype: OptChartJs.OptionsPie
    """
    return super().options

  def new_dataset(self, index, data, label="", colors=None, opacity=None, kind=None, **kwargs):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param index: Integer.
    :param data: List. The list of points (float).
    :param label: String. Optional. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Number. Optional. The opacity factory from 0 to 1.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
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

  def add_dataset(self, data, label="", colors=None, opacity=None, **kwargs):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: String. Optional. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Number. Optional. The opacity factory from 0 to 1.
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
          }); result.datasets.push(dataSet)})}
      return result'''


class ChartRadar(Chart):
  _chart__type = 'radar'

  def new_dataset(self, index, data, label, colors=None, opacity=None, kind=None, **kwargs):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param index: Integer.
    :param data: List. The list of points (float).
    :param label: String. Optional. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Number. Optional. The opacity factory from 0 to 1.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
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

  def add_dataset(self, data, label, colors=None, opacity=None, **kwargs):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: String. Optional. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Number. Optional. The opacity factory from 0 to 1.
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
          }); result.datasets.push(dataSet)})}
      return result'''


class ChartScatter(Chart):
  _chart__type = 'scatter'

  def new_dataset(self, index, data, label, colors=None, kind=None, **kwargs):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param index: Integer.
    :param data: List. The list of points (float).
    :param label: String. Optional. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
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

  def add_dataset(self, data, label, colors=None, **kwargs):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: String. Optional. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
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
        result.datasets.push(dataSet)})}
    return result'''


class ChartTreeMap(Chart):
  requirements = ('chart.js', 'chartjs-chart-treemap')
  _chart__type = 'treemap'
  _option_cls = OptChartJs.OptionsTreeMap

  def add_dataset(self, tree, label, colors=None, **kwargs):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param tree: List. The list of points (float).
    :param label: String. Optional. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    """
    data = self.new_dataset(len(self._datasets), tree, label, colors, **kwargs)
    self._datasets.append(data)
    return data

  def new_dataset(self, index, data, label, colors=None, kind=None, **kwargs):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param index: Integer.
    :param data: List. The list of points (float).
    :param label: String. Optional. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
    """
    data = JsChartJs.DataSetTreeMap(self.page, attrs={"data": data})
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


class ChartExts(ChartPie):

  def __init__(self, page, width, height, html_code, options, profile):
    super(ChartExts, self).__init__(page, width, height, html_code, options, profile)
    self.jsImports.add(options['npm'])
    self.options.type = options['type']

