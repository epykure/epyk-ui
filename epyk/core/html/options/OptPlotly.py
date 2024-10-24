
from epyk.core.html.options import OptChart
from epyk.core.data.DataClass import DataClass


class OptionsChartSharedPlotly(OptChart.OptionsChartShared):

  def x_format(self, js_funcs, profile=None):
    pass

  def x_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    pass

  def x_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    pass

  def x_label(self, value):
    """   Set the label of the x axis.
 
    :param value: String. The axis label.
    """
    pass

  def x_tick_count(self, num):
    return self

  def y_format(self, js_funcs, profile=None):
    pass

  def y_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
    pass

  def y_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
    pass

  def y_label(self, value):
    """   Set the label of the y axis.
 
    :param value: String. The axis label.
    """
    pass

  def y_tick_count(self, num):
    return self


class OptionConfig(OptChart.OptionsChart):

  @property
  def mode(self):
    """

    Usage::

    """
    return self._config_get(None)

  @mode.setter
  def mode(self, value):
    self._config(value)

  @property
  def responsive(self):
    """

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self._config_get(True)

  @responsive.setter
  def responsive(self, val):
    self._config(val)

  @property
  def displayModeBar(self):
    """

    Related Pages:

      https://plotly.com/javascript/configuration-options/
    """
    return self._config_get(True)

  @displayModeBar.setter
  def displayModeBar(self, flag):
    self._config(flag)

  @property
  def editable(self):
    """

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self._config_get(False)

  @editable.setter
  def editable(self, val):
    self._config(val)

  @property
  def staticPlot(self):
    """

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self._config_get(None)

  @staticPlot.setter
  def staticPlot(self, val):
    self._config(val)

  @property
  def scrollZoom(self):
    """

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self._config_get(None)

  @scrollZoom.setter
  def scrollZoom(self, val):
    self._config(val)

  @property
  def mapboxAccessToken(self):
    """

    Related Pages:

      https://plot.ly/javascript/configuration-options/
    """
    return self._config_get(None)

  @mapboxAccessToken.setter
  def mapboxAccessToken(self, val):
    self._config(val)


class DataFill(DataClass):

  @property
  def color(self):
    return self._attrs["color"]

  @color.setter
  def color(self, val):
    self._attrs["color"] = val


class LayoutAnnotation(DataClass):

  @property
  def xanchor(self):
    return self._attrs["xanchor"]

  @xanchor.setter
  def xanchor(self, val):
    self._attrs["xanchor"] = val

  @property
  def ax(self):
    return self._attrs["ax"]

  @ax.setter
  def ax(self, val):
    self._attrs["ax"] = val

  @property
  def ay(self):
    return self._attrs["ay"]

  @ay.setter
  def ay(self, val):
    self._attrs["ay"] = val

  @property
  def text(self):
    return self._attrs["text"]

  @text.setter
  def text(self, val):
    self._attrs["text"] = val

  @property
  def showarrow(self):
    return self._attrs["showarrow"]

  @showarrow.setter
  def showarrow(self, val):
    self._attrs["showarrow"] = val

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
  def xref(self):
    return self._attrs["xref"]

  @xref.setter
  def xref(self, val):
    self._attrs["xref"] = val

  @property
  def yref(self):
    return self._attrs["yref"]

  @yref.setter
  def yref(self, val):
    self._attrs["yref"] = val

  @property
  def font(self):
    return self.sub_data("font", DataFont)


