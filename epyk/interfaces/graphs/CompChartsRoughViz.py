
from epyk.core.html import graph
from epyk.interfaces import Arguments


class CompRoughViz:

  def __init__(self, ui):
    self.page = ui.page

  def plot(self, record=None, y=None, x=None, kind="line", profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """ Create a roughViz chart component.

    Related Pages:

      https://github.com/jwilber/roughViz

    :tags:
    :categories:

    Related Pages:

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
    if y is not None and not isinstance(y, list):
      y = [y]
    return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """ Create a roughViz line component.

    Related Pages:

      https://github.com/jwilber/roughViz

    TODO: Find answer for https://stackoverflow.com/questions/67456146/input-data-for-line-chart-in-roughviz

    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    line_chart = graph.GraphRoughViz.RoughViz(self.page, width, height, html_code, options, profile)
    line_chart.style.css.inline()
    line_chart.options.height = height[0]
    line_chart.options.xLabel = x_axis
    if width[1] != "%":
      line_chart.options.width = width[0]
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.options.data.labels = [i for i in range(len(data["labels"]))]
    for i, dataset in enumerate(data["datasets"]):
      line_chart.options.data.add(data["series"][i], dataset)
    return line_chart

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    """ Create a roughViz scatter component.

    Related Pages:

      https://github.com/jwilber/roughViz

    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    line_chart = graph.GraphRoughViz.RoughVizScatter(self.page, width, height, html_code, options, profile)
    line_chart.style.css.inline()
    line_chart.options.height = height[0]
    line_chart.options.xLabel = x_axis
    if width[1] != "%":
      line_chart.options.width = width[0]
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.options.data.x = [i for i in range(len(data["labels"]))]
    line_chart.options.data.y = data["datasets"][0]
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """ Create a roughViz bar component.

    Related Pages:

      https://github.com/jwilber/roughViz

    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    line_chart = graph.GraphRoughViz.RoughVizBar(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.style.css.inline()
    if width[1] != "%":
      line_chart.options.width = width[0]
    line_chart.options.xLabel = x_axis
    if y_columns is not None and len(y_columns) == 1:
      line_chart.options.yLabel = y_columns[0]
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.options.data.labels = data["labels"]
    line_chart.options.data.values = data["datasets"][0]
    return line_chart

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """ Create a roughViz Horizontal bar component.

    Related Pages:

      https://github.com/jwilber/roughViz

    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    line_chart = graph.GraphRoughViz.RoughVizBar(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.style.css.inline()
    if width[1] != "%":
      line_chart.options.width = width[0]
    line_chart.options.xLabel = x_axis
    if y_columns is not None and len(y_columns) == 1:
      line_chart.options.yLabel = y_columns[0]
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.options.data.labels = data["labels"]
    line_chart.options.data.values = data["datasets"][0]
    return line_chart

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """ Create a roughViz pie component.

    Related Pages:

      https://github.com/jwilber/roughViz

    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    line_chart = graph.GraphRoughViz.RoughVizPie(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.style.css.inline()
    line_chart.options.xLabel = x_axis
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    if width[1] != "%":
      line_chart.options.width = width[0]
    if y_columns is not None and len(y_columns) == 1:
      line_chart.options.yLabel = y_columns[0]
    line_chart.options.data.labels = data["labels"]
    line_chart.options.data.values = data["datasets"][0]
    return line_chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """ Create a roughViz donut component.

    Related Pages:

      https://github.com/jwilber/roughViz

    :param record: List. Optional. The list of dictionaries with the input data.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    line_chart = graph.GraphRoughViz.RoughVizDonut(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.style.css.inline()
    if width[1] != "%":
      line_chart.options.width = width[0]
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.options.xLabel = x_axis
    if y_columns is not None and len(y_columns) == 1:
      line_chart.options.yLabel = y_columns[0]
    line_chart.options.data.labels = data["labels"]
    line_chart.options.data.values = data["datasets"][0]
    return line_chart
