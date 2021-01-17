#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.js.packages import JsQuery
from epyk.core.html.options import OptJqvM


class JqueryVectorMap(Html.Html):
  name = 'Jquery Vector Map'
  requirements = ('jqvmap', )

  def __init__(self,  report, width, height, htmlCode, options, profile):
    self.height = height[0]
    super(JqueryVectorMap, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptJqvM.OptionsJqVM(self, options)
    self.chartId = "%s_obj" % self.htmlCode

  def click(self,  js_funcs, profile=False, source_event=None, onReady=False):
    """
    Description:
    -----------
    The onclick event occurs when the user clicks on an element.
    This function will receive the region, code and element. The common data variable is mapped to the region.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/event_onclick.asp

    Attributes:
    ----------
    :param js_funcs: List | String. A Javascript Python function
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.options.onRegionClick(js_funcs, profile)
    return self

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptJqvM.OptionsJqVM
    """
    return self.__options

  _js__builder__ = '''%s.vectorMap(options)''' % JsQuery.decorate_var("htmlObj", convert_var=False)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())
