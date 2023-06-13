import re
from pathlib import Path
from typing import Optional, List, Tuple, Any
from epyk.core.py import primitives, types

from epyk.core.html.Html import Html
from epyk.core.html.options import OptionsWithTemplates
from epyk.core.html.mixins import MixHtmlState

from epyk.core.js import JsUtils
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.html import JsHtml
from epyk.core.js.packages import JsPackage


class DomComponent(JsHtml.JsHtml):

    @property
    def container(self):
        """ Get the DOM container created by the process """
        return JsNodeDom.JsDoms.get('document.querySelector("#%s").closest("div[name=%s]")' % (
            self.component.html_code, self.component.selector))

    @property
    def element(self):
        """ Return always the real DOM element. """
        return JsNodeDom.JsDoms.get("document.getElementById('%s')" % self.component.html_code)

    @property
    def content(self) -> JsHtml.ContentFormatters:
        """ Get the component content. """
        return JsHtml.ContentFormatters(self.page, "(function(){if(%(object)s.value != undefined){return %(object)s.value()} else {return %(code)s.innerHTML}})()" % {
            "object": self.component.js.objectId, "code": self.varName})

    @property
    def lastChild(self):
        """ Get the last child from the component container """
        return JsNodeDom.JsDoms.get("document.getElementById('%s').lastChild" % self.component.html_code)

    def get_child_by_tag(self, tag: str):
        """
        Get a child by tag from the component container

        Usage::

            page.onDOMContentLoaded([
                page.js.console.log(comp.dom.get_child_by_tag("div[name=label]"))])

        :param tag: The tag definition
        """
        return JsNodeDom.JsDoms.get("document.querySelector('#%s').closest('div[name=%s]').querySelector(%s)" % (
            self.component.html_code, self.component.selector, JsUtils.jsConvertData(tag, None)))

    def querySelector(self, tag):
        """
        Get the dom based on a specific tag.

        Usage::

            ...

        :param tag: The specific tag
        """
        return JsNodeDom.JsDoms.get(tag)


class JsComponents(JsPackage):

    def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
                 is_py_data: bool = True, page: primitives.PageModel = None):
        self.varName, self.varData, self.__var_def = js_code, "", None
        self.component, self.page = component, page
        self._js, self._jquery = [], None

    @property
    def objectId(self) -> str:
        """ JavaScript underlying object reference (Proxy Js class) """
        return "window['%s']" % self.component.html_code

    def build(self, data: types.JS_DATA_TYPES, options: types.JS_DATA_TYPES = None):
        """

        :param data: Optional. Component data
        :param options: Optional. Specific Python options available for this component
        """
        return JsObjects.JsObject.JsObject.get("%s.build(%s, %s)" % (
            self.varName, JsUtils.jsConvertData(data, None), JsUtils.jsConvertData(options or {}, None)))

    def empty(self, options: types.JS_DATA_TYPES = None):
        """
        Empty the content of the container.

        This will call the underlying empty function which must be defined in the JavaScript component.

        :param options: Optional. Specific Python options available for this component
        """
        return JsObjects.JsObject.JsObject.get("%s.empty(%s)" % (
            self.varName, JsUtils.jsConvertData(options, None)))

    def custom(self, func_name: str, **kwargs):
        """
        Map a custom method not yet defined in the Python schema.

        This will accept also any kwargs in order to pass this to the JavaScript underlying method.

        Usage::

            # JavaScript side
            Component.prototype.testFnc = function(data){ console.log(data) }

            # Python

        :param func_name: The function name
        """
        _args = ["%s=%s" % (k, JsUtils.jsConvertData(v, None)) for k, v in kwargs.items()]
        return JsObjects.JsObject.JsObject.get("%s.%s(%s)" % (self.varName, func_name, ", ".join(_args)))


