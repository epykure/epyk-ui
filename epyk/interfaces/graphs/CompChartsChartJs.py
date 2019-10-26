"""


"""

import sys

from epyk.core.html import graph
from epyk.core.js.Imports import requires


class ChartJs(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "ChartJs"

  def line(self, data=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
           width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://www.chartjs.org/

    :param data:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:

    :return:
    """
    line_chart = graph.GraphChartJs.ChartLine(self.parent.context.rptObj, width, height, title, options or {}, htmlCode,
                                              filters, profile)
    line_chart.chart._data_attrs["data"] = self.parent.context.rptObj.js.data.records(data).to.chartJs.line(y_columns, x_axis, profile or False).toStr()
    print(self.parent.context.rptObj.js.data.records(data).to.chartJs.line(y_columns, x_axis, profile or False).toStr())
    self.parent.context.register(line_chart)
    return line_chart

  def pie(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None, filters=None, profile=None,
          xAxisOrder=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    :param data:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param title:
    :param profile:
    :param xAxisOrder:
    :param width:
    :param height:
    :param htmlCode:

    :return:

    :rtype: graph.GraphChartJs.Chart
    """
    if options is None:
      options = {}
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, data=data, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, title=title, chartFamily=self.chartFamily,
                                     filters=filters, profile=profile, xAxisOrder=xAxisOrder, options=options, width=width,
                                     height=height, htmlCode=htmlCode)

  def donut(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None, filters=None, profile=None,
            xAxisOrder=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    :param data:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param title:
    :param profile:
    :param xAxisOrder:
    :param width:
    :param height:
    :param htmlCode:
    :return:
    :rtype: graph.GraphChartJs.Chart
    """
    if options is None:
      options = {}
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, data=data, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, title=title, chartFamily=self.chartFamily,
                                     filters=filters, profile=profile, xAxisOrder=xAxisOrder, options=options, width=width,
                                     height=height, htmlCode=htmlCode)

  def area(self, aresDf=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
           globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
           width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    """

    :param aresDf:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param title:
    :param globalFilter:
    :param filterSensitive:
    :param profile:
    :param dataSrc:
    :param xAxisOrder:
    :param chartOptions:
    :param width:
    :param widthUnit:
    :param height:
    :param heightUnit:
    :param htmlCode:
    :return:
    :rtype: graph.GraphChartJs.Chart
    """
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, aresDf=aresDf, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, dataFncs=dataFncs, title=title,
                                     chartFamily=self.chartFamily,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile,
                                     dataSrc=dataSrc,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)

  def step(self, aresDf=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
           globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
           width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    """

    :param aresDf:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param title:
    :param globalFilter:
    :param filterSensitive:
    :param profile:
    :param dataSrc:
    :param xAxisOrder:
    :param chartOptions:
    :param width:
    :param widthUnit:
    :param height:
    :param heightUnit:
    :param htmlCode:
    :return:
    :rtype: graph.GraphChartJs.Chart
    """
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, aresDf=aresDf, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, dataFncs=dataFncs, title=title,
                                     chartFamily=self.chartFamily,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile,
                                     dataSrc=dataSrc,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)

  def bar(self, aresDf=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
           globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
           width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    """

    :param aresDf:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param title:
    :param globalFilter:
    :param filterSensitive:
    :param profile:
    :param dataSrc:
    :param xAxisOrder:
    :param chartOptions:
    :param width:
    :param widthUnit:
    :param height:
    :param heightUnit:
    :param htmlCode:
    :return:
    :rtype: graph.GraphChartJs.Chart
    """
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, aresDf=aresDf, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, dataFncs=dataFncs, title=title,
                                     chartFamily=self.chartFamily,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile,
                                     dataSrc=dataSrc,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)

  def hbar(self, aresDf=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
           globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
           width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    """

    :param aresDf:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param title:
    :param globalFilter:
    :param filterSensitive:
    :param profile:
    :param dataSrc:
    :param xAxisOrder:
    :param chartOptions:
    :param width:
    :param widthUnit:
    :param height:
    :param heightUnit:
    :param htmlCode:
    :return:
    :rtype: graph.GraphChartJs.Chart
    """
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, aresDf=aresDf, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, dataFncs=dataFncs, title=title,
                                     chartFamily=self.chartFamily,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile,
                                     dataSrc=dataSrc,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)

  def multi(self, aresDf=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
           globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
           width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    """

    :param aresDf:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param title:
    :param globalFilter:
    :param filterSensitive:
    :param profile:
    :param dataSrc:
    :param xAxisOrder:
    :param chartOptions:
    :param width:
    :param widthUnit:
    :param height:
    :param heightUnit:
    :param htmlCode:
    :return:
    :rtype: graph.GraphChartJs.Chart
    """
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, aresDf=aresDf, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, dataFncs=dataFncs, title=title,
                                     chartFamily=self.chartFamily,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile,
                                     dataSrc=dataSrc,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)

  def scatter(self, aresDf=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
           globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
           width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    """

    :param aresDf:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param title:
    :param globalFilter:
    :param filterSensitive:
    :param profile:
    :param dataSrc:
    :param xAxisOrder:
    :param chartOptions:
    :param width:
    :param widthUnit:
    :param height:
    :param heightUnit:
    :param htmlCode:
    :return:
    :rtype: graph.GraphChartJs.Chart
    """
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, aresDf=aresDf, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, dataFncs=dataFncs, title=title,
                                     chartFamily=self.chartFamily,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile,
                                     dataSrc=dataSrc,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)

  def bubble(self, aresDf=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
           globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
           width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    """

    :param aresDf:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param title:
    :param globalFilter:
    :param filterSensitive:
    :param profile:
    :param dataSrc:
    :param xAxisOrder:
    :param chartOptions:
    :param width:
    :param widthUnit:
    :param height:
    :param heightUnit:
    :param htmlCode:
    :return:
    :rtype: graph.GraphChartJs.Chart
    """
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, aresDf=aresDf, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, dataFncs=dataFncs, title=title,
                                     chartFamily=self.chartFamily,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile,
                                     dataSrc=dataSrc,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)

  def polar(self, aresDf=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
           globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
           width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    """

    :param aresDf:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param title:
    :param globalFilter:
    :param filterSensitive:
    :param profile:
    :param dataSrc:
    :param xAxisOrder:
    :param chartOptions:
    :param width:
    :param widthUnit:
    :param height:
    :param heightUnit:
    :param htmlCode:
    :return:
    :rtype: graph.GraphChartJs.Chart
    """
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, aresDf=aresDf, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, dataFncs=dataFncs, title=title,
                                     chartFamily=self.chartFamily,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile,
                                     dataSrc=dataSrc,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)

  def radar(self, aresDf=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
           globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
           width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    """

    :param aresDf:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param title:
    :param globalFilter:
    :param filterSensitive:
    :param profile:
    :param dataSrc:
    :param xAxisOrder:
    :param chartOptions:
    :param width:
    :param widthUnit:
    :param height:
    :param heightUnit:
    :param htmlCode:
    :return:
    :rtype: graph.GraphChartJs.Chart
    """
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, aresDf=aresDf, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, dataFncs=dataFncs, title=title,
                                     chartFamily=self.chartFamily,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile,
                                     dataSrc=dataSrc,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)

  def kde(self, aresDf=None, seriesNames=None, otherDims=None, dataFncs=None, title='',
            globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
            width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    """

    Specific options to the chartOptions
      - step      : The number of step used in the gaussian_kde function
      - chartType : The type of display for the result

    :param aresDf:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param title:
    :param globalFilter:
    :param filterSensitive:
    :param profile:
    :param dataSrc:
    :param xAxisOrder:
    :param chartOptions:
    :param width:
    :param widthUnit:
    :param height:
    :param heightUnit:
    :param htmlCode:
    :return: The Python Chart object
    :rtype: graph.GraphChartJs.Chart
    """

    # Those two packages are required for this type of chart
    ares_numpy = requires("numpy", reason='Missing Package', install='numpy', autoImport=True, sourceScript=__file__)
    ares_scipy_stats = requires(name='scipy.stats', reason='Missing Package', install='scipy', autoImport=True, sourceScript=__file__)

    step, chartType = 500, 'line'
    if chartOptions is not None and "step" in chartOptions:
      step = chartOptions["step"]
      del chartOptions["step"]

    if chartOptions is not None and "chartType" in chartOptions:
      chartType = chartOptions["chartType"]
      del chartOptions["chartType"]

    kdeSeries = {}
    for series in seriesNames:
      x = ares_numpy.linspace(min(aresDf[series]), max(aresDf[series]), step)
      kdeSeries[series] = ares_scipy_stats.gaussian_kde(list(aresDf[series]))(x)

    newDff = []
    for i in range(step):
      row = {'x': i}
      for series in seriesNames:
        row[series] = kdeSeries[series][i]
      newDff.append(row)

    return self.parent.context.chart(chartType=chartType, aresDf=newDff, seriesNames=seriesNames,
                                     xAxis="x", otherDims=otherDims, dataFncs=dataFncs, title=title,
                                     chartFamily=self.chartFamily, dataSrc=dataSrc,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)

