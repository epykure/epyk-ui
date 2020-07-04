#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsGoogleAPI

from epyk.core.html.options import OptGoogle


class ChartGeoGoogle(Html.Html):
  name = 'Google Chart'
  requirements = ('google-maps', )

  def __init__(self,  report, width, height, options, htmlCode, profile):
    super(ChartGeoGoogle, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.style.css.margin = "10px 0"
    self.__options = OptGoogle.OptionMaps(self, options)

  @property
  def chartId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlCode

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript base function

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    :return: A Javascript object

    :rtype: JsGoogleAPI.GoogleMapsAPI
    """
    if self._js is None:
      self._js = JsGoogleAPI.GoogleMapsAPI(selector="window['%s']" % self.chartId, src=self)
    return self._js

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptGoogle.OptionMaps
    """
    return self.__options

  def build(self, data=None, options=None, profile=False):
    js_options = []
    for k, v in self._jsStyles.items():
      if self.options.isJsContent(k) or str(v).strip().startswith("function"):
        js_options.append("%s: %s" % (k, v))
      else:
        js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
    return '%s = new google.maps.Map(%s, {%s})' % (self.chartId, self.dom.varId, ",".join(js_options))

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())
