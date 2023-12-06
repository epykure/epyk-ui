#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from typing import Optional, List
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.fncs import JsFncs
from epyk.core.js.statements import JsIf

from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsD3

from epyk.core.js.primitives import JsObjects
from epyk.core.js.objects import JsCanvas
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsBoolean

from epyk.core.html import Defaults as Defaults_html


class ChartJs(JsCanvas.Canvas):
    display_value = "inline-block"

    def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
                 is_py_data: bool = True, page: primitives.PageModel = None):
        self.htmlCode = js_code if js_code is not None else component.html_code
        self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
        self.component, self.page = component, page
        self._js = []
        self._jquery, self._jquery_ui, self._d3 = None, None, None

    @property
    def val(self):
        """Return a Javascript val object"""
        return JsObjects.JsObjects.get(
            "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
                self.htmlCode, self.content.toStr()))

    @property
    def by_name(self) -> JsNodeDom.JsDomsList:
        """Get Chart objects by name"""
        if self.component.attr.get('name') is not None:
            return JsNodeDom.JsDomsList(
                None, "document.getElementsByName('%s')" % self.component.attr.get('name'), page=self.page)

        return self

    @property
    def isInViewPort(self) -> JsObjects.JsObject.JsObject:
        """Check if the component is in the visible part of the page (the viewport).

        :return: A Javascript boolean
        """
        flag = JsBoolean.JsBoolean("!(rect.bottom < 0 || rect.top - viewHeight >= 0)", js_code="visibleFlag",
                                   set_var=True,
                                   is_py_data=False)
        flag._js.insert(0, self.component.js.viewHeight.setVar('viewHeight'))
        flag._js.insert(0, self.getBoundingClientRect().setVar("rect"))
        return JsFncs.JsAnonymous(flag.r).return_("visibleFlag").call()

    def onViewPort(self, js_funcs: types.JS_FUNCS_TYPES):
        """Trigger some code when the component is visible on the visible part of the page (the viewport).

        :param js_funcs: The Javascript events
        """
        return self.component.js.if_(self.isInViewPort, js_funcs)

    @property
    def content(self):
        """The component content object"""
        return JsHtml.ContentFormatters(self.page, "%s.value" % self.varName)

    def empty(self):
        return '%s.value = ""' % self.varName

    @property
    def events(self) -> JsNodeDom.JsDomEvents:
        """Link to the events attached to a Javascript DOM object"""
        return JsNodeDom.JsDomEvents(self.component)

    @property
    def jquery(self) -> JsQuery.JQuery:
        """Link to the JQuery functions"""
        if self._jquery is None:
            self._jquery = JsQuery.JQuery(component=self.component,
                                          selector=JsQuery.decorate_var("#%s" % self.component.htmlCode), set_var=False)
        return self._jquery

    @property
    def d3(self) -> JsD3.D3Select:
        """Wrapper to the D3 library"""
        if self._d3 is None:
            self._d3 = JsD3.D3Select(component=self.component, selector="d3.select('#%s')" % self.component.htmlCode)
        return self._d3

    @property
    def objects(self) -> JsObjects.JsObjects:
        """Interface to the main Javascript Classes and Primitives"""
        return JsObjects.JsObjects(self.page)

    @property
    def format(self) -> JsHtml.Formatters:
        """ Specific formatters for the HTML components. """
        return JsHtml.Formatters(self.page, self.content.toStr())

    def style(self, attrs: dict):
        """Style property to change from the javascript the CSS attributes of an HTML object.

        Usage::

          button.js.style({"backgroundColor": 'red'})
          button.js.style({"backgroundColor": None})

        `CSS Doc <https://www.w3.org/TR/DOM-Level-2-Style/css.html#CSS-CSSStyleRule-style>`_

        :param attrs: The CSS attributes
    """
        styles = []
        for k, v in attrs.items():
            if "-" in k:
                split_css = k.split("-")
                k = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
            styles.append("this.style.%s = %s" % (k, json.dumps(v)))
        return JsUtils.jsConvertFncs(styles, toStr=True)

    def registerFunction(self, func_name: str, js_funcs: types.JS_FUNCS_TYPES, pmts: Optional[dict] = None,
                         profile: types.PROFILE_TYPE = None):
        """Javascript Framework extension.

        Register a predefined Javascript function.
        This is only dedicated to specific Javascript transformation functions.

        :param func_name: The function name
        :param js_funcs: The Javascript function definition
        :param pmts: Optional.
        :param profile: Optional. A flag to set the component performance storage

        :return: The JsObject
        """
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self.page.properties.js.add_function(func_name, js_data, pmts)
        return self

    def hide(self):
        """Hide the component.

        Usage::

          input.js.hide()

        `Hide Effect Doc <https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/>`_
        """
        return self.css("display", "none")

    def show(self, inline: Optional[str] = None, duration: Optional[int] = None, display_value: Optional[str] = None):
        """Display the component.

        Usage::

          input.js.show()

        `Show Effect Doc <https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/>`_

        :param inline:
        :param duration: A time in second for the component display
        :param display_value: Optional. The value to display. Default inline-block
        """
        display_value = display_value or self.display_value
        if duration is not None:
            return super(JsHtml, self).show('inline-block' if inline else display_value, duration)

        return JsUtils.jsConvertData(self.css("display", 'inline-block' if inline else display_value), None)

    def visible(self, data, inline: Optional[str] = None, display_value: Optional[str] = None):
        """

        :param data: Boolean.
        :param inline:
        :param display_value:
        """
        data = JsUtils.jsConvertData(data, None)
        return JsObjects.JsVoid(
            "if(%s){%s} else{%s}" % (data, self.show(inline, display_value=display_value).r, self.hide().r))

    def select(self):
        """ Select the content of the HTMl component. """
        return JsObjects.JsObjects.get("%s.select()" % self.varName)

    def toggle(self, attr: str = "display", js_val1: Optional[str] = None, js_val2: str = "none"):
        """Toggle (hide / show) the display of the component

        Usage::

          input.js.toggle()
          input.js.toggle("background", "red", "blue")

        `Toggle Effect Doc <https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/>`_

        :param attr:
        :param js_val1:
        :param js_val2:

        :return: A Javascript if statement
        """
        if attr == 'display' and js_val1 is None:
            js_val1 = self.display_value
        return JsIf.JsIf(self.css(attr) == js_val2, [self.css(attr, js_val1)]).else_([self.css(attr, js_val2)])

    def highlight(self, css_attrs: Optional[dict] = None, time_event: int = 1000):
        """

        Usage::

          s.dom.highlight()
          s.dom.highlight(css_attrs={"background": "red"}),

        :param css_attrs: A dictionary with the CSS attributes
        :param time_event: The time of the event
        """
        if css_attrs is None:
            css_attrs, css_attrs_origin = {}, {}
            for k, v in Defaults_html.HTML_HIGHLIGHT.items():
                if isinstance(v, dict):
                    dyn_attrs, dyn_attrs_orign = {}, {}
                    if 'color' in v:
                        dyn_attrs['color'] = getattr(self.page.theme, *v['color'])
                        dyn_attrs_orign['color'] = self.page.theme.greys[0]
                    css_attrs[k] = v['attr'] % dyn_attrs
                    css_attrs_origin[k] = self.component.attr[k] if k in self.component.attr else v[
                                                                                                      'attr'] % dyn_attrs_orign
                else:
                    css_attrs[k] = v
                    css_attrs_origin[k] = self.component.attr[k] if k in self.component.attr else "none"
        else:
            css_attrs_origin = {}
            for k in css_attrs.keys():
                if k in self.component.attr:
                    css_attrs_origin[k] = self.component.attr[k]
                else:
                    css_attrs_origin[k] = "none"
        return '''%s; setTimeout(function(){%s}, %s)
        ''' % (self.css(css_attrs).r, self.css(css_attrs_origin).r, time_event)

    def loadHtml(self, components: List[primitives.HtmlModel], append: bool = False,
                 profile: types.PROFILE_TYPE = None):
        """Load during a Javascript event a component within the one using this method.
        This cannot be tested during the Python execution and should be tested in the browser.

        Tip: It is possible to add a break point to debug in the browser by adding.

        Usage::

          d = page.ui.div().css({"border": "1px solid black"})
          b = page.ui.button("test")
          b.click([
            page.js.console.debugger,
            d.dom.loadHtml(page.ui.texts.label("test label").css({"color": 'blue', 'float': 'none'}))
          ])

        :param components: The different HTML objects to be added to the component
        :param append: Optional. Mention if the component should replace or append the data
        :param profile: Optional. A flag to set the component performance storage

        :return: The Javascript string to be added to the page
        """
        if not isinstance(components, list):
            components = [components]

        js_funcs = []
        for i, h in enumerate(components):
            h.options.managed = False
            js_funcs.append(self.page.js.objects.new(str(h), isPyData=True, varName="obj_%s" % i))
            js_funcs.append(self.innerHTML(self.page.js.objects.get("obj_%s" % i), append=append).r)
        return JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)

    def options(self, options: Optional[dict] = None):
        """Return the builder options used to generate the object on the Javascript side.
        This is not necessarily the same object as the component options as some can be only used on the Python side.

        This will not change the original option object used during the first object creation.

        :param options: Optional. The value to be changed
        """
        opt = dict(self.component._jsStyles)
        if options is not None:
            opt.update(options)
        return opt

    def copyToClipboard(self, clipboardCopySelector=None, with_header=True):
        """

        :param clipboardCopySelector:
        :param with_header:
        """
        return JsObjects.JsVoid(
            "(function(canvas){var image = new Image(); image.src = canvas.toDataURL('image/png'); return image})(%s)" % self.varName)

    def active(self):
        """Return the active clicked point"""
        if self.component._chart__type in ["scatter", "bubble"]:
            active_points = self.component.activePoints()
            return JsObjects.JsObject.JsObject.get("{x: %s, y: %s, label: %s}" % (
                active_points.label,
                JsUtils.jsWrap("%s.data.datasets[%s].data[activePoints[0].index].y" % (
                    active_points.js_code, active_points.num)),
                active_points.x,
            ))

        return JsObjects.JsObject.JsObject.get("{x: %s, y: %s, label: %s}" % (
            self.component.activePoints().label,
            self.component.activePoints().y,
            self.component.activePoints().x,
        ))

    def createWidget(self, html_code: str, container: str = None, options: types.JS_DATA_TYPES = None):
        """Create a new widget derived from an existing one.
        Using this method will make the main object as a template namely it will be removed from the page scope.

        :param html_code: The widget HTML code
        :param container: The widget container. Default the body
        :param options: The specific widget options
        """
        self.component.options.managed = False
        self.component.js_code = html_code
        js_code = JsUtils.jsConvertData(self.component.js_code, None).toStr()
        if js_code.startswith("window"):
            js_code = js_code[7:-1]
        return JsUtils.jsWrap('''(function(containerId, tag, htmlCode, jsCode, ctx, attrs){
    const contDiv = document.createElement("div");
    const newDiv = document.createElement(tag);Object.keys(attrs).forEach( 
        function(key) {contDiv.setAttribute(key, attrs[key]);}); newDiv.id = htmlCode;
    contDiv.appendChild(newDiv);
    if(!containerId){ document.body.appendChild(contDiv)} else {document.getElementById(containerId).appendChild(contDiv)};
    window[jsCode] = new Chart(newDiv.getContext("2d"), ctx); return newDiv;
})(%(container)s, "%(tag)s", %(html_code)s, %(js_code)s, %(ctx)s, %(attrs)s)''' % {
            "js_code": js_code,
            "attrs": self.component.get_attrs(css_class_names=self.component.style.get_classes(), to_str=False),
            "html_code": JsUtils.jsConvertData(html_code or self.component.html_code, None),
            "tag": self.component.tag, "ctx": self.component.getCtx(options),
            "container": JsUtils.jsConvertData(container, None),
        })


