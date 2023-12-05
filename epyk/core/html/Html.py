#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import json
import collections
import functools
import logging
import inspect

from pathlib import Path
from typing import Union, Optional, List, Any
from epyk.core.py import primitives, types

from epyk.core.js import JsUtils
from epyk.core.js import Js
from epyk.core.js import Imports
from epyk.core.js.html import JsHtml
from epyk.core.js import packages
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import packageImport

from epyk.core.css.styles import GrpCls
from epyk.core.css import Defaults as Defaults_css

from epyk.core.html import Aria
from epyk.core.html import WebComponents
from epyk.core.html import KeyCodes
from epyk.core.html.options import Options
from epyk.core.html import Defaults as Default_html

try:  # For python 3
    import urllib.request as urllib2
    import urllib.parse as parse
except ImportError:  # For Python 2
    import urllib2
    import urllib as parse

regex = re.compile('[^a-zA-Z0-9_]')


def cleanData(value: str):
    """Function to clean the javascript data to allow the use of variables

      :param value: The value to clean
      """
    return regex.sub('', value.strip())


# ---------------------------------------------------------------------------------------------------------
#                                          FRAMEWORK DECORATORS
#
# ---------------------------------------------------------------------------------------------------------
def deprecated(comment: str):
    """This is a decorator which can be used to mark functions as deprecated. It will result in a warning being emitted
    when the function is used.

    :param comment:
    """

    def decorator(func):
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            import os
            logging.warning('#########################################')
            logging.warning("Action => {}.".format(os.getcwd()))
            logging.warning("Call to deprecated function {}.".format(func.__name__))
            logging.warning("Action => {}.".format(comment))
            logging.warning('#########################################')
            return func(*args, **kwargs)

        return new_func

    return decorator


def inprogress(func):
    """Decorator to specify a function is still in development so the result might not be fully tested yet.

    :param func: Function. A python function.
    """

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        # warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        # warnings.warn('############################################################################')
        # warnings.warn("Call to a test function {}.".format(func.__name__), category=DeprecationWarning, stacklevel=2)
        # warnings.warn('############################################################################')
        # warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return func(*args, **kwargs)

    return new_func


def jbuider(group: str = None, name: str = None, refresh: bool = False, asynchronous: bool = False):
    def decorator(func):
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            component = args[0]
            if name is not None:
                component.builder_name = name
            if not component.page.properties.js.has_constructor(component.builder_name) or refresh:
                native_path = os.environ.get("NATIVE_JS_PATH")
                if group is not None:
                    internal_native_path = Path(Path(__file__).resolve().parent, "..", "js", "native", group)
                else:
                    internal_native_path = Path(Path(__file__).resolve().parent, "..", "js", "native")
                if native_path is None:
                    native_path = internal_native_path
                native_builder = Path(native_path, "%s.js" % component.builder_name)
                internal_native_builder = Path(internal_native_path, "%s.js" % component.builder_name)
                if native_builder.exists():
                    component.page.js.customFile("%s.js" % component.builder_name, path=native_path, authorize=True)
                    component.builder_name = "%s%s" % (component.builder_name[0].lower(), component.builder_name[1:])
                    component.page.properties.js.add_constructor(component.builder_name, None)
                elif internal_native_builder.exists():
                    component.page.js.customFile(
                      "%s.js" % component.builder_name, path=internal_native_builder, authorize=True)
                    component.builder_name = "%s%s" % (component.builder_name[0].lower(), component.builder_name[1:])
                    component.page.properties.js.add_constructor(component.builder_name, None)
                else:
                    if not component.builder_name or component._js__builder__ is None:
                        raise ValueError("No builder defined for this HTML component %s" % component.__class__.__name__)

                    if component.async_builder or asynchronous:
                        component.page.properties.js.add_constructor(
                            component.builder_name, "async function %s(htmlObj, data, options){%s}" % (
                                component.builder_name, component._js__builder__))
                    else:
                        component.page.properties.js.add_constructor(
                            component.builder_name, "function %s(htmlObj, data, options){%s}" % (
                                component.builder_name, component._js__builder__))
            return func(*args, **kwargs)

        return new_func

    return decorator


