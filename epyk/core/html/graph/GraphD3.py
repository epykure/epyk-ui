#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://bl.ocks.org/ctufts/f38ef0187f98c537d791d24fda4a6ef9
from epyk.core.py import types as etypes
from typing import List, Union
from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.css import Colors
from epyk.core.js.packages import JsD3
from epyk.core.html.options import OptChart


class Script(Html.Html):
    name = 'D3 Script'
    tag = "div"
    _option_cls = OptChart.OptionsChart
    requirements = ('d3',)

    def __init__(self, page: primitives.PageModel, data, width, height, html_code, options, profile):
        super(Script, self).__init__(page, data, html_code=html_code, profile=profile, options=options,
                                     css_attrs={"width": width, "height": height})
        self._js__builder__ = ""
        self.style.css.padding = 5
        self.options.height = height[0]

    @property
    def options(self) -> OptChart.OptionsChart:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def colors(self, hex_values: List[str]):
        """Set specific chart color codes.

        :param hex_values: Color codes.
        """
        line_colors, bg_colors = [], []
        for h in hex_values:
            if h.upper() in Colors.defined:
                h = Colors.defined[h.upper()]['hex']
            if not isinstance(h, tuple):
                line_colors.append(h)
                bg_colors.append("rgba(%s, %s, %s, %s" % (
                    Colors.getHexToRgb(h)[0], Colors.getHexToRgb(h)[1],
                    Colors.getHexToRgb(h)[2], self.options.opacity))
            else:
                line_colors.append(h[0])
                bg_colors.append(h[0])
        self.options.colors = line_colors
        self.options.background_colors = bg_colors
        return self

    def data(self, data: Union[list, dict, str]):
        """

        :param data:
        """
        if not isinstance(data, (list, dict)):
            data = data.split(" ")
        self._vals = data

    def loader(self, str_frg: str):
        """Loader for the script.

        :param str_frg: The javascript fragments.
        """
        self.builder_name = "D3Builder%s" % self.page.py.hash(str_frg)
        self._js__builder__ = 'if (!htmlObj.select("svg").empty()){htmlObj.select("svg").remove()}; %s' % str_frg

    def build(self, data: etypes.JS_DATA_TYPES = None, options: etypes.OPTION_TYPE = None,
              profile: etypes.PROFILE_TYPE = False, component_id: str = None, dataflows: List[dict] = None) -> str:
        return super().build(data, options, profile, component_id=self.dom.d3.varId, dataflows=dataflows)

    def define(self, options: etypes.JS_DATA_TYPES = None, dataflows: List[dict] = None) -> str:
        """Not yet defined for this chart """
        return ""

    def responsive(self):
        """Make the SVG chart responsive when the window change size.
        TODO: Find a way to get the update SVG data.
        """
        return self.onReady("d3.select(window).on('resize.updatesvg', function(){%s(%s, %s, %s)})" % (
            self.builder_name, self.dom.d3.varId, self._vals, self.options.config_js()))

    @property
    def svg(self):
        return JsD3.D3Svg(self.page, "%s.select('svg')" % self.dom.d3.varId, set_var=False)

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)
