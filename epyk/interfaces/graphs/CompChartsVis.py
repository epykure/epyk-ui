
import sys

from epyk.core.html import graph


class Vis2D(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Vis"

  def line(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
           htmlCode=None):
    """
    Description:
    -----------
    Graph2d is an interactive visualization chart to draw data in a 2D graph. You can freely move and zoom in the graph by dragging and scrolling in the window.

    Graph2d uses HTML DOM and SVG for rendering. This allows for flexible customization using css styling.

    elated Pages:
    --------------
    http://www.chartjs.org/
    https://visjs.github.io/vis-timeline/examples/graph2d/16_bothAxisTitles.html

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis],  0) + float(rec[y])
    labels, data = set(), []
    for i, c in enumerate(y_columns):
      series = []
      for x, y in agg_data[c].items():
        labels.add(x)
        series.append({"x": x, "y": y, 'group': i})
      data.append(series)

    line_chart = graph.GraphVis.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    #line_chart.groups.add(sorted(list(labels)))
    for d in data:
      line_chart.add_items(d)

    self.parent.context.register(line_chart)
    return line_chart

  def scatter(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, htmlCode=None):
    """
    Description:
    -----------

    elated Pages:
    --------------
    http://www.chartjs.org/

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis],  0) + float(rec[y])
    labels, data = set(), []
    for i, c in enumerate(y_columns):
      series = []
      for x, y in agg_data[c].items():
        labels.add(x)
        series.append({"x": x, "y": y, 'group': i})
      data.append(series)

    line_chart = graph.GraphVis.ChartScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.options.height = height[0]
    #line_chart.groups.add(sorted(list(labels)))
    for d in data:
      line_chart.add_items(d)

    self.parent.context.register(line_chart)
    return line_chart

  def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, htmlCode=None):
    """
    Description:
    -----------

    elated Pages:
    --------------
    http://www.chartjs.org/

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis],  0) + float(rec[y])
    labels, data = set(), []
    for i, c in enumerate(y_columns):
      series = []
      for x, y in agg_data[c].items():
        labels.add(x)
        series.append({"x": x, "y": y, 'group': i})
      data.append(series)

    line_chart = graph.GraphVis.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.options.height = height[0]
    #line_chart.groups.add(sorted(list(labels)))
    for d in data:
      line_chart.add_items(d)

    self.parent.context.register(line_chart)
    return line_chart

  def timeline(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
               options=None, htmlCode=None):
    """
    Description:
    -----------

    Related Pages:
http://www.chartjs.org/

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param height:
    :param htmlCode:
    """
    series = []
    for rec in record:
      for i, y in enumerate(y_columns):
        if y in rec:
          series.append({"x": rec[x_axis], "y": rec[y], 'group': i})

    line_chart = graph.GraphVis.ChartTimeline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.options.height = height[0]
    line_chart.options.editable = True
    line_chart.options.showCurrentTime = True
    line_chart.add_items(series)

    self.parent.context.register(line_chart)
    return line_chart

  def network(self, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    line_chart = graph.GraphVis.ChartNetwork(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.options.height = height[0]
    self.parent.context.register(line_chart)
    return line_chart


class Vis3D(object):

  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Vis"

  def line(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
                height=(330, "px"), options=None, htmlCode=None):
    agg_data = {}
    for rec in record:
      key_point = (rec[x_axis], rec[z_axis])
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[key_point] = agg_data.get(y, {}).get(key_point,  0) + float(rec[y])
    labels, data = set(), []
    for i, c in enumerate(y_columns):
      series = []
      for point, y in agg_data[c].items():
        series.append({"x": point[0], "y": y, 'z': point[1], 'group': i})
      data.append(series)

    line_chart = graph.GraphVis.Chart3DLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    for d in data:
      line_chart.add_items(d)

    self.parent.context.register(line_chart)
    return line_chart

  def bar(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
          height=(330, "px"), options=None, htmlCode=None):
    agg_data = {}
    for rec in record:
      key_point = (rec[x_axis], rec[z_axis])
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[key_point] = agg_data.get(y, {}).get(key_point,  0) + float(rec[y])
    labels, data = set(), []
    for i, c in enumerate(y_columns):
      series = []
      for point, y in agg_data[c].items():
        series.append({"x": point[0], "y": y, 'z': point[1], 'group': i})
      data.append(series)

    line_chart = graph.GraphVis.Chart3DBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    for d in data:
      line_chart.add_items(d)

    self.parent.context.register(line_chart)
    return line_chart

  def surface(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
              height=(330, "px"), options=None, htmlCode=None):
    agg_data = {}
    for rec in record:
      key_point = (rec[x_axis], rec[z_axis])
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[key_point] = agg_data.get(y, {}).get(key_point,  0) + float(rec[y])
    labels, data = set(), []
    for i, c in enumerate(y_columns):
      series = []
      for point, y in agg_data[c].items():
        series.append({"x": point[0], "y": y, 'z': point[1], 'group': i})
      data.append(series)

    line_chart = graph.GraphVis.Chart3D(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    for d in data:
      line_chart.add_items(d)

    self.parent.context.register(line_chart)
    return line_chart

  def scatter(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
              height=(330, "px"), options=None, htmlCode=None):
    agg_data = {}
    for rec in record:
      key_point = (rec[x_axis], rec[z_axis])
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[key_point] = agg_data.get(y, {}).get(key_point,  0) + float(rec[y])
    labels, data = set(), []
    for i, c in enumerate(y_columns):
      series = []
      for point, y in agg_data[c].items():
        series.append({"x": point[0], "y": y, 'z': point[1], 'group': i})
      data.append(series)

    line_chart = graph.GraphVis.Chart3DScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    for d in data:
      line_chart.add_items(d)

    self.parent.context.register(line_chart)
    return line_chart

  def series(self, record=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
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
    :rtype: graph.GraphVis.Chart
    """
    return self.parent.context.chart(chartType=sys._getframe().f_code.co_name, aresDf=record, seriesNames=seriesNames,
                                     xAxis=xAxis, otherDims=otherDims, dataFncs=dataFncs, title=title, chartFamily=self.chartFamily,
                                     globalFilter=globalFilter, filterSensitive=filterSensitive, profile=profile, dataSrc=dataSrc,
                                     xAxisOrder=xAxisOrder, chartOptions=chartOptions, width=width, widthUnit=widthUnit,
                                     height=height, heightUnit=heightUnit, htmlCode=htmlCode)


class Vis(Vis2D):

  def __init__(self, context):
    super(Vis, self).__init__(context)
    self._3d = Vis3D(context)

  def surface(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
              height=(330, "px"), options=None, htmlCode=None):
    return self._3d.surface(record, y_columns, x_axis, z_axis, profile, width, height, options, htmlCode)

  def scatter3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
                height=(330, "px"), options=None, htmlCode=None):
    return self._3d.scatter(record, y_columns, x_axis, z_axis, profile, width, height, options, htmlCode)

  def series3d(self, record=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
               globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
               width=100, widthUnit="%", height=330, heightUnit="px", htmlCode=None):
    return self._3d.series(record, seriesNames, xAxis, otherDims, dataFncs, title, globalFilter, filterSensitive)

  def line3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
             height=(330, "px"), options=None, htmlCode=None):
    return self._3d.line(record, y_columns, x_axis, z_axis, profile, width, height, options, htmlCode)
