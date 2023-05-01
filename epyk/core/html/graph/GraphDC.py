#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives, types as etypes
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.html.options import OptionsWithTemplates

from epyk.core.js.packages import JsDc


class Chart(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'DC Chart'
    requirements = ('dc', 'crossfilter')
    _option_cls = OptionsWithTemplates

    def __init__(self, page: primitives.PageModel, width, height, title, options, html_code, profile):
        super(Chart, self).__init__(page, [], html_code=html_code, profile=profile,
                                    css_attrs={"width": width, "height": height})
        self.style.css.margin = "10px 0"

    @property
    def options(self) -> OptionsWithTemplates:
        """
        Property to set all the possible object for a button.

        Usage::

          div = page.ui.div(htmlCode="testDiv")
          div.options.inline = True
        """
        return super().options

    @property
    def chartId(self) -> str:
        """ Return the Javascript variable of the chart. """
        return "chart_%s" % self.htmlCode

    def crossFilter(self, dimension, group):
        """

        :param dimension:
        :param group:
        """
        self.dom.dimension(dimension.varId).group(group.varId)
        return self

    def build(self, data=None, options=None, profile=False, component_id=None):
        """

        :param data:
        :param options:
        :param profile:
        :param component_id:
        """
        return self.dom.render().toStr()

    def define(self, options: etypes.JS_DATA_TYPES = None) -> str:
        """ Not yet defined for this chart """
        return ""

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())


class ChartLine(Chart):

    @property
    def dom(self) -> JsDc.Line:
        """
        A line chart is used to display information as a series of data points connected by straight lines.

        A data point represents two values, one plotted along the horizontal axis and another along the vertical axis.
        For example, the popularity of food items can be drawn as a line chart in such a way that the food item is
        represented along the x-axis and its popularity is represented along the y-axis.

        Related Pages:

          https://www.tutorialspoint.com/dcjs/dcjs_line_chart.htm
        """
        if self._dom is None:
            self._dom = JsDc.Line(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartBar(Chart):

    @property
    def dom(self) -> JsDc.Bar:
        """
        Bar chart is one of the most commonly used types of graph and are used to display and compare the number,
        frequency or other measure (e.g. mean) for different discrete categories or groups.
        The graph is constructed such that the heights or lengths of the different bars are proportional to the size of
        the category they represent.

        Related Pages:

          https://www.tutorialspoint.com/dcjs/dcjs_bar_chart.htm
        """
        if self._dom is None:
            self._dom = JsDc.Bar(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartRow(Chart):

    @property
    def dom(self) -> JsDc.Row:
        """ Interface for the Row Chart component. """
        if self._dom is None:
            self._dom = JsDc.Row(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartScatter(Chart):

    @property
    def dom(self) -> JsDc.Scatter:
        """
        A scatter plot is a type of mathematical diagram.

        It is represented using the Cartesian coordinates to display values for typically two variables for a set of data.
        The data is displayed as a collection of points and the points maybe colored.

        Related Pages:

          https://www.tutorialspoint.com/dcjs/dcjs_scatter_plot.htm
        """
        if self._dom is None:
            self._dom = JsDc.Scatter(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartBubble(Chart):

    @property
    def dom(self) -> JsDc.Bubble:
        """
        A bubble chart is used to display three dimensions of the data.

        It is a variation of scatter chart, in which the data points are replaced with bubbles. The bubble sizes are
        represented with respect to the data dimension.
        It uses horizontal and vertical axes as value axes.

        Related Pages:

          https://www.tutorialspoint.com/dcjs/dcjs_bubble_chart.htm
        """
        if self._dom is None:
            self._dom = JsDc.Bubble(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartPie(Chart):

    @property
    def dom(self) -> JsDc.Pie:
        """
        A pie chart is a circular statistical graph. It is divided into slices to show a numerical proportion.

        Related Pages:

          https://www.tutorialspoint.com/dcjs/dcjs_pie_chart.htm
        """
        if self._dom is None:
            self._dom = JsDc.Pie(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartSunburst(Chart):

    @property
    def dom(self) -> JsDc.Sunburst:
        """ Get the interface for the Sunburst Dom element. """
        if self._dom is None:
            self._dom = JsDc.Sunburst(page=self.page, js_code=self.chartId, component=self)
        return self._dom


class ChartSeries(Chart):

    @property
    def dom(self) -> JsDc.Series:
        """
        A series is a set of data. You can plot a chart based on the data.

        Related Pages:

          https://www.tutorialspoint.com/dcjs/dcjs_series_chart.htm
        """
        if self._dom is None:
            self._dom = JsDc.Series(page=self.page, js_code=self.chartId, component=self)
        return self._dom
