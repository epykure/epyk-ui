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

  def text(self, text, x, y):
    """

    :param text:
    :param x:
    :param y:

    :return:
    """
    self.html_objs.append(Text(self._report, text, x, y))
    return self.html_objs[-1]

  def rect(self, x, y, width, height, fill):
    """

    :param x:
    :param y:
    :param width:
    :param height:
    :param fill:
    :return:
    """
    self.html_objs.append(Rectangle(self._report, x, y, width, height, fill))
    return self.html_objs[-1]

  def line(self, x1, y1, x2, y2):
    """

    :param x1:
    :param y1:
    :param x2:
    :param y2:

    :return:
    """
    self.html_objs.append(Line(self._report, x1, y1, x2, y2))
    return self.html_objs[-1]

  def circle(self, x, y, r):
    """

    :param x:
    :param y:
    :param r:
    :return:
    """
    self.html_objs.append(Circle(self._report, x, y, r))
    return self.html_objs[-1]

  def ellipse(self, cx, cy, rx, ry):
    self.html_objs.append(Ellipse(self._report, cx, cy, rx, ry))
    return self.html_objs[-1]

  def polygon(self, points):
    self.html_objs.append(Polygone(self._report, points))
    return self.html_objs[-1]

  def triangle(self, width, options=None):
    """

    :param width:
    :param options:
    :return:
    """
    if isinstance(width, int):
      width = (width, "px")
    self.html_objs.append(Polyline(self._report, [(0, width[0]), (width[0]/2, 0), (width[0], width[0]), (0, width[0])],
                                   width, width, options or {}))
    return self

  def g(self):
    """

    :return:
    """
    self.html_objs.append(G(self._report))
    return self.html_objs[-1]

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class G(SVG):
  def __init__(self, report):
    super(G, self).__init__(report, None, None)
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<g %s>%s</g>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class SVGItem(Html.Html):

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
  def __init__(self, report, points):
    super(Polygone, self).__init__(report, points)
    self.set_attrs(({"points": " ".join(["%s,%s" % (x, y) for x, y in self.val])}))
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
  def __init__(self, report, x, y, width, height, fill):
    super(Rectangle, self).__init__(report, "", css_attrs={"width": width, "height": height})
    self.set_attrs({"x": x, "y": y, "fill": fill})
    self.css({"display": 'inline-block'})
    self.html_objs = []

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<rect %s>%s</rect>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Circle(SVGItem):
  def __init__(self, report, x, y, r):
    super(Circle, self).__init__(report, "")
    self.set_attrs({"cx": x, "cy": y, "r": r})
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
    self.html_objs.append(TSpan(self._report, text, x, y))
    return self

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


class Animate(Html.Html):
  # https://css-tricks.com/guide-svg-animations-smil/

  def __init__(self, report, attributeName, type,  from_pos, to_pos, duration, repeatCount):
    super(Animate, self).__init__(report, "")
    self.set_attrs({"attributeName": attributeName, "type": type, "from": from_pos, "to": to_pos,
                    "dur": "%ss" % duration, "repeatCount": repeatCount})

  def __str__(self):
    return "<animateTransform %s />" % self.get_attrs(pyClassNames=self.style.get_classes())
