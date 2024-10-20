#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.css import Colors
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsQuery
from epyk.core.js.html import JsHtmlJqueryUI

# The list of CSS classes
from epyk.core.css.styles import GrpClsChart
from epyk.core.html.options import OptSparkline


# TODO add event and tooltip style
# TODO Fix display tooltips in Jupyter


class Sparklines(MixHtmlState.HtmlOverlayStates, Html.Html):
    requirements = ('jquery-sparkline',)
    tag = "span"
    name = 'Sparkline'
    _option_cls = OptSparkline.OptionsSparkLine

    def __init__(self, page, data, title, width, height, options, profile):
        super(Sparklines, self).__init__(page, data, css_attrs={'width': width, 'height': height},
                                         options=options, profile=profile)
        self.title = None
        if title is not None:
            self.title = self.page.ui.title(title, level=4)
            self.title.options.managed = False

    @property
    def style(self) -> GrpClsChart.ClassBSpartlines:
        """Property to the sparkline style properties.
        This will group all the default CSS classes which are defined by default to a sparkline component.
        """
        if self._styleObj is None:
            self._styleObj = GrpClsChart.ClassBSpartlines(self)
        return self._styleObj

    @property
    def options(self) -> OptSparkline.OptionsSparkLine:
        """Property to set all the possible object for a button"""
        return super().options

    @property
    def dom(self) -> JsHtmlJqueryUI.JsHtmlSparkline:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlJqueryUI.JsHtmlSparkline(component=self, page=self.page)
        return self._dom

    def click(self, js_funcs, profile: bool = False, source_event=None, on_ready=False):
        """When a user clicks on a sparkline, a sparklineClick event is generated.

        The event object contains a property called "sparklines" that holds an array of the sparkline objects under
        the mouse at the time of the click.
        For non-composite sparklines, this array will have just one entry.

        `Jquery Sparkline <https://omnipotent.net/jquery.sparkline/#interactive>`_

        :param js_funcs: List | String. Required. Javascript functions.
        :param profile: Boolean | Dictionary. Required. A flag to set the component performance storage.
        :param source_event: String. Required. The source target for the event.
        :param on_ready: Boolean. Required. Specify if the event needs to be trigger when the page is loaded.
        """
        self.onReady("%s.bind('sparklineClick', function(event) {%s})" % (
            self.dom.jquery.varId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
        return self

    def hover(self, js_funcs, profile: bool = False, source_event: str = None):
        """When the mouse moves over a different value in a sparkline a sparklineRegionChange event is generated.
        This can be useful to hook in an alternate tooltip library.

        Jquery Sparkline <https://omnipotent.net/jquery.sparkline/#interactive>`_

        :param js_funcs: List | String. Required. Javascript functions.
        :param profile: Boolean | Dictionary. Required. A flag to set the component performance storage.
        :param source_event: String. Required. The source target for the event.
        """
        self.onReady("%s.bind('sparklineRegionChange', function(event) {%s})" % (
            self.dom.jquery.varId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
        return self

    def color(self, hex_value: str, background: str = None):
        """Set the colors of the chart.
        hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
        If the background colors are not specified they will be deduced from the colors list changing the opacity.

        Usage::

            chart = page.ui.charts.sparkline("line", [1, 2, 3, 4, 5, 4, 3, 2, 1])
            chart.color("#FFFF00")

        :param hex_value: hexadecimal color code
        :param background:
        """
        if background is None:
            self.options.fillColor = "rgba(%s, %s, %s, %s" % (
                Colors.getHexToRgb(hex_value)[0], Colors.getHexToRgb(hex_value)[1],
                Colors.getHexToRgb(hex_value)[2], self.options.opacity)
        else:
            self.options.fillColor = background
        self.options.lineColor = hex_value
        self.options.spotColor = hex_value

    _js__builder__ = '%(htmlObj)s.sparkline(data, options)' % {
        "htmlObj": JsQuery.decorate_var("htmlObj", convert_var=False)}

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        if self.title is not None:
            return "<div style='display:inline-block;text-align:center'>%s<%s %s></%s></div>" % (
                self.title, self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)

        return "<%s %s>Loading..</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


class SparklinesBar(Sparklines):
    requirements = ('jquery-sparkline',)
    name = 'Sparkline Bar'
    _option_cls = OptSparkline.OptionsSparkLineBar


class SparklinesTristate(Sparklines):
    requirements = ('jquery-sparkline',)
    name = 'Sparkline Tristate'
    _option_cls = OptSparkline.OptionsSparkLineTristate


class SparklinesDiscrete(Sparklines):
    requirements = ('jquery-sparkline',)
    name = 'Sparkline Discrete'
    _option_cls = OptSparkline.OptionsSparkLineDiscrete


class SparklinesBullet(Sparklines):
    requirements = ('jquery-sparkline',)
    name = 'Sparkline Bullet'
    _option_cls = OptSparkline.OptionsSparkLineBullet


class SparklinesPie(Sparklines):
    requirements = ('jquery-sparkline',)
    name = 'Sparkline Pie'
    _option_cls = OptSparkline.OptionsSparkLinePie


class SparklinesBoxPlot(Sparklines):
    requirements = ('jquery-sparkline',)
    name = 'Sparkline BoxPlot'
    _option_cls = OptSparkline.OptionsSparkLineBoxPlot
