#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO PanelSliding: find a way to introduce CSS transform for the panel display

import logging
from pathlib import Path
from typing import Union, Optional, List, Tuple
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.interfaces import Arguments

from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.html.options import OptPanel
from epyk.core.html.options import OptText
from epyk.core.html.options import OptGridstack

from epyk.core.js import treemap
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.html import JsHtmlPanels
from epyk.core.js.packages import JsGridstack

# The list of CSS classes
from epyk.core.css.styles import GrpClsContainer


class Panel(Html.Html):
    name = 'Panel'
    tag = "div"

    def __init__(self, page: primitives.PageModel, components: Union[List[Html.Html], Html.Html],
                 title: Optional[str], color: Optional[str], width: types.SIZE_TYPE, height: types.SIZE_TYPE,
                 html_code: Optional[str], helper: Optional[str], options: types.OPTION_TYPE,
                 profile: types.PROFILE_TYPE):
        if isinstance(components, list) and components:
            for component in components:
                if hasattr(component, 'options'):
                    component.options.managed = False
        elif components is not None and hasattr(components, 'options'):
            components.options.managed = False
        component, self.menu = [], None
        if title is not None:
            self.title = page.ui.title(title)
            self.title.options.managed = False
            component.append(self.title)
        container = page.ui.div(components)
        container.options.managed = False
        component.append(container)
        self.add_helper(helper)
        super(Panel, self).__init__(page, component, html_code=html_code, profile=profile, options=options,
                                    css_attrs={"color": color, "width": width, "height": height})
        container.set_attrs(name="name", value="panel_%s" % self.html_code)

    @property
    def style(self) -> GrpClsContainer.ClassDiv:
        """Property to the CSS Style of the component."""
        if self._styleObj is None:
            self._styleObj = GrpClsContainer.ClassDiv(self)
        return self._styleObj

    @property
    def dom(self) -> JsHtmlPanels.JsHtmlPanel:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlPanels.JsHtmlPanel(component=self, page=self.page)
        return self._dom

    def extend(self, components: List[Html.Html]):
        """Add multiple HTML components to the container.

        :param components: The list of components.
        """
        for component in components:
            self.add(component)
        return self

    def add_menu(self, close: bool = True, mini: bool = True, info: Optional[bool] = None, pin: Optional[bool] = False):
        """Add specific and predefined options to the panels.

        :param close: Optional. Add a close button to the panel
        :param mini: Optional. Add a minimize button to the panel
        :param info: Optional. Add a info button to the panel
        :param pin: Optional. Add a pin button to the panel
        """
        self.style.css.position = "relative"
        self.style.css.min_height = 25
        self.style.css.min_width = 25
        if self.menu is None:
            self.menu = self.page.ui.div()
            self.menu.options.managed = False
            self.menu.style.css.position = "absolute"
            self.menu.style.css.text_align = "right"
            self.menu.style.css.top = 2
            self.menu.style.css.right = 5
            self.menu.style.css.margin = 0
        if pin:
            pin_comp = self.page.ui.icon("fas fa-thumbtack")
            pin_comp.style.css.margin_right = 10
            pin_comp.tooltip(info)
            pin_comp.style.css.color = self.page.theme.greys[6]
            self.menu.add(pin_comp)
        if info is not None:
            info_comp = self.page.ui.icon("question")
            info_comp.style.css.margin_right = 10
            info_comp.style.css.font_factor(-5)
            info_comp.tooltip(info)
            info_comp.click([
                self.dom.querySelector("div[name=panel]").toggle()])
            info_comp.style.css.color = self.page.theme.greys[6]
            self.menu.add(info_comp)
        if mini:
            remove = self.page.ui.icon("square_minus")
            remove.style.css.margin_right = 10
            remove.click([
                self.dom.querySelector("div[name=panel]").toggle()])
            remove.style.css.color = self.page.theme.greys[6]
            self.menu.add(remove)
        if close:
            remove = self.page.ui.icon("times")
            remove.style.css.margin_right = 10
            remove.click([self.dom.remove()])
            remove.style.css.color = self.page.theme.greys[6]
            self.menu.add(remove)
        return self.menu

    def __str__(self):
        str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
        if self.menu is None:
            return "<%s %s>%s</%s>%s" % (
                self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_div, self.tag, self.helper)

        menu_width = "100%"
        if self.style.css.width.endswith('px'):
            menu_width = self.style.css.width
            self.style.css.width = None
        return "<%s %s>%s<div style='width:%s' name='panel'>%s</div></%s>%s" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.menu.html(), menu_width, str_div,
            self.helper, self.tag)


class PanelSplit(Html.Html):
    name = 'Panel Horizontal Split'
    tag = 'div'

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-panel-h.css",
    ]

    style_refs = {
        "html-panel-h": "html-panel-h",
        "html-panel-h-gutter": "html-panel-h-gutter",
        "html-panel-h-pane": "html-panel-h-pane",
        "html-panel-h-left": "html-panel-h-left",
        "html-panel-h-right": "html-panel-h-right",
    }

    def __init__(self, page: primitives.PageModel, width: types.SIZE_TYPE, height: types.SIZE_TYPE,
                 left_width: types.SIZE_TYPE, left_obj, right_obj, resizable: bool, helper,
                 options: types.OPTION_TYPE, profile: types.PROFILE_TYPE):
        self.__resizable = resizable
        super(PanelSplit, self).__init__(page, None, profile=profile, options=options,
                                         css_attrs={"width": width, "height": height, 'white-space': 'nowrap'})
        self.classList.add(self.style_refs["html-panel-h"])
        self.gutter = self.page.ui.div(html_code=self.sub_html_code("gutter"))
        self.gutter.style.clear_all(False, True)
        self.gutter.options.managed = False
        self.gutter.classList.add(self.style_refs["html-panel-h-gutter"])
        self.panels = {
            "left": self.page.ui.div([], html_code=self.sub_html_code("left")),
            "right": self.page.ui.div([self.gutter], html_code=self.sub_html_code("right"))}
        self.panels["left"].style.clear_all(False, True)
        self.panels["left"].style.css.width = Arguments.size(left_width, unit="px", toStr=True)
        self.panels["left"].style.css.overflow_x = "auto"
        self.panels["left"].classList.add(self.style_refs["html-panel-h-pane"])
        self.panels["left"].classList.add(self.style_refs["html-panel-h-left"])
        self.panels["left"].options.managed = False
        self.panels["right"].style.clear_all(False, True)
        self.panels["right"].style.css.overflow_x = "auto"
        self.panels["right"].classList.add(self.style_refs["html-panel-h-pane"])
        self.panels["right"].classList.add(self.style_refs["html-panel-h-right"])
        self.panels["right"].options.managed = False
        if left_obj:
            if not isinstance(left_obj, list):
                left_obj = [left_obj]
            for o in left_obj:
                self.left(o)
        if right_obj:
            if not isinstance(right_obj, list):
                right_obj = [right_obj]
            for o in right_obj:
                self.right(o)
        self.add_helper(helper)
        if resizable:
            self.gutter.style.css.cursor = "col-resize"
            self.gutter.dblclick([
                self.panels["left"].dom.css("width", "100%").r,
                self.panels["right"].dom.toggle()
            ])

    def left(self, component: Html.Html):
        """Add the left component to the panel.

        Usage::
          split_panel = page.ui.panels.split()
          split_panel.left(page.ui.col([page.ui.text("Left")]))

        :param component: An HTML component
        """
        if hasattr(component, "options"):
            component.options.managed = False
        self.panels["left"].add(component)
        return self

    def right(self, component: Html.Html):
        """Add the right component to the panel.

        Usage::
          split_panel = page.ui.panels.split()
          split_panel.right(page.ui.col([page.ui.text("Right")]))

        :param component: An HTML component
        """
        if hasattr(component, "options"):
            component.options.managed = False
        self.panels["right"].add(component)
        return self

    def toggle(self, button, panel: str = 'right'):
        """Toggle (show / hide) a given panel based on an external component click.

        :param button: The external component used to trigger the change
        :param panel: The panel alias.
        """
        side_panel = "left" if panel == "right" else "right"
        if panel == "left":
            return button.click([
                self.page.js.if_(self.panels[panel].dom.css("display") == "none", [
                    self.panels[side_panel].dom.css("width", "auto").r]).else_([self.panels[side_panel].dom.css("width", "100%").r]),
                self.panels[panel].dom.toggle()
            ])

        return button.click([
            self.panels[side_panel].dom.css("width", "100%").r,
            self.panels[panel].dom.toggle()
        ])

    def __str__(self):
        if self.__resizable:
            dr = JsUtils.DefinedResource(self.page, "PanelResizerH", "utils")
            self.gutter.on("mousedown", dr.on_event("resizerH"))
        return '''<%(tag)s %(attrs)s>%(left)s%(right)s</%(tag)s>%(helper)s''' % {
            "attrs": self.get_attrs(css_class_names=self.style.get_classes()), 'left': self.panels["left"].html(),
            'right': self.panels["right"].html(), "helper": self.helper, "tag": self.tag}


