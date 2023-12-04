#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional

from epyk.core.html import Html
from epyk.core.html.options import OptJqvM
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryVectorMap

from epyk.core.py import types as etypes


class JqueryVectorMap(Html.Html):
    name = 'Jquery Vector Map'
    requirements = ('jqvmap',)
    _option_cls = OptJqvM.OptionsJqVM

    def __init__(self, page, width, height, html_code: Optional[str], options, profile: etypes.PROFILE_TYPE):
        self.height = height[0]
        super(JqueryVectorMap, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                              css_attrs={"width": width, "height": height})
        self.style.css.display = "inline-block"

    def click(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """The onclick event occurs when the user clicks on an element.
        This function will receive the region, code and element. The common data variable is mapped to the region.

        `JQV Doc <https://www.w3schools.com/jsref/event_onclick.asp`>_

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: Optional. The source target for the event
        :param on_ready: Boolean. Specify if the event needs to be trigger when the page is loaded
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.options.onRegionClick(js_funcs, profile)
        return self

    def drag(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None,
             source_event: Optional[str] = None, on_ready: bool = False):
        """

        :param js_funcs: A Javascript Python function
        :param profile: Set to true to get the profile for the function on the Javascript console
        :param source_event: The source target for the event
        :param on_ready: Specify if the event needs to be trigger when the page is loaded
        """
        source_event = source_event or JsQuery.decorate_var(self.html_code, convert_var=False)
        self.on("drag", js_funcs, profile, source_event=source_event, on_ready=on_ready)
        self._browser_data['mouse']["drag"][source_event]['fncType'] = "on"
        return self

    @property
    def js(self) -> JsQueryVectorMap.JQVMap:
        """Javascript base function.
        Return all the Javascript functions defined in the framework.
        THis is an entry point to the full Javascript ecosystem.

        :return: A Javascript object.
        """
        if self._js is None:
            self._js = JsQueryVectorMap.JQVMap(
                component=self, js_code=JsQuery.decorate_var(self.html_code, convert_var=False), page=self.page)
        return self._js

    @property
    def options(self) -> OptJqvM.OptionsJqVM:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    _js__builder__ = '''%s.vectorMap(options)''' % JsQuery.decorate_var("htmlObj", convert_var=False)

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)
