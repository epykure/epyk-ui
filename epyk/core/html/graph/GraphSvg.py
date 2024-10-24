#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html


class SVG(Html.Html):
    name = 'SVG'
    tag = "svg"

    def __init__(self, page, width, height, html_code=None, options=None, profile=None):
        super(SVG, self).__init__(
            page, "", html_code=html_code, options=options, profile=profile,
            css_attrs={"width": width, "height": height})
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
        """Add an event on the SVG.

        :param js_funcs: List of Js Functions. A Javascript Python function.
        :param profile: A Boolean. Set to true to get the profile for the function on the Javascript console.
        :param source_event: A String. Optional. The source target for the event.
        :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
        """
        self.css({"cursor": 'pointer'})
        return self.on("click", js_funcs, profile, source_event)

    def defs(self):
        """The <defs> element is used to store graphical objects that will be used at a later time.
        Objects created inside a <defs> element are not rendered directly.
        To display them you have to reference them (with a <use> element for example

        Usage::

          defs = poly.defs()

        `SVG Doc <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/defs>`_
        """
        self.html_objs.append(Defs(self.page))
        return self.html_objs[-1]

    def text(self, text, x, y, fill=None):
        """The <text> element can be arranged in any number of sub-groups with the <tspan> element.
        Each <tspan> element can contain different formatting and position.

        `SVG Doc <https://www.w3schools.com/graphics/svg_text.asp>`_

        :param text: String. The text to be added to the container.
        :param x: Float. The x coordinate of the starting point of the text baseline.
        :param y: Float. The y coordinate of the starting point of the text baseline.
        :param fill:
        """
        fill = fill or self.page.theme.greys[-1]
        self.html_objs.append(Text(self.page, text, x, y, fill=fill))
        self.html_objs[-1].options.managed = False
        return self.html_objs[-1]

    def rect(self, x, y, width, height, fill, rx=0, ry=0):
        """The <rect> element is used to create a rectangle and variations of a rectangle shape.

        `SVG Doc <https://www.w3schools.com/graphics/svg_rect.asp>`_

        :param x:
        :param y:
        :param width:
        :param height:
        :param fill:
        :param rx:
        :param ry:

        :rtype: Rectangle
        """
        self.html_objs.append(Rectangle(self.page, x, y, width, height, fill, rx, ry))
        self.html_objs[-1].options.managed = False
        return self.html_objs[-1]

    def line(self, x1, y1, x2, y2, stroke=None, stroke_width=None) -> 'Line':
        """The <line> element is used to create a line.

        `SVG Doc <https://www.w3schools.com/graphics/svg_line.asp>`_

        :param x1: Float. The x1 attribute defines the start of the line on the x-axis.
        :param y1: Float. The y1 attribute defines the start of the line on the y-axis.
        :param x2: Float. The x2 attribute defines the end of the line on the x-axis.
        :param y2: Float. The y2 attribute defines the end of the line on the y-axis.
        :param stroke:
        :param stroke_width:
        """
        line = Line(self.page, x1, y1, x2, y2)
        line.options.managed = False
        self.html_objs.append(line)
        if stroke is not None:
            line.css({"stroke": stroke, "stroke-width": stroke_width or 1})
        return self.html_objs[-1]

    def circle(self, x, y, r, fill="None", stroke=None, stroke_width=None) -> 'Circle':
        """The <circle> element is used to create a circle.

        `SVG Doc <https://www.w3schools.com/graphics/svg_circle.asp>`_

        :param x: Float. The x coordinate of the circle.
        :param y: Float. The y coordinate of the circle.
        :param r: Float. The r attribute defines the radius of the circle.
        :param fill:
        :param stroke:
        :param stroke_width:
        """
        circle = Circle(self.page, x, y, r, fill)
        circle.options.managed = False
        self.html_objs.append(circle)
        if stroke is not None:
            circle.set_attrs({"stroke": stroke, "stroke-width": stroke_width or 1})
        return self.html_objs[-1]

    def ellipse(self, cx, cy, rx, ry) -> 'Ellipse':
        """The <ellipse> element is used to create an ellipse.

        `SVG Doc <https://www.w3schools.com/graphics/svg_ellipse.asp>`_

        :param cx: Float. The cx attribute defines the x coordinate of the center of the ellipse.
        :param cy: Float. The cy attribute defines the y coordinate of the center of the ellipse.
        :param rx: Float. The rx attribute defines the horizontal radius.
        :param ry: Float. The ry attribute defines the vertical radius.
        """
        self.html_objs.append(Ellipse(self.page, cx, cy, rx, ry))
        self.html_objs[-1].options.managed = False
        return self.html_objs[-1]

    def polygon(self, points, fill="None") -> 'Polygone':
        """The <polygon> element is used to create a graphic that contains at least three sides.

        `SVG Doc <https://www.w3schools.com/graphics/svg_polygon.asp>`_

        :param points: String. The points attribute defines the x and y coordinates for each corner of the polygon.
        :param fill: String. Optional.
        """
        self.html_objs.append(Polygone(self.page, points, fill))
        self.html_objs[-1].options.managed = False
        return self.html_objs[-1]

    def polyline(self, points, fill="None") -> 'Polyline':
        """The <polyline> element is used to create any shape that consists of only straight lines (that is connected at
        several points).

        `SVG Doc <https://www.w3schools.com/graphics/svg_polyline.asp>`_

        :param points:
        :param fill:
        """
        polygone = Polyline(self.page, points, height=None, width=None, fill=fill, options={})
        polygone.options.managed = False
        self.html_objs.append(polygone)
        return polygone

    def triangle(self, points, fill="None", options=None) -> 'Polyline':
        """A polyline element with three points.

        `SVG Doc <https://www.w3schools.com/graphics/svg_polyline.asp>`_

        :param points:
        :param fill:
        :param options:
        """
        self.html_objs.append(Polyline(self.page, points, None, None, fill, options or {}))
        self.html_objs[-1].options.managed = False
        return self.html_objs[-1]

    def g(self, fill="None", stroke=None, stroke_width=None) -> 'G':
        """The <g> SVG element is a container used to group other SVG elements.

        `SVG Doc <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/g>`_

        :param fill: String. Optional. The color for the component background.
        :param stroke: String. Optional. The color for the border.
        :param stroke_width: Float. Optional. The width of the component's border.
        """
        self.html_objs.append(G(self.page, fill, stroke, stroke_width))
        self.html_objs[-1].options.managed = False
        return self.html_objs[-1]

    def path(self, x=0, y=0, fill='none', from_origin=False, bespoke_path=None, stroke=None) -> 'Path':
        """The <path> element is used to define a path.

        `SVG Doc <https://www.w3.org/TR/SVG/paths.html>`_
        `SVG Path Doc <https://www.w3.org/TR/svg-paths/>`_

        :param x: Number.
        :param y: Number.
        :param fill: String. Optional.
        :param from_origin:
        :param bespoke_path:
        :param stroke:
        """
        if from_origin:
            x += self.origine[0]
            y += self.origine[1]
        path = Path(self.page, x, y, fill, self.origine, bespoke_path, stroke=stroke)
        path.options.managed = False
        self.html_objs.append(path)
        return self.html_objs[-1]

    def foreignObject(self, x, y, width, height) -> 'ForeignObject':
        """The <foreignObject> SVG element includes elements from a different XML namespace. In the context of a
        browser, it is most likely (X)HTML.

        `SVG Doc <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/foreignObject>`_

        :param x: Float. The x coordinate of the foreignObject.
        :param y: Float. The y coordinate of the foreignObject.
        :param width: Float or Percentage. The width of the foreignObject.
        :param height: Float or Percentage. The height of the foreignObject.
        """
        self.html_objs.append(ForeignObject(self.page, x, y, width, height))
        self.html_objs[-1].options.managed = False
        return self.html_objs[-1]

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_c, self.tag)