class PanelVSplit(Html.Html):
    name = 'Panel Vertical Split'
    tag = 'div'

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-panel-v.css",
    ]

    style_refs = {
        "html-panel-v": "html-panel-v",
        "html-panel-v-gutter": "html-panel-v-gutter",
        "html-panel-v-pane": "html-panel-v-pane",
        "html-panel-v-top": "html-panel-v-top",
        "html-panel-v-bottom": "html-panel-v-bottom",
    }

    def __init__(self, page: primitives.PageModel, width: types.SIZE_TYPE, height: types.SIZE_TYPE,
                 top_height: types.SIZE_TYPE, top_obj, bottom_obj, resizable: bool, helper,
                 options: types.OPTION_TYPE, profile: types.PROFILE_TYPE):
        self.__resizable = resizable
        super(PanelVSplit, self).__init__(page, None, profile=profile, options=options,
                                         css_attrs={"width": width, "height": height, 'white-space': 'nowrap'})
        self.classList.add(self.style_refs["html-panel-v"])
        self.gutter = self.page.ui.div(html_code=self.sub_html_code("gutter"))
        self.gutter.style.clear_all(False, True)
        self.gutter.options.managed = False
        self.gutter.classList.add(self.style_refs["html-panel-v-gutter"])
        self.panels = {
            "top": self.page.ui.div([], html_code=self.sub_html_code("top")),
            "bottom": self.page.ui.div([], html_code=self.sub_html_code("bottom"))}
        self.panels["top"].style.clear_all(False, True)
        self.panels["top"].style.css.height = Arguments.size(top_height, unit="px", toStr=True)
        self.panels["top"].style.css.overflow_y = "auto"
        self.panels["top"].classList.add(self.style_refs["html-panel-v-pane"])
        self.panels["top"].classList.add(self.style_refs["html-panel-v-top"])
        self.panels["top"].options.managed = False
        self.panels["bottom"].style.clear_all(False, True)
        self.panels["bottom"].style.css.overflow_y = "auto"
        self.panels["bottom"].classList.add(self.style_refs["html-panel-v-pane"])
        self.panels["bottom"].classList.add(self.style_refs["html-panel-v-bottom"])
        self.panels["bottom"].options.managed = False
        if top_obj:
            if not isinstance(top_obj, list):
                top_obj = [top_obj]
            for o in top_obj:
                self.top(o)
        if bottom_obj:
            if not isinstance(bottom_obj, list):
                bottom_obj = [bottom_obj]
            for o in bottom_obj:
                self.bottom(o)
        self.add_helper(helper)
        if resizable:
            self.gutter.style.css.cursor = "row-resize"
            self.gutter.dblclick([
                self.panels["top"].dom.css("width", "100%").r,
                self.panels["bottom"].dom.toggle()
            ])

    def top(self, component: Html.Html):
        """Add the left component to the panel.

        Usage::
          split_panel = page.ui.panels.split()
          split_panel.left(page.ui.col([page.ui.text("Left")]))

        :param component: An HTML component
        """
        if hasattr(component, "options"):
            component.options.managed = False
        self.panels["top"].add(component)
        return self

    def bottom(self, component: Html.Html):
        """Add the right component to the panel.

        Usage::
          split_panel = page.ui.panels.split()
          split_panel.right(page.ui.col([page.ui.text("Right")]))

        :param component: An HTML component
        """
        if hasattr(component, "options"):
            component.options.managed = False
        self.panels["bottom"].add(component)
        return self

    def toggle(self, button, panel: str = 'bottom'):
        """Toggle (show / hide) a given panel based on an external component click.

        :param button: The external component used to trigger the change
        :param panel: The panel alias.
        """
        side_panel = "top" if panel == "bottom" else "bottom"
        if panel == "top":
            return button.click([
                self.page.js.if_(self.panels[panel].dom.css("display") == "none", [
                    self.panels[side_panel].dom.css("width", "auto").r]).else_([self.panels[side_panel].dom.css("width", "100%").r]),
                self.panels[panel].dom.toggle()
            ])

        return button.click([
            self.panels[side_panel].dom.css("width", "100%").r,
            self.panels[panel].dom.toggle()
        ])

    def __str__(self):
        if self.__resizable:
            dr = JsUtils.DefinedResource(self.page, "PanelResizerV", "utils")
            self.gutter.on("mousedown", dr.on_event("resizerV"))
        return '''<%(tag)s %(attrs)s>%(top)s%(gutter)s%(bottom)s</%(tag)s>%(helper)s''' % {
            "attrs": self.get_attrs(css_class_names=self.style.get_classes()),
            'top': self.panels["top"].html(), 'bottom': self.panels["bottom"].html(), "helper": self.helper,
            "tag": self.tag, "gutter": self.gutter.html()}


class PanelSlide(Panel):
    name = 'Slide Panel'
    _option_cls = OptPanel.OptionPanelSliding
    tag = 'div'
    category = None

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-panel-slide.css"
    ]

    style_refs = {
        "html-slidepanel-title": "html-slidepanel-title",
        "html-slidepanel-content": "html-slidepanel-content",
        "html-slidepanel-icon": "html-slidepanel-icon",
        "html-slidepanel-center": "html-slidepanel-center",
    }

    def __init__(self, page: primitives.PageModel, components: Optional[List[Html.Html]],
                 title: Union[Html.Html, str], color: Optional[str], width: types.SIZE_TYPE,
                 height: types.SIZE_TYPE, html_code: Optional[str], helper,
                 options: types.OPTION_TYPE, profile: types.PROFILE_TYPE):
        if components:
            for c in components:
                c.options.managed = False
        super(PanelSlide, self).__init__(
            page, components, None, color, width, height, html_code, helper, options, profile)
        self.add_helper(helper)
        self.icon = self.page.ui.icon("", html_code=self.sub_html_code("icon"))
        self.icon.add_style(self.style_refs["html-slidepanel-icon"], clear_first=True)
        self.icon.options.managed = False
        if hasattr(title, 'options'):
            self.text = title
            self.text.options.managed = False
        else:
            self.text = self.page.ui.title(title, html_code=self.sub_html_code("title"))
        self.text.classList.add(self.style_refs["html-slidepanel-content"])
        self.title = self.page.ui.div([self.icon, self.text], html_code=self.sub_html_code("panel"))
        self.title.classList.add(self.style_refs["html-slidepanel-title"])
        self.title.options.managed = False
        self._vals, self.__clicks, self.__clicks_open = [self.title] + self._vals, [], []

    @classmethod
    def get_requirements(cls, page: primitives.PageModel, options: types.OPTION_TYPE = None) -> tuple:
        """Update requirements with the defined Icons' family.

        :param page: Page context
        :param options: Component input options
        """
        if options and options.get('icon_family') is not None:
            return (options['icon_family'],)

        return (page.icons.family,)

    @property
    def panel(self):
        return self.val[1]

    @property
    def options(self) -> OptPanel.OptionPanelSliding:
        """Property to the comments component options.
        Optional can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def dom(self) -> JsHtmlPanels.JsHtmlSlidingPanel:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlPanels.JsHtmlSlidingPanel(self, page=self.page)
        return self._dom

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """Event added to the title bar.
        This will be triggered first.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__clicks = js_funcs
        return self

    def open(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None, on_ready: str = False):
        """Event triggered when the sliding panel is open.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if not js_funcs:
            js_funcs = []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__clicks_open = [self.page.js.if_(self.icon.dom.content.toString().indexOf(
            self.options.icon_expanded.split(" ")[-1]) >= 0, js_funcs, profile=profile).toStr()]
        return self

    def __add__(self, component: Html.Html):
        """Add items to a container """
        self.val[1] += component
        component.options.managed = False
        return self

    def insert(self, n, component: Html.Html):
        """Insert a component at a given position in the content panel"""
        self.val[1].insert(n, component)
        component.options.managed = False
        return self

    def __str__(self):
        self.title.style.css.text_align = self.options.title_align
        if self.options.title_align == "right":
            self.text.style.css.margin_right = 5
        if self.options.expanded:
            icon_change = self.options.icon_closed
            icon_current = self.options.icon_expanded
            self.icon.set_icon(self.options.icon_expanded)
        else:
            icon_change = self.options.icon_expanded
            icon_current = self.options.icon_closed
            self._vals[1].style.css.display = 'none'
            self.icon.set_icon(self.options.icon_closed)
        if self.options.icon_position == "right":
            self.icon.style.css.float = "right"
        click_frg = [self.page.js.getElementsByName("panel_%s" % self.htmlCode).first.toggle()]
        if icon_change and icon_current:
            click_frg.append(self.icon.dom.switchClass(icon_current, icon_change))
        if self.options.click_type == 'title':
            self.title.style.css.cursor = "pointer"
            self.title.click(self.__clicks + click_frg + self.__clicks_open)
        elif self.options.click_type == 'icon':
            self.icon.click(self.__clicks + click_frg + self.__clicks_open)
        str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
        return "<%s %s>%s</%s>%s" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_div, self.tag,  self.helper)


class Div(Html.Html):
    name = 'Simple Container'
    _option_cls = OptPanel.OptionsDiv

    def __init__(self, page: primitives.PageModel, components: List[Html.Html], label: Optional[str],
                 color: Optional[str], width: types.SIZE_TYPE, icon: Optional[str], height: types.SIZE_TYPE,
                 editable: bool, align: str, padding: Optional[str], html_code: Optional[str],
                 tag: str, helper: Optional[str], options: types.OPTION_TYPE, profile: types.OPTION_TYPE):
        super(Div, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                  css_attrs={"color": color, "width": width, "height": height})
        if not isinstance(components, list):
            components = [components]
        for obj in components:
            if isinstance(obj, list) and obj:
                component = page.ui.div(
                    obj, label, color, width, icon, height, editable, align, padding, html_code, tag, helper, profile,
                    position=options.get("position", None))
            else:
                component = obj
            if hasattr(component, 'options'):
                self.__add__(component)
                if self.options.get(None, "position") is not None:
                    component.style.css.vertical_align = self.options.get(None, "position")
            else:
                if self.options.html_encode:
                    obj = self.page.py.encode_html(obj)
                if self.options.multiline:
                    obj = obj.replace("\n", "<br/>")
                self.val.append(obj)
        self.tag = tag
        # Add the component predefined elements
        self.add_icon(icon, html_code=self.html_code, family=options.get("icon_family", None))
        self.add_label(label, html_code=self.html_code)
        self.add_helper(helper)
        if helper is not None:
            self.helper.style.css.position = "absolute"
            self.helper.style.css.bottom = 10
            self.helper.style.css.right = 25
        self.css({'text-align': align})
        if padding is not None:
            self.css('padding', '%s' % padding)
        if editable:
            self.set_attrs(name='contenteditable', value="true")
            self.css('overflow', 'auto')

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return True

    def goto(self, url: str, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
             target: str = "_blank", source_event: Optional[str] = None):
        """Click event which redirect to another page.

        `Related Pages <https://www.w3schools.com/tags/att_a_target.asp>`_

        :param url: the url
        :param js_funcs: Optional. The Javascript Events triggered before the redirection
        :param profile: Optional. A flag to set the component performance storage
        :param target: Optional. The target attribute specifies where to open the linked document
        :param source_event: Optional. The event source
        """
        self.style.css.cursor = "pointer"
        js_funcs = js_funcs or []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_funcs.append(self.js.location.open_new_tab(url, target))
        return self.click(js_funcs, profile, source_event)

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
        self.css({"cursor": "pointer"})
        return super(Div, self).click(js_funcs=js_funcs, profile=profile, source_event=source_event, on_ready=on_ready)

    @property
    def dom(self) -> JsHtml.JsHtmlRich:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlRich(self, page=self.page)
        return self._dom

    def __add__(self, component: Html.Html):
        """ Add items to a container """
        if isinstance(component, list):
            component = self.page.ui.row(component, position=self.options.get(None, "position"),
                                         html_code=self.sub_html_code("row", auto_inc=True))
        # Has to be defined here otherwise it is set to late
        component.options.managed = False
        if self.options.inline:
            component.style.css.display = 'inline-block'
            component.style.css.font_weight = 900
        if not isinstance(self.val, list):
            self._vals = [self.val]
        # Avoid having duplicated entries
        # This could happen in the __str__ method of the HTML Components (example Popup)
        if component.html_code not in self.components:
            self.val.append(component)
            self.components[component.html_code] = component
        return self

    def insert(self, n: int, component: Html.Html):
        """Insert a component to a div.

        :param n: The expected position of the component in the list
        :param component: The component to be added to the underlying list
        """
        if isinstance(component, list):
            component = self.page.ui.row(component, html_code=self.sub_html_code("row", auto_inc=True))
        # Has to be defined here otherwise it is set to late
        component.options.managed = False
        if self.options.inline:
            component.style.css.display = 'inline-block'
            component.style.css.font_weight = 900
        if not isinstance(self.val, list):
            self._vals = [self.val]
        self.val.insert(n, component)
        self.components[component.htmlCode] = component
        return self

    def extend(self, components: List[Html.Html]):
        """Add multiple HTML components to the container.

        :param components: The list of components
        """
        for component in components:
            self.add(component)
        return self

    @property
    def options(self) -> OptPanel.OptionsDiv:
        """Property to set all the possible object for a button."""
        return super().options

    @property
    def style(self) -> GrpClsContainer.ClassDiv:
        """Property to the CSS Style of the component."""
        if self._styleObj is None:
            self._styleObj = GrpClsContainer.ClassDiv(self)
        return self._styleObj

    def build(self, data: types.JS_DATA_TYPES = None, options: Optional[dict] = None,
              profile: types.PROFILE_TYPE = None, component_id: Optional[str] = None,
              dataflows: List[dict] = None, **kwargs):
        """Build / Update the component.
        This is a function triggered on the JavaScript side.

        :param data: Optional. A String corresponding to a JavaScript object
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. A DOM component reference in the page
        :param dataflows: Chain of data transformations
        """
        # check if there is no nested HTML components in the data
        if isinstance(data, dict):
            js_data = "{%s}" % ",".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in data.items()])
        else:
            js_data = JsUtils.dataFlows(data, dataflows, self.page)
        options, js_options = options or {}, []
        for k, v in options.items():
            if isinstance(v, dict):
                row = ["%s: %s" % (s_k, JsUtils.jsConvertData(s_v, None)) for s_k, s_v in v.items()]
                js_options.append("%s: {%s}" % (k, ", ".join(row)))
            else:
                js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
        return "%s.innerHTML = %s" % (component_id or self.dom.varId, js_data)

    def focus(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
              options: dict = None, source_event: str = None, on_ready: bool = False):
        """Action on focus.

        :param js_funcs: Optional. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param options: Optional. Specific Python options available for this component
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.attr["tabindex"] = "0"
        if js_funcs is None:
            js_funcs = []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        return self.on("focus", js_funcs, profile, source_event, on_ready)

    def __str__(self):
        rows = []
        for component in self.val:
            if hasattr(component, 'html'):
                if self._sort_propagate:
                    component.sortable(self._sort_options)
                rows.append(component.html())
            else:
                rows.append(str(component))

        return "<%(tag)s %(attrs)s>%(content)s</%(tag)s>%(badge)s%(helper)s" % {
            'tag': self.tag or 'div', 'attrs': self.get_attrs(css_class_names=self.style.get_classes()),
            "content": "".join(rows), "helper": self.helper, "badge": self.badge}


