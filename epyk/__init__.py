import inspect
import json

from typing import List, Union
from epyk.core import Page as Rpt
from epyk._version import __version__
from epyk.core.data import events
from epyk.core.data import configs
from epyk.core.data import datamap as js_datamap
from epyk.core.data import components as inputs
from epyk.core.data import DataPy as transforms

from epyk.core.html import Defaults as settings
from epyk.core.html.symboles import Symboles as symboles
from epyk.core.html.Standalone import Component as standalone
from epyk.core.html.Standalone import Resources as resources

from epyk.core.css import themes
from epyk.core.css import Defaults as settings_css
from epyk.core.css.Icons import get_icon, defined_icons, set_family
from epyk.core.css import Colors as colors, scss_colors, scss_icons, css_files_loader, export_scss_files
from epyk.core.css.themes import palettes, add_themes, set_theme, Theme, get_themes, get_theme
from epyk.core.css.themes.Theme import Theme
from epyk.core.css.styles.attributes import CssInline

# Add JavaScript shortcuts
from epyk.core.js import std as js_std
from epyk.core.js import expr as js_expr
from epyk.core.js import libs as js_libs
from epyk.core.js.JsUtils import jsWrap as js_callback, urlInputs as url_input

from epyk.core.js.Imports import Package as package, save_resources, string_to_base64
from epyk.core.js.Imports import PACKAGE_STATUS, JS_IMPORTS, CSS_IMPORTS

from epyk.core.js.treemap import add as treemap_add

#
from epyk.core.py.PyRest import PyRest as rest
from epyk.web import jupyter, npm, react, angular, svelte, vue

# Attach the generic data transforms
from epyk.core.data import DataCore
aggs = DataCore.DataAggregators()
"""JavaScript data aggregators"""
fltrs = DataCore.DataFilters()
"""JavaScript data filters"""
Page = Rpt.Report
"""Shortcut to standard dashboard features """
LOG_SERVICE = None
""" """


def css_inline(attrs: dict = None) -> CssInline:
    """Create a CSS Inline style.

    Usage::

      # Create the inline style
      css = pk.css_inline()
      css.color = "red"

      page = pk.Page()
      # Attach the class to your page
      css.define_class("textColor", page)

    :param attrs: Init CSS attributes
    """
    css_obj = CssInline()
    if attrs is not None:
        css_obj.css(attrs)
    return css_obj


def rename_css_cls(mappings: dict):
    """Change the name of the CSS classes in the framework.
    This function need to be used before the creation of any component in the page.

    This will not change the content. it will only rename them.
    To remove a CSS class or to change it in a component type have a look at components_skin

    :param dict mappings: The CSS class names to be renamed
    """
    from epyk.core.css import Classes

    Classes.OVERRIDES = mappings


def packages_black_list(pkgs_alias: List[str], raise_exception: bool = True):
    """All packages in this list will be considered as forbidden.
    The other packages will be authorised.

    :param pkgs_alias: A list of packages reference
    :param raise_exception: Optional. The kind of error triggered
    """
    global PACKAGE_STATUS

    for pkg in pkgs_alias:
        if raise_exception:
            PACKAGE_STATUS[pkg] = {"allowed": False}
        else:
            PACKAGE_STATUS[pkg] = {"allowed": True, "info": "Package in Black list"}


def packages_white_list(pkgs_alias: List[str], raise_exception: bool = True):
    """All packages not in those lists will be considered as forbidden.

    :param pkgs_alias: A list of packages reference
    :param raise_exception: Optional. The kind of error triggered
    """
    global PACKAGE_STATUS

    for js_pkg in JS_IMPORTS:
        if js_pkg in pkgs_alias:
            PACKAGE_STATUS[js_pkg] = {"allowed": True}
        else:
            if raise_exception:
                PACKAGE_STATUS[js_pkg] = {"allowed": False}
            else:
                PACKAGE_STATUS[js_pkg] = {"allowed": True, "info": "Missing from white list"}
    for css_pkg in CSS_IMPORTS:
        if css_pkg in pkgs_alias:
            PACKAGE_STATUS[css_pkg] = {"allowed": True}
        else:
            if raise_exception:
                PACKAGE_STATUS[css_pkg] = {"allowed": False}
            else:
                PACKAGE_STATUS[css_pkg] = {"allowed": True, "info": "Missing from white list"}


