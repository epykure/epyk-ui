
from epyk.core.html import Html
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsQuery
from epyk.core.js.html import JsHtmlJqueryUI

# The list of CSS classes
from epyk.core.css.styles import GrpChart


class Sparklines(Html.Html):
  __reqJs = ['jquery-sparklines']
  name, category, callFnc = 'sparkline', 'Charts', 'sparkline'

  def __init__(self, report, data, chart_type, title, options):
    super(Sparklines, self).__init__(report, data)
    self._jsStyles, self.title = {"type": chart_type}, None
    if title is not None:
      self.title = self._report.ui.title(title, level=4)
      self.title.inReport = False
    if options is not None:
      self._jsStyles.update(options)

  @property
  def style(self):
    """
    Description:
    ------------

    :rtype: GrpChart.ClassBSpartlines
    """
    if self._styleObj is None:
      self._styleObj = GrpChart.ClassBSpartlines(self)
    return self._styleObj

  def options(self, attrs):
    """
    Description:
    ------------
    Add any option to the sparkline object

    Example
    chartObj.options({"lineColor": 'yellow'})

    Related Pages:

			https://omnipotent.net/jquery.sparkline/#s-docs

    Attributes:
    ----------
    :param attrs: A python dictionary

    :return: The sparkline object
    """
    self._jsStyles.update(attrs)
    return self

  @property
  def dom(self):
    """
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlSparkline
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSparkline(self, report=self._report)
    return self._dom

  def click(self, jsFnc, profile=False):
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
    :param jsFnc:
    :param profile:
    """
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(
      "%s.bind('sparklineClick', function(event) { %s })" % (self.dom.jquery.varId, JsUtils.jsConvertFncs(jsFnc, toStr=True)))
    return self

  def hover(self, jsFnc, profile=False):
    """
    Description:
    ------------
    When the mouse moves over a different value in a sparkline a sparklineRegionChange event is generated.
    This can be useful to hook in an alternate tooltip library.

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#interactive

    Attributes:
    ----------
    :param jsFnc:
    :param profile:
    """
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(
      "%s.bind('sparklineRegionChange', function(event) { %s })" % (
      self.dom.jquery.varId, JsUtils.jsConvertFncs(jsFnc, toStr=True)))
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
