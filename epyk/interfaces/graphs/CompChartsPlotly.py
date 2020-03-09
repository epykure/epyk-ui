
import sys

from epyk.core.html import graph


class Plotly(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Plotly"

  def line(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
           width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    line_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    line_chart.options.responsive = True
    self.parent.context.register(line_chart)
    for d in data:
      line_chart.add_trace(d)
    return line_chart

  def bar(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
          width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    bar_chart = graph.GraphPlotly.Bar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(bar_chart)
    for d in data:
      bar_chart.add_trace(d)
    return bar_chart

  def hbar(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
          width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    bar_chart = graph.GraphPlotly.Bar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(bar_chart)
    for d in data:
      bar_chart.add_trace(d, type='bar')
      bar_chart.data.orientation = 'h'
    return bar_chart

  def scatter(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    sc_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(sc_chart)
    for d in data:
      sc_chart.add_trace(d, mode='markers')
    return sc_chart

  def scattergl(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    sc_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(sc_chart)
    for d in data:
      sc_chart.add_trace(d, type="scattergl", mode='markers')
    return sc_chart

  def histogram(self, record, y_columns=None, x_columns=None, title=None, filters=None, profile=None, options=None,
                width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:

    :return:

    :rtype: graph.GraphPlotly.Chart
    """
    data = []
    histo_axis = ('y', y_columns) if y_columns is not None else ('x', x_columns)
    for rec in record:
      for y in histo_axis[1]:
        series = {histo_axis[0]: []}
        if y in rec:
          series[histo_axis[0]].append(float(rec[y]))
        data.append(series)
    histo_chart = graph.GraphPlotly.Bar(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(histo_chart)

    for d in data:
      histo_chart.add_trace(d, type='histogram')
    return histo_chart

  def pie(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    data = []
    for c in y_columns:
      series = {'labels': [], 'values': []}
      for x, y in agg_data[c].items():
        series['labels'].append(x)
        series['values'].append(y)
      data.append(series)

    pie_chart = graph.GraphPlotly.Pie(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(pie_chart)
    for d in data:
      pie_chart.add_trace(d)
    return pie_chart

  def area(self, record, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param record:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    agg_data = {}
    for rec in record:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data[c].items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)

    line_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(line_chart)
    for d in data:
      line_chart.add_trace(d)
      line_chart.data.type = "scatter"
      line_chart.data.fill = "tozeroy"
    return line_chart

  def bubble(self, data=None, y_columns=None, x_axis=None, title=None, filters=None, profile=None, options=None,
              width=(100, "%"), height=(330, "px"), htmlCode=None):
    """

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#common-parameters
    https://plot.ly/javascript/

    :param data:
    :param title:
    :param profile:
    :param width:
    :param height:
    :param htmlCode:
    """
    line_chart = graph.GraphPlotly.Line(self.parent.context.rptObj, width, height, title, options or {}, htmlCode, filters, profile)
    self.parent.context.register(line_chart)
    line_chart.add_trace({
      "x": [1, 2, 3, 4], "y": [12, 9, 15, 12]}, mode="markers")
    line_chart.data.marker.size = [40, 60, 80, 100]
    line_chart.data.marker.color = ['green', 'red']
    return line_chart
