"""

"""

from epyk.core.html import graph


class Nvd3(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "NVD3"

  def line(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None, filters=None, profile=None,
           xAxisOrder=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/line.html

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
    """
    line_chart = graph.GraphNVD3.ChartBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(line_chart)
    return line_chart

  def bar(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None, filters=None, profile=None,
          xAxisOrder=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/discreteBar.html

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

    """
    bar_chart = graph.GraphNVD3.ChartBar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(bar_chart)
    return bar_chart

  def pie(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None, filters=None, profile=None,
          xAxisOrder=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    http://nvd3.org/examples/pie.html

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

    """
    pie_chart = graph.GraphNVD3.ChartPie(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(pie_chart)
    return pie_chart