class LayoutShape(DataClass):

  def add_path(self, points, color: str = None):
    """

    https://plot.ly/javascript/shapes/

    :param points:
    :param color:
    """
    self._attrs.update({'type': 'path', 'path': points})
    self.fillcolor = color or self.page.theme.warning.light
    return self

  def add_line(self, x, y, x1, y1, opacity=0.2, color=None):
    """

    .layout.shapes.add_line(-100, 10, -50, -10, color="red")

    :param x:
    :param y:
    :param x1:
    :param y1:
    :param opacity:
    :param color:
    """
    self._attrs.update({'type': 'line', 'xref': 'x', 'yref': 'y', 'x0': x, 'y0': y, 'x1': x1, 'y1': y1})
    self.line.color = color or self.page.theme.warning.light
    self.line.dash = 'dot'
    self.opacity = opacity
    return self

  def add_circle(self, x, y, x1, y1, opacity=0.2, color=None):
    """

    :param x:
    :param y:
    :param x1:
    :param y1:
    :param opacity:
    :param color:
    """
    self._attrs.update({'type': 'circle', 'xref': 'x', 'yref': 'y', 'x0': x, 'y0': y, 'x1': x1, 'y1': y1})
    self.fillcolor = color or self.page.theme.warning.light
    self.line.width = 0
    self.opacity = opacity
    return self

  def add_rect(self, x, y, x1, y1, opacity=0.2, color=None):
    """

    :param x:
    :param y:
    :param x1:
    :param y1:
    :param opacity:
    :param color:
    """
    self._attrs.update({'type': 'rect', 'xref': 'x', 'yref': 'paper', 'x0': x, 'y0': y, 'x1': x1, 'y1': y1})
    self.fillcolor = color or self.page.theme.warning.light
    self.line.width = 0
    self.opacity = opacity
    return self

  @property
  def type(self):
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    self._attrs["type"] = val

  @property
  def xref(self):
    return self._attrs["xref"]

  @xref.setter
  def xref(self, val):
    self._attrs["xref"] = val

  @property
  def yref(self):
    return self._attrs["yref"]

  @yref.setter
  def yref(self, val):
    self._attrs["yref"] = val

  @property
  def x0(self):
    return self._attrs["x0"]

  @x0.setter
  def x0(self, val):
    self._attrs["x0"] = val

  @property
  def y0(self):
    return self._attrs["y0"]

  @y0.setter
  def y0(self, val):
    self._attrs["y0"] = val

  @property
  def x1(self):
    return self._attrs["x1"]

  @x1.setter
  def x1(self, val):
    self._attrs["x1"] = val

  @property
  def y1(self):
    return self._attrs["y1"]

  @y1.setter
  def y1(self, val):
    self._attrs["y1"] = val

  @property
  def fillcolor(self):
    return self._attrs["fillcolor"]

  @fillcolor.setter
  def fillcolor(self, val):
    self._attrs["fillcolor"] = val

  @property
  def opacity(self):
    return self._attrs["opacity"]

  @opacity.setter
  def opacity(self, val):
    self._attrs["opacity"] = val

  @property
  def line(self):
    """

    :rtype: DataMarkersLine
    """
    return self.sub_data("line", DataMarkersLine)


class LayoutFont(DataClass):

  @property
  def color(self):
    """

    :prop color: color or array of colors
    """
    return self._attrs["color"]

  @color.setter
  def color(self, val):
    self._attrs["color"] = val

  @property
  def family(self):
    """
    HTML font family - the typeface that will be applied by the web browser.

    https://plot.ly/javascript/reference/#pie-outsidetextfont-family

    :prop font-family:  string or array of strings
    """
    return self._attrs["family"]

  @family.setter
  def family(self, val):
    self._attrs["family"] = val

  @property
  def size(self):
    """

    https://plot.ly/javascript/reference/#pie-outsidetextfont-family

    :return: number or array of numbers greater than or equal to 1
    """
    return self._attrs["size"]

  @size.setter
  def size(self, val):
    self._attrs["size"] = val


class LayoutGrid(DataClass):

  @property
  def rows(self):
    return self._attrs["rows"]

  @rows.setter
  def rows(self, val):
    self._attrs["rows"] = val

  @property
  def columns(self):
    return self._attrs["columns"]

  @columns.setter
  def columns(self, val):
    self._attrs["columns"] = val

  @property
  def pattern(self):
    return self._attrs["pattern"]

  @pattern.setter
  def pattern(self, val):
    self._attrs["pattern"] = val