class Td(Html.Html):
    name = 'Cell'

    def __init__(self, page: primitives.PageModel, components: Optional[List[Union[Html.Html, str]]],
                 header: bool, position: Optional[str], width: types.SIZE_TYPE,
                 height: types.SIZE_TYPE, align: Optional[str], options: types.OPTION_TYPE,
                 profile: types.PROFILE_TYPE, html_code: Optional[str] = None):
        self.position, self.rows_css, self.row_css_dflt, self.header = position, {}, {}, header
        super(Td, self).__init__(page, [], profile=profile, html_code=html_code,
                                 css_attrs={"width": width, "height": height, 'white-space': 'nowrap'})
        self.__options = options
        self.attr["align"] = options.cell_align or align
        if components is not None:
            for component in components:
                self.__add__(component)

    def colspan(self, i: int):
        """The colspan attribute defines the number of columns a cell should span.

        `Related Pages <https://www.w3schools.com/tags/att_td_colspan.asp>`_

        :param i: The column span value for the cell object
        """
        self.attr['colspan'] = i
        return self

    def rowspan(self, i: int):
        """The rowspan attribute specifies the number of rows a cell should span.

        `Related Pages <https://www.w3schools.com/tags/att_td_rowspan.asp>`_

        :param i: The row span value for the cell
        """
        self.attr['rowspan'] = i
        return self

    def __str__(self):
        content = [htmlObj.html() if hasattr(htmlObj, 'options') else str(htmlObj) for htmlObj in self.val]
        if self.header:
            return '<th %s>%s</th>' % (self.get_attrs(css_class_names=self.style.get_classes()), "".join(content))

        return '<td %s>%s</td>' % (self.get_attrs(css_class_names=self.style.get_classes()), "".join(content))


class Tr(Html.Html):
    name = 'Column'
    tag = "tr"

    def __init__(self, page: primitives.PageModel, components: Optional[List[Html.Html]],
                 header, position, width: types.SIZE_TYPE, height: types.SIZE_TYPE,
                 align: Optional[str], options: types.OPTION_TYPE, profile, html_code: Optional[str] = None):
        self.position, self.header = position, header
        super(Tr, self).__init__(
            page, [], html_code=html_code, profile=profile,
            css_attrs={"width": width, "height": height, 'text-align': align})
        self.__options = options
        if components is not None:
            for component in components:
                self.__add__(component)
        self.style.justify_content = self.position

    def __add__(self, component: Html.Html):
        """Add items to a container.

        :param component: The underlying HTML component to be added this container
        """
        if not isinstance(component, Td):
            if not isinstance(component, list):
                component = [component]
            component = Td(self.page, component, self.header, None, (None, "%"), (None, "%"),
                           'center', self.__options, False)
        super(Tr, self).__add__(component)
        return self

    @property
    def dom(self) -> JsHtmlPanels.JsHtmlTr:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlPanels.JsHtmlTr(self, page=self.page)
        return self._dom

    def __str__(self):
        cols = [htmlObj.html() for i, htmlObj in enumerate(self.val)]
        return '<%s %s>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), "".join(cols), self.tag)


class Caption(Html.Html):
    name = 'Table Caption'
    _option_cls = OptText.OptionsText
    tag = "caption"

    def __init__(self, page: primitives.PageModel, text: Optional[str], color: Optional[str], align: Optional[str],
                 width: types.SIZE_TYPE, height: types.SIZE_TYPE, html_code: Optional[str],
                 tooltip: Optional[str], options: types.OPTION_TYPE, profile: types.PROFILE_TYPE):
        super(Caption, self).__init__(page, text, html_code=html_code, profile=profile, options=options,
                                      css_attrs={"width": width, "height": height, "color": color, 'text-align': align})
        if tooltip is not None:
            self.tooltip(tooltip)

    @property
    def options(self) -> OptText.OptionsText:
        """Property to set all the possible object for a button."""
        return super().options

    def __str__(self):
        val = self.page.py.markdown.all(self.val) if self.options.showdown is not False else self.val
        return '<%s %s>%s</%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), val, self.tag)


