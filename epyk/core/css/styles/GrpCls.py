#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging

from typing import Optional, List, Dict
from epyk.core.py import primitives

from epyk.core.css import Classes
from epyk.core.css import Defaults_css
from epyk.core.css import css_files_loader
from epyk.core.css import Properties
from epyk.core.css.styles.effects import Effects
from epyk.core.css.styles import GrpConfigs
from epyk.core.css.styles.attributes import Attrs  # for the rtype in the documentation
from epyk.core.css.styles.attributes import Commons, Body, Empty
from epyk.core.css.styles.classes import CssStyle, CssStyleScrollbar, CssStylesPage
from epyk.core.py import OrderedSet
from epyk.fwk.bs import CssClasses as BsCssClasses
from epyk.core.js.Imports import string_to_base64


class ClassPage:

    def __init__(self, component: primitives.HtmlModel = None, page: primitives.PageModel = None):
        self._css_struct, self._css_class = None, None
        self.component, self.page = component, page
        if component is not None:
            self.page = component.page
        self.__webkitscrollbar, self.__webkitscrollbar_track, self.__webkitscrollbar_thumb, self.__selection = 4 * [
            None]
        self.__contenteditable, self.__global_styles, self.__moz_selection = None, None, None
        self.classList, self.__cls_defined, self.__cls_catalog = {"main": OrderedSet(),
                                                                  'other': OrderedSet()}, None, None

    @property
    def css(self) -> Body:
        """ Property to the underlying CSS definition to be added to the style HTML tag of a component. """
        if self._css_struct is None:
            self._css_struct = Body(self.component, page=self.page)
        return self._css_struct

    @property
    def vars(self) -> str:
        """Return the CSS variables mappings for the loaded theme"""
        results = []
        if self.component.css_map_files:
            style_vars = self.page.theme.all()
            style_vars.update(self.page.body.style.globals.vars())
            for f in self.component.css_map_files:
                with open(f) as fp:
                    content = fp.read()
                    for k in sorted(style_vars, key=lambda k: len(k), reverse=True):
                        # Important to replace by starting with the longest string to avoid issues
                        content = content.replace("$%s" % k, style_vars[k])
                    results.append(content)
        return "".join(results)

    @property
    def css_class(self) -> Classes.CatalogDiv.CatalogDiv:
        """The internal class used to put a custom Style to this object.

        Only 1 CSS class can be added to an HTML object.
        """
        if self._css_class is None:
            self._css_class = Classes.CatalogDiv.CatalogDiv(
                self.page, self.classList['main'], html_id=self.component.html_code).no_border()
        return self._css_class

    @property
    def globals(self) -> Defaults_css.GlobalStyle:
        """Reference for all the global setting in the page.

        This should be changed in order to be the proxy to the Default CSS settings in the framework.
        Changing this should only impact the report default settings.

        TODO: Extend to more than the font
        """
        if self.__global_styles is None:
            self.__global_styles = Defaults_css.GlobalStyle(self.page)
        return self.__global_styles

    @property
    def scrollbar_webkit(self) -> CssStyleScrollbar.CssWebkitScrollbar:
        """Scrollbars predefined styles. """
        if not self.__webkitscrollbar:
            self.__webkitscrollbar = CssStyleScrollbar.CssWebkitScrollbar(self.page)
        return self.__webkitscrollbar

    @property
    def scrollbar_webkit_thumb(self) -> CssStyleScrollbar.CssWebkitScrollbarThumb:
        """Scrollbars predefined styles. """
        if not self.__webkitscrollbar_thumb:
            self.__webkitscrollbar_thumb = CssStyleScrollbar.CssWebkitScrollbarThumb(self.page)
        return self.__webkitscrollbar_thumb

    @property
    def scrollbar_webkit_track(self):
        """Scrollbars predefined styles. """
        if not self.__webkitscrollbar_track:
            self.__webkitscrollbar_track = CssStyleScrollbar.CssWebkitScrollbarTrack(self.page)
        return self.__webkitscrollbar_track

    @property
    def selection(self) -> CssStyleScrollbar.CssWebkitSelection:
        """Selection predefined style (background color based on the selected theme).

        Related Pages:

          https://www.w3schools.com/howto/howto_css_text_selection.asp
        """
        if not self.__selection:
            self.__selection = CssStyleScrollbar.CssWebkitSelection(self.page)
        return self.__selection

    @property
    def moz_selection(self) -> CssStyleScrollbar.CssWebkitMozSelection:
        """Selection predefined style (background color based on the selected theme).

        Related Pages:

          https://www.w3schools.com/howto/howto_css_text_selection.asp
        """
        if not self.__moz_selection:
            self.__moz_selection = CssStyleScrollbar.CssWebkitMozSelection(self.page)
        return self.__moz_selection

    def contenteditable(self) -> CssStylesPage.CssPageContentEditable:
        """Set the border color of the editable content according to the selected theme.

        Related Pages:

          https://www.w3schools.com/howto/howto_css_contenteditable_border.asp
        """
        if not self.__contenteditable:
            self.__contenteditable = CssStylesPage.CssPageContentEditable(self.page)
            self.classList['other'].add(self.__contenteditable)
        return self.__contenteditable

    def fit_screen_height(self, margin_size: int = None):
        """

        :param margin_size: Optional.
        """
        if margin_size is not None:
            self.component.page.properties.css.add_text(
                "body {height: calc(100%% - %spx)}" % margin_size)
        else:
            self.component.page.properties.css.add_text("body {height: 100%}")
        return self

    @property
    def defaults(self):
        """The Default CSS Attributes in the framework. """
        return Defaults_css

    @property
    def add_classes(self) -> Classes.Catalog:
        """Property to get access to the catalog of CSS classes to be added to the HTML class tag component. """
        if self.__cls_catalog is None:
            self.__cls_catalog = Classes.Catalog(self.page, self.classList)
        return self.__cls_catalog._class_type('main')

    @property
    def define_classes(self) -> Classes.Catalog:
        """Property to get access to the catalog of CSS classes to be loaded in the page.

        Those classes will not be automatically added to any HTML tag and they need to be added manually.
        """
        if self.__cls_catalog is None:
            self.__cls_catalog = Classes.Catalog(self.page, self.classList)
        return self.__cls_catalog._class_type('other')

    def get_classes(self):
        """Returns the list of Internal and bespoke classes to be added to the class HTML table on the component. """
        for css_cls in self.classList.values():
            for c in css_cls:
                if hasattr(c, 'get_ref'):
                    self.component.page._css[c.get_ref()] = str(c)
        return self.classList

    def get_classes_css(self):
        """Attach the predefined styles for the scrollbar and selection then return all the classes. """
        self.classList['other'].add(self.scrollbar_webkit)
        self.classList['other'].add(self.scrollbar_webkit_thumb)
        self.classList['other'].add(self.scrollbar_webkit_track)
        self.classList['other'].add(self.selection)
        self.classList['other'].add(self.moz_selection)

        css_frgs = {}
        for css_cls in self.classList.values():
            for c in css_cls:
                if hasattr(c, 'get_ref'):
                    css_frgs[c.get_ref()] = str(c)
        return css_frgs

    def custom_class(self, css_attrs: dict, classname: str = None, selector: str = None, is_class: bool = True,
                     important: bool = False) -> dict:
        """This will create dynamic CSS class which will not be added to any component.

        The class definition can then be reused in multiple components.
        The CSS style of the body can only be done using predefined classes or inline CSS.

        TODO: Enable the important for nested css_attrs.

        Usage::

          page.body.style.custom_class(css_attrs={"_attrs": {"fill": 'red'}}, classname='nvd3.nv-pie .nv-pie-title')

        :param css_attrs: Nested dictionary with the different attributes
        :param classname: Optional. The classname in the CSS definition
        :param selector: Optional. The class selector (if it is not a classname using . but a strict definition)
        :param is_class: Optional. Automatically transform the name to a CSS class definition by adding a dot
        :param important: Optional. Specify if the style is important
        """
        if classname is None:
            cls_def = {"classname": False, '_selector': selector}
        else:
            cls_def = {"classname": classname}
        if '_attrs' not in css_attrs and '_hover' not in css_attrs:
            if important:
                css_attrs = {k: "%s !IMPORTANT" % v for k, v in css_attrs.items()}
            css_attrs = {"_attrs": css_attrs}
        css_attrs['is_class'] = is_class
        cls_def.update(css_attrs)
        v_cls = type(classname, (CssStyle.Style,), cls_def)
        cls_obj = v_cls(self.page)
        self.classList['other'].add(cls_obj)
        return cls_def

    def add_stylesheet(self, css_files: List[str], title: str = "custom stylesheet"):
        """Add stylesheets to the style section of the page.

        :param css_files: List of CSS files to attach
        :param title: Style ID (used as reference for the set of CSS files to avoid adding them multiple times)
        """
        style_vars = self.page.theme.all()
        style_vars.update(self.page.body.style.globals.vars())
        css_content = css_files_loader(css_files, style_vars=style_vars)
        if css_content:
            self.page.body.set_css_maps(style_vars)
            self.page.properties.css.add_text(css_content, map_id=title)
        else:
            logging.warning("CSS | %s | Empty CSS for files: %s" % (title, css_files))