class Interface:
    """Quick interface for building dashboards.

    Usages::

      interf = pk.Interface(
        inputs=[
          {"type": "fields.date", "label": "test"},
          {"type": "fields.input", "label": "test"},
          {"type": "fields.toggle", "label": "test"},
          {"type": "fields.input", "label": "test"},
          {"type": "fields.slider", "label": "test"},
          {"type": "fields.toggle", "label": "test"},
          {"type": "fields.input", "label": "test"},
        ],
        outputs=[{"type": "lists.items", "options": {
              "checked_key": "selected",
              "items_type": "check",
              "text_click": True}
                  }],
        event={"url": "/autocomplete"},
        verbose=True,
        family="tui"
      )

    TODO add more components.

    :param inputs: The list of input components
    :param outputs: The list of input components
    :param event: The event definition
    :param verbose: Print further logs messages
    :param family: Set the web framework component family (default std components)
    :param run_label: Button's label text
    """

    def __init__(self, inputs: List[Union[str, dict]], outputs: List[Union[str, dict]] = None, event: dict = None,
                 verbose: bool = False, family: str = 'std', run_label: str = "Run"):
        self.page = Page()
        out_components, in_components = [], []
        ui_components = getattr(self.page.web, family)
        for i, inp in enumerate(inputs):
            component = self.__build_comp(inp, i, verbose=verbose, family=family)
            if component is not None:
                in_components.append(component)
            else:
                print("%s not defined" % inp)

        for j, out in enumerate(outputs, start=1):
            component = self.__build_comp(out, i + j, verbose=verbose, family=family)
            if component is not None:
                out_components.append(component)
            else:
                print("%s not defined" % out)

        if event is not None:
            btn = ui_components.button(run_label, align="center", options={"colored": True})
            btn.style.css.margin_top = 10
            btn.style.css.padding_top = "5px"
            btn.style.css.padding_bottom = "5px"
            btn.style.css.padding_left = "20px"
            btn.style.css.padding_right = "20px"
            inputs_comps = []
            for comp in in_components:
                if hasattr(comp, 'input'):
                    inputs_comps.append(getattr(comp, 'input'))
                else:
                    inputs_comps.append(comp)
            if len(out_components) == 1:
                btn.click(
                    getattr(self.page.js, event.get("method", "get").lower())(event["url"],
                                                                              components=inputs_comps).onSuccess([
                        out_components[0].build(events.data)
                    ]))
            else:
                btn.click(
                    getattr(self.page.js, event.get("method", "get").lower())(
                        event["url"], components=inputs_comps).onSuccess([
                        self.page.js.if_(events.data.has_key(comp.html_code), [
                            comp.build(events.data[comp.html_code])]) for comp in out_components
                    ]))
            in_components.append(btn)
        self.page.ui.row([in_components, out_components], position="top")

    def __build_comp(self, inp: Union[str, dict], i: int = None, verbose: bool = False, family: str = 'std'):
        """ Internal private method to build the dashboard. """
        comp = None
        pos = getattr(self.page.web, family)
        pos_std = self.page.web.std
        if isinstance(inp, dict):
            is_valid = True
            for frg in inp["type"].split("."):
                if hasattr(pos, frg):
                    pos = getattr(pos, frg)
                else:
                    is_valid = False
                    break

            if not is_valid:
                is_valid = True
                pos = pos_std
                for frg in inp["type"].split("."):
                    if hasattr(pos, frg):
                        pos = getattr(pos, frg)
                    else:
                        is_valid = False
                        break

            if is_valid:
                pmts = {}
                funcs_args = inspect.getfullargspec(pos)[0][1:]
                if verbose:
                    print("%s got arguments %s" % (pos.__name__, funcs_args))
                for arg_name in funcs_args:
                    if arg_name in inp:
                        pmts[arg_name] = inp[arg_name]
                if "html_code" not in pmts:
                    pmts["html_code"] = "comp_%s" % i
                comp = pos(**pmts)
                if 'css' in inp:
                    comp.css(inp["css"])
                if 'class' in inp:
                    comp["attr"]["class"].add(inp["class"])
        else:
            is_valid = True
            for frg in inp.split("."):
                if hasattr(pos, frg):
                    pos = getattr(pos, frg)
                else:
                    is_valid = False
                    break

            if not is_valid:
                is_valid = True
                pos = pos_std
                for frg in inp.split("."):
                    if hasattr(pos, frg):
                        pos = getattr(pos, frg)
                    else:
                        is_valid = False
                        break

            if is_valid:
                comp = pos(html_code="comp_%s" % i)
        return comp

    def launch(self, force_jupyter: bool = False, lab: bool = False):
        """
        Render either the HTML content or the Jupyter results.

        :param force_jupyter:
        :param lab:
        """
        if jupyter.is_notebook() or force_jupyter:
            if lab:
                return self.page.outs.jupyterlab()

            return self.page.outs.jupyter(closure=False)

        return self.page.outs.html()


MAP_FIELDS = {
    "div": {"values": "components"},
    "row": {"values": "components"},
    "button": {"value": "text"},
    "colored": {"value": "text"},
    "text": {"value": "text"},
    "bar": {"y": "y_columns", "x": "x_axis"},
    "line": {"y": "y_columns", "x": "x_axis"},
    "pie": {"y": "y_columns", "x": "x_axis"},
}