def jformatter(group: str = None, name: str = None, refresh: bool = False, asynchronous: bool = False):
  def decorator(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
      component = args[0]
      if name is not None:
        component.builder_name = name
      if not component.page.properties.js.has_constructor(component.builder_name) or refresh:
        native_path = os.environ.get("NATIVE_JS_PATH")
        if group is not None:
          internal_native_path = Path(Path(__file__).resolve().parent, "..", "js", "native", group)
        else:
          internal_native_path = Path(Path(__file__).resolve().parent, "..", "js", "native")
        if native_path is None:
          native_path = internal_native_path
        native_builder = Path(native_path, "%s.js" % component.builder_name)
        internal_native_builder = Path(internal_native_path, "%s.js" % component.builder_name)
        if native_builder.exists():
          component.page.js.customFile("%s.js" % component.builder_name, path=native_path, authorize=True)
          component.builder_name = "%s%s" % (component.builder_name[0].lower(), component.builder_name[1:])
          component.page.properties.js.add_constructor(component.builder_name, None)
        elif internal_native_builder.exists():
          component.page.js.customFile(
            "%s.js" % component.builder_name, path=internal_native_builder, authorize=True)
          component.builder_name = "%s%s" % (component.builder_name[0].lower(), component.builder_name[1:])
          component.page.properties.js.add_constructor(component.builder_name, None)
        else:
          if not component.builder_name or component._js__builder__ is None:
            raise ValueError("No builder defined for this HTML component %s" % component.__class__.__name__)

          if component.async_builder or asynchronous:
            component.page.properties.js.add_constructor(
              component.builder_name, "async function %s(data, options){%s}" % (
                component.builder_name, component._js__builder__))
          else:
            component.page.properties.js.add_constructor(
              component.builder_name, "function %s(data, options){%s}" % (
                component.builder_name, component._js__builder__))
      return func(*args, **kwargs)

    return new_func

  return decorator


def set_component_skin(component: primitives.HtmlModel):
    """

    :param component:
    """
    if component.page.ui.components_skin is not None:
        shortcuts = {"button": "buttons.button", "title": "texts.title"}
        for sc, msc in shortcuts.items():
            if sc in component.page.ui.components_skin:
                component.page.ui.components_skin[msc] = component.page.ui.components_skin[sc]
        alias = inspect.stack()[1].function.lower()
        if alias in component.page.ui.components_skin:
            comp_skin = component.page.ui.components_skin[alias]
            if 'clear' in comp_skin:
                if comp_skin["clear"].get("css"):
                    component.style.clear_style()
                if comp_skin["clear"].get("cls"):
                    component.style.clear(True)
            component.css(component.page.ui.components_skin[alias].get('css', {}))
            for cls in comp_skin.get("cls", []):
                component.attr["class"].add(cls)
    return component


class Required:
    js, css = None, None

    def __init__(self, page: primitives.PageModel):
        self.js, self.css = {}, {}
        self._page = page

    def add(self, package: str, version: Optional[str] = None, verbose: bool = None):
        """Add the package to the main page context.

        TODO: Use the version number

        :param package: The package alias.
        :param version: Optional. The package version number.
        :param verbose: Optional. Display version details (default True).
        """
        html_types = set()
        if package in Imports.JS_IMPORTS:
            self.js[package] = version or '*'
            self._page.jsImports.add(package)
            html_types.add('js')
        if package in Imports.CSS_IMPORTS:
            self.css[package] = version or '*'
            self._page.cssImport.add(package)
            html_types.add('css')
        if self._page.ext_packages is not None and package in self._page.ext_packages:
            for mod in self._page.ext_packages[package]['modules']:
                if mod['script'].endswith(".css"):
                    self._page.cssImport.add(package)
                    html_types.add('css')
                elif mod['script'].endswith(".js"):
                    self._page.jsImports.add(package)
                    html_types.add('js')
            if "services" in self._page.ext_packages[package]:
                self._page.cssImport.add(package)
        if not html_types and verbose and package != "other-icons":
            logging.warning("%s - Not defined in neither JS nor CSS configurations" % package)
        if version:
            if self._page.imports.setVersion(package, version, verbose=verbose):
                self._page.imports.reload()


class EventTouch:

    def __init__(self, page):
        self._page = page

    def start(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False,
              source_event: Optional[str] = None):
        """The touchstart event occurs when the user touches an element.
        Note: The touchstart event will only work on devices with a touch screen.

        Tip: Other events related to the touchstart event are:

        Usage::

          start([page.js.alert("Test")])

        `Learn more <https://www.w3schools.com/jsref/event_touchstart.asp>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        self._page.on("touchstart", js_funcs, profile, source_event=source_event)
        return self._page

    def move(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False,
             source_event: Optional[str] = None):
        """The touchmove event occurs when the user moves the finger across the screen.

        The touchmove event will be triggered once for each movement, and will continue to be triggered until the finger
        is released.

        Usage::

            move([page.js.alert("Test")])

        `Learn more <https://www.w3schools.com/jsref/event_touchmove.asp>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        self._page.on("touchmove", js_funcs, profile, source_event=source_event)
        return self._page

    def cancel(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False,
               source_event: Optional[str] = None):
        """The touchcancel event occurs when the touch event gets interrupted.

        Different devices will interrupt a touch event at different actions, and it is considered good practice to include
        this event to clean up code if this "error" should occur.

        Usage::

            cancel([page.js.alert("Test")])

        `Learn more <https://www.w3schools.com/jsref/event_touchcancel.asp>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        self._page.on("touchcancel", js_funcs, profile, source_event=source_event)
        return self._page

    def end(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False,
            source_event: Optional[str] = None):
        """The touchend event occurs when the user removes the finger from an element.

        Note: The touchend event will only work on devices with a touch screen.

        Tip: Other events related to the touchend event are:

        Usage::

            end([page.js.alert("Test")])

        `Learn more <https://www.w3schools.com/jsref/event_touchend.asp>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        self._page.on("touchend", js_funcs, profile, source_event=source_event)
        return self._page

    def swap(self, js_funcs_left: types.JS_FUNCS_TYPES, js_funcs_right: types.JS_FUNCS_TYPES,
             profile: types.PROFILE_TYPE = False, source_event: Optional[str] = None):
        """Add swap event functions.

        :param js_funcs_left: Javascript functions
        :param js_funcs_right: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        self.start(["window.longTouch = event.touches[0].clientX || event.originalEvent.touches[0].clientX"],
                   profile=profile, source_event=source_event)
        self.move(self._page.js.if_("window.longTouch != null", [
            "let swap =  (event.touches[0].clientX || event.originalEvent.touches[0].clientX) - window.longTouch",
            "window.longTouch = null", self._page.js.if_("swap < 0", js_funcs_left).else_(js_funcs_right)],
                                    profile=profile),
                  source_event=source_event)
        return self


class Components(collections.OrderedDict):

    def css(self, attrs: dict):
        """Set the CSS style for all the inner components.

        :param attrs: The CSS attributes.
        """
        for component in self.values():
            if hasattr(component, "css"):
                component.css(attrs)
        return self

    def add(self, component: primitives.HtmlModel):
        """Standard way to add a component to the rendered dictionary.

        :param component: HTML component.
        """
        self[component.htmlCode] = component
        return self


class Html(primitives.HtmlModel):
    """Parent class for all the HTML components. All the function defined here are available in the children classes.
Child class can from time to time re implement the logic but the function will always get the same meaning (namely
the same signature and return).
"""
    requirements = None
    defined_code = False
    builder_name, _js__builder__, async_builder = None, None, False
    _option_cls = Options
    tag = None

    def __init__(self, page: primitives.PageModel, vals, html_code: Optional[str] = None,
                 options: types.OPTION_TYPE = None, profile: types.JS_FUNCS_TYPES = None,
                 css_attrs: Optional[dict] = None, verbose: bool = False):
        """ Create an python HTML object """
        # Child component for this component
        self.components = Components()
        self.page = page
        self.require = Required(page)
        for package in self.requirements or []:
            if isinstance(package, tuple):
                self.require.add(package[0], package[1], verbose=verbose)
            else:
                self.require.add(package, verbose=verbose)

        self.profile = profile
        self._on_ready_js, self._sort_propagate, self._sort_options, self.__aliasCode = {}, False, None, None
        self._dom, self._sub_htmls, self._js, self.helper, self._styleObj, self.__htmlCode = None, [], None, "", None, None

        self._browser_data = {"mouse": collections.OrderedDict(), 'component_ready': [],
                              'page_ready': collections.OrderedDict(), 'keys': collections.OrderedDict()}

        # to be deleted - because changed should be done only on the component self.require
        self.jsImports = page.jsImports
        self.cssImport = page.cssImport

        self._jsStyles = {}  # to be deleted - because code => htmlCode, _jsStyles should be renamed

        self.innerPyHTML = None  # to be reviewed - not sure this is still useful

        self.__options = self._option_cls(component=self, attrs=options, page=self.page)

        self.attr = {'class': self.style.classList['main'], 'css': self.style.css.attrs}
        if css_attrs is not None:
            self.css(css_attrs)

        if html_code is not None:
            if html_code[0].isdigit() or cleanData(html_code) != html_code:
                raise ValueError("htmlCode %s cannot start with a number or contain, suggestion %s " % (
                    html_code, cleanData(html_code)))

            if html_code in self.page.components:
                if html_code in ["content", "content_page", "page_nav_bar"]:
                    raise ValueError(
                        "Duplicated Html code '%s', this is used internally in the framework !" % html_code)

                # Move to reference instead of HTML_code because not unique for component in the page context
                # Component can still be retrieved using ths code by using explicitly the get_components_by_ref method/
                self.__aliasCode = html_code
                i = 1
                temp_html_code = "%s_%s" % (html_code, i)
                while temp_html_code in self.page.components:
                    i += 1
                    temp_html_code = "%s_%s" % (html_code, i)
                html_code = temp_html_code

            self.__htmlCode = html_code
            self.js_code = html_code
            self.defined_code = True
            if html_code in self.page.inputs:
                vals = self.page.inputs[html_code]

        self.page.components[self.htmlCode] = self
        self._vals = vals
        if self.builder_name is None:
            self.builder_name = self.__class__.__name__
        self._internal_components = [self.htmlCode]

    def with_profile(self, profile: types.PROFILE_TYPE, event: Optional[str] = None,
                     element_id: Optional[str] = None) -> dict:
        """Return the profile options.

        :param profile: Optional. A flag to set the component performance storage.
        :param event: Optional. The event name.
        :param element_id: Optional. A DOM component reference in the page.
        """
        if profile is None and self.profile:
            if event is None:
                return {"name": element_id or self.htmlCode}

            return {"name": "%s[%s]" % (element_id or self.htmlCode, event)}

        if profile is None and self.page.profile:
            if event is None:
                return {"name": element_id or self.htmlCode}

            return {"name": "%s[%s]" % (element_id or self.htmlCode, event)}

        return profile

    def add(self, component: primitives.HtmlModel):
        """Add items to a container.

        The added HTML component will not be managed by the page by default. This means it might not be visible on the
        JavaScript page if it is not by default managed by the main HTML component.

        For example containers are designed to handle subcomponents.

        Usage::

          div = page.ui.div()
          div.add(page.ui.button("Run"))

        :param component: Component added to the val main component
        """
        return self.__add__(component)

    def insert(self, i: int, component: primitives.HtmlModel):
        """Add a component to the sub list of components for a container at a defined position.
        This is a user-friendly shortcut to the self.val feature.

        Usage::

          comp_title.style.css.float = "left"
          comp_title.style.css.font_size = self.page.body.style.globals.font.normal(-2)
          comp_title.style.css.color = self.page.theme.greys[-2]
          menu_items.insert(0, comp_title)

        :param i: The position for the component in the container
        :param component: Component added to the val main component
        """
        if not hasattr(component, 'options'):
            component = self.page.ui.div(component)
        component.options.managed = False
        self.val.insert(i, component)
        return self

    def __add__(self, component: primitives.HtmlModel):
        """ Add items to a container """
        if hasattr(component, 'options'):
            component.options.managed = False
        self.val.append(component)
        return self

    def __getitem__(self, i: int):
        if not isinstance(i, int) and i in self.components:
            return list(self.components.items())[i][1]

        return self.val[i]

    def set_builder(self, name: str, all_components: bool = True):
        """Change the default builder definition.

        This method can be used to externalise the JavaScript expression to dedicated modules.
        If nothing is defined the default one defined in the class property `_js__builder__`  will be used.

        Usage::

          page = pk.Page()
          page.properties.js.add_text('''
          function NewButton(htmlObj, data, options){
            htmlObj.style.color = "red"; htmlObj.innerHTML = data}
          ''')
          page.properties.js.set_constructor("NewButton")
          btn = page.ui.button("click")
          btn.set_builder("NewButton")
          btn2 = page.ui.button("click 2")
          btn.click([btn.build("Clicked"), btn2.build("Clicked")])

        :param name: The builder name (alias but also function name)
        :param all_components: Apply the builder change to all components generated from this class
        """
        self.builder_name = name
        if all_components:
            self.__class__.builder_name = name

    @property
    def style(self) -> GrpCls.ClassHtml:
        """The CSS style (class and attributes) of the HTML component.
        This property will allow to custom any component in the page.

        Usage::

          div = page.ui.div()
          div.style.css.background = 'black'
        """
        if self._styleObj is None:
            self._styleObj = GrpCls.ClassHtml(self)
        return self._styleObj

    @property
    def html_code(self) -> str:
        """Unique reference for any HTML component in the framework. This must be defined in the interface and cannot be
        changed in the report.

        This reference can be used in the Python to get the html object from components in the page but it is also
        used in any web framework by the JavaScript to get the DOM object and apply the necessary transformations.

        There is no setter for this property in order to ensure a consistency in Python and JavaScript.

        Usage::

          div = page.ui.div(html_code="testDiv")
          print(div.html_code)
        """
        if self.__htmlCode is not None:
            return self.__htmlCode

        return "%s_%s" % (self.__class__.__name__.lower(), id(self))

    @property
    def js_code(self):
        if self.__htmlCode is not None:
            if hasattr(self.__htmlCode, "toStr"):
                return JsUtils.jsWrap("window[%s + 'Id']" % self.__htmlCode)

            return "%sId" % self.__htmlCode

        return "%s%sId" % (self.__class__.__name__.lower(), id(self))

    @js_code.setter
    def js_code(self, value: str):
        if value is not None:
            self.__htmlCode = value
            if hasattr(self.__htmlCode, "toStr"):
                self._set_js_code(value, "window[%s + 'Id']" % self.__htmlCode)
            else:
                self._set_js_code(value, "%sId" % value)

    def _set_js_code(self, html_code: str, js_code: str) -> str:
        ...

    @property
    def ref(self) -> str:
        """ The component ref used in REST calls when html_code is not unique in current context"""
        return self.__aliasCode or self.html_code

    @property
    def htmlCode(self) -> str:
        """Unique reference for any HTML component in the framework. This must be defined in the interface and cannot
        be changed in the report.

        This reference can be used in the Python to get the html object from components in the page but it is also
        used in any web framework by the JavaScript to get the DOM object and apply the necessary transformations.

        There is no setter for this property in order to ensure a consistency in Python and JavaScript.

        Usage::

          div = page.ui.div(htmlCode="testDiv")
          print(div.htmlCode)
        """
        if self.__htmlCode is not None:
            return self.__htmlCode

        return "%s_%s" % (self.__class__.__name__.lower(), id(self))

    @property
    def js(self) -> 'Js.JsBase':
        """Javascript base function.

        Return all the Javascript functions defined in the framework.
        THis is an entry point to the full Javascript ecosystem.

        Usage::

          div = page.ui.div(htmlCode="testDiv")
          div.click([
            div.js.alert("Hello")
          ])

        :return: A Javascript object
        """
        if self._js is None:
            self._js = Js.JsBase(self.page, component=self)
        return self._js

    @property
    def dom(self) -> JsHtml.JsHtml:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript available for a DOM element by default.

        Usage::

          div = page.ui.div(htmlCode="testDiv")
          print(div.dom.content)

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtml(component=self, page=self.page)
        return self._dom

    @property
    def options(self) -> Options:
        """Property to set all the possible object for a button.
    
        Usage::

          div = page.ui.div(htmlCode="testDiv")
          div.options.inline = True
        """
        return self.__options

    def prepend_child(self, component: primitives.HtmlModel, profile: types.PROFILE_TYPE = None):
        """Wrapper to the Javascript method insertChild to add an HTML component.

        Usage::

          for i in range(10):
            comp = page.ui.texts.label("Add Label %s" % i).css({"width": "100%", "display": 'block'})
            select.prepend_child(comp)

        `Learn more <https://www.w3schools.com/jsref/met_node_insertbefore.asp>`_

        :param component: The html component
        :param profile: Optional. A flag to set the component performance storage

        :return: The HTML component.
        """
        self._sub_htmls.append(component)
        self.components[component.htmlCode] = component
        # add a flag to propagate on the Javascript the fact that some child nodes will be added
        # in this case innerHYML cannot be used anymore
        self._jsStyles["_children"] = self._jsStyles.get("_children", 0) + 1
        self.page.properties.js.add_builders(JsUtils.jsConvertFncs([
            self.dom.insertBefore(component.dom)], toStr=True, profile=profile))
        return self

    def append_child(self, component: primitives.HtmlModel, profile: types.PROFILE_TYPE = None):
        """Wrapper to the Javascript method appendChild to append an HTML component.

        Usage::

          for i in range(10):
            component = page.ui.texts.label("Add Label %s" % i).css({"width": "100%", "display": 'block'})
            select.append_child(component)

        `Learn more <https://www.w3schools.com/jsref/met_node_appendchild.asp>`_

        :param component: The html component
        :param profile: Optional. A flag to set the component performance storage

        :return: The HTML component.
        """
        self._sub_htmls.append(component)
        # add a flag to propagate on the Javascript the fact that some child nodes will be added
        # in this case innerHYML cannot be used anymore
        self._jsStyles["_children"] = self._jsStyles.get("_children", 0) + 1
        self.page.properties.js.add_builders(JsUtils.jsConvertFncs([
            self.dom.appendChild(component.dom)], toStr=True, profile=profile))
        return self

    def onReady(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Add set of event / actions which will be triggered after the build of the object.
        Usually this can be used to add js functions on a chart or a table.

        Usage::

          network = page.ui.charts.vis.network()
          network.onReady([network.js.setData({"nodes": [{"id": 0, "label": "test"}], "edges": []})])

        :param js_funcs: Javascript functions
        :param profile: A flag to set the component performance storage
        """
        if not profile and self.page.profile:
            profile = {"name": "%s[onReady" % self.htmlCode}
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._browser_data['component_ready'].extend(JsUtils.jsConvertFncs(js_funcs, profile=profile))

    def add_banner(self, component: primitives.HtmlModel, css: Optional[dict] = None):
        """Add a banner to a component.

        This will change the position of the container.

        :param component: The banner component
        :param css: Optional. A dictionary with the CSS style to be added to the component
        """
        self.style.css.position = "relative"
        self.style.css.overflow = "hidden"
        component.style.css.position = "absolute"
        self.add(component)
        if css is not None:
            self.css(css)
        return self

    def add_menu(self, context_menu: primitives.HtmlModel):
        """Attach a context menu to an existing component. A context menu must have a component attached to otherwise
        the report will not be triggered.

        :param context_menu: A Python context menu object
        """
        context_menu.source = self
        self.page._contextMenu[self.dom.jquery.varName] = context_menu
        return self

    def add_icon(self, text: str, css: Optional[dict] = None, position: str = "before", family: Optional[str] = None,
                 html_code: Optional[str] = None):
        """Add an icon to the HTML object.

        Usage::

          checks.title.add_icon("wrench") # For cross family icon definition
          checks.title.add_icon("fas fa-align-center") # for font awesome icon

        :param text: The icon reference from font-awesome website
        :param css: Optional. A dictionary with the CSS style to be added to the component
        :param position: Optional. The position compared to the main component tag
        :param family: Optional. The icon framework to be used (preferred one is font-awesome)
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)

        :return: The Html object.
        """
        self.icon = ""
        defined_families = ('office-ui-fabric-core', 'material-design-icons', 'font-awesome', 'bootstrap-icons')
        if family is not None and self.options.verbose and family not in defined_families:
            logging.warning("Family %s not defined in %s" % (family, defined_families))

        if family is None:
            family = self.page.icons.family
        if text is not None:
            html_code_icon = "%s_icon" % html_code if html_code is not None else html_code
            self.icon = self.page.ui.images.icon(
                text, html_code=html_code_icon, family=family).css({"margin-right": '5px', 'font-size': 'inherit'})
            self.icon.defined_code = self.defined_code
            if position == "before":
                self.prepend_child(self.icon)
            else:
                self.append_child(self.icon)
            if css is not None:
                self.icon.css(css)
        return self

    def add_label(self, text: str, css: Optional[dict] = None, position: str = "before", for_: str = None,
                  html_code: Optional[str] = None, options: types.OPTION_TYPE = None):
        """Add an elementary label component.

        `Learn more <https://www.w3schools.com/tags/tag_label.asp>`_

        :param text: The label content
        :param css: Optional. A dictionary with the CSS style to be added to the component
        :param position: Optional. The position compared to the main component tag
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param for_: Optional. Specifies which form element a label is bound to
        """
        self.label = ""
        if text is not None:
            html_code_label = "%s_label" % html_code if html_code is not None else html_code
            self.label = self.page.ui.texts.label(text, options=options, html_code=html_code_label)
            self.label.defined_code = self.defined_code
            if for_ is not None:
                # Attach the label to another HTML component based on the ID
                self.label.attr['for'] = for_
            if position == "before":
                self.prepend_child(self.label)
            else:
                self.append_child(self.label)
            if css == False:
                self.label.attr['css'] = {}
            elif css is not None:
                self.label.css(css)
        return self

    def add_span(self, text: str, css: Optional[Union[dict, bool]] = None, position: str = "before",
                 html_code: Optional[str] = None, i: Optional[int] = None):
        """Add an elementary span component.

        `Learn more <https://fontawesome.com/how-to-use/on-the-web/styling/layering>`_

        :param text: The Span content
        :param css: Optional. The CSS style to be added to the component
        :param position: Optional. The position compared to the main component tag
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param i: Optional. The index of the span element to be created
        """
        key_attr = 'span_%s' % i if i is not None else 'span'
        setattr(self, key_attr, '')
        if text is not None:
            html_code_span = "%s_span" % html_code if html_code is not None else html_code
            setattr(self, key_attr, self.page.ui.texts.span(text, html_code=html_code_span))
            span = getattr(self, key_attr)
            if position == "before":
                self.prepend_child(span)
            else:
                self.append_child(span)
            if css == False:
                span.attr['css'] = {}
            elif css is not None:
                span.css(css)
        return self

    def add_link(self, text: str, url: str = None, script_name: Optional[str] = None, report_name: Optional[str] = None,
                 name: Optional[str] = None, icon: Optional[str] = None, css: Optional[dict] = None,
                 position: str = "before", options: types.OPTION_TYPE = None):
        """Add an elementary label component.

        Usage::

          div = page.ui.div()
          div.add_link("test.py", name="Click to go to the test report")

        :param text: The value of the link displayed in the page
        :param url: Optional. The URL path
        :param script_name:
        :param report_name:
        :param name:
        :param icon:
        :param css: Optional. A dictionary with the CSS style to be added to the component
        :param position: Optional. The position compared to the main component tag
        :param options:
        """
        self.link = ""
        if url is not None or script_name is not None:
            dfl_options = {"name": name} if name is not None else {}
            if options is not None:
                dfl_options.update(options)
            if url is not None:
                self.link = self.page.ui.links.external(text, url, options=dfl_options)
            else:
                self.link = self.page.ui.links.script(text, script_name, report_name, icon=icon, options=dfl_options)
            if position == "before":
                self.prepend_child(self.link)
            else:
                self.append_child(self.link)
            if css is not None:
                self.link.css(css)
        return self

    def add_title(self, text: str, level: Optional[int] = None, css: Optional[dict] = None, position: str = "before",
                  options: types.OPTION_TYPE = None):
        """Add an elementary title component.

        :param text: The title content
        :param level: Optional. The level of title
        :param css: Optional. The CSS style to be added to the component
        :param position: Optional. The position compared to the main component tag
        :param options: Optional. Specific Python options available for this component
        """
        self.title = ""
        if text is not None:
            self.title = self.page.ui.texts.title(text, level=level, options=options)
            if options is not None and options.get('managed', True):
                if position == "before":
                    self.prepend_child(self.title)
                else:
                    self.append_child(self.title)
            else:
                self.title.options.managed = False
            if css == False:
                self.title.attr['css'] = {}
            elif css is not None:
                self.title.css(css)
        return self

    def add_input(self, text: str, css: Optional[dict] = None, attrs: Optional[dict] = None, position: str = "before",
                  options: types.OPTION_TYPE = None):
        """Add an elementary input component.

        :param text: The title content
        :param css: Optional. The CSS style to be added to the component
        :param attrs: Optional. The HTML tag attributes
        :param position: Optional. Specific Python options available for this component
        :param options: Optional. Specific Python options available for this component
        """
        self.input = ""
        if text is not None:
            if options is not None and options.get("autocomplete"):
                input_options = dict(options)
                if 'position' in input_options:
                    del input_options['position']
                del input_options['autocomplete']

                self.input = self.page.ui.inputs.autocomplete(
                    text, width=(100, '%'), html_code="%s_input" % self.htmlCode, options=input_options)
                self.input.options.appendTo = "#%s" % self.htmlCode
                self.input.options.position()
            else:
                self.input = self.page.ui.inputs.input(text, html_code="%s_input" % self.htmlCode, options=options)
            if position == "before":
                self.prepend_child(self.input)
            else:
                self.append_child(self.input)
            if css is not None:
                self.input.css(css)
            if attrs is not None:
                self.input.set_attrs(attrs=attrs)
        return self

    def add_checkbox(self, flag: bool, css: Optional[dict] = None, attrs: Optional[dict] = None,
                     position: str = "before"):
        """Add an elementary checkbox component.

        :param flag: The state of the checkbox component
        :param css: Optional. The CSS style to be added to the component
        :param attrs: Optional. The HTML tag attributes
        :param position: Optional. Specific Python options available for this component
        """
        self.checkbox = ""
        if flag is not None:
            self.checkbox = self.page.ui.inputs.checkbox(flag)
            if position == "before":
                self.prepend_child(self.checkbox)
            else:
                self.append_child(self.checkbox)
            if css is not None:
                self.checkbox.css(css)
            if attrs is not None:
                self.checkbox.set_attrs(attrs=attrs)
        return self

    def add_helper(self, text: str, css: dict = None):
        """Add an elementary helper icon.

        The helper is not managed by the main page and should be written in the component.

        :param text: The helper content
        :param css: Optional. The CSS style to be added to the component
        """
        if text is not None:
            self.helper = self.page.ui.rich.info(text)
            self.helper.options.managed = False
            if css is not None:
                self.helper.css(css)
        return self

    @property
    def keydown(self) -> KeyCodes.KeyCode:
        """The onkeydown event occurs when the user is pressing a key (on the keyboard).

        `Learn more <https://www.w3schools.com/jsref/event_onkeydown.asp>`_
        """
        if self._browser_data.get('keys', {}).get('keydown') is None:
            self._browser_data['keys']['keydown'] = KeyCodes.KeyCode(component=self)
        return self._browser_data['keys']['keydown']

    @property
    def keypress(self) -> KeyCodes.KeyCode:
        """The onkeypress event occurs when the user presses a key (on the keyboard).

        `Learn more <https://www.w3schools.com/jsref/event_onkeypress.asp>`_
        """
        if self._browser_data.get('keys', {}).get('keypress') is None:
            self._browser_data['keys']['keypress'] = KeyCodes.KeyCode(component=self)
        return self._browser_data['keys']['keypress']

    @property
    def keyup(self) -> KeyCodes.KeyCode:
        """The onkeypress event occurs when the user presses a key (on the keyboard).

        `Learn more <https://www.w3schools.com/jsref/event_onkeypress.asp>`_
        """
        if self._browser_data.get('keys', {}).get('keyup') is None:
            self._browser_data['keys']['keyup'] = KeyCodes.KeyCode(component=self)
        return self._browser_data['keys']['keyup']

    @property
    def aria(self) -> Aria.Aria:
        """Accessible Rich Internet Applications is a [HTML] specification module.
        Web developers MAY use the ARIA role and aria-* attributes on HTML elements.

        `Learn more <https://www.w3.org/TR/html-aria/#allowed-aria-roles-states-and-properties>`_
        """
        return Aria.Aria(self)

    @property
    def val(self):
        """Property to get the jquery value of the HTML object in a python HTML object.

        This method can be used in any jsFunction to get the value of a component in the browser.
        This method will only be used on the javascript side, so please do not consider it in your algorithm in Python.

        :returns: Javascript string with the function to get the current value of the component
        """
        return self._vals

    @property
    def content(self):
        """Get the HTML content of the component as a string. """
        if self.innerPyHTML is not None:
            if isinstance(self.innerPyHTML, list):
                return "".join([h.html() if hasattr(h, "html") else str(h) for h in self.innerPyHTML])

            return self.innerPyHTML.html()

        return self.val if not hasattr(self.val, "html") else self.val.html()

    def move(self):
        """Move the component to this position in the page. """
        self.page.components.move_to_end(self.htmlCode)

    def css(self, key: Union[str, dict] = None, value: Optional[str] = None, reset: bool = False):
        """Change the CSS Style of a main component. This is trying to mimic the signature of the Jquery css function.

        `Learn more <http://api.jquery.com/css/>`_

        :param key: Optional. The key style in the CSS attributes (Can also be a dictionary)
        :param value: Optional. The value corresponding to the key style
        :param reset: Optional. Specify if the CSS styles need to be emptied first

        :return: The python object itself.
        """
        if key is None and value is None:
            return self.attr['css']

        if reset:
            self.style.css.attrs = {}
            self.attr['css'] = self.style.css.attrs
        # Do not add None value to the CSS otherwise it will break the page on the front end side
        if value is None and isinstance(key, dict):
            css_vals = key if isinstance(key, dict) else {}
        elif value is None and hasattr(key, "attrs"):
            # Accept the CSSInline object
            self.attr['css'].update(key.attrs)
            return self

        elif value is None and not isinstance(key, dict):
            return self.attr['css'].get(key)

        else:
            if isinstance(value, tuple):
                value = value[0] if value[0] is None else "%s%s" % (value[0], value[1])
            css_vals = {key: value}
        if 'css' not in self.attr:
            self.attr['css'] = self.style.css.attrs
        for key, value in css_vals.items():
            if isinstance(value, tuple):
                if value[0] is None:
                    continue

                value = "%s%s" % (value[0], value[1])
            if value is None:
                continue

            self.attr['css'][key] = value if isinstance(value, str) else json.dumps(value)
        return self

    def add_style(self, css_classes: Optional[Union[str, list]] = None, css_attrs: Optional[dict] = None,
                  clear_first: bool = False, keep_css_keys: Optional[tuple] = ("width", "height")):
        """Add CSS styles (inline and classes) to the component.

        This function could also remove all the predefined CSS style first.
        To create inline CSS it will use the underlying css function.

        :param css_classes: Optional. The CSS class reference
        :param css_attrs: Optional. The CSS attributes
        :param clear_first: Optional. Remove all the predefined CSS Inline style and classes for the component
        :param keep_css_keys: Optional. List of attributes to maintain (default width and height)
        """
        if clear_first:
            self.attr["class"].clear()
            if keep_css_keys is not None:
                if css_attrs is None:
                    css_attrs = {}
                for css_key in keep_css_keys:
                    if css_key in self.attr["css"]:
                        css_attrs[css_key] = self.attr["css"][css_key]
            self.style.clear_style()
        if not isinstance(css_classes, list):
            css_classes = [css_classes]
        for classname in css_classes:
            if classname is not None:
                if classname == "active":
                    self.aria.current = "true"
                self.attr["class"].add(classname)
        if css_attrs is not None:
            self.css(css_attrs)
        return self

    @packages.packageImport('bootstrap', 'bootstrap')
    def tooltip(self, value: types.JS_DATA_TYPES, location: str = 'top', options: types.OPTION_TYPE = None):
        """Add the Tooltip feature when the mouse is over the component.
        This tooltip version is coming from Bootstrap.

        Usage::

          htmlObj.tooltip("My tooltip", location="bottom")

        `Learn more <https://getbootstrap.com/docs/4.1/components/tooltips/>`_

        TODO Change background color

        :param value: The tooltip text
        :param location: Optional. The position of the tooltip
        :param options: Optional. Specific Python options available for this component

        :return: The Python object self.
        """
        if self.page.imports.pkgs.bootstrap.version[0] > "5.":
            if value is not None:
                self.attr.update({'data-bs-html': 'true', 'data-bs-placement': location, "data-bs-toggle": "tooltip"})
                if options is not None:
                    self.attr.update(options)
                self.page.properties.js.add_on_ready('''
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)})''')
                if hasattr(value, 'toStr'):
                    self.onReady([self.dom.setattr("title", value), self.dom.setattr("alt", value)])
                else:
                    self.attr.update({'title': value, 'alt': value})

        else:
            if value is not None:
                self.attr.update({'data-html': 'true', 'data-placement': location})
                # TODO Check with error with 'data-toggle': 'tooltip'
                if options is not None:
                    self.attr.update(options)
                self.page.properties.js.add_on_ready(
                    "%s.tooltip()" % JsQuery.decorate_var("'[data-toggle=tooltip]'", convert_var=False))
                if hasattr(value, 'toStr'):
                    self.onReady([self.dom.setattr("title", value), self.dom.setattr("alt", value)])
                else:
                    self.attr.update({'title': value, 'alt': value})
        return self

    @packages.packageImport('bootstrap', 'bootstrap')
    def popover(self, content: str, title: str = None, options: types.OPTION_TYPE = None):
        """Add a tooltip using Bootstrap Popover feature.

        `Learn more <https://getbootstrap.com/docs/4.4/components/popovers/>`_

        :param content: The tooltip content
        :param title: Optional. The tooltip title
        :param options: Optional. Specific Python options available for this component
        """
        if content is not None:
            self.attr["data-content"] = content
            if title is not None:
                self.attr["data-title"] = title
            if options is not None:
                for k, v in options.items():
                    self.attr["data-%s" % k] = title
            self.attr["data-toggle"] = 'popover'
            self.page.properties.js.add_on_ready(
                "%s.popover()" % JsQuery.decorate_var("'[data-toggle=popover]'", convert_var=False))
        return self

    def draggable(self, js_funcs: types.JS_FUNCS_TYPES = None, options: types.OPTION_TYPE = None,
                  profile: types.PROFILE_TYPE = None, source_event: str = None):
        """Set the component as a draggable item.

        :param js_funcs: Javascript functions
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        js_funcs = js_funcs or []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.attr["draggable"] = True
        return self.on("dragstart", js_funcs + [
            'event.dataTransfer.setData("text", event.target.innerHTML)'], profile=profile, source_event=source_event)

    def sticky(self, anchor: primitives.HtmlModel, css_attrs: dict = None):
        """Change the CSS style of the component to be sticky on the page.

        This will add a class to the component. It is possible to set some attributes in order to
        change its style.

        :param anchor: the component which will be used to check the position
        :param css_attrs: Optional. The CSS attributes of the component once sticky
        """
        if anchor.htmlCode == self.htmlCode:
            raise ValueError("Anchor cannot be the moving component")

        css_attrs = css_attrs or {"bottom": "10px", "left": "10px", "height": "200px !IMPORTANT"}
        css_attrs["position"] = "fixed"
        css_vals = "{%s}" % "; ".join(["%s: %s" % (k, v) for k, v in css_attrs.items()])
        cls_name = "sticky_component_%s" % self.page.py.hash(css_vals)
        self.page.properties.css.add_text(".%s %s\n" % (cls_name, css_vals))
        self.page.body.scroll([
            self.page.js.if_(anchor.dom.isInViewPort, [
                self.dom.classList.remove(cls_name)
            ]).else_([
                self.page.js.if_(self.dom.classList.is_missing(cls_name), [
                    self.dom.classList.add(cls_name)])])
        ])
        return self

    def add_options(self, options: types.OPTION_TYPE = None, name: str = None, value: str = None):
        """Change the Javascript options of the component.

        This will change the options sent to the Javascript.

        :param options: Optional. the extra options to be added to the component
        :param name: Optional. The key. The option name
        :param value: Optional. The value. The option value

        :return: self to allow the chains
        """
        if options is None and name is None:
            raise ValueError("Either the attrs or the name should be specified")

        if options is None:
            options = {name: value}
        for k, v in options.items():
            self._jsStyles[k] = v
        return self

    def set_attrs(self, attrs: Optional[dict] = None, name: Optional[str] = None, value: Optional[Any] = None,
                  remove_if_none: bool = True):
        """Function to update the internal dictionary of object attributes. Those attributes will be used when the HTML
        component will be defined.

        Basically all sort of attributes can be defined here: CSS attributes, but also data, name...
        Either the attrs or the tuple (name, value) can be used to add information to the dom object.

        All the attributes should be Python object which are ready to use on the Javascript side.
        For example True should be written 'true'.

        Tips: It is possible to use the data- attributes to store any kind of information in the dom.

        `Learn more <https://www.w3schools.com/html/html_attributes.asp>`_

        :param attrs: Optional. All the HTML tags attributes
        :param name: Optional. A python string with the name of the attribute
        :param value: Optional. A python string with the value of the attribute
        :param remove_if_none: Optional. Remove attribute if true
        """
        if attrs is None and name is None:
            raise ValueError("Either the attrs or the name should be specified")

        if attrs is None:
            attrs = {name: value}
        for k, v in attrs.items():
            if k == 'css':
                # Section for the Style attributes
                if v is None:
                    self.style.clear_style()
                    continue

                if 'css' not in self.attr:
                    self.attr['css'] = dict(v)
                else:
                    self.attr['css'].update(v)
            elif k == 'class':
                self.style.clear()
                if v is None:
                    continue

                if not isinstance(v, set):
                    v = set(v.split(" "))
                for c in v:
                    self.attr['class'].add(c)
            else:
                # Section for all the other attributes#
                if v is not None:
                    self.attr[k] = v
                elif remove_if_none:
                    if k in self.attr:
                        # Remove the None value if present in the component's attributes
                        del self.attr[k]
                else:
                    # Set the non value anyway
                    self.attr[k] = v

        return self

    def get_attrs(self, with_id: bool = True, css_class_names: List[str] = None, to_str: bool = True):
        """Return the string line with all the attributes.

        All the attributes in the div should use double quote and not simple quote to be consistent everywhere in the
        framework and also in the javascript. If there is an inconsistency, the aggregation of the string fragments will
        not work

        :param with_id: Optional. Add the ID tag. This is handled by the framework. (Default true)
        :param css_class_names: Optional. The Python class names

        :return: A string with the dom attributes
        """
        css_style, css_class, class_data, attrs = '', '', '', {}
        if 'css' in self.attr:
            styles = ";".join(["%s:%s" % (key, val) for key, val in self.attr["css"].items()])
            if styles:
                css_style = 'style="%s"' % styles
                attrs["style"] = styles
        if 'class' in self.attr and len(self.attr['class']) > 0 and class_data:
            if css_class_names is not None:
                # Need to merge in the class attribute some static classes coming from external CSS Styles sheets
                # and the static python classes defined on demand in the header of your report
                # self.page.cssObj.getClsTag(pyClassNames)[:-1] to remove the ' generated in the module automatically
                css_class = self.page.style.getClsTag(css_class_names.clsMap).replace('class="', 'class="%s ')
                if css_class:
                    css_class %= class_data
                else:
                    css_class = 'class="%s"' % class_data
            else:
                css_class = 'class="%s"' % class_data
        elif css_class_names is not None:
            py_cls_names = [cls.get_ref() if hasattr(cls, 'get_ref') else cls for cls in css_class_names['main']]
            css_class = 'class="%s"' % " ".join(py_cls_names) if len(py_cls_names) > 0 else ""
        attrs["class"] = css_class[7:-1]

        if with_id:
            self.attr['id'] = self.html_code
            self.attr['data-builder'] = self.builder_name
            attrs["id"] = self.html_code
            attrs["data-builder"] = self.builder_name
        html_tags = []
        for key, val in self.attr.items():
            if key not in ('css', 'class'):
                if val is not None:
                    attrs[key] = str(val).replace('"', "'")
                    html_tags.append('%s="%s"' % (key, str(val).replace('"', "'")))
                else:
                    html_tags.append(key)

        #html_tags = ['%s="%s"' % (key, str(val).replace('"', "'")) if val is not None else key for key, val in
        #             self.attr.items() if key not in ('css', 'class')]
        for tag in [css_style, css_class]:
            if tag:
                html_tags.append(tag)
        str_tag = " ".join(html_tags)
        if to_str:
            return str_tag.strip()

        return attrs

    def on(self, event: str, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
           source_event: Optional[str] = None, on_ready: bool = False, func_args: List[str] = None,
           method: str = "addEventListener"):
        """Add an event to the document ready function.

        This is to mimic the Jquery on function.

        Tip: use the r function to not have side effects when Python is building the JavaScript:
          span.on("mouseover", span.dom.css("color", "red").r)
          span.on("mouseleave", span.dom.css("color", "blue"))

        `Learn more event <https://www.w3schools.com/jquery/event_on.asp>`_
        `Learn more event listener <https://www.w3schools.com/js/js_htmldom_eventlistener.asp>`_
        `Learn more dom event <https://www.w3schools.com/jsref/dom_obj_event.asp>`_

        :param event: The Javascript event type from the dom_obj_event.asp
        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        :param func_args:
        :param method:

        :return: self to allow the chains.
        """
        profile = self.with_profile(profile, event=event)
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        source_event = source_event or self.dom.varId
        if event not in self._browser_data['mouse']:
            self._browser_data['mouse'][event] = {}
        self._browser_data['mouse'][event].setdefault(source_event, {}).setdefault("content", []).extend(
            JsUtils.jsConvertFncs(js_funcs))
        self._browser_data['mouse'][event][source_event]['profile'] = profile
        self._browser_data['mouse'][event][source_event]['fncType'] = method
        if func_args:
            self._browser_data['mouse'][event][source_event]['args'] = func_args
        if on_ready:
            self.page.body.onReady([self.dom.events.trigger(event)])
        return self

    def event_fnc(self, event: str):
        """Function to get the generated JavaScript method in order to then reuse it in other components.

        This will return the event function in a string already transpiled.

        :param event: The event function
        """
        return list(self._browser_data['mouse'][event][self.dom.varId]["content"])

    def drop(self, js_funcs: types.JS_FUNCS_TYPES, prevent_default: bool = True, profile: types.PROFILE_TYPE = None):
        """Add a drag and drop property to the element.

        Usage::

          d = page.ui.div()
          d.drop([page.js.objects.data.toRecord([1, 2, 3, 4], "result")])

        :param js_funcs: A Javascript Python function
        :param prevent_default: Optional. Specify if the event should have a default behaviour on the page
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console

        :return: Return self to allow the chaining
        """
        if not profile and self.page.profile:
            profile = {"name": "%s[drop]" % self.htmlCode}
        dft_fnc = ""
        if prevent_default:
            dft_fnc = self.page.js.objects.event.preventDefault()
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_funcs = JsUtils.jsConvertFncs(
            ["var data = %s" % self.page.js.objects.event.dataTransfer.text] + js_funcs, toStr=True, profile=profile)
        # By default change the box shadow of this component
        self.attr["ondrop"] = "(function(event){%s; %s; %s; return false})(event)" % (
            dft_fnc, str_funcs, self.dom.css('box-shadow', 'none').r)
        self.attr["ondragover"] = "(function(event){%s; %s})(event)" % (
            dft_fnc, self.dom.css('box-shadow', 'inset 0px 0px 0px 2px %s' % self.page.theme.success.base).r)
        self.attr["ondragleave"] = "(function(event){%s; %s})(event)" % (
            dft_fnc, self.dom.css('box-shadow', 'none').r)
        return self

    def hover(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
              source_event: Optional[str] = None):
        """Add a mouse hover event on the component.

        Usage::

          div = page.ui.div()
          div.hover([page.js.alert("This is a test")])

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self.on("mouseover", js_funcs, profile, source_event)

    def viewport(self, js_funcs: types.JS_FUNCS_TYPES, options: dict = None, profile: types.PROFILE_TYPE = None,
                 source_event: Optional[str] = None):
        """Trigger an event when the component is visible.

        The result of the event can be on the component itself (the observer) or another component (to load / add items).

        Usage::

          text = page.ui.text("This is a text")
          text.viewport([
            page.js.delay([text.build("Change the value")], 5),
            text.dom.css("color", "red")])

        :param js_funcs: A Javascript Python function
        :param options: Optional.
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: Optional. The source target for the event
        """
        return self.page.body.onReady([
            self.page.js.intersectionObserver(
                js_code="observer_%s" % self.html_code, callback=js_funcs, options=options, profile=profile,
                observe_once=True).observe(source_event or self)
        ])

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """The onclick event occurs when the user clicks on an element.

        Usage::

          div = page.ui.div()
          div.click([page.js.alert("This is a test")])

        `Learn more <https://www.w3schools.com/jsref/event_onclick.asp>`_

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if on_ready:
            self.page.body.onReady([self.dom.events.trigger("click")])
        return self.on("click", js_funcs, profile, source_event)

    def focusout(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                 source_event: Optional[str] = None):
        """The onfocusout event occurs when the user select an element.

        Usage::

          div = page.ui.div()
          div.focusout([page.js.alert("This is a test")])

        `Learn more <https://www.w3schools.com/jsref/event_onfocusout.asp>`_

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function in the console
        :param source_event: Optional. The source target for the event
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_funcs.insert(0, "if(%(dom)s.contains(event.relatedTarget)) {return ;}" % {
            "dom": source_event or self.dom.varId})
        return self.on("focusout", js_funcs, profile, source_event)

    def dblclick(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                 source_event: Optional[str] = None, on_ready: bool = False):
        """The ondblclick event occurs when the user double-clicks on an element.

        `Learn more <https://www.w3schools.com/jsref/event_ondblclick.asp>`_

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the console
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if on_ready:
            self.page.body.onReady([self.dom.events.trigger("dblclick")])
        return self.on("dblclick", js_funcs, profile, source_event)

    def scroll(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
               source_event: Optional[str] = None):
        """The onscroll event occurs when an element's scrollbar is being scrolled.

        `Learn more <https://www.w3schools.com/jsref/event_onscroll.asp>`_

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: Optional. The source target for the event
        """
        return self.on("scroll", js_funcs, profile, source_event)

    def mouse(self, on_funcs: types.JS_FUNCS_TYPES = None, out_funcs: types.JS_FUNCS_TYPES = None,
              profile: types.PROFILE_TYPE = None, source_event: Optional[str] = None):
        """Wrapper function fot the mouse event.

        This function will cover the on mouse hover event and mouse out.

        More specific events are possible using the generic out function.

        Tip: As function are defined to be chaining in most of the components use .r to get the string representation and
        clean the cache.

        Usage::

          span.mouse([
              span.dom.css("color", "red"),
              span.dom.css("cursor", "pointer").r],
            span.dom.css("color", "blue").r)

        :param on_funcs: Optional. The Javascript events
        :param out_funcs: Optional. The Javascript events
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event

        :return: self to allow the chains.
        """
        self.style.css.cursor = 'pointer'
        if on_funcs is not None:
            self.on("mouseenter", on_funcs, profile, source_event)
        if out_funcs is not None:
            self.on("mouseleave", out_funcs, profile, source_event)
        return self

    def paste(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, source_event=None,
              components=None):
        """Add a paste event to the component.

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        :param components: Optional.
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        data_map = self.page.js.data.datamap(components, {"clipboard": self.page.js.objects.event.clipboardData.text})
        str_fncs = JsUtils.jsConvertFncs(
            ["var data = %s" % data_map.toStr()] + js_funcs, toStr=True)
        return self.on("paste", str_fncs, profile, source_event)

    def contextMenu(self, menu, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None):
        """Attach a context menu to a component and set a function to called before the display.

        TODO Test context menu

        :param menu:
        :param js_funcs: Optional. The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not hasattr(menu, 'source'):
            menu = self.page.ui.menus.contextual(menu)
        self.context_menu = menu
        menu.source = self
        new_js_funcs = (js_funcs or []) + [
            self.page.js.objects.mouseEvent.stopPropagation(),
            self.context_menu.dom.css({"display": 'block', 'left': self.page.js.objects.mouseEvent.clientX + "'px'",
                                       'top': self.page.js.objects.mouseEvent.clientY + "'px'"}),
            self.page.js.objects.mouseEvent.preventDefault()]
        self.on("contextmenu", new_js_funcs, profile)
        return menu

    @property
    def touch(self) -> EventTouch:
        """Shortcut property to all the Touch event.

        Events that occur when user touches a touch-based device, belongs to the TouchEvent Object.

        `Learn more <https://www.w3schools.com/jsref/obj_touchevent.asp>`_

        Usage::

          component.touch.
        """
        return EventTouch(self)

    def _set_js_code(self, html_code: str, js_code: str):
        """Set a different code for the component.
        This method will ensure both HTML and Js references will be properly changed for this component.
        This method is used by the js_code property and should not be used directly.

        :param html_code: The new HTML code
        :param js_code: The new JavaScript code
        """
        self.js.varName = js_code
        self.dom.varName = "document.getElementById(%s)" % JsUtils.jsConvertData(html_code, None)

    @jbuider()
    def build(self, data: types.JS_DATA_TYPES = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None, component_id: Optional[str] = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """Return the JavaScript fragment to refresh the component content.

        Usage::

          dt = page.ui.rich.update()
          page.ui.button("Update").click([dt.refresh()])

        :param data: Optional. Component data
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The object reference ID
        :param dataflows: Chain of data transformations
        """
        self.js_code = component_id
        self.options.builder = self.builder_name
        # check if there is no nested HTML components in the data
        if isinstance(data, dict):
            tmp_data = ["%s: %s" % (JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)) for k, v in
                        data.items()]
            js_data = "{%s}" % ",".join(tmp_data)
        else:
            js_data = JsUtils.dataFlows(data, dataflows, self.page)
        fnc_call = "%s(%s, %s, %s)" % (
            self.builder_name, self.dom.varId, js_data, self.options.config_js(options))
        profile = self.with_profile(profile, event="Builder")
        if profile:
            fnc_call = JsUtils.jsConvertFncs(
                ["var result = %s(htmlObj, data, options)" % self.builder_name], toStr=True, profile=profile)
            fnc_call = "(function(htmlObj, data, options){%s; return result})(%s, %s, %s)" % (
                fnc_call, self.dom.varId, js_data, self.options.config_js(options))
        return fnc_call

    def build_from_url(self, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None, component_id: Optional[str] = None,
              dataflows: List[dict] = None):
        """Return the JavaScript fragment to refresh the component content from url parameters.
        This could be usually used at the start when component is loaded.

        Data will come from the url from the html_code defined for this component.

        Usage::

          dt = page.ui.rich.update(html_code='updt')
          page.ui.button("Update").onReady([dt.build_from_url()])

        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The object reference ID
        :param dataflows: Chain of data transformations
        """
        return JsUtils.jsWrap('''(function(param){
const queryString = window.location.search; const urlParams = new URLSearchParams(queryString);
if (urlParams.has(param)){paramValue = urlParams.get(param); %s}; 
})(%s)''' % (self.build(
            JsUtils.jsWrap("paramValue"), options=options, profile=profile, component_id=component_id,
            dataflows=dataflows),
             JsUtils.jsConvertData(self.html_code, None)))

    def refresh(self):
        """Component refresh function. Javascript function which can be called in any Javascript event.

        Tip: This function cannot be used in a plan Python section but in a JavaScript one defined in an event for
        example.
        """
        return self.build(self.val, None)

    def subscribe(self, socket, channel: str, data=None, options: Optional[dict] = None,
                  js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None):
        """Subscribe to a socket channel.

        Data received from the socket are defined as a dictionary with a field data.

        The content of data will be used by this component.

        `Learn more <https://timepicker.co/options/>`_

        :param socket: Socket. A python socket object
        :param channel: The channel on which events will be received
        :param data:
        :param options: Optional. Specific Python options available for this component
        :param js_funcs: Optional. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if data is None:
            data = socket.message
        js_funcs = js_funcs if js_funcs is not None else []
        socket.on(channel, [self.build(data, options, profile)] + js_funcs)
        return self

    @packageImport('sortablejs')
    def sortable(self, options: types.OPTION_TYPE = None, propagate: bool = True, propagate_only: bool = False):
        """Sortable is a JavaScript library for reorderable drag-and-drop lists.

        `Learn more <https://github.com/SortableJS/Sortable>`_

        :param options: Optional. The sortable options
        :param propagate: Optional. Specify if the sub children should get the draggable property
        :param propagate_only: Optional. Specify if the first level of child is draggable

        :rtype: JsSortable.Sortable
        """
        from epyk.core.js.packages import JsSortable

        self._sort_propagate = propagate
        if not propagate_only:
            if 'sortable' not in self._on_ready_js:
                self._on_ready_js['sortable'] = JsSortable.Sortable(
                    self, js_code="%s_sortable" % self.htmlCode, selector=self.dom.varId, page=self.page)
                dfl_options = {"group": self.htmlCode}
                dfl_options.update(options or {})
                self._sort_options = dfl_options
                self._on_ready_js['sortable'].create(self.dom.varId, dfl_options)
            return self._on_ready_js['sortable']

    def __str__(self):
        """Apply the corresponding function to build the HTML result.

        This function is very specific and it has to be defined in each class.
        """
        raise NotImplementedError('subclasses must override __str__()!')

    @property
    def component(self) -> WebComponents.Component:
        """The static component definition on the Javascript Side.

        This will be then used by the different framework to define the elementary bricks on which the complex component
        will be based on.
        """
        return WebComponents.Component(self)

    def html(self):
        """Render the HTML component to the JavaScript.

        This will be the main function called by the page to render all the component.s
        """
        str_result = []
        if self._on_ready_js:
            self.onReady(list(self._on_ready_js.values()))
        if self.helper != "":
            self.helper.html()

        # Propagate the external requirements to the page
        for js in self.require.js:
            self.page.jsImports.add(js)
        for css in self.require.css:
            self.page.cssImport.add(css)

        if self.defined_code:
            self.page.properties.js.set_init_options(self.html_code, self.options.config_js().toStr())
        str_result.append(str(self))
        return "".join(str_result)

    def export(self) -> dict:
        comp_props = {
            'folder': self.__class__.__name__.lower(), 'class': "%sComponent" % self.__class__.__name__,
            'styleUrls': "", "externalVars": "", "componentFunctions": [], "requirements": list(self.requirements),
            'htmlTag': "app-epyk-%s" % self.__class__.__name__.lower()}
        if self._js__builder__ is not None:
            comp_props["builder"] = "%s(htmlObj, data, options){%s}" % (self.builder_name, self._js__builder__)
        return comp_props

    def loading(self, status: bool = True, label: str = Default_html.TEMPLATE_LOADING_ONE_LINE,
                data: types.JS_DATA_TYPES = None) -> str:
        return ""

    def error(self, status: bool = True, label: str = Default_html.TEMPLATE_ERROR_LINE,
              data: types.JS_DATA_TYPES = None) -> str:
        return ""


class Body(Html):
    name = "Body"
    tag = "body"

    def __init__(self, report, vals, html_code: Optional[str] = None, options: types.OPTION_TYPE = None,
                 profile: types.PROFILE_TYPE = None, css_attrs: dict = None, verbose: bool = False):
        super(Body, self).__init__(report, vals, html_code, options, profile, css_attrs, verbose=verbose)
        if Defaults_css.BODY_STYLE is not None:
            for attrs in Defaults_css.BODY_STYLE.split(";"):
                k, v = attrs.split(":")
                self.css(key=k, value=v)
        self._template = None
        # header and footer.
        self.header, self.footer = None, None

    @property
    def style(self) -> GrpCls.ClassPage:
        """A property to the CSS style of the DOM component.

        Each component will have default CSS style but they can be overridden.
        """
        if self._styleObj is None:
            self._styleObj = GrpCls.ClassPage(self)
        return self._styleObj

    @property
    def dom(self) -> JsHtml.JsHtml:
        """Return all the Javascript functions defined for an HTML Component.

        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtml(self, page=self.page)
            self._dom.varName = "document.body"
        return self._dom

    def scroll(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
               source_event: str = None):
        """The onscroll event occurs when an element's scrollbar is being scrolled.

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.page.js.onReady(
            self.page.js.window.events.addScrollListener(JsUtils.jsConvertFncs(js_funcs, toStr=True)))
        return self

    def onReady(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Add set of event / actions which will be triggered after the build of the object.

        usually this can be used to add js functions on a chart or a table.

        Usage::

          network = page.ui.charts.vis.network()
          network.onReady([network.js.setData({"nodes": [{"id": 0, "label": "test"}], "edges": []})])

        :param js_funcs: Javascript function to be added once the object is built
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.page.js.onReady(js_funcs)

    def onLoad(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Add a JavaScript function in the builder section which correspond to the JavaScript onload.

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.page.properties.js.add_builders(JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))

    def fromConfig(self, js_funcs: types.JS_FUNCS_TYPES = None,
                   components: Optional[List[primitives.HtmlModel]] = None,
                   lang: Optional[str] = "eng", end_point: str = "/static/configs", sync: bool = True,
                   filename: Optional[str] = None):
        """Load teh configuration file in order to fill the templates with static data.

        This will allow to externalise the configuration and design rich web templates.

        Do not forget to use CTRL+F5 in order to refresh the browser cache to get the updates.

        Usage::

          title = page.ui.title(html_code="title")
          page.body.onReady([page.body.fromConfig(components=[title], end_point="/static", lang=None)])

        :param js_funcs: Optional. The various transformations to be triggered from the configuration data
        :param components: Optional. The various HTML Components to be updated from the configuration file
        :param lang: Optional. The default lang for the configuration
        :param end_point: Optional. The url for the configuration files
        :param sync: Optional. Specify if the type of loading event
        :param filename: Optional. The filename for the configuration
        """
        if self.page.json_config_file is None:
            raise ValueError("json_config_file must be attached to the page to load the corresponding configuration")

        js_funcs = js_funcs or []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]

        from epyk import configs

        builders = []
        for c in components:
            configs.keys[c.htmlCode] = c.options.config_default
            builders.append(c.build(self.page.js.objects.get("data['%s']" % c.htmlCode)))
        return '''
      if (typeof window['page_config'] === 'undefined'){
        var rawFile = new XMLHttpRequest(); const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString); var lang = urlParams.get('lang') || %(lang)s; 
        rawFile.overrideMimeType("application/json"); 
        if(lang != null){ rawFile.open("GET", "%(url)s/"+ lang +"/%(json)s.json", %(sync)s)}
        else{rawFile.open("GET", "%(url)s/%(json)s.json", %(sync)s)};
        rawFile.onreadystatechange = function() {
            if (rawFile.readyState === 4 && rawFile.status == "200") {
               var data = JSON.parse(rawFile.responseText); window['page_config'] = data; %(fncs)s}}
        rawFile.send(null)} 
      else {var data = window['page_config']; %(fncs)s}''' % {
            "sync": JsUtils.jsConvertData(not sync, None), "lang": JsUtils.jsConvertData(lang, None), 'url': end_point,
            'json': filename or self.page.json_config_file,
            'fncs': JsUtils.jsConvertFncs(js_funcs + builders, toStr=True)}

    def set_content(self, page: primitives.PageModel, page_content: str):
        """Function to allow the templating of the report.

        This can be overridden by a generic class which can be shared within a set of report

        :param page: The main report object
        :param page_content: The html content of the page

        :return: The Body HTML object
        """
        self._html_content = page_content
        return self

    def set_background(self, start_color: Optional[str] = None, end_color: Optional[str] = None,
                       from_theme: bool = False):
        """Change the body background color.

        Usage::

          page.body.set_background("#101626", "#374F67")

        :param start_color: Optional. The first code color
        :param end_color: Optional. The last code color
        :param from_theme: Optional. Default to the code colors defined in the theme
        """
        if from_theme or (start_color is None and end_color is None):
            self.style.css.background = "linear-gradient(%s 0%%, %s 100%%)" % (
                self.page.theme.colors[-1], self.page.theme.colors[2])
        elif end_color is not None:
            self.style.css.background = "linear-gradient(%s 0%%, %s 100%%)" % (start_color, end_color)
        else:
            self.style.css.background = start_color
        self.style.css.background_repeat = "no-repeat"
        self.style.css.background_color = self.page.theme.colors[2]
        return self

    def loading(self, status: bool = True, label: str = "Loading...", component=None,
                z_index: int = 500, attrs: dict = None):
        """Display a loading page.

        Usage::

          page.body.loading(),
          ...
          page.body.loading(False)

        :param status: Optional. A flag to specify the status of the loading event
        :param z_index: Optional. Specifies the stack order of an element
        :param label: Optional.
        :param component: Optional.
        :param attrs: Optional.
        """
        if status:
            attrs = attrs or {"font-size": "50px", "color": self.page.theme.dark_or_white()}
            if not hasattr(component, 'options'):
                component = self.page.ui.icon(component or "fas fa-spinner fa-spin")
                component.options.managed = False
                component.style.css.margin_right = 5
                component.style.css.font_size = "inherit"
            return ''' 
        if (typeof window['popup_loading_body'] === 'undefined'){
          window['popup_loading_body'] = document.createElement("div"); 
          window['popup_loading_body'].style.width = '100%%'; window['popup_loading_body'].style.height = '100%%'; window['popup_loading_body'].style.opacity = 0.3;
          window['popup_loading_body'].style.position = 'fixed'; window['popup_loading_body'].style.top = 0; window['popup_loading_body'].style.left = 0; window['popup_loading_body'].style.zIndex = %(z_index)s;
          window['popup_loading_body'].style.background = '%(background)s'; window['popup_loading_body'].style.color = 'white'; window['popup_loading_body'].style.textAlign = 'center'; window['popup_loading_body'].style.paddingTop = '50vh';
          let loadingContainer = document.createElement("div"); 
          Object.keys(%(attrs)s).forEach(function(cssKey) {loadingContainer.style[cssKey] = %(attrs)s[cssKey]});
          let loadingLabel = document.createElement("div");
          loadingLabel.style["display"] = "inline-block";
          loadingLabel.innerHTML = %(label)s; 
          loadingContainer.innerHTML = '%(icon)s';
          loadingContainer.appendChild(loadingLabel);
          window['popup_loading_body'].appendChild(loadingContainer);
          document.body.appendChild(window['popup_loading_body'])
        } ''' % {"z_index": z_index, "background": self.page.theme.notch(),
                 "label": JsUtils.jsConvertData(label, None), "attrs": attrs, "icon": component.html()}

        return '''if (typeof window['popup_loading_body'] !== 'undefined'){
document.body.removeChild(window['popup_loading_body']); window['popup_loading_body'] = undefined}'''

    def add_template(self, css: dict = None, defined_style: str = None):
        """Add an extra layer.

        Usage::

          page = pk.Page()
          template = page.body.add_template(defined_style="margins")
          template.style.css.background = "white"

          page.body.add_template(css={"background": "white"}, defined_style="doc")

        :param css: Optional. The CSS attributes to be added to the HTML component
        :param defined_style: Optional. A predefined style attached to the style property
        """
        if css is not None:
            self.template.css(css)
        if defined_style is not None:
            getattr(self.template.style.configs, defined_style)()
        return self._template

    @property
    def template(self):
        """Shortcut to the body template component.

        This will just be an intermediate div tag on which all the component will be attached.

        Usage::

          page = pk.Page()
          page.body.template.margins(5)
          page.body.template.style.css.background = "white"

          # Add a predefined template
          page.body.template.style.configs.doc(max_width=900, background="white")
        """
        if self._template is None:
            self.header = self.page.ui.div()
            self.header.options.managed = False
            self.header.style.clear_all()
            self.footer = self.page.ui.div()
            self.footer.options.managed = False
            self.footer.style.clear_all()
            self._template = self.page.ui.div()
            self._template.options.managed = False
            self._template.style.clear_all()
        return self._template

    def add_header(self, components: Html, **kwargs):
        """Add a header to the page.

        :param components:
        """
        self.header = self.page.ui.div(components, tag="header", **kwargs)
        return self.header

    def add_footer(self, components: Html, **kwargs):
        """Add a footer to the page.

        :param components:
        """
        self.footer = self.page.ui.div(components, tag="footer", **kwargs)
        return self.footer

    def __str__(self):
        if getattr(self, '_template', None) is not None:
            self._template._vals = str(self._html_content)
            return '<body %s>%s%s%s</body>' % (
                self.get_attrs(
                    css_class_names=self.style.get_classes(), with_id=False), self.header.html(), self.template.html(),
                self.footer.html())

        return '<%s %s>\n%s\n</%s>' % (self.tag,
            self.get_attrs(css_class_names=self.style.get_classes(), with_id=False), self._html_content, self.tag)


class Component(Html):
    """Component interface.

    This is the main interface to create bridges to external Web frameworks.

    The default self.style, self.options and self.js properties can be overridden in order to respectively set the
    styles, the options and the event API of the component.

    With:
      - css_classes: List. Optional. The component classes.
      - str_repr String. Mandatory. The component HTML definition.
      - dyn_repr String. Optional. The sub items HTML definition.
    """
    css_classes: Optional[List] = None
    str_repr = None
    dyn_repr = None

    def __init__(self, page: primitives.PageModel, vals, html_code: Optional[str] = None,
                 options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None,
                 css_attrs: Optional[dict] = None, verbose: bool = False):
        super(Component, self).__init__(page, vals, html_code, options, profile, css_attrs, verbose=verbose)
        self.style.clear_style(persist_attrs=css_attrs)  # Clear all default CSS styles.
        if self.css_classes is not None:
            self.add_style(self.css_classes, clear_first=True, css_attrs=css_attrs, keep_css_keys=None)
        self.items = []

    @property
    def var(self) -> str:
        """Return the javaScript object reference after the builder. """
        return "window['%s']" % self.htmlCode

    def add_item(self, component: Union[Html, str]):
        """Add the sub item to the list of items.

        This will also add the component to the page component dictionary.

        :param component: The component
        """
        raise ValueError("Needs to be implemented")

    def write_item(self, item: primitives.HtmlModel) -> dict:
        """Write an item in the component. This function is call by the __str__ method for each item attached to the
        HTML component.

        This method return a dictionary which will be directly used to define the string set in self.dyn_repr.
        If this string framework is not defined this method will not be called.

        .. tip::

          If more interaction is needed between the component for the writing of the component, this should not be done
          in self.dyn_repr but the full logic can be implemented in the write_values method. In this case does not need to
          be defined.

        :param item: The item added to the self.items
        """
        return {"sub_item": item.html()}

    def write_values(self) -> dict:
        """Prepare the data to be written to the self.str_repr module variable.

        The keys {attrs} and {htmlCode} will be automatically added by the core framework.

        By default this function will add the values defined for the component to the {text} key.
        """
        return {"text": self._vals}

    def __str__(self):
        values = self.write_values()
        values["attrs"] = self.get_attrs(css_class_names=self.style.get_classes())
        values["htmlCode"] = self.htmlCode
        if self.dyn_repr is not None:
            str_frgs = [self.dyn_repr.format(**self.write_item(item)) for item in self.items]
            values["sub_items"] = "".join(str_frgs)
        if self._js__builder__ is not None:
            self.page.properties.js.add_builders(self.refresh())
        return self.str_repr.format(**values)


class StructComponent(Html):
    """Component interface.

    This is the main interface to create bridges to external Web frameworks.

    The default self.style, self.options and self.js properties can be overridden in order to respectively set the
    styles, the options and the event API of the component.

    With:
      - css_classes: List. Optional. The component classes.
      - str_repr String. Mandatory. The component HTML definition.
    """

    css_classes: Optional[List] = None
    str_repr = None

    def __init__(self, page: primitives.PageModel, vals, html_code: Optional[str] = None,
                 options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None,
                 css_attrs: Optional[dict] = None, verbose: bool = False):
        super(StructComponent, self).__init__(page, vals, html_code, options, profile, css_attrs, verbose=verbose)
        if self.css_classes is not None:
            self.add_style(self.css_classes, clear_first=True)
        self.items = {}

    def add_to(self, group: str, content: Union[Html, str]):
        """Add subcomponent to the main component.

        :param group: The category for the component
        :param content: The HTML component to be added
        """
        if not hasattr(content, "options"):
            content = self.page.web.std.div(content)
            content.style.clear_all(no_default=True)
            content.options.managed = False
        self.items.setdefault(group, []).append(content)
        return content

    def write_values(self):
        """Prepare the data to be written to the self.str_repr module variable.

        The keys {attrs} and {htmlCode} will be automatically added by the core framework.

        By default this function will add the values defined for the component to the {text} key.
        """
        raise ValueError("Method write_values must be defined")

    def __str__(self):
        values = self.write_values()
        values["attrs"] = self.get_attrs(css_class_names=self.style.get_classes())
        values["htmlCode"] = self.htmlCode
        if self._js__builder__ is not None:
            self.page.properties.js.add_builders(self.refresh())
        return self.str_repr.format(**values)