class LinearGradient(Html.Html):
    def __init__(self, page, html_code, x1, y1, x2, y2, gradient_transform):
        super(LinearGradient, self).__init__(page, "", html_code=html_code)
        self.set_attrs({'gradientTransform': gradient_transform, "x1": x1, "y1": y1, "x2": x2, "y2": y2})
        self.items = []

    @property
    def url(self):
        return "url(#%s)" % self.htmlCode

    def stop(self, offset, styles):
        """

        :param offset:
        :param styles:
        """
        self.items.append('<stop offset="%s" style="%s" />' % (
            offset, ";".join(["%s:%s" % (k, v) for k, v in styles.items()])))
        return self

    def __str__(self):
        return "<linearGradient %s>%s</linearGradient>" % (
            self.get_attrs(css_class_names=self.style.get_classes()), "".join(self.items))


class RadialGradient(Html.Html):
    name = "SVG RadialGradient"

    def __init__(self, page, html_code):
        super(RadialGradient, self).__init__(page, "", html_code=html_code)
        self.items = []

    @property
    def url(self) -> str:
        return "url(#%s)" % self.htmlCode

    def stop(self, offset, styles):
        """

        :param offset:
        :param styles:
        """
        self.items.append('<stop offset="%s" style="%s" />' % (
            offset, ";".join(["%s:%s" % (k, v) for k, v in styles.items()])))
        return self

    def __str__(self):
        return "<radialGradient %s>%s</radialGradient>" % (
            self.get_attrs(css_class_names=self.style.get_classes()), "".join(self.items))


