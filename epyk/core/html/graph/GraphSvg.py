from epyk.core.html import Html


class SVG(Html.Html):
  def __init__(self, report, height, width):
    super(SVG, self).__init__(report, "", css_attrs={"width": width, "height": height})
    self.css({"display": 'inline-block'})
    self.html_objs = []

  def __getitem__(self, i):
    return self.html_objs[i]

  def text(self, text, x, y, options):
    """

    :param text:
    :param x:
    :param y:
    :param options:
    :return:
    """
    vals = ["%s='%s'" % (k, v) for k, v in options.items()]
    self.html_objs.append("<text x='%s' y='%s' %s>%s</text>" % (x, y, " ".join(vals), text))

  def rect(self, x, y, width, height, fill):
    self.html_objs.append(Rectangle(self._report, x, y, width, height, fill))

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


class Line(Html.Html):
  def __init__(self, report, x1, y1, x2, y2, height, width, options):
    super(Line, self).__init__(report, {"x1": x1, "y1": y1, "x2": x2, "y2": y2}, css_attrs={"width": width, "height": height})
    if options is not None:
      self._jsStyles.update(options)
    self.css({"display": 'inline-block'})

  def __str__(self):
    html_line = "<line x1='%s' y1='%s' x2='%s' y2='%s' style='stroke:%s;stroke-width:%s' />" % (self.val['x1'], self.val['y1'], self.val['x2'], self.val['y2'], self._jsStyles['stroke'], self._jsStyles["stroke-width"])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.style.get_classes()), html_line)


class Ellipse(Html.Html):
  def __init__(self, report, cx, cy, rx, ry, height, width, options):
    super(Ellipse, self).__init__(report, {"cx": cx, "cy": cy, "rx": rx, "ry": ry}, css_attrs={"width": width, "height": height})
    if options is not None:
      self._jsStyles.update(options)
    self.css({"display": 'inline-block'})

  def __str__(self):
    html_line = "<ellipse cx='%s' cy='%s' rx='%s' ry='%s' style='fill:%s;stroke:%s;stroke-width:%s' />" % (self.val['cx'], self.val['cy'], self.val['rx'], self.val['ry'], self._jsStyles['fill'], self._jsStyles['stroke'], self._jsStyles["stroke-width"])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.style.get_classes()), html_line)


class Polygone(Html.Html):
  def __init__(self, report, points, height, width, options):
    super(Polygone, self).__init__(report, points, css_attrs={"width": width, "height": height})
    if options is not None:
      self._jsStyles.update(options)
    self.css({"display": 'inline-block'})
    self._transform = None

  def animate(self, attributeName, type, from_pos, to_pos, duration=4, repeatCount="indefinite"):
    """

    :param attributeName:
    :param type:
    :param from_pos:
    :param to_pos:
    :param duration:
    :param repeatCount:

    :return:
    """
    self._transform = "<animateTransform attributeName='%s' type='%s' from='%s' to='%s' dur='%ss' repeatCount='%s' />" % (attributeName, type, from_pos, to_pos, duration, repeatCount)

  def __str__(self):
    str_point = " ".join(["%s,%s" % (x, y) for x, y in self.val])
    if self._transform is not None:
      html_line = "<polygon points='%s' style='fill:%s;stroke:%s;stroke-width:%s'>%s</polygon>" % (str_point, self._jsStyles['fill'], self._jsStyles['stroke'], self._jsStyles["stroke-width"], self._transform)
    else:
      html_line = "<polygon points='%s' style='fill:%s;stroke:%s;stroke-width:%s' />" % (str_point, self._jsStyles['fill'], self._jsStyles['stroke'], self._jsStyles["stroke-width"])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.style.get_classes()), html_line)


class Polyline(Html.Html):
  def __init__(self, report, points, height, width, options):
    super(Polyline, self).__init__(report, points, css_attrs={"width": width, "height": height})
    if options is not None:
      self._jsStyles.update(options)
    self.css({"display": 'inline-block'})

  def __str__(self):
    str_point = " ".join(["%s,%s" % (x, y) for x, y in self.val])
    html_line = "<polyline points='%s' style='fill:%s;stroke:%s;stroke-width:%s' />" % (str_point, self._jsStyles['fill'], self._jsStyles['stroke'], self._jsStyles["stroke-width"])
    return "<svg %s>%s</svg>" % (self.get_attrs(pyClassNames=self.style.get_classes()), html_line)


class Rectangle(Html.Html):
  def __init__(self, report, x, y, width, height, fill):
    super(Rectangle, self).__init__(report, "", css_attrs={"width": width, "height": height})
    self.set_attrs({"x": x, "y": y, "fill": fill})
    self.css({"display": 'inline-block'})
    self.html_objs = []

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

  def __str__(self):
    str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
    return "<rect %s>%s</rect>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_c)


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
