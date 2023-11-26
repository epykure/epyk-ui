import sys

from typing import Union, Any
from epyk.core.py import primitives

from epyk.core.css import Properties
from epyk.core.css.styles.classes.CssStyle import Style

IMPORTANT_EXPR = "{} !IMPORTANT"


class Attrs(Properties.CssMixin):

    def __init__(self, component: primitives.HtmlModel, page: primitives.PageModel = None):
        self.attrs = {}
        self.component = component
        self.page = page
        if component is not None and page is None:
            self.page = component.page

    def css(self, attrs: Union[dict, str], value: Any = None, important: bool = False):
        """
    Set multiple CSS attributes to the HTML component.

    :param attrs: optional. The attributes to be added
    :param value: Optional. The value for a given item
    :param important: Optional. Flag the attribute to be important
    """
        if not isinstance(attrs, dict):
            if value is None:
                return self.attrs.get(attrs)

            if important:
                value = IMPORTANT_EXPR.format(value)
            self.attrs[attrs] = value

        for k, v in attrs.items():
            if important:
                v = IMPORTANT_EXPR.format(v)
            self.attrs[k] = v
        return self.attrs

    def remove(self, attr: str = None, set_none: bool = False):
        """
    Remove a CSS attribute to the HTML component.

    This function will either remove it if it is part of the existing CSS attribute or set it to auto in case it is
    coming from a CSS class.

    :param str attr: Optional. The attribute to be removed.
    :param bool set_none: Optional. Set the CSS attribute value to None on the CSS.
    """
        key = attr or sys._getframe().f_back.f_code.co_name.replace("_", "-")
        if set_none:
            self.attrs[key] = "none"
            self.component.attr['css'][key] = "none"
        else:
            if key in self.attrs:
                del self.attrs[key]
                if key in self.component.attr['css']:
                    del self.component.attr['css'][key]
            else:
                self.attrs[key] = "unset"
                self.component.attr['css'][key] = "auto"

    def __str__(self):
        css_tag = ["%s:%s" % (k, v) for k, v in self.attrs.items()]
        return ";".join(css_tag)


class Commons(Attrs):

    def __init__(self, component: primitives.HtmlModel, page: primitives.PageModel = None):
        super(Commons, self).__init__(component, page=page)
        self.font_size = 'inherit'
        self.font_family = 'inherit'
        self.box_sizing = 'border-box'


class Empty(Attrs):

    def __init__(self, component: primitives.HtmlModel, page: primitives.PageModel = None):
        super(Empty, self).__init__(component, page=page)


class Body(Attrs):

    def __init__(self, component: primitives.HtmlModel, page: primitives.PageModel = None):
        super(Body, self).__init__(component, page=page)
        self.font_size = component.style.globals.font.normal()
        self.font_family = component.style.globals.font.family
        self.margin = 0


class CssInline(Attrs):
    classname: str = None

    def __init__(self, component: primitives.HtmlModel = None, page: primitives.PageModel = None):
        super(CssInline, self).__init__(component, page=page)

    @property
    def stroke_dasharray(self):
        return self.css("stroke-dasharray")

    @stroke_dasharray.setter
    def stroke_dasharray(self, val):
        self.css({"stroke-dasharray": val})

    @property
    def stroke_width(self):
        return self.css("stroke-width")

    @stroke_width.setter
    def stroke_width(self, val):
        self.css({"stroke-width": val})

    @property
    def fill(self):
        return self.css("fill")

    @fill.setter
    def fill(self, val):
        self.css({"fill": val})

    @property
    def fill_opacity(self):
        return self.css("fill-opacity")

    @fill_opacity.setter
    def fill_opacity(self, num):
        self.css({"fill-opacity": num})

    def to_dict(self, copy: bool = False):
        """
      Returns the underlying CSS attributes.
      This is the internal object and not a copy by default.

      :param copy: Optional. Specify if a copy must be returned.
      """
        if copy:
            return dict(self.attrs)

        return self.attrs

    def important(self, attrs: list = None):
        """

        If attrs is not defined all the attributes will be important.

        :param attrs: The Css Python property to be changed.
        """
        if attrs is None:
            for k in self.attrs.items():
                self.attrs[k] = "%s !IMPORTANT" % self.attrs[k]
        else:
            for k in attrs:
                setattr(self, k, "%s !IMPORTANT" % getattr(self, k))

    def to_class(self, class_name: str = None):
        """
        The CSS class object.

        :param class_name: The class name
        """
        class_name = class_name or self.classname
        if class_name is None:
            raise Exception("Class Name must be defined to create virtual class")

        v_cls = type(class_name, (Style,), {"_attrs": self.attrs})
        return v_cls(None)

    def define_class(self, class_name: str, page):
        v_cls = page.body.style.custom_class({"_attrs": self.attrs}, class_name)
        return v_cls

    def toStr(self) -> str:
        """ Change the class definition to a string expression. """
        if self.classname is None:
            raise Exception("Class Name must be defined to create virtual class")

        return "'.%s {%s}'" % (self.classname, str(self))