class LayoutButtons(DataClass):

  @property
  def count(self):
    return self._attrs["count"]

  @count.setter
  def count(self, val):
    self._attrs["count"] = val

  @property
  def label(self):
    return self._attrs["label"]

  @label.setter
  def label(self, val):
    self._attrs["label"] = val

  @property
  def step(self):
    return self._attrs["step"]

  @step.setter
  def step(self, val):
    self._attrs["step"] = val

  @property
  def stepmode(self):
    return self._attrs["stepmode"]

  @stepmode.setter
  def stepmode(self, val):
    self._attrs["stepmode"] = val


class LayoutRangeSelector(DataClass):

  @property
  def buttons(self) -> LayoutButtons:
    """

    https://plot.ly/javascript/time-series/
    https://plot.ly/javascript/range-slider/

    :rtype: LayoutButtons
    """
    return self.sub_data_enum("buttons", LayoutButtons)

  def month(self, n):
    but = self.buttons
    but.step = 'month'
    but.stepmode = 'backward'
    but.count = n
    but.label = "%sm" % n
    return self

  def year(self, n=0):
    but = self.buttons
    but.step = 'year'
    but.count = n
    but.stepmode = 'todate' if n == 0 else 'backward'
    but.label = 'YTD' if n == 0 else "%sy" % n
    return self

  def all(self):
    but = self.buttons
    but.step = 'all'
    return self


class LayoutRangeSlider(DataClass):

  @property
  def range(self):
    return self._attrs["range"]

  @range.setter
  def range(self, val):
    self._attrs["range"] = val


class LayoutAxis(DataClass):

  @property
  def title(self):
    return self._attrs["title"]

  @title.setter
  def title(self, val):
    self._attrs["title"] = val

  @property
  def showbackground(self):
    return self._attrs["showbackground"]

  @showbackground.setter
  def showbackground(self, val):
    self._attrs["showbackground"] = val

  @property
  def backgroundcolor(self):
    return self._attrs["backgroundcolor"]

  @backgroundcolor.setter
  def backgroundcolor(self, val):
    self._attrs["backgroundcolor"] = val

  @property
  def tickangle(self):
    return self._attrs["tickangle"]

  @tickangle.setter
  def tickangle(self, val):
    self._attrs["tickangle"] = val

  @property
  def titlefont(self) -> LayoutFont:
    """

    :rtype: LayoutFont

    :return:
    """
    return self.sub_data("titlefont", LayoutFont)

  @property
  def tickfont(self) -> LayoutFont:
    """

    :rtype: LayoutFont

    :return:
    """
    return self.sub_data("tickfont", LayoutFont)

  def set_color(self, color):
    """

    :param color:
    """
    self.titlefont.color = color
    self.tickfont.color = color
    return self

  @property
  def overlaying(self):
    return self._attrs["overlaying"]

  @overlaying.setter
  def overlaying(self, val):
    self._attrs["overlaying"] = val

  @property
  def side(self):
    return self._attrs["side"]

  @side.setter
  def side(self, val):
    self._attrs["side"] = val

  @property
  def anchor(self):
    return self._attrs["anchor"]

  @anchor.setter
  def anchor(self, val):
    self._attrs["anchor"] = val

  @property
  def domain(self):
    return self._attrs["domain"]

  @domain.setter
  def domain(self, val):
    self._attrs["domain"] = val

  @property
  def dtick(self):
    return self._attrs["dtick"]

  @dtick.setter
  def dtick(self, val):
    self._attrs["dtick"] = val

  @property
  def autorange(self):
    return self._attrs["autorange"]

  @autorange.setter
  def autorange(self, val):
    self._attrs["autorange"] = val

  @property
  def position(self):
    return self._attrs["position"]

  @position.setter
  def position(self, val):
    self._attrs["position"] = val

  @property
  def paper_bgcolor(self):
    return self._attrs["paper_bgcolor"]

  @paper_bgcolor.setter
  def paper_bgcolor(self, val):
    self._attrs["paper_bgcolor"] = val

  @property
  def plot_bgcolor(self):
    return self._attrs["plot_bgcolor"]

  @plot_bgcolor.setter
  def plot_bgcolor(self, val):
    self._attrs["plot_bgcolor"] = val

  @property
  def range(self):
    return self._attrs["range"]

  @range.setter
  def range(self, val):
    self._attrs["range"] = val

  @property
  def gridcolor(self):
    return self._attrs["gridcolor"]

  @gridcolor.setter
  def gridcolor(self, val):
    self._attrs["gridcolor"] = val

  @property
  def gridwidth(self):
    return self._attrs["gridwidth"]

  @gridwidth.setter
  def gridwidth(self, val):
    self._attrs["gridwidth"] = val

  @property
  def type(self):
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    self._attrs["type"] = val

  @property
  def zeroline(self):
    return self._attrs["zeroline"]

  @zeroline.setter
  def zeroline(self, val):
    self._attrs["zeroline"] = val

  @property
  def showline(self):
    return self._attrs["showline"]

  @showline.setter
  def showline(self, val):
    self._attrs["showline"] = val

  @property
  def showgrid(self):
    return self._attrs["showgrid"]

  @showgrid.setter
  def showgrid(self, val):
    self._attrs["showgrid"] = val

  @property
  def showticklabels(self):
    return self._attrs["showticklabels"]

  @showticklabels.setter
  def showticklabels(self, val):
    self._attrs["showticklabels"] = val

  @property
  def rangeselector(self) -> LayoutRangeSelector:
    """

    https://plot.ly/javascript/time-series/

    :rtype: LayoutRangeSelector
    """
    return self.sub_data("rangeselector", LayoutRangeSelector)

  @property
  def rangeslider(self) -> LayoutRangeSlider:
    """

    https://plot.ly/javascript/time-series/

    :rtype: LayoutRangeSlider
    """
    return self.sub_data("rangeslider", LayoutRangeSlider)


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

  def clear(self, l=0, r=0, b=0, t=0):
    self.l = l
    self.r = r
    self.b = b
    self.t = t


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
  def eye(self) -> LayoutEye:
    """

    :rtype: LayoutEye

    :return:
    """
    return self.sub_data("eye", LayoutEye)


