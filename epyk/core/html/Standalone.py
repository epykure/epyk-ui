import json
import logging
from pathlib import Path
from typing import Optional, List, Tuple, Any, Dict, Union
from epyk.core.py import primitives, types

from epyk.core.html import html_template_loader, html_formatter
from epyk.core.html.Html import Html
from epyk.core.html.options import OptionsWithTemplates
from epyk.core.html.mixins import MixHtmlState

from epyk.core.css import css_files_loader

from epyk.core.js import JsUtils
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.html import JsHtml
from epyk.core.js.packages import JsPackage


def resolve_attributes(attributes: list, result: dict = None):
    """
    Convert initial options defined in the component.json structure file to valid
    attributes automatically loaded by the Python.

    Component must have the below structure in the json component file:

        "attributes": [
        {
          "name": "type",
          "value": "line"
        },
        {
          "name": "option",
          "values": [
            {
              "name": "responsive",
              "value": true
            }
          ]
        ...

    :param attributes: Component's attributes
    :param result: Resolved attributes
    """
    for attr in attributes:
        if "values" in attr:
            if isinstance(attr["values"][0], dict):
                result[attr["name"]] = {}
                resolve_attributes(attr["values"], result[attr["name"]])
            else:
                result[attr["name"]] = attr["values"]
        else:
            result[attr["name"]] = attr["value"]