class ChartFrappe(JsHtml.JsHtml):

    def createWidget(self, html_code: str, container: str = None, options: types.JS_DATA_TYPES = None):
        """Create a new widget derived from an existing one.
        Using this method will make the main object as a template namely it will be removed from the page scope.

        :param html_code: The widget HTML code
        :param container: The widget container. Default the body
        :param options: The specific widget options
        """
        self.component.options.managed = False
        self.component.js_code = html_code
        js_code = JsUtils.jsConvertData(self.component.js_code, None).toStr()
        if js_code.startswith("window"):
            js_code = js_code[7:-1]
        return JsUtils.jsWrap('''(function(containerId, tag, htmlCode, jsCode, ctx, attrs){
    const newDiv = document.createElement(tag); Object.keys(attrs).forEach(function(key) {
        newDiv.setAttribute(key, attrs[key]);}); newDiv.id = htmlCode;
    if(!containerId){document.body.appendChild(newDiv)} else {document.getElementById(containerId).appendChild(newDiv)};
    window[jsCode] = new frappe.Chart('#'+ htmlCode, ctx); return newDiv
})(%(container)s, "%(tag)s", %(html_code)s, %(js_code)s, %(ctx)s, %(attrs)s)''' % {
            "js_code": js_code,
            "attrs": self.component.get_attrs(css_class_names=self.component.style.get_classes(), to_str=False),
            "html_code": JsUtils.jsConvertData(html_code or self.component.html_code, None),
            "tag": self.component.tag, "ctx": self.component.options.config_js(options).toStr(),
            "container": JsUtils.jsConvertData(container, None),
        })