class Marker(SVG):
    tag = "marker"

    def __init__(self, page, html_code, viewBox, refX, refY):
        super(Marker, self).__init__(page, None, None, html_code=html_code)
        self.set_attrs({'id': html_code, "viewBox": viewBox, "refX": refX, "refY": refY})
        self.html_objs = []

    @property
    def url(self):
        """

        `SVG Doc <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/marker>`_
        """
        return "url(#%s)" % self.htmlCode

    def orient(self, orientation):
        """

        :param orientation:
        """
        self.set_attrs(name="orient", value=orientation)
        return self

    def markerWidth(self, value):
        """

        :param value:
        """
        self.set_attrs(name="markerWidth", value=value)
        return self

    def markerHeight(self, value):
        """

        :param value:
        """
        self.set_attrs(name="markerHeight", value=value)
        return self

    def arrow(self, size=None):
        """

        `SVG Doc <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/marker>`_

        :param size:
        """
        self.html_objs.append("<path d='M 0 0 L 10 5 L 0 10 z' />")
        if size is not None:
            self.markerWidth(size).markerHeight(size)
        return self

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_c, self.tag)


class Defs(Html.Html):
    name = 'SVG Defs'
    tag = 'defs'

    def __init__(self, page):
        super(Defs, self).__init__(page, "")
        self.html_objs = []

    def linearGradient(
            self, html_code, x1="0%", y1="0%", x2="100%", y2="0%", gradient_transform=None) -> 'LinearGradient':
        """The <linearGradient> element lets authors define linear gradients that can be applied to fill or stroke of
        graphical elements.

        `SVG Doc <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/linearGradient>`_

        :param html_code: String. The HTML id of the component
        :param x1: Float.
        :param y1: Float.
        :param x2: Float.
        :param y2: Float.
        :param gradient_transform:
        """
        self.html_objs.append(LinearGradient(self.page, html_code, x1, y1, x2, y2, gradient_transform))
        return self.html_objs[-1]

    def radialGradient(self, html_code: str) -> 'radialGradient':
        """The <radialGradient> element lets authors define radial gradients that can be applied to fill or stroke of
        graphical elements.

        `SVG Doc <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/radialGradient>`_

        :param html_code: The HTML id of the component.
        """
        self.html_objs.append(RadialGradient(self.page, html_code))
        return self.html_objs[-1]

    def marker(self, html_code, viewBox, refX, refY) -> 'Marker':
        """The <marker> element defines the graphic that is to be used for drawing arrowheads or polymarkers on a given
        <path>, <line>, <polyline> or <polygon> element.

        `SVG Doc <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/marker>`_

        :param html_code:
        :param viewBox:
        :param refX:
        :param refY:
        """
        self.html_objs.append(Marker(self.page, html_code, viewBox, refX, refY))
        return self.html_objs[-1]

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_c, self.tag)


class ForeignObject(SVG):
    tag = "foreignObject"

    def __init__(self, page, x, y, width, height):
        super(ForeignObject, self).__init__(page, None, None)
        self.set_attrs({"x": x, "y": y, "width": width, "height": height})
        self.html_objs = []

    def add(self, components):
        """

        :param components:
        """
        if not isinstance(components, list):
            components = [components]
        for h in components:
            h.options.managed = False
            self.html_objs.append(h)

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_c, self.tag)


class G(SVG):
    tag = 'g'

    def __init__(self, page, fill, stroke, stroke_width):
        super(G, self).__init__(page, None, None)
        self.set_attrs({"fill": fill, "stroke": stroke, "stroke-width": stroke_width})
        self.html_objs = []

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_c, self.tag)