class LayoutScene(DataClass):

  @property
  def camera(self) -> LayoutCamera:
    """

    :rtype: LayoutCamera

    :return:
    """
    return self.sub_data("scene", LayoutCamera)

  @property
  def xaxis(self) -> LayoutAxis:
    """

    :rtype: LayoutAxis

    :return:
    """
    return self.sub_data("xaxis", LayoutAxis)

  @property
  def yaxis(self) -> LayoutAxis:
    """

    :rtype: LayoutAxis

    :return:
    """
    return self.sub_data("yaxis", LayoutAxis)

  @property
  def zaxis(self) -> LayoutAxis:
    """

    :rtype: LayoutAxis

    :return:
    """
    return self.sub_data("zaxis", LayoutAxis)


class LayoutLegend(DataClass):

  @property
  def x(self):
    return self._attrs["x"]

  @x.setter
  def x(self, val):
    self._attrs["x"] = val

  @property
  def bgcolor(self):
    return self._attrs["bgcolor"]

  @bgcolor.setter
  def bgcolor(self, val):
    self._attrs["bgcolor"] = val

  @property
  def bordercolor(self):
    return self._attrs["bordercolor"]

  @bordercolor.setter
  def bordercolor(self, val):
    self._attrs["bordercolor"] = val

  @property
  def borderwidth(self):
    return self._attrs["borderwidth"]

  @borderwidth.setter
  def borderwidth(self, val):
    self._attrs["borderwidth"] = val

  @property
  def traceorder(self):
    return self._attrs["traceorder"]

  @traceorder.setter
  def traceorder(self, val):
    self._attrs["traceorder"] = val

  @property
  def orientation(self):
    return self._attrs["orientation"]

  @orientation.setter
  def orientation(self, val):
    self._attrs["orientation"] = val

  @property
  def y(self):
    return self._attrs["y"]

  @y.setter
  def y(self, val):
    self._attrs["y"] = val

  @property
  def xanchor(self):
    return self._attrs["xanchor"]

  @xanchor.setter
  def xanchor(self, val):
    self._attrs["xanchor"] = val

  @property
  def font(self) -> LayoutFont:
    """

    :rtype: LayoutFont
    """
    return self.sub_data("font", LayoutFont)