class ChartApex(JsHtml.JsHtml):

    def createWidget(self, html_code: str, container: str = None, options: types.JS_DATA_TYPES = None):
        """Create a new widget derived from an existing one.
        Using this method will make the main object as a template namely it will be removed from the page scope.

        :param html_code: The widget HTML code
        :param container: The widget container. Default the body
        :param options: The specific widget options
        """
        self.component.options.managed = False
        self.component.js_code = html_code
        js_code = JsUtils.jsConvertData(self.component.js_code, None).toStr()
        if js_code.startswith("window"):
            js_code = js_code[7:-1]
        return JsUtils.jsWrap('''(function(containerId, tag, htmlCode, jsCode, ctx, attrs){
    const newDiv = document.createElement(tag); Object.keys(attrs).forEach(function(key) {
        newDiv.setAttribute(key, attrs[key]);}); newDiv.id = htmlCode;
    if(!containerId){document.body.appendChild(newDiv)} else {document.getElementById(containerId).appendChild(newDiv)};
    window[jsCode] = new ApexCharts(newDiv, ctx); window[jsCode].render(); return newDiv
})(%(container)s, "%(tag)s", %(html_code)s, %(js_code)s, %(ctx)s, %(attrs)s)''' % {
            "js_code": js_code,
            "attrs": self.component.get_attrs(css_class_names=self.component.style.get_classes(), to_str=False),
            "html_code": JsUtils.jsConvertData(html_code or self.component.html_code, None),
            "tag": self.component.tag, "ctx": self.component.options.config_js(options).toStr(),
            "container": JsUtils.jsConvertData(container, None),
        })


