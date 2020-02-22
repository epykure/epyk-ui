from epyk.core.html import Html


class SVG(Html.Html):
  def __init__(self, report, width, height):
    super(SVG, self).__init__(report, "", css_attrs={"width": width, "height": height})
    if width is not None:
      self.set_attrs({"viewBox": "0 0 %s %s" % (width[0], height[0]), "version": '1.1', 'preserveAspectRatio': 'xMinYMin meet'})
    self.css({"display": 'inline-block'})
    self.html_objs = []

  def __getitem__(self, i):
    return self.html_objs[i]

  def defs(self):
    """
    Description:
    ------------
    The <defs> element is used to store graphical objects that will be used at a later time.
    Objects created inside a <defs> element are not rendered directly.
    To display them you have to reference them (with a <use> element for exampl

    Usage:
    ------
    defs = poly.defs()

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/defs
    """
    self.html_objs.append(Defs(self._report))
    return self.html_objs[-1]

  def text(self, text, x, y):
    """
    Description:
    ------------
    The <text> element can be arranged in any number of sub-groups with the <tspan> element.
    Each <tspan> element can contain different formatting and position.

    Usage:
    ------

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_text.asp

    Attributes:
    ----------
    :param text: String. The text to be added to the container
    :param x: Float. The x coordinate of the starting point of the text baseline.
    :param y: Float. The y coordinate of the starting point of the text baseline.

    :rtype: Text
    """
    self.html_objs.append(Text(self._report, text, x, y))
    return self.html_objs[-1]

  def rect(self, x, y, width, height, fill, rx=0, ry=0):
    """
    Description:
    ------------
    The <rect> element is used to create a rectangle and variations of a rectangle shape

    Usage:
    ------

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_rect.asp

    Attributes:
    ----------
    :param x:
    :param y:
    :param width:
    :param height:
    :param fill:
    :param rx:
    :param ry:
    """
    self.html_objs.append(Rectangle(self._report, x, y, width, height, fill, rx, ry))
    return self.html_objs[-1]

  def line(self, x1, y1, x2, y2):
    """
    Description:
    ------------
    The <line> element is used to create a line

    Usage:
    ------

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_line.asp

    Attributes:
    ----------
    :param x1: Float. The x1 attribute defines the start of the line on the x-axis
    :param y1: Float. The y1 attribute defines the start of the line on the y-axis
    :param x2: Float. The x2 attribute defines the end of the line on the x-axis
    :param y2: Float. The y2 attribute defines the end of the line on the y-axis

    :rtype: Line
    """
    self.html_objs.append(Line(self._report, x1, y1, x2, y2))
    return self.html_objs[-1]

  def circle(self, x, y, r, fill):
    """
    Description:
    ------------
    The <circle> element is used to create a circle

    Usage:
    ------

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_circle.asp

    Attributes:
    ----------
    :param x: Float. The x coordinate of the circle
    :param y: Float. The y coordinate of the circle
    :param r: Float. The r attribute defines the radius of the circle

    :rtype: Circle
    """
    self.html_objs.append(Circle(self._report, x, y, r, fill))
    return self.html_objs[-1]

  def ellipse(self, cx, cy, rx, ry):
    """
    Description:
    ------------
    The <ellipse> element is used to create an ellipse

    Usage:
    ------

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_ellipse.asp

    Attributes:
    ----------
    :param cx: Float. The cx attribute defines the x coordinate of the center of the ellipse
    :param cy: Float. The cy attribute defines the y coordinate of the center of the ellipse
    :param rx: Float. The rx attribute defines the horizontal radius
    :param ry: Float. The ry attribute defines the vertical radius

    :rtype: Ellipse
    """
    self.html_objs.append(Ellipse(self._report, cx, cy, rx, ry))
    return self.html_objs[-1]

  def polygon(self, points, fill=None):
    """
    Description:
    ------------
    The <polygon> element is used to create a graphic that contains at least three sides.

    Usage:
    ------

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_polygon.asp

    Attributes:
    ----------
    :param points: String. The points attribute defines the x and y coordinates for each corner of the polygon

    :rtype: Polygone
    """
    self.html_objs.append(Polygone(self._report, points, fill))
    return self.html_objs[-1]

  def polyline(self, points):
    """
    Description:
    ------------
    The <polyline> element is used to create any shape that consists of only straight lines (that is connected at several points)

    Usage:
    ------

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_polyline.asp

    Attributes:
    ----------
    :param points:

    :rtype: Polyline
    """

  def triangle(self, width, options=None):
    """
    Description:
    ------------
    A polyline element with three points

    Usage:
    ------

    Related Pages:
    --------------
    https://www.w3schools.com/graphics/svg_polyline.asp

    Attributes:
    ----------
    :param width:
    :param options:

    :rtpye: Polyline
    """
    if isinstance(width, int):
      width = (width, "px")
    self.html_objs.append(Polyline(self._report, [(0, width[0]), (width[0]/2, 0), (width[0], width[0]), (0, width[0])],
                                   width, width, options or {}))
    return self.html_objs[-2]

  def g(self, fill=None, stroke=None, stroke_width=None):
    """
    Description:
    ------------
    The <g> SVG element is a container used to group other SVG elements.

    Usage:
    ------

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/g

    Attributes:
    ----------
    :param fill: String. The color for the component background
    :param stroke: String. The color for the border
    :param stroke_width: Float. The width of the component's border

    :rtype: G
    """
    self.html_objs.append(G(self._report, fill, stroke, stroke_width))
    return self.html_objs[-1]

  def foreignObject(self, x, y, width, height):
    """
    Description:
    ------------
    The <foreignObject> SVG element includes elements from a different XML namespace. In the context of a browser, it is most likely (X)HTML.

    Usage:
    ------

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/foreignObject

    Attributes:
    ----------
    :param x: Float. The x coordinate of the foreignObject.
    :param y: Float. The y coordinate of the foreignObject.
    :param width: Float or Percentage. The width of the foreignObject.
    :param height: Float or Percentage. The height of the foreignObject.

    :rtype: ForeignObject
    """
    self.html_objs.append(ForeignObject(self._report, x, y, width, height))
    return self.html_objs[-1]

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class LinearGradient(Html.Html):
  def __init__(self, report, htmlCode, x1, y1, x2, y2, gradientTransform):
    super(LinearGradient, self).__init__(report, "", htmlCode=htmlCode)
    self.set_attrs({'gradientTransform': gradientTransform, "x1": x1, "y1": y1, "x2": x2, "y2": y2})
    self.items = []

  @property
  def url(self):
    return "url(#%s)" % self.htmlCode

  def stop(self, offset, styles):
    self.items.append('<stop offset="%s" style="%s" />' % (offset, ";".join(["%s:%s" % (k, v) for k, v in styles.items()])))
    return self

  def __str__(self):
    return "<linearGradient %s>%s</linearGradient>" % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(self.items))