class TSection(Html.Html):
    name = 'Table Section'
    _option_cls = OptPanel.OptionPanelTable

    def __init__(self, page: primitives.PageModel, type: str, rows: Optional[list] = None,
                 options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None,
                 html_code: Optional[str] = None):
        super(TSection, self).__init__(page, [], html_code=html_code, options=options, profile=profile)
        self.__section = type
        if rows is not None:
            for row in rows:
                self.__add__(row)

    @property
    def options(self) -> OptPanel.OptionPanelTable:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def __add__(self, row_data: Union[Tr, List[Html.Html]]):
        """Add items to a container """
        if not isinstance(row_data, Tr):
            row_data = Tr(
                self.page, row_data, self.__section == 'thead', None, (100, "%"), (100, "%"),
                'center', self.options, False, html_code=self.sub_html_code("thead", auto_inc=True))
        super(TSection, self).__add__(row_data)
        return self

    def __str__(self):
        cols = []
        for component in self.val:
            if self._sort_propagate:
                component.sortable(self._sort_options)
            cols.append(component.html())
        return '<%(section)s %(attr)s>%(cols)s</%(section)s>' % {
            'section': self.__section, 'cols': "".join(cols),
            'attr': self.get_attrs(css_class_names=self.style.get_classes())}


class Table(Html.Html):
    name = 'Table'
    _option_cls = OptPanel.OptionPanelTable
    tag = "table"

    def __init__(self, page: primitives.PageModel, rows, width: types.SIZE_TYPE, height: types.SIZE_TYPE,
                 helper: Optional[str], options: types.OPTION_TYPE, profile: types.PROFILE_TYPE, html_code: str = None):
        super(Table, self).__init__(page, [], css_attrs={
            "width": width, "height": height, 'table-layout': 'auto', 'white-space': 'nowrap',
            'border-collapse': 'collapse',
            'box-sizing': 'border-box'}, profile=profile, options=options, html_code=html_code)
        self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
        self.header = TSection(self.page, 'thead', options=options, html_code=self.sub_html_code('thead'))
        self.body = TSection(self.page, 'tbody', options=options, html_code=self.sub_html_code('tbody'))
        self.footer = TSection(self.page, 'tfoot', options=options, html_code=self.sub_html_code('tfoot'))
        self.header.options.managed = False
        self.body.options.managed = False
        self.footer.options.managed = False
        self.caption = None
        if rows is not None:
            for row in rows:
                self.__add__(row)

    @property
    def options(self) -> OptPanel.OptionPanelTable:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def __add__(self, row_data: Union[Tr, List[Html.Html]]):
        """Add items to a container """
        if isinstance(row_data, Tr):
            row = row_data
        else:
            if not self.header.val and not self.body.val and self.options.header:
                row = Tr(self.page, row_data, True, None, (100, "%"), (100, "%"), 'center', self.options, False)
            else:
                row = Tr(self.page, row_data, False, None, (100, "%"), (100, "%"), 'left', self.options, False)
        if row.header:
            self.header += row
        else:
            self.body += row
        return self

    def from_array(self, data: list, dim: int):
        """Load data from a 2D array.

        :param data: The list of data
        :param dim: The number of columns in the table
        """
        v_count = len(data)
        modulo_rest = v_count % dim
        modulo_result = v_count // dim
        for i in range(0, modulo_result):
            row = [data[i * dim + j] for j in range(0, dim)]
            self += row
        if modulo_rest:
            self += data[-modulo_rest:]

    def line(self, text: str = "&nbsp;", align: str = "left", dim: Optional[int] = None):
        """
        :param text: Optional. The value to be displayed to the component
        :param align: Optional. The text-align property within this component
        :param dim: Optional. The number of columns in the table
        """
        cell = Td(
            self.page, [text], False, None, (None, "%"), (None, "%"), align,
            self.options, False, html_code=self.sub_html_code("td", auto_inc=True))
        cell.colspan(dim or len(self.body.val[0].val))
        self += Tr(
            self.page, [cell], False, None, (100, "%"), (100, "%"), align,
            self.options, False, html_code=self.sub_html_code("tr", auto_inc=True))
        return cell

    def add_caption(self, text: str, color: Optional[str] = None, align: Optional[str] = None,
                    width: tuple = (100, "%"),
                    height: tuple = (100, "%"), html_code: Optional[str] = None, tooltip: Optional[str] = None,
                    options: Optional[dict] = None, profile: types.PROFILE_TYPE = None):
        """The <caption> tag defines a table caption.

        `Related Pages <https://www.w3schools.com/tags/tag_caption.asp>`_

        :param text: Optional. The value to be displayed to the component
        :param color: Optional. The font color in the component. Default inherit
        :param align: Optional. The text-align property within this component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param tooltip: Optional. A string with the value of the tooltip
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        self.caption = Caption(self.page, text, color, align, width, height, html_code, tooltip, options, profile)
        return self.caption

    def get_header(self, i: int = 0):
        """Get a component from the header based on its position.

        :param i: Optional. The component index in the header
        """
        return self.header.val[i]

    def get_footer(self, i: int = 0):
        """Get a specific items from the table footer.

        :param i: Optional. The table footer component position
        """
        return self.footer.val[i]

    def col(self, i: int):
        """
        :param i: The column index
        """
        cells = []
        if self.header:
            for h in self.header:
                cells.append(h[i])
        if self.body:
            for b in self.body:
                cells.append(b[i])
        if self.footer:
            for f in self.footer:
                cells.append(f[i])
        for c in cells:
            yield c

    def __getitem__(self, i: int) -> Optional[Tr]:
        """Get the underlying body attached to the component.

        :param i: The internal row based on the index
        """
        if not self.body.val:
            return None

        return self.body.val[i]

    def __str__(self):
        caption = "" if self.caption is None else self.caption.html()
        return '<%s %s>%s%s%s%s</%s>%s' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), caption, self.header.html(),
            self.body.html(), self.footer.html(), self.tag, self.helper)


class Col(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'Column'
    requirements = ('bootstrap',)
    _option_cls = OptPanel.OptionGrid
    tag = 'div'
    html_class: str = None

    def __init__(self, page, components, position: str, width: types.SIZE_TYPE, height: types.SIZE_TYPE, align: str,
                 helper: str, options: types.OPTION_TYPE, profile: types.PROFILE_TYPE, html_code: str = None):
        self.position, self.rows_css, self.row_css_dflt = position, {}, {}
        super(Col, self).__init__(page, [], profile=profile, options=options, html_code=html_code)
        self.__set_size = None
        self.style.clear_all(no_default=True)
        self.css({"width": width, "height": height})
        if components is not None:
            for component in components:
                self.add(component)
        if align == "center":
            self.css({'margin-left': 'auto', 'margin-right': 'auto', 'display': 'inline-block', 'text-align': 'center'})
        else:
            self.css({'display': 'inline-block'})
        self.attr["class"].add('col')
        self.style.justify_content = self.position
        # Bootstrap vertical align middle
        if self.style.css.height == '100%':
            self.attr["class"].add('h-auto')
        elif self.position == 'middle':
            self.attr["class"].add('my-auto')

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return True

    @property
    def options(self) -> OptPanel.OptionGrid:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript available for a DOM element by default.
        """
        return super().options

    def add(self, component: Html.Html, **kwargs):
        """Add items to a container.

        :param component:
        """
        if not hasattr(component, 'options'):
            component = self.page.ui.div(component, align=None)
        super(Col, self).__add__(component)
        return self

    def build(self, data=None, options: Optional[dict] = None, profile: types.PROFILE_TYPE = None,
              component_id: Optional[str] = None, dataflows: List[dict] = None, **kwargs):
        """

        :param data:
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. A DOM component reference in the page
        :param dataflows: Chain of data transformations
        """
        return self.val[0].build(data, options, profile, component_id=component_id, dataflows=dataflows)

    def set_size(self, n: int, break_point: str = "lg"):
        """Set the column size.

        Usage::

          ps = page.ui.layouts.grid()
          ps += [page.ui.text("test %s" % i) for i in range(5)]
          ps[0][0].set_size(10)

        :param n: The size of the component in the bootstrap row.
        :param break_point: Optional. Grid system category, with
          - xs (for phones - screens less than 768px wide)
          - sm (for tablets - screens equal to or greater than 768px wide)
          - md (for small laptops - screens equal to or greater than 992px wide)
          - lg (for laptops and desktops - screens equal to or greater than 1200px wide)
        """
        if self.__set_size is None:
            if not n:
                self.__set_size = False
                return self

            if isinstance(n, int) or n.is_integer():
                self.__set_size = "col-%s-%s" % (break_point, int(n))
            else:
                self.__set_size = "col-%s" % break_point
            self.attr["class"].add(self.__set_size)
            if self.options.responsive and break_point != 'lg':
                self.attr["class"].add("col-%s-%s" % (break_point, min(int(n) * 2, 12)))
                self.attr["class"].add("col-12")
        return self

    def __str__(self):
        content = [htmlObj.html() for htmlObj in self.val]
        return '<%s %s>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), "".join(content), self.tag)


