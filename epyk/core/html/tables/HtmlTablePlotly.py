
from epyk.core.html.graph import GraphPlotly

from epyk.core.js.packages import JsPlotly


class DataHeader(GraphPlotly.DataChart):

  @property
  def align(self):
    return self._attrs["align"]

  @align.setter
  def align(self, val):
    self._attrs["align"] = val

  @property
  def values(self):
    return self._attrs["values"]

  @values.setter
  def values(self, val):
    self._attrs["values"] = val

  @property
  def line(self):
    """

    https://plot.ly/javascript/bubble-maps/

    :rtype: GraphPlotly.DataMarkersLine
    """
    return self.sub_data("line", GraphPlotly.DataMarkersLine)

  @property
  def font(self):
    """

    https://plot.ly/javascript/bubble-maps/

    :rtype: GraphPlotly.DataFont
    """
    return self.sub_data("font", GraphPlotly.DataFont)

  @property
  def fill(self):
    """

    https://plot.ly/javascript/bubble-maps/

    :rtype: GraphPlotly.DataFill
    """
    return self.sub_data("fill", GraphPlotly.DataFill)


class DataCells(GraphPlotly.DataChart):

  @property
  def align(self):
    return self._attrs["align"]

  @align.setter
  def align(self, val):
    self._attrs["align"] = val

  @property
  def values(self):
    return self._attrs["values"]

  @values.setter
  def values(self, val):
    self._attrs["values"] = val

  @property
  def line(self):
    """

    https://plot.ly/javascript/bubble-maps/

    :rtype: GraphPlotly.DataMarkersLine
    """
    return self.sub_data("line", GraphPlotly.DataMarkersLine)

  @property
  def font(self):
    """

    https://plot.ly/javascript/bubble-maps/

    :rtype: GraphPlotly.DataFont
    """
    return self.sub_data("font", GraphPlotly.DataFont)

  @property
  def fill(self):
    """

    https://plot.ly/javascript/bubble-maps/

    :rtype: GraphPlotly.DataFill
    """
    return self.sub_data("fill", GraphPlotly.DataFill)


class DataDomain(GraphPlotly.DataChart):

  @property
  def x(self):
    return self._attrs["x"]

  @x.setter
  def x(self, val):
    self._attrs["x"] = val

  @property
  def y(self):
    return self._attrs["y"]

  @y.setter
  def y(self, val):
    self._attrs["y"] = val


class DataTable(GraphPlotly.DataChart):

  @property
  def domain(self):
    """

    :rtype: DataDomain
    """
    return self.sub_data("domain", DataDomain)

  def set_domain(self, x, y=None):
    self.domain.x = x
    self.domain.y = y or x

  @property
  def columnorder(self):
    return self._attrs["columnorder"]

  @columnorder.setter
  def columnorder(self, val):
    self._attrs["columnorder"] = val

  @property
  def columnwidth(self):
    return self._attrs["columnwidth"]

  @columnwidth.setter
  def columnwidth(self, val):
    self._attrs["columnwidth"] = val

  @property
  def header(self):
    """

    https://plot.ly/javascript/bubble-maps/

    :rtype: DataHeader
    """
    return self.sub_data("header", DataHeader)

  @property
  def cells(self):
    """

    https://plot.ly/javascript/bubble-maps/

    :rtype: DataCells
    """
    return self.sub_data("cells", DataCells)


class Table(GraphPlotly.Chart):

  __reqJs = ['plotly.js']

  @property
  def chart(self):
    """

    :rtype: JsPlotly.Pie
    """
    if self._chart is None:
      self._chart = JsPlotly.Pie(self._report, varName=self.chartId)
    return self._chart

  @property
  def layout(self):
    """

    :rtype: GraphPlotly.Layout
    """
    if self._layout is None:
      self._layout = GraphPlotly.Layout(self._report)
    return self._layout

  @property
  def data(self):
    return self._traces[-1]

  def headers_color(self, colors):
    """
    Description:
    ------------
    Set the background color of the header


    :param colors:
    """
    self.data.header.fill.color = colors
    return self

  def headers_font_color(self, colors):
    """

    :param colors:
    """
    self.data.header.font.color = colors
    return self

  def columns_color(self, colors):
    """

    :param colors:
    """
    self.data.cells.fill.color = colors
    return self

  def columns_font_color(self, colors):
    """

    :param colors:
    """
    self.data.cells.font.color = colors
    return self

  def add_trace(self, data, type='table', mode=None):
    """

    :param data:
    :param type:
    :param mode:
    """
    if type != 'table':
      c_data = dict(data)
      if type is not None:
        c_data['type'] = type
      if mode is not None:
        c_data['mode'] = mode
      trace = GraphPlotly.DataChart(self._report, attrs=c_data)
    else:
      c_data = {}
      if type is not None:
        c_data['type'] = type
      if mode is not None:
        c_data['mode'] = mode
      trace = DataTable(self._report, attrs=c_data)
      trace.cells.values = data
    self._traces.append(trace)
    return self

  @property
  def _js__convertor__(self):
    # TODO implement the else statement
    return '''
        if(data.python){
          var dataset = {type: options.type, mode: data.mode = options.mode, cells: {values: data.values}, header: {values: data.header}}; 
          if(typeof options.attrs !== undefined){ for(var attr in options.attrs){dataset[attr] = options.attrs[attr]} };
          if(typeof options.marker !== undefined){ for(var attr in options.marker){dataset.marker[attr] = options.marker[attr]} }; 
          result = [dataset];
        } else { }'''