class Defs(Html.Html):
  def __init__(self, report):
    super(Defs, self).__init__(report, "")
    self.html_objs = []

  def linearGradient(self, htmlCode, x1="0%", y1="0%", x2="100%", y2="0%", gradientTransform=None):
    """

    Attributes:
    ----------
    :param htmlCode:
    :param gradientTransform:

    :rtype: LinearGradient
    """
    self.html_objs.append(LinearGradient(self._report, htmlCode, x1, y1, x2, y2, gradientTransform))
    return self.html_objs[-1]

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<defs %s>%s</defs>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class ForeignObject(SVG):
  def __init__(self, report, x, y, width, height):
    super(ForeignObject, self).__init__(report, None, None)
    self.set_attrs({"x": x, "y": y, "width": width, "height": height})
    self.html_objs = []

  def add(self, htmlObj):
    """

    :param htmlObj:
    """
    if not isinstance(htmlObj, list):
      htmlObj = [htmlObj]
    for h in htmlObj:
      h.inReport = False
      self.html_objs.append(h)

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<foreignObject %s>%s</foreignObject>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class G(SVG):
  def __init__(self, report, fill, stroke, stroke_width):
    super(G, self).__init__(report, None, None)
    self.set_attrs({"fill": fill, "stroke": stroke, "stroke-width": stroke_width})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<g %s>%s</g>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class SVGItem(Html.Html):

  def fill(self, color):
    """

    :param color:
    :return:
    """
    self.set_attrs(name="fill", value=color)
    return self

  def transform(self, attributeName, type, from_pos, to_pos, duration=4, repeatCount="indefinite"):
    """

    :param attributeName:
    :param type:
    :param from_pos:
    :param to_pos:
    :param duration:
    :param repeatCount:

    :return:
    """
    self.html_objs.append(AnimateTransform(self._report, attributeName, type, from_pos, to_pos, duration, repeatCount))
    return self