class SVGItem(Html.Html):
    name = 'SVG Item'

    def fill(self, color):
        """

        :param color:
        """
        self.set_attrs(name="fill", value=color)
        return self

    def transform(self, attribute_name, type, from_pos, to_pos, duration=4, repeat_count="indefinite"):
        """

        :param attribute_name:
        :param type:
        :param from_pos:
        :param to_pos:
        :param duration:
        :param repeat_count:
        """
        self.html_objs.append(AnimateTransform(
            self.page, attribute_name, type, from_pos, to_pos, duration, repeat_count))
        return self


class Polygone(SVGItem):
    name = 'SVG Polygone'
    tag = "polygon"

    def __init__(self, page, points, fill):
        super(Polygone, self).__init__(page, points)
        self.set_attrs(({"points": " ".join(["%s,%s" % (x, y) for x, y in self.val]), "fill": fill}))
        self.css({'stroke': page.theme.greys[-1], 'stroke-width': 1})
        self.html_objs = []

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_c, self.tag)


class Ellipse(SVGItem):
    name = 'SVG Epplipse'
    tag = "ellipse"

    def __init__(self, page, cx, cy, rx, ry):
        super(Ellipse, self).__init__(page, "")
        self.set_attrs({"cx": cx, "cy": cy, "rx": rx, "ry": ry})
        self.css({'stroke': page.theme.success[1], 'stroke-width': 1, 'fill': 'none'})
        self.html_objs = []

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_c, self.tag)


class Line(SVGItem):
    name = 'SVG Line'
    tag = "line"

    def __init__(self, page, x1, y1, x2, y2):
        super(Line, self).__init__(page, "")
        self.set_attrs({"x1": x1, "y1": y1, "x2": x2, "y2": y2})
        self.css({"stroke": page.theme.greys[-1], "stroke-width": 1})
        self.html_objs = []

    def markers(self, marker_code):
        """

        :param marker_code:
        """
        self.set_attrs(name="marker-start", value=marker_code)
        self.set_attrs(name="marker-mid", value=marker_code)
        self.set_attrs(name="marker-end", value=marker_code)
        return self

    def marker_start(self, marker_code):
        """

        :param marker_code:
        """
        self.set_attrs(name="marker-start", value=marker_code)

    def marker_mid(self, marker_code):
        """

        :param marker_code:
        """
        self.set_attrs(name="marker-mid", value=marker_code)

    def marker_end(self, marker_code):
        """

        :param marker_code:
        """
        self.set_attrs(name="marker-end", value=marker_code)

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_c, self.tag)


class Polyline(SVGItem):
    name = 'SVG Polyline'
    tag = "polyline"

    def __init__(self, page, points, height, width, fill, options):
        super(Polyline, self).__init__(page, points, css_attrs={"width": width, "height": height})
        self.set_attrs({"fill": fill, "points": " ".join(["%s,%s" % (x, y) for x, y in self.val])})
        self.html_objs = []
        if options is not None:
            self._jsStyles.update(options)
        self.css({"display": 'inline-block', "fill": options.get('fill', ''),
                  'stroke': options.get('stroke', page.theme.success[1]),
                  'stroke-width': options.get('stroke-width', 1)})

    def markers(self, marker_code):
        """

        :param marker_code:
        """
        self.set_attrs(name="marker-start", value=marker_code)
        self.set_attrs(name="marker-mid", value=marker_code)
        self.set_attrs(name="marker-end", value=marker_code)
        return self

    def marker_start(self, marker_code):
        """

        :param marker_code:
        """
        self.set_attrs(name="marker-start", value=marker_code)

    def marker_mid(self, marker_code):
        """

        :param marker_code:
        """
        self.set_attrs(name="marker-mid", value=marker_code)

    def marker_end(self, marker_code):
        """

        :param marker_code:
        """
        self.set_attrs(name="marker-end", value=marker_code)

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_c, self.tag)


class Rectangle(SVGItem):
    name = 'SVG Rectangle'
    tag = "rect"

    def __init__(self, page, x, y, width, height, fill, rx, ry):
        super(Rectangle, self).__init__(page, "", css_attrs={"width": width, "height": height})
        self.set_attrs({"x": x, "y": y, "fill": fill, "rx": rx, "ry": ry})
        self.css({"display": 'inline-block'})
        self.html_objs = []

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_c, self.tag)