class LayoutTitle(DataClass):

  @property
  def text(self):
    return self._attrs["text"]

  @text.setter
  def text(self, val):
    self._attrs["text"] = val


class Layout(DataClass):


  @property
  def title(self):
    """


    :rtype: LayoutTitle
    """
    return self.sub_data("title", LayoutTitle)

  @property
  def paper_bgcolor(self):
    return self._attrs["paper_bgcolor"]

  @paper_bgcolor.setter
  def paper_bgcolor(self, val):
    self._attrs["paper_bgcolor"] = val

  @property
  def plot_bgcolor(self):
    return self._attrs["plot_bgcolor"]

  @plot_bgcolor.setter
  def plot_bgcolor(self, val):
    self._attrs["plot_bgcolor"] = val

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

    :rtype: LayoutScene
    """
    return self.sub_data("scene", LayoutScene)

  @property
  def legend(self):
    """

    https://plot.ly/javascript/legend/

    :rtype: LayoutLegend
    """
    return self.sub_data("legend", LayoutLegend)

  @property
  def xaxis(self):
    """

    https://plot.ly/javascript/time-series/

    :rtype: LayoutAxis
    """
    return self.sub_data("xaxis", LayoutAxis)

  @property
  def xaxis2(self):
    """

    https://plot.ly/javascript/time-series/

    :rtype: LayoutAxis
    """
    return self.sub_data("xaxis2", LayoutAxis)

  @property
  def grid(self):
    """

    https://plot.ly/javascript/subplots/

    :rtype: LayoutGrid
    """
    return self.sub_data("grid", LayoutGrid)

  @property
  def yaxis(self):
    """

    https://plot.ly/javascript/time-series/

    :rtype: LayoutAxis
    """
    return self.sub_data("yaxis", LayoutAxis)

  @property
  def yaxis2(self):
    """

    https://plot.ly/javascript/time-series/

    :rtype: LayoutAxis
    """
    return self.sub_data("yaxis2", LayoutAxis)

  @property
  def margin(self):
    """

    https://plot.ly/javascript/3d-surface-plots/

    :rtype: LayoutMargin
    """
    return self.sub_data("margin", LayoutMargin)

  def sub_plot(self, columns, rows=1, pattern='independent'):
    self.grid.rows = rows
    self.grid.columns = columns
    self.grid.pattern = pattern
    return self

  def inset_trace(self, x_domain, x, y=None, y_domain=None):
    """

    https://plot.ly/javascript/insets/

    :param x_domain:
    :param x:
    :param y:
    :param y_domain:
    """
    y = y or x
    y_domain = y_domain or x_domain
    x_axis = self.sub_data('xaxis%s' % x, LayoutAxis)
    x_axis.domain = x_domain
    x_axis.anchor = "y%s" % y
    y_axis = self.sub_data('yaxis%s' % y, LayoutAxis)
    y_axis.domain = y_domain
    y_axis.anchor = "x%s" % x
    return self

  def no_background(self):
    """

    https://community.plot.ly/t/you-can-remove-the-white-background-of-the-graphics-background/933

    :return:
    """
    self.paper_bgcolor = 'rgba(0,0,0,0)'
    self.plot_bgcolor = 'rgba(0,0,0,0)'
    return self

  def no_grid(self):
    """
    Remove the vertical and horizontal sub axis from the chart display.
    Keep the zeroline axis

    :return: The attribute object to allow the chaining
    """
    self.xaxis.showgrid = False
    self.xaxis.showline = False
    self.xaxis.showticklabels = False
    self.yaxis.showgrid = False
    self.yaxis.showline = False
    self.yaxis.showticklabels = False
    return self

  def grid_colors(self, x_color, y_color=None):
    """

    :param x_color:
    :param y_color:

    :return:
    """
    self.xaxis.gridcolor = x_color
    self.yaxis.gridcolor = y_color or x_color
    return self

  def axis_colors(self, x_color, y_color=None):
    """

    :param x_color:
    :param y_color:

    :return:
    """
    self.xaxis.set_color(x_color)
    self.yaxis.set_color(y_color or x_color)
    return self

  @property
  def shapes(self):
    """

    https://plot.ly/javascript/shapes/

    :rtype: LayoutShape
    """
    return self.sub_data_enum("shapes", LayoutShape)

  @property
  def annotations(self):
    """

    https://plot.ly/javascript/shapes/

    :rtype: LayoutAnnotation
    """
    return self.sub_data_enum("annotations", LayoutAnnotation)


class Layout3D(Layout):

  @property
  def scene(self):
    """

    :rtype: LayoutScene
    """
    return self.sub_data("scene", LayoutScene)

  def grid_colors(self, x_color, y_color=None, z_color=None):
    """

    :param x_color:
    :param y_color:
    :param z_color:
    """
    self.scene.xaxis.gridcolor = x_color
    self.scene.xaxis.zerolinecolor = x_color
    self.scene.yaxis.gridcolor = y_color
    self.scene.yaxis.zerolinecolor = y_color
    self.scene.zaxis.gridcolor = z_color
    self.scene.zaxis.zerolinecolor = z_color
    return self

  def axis_colors(self, x_color, y_color=None, z_color=None):
    """

    :param x_color:
    :param y_color:
    :param z_color:

    :return:
    """
    self.scene.xaxis.set_color(x_color)
    self.scene.yaxis.set_color(y_color or x_color)
    self.scene.zaxis.set_color(z_color or x_color)
    return self


class LayoutBar(Layout):

  @property
  def barmode(self):
    return self._attrs["barmode"]

  @barmode.setter
  def barmode(self, val):
    self._attrs["barmode"] = val


class LayoutBox(Layout):
  @property
  def boxmode(self):
    return self._attrs["boxmode"]

  @boxmode.setter
  def boxmode(self, val):
    self._attrs["boxmode"] = val


class DataFont(DataClass):

  @property
  def family(self):
    return self._attrs["family"]

  @family.setter
  def family(self, val):
    self._attrs["family"] = val

  @property
  def size(self):
    return self._attrs["size"]

  @size.setter
  def size(self, val):
    self._attrs["size"] = val

  @property
  def color(self):
    return self._attrs["color"]

  @color.setter
  def color(self, val):
    self._attrs["color"] = val


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

  @property
  def dash(self):
    return self._attrs["dash"]

  @dash.setter
  def dash(self, val):
    self._attrs["dash"] = val

  @property
  def outliercolor(self):
    return self._attrs["outliercolor"]

  @outliercolor.setter
  def outliercolor(self, val):
    self._attrs["outliercolor"] = val

  @property
  def outlierwidth(self):
    return self._attrs["outlierwidth"]

  @outlierwidth.setter
  def outlierwidth(self, val):
    self._attrs["outlierwidth"] = val


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
  def colors(self):
    return self._attrs["colors"]

  @colors.setter
  def colors(self, val):
    self._attrs["colors"] = val

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
  def outliercolor(self):
    """

    https://plot.ly/javascript/box-plots/
    """
    return self._attrs["outliercolor"]

  @outliercolor.setter
  def outliercolor(self, val):
    self._attrs["outliercolor"] = val

  @property
  def line(self):
    """

    https://plot.ly/javascript/webgl-vs-svg/

    :rtype: DataMarkersLine
    """
    return self.sub_data("line", DataMarkersLine)


class DataChart(DataClass):

  @property
  def automargin(self):
    return self._attrs["automargin"]

  @automargin.setter
  def automargin(self, val):
    self._attrs["automargin"] = val

  @property
  def hole(self):
    return self._attrs["hole"]

  @hole.setter
  def hole(self, val):
    self._attrs["hole"] = val

  @property
  def opacity(self):
    return self._attrs["opacity"]

  @opacity.setter
  def opacity(self, val):
    self._attrs["opacity"] = val

  @property
  def name(self):
    return self._attrs["name"]

  @name.setter
  def name(self, val):
    self._attrs["name"] = val

  @property
  def mode(self):
    return self._attrs["mode"]

  @mode.setter
  def mode(self, val):
    self._attrs["mode"] = val

  @property
  def fill(self):
    return self._attrs["fill"]

  @fill.setter
  def fill(self, val):
    self._attrs["fill"] = val

  @property
  def fillcolor(self):
    return self._attrs["fillcolor"]

  @fillcolor.setter
  def fillcolor(self, val):
    self._attrs["fillcolor"] = val

  @property
  def orientation(self):
    return self._attrs["orientation"]

  @orientation.setter
  def orientation(self, val):
    self._attrs["orientation"] = val

  @property
  def type(self):
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    self._attrs["type"] = val

  @property
  def showlegend(self):
    return self._attrs["showlegend"]

  @showlegend.setter
  def showlegend(self, val):
    self._attrs["showlegend"] = val

  @property
  def legendgroup(self):
    return self._attrs["legendgroup"]

  @legendgroup.setter
  def legendgroup(self, val):
    self._attrs["legendgroup"] = val

  @property
  def mode(self):
    return self._attrs["mode"]

  @mode.setter
  def mode(self, val):
    self._attrs["mode"] = val

  @property
  def xaxis(self):
    return self._attrs["xaxis"]

  @xaxis.setter
  def xaxis(self, val):
    self._attrs["xaxis"] = val

  @property
  def yaxis(self):
    return self._attrs["yaxis"]

  @yaxis.setter
  def yaxis(self, val):
    self._attrs["yaxis"] = val

  def axis_index(self, x, y=None):
    """

    :param x:
    :param y:
    """
    self.xaxis = "x%s" % x
    self.yaxis = "y%s" % (y or x)
    return self

  @property
  def marker(self):
    """

    https://plot.ly/javascript/bubble-charts/

    :rtype: DataMarkers
    """
    return self.sub_data("marker", DataMarkers)


class DataXY(DataChart):

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
  def text(self):
    return self._attrs["text"]

  @text.setter
  def text(self, val):
    self._attrs["text"] = val

  @property
  def line(self):
    return self.sub_data("line", DataLine)


class DataPie(DataChart):

  @property
  def hole(self):
    return self._attrs["hole"]

  @hole.setter
  def hole(self, val):
    self._attrs["hole"] = val

  @property
  def values(self):
    return self._attrs["values"]

  @values.setter
  def values(self, val):
    self._attrs["values"] = val

  @property
  def labels(self):
    return self._attrs["labels"]

  @labels.setter
  def labels(self, val):
    self._attrs["labels"] = val

  @property
  def textinfo(self):
    return self._attrs["textinfo"]

  @textinfo.setter
  def textinfo(self, val):
    self._attrs["textinfo"] = val

  @property
  def outsidetextfont(self):
    """
    Sets the font used for `textinfo` lying outside the sector.

    https://plot.ly/javascript/reference/#pie-outsidetextfont-family

    :rtype: DataFont
    """
    return self.sub_data("outsidetextfont", DataFont)

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

    :rtype: DataProject
    """
    return self.sub_data("project", DataProject)


