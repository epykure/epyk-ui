"""
SVG defines vector-based graphics in XML format

Documentation
https://www.w3schools.com/graphics/svg_intro.asp
"""

from epyk.core.html import Html


class SVG(Html.Html):
  def __init__(self, report, height, width):
    super(SVG, self).__init__(report, "", width=width[0], widthUnit=width[1],
                               height=height[0], heightUnit=height[1])
    self.css({"display": 'inline-block'})
    self.html_objs = []

  def add_text(self, text, x, y, options):
    """

    :param text:
    :param x:
    :param y:
    :param options:
    :return:
    """
    vals = ["%s='%s'" % (k, v) for k, v in options.items()]
    self.html_objs.append("<text x='%s' y='%s' %s>%s</text>" % (x, y, " ".join(vals), text))

  def __str__(self):
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.defined), "".join(self.html_objs))


class Line(Html.Html):
  def __init__(self, report, x1, y1, x2, y2, height, width, options):
    super(Line, self).__init__(report, {"x1": x1, "y1": y1, "x2": x2, "y2": y2}, width=width[0], widthUnit=width[1],
                               height=height[0], heightUnit=height[1])
    if options is not None:
      self._jsStyles.update(options)
    self.css({"display": 'inline-block'})

  def __str__(self):
    html_line = "<line x1='%s' y1='%s' x2='%s' y2='%s' style='stroke:%s;stroke-width:%s' />" % (self.val['x1'], self.val['y1'], self.val['x2'], self.val['y2'], self._jsStyles['stroke'], self._jsStyles["stroke-width"])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.defined), html_line)


class Ellipse(Html.Html):
  def __init__(self, report, cx, cy, rx, ry, height, width, options):
    super(Ellipse, self).__init__(report, {"cx": cx, "cy": cy, "rx": rx, "ry": ry}, width=width[0], widthUnit=width[1],
                                  height=height[0], heightUnit=height[1])
    if options is not None:
      self._jsStyles.update(options)
    self.css({"display": 'inline-block'})

  def __str__(self):
    html_line = "<ellipse cx='%s' cy='%s' rx='%s' ry='%s' style='fill:%s;stroke:%s;stroke-width:%s' />" % (self.val['cx'], self.val['cy'], self.val['rx'], self.val['ry'], self._jsStyles['fill'], self._jsStyles['stroke'], self._jsStyles["stroke-width"])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.defined), html_line)


class Polygone(Html.Html):
  def __init__(self, report, points, height, width, options):
    super(Polygone, self).__init__(report, points, width=width[0], widthUnit=width[1],
                                  height=height[0], heightUnit=height[1])
    if options is not None:
      self._jsStyles.update(options)
    self.css({"display": 'inline-block'})

  def __str__(self):
    str_point = " ".join(["%s,%s" % (x, y) for x, y in self.val])
    print(str_point)
    html_line = "<polygon points='%s' style='fill:%s;stroke:%s;stroke-width:%s' />" % (str_point, self._jsStyles['fill'], self._jsStyles['stroke'], self._jsStyles["stroke-width"])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.defined), html_line)


class Polyline(Html.Html):
  def __init__(self, report, points, height, width, options):
    super(Polyline, self).__init__(report, points, width=width[0], widthUnit=width[1],
                                  height=height[0], heightUnit=height[1])
    if options is not None:
      self._jsStyles.update(options)
    self.css({"display": 'inline-block'})

  def __str__(self):
    str_point = " ".join(["%s,%s" % (x, y) for x, y in self.val])
    print(str_point)
    html_line = "<polyline points='%s' style='fill:%s;stroke:%s;stroke-width:%s' />" % (str_point, self._jsStyles['fill'], self._jsStyles['stroke'], self._jsStyles["stroke-width"])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.defined), html_line)