class Row(Html.Html):
    name = 'Column'
    requirements = ('bootstrap',)
    _option_cls = OptPanel.OptionGrid
    html_class: str = None

    def __init__(self, page, components, position: str, width: types.SIZE_TYPE, height: types.SIZE_TYPE,
                 align: str, helper: str, options: types.OPTION_TYPE, profile: types.PROFILE_TYPE,
                 html_code: str = None):
        self.position, self.align = position, align
        super(Row, self).__init__(page, [], css_attrs={"width": width, "height": height},
                                  options=options, profile=profile, html_code=html_code)
        if components is not None:
            for component in components:
                self.add(component)
        self.attr["class"].add('row')
        self.style.css.justify_content = self.position
        if align == 'center':
            self.css({'margin': 'auto'})
        if options.get("size_cols"):
            self.set_size_cols(*options["size_cols"])
        if options.get("width_cols"):
            self.set_width_cols(*options["width_cols"])

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return True

    @property
    def options(self) -> OptPanel.OptionGrid:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def dom(self) -> JsHtmlPanels.JsHtmlRow:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlPanels.JsHtmlRow(self, page=self.page)
        return self._dom

    def set_size_cols(self, *args, break_point: str = "lg"):
        """Set the dimension of the columns in the row container.
        The sum of the various columns should not exceed 12, the max layout in Bootstrap.

        :param args: Integer the size of the different columns.
        :param break_point: Optional. Grid system category, with
          - xs (for phones - screens less than 768px wide)
          - sm (for tablets - screens equal to or greater than 768px wide)
          - md (for small laptops - screens equal to or greater than 992px wide)
          - lg (for laptops and desktops - screens equal to or greater than 1200px wide)
        """
        vals = list(args)
        if len(vals) != len(self.val):
            space_left = 12 - sum(vals)
            cols = len(self.val) - len(vals)
            for i in range(cols):
                vals.append(space_left // cols)
        for i, col in enumerate(self):
            col.set_size(vals[i], break_point=break_point)
        return self

    def set_width_cols(self, *args):
        """Force the width of the different columns in the tow component.

        :param args: The width object (value, unit)
        """
        for i, val in enumerate(list(args)):
            self[i].style.css.width = "%s%s" % (val[0], val[1])
            if val[1] == "px":
                if "col" in self[i].attr["class"]:
                    self[i].attr["class"].remove("col")
                if 'my-auto' in self[i].attr["class"]:
                    self[i].attr["class"].remove("my-auto")
                self[i].attr["class"].add("col-pixel-width-%s" % val[0])
                self[i].aria.custom("responsive", False)
        return self

    def __len__(self):
        return len(self.val)

    def add(self, components: Union[Html.Html, List[Html.Html]], **kwargs):
        """ Add items to a container """
        # hack to propagate the height of the row to the underlying columns
        if not isinstance(components, Col):
            if not isinstance(components, list):
                components = [components]
            components = self.page.ui.layouts.col(
                components, align=self.align, height=(self.css("height"), ''), position=self.position,
                options=self.options._attrs)
            components.style.css.margin_left = "auto"
            components.style.css.margin_right = "auto"
            components.options.managed = False
        super(Row, self).__add__(components)
        return self

    def __str__(self):
        cols = []
        if self.options.noGutters:
            self.attr["class"].add('no-gutters')
        responsive_components = []
        for component in self.val:
            if component.aria.get("responsive", True):
                responsive_components.append(component)
        for i, component in enumerate(self.val):
            if hasattr(component, 'set_size') and self.options.autoSize:
                if component.aria.get("responsive", True):
                    if len(responsive_components) == 1 and len(responsive_components) != len(self.val):
                        component.set_size(None)
                    else:
                        component.set_size(12.0 / len(responsive_components))
            cols.append(component.html() if hasattr(component, 'options') else str(component))
        return '<div %s>%s</div>' % (self.get_attrs(css_class_names=self.style.get_classes()), "".join(cols))


class Grid(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'Grid'
    builder_module = 'BsGrid'
    requirements = ('bootstrap',)
    tag = 'div'
    _option_cls = OptPanel.OptionGrid
    html_class: str = None

    def __init__(self, page: primitives.PageModel, rows: list, width: tuple, height: tuple, align: str, position: str,
                 options: types.OPTION_TYPE, profile: Optional[Union[bool, dict]], html_code: str = None):
        super(Grid, self).__init__(
            page, [], options=options, css_attrs={"width": width, "height": height}, profile=profile, html_code=html_code)
        self.position = position
        self.style.clear(no_default=True)
        self.css({'overflow-x': 'hidden', 'padding': 0})
        self.attr["class"].add(self.options.classe)
        if align == 'center':
            self.css({'margin': 'auto'})
        if rows is not None:
            for row in rows:
                self.__add__(row)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return True

    def build(self, data: types.JS_DATA_TYPES = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None, component_id: Optional[str] = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        self.options.template.options.managed = False
        self.options.template.dom._container = self.dom.varId
        if self.options.pivot is None or self.options.template is None:
            raise Exception("Template and Pivot options must be defined to use the grid builder")

        comp_builder = "%(create)s; %(builder)s" % {
            "create": self.options.template.dom.createWidget(
                html_code=JsUtils.jsWrap("'%s_dyn_' + i" % self.html_code), container=JsUtils.jsWrap("col.id")),
            "builder": self.options.template.build(
                JsUtils.jsWrap("results[keys[i]]"), dataflows=dataflows, component_id=JsUtils.jsWrap("htmlObj.id"),
                profile=profile, stop_state=stop_state)}
        func = "Grid%sBuilder" % abs(hash(comp_builder))
        self.page.properties.js.add_constructor(func, '''function %(fnc)s(container, data, options){ 
container.innerHTML = ""; let results = {}; let componentsHolders = []; let i = 0;
data.forEach(function(row){
  if (!results[row[options.pivot]]){results[row[options.pivot]] = []}; results[row[options.pivot]].push(row)}); 
let keys = Object.keys(results); let rowsNum = Math.ceil(keys.length / options.columns);   
for (let n=0; n < rowsNum; n++) {
    let row = document.createElement("div"); row.setAttribute('class', options.class_row); 
    for (let c=0; c < options.columns; c++) {let k = keys[i];
        if (k){
            let col = document.createElement("div"); col.setAttribute('class', options.class_col); 
            col.id = container.id + "_w_" + i; row.appendChild(col); componentsHolders.push(col); i++;
            let colLabel = document.createElement(options.title_tag); colLabel.innerHTML = k;
            colLabel.setAttribute('class', options.class_title); col.appendChild(colLabel)}};
    container.appendChild(row); if (options.sortable){Sortable.create(row, options.sortable)}
    }; 
    componentsHolders.forEach(function(col, i){let htmlObj = %(comp_builder)s;})}''' % {
            "comp_builder": comp_builder, "fnc": func})
        return "%(fnc)s(%(container)s, %(data)s, %(options)s)" % {
            "fnc": func, "container": self.dom.varId, "data": JsUtils.jsConvertData(data, None),
            "options": self.options.config_js(options)}

    def row(self, n: int):
        return self._vals[n]

    def col(self, n: int):
        cells = [row[n] for row in self._vals]
        return cells

    @property
    def options(self) -> OptPanel.OptionGrid:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def __add__(self, row_data: Union[Row, tuple]):
        """ Add items to a container """
        if isinstance(row_data, Row):
            row = row_data
        else:
            row = self.page.ui.layouts.row(position=self.position, options=self.options._attrs, align=None)
            row.style.clear(no_default=True)
            row.style.css.margin = 'auto'
            row.attr["class"].add("row")
            for component_with_dim in row_data:
                if isinstance(component_with_dim, tuple):
                    component, dim = component_with_dim
                else:
                    component, dim = component_with_dim, None
                row.add(component)
                if dim is not None:
                    row[-1].attr["class"].add("col-%s" % dim)
        super(Grid, self).__add__(row)
        return self

    @property
    def dom(self) -> JsHtmlPanels.JsHtmlGrid:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlPanels.JsHtmlGrid(self, page=self.page)
        return self._dom

    def __str__(self):
        rows = []
        for component in self.val:
            if self._sort_propagate:
                component.sortable(self._sort_options)
            rows.append(component.html())
        return '<%s %s>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), "".join(rows), self.tag)


class Tabs(Html.Html):
    name = 'Tabs'
    _option_cls = OptPanel.OptionPanelTabs
    tag = "div"

    def __init__(self, page: primitives.PageModel, color: str, width: tuple, height: tuple, html_code: Optional[str],
                 helper: Optional[str], options: Optional[dict], profile: Optional[Union[dict, bool]]):
        super(Tabs, self).__init__(page, "", html_code=html_code, profile=profile, options=options,
                                   css_attrs={"width": width, "height": height, 'color': color})
        self.__panels, self.__panel_objs, self.__selected = [], {}, None
        self.tabs_name, self.panels_name = self.sub_html_code("button"), self.sub_html_code("panel")
        self.tabs_container = self.page.ui.div([], html_code=self.sub_html_code("parent"))
        self.tabs_container.options.managed = False
        self.add_helper(helper)

    @property
    def options(self) -> OptPanel.OptionPanelTabs:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def dom(self) -> JsHtmlPanels.JsHtmlTabs:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlPanels.JsHtmlTabs(self, page=self.page)
        return self._dom

    def __getitem__(self, name: str):
        return self.__panel_objs[name]

    def select(self, name: str):
        """Set a value to be selected when the component is created.

        :param name: The selected value
        """
        self.__selected = name
        return self

    def panel(self, name: str):
        """Get the panel object.

        :param name: The tab name
        """
        return self.__panel_objs[name]["content"]

    def tab(self, name: str) -> Div:
        """Get the tab container.

        :param name: The tab name
        """
        return self.__panel_objs[name]["tab"][0]

    def tab_holder(self, name: str) -> Div:
        """Get the tab container.

        :param name: The tab name
        """
        return self.__panel_objs[name]["tab"]

    def tabs(self):
        """Get the tab container. """
        for tab_obj in self.__panel_objs.values():
            yield tab_obj["tab"]

    def add_panel(self, name: str, div: Html.Html = None, icon: str = None, selected: bool = False,
                  css_tab: dict = None, css_tab_clicked: dict = None, width: tuple = None,
                  tooltip: str = None, menu: Html.Html = None):
        """Add a panel / tab to a tabs container.

         https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_display_element_hover

        :param name: The panel name.
        :param div: HTML Component.
        :param icon: Optional.
        :param selected: Optional. Flag to set the selected panel
        :param css_tab: Optional. The CSS attributes to be added to the HTML component
        :param css_tab_clicked: Optional. The CSS attributes to be added to the HTML component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param tooltip: Optional. Add a tooltip to the tab
        :param menu: Optional. Ada a sub panel between the tab and content
        """
        width = Arguments.size(width or self.options.width, unit="px")
        if not hasattr(div, 'options'):
            if div is None:
                div = self.page.ui.div(html_code=self.sub_html_code("panel", auto_inc=True))
                show_div = []
            else:
                div = self.page.ui.div(div, html_code=self.sub_html_code("panel", auto_inc=True))
                show_div = [div.dom.show()]
            div.style.clear(no_default=True)
            div.style.css.padding_left = 3
            div.style.css.padding_right = 3
        else:
            show_div = [div.dom.show()]
        div.css({"display": 'none', "width": "100%"})
        div.options.managed = False
        div.set_attrs(name="name", value=self.panels_name)

        self.__panels.append(name)
        if icon is not None:
            html_code_tab = self.sub_html_code("tab", auto_inc=True)
            tab = self.page.ui.div([
                self.page.ui.icon(icon, html_code="%s_icon" % html_code_tab).css(
                    {"display": 'block', 'color': 'inherit', "width": '100%',
                     "font-size": self.page.body.style.globals.font.normal(4)}),
                name], width=width, html_code=html_code_tab)
        else:
            if hasattr(name, "html"):
                tab = self.page.ui.div(name, width=width, html_code=self.sub_html_code("tab", auto_inc=True))
            else:
                html_code_tab = "%s_%s" % (self.html_code, JsUtils.getJsValid(name, False))
                tab = self.page.ui.div(name, width=width, html_code=html_code_tab)
        tab_style = self.options.tab_style(name, css_tab)
        tab_style_clicked = self.options.tab_clicked_style(name, css_tab_clicked)
        tab.css(tab_style).css({"padding": '2px 0'})
        tab.set_attrs(name="name", value=self.tabs_name)
        tab.set_attrs(name="data-index", value=len(self.__panels) - 1)
        tab_container = self.page.ui.div(tab, width=width)
        tab_container.options.managed = False
        if css_tab:
            tab_container.css(css_tab)
        tab_container.css({'display': 'inline-block'})
        css_cls_name = None
        if tooltip:
            tab.tooltip(tooltip)
        tab.click([
            self.dom.deselect_tabs(),
            tab.dom.setAttribute("data-selected", True).r,
            self.page.js.getElementsByName(self.panels_name).all([
                                                                     tab.dom.css(tab_style_clicked),
                                                                     self.page.js.data.all.element.hide(),
                                                                     tab_container.dom.toggleClass(css_cls_name,
                                                                                                   propagate=True) if css_cls_name is not None else "",
                                                                 ] + show_div)])
        tab.options.managed = False
        self.__panel_objs[name] = {"tab": tab_container, "content": div, "menu": menu}
        if selected:
            self.__selected = name
        return self

    def add_sub_menus(
            self, name: str, values: List[list], width: Tuple[int, str] = (100, "px"), css_attrs: dict = None) -> Div:
        """Add a panel with sub menus.

        Usage::
            p = page.ui.panels.pills(height=60)
            p.add_panel("Pill 1", "test")
            p.add_sub_menus("Pill 1", [[{"text": "col1 %s" % i, "url": "#"} for i in range(10)], [{"text": "col2 %s" % i} for i in range(10)]])

        :param name: Panel's name
        :param values: The list of columns to add to the sub menu
        :param width: Optional. The column width
        :param css_attrs: Optional. Menu panel's CSS attributes
        """
        links = []
        for row in values:
            col_links = []
            for col in row:
                if isinstance(col, dict):
                    a = self.page.ui.link(**col)
                    a.style.css.display = "block"
                    a.style.css.padding = "3px 5px"
                    col_links.append(a)
                else:
                    col_links.append(col)
            links.append(self.page.ui.div(col_links, width=width))
        sub_items = self.page.ui.div(links)
        sub_items.style.css.display = None
        sub_items.style.css.min_height = "150px"
        sub_items.style.css.background = self.page.theme.white
        sub_items.style.css.position = "absolute"
        if not css_attrs:
            sub_items.css(css_attrs)
        self.__panel_objs[name]["tab"].add(sub_items)
        self.__panel_objs[name]["tab"].hover([
            sub_items.dom.css({
                "left": self.__panel_objs[name]["tab"].dom.parentNode.getBoundingClientRect(unit=True).window_left,
                "width": self.__panel_objs[name]["tab"].dom.parentNode.getComputedStyle("width")}).r,
            sub_items.dom.show(display_value="block")])
        self.__panel_objs[name]["tab"].on("mouseout", [sub_items.dom.hide()])
        return sub_items


    def __str__(self):
        if self.__selected is not None:
            self.__panel_objs[self.__selected]["content"].style.css.display = self.options.display
            self.__panel_objs[self.__selected]["tab"][0].css(self.options.tab_clicked_style(self.__selected))
            self.__panel_objs[self.__selected]["tab"][0].attr["data-selected"] = 'true'
        content = []
        self.tabs_container._vals = []
        self.tabs_container.components = {}
        for p in self.__panels:
            self.tabs_container.add(self.__panel_objs[p]["tab"])
            content.append(self.__panel_objs[p]["content"].html())
        return "<%s %s>%s%s</%s>%s" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tabs_container.html(),
            "".join(content), self.tag, self.helper)


class TabsArrowsDown(Tabs):
    name = 'Tabs Arrow Down'

    def add_panel(
            self, name: str, div, icon=None, selected=False, css_tab=None, css_tab_clicked=None, width=None, **kwargs):
        super(TabsArrowsDown, self).add_panel(name, div, icon, selected, css_tab, css_tab_clicked, width)
        self.tab_holder(name).style.add_classes.layout.panel_arrow_down()
        return self


class TabsArrowsUp(Tabs):
    name = 'Tabs Arrow Up'

    def add_panel(
            self, name: str, div, icon=None, selected=False, css_tab=None, css_tab_clicked=None, width=None, **kwargs):
        super(TabsArrowsUp, self).add_panel(name, div, icon, selected, css_tab, css_tab_clicked, width)
        self.tab_holder(name).style.add_classes.layout.panel_arrow_up()
        return self


class IFrame(Html.Html):
    name: str = 'IFrame'
    tag: str = "iframe"
    set_exports: bool = False
    _option_cls = OptPanel.OptionIFrame

    def __init__(self, report, url, width, height, helper, profile, options):
        super(IFrame, self).__init__(report, url, css_attrs={"width": width, "height": height},
                                     profile=profile, options=options)
        self.css({"overflow-x": 'hidden'})
        self.attr["frameborder"] = "0"
        self.attr["scrolling"] = "no"
        self.add_helper(helper)
        self.headers, self.body, self.scripts = [], [], []

    def _load_component(self, component: Html.Html) -> str:
        """Load a component into the Iframe.

        :param component: HTML component to be added to the page
        """
        if hasattr(component, "options"):
            if component.requirements:
                for r in self.page.imports.jsResolve(component.requirements).split("\n"):
                    self.to_header(r, force=True)
                for r in self.page.imports.cssResolve(component.requirements).split("\n"):
                    self.to_header(r, force=True)
            c = {}
            JsUtils.addJsResources(
                c, component.builder_module + ".js", verbose=False,
                required_funcs=treemap._BUILDERS_MAP.get(component.builder_name, []))
            for v in c.values():
                self.options.exts.append(v)
            self.onReady(component.refresh())
            component.options.managed = False
            return component.html()

        return str(component)

    @property
    def options(self) -> OptPanel.OptionIFrame:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def dom(self) -> JsHtmlPanels.JsHtmlIFrame:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtmlPanels.JsHtmlIFrame(self, page=self.page)
        return self._dom

    def scrolling(self, flag: bool = True):
        """
        `Related Pages <https://www.w3schools.com/tags/tag_iframe.ASP>`_

        :param flag: Optional.
        """
        if flag:
            self.style.css.overflow_y = "visible"
            self.attr["scrolling"] = "yes"
        else:
            self.attr["scrolling"] = "no"
        return self

    def sandbox(self, text: str):
        """
        `Related Pages <https://www.w3schools.com/tags/att_iframe_sandbox.asp>`_

        :param text: Enables an extra set of restrictions for the content in an <iframe>
        """
        self.attr["sandbox"] = text
        return self

    def allowfullscreen(self, flag: bool = True):
        """
        `Related Pages <https://www.w3schools.com/tags/tag_iframe.ASP>`_

        :param flag: optional. The <iframe> can activate fullscreen mode by calling the requestFullscreen() method
        """
        self.attr["allowfullscreen"] = 'true' if flag else 'false'
        return self

    def referrerpolicy(self, text: str):
        """
        `Related Pages <https://www.w3schools.com/tags/att_iframe_referrerpolicy.asp>`_

        :param text:
        """
        self.attr["referrerpolicy"] = text
        return self

    def setEventListener(self, event: str, source, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Add an event to the document ready function. This is to mimic the Jquery on function.

        :param event: The Javascript event type from the dom_obj_event.asp
        :param source: The source component for the event
        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        """
        event = JsUtils.jsConvertData(event, None)
        self.onReady(["%s.addEventListener(%s, function(event) {%s})" % (
            source.dom.varId, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))])

    def to_header(self, aliases: List[str], force: bool = False, need_exports: bool = False):
        """Set the IFrame header section.

        :param aliases: External JavaScript and CSS packages
        :param force: For the alias to be added as a string
        :param need_exports:
        """
        self.options.srcFunc = "srcdoc"
        self.set_exports = self.set_exports or need_exports
        if force:
            self.headers.extend(aliases)
            self.options.header.extend(aliases)
        else:
            scripts = self.page.imports.jsResolve(aliases)
            if scripts:
                self.headers.append(scripts.replace("\n", ""))
                self.options.header.append(scripts.replace("\n", ""))
            scripts = self.page.imports.cssResolve(aliases)
            if scripts:
                self.headers.append(scripts.replace("\n", ""))
                self.options.header.append(scripts.replace("\n", ""))
        return self

    def to_body(self, components: Union[Html.Html, List[Html.Html]]):
        """Update the static HTML definition of the IFrame.
        Components added to the IFrame should be fully defined before added to the body.

        :param components: List of HTML components
        """
        self.options.srcFunc = "srcdoc"
        if isinstance(components, list):
            components = [self._load_component(c) for c in components]
            self.body.extend(components)
            self.options.body.extend(components)
        else:
            components = self._load_component(components)
            self.body.append(components)
        return self

    def onReady(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Add JavaScript function to the script body in the IFrame.

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        """
        self.options.srcFunc = "srcdoc"
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]

        js_funcs_str = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self.scripts.append(js_funcs_str)
        self.options.script.append(js_funcs_str)
        return self

    def __str__(self):
        if self.options.srcFunc == "srcdoc":
            self.attr["srcdoc"] = self.dom.get_doc().toStr()
        return "<%s src='%s' %s></%s>%s" % (
            self.tag, self.val, self.get_attrs(css_class_names=self.style.get_classes()), self.tag, self.helper)


class IconsMenu(Html.Html):
    name = 'Icons Menu'
    tag = "div"

    def __init__(self, icon_names: list, page: primitives.PageModel, width, height, html_code, helper, profile):
        super(IconsMenu, self).__init__(
            page, None, css_attrs={"width": width, "height": height}, html_code=html_code, profile=profile)
        self._jsActions, self._definedActions = {}, []
        self._icons, self.icon = [], None
        self.css({"margin": "5px 0"})
        for icon_name in icon_names:
            self.add_icon(icon_name)

    @classmethod
    def get_requirements(cls, page: primitives.PageModel, options: types.OPTION_TYPE = None) -> tuple:
        """Update requirements with the defined Icons' family.

        :param page: Page context
        :param options: Component input options
        """
        if options and options.get('icon_family') is not None:
            return (options['icon_family'],)

        return (page.icons.family,)

    def __getitem__(self, i):
        return self._icons[i]

    def add_icon(self, text: str, css: Optional[dict] = None, position: str = "after", family: Optional[str] = None,
                 html_code: Optional[str] = None, **kwargs):
        """Add an icon to the HTML object.

        Usage::
          checks.title.add_icon("fas fa-align-center")

        :param text: The icon reference from font-awesome website
        :param css: Optional. A dictionary with the CSS style to be added to the component
        :param position: Optional. The position compared to the main component tag
        :param family: Optional. The icon framework to be used (preferred one is font-awesome)
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        """
        defined_families = ('office-ui-fabric-core', 'material-design-icons')
        if family is not None and self.options.verbose and family not in defined_families:
            logging.warning("Family %s not defined in %s" % (family, defined_families))

        if text is not None:
            html_code_icon = self.sub_html_code("icon")
            self._icons.append(self.page.ui.images.icon(text, html_code=html_code_icon, family=family).css(
                {"margin-right": '5px', 'cursor': "pointer"}))
            self.icon = self._icons[-1]
            if position == "before":
                self.prepend_child(self.icon)
            else:
                self.append_child(self.icon)
            if css is not None:
                self.icon.css(css)
        return self

    def add_select(self, action: str, data, width: int = 150):
        """
        :param action:
        :param data:
        :param int width:
        """
        options = ["<option>%s</option>" % d for d in data]
        self._jsActions[
            action] = '<select id="inputState" class="form-control" style="width:%spx;display:inline-block">%s</select>' % (
            width, "".join(options))
        self._definedActions.append(action)
        return self

    def __str__(self):
        html_icons = [htmlDef for action, htmlDef in self._jsActions.items()]
        return "<%s %s>%s</%s>" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), "".join(html_icons), self.tag)


