#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.js.packages import JsQuery
from epyk.core.html.options import OptJqvM
from epyk.core.js.packages import JsQueryVectorMap


class JqueryVectorMap(Html.Html):
    name = 'Jquery Vector Map'
    requirements = ('jqvmap',)
    _option_cls = OptJqvM.OptionsJqVM

    def __init__(self, page, width, height, html_code, options, profile):
        self.height = height[0]
        super(JqueryVectorMap, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                              css_attrs={"width": width, "height": height})
        self.chartId = "%s_obj" % self.htmlCode
        self.style.css.display = "inline-block"

    def click(self, js_funcs, profile=None, source_event=None, on_ready=False):
        """
        The onclick event occurs when the user clicks on an element.
        This function will receive the region, code and element. The common data variable is mapped to the region.

        Related Pages:

          https://www.w3schools.com/jsref/event_onclick.asp

        :param js_funcs: List | String. A Javascript Python function
        :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
        :param source_event: String. Optional. The source target for the event.
        :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.options.onRegionClick(js_funcs, profile)
        return self

    def drag(self, js_funcs, profile=None, source_event=None, on_ready=False):
        """

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        source_event = source_event or JsQuery.decorate_var(self.htmlCode, convert_var=False)
        self.on("drag", js_funcs, profile, source_event=source_event, on_ready=on_ready)
        self._browser_data['mouse']["drag"][source_event]['fncType'] = "on"
        return self

    @property
    def js(self) -> JsQueryVectorMap.JQVMap:
        """
        Javascript base function.

        Return all the Javascript functions defined in the framework.
        THis is an entry point to the full Javascript ecosystem.

        :return: A Javascript object.
        """
        if self._js is None:
            self._js = JsQueryVectorMap.JQVMap(
                component=self, js_code=JsQuery.decorate_var(self.htmlCode, convert_var=False), page=self.page)
        return self._js

    @property
    def options(self) -> OptJqvM.OptionsJqVM:
        """
        Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    _js__builder__ = '''%s.vectorMap(options)''' % JsQuery.decorate_var("htmlObj", convert_var=False)

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())
