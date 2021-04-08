#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html


class SVG(Html.Html):
  name = 'SVG'

  def __init__(self, report, width, height, html_code=None, options=None, profile=None):
    super(SVG, self).__init__(
      report, "", html_code=html_code, options=options, profile=profile, css_attrs={"width": width, "height": height})
    self.origine = None
    if width is not None:
      self.set_attrs({"viewBox": "0 0 %s %s" % (width[0], height[0]), "version": '1.1',
                      'preserveAspectRatio': 'xMinYMin meet'})
    self.css({"display": 'inline-block'})
    self.html_objs = []

  def __add__(self, component):
    component.options.managed = False
    self.html_objs.append(component)

  def __getitem__(self, i):
    return self.html_objs[i]

  def click(self, js_funcs, profile=False, source_event=None, on_ready=False):
    """
    Description:
    ------------
    Add an event on the SVG.

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List of Js Functions. A Javascript Python function.
    :param profile: A Boolean. Set to true to get the profile for the function on the Javascript console.
    :param source_event: A String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    self.css({"cursor": 'pointer'})
    return self.on("click", js_funcs, profile, source_event)

  def defs(self):
    """
    Description:
    ------------
    The <defs> element is used to store graphical objects that will be used at a later time.
    Objects created inside a <defs> element are not rendered directly.
    To display them you have to reference them (with a <use> element for example

    Usage:
    -----

      defs = poly.defs()

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/SVG/Element/defs
    """
    self.html_objs.append(Defs(self._report))
    return self.html_objs[-1]

  def text(self, text, x, y, fill=None):
    """
    Description:
    ------------
    The <text> element can be arranged in any number of sub-groups with the <tspan> element.
    Each <tspan> element can contain different formatting and position.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/graphics/svg_text.asp

    Attributes:
    ----------
    :param text: String. The text to be added to the container.
    :param x: Float. The x coordinate of the starting point of the text baseline.
    :param y: Float. The y coordinate of the starting point of the text baseline.
    :param fill:

    :rtype: Text
    """
    fill = fill or self._report.theme.greys[-1]
    self.html_objs.append(Text(self._report, text, x, y, fill=fill))
    self.html_objs[-1].options.managed = False
    return self.html_objs[-1]

  def rect(self, x, y, width, height, fill, rx=0, ry=0):
    """
    Description:
    ------------
    The <rect> element is used to create a rectangle and variations of a rectangle shape.

    Usage:
    -----

    Related Pages:

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

    :rtype: Rectangle
    """
    self.html_objs.append(Rectangle(self._report, x, y, width, height, fill, rx, ry))
    self.html_objs[-1].options.managed = False
    return self.html_objs[-1]

  def line(self, x1, y1, x2, y2, stroke=None, stroke_width=None):
    """
    Description:
    ------------
    The <line> element is used to create a line.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/graphics/svg_line.asp

    Attributes:
    ----------
    :param x1: Float. The x1 attribute defines the start of the line on the x-axis.
    :param y1: Float. The y1 attribute defines the start of the line on the y-axis.
    :param x2: Float. The x2 attribute defines the end of the line on the x-axis.
    :param y2: Float. The y2 attribute defines the end of the line on the y-axis.
    :param stroke:
    :param stroke_width:

    :rtype: Line
    """
    line = Line(self._report, x1, y1, x2, y2)
    line.options.managed = False
    self.html_objs.append(line)
    if stroke is not None:
      line.css({"stroke": stroke, "stroke-width": stroke_width or 1})
    return self.html_objs[-1]

  def circle(self, x, y, r, fill="None", stroke=None, stroke_width=None):
    """
    Description:
    ------------
    The <circle> element is used to create a circle.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/graphics/svg_circle.asp

    Attributes:
    ----------
    :param x: Float. The x coordinate of the circle.
    :param y: Float. The y coordinate of the circle.
    :param r: Float. The r attribute defines the radius of the circle.
    :param fill:
    :param stroke:
    :param stroke_width:

    :rtype: Circle
    """
    circle = Circle(self._report, x, y, r, fill)
    circle.options.managed = False
    self.html_objs.append(circle)
    if stroke is not None:
      circle.set_attrs({"stroke": stroke, "stroke-width": stroke_width or 1})
    return self.html_objs[-1]

  def ellipse(self, cx, cy, rx, ry):
    """
    Description:
    ------------
    The <ellipse> element is used to create an ellipse.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/graphics/svg_ellipse.asp

    Attributes:
    ----------
    :param cx: Float. The cx attribute defines the x coordinate of the center of the ellipse.
    :param cy: Float. The cy attribute defines the y coordinate of the center of the ellipse.
    :param rx: Float. The rx attribute defines the horizontal radius.
    :param ry: Float. The ry attribute defines the vertical radius.

    :rtype: Ellipse
    """
    self.html_objs.append(Ellipse(self._report, cx, cy, rx, ry))
    self.html_objs[-1].options.managed = False
    return self.html_objs[-1]

  def polygon(self, points, fill="None"):
    """
    Description:
    ------------
    The <polygon> element is used to create a graphic that contains at least three sides.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/graphics/svg_polygon.asp

    Attributes:
    ----------
    :param points: String. The points attribute defines the x and y coordinates for each corner of the polygon.
    :param fill: String. Optional.

    :rtype: Polygone
    """
    self.html_objs.append(Polygone(self._report, points, fill))
    self.html_objs[-1].options.managed = False
    return self.html_objs[-1]

  def polyline(self, points, fill="None"):
    """
    Description:
    ------------
    The <polyline> element is used to create any shape that consists of only straight lines (that is connected at
    several points).

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/graphics/svg_polyline.asp

    Attributes:
    ----------
    :param points:
    :param fill:

    :rtype: Polyline
    """
    polygone = Polyline(self._report, points, height=None, width=None, fill=fill, options={})
    polygone.options.managed = False
    self.html_objs.append(polygone)
    return polygone

  def triangle(self, points, fill="None", options=None):
    """
    Description:
    ------------
    A polyline element with three points.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/graphics/svg_polyline.asp

    Attributes:
    ----------
    :param points:
    :param fill:
    :param options:

    :rtpye: Polyline
    """
    self.html_objs.append(Polyline(self._report, points, None, None, fill, options or {}))
    self.html_objs[-1].options.managed = False
    return self.html_objs[-1]

  def g(self, fill="None", stroke=None, stroke_width=None):
    """
    Description:
    ------------
    The <g> SVG element is a container used to group other SVG elements.

    Usage:
    -----

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/SVG/Element/g

    Attributes:
    ----------
    :param fill: String. Optional. The color for the component background.
    :param stroke: String. Optional. The color for the border.
    :param stroke_width: Float. Optional. The width of the component's border.

    :rtype: G
    """
    self.html_objs.append(G(self._report, fill, stroke, stroke_width))
    self.html_objs[-1].options.managed = False
    return self.html_objs[-1]

  def path(self, x=0, y=0, fill='none', from_origin=False, bespoke_path=None, stroke=None):
    """
    Description:
    ------------
    The <path> element is used to define a path.

    Related Pages:

      https://www.w3.org/TR/SVG/paths.html
      https://www.w3.org/TR/svg-paths/

    Attributes:
    ----------
    :param x: Number.
    :param y: Number.
    :param fill: String. Optional.
    :param from_origin:
    :param bespoke_path:
    :param stroke:

    :rtype: Path
    """
    if from_origin:
      x += self.origine[0]
      y += self.origine[1]
    path = Path(self._report, x, y, fill, self.origine, bespoke_path, stroke=stroke)
    path.options.managed = False
    self.html_objs.append(path)
    return self.html_objs[-1]

  def foreignObject(self, x, y, width, height):
    """
    Description:
    ------------
    The <foreignObject> SVG element includes elements from a different XML namespace. In the context of a browser,
    it is most likely (X)HTML.

    Usage:
    -----

    Related Pages:

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
    self.html_objs[-1].options.managed = False
    return self.html_objs[-1]

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class LinearGradient(Html.Html):
  def __init__(self, report, html_code, x1, y1, x2, y2, gradient_transform):
    super(LinearGradient, self).__init__(report, "", html_code=html_code)
    self.set_attrs({'gradientTransform': gradient_transform, "x1": x1, "y1": y1, "x2": x2, "y2": y2})
    self.items = []

  @property
  def url(self):
    """
    Description:
    -----------

    """
    return "url(#%s)" % self.htmlCode

  def stop(self, offset, styles):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param offset:
    :param styles:
    """
    self.items.append('<stop offset="%s" style="%s" />' % (
      offset, ";".join(["%s:%s" % (k, v) for k, v in styles.items()])))
    return self

  def __str__(self):
    return "<linearGradient %s>%s</linearGradient>" % (
      self.get_attrs(pyClassNames=self.style.get_classes()), "".join(self.items))


class RadialGradient(Html.Html):
  name = "SVG RadialGradient"

  def __init__(self, report, html_code):
    super(RadialGradient, self).__init__(report, "", html_code=html_code)
    self.items = []

  @property
  def url(self):
    """
    Description:
    -----------

    """
    return "url(#%s)" % self.htmlCode

  def stop(self, offset, styles):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param offset:
    :param styles:
    """
    self.items.append('<stop offset="%s" style="%s" />' % (
      offset, ";".join(["%s:%s" % (k, v) for k, v in styles.items()])))
    return self

  def __str__(self):
    return "<radialGradient %s>%s</radialGradient>" % (
      self.get_attrs(pyClassNames=self.style.get_classes()), "".join(self.items))


class Marker(SVG):

  def __init__(self, report, html_code, viewBox, refX, refY):
    super(Marker, self).__init__(report, None, None, html_code=html_code)
    self.set_attrs({'id': html_code, "viewBox": viewBox, "refX": refX, "refY": refY})
    self.html_objs = []

  @property
  def url(self):
    """
    Description:
    -----------

    Usage:
    -----

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/SVG/Element/marker
    """
    return "url(#%s)" % self.htmlCode

  def orient(self, orientation):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param orientation:
    """
    self.set_attrs(name="orient", value=orientation)
    return self

  def markerWidth(self, value):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param value:
    """
    self.set_attrs(name="markerWidth", value=value)
    return self

  def markerHeight(self, value):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param value:
    """
    self.set_attrs(name="markerHeight", value=value)
    return self

  def arrow(self, size=None):
    """
    Description:
    -----------

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/SVG/Element/marker

    Attributes:
    ----------
    :param size:
    """
    self.html_objs.append("<path d='M 0 0 L 10 5 L 0 10 z' />")
    if size is not None:
      self.markerWidth(size).markerHeight(size)
    return self

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<marker %s>%s</marker>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Defs(Html.Html):
  name = 'SVG Defs'

  def __init__(self, report):
    super(Defs, self).__init__(report, "")
    self.html_objs = []

  def linearGradient(self, html_code, x1="0%", y1="0%", x2="100%", y2="0%", gradient_transform=None):
    """
    Description:
    ------------
    The <linearGradient> element lets authors define linear gradients that can be applied to fill or stroke of
    graphical elements.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/SVG/Element/linearGradient

    Attributes:
    ----------
    :param html_code: String. The HTML id of the component
    :param x1: Float.
    :param y1: Float.
    :param x2: Float.
    :param y2: Float.
    :param gradient_transform:

    :rtype: LinearGradient
    """
    self.html_objs.append(LinearGradient(self._report, html_code, x1, y1, x2, y2, gradient_transform))
    return self.html_objs[-1]

  def radialGradient(self, html_code):
    """
    Description:
    ------------
    The <radialGradient> element lets authors define radial gradients that can be applied to fill or stroke of
    graphical elements.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/SVG/Element/radialGradient

    Attributes:
    ----------
    :param html_code: String. The HTML id of the component.

    :rtype: radialGradient
    """
    self.html_objs.append(RadialGradient(self._report, html_code))
    return self.html_objs[-1]

  def marker(self, html_code, viewBox, refX, refY):
    """
    Description:
    -----------
    The <marker> element defines the graphic that is to be used for drawing arrowheads or polymarkers on a given
    <path>, <line>, <polyline> or <polygon> element.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/SVG/Element/marker

    Attributes:
    ----------
    :param html_code:
    :param viewBox:
    :param refX:
    :param refY:

    :rtype: Marker
    """
    self.html_objs.append(Marker(self._report, html_code, viewBox, refX, refY))
    return self.html_objs[-1]

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<defs %s>%s</defs>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class ForeignObject(SVG):
  def __init__(self, report, x, y, width, height):
    super(ForeignObject, self).__init__(report, None, None)
    self.set_attrs({"x": x, "y": y, "width": width, "height": height})
    self.html_objs = []

  def add(self, components):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param components:
    """
    if not isinstance(components, list):
      components = [components]
    for h in components:
      h.options.managed = False
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
  name = 'SVG Item'

  def fill(self, color):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param color:
    """
    self.set_attrs(name="fill", value=color)
    return self

  def transform(self, attribute_name, type, from_pos, to_pos, duration=4, repeat_count="indefinite"):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param attribute_name:
    :param type:
    :param from_pos:
    :param to_pos:
    :param duration:
    :param repeat_count:
    """
    self.html_objs.append(AnimateTransform(
      self._report, attribute_name, type, from_pos, to_pos, duration, repeat_count))
    return self


class Polygone(SVGItem):
  name = 'SVG Polygone'

  def __init__(self, report, points, fill):
    super(Polygone, self).__init__(report, points)
    self.set_attrs(({"points": " ".join(["%s,%s" % (x, y) for x, y in self.val]), "fill": fill}))
    self.css({'stroke': report.theme.greys[-1], 'stroke-width': 1})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<polygon %s>%s</polygon>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Ellipse(SVGItem):
  name = 'SVG Epplipse'

  def __init__(self, report, cx, cy, rx, ry):
    super(Ellipse, self).__init__(report, "")
    self.set_attrs({"cx": cx, "cy": cy, "rx": rx, "ry": ry})
    self.css({'stroke': report.theme.success[1], 'stroke-width': 1, 'fill': 'none'})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<ellipse %s>%s</ellipse>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Line(SVGItem):
  name = 'SVG Line'

  def __init__(self, report, x1, y1, x2, y2):
    super(Line, self).__init__(report, "")
    self.set_attrs({"x1": x1, "y1": y1, "x2": x2, "y2": y2})
    self.css({"stroke": report.theme.greys[-1], "stroke-width": 1})
    self.html_objs = []

  def markers(self, marker_code):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param marker_code:
    """
    self.set_attrs(name="marker-start", value=marker_code)
    self.set_attrs(name="marker-mid", value=marker_code)
    self.set_attrs(name="marker-end", value=marker_code)
    return self

  def marker_start(self, marker_code):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param marker_code:
    """
    self.set_attrs(name="marker-start", value=marker_code)

  def marker_mid(self, marker_code):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param marker_code:
    """
    self.set_attrs(name="marker-mid", value=marker_code)

  def marker_end(self, marker_code):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param marker_code:
    """
    self.set_attrs(name="marker-end", value=marker_code)

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<line %s>%s</line>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Polyline(SVGItem):
  name = 'SVG Polyline'

  def __init__(self, report, points, height, width, fill, options):
    super(Polyline, self).__init__(report, points, css_attrs={"width": width, "height": height})
    self.set_attrs({"fill": fill, "points": " ".join(["%s,%s" % (x, y) for x, y in self.val])})
    self.html_objs = []
    if options is not None:
      self._jsStyles.update(options)
    self.css({"display": 'inline-block', "fill": options.get('fill', ''),
              'stroke': options.get('stroke', report.theme.success[1]), 'stroke-width': options.get('stroke-width', 1)})

  def markers(self, marker_code):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param marker_code:
    """
    self.set_attrs(name="marker-start", value=marker_code)
    self.set_attrs(name="marker-mid", value=marker_code)
    self.set_attrs(name="marker-end", value=marker_code)
    return self

  def marker_start(self, marker_code):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param marker_code:
    """
    self.set_attrs(name="marker-start", value=marker_code)

  def marker_mid(self, marker_code):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param marker_code:
    """
    self.set_attrs(name="marker-mid", value=marker_code)

  def marker_end(self, marker_code):
    """

    Attributes:
    ----------
    :param marker_code:
    """
    self.set_attrs(name="marker-end", value=marker_code)

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<polyline %s>%s</polyline>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Rectangle(SVGItem):
  name = 'SVG Rectangle'

  def __init__(self, report, x, y, width, height, fill, rx, ry):
    super(Rectangle, self).__init__(report, "", css_attrs={"width": width, "height": height})
    self.set_attrs({"x": x, "y": y, "fill": fill, "rx": rx, "ry": ry})
    self.css({"display": 'inline-block'})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<rect %s>%s</rect>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Circle(SVGItem):
  name = 'SVG Circle'

  def __init__(self, report, x, y, r, fill):
    super(Circle, self).__init__(report, "")
    self.set_attrs({"cx": x, "cy": y, "r": r, "fill": fill})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<circle %s>%s</circle>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Text(SVGItem):
  name = 'SVG Text'

  def __init__(self, report, text, x, y, fill):
    super(Text, self).__init__(report, text)
    self.set_attrs({"x": x, "y": y, 'fill': fill})
    self.html_objs = []

  def line(self, text, x, y):
    """
    Description:
    ------------
    The SVG <tspan> element defines a subtext within a <text> element or another <tspan> element.
    It allows for adjustment of the style and/or position of that subtext as needed.

    Related Pages:

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
  name = 'SVG TSpan'

  def __init__(self, report, text, x, y):
    super(TSpan, self).__init__(report, text)
    self.set_attrs({"x": x, "y": y, 'fill': 'black'})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<tspan %s>%s%s</tspan>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val, str_c)


