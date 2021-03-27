#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.css import Colors
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsQuery
from epyk.core.js.html import JsHtmlJqueryUI

# The list of CSS classes
from epyk.core.css.styles import GrpClsChart
from epyk.core.html.options import OptSparkline

# TODO add event and tooltip style


class Sparklines(Html.Html):
  requirements = ('jquery-sparkline', )
  name = 'Sparkline'
  _option_cls = OptSparkline.OptionsSparkLine

  def __init__(self, report, data, title, width, height, options, profile):
    super(Sparklines, self).__init__(report, data, css_attrs={'width': width, 'height': height},
                                     options=options, profile=profile)
    self.title = None
    if title is not None:
      self.title = self._report.ui.title(title, level=4)
      self.title.options.managed = False

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the sparkline style properties.
    This will group all the default CSS classes which are defined by default to a sparkline component.

    Usage:
    -----

    :rtype: GrpClsChart.ClassBSpartlines
    """
    if self._styleObj is None:
      self._styleObj = GrpClsChart.ClassBSpartlines(self)
    return self._styleObj

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the possible object for a button.

    Usage:
    -----

    :rtype: OptSparkline.OptionsSparkLine
    """
    return super().options

  @property
  def dom(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlSparkline
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSparkline(self, report=self._report)
    return self._dom

  def click(self, js_funcs, profile=False, source_event=None, on_ready=False):
    """
    Description:
    ------------
    When a user clicks on a sparkline, a sparklineClick event is generated.
    The event object contains a property called "sparklines" that holds an array of the sparkline objects under
    the mouse at the time of the click.
    For non-composite sparklines, this array will have just one entry.

    Usage:
    -----

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#interactive

    Attributes:
    ----------
    :param js_funcs: List | String. Required. Javascript functions.
    :param profile: Boolean | Dictionary. Required. A flag to set the component performance storage.
    :param source_event: String. Required. The source target for the event.
    :param on_ready: Boolean. Required. Specify if the event needs to be trigger when the page is loaded.
    """
    self.onReady("%s.bind('sparklineClick', function(event) {%s})" % (
      self.dom.jquery.varId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def hover(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    ------------
    When the mouse moves over a different value in a sparkline a sparklineRegionChange event is generated.
    This can be useful to hook in an alternate tooltip library.

    Usage:
    -----

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#interactive

    Attributes:
    ----------
    :param js_funcs: List | String. Required. Javascript functions.
    :param profile: Boolean | Dictionary. Required. A flag to set the component performance storage.
    :param source_event: String. Required. The source target for the event.
    """
    self.onReady("%s.bind('sparklineRegionChange', function(event) {%s})" % (
      self.dom.jquery.varId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def color(self, hex_value, background=None):
    """
    Description:
    -----------
    Set the colors of the chart.

    hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
    If the background colors are not specified they will be deduced from the colors list changing the opacity.

    Usage:
    -----

    Attributes:
    ----------
    :param hex_values: List. An array of hexadecimal color codes.
    """
    if background is None:
      self.options.fillColor = "rgba(%s, %s, %s, %s" % (
        Colors.getHexToRgb(hex_value)[0], Colors.getHexToRgb(hex_value)[1],
        Colors.getHexToRgb(hex_value)[2], self.options.opacity)
    else:
      self.options.fillColor = background
    self.options.lineColor = hex_value
    self.options.spotColor = hex_value

  _js__builder__ = '%s.sparkline(data, options)' % JsQuery.decorate_var("htmlObj", convert_var=False)

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    if self.title is not None:
      return "<div style='display:inline-block;text-align:center'>%s<span %s></span></div>" % (
        self.title, self.get_attrs(pyClassNames=self.style.get_classes()))

    return "<span %s>Loading..</span>" % self.get_attrs(pyClassNames=self.style.get_classes())


class SparklinesBar(Sparklines):
  requirements = ('jquery-sparkline', )
  name = 'Sparkline Bar'
  _option_cls = OptSparkline.OptionsSparkLineBar


class SparklinesTristate(Sparklines):
  requirements = ('jquery-sparkline', )
  name = 'Sparkline Tristate'
  _option_cls = OptSparkline.OptionsSparkLineTristate


class SparklinesDiscrete(Sparklines):
  requirements = ('jquery-sparkline', )
  name = 'Sparkline Discrete'
  _option_cls = OptSparkline.OptionsSparkLineDiscrete


class SparklinesBullet(Sparklines):
  requirements = ('jquery-sparkline', )
  name = 'Sparkline Bullet'
  _option_cls = OptSparkline.OptionsSparkLineBullet


class SparklinesPie(Sparklines):
  requirements = ('jquery-sparkline', )
  name = 'Sparkline Pie'
  _option_cls = OptSparkline.OptionsSparkLinePie


class SparklinesBoxPlot(Sparklines):
  requirements = ('jquery-sparkline',)
  name = 'Sparkline BoxPlot'
  _option_cls = OptSparkline.OptionsSparkLineBoxPlot
