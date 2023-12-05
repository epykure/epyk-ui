#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from epyk.core.html import Html
from epyk.core.html.options import OptionsLeaflet
from epyk.core.js.packages import JsLeaflet
from epyk.core.js import JsUtils
from epyk.core.py import types


class GeoLeaflet(Html.Html):
    name = 'Leaflet Map'
    tag = "div"
    requirements = ('leaflet',)
    _option_cls = OptionsLeaflet.Leaflet

    def __init__(self, page, width, height, html_code, options, profile):
        self.height = height[0]
        super(GeoLeaflet, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                         css_attrs={"width": width, "height": height})
        self.style.css.display = "inline-block"
        self.__loader_funcs = []

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
              source_event: str = None, on_ready: bool = False):
        """The onclick event occurs when the user clicks on an element.
        This function will receive the region, code and element. The common data variable is mapped to the region.

        `Leaflet Doc <https://www.w3schools.com/jsref/event_onclick.asp>`_

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.js.onRegionClick(js_funcs, profile)
        return self

    @property
    def js(self) -> JsLeaflet.LeafLet:
        """The Javascript functions defined for this component.
        Those can be specific ones for the module or generic ones from the language.

        :return: A Javascript Dom object functions.
        """
        if self._js is None:
            self._js = JsLeaflet.LeafLet(selector=self.js_code, component=self, page=self.page)
        return self._js

    @property
    def options(self) -> OptionsLeaflet.Leaflet:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def loader(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """

        :param js_funcs:
        :param profile:
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__loader_funcs.append(JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self

    def build(self, data: types.JS_DATA_TYPES = None, options: types.JS_DATA_TYPES = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """Update the chart with context and / or data changes.

        :param data: Optional. The full datasets object expected by ChartJs
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. Not used
        :param stop_state: Remove the top panel for the component state (error, loading...)
        :param dataflows: Chain of data transformations
        """
        self.js_code = component_id
        str_frg = JsUtils.jsConvertFncs(self.__loader_funcs, toStr=True, profile=profile)
        self.builder_name = "LeafletBuilder%s" % self.page.py.hash(str_frg)
        self._js__builder__ = str_frg
        return super().build(data, options, profile, component_id=component_id, dataflows=dataflows)

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)