def from_json_to_html(content: dict, page: Rpt = None):
    if page is None:
        page = Page()
    components = content["components"] if "components" in content else content
    for alias, component in components.items():
        comp_type = component.get("type", alias)
        comp_category = component.get("category")
        comp_family = component.get("family", "ui")
        comp_library = component.get("library")
        component["html_code"] = alias
        ui_age = getattr(page, comp_family)
        if comp_category is not None:
            ui_age = getattr(ui_age, comp_category)
        if comp_library is not None:
            ui_age = getattr(ui_age, comp_library)
        ui_component_cls = getattr(ui_age, comp_type)
        funcs_args = inspect.getfullargspec(ui_component_cls)[0][1:]
        pmts = {}
        for field, mapped_field in MAP_FIELDS.get(comp_type, {}).items():
            if field in component:
                component[mapped_field] = component[field]
                del component[field]

        if comp_type in ["div", "row"]:
            values = []
            for val in component["components"]:
                if val in page.components:
                    values.append(page.components[val])
                else:
                    values.append(val)
            component["components"] = values
        for arg_name in funcs_args:
            if arg_name in component:
                pmts[arg_name] = component[arg_name]
        ui_component = ui_component_cls(**pmts)
        if 'css' in component:
            ui_component.css(component["css"])
        if "style" in component:
            if "theme" in component["style"]:
                ui_component.style.theme(component["style"]["theme"])
        if 'class' in component:
            ui_component["attr"]["class"].add(component["class"])
    # Second loop to add the events
    event_count = 1
    for alias, component in components.items():
        for event, event_details in component.get("events", {}).items():
            event_frgs = []
            if "print" in event_details:
                if event_details["print"] in page.components:
                    event_frgs.append(page.js.alert(page.components[event_details["print"]].dom.content))
                else:
                    event_frgs.append(page.js.alert(event_details["print"]))
            if "console" in event_details:
                if event_details["console"] == "event":
                    event_frgs.append(page.js.console.log(events.event))
                elif event_details["console"] == "data":
                    event_frgs.append(page.js.console.log(events.data))
                else:
                    event_frgs.append(page.js.console.log(event_details["console"]))
            for target_alias, target_value in event_details.get("targets", {}).items():
                if isinstance(target_value, dict):
                    event_frgs.append(page.components[target_alias].build(events.data[target_value["field"]]))
                elif target_value in page.components:
                    event_frgs.append(page.components[target_alias].build(page.components[target_value].dom.content))
                else:
                    event_frgs.append(page.components[target_alias].build(target_value))
            if hasattr(page.components[alias], event):
                if "url" in event_details:
                    query_inputs, query_data = None, {}
                    if "inputs" in event_details:
                        query_inputs = []
                        for query_alias in event_details["inputs"]:
                            if isinstance(query_alias, dict):
                                for k, v in query_alias.items():
                                    if isinstance(v, dict):
                                        if "type" in v and k in page.components:
                                            if "transform" in v:
                                                if v["transform"] == 'stringify':
                                                    query_data[k] = page.js.json.stringify(
                                                        getattr(page.components[k].dom, v["type"])())
                                            else:
                                                query_data[k] = getattr(page.components[k].dom, v["type"])()
                                    else:
                                        query_inputs.append((page.components[k], v))
                                        # query_inputs.append((v, page.components[k]))
                            else:
                                query_inputs.append(page.components[query_alias])
                    url_method = event_details.get("method", 'post').lower()
                    for data in event_details.get("data", []):
                        if isinstance(data, dict):
                            for k, v in data.items():
                                if isinstance(v, dict):
                                    if "type" in v and k in page.components:
                                        if "transform" in v:
                                            if v["transform"] == 'stringify':
                                                query_data[k] = page.js.json.stringify(
                                                    getattr(page.components[k].dom, v["type"])())
                                        else:
                                            query_data[k] = getattr(page.components[k].dom, v["type"])()
                                else:
                                    query_data[k] = v
                    getattr(page.components[alias], event)([
                        page.js.rest(url_method, url=event_details["url"], data=query_data or None,
                                     components=query_inputs,
                                     js_code="response%s" % event_count, headers={'Access-Control-Allow-Origin': '*'},
                                     stringify=event_details.get("json", True)  # default use json
                                     ).onSuccess(event_frgs)])
                    event_count += 1
                else:
                    getattr(page.components[alias], event)(event_frgs)
            else:
                if "url" in event_details:
                    query_inputs = None
                    if "inputs" in event_details:
                        query_inputs = []
                        for query_alias in event_details["inputs"]:
                            if isinstance(query_alias, dict):
                                for k, v in query_alias.items():
                                    query_inputs.append((v, page.components[k]))
                            else:
                                query_inputs.append(page.components[query_alias])
                    url_method = event_details.get("method", 'post').lower()
                    page.components[alias].on(
                        page.js.rest(url_method)(event_details["url"]).onSuccess(event_frgs))
                else:
                    page.components[alias].on(event, event_frgs)

    if "body" in content:
        if "css" in content["body"]:
            page.body.css(content["body"]["css"])
    return page
