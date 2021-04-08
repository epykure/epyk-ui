

from epyk.core.html import graph


class ChartGoogle:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Google"

  def plot(self, record=None, y=None, x=None, kind="line", profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

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
    if not isinstance(y, list):
      y = [y]
    return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def line(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
           html_code=None):
    """
    Description:
    ------------
    A line chart that is rendered within the browser using SVG or VML. Displays tooltips when hovering over points.

    :tags:
    :categories:

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/linechart

    Usage:
    -----

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'LineChart'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)
    return line_chart

  def column(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
    """
    Description:
    ------------
    A column chart is a vertical bar chart rendered in the browser using SVG or VML,
    whichever is appropriate for the user's browser.
    Like all Google charts, column charts display tooltips when the user hovers over the data.
    For a horizontal version of this chart, see the bar chart.

    :tags:
    :categories:

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/columnchart

    Usage:
    -----

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'ColumnChart'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts,
                    'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(
      self.page, data, width, height, html_code, options, profile)
    return line_chart

  def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
          html_code=None):
    """
    Description:
    ------------
    Google bar charts are rendered in the browser using SVG or VML, whichever is appropriate for the user's browser.
    Like all Google charts, bar charts display tooltips when the user hovers over the data. For a vertical version of
    this chart, see the column chart.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/barchart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'BarChart'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)
    return line_chart

  def scatter(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    """
    Description:
    ------------
    Scatter charts plot points on a graph.
    When the user hovers over the points, tooltips are displayed with more information.

    Google scatter charts are rendered within the browser using SVG or VML depending on browser capabilities.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/scatterchart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'ScatterChart'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis, options={"agg": options.get('agg', 'distinct')})
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)
    return line_chart

  def histogram(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
                options=None, html_code=None):
    """
    Description:
    ------------
    A histogram is a chart that groups numeric data into bins, displaying the bins as segmented columns.
    They're used to depict the distribution of a dataset: how often values fall into ranges.

    Google Charts automatically chooses the number of bins for you.
    All bins are equal width and have a height proportional to the number of data points in the bin.
    In other respects, histograms are similar to column charts.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/histogram

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'Histogram'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)
    return line_chart

  def area(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
           html_code=None):
    """
    Description:
    ------------
    An area chart that is rendered within the browser using SVG or VML. Displays tips when hovering over points.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/areachart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'AreaChart'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)
    return line_chart

  def bubble(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
    """
    Description:
    ------------
    A bubble chart that is rendered within the browser using SVG or VML. Displays tips when hovering over bubbles.

    A bubble chart is used to visualize a data set with two to four dimensions.
    The first two dimensions are visualized as coordinates, the third as color and the fourth as size.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/bubblechart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'BubbleChart'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)
    return line_chart

  def pie(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
          html_code=None):
    """
    Description:
    ------------
    A pie chart that is rendered within the browser using SVG or VML. Displays tooltips when hovering over slices.

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/piechart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'PieChart'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)
    return line_chart

  def donut(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
            html_code=None):
    """
    Description:
    ------------
    A donut chart that is rendered within the browser using SVG or VML. Displays tooltips when hovering over slices.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/piechart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'PieChart'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)
    return line_chart

  def treemap(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/treemap

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'TreeMap'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)
    return line_chart

  def candlestick(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
                  options=None, html_code=None):
    """
    Description:
    ------------
    A candlestick chart is used to show an opening and closing value overlaid on top of a total variance.
    Candlestick charts are often used to show stock value behavior.
    In this chart, items where the opening value is less than the closing value (a gain) are drawn as filled boxes,
    and items where the opening value is more than the closing value (a loss) are drawn as hollow boxes.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/candlestickchart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'CandlestickChart'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)

    return line_chart

  def gauge(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
            html_code=None):
    """
    Description:
    ------------
    A gauge with a dial, rendered within the browser using SVG or VML.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/gauge

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'Gauge'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)
    return line_chart

  def geo(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
          html_code=None):
    """
    Description:
    ------------
    A geochart is a map of a country, a continent, or a region with areas identified in one of three ways:

      The region mode colors whole regions, such as countries, provinces, or states.
      The markers mode uses circles to designate regions that are scaled according to a value that you specify.
      The text mode labels the regions with identifiers (e.g., "Russia" or "Asia").

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/geochart

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {'type': 'GeoChart'}
    options.update(
      {'y_columns': y_columns, 'x_column': x_axis, 'colors': self.page.theme.charts, 'attrs': {'fill': None}})
    data = self.page.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.page, data, width, height, html_code, options, profile)
    return line_chart