class ClassHtml:

    def __init__(self, component: primitives.HtmlModel = None, page: primitives.PageModel = None):
        self._css_struct, self._css_class = None, None
        self.component, self.page = component, page
        if component is not None:
            self.page = component.page
        self.classList, self.__cls_defined, self.__cls_catalog = {"main": OrderedSet(),
                                                                  'other': OrderedSet()}, None, None
        self.__cls_effects, self.__css_virtual = None, {}
        self.classList['main'].add(self.css_class)

    @property
    def varName(self) -> str:
        """Unique identifier for the CSS object on the Javascript side. """
        return "%s_css" % self.component.html_code

    @property
    def css(self) -> Commons:
        """Property to the underlying CSS definition to be added to the style HTML tag of a component. """
        if self._css_struct is None:
            self._css_struct = Commons(self.component)
        return self._css_struct

    @property
    def files(self) -> Optional[dict]:
        """Read / Only Internal files definition used to set the component styles"""
        if self.component.style_urls:
            return {str(fs): fs.exists() for fs in self.component.style_urls}

        return {}

    @property
    def raw(self)-> Optional[dict]:
        """Returns the raw CSS files definition for the component in a dictionary"""
        if self.component.style_urls:
            result = {}
            for fs in self.component.style_urls:
                if fs.exists():
                    with open(fs) as fp:
                        result[str(fs)] = fp.read()
            return result

        return {}

    @property
    def classes(self) -> Optional[dict]:
        """Predefined CSS Classes for the component.

        Usage::

            btns = page.ui.menus.buttons(["A", "B", "C", "D"], html_code="group")
            btns.style.classes_map({"html-button": "html-button-new", "Other": "test"}, replace=False)
        """
        if self.component.style_refs:
            return self.component.style_refs

        return {}

    def classes_map(self, ovrs: Dict[str, str], replace: bool = True):
        """Change the component pre defined classes

        Usage::

            btns = page.ui.menus.buttons(["A", "B", "C", "D"], html_code="group")
            btns.options.classes = ["html-button-new"]

        :param ovrs: Dictionary with the new class values
        :param replace: Change the style_refs definition for all components
        """
        if not replace:
            self.component.style_refs = dict(self.component.style_refs)
        for k, v in ovrs.items():
            if k not in self.component.style_refs:
                logging.warning("Style | GrpCls | Missing definition %s for in style_refs for %s" % (k, self.component.__class__.__name__))
            self.component.style_refs[k] = v

    def from_str(self, content: str, replace: bool = True, dsc: str = None):
        """Set new CSS content for a component.
        This will receive a string and it will create a base64 content added to the HTML page header.

        Usage::

            btns2 = page.ui.menus.buttons(html_code="group2")
            btns2.style.from_str('''.html-button-new {
                color: white; background-color: red ; border-color: red ; min-width: 80px ;}
            .html-button-new.selected {color: green;}
            ''')

        :param content: New CSS content
        :param replace: Replace the definition at class definition level
        :param dsc: content description to be added to the header
        """
        if replace:
            self.component.style_urls = None
        self.page.headers.links.stylesheet(
            "data:text/css;base64,%s" % string_to_base64(content), title=dsc or self.component.__class__.__name__)

    @property
    def css_class(self) -> Classes.CatalogDiv.CatalogDiv:
        """The internal class used to put a custom Style to this object. Only 1 CSS class can be added to an HTML object
        """
        if self._css_class is None:
            self._css_class = Classes.CatalogDiv.CatalogDiv(
                self.page, self.classList['main'], html_id=self.component.html_code).no_border()
        return self._css_class

    def shadows(self, num: int):
        """Shortcut to various shadow styles.

        Related Pages:

          https://getcssscan.com/css-box-shadow-examples

        :param num: The template number.
        """
        shadow_styles = {
            0: {"box-shadow": "rgba(149, 157, 165, 0.2) 0px 8px 24px"},
            1: {"box-shadow": "rgba(100, 100, 111, 0.2) 0px 7px 29px 0px"},
            2: {"box-shadow": "rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px"},
            3: {"box-shadow": "rgba(0, 0, 0, 0.35) 0px 5px 15px"},
            4: {"box-shadow": "rgba(0, 0, 0, 0.16) 0px 1px 4px"},
            5: {"box-shadow": "rgba(0, 0, 0, 0.24) 0px 3px 8px"},
            6: {"box-shadow": "rgba(99, 99, 99, 0.2) 0px 2px 8px 0px"},
            7: {"box-shadow": "rgba(0, 0, 0, 0.16) 0px 1px 4px, rgb(51, 51, 51) 0px 0px 0px 3px"},
            8: {"box-shadow": "rgba(0, 0, 0, 0.02) 0px 1px 3px 0px, rgba(27, 31, 35, 0.15) 0px 0px 0px 1px"},
            9: {"box-shadow": "rgba(0, 0, 0, 0.1) 0px 4px 12px"},
            10: {
                "box-shadow": "rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px"},
            11: {"box-shadow": "rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px"},
            12: {"box-shadow": "rgba(0, 0, 0, 0.16) 0px 10px 36px 0px, rgba(0, 0, 0, 0.06) 0px 0px 0px 1px"},
            13: {"box-shadow": "rgba(17, 12, 46, 0.15) 0px 48px 100px 0px"},
            14: {
                "box-shadow": "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset"},
            20: {"box-shadow": "rgb(38, 57, 77) 0px 20px 30px -10px"},
            30: {"box-shadow": "rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px"},
            43: {
                "box-shadow": "rgba(0, 0, 0, 0.07) 0px 1px 2px, rgba(0, 0, 0, 0.07) 0px 2px 4px, rgba(0, 0, 0, 0.07) 0px 4px 8px, rgba(0, 0, 0, 0.07) 0px 8px 16px, rgba(0, 0, 0, 0.07) 0px 16px 32px, rgba(0, 0, 0, 0.07) 0px 32px 64px"},
            55: {"box-shadow": "rgba(3, 102, 214, 0.3) 0px 0px 0px 3px"},
            57: {
                "box-shadow": "rgba(0, 0, 0, 0.2) 0px 12px 28px 0px, rgba(0, 0, 0, 0.1) 0px 2px 4px 0px, rgba(255, 255, 255, 0.05) 0px 0px 0px 1px inset"},
            60: {
                "box-shadow": "blue 0px 0px 0px 2px inset, rgb(255, 255, 255) 10px -10px 0px -3px, rgb(31, 193, 27) 10px -10px, rgb(255, 255, 255) 20px -20px 0px -3px, rgb(255, 217, 19) 20px -20px, rgb(255, 255, 255) 30px -30px 0px -3px, rgb(255, 156, 85) 30px -30px, rgb(255, 255, 255) 40px -40px 0px -3px, rgb(255, 85, 85) 40px -40px"},
            83: {"box-shadow": "rgba(0, 0, 0, 0.56) 0px 22px 70px 4px"},
        }
        self.component.css(shadow_styles[num])

    @property
    def configs(self) -> GrpConfigs.ClsConfigs:
        """All predefined CSS configurations."""
        return GrpConfigs.ClsConfigs(self.component)

    @property
    def defaults(self):
        """The Default CSS Attributes in the framework. """
        return Defaults_css

    @property
    def effects(self) -> Effects.Effects:
        """Add animation effect to the component based either on a bespoke definition or a predefined one."""
        if self.__cls_effects is None:
            self.__cls_effects = Effects.Effects(self.page, self.component)
        return self.__cls_effects

    @property
    def add_classes(self) -> Classes.Catalog:
        """Property to get access to the catalog of CSS classes to be added to the HTML class tag component."""
        if self.__cls_catalog is None:
            self.__cls_catalog = Classes.Catalog(self.page, self.classList)
        return self.__cls_catalog._class_type('main')

    @property
    def define_classes(self) -> Classes.Catalog:
        """Property to get access to the catalog of CSS classes to be loaded in the page.
        Those classes will not be automatically added to any HTML tag and they need to be added manually.
        """
        if self.__cls_catalog is None:
            self.__cls_catalog = Classes.Catalog(self.page, self.classList)
        return self.__cls_catalog._class_type('other')

    def add_class(self, name: str):
        """Add bespoke class to a component.

        Usage::

          page = pk.Page()
          page.properties.css.add_text('''
          .redCls {color: red}
          ''')
          text = page.ui.text("Hello World !")
          text.style.add_class("redCls")
          page.outs.html_file(name="test", print_paths=True)

        :param name: CSS Class name
        """
        self.classList['main'].add(name)

    def extend_class(self, names: List[str]):
        """Append classes to the class attribute.

        :param names: The CSS classes to be added to the main definition
        """
        if names:
            self.classList['main'].extend(names)

    def attr(self, key: str, name: str, dflt: Optional[str] = None, suffix: str = "temp"):
        """The attr() function returns the value of an attribute of the selected elements.

        Related Pages:

          https://www.w3schools.com/cssref/func_attr.asp

        :param key: The attribute key
        :param name: The attribute value
        :param dflt: Optional. The default value for the attribute
        :param suffix: Optional. The suffix for the attribute
        """
        key_selector = "_%s" % suffix
        if key_selector not in self.__css_virtual:
            self.__css_virtual[key_selector] = {}
        if dflt is not None:
            self.__css_virtual[key_selector].update({key: "attr(%s, %s)" % (name, dflt)})
        else:
            self.__css_virtual[key_selector].update({key: "attr(%s)" % name})

    def attr_content(self, name: str):
        """Use of the attr function for the before content value.
        This is the unique valid use of this CSS function in most of the browser.

        Related Pages:

          https://gomakethings.com/how-to-access-and-use-data-attributes-in-your-css/

        :param name: The attribute content name
        """
        self.attr("content", name, suffix='before')

    def hover(self, attrs: dict):
        """Add onmousever style.

        :param attrs: The CSS attributes for the mouse hover style
        """
        self.selector("hover", attrs)

    def standard(self, percent: int = 10, width_adj: bool = True):
        """

        :param percent: Optional. The percentage of space on the left and right
        :param width_adj: Optional. Adjust the width of the component considering this space
        """
        if width_adj:
            self.css.margins(left=(percent, '%'), right=(percent, '%'))
        else:
            self.css.margin_left = "%s%%" % percent
            self.css.margin_right = "%s%%" % percent

    def selector(self, suffix: str, attrs: dict):
        """Set the selector name.

        :param suffix: The selector suffix value
        :param attrs: The CSS attributes
        """
        key_selector = "_%s" % suffix
        if key_selector not in self.__css_virtual:
            self.__css_virtual[key_selector] = {}
        self.__css_virtual[key_selector].update(attrs)

    def add_custom_class(self, css_attrs: dict, classname: str = None, selector: str = None,
                         is_class: bool = True, to_component: bool = False):
        """This will create dynamic CSS class which will not be added to any component.
        The class definition can then be reused in multiple components.

        The CSS style of the body can only be done using predefined classes or inline CSS.

        Usage::

          page.body.style.custom_class(css_attrs={"_attrs": {"fill": 'red'}}, classname='nvd3.nv-pie .nv-pie-title')

          p = page.ui.texts.paragraph("This is a paragraph", helper="Paragraph helper")
          p.style.add_custom_class({"_attrs": {"color": "green"}, "_hover": {"color": "blue"}})

        :param css_attrs: Nested dictionary with the different attributes.
        :param classname: Optional. The classname in the CSS definition.
        :param selector: Optional. The class selector (if it is not a classname using . but a strict definition).
        :param is_class: Optional. Automatically transform the name to a CSS class definition by adding a .
        :param to_component: Optional.
        """
        if classname is None:
            classname = "Virtual%s" % abs(hash(str(css_attrs)))
            if to_component:
                cls_def = {"classname": classname}
            else:
                cls_def = {"classname": False, '_selector': selector}
        else:
            cls_def = {"classname": classname}
        if '_attrs' not in css_attrs and '_hover' not in css_attrs:
            css_attrs = {"_attrs": css_attrs}
        css_attrs['is_class'] = is_class
        cls_def.update(css_attrs)
        v_cls = type(classname, (CssStyle.Style,), cls_def)
        cls_obj = v_cls(self.page)
        if to_component:
            self.classList['main'].add(cls_obj)
        else:
            self.classList['other'].add(cls_obj)
        return cls_def

    def no_class(self):
        """Clear all the Style, Classes and CSS attributes for the HTML component.
        Once this function is called it is possible to add new CSS attributes or classes using the different catalog.

        :return: self to allow the chaining.
        """
        self.classList['main'] = OrderedSet()
        self.component.attr['class'] = self.classList['main']
        self._css_class = None
        return self

    def clear_class(self, classname: str):
        """Remove a class from the main class object attribute.

        :param classname: The CSS class name to be removed for the component.

        :return: The style property for chaining.
        """
        classes = OrderedSet()
        for cls in self.classList['main']:
            if classname.lower() != cls.classname:
                classes.add(cls)
        self.classList['main'] = classes
        self.component.attr['class'] = self.classList['main']
        return self

    def clear_style(self, persist_attrs: dict = None, keep_attrs: list = None):
        """Clear all the inline CSS styles defined for the component.

        :param persist_attrs: Optional. CSS attributes to be maintained
        :param keep_attrs: Optional. CSS attributes to keep from the initial state

        :return: self to allow the chaining.
        """
        if keep_attrs is not None:
            if persist_attrs is not None:
                persist_attrs = dict(persist_attrs)
            else:
                persist_attrs = {}
            for k in keep_attrs:
                val = self.component.attr['css'][k]
                if val is not None:
                    persist_attrs[k] = val
        self.component.attr['css'] = {}
        if persist_attrs is not None:
            self.component.attr['css'].update(persist_attrs)
        self.css.attrs = self.component.attr['css']
        return self

    def clear(self, no_default: bool = False):
        """Remove the predefined class and set the default one for the div components.

        :param no_default: Optional. Remove the default class

        :return: self to allow the chaining.
        """
        self.classList['main'] = OrderedSet()
        if Defaults_css.DEFAULT_STYLE == 'no_border':
            if no_default:
                self._css_class = ""
            else:
                self._css_class = Classes.CatalogDiv.CatalogDiv(
                    self.page, self.classList['main'], html_id=self.component.htmlCode).no_border()
        else:
            self._css_class = Defaults_css.DEFAULT_STYLE
        self.component.attr['class'] = self.classList['main']
        return self

    def clear_all(self, no_default: bool = False):
        """Clear all the Style, Classes and CSS attributes for the HTML component.

        Once this function is called it is possible to add new CSS attributes or classes using the different catalog.
        Set the default style to no margin and no padding.

        :param no_default: Optional. Remove the default class.

        :return: self to allow the chaining.
        """
        self.clear_style()
        self.clear(no_default)
        return self

    def builder(self, name: str, js_frg: str):
        """Attach a Javascript Builder to a CSS style.

        It will be triggered only once for all the HTML components using this style.

        :param name: The Javascript variable name
        :param js_frg: The Javascript framework corresponding to the Js builder
        """
        self.component.page.properties.css.add_builders("const %s = %s" % (name, js_frg))
        return self

    def get_classes(self):
        """Returns the list of Internal and bespoke classes to be added to the class HTML table on the component. """
        if self.__css_virtual and '_attrs' not in self.__css_virtual:
            self.__css_virtual["_attrs"] = self.__css_virtual.get('_temp', {})
            self.__css_virtual["_attrs"].update(dict(self.css.attrs))
            self.__css_virtual['classname'] = "style_%s" % self.component.htmlCode
            meta_cls = type('Style%s' % self.component.htmlCode, (CssStyle.Style,), self.__css_virtual)
            self.css.attrs = {}
            self.classList['main'].add(meta_cls(self.page))
            self.component.attr['css'] = {}
        computed_classlist = {"main": OrderedSet(), 'other': OrderedSet()}
        for css_category, css_cls in self.classList.items():
            for c in css_cls:
                if hasattr(c, 'get_ref'):
                    c = Classes.get_class_override(c)
                    if not c:
                        continue

                    if c.is_page_scope:
                        self.page._css[c.get_ref()] = c
                computed_classlist[css_category].add(c)
        return computed_classlist

    def get_classes_css(self):
        """ """
        css_frgs = {}
        for css_cls in self.classList.values():
            for c in css_cls:
                if hasattr(c, 'get_ref'):
                    c = Classes.get_class_override(c)
                    if not c:
                        continue

                    if c.is_page_scope:
                        css_frgs[c.get_ref()] = str(c)
        return css_frgs

    def add(self, class_name: str):
        """Shortcut to add a Class class defined with a string.

        :param class_name: CSS class reference (selector)
        """
        self.classList["main"].add(class_name)

    @property
    def bs(self) -> BsCssClasses.Style:
        """Add shortcut to the Bootstrap predefined styles.

        Related Pages:

          https://getbootstrap.com/docs/5.0/getting-started/introduction/
        """
        self.page.jsImports.add("bootstrap")
        self.page.cssImport.add("bootstrap")
        return BsCssClasses.Style(self.component.attr['class'])


class ClassHtmlEmpty(ClassHtml):

    @property
    def css(self) -> Empty:
        """Property to the underlying CSS definition to be added to the style HTML tag of a component."""
        if self._css_struct is None:
            self._css_struct = Empty(self.component, page=self.page)
        return self._css_struct
