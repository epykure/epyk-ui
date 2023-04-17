#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html

from epyk.core.py import types
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsGoogleAPI

from epyk.core.html.options import OptGoogle


class ChartGeoGoogle(Html.Html):
    name = 'Google Chart'
    requirements = ('google-maps',)
    _option_cls = OptGoogle.OptionMaps

    def __init__(self, page, width, height, options, html_code, profile):
        super(ChartGeoGoogle, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                             css_attrs={"width": width, "height": height})
        self.style.css.margin = "10px 0"

    @property
    def chartId(self):
        """ Return the Javascript variable of the chart. """
        return "%s_obj" % self.htmlCode

    @property
    def js(self) -> JsGoogleAPI.GoogleMapsAPI:
        """
        Javascript base function.

        Return all the Javascript functions defined in the framework.
        THis is an entry point to the full Javascript ecosystem.

        :return: A Javascript object.
        """
        if self._js is None:
            self._js = JsGoogleAPI.GoogleMapsAPI(selector="window['%s']" % self.chartId, component=self, page=self.page)
        return self._js

    @property
    def options(self) -> OptGoogle.OptionMaps:
        """
        Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def build(self, data: types.JS_DATA_TYPES = None, options: types.JS_DATA_TYPES = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None, stop_state: bool = True):
        """
        Update the chart with context and / or data changes.

        :param data: Optional. The full datasets object expected by ChartJs
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. Not used
        :param stop_state: Remove the top panel for the component state (error, loading...)
        """
        return '%s = new google.maps.Map(%s, {%s})' % (
            self.chartId, component_id or self.dom.varId, self.options.config_js(options))

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())