class Form(Html.Html):
    name = 'Generic Form'
    tag = "form"

    def __init__(self, page: primitives.PageModel, components: List[Html.Html], helper: Optional[str]):
        super(Form, self).__init__(page, [])
        self.style.css.padding = "5px"
        self.method, self.action, self.label = None, None, None
        self.add_helper(helper)
        self.__submit, self._has_container = None, False
        for i, component in enumerate(components):
            self.__add__(component)

    def __add__(self, component: Html.Html):
        """Add items to a container"""
        component.css({'text-align': 'left'})
        super(Form, self).__add__(component)
        return self

    def extend(self, components: List[Html.Html]):
        """Add multiple HTML components to the container.

        :param components: The list of components
        """
        for component in components:
            self.add(component)
        return self

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self.__submit is None:
            self.submit(self.method, self.action, self.label)

    def submit(self, method: str = None, action: str = None, text: str = None):
        """ Add a submit event to the form.

        :param method: Optional. The method used to transfer data
        :param action: Optional. The end point for submitting
        :param text: Optional. The text on the submit button
        """
        self.attr.update({"action": action or self.action, "method": method or self.method})
        self.__submit = self.page.ui.button(text, html_code=self.sub_html_code("button")).set_attrs({"type": 'submit'})
        self.__submit.style.css.margin_top = 10
        self.__submit.options.managed = False
        if self._has_container:
            self[0].add(self.__submit)
        return self

    def __str__(self):
        if self.__submit is None:
            raise ValueError("Submit must be defined in a form ")

        str_vals = "".join([i.html() for i in self.val]) if self.val is not None else ""
        return '<%s %s>%s%s</%s>%s' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_vals, self.__submit.html(),
            self.tag, self.helper)


