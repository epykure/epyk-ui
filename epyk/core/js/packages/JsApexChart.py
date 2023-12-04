#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class _Export:

  @property
  def options(self):
    """ """
    return JsObjects.JsObject.JsObject.get("options")

  @property
  def event(self):
    """ """
    return JsObjects.JsObject.JsObject.get("event")

  @property
  def config(self):
    """ """
    return JsObjects.JsObject.JsObject.get("config")

  @property
  def chartContext(self):
    """ """
    return JsObjects.JsObject.JsObject.get("chartContext")

  @property
  def seriesIndex(self):
    """ """
    return JsObjects.JsNumber.JsNumber.get("seriesIndex")

  @property
  def x(self):
    """ """
    return JsObjects.JsObject.JsObject.get("config.globals.labels[config.dataPointIndex]")

  @property
  def y(self):
    """ """
    return JsObjects.JsNumber.JsNumber.get("config.globals.series[config.seriesIndex][config.dataPointIndex]")


class ApexChart(JsPackage):
  lib_alias = {'js': "apexcharts", 'css': 'apexcharts'}

  def __init__(self, html_code=None, config=None, page: primitives.PageModel = None, js_code=None,
               selector: str = None, set_var=False, component: primitives.HtmlModel = None):
    self.page, self.component = page, component
    if selector is None:
      self._selector = self.new(html_code, config, js_code).toStr()
    else:
      self._selector = selector
    self.varName, self.setVar = js_code or self._selector, set_var
    self.page.jsImports.add(self.lib_alias['js'])
    self.page.cssImport.add(self.lib_alias['css'])
    self._js = []

  def new(self, html_code: str, options, js_code: str):
    """

    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: The parameters which are accepted in the original method will be passed here in the same order
    :param js_code:
    """
    options = JsUtils.jsConvertData(options, None)
    if js_code is not None:
      return JsObjects.JsVoid('%s = new ApexCharts(%s, %s)' % (js_code, html_code, options))

    return JsObjects.JsVoid('new ApexCharts(%s, %s)' % (html_code, options))

  def render(self):
    """The render() method is responsible for drawing the chart on the page.
    It is the primary method that has to be called after configuring the options.

    `Package Doc <https://apexcharts.com/docs/methods/#render>`_
    """
    return JsObjects.JsVoid("%s.render()" % self.varName)

  def exec(self, html_code: str, method_name: str, options: dict = None):
    """
    If you want to call chart methods without referencing the instance of the chart,
    you can call the exec() method directly.
    The exec() method takes chartID as the first parameter and finds the chart instance based on that ID to execute
    method on that chart instance.

    Related Pages:

      https://apexcharts.com/docs/methods/#exec

    :param html_code: An identifier for this component (on both Python and Javascript side)
    :param method_name: Any function which can directly be called on chart instance can be named in method parameter
    :param options: The parameters which are accepted in the original method will be passed here in the same order
    """
    html_code = JsUtils.jsConvertData(html_code, None)
    method_name = JsUtils.jsConvertData(method_name, None)
    options = JsUtils.jsConvertData(options or {}, None, depth=True)
    return JsObjects.JsVoid("ApexCharts.exec(%s, %s, %s)" % (html_code, method_name, options))

  def updateOptions(self, new_options: dict, redraw_paths: bool = False, animate: bool = True,
                    update_synced_charts: bool = True):
    """This method allows you to update the configuration object by passing the options as the first parameter.
    The new config object is merged with the existing config object preserving the existing configuration.

    Usage::

      but_title = page.ui.button("Change Title")
      label = page.ui.input(placeholder="Set chart title")
      but_title.click([chart.js.updateOptions({"title": {"text": label.dom.content}})])

    `Package Doc <https://apexcharts.com/docs/methods/#updateOptions>`_

    :param new_options: The configuration object to merge on the existing one
    :param redraw_paths: Optional. When the chart is re-rendered, should it draw from the existing paths or
      completely redraw the chart paths from the beginning. By default, the chart is re-rendered from the existing paths
    :param animate: Optional. Should the chart animate on re-rendering
    :param update_synced_charts: Optional. All the charts in a group should also update when one chart in a group is updated
    """
    new_options = JsUtils.jsConvertData(new_options, None, depth=True)
    redraw_paths = JsUtils.jsConvertData(redraw_paths, None)
    animate = JsUtils.jsConvertData(animate, None)
    update_synced_charts = JsUtils.jsConvertData(update_synced_charts, None)
    return JsObjects.JsVoid("%s.updateOptions(%s, %s, %s, %s)" % (
      self.varName, new_options, redraw_paths, animate, update_synced_charts))

  def updateSeries(self, new_series: list, animate: bool = True, dataflows: List[dict] = None):
    """Allows you to update the series array overriding the existing one.
    If you want to append series to existing series, use the appendSeries() method

    `Package Doc <https://apexcharts.com/docs/methods/#updateSeries>`_

    :param new_series: The series array to override the existing one
    :param animate: Optional. Should the chart animate on re-rendering
    :param dataflows: Chain of data transformations
    """
    new_series = JsUtils.dataFlows(new_series, dataflows, self.page)
    animate = JsUtils.jsConvertData(animate, None)
    return JsObjects.JsVoid("%s.updateSeries(%s, %s)" % (self.varName, new_series, animate))

  def appendSeries(self, new_series: dict, animate: bool = True, dataflows: List[dict] = None):
    """
    This method allows you to append a new series to the existing one.

    Usage::

      but_series.click([chart.js.appendSeries({"name": 'newSeries', 'data': [23, 45, 23]})])

    Related Pages:

      https://apexcharts.com/docs/methods/#appendSeries

    :param new_series: The series to be added
    :param animate: Optional. Should the chart animate on re-rendering
    :param dataflows: Chain of data transformations
    """
    new_series = JsUtils.dataFlows(new_series, dataflows, self.page)
    animate = JsUtils.jsConvertData(animate, None)
    return JsObjects.JsVoid("%s.appendSeries(%s, %s)" % (self.varName, new_series, animate))

  def toggleSeries(self, series_name: str):
    """
    This method allows you to toggle the visibility of series programmatically.
    Useful when you have a custom legend.

    Related Pages:

      https://apexcharts.com/docs/methods/#toggleSeries

    :param series_name: String. The series name which you want to toggle visibility for.
    """
    series_name = JsUtils.jsConvertData(series_name, None)
    return JsObjects.JsVoid("%s.toggleSeries(%s)" % (self.varName, series_name))

  def showSeries(self, series_name: str):
    """
    This method allows you to show the hidden series.
    If the series is already visible, this doesn’t affect it.

    Related Pages:

      https://apexcharts.com/docs/methods/#showSeries

    :param series_name: String. The series name which you want to hide
    """
    series_name = JsUtils.jsConvertData(series_name, None)
    return JsObjects.JsVoid("%s.showSeries(%s)" % (self.varName, series_name))

  def hideSeries(self, series_name: str):
    """
    This method allows you to hide the visible series.
    If the series is already hidden, this method doesn’t affect it.

    Related Pages:

      https://apexcharts.com/docs/methods/#hideSeries

    :param series_name: The series name which you want to hide
    """
    series_name = JsUtils.jsConvertData(series_name, None)
    return JsObjects.JsVoid("%s.hideSeries(%s)" % (self.varName, series_name))

  def zoomX(self, start: int, end: int):
    """
    Manually zoom into the chart with the start and end X values.

    Related Pages:

      https://apexcharts.com/docs/methods/#zoomX

    :param start: The ending x-axis value. Accepts timestamp or a number
    :param end: The ending x-axis value. Accepts timestamp or a number
    """
    return JsObjects.JsVoid("%s.zoomX(%s, %s)" % (self.varName, start, end))

  def resetSeries(self, should_update_chart: bool = True, should_reset_zoom: bool = True):
    """
    Resets all toggled series and bring back the chart to its original state.

    Related Pages:

      https://apexcharts.com/docs/methods/#resetSeries

    :param should_update_chart: Optional. After resetting the series, the chart data should update and return
      to it’s original series
    :param should_reset_zoom: Optional. If the user has zoomed in when this method is called, the zoom level
      should also reset
    """
    should_update_chart = JsUtils.jsConvertData(should_update_chart, None)
    should_reset_zoom = JsUtils.jsConvertData(should_reset_zoom, None)
    return JsObjects.JsVoid("%s.resetSeries(%s, %s)" % (self.varName, should_update_chart, should_reset_zoom))

  def appendData(self, new_data: list, dataflows: List[dict] = None):
    """
    This method allows you to append new data to the series array.
    If you have existing multiple series, provide the new array in the same indexed order.

    Usage::

        btn.click([
          chart.js.appendData([{'data': {}}, {"name": "toto2", 'data': [32, 44, 31, 41, 22]}]) ])

    Related Pages:

      https://apexcharts.com/docs/methods/#appendData

    :param new_data: The data array to append the existing series datasets
    :param dataflows: Chain of data transformations
    """
    new_data = JsUtils.dataFlows(new_data, dataflows, self.page)
    return JsObjects.JsVoid("%s.appendData(%s)" % (self.varName, new_data))

  def toggleDataPointSelection(self, series_index: int, data_point_index: int):
    """
    This method allows you to select/deselect a data-point of a particular series.

    Related Pages:

      https://apexcharts.com/docs/methods/#toggleDataPointSelection

    :param series_index: Index of the series array
    :param data_point_index: Index of the data-point in the series selected in previous argument
    """
    series_index = JsUtils.jsConvertData(series_index, None)
    data_point_index = JsUtils.jsConvertData(data_point_index, None)
    return JsObjects.JsVoid("%s.toggleDataPointSelection(%s, %s)" % (self.varName, series_index, data_point_index))

  def addXaxisAnnotation(self, options: dict, push_to_memory: bool = True):
    """
    The addXaxisAnnotation() method can be used to draw annotations after chart is rendered.

    Related Pages:

      https://apexcharts.com/docs/methods/#addxaxisannotation

    :param options: This function accepts the same parameters as it accepts in the point annotations config.
    :param push_to_memory: Optional. When enabled, it preserves the annotations in subsequent chart updates.
      If you don’t want it to be saved for the next updates, turn off this option
    """
    options = JsUtils.jsConvertData(options, None, depth=True)
    push_to_memory = JsUtils.jsConvertData(push_to_memory, None)
    return JsObjects.JsVoid("%s.addXaxisAnnotation(%s, %s)" % (self.varName, options, push_to_memory))

  def addYaxisAnnotation(self, options: dict, push_to_memory: bool = True):
    """
    The addYaxisAnnotation() method can be used to draw annotations after chart is rendered.

    Related Pages:

      https://apexcharts.com/docs/methods/#addxaxisannotation

    :param options: This function accepts the same parameters as it accepts in the point annotations config.
    :param push_to_memory: Optional. When enabled, it preserves the annotations in subsequent chart updates.
      If you don’t want it to be saved for the next updates, turn off this option
    """
    options = JsUtils.jsConvertData(options, None, depth=True)
    push_to_memory = JsUtils.jsConvertData(push_to_memory, None)
    return JsObjects.JsVoid("%s.addYaxisAnnotation(%s, %s)" % (self.varName, options, push_to_memory))

  def addPointAnnotation(self, options: dict, push_to_memory: bool = True):
    """
    The addPointAnnotation() method can be used to draw annotations after chart is rendered.

    Usage::

      text = page.ui.input(placeholder="Annotation value")
      but_series.click([
        chart.js.addPointAnnotation({"x": 2, "y": 5, "label": {"text": text.dom.content}})])

    Related Pages:

      https://apexcharts.com/docs/methods/#addpointannotation

    :param options: This function accepts the same parameters as it accepts in the point annotations config.
    :param push_to_memory: Optional. When enabled, it preserves the annotations in subsequent chart updates.
      If you don’t want it to be saved for the next updates, turn off this option
    """
    options = JsUtils.jsConvertData(options, None, depth=True)
    push_to_memory = JsUtils.jsConvertData(push_to_memory, None)
    return JsObjects.JsVoid("%s.addPointAnnotation(%s, %s)" % (self.varName, options, push_to_memory))

  def removeAnnotation(self, annotation_id: str):
    """
    The removeAnnotation() method can be used to delete any previously added annotations.
    Only annotations which are added by external methods (addPointAnnotation, addXaxisAnnotation, addYaxisAnnotation)
    are affected.
    Annotations defined in the options/config object are not affected.

    Related Pages:

      https://apexcharts.com/docs/methods/#removeAnnotation

    :param annotation_id: The unique identifier of the annotation which was created using the
      addPointAnnotation, addXaxisAnnotation or addYaxisAnnotation methods.
    """
    annotation_id = JsUtils.jsConvertData(annotation_id, None)
    return JsObjects.JsVoid("%s.removeAnnotation(%s)" % (self.varName, annotation_id))

  def clearAnnotations(self):
    """
    The clearAnnotations() method is used to delete all annotation elements which are added dynamically using the
    three methods stated above.

    Related Pages:

      https://apexcharts.com/docs/methods/#clearAnnotations
    """
    return JsObjects.JsVoid("%s.clearAnnotations()" % self.varName)

  def dataURI(self):
    """
    The dataURI() method is used to get base64 dataURI. Then this dataURI can be used to generate PDF using jsPDF.

    Related Pages:

      https://apexcharts.com/docs/methods/#dataURI
    """
    return JsObjects.JsVoid("%s.dataURI()" % self.varName)

  def destroy(self):
    """
    Removes the SVG element that belongs to the chart instance also removing all events handlers attached to it.

    Related Pages:

      https://apexcharts.com/docs/methods/#destroy
    """
    return JsObjects.JsVoid("%s.destroy()" % self.varName)
