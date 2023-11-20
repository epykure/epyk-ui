
from typing import Union
from epyk.core.py import primitives, types
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsObjects

from epyk.core.js.packages import JsPackage


class JsPlotly(JsPackage):

  #  -----------------------------------------
  #  Common table javascript interface
  #  -----------------------------------------
  def empty(self):
    """   

    """
    pass

  def download(self, filename: str = None, options: dict = None, *args, **kwargs):
    """
    Common download feature for tables.

    :param filename: Filename
    :param options: Download option
    """
    filename = filename or self.component.html_code
    pass

  def add_row(self, data, flag: Union[types.JS_DATA_TYPES, bool] = False):
    pass

  def show_column(self, column: str):
    pass

  def hide_column(self, column: str):
    pass

  def redraw(self, flag: bool = False):
    return ""

  #  -----------------------------------------
  #  Specific table javascript interface
  #  -----------------------------------------
  def newPlot(self, data=None, layout=None, config=None, html_code=None):
    """
    Draws a new plot in an <div> element, overwriting any existing plot. To update an existing plot in a <div>,
    it is much more efficient to use Plotly.react than to overwrite it.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param data: array of objects, see documentation (defaults to []).
    :param layout: object, see documentation (defaults to {}).
    :param config: object, see documentation (defaults to {}).
    :param html_code: String. Optional. DOM node or string id of a DOM node.
    """
    data = JsUtils.jsConvertData(data or [], None)
    layout = JsUtils.jsConvertData(layout or {}, None)
    config = JsUtils.jsConvertData(config or {}, None)
    return JsObject.JsObject.get(
      "Plotly.newPlot('%s', %s, %s, %s)" % (html_code or self.component.dom.varName, data, layout, config))

  def react(self, data=None, layout=None, config=None, html_code=None):
    """
    Plotly.react has the same signature as Plotly.newPlot above, and can be used in its place to create a plot,
    but when called again on the same <div> will update it far more efficiently than Plotly.newPlot,
    which would destroy and recreate the plot.
    Plotly.react is as fast as Plotly.restyle/Plotly.relayout documented below.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param data: array of objects, see documentation (defaults to []).
    :param layout: object, see documentation (defaults to {}).
    :param config: object, see documentation (defaults to {}).
    :param html_code: String. Optional. DOM node or string id of a DOM node.
    """
    data = JsUtils.jsConvertData(data or [], None)
    layout = JsUtils.jsConvertData(layout or {}, None)
    config = JsUtils.jsConvertData(config or {}, None)
    return JsObject.JsObject.get(
      "Plotly.react(%s, %s, %s, %s)" % (html_code or self.component.dom.varName, data, layout, config))

  def restyle(self, update=None, trace_indices=None, html_code=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot
    with Plotly.newPlot.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param update: object, see below for examples (defaults to {})
    :param trace_indices: array of integer indices into existing value of data (optional, default behaviour is to
      apply to all traces)
    :param html_code: String. Optional. DOM node or string id of a DOM node.
    """
    update = JsUtils.jsConvertData(update or {}, None)
    if trace_indices is None:
      return JsObject.JsObject.get("Plotly.restyle(%s, %s)" % (html_code or self.component.dom.varName, update))

    trace_indices = JsUtils.jsConvertData(trace_indices, None)
    return JsObject.JsObject.get(
      "Plotly.restyle(%s, %s, %s)" % (html_code or self.component.dom.varName, update, trace_indices))

  def relayout(self, update=None, html_code=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing
    the whole plot with Plotly.newPlot.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param update: object, see below for examples (defaults to {})
    :param html_code: String. Optional. DOM node or string id of a DOM node.
    """
    update = JsUtils.jsConvertData(update or {}, None)
    return JsObject.JsObject.get("Plotly.relayout(%s, %s)" % (html_code or self.component.dom.varName, update))

  def update(self, data_update=None, layout_update=None, trace_indices=None, html_code=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing
    the whole plot with Plotly.newPlot.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param data_update: object, see Plotly.restyle above (defaults to {})
    :param layout_update: object, see Plotly.relayout above (defaults to {})
    :param trace_indices: array of integer indices into existing value of data, see Plotly.restyle above
      (optional, default behaviour is to apply to all traces)
    :param html_code: String. Optional. DOM node or string id of a DOM node.
    """
    data_update = JsUtils.jsConvertData(data_update or {}, None)
    layout_update = JsUtils.jsConvertData(layout_update or {}, None)
    if trace_indices is None:
      return JsObject.JsObject.get(
        "Plotly.update(%s, %s, %s)" % (html_code or self.component.dom.varName, data_update, layout_update))

    trace_indices = JsUtils.jsConvertData(trace_indices, None)
    return JsObject.JsObject.get("Plotly.update(%s, %s, %s, %s)" % (
      html_code or self.component.dom.varName, data_update, layout_update, trace_indices))

  def validate(self, data, layout):
    """
    Plotly.validate allows users to validate their input data array and layout object.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param data: array of objects
    :param layout: object
    """
    data = JsUtils.jsConvertData(data, None)
    layout = JsUtils.jsConvertData(layout, None)
    return JsObject.JsObject.get("Plotly.validate(%s, %s)" % (data, layout))

  def makeTemplate(self, figure):
    """
    Plotly.makeTemplate copies the style information from a figure.
    It does this by returning a template object which can be passed to the layout.template attribute of another figure.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    Usage::

    :param figure: figure or DOM Node where figure is a plot object, with {data, layout} members.
    If a DOM node is used it must be a div element already containing a plot.
    """
    figure = JsUtils.jsConvertData(figure, None)
    return JsObject.JsObject.get("Plotly.makeTemplate(%s)" % figure)

  def validateTemplate(self, figure, template):
    """
    Plotly.validateTemplate allows users to Test for consistency between the given figure and a template,
    either already included in the figure or given separately.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    Usage::

    :param figure: figure or DOM Node where figure is a plot object, with {data, layout} members.
    :param template: the template, with its own {data, layout}, to test. If omitted, we will look for a template
      already attached as the plot's
    """
    figure = JsUtils.jsConvertData(figure, None)
    template = JsUtils.jsConvertData(template, None)
    return JsObject.JsObject.get("Plotly.validateTemplate(%s, %s)" % (figure, template))

  def load(self, name, data, options=None):
    options = options or {}
    return self.addTraces([{"y": data, "name": name, "type": options.get("type", "line")}])

  def addTraces(self, traces, position=None, html_code=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot
    with Plotly.newPlot.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param traces:
    :param position: Integer.
    :param html_code: String. Optional. DOM node or string id of a DOM node.
    """
    traces = JsUtils.jsConvertData(traces, None)
    if position is None:
      return JsObject.JsObject.get("Plotly.addTraces(%s, %s)" % (html_code or self.component.dom.varName, traces))

    position = JsUtils.jsConvertData(position, None)
    return JsObjects.JsVoid("Plotly.addTraces(%s, %s, %s)" % (html_code or self.component.dom.varName, traces, position))

  def deleteAllTraces(self, html_code=None):
    """
    Remove all the traces defined in the chart.

    :param html_code:
    """
    return JsObject.JsObject.get("%(graphId)s.data = []" % {"graphId": html_code or self.component.dom.varName})

  def deleteTraces(self, positions, html_code=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot
    with Plotly.newPlot.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param positions: List.
    :param html_code: String. Optional. DOM node or string id of a DOM node.
    """
    positions = JsUtils.jsConvertData(positions, None)
    return JsObject.JsObject.get("Plotly.deleteTraces(%s, %s)" % (html_code or self.component.dom.varName, positions))

  @property
  def traceCount(self):
    """
    Return the number of traces on a chart
    """
    return JsObjects.JsNumber.JsNumber.get("%s.data.length" % self.component.dom.varName)

  def moveTraces(self, current_position, dest_position=None, html_code=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot
    with Plotly.newPlot.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param current_position:
    :param dest_position: Integer. Optional.
    :param html_code: String. Optional. DOM node or string id of a DOM node.
    """
    current_position = JsUtils.jsConvertData(current_position, None)
    if dest_position is None:
      return JsObject.JsObject.get(
        "Plotly.moveTraces(%s, %s)" % (html_code or self.component.dom.varName, current_position))

    return JsObject.JsObject.get(
      "Plotly.moveTraces(%s, %s, %s)" % (html_code or self.component.dom.varName, current_position, dest_position))

  def extendTraces(self, traces_extension, index_traces, html_code=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot
    with Plotly.newPlot.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param traces_extension:
    :param index_traces: List.
    :param html_code: String. Optional. DOM node or string id of a DOM node
    """
    traces_extension = JsUtils.jsConvertData(traces_extension, None)
    index_traces = JsUtils.jsConvertData(index_traces, None)
    return JsObject.JsObject.get("Plotly.extendTraces(%s, %s, %s)" % (
      html_code or self.component.dom.varName, traces_extension, index_traces))

  def prependTraces(self, traces_new, index_traces, html_code=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot
    with Plotly.newPlot.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param tracesNew:
    :param index_traces: List.
    :param html_code: String. Optional. DOM node or string id of a DOM node
    """
    traces_new = JsUtils.jsConvertData(traces_new, None)
    index_traces = JsUtils.jsConvertData(index_traces, None)
    return JsObject.JsObject.get(
      "Plotly.prependTraces(%s, %s, %s)" % (html_code or self.component.dom.varName, traces_new, index_traces))

  def animate(self, frame_or_group_name_or_frameList, animation_attributes, html_code=None):
    """
    This allows you to add animation frames to a graphDiv. The group or name attribute of a frame can be used by
    Plotly.animate in place of a frame object (or array of frame objects). See example here.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param frame_or_group_name_or_frameList: A frame to be animated or an array of frames to be animated in sequence.
    :param animation_attributes: An object, see documentation for examples.
    :param html_code: String. Optional. DOM node or string id of a DOM node
    """
    frame_or_group_name_or_frameList = JsUtils.jsConvertData(frame_or_group_name_or_frameList, None)
    animation_attributes = JsUtils.jsConvertData(animation_attributes, None)
    return JsObject.JsObject.get(
      "Plotly.animate(%s, %s, %s)" % (
        html_code or self.component.dom.varName, frame_or_group_name_or_frameList, animation_attributes))

  def purge(self):
    """
    Using purge will clear the div, and remove any Plotly plots that have been placed in it.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot
    """
    return JsObject.JsObject.get("Plotly.purge()")

  def toImage(self, img_format: str, html_code: str = None):
    """
    toImage will generate a promise to an image of the plot in data URL format.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param str img_format:
    :param str html_code: Optional. DOM node or string id of a DOM node
    """
    img_format = JsUtils.jsConvertData(img_format, None)
    return JsObjects.JsPromise("Plotly.toImage(%s, %s)" % (html_code or self.component.dom.varName, img_format))

  def downloadImage(self, img_format: str, html_code: str = None, *args, **kwargs):
    """
    downloadImage will trigger a request to download the image of a Plotly plot.

    Related Pages:

      https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param str img_format:
    :param str html_code: Optional. DOM node or string id of a DOM node.
    """
    img_format = JsUtils.jsConvertData(img_format, None)
    return JsObject.JsObject.get("Plotly.downloadImage(%s, %s)" % (html_code or self.component.dom.varName, img_format))


class JsPlotlyLegend:

  def x(self):
    pass

  def y(self):
    pass

  def bgcolor(self):
    pass

  def bordercolor(self):
    pass

  def traceorder(self):
    pass

  def font(self):
    pass

  def yref(self):
    pass

  def showlegend(self):
    pass


class JsPlotlyAxis:

  def title(self):
    pass

  def showline(self):
    pass

  def showticklabels(self):
    pass

  def showgrid(self):
    pass

  def zeroline(self):
    pass

  def range(self):
    pass

  def autorange(self):
    pass


class JsPlotlyMargin:

  def autoexpand(self):
    pass

  def l(self):
    pass

  def r(self):
    pass

  def t(self):
    pass


class JsPlotlyAnnotation:
  pass


class JsPlotlyLayout:

  def __init__(self, attrs: dict):
    self.__attrs = {}

  @property
  def width(self):
    """
    Type: number greater than or equal to 10
    Sets the plot's width (in px).

    https://plot.ly/javascript/reference/#width
    """
    return self.__attrs["width"]

  @width.setter
  def width(self, val):
    self.__attrs["width"] = float(val)

  @property
  def height(self):
    return

  def legend(self):
    pass

  def title(self):
    pass

  def paper_bgcolor(self):
    pass

  def plot_bgcolor(self):
    pass

  def showlegend(self):
    pass

  def bargap(self):
    pass

  def barmode(self):
    pass

  def xaxis(self):
    pass

  def toStr(self):
    return {}


class PlotlyFont:

  def size(self):
    pass


class PlotlyMarkers:

  def arearatio(self):
    pass

  def sizemin(self):
    pass

  def sizemax(self):
    pass

  def blend(self):
    pass

  def border(self):
    pass

  def color(self):
    pass

  def size(self):
    pass

  def line(self):
    pass

  def sizeref(self):
    pass

  def opacity(self):
    pass

  def sizemode(self):
    pass


class JsPlotlyTrace:

  def __init__(self, component: primitives.HtmlModel, js_code=None, is_py_data=True, page: primitives.PageModel = None):
    self.component, self.chartId, self.page = component, is_py_data, page
    self._layout, self.varName = None, js_code or "document.getElementById('%s')" % component.html_code

  def mode(self):
    pass

  def type(self):
    pass

  def name(self):
    pass

  def text(self):
    pass

  def line(self):
    pass

  def connectgaps(self):
    pass


class Line(JsPlotlyTrace):
  lib_alias = {'js': 'plotly.js'}

  @property
  def varId(self): return ""

  @property
  def layout(self) -> JsPlotlyLayout:
    if self._layout is None:
      self._layout = JsPlotlyLayout({})
    return self._layout

  def add_trace(self, x, y):
    return JsObject.JsObject.get("Plotly.addTraces('%s', {y: %s, x: %s})" % (self.component.html_code, y, x))

  def deleteTraces(self, i: int):
    return JsObject.JsObject.get("Plotly.deleteTraces('%s', %s)" % (self.component.html_code, i))


class Bar(JsPlotlyTrace):
  lib_alias = {'js': 'plotly.js'}

  @property
  def layout(self) -> JsPlotlyLayout:
    if self._layout is None:
      self._layout = JsPlotlyLayout({})
    return self._layout


class Pie(JsPlotlyTrace):
  lib_alias = {'js': 'plotly.js'}

  @property
  def layout(self) -> JsPlotlyLayout:
    if self._layout is None:
      self._layout = JsPlotlyLayout({})
    return self._layout
