"""

"""

import sys

from epyk.core.html import graph


class DC(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "DC"

  def line(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None, filters=None, profile=None,
           xAxisOrder=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://square.github.io/crossfilter/
    https://dc-js.github.io/dc.js/

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