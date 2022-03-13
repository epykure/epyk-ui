#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional, List
from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import DataAttrs
from epyk.core.js.packages import JsPackage

from epyk.core.css import Colors


EASING_OPTIONS = ['linear', 'easeInQuad', 'easeOutQuad', 'easeInOutQuad', 'easeInCubic', 'easeOutCubic',
                  'easeInOutCubic', 'easeInQuart', 'easeOutQuart', 'easeInOutQuart', 'easeInQuint', 'easeOutQuint',
                  'easeInOutQuint', 'easeInSine', 'easeOutSine', 'easeInOutSine', 'easeInExpo', 'easeOutExpo',
                  'easeInOutExpo', 'easeInCirc', 'easeOutCirc', 'easeInOutCirc', 'easeInElastic', 'easeOutElastic',
                  'easeInOutElastic', 'easeInBack', 'easeOutBack', 'easeInOutBack', 'easeInBounce', 'easeOutBounce',
                  'easeInOutBounce']


class Config(DataAttrs):

  @property
  def duration(self):
    """
    Description:
    ------------
    Time for the animation of the redraw in milliseconds.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html
    """
    return self._attrs["duration"]

  @duration.setter
  def duration(self, time):
    self._attrs["duration"] = time

  @property
  def lazy(self):
    """
    Description:
    ------------
    If true, the animation can be interrupted by other animations.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html
    """
    return self._attrs["lazy"]

  @lazy.setter
  def lazy(self, flag):
    self._attrs["lazy"] = flag

  @property
  def easing(self):
    """
    Description:
    ------------
    Set the easing option.

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/animations.html
    """
    return self._attrs["easing"]

  @easing.setter
  def easing(self, value):
    if value not in EASING_OPTIONS:
      raise ValueError("%s is not allowed" % value)

    self._attrs["easing"] = value


