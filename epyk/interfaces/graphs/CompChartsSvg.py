
from epyk.core.html import graph


class SVG(object):
  def __init__(self, context):
    self.parent = context

  def new(self, height=(100, "%"), width=(30, "px")):
    """
    SVG stands for Scalable Vector Graphics.

    SVG defines vector-based graphics in XML format.

    Example
    svg = rptObj.ui.charts.svg.new(width=200)
    svg.add_text("I love SVG!", x=0, y=15, options={"fill": 'red'})

    Documentation
    https://developer.mozilla.org/en-US/docs/Web/SVG
    https://www.w3schools.com/graphics/svg_intro.asp

    :param height:
    :param width:

    :return:
    """
    if not isinstance(width, tuple):
      width = (width, "px")
    html_svg = graph.GraphSvg.SVG(self.parent.context.rptObj, height, width)
    self.parent.context.register(html_svg)
    return html_svg

  def line(self, x1=0, y1=None, x2=None, y2=None, height=(100, "%"), width=(30, "px"), options=None):
    """
    Entry point to the basic line definition in a SVG HTML Tag

    Documentation
    https://www.w3schools.com/graphics/svg_line.asp

    :param x1: The x1 attribute defines the start of the line on the x-axis
    :param y1: The y1 attribute defines the start of the line on the y-axis
    :param x2: The x2 attribute defines the end of the line on the x-axis
    :param y2: The y2 attribute defines the end of the line on the y-axis
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param options:
    """
    x2 = x2 or width[0]
    y2 = 0 if height[1] == "%" else y2 / 2
    y1 = 0 if height[1] == "%" else y1 / 2
    dftl_options = {"stroke": "green", "stroke-width": 1}
    if options is not None:
      dftl_options.update(options)
    line = graph.GraphSvg.Line(self.parent.context.rptObj, x1, y1, x2, y2, height, width, dftl_options)
    self.parent.context.register(line)
    return line

  def ellipse(self, cx, cy, rx, ry, height=(100, "%"), width=(30, "px"), options=None):
    """
    SVG Ellipse - <ellipse>

    Documentation
    https://www.w3schools.com/graphics/svg_ellipse.asp

    Example
    rptObj.ui.charts.svg.ellipse(200, 80, 100, 50, height=("140", "px"), width=("500", "px"))

    :param cx: The cx attribute defines the x coordinate of the center of the ellipse
    :param cy: The cy attribute defines the y coordinate of the center of the ellipse
    :param rx: The rx attribute defines the horizontal radius
    :param ry: The ry attribute defines the vertical radius
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param options:
    """
    dftl_options = {"stroke": "green", "stroke-width": 1, 'fill': "none"}
    if options is not None:
      dftl_options.update(options)
    line = graph.GraphSvg.Ellipse(self.parent.context.rptObj, cx, cy, rx, ry, height, width, dftl_options)
    self.parent.context.register(line)
    return line

  def polyline(self, points, height=(100, "%"), width=(30, "px"), options=None):
    """

    Documentation
    https://www.w3schools.com/graphics/svg_polyline.asp

    Example
    rptObj.ui.charts.svg.polyline(points=[(200,10), (250,190), (160,190)], height=("210", "px"), width=("500", "px"))

    :param points: The points attribute defines the list of points (pairs of x and y coordinates) required to draw the polyline
    :param height:
    :param width:
    :param options:
    :return:
    """
    dflt_options = {"stroke": "green", "stroke-width": 1, 'fill': "none"}
    if options is not None:
      dflt_options.update(options)
    shape = graph.GraphSvg.Polyline(self.parent.context.rptObj, points, height, width, dflt_options)
    self.parent.context.register(shape)
    return shape

  def polygone(self, points, height=(100, "%"), width=(30, "px"), options=None):
    """
    Documentation
    https://www.w3schools.com/graphics/tryit.asp?filename=trysvg_polygon

    Example
    rptObj.ui.charts.svg.polygone(points=[(200, 10), (250, 190), (160, 190)], height=("210", "px"), width=("500", "px"))

    :param points: The points attribute defines the list of points (pairs of x and y coordinates) required to draw the polyline
    :param height:
    :param width:
    :param options:
    :return:
    """
    dflt_options = {"stroke": "green", "stroke-width": 1, 'fill': "none"}
    if options is not None:
      dflt_options.update(options)
    shape = graph.GraphSvg.Polygone(self.parent.context.rptObj, points, height, width, dflt_options)
    self.parent.context.register(shape)
    return shape

  def triangle(self, width=20, options=None):
    """
    Documentation
    https://www.w3schools.com/graphics/svg_polyline.asp

    Example
    rptObj.ui.charts.svg.triangle()

    :param width:
    :param options:

    :return:
    """
    if not isinstance(width, tuple):
      width = (width, "px")
    dflt_options = {"stroke": self.parent.context.rptObj.theme.success[1], "stroke-width": 1,
                    'fill': self.parent.context.rptObj.theme.success[1]}
    if options is not None:
      dflt_options.update(options)
    tri = graph.GraphSvg.SVG(self.parent.context.rptObj, (100, "%"), (200, "px"))
    tri.rect([(0, width[0]), (width[0]/2, 0), (width[0], width[0]), (0, width[0])],
                                    width, width, dflt_options)
    self.parent.context.register(tri)
    return tri

  def rectangle(self, x, y, width, height, fill=None, rx=0, ry=0):
    """

    :param x:
    :param y:
    :param width:
    :param height:
    :param fill:
    :param rx:
    :param ry:
    """
    rect = graph.GraphSvg.SVG(self.parent.context.rptObj, (900, "px"), (200, "px"))
    rect.rect(x, y, width, height, fill, rx=rx, ry=ry)
    self.parent.context.register(rect)
    return rect