class Circle(SVGItem):
    name = 'SVG Circle'
    tag = "circle"

    def __init__(self, report, x, y, r, fill):
        super(Circle, self).__init__(report, "")
        self.set_attrs({"cx": x, "cy": y, "r": r, "fill": fill})
        self.html_objs = []

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_c, self.tag)


class Text(SVGItem):
    name = 'SVG Text'
    tag = "text"

    def __init__(self, page, text, x, y, fill):
        super(Text, self).__init__(page, text)
        self.set_attrs({"x": x, "y": y, 'fill': fill})
        self.html_objs = []

    def line(self, text: str, x: float, y: float) -> 'TSpan':
        """The SVG <tspan> element defines a subtext within a <text> element or another <tspan> element.
        It allows for adjustment of the style and/or position of that subtext as needed.

        `SVG Doc <https://developer.mozilla.org/en-US/docs/Web/SVG/Element/tspan>`_

        :param text: The text to be added to the container
        :param x: The x coordinate of the starting point of the text baseline.
        :param y: The y coordinate of the starting point of the text baseline.
        """
        self.html_objs.append(TSpan(self.page, text, x, y))
        return self.html_objs[-1]

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s%s</%s>" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.val, str_c, self.tag)


class TSpan(SVGItem):
    name = 'SVG TSpan'
    tag = "tspan"

    def __init__(self, page, text, x, y):
        super(TSpan, self).__init__(page, text)
        self.set_attrs({"x": x, "y": y, 'fill': 'black'})
        self.html_objs = []

    def __str__(self):
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s%s</%s>" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.val, str_c, self.tag)


class Path(SVGItem):
    name = 'SVG Path'
    tag = "path"

    def __init__(self, page, x, y, fill, origin, bespoke_path, stroke=None, options=None, profile=None):
        super(Path, self).__init__(page, "", options=options, profile=profile)
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

        :param marker_code:
        """
        self.set_attrs(name="marker-start", value=marker_code)
        self.set_attrs(name="marker-mid", value=marker_code)
        self.set_attrs(name="marker-end", value=marker_code)
        return self

    def line_to(self, x, y):
        """

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

        :param x: Number.
        """
        if self.origin is not None:
            x = self.origin[0] + x
        self.__path.append("H%s" % x)
        return self

    def vertical_line_to(self, y):
        """

        :param y: Number.
        """
        if self.origin is not None:
            y = self.origin[1] - y
        self.__path.append("V%s" % y)
        return self

    def move_to(self, x, y):
        """

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

        `SVG Doc <https://www.w3.org/TR/svg-paths/>`_

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

        `SVG Doc <https://www.w3.org/TR/svg-paths/>`_

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

        `SVG Doc <https://www.w3.org/TR/svg-paths/>`_

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

        `SVG Doc <https://www.w3.org/TR/svg-paths/>`_

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
        self.__path.append("Z")
        return self

    def __str__(self):
        self.set_attrs(name="d", value="".join(self.__path))
        str_c = "".join([h.html() if hasattr(h, 'html') else str(h) for h in self.html_objs])
        return "<%s %s>%s%s</%s>" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.val, str_c, self.tag)


class AnimateTransform(Html.Html):
    name = "SVG AnimateTransform"

    def __init__(self, page, attribute_name, type, from_pos, to_pos, duration, repeat_count):
        super(AnimateTransform, self).__init__(page, "")
        self.set_attrs({"attributeName": attribute_name, "type": type, "from": from_pos, "to": to_pos,
                        "dur": "%ss" % duration, "repeatCount": repeat_count})

    def __str__(self):
        return "<animateTransform %s />" % self.get_attrs(css_class_names=self.style.get_classes())


# https://stackoverflow.com/questions/6725288/svg-text-inside-rect


class Animate(Html.Html):
    name = "SVG Animate"

    # https://css-tricks.com/guide-svg-animations-smil/

    def __init__(self, page, attribute_name, type, from_pos, to_pos, duration, repeat_count):
        super(Animate, self).__init__(page, "")
        self.set_attrs({"attributeName": attribute_name, "type": type, "from": from_pos, "to": to_pos,
                        "dur": "%ss" % duration, "repeatCount": repeat_count})

    def __str__(self):
        return "<animateTransform %s />" % self.get_attrs(css_class_names=self.style.get_classes())