def load_component(component_path: Path, raise_exception: bool = True) -> dict:
    """
    Load a component from the static file definition.

    Component folder structure:

        /<folder_name>
            - component.json
            - <selector>.css
            - <selector>.html
            - <selector>.js

    :param component_path: The root path for the component definition
    :param raise_exception: Flag to stop the process and raise an exception
    """
    if component_path.is_dir():
        component_config_path = Path(component_path, "component.json")
        if not component_config_path.exists():
            if raise_exception:
                raise ValueError("Component file does not exist: %s" % component_path)

            logging.error("Component file does not exist: %s" % component_path)
            return {}

        with open(component_config_path) as fp:
            content = json.load(fp)
            component_attrs = {}
            resolve_attributes(content.get("attributes", []), component_attrs)
            for prop, f_type in [
                ("component_url", "js"), ("style_urls", "css"), ("template_url", "html"),
                ("toml_directives_url", "toml")]:
                if prop not in content:
                    struct_name = "%s.%s" % (content["selector"], f_type)
                    struct_file = Path(component_path, struct_name)
                    if struct_file.exists():
                        if prop.endswith("s"):
                            content[prop] = [str(struct_file)]
                        else:
                            content[prop] = str(struct_file)
                else:
                    if prop.endswith("s"):
                        nf = []
                        for f in content[prop]:
                            fp = Path(f)
                            if not fp.exists():
                                nf.append(str(Path(component_path, fp)))
                            else:
                                nf.append(f)
                        content[prop] = nf
                    else:
                        fp = Path(content[prop])
                        if not fp.exists():
                            content[prop] = str(Path(component_path, fp))
            class_name = "".join(map(lambda x: x.capitalize(), content["selector"].split("-")))
            cls = type(class_name, (Component,), content)
            if "dependencies" in content:
                requirements = []
                for dep, dep_version in content["dependencies"].items():
                    if dep_version:
                        requirements.append((dep, dep_version))
                    else:
                        requirements.append(dep)
                cls.requirements = requirements
            cls.js_funcs_map = content.get("defined_functions", {})
            if "additional_functions" in content:
                cls_js = type(class_name, (JsComponents,), {})
                for add_func, func_prop in content["additional_functions"].items():
                    func_name = "%s%s" % (cls_js.__name__, add_func)
                    args, js_args = ["self"], []
                    for k, props in func_prop.get("properties", {}).items():
                        js_args.append(k)
                        if "default" in props:
                            args.append("%s=%s" % (k, props["default"]))
                        else:
                            args.append(k)
                    func_expr = '''
def %s(%s): 
    return JsObjects.JsObject.JsObject.get("%%s.%s({%%s})" %% (self.varName, ", ".join([
        "%%s: %%s" %% (k, JsUtils.jsConvertData(v, None)) for k, v in {%s}.items()])))''' % (
                        func_name, ",".join(args), add_func, ",".join(["'%s': %s" % (k, k) for k in js_args] ))
                    exec(func_expr.strip())
                    setattr(cls_js, add_func, eval(func_name))
                cls._def_js_cls = cls_js
            if component_attrs:
                cls._init__options = component_attrs
            return {"class": cls, "content": content}


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
        """ Get the component content. - can be overriden with js mapping value: getComponentValue() for instance """
        if "value" in self.component.js_funcs_map:
            return JsHtml.ContentFormatters(self.page, "%s.%s()" % (self.component.js.objectId, self.component.js_funcs_map["value"]))

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

    def querySelector(self, tag: str):
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

    def build(self, data: types.JS_DATA_TYPES, options: types.JS_DATA_TYPES = None, fnc: str = "build"):
        """

        :param data: Optional. Component data
        :param options: Optional. Specific Python options available for this component
        :param fnc: Optional. The underlying method used in the template
        """
        fnc = self.component.js_funcs_map.get(fnc, fnc)
        return JsObjects.JsObject.JsObject.get("%s.%s(%s, %s)" % (
            self.varName, fnc, JsUtils.jsConvertData(data, None), JsUtils.jsConvertData(options or {}, None)))

    def empty(self, options: types.JS_DATA_TYPES = None, fnc: str = "empty"):
        """
        Empty the content of the container.

        This will call the underlying empty function which must be defined in the JavaScript component.

        :param options: Optional. Specific Python options available for this component
        :param fnc: Optional. The underlying method used in the template
        """
        fnc = self.component.js_funcs_map.get(fnc, fnc)
        return JsObjects.JsObject.JsObject.get("%s.%s(%s)" % (
            self.varName, fnc, JsUtils.jsConvertData(options, None)))

    def set(self, data: types.JS_DATA_TYPES = None, options: types.JS_DATA_TYPES = None, fnc: str = "set"):
        """
        Set the content of the container.
        This method usually is used fto init / reset the component.

        This will call the underlying set function which must be defined in the JavaScript component.

        :param data: Optional. The value
        :param options: Optional. Specific Python options available for this component
        :param fnc: Optional. The underlying method used in the template
        """
        fnc = self.component.js_funcs_map.get(fnc, fnc)
        return JsObjects.JsObject.JsObject.get("%s.%s(%s, %s)" % (
            self.varName, fnc, JsUtils.jsConvertData(data, None),
            JsUtils.jsConvertData(options, None)))

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
            self.attr(k, v)
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

    JavaScript script must have the name of the Python class which will inherit from Component.
    The HtML structure should container the variable {{ attrs }} to set the CSS and the html_id of the main dom object.

    It is also possible to use {{ htmlCode }} or to create specific variables using the prepare method.
    """
    standalone: bool = True

    selector: str
    requirements: Tuple[str]
    used: Tuple[str] = None
    style_urls: List[str] = None

    component_url: str = None
    # The template definition (either a string or a url)
    template_url: str = None
    template: str = None

    # Structural directives to build template from Virtual DOM (or Python)
    toml_directives_url: str = None
    toml_directives: str = None

    _option_cls = SdOptions
    _init__options: dict = None

    js_funcs_map: dict = {}   # Internal mapping for Js functions
    _def_js_cls = JsComponents

    def __init__(self, page: primitives.PageModel, vals: Any = None, html_code: Optional[str] = None,
                 options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None,
                 css_attrs: Optional[dict] = None, verbose: bool = None, **kwargs):
        if self.selector is None:
            raise ValueError("selector must be defined for a standalone component")

        super(Component, self).__init__(page, vals, html_code, options, profile, css_attrs, verbose=verbose)
        self.style.clear_style(persist_attrs=css_attrs)  # Clear all default CSS styles.
        self.style.no_class()  # Clear all default CSS Classes.
        self.items, self.__metadata, self.__directives, self.__html_content = [], {}, None, None
        self.prepare(**kwargs)
        if self._init__options:
            self.options.for_construct(self._init__options)

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
            self._js = self._def_js_cls(self, page=self.page, js_code=self.html_code)
        return self._js

    @classmethod
    def directives(cls, framework: str = None) -> dict:
        """
        Load structure directives for the HTML templates

        :param framework: The JavaScript framework
        """
        framework = framework or "python"
        if cls.toml_directives_url is not None:
            try:
                import tomllib
                with open(cls.toml_directives_url, 'rb') as fp:
                    rules = tomllib.load(fp)
            except:
                return {}

        elif cls.toml_directives is not None:
            try:
                import tomllib
                rules = tomllib.loads(cls.toml_directives)
            except:
                return {}

        else:
            rules = {}
        directives = rules.get("epyk", {}).get("directives", {}).get(framework, {})
        if framework == "angular":
            directives["content"] = "<ng-content></ng-content>"
            for t in ["class", "style"]:
                if t not in directives:
                    directives[t] = ""
        return directives

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
        if hasattr(data, "toStr") and not hasattr(js_data, "toStr"):
            js_data = JsUtils.jsWrap(js_data)
        fnc_call = self.js.build(js_data, self.options.config_js(options))
        if stop_state:
            fnc_call = "%s;%s" % (fnc_call, self.hide_state(component_id))
        profile = self.with_profile(profile, event="Builder")
        if profile:
            fnc_call = "(function(data, options){var result = %s; return result})(%s, %s)" % (
                self.js.build(js_data, self.options.config_js(options)), js_data, self.options.config_js(options))
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

    def html_extension(self, html: str):
        """
        Update the HTML content of a component

        :param html: The HTML string expression
        """
        self.__html_content = str(html)

    def prepare(self, **kwargs):
        """
        Prepare the data to be written to the html template.

        The below keys will be automatically added by the core framework:
            {{ cssStyle }} - The CSS styles properties
            {{ cssClass }} - The CSS classes to be added to a DOM object
            {{ selector }} - The JavaScript / Python class name
            {{ attrs }} - The entire tags style, class and id + others
            {{ attrsOnly }} - The entire tags style, class + others (without ID)
            {{ id }} - The DOM id of the component
            {{ htmlCode }} - Same value than the id

        By default this function will add the values defined for the component to the {text} key.

        Usage::

            comp = page.ui.component("test-color")
            comp.prepare(text="Test")
        """
        self.__metadata = dict(kwargs)
        return self

    @classmethod
    def get_import(cls, path: str, suffix: str = "", root_path: Union[Path, str] = None, is_ts: bool = True) -> str:
        """
        Get the import statement to be added to a module.
        This would work with ts or js files.

        If the root_path of the application file is added, the process will check if the component file exists.

        :param path: The component file path
        :param suffix:Suffix import for Component or Modules derived from the core builder
        :param root_path: The application file path (within the app/ folder)
        :param is_ts: Flag to specify the file format (ts or js)
        """
        if root_path is not None:
            script_path = Path(root_path, "%s.%s" % (path, "ts" if is_ts else 'js'))
            if not script_path.exists():
                raise ValueError("Component script does not exist: %s" % script_path)

        return "import { %s%s } from '%s'" % (cls.__name__, suffix, path)

    def __str__(self):
        if self.component_url is not None:
            if Path(self.component_url).exists():
                component_path = Path(self.component_url)
                if component_path.is_absolute():
                    self.page.js.customFile(
                        component_path.name, path=component_path.parent.resolve(), absolute_path=True, authorize=True)
                else:
                    self.page.js.customFile(self.component_url, absolute_path=True, authorize=True)
                self.page.properties.js.add_builders([
                    "%s = new %s(%s, initValue=%s, options=%s)" % (
                        self.js.objectId, self.__class__.__name__, self.dom.varId,
                        JsUtils.jsConvertData(self._vals, None), self.options.config_attrs())])
            else:
                raise ValueError("Component file - %s - was not loaded correctly" % self.__class__.__name__)

        if self.style_urls is not None:
            css_content = css_files_loader(self.style_urls, self.selector, style_vars=self.page.theme.all())
            if css_content:
                self.page.properties.css.add_text(css_content, map_id=self.selector)

        values = dict(self.__metadata)
        # Set all the templates attributes
        values["cssStyle"] = ";".join(["%s:%s" % (key, val) for key, val in self.attr["css"].items()])
        values["cssClass"] = " ".join(self.attr["class"])
        values["selector"] = self.__class__.__name__.lower()
        values["attrsOnly"] = self.get_attrs(css_class_names=self.style.get_classes(), with_id=False)
        values["attrs"] = self.get_attrs(css_class_names=self.style.get_classes())
        values["htmlCode"] = self.htmlCode
        values["id"] = self.htmlCode
        directives = self.directives()
        directives["style"] = 'style="%s"' % values["cssStyle"]
        directives["class"] = 'class="%s"'  % values["cssClass"]
        if self.__html_content is not None:
            # Override the [content] section in the case of a standard Python web component
            directives["class"] = self.__html_content
        if self.template_url is not None:
            html_def = html_template_loader(
                self.template_url, values, ref_expr='id="{{ id }}"', directives=directives)
        elif self.template is not None:
            html_def = html_formatter(self.template, values, ref_expr='id="{{ id }}"', directives=directives)
        else:
            raise ValueError("Missing template definition")

        return "<div name='%s' style='%s'>%s</div>" % (
            self.selector,
            ";".join(["%s:%s" % (k, v) for k, v in self.options.container.items()]),
            html_def["template"])

    @staticmethod
    def from_json(path: Path, is_parent: bool = False, raise_exception: bool = False) -> Dict[Any, dict]:
        """
        Load component definition from a json configuration file.
        This can load a single component or all components within the folder using the parent flag.

        It is recommended to have each component definition segregated in a dedicated folder,

        :param path: Component(s) path
        :param is_parent: Flag to specify if the process will load multiple components
        :param raise_exception: Flag to raise an exception if component not loaded
        """
        components = {}
        if is_parent:
            for folder in Path(path).iterdir():
                result = load_component(folder, raise_exception=raise_exception)
                if result:
                    components[result["class"]] = result["content"]
        else:
            result = load_component(path, raise_exception=raise_exception)
            if result:
                components[result["class"]] = result["content"]
        return components
