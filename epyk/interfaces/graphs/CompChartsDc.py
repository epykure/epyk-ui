
from epyk.core.html.graph import GraphDC
from epyk.core.js.objects import JsChartDC


class DC(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "DC"

  def line(self, data=None, y_columns=None, x_axis=None, otherDims=None, title=None, filters=None, profile=None,
           xAxisOrder=None, options=None, width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://square.github.io/crossfilter/
    https://dc-js.github.io/dc.js/

    :param data:
    :param y_columns:
    :param x_axis:
    :param otherDims:
    :param title:
    :param profile:
    :param xAxisOrder:
    :param width:
    :param height:
    :param htmlCode:
    """
    line_chart = GraphDC.ChartLine(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, profile)
    line_chart.dom.height(height[0]).x().yAxisLabel("This is the Y Axis!").renderArea(True).dimension("ndx").group("ndx.group().reduceSum(function(d) {return d.a * d.b ;})")
    self.parent.context.register(line_chart)
    return line_chart

  def pie(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None, filters=None, profile=None,
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

    :rtype: GraphDC.Chart
    """
    chart_obj = JsChartDC.JsPie(self.parent.context.rptObj, data, {'static': {}, 'dynamic': {}})
    return self.parent.context.register(GraphDC.Chart(self.parent.context.rptObj, chart_obj, width, height, title,
                                                      options or {}, htmlCode, filters, profile))

  def bubble(self, data=None, seriesNames=None, xAxis=None, otherDims=None, title=None, filters=None, profile=None,
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

    :rtype: GraphDC.Chart
    """
    chart_obj = JsChartDC.JsBuble(self.parent.context.rptObj, data, {'static': {}, 'dynamic': {}})
    return self.parent.context.register(GraphDC.Chart(self.parent.context.rptObj, chart_obj, width, height, title,
                                                      options or {}, htmlCode, filters, profile))