class Modal(Html.Html):
    name = 'Modal Popup'
    tag = 'div'

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-popup.css",
    ]

    style_refs = {
        "html-popup": "html-popup",
        "html-popup-background": "html-popup-background",
        "html-popup-nobackground": "html-popup-nobackground",
        "html-popup-window": "html-popup-window",
        "html-popup-body": "html-popup-body",
        "html-popup-container": "html-popup-container",
        "html-popup-close": "html-popup-close",
    }

    def __init__(
            self, page: primitives.PageModel, components: List[Html.Html], header, footer, submit, helper,
            html_code = None, options = None):
        """Constructor for the modal item.
        This object is composed of three parts: a header, which is a row of object, a body which is a column and a footer
        which is a row they all accept collections of html objects and are configurable just like the normal rows and
        column objects.
        """
        options = options or {}
        super(Modal, self).__init__(page, [], html_code=html_code)
        self.add_helper(helper)
        self.doSubmit = submit
        if self.doSubmit:
            self.submit = page.ui.buttons.important("Submit", html_code=self.sub_html_code("button")).set_attrs({
                "type": 'submit'})
            self.submit.options.managed = False
        self.closeBtn = page.ui.texts.span('&times', width='auto', html_code=self.sub_html_code("close"))
        self.closeBtn.css(None, reset=True)
        self.closeBtn.style.add_classes.div.span_close()
        self.closeBtn.click(page.js.getElementById(self.htmlCode).css({'display': "none"}))
        self.__header = page.ui.row([])
        self.__header.options.managed = False
        if header:
            for obj in header:
                self.__header + obj
        self.__header += self.closeBtn
        if footer:
            for obj in footer:
                self.__footer + obj
        self.__footer = page.ui.row([], html_code=self.sub_html_code("footer"))
        self.__footer.options.managed = False
        self.__body = page.ui.col([], html_code=self.sub_html_code("body")).css({
            'position': 'relative', 'overflow-y': 'scroll'})
        self.__body.options.managed = False
        self.col = page.ui.col([self.__header, self.__body, self.__footer], html_code=self.sub_html_code("col")).css({
            'width': 'auto'}, reset=True)
        self.col.style.add_classes.div.modal_content()
        self.col.style.css.margin_top = "10% !IMPORTANT"
        self.col.options.managed = False
        self.val.append(self.col)
        self.__outOfScopeClose = True
        self.classList.add("html-popup-background")
        for component in components:
            self.__add__(component)

    @property
    def outOfScopeClose(self):
        return self.__outOfScopeClose

    @outOfScopeClose.setter
    def outOfScopeClose(self, val):
        self.__outOfScopeClose = val

    @property
    def style(self) -> GrpClsContainer.ClassModal:
        """Property to the CSS Style of the component."""
        if self._styleObj is None:
            self._styleObj = GrpClsContainer.ClassModal(self)
        return self._styleObj

    @property
    def header(self):
        return self.__header

    @property
    def footer(self):
        return self.__footer

    @property
    def body(self):
        return self.__body

    def show(self):
        return self.page.js.getElementById(self.htmlCode).css({'display': 'block'})

    def close(self):
        return self.page.js.getElementById(self.htmlCode).css({'display': 'none'})

    def close_on_background(self):
        """Will allow an event to close the modal if a click event is detected anywhere outside the modal."""
        modal = self.page.js.getElementById(self.htmlCode)
        self.page.js.onReady(self.page.js.window.events.addClickListener(
            self.page.js.if_('event.target == %s' % modal, modal.css({'display': 'none'})), sub_events=['event']))

    def __add__(self, component: Html.Html):
        """ Add items to a container """
        # Has to be defined here otherwise it is set too late
        component.options.managed = False
        self.__body += component
        return self

    def __str__(self):
        if self.__outOfScopeClose:
            self.close_on_background()
        str_vals = "".join([i.html() for i in self.val]) if self.val is not None else ""
        self.set_attrs({'css': self.style.css.attrs})
        if self.doSubmit:
            self.col += self.submit
        return '<%s %s>%s</%s>%s' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_vals, self.tag, self.helper)