class Path(SVGItem):
  name = 'SVG Path'

  def __init__(self, report, x, y, fill, origin, bespoke_path, stroke=None, options=None, profile=None):
    super(Path, self).__init__(report, "", options=options, profile=profile)
    self.set_attrs({'fill': fill})
    if stroke is not None:
      self.set_attrs({"stroke": stroke, "stroke-width": 1})
    if bespoke_path:
      if type(bespoke_path) != list:
        bespoke_path = [bespoke_path]
      self.__path = bespoke_path
    else:
      self.__path = ["M%s %s" % (x, y)]
    self.html_objs = []
    self.origin = origin

  def markers(self, marker_code):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param marker_code:
    """
    self.set_attrs(name="marker-start", value=marker_code)
    self.set_attrs(name="marker-mid", value=marker_code)
    self.set_attrs(name="marker-end", value=marker_code)
    return self

  def line_to(self, x, y):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param x: Number.
    :param y: Number.
    """
    if self.origin is not None:
      x = self.origin[0] + x
      y = self.origin[1] - y
    self.__path.append("L%s %s" % (x, y))
    return self

  def horizontal_line_to(self, x):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param x: Number.
    """
    if self.origin is not None:
      x = self.origin[0] + x
    self.__path.append("H%s" % x)
    return self

  def vertical_line_to(self, y):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param y: Number.
    """
    if self.origin is not None:
      y = self.origin[1] - y
    self.__path.append("V%s" % y)
    return self

  def move_to(self, x, y):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param x: Number.
    :param y: Number.
    """
    if self.origin is not None:
      x = self.origin[0] + x
      y = self.origin[1] - y
    self.__path.append("M%s %s" % (x, y))
    return self

  def curve_to(self, x1, y1, x2, y2):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3.org/TR/svg-paths/

    Attributes:
    ----------
    :param x1: Number.
    :param y1: Number.
    :param x2: Number.
    :param y2: Number.
    """
    if self.origin is not None:
      x1 = self.origin[0] + x1
      y1 = self.origin[1] - y1
      x2 = self.origin[0] + x2
      y2 = self.origin[1] - y2
    self.__path.append("C%s %s %s %s" % (x1, y1, x2, y2))
    return self

  def smooth_curve_to(self, x1, y1, x2, y2):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3.org/TR/svg-paths/

    Attributes:
    ----------
    :param x1: Number.
    :param y1: Number.
    :param x2: Number.
    :param y2: Number.
    """
    if self.origin is not None:
      x1 = self.origin[0] + x1
      y1 = self.origin[1] - y1
      x2 = self.origin[0] + x2
      y2 = self.origin[1] - y2
    self.__path.append("S%s %s %s %s" % (x1, y1, x2, y2))
    return self

  def quadratic_bezier_curve_to(self, x1, y1, x2, y2):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3.org/TR/svg-paths/

    Attributes:
    ----------
    :param x1: Number.
    :param y1: Number.
    :param x2: Number.
    :param y2: Number.
    """
    if self.origin is not None:
      x1 = self.origin[0] + x1
      y1 = self.origin[1] - y1
      x2 = self.origin[0] + x2
      y2 = self.origin[1] - y2
    self.__path.append("Q%s %s %s %s" % (x1, y1, x2, y2))
    return self

  def smooth_quadratic_bezier_curve_to(self, x, y, absolute=True):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3.org/TR/svg-paths/

    Attributes:
    ----------
    :param x: Number.
    :param y: Number.
    :param absolute: Boolean. Optional.
    """
    if self.origin is not None:
      x = self.origin[0] + x
      y = self.origin[1] - y
    self.__path.append("T%s %s" % (x, y))
    return self

  def close_path(self):
    """
    Description:
    -----------

    """
    self.__path.append("Z")
    return self

  def __str__(self):
    self.set_attrs(name="d", value="".join(self.__path))
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<path %s>%s%s</path>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val, str_c)


class AnimateTransform(Html.Html):
  name = "SVG AnimateTransform"

  def __init__(self, report, attribute_name, type,  from_pos, to_pos, duration, repeat_count):
    super(AnimateTransform, self).__init__(report, "")
    self.set_attrs({"attributeName": attribute_name, "type": type, "from": from_pos, "to": to_pos,
                    "dur": "%ss" % duration, "repeatCount": repeat_count})

  def __str__(self):
    return "<animateTransform %s />" % self.get_attrs(pyClassNames=self.style.get_classes())


# https://stackoverflow.com/questions/6725288/svg-text-inside-rect


class Animate(Html.Html):
  name = "SVG Animate"
  # https://css-tricks.com/guide-svg-animations-smil/

  def __init__(self, report, attribute_name, type, from_pos, to_pos, duration, repeat_count):
    super(Animate, self).__init__(report, "")
    self.set_attrs({"attributeName": attribute_name, "type": type, "from": from_pos, "to": to_pos,
                    "dur": "%ss" % duration, "repeatCount": repeat_count})

  def __str__(self):
    return "<animateTransform %s />" % self.get_attrs(pyClassNames=self.style.get_classes())
