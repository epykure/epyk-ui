#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsGoogleAPI

from epyk.core.html.options import OptGoogle


class ChartGeoGoogle(Html.Html):
  name = 'Google Chart'
  requirements = ('google-maps', )
  _option_cls = OptGoogle.OptionMaps

  def __init__(self,  page, width, height, options, html_code, profile):
    super(ChartGeoGoogle, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                         css_attrs={"width": width, "height": height})
    self.style.css.margin = "10px 0"

  @property
  def chartId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart.
    """
    return "%s_obj" % self.htmlCode

  @property
  def js(self) -> JsGoogleAPI.GoogleMapsAPI:
    """
    Description:
    -----------
    Javascript base function.

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    :return: A Javascript object.

    :rtype: JsGoogleAPI.GoogleMapsAPI
    """
    if self._js is None:
      self._js = JsGoogleAPI.GoogleMapsAPI(selector="window['%s']" % self.chartId, src=self)
    return self._js

  @property
  def options(self) -> OptGoogle.OptionMaps:
    """
    Description:
    -----------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptGoogle.OptionMaps
    """
    return super().options

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param options:
    :param profile:
    :param component_id:
    """
    return '%s = new google.maps.Map(%s, {%s})' % (
      self.chartId, component_id or self.dom.varId, self.options.config_js(options))

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())
