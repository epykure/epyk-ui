#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsQuery
from epyk.core.js.html import JsHtmlJqueryUI

# The list of CSS classes
from epyk.core.css.styles import GrpChart
from epyk.core.html.options import OptSparkline


class Sparklines(Html.Html):
  requirements = ('jquery-sparkline', )
  name = 'Sparkline'

  def __init__(self, report, data, chart_type, title, width, height, options):
    super(Sparklines, self).__init__(report, data, css_attrs={'width': width, 'height': height})
    self._jsStyles, self.title = {"type": chart_type}, None
    if title is not None:
      self.title = self._report.ui.title(title, level=4)
      self.title.options.managed = False
    self.__options = OptSparkline.OptionsSparkLine(self, options or {})

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the sparkline style properties.
    This will group all the default CSS classes which are defined by default to a sparkline component.

    :rtype: GrpChart.ClassBSpartlines
    """
    if self._styleObj is None:
      self._styleObj = GrpChart.ClassBSpartlines(self)
    return self._styleObj

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the possible object for a button

    :rtype: OptSparkline.OptionsSparkLine
    """
    return self.__options

  @property
  def dom(self):
    """
    Description:
    -----------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlSparkline
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSparkline(self, report=self._report)
    return self._dom

  def click(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------
    When a user clicks on a sparkline, a sparklineClick event is generated.
    The event object contains a property called "sparklines" that holds an array of the sparkline objects under the mouse at the time of the click.
    For non-composite sparklines, this array will have just one entry.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#interactive

    Attributes:
    ----------
    :param jsFncs: List of Js Functions. A Javascript Python function
    :param profile: A Boolean. Set to true to get the profile for the function on the Javascript console.
    :param source_event: A String. Optional. The source target for the event.
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    self.onReady("%s.bind('sparklineClick', function(event) { %s })" % (self.dom.jquery.varId, JsUtils.jsConvertFncs(jsFncs, toStr=True)))
    return self

  def hover(self, jsFncs, profile=False, source_event=None):
    """
    Description:
    ------------
    When the mouse moves over a different value in a sparkline a sparklineRegionChange event is generated.
    This can be useful to hook in an alternate tooltip library.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#interactive

    Attributes:
    ----------
    :param jsFncs: List of Js Functions. A Javascript Python function
    :param profile: A Boolean. Set to true to get the profile for the function on the Javascript console.
    :param source_event: A String. Optional. The source target for the event.
    """
    self.onReady("%s.bind('sparklineRegionChange', function(event) { %s })" % (self.dom.jquery.varId, JsUtils.jsConvertFncs(jsFncs, toStr=True)))
    return self

  @property
  def _js__builder__(self):
    return '%s.sparkline(data, options)' % JsQuery.decorate_var("htmlObj", convert_var=False)

  def __str__(self):
    # Javascript builder is mandatory for this object
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    if self.title is not None:
      return "<div style='display:inline-block;text-align:center'>%s<span %s></span></div>" % (self.title, self.get_attrs(pyClassNames=self.style.get_classes()))

    return "<span %s>Loading..</span>" % self.get_attrs(pyClassNames=self.style.get_classes())