class Polygone(SVGItem):
  def __init__(self, report, points, fill):
    super(Polygone, self).__init__(report, points)
    self.set_attrs(({"points": " ".join(["%s,%s" % (x, y) for x, y in self.val]), "fill": fill}))
    self.css({'stroke': report.theme.success[1], 'stroke-width': 1, 'fill': 'none'})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<polygon %s>%s</polygon>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Ellipse(SVGItem):
  def __init__(self, report, cx, cy, rx, ry):
    super(Ellipse, self).__init__(report, "")
    self.set_attrs({"cx": cx, "cy": cy, "rx": rx, "ry": ry})
    self.css({'stroke': report.theme.success[1], 'stroke-width': 1, 'fill': 'none'})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<ellipse %s>%s</ellipse>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Line(SVGItem):
  def __init__(self, report, x1, y1, x2, y2):
    super(Line, self).__init__(report, "")
    self.set_attrs({"x1": x1, "y1": y1, "x2": x2, "y2": y2})
    self.css({"stroke": report.theme.success[1], "stroke-width": 1})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<line %s>%s</line>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Polyline(SVGItem):
  def __init__(self, report, points, height, width, options):
    super(Polyline, self).__init__(report, points, css_attrs={"width": width, "height": height})
    self.set_attrs({"points": " ".join(["%s,%s" % (x, y) for x, y in self.val])})
    self.html_objs = []
    if options is not None:
      self._jsStyles.update(options)
    self.css({"display": 'inline-block', "fill": options.get('fill', ''),
              'stroke': options.get('stroke', report.theme.success[1]), 'stroke-width': options.get('stroke-width', 1)})

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<polyline %s>%s</polyline>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Rectangle(SVGItem):
  def __init__(self, report, x, y, width, height, fill, rx, ry):
    super(Rectangle, self).__init__(report, "", css_attrs={"width": width, "height": height})
    self.set_attrs({"x": x, "y": y, "fill": fill, "rx": rx, "ry": ry})
    self.css({"display": 'inline-block'})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<rect %s>%s</rect>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Circle(SVGItem):
  def __init__(self, report, x, y, r, fill):
    super(Circle, self).__init__(report, "")
    self.set_attrs({"cx": x, "cy": y, "r": r, "fill": fill})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<circle %s>%s</circle>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Text(SVGItem):
  def __init__(self, report, text, x, y):
    super(Text, self).__init__(report, text)
    self.set_attrs({"x": x, "y": y, 'fill': 'black'})
    self.html_objs = []

  def line(self, text, x, y):
    """
    Description:
    ------------
    The SVG <tspan> element defines a subtext within a <text> element or another <tspan> element.
    It allows for adjustment of the style and/or position of that subtext as needed.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/tspan

    Attributes:
    ----------
    :param text: String. The text to be added to the container
    :param x: Float. The x coordinate of the starting point of the text baseline.
    :param y: Float. The y coordinate of the starting point of the text baseline.

    :rtype: TSpan
    """
    self.html_objs.append(TSpan(self._report, text, x, y))
    return self.html_objs[-1]

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<text %s>%s%s</text>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val, str_c)


class TSpan(SVGItem):
  def __init__(self, report, text, x, y):
    super(TSpan, self).__init__(report, text)
    self.set_attrs({"x": x, "y": y, 'fill': 'black'})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<tspan %s>%s%s</tspan>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val, str_c)


class AnimateTransform(Html.Html):

  def __init__(self, report, attributeName, type,  from_pos, to_pos, duration, repeatCount):
    super(AnimateTransform, self).__init__(report, "")
    self.set_attrs({"attributeName": attributeName, "type": type, "from": from_pos, "to": to_pos,
                    "dur": "%ss" % duration, "repeatCount": repeatCount})

  def __str__(self):
    return "<animateTransform %s />" % self.get_attrs(pyClassNames=self.style.get_classes())

# https://stackoverflow.com/questions/6725288/svg-text-inside-rect

class Animate(Html.Html):
  # https://css-tricks.com/guide-svg-animations-smil/

  def __init__(self, report, attributeName, type,  from_pos, to_pos, duration, repeatCount):
    super(Animate, self).__init__(report, "")
    self.set_attrs({"attributeName": attributeName, "type": type, "from": from_pos, "to": to_pos,
                    "dur": "%ss" % duration, "repeatCount": repeatCount})

  def __str__(self):
    return "<animateTransform %s />" % self.get_attrs(pyClassNames=self.style.get_classes())
