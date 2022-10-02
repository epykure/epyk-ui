#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html


class Sparkline:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Sparkline"

  def bar(self, data=None, title=None, options=None, width=(None, "%"), height=(None, "px"), profile=False):
    """

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about

    :param data: String. Optional. A String corresponding to a JavaScript object.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    data = data or []
    html_chart = html.graph.GraphSparklines.SparklinesBar(
      self.page, data, title, width, height, options or {}, profile)
    html_chart.color(self.page.theme.charts[0])
    html_chart.options.type = "bar"
    return html_chart

  def line(self, data=None, title=None, options=None, width=(None, "%"), height=(None, "px"), profile=False):
    """

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about

    :param data: String. Optional. A String corresponding to a JavaScript object.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    data = data or []
    html_chart = html.graph.GraphSparklines.SparklinesBar(
      self.page, data, title, width, height, options or {}, profile)
    html_chart.color(self.page.theme.charts[0])
    html_chart.options.type = "line"
    return html_chart

  def tristate(self, data=None, title=None, options=None, width=(None, "%"), height=(None, "px"), profile=False):
    """

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about

    :param data: String. Optional. A String corresponding to a JavaScript object.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    data = data or []
    html_chart = html.graph.GraphSparklines.SparklinesTristate(
      self.page, data, title, width, height, options or {}, profile)
    html_chart.color(self.page.theme.charts[0])
    html_chart.options.type = "tristate"
    return html_chart

  def discrete(self, data=None, title=None, options=None, width=(None, "%"), height=(None, "px"), profile=False):
    """

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about

    :param data: String. Optional. A String corresponding to a JavaScript object.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    data = data or []
    html_chart = html.graph.GraphSparklines.SparklinesDiscrete(
      self.page, data, title, width, height, options or {}, profile)
    html_chart.color(self.page.theme.charts[0])
    html_chart.options.type = "discrete"
    return html_chart

  def bullet(self, data=None, title=None, options=None, width=(None, "%"), height=(None, "px"), profile=False):
    """

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about

    :param data: String. Optional. A String corresponding to a JavaScript object.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    data = data or []
    html_chart = html.graph.GraphSparklines.SparklinesBullet(
      self.page, data, title, width, height, options or {}, profile)
    html_chart.color(self.page.theme.charts[0])
    html_chart.options.type = "bullet"
    return html_chart

  def pie(self, data=None, title=None, options=None, width=(None, "%"), height=(None, "px"), profile=False):
    """

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about

    :param data: String. Optional. A String corresponding to a JavaScript object.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    data = data or []
    html_chart = html.graph.GraphSparklines.SparklinesPie(
      self.page, data, title, width, height, options or {}, profile)
    html_chart.color(self.page.theme.charts[0])
    html_chart.options.type = "pie"
    return html_chart

  def box_plot(self, data=None, title=None, options=None, width=(None, "%"), height=(None, "px"), profile=False):
    """

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about

    :param data: String. Optional. A String corresponding to a JavaScript object.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    data = data or []
    html_chart = html.graph.GraphSparklines.SparklinesBoxPlot(
      self.page, data, title, width, height, options or {}, profile)
    html_chart.color(self.page.theme.charts[0])
    html_chart.options.type = "box"
    return html_chart
