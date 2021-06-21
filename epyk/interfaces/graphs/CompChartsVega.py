

from epyk.core.html import graph


class VegaEmbedded:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Vega"

  def plot(self, record=None, y=None, x=None, kind="line", profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y: List | String. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param kind: String. Optional. The chart type.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    line_chart = graph.GraphVega.VegaEmdedCharts(self.page, [], width, height, html_code, options, profile)
    line_chart.options.spec.mark = kind
    if width[1] == "px":
      line_chart.options.width = width[0]
    else:
      line_chart.options.parent_width(width[0] - 5)
    if height[1] == "px":
      line_chart.options.height = height[0]

    if record is not None:
      line_chart.options.data.name = "table"
      line_chart.options.data.values = record

    if x is not None:
      xaxis = line_chart.options.spec.encoding.x
      xaxis.field = x
      xaxis.bind = True
      xaxis.type = "nominal"

    if y is not None:
      line_chart.options.repeat.layer = y
      yaxis = line_chart.options.spec.encoding.y
      yaxis.field = {"repeat": "layer"}
      yaxis.type = "quantitative"
      yaxis.aggregate = "sum"

    caxis = line_chart.options.spec.encoding.color
    caxis.datum = {"repeat": "layer"}
    caxis.type = "nominal"

    caxis.legend.orient = "bottom"
    return line_chart

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    return self.plot(record, y_columns, x_axis, kind="line", profile=profile, width=width, height=height,
                     options=options, html_code=html_code)

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):

    line_chart = graph.GraphVega.VegaEmdedCharts(self.page, [], width, height, html_code, options, profile)
    data_layer = line_chart.options.add_layer()

    if width[1] == "px":
      line_chart.options.width = width[0]
    else:
      line_chart.options.parent_width(width[0] - 5)
    if height[1] == "px":
      line_chart.options.height = height[0]

    if record is not None:
      data_layer.data.name = "table"
      data_layer.data.values = record

    if x_axis is not None:
      xaxis = data_layer.encoding.x
      xaxis.field = x_axis
      xaxis.bind = True
      xaxis.type = "nominal"

    if y_columns is not None:
      data_layer.repeat.layer = y_columns
      yaxis = data_layer.encoding.y
      yaxis.field = {"repeat": "layer"}
      yaxis.type = "quantitative"
      yaxis.aggregate = "sum"

    caxis = data_layer.encoding.color
    caxis.datum = {"repeat": "layer"}
    caxis.type = "nominal"
    caxis.legend.orient = "bottom"

    mark_layer = data_layer.add_layer()
    mark_layer.add_mark("bar")
    return line_chart
    #return self.plot(record, y_columns, x_axis, kind="bar", profile=profile, width=width, height=height,
    #                 options=options, html_code=html_code)

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    return self.plot(record, y_columns, x_axis, kind="point", profile=profile, width=width, height=height,
                     options=options, html_code=html_code)
