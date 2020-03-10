
from epyk.core.html import Html
from epyk.core.html.options import OptPlotly

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject

from epyk.core.data import DataClass

from epyk.core.js.packages import JsPlotly
from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name, category, callFnc = 'Plotly', 'Charts', 'plotly'

  def __init__(self,  report, width, height, title, options, htmlCode, filters, profile):
    self.seriesProperties, self.__chartJsEvents, self.height = {'static': {}, 'dynamic': {}}, {}, height[0]
    super(Chart, self).__init__(report, [], code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self._attrs, self._traces, self._layout, self._options = None, None, [], None, None
    self._options_init = options

  @property
  def chartId(self):
    """
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlId

  @property
  def data(self):
    return self._traces[-1]

  @property
  def options(self):
    """

    :rtype: Options
    :return:
    """
    if self._options is None:
      self._options = OptPlotly.OptionConfig(self._report, attrs=self._options_init)
    return self._options

  def traces(self, i=None):
    """

    :rtype: JsChartJs.DataSetPie
    """
    if i is None:
      return self._traces[-1]

    return self._traces[i]

  @property
  def layout(self):
    if self._layout is None:
      self._layout = Layout(self._report)
    return self._layout

  @property
  def d3(self):
    if self._d3 is None:
      self._d3 = JsD3.D3Select(self._report, id="#%s" % self.htmlId)
    return self._d3

  def add_trace(self, data, type=None, mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(DataChart(self._report, attrs=c_data))
    return self

  @property
  def chart(self):
    raise Exception("Chart object should be defined in the configuration")

  def build(self, data=None, options=None, profile=False):
    str_traces = []
    for t in self._traces:
      str_traces.append("{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in t.items()]))
    obj_datasets = JsObject.JsObject.get("[%s]" % ", ".join(str_traces))
    return JsUtils.jsConvertFncs([JsPlotly.JsPlotly(src=self._report).newPlot(self.htmlId, obj_datasets, self.layout, self.options)], toStr=True)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class Line(Chart):
  __reqJs = ['plotly.js']

  @property
  def chart(self):
    """
    :rtype: JsPlotly.Line
    """
    if self._chart is None:
      self._chart = JsPlotly.Line(self._report, varName=self.chartId)
    return self._chart

  def add_trace(self, data, type=None, mode='lines+markers'):
    return super(Line, self).add_trace(data, type, mode)


class Bar(Chart):
  __reqJs = ['plotly.js']

  @property
  def chart(self):
    """
    :rtype: JsPlotly.Bar
    """
    if self._chart is None:
      self._chart = JsPlotly.Bar(self._report, varName=self.chartId)
    return self._chart

  @property
  def layout(self):
    if self._layout is None:
      self._layout = LayoutBar(self._report)
    return self._layout

  def add_trace(self, data, type='bar', mode=None):
    return super(Bar, self).add_trace(data, type, mode)


class LayoutAxis(DataClass):

  @property
  def autorange(self):
    return self._attrs["autorange"]

  @autorange.setter
  def autorange(self, val):
    self._attrs["autorange"] = val

  @property
  def range(self):
    return self._attrs["range"]

  @range.setter
  def range(self, val):
    self._attrs["range"] = val

  @property
  def type(self):
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    self._attrs["type"] = val


class LayoutMargin(DataClass):

  @property
  def l(self):
    return self._attrs["l"]

  @l.setter
  def l(self, val):
    self._attrs["l"] = val

  @property
  def r(self):
    return self._attrs["r"]

  @r.setter
  def r(self, val):
    self._attrs["r"] = val

  @property
  def b(self):
    return self._attrs["b"]

  @b.setter
  def b(self, val):
    self._attrs["b"] = val

  @property
  def t(self):
    return self._attrs["t"]

  @t.setter
  def t(self, val):
    self._attrs["t"] = val


class LayoutEye(DataClass):

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

  @property
  def z(self):
    return self._attrs["z"]

  @z.setter
  def z(self, val):
    self._attrs["z"] = val


class LayoutCamera(DataClass):

  @property
  def eye(self):
    return self.sub_data("eye", LayoutEye)


class LayoutScene(DataClass):

  @property
  def camera(self):
    return self.sub_data("scene", LayoutCamera)


class Layout(DataClass):

  @property
  def title(self):
    return self._attrs["title"]

  @title.setter
  def title(self, val):
    self._attrs["title"] = val

  @property
  def showlegend(self):
    return self._attrs["showlegend"]

  @showlegend.setter
  def showlegend(self, val):
    self._attrs["showlegend"] = val

  @property
  def height(self):
    return self._attrs["height"]

  @height.setter
  def height(self, val):
    self._attrs["height"] = val

  @property
  def width(self):
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val

  @property
  def scene(self):
    """

    """
    return self.sub_data("scene", LayoutScene)

  @property
  def xaxis(self):
    """

    https://plot.ly/javascript/time-series/
    """
    return self.sub_data("xaxis", LayoutAxis)

  @property
  def yaxis(self):
    """

    https://plot.ly/javascript/time-series/
    """
    return self.sub_data("yaxis", LayoutAxis)

  @property
  def margin(self):
    """

    https://plot.ly/javascript/3d-surface-plots/
    """
    return self.sub_data("margin", LayoutMargin)


class LayoutBar(Layout):

  @property
  def barmode(self):
    return self._attrs["barmode"]

  @barmode.setter
  def barmode(self, val):
    self._attrs["barmode"] = val


class DataMarkersLine(DataClass):

  @property
  def width(self):
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val

  @property
  def color(self):
    return self._attrs["color"]

  @color.setter
  def color(self, val):
    self._attrs["color"] = val


class DataMarkers(DataClass):

  @property
  def size(self):
    return self._attrs["size"]

  @size.setter
  def size(self, val):
    self._attrs["size"] = val

  @property
  def symbol(self):
    return self._attrs["symbol"]

  @symbol.setter
  def symbol(self, val):
    self._attrs["symbol"] = val

  @property
  def sizemode(self):
    return self._attrs["sizemode"]

  @sizemode.setter
  def sizemode(self, val):
    self._attrs["sizemode"] = val

  @property
  def color(self):
    return self._attrs["color"]

  @color.setter
  def color(self, val):
    self._attrs["color"] = val

  @property
  def opacity(self):
    return self._attrs["opacity"]

  @opacity.setter
  def opacity(self, val):
    self._attrs["opacity"] = val

  @property
  def width(self):
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val

  @property
  def line(self):
    """

    https://plot.ly/javascript/webgl-vs-svg/
    """
    return self.sub_data("line", DataMarkersLine)


class DataChart(DataClass):

  @property
  def hole(self):
    return self._attrs["hole"]

  @hole.setter
  def hole(self, val):
    self._attrs["hole"] = val

  @property
  def name(self):
    return self._attrs["name"]

  @name.setter
  def name(self, val):
    self._attrs["name"] = val

  @property
  def fill(self):
    return self._attrs["fill"]

  @fill.setter
  def fill(self, val):
    self._attrs["fill"] = val

  @property
  def orientation(self):
    return self._attrs["orientation"]

  @orientation.setter
  def orientation(self, val):
    self._attrs["orientation"] = val

  @property
  def marker(self):
    """

    https://plot.ly/javascript/bubble-charts/
    """
    return self.sub_data("marker", DataMarkers)


class DataPie(DataChart):

  @property
  def hole(self):
    return self._attrs["hole"]

  @hole.setter
  def hole(self, val):
    self._attrs["hole"] = val

  @property
  def hoverinfo(self):
    return self._attrs["hoverinfo"]

  @hoverinfo.setter
  def hoverinfo(self, val):
    self._attrs["hoverinfo"] = val

  @property
  def text(self):
    return self._attrs["text"]

  @text.setter
  def text(self, val):
    self._attrs["text"] = val

  @property
  def textposition(self):
    return self._attrs["textposition"]

  @textposition.setter
  def textposition(self, val):
    self._attrs["textposition"] = val


class DataProject(DataChart):

  @property
  def z(self):
    return self._attrs["z"]

  @z.setter
  def z(self, val):
    self._attrs["z"] = val


class DataZ(DataChart):

  @property
  def show(self):
    return self._attrs["show"]

  @show.setter
  def show(self, val):
    self._attrs["show"] = val

  @property
  def usecolormap(self):
    return self._attrs["usecolormap"]

  @usecolormap.setter
  def usecolormap(self, val):
    self._attrs["usecolormap"] = val

  @property
  def highlightcolor(self):
    return self._attrs["highlightcolor"]

  @highlightcolor.setter
  def highlightcolor(self, val):
    self._attrs["highlightcolor"] = val

  @property
  def project(self):
    """

    https://plot.ly/javascript/3d-surface-plots/
    """
    return self.sub_data("project", DataProject)


class DataContours(DataChart):

  @property
  def z(self):
    """

    https://plot.ly/javascript/3d-surface-plots/
    """
    return self.sub_data("z", DataZ)


class DataSurface(DataChart):

  @property
  def showscale(self):
    return self._attrs["showscale"]

  @showscale.setter
  def showscale(self, val):
    self._attrs["showscale"] = val

  @property
  def contours(self):
    """

    https://plot.ly/javascript/3d-surface-plots/
    """
    return self.sub_data("contours", DataContours)


class Pie(Chart):

  __reqJs = ['plotly.js']

  @property
  def chart(self):
    """
    :rtype: JsPlotly.Bar
    """
    if self._chart is None:
      self._chart = JsPlotly.Pie(self._report, varName=self.chartId)
    return self._chart

  @property
  def data(self):
    return self._traces[-1]

  def add_trace(self, data, type='pie', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(DataPie(self._report, attrs=c_data))
    return self


class Surface(Chart):
  __reqJs = ['plotly.js']

  @property
  def chart(self):
    """
    :rtype: JsPlotly.Bar
    """
    if self._chart is None:
      self._chart = JsPlotly.Pie(self._report, varName=self.chartId)
    return self._chart

  @property
  def data(self):
    return self._traces[-1]

  def add_trace(self, data, type='surface', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(DataSurface(self._report, attrs=c_data))
    return self


class Mesh3d(Chart):
  __reqJs = ['plotly.js']

  @property
  def chart(self):
    """
    :rtype: JsPlotly.Bar
    """
    if self._chart is None:
      self._chart = JsPlotly.Pie(self._report, varName=self.chartId)
    return self._chart

  @property
  def data(self):
    return self._traces[-1]

  def add_trace(self, data, type='mesh3d', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(DataSurface(self._report, attrs=c_data))
    return self
