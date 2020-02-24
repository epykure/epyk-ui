
from epyk.core.html import graph


class SVG(object):
  def __init__(self, context):
    self.parent = context

  def new(self, width=(500, "px"), height=(300, "px")):
    """
    Description:
    ------------
    SVG stands for Scalable Vector Graphics.

    SVG defines vector-based graphics in XML format.

    Usage:
    ------
    svg = rptObj.ui.charts.svg.new(width=200)
    svg.add_text("I love SVG!", x=0, y=15, options={"fill": 'red'})

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/SVG
    https://www.w3schools.com/graphics/svg_intro.asp

    Attributes:
    ----------
    :param height: Optional. Integer for the component width
    :param width: Optional. Integer for the component height
    """
    if not isinstance(width, tuple):
      width = (width, "px")
    html_svg = graph.GraphSvg.SVG(self.parent.context.rptObj, width, height)
    self.parent.context.register(html_svg)
    return html_svg

  def line(self, x1=0, y1=None, x2=None, y2=None, width=(500, "px"), height=(300, "px"), options=None):
    """
    Description:
    ------------
    Entry point to the basic line definition in a SVG HTML Tag

    Usage:
    ------
    rptObj.ui.charts.svg.line(10, 30, 40, 69)

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_line.asp

    Attributes:
    ----------
    :param x1: The x1 attribute defines the start of the line on the x-axis
    :param y1: The y1 attribute defines the start of the line on the y-axis
    :param x2: The x2 attribute defines the end of the line on the x-axis
    :param y2: The y2 attribute defines the end of the line on the y-axis
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param options:
    """
    x2 = x2 or width[0]
    if y2 is None:
      y2 = 0 if height[1] == "%" else height[0] / 2
    if y1 is None:
      y1 = 0 if height[1] == "%" else height[0] / 2
    html_svg = graph.GraphSvg.SVG(self.parent.context.rptObj, width, height)
    html_svg.line(x1, y1, x2, y2)
    self.parent.context.register(html_svg)
    return html_svg

  def arrow_right(self, x1=0, y1=None, x2=None, y2=None, size=10, width=(500, "px"), height=(300, "px"), options=None):
    """

    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param width:
    :param height:
    :param options:
    """
    line = self.line(x1, y1, x2 or width[0]-size, y2, width, height, options)
    defs = line.defs()
    m = defs.marker("arrow", "0 0 10 10", 5, 5)
    m.arrow(size)
    line[0].marker_end(m.url)
    return line

  def arrow_left(self, x1=0, y1=None, x2=None, y2=None, size=10, width=(500, "px"), height=(300, "px"), options=None):
    """

    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param width:
    :param height:
    :param options:
    """
    line = self.line(x1+size, y1, x2, y2, width, height, options)
    defs = line.defs()
    m = defs.marker("arrow", "0 0 10 10", 5, 5)
    m.arrow(size).orient("auto-start-reverse")
    line[0].marker_start(m.url)
    return line

  def ellipse(self, cx, cy, rx, ry, width=(500, "px"), height=(300, "px"), options=None):
    """
    Description:
    ------------
    SVG Ellipse - <ellipse>

    Usage:
    ------
    rptObj.ui.charts.svg.ellipse(100, 100, 40, 69)

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_ellipse.asp

    Attributes:
    ----------
    :param cx: The cx attribute defines the x coordinate of the center of the ellipse
    :param cy: The cy attribute defines the y coordinate of the center of the ellipse
    :param rx: The rx attribute defines the horizontal radius
    :param ry: The ry attribute defines the vertical radius
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param options:
    """
    html_svg = graph.GraphSvg.SVG(self.parent.context.rptObj, width, height)
    html_svg.ellipse(cx, cy, rx, ry)
    self.parent.context.register(html_svg)
    return html_svg

  def polyline(self, points, width=(500, "px"), height=(300, "px"), options=None):
    """
    Description:
    ------------

    Usage:
    --------------
    rptObj.ui.charts.svg.polyline([(15, 80), (29, 50), (43, 60), (57, 30), (71, 40), (85, 15)])

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_polyline.asp

    Attributes:
    ----------
    :param points: The points attribute defines the list of points (pairs of x and y coordinates) required to draw the polyline
    :param height:
    :param width:
    :param options:
    """
    html_svg = graph.GraphSvg.SVG(self.parent.context.rptObj, width, height)
    html_svg.polyline(points)
    self.parent.context.register(html_svg)
    return html_svg

  def polygone(self, points, width=(500, "px"), height=(300, "px"), options=None):
    """
    Description:
    ------------

    Usage:
    --------------
    rptObj.ui.charts.svg.polygone([(15, 80), (29, 50), (43, 60), (57, 30), (71, 40), (85, 15)])

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/tryit.asp?filename=trysvg_polygon

    Attributes:
    ----------
    :param points: The points attribute defines the list of points (pairs of x and y coordinates) required to draw the polyline
    :param height:
    :param width:
    :param options:
    """
    html_svg = graph.GraphSvg.SVG(self.parent.context.rptObj, width, height)
    html_svg.polygon(points)
    self.parent.context.register(html_svg)
    return html_svg

  def triangle(self, point1, point2=None, point3=None, fill='None', width=(500, "px"), height=(300, "px"), options=None):
    """
    Description:
    ------------

    Usage:
    --------------
    rptObj.ui.charts.svg.triangle((50, 100))

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_polyline.asp

    Attributes:
    ----------
    :param point1:
    :param point2:
    :param point3:
    :param fill:
    :param width:
    :param height:
    :param options:
    """
    if point2 is None:
      point2 = (point1[1]/2, point1[0])
    if point3 is None:
      point3 = (point1[1], point1[1])
    tri = graph.GraphSvg.SVG(self.parent.context.rptObj, width, height)
    tri.triangle([point1, point2, point3, point1], fill=fill, options=options)
    self.parent.context.register(tri)
    return tri

  def axes(self, size=10, width=(500, "px"), height=(300, "px")):
    """
    Description:
    ------------

    Usage:
    --------------
    svg = rptObj.ui.charts.svg.axes()
    m = svg.defs().marker("circle", "0 0 10 10", 5, 5)
    m.circle(5, 5, 5, 'red')
    m.markerWidth(10).markerHeight(10)
    p = svg.path(0, 0, from_origin=True).line_to(50, 100).horizontal_line_to(300).line_to(400, 200)
    p.markers(m.url)

    Attributes:
    ----------
    :param size:
    :param width:
    :param height:
    """
    svg = graph.GraphSvg.SVG(self.parent.context.rptObj, width, height)
    svg.origine = (size, height[0]-size)
    defs = svg.defs()
    m = defs.marker("arrow", "0 0 10 10", 5, 5)
    m.arrow().orient("auto-start-reverse")
    m.markerWidth(size).markerHeight(size)
    pl = svg.polyline([(size, size), (size, height[0]-size), (width[0]-size, height[0]-size)]).css({'stroke': "black"})
    pl.marker_start(m.url)
    pl.marker_end(m.url)
    self.parent.context.register(svg)
    return svg

  def rectangle(self, x, y, width=(500, "px"), height=(300, "px"), fill=None, rx=0, ry=0):
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

  def heart(self, w, h, fill='none', width=(500, "px"), height=(300, "px")):
    """

    c = rptObj.ui.charts.svg.heart(w=50, h=100, fill="pink")
    c[0].transform("transform", "rotate", "0 100 100", "360 100 10")

    :param w:
    :param h:
    :param fill:
    :param width:
    :param height:
    """
    svg = graph.GraphSvg.SVG(self.parent.context.rptObj, width, height)
    svg.polygon([(w, w), (3/4 * h, 3/4 * h), (h, w), (h, 3/4 * w), (9/10 * h, 6/10 * w), (8.5/10 * h, 6/10 * w), (3/4 * h, 3/4 * w),
                 (2/3 * h, 6/10 * w), (6/10 * h, 6/10 * w), (w, 3/4 * w), (w, w)], fill=fill)
    self.parent.context.register(svg)
    return svg

  def star(self, fill='none', width=(500, "px"), height=(300, "px")):
    """

    https://codepen.io/susanwinters/pen/WxbRJK

    :param w:
    :param h:
    :param fill:
    :param width:
    :param height:
    """
    svg = graph.GraphSvg.SVG(self.parent.context.rptObj, width, height)
    svg.polygon([(100, 10), (40, 180), (190, 60), (10, 60), (160, 180)], fill=fill)
    svg[-1].css({"stroke": 'none'})
    self.parent.context.register(svg)
    return svg
