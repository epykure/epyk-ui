"""
Module in charge of producing Jquery sparklines charts

https://omnipotent.net/jquery.sparkline/#s-docs
"""

from epyk.core.html import Html
from epyk.core.js.packages import JsQuery

# The list of CSS classes
from epyk.core.css.groups import CssGrpClsCharts


class Sparklines(Html.Html):
  __reqJs = ['jquery-sparklines']
  name, category, callFnc = 'sparkline', 'Charts', 'sparkline'
  _grpCls = CssGrpClsCharts.CssClassChartsSparkline

  def __init__(self, report, data, chart_type, title, options):
    super(Sparklines, self).__init__(report, data)
    self._jsStyles = {"type": chart_type}
    if title is not None:
      self.title = self._report.ui.title(title, level=4)
      self.title.inReport = False
    if options is not None:
      self._jsStyles.update(options)
    self.css({"margin-top": '5px', 'display': 'inline-block'})

  def options(self, attrs):
    """
    Add any option to the sparkline object

    Example
    chartObj.options({"lineColor": 'yellow'})

    Documentation
    https://omnipotent.net/jquery.sparkline/#s-docs

    :param attrs: A python dictionary

    :return: The sparkline object
    """
    self._jsStyles.update(attrs)
    return self

  @property
  def _js__builder__(self):
    return '%s.sparkline(data, options)' % JsQuery.decorate_var("htmlObj", convert_var=False)

  def __str__(self):
    # Javascript builder is mandatory for this object
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    if self.title is not None:
      return "<div style='display:inline-block;text-align:center'>%s<span %s></span></div>" % (self.title, self.get_attrs(pyClassNames=self.defined))

    return "<span %s></span>" % self.get_attrs(pyClassNames=self.defined)
