
from epyk.core.html import graph


class SVG:

  def __init__(self, ui):
    self.page = ui.page

  def new(self, width=(500, "px"), height=(300, "px")):
    """
    Description:
    ------------
    SVG stands for Scalable Vector Graphics.

    SVG defines vector-based graphics in XML format.

    :tags:
    :categories:

    Usage::

      svg = page.ui.charts.svg.new(width=200)
      svg.add_text("I love SVG!", x=0, y=15, options={"fill": 'red'})

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/SVG
      https://www.w3schools.com/graphics/svg_intro.asp

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    """
    if not isinstance(width, tuple):
      width = (width, "px")
    html_svg = graph.GraphSvg.SVG(self.page, width, height)
    return html_svg

  def line(self, x1=0, y1=None, x2=None, y2=None, width=(500, "px"), height=(300, "px"), options=None, profile=None):
    """
    Description:
    ------------
    Entry point to the basic line definition in a SVG HTML Tag.

    :tags:
    :categories:

    Usage::

      page.ui.charts.svg.line(10, 30, 40, 69)

    Related Pages:

      https://www.w3schools.com/graphics/svg_line.asp

    Attributes:
    ----------
    :param x1: The x1 attribute defines the start of the line on the x-axis.
    :param y1: The y1 attribute defines the start of the line on the y-axis.
    :param x2: The x2 attribute defines the end of the line on the x-axis.
    :param y2: The y2 attribute defines the end of the line on the y-axis.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    x2 = x2 or width[0]
    if y2 is None:
      y2 = 0 if height[1] == "%" else height[0] / 2
    if y1 is None:
      y1 = 0 if height[1] == "%" else height[0] / 2
    html_svg = graph.GraphSvg.SVG(self.page, width, height, options=options, profile=profile)
    html_svg.line(x1, y1, x2, y2)
    return html_svg

  def circle(self, x, y, r, width=(500, "px"), height=(300, "px"), options=None, profile=None):
    """
    Description:
    ------------
    Entry point to the basic line definition in a SVG HTML Tag.

    :tags:
    :categories:

    Usage::

      page.ui.charts.svg.line(10, 30, 40, 69)

    Related Pages:

      https://www.w3schools.com/graphics/svg_line.asp

    Attributes:
    ----------
    :param x: Float. The x attribute defines the start of the line on the x-axis.
    :param y: Float. The y attribute defines the start of the line on the y-axis.
    :param r: Float. The r attribute defines the radius.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_svg = graph.GraphSvg.SVG(self.page, width, height, options=options, profile=profile)
    html_svg.circle(x, y, r)
    return html_svg

  def arrow_right(self, x1=0, y1=None, x2=None, y2=None, size=10, width=(500, "px"), height=(300, "px"), html_code=None,
                  options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param size: Integer. Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    line = self.line(x1, y1, x2 or width[0]-size, y2, width, height, options, profile)
    defs = line.defs()
    m = defs.marker(html_code or "arrow_right", "0 0 10 10", 5, 5)
    m.arrow(size)
    line[0].marker_end(m.url)
    return line

  def arrow_left(self, x1=0, y1=None, x2=None, y2=None, size=10, width=(500, "px"), height=(300, "px"), html_code=None,
                 options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.charts.svg.arrow_left()

    Attributes:
    ----------
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param size: Integer. Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    line = self.line(x1+size, y1, x2, y2, width, height, options, profile)
    defs = line.defs()
    m = defs.marker(html_code or "arrow_left", "0 0 10 10", 5, 5)
    m.arrow(size).orient("auto-start-reverse")
    line[0].marker_start(m.url)
    return line

  def ellipse(self, cx, cy, rx, ry, width=(500, "px"), height=(300, "px"), options=None, profile=None):
    """
    Description:
    ------------
    SVG Ellipse - <ellipse>.

    :tags:
    :categories:

    Usage::

      page.ui.charts.svg.ellipse(100, 100, 40, 69)

    Related Pages:

      https://www.w3schools.com/graphics/svg_ellipse.asp

    Attributes:
    ----------
    :param cx: The cx attribute defines the x coordinate of the center of the ellipse
    :param cy: The cy attribute defines the y coordinate of the center of the ellipse
    :param rx: The rx attribute defines the horizontal radius
    :param ry: The ry attribute defines the vertical radius
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_svg = graph.GraphSvg.SVG(self.page, width, height, options=options, profile=profile)
    html_svg.ellipse(cx, cy, rx, ry)
    return html_svg

  def polyline(self, points, width=(500, "px"), height=(300, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.charts.svg.polyline([(15, 80), (29, 50), (43, 60), (57, 30), (71, 40), (85, 15)])

    Related Pages:

      https://www.w3schools.com/graphics/svg_polyline.asp

    Attributes:
    ----------
    :param points: The points attribute defines the list of points (pairs of coordinates) required to draw the polyline.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_svg = graph.GraphSvg.SVG(self.page, width, height, options=options, profile=profile)
    html_svg.polyline(points)
    return html_svg

  def polygone(self, points, width=(500, "px"), height=(300, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.charts.svg.polygone([(15, 80), (29, 50), (43, 60), (57, 30), (71, 40), (85, 15)])

    Related Pages:

      https://www.w3schools.com/graphics/tryit.asp?filename=trysvg_polygon

    Attributes:
    ----------
    :param points: The points attribute defines the list of points (pairs of coordinates) required to draw the polyline.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_svg = graph.GraphSvg.SVG(self.page, width, height, options=options, profile=profile)
    html_svg.polygon(points)
    return html_svg

  def triangle(self, point1, point2=None, point3=None, fill='None', width=(500, "px"), height=(300, "px"), options=None,
               profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      rptObj.ui.charts.svg.triangle((50, 100))

    Related Pages:

      https://www.w3schools.com/graphics/svg_polyline.asp

    Attributes:
    ----------
    :param point1:
    :param point2:
    :param point3:
    :param fill:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if point2 is None:
      point2 = (point1[1]/2, point1[0])
    if point3 is None:
      point3 = (point1[1], point1[1])
    tri = graph.GraphSvg.SVG(self.page, width, height, options=options, profile=profile)
    tri.triangle([point1, point2, point3, point1], fill=fill, options=options)
    return tri

  def axes(self, size=10, width=(500, "px"), height=(300, "px"), html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      svg = page.ui.charts.svg.axes()
      m = svg.defs().marker("circle", "0 0 10 10", 5, 5)
      m.circle(5, 5, 5, 'red')
      m.markerWidth(10).markerHeight(10)
      p = svg.path(0, 0, from_origin=True).line_to(50, 100).horizontal_line_to(300).line_to(400, 200)
      p.markers(m.url)

    Attributes:
    ----------
    :param size: Integer. Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    svg = graph.GraphSvg.SVG(self.page, width, height, options=options, profile=profile)
    svg.origine = (size, height[0]-size)
    defs = svg.defs()
    m = defs.marker(html_code or "arrow", "0 0 10 10", 5, 5)
    m.arrow().orient("auto-start-reverse")
    m.markerWidth(size).markerHeight(size)
    pl = svg.polyline([(size, size), (size, height[0]-size), (width[0]-size, height[0]-size)]).css({'stroke': "black"})
    pl.marker_start(m.url)
    pl.marker_end(m.url)
    return svg

  def rectangle(self, x, y, width=(500, "px"), height=(300, "px"), fill=None, rx=0, ry=0, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param x:
    :param y:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param fill:
    :param rx:
    :param ry:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    rect = graph.GraphSvg.SVG(self.page, (900, "px"), (200, "px"), options=options, profile=profile)
    rect.rect(x, y, width, height, fill, rx=rx, ry=ry)
    return rect

  def heart(self, w, h, fill='none', width=(500, "px"), height=(300, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      c = page.ui.charts.svg.heart(w=50, h=100, fill="pink")
      c[0].transform("transform", "rotate", "0 100 100", "360 100 10")

    Attributes:
    ----------
    :param w:
    :param h:
    :param fill:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    svg = graph.GraphSvg.SVG(self.page, width, height, options=options, profile=profile)
    svg.polygon([(w, w), (3/4 * h, 3/4 * h), (h, w), (h, 3/4 * w), (9/10 * h, 6/10 * w), (8.5/10 * h, 6/10 * w),
                 (3/4 * h, 3/4 * w), (2/3 * h, 6/10 * w), (6/10 * h, 6/10 * w), (w, 3/4 * w), (w, w)], fill=fill)
    return svg

  def star(self, fill='none', width=(500, "px"), height=(300, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://codepen.io/susanwinters/pen/WxbRJK

    Attributes:
    ----------
    :param fill:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    svg = graph.GraphSvg.SVG(self.page, width, height, options=options, profile=profile)
    svg.polygon([(100, 10), (40, 180), (190, 60), (10, 60), (160, 180)], fill=fill)
    svg[-1].css({"stroke": 'none'})
    return svg

  def path(self, x=0, y=0, fill='none', origin=False, bespoke_path=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

    Attributes:
    ----------
    :param x:
    :param y:
    :param fill:
    :param origin:
    :param bespoke_path:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    path = graph.GraphSvg.Path(self.page, x, y, fill, origin, bespoke_path, options=options, profile=profile)
    return path