class ChartJs(JsPackage):
  lib_alias = {'js': 'chart.js'}

  def __init__(self, html_code: str = None, config=None, component: primitives.HtmlModel = None, js_code: str = None,
               selector: str = None, set_var: bool = False, page: primitives.PageModel = None):
    self.component = component
    if component is None:
      self.page = page
    else:
      self.page = component.page
    if selector is None:
      self._selector = 'new Chart(%s.getContext("2d"), %s)' % (html_code, config.toStr())
    else:
      self._selector = selector
    self.varName, self.setVar = js_code or self._selector, set_var
    self.component.jsImports.add(self.lib_alias['js'])
    self._js = []

  def getElementsAtEvent(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
    """
    Description:
    -----------
    Calling getElementsAtEvent(event) on your Chart instance passing an argument of an event,
    or jQuery event, will return the point elements that are at that the same position of that event.

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if self.page.imports.pkgs.chart_js.version:
      return self.getElementsAtEventForMode(js_funcs, profile=profile)
    else:
      if not isinstance(js_funcs, list):
        js_funcs = [js_funcs]
      return JsObjects.JsArray.JsArray("%s.getElementsAtEvent(%s)" % (
        self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)), is_py_data=False)

  @JsUtils.fromVersion({'chart.js': '3.0.0'})
  def getElementsAtEventForMode(self, js_funcs: Union[list, str], mode: str = "nearest", options: dict = None,
                                use_final_position: bool = True, profile: Optional[Union[dict, bool]] = False):
    """
    Description:
    -----------
    Calling getElementsAtEventForMode(e, mode, options, useFinalPosition) on your Chart instance passing an event and a
    mode will return the elements that are found. The options and useFinalPosition arguments are passed through to the
    handlers.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param str mode:
    :param dict options:
    :param bool use_final_position:
    :param Optional[Union[dict, bool]] profile:
    """
    mode = JsUtils.jsConvertData(mode, None)
    options = options or {"intersect": True}
    options = JsUtils.jsConvertData(options, None)
    use_final_position = JsUtils.jsConvertData(use_final_position, None)
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return JsObjects.JsArray.JsArray("%s.getElementsAtEventForMode(%s, %s, %s, %s)" % (
      self.varName, JsUtils.jsConvertFncs(
        js_funcs, toStr=True, profile=profile), mode, options, use_final_position), is_py_data=False)

  def add(self, point: Union[str, primitives.JsDataModel], values: Union[dict, primitives.JsDataModel]):
    """
    Description:
    -----------
    Add point to an exiting chart on existing series.

    Note: Do not forget to trigger an update on the chart once all your transformations are done.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param point: Object. The point to add on the x-axis.
    :param values: Dictionary. The value per series name.
    """
    point = JsUtils.jsConvertData(point, None)
    values = JsUtils.jsConvertData(values, None)
    return JsObjects.JsVoid('''
      var index = %(varName)s.data.labels.indexOf(%(point)s);
      if(index >= 0){
        %(varName)s.data.datasets.forEach(function(dataset){
          if(%(values)s[dataset.label] !== undefined){dataset.data[index] = %(values)s[dataset.label] }})
      } else {
        %(varName)s.data.labels.push(%(point)s);
        %(varName)s.data.datasets.forEach(function(dataset){
          dataset.data.push(%(values)s[dataset.label])})}''' % {
      'varName': self.varName, 'point': point, 'values': values})

  def remove(self, point=None, series_names: Union[list, primitives.JsDataModel] = None):
    """
    Description:
    -----------
    Remove point to existing series.

    Note: Do not forget to trigger an update on the chart once all your transformations are done.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param point: Object. Optional. The point to be removed on the series. If none the last one will be removed.
    :param series_names: List. Optional. The series name.
    """
    point = JsUtils.jsConvertData(point, None)
    if series_names is None:
      if point is None:
        return JsObjects.JsVoid('''
          %(varName)s.data.labels.pop();
          %(varName)s.data.datasets.forEach(function(dataset){ dataset.data.pop() })''' % {'varName': self.varName})

      return JsObjects.JsVoid('''
        var index = %(varName)s.data.labels.indexOf(%(point)s);
        if(index >= 0){
          %(varName)s.data.labels.splice(index, 1);
          %(varName)s.data.datasets.forEach(function(dataset){ dataset.data.splice(index, 1) })
        } ''' % {'varName': self.varName, 'point': point})

    series_names = JsUtils.jsConvertData(series_names, None)
    return JsObjects.JsVoid('''
        var index = %(varName)s.data.labels.indexOf(%(point)s);
        if(index >= 0){
          %(varName)s.data.datasets.forEach(function(dataset){
            if (%(seriesNames)s.includes(dataset.label)){
              dataset.data[index] = null}})} ''' % {
      'varName': self.varName, 'point': point, 'seriesNames': series_names})

  def empty(self):
    """
    Description:
    -----------
    Empty a chartJs component. Namely it will set empty lists for the dataSets and the labels.
    This will also update the chart to trigger the animation.
    """
    return JsObjects.JsVoid(
      "%(varName)s.data.datasets = []; %(varName)s.data.labels = []; %(varName)s.update()" % {"varName": self.varName})

  def data(self, datasets: dict, options: dict = None, profile=None):
    """
    Description:
    -----------
    Update all the data in the chart.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param dict datasets: The full datasets object expected by ChartJs.
    :param dict options: Optional. Specific Python options available for this component.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return self.component.build(
      JsUtils.jsWrap("Object.assign(%s, {python: true})" % JsUtils.jsConvertData(datasets, None)), options, profile)

  def load(self, name: str, points: Union[List[dict], primitives.JsDataModel], options: dict = None, color: str = ""):
    """
    Description:
    -----------
    Loads new series on an existing chart.
    existing x axis will not be changed and they will be used to add the points.

    Note: Do not forget to trigger an update on the chart once all your transformations are done.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param name: String. The series name.
    :param List[dict] points: The list of points ({x: , y: }) to be added to the chart.
    :param dict options: Optional. Specific Python options available for this series.
    :param str color: Optional. The color code for the chart.
    """
    name = JsUtils.jsConvertData(name, None)
    points = JsUtils.jsConvertData(points, None)
    current_options = dict(self.component.options.commons)
    current_options.update(options or {})
    options = self.component.options.config_js({"commons": current_options})
    return JsObjects.JsVoid('''
      var values = []; var index= -1; var %(htmlCode)s_options = %(options)s;
      %(varName)s.data.datasets.forEach(function(d, i){if(d.label == %(name)s){index = i}});
      if (index == -1){
        %(varName)s.data.labels.forEach(function(v){values.push(%(points)s)});
        if(!'%(color)s'){
          var nextIndex = %(varName)s.data.datasets.length;
          %(htmlCode)s_options.commons.backgroundColor = %(htmlCode)s_options.background_colors[nextIndex];
          %(htmlCode)s_options.commons.borderColor = %(htmlCode)s_options.colors[nextIndex];
          %(htmlCode)s_options.commons.hoverBackgroundColor = %(htmlCode)s_options.background_colors[nextIndex]};
        if (%(htmlCode)s_options.commons.type == "line"){%(htmlCode)s_options.commons.fill = null};
        if(['polarArea', 'pie', 'radar', 'doughnut'].indexOf(%(varName)s.config._config.type) > 0){%(varName)s.data.labels.push(%(name)s); %(varName)s.data.datasets[0].data.push(%(points)s)}
        else{%(varName)s.data.datasets.push(Object.assign({label: %(name)s, data: %(points)s}, %(htmlCode)s_options.commons))}
      }''' % {'varName': self.varName, 'name': name, 'points': points, "options": options.toStr(),
              "htmlCode": self.component.htmlCode, "color": color})

  def unload(self, names: list = None):
    """
    Description:
    -----------
    Remove series from the chart.

    Note: Do not forget to trigger an update on the chart once all your transformations are done.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param list names: Optional. The series names to be removed from the chart. If none all series will be removed.
    """
    if names is None:
      return JsObjects.JsVoid(
        '%(varName)s.data.labels = []; %(varName)s.data.datasets = []' % {'varName': self.varName})

    names = JsUtils.jsConvertData(names, None)
    return JsObjects.JsVoid('''
      var indices = [];
      %(varName)s.data.datasets.forEach(function(d, i){ if(%(names)s.includes(d.label)){ indices.push(i)}});
      indices.sort().reverse().forEach(function(i){%(varName)s.data.datasets.splice(i, 1)})
      ''' % {'varName': self.varName, 'names': names})

  @property
  def label(self):
    """
    Description:
    -----------
    Return the series label.
    """
    return JsObjects.JsString.JsString("%s.data.labels[activePoints[0]['_index']]" % self.varName, is_py_data=False)

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObject.JsObject(
      "%s.data.datasets[0].data[activePoints[0]['_index']]" % self.varName, is_py_data=False)

  @property
  def value(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsString.JsString("{%(htmlCode)s: {point: %(chart)s.data.datasets[0].data[activePoints[0]['_index']], label: %(chart)s.data.labels[activePoints[0]['_index']]}}" % {
      'htmlCode': self.component.htmlCode, "chart": self.varName}, is_py_data=False)

  def update(self, config: Union[dict, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Triggers an update of the chart. This can be safely called after updating the data object.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    Attributes:
    ----------
    :param Union[dict, primitives.JsDataModel] config: Optional. A config object can be provided with additional
    configuration for the process.
    """
    if config is None:
      return JsObjects.JsObject.JsObject("%s.update()" % self.toStr())

    config = JsUtils.jsConvertData(config, None)
    return JsObjects.JsObject.JsObject("%s.update(%s)" % (self.toStr(), config))

  def reset(self):
    """
    Description:
    ------------
    Reset the chart to it's state before the initial animation.
    A new animation can then be triggered using update.

    Usage::

      myLineChart.reset()

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html
    """
    return JsObjects.JsObject.JsObject("%s.reset()" % self.toStr())

  def stop(self):
    """
    Description:
    ------------
    Use this to stop any current animation loop. This will pause the chart during any current animation frame.

    Usage::

      chart.stop()

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    :return: 'this' for chainability
    """
    self._js.append("stop()")
    return self

  def resize(self):
    """
    Description:
    ------------
    Use this to manually resize the canvas element.

    This is run each time the canvas container is resized, but you can call this method manually if you change the size
    of the canvas nodes container element.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    :return: 'this' for chainability
    """
    self._js.append("%s.resize()" % self.toStr())
    return self

  def clear(self):
    """
    Description:
    ------------
    Will clear the chart canvas. Used extensively internally between animation frames, but you might find it useful.

    Usage::

      chart.clear()

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    :return: 'this' for chainability
    """
    return JsObjects.JsVoid("%s.clear()" % self.toStr())

  def toBase64Image(self):
    """
    Description:
    ------------
    This returns a base 64 encoded string of the chart in it's current state.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    :return: png data url of the image on the canvas
    """
    return JsObjects.JsObject.JsObject("%s.toBase64Image()" % self.toStr())

  def generateLegend(self):
    """
    Description:
    ------------
    Returns an HTML string of a legend for that chart. The legend is generated from the legendCallback in the options.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    :return: HTML string of a legend for this chart
    """
    return JsObjects.JsObject.JsObject("%s.generateLegend()" % self.toStr())

  def getElementAtEvent(self, event: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Calling getElementAtEvent(event) on your Chart instance passing an argument of an event, or jQuery event,
    will return the single element at the event position

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] event: The javascript event.

    :return: the first element at the event point.
    """
    event = JsUtils.jsConvertData(event, None)
    return JsObjects.JsObject.JsObject("%s.getElementAtEvent(%s)" % (self.toStr(), event))

  def getDatasetAtEvent(self, event: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Looks for the element under the event point, then returns all elements from that dataset.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] event: The javascript event.

    :return: an array of elements
    """
    event = JsUtils.jsConvertData(event, None)
    return JsObjects.JsArray.JsArray("%s.getDatasetAtEvent(%s)" % (self.toStr(), event))

  def getDatasetMeta(self, index: int):
    """
    Description:
    ------------
    Looks for the dataset that matches the current index and returns that metadata.

    Usage::

      chart.getDatasetMeta(0)

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    Attributes:
    ----------
    :param int index: The index value of the series.
    """
    return JsObjects.JsObject.JsObject("%s.getDatasetMeta(%s)" % (self.toStr(), index))

  def render(self, config: Union[dict, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Triggers a redraw of all chart elements. Note, this does not update elements for new data.
    Use .update() in that case.

    Usage::

      chart.render({duration: 800, lazy: false, easing: 'easeOutBounce'})

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html

    Attributes:
    ----------
    :param Union[dict, primitives.JsDataModel] config: Optional. A python dictionary as config object.
    """
    if config is None:
      return JsObjects.JsObject.JsObject("%s.render()" % self.toStr())

    config = JsUtils.jsConvertData(config, None)
    return JsObjects.JsObject.JsObject("%s.render(%s)" % (self.toStr(), config))

  def destroy(self):
    """
    Description:
    ------------
    Use this to destroy any chart instances that are created.

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/api.html
    """
    return JsObjects.JsObject.JsObject("%s.destroy()" % self.toStr())

  def download(self, format, filename, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param format: String. The file format.
    :param filename: String. The file name.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    return self.toBase64Image()

  def clearData(self):
    """
    Description:
    ------------

    """
    return self.clear()

  def toStr(self):
    """
    Description:
    ------------
    Javascript representation.

    :return: Return the Javascript String.
    """
    if self._selector is None:
      raise ValueError("Selector not defined, use this() or new() first")

    if self.setVar:
      if len(self._js) > 0:
        str_data = ".".join(self._js)
        str_data = "var %s = %s.%s" % (self.varName, self._selector, str_data)
      else:
        str_data = "var %s = %s" % (self.varName, self._selector)
      self.setVar = False
    else:
      if len(self._js) > 0:
        str_data = ".".join(self._js)
        str_data = "%s.%s" % (self.varName, str_data)
      else:
        str_data = self.varName
    self._js = []
    return str_data


class ChartJsOptTicks(DataAttrs):

  def beginAtZero(self, flag: Union[bool, primitives.JsDataModel]):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: A flag to activate the start to zero of the series.
    """
    self._attrs["beginAtZero"] = JsUtils.jsConvertData(flag, None)
    return self

  def display(self, flag: Union[bool, primitives.JsDataModel]):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: Show the series.
    """
    self._attrs["display"] = JsUtils.jsConvertData(flag, None)
    return self


class ChartJsOptGridLines(DataAttrs):

  def display(self, flag: Union[bool, primitives.JsDataModel] = False):
    """
    Description:
    ------------
    If false, do not display grid lines for this axis.

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: Optional.
    """
    self._attrs["display"] = JsUtils.jsConvertData(flag, None)
    return self

  def circular(self, flag: Union[bool, primitives.JsDataModel] = False):
    """
    Description:
    ------------
    If true, gridlines are circular (on radar chart only).

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: Optional.
    """
    self._attrs["circular"] = JsUtils.jsConvertData(flag, None)
    return self

  def color(self, colors: Union[str, primitives.JsDataModel] = ""):
    """
    Description:
    ------------
    The color of the grid lines.
    If specified as an array, the first color applies to the first grid line,
    the second to the second grid line and so on.

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] colors: Optional. The color code.
    """
    self._attrs["color"] = JsUtils.jsConvertData(colors, None)
    return self

  def borderDash(self, narray: Union[list, primitives.JsDataModel]):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[list, primitives.JsDataModel] narray:
    """
    self._attrs["borderDash"] = JsUtils.jsConvertData(narray, None)
    return self

  def borderDashOffset(self, n: Union[float, primitives.JsDataModel] = 0.0):
    """
    Description:
    ------------
    Offset for line dashes.

    Attributes:
    ----------
    :param Union[float, primitives.JsDataModel] n: Optional. The dash offset number.
    """
    self._attrs["borderDashOffset"] = JsUtils.jsConvertData(n, None)
    return self

  def lineWidth(self, num: Union[float, primitives.JsDataModel]):
    """
    Description:
    ------------
    Stroke width of grid lines.

    Attributes:
    ----------
    :param Union[float, primitives.JsDataModel] num: The line width.
    """
    self._attrs["lineWidth"] = JsUtils.jsConvertData(num, None)
    return self

  def drawBorder(self, flag: Union[bool, primitives.JsDataModel] = True):
    """
    Description:
    ------------
    If true, draw border at the edge between the axis and the chart area.

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: Optional. Flag to draw the border.
    """
    self._attrs["drawBorder"] = JsUtils.jsConvertData(flag, None)
    return self

  def drawOnChartArea(self, flag: Union[bool, primitives.JsDataModel] = True):
    """
    Description:
    ------------
    If true, draw lines on the chart area inside the axis lines.
    This is useful when there are multiple axes and you need to control which grid lines are drawn.

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: Optional.
    """
    self._attrs["drawOnChartArea"] = JsUtils.jsConvertData(flag, None)
    return self

  def drawTicks(self, flag: Union[bool, primitives.JsDataModel] = True):
    """
    Description:
    ------------
    If true, draw lines beside the ticks in the axis area beside the chart.

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: Optional.
    """
    self._attrs["drawTicks"] = JsUtils.jsConvertData(flag, None)
    return self

  def tickMarkLength(self, n: Union[int, primitives.JsDataModel] = 10):
    """
    Description:
    ------------
    Length in pixels that the grid lines will draw into the axis area.

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] n: Optional.
    """
    self._attrs["tickMarkLength"] = JsUtils.jsConvertData(n, None)
    return self

  def zeroLineWidth(self, n: Union[int, primitives.JsDataModel] = 1):
    """
    Description:
    ------------
    Stroke width of the grid line for the first index (index 0).

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] n: Optional.
    """
    self._attrs["zeroLineWidth"] = JsUtils.jsConvertData(n, None)
    return self

  def zeroLineColor(self, color: Union[str, primitives.JsDataModel] = "rgba(0, 0, 0, 0.25)"):
    """
    Description:
    ------------
    Stroke color of the grid line for the first index (index 0).

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] color: Optional. The RGBA color code.
    """
    self._attrs["zeroLineColor"] = JsUtils.jsConvertData(color, None)
    return self

  def zeroLineBorderDash(self, narray: Union[list, primitives.JsDataModel]):
    """
    Description:
    ------------
    Length and spacing of dashes of the grid line for the first index (index 0).

    Attributes:
    ----------
    :param Union[list, primitives.JsDataModel] narray:
    """
    self._attrs["zeroLineBorderDash"] = JsUtils.jsConvertData(narray, None)
    return self

  def zeroLineBorderDashOffset(self, n: Union[float, primitives.JsDataModel] = 0.0):
    """
    Description:
    ------------
    Offset for line dashes of the grid line for the first index (index 0).

    Attributes:
    ----------
    :param Union[float, primitives.JsDataModel] n: Optional.
    """
    self._attrs["zeroLineBorderDashOffset"] = JsUtils.jsConvertData(n, None)
    return self

  def offsetGridLines(self, flag: Union[bool, primitives.JsDataModel] = True):
    """
    Description:
    ------------
    If true, the bars for a particular data point fall between the grid lines.
    The grid line will move to the left by one half of the tick interval, which is the space between the grid lines.
    If false, the grid line will go right down the middle of the bars.
    This is set to true for a category scale in a bar chart while false for other scales or chart types by default.

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: Optional.
    """
    self._attrs["offsetGridLines"] = JsUtils.jsConvertData(flag, None)
    return self


class ChartJsOptScale(DataAttrs):

  def ticks(self) -> ChartJsOptTicks:
    if "ticks" not in self._attrs:
      self._attrs["ticks"] = ChartJsOptTicks(self.page)
    return self._attrs["ticks"]

  @property
  def gridLines(self) -> ChartJsOptGridLines:
    """
    Description:
    ------------

    :rtype: ChartJsOptGridLines
    """
    if "gridLines" not in self._attrs:
      self._attrs["gridLines"] = ChartJsOptGridLines(self.page)
    return self._attrs["gridLines"]

  def stacked(self, flag: Union[bool, primitives.JsDataModel] = False):
    pass


class ChartJsOptScaleBar(ChartJsOptScale):

  def barPercentage(self, n: Union[float, primitives.JsDataModel] = 0.9):
    """
    Description:
    ------------
    Percent (0-1) of the available width each bar should be within the category width.
    1.0 will take the whole category width and put the bars right next to each other.

    Attributes:
    ----------
    :param Union[float, primitives.JsDataModel] n: Optional.
    """
    if n > 1:
      raise ValueError("n cannot exceed 1")

    self._attrs["barPercentage"] = JsUtils.jsConvertData(n, None)
    return self

  def categoryPercentage(self, n: Union[float, primitives.JsDataModel] = 0.8):
    """
    Description:
    ------------
    Percent (0-1) of the available width each category should be within the sample width.

    Attributes:
    ----------
    :param Union[float, primitives.JsDataModel] n: Optional.
    """
    self._attrs["categoryPercentage"] = JsUtils.jsConvertData(n, None)
    return self

  def barThickness(self, width: Union[str, primitives.JsDataModel] = "flex"):
    """
    Description:
    ------------
    Manually set width of each bar in pixels.

    If set to 'flex', it computes "optimal" sample widths that globally arrange bars side by side.
    If not set (default), bars are equally sized based on the smallest interval.

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] width: Optional.
    """
    self._attrs["barThickness"] = JsUtils.jsConvertData(width, None)
    return self

  def maxBarThickness(self, width: Union[float, primitives.JsDataModel]):
    """
    Description:
    ------------
    Set this to ensure that bars are not sized thicker than this.

    Attributes:
    ----------
    :param Union[float, primitives.JsDataModel] width: A float
    """
    self._attrs["barThickness"] = JsUtils.jsConvertData(width, None)
    return self

  def minBarLength(self, width: Union[float, primitives.JsDataModel]):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[float, primitives.JsDataModel] width:
    """
    self._attrs["minBarLength"] = JsUtils.jsConvertData(width, None)
    return self


class ChartJsOptTooltip(DataAttrs):
  pass


class ChartJsOptLabels(DataAttrs):

  @property
  def fontColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/general/fonts.html
    """
    return self._attrs["fontColor"]

  @fontColor.setter
  def fontColor(self, val):
    self._attrs["fontColor"] = val


class ChartJsOptPadding(DataAttrs):
  @property
  def left(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/general/fonts.html
    """
    return self._attrs["left"]

  @left.setter
  def left(self, val):
    self._attrs["left"] = val

  @property
  def right(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/layout.html
    """
    return self._attrs["right"]

  @right.setter
  def right(self, val):
    self._attrs["right"] = val

  @property
  def top(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/layout.html
    """
    return self._attrs["top"]

  @top.setter
  def top(self, val):
    self._attrs["top"] = val

  @property
  def bottom(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/layout.html
    """
    return self._attrs["bottom"]

  @bottom.setter
  def bottom(self, val):
    self._attrs["bottom"] = val


class OptionsLegend(DataAttrs):
  def display(self, flag: Union[bool, primitives.JsDataModel] = True):
    """
    Description:
    ------------
    Is the legend shown?

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/legend.html

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: Optional.
    """
    self._attrs["display"] = JsUtils.jsConvertData(flag, None)
    return self

  def position(self, location: Union[str, primitives.JsDataModel] = "top"):
    """
    Description:
    ------------
    Position of the legend.

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] location: Optional.
    """
    self._attrs["position"] = JsUtils.jsConvertData(location, None)
    return self

  def fullWidth(self, flag: Union[bool, primitives.JsDataModel] = True):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: Optional.
    """

  def onClick(self, callback: Union[List[Union[str, primitives.JsDataModel]], str],
              profile: Optional[Union[dict, bool]] = False):
    """
    Description:
    ------------
    A callback that is called when a click event is registered on a label item.

    Attributes:
    ----------
    :param Union[List[Union[str, primitives.JsDataModel]], str] callback: The Javascript functions
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self._attrs["onClick"] = JsUtils.jsConvertFncs(callback, profile=profile)
    return self

  def onHover(self, callback: Union[List[Union[str, primitives.JsDataModel]], str],
              profile: Optional[Union[dict, bool]] = False):
    """
    Description:
    ------------
    A callback that is called when a 'mousemove' event is registered on top of a label item.

    Attributes:
    ----------
    :param Union[List[Union[str, primitives.JsDataModel]], str] callback: The Javascript functions
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self._attrs["onHover"] = JsUtils.jsConvertFncs(callback, profile=profile)
    return self

  def onLeave(self, callback: Union[List[Union[str, primitives.JsDataModel]], str],
              profile: Optional[Union[dict, bool]] = False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param callback: String | List. The Javascript functions
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self._attrs["onLeave"] = JsUtils.jsConvertFncs(callback, profile=profile)
    return self

  def reverse(self, flag: Union[bool, primitives.JsDataModel] = False):
    """
    Description:
    ------------
    Legend will show datasets in reverse order.

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: Boolean. Optional.
    """
    self._attrs["reverse"] = JsUtils.jsConvertData(flag, None)
    return self

  @property
  def labels(self) -> ChartJsOptLabels:
    """
    Description:
    ------------

    :rtype: ChartJsOptLabels
    """
    if 'labels' not in self._attrs:
      self._attrs["labels"] = ChartJsOptLabels(self.page)
    return self._attrs["labels"]


class OptionsTitle(DataAttrs):
  @property
  def display(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/configuration/title.html
    """
    return self._attrs["display"]

  @display.setter
  def display(self, val):
    self._attrs["display"] = val

  @property
  def text(self):
    """
    Description:
    ------------
    """
    return self._attrs["text"]

  @text.setter
  def text(self, val):
    self._attrs["text"] = val

  @property
  def position(self):
    """
    Description:
    ------------
    """
    return self._attrs["position"]

  @position.setter
  def position(self, val):
    self._attrs["position"] = val

  @property
  def fontSize(self):
    """
    Description:
    ------------
    """
    return self._attrs["fontSize"]

  @fontSize.setter
  def fontSize(self, val):
    self._attrs["fontSize"] = val

  @property
  def fontFamily(self):
    """
    Description:
    ------------
    """
    return self._attrs["fontFamily"]

  @fontFamily.setter
  def fontFamily(self, val):
    self._attrs["fontFamily"] = val

  @property
  def fontColor(self):
    """
    Description:
    ------------
    """
    return self._attrs["fontColor"]

  @fontColor.setter
  def fontColor(self, val):
    self._attrs["fontColor"] = val

  @property
  def fontStyle(self):
    """
    Description:
    ------------
    """
    return self._attrs["fontStyle"]

  @fontStyle.setter
  def fontStyle(self, val):
    self._attrs["fontStyle"] = val

  @property
  def padding(self):
    """
    Description:
    ------------
    """
    return self._attrs["padding"]

  @padding.setter
  def padding(self, val):
    self._attrs["padding"] = val

  @property
  def lineHeight(self):
    """
    Description:
    ------------
    """
    return self._attrs["lineHeight"]

  @lineHeight.setter
  def lineHeight(self, val):
    self._attrs["lineHeight"] = val


class Options(DataAttrs):

  def __init__(self, page, attrs=None, options=None):
    super(Options, self).__init__(page, attrs, options)

  def title(self):
    """
    Description:
    ------------

    """
    if self._attrs.get("title") is None:
      self._attrs['title'] = OptionsTitle(self.page)
    return self._attrs['title']


class DataSet(DataAttrs):

  @property
  def backgroundColor(self):
    """
    Description:
    ------------
    Arc background color.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/doughnut.html
      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("backgroundColor")

  @backgroundColor.setter
  def backgroundColor(self, val: str):
    self._attrs["backgroundColor"] = val

  @property
  def borderColor(self):
    """
    Description:
    ------------
    Arc border color.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/doughnut.html
    """
    return self._attrs.get("borderColor")

  @borderColor.setter
  def borderColor(self, val: str):
    self._attrs["borderColor"] = val

  @property
  def borderWidth(self):
    """
    Description:
    ------------
    Arc border width (in pixels).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/doughnut.html
    """
    return self._attrs.get("borderWidth")

  @borderWidth.setter
  def borderWidth(self, val: int):
    self._attrs["borderWidth"] = val

  @property
  def fillOpacity(self):
    """
    Description:
    ------------
    Convert the hexadecimal color to the corresponding RGB one with the opacity.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/doughnut.html
    """
    return self._attrs.get("backgroundColor")

  @fillOpacity.setter
  def fillOpacity(self, val):
    bg_colors = self._attrs["backgroundColor"]
    if isinstance(bg_colors, list):
      op_colors = []
      for c in bg_colors:
        color = Colors.getHexToRgb(c)
        op_colors.append("rgba(%s, %s, %s, %s)" % (color[0], color[1], color[2], val))
      self._attrs["backgroundColor"] = op_colors
    else:
      if bg_colors.startswith("rgba"):
        split_colors = bg_colors.split(",")
        split_colors[3] = " %s)" % val
        self._attrs["backgroundColor"] = ",".join(split_colors)
      else:
        color = Colors.getHexToRgb(self._attrs["backgroundColor"])
        self._attrs["backgroundColor"] = "rgba(%s, %s, %s, %s)" % (color[0], color[1], color[2], val)

  def set_style(self, background_color=None, fill_opacity=None, border_width=None, border_color=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param background_color: String. Optional. The background color code.
    :param fill_opacity: Number. Optional. The opacity factor.
    :param border_width: Number. Optional. The border width.
    :param border_color: String. Optional. The border color code.
    """
    if background_color is not None:
      self.backgroundColor = background_color
    if fill_opacity is not None:
      self.fillOpacity = fill_opacity
    if border_width is not None:
      self.borderWidth = border_width
    if border_color is not None:
      self.borderColor = border_color
    return self


class DataSetPie(DataSet):

  @property
  def borderAlign(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/doughnut.html
    """
    return self._attrs.get("borderAlign")

  @borderAlign.setter
  def borderAlign(self, val):
    self._attrs["borderAlign"] = val

  @property
  def data(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/doughnut.html
    """
    return self._attrs["data"]

  @data.setter
  def data(self, val):
    self._attrs["data"] = val

  @property
  def hoverBackgroundColor(self):
    """
    Description:
    ------------
    Arc background color when hovered.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/doughnut.html
    """
    return self._attrs.get("hoverBackgroundColor")

  @hoverBackgroundColor.setter
  def hoverBackgroundColor(self, val):
    self._attrs["hoverBackgroundColor"] = val

  @property
  def hoverBorderColor(self):
    """
    Description:
    ------------
    Arc border color when hovered.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/doughnut.html
    """
    return self._attrs.get("hoverBorderColor")

  @hoverBorderColor.setter
  def hoverBorderColor(self, val):
    self._attrs["hoverBorderColor"] = val

  @property
  def hoverBorderWidth(self):
    """
    Description:
    ------------
    Arc border width when hovered (in pixels).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/doughnut.html
    """
    return self._attrs.get("hoverBorderWidth")

  @hoverBorderWidth.setter
  def hoverBorderWidth(self, val):
    self._attrs["hoverBorderWidth"] = val

  @property
  def weight(self):
    """
    Description:
    ------------
    The relative thickness of the dataset.
    Providing a value for weight will cause the pie or doughnut dataset to be drawn with a thickness relative to the
    sum of all the dataset weight values.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/doughnut.html
    """
    return self._attrs.get("weight")

  @weight.setter
  def weight(self, val):
    self._attrs["weight"] = val

  def set_style(self, background_colors=None, fill_opacity=None, border_width=None, border_colors=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param background_colors: List. Optional.
    :param fill_opacity: Number. Optional. The opacity factor.
    :param border_width:
    :param border_colors:
    """
    if background_colors is not None:
      self.backgroundColor = background_colors
    if fill_opacity is not None:
      self.fillOpacity = fill_opacity
    if border_width is not None:
      self.borderWidth = border_width
    if border_colors is not None:
      self.borderColor = border_colors
    return self


class DataSetScatterLine(DataSet):
  @property
  def borderCapStyle(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("borderCapStyle")

  @borderCapStyle.setter
  def borderCapStyle(self, val):
    self._attrs["borderCapStyle"] = val

  @property
  def borderDash(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("borderDash")

  @borderDash.setter
  def borderDash(self, val):
    self._attrs["borderDash"] = val

  @property
  def borderDashOffset(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("borderDashOffset")

  @borderDashOffset.setter
  def borderDashOffset(self, val):
    self._attrs["borderDashOffset"] = val

  @property
  def borderJoinStyle(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("borderJoinStyle")

  @borderJoinStyle.setter
  def borderJoinStyle(self, val):
    self._attrs["borderJoinStyle"] = val

  @property
  def cubicInterpolationMode(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("cubicInterpolationMode")

  @cubicInterpolationMode.setter
  def cubicInterpolationMode(self, val):
    self._attrs["cubicInterpolationMode"] = val

  @property
  def clip(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("clip")

  @clip.setter
  def clip(self, val):
    self._attrs["clip"] = val

  @property
  def fill(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("fill")

  @fill.setter
  def fill(self, val):
    self._attrs["fill"] = val

  @property
  def hoverBackgroundColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("hoverBackgroundColor")

  @hoverBackgroundColor.setter
  def hoverBackgroundColor(self, val: str):
    self._attrs["hoverBackgroundColor"] = val

  @property
  def hoverBorderCapStyle(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("hoverBorderCapStyle")

  @hoverBorderCapStyle.setter
  def hoverBorderCapStyle(self, val):
    self._attrs["hoverBorderCapStyle"] = val

  @property
  def hoverBorderColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("hoverBorderColor")

  @hoverBorderColor.setter
  def hoverBorderColor(self, val: str):
    self._attrs["hoverBorderColor"] = val

  @property
  def hoverBorderDash(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("hoverBorderDash")

  @hoverBorderDash.setter
  def hoverBorderDash(self, val):
    self._attrs["hoverBorderDash"] = val

  @property
  def hoverBorderDashOffset(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("hoverBorderDashOffset")

  @hoverBorderDashOffset.setter
  def hoverBorderDashOffset(self, val):
    self._attrs["hoverBorderDashOffset"] = val

  @property
  def hoverBorderJoinStyle(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("hoverBorderJoinStyle")

  @hoverBorderJoinStyle.setter
  def hoverBorderJoinStyle(self, val):
    self._attrs["hoverBorderJoinStyle"] = val

  @property
  def hoverBorderWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("hoverBorderWidth")

  @hoverBorderWidth.setter
  def hoverBorderWidth(self, val: int):
    self._attrs["hoverBorderWidth"] = val

  @property
  def label(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("label")

  @label.setter
  def label(self, val: str):
    self._attrs["label"] = val

  @property
  def lineTension(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("lineTension")

  @lineTension.setter
  def lineTension(self, val: float):
    self._attrs["lineTension"] = val

  @property
  def order(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("order")

  @order.setter
  def order(self, val):
    self._attrs["order"] = val

  @property
  def pointBackgroundColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("pointBackgroundColor")

  @pointBackgroundColor.setter
  def pointBackgroundColor(self, val: str):
    self._attrs["pointBackgroundColor"] = val

  @property
  def pointBorderColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("pointBorderColor")

  @pointBorderColor.setter
  def pointBorderColor(self, val: str):
    self._attrs["pointBorderColor"] = val

  @property
  def pointBorderWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("pointBorderWidth")

  @pointBorderWidth.setter
  def pointBorderWidth(self, val):
    self._attrs["pointBorderWidth"] = val

  @property
  def pointHitRadius(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("pointHitRadius")

  @pointHitRadius.setter
  def pointHitRadius(self, val):
    self._attrs["pointHitRadius"] = val

  @property
  def pointHoverBackgroundColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("pointHoverBackgroundColor")

  @pointHoverBackgroundColor.setter
  def pointHoverBackgroundColor(self, val):
    self._attrs["pointHoverBackgroundColor"] = val

  @property
  def pointHoverBorderColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("pointHoverBorderColor")

  @pointHoverBorderColor.setter
  def pointHoverBorderColor(self, val):
    self._attrs["pointHoverBorderColor"] = val

  @property
  def pointHoverBorderWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("pointHoverBorderWidth")

  @pointHoverBorderWidth.setter
  def pointHoverBorderWidth(self, val):
    self._attrs["pointHoverBorderWidth"] = val

  @property
  def pointHoverRadius(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("pointHoverRadius")

  @pointHoverRadius.setter
  def pointHoverRadius(self, val):
    self._attrs["pointHoverRadius"] = val

  @property
  def pointRadius(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("pointRadius")

  @pointRadius.setter
  def pointRadius(self, val):
    self._attrs["pointRadius"] = val

  @property
  def pointRotation(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("pointRotation")

  @pointRotation.setter
  def pointRotation(self, val):
    self._attrs["pointRotation"] = val

  @property
  def pointStyle(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("pointStyle")

  @pointStyle.setter
  def pointStyle(self, val):
    self._attrs["pointStyle"] = val

  @property
  def showLine(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("showLine")

  @showLine.setter
  def showLine(self, val):
    self._attrs["showLine"] = val

  @property
  def spanGaps(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("spanGaps")

  @spanGaps.setter
  def spanGaps(self, val):
    self._attrs["spanGaps"] = val

  @property
  def steppedLine(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("steppedLine")

  @steppedLine.setter
  def steppedLine(self, val):
    self._attrs["steppedLine"] = val

  @property
  def xAxisID(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("xAxisID")

  @xAxisID.setter
  def xAxisID(self, val):
    self._attrs["xAxisID"] = val

  @property
  def yAxisID(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._attrs.get("yAxisID")

  @yAxisID.setter
  def yAxisID(self, val):
    self._attrs["yAxisID"] = val

  def set_style(self, background_color=None, fill_opacity=None, border_width=None, border_color=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param background_color:
    :param fill_opacity:
    :param border_width:
    :param border_color:
    """
    if background_color is not None:
      self.backgroundColor = background_color
    if fill_opacity is not None:
      self.fillOpacity = fill_opacity
    if border_width is not None:
      self.borderWidth = border_width
    if border_color is not None:
      self.borderColor = border_color
    return self


class DataSetBar(DataSet):

  @property
  def barPercentage(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs.get("barPercentage")

  @barPercentage.setter
  def barPercentage(self, val):
    self._attrs["barPercentage"] = val

  @property
  def barThickness(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs.get("barThickness")

  @barThickness.setter
  def barThickness(self, val):
    self._attrs["barThickness"] = val

  @property
  def maxBarThickness(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs.get("maxBarThickness")

  @maxBarThickness.setter
  def maxBarThickness(self, val):
    self._attrs["maxBarThickness"] = val

  @property
  def minBarLength(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs.get("minBarLength")

  @minBarLength.setter
  def minBarLength(self, val):
    self._attrs["minBarLength"] = val

  @property
  def borderSkipped(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs.get("borderSkipped")

  @borderSkipped.setter
  def borderSkipped(self, val):
    self._attrs["borderSkipped"] = val

  @property
  def data(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs["data"]

  @data.setter
  def data(self, val):
    self._attrs["data"] = val

  @property
  def hoverBackgroundColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs.get("hoverBackgroundColor")

  @hoverBackgroundColor.setter
  def hoverBackgroundColor(self, val):
    self._attrs["hoverBackgroundColor"] = val

  @property
  def hoverBorderColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs.get("hoverBorderColor")

  @hoverBorderColor.setter
  def hoverBorderColor(self, val):
    self._attrs["hoverBorderColor"] = val

  @property
  def hoverBorderWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs.get("hoverBorderWidth")

  @hoverBorderWidth.setter
  def hoverBorderWidth(self, val):
    self._attrs["hoverBorderWidth"] = val

  @property
  def label(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs["label"]

  @label.setter
  def label(self, val):
    self._attrs["label"] = val

  @property
  def order(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs.get("order")

  @order.setter
  def order(self, val):
    self._attrs["order"] = val

  @property
  def xAxisID(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs.get("xAxisID")

  @xAxisID.setter
  def xAxisID(self, val):
    self._attrs["xAxisID"] = val

  @property
  def yAxisID(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._attrs.get("yAxisID")

  @yAxisID.setter
  def yAxisID(self, val):
    self._attrs["yAxisID"] = val


class DataSetPolar(DataSet):

  @property
  def borderAlign(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/polar.html
    """
    return self._attrs.get("borderAlign")

  @borderAlign.setter
  def borderAlign(self, val):
    self._attrs["borderAlign"] = val

  @property
  def data(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/polar.html
    """
    return self._attrs["data"]

  @data.setter
  def data(self, val):
    self._attrs["data"] = val

  @property
  def hoverBackgroundColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/polar.html
    """
    return self._attrs.get("hoverBackgroundColor")

  @hoverBackgroundColor.setter
  def hoverBackgroundColor(self, val):
    self._attrs["hoverBackgroundColor"] = val

  @property
  def hoverBorderColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/polar.html
    """
    return self._attrs.get("hoverBorderColor")

  @hoverBorderColor.setter
  def hoverBorderColor(self, val):
    self._attrs["hoverBorderColor"] = val

  @property
  def hoverBorderWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/polar.html
    """
    return self._attrs.get("hoverBorderWidth")

  @hoverBorderWidth.setter
  def hoverBorderWidth(self, val):
    self._attrs["hoverBorderWidth"] = val


class DataSetRadar(DataSet):

  @property
  def borderCapStyle(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("borderCapStyle")

  @borderCapStyle.setter
  def borderCapStyle(self, val):
    self._attrs["borderCapStyle"] = val

  @property
  def borderDash(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("borderDash")

  @borderDash.setter
  def borderDash(self, val):
    self._attrs["borderDash"] = val

  @property
  def borderDashOffset(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("borderDashOffset")

  @borderDashOffset.setter
  def borderDashOffset(self, val):
    self._attrs["borderDashOffset"] = val

  @property
  def borderJoinStyle(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("borderJoinStyle")

  @borderJoinStyle.setter
  def borderJoinStyle(self, val):
    self._attrs["borderJoinStyle"] = val

  @property
  def hoverBackgroundColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("hoverBackgroundColor")

  @hoverBackgroundColor.setter
  def hoverBackgroundColor(self, val):
    self._attrs["hoverBackgroundColor"] = val

  @property
  def hoverBorderCapStyle(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("hoverBorderCapStyle")

  @hoverBorderCapStyle.setter
  def hoverBorderCapStyle(self, val):
    self._attrs["hoverBorderCapStyle"] = val

  @property
  def hoverBorderColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("hoverBorderColor")

  @hoverBorderColor.setter
  def hoverBorderColor(self, val):
    self._attrs["hoverBorderColor"] = val

  @property
  def hoverBorderDash(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("hoverBorderDash")

  @hoverBorderDash.setter
  def hoverBorderDash(self, val):
    self._attrs["hoverBorderDash"] = val

  @property
  def hoverBorderDashOffset(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("hoverBorderDashOffset")

  @hoverBorderDashOffset.setter
  def hoverBorderDashOffset(self, val):
    self._attrs["hoverBorderDashOffset"] = val

  @property
  def hoverBorderJoinStyle(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("hoverBorderJoinStyle")

  @hoverBorderJoinStyle.setter
  def hoverBorderJoinStyle(self, val):
    self._attrs["hoverBorderJoinStyle"] = val

  @property
  def hoverBorderWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("hoverBorderWidth")

  @hoverBorderWidth.setter
  def hoverBorderWidth(self, val):
    self._attrs["hoverBorderWidth"] = val

  @property
  def fill(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("fill")

  @fill.setter
  def fill(self, val):
    self._attrs["fill"] = val

  @property
  def label(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs["label"]

  @label.setter
  def label(self, val):
    self._attrs["label"] = val

  @property
  def order(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("order")

  @order.setter
  def order(self, val):
    self._attrs["order"] = val

  @property
  def lineTension(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("lineTension")

  @lineTension.setter
  def lineTension(self, val):
    self._attrs["lineTension"] = val

  @property
  def pointBackgroundColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("pointBackgroundColor")

  @pointBackgroundColor.setter
  def pointBackgroundColor(self, val):
    self._attrs["pointBackgroundColor"] = val

  @property
  def pointBorderColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("pointBorderColor")

  @pointBorderColor.setter
  def pointBorderColor(self, val):
    self._attrs["pointBorderColor"] = val

  @property
  def pointBorderWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("pointBorderWidth")

  @pointBorderWidth.setter
  def pointBorderWidth(self, val):
    self._attrs["pointBorderWidth"] = val

  @property
  def pointHitRadius(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("pointHitRadius")

  @pointHitRadius.setter
  def pointHitRadius(self, val):
    self._attrs["pointHitRadius"] = val

  @property
  def pointHoverBackgroundColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("pointHoverBackgroundColor")

  @pointHoverBackgroundColor.setter
  def pointHoverBackgroundColor(self, val):
    self._attrs["pointHoverBackgroundColor"] = val

  @property
  def pointHoverBorderColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("pointHoverBorderColor")

  @pointHoverBorderColor.setter
  def pointHoverBorderColor(self, val):
    self._attrs["pointHoverBorderColor"] = val

  @property
  def pointHoverBorderWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("pointHoverBorderWidth")

  @pointHoverBorderWidth.setter
  def pointHoverBorderWidth(self, val):
    self._attrs["pointHoverBorderWidth"] = val

  @property
  def pointHoverRadius(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("pointHoverRadius")

  @pointHoverRadius.setter
  def pointHoverRadius(self, val):
    self._attrs["pointHoverRadius"] = val

  @property
  def pointRadius(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("pointRadius")

  @pointRadius.setter
  def pointRadius(self, val):
    self._attrs["pointRadius"] = val

  @property
  def pointRotation(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("pointRotation")

  @pointRotation.setter
  def pointRotation(self, val):
    self._attrs["pointRotation"] = val

  @property
  def pointStyle(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("pointStyle")

  @pointStyle.setter
  def pointStyle(self, val):
    self._attrs["pointStyle"] = val

  @property
  def spanGaps(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/radar.html
    """
    return self._attrs.get("spanGaps")

  @spanGaps.setter
  def spanGaps(self, val):
    self._attrs["spanGaps"] = val


class DataSetBubble(DataSet):

  @property
  def data(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bubble.html
    """
    return self._attrs["data"]

  @data.setter
  def data(self, val):
    self._attrs["data"] = val

  @property
  def hoverBackgroundColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bubble.html
    """
    return self._attrs["hoverBackgroundColor"]

  @hoverBackgroundColor.setter
  def hoverBackgroundColor(self, val):
    self._attrs["hoverBackgroundColor"] = val

  @property
  def hoverBorderColor(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bubble.html
    """
    return self._attrs["hoverBorderColor"]

  @hoverBorderColor.setter
  def hoverBorderColor(self, val):
    self._attrs["hoverBorderColor"] = val

  @property
  def hoverBorderWidth(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bubble.html
    """
    return self._attrs["hoverBorderWidth"]

  @hoverBorderWidth.setter
  def hoverBorderWidth(self, val):
    self._attrs["hoverBorderWidth"] = val

  @property
  def hoverRadius(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bubble.html
    """
    return self._attrs["hoverRadius"]

  @hoverRadius.setter
  def hoverRadius(self, val):
    self._attrs["hoverRadius"] = val

  @property
  def hitRadius(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bubble.html
    """
    return self._attrs["hitRadius"]

  @hitRadius.setter
  def hitRadius(self, val):
    self._attrs["hitRadius"] = val

  @property
  def label(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bubble.html
    """
    return self._attrs["label"]

  @label.setter
  def label(self, val):
    self._attrs["label"] = val

  @property
  def order(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bubble.html
    """
    return self._attrs["order"]

  @order.setter
  def order(self, val):
    self._attrs["order"] = val

  @property
  def pointStyle(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bubble.html
    """
    return self._attrs["pointStyle"]

  @pointStyle.setter
  def pointStyle(self, val):
    self._attrs["pointStyle"] = val

  @property
  def rotation(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bubble.html
    """
    return self._attrs["rotation"]

  @rotation.setter
  def rotation(self, val):
    self._attrs["rotation"] = val

  @property
  def radius(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bubble.html
    """
    return self._attrs["radius"]

  @radius.setter
  def radius(self, val):
    self._attrs["radius"] = val


# class ChartJsType(object):
#
#   def __init__(self, report, type, data):
#     self._report, self._type, self._data = report, type, data
#     self._data_attrs, self._opts_attrs = {}, {}
#
#   def toStr(self):
#     return '{type: "%s", data: %s}' % (self._type, self._data.toStr())
#
#   def backgroundColor(self, colors):
#     """
#     Data attribute to change the background color (the area between the line chart and the x axis)
#
#     :param colors: Array. The list of colors to add to the data definition
#     :return: The ChartJs configuration dictionary for chaining
#     """
#     self._data_attrs["backgroundColor"] = colors
#     return self
#
#   def pointStyle(self, text):
#     """
#
#     Documentation
#
#     :param text:
#     :return:
#     """
#     self._data_attrs["pointStyle"] = text
#     return self
#
#   def borderColor(self, colors):
#     """
#
#     Documentation
#
#     :param colors:
#     :return:
#     """
#     self._data_attrs["backgroundColor"] = colors
#     return self
#
#   def fill(self, flag):
#     """
#
#     Documentation
#
#     :param flag:
#     :return:
#     """
#     self._data_attrs["fill"] = flag
#     return self
#
#   def steppedLine(self, flag):
#     self._data_attrs["steppedLine"] = flag
#     return self
#
#   def customDataAttr(self, name, value):
#     """
#     Add a bespoke attribute to the ChartJs definition
#
#     Example
#
#     Documentation
#
#     :param name: The name of the option
#     :param value: The value of the option
#
#     :return:
#     """
#     self._data_attrs[name] = JsUtils.jsConvertData(value, None)
#     return self
#
#   def maintainAspectRatio(self, flag):
#     """
#
#     Example
#
#     Documentation
#
#     :param flag:
#     :return:
#     """
#     self._opts_attrs["maintainAspectRatio"] = flag
#     return self
#
#   def responsive(self, flag):
#     self._opts_attrs["responsive"] = flag
#     return self
#
#   def scaleShowLabels(self, flag):
#     self._opts_attrs["scaleShowLabels"] = flag
#     return self
#
#   def customOption(self, name, value):
#     """
#     Add a bespoke option to the ChartJs definition
#
#     :param name: The name of the option
#     :param value: The value of the option
#
#     :return:
#     """
#     self._opts_attrs[name] = JsUtils.jsConvertData(value, None)
#     return self
#
#   @property
#   def legend(self):
#     return OptionsLegend(self._report)
#
#   @property
#   def xAxes(self):
#     self._opts_attrs.setdefault("scales", {})["xAxes"] = []
#     return ChartJsOptScale(self._opts_attrs.setdefault("scales", {})["xAxes"])
#
#   @property
#   def yAxes(self):
#     self._opts_attrs.setdefault("scales", {})["yAxes"] = []
#     return ChartJsOptScale(self._opts_attrs.setdefault("scales", {})["yAxes"])
#
#   def build(self, htmlCode, varName):
#     return "var %s = new Chart(document.getElementById('%s'), %s)" % (varName, htmlCode, self)
#
#
# class ChartJsTypeBar(ChartJsType):
#
#   def __init__(self, report, data, type='bar'):
#     super(ChartJsTypeBar, self).__init__(report, type, data)
#     self._data_attrs, self._opts_attrs = {}, {}
#     self._data_attrs.update({"type": JsUtils.jsConvertData(type, None), "data": data})
#
#   def backgroundColor(self, colors='rgba(0, 0, 0, 0.1)'):
#     """
#
#     Documentation
#     https://www.chartjs.org/docs/latest/charts/bar.html
#
#     :param colors:
#     :return:
#     """
#     if not isinstance(colors, list):
#       colors = [colors]
#     self._data_attrs["backgroundColor"] = colors
#     return self
#
#   def borderColor(self, colors='rgba(0, 0, 0, 0.1)'):
#     """
#
#     Documentation
#     https://www.chartjs.org/docs/latest/charts/bar.html
#
#     :param colors:
#     :return:
#     """
#     if not isinstance(colors, list):
#       colors = [colors]
#     self._data_attrs["borderColor"] = colors
#     return self
#
#   def borderSkipped(self, text='bottom'):
#     """
#     This setting is used to avoid drawing the bar stroke at the base of the fill.
#     In general, this does not need to be changed except when creating chart types that derive from a bar chart.
#
#     Documentation
#     https://www.chartjs.org/docs/latest/charts/bar.html#borderskipped
#
#     :param text: A value among ['bottom', 'left', 'top', 'right', False]
#
#     :return:
#     """
#     skipped_pos = ['bottom', 'left', 'top', 'right', False]
#     if not text in skipped_pos:
#       raise Exception("text value should be in %s" % skipped_pos)
#
#     self._data_attrs["borderSkipped"] = JsUtils.jsConvertData(text, None)
#     return self
#
#   def borderWidth(self, n=0):
#     """
#     If this value is a number, it is applied to all sides of the rectangle (left, top, right, bottom), except borderSkipped.
#     If this value is an object, the left property defines the left border width.
#     Similarly the right, top and bottom properties can also be specified. Omitted borders and borderSkipped are skipped.
#
#     Documentation
#     https://www.chartjs.org/docs/latest/charts/bar.html#borderwidth
#
#     :param n:
#     :return:
#     """
#     self._data_attrs["borderWidth"] = n
#     return self
#
#   def hoverBackgroundColor(self, colors):
#     pass
#
#   def hoverBorderColor(self, colors):
#     pass
#
#   def hoverBorderWidth(self, n):
#     pass
#
#   def label(self, text):
#     """
#     The label for the dataset which appears in the legend and tooltips.
#
#     :param text:
#     :return:
#     """
#     self._data_attrs["label"] = JsUtils.jsConvertData(text, None)
#     return self
#
#   def xAxisID(self, axisId):
#     """
#     The ID of the x axis to plot this dataset on.
#
#     Documentation
#     https://www.chartjs.org/docs/latest/charts/bar.html#general
#
#     :param axisId: The ID of the x axis to plot this dataset on.
#
#     """
#
#   def yAxisID(self, axisId):
#     pass
#
#   @property
#   def scales(self):
#     """
#
#     :rtype: ChartJsOptScaleBar
#     :return:
#     """
#     if not "scales" in self._data_attrs:
#       self._data_attrs["scales"] = ChartJsOptScaleBar(self._report)
#     return self._data_attrs["scales"]
#
#   def __str__(self):
#     return "{%s}" % ", ".join(["%s: %s" % (k, v) for k, v in self._data_attrs.items()])
#
#
# class ChartJsTypeRadar(ChartJsType):
#   def __init__(self, report, data, type='radar'):
#     super(ChartJsTypeRadar, self).__init__(report, type, data)
#     self._datasets, self.__options, self.__config = [], None, None
#
#   def dataset(self, i=None):
#     if i is None:
#       return self._datasets[-1]
#
#     return self._datasets[i]
#
#   def add_dataset(self, data):
#     """
#
#     :param data:
#     :return:
#     """
#     data = DataSetRadar(self._report, attrs={"data": data})
#     self._datasets.append(data)
#     return data
#
#   @property
#   def config(self):
#     """
#
#     :rtype: Config
#     :return:
#     """
#     if self.__config is None:
#       self.__config = Config(self._report)
#     return self.__config
#
#   @property
#   def options(self):
#     """
#
#     :rtype: Options
#     :return:
#     """
#     if self._options is None:
#       self._options = Options(self._report)
#     return self._options
#
#   def toStr(self):
#     print(self.config.toStr())
#     print("{%s}" % ", ".join([d.toStr() for d in self._datasets]))
#

# class ChartJsTypePie(ChartJsType):
#   def __init__(self, report, data, type='pie'):
#     super(ChartJsTypePie, self).__init__(report, type, data)
#     self._datasets, self.__options, self.__config = [], None, None
#
#   def dataset(self, i=None):
#     if i is None:
#       return self._datasets[-1]
#
#     return self._datasets[i]
#
#   def add_dataset(self, data):
#     """
#
#     :param data:
#     """
#     data = DataSetPie(self._report, attrs={"data": data})
#     self._datasets.append(data)
#     return data
#
#   def toStr(self):
#     return "{type: '%s', data: {labels: %s, datasets: [%s]}}" % (self._type, self.labels, ", ".join([d.toStr() for d in self._datasets]))
#


#
# if __name__ == '__main__':
#   # chart_bar = ChartJsTypeBar(None, []).label("test")
#   # chart_bar.scales.barPercentage(0.4).barThickness(3)
#   # chart_bar.scales.gridLines.circular(True).color(["red"]).drawTicks()
#   # print(chart_bar.build("A", "toto"))
#   chart = ChartJsTypeRadar(None, [])
#   #chart.config.duration = 40
#   dataset = chart.add_dataset([])
#   dataset.label = "test"
#   dataset.borderColor = 'red'
#
#   print(chart.toStr())
#
#   data = '''
# backgroundColor	The line fill color.
# borderCapStyle	Cap style of the line. See MDN.
# borderColor	The line color.
# borderDash	Length and spacing of dashes. See MDN.
# borderDashOffset	Offset for line dashes. See MDN.
# borderJoinStyle	Line joint style. See MDN.
# borderWidth	The line width (in pixels).
# clip	How to clip relative to chartArea. Positive value allows overflow, negative value clips that many pixels inside chartArea. 0 = clip at chartArea. Clipping can also be configured per side: clip: {left: 5, top: false, right: -2, bottom: 0}
# fill	How to fill the area under the line. See area charts.
# lineTension	Bezier curve tension of the line. Set to 0 to draw straightlines. This option is ignored if monotone cubic interpolation is used.
# showLine	If false, the line is not drawn for this dataset.
# spanGaps	If true, lines will be drawn between points with no or null data. If false, points with NaN data will create a break in the line.
# '''
#   for r in data.split("\n"):
#     row = r.strip().split()
#     if row:
#       data = {"attr": row[0], 'web': "https://www.chartjs.org/docs/latest/charts/line.html"}
#       print('''
#     @property
#     def %(attr)s(self):
#       """
#       %(web)s
#       """
#       return self._attrs["%(attr)s"]
#
#     @%(attr)s.setter
#     def %(attr)s(self, val):
#       self._attrs["%(attr)s"] = val
#       ''' % data)
