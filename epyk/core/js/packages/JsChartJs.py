#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional, List, Dict
from epyk.core.py import primitives, types
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
        """Time for the animation of the redraw in milliseconds.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_
        """
        return self._attrs["duration"]

    @duration.setter
    def duration(self, time):
        self._attrs["duration"] = time

    @property
    def lazy(self):
        """If true, the animation can be interrupted by other animations.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_
        """
        return self._attrs["lazy"]

    @lazy.setter
    def lazy(self, flag):
        self._attrs["lazy"] = flag

    @property
    def easing(self):
        """Set the easing option.

        `Animation <https://www.chartjs.org/docs/latest/configuration/animations.html>`_
        """
        return self._attrs["easing"]

    @easing.setter
    def easing(self, value: str):
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

    def getElementsAtEvent(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
        """Calling getElementsAtEvent(event) on your Chart instance passing an argument of an event,
        or jQuery event, will return the point elements that are at that the same position of that event.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if self.page.imports.pkgs.chart_js.version:
            return self.getElementsAtEventForMode(js_funcs, profile=profile)
        else:
            if not isinstance(js_funcs, list):
                js_funcs = [js_funcs]
            return JsObjects.JsArray.JsArray("%s.getElementsAtEvent(%s)" % (
                self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)), is_py_data=False)

    @JsUtils.fromVersion({'chart.js': '3.0.0'})
    def getElementsAtEventForMode(self, js_funcs: types.JS_FUNCS_TYPES, mode: str = "nearest",
                                  options: types.OPTION_TYPE = None, use_final_position: bool = True,
                                  profile: types.PROFILE_TYPE = False):
        """Calling getElementsAtEventForMode(e, mode, options, useFinalPosition) on your Chart instance passing an event
        and a mode will return the elements that are found. The options and useFinalPosition arguments are passed
        through to the handlers.

        `Animation <https://www.chartjs.org/docs/latest/configuration/animations.html>`_

        :param js_funcs: The Javascript functions
        :param mode: Optional.
        :param options: Optional.
        :param use_final_position: Optional.
        :param profile: Optional.
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
        """Add point to an exiting chart on existing series.

        Note: Do not forget to trigger an update on the chart once all your transformations are done.

        `Updated <https://www.chartjs.org/docs/latest/developers/updates.html>`_

        :param point: The point to add on the x-axis
        :param values: The value per series name
        """
        point = JsUtils.jsConvertData(point, None)
        values = JsUtils.jsConvertData(values, None)
        return JsObjects.JsVoid('''var index = %(varName)s.data.labels.indexOf(%(point)s);
if(index >= 0){
  %(varName)s.data.datasets.forEach(function(dataset){
    if(%(values)s[dataset.label] !== undefined){dataset.data[index] = %(values)s[dataset.label] }})
} else {
  %(varName)s.data.labels.push(%(point)s);
  %(varName)s.data.datasets.forEach(function(dataset){
    dataset.data.push(%(values)s[dataset.label])})}''' % {
      'varName': self.varName, 'point': point, 'values': values})

    def remove(self, point=None, series_names: Union[list, primitives.JsDataModel] = None):
        """Remove point to existing series.

        Note: Do not forget to trigger an update on the chart once all your transformations are done.

        `Updated <https://www.chartjs.org/docs/latest/developers/updates.html>`_

        :param point: Optional. The point to be removed on the series. If none the last one will be removed
        :param series_names: Optional. The series name
        """
        point = JsUtils.jsConvertData(point, None)
        if series_names is None:
            if point is None:
                return JsObjects.JsVoid('''
%(varName)s.data.labels.pop(); %(varName)s.data.datasets.forEach(function(dataset){dataset.data.pop()})''' % {
                  'varName': self.varName})

            return JsObjects.JsVoid('''var index = %(varName)s.data.labels.indexOf(%(point)s);
if(index >= 0){
  %(varName)s.data.labels.splice(index, 1);
  %(varName)s.data.datasets.forEach(function(dataset){ dataset.data.splice(index, 1)})
} ''' % {'varName': self.varName, 'point': point})

        series_names = JsUtils.jsConvertData(series_names, None)
        return JsObjects.JsVoid('''var index = %(varName)s.data.labels.indexOf(%(point)s);
if(index >= 0){
  %(varName)s.data.datasets.forEach(function(dataset){
    if (%(seriesNames)s.includes(dataset.label)){dataset.data[index] = null}})}''' % {
          'varName': self.varName, 'point': point, 'seriesNames': series_names})

    def empty(self):
        """Empty a chartJs component. Namely it will set empty lists for the dataSets and the labels.
        This will also update the chart to trigger the animation.
        """
        return JsObjects.JsVoid(
            "%(varName)s.data.datasets = []; %(varName)s.data.labels = []; %(varName)s.update()" % {
                "varName": self.varName})

    def data(self, datasets: dict, options: dict = None, profile: types.PROFILE_TYPE = None):
        """Update all the data in the chart.

        `Updated <https://www.chartjs.org/docs/latest/developers/updates.html>`_

        :param datasets: The full datasets object expected by ChartJs
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        return self.component.build(
            JsUtils.jsWrap("Object.assign(%s, {python: true})" % JsUtils.jsConvertData(datasets, None)), options,
            profile)

    def load(self, name: str, points: Union[List[dict], primitives.JsDataModel], options: dict = None, color: str = ""):
        """Loads new series on an existing chart.
        existing x-axis will not be changed and they will be used to add the points.

        Note: Do not forget to trigger an update on the chart once all your transformations are done.

        `Updated <https://www.chartjs.org/docs/latest/developers/updates.html>`_

        :param name: The series name
        :param points: The list of points ({x: , y: }) to be added to the chart
        :param options: Optional. Specific Python options available for this series
        :param color: Optional. The color code for the chart
        """
        name = JsUtils.jsConvertData(name, None)
        points = JsUtils.jsConvertData(points, None)
        current_options = dict(self.component.options.commons)
        current_options.update(options or {})
        options = self.component.options.config_js({"commons": current_options})
        return JsObjects.JsVoid('''var values = []; var index= -1; var %(htmlCode)s_options = %(options)s;
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
        """Remove series from the chart.

        Note: Do not forget to trigger an update on the chart once all your transformations are done.

        `Updated <https://www.chartjs.org/docs/latest/developers/updates.html>`_

        :param names: Optional. The series names to be removed from the chart. If none all series will be removed
        """
        if names is None:
            return JsObjects.JsVoid(
                '%(varName)s.data.labels = []; %(varName)s.data.datasets = []' % {'varName': self.varName})

        names = JsUtils.jsConvertData(names, None)
        return JsObjects.JsVoid('''
var indices = []; %(varName)s.data.datasets.forEach(function(d, i){ if(%(names)s.includes(d.label)){ indices.push(i)}});
indices.sort().reverse().forEach(function(i){%(varName)s.data.datasets.splice(i, 1)})
''' % {'varName': self.varName, 'names': names})

    @property
    def label(self):
        """Return the series label"""
        return JsObjects.JsString.JsString("%s.data.labels[activePoints[0]['_index']]" % self.varName, is_py_data=False)

    @property
    def content(self):
        """ """
        return JsObjects.JsObject.JsObject(
            "%s.data.datasets[0].data[activePoints[0]['_index']]" % self.varName, is_py_data=False)

    @property
    def value(self):
        """ """
        return JsObjects.JsString.JsString(
            "{%(htmlCode)s: {point: %(chart)s.data.datasets[0].data[activePoints[0]['_index']], label: %(chart)s.data.labels[activePoints[0]['_index']]}}" % {
                'htmlCode': self.component.htmlCode, "chart": self.varName}, is_py_data=False)

    def update(self, config: Union[dict, primitives.JsDataModel] = None, mode: str = None):
        """Triggers an update of the chart. This can be safely called after updating the data object.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_
        `ChartJs Updates <https://www.chartjs.org/docs/latest/developers/updates.html>`_

        :param config: Optional. A config object can be provided with additional configuration for the process
        :param mode. Optional. Triggers an update of the chart. This can be safely called after updating the data object
        """
        if config is None:
            return JsObjects.JsObject.JsObject("%s.update()" % self.toStr())

        config = JsUtils.convertOptions(config, self.component.js_code)
        return JsUtils.jsWrap('''%s;%s.update(%s)''' % (config, self.toStr(), JsUtils.jsConvertData(mode, None)))

    def hide(self, dataset_index: int, data_index: int = None):
        """If dataIndex is not specified, sets the visibility for the given dataset to false.
        Updates the chart and animates the dataset with 'hide' mode.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :param dataset_index:
        :param data_index:
        """
        if data_index is not None:
            return JsObjects.JsObject.JsObject("%s.hide(%s, %s)" % (self.toStr(), dataset_index, data_index))

        return JsObjects.JsObject.JsObject("%s.hide(%s)" % (self.toStr(), dataset_index))

    def show(self, dataset_index: int, data_index: int = None) -> JsObjects.JsObject.JsObject:
        """If dataIndex is not specified, sets the visibility for the given dataset to true.
        Updates the chart and animates the dataset with 'show' mode.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :param dataset_index:
        :param data_index:
        """
        if data_index is not None:
            return JsObjects.JsObject.JsObject("%s.show(%s, %s)" % (self.toStr(), dataset_index, data_index))

        return JsObjects.JsObject.JsObject("%s.show(%s)" % (self.toStr(), dataset_index))

    def reset(self):
        """Reset the chart to it's state before the initial animation.
        A new animation can then be triggered using update.

        Usage::

          myLineChart.reset()

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_
        """
        return JsObjects.JsObject.JsObject("%s.reset()" % self.toStr())

    def stop(self):
        """Use this to stop any current animation loop. This will pause the chart during any current animation frame.

        Usage::

          chart.stop()

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :return: 'this' for chainability
        """
        self._js.append("stop()")
        return self

    def resize(self):
        """Use this to manually resize the canvas element.

        This is run each time the canvas container is resized, but you can call this method manually if you change the size
        of the canvas nodes container element.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :return: 'this' for chainability
        """
        self._js.append("%s.resize()" % self.toStr())
        return self

    def clear(self):
        """Will clear the chart canvas. Used extensively internally between animation frames, but you might find it
        useful.

        Usage::

          chart.clear()

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :return: 'this' for chainability
        """
        return JsObjects.JsVoid("%s.clear()" % self.toStr())

    def toBase64Image(self, type: str = None, quality: int = None):
        """This returns a base 64 encoded string of the chart in it's current state.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :param type:
        :param quality:
        :return: png data url of the image on the canvas
        """
        if type is not None:
            if quality is not None:
                return JsObjects.JsObject.JsObject("%s.toBase64Image(%s, %s)" % (
                    self.toStr(), JsUtils.jsConvertData(type, None), quality))

            return JsObjects.JsObject.JsObject(
                "%s.toBase64Image(%s)" % (self.toStr(), JsUtils.jsConvertData(type, None)))

        return JsObjects.JsObject.JsObject("%s.toBase64Image()" % self.toStr())

    def generateLegend(self):
        """Returns an HTML string of a legend for that chart. The legend is generated from the legendCallback in the
        options.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :return: HTML string of a legend for this chart
        """
        return JsObjects.JsObject.JsObject("%s.generateLegend()" % self.toStr())

    def getElementAtEvent(self, event: Union[str, primitives.JsDataModel]):
        """Calling getElementAtEvent(event) on your Chart instance passing an argument of an event, or jQuery event,
        will return the single element at the event position

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :param event: The javascript event

        :return: the first element at the event point.
        """
        event = JsUtils.jsConvertData(event, None)
        return JsObjects.JsObject.JsObject("%s.getElementAtEvent(%s)" % (self.toStr(), event))

    def getDatasetAtEvent(self, event: Union[str, primitives.JsDataModel]):
        """Looks for the element under the event point, then returns all elements from that dataset.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :param event: The javascript event

        :return: an array of elements
        """
        event = JsUtils.jsConvertData(event, None)
        return JsObjects.JsArray.JsArray("%s.getDatasetAtEvent(%s)" % (self.toStr(), event))

    def getDatasetMeta(self, index: int):
        """Looks for the dataset that matches the current index and returns that metadata.

        Usage::

          chart.getDatasetMeta(0)

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :param index: The index value of the series
        """
        return JsObjects.JsObject.JsObject("%s.getDatasetMeta(%s)" % (self.toStr(), index))

    def render(self, config: Union[dict, primitives.JsDataModel] = None):
        """Triggers a redraw of all chart elements. Note, this does not update elements for new data.
        Use .update() in that case.

        Usage::

          chart.render({duration: 800, lazy: false, easing: 'easeOutBounce'})

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :param config: Optional. A python dictionary as config object
        """
        if config is None:
            return JsObjects.JsObject.JsObject("%s.render()" % self.toStr())

        config = JsUtils.jsConvertData(config, None)
        return JsObjects.JsObject.JsObject("%s.render(%s)" % (self.toStr(), config))

    def destroy(self):
        """Use this to destroy any chart instances that are created.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_
        """
        return JsObjects.JsObject.JsObject("%s.destroy()" % self.toStr())

    def download(self, filename: str = None, options: dict = None, *args, **kwargs):
        """Download data in a CSV file.

        :param filename: filename
        :param options: export options
        """
        filename = filename or "%s.csv" % self.component.html_code
        return r'''
var data, filename, link; var columnDelimiter = ",";
if (["scatter", "bubble"].includes(%(chartId)s.config.type)){
  var labels = []; var dims = [];
  for (var i = 0; i < %(chartId)s.data.labels.length; i++) {
    labels.push(%(chartId)s.data.labels[i] + columnDelimiter + columnDelimiter);
    dims.push("x"+ columnDelimiter + "y"+ columnDelimiter + "r");
  }
  var csv = ["Series" + columnDelimiter + labels.join(columnDelimiter)];
  csv.push("" + columnDelimiter + dims.join(columnDelimiter));
  for (var i = 0; i < %(chartId)s.data.datasets.length; i++) {
    var series = [];
    for (var j=0; j < %(chartId)s.data.datasets[i].data.length; j++){ 
      var point = %(chartId)s.data.datasets[i].data[j];
      series.push(point.x + columnDelimiter + point.y + columnDelimiter + point.r)
    };
    csv.push(%(chartId)s.data.datasets[i].label + columnDelimiter + series.join(columnDelimiter))}
} else{
  var csv = ["Series" + columnDelimiter + %(chartId)s.data.labels.join(columnDelimiter)];
  for (var i = 0; i < %(chartId)s.data.datasets.length; i++) {
    csv.push(%(chartId)s.data.datasets[i].label + columnDelimiter + %(chartId)s.data.datasets[i].data.join(columnDelimiter))}
}
var csvContent = csv.join("\n"); filename = '%(filename)s';
if (!csvContent.match(/^data:text\/csv/i)) {csvContent = 'data:text/csv;charset=utf-8,' + csvContent}
data = encodeURI(csvContent); link = document.createElement('a');
link.setAttribute('href', data); link.setAttribute('download', filename);
document.body.appendChild(link); link.click(); document.body.removeChild(link);
''' % {"chartId": self.component.js_code, "filename": filename}

    def capture(self):
        """ """
        return '''navigator.clipboard.write([
  new ClipboardItem({1'0image/png': new Blob([atob(decodeURIComponent(%s))],  {type: 'image/png'})})])
''' % self.toBase64Image('image/png', 1)

    def clearData(self):
        """ """
        return self.clear()

    def setDatasetVisibility(self, dataset_index: int, visibility: bool):
        """Sets the visibility for a given dataset. This can be used to build a chart legend in HTML.
        During click on one of the HTML items, you can call setDatasetVisibility to change the appropriate dataset.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :param dataset_index:
        :param visibility:
        """
        return JsObjects.JsObject.JsObject("%s.setDatasetVisibility(%s, %s)" % (
            self.toStr(), JsUtils.jsConvertData(dataset_index, None), JsUtils.jsConvertData(visibility, None)))

    def toggleDataVisibility(self, dataset_index: int):
        """Toggles the visibility of an item in all datasets. A dataset needs to explicitly support this feature
        for it to have an effect. From internal chart types, doughnut / pie, polar area, and bar use this.

        `ChartJs API <https://www.chartjs.org/docs/latest/developers/api.html>`_

        :param dataset_index:
        """
        return JsObjects.JsObject.JsObject("%s.toggleDataVisibility(%s)" % (self.toStr(), dataset_index))

    def setTitle(self, value: primitives.JsDataModel):
        """

        :param value:
        :return:
        """
        return JsObjects.JsString.JsString.get("%s.options.plugins.title.text = %s" % (
            self.component.js_code, JsUtils.jsConvertData(value, None)))

    def toStr(self):
        """Javascript representation.

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

        :param flag: A flag to activate the start to zero of the series
        """
        self._attrs["beginAtZero"] = JsUtils.jsConvertData(flag, None)
        return self

    def display(self, flag: Union[bool, primitives.JsDataModel]):
        """

        :param flag: Show the series
        """
        self._attrs["display"] = JsUtils.jsConvertData(flag, None)
        return self


class ChartJsOptGridLines(DataAttrs):

    def display(self, flag: Union[bool, primitives.JsDataModel] = False):
        """If false, do not display grid lines for this axis.

        :param flag: Optional
        """
        self._attrs["display"] = JsUtils.jsConvertData(flag, None)
        return self

    def circular(self, flag: Union[bool, primitives.JsDataModel] = False):
        """If true, gridlines are circular (on radar chart only).

        :param flag: Optional
        """
        self._attrs["circular"] = JsUtils.jsConvertData(flag, None)
        return self

    def color(self, colors: Union[str, primitives.JsDataModel] = ""):
        """The color of the grid lines.
        If specified as an array, the first color applies to the first grid line,
        the second to the second grid line and so on.

        :param colors: Optional. The color code
        """
        self._attrs["color"] = JsUtils.jsConvertData(colors, None)
        return self

    def borderDash(self, narray: Union[list, primitives.JsDataModel]):
        """

        :param narray:
        """
        self._attrs["borderDash"] = JsUtils.jsConvertData(narray, None)
        return self

    def borderDashOffset(self, n: Union[float, primitives.JsDataModel] = 0.0):
        """Offset for line dashes.

        :param n: Optional. The dash offset number
        """
        self._attrs["borderDashOffset"] = JsUtils.jsConvertData(n, None)
        return self

    def lineWidth(self, num: Union[float, primitives.JsDataModel]):
        """Stroke width of grid lines.

        :param num: The line width
        """
        self._attrs["lineWidth"] = JsUtils.jsConvertData(num, None)
        return self

    def drawBorder(self, flag: Union[bool, primitives.JsDataModel] = True):
        """If true, draw border at the edge between the axis and the chart area.

        :param flag: Optional. Flag to draw the border
        """
        self._attrs["drawBorder"] = JsUtils.jsConvertData(flag, None)
        return self

    def drawOnChartArea(self, flag: Union[bool, primitives.JsDataModel] = True):
        """If true, draw lines on the chart area inside the axis lines.
        This is useful when there are multiple axes and you need to control which grid lines are drawn.

        :param flag: Optional.
        """
        self._attrs["drawOnChartArea"] = JsUtils.jsConvertData(flag, None)
        return self

    def drawTicks(self, flag: Union[bool, primitives.JsDataModel] = True):
        """If true, draw lines beside the ticks in the axis area beside the chart.

        :param flag: Optional.
        """
        self._attrs["drawTicks"] = JsUtils.jsConvertData(flag, None)
        return self

    def tickMarkLength(self, n: Union[int, primitives.JsDataModel] = 10):
        """Length in pixels that the grid lines will draw into the axis area.

        :param n: Optional.
        """
        self._attrs["tickMarkLength"] = JsUtils.jsConvertData(n, None)
        return self

    def zeroLineWidth(self, n: Union[int, primitives.JsDataModel] = 1):
        """Stroke width of the grid line for the first index (index 0).

        :param n: Optional.
        """
        self._attrs["zeroLineWidth"] = JsUtils.jsConvertData(n, None)
        return self

    def zeroLineColor(self, color: Union[str, primitives.JsDataModel] = "rgba(0, 0, 0, 0.25)"):
        """Stroke color of the grid line for the first index (index 0).

        :param color: Optional. The RGBA color code.
        """
        self._attrs["zeroLineColor"] = JsUtils.jsConvertData(color, None)
        return self

    def zeroLineBorderDash(self, narray: Union[list, primitives.JsDataModel]):
        """Length and spacing of dashes of the grid line for the first index (index 0).

        :param narray:
        """
        self._attrs["zeroLineBorderDash"] = JsUtils.jsConvertData(narray, None)
        return self

    def zeroLineBorderDashOffset(self, n: Union[float, primitives.JsDataModel] = 0.0):
        """Offset for line dashes of the grid line for the first index (index 0).

        :param n: Optional.
        """
        self._attrs["zeroLineBorderDashOffset"] = JsUtils.jsConvertData(n, None)
        return self

    def offsetGridLines(self, flag: Union[bool, primitives.JsDataModel] = True):
        """If true, the bars for a particular data point fall between the grid lines.
        The grid line will move to the left by one half of the tick interval, which is the space between the grid lines.
        If false, the grid line will go right down the middle of the bars.
        This is set to true for a category scale in a bar chart while false for other scales or chart types by default.

        :param flag: Optional.
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
        """ """
        if "gridLines" not in self._attrs:
            self._attrs["gridLines"] = ChartJsOptGridLines(self.page)
        return self._attrs["gridLines"]

    def stacked(self, flag: Union[bool, primitives.JsDataModel] = False):
        pass


class ChartJsOptScaleBar(ChartJsOptScale):

    def barPercentage(self, n: Union[float, primitives.JsDataModel] = 0.9):
        """Percent (0-1) of the available width each bar should be within the category width.
        1.0 will take the whole category width and put the bars right next to each other.

        :param n: Optional.
        """
        if n > 1:
            raise ValueError("n cannot exceed 1")

        self._attrs["barPercentage"] = JsUtils.jsConvertData(n, None)
        return self

    def categoryPercentage(self, n: Union[float, primitives.JsDataModel] = 0.8):
        """Percent (0-1) of the available width each category should be within the sample width.

        :param n: Optional.
        """
        self._attrs["categoryPercentage"] = JsUtils.jsConvertData(n, None)
        return self

    def barThickness(self, width: Union[str, primitives.JsDataModel] = "flex"):
        """Manually set width of each bar in pixels.

        If set to 'flex', it computes "optimal" sample widths that globally arrange bars side by side.
        If not set (default), bars are equally sized based on the smallest interval.

        :param width: Optional.
        """
        self._attrs["barThickness"] = JsUtils.jsConvertData(width, None)
        return self

    def maxBarThickness(self, width: Union[float, primitives.JsDataModel]):
        """Set this to ensure that bars are not sized thicker than this.

        :param width: A float
        """
        self._attrs["barThickness"] = JsUtils.jsConvertData(width, None)
        return self

    def minBarLength(self, width: Union[float, primitives.JsDataModel]):
        """

        :param width:
        """
        self._attrs["minBarLength"] = JsUtils.jsConvertData(width, None)
        return self


class ChartJsOptTooltip(DataAttrs):
    pass


class ChartJsOptLabels(DataAttrs):

    @property
    def fontColor(self):
        """
        `ChartJs Fonts <https://www.chartjs.org/docs/latest/general/fonts.html>`_
         """
        return self._attrs["fontColor"]

    @fontColor.setter
    def fontColor(self, val):
        self._attrs["fontColor"] = val


class ChartJsOptPadding(DataAttrs):
    @property
    def left(self):
        """
        `ChartJs Fonts <https://www.chartjs.org/docs/latest/general/fonts.html>`_
        """
        return self._attrs["left"]

    @left.setter
    def left(self, val):
        self._attrs["left"] = val

    @property
    def right(self):
        """
        `ChartJs layout <https://www.chartjs.org/docs/latest/configuration/layout.html>`_
        """
        return self._attrs["right"]

    @right.setter
    def right(self, val):
        self._attrs["right"] = val

    @property
    def top(self):
        """
        `ChartJs layout <https://www.chartjs.org/docs/latest/configuration/layout.html>`_
        """
        return self._attrs["top"]

    @top.setter
    def top(self, val):
        self._attrs["top"] = val

    @property
    def bottom(self):
        """
        `ChartJs layout <https://www.chartjs.org/docs/latest/configuration/layout.html>`_
        """
        return self._attrs["bottom"]

    @bottom.setter
    def bottom(self, val):
        self._attrs["bottom"] = val


class OptionsLegend(DataAttrs):
    def display(self, flag: Union[bool, primitives.JsDataModel] = True):
        """Is the legend shown.

        `ChartJs layout <https://www.chartjs.org/docs/latest/configuration/legend.html>`_

        :param flag: Optional.
        """
        self._attrs["display"] = JsUtils.jsConvertData(flag, None)
        return self

    def position(self, location: Union[str, primitives.JsDataModel] = "top"):
        """Position of the legend.

        :param location: Optional.
        """
        self._attrs["position"] = JsUtils.jsConvertData(location, None)
        return self

    def fullWidth(self, flag: Union[bool, primitives.JsDataModel] = True):
        """

        :param flag: Optional.
        """

    def onClick(self, callback: Union[List[Union[str, primitives.JsDataModel]], str],
                profile: Optional[Union[dict, bool]] = False):
        """A callback that is called when a click event is registered on a label item.

        :param callback: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        self._attrs["onClick"] = JsUtils.jsConvertFncs(callback, profile=profile)
        return self

    def onHover(self, callback: Union[List[Union[str, primitives.JsDataModel]], str],
                profile: Optional[Union[dict, bool]] = False):
        """A callback that is called when a 'mousemove' event is registered on top of a label item.

        :param callback: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        self._attrs["onHover"] = JsUtils.jsConvertFncs(callback, profile=profile)
        return self

    def onLeave(self, callback: Union[List[Union[str, primitives.JsDataModel]], str],
                profile: Optional[Union[dict, bool]] = False):
        """

        :param callback: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        self._attrs["onLeave"] = JsUtils.jsConvertFncs(callback, profile=profile)
        return self

    def reverse(self, flag: Union[bool, primitives.JsDataModel] = False):
        """Legend will show datasets in reverse order.

        :param flag: Boolean. Optional
        """
        self._attrs["reverse"] = JsUtils.jsConvertData(flag, None)
        return self

    @property
    def labels(self) -> ChartJsOptLabels:
        """ """
        if 'labels' not in self._attrs:
            self._attrs["labels"] = ChartJsOptLabels(self.page)
        return self._attrs["labels"]


class OptionsTitle(DataAttrs):
    @property
    def display(self):
        """
        `ChartJs title <https://www.chartjs.org/docs/latest/configuration/title.html>`_
        """
        return self._attrs["display"]

    @display.setter
    def display(self, val):
        self._attrs["display"] = val

    @property
    def text(self):
        """ """
        return self._attrs["text"]

    @text.setter
    def text(self, val):
        self._attrs["text"] = val

    @property
    def position(self):
        """ """
        return self._attrs["position"]

    @position.setter
    def position(self, val):
        self._attrs["position"] = val

    @property
    def fontSize(self):
        """ """
        return self._attrs["fontSize"]

    @fontSize.setter
    def fontSize(self, val):
        self._attrs["fontSize"] = val

    @property
    def fontFamily(self):
        """ """
        return self._attrs["fontFamily"]

    @fontFamily.setter
    def fontFamily(self, val):
        self._attrs["fontFamily"] = val

    @property
    def fontColor(self):
        """ """
        return self._attrs["fontColor"]

    @fontColor.setter
    def fontColor(self, val):
        self._attrs["fontColor"] = val

    @property
    def fontStyle(self):
        """ """
        return self._attrs["fontStyle"]

    @fontStyle.setter
    def fontStyle(self, val):
        self._attrs["fontStyle"] = val

    @property
    def padding(self):
        """ """
        return self._attrs["padding"]

    @padding.setter
    def padding(self, val):
        self._attrs["padding"] = val

    @property
    def lineHeight(self):
        """ """
        return self._attrs["lineHeight"]

    @lineHeight.setter
    def lineHeight(self, val):
        self._attrs["lineHeight"] = val


class OptionsLabels(DataAttrs):

    @property
    def display(self):
        """Display the labels.

        `ChartJs labels <https://chartjs-chart-treemap.pages.dev/usage.html#labels>`_
        """
        return self._attrs["display"]

    @display.setter
    def display(self, val):
        self._attrs["display"] = val

    @property
    def align(self):
        """Align property specifies the text horizontal alignment used when drawing the label.

        `ChartJs labels <https://chartjs-chart-treemap.pages.dev/usage.html#labels>`_
        """
        return self._attrs["align"]

    @align.setter
    def align(self, text: str):
        self._attrs["align"] = text

    @property
    def color(self):
        """The label align position.

        `ChartJs labels <https://chartjs-chart-treemap.pages.dev/usage.html#labels>`_
        """
        return self._attrs["color"]

    @color.setter
    def color(self, text: str):
        self._attrs["color"] = text

    @property
    def hoverColor(self):
        """

        `ChartJs labels <https://chartjs-chart-treemap.pages.dev/usage.html#labels>`_
        """
        return self._attrs["hoverColor"]

    @hoverColor.setter
    def hoverColor(self, text: str):
        self._attrs["hoverColor"] = text

    @property
    def padding(self):
        """
        `ChartJs labels <https://chartjs-chart-treemap.pages.dev/usage.html#labels>`_
        """
        return self._attrs["padding"]

    @padding.setter
    def padding(self, num: str):
        self._attrs["padding"] = num

    @property
    def position(self):
        """The position property specifies the text vertical alignment used when drawing the label.

        `ChartJs labels <https://chartjs-chart-treemap.pages.dev/usage.html#labels>`_
        """
        return self._attrs["position"]

    @position.setter
    def position(self, text: str):
        self._attrs["position"] = text

    def formatter_map(self, labels):
        self.custom("formatter", JsUtils.jsWrap(
            "function(ctx){let treeLabels = %(labels)s; return treeLabels[ctx.dataIndex]}" % {
                "labels": JsUtils.jsConvertData(labels, None)
            }))

    @property
    def formatter(self):
        """Data values are converted to string.
        If values are grouped, the value of the group and the value (as string) are shown.

        `ChartJs labels <https://chartjs-chart-treemap.pages.dev/usage.html#labels>`_
        """
        return self._attrs["formatter"]

    @formatter.setter
    def formatter(self, text: str):
        self.set_val(text)


class Options(DataAttrs):

    def __init__(self, page, attrs=None, options=None):
        super(Options, self).__init__(page, attrs, options)

    def title(self):
        """ """
        if self._attrs.get("title") is None:
            self._attrs['title'] = OptionsTitle(self.page)
        return self._attrs['title']


class DataSet(DataAttrs):

    @property
    def backgroundColor(self):
        """Arc background color.

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
        `ChartJs line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("backgroundColor")

    @backgroundColor.setter
    def backgroundColor(self, color: str):
        self.set_val(color)

    @property
    def borderColor(self):
        """Arc border color.

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
        """
        return self._attrs.get("borderColor")

    @borderColor.setter
    def borderColor(self, color: str):
        self.set_val(color)

    @property
    def borderWidth(self):
        """Arc border width (in pixels).

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
        """
        return self._attrs.get("borderWidth")

    @borderWidth.setter
    def borderWidth(self, val: int):
        self._attrs["borderWidth"] = val

    @property
    def fillOpacity(self):
        """Convert the hexadecimal color to the corresponding RGB one with the opacity.

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
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

    @property
    def fontColor(self):
        """

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
        `ChartJs line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("fontColor")

    @fontColor.setter
    def fontColor(self, color: str):
        self.set_val(color)

    @property
    def fontFamily(self):
        """

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
        `ChartJs line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("fontFamily")

    @fontFamily.setter
    def fontFamily(self, value: str):
        self.set_val(value)

    def set_style(self, background_color: str = None, fill_opacity: int = None, border_width: int = None,
                  border_color: str = None):
        """

        :param background_color: Optional. The background color code
        :param fill_opacity: Optional. The opacity factor
        :param border_width: Optional. The border width
        :param border_color: Optional. The border color code
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

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
        """
        return self._attrs.get("borderAlign")

    @borderAlign.setter
    def borderAlign(self, val):
        self._attrs["borderAlign"] = val

    @property
    def data(self):
        """

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
        """
        return self._attrs["data"]

    @data.setter
    def data(self, val):
        self._attrs["data"] = val

    @property
    def hoverBackgroundColor(self):
        """Arc background color when hovered.

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
        """
        return self._attrs.get("hoverBackgroundColor")

    @hoverBackgroundColor.setter
    def hoverBackgroundColor(self, val):
        self._attrs["hoverBackgroundColor"] = val

    @property
    def hoverBorderColor(self):
        """Arc border color when hovered.

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
        """
        return self._attrs.get("hoverBorderColor")

    @hoverBorderColor.setter
    def hoverBorderColor(self, val):
        self._attrs["hoverBorderColor"] = val

    @property
    def hoverBorderWidth(self):
        """Arc border width when hovered (in pixels).

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
        """
        return self._attrs.get("hoverBorderWidth")

    @hoverBorderWidth.setter
    def hoverBorderWidth(self, val):
        self._attrs["hoverBorderWidth"] = val

    @property
    def weight(self):
        """The relative thickness of the dataset.

        Providing a value for weight will cause the pie or doughnut dataset to be drawn with a thickness relative to the
        sum of all the dataset weight values.

        `ChartJs doughnut <https://www.chartjs.org/docs/latest/charts/doughnut.html>`_
        """
        return self._attrs.get("weight")

    @weight.setter
    def weight(self, val):
        self._attrs["weight"] = val

    def set_style(self, background_colors: list = None, fill_opacity: float = None, border_width: int = None,
                  border_colors: list = None):
        """

        :param background_colors: Optional. The background colors
        :param fill_opacity: Optional. The opacity factor
        :param border_width: Optional. The border width in pixel
        :param border_colors: Optional. The border colors
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
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("borderCapStyle")

    @borderCapStyle.setter
    def borderCapStyle(self, val):
        self._attrs["borderCapStyle"] = val

    @property
    def borderDash(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("borderDash")

    @borderDash.setter
    def borderDash(self, val):
        self._attrs["borderDash"] = val

    @property
    def borderDashOffset(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("borderDashOffset")

    @borderDashOffset.setter
    def borderDashOffset(self, val):
        self._attrs["borderDashOffset"] = val

    @property
    def borderJoinStyle(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("borderJoinStyle")

    @borderJoinStyle.setter
    def borderJoinStyle(self, val):
        self._attrs["borderJoinStyle"] = val

    @property
    def cubicInterpolationMode(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("cubicInterpolationMode")

    @cubicInterpolationMode.setter
    def cubicInterpolationMode(self, val):
        self._attrs["cubicInterpolationMode"] = val

    @property
    def clip(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("clip")

    @clip.setter
    def clip(self, val):
        self._attrs["clip"] = val

    @property
    def fill(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("fill")

    @fill.setter
    def fill(self, val):
        self._attrs["fill"] = val

    @property
    def hoverBackgroundColor(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("hoverBackgroundColor")

    @hoverBackgroundColor.setter
    def hoverBackgroundColor(self, val: str):
        self._attrs["hoverBackgroundColor"] = val

    @property
    def hoverBorderCapStyle(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("hoverBorderCapStyle")

    @hoverBorderCapStyle.setter
    def hoverBorderCapStyle(self, val):
        self._attrs["hoverBorderCapStyle"] = val

    @property
    def hoverBorderColor(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("hoverBorderColor")

    @hoverBorderColor.setter
    def hoverBorderColor(self, val: str):
        self._attrs["hoverBorderColor"] = val

    @property
    def hoverBorderDash(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("hoverBorderDash")

    @hoverBorderDash.setter
    def hoverBorderDash(self, val):
        self._attrs["hoverBorderDash"] = val

    @property
    def hoverBorderDashOffset(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("hoverBorderDashOffset")

    @hoverBorderDashOffset.setter
    def hoverBorderDashOffset(self, val):
        self._attrs["hoverBorderDashOffset"] = val

    @property
    def hoverBorderJoinStyle(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("hoverBorderJoinStyle")

    @hoverBorderJoinStyle.setter
    def hoverBorderJoinStyle(self, val):
        self._attrs["hoverBorderJoinStyle"] = val

    @property
    def hoverBorderWidth(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("hoverBorderWidth")

    @hoverBorderWidth.setter
    def hoverBorderWidth(self, val: int):
        self._attrs["hoverBorderWidth"] = val

    @property
    def label(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("label")

    @label.setter
    def label(self, val: str):
        self._attrs["label"] = val

    @property
    def lineTension(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("lineTension")

    @lineTension.setter
    def lineTension(self, val: float):
        self._attrs["lineTension"] = val

    @property
    def order(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("order")

    @order.setter
    def order(self, val):
        self._attrs["order"] = val

    @property
    def pointBackgroundColor(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("pointBackgroundColor")

    @pointBackgroundColor.setter
    def pointBackgroundColor(self, val: str):
        self._attrs["pointBackgroundColor"] = val

    @property
    def pointBorderColor(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("pointBorderColor")

    @pointBorderColor.setter
    def pointBorderColor(self, val: str):
        self._attrs["pointBorderColor"] = val

    @property
    def pointBorderWidth(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("pointBorderWidth")

    @pointBorderWidth.setter
    def pointBorderWidth(self, val):
        self._attrs["pointBorderWidth"] = val

    @property
    def pointHitRadius(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("pointHitRadius")

    @pointHitRadius.setter
    def pointHitRadius(self, val):
        self._attrs["pointHitRadius"] = val

    @property
    def pointHoverBackgroundColor(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("pointHoverBackgroundColor")

    @pointHoverBackgroundColor.setter
    def pointHoverBackgroundColor(self, val):
        self._attrs["pointHoverBackgroundColor"] = val

    @property
    def pointHoverBorderColor(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("pointHoverBorderColor")

    @pointHoverBorderColor.setter
    def pointHoverBorderColor(self, val):
        self._attrs["pointHoverBorderColor"] = val

    @property
    def pointHoverBorderWidth(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("pointHoverBorderWidth")

    @pointHoverBorderWidth.setter
    def pointHoverBorderWidth(self, val):
        self._attrs["pointHoverBorderWidth"] = val

    @property
    def pointHoverRadius(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("pointHoverRadius")

    @pointHoverRadius.setter
    def pointHoverRadius(self, val):
        self._attrs["pointHoverRadius"] = val

    @property
    def pointRadius(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
        """
        return self._attrs.get("pointRadius")

    @pointRadius.setter
    def pointRadius(self, val):
        self._attrs["pointRadius"] = val

    @property
    def pointRotation(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
            """
        return self._attrs.get("pointRotation")

    @pointRotation.setter
    def pointRotation(self, val):
        self._attrs["pointRotation"] = val

    @property
    def pointStyle(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
            """
        return self._attrs.get("pointStyle")

    @pointStyle.setter
    def pointStyle(self, val):
        self._attrs["pointStyle"] = val

    @property
    def showLine(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
            """
        return self._attrs.get("showLine")

    @showLine.setter
    def showLine(self, val):
        self._attrs["showLine"] = val

    @property
    def spanGaps(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
            """
        return self._attrs.get("spanGaps")

    @spanGaps.setter
    def spanGaps(self, val):
        self._attrs["spanGaps"] = val

    @property
    def steppedLine(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
            """
        return self._attrs.get("steppedLine")

    @steppedLine.setter
    def steppedLine(self, val):
        self._attrs["steppedLine"] = val

    @property
    def xAxisID(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
            """
        return self._attrs.get("xAxisID")

    @xAxisID.setter
    def xAxisID(self, val):
        self._attrs["xAxisID"] = val

    @property
    def yAxisID(self):
        """
        `Line <https://www.chartjs.org/docs/latest/charts/line.html>`_
            """
        return self._attrs.get("yAxisID")

    @yAxisID.setter
    def yAxisID(self, val):
        self._attrs["yAxisID"] = val

    def set_style(self, background_color: str = None, fill_opacity: float = None, border_width: int = None,
                  border_color: str = None):
        """

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
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("barPercentage")

    @barPercentage.setter
    def barPercentage(self, val):
        self._attrs["barPercentage"] = val

    @property
    def barThickness(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("barThickness")

    @barThickness.setter
    def barThickness(self, val):
        self._attrs["barThickness"] = val

    @property
    def maxBarThickness(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("maxBarThickness")

    @maxBarThickness.setter
    def maxBarThickness(self, val):
        self._attrs["maxBarThickness"] = val

    @property
    def minBarLength(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("minBarLength")

    @minBarLength.setter
    def minBarLength(self, val):
        self._attrs["minBarLength"] = val

    @property
    def borderSkipped(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("borderSkipped")

    @borderSkipped.setter
    def borderSkipped(self, val):
        self._attrs["borderSkipped"] = val

    @property
    def data(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs["data"]

    @data.setter
    def data(self, val):
        self._attrs["data"] = val

    @property
    def hoverBackgroundColor(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("hoverBackgroundColor")

    @hoverBackgroundColor.setter
    def hoverBackgroundColor(self, val):
        self._attrs["hoverBackgroundColor"] = val

    @property
    def hoverBorderColor(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("hoverBorderColor")

    @hoverBorderColor.setter
    def hoverBorderColor(self, val):
        self._attrs["hoverBorderColor"] = val

    @property
    def hoverBorderWidth(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("hoverBorderWidth")

    @hoverBorderWidth.setter
    def hoverBorderWidth(self, val):
        self._attrs["hoverBorderWidth"] = val

    @property
    def label(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs["label"]

    @label.setter
    def label(self, val):
        self._attrs["label"] = val

    @property
    def order(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("order")

    @order.setter
    def order(self, val):
        self._attrs["order"] = val

    @property
    def xAxisID(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("xAxisID")

    @xAxisID.setter
    def xAxisID(self, val):
        self._attrs["xAxisID"] = val

    @property
    def yAxisID(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("yAxisID")

    @yAxisID.setter
    def yAxisID(self, val):
        self._attrs["yAxisID"] = val


class DataSetPolar(DataSet):

    @property
    def borderAlign(self):
        """
        `Bar <https://www.chartjs.org/docs/latest/charts/bar.html>`_
        """
        return self._attrs.get("borderAlign")

    @borderAlign.setter
    def borderAlign(self, val):
        self._attrs["borderAlign"] = val

    @property
    def data(self):
        """
        `Polas <https://www.chartjs.org/docs/latest/charts/polar.html>`_
        """
        return self._attrs["data"]

    @data.setter
    def data(self, val):
        self._attrs["data"] = val

    @property
    def hoverBackgroundColor(self):
        """
        `Polas <https://www.chartjs.org/docs/latest/charts/polar.html>`_
        """
        return self._attrs.get("hoverBackgroundColor")

    @hoverBackgroundColor.setter
    def hoverBackgroundColor(self, val):
        self._attrs["hoverBackgroundColor"] = val

    @property
    def hoverBorderColor(self):
        """
        `Polas <https://www.chartjs.org/docs/latest/charts/polar.html>`_
        """
        return self._attrs.get("hoverBorderColor")

    @hoverBorderColor.setter
    def hoverBorderColor(self, val):
        self._attrs["hoverBorderColor"] = val

    @property
    def hoverBorderWidth(self):
        """
        `Polas <https://www.chartjs.org/docs/latest/charts/polar.html>`_
        """
        return self._attrs.get("hoverBorderWidth")

    @hoverBorderWidth.setter
    def hoverBorderWidth(self, val):
        self._attrs["hoverBorderWidth"] = val


class DataSetRadar(DataSet):

    @property
    def borderCapStyle(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("borderCapStyle")

    @borderCapStyle.setter
    def borderCapStyle(self, val):
        self._attrs["borderCapStyle"] = val

    @property
    def borderDash(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("borderDash")

    @borderDash.setter
    def borderDash(self, val):
        self._attrs["borderDash"] = val

    @property
    def borderDashOffset(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("borderDashOffset")

    @borderDashOffset.setter
    def borderDashOffset(self, val):
        self._attrs["borderDashOffset"] = val

    @property
    def borderJoinStyle(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("borderJoinStyle")

    @borderJoinStyle.setter
    def borderJoinStyle(self, val):
        self._attrs["borderJoinStyle"] = val

    @property
    def hoverBackgroundColor(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("hoverBackgroundColor")

    @hoverBackgroundColor.setter
    def hoverBackgroundColor(self, val):
        self._attrs["hoverBackgroundColor"] = val

    @property
    def hoverBorderCapStyle(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("hoverBorderCapStyle")

    @hoverBorderCapStyle.setter
    def hoverBorderCapStyle(self, val):
        self._attrs["hoverBorderCapStyle"] = val

    @property
    def hoverBorderColor(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("hoverBorderColor")

    @hoverBorderColor.setter
    def hoverBorderColor(self, val):
        self._attrs["hoverBorderColor"] = val

    @property
    def hoverBorderDash(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("hoverBorderDash")

    @hoverBorderDash.setter
    def hoverBorderDash(self, val):
        self._attrs["hoverBorderDash"] = val

    @property
    def hoverBorderDashOffset(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("hoverBorderDashOffset")

    @hoverBorderDashOffset.setter
    def hoverBorderDashOffset(self, val):
        self._attrs["hoverBorderDashOffset"] = val

    @property
    def hoverBorderJoinStyle(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("hoverBorderJoinStyle")

    @hoverBorderJoinStyle.setter
    def hoverBorderJoinStyle(self, val):
        self._attrs["hoverBorderJoinStyle"] = val

    @property
    def hoverBorderWidth(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("hoverBorderWidth")

    @hoverBorderWidth.setter
    def hoverBorderWidth(self, val):
        self._attrs["hoverBorderWidth"] = val

    @property
    def fill(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("fill")

    @fill.setter
    def fill(self, val):
        self._attrs["fill"] = val

    @property
    def label(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs["label"]

    @label.setter
    def label(self, val):
        self._attrs["label"] = val

    @property
    def order(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("order")

    @order.setter
    def order(self, val):
        self._attrs["order"] = val

    @property
    def lineTension(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("lineTension")

    @lineTension.setter
    def lineTension(self, val):
        self._attrs["lineTension"] = val

    @property
    def pointBackgroundColor(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("pointBackgroundColor")

    @pointBackgroundColor.setter
    def pointBackgroundColor(self, val):
        self._attrs["pointBackgroundColor"] = val

    @property
    def pointBorderColor(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("pointBorderColor")

    @pointBorderColor.setter
    def pointBorderColor(self, val):
        self._attrs["pointBorderColor"] = val

    @property
    def pointBorderWidth(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("pointBorderWidth")

    @pointBorderWidth.setter
    def pointBorderWidth(self, val):
        self._attrs["pointBorderWidth"] = val

    @property
    def pointHitRadius(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("pointHitRadius")

    @pointHitRadius.setter
    def pointHitRadius(self, val):
        self._attrs["pointHitRadius"] = val

    @property
    def pointHoverBackgroundColor(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("pointHoverBackgroundColor")

    @pointHoverBackgroundColor.setter
    def pointHoverBackgroundColor(self, val):
        self._attrs["pointHoverBackgroundColor"] = val

    @property
    def pointHoverBorderColor(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("pointHoverBorderColor")

    @pointHoverBorderColor.setter
    def pointHoverBorderColor(self, val):
        self._attrs["pointHoverBorderColor"] = val

    @property
    def pointHoverBorderWidth(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("pointHoverBorderWidth")

    @pointHoverBorderWidth.setter
    def pointHoverBorderWidth(self, val):
        self._attrs["pointHoverBorderWidth"] = val

    @property
    def pointHoverRadius(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("pointHoverRadius")

    @pointHoverRadius.setter
    def pointHoverRadius(self, val):
        self._attrs["pointHoverRadius"] = val

    @property
    def pointRadius(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("pointRadius")

    @pointRadius.setter
    def pointRadius(self, val):
        self._attrs["pointRadius"] = val

    @property
    def pointRotation(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("pointRotation")

    @pointRotation.setter
    def pointRotation(self, val):
        self._attrs["pointRotation"] = val

    @property
    def pointStyle(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("pointStyle")

    @pointStyle.setter
    def pointStyle(self, val):
        self._attrs["pointStyle"] = val

    @property
    def spanGaps(self):
        """
        `Radar <https://www.chartjs.org/docs/latest/charts/radar.html>`_
        """
        return self._attrs.get("spanGaps")

    @spanGaps.setter
    def spanGaps(self, val):
        self._attrs["spanGaps"] = val


class DataSetBubble(DataSet):

    @property
    def data(self):
        """
        `Bubble <https://www.chartjs.org/docs/latest/charts/bubble.html>`_
        """
        return self._attrs["data"]

    @data.setter
    def data(self, val):
        self._attrs["data"] = val

    @property
    def hoverBackgroundColor(self):
        """
        `Bubble <https://www.chartjs.org/docs/latest/charts/bubble.html>`_
        """
        return self._attrs["hoverBackgroundColor"]

    @hoverBackgroundColor.setter
    def hoverBackgroundColor(self, val):
        self._attrs["hoverBackgroundColor"] = val

    @property
    def hoverBorderColor(self):
        """
        `Bubble <https://www.chartjs.org/docs/latest/charts/bubble.html>`_
        """
        return self._attrs["hoverBorderColor"]

    @hoverBorderColor.setter
    def hoverBorderColor(self, val):
        self._attrs["hoverBorderColor"] = val

    @property
    def hoverBorderWidth(self):
        """
        `Bubble <https://www.chartjs.org/docs/latest/charts/bubble.html>`_
        """
        return self._attrs["hoverBorderWidth"]

    @hoverBorderWidth.setter
    def hoverBorderWidth(self, val):
        self._attrs["hoverBorderWidth"] = val

    @property
    def hoverRadius(self):
        """
        `Bubble <https://www.chartjs.org/docs/latest/charts/bubble.html>`_
        """
        return self._attrs["hoverRadius"]

    @hoverRadius.setter
    def hoverRadius(self, val):
        self._attrs["hoverRadius"] = val

    @property
    def hitRadius(self):
        """
        `Bubble <https://www.chartjs.org/docs/latest/charts/bubble.html>`_
        """
        return self._attrs["hitRadius"]

    @hitRadius.setter
    def hitRadius(self, val):
        self._attrs["hitRadius"] = val

    @property
    def label(self):
        """
        `Bubble <https://www.chartjs.org/docs/latest/charts/bubble.html>`_
        """
        return self._attrs["label"]

    @label.setter
    def label(self, val):
        self._attrs["label"] = val

    @property
    def order(self):
        """
        `Bubble <https://www.chartjs.org/docs/latest/charts/bubble.html>`_
        """
        return self._attrs["order"]

    @order.setter
    def order(self, val):
        self._attrs["order"] = val

    @property
    def pointStyle(self):
        """
        `Bubble <https://www.chartjs.org/docs/latest/charts/bubble.html>`_
        """
        return self._attrs["pointStyle"]

    @pointStyle.setter
    def pointStyle(self, val):
        self._attrs["pointStyle"] = val

    @property
    def rotation(self):
        """
        `Bubble <https://www.chartjs.org/docs/latest/charts/bubble.html>`_
        """
        return self._attrs["rotation"]

    @rotation.setter
    def rotation(self, val):
        self._attrs["rotation"] = val

    @property
    def radius(self):
        """
        `Bubble <https://www.chartjs.org/docs/latest/charts/bubble.html>`_
        """
        return self._attrs["radius"]

    @radius.setter
    def radius(self, val):
        self._attrs["radius"] = val


class DataSetTreeMap(DataSet):

    @property
    def captions(self):
        """ The captions options can control if and how a captions, to represent the group of the chart,
        can be shown in the rectangle, with the following properties:

        Related Pages:

          https://chartjs-chart-treemap.pages.dev/usage.html#captions
          https://chartjs-chart-treemap.pages.dev/usage.html#dataset-optionsl
        """
        return self._attrs["captions"]

    @captions.setter
    def captions(self, values: dict):
        self._attrs["captions"] = values

    @property
    def dividers(self):
        """ The divider is a line which splits a treemap elements in grouped elements and can be controlled with
        the following properties.

        Related Pages:

          https://chartjs-chart-treemap.pages.dev/usage.html#dividers
          https://chartjs-chart-treemap.pages.dev/usage.html#dataset-optionsl
        """
        return self._attrs["dividers"]

    @dividers.setter
    def dividers(self, values: dict):
        self._attrs["dividers"] = values

    @property
    def label(self):
        """ The labels options can control if and how a label, to represent the data, can be shown in the rectangle,
        with the following properties:

        Related Pages:

          https://chartjs-chart-treemap.pages.dev/usage.html#dataset-optionsl
        """
        return self._attrs["label"]

    @label.setter
    def label(self, val: str):
        self.set_val(val)

    @property
    def spacing(self):
        """ Fixed distance (in pixels) between all treemap elements.

        Related Pages:

          https://chartjs-chart-treemap.pages.dev/usage.html#dataset-options
        """
        return self._attrs.get("spacing", 0)

    @spacing.setter
    def spacing(self, num: int):
        self._attrs["spacing"] = num

    @property
    def rtl(self):
        """ If true, the treemap elements are rendering from right to left.

        Related Pages:

          https://chartjs-chart-treemap.pages.dev/usage.html#dataset-options
        """
        return self._attrs.get("rtl", False)

    @rtl.setter
    def rtl(self, flag: bool):
        self._attrs["rtl"] = flag

    @property
    def tree(self):
        """ Tree data should be provided in tree property of dataset. data is then automatically build.

        Related Pages:

          https://chartjs-chart-treemap.pages.dev/usage.html#dataset-options
        """
        return self._attrs.get("tree")

    @tree.setter
    def tree(self, values):
        self._attrs["tree"] = values

    @property
    def treeLeafKey(self):
        """ The name of the key where the object key of leaf node of tree object is stored.
        Used only when tree is an object, as hierarchical data.

        Related Pages:

          https://chartjs-chart-treemap.pages.dev/usage.html#dataset-options
        """
        return self._attrs.get("treeLeafKey")

    @treeLeafKey.setter
    def treeLeafKey(self, values):
        self._attrs["treeLeafKey"] = values

    @property
    def key(self):
        """ Define the key name in data objects to use for value.

        Related Pages:

          https://chartjs-chart-treemap.pages.dev/usage.html#dataset-options
        """
        return self._attrs.get("key")

    @key.setter
    def key(self, value: str):
        self._attrs["key"] = value

    @property
    def groups(self):
        """ Define how to display multiple levels of hierarchy. Data is summarized to groups internally.

        Related Pages:

          https://chartjs-chart-treemap.pages.dev/usage.html#dataset-options
        """
        return self._attrs.get("groups")

    @groups.setter
    def groups(self, values: List[str]):
        self._attrs["groups"] = values

    @property
    def labels(self) -> OptionsLabels:
        """ The labels options can control if and how a label, to represent the data, can be shown in the rectangle.

        `Labels <https://chartjs-chart-treemap.pages.dev/usage.html#labels>`_
        """
        if self._attrs.get("labels") is None:
            self._attrs['labels'] = OptionsLabels(self.page)
        return self._attrs['labels']

    @property
    def sumKeys(self):
        """ Define multiple keys to add additional sums, on top of the key one, for scriptable options use.

        Related Pages:

          https://chartjs-chart-treemap.pages.dev/usage.html#dataset-options
        """
        return self._attrs.get("sumKeys")

    @sumKeys.setter
    def sumKeys(self, values: List[str]):
        self._attrs["sumKeys"] = values


class DataSetSankey(DataSet):

    @property
    def colorMode(self):
        """
        `Sankey <https://github.com/kurkle/chartjs-chart-sankey>`_
        """
        return self._attrs["colorMode"]

    @colorMode.setter
    def colorMode(self, value: str):
        if value not in ["gradient", "from", "to"]:
            raise ValueError("ColorMode not defined")

        self.set_val(value)

    @property
    def column(self):
        """
        `Sankey <https://github.com/kurkle/chartjs-chart-sankey>`_
        """
        return self._attrs["priority"]

    @column.setter
    def column(self, values: Dict[str, int]):
        self.set_val(values)

    @property
    def label(self):
        """
        The labels options can control if and how a label, to represent the data, can be shown in the rectangle,
        with the following properties:

        `Sankey <https://github.com/kurkle/chartjs-chart-sankey>`_
        """
        return self._attrs["label"]

    @label.setter
    def label(self, val: str):
        self.set_val(val)

    @property
    def labels(self):
        """
        `Sankey <https://github.com/kurkle/chartjs-chart-sankey>`_
        """
        return self._attrs["label"]

    @labels.setter
    def labels(self, values: Dict[str, str]):
        self.set_val(values)

    @property
    def priority(self):
        """
        `Sankey <https://github.com/kurkle/chartjs-chart-sankey>`_
        """
        return self._attrs["priority"]

    @priority.setter
    def priority(self, values: Dict[str, int]):
        self.set_val(values)

    @property
    def size(self):
        """
        `Sankey <https://github.com/kurkle/chartjs-chart-sankey>`_
        """
        return self._attrs["size"]

    @size.setter
    def size(self, value: str):
        if value not in ["max", "min"]:
            raise ValueError("'max', // or 'min' if flow overlap is preferred")

        self.set_val(value)