class DataContours(DataChart):

  @property
  def z(self):
    """

    https://plot.ly/javascript/3d-surface-plots/

    :rtype: DataZ
    """
    return self.sub_data("z", DataZ)


class DataLine(DataChart):

  @property
  def color(self):
    return self._attrs["color"]

  @color.setter
  def color(self, val):
    self._attrs["color"] = val

  @property
  def width(self):
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val


class DataMove(DataChart):

  @property
  def line(self):
    """

    :rtype: DataLine

    :return:
    """
    return self.sub_data("line", DataLine)


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

    :rtype: DataContours
    """
    return self.sub_data("contours", DataContours)

  @property
  def line(self):
    """

    :rtype: DataLine

    :return:
    """
    return self.sub_data("line", DataLine)


class DataDelta(DataClass):

  @property
  def reference(self):
    return self._attrs["reference"]

  @reference.setter
  def reference(self, val):
    self._attrs["reference"] = val

  @property
  def relative(self):
    return self._attrs["relative"]

  @relative.setter
  def relative(self, val):
    self._attrs["relative"] = val

  @property
  def position(self):
    return self._attrs["position"]

  @position.setter
  def position(self, val):
    self._attrs["position"] = val

  @property
  def valueformat(self):
    return self._attrs["valueformat"]

  @valueformat.setter
  def valueformat(self, val):
    self._attrs["valueformat"] = val


class DataTitle(DataChart):

  @property
  def text(self):
    return self._attrs["text"]

  @text.setter
  def text(self, val):
    self._attrs["text"] = val


class DataNumber(DataChart):

  @property
  def prefix(self):
    return self._attrs["prefix"]

  @prefix.setter
  def prefix(self, val):
    self._attrs["prefix"] = val


class DataGauge(DataChart):

  @property
  def shape(self):
    return self._attrs["shape"]

  @shape.setter
  def shape(self, val):
    self._attrs["shape"] = val

  @property
  def axis(self):
    """

    https://plot.ly/javascript/indicator/

    :rtype: LayoutAxis
    """
    return self.sub_data("axis", LayoutAxis)


class DataIndicator(DataChart):

  @property
  def vmax(self):
    return self._attrs["vmax"]

  @vmax.setter
  def vmax(self, val):
    self._attrs["vmax"] = val

  def domain(self, x, y):
    """

    https://plot.ly/javascript/indicator/

    :param x:
    :param y:
    """
    self._attrs['domain'] = {"x": x, 'y': y}

  @property
  def title(self):
    """

    https://plot.ly/javascript/indicator/

    :rtype: DataTitle
    """
    return self.sub_data("title", DataTitle)

  @property
  def number(self):
    """

    https://plot.ly/javascript/indicator/

    :rtype: DataNumber
    """
    return self.sub_data("number", DataNumber)

  @property
  def gauge(self):
    """

    https://plot.ly/javascript/indicator/

    :rtype: DataGauge
    """
    if 'gauge' not in self.mode:
      self.mode = "%s+gauge" % self.mode
    return self.sub_data("gauge", DataGauge)

  def add_prefix(self, text):
    self.number.prefix = text
    return self

  def add_title(self, text):
    """

    delta.data.add_title("<b style='color:red'>test</b>")

    https://plot.ly/javascript/indicator/

    :param text:

    :return:
    """
    self.title.text = text
    return self

  @property
  def delta(self):
    """

    https://plot.ly/javascript/3d-surface-plots/

    :rtype: DataDelta
    """
    return self.sub_data("delta", DataDelta)


class DataBox(DataChart):

  @property
  def boxpoints(self):
    return self._attrs["boxpoints"]

  @boxpoints.setter
  def boxpoints(self, val):
    self._attrs["boxpoints"] = val

  @property
  def boxmean(self):
    return self._attrs["boxmean"]

  @boxmean.setter
  def boxmean(self, val):
    self._attrs["boxmean"] = val

  @property
  def jitter(self):
    return self._attrs["jitter"]

  @jitter.setter
  def jitter(self, val):
    self._attrs["jitter"] = val

  @property
  def whiskerwidth(self):
    return self._attrs["whiskerwidth"]

  @whiskerwidth.setter
  def whiskerwidth(self, val):
    self._attrs["whiskerwidth"] = val

  @property
  def pointpos(self):
    return self._attrs["pointpos"]

  @pointpos.setter
  def pointpos(self, val):
    self._attrs["pointpos"] = val


class DataCandle(DataChart):

  @property
  def close(self):
    return self._attrs["close"]

  @close.setter
  def close(self, val):
    self._attrs["close"] = val

  @property
  def high(self):
    return self._attrs["high"]

  @high.setter
  def high(self, val):
    self._attrs["high"] = val

  @property
  def low(self):
    return self._attrs["low"]

  @low.setter
  def low(self, val):
    self._attrs["low"] = val

  @property
  def open(self):
    return self._attrs["open"]

  @open.setter
  def open(self, val):
    self._attrs["open"] = val

  @property
  def increasing(self):
    """

    :rtype: DataMove

    :return:
    """
    return self.sub_data("increasing", DataMove)

  @property
  def decreasing(self):
    """

    :rtype: DataMove

    :return:
    """
    return self.sub_data("decreasing", DataMove)
