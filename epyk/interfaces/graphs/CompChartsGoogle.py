

from epyk.core.html import graph


class ChartGoogle(object):

  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Google"

  def line(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    A line chart that is rendered within the browser using SVG or VML. Displays tooltips when hovering over points.

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/linechart

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'LineChart'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)
    return line_chart

  def column(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    A column chart is a vertical bar chart rendered in the browser using SVG or VML, whichever is appropriate for the user's browser.
    Like all Google charts, column charts display tooltips when the user hovers over the data. For a horizontal version of this chart, see the bar chart.

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/columnchart

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'ColumnChart'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts,
                    'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options,
                                             profile)
    return line_chart

  def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Google bar charts are rendered in the browser using SVG or VML, whichever is appropriate for the user's browser.
    Like all Google charts, bar charts display tooltips when the user hovers over the data. For a vertical version of this chart, see the column chart.

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/barchart

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'BarChart'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)
    return line_chart

  def scatter(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    Scatter charts plot points on a graph. When the user hovers over the points, tooltips are displayed with more information.

    Google scatter charts are rendered within the browser using SVG or VML depending on browser capabilities.

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/scatterchart

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'ScatterChart'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)
    return line_chart

  def histogram(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    A histogram is a chart that groups numeric data into bins, displaying the bins as segmented columns.
    They're used to depict the distribution of a dataset: how often values fall into ranges.

    Google Charts automatically chooses the number of bins for you.
    All bins are equal width and have a height proportional to the number of data points in the bin.
    In other respects, histograms are similar to column charts.

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/histogram

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'Histogram'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)
    return line_chart

  def area(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    An area chart that is rendered within the browser using SVG or VML. Displays tips when hovering over points.

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/areachart

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'AreaChart'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)
    return line_chart

  def bubble(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    A bubble chart that is rendered within the browser using SVG or VML. Displays tips when hovering over bubbles.

    A bubble chart is used to visualize a data set with two to four dimensions.
    The first two dimensions are visualized as coordinates, the third as color and the fourth as size.

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/bubblechart

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'BubbleChart'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)
    return line_chart

  def pie(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    A pie chart that is rendered within the browser using SVG or VML. Displays tooltips when hovering over slices.

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/piechart

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'PieChart'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)
    return line_chart

  def treemap(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/treemap

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'TreeMap'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)
    return line_chart

  def candlestick(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    A candlestick chart is used to show an opening and closing value overlaid on top of a total variance. Candlestick charts are often used to show stock value behavior.
    In this chart, items where the opening value is less than the closing value (a gain) are drawn as filled boxes, and items where the opening value is more than the closing value (a loss) are drawn as hollow boxes.

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/candlestickchart

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'CandlestickChart'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)

    return line_chart

  def gauge(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    A gauge with a dial, rendered within the browser using SVG or VML.

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/gauge

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'Gauge'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)
    return line_chart

  def geo(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    ------------
    A geochart is a map of a country, a continent, or a region with areas identified in one of three ways:

      The region mode colors whole regions, such as countries, provinces, or states.
      The markers mode uses circles to designate regions that are scaled according to a value that you specify.
      The text mode labels the regions with identifiers (e.g., "Russia" or "Asia").

    Related Pages:

      https://developers.google.com/chart/interactive/docs/gallery/geochart

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    """
    options = options or {'type': 'GeoChart'}
    options.update({'y_columns': y_columns, 'x_column': x_axis, 'colors': self.parent.context.rptObj.theme.charts, 'attrs': {'fill': None}})
    data = self.parent.context.rptObj.data.google.y(record, y_columns, x_axis)
    line_chart = graph.GraphGoogle.ChartLine(self.parent.context.rptObj, data, width, height, htmlCode, options, profile)
    return line_chart