class Indices(Html.Html):
    name = 'Index'
    _option_cls = OptPanel.OptionsPanelPoints
    tag = 'div'

    def __init__(self, page: primitives.PageModel, count: int, width: tuple, height: tuple, html_code: str,
                 options: dict, profile: Optional[Union[dict, bool]]):
        super(Indices, self).__init__(page, count, html_code=html_code, profile=profile, options=options,
                                      css_attrs={"width": width, "height": height})
        self.items = []
        for i in range(count):
            div = self.page.ui.div(i, width=(15, "px"), html_code=self.sub_html_code("item_%s" % i))
            div.attr["name"] = self.html_code
            div.attr["data-position"] = i + 1
            div.css({"display": 'inline-block', "padding": "2px", "text-align": "center"})
            div.css(self.options.div_css)
            div.style.add_classes.div.background_hover()
            div.options.managed = False
            self.items.append(div)

        self.first = self.page.ui.icon(
            "fas fa-angle-double-left", width=(20, 'px'),
            html_code=self.sub_html_code("icon_first")).css({"display": 'inline-block'})
        self.first.options.managed = False
        self.prev = self.page.ui.icon(
            "fas fa-chevron-left", width=(20, 'px'),
            html_code=self.sub_html_code("icon_prev")).css({"display": 'inline-block'})
        self.prev.options.managed = False
        self.next = self.page.ui.icon("fas fa-chevron-right", width=(20, 'px'),
                                      html_code=self.sub_html_code("icon_next")).css({"display": 'inline-block'})
        self.next.options.managed = False
        self.last = self.page.ui.icon("fas fa-angle-double-right", width=(20, 'px'),
                                      html_code=self.sub_html_code("icon_last")).css({"display": 'inline-block'})
        self.last.options.managed = False

    @classmethod
    def get_requirements(cls, page: primitives.PageModel, options: types.OPTION_TYPE = None) -> tuple:
        """Update requirements with the defined Icons' family.

        :param page: Page context
        :param options: Component input options
        """
        if options and options.get('icon_family') is not None:
            return (options['icon_family'],)

        return (page.icons.family,)

    @property
    def options(self) -> OptPanel.OptionsPanelPoints:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def __getitem__(self, i: int) -> Html.Html:
        return self.items[i]

    def click_item(self, i: int, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """

        :param i:
        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        return self[i].on("click", [
            self[i].dom.by_name.css({"border-bottom": "1px solid %s" % self.page.theme.colors[0]}).r,
            self[i].dom.css({"border-bottom": "1px solid %s" % self.options.background_color})] + js_funcs, profile)

    def __str__(self):
        str_vals = "".join([self.first.html(), self.prev.html()] + [i.html() for i in self.items] + [
            self.next.html(), self.last.html()])
        return '<%s %s>%s</%s>%s' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_vals, self.tag, self.helper)


class Points(Html.Html):
    name = 'Index'
    _option_cls = OptPanel.OptionsPanelPoints
    tag = 'div'

    def __init__(self, page: primitives.PageModel, count: int, width: tuple, height: tuple, html_code: str,
                 options: dict, profile: Union[dict, bool]):
        super(Points, self).__init__(page, count, html_code=html_code, profile=profile, options=options,
                                     css_attrs={"width": width, "height": height})
        self.items = []
        self.css({"text-align": "center"})
        for i in range(count):
            div = self.page.ui.div(self.page.entities.non_breaking_space, html_code=self.sub_html_code("item_%s" % i))
            div.attr["name"] = html_code
            div.attr["data-position"] = i
            div.css({"border": "1px solid %s" % self.page.theme.greys[5], "border-radius": "10px", "width": "15px",
                     "height": "15px"})
            div.css(self.options.div_css)
            div.style.add_classes.div.background_hover()
            div.options.managed = False
            self.items.append(div)
        self.items[self.options.selected].css({"background-color": self.options.background_color})

    @property
    def options(self) -> OptPanel.OptionsPanelPoints:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def on(self, event: str, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
           source_event: Optional[str] = None, on_ready: bool = False, **kwargs):
        """Add Javascript events to all the items in the component.

        `Related Pages <https://www.w3schools.com/jsref/obj_events.asp>`_

        :param str event: The event type for an HTML object
        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_fnc = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if event == "click":
            for i in range(len(self.items)):
                self.click_item(i, str_fnc)
        else:
            for i in range(len(self.items)):
                self.on_item(i, event, str_fnc)
        return self

    def on_item(self, i: int, event: Union[list, str], js_funcs: types.JS_FUNCS_TYPES,
                profile: types.PROFILE_TYPE = False, source_event: Optional[str] = None,
                on_ready: bool = False):
        """Add specific event on the container items.

        :param i: The item index in the container
        :param event: The Javascript event type from the dom_obj_event.asp
        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        return self[i].on(event, [
            'var data = {position: this.getAttribute("data-position")}'] + js_funcs, profile, source_event, on_ready)

    def click_item(self, i: int, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                   on_ready: bool = False):
        """Add a click event on a particular item of the component.

        :param i: The item index
        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        return self.items[i].click([
                                       'var data = {position: this.getAttribute("data-position")}',
                                       self.items[i].dom.by_name.css({"background-color": ""}).r,
                                       self.items[i].dom.css(
                                           {"background-color": self.options.background_color})] + js_funcs, profile,
                                   on_ready=on_ready)

    def __getitem__(self, i: int) -> Html.Html:
        return self.items[i]

    def __str__(self):
        str_vals = "".join([i.html() for i in self.items])
        return '<%s %s>%s</%s>%s' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_vals, self.tag, self.helper)


class Header(Html.Html):
    name = 'Header'
    _option_cls = OptPanel.OptionsDiv
    tag = "header"

    def __init__(self, page: primitives.PageModel, component: primitives.HtmlModel, width: tuple, height: tuple,
                 html_code: str, helper: str, options: dict, profile: Union[dict, bool]):
        super(Header, self).__init__(page, component, html_code=html_code, profile=profile, options=options,
                                     css_attrs={"width": width, "height": height})
        self.add_helper(helper)

    @property
    def options(self) -> OptPanel.OptionsDiv:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def __add__(self, component: Html.Html):
        """ Add items to a container """
        # Has to be defined here otherwise it is set to late
        component.options.managed = False
        if self.options.inline:
            component.style.css.display = 'inline-block'
        self.val.append(component)
        return self

    def __str__(self):
        str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
        return "<%s %s>%s</%s>%s" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_div, self.tag, self.helper)


class Section(Html.Html):
    name = 'Section'
    _option_cls = OptPanel.OptionsDiv
    tag = "section"

    def __init__(self, page: primitives.PageModel, component: Union[Html.Html, List[Html.Html]], width: tuple,
                 height: tuple,
                 html_code: str, helper: str, options: dict, profile: Union[dict, bool]):
        super(Section, self).__init__(page, component, html_code=html_code, profile=profile, options=options,
                                      css_attrs={"width": width, "height": height})
        self.add_helper(helper)

    @property
    def options(self) -> OptPanel.OptionsDiv:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def __add__(self, component: Html.Html):
        """ Add items to a container """
        if self.options.inline:
            component.style.css.display = 'inline-block'
        super(Section, self).__add__(component)
        return self

    def __str__(self):
        str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
        return "<%s %s>%s</%s>%s" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_div, self.tag, self.helper)


class GridStack(Html.Html):
    name = 'Gridstack'
    requirements = ('gridstack',)
    _option_cls = OptGridstack.OptionsGridStack
    tag = "div"

    def __init__(self, page: primitives.PageModel, rows: Union[Html.Html, List[Html.Html]], width: tuple, height: tuple,
                 html_code: str, options: dict, profile: Union[dict, bool]):
        super(GridStack, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                        css_attrs={"width": width, "height": height})
        self.style.add("grid-stack")

    def change(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, on_ready: bool = False):
        """Javascript event triggered when the value has changed.

        :param js_funcs: Set of Javascript function to trigger on this event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_funcs.insert(0, "let data = items")
        return self.on("change", js_funcs, profile, self.html_code, on_ready, func_args=["items"], method="on")

    def add_item(self, component, w: int = None, h: int = None, attrs: dict = None) -> Div:
        """Add a component to the grid

        :param component: The HTML component
        :param w: The number of columns for the width (0 to 12)
        :param h: The number of columns for the height (0 to 12)
        :param attrs: Any other item attributes
        """
        grid_stack_item_content = self.page.ui.div([component], html_code=self.sub_html_code("content"))
        grid_stack_item_content.style.add("grid-stack-item-content")
        grid_stack_item = self.page.ui.div([grid_stack_item_content], html_code=self.sub_html_code("item"))
        grid_stack_item.style.add("grid-stack-item")
        grid_stack_item.options.managed = False
        if w is not None:
            grid_stack_item.attr["gs-w"] = w
        if h is not None:
            grid_stack_item.attr["gs-h"] = h
        if attrs:
            for k, v in attrs.items():
                if not k.startswith("gs-"):
                    k = "gs-%s" % k
                grid_stack_item.attr[k] = v
        self.val.append(grid_stack_item)
        return grid_stack_item

    @property
    def options(self) -> OptGridstack.OptionsGridStack:
        """Property to set all the possible object for a gridstack"""
        return super().options

    @property
    def js(self) -> JsGridstack.GS:
        """Gridstack javascript API"""
        if self._js is None:
            self._js = JsGridstack.GS(self, page=self.page, js_code=self.html_code)
        return self._js

    def __str__(self):
        self.page.properties.js.add_builders(self.js.init_())
        str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
        return "<%s %s>%s</%s>%s" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_div, self.tag, self.helper)