class ChartC3(JsHtml.JsHtml):
    ...


class ChartBillboard(ChartC3):
    ...


class Chartist(JsHtml.JsHtml):

    def createWidget(self, html_code: str, container: str = None, options: types.JS_DATA_TYPES = None):
        """Create a new widget derived from an existing one.
        Using this method will make the main object as a template namely it will be removed from the page scope.

        :param html_code: The widget HTML code
        :param container: The widget container. Default the body
        :param options: The specific widget options
        """
        self.component.options.managed = False
        self.component.js_code = html_code
        js_code = JsUtils.jsConvertData(self.component.js_code, None).toStr()
        if js_code.startswith("window"):
            js_code = js_code[7:-1]
        return JsUtils.jsWrap('''(function(containerId, tag, htmlCode, jsCode, chartType, ctx, attrs){
    const newDiv = document.createElement(tag); Object.keys(attrs).forEach(function(key) {
        newDiv.setAttribute(key, attrs[key]);}); newDiv.id = htmlCode;
    if(!containerId){document.body.appendChild(newDiv)} else {document.getElementById(containerId).appendChild(newDiv)};
    window[jsCode] = new Chartist[chartType]("#"+ htmlCode, {}, ctx); return newDiv
})(%(container)s, "%(tag)s", %(html_code)s, %(js_code)s, %(chart_type)s, %(ctx)s, %(attrs)s)''' % {
            "js_code": js_code,
            "attrs": self.component.get_attrs(css_class_names=self.component.style.get_classes(), to_str=False),
            "chart_type": JsUtils.jsConvertData(self.component._chart__type, None),
            "html_code": JsUtils.jsConvertData(html_code or self.component.html_code, None),
            "tag": self.component.tag, "ctx": self.component.options.config_js(options).toStr(),
            "container": JsUtils.jsConvertData(container, None),
        })


class RoughViz(JsHtml.JsHtml):

    def createWidget(self, html_code: str, container: str = None, options: types.JS_DATA_TYPES = None):
        """Create a new widget derived from an existing one.
        Using this method will make the main object as a template namely it will be removed from the page scope.

        :param html_code: The widget HTML code
        :param container: The widget container. Default the body
        :param options: The specific widget options
        """
        self.component.options.managed = False
        self.component.js_code = html_code
        js_code = JsUtils.jsConvertData(self.component.js_code, None).toStr()
        if js_code.startswith("window"):
            js_code = js_code[7:-1]
        return JsUtils.jsWrap('''(function(containerId, tag, htmlCode, jsCode, chartType, ctx, attrs){
    const newDiv = document.createElement(tag); Object.keys(attrs).forEach(function(key) {
        newDiv.setAttribute(key, attrs[key]);}); newDiv.id = htmlCode;
    if(!containerId){document.body.appendChild(newDiv)} else {document.getElementById(containerId).appendChild(newDiv)};
    window[jsCode] = new roughViz[chartType](ctx); return newDiv
})(%(container)s, "%(tag)s", %(html_code)s, %(js_code)s, %(chart_type)s, %(ctx)s, %(attrs)s)''' % {
            "js_code": js_code,
            "attrs": self.component.get_attrs(css_class_names=self.component.style.get_classes(), to_str=False),
            "chart_type": JsUtils.jsConvertData(self.component._chart__type, None),
            "html_code": JsUtils.jsConvertData(html_code or self.component.html_code, None),
            "tag": self.component.tag, "ctx": self.component.options.config_js(options).toStr(),
            "container": JsUtils.jsConvertData(container, None),
        })