class SdOptions(OptionsWithTemplates):

    @property
    def container(self):
        """ Button category to specify the style. """
        return self.get({"display": "inline-block"})

    @container.setter
    def container(self, values: dict):
        self.set(values)

    def for_construct(self, values: dict):
        """
        Set of options used to build the components (on the HTML side).
        Those options will mainly remain on the Python side to decide the component structure.

        :param values: A dictionary of options
        :return: The underlying component for chaining
        """
        for k, v in values.items():
            self.attr(v, k)
        return self.component

    def for_build(self, values: dict, js_keys: List[str] = None):
        """
        Set of options passed to the JavaScript layer to build / update the component.

        :param values: The dictionary to be passed to the JavaScript layer within the builder
        :param js_keys: The list of keys coming from JavaScript
        :return: The underlying component for chaining
        """
        for k, v in values.items():
            if js_keys is not None:
                self._config(v, k, js_type=k in js_keys)
            else:
                self._config(v, k, js_type=False)
        return self.component


class Component(MixHtmlState.HtmlOverlayStates, Html):
    """
    A Standalone component class must be an interface which will link Python functions to
        - A JavaScript class
        - A set of CSS specific styles
        - An HTML structure

    JavaScript script must of the name of the Python class which will inherit from Component.
    The HtML structure should container the variable {{ attrs }} to set the CSS and the html_id of the main dom object.

    It is also possible to use {{ htmlCode }} or to create specific variables using the prepare method.
    """
    standalone: bool = True

    selector: str
    requirements: Tuple[str]
    style_urls: List[str] = None

    component_url: str = None
    # The template definition (either a string or a url)
    template_url: str = None
    template: str = None

    _option_cls = SdOptions

    def __init__(self, page: primitives.PageModel, vals: Any = None, html_code: Optional[str] = None,
                 options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None,
                 css_attrs: Optional[dict] = None):
        if self.selector is None:
            raise ValueError("selector must be defined for a standalone component")

        super(Component, self).__init__(page, vals, html_code, options, profile, css_attrs)
        self.style.clear_style(persist_attrs=css_attrs)  # Clear all default CSS styles.
        self.style.no_class()  # Clear all default CSS Classes.
        self.items, self.__metadata = [], {}

    @property
    def options(self) -> SdOptions:
        """ Property to set all the possible object for a standalone component. """
        return super().options

    @property
    def dom(self) -> DomComponent:
        """
        Return all the Javascript functions defined for an HTML Component.

        Those functions will use plain javascript available for a DOM element by default.

        Usage::

            page.onDOMContentLoaded([
                comp.dom.container.lastChild.css({"border": "1px solid red"}),
                comp.dom.container.child(1).css({"color": "blue"})
            ])

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = DomComponent(component=self, page=self.page)
        return self._dom

    @property
    def js(self) -> JsComponents:
        """
        The Javascript functions defined for this component.

        Those can be specific ones for the module or generic ones from the language.

        :return: A Javascript Dom object.
        """
        if self._js is None:
            self._js = JsComponents(self, page=self.page, js_code=self.html_code)
        return self._js

    def build(self, data: types.JS_DATA_TYPES = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None, component_id: Optional[str] = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """
        Return the JavaScript fragment to refresh the component content.

        Usage::

          dt = page.ui.rich.update()
          page.ui.button("Update").click([dt.refresh()])

        :param data: Optional. Component data
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The object reference ID
        :param stop_state:
        :param dataflows: Chain of data transformations
        """
        # check if there is no nested HTML components in the data
        if isinstance(data, dict):
            tmp_data = ["%s: %s" % (JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)) for k, v in
                        data.items()]
            js_data = "{%s}" % ",".join(tmp_data)
        else:
            js_data = JsUtils.dataFlows(data, dataflows, self.page)
        if hasattr(data, "toStr"):
            js_data = JsUtils.jsWrap(js_data)
        fnc_call = self.js.build(js_data, self.options.config_js(options))
        if stop_state:
            fnc_call = "%s;%s" % (fnc_call, self.hide_state(component_id))
        profile = self.with_profile(profile, event="Builder")
        if profile:
            fnc_call = ["var result = %s" % self.js.build(js_data, self.options.config_js(options))]
            fnc_call = "(function(data, options){%s; return result})(%s, %s)" % (
                fnc_call, js_data, self.options.config_js(options))
        return self.page.js.console.tryCatch(fnc_call, self.error(
            JsUtils.jsWrap("err"), label="`<i class='fas fa-exclamation-triangle' style='margin-right:5px;color:red'></i>Error during the processing: <b>${err}</b>`"), profile=profile)

    def child_event(
            self, event: str, tag: str, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
            on_ready: bool = False):
        """
        Add an event on a specific child for a given component.

        Usage::

            comp = page.ui.component("test-color")
            comp.prepare(text="Test")
            comp.child_event("click", "div[name=label]", [comp.build("test")])

        :param event: The event types
        :param tag: The source component tag name within the component
        :param js_funcs: Javascript function to be added once the object is built
        :param profile: Optional. A flag to set the component performance storage
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        return self.on(
            event, js_funcs=js_funcs, profile=profile,
            source_event=self.dom.get_child_by_tag(tag).toStr(),
            on_ready=on_ready)

    def prepare(self, **kwargs):
        """
        Prepare the data to be written to the html template.

        The keys {attrs} and {htmlCode} will be automatically added by the core framework.

        By default this function will add the values defined for the component to the {text} key.

        Usage::

            comp = page.ui.component("test-color")
            comp.prepare(text="Test")
        """
        self.__metadata = dict(kwargs)
        return self

    def __str__(self):
        if self.component_url is not None:
            if Path(self.component_url).exists():
                self.page.js.customFile(self.component_url, absolute_path=True, authorize=True)
                self.page.properties.js.add_builders([
                    "%s = new %s(%s, initValue=%s, options=%s)" % (
                        self.js.objectId, self.__class__.__name__, self.dom.varId,
                        JsUtils.jsConvertData(self._vals, None), self.options.config_js())])
            else:
                raise ValueError("Component file was not loaded correctly")

        if self.style_urls is not None:
            regex = re.compile(r"([A-Za-z0-9\.,\-\=\"'\[\]]*) {([#A-Za-z0-9\ \:\;\-]*) }")
            for css_file in self.style_urls:
                if Path(css_file).exists():
                    if css_file.endswith(".css"):
                        with open(css_file) as fp:
                            css_data = " ".join([line.strip() for line in fp])
                            for k, v in self.page.theme.all().items():
                                css_data = css_data.replace("$%s" % k, v)
                            css_formatted = []
                            for m  in regex.findall(css_data):
                                css_formatted.append("div[name=%s] > %s { %s }" % (self.selector, m[0], m[1]))
                            self.page.properties.css.add_text(" ".join(css_formatted))
                    else:
                        raise ValueError("CSS file format not supported only (.css and .scss)" % css_file)

                else:
                    for k, v in self.page.theme.all().items():
                        css_file = css_file.replace("$%s" % k, v)
                    css_formatted = []
                    for m  in regex.findall(css_data):
                        css_formatted.append("div[name=%s] > %s { %s }" % (self.selector, m[0], m[1]))
                    self.page.properties.css.add_text(" ".join(css_formatted))
        values = dict(self.__metadata)
        values["attrsOnly"] = self.get_attrs(css_class_names=self.style.get_classes(), with_id=False)
        values["attrs"] = self.get_attrs(css_class_names=self.style.get_classes())
        values["htmlCode"] = self.htmlCode
        if self.template_url and self.template is None:
            template_path = Path(self.template_url)
            if Path(template_path).exists():
                with open(self.template_url) as fp:
                    self.template = fp.read()
            else:
                raise ValueError("template_url: %s does not exist" % self.template_url)

        if self.template is None:
            raise ValueError("Missing template definition")

        template = self.template
        regex_tplm = re.compile(r"{{([a-zA-Z_\.\ 0-9]*)}}")
        for m in regex_tplm.findall(template):
            template = template.replace("{{%s}}" % m, str(values[m.strip()]))
        return "<div name='%s' style='%s'>%s</div>" % (
            self.selector,
            ";".join(["%s:%s" % (k, v) for k, v in self.options.container.items()]),
            template)
