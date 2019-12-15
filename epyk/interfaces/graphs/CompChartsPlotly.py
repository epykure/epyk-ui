#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from epyk.core.html import graph


class Plotly(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Plotly"

  def line(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None,
           filters=None, profile=None, xAxisOrder=None, options=None,
           width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

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

    :rtype: graph.GraphPlotly.Chart
    """
    if options is None:
      options = {}
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, data=data, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, title=title, chartFamily=self.chartFamily,
                                     filters=filters, profile=profile, xAxisOrder=xAxisOrder, options=options, width=width,
                                     height=height, htmlCode=htmlCode)


  def bar(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None,
           filters=None, profile=None, xAxisOrder=None, options=None,
           width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

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

    :rtype: graph.GraphPlotly.Chart
    """
    if options is None:
      options = {}
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, data=data, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, title=title, chartFamily=self.chartFamily,
                                     filters=filters, profile=profile, xAxisOrder=xAxisOrder, options=options, width=width,
                                     height=height, htmlCode=htmlCode)

  def scatter(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None,
           filters=None, profile=None, xAxisOrder=None, options=None,
           width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

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

    :rtype: graph.GraphPlotly.Chart
    """
    if options is None:
      options = {}
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, data=data, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, title=title, chartFamily=self.chartFamily,
                                     filters=filters, profile=profile, xAxisOrder=xAxisOrder, options=options, width=width,
                                     height=height, htmlCode=htmlCode)

  def histogram(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None,
                filters=None, profile=None, xAxisOrder=None, options=None,
                width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

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

    :rtype: graph.GraphPlotly.Chart
    """
    if options is None:
      options = {}
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, data=data, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, title=title, chartFamily=self.chartFamily,
                                     filters=filters, profile=profile, xAxisOrder=xAxisOrder, options=options, width=width,
                                     height=height, htmlCode=htmlCode)

  def pie(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None,
                filters=None, profile=None, xAxisOrder=None, options=None,
                width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

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

    :rtype: graph.GraphPlotly.Chart
    """
    if options is None:
      options = {}
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, data=data, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, title=title, chartFamily=self.chartFamily,
                                     filters=filters, profile=profile, xAxisOrder=xAxisOrder, options=options, width=width,
                                     height=height, htmlCode=htmlCode)

  def area(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None,
           filters=None, profile=None, xAxisOrder=None, options=None,
           width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

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

    :rtype: graph.GraphPlotly.Chart
    """
    if options is None:
      options = {}
    return self.parent.context.chart(chartType="scatter", data=data, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, title=title, chartFamily=self.chartFamily,
                                     filters=filters, profile=profile, xAxisOrder=xAxisOrder, options=options, width=width,
                                     height=height, htmlCode=htmlCode)
