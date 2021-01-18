#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class _Export:

  @property
  def options(self):
    """

    """
    return JsObjects.JsObject.JsObject.get("options")

  @property
  def event(self):
    """

    """
    return JsObjects.JsObject.JsObject.get("event")

  @property
  def config(self):
    """

    """
    return JsObjects.JsObject.JsObject.get("config")

  @property
  def chartContext(self):
    """

    """
    return JsObjects.JsObject.JsObject.get("chartContext")

  @property
  def seriesIndex(self):
    """

    """
    return JsObjects.JsNumber.JsNumber.get("seriesIndex")

  @property
  def x(self):
    """

    """
    return JsObjects.JsObject.JsObject.get("config.globals.labels[config.dataPointIndex]")

  @property
  def y(self):
    """

    """
    return JsObjects.JsNumber.JsNumber.get("config.globals.series[config.seriesIndex][config.dataPointIndex]")


class ApexChart(JsPackage):
  lib_alias = {'js': "apexcharts", 'css': 'apexcharts'}

  def __init__(self, htmlCode=None, config=None, src=None, varName=None, selector=None, setVar=False):
    self.src = src if src is not None else self.__internal()
    if selector is None:
      self._selector = self.new(htmlCode, config, varName).toStr()
    else:
      self._selector = selector
    self.varName, self.setVar = varName or self._selector, setVar
    self.src.jsImports.add(self.lib_alias['js'])
    self.src.cssImport.add(self.lib_alias['css'])
    self._js = []

  def new(self, htmlCode, options, varName):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options:
    """
    options = JsUtils.jsConvertData(options, None)
    if varName is not None:
      return JsObjects.JsVoid('%s = new ApexCharts(%s, %s)' % (varName, htmlCode, options))

    return JsObjects.JsVoid('new ApexCharts(%s, %s)' % (htmlCode, options))

  def render(self):
    """
    Description:
    -----------
    The render() method is responsible for drawing the chart on the page.
    It is the primary method that has to be called after configuring the options.

    Related Pages:

      https://apexcharts.com/docs/methods/#render
    """
    return JsObjects.JsVoid("%s.render()" % self.varName)

  def exec(self, htmlCode, methodName, options=None):
    """
    Description:
    -----------
    If you want to call chart methods without referencing the instance of the chart, you can call the exec() method directly.
    The exec() method takes chartID as the first parameter and finds the chart instance based on that ID to execute method on that chart instance.

    Related Pages:

      https://apexcharts.com/docs/methods/#exec

    Attributes:
    ----------
    :param htmlCode: String. An identifier for this component (on both Python and Javascript side).
    :param methodName: String. Any function which can directly be called on chart instance can be named in method parameter.
    :param options: Dictionary. The parameters which are accepted in the original method will be passed here in the same order.
    """
    htmlCode = JsUtils.jsConvertData(htmlCode, None)
    methodName = JsUtils.jsConvertData(methodName, None)
    options = JsUtils.jsConvertData(options or {}, None, depth=True)
    return JsObjects.JsVoid("ApexCharts.exec(%s, %s, %s)" % (htmlCode, methodName, options))

  def updateOptions(self, newOptions, redrawPaths=False, animate=True, updateSyncedCharts=True):
    """
    Description:
    -----------
    This method allows you to update the configuration object by passing the options as the first parameter.
    The new config object is merged with the existing config object preserving the existing configuration.

    Related Pages:

      https://apexcharts.com/docs/methods/#updateOptions

    Attributes:
    ----------
    :param newOptions: Dictionary. The configuration object to merge on the existing one.
    :param redrawPaths: Boolean. Optional. When the chart is re-rendered, should it draw from the existing paths or completely redraw the chart paths from the beginning. By default, the chart is re-rendered from the existing paths
    :param animate: Boolean. Optional. Should the chart animate on re-rendering.
    :param updateSyncedCharts: Boolean. Optional. All the charts in a group should also update when one chart in a group is updated.
    """
    newOptions = JsUtils.jsConvertData(newOptions, None, depth=True)
    redrawPaths = JsUtils.jsConvertData(redrawPaths, None)
    animate = JsUtils.jsConvertData(animate, None)
    updateSyncedCharts = JsUtils.jsConvertData(updateSyncedCharts, None)
    return JsObjects.JsVoid("%s.updateOptions(%s, %s, %s, %s)" % (self.varName, newOptions, redrawPaths, animate, updateSyncedCharts))

  def updateSeries(self, newSeries, animate=True):
    """
    Description:
    -----------
    Allows you to update the series array overriding the existing one.
    If you want to append series to existing series, use the appendSeries() method

    Related Pages:

      https://apexcharts.com/docs/methods/#updateSeries

    Attributes:
    ----------
    :param newSeries: List. The series array to override the existing one.
    :param animate: Boolean. Optional. Should the chart animate on re-rendering.
    """
    newSeries = JsUtils.jsConvertData(newSeries, None)
    animate = JsUtils.jsConvertData(animate, None)
    return JsObjects.JsVoid("%s.updateSeries(%s, %s)" % (self.varName, newSeries, animate))

  def appendSeries(self, newSeries, animate=True):
    """
    Description:
    -----------
    This method allows you to append a new series to the existing one.

    Related Pages:

      https://apexcharts.com/docs/methods/#appendSeries

    Attributes:
    ----------
    :param newSeries: Dictionary. The series to be added.
    :param animate: Boolean. Optional. Should the chart animate on re-rendering.
    """
    newSeries = JsUtils.jsConvertData(newSeries, None)
    animate = JsUtils.jsConvertData(animate, None)
    return JsObjects.JsVoid("%s.appendSeries(%s, %s)" % (self.varName, newSeries, animate))

  def toggleSeries(self, seriesName):
    """
    Description:
    -----------
    This method allows you to toggle the visibility of series programmatically. Useful when you have a custom legend.

    Related Pages:

      https://apexcharts.com/docs/methods/#toggleSeries

    Attributes:
    ----------
    :param seriesName: String. The series name which you want to toggle visibility for.
    """
    seriesName = JsUtils.jsConvertData(seriesName, None)
    return JsObjects.JsVoid("%s.toggleSeries(%s)" % (self.varName, seriesName))

  def showSeries(self, seriesName):
    """
    Description:
    -----------
    This method allows you to show the hidden series.
    If the series is already visible, this doesn’t affect it.

    Related Pages:

      https://apexcharts.com/docs/methods/#showSeries

    Attributes:
    ----------
    :param seriesName: String. The series name which you want to hide
    """
    seriesName = JsUtils.jsConvertData(seriesName, None)
    return JsObjects.JsVoid("%s.showSeries(%s)" % (self.varName, seriesName))

  def hideSeries(self, seriesName):
    """
    Description:
    -----------
    This method allows you to hide the visible series.
    If the series is already hidden, this method doesn’t affect it.

    Related Pages:

      https://apexcharts.com/docs/methods/#hideSeries

    Attributes:
    ----------
    :param seriesName: String. The series name which you want to hide.
    """
    seriesName = JsUtils.jsConvertData(seriesName, None)
    return JsObjects.JsVoid("%s.hideSeries(%s)" % (self.varName, seriesName))

  def zoomX(self, start, end):
    """
    Description:
    -----------
    Manually zoom into the chart with the start and end X values.

    Related Pages:

      https://apexcharts.com/docs/methods/#zoomX

    Attributes:
    ----------
    :param start: Integer. The ending x-axis value. Accepts timestamp or a number.
    :param end: Integer. The ending x-axis value. Accepts timestamp or a number.
    """
    return JsObjects.JsVoid("%s.zoomX(%s, %s)" % (self.varName, start, end))

  def resetSeries(self, shouldUpdateChart=True, shouldResetZoom=True):
    """
    Description:
    -----------
    Resets all toggled series and bring back the chart to its original state.

    Related Pages:

      https://apexcharts.com/docs/methods/#resetSeries

    Attributes:
    ----------
    :param shouldUpdateChart: Boolean. Optional. After resetting the series, the chart data should update and return to it’s original series.
    :param shouldResetZoom: Boolean. Optional. If the user has zoomed in when this method is called, the zoom level should also reset.
    """
    shouldUpdateChart = JsUtils.jsConvertData(shouldUpdateChart, None)
    shouldResetZoom = JsUtils.jsConvertData(shouldResetZoom, None)
    return JsObjects.JsVoid("%s.resetSeries(%s, %s)" % (self.varName, shouldUpdateChart, shouldResetZoom))

  def appendData(self, newData):
    """
    Description:
    -----------
    This method allows you to append new data to the series array.
    If you have existing multiple series, provide the new array in the same indexed order.

    Related Pages:

      https://apexcharts.com/docs/methods/#appendData

    Attributes:
    ----------
    :param newData: List. The data array to append the existing series datasets.
    """
    newData = JsUtils.jsConvertData(newData, None)
    return JsObjects.JsVoid("%s.appendData(%s)" % (self.varName, newData))

  def toggleDataPointSelection(self, seriesIndex, dataPointIndex):
    """
    Description:
    -----------
    This method allows you to select/deselect a data-point of a particular series.

    Related Pages:

      https://apexcharts.com/docs/methods/#toggleDataPointSelection

    Attributes:
    ----------
    :param seriesIndex: Integer. Index of the series array
    :param dataPointIndex: Integer. Index of the data-point in the series selected in previous argument.
    """
    seriesIndex = JsUtils.jsConvertData(seriesIndex, None)
    dataPointIndex = JsUtils.jsConvertData(dataPointIndex, None)
    return JsObjects.JsVoid("%s.toggleDataPointSelection(%s, %s)" % (self.varName, seriesIndex, dataPointIndex))

  def addXaxisAnnotation(self, options, pushToMemory=True):
    """
    Description:
    -----------
    The addXaxisAnnotation() method can be used to draw annotations after chart is rendered.

    Related Pages:

      https://apexcharts.com/docs/methods/#addxaxisannotation

    Attributes:
    ----------
    :param options: Dictionary. This function accepts the same parameters as it accepts in the point annotations config.
    :param pushToMemory: Boolean. Optional. When enabled, it preserves the annotations in subsequent chart updates. If you don’t want it to be saved for the next updates, turn off this option
    """
    options = JsUtils.jsConvertData(options, None, depth=True)
    pushToMemory = JsUtils.jsConvertData(pushToMemory, None)
    return JsObjects.JsVoid("%s.addXaxisAnnotation(%s, %s)" % (self.varName, options, pushToMemory))

  def addYaxisAnnotation(self, options, pushToMemory=True):
    """
    Description:
    -----------
    The addYaxisAnnotation() method can be used to draw annotations after chart is rendered.

    Related Pages:

      https://apexcharts.com/docs/methods/#addxaxisannotation

    Attributes:
    ----------
    :param options: Dictionary. This function accepts the same parameters as it accepts in the point annotations config.
    :param pushToMemory: Boolean. Optional. When enabled, it preserves the annotations in subsequent chart updates. If you don’t want it to be saved for the next updates, turn off this option
    """
    options = JsUtils.jsConvertData(options, None, depth=True)
    pushToMemory = JsUtils.jsConvertData(pushToMemory, None)
    return JsObjects.JsVoid("%s.addYaxisAnnotation(%s, %s)" % (self.varName, options, pushToMemory))

  def addPointAnnotation(self, options, pushToMemory=True):
    """
    Description:
    -----------
    The addPointAnnotation() method can be used to draw annotations after chart is rendered.

    Related Pages:

      https://apexcharts.com/docs/methods/#addpointannotation

    Attributes:
    ----------
    :param options: Dictionary. This function accepts the same parameters as it accepts in the point annotations config.
    :param pushToMemory: Boolean. Optional. When enabled, it preserves the annotations in subsequent chart updates. If you don’t want it to be saved for the next updates, turn off this option
    """
    options = JsUtils.jsConvertData(options, None, depth=True)
    pushToMemory = JsUtils.jsConvertData(pushToMemory, None)
    return JsObjects.JsVoid("%s.addPointAnnotation(%s, %s)" % (self.varName, options, pushToMemory))

  def removeAnnotation(self, annotationId):
    """
    Description:
    -----------
    The removeAnnotation() method can be used to delete any previously added annotations.
    Only annotations which are added by external methods (addPointAnnotation, addXaxisAnnotation, addYaxisAnnotation) are affected.
    Annotations defined in the options/config object are not affected.

    Related Pages:

      https://apexcharts.com/docs/methods/#removeAnnotation

    Attributes:
    ----------
    :param annotationId: String. The unqiue identifier of the annotation which was created using the addPointAnnotation, addXaxisAnnotation or addYaxisAnnotation methods.
    """
    annotationId = JsUtils.jsConvertData(annotationId, None)
    return JsObjects.JsVoid("%s.removeAnnotation(%s)" % (self.varName, annotationId))

  def clearAnnotations(self):
    """
    Description:
    -----------
    The clearAnnotations() method is used to delete all annotation elements which are added dynamically using the three methods stated above.

    Related Pages:

      https://apexcharts.com/docs/methods/#clearAnnotations
    """
    return JsObjects.JsVoid("%s.clearAnnotations()" % self.varName)

  def dataURI(self):
    """
    Description:
    -----------
    The dataURI() method is used to get base64 dataURI. Then this dataURI can be used to generate PDF using jsPDF.

    Related Pages:

      https://apexcharts.com/docs/methods/#dataURI
    """
    return JsObjects.JsVoid("%s.dataURI()" % self.varName)

  def destroy(self):
    """
    Description:
    -----------
    Removes the SVG element that belongs to the chart instance also removing all events handlers attached to it.

    Related Pages:

      https://apexcharts.com/docs/methods/#destroy
    """
    return JsObjects.JsVoid("%s.destroy()" % self.varName)
