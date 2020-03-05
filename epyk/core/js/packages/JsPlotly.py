
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsObjects

from epyk.core.js.packages import JsPackage
from epyk.core.js.packages import DataAttrs


class JsPlotly(JsPackage):
  lib_alias = {'js': 'plotly.js'}

  def newPlot(self, htmlId, data=None, layout=None, config=None):
    """
    Draws a new plot in an <div> element, overwriting any existing plot. To update an existing plot in a <div>, it is much more efficient to use Plotly.react than to overwrite it.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId: DOM node or string id of a DOM node
    :param data: array of objects, see documentation (defaults to [])
    :param layout: object, see documentation (defaults to {})
    :param config: object, see documentation (defaults to {})
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    data = JsUtils.jsConvertData(data or [], None)
    layout = JsUtils.jsConvertData(layout or {}, None)
    config = JsUtils.jsConvertData(config or {}, None)
    return JsObject.JsObject.get("Plotly.newPlot(%s, %s, %s, %s)" % (htmlId, data, layout, config))

  def react(self, htmlId, data=None, layout=None, config=None):
    """
    Plotly.react has the same signature as Plotly.newPlot above, and can be used in its place to create a plot, but when called again on the same <div> will update it far more efficiently than Plotly.newPlot, which would destroy and recreate the plot. Plotly.react is as fast as Plotly.restyle/Plotly.relayout documented below.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId: DOM node or string id of a DOM node
    :param data: array of objects, see documentation (defaults to [])
    :param layout: object, see documentation (defaults to {})
    :param config: object, see documentation (defaults to {})
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    data = JsUtils.jsConvertData(data or [], None)
    layout = JsUtils.jsConvertData(layout or {}, None)
    config = JsUtils.jsConvertData(config or {}, None)
    return JsObject.JsObject.get("Plotly.react(%s, %s, %s, %s)" % (htmlId, data, layout, config))

  def restyle(self, htmlId, update=None, traceIndices=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot with Plotly.newPlot.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId: DOM node or string id of a DOM node
    :param update: object, see below for examples (defaults to {})
    :param traceIndices: array of integer indices into existing value of data (optional, default behaviour is to apply to all traces)
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    update = JsUtils.jsConvertData(update or {}, None)
    if traceIndices is None:
      return JsObject.JsObject.get("Plotly.restyle(%s, %s)" % (htmlId, update))

    traceIndices = JsUtils.jsConvertData(traceIndices, None)
    return JsObject.JsObject.get("Plotly.restyle(%s, %s, %s)" % (htmlId, update, traceIndices))

  def relayout(self, htmlId, update=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot with Plotly.newPlot.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId: DOM node or string id of a DOM node
    :param update: object, see below for examples (defaults to {})
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    update = JsUtils.jsConvertData(update or {}, None)
    return JsObject.JsObject.get("Plotly.relayout(%s, %s)" % (htmlId, update))

  def update(self, htmlId, data_update=None, layout_update=None, traceIndices=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot with Plotly.newPlot.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId: DOM node or string id of a DOM node
    :param data_update: object, see Plotly.restyle above (defaults to {})
    :param layout_update: object, see Plotly.relayout above (defaults to {})
    :param traceIndices: array of integer indices into existing value of data, see Plotly.restyle above (optional, default behaviour is to apply to all traces)
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    data_update = JsUtils.jsConvertData(data_update or {}, None)
    layout_update = JsUtils.jsConvertData(layout_update or {}, None)
    if traceIndices is None:
      return JsObject.JsObject.get("Plotly.update(%s, %s, %s)" % (htmlId, data_update, layout_update))

    traceIndices = JsUtils.jsConvertData(traceIndices, None)
    return JsObject.JsObject.get("Plotly.update(%s, %s, %s, %s)" % (htmlId, data_update, layout_update, traceIndices))

  def validate(self, data, layout):
    """
    Plotly.validate allows users to validate their input data array and layout object.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param data: array of objects
    :param layout: object
    """
    data = JsUtils.jsConvertData(data, None)
    layout = JsUtils.jsConvertData(layout, None)
    return JsObject.JsObject.get("Plotly.validate(%s, %s)" % (data, layout))

  def makeTemplate(self, figure):
    """
    Plotly.makeTemplate copies the style information from a figure. It does this by returning a template object which can be passed to the layout.template attribute of another figure.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param figure: figure or DOM Node where figure is a plot object, with {data, layout} members. If a DOM node is used it must be a div element already containing a plot.
    """
    figure = JsUtils.jsConvertData(figure, None)
    return JsObject.JsObject.get("Plotly.makeTemplate(%s)" % figure)

  def validateTemplate(self, figure, template):
    """
    Plotly.validateTemplate allows users to Test for consistency between the given figure and a template, either already included in the figure or given separately.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param figure: figure or DOM Node where figure is a plot object, with {data, layout} members.
    :param template: the template, with its own {data, layout}, to test. If omitted, we will look for a template already attached as the plot's
    """
    figure = JsUtils.jsConvertData(figure, None)
    template = JsUtils.jsConvertData(template, None)
    return JsObject.JsObject.get("Plotly.validateTemplate(%s, %s)" % (figure, template))

  def addTraces(self, htmlId, traces, position=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot with Plotly.newPlot.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId:
    :param traces:
    :param position:
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    traces = JsUtils.jsConvertData(traces, None)
    if position is None:
      return JsObject.JsObject.get("Plotly.addTraces(%s, %s)" % (htmlId, traces))

      position = JsUtils.jsConvertData(position, None)
    return JsObject.JsObject.get("Plotly.addTraces(%s, %s, %s)" % (htmlId, traces, position))

  def deleteTraces(self, htmlId, positions):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot with Plotly.newPlot.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId:
    :param positions:
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    positions = JsUtils.jsConvertData(positions, None)
    return JsObject.JsObject.get("Plotly.deleteTraces(%s, %s)" % (htmlId, positions))

  def moveTraces(self, htmlId, currentPosition, destPosition=None):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot with Plotly.newPlot.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId:
    :param currentPosition:
    :param destPosition:
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    currentPosition = JsUtils.jsConvertData(currentPosition, None)
    if destPosition is None:
      return JsObject.JsObject.get("Plotly.moveTraces(%s, %s)" % (htmlId, currentPosition))

    return JsObject.JsObject.get("Plotly.moveTraces(%s, %s, %s)" % (htmlId, currentPosition, destPosition))

  def extendTraces(self, htmlId, tracesExtension, indexTraces):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot with Plotly.newPlot.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId:
    :param tracesExtension:
    :param indexTraces:
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    tracesExtension = JsUtils.jsConvertData(tracesExtension, None)
    indexTraces = JsUtils.jsConvertData(indexTraces, None)
    return JsObject.JsObject.get("Plotly.extendTraces(%s, %s, %s)" % (htmlId, tracesExtension, indexTraces))

  def prependTraces(self, htmlId, tracesNew, indexTraces):
    """
    This function has comparable performance to Plotly.react and is faster than redrawing the whole plot with Plotly.newPlot.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId:
    :param tracesNew:
    :param indexTraces:
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    tracesNew = JsUtils.jsConvertData(tracesNew, None)
    indexTraces = JsUtils.jsConvertData(indexTraces, None)
    return JsObject.JsObject.get("Plotly.prependTraces(%s, %s, %s)" % (htmlId, tracesNew, indexTraces))

  def animate(self, htmlId, frameOrGroupNameOrFrameList, animationAttributes):
    """
    This allows you to add animation frames to a graphDiv. The group or name attribute of a frame can be used by Plotly.animate in place of a frame object (or array of frame objects). See example here.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId: DOM node or string id of a DOM node
    :param frameOrGroupNameOrFrameList: A frame to be animated or an array of frames to be animated in sequence.
    :param animationAttributes: An object, see documentation for examples.
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    frameOrGroupNameOrFrameList = JsUtils.jsConvertData(frameOrGroupNameOrFrameList, None)
    animationAttributes = JsUtils.jsConvertData(animationAttributes, None)
    return JsObject.JsObject.get("Plotly.animate(%s, %s, %s)" % (htmlId, frameOrGroupNameOrFrameList, animationAttributes))

  def purge(self):
    """
    Using purge will clear the div, and remove any Plotly plots that have been placed in it.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot
    """
    return JsObject.JsObject.get("Plotly.purge()")

  def toImage(self, htmlId, format):
    """
    toImage will generate a promise to an image of the plot in data URL format.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId:
    :param format:
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    format = JsUtils.jsConvertData(format, None)
    return JsObjects.JsPromise("Plotly.toImage(%s, %s)" % (htmlId, format))

  def downloadImage(self, htmlId, format):
    """
    downloadImage will trigger a request to download the image of a Plotly plot.

    https://plot.ly/javascript/plotlyjs-function-reference/#plotlynewplot

    :param htmlId:
    :param format:
    """
    htmlId = JsUtils.jsConvertData(htmlId, None)
    format = JsUtils.jsConvertData(format, None)
    return JsObject.JsObject.get("Plotly.downloadImage(%s, %s)" % (htmlId, format))


class JsPlotlyLegend(object):

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


class JsPlotlyAxis(object):

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


class JsPlotlyMargin(object):

  def autoexpand(self):
    pass

  def l(self):
    pass

  def r(self):
    pass

  def t(self):
    pass


class JsPlotlyAnnotation(object):
  pass


class JsPlotlyLayout(object):

  def __init__(self, attrs):
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


class PlotlyFont(object):

  def size(self):
    pass


class PlotlyMarkers(object):

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


class JsPlotlyTrace(object):

  def __init__(self, src, varName):
    self._src, self.varName = src, varName
    self._layout = None

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

  @property
  def layout(self):
    if self._layout is None:
      self._layout = JsPlotlyLayout({})
    return self._layout


if __name__ == '__main__':
  pass
