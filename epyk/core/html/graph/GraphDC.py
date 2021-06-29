#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html

from epyk.core.js.packages import JsDc


class Chart(Html.Html):
  name = 'DC Chart'
  requirements = ('dc', 'crossfilter')

  def __init__(self,  report, width, height, title, options, html_code, profile):
    super(Chart, self).__init__(report, [], html_code=html_code, profile=profile,
                                css_attrs={"width": width, "height": height})
    self.style.css.margin = "10px 0"

  @property
  def chartId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart.

    Usage::
    """
    return "chart_%s" % self.htmlCode

  def crossFilter(self, dimension, group):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param dimension:
    :param group:
    """
    self.dom.dimension(dimension.varId).group(group.varId)
    return self

  def build(self, data=None, options=None, profile=False, component_id=None):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param data:
    :param options:
    :param profile:
    :param component_id:
    """
    return self.dom.render().toStr()

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class ChartLine(Chart):

  @property
  def dom(self):
    """
    Description:
    -----------
    A line chart is used to display information as a series of data points connected by straight lines.
    A data point represents two values, one plotted along the horizontal axis and another along the vertical axis.
    For example, the popularity of food items can be drawn as a line chart in such a way that the food item is
    represented along the x-axis and its popularity is represented along the y-axis.

    Usage::


    Related Pages:

      https://www.tutorialspoint.com/dcjs/dcjs_line_chart.htm

    :rtype: JsDc.JsLine
    """
    if self._dom is None:
      self._dom = JsDc.Line(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartBar(Chart):

  @property
  def dom(self):
    """
    Description:
    -----------
    Bar chart is one of the most commonly used types of graph and are used to display and compare the number,
    frequency or other measure (e.g. mean) for different discrete categories or groups.
    The graph is constructed such that the heights or lengths of the different bars are proportional to the size of
    the category they represent.

    Usage::

    Related Pages:

      https://www.tutorialspoint.com/dcjs/dcjs_bar_chart.htm

    :rtype: JsDc.Bar
    """
    if self._dom is None:
      self._dom = JsDc.Bar(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartRow(Chart):

  @property
  def dom(self):
    """
    Description:
    -----------

    Usage::

    :rtype: JsDc.Row
    """
    if self._dom is None:
      self._dom = JsDc.Row(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartScatter(Chart):

  @property
  def dom(self):
    """
    Description:
    -----------
    A scatter plot is a type of mathematical diagram.
    It is represented using the Cartesian coordinates to display values for typically two variables for a set of data.
    The data is displayed as a collection of points and the points maybe colored.

    Usage::


    Related Pages:

      https://www.tutorialspoint.com/dcjs/dcjs_scatter_plot.htm

    :rtype: JsDc.Scatter
    """
    if self._dom is None:
      self._dom = JsDc.Scatter(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartBubble(Chart):

  @property
  def dom(self):
    """
    Description:
    -----------
    A bubble chart is used to display three dimensions of the data.
    It is a variation of scatter chart, in which the data points are replaced with bubbles. The bubble sizes are
    represented with respect to the data dimension.
    It uses horizontal and vertical axes as value axes.

    Usage::

    Related Pages:

      https://www.tutorialspoint.com/dcjs/dcjs_bubble_chart.htm

    :rtype: JsDc.Bubble
    """
    if self._dom is None:
      self._dom = JsDc.Bubble(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartPie(Chart):

  @property
  def dom(self):
    """
    Description:
    -----------
    A pie chart is a circular statistical graph. It is divided into slices to show a numerical proportion.

    Usage::

    Related Pages:

      https://www.tutorialspoint.com/dcjs/dcjs_pie_chart.htm

    :rtype: JsDc.Pie
    """
    if self._dom is None:
      self._dom = JsDc.Pie(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartSunburst(Chart):

  @property
  def dom(self):
    """
    Description:
    -----------

    Usage::

    :rtype: JsDc.Sunburst
    """
    if self._dom is None:
      self._dom = JsDc.Sunburst(self._report, varName=self.chartId, parent=self)
    return self._dom


class ChartSeries(Chart):

  @property
  def dom(self):
    """
    Description:
    -----------
    A series is a set of data. You can plot a chart based on the data.

    Usage::

    Related Pages:

      https://www.tutorialspoint.com/dcjs/dcjs_series_chart.htm

    :rtype: JsDc.Series
    """
    if self._dom is None:
      self._dom = JsDc.Series(self._report, varName=self.chartId, parent=self)
    return self._dom
