#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.js.packages import JsQuery
from epyk.core.html.options import OptJqvM


class JqueryVectorMap(Html.Html):
  name = 'Jquery Vector Map'
  requirements = ('jqvmap', )
  _option_cls = OptJqvM.OptionsJqVM

  def __init__(self,  report, width, height, html_code, options, profile):
    self.height = height[0]
    super(JqueryVectorMap, self).__init__(report, [], html_code=html_code, profile=profile, options=options,
                                          css_attrs={"width": width, "height": height})
    self.chartId = "%s_obj" % self.htmlCode
    self.style.css.display = "inline-block"

  def click(self,  js_funcs, profile=None, source_event=None, on_ready=False):
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
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
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
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptJqvM.OptionsJqVM
    """
    return super().options

  _js__builder__ = '''%s.vectorMap(options)''' % JsQuery.decorate_var("htmlObj", convert_var=False)

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())
