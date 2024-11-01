#!/usr/bin/python
# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.html import Html

from epyk.core.js import expr
from epyk.core.css import Selector

from epyk.core.html import Defaults
from epyk.core.html.options import OptPanel
from epyk.core.css.styles import GrpClsContainer
from epyk.core.js.html import JsHtmlStepper


class Drawer(Html.Html):
    name = 'Drawer'
    _option_cls = OptPanel.OptionDrawer

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-drawer.css",
    ]

    style_refs = {
        "html-drawer": "html-drawer",
        "html-drawer-panels": "html-drawer-panels",
        "html-drawer-handle": "html-drawer-handle",
        "html-drawers": "html-drawers",
        "html-drawer-panel": "html-drawer-panel",
        "html-drawer-link": "html-drawer-link",
    }

    def __init__(self, page: primitives.PageModel, width: tuple, height: tuple, options: Optional[dict],
                 helper: Optional[str], profile: Optional[Union[dict, bool]], verbose: bool = False):
        super(Drawer, self).__init__(page, None, profile=profile, options=options,
                                     css_attrs={"width": width, "height": height}, verbose=verbose)
        self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
        self.classList.add(self.style_refs["html-drawer"])

        self.panels = page.ui.div(html_code=self.sub_html_code("panels"))
        self.panels.options.managed = False
        self.panels.classList.add(self.style_refs["html-drawer-panels"])
        self.panels.attr['name'] = 'drawer_panels'

        self.handle = page.ui.div(html_code=self.sub_html_code("handle"))
        self.handle.style.clear_all()
        self.handle.classList.add(self.style_refs["html-drawer-handle"])
        self.handle.options.managed = False
        self.handle.attr['name'] = 'drawer_handle'

        self.drawers = page.ui.div(html_code=self.sub_html_code("drawers"))
        self.drawers.style.clear_all()
        self.drawers.classList.add(self.style_refs["html-drawers"])
        self.drawers.options.managed = False
        self.drawers.attr['name'] = 'drawer_content'

    @property
    def dom(self) -> JsHtmlStepper.Drawer:
        """Property to get the common dom features. """
        if self._dom is None:
            self._dom = JsHtmlStepper.Drawer(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptPanel.OptionDrawer:
        """Property to set all the possible object for a drawer. """
        return super().options

    def add_panel(self, link: Union[Html.Html, str], container: Html.Html, display: bool = False):
        """Add panel to the drawer object.

        :param link: The value in the drawer
        :param container: The component to be displayed
        :param display: Optional. The CSS Display property
        """
        if not hasattr(link, 'options'):
            link = self.page.ui.div(link, html_code=self.sub_html_code("link", auto_inc=True))
            link.classList.add(self.style_refs["html-drawer-link"])
            link.options.managed = False
        if not hasattr(container, 'options'):
            container = self.page.ui.div(container, html_code=self.sub_html_code("panel", auto_inc=True))
        container.style.css.display = display
        container.options.managed = False
        self.panels += container
        self.drawers += link
        return container

    def set_handle(self, component: Html.Html):
        """Set the handle used to trigger the open / close events.

        :param component: An HTML component.
        """
        self.handle = self.page.ui.div(html_code=self.sub_html_code("handle"))
        self.handle.style.clear_all()
        if self.options.side == 'left':
            component.click([self.drawers.dom.toggle_transition("margin-right", "0px", "-%s" % self.options.width)])
        else:
            component.click([self.drawers.dom.toggle_transition("margin-left", "0px", "-%s" % self.options.width)])

    def __str__(self):
        self.handle.style.css.float = self.options.side
        if self.options.side == 'left':
            if self.options.push:
                self.drawers.style.css.width = 0
                self.panels.style.css.margin_right = 0
                self.handle.on(self.options.trigger, [
                    self.panels.dom.toggle_transition("margin-right", "0px", self.options.width),
                    self.panels.dom.toggle_transition("width", self.panels.style.css.width, "calc(%s - %s)" % (
                        self.panels.style.css.width, self.options.width)),
                    self.drawers.dom.toggle_transition("width", "0px", self.options.width),
                ])
            else:
                self.drawers.style.css.width = self.options.width
                self.drawers.style.css.margin_right = "-%s" % self.options.width
                self.handle.on(
                    self.options.trigger, [
                        self.drawers.dom.toggle_transition("margin-right", "0px", "-%s" % self.options.width)])
        else:
            if self.options.push:
                self.drawers.style.css.width = 0
                self.panels.style.css.margin_left = 0
                self.handle.on(self.options.trigger, [
                    self.panels.dom.toggle_transition("margin-left", "0px", self.options.width),
                    self.panels.dom.toggle_transition("width", self.panels.style.css.width, "calc(%s - %s)" % (
                        self.panels.style.css.width, self.options.width)),
                    self.drawers.dom.toggle_transition("width", "0px", self.options.width),
                ])
            else:
                self.drawers.style.css.width =  self.options.width
                self.drawers.style.css.margin_left = "-%s" % self.options.width
                self.handle.on(self.options.trigger, [
                    self.drawers.dom.toggle_transition("margin-left", "0px", "-%s" % self.options.width),
                ])
        position = {"left": 'right', 'right': 'left'}
        return '''<div %(attr)s>%(panels)s<div name='drawer' class='%(cls)s' style='%(side)s:0'>
%(helper)s%(handle)s%(drawer)s</div></div>''' % {
            'attr': self.get_attrs(css_class_names=self.style.get_classes()), 'htmlCode': self.html_code,
            'drawer': self.drawers.html(), 'handle': self.handle.html(), 'panels': self.panels.html(),
            'side': position[self.options.side], 'helper': self.helper, "cls": self.style_refs["html-drawer-panel"]}


class DrawerMulti(Html.Html):
    name = 'Multi Drawers'
    _option_cls = OptPanel.OptionDrawer

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-drawer.css",
    ]

    style_refs = {
        "html-drawer": "html-drawer",
        "html-drawer-panels": "html-drawer-panels",
        "html-drawers": "html-drawers",
        "html-drawer-large-handle": "html-drawer-large-handle",
        "html-drawer-panel": "html-drawer-panel",
        "html-drawer-links": "html-drawer-links",
    }

    def __init__(self, page: primitives.PageModel, component: Html.Html, width: tuple, height: tuple,
                 options: Optional[dict], helper: Optional[str], profile: Optional[Union[bool, dict]],
                 verbose: bool = False):
        super(DrawerMulti, self).__init__(page, None, options=options, css_attrs={"width": width, "height": height},
                                          profile=profile, verbose=verbose)
        self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
        self.classList.add(self.style_refs["html-drawer"])

        if not component:
            self.panels = page.ui.div(html_code=self.sub_html_code("panels"))
        else:
            self.panels = component
        self.panels.options.managed = False
        self.panels.classList.add(self.style_refs["html-drawer-panels"])
        self.panels.style.css.display = "inline-block"

        self.handle = page.ui.div(html_code=self.sub_html_code("handle"))
        self.handle.style.clear_all()
        self.handle.classList.add(self.style_refs["html-drawer-large-handle"])
        self.handle.style.css.z_index = 10
        self.handle.style.css.position = 'relative'

        self.handle.options.managed = False
        self.handle.attr['name'] = 'drawer_handle'

        self.drawers = page.ui.div(html_code=self.sub_html_code("drawers"))
        self.drawers.style.clear_all()
        self.drawers.classList.add(self.style_refs["html-drawers"])
        self.drawers.options.managed = False
        self.drawers.attr['name'] = 'drawer_content'

    @property
    def dom(self) -> JsHtmlStepper.Drawer:
        """Property to get the common dom features. """
        if self._dom is None:
            self._dom = JsHtmlStepper.Drawer(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptPanel.OptionDrawer:
        """Property to set all the possible object for a drawer. """
        return super().options

    def add_drawer(self, link: Union[str, Html.Html], container: Html.Html):
        """Add panel to the drawer object.

        :param link: The value in the drawer
        :param container: The component to be displayed
        """
        if not hasattr(link, 'options'):
            link = self.page.ui.div(link, html_code=self.sub_html_code("link", auto_inc=True))
        link.classList.add(self.style_refs["html-drawer-links"])
        link.style.css.color = self.page.theme.colors[0]
        link.options.managed = False
        if not hasattr(container, 'options'):
            container = self.page.ui.div(container, html_code=self.sub_html_code("panel", auto_inc=True))
            container.style.css.padding = 5
        container.options.managed = False
        self.handle += link
        self.drawers += container
        link.click([
            self.page.js.querySelectorAll(
                Selector.Selector(self.drawers).with_child_element("div").excluding(container)).css(
                {"display": 'none'}),
            expr.if_(self.panels.dom.getAttribute("data-panel") == container.htmlCode, [
                self.drawers.dom.toggle_transition(
                    "margin-right" if self.options.side == 'left' else "margin-left", "-%s" % self.options.width,
                    "0px"),
                container.dom.css({"display": 'none'}),
                self.panels.dom.setAttribute("data-panel", '')])
            .else_([
                expr.if_(self.page.js.querySelector(Selector.Selector(self.drawers)).css("margin-left") != "0px", [
                    self.drawers.dom.toggle_transition(
                        "margin-right" if self.options.side == 'left' else "margin-left", "0px",
                        "-%s" % self.options.width),
                ]),
                self.panels.dom.setAttribute("data-panel", container.htmlCode),
                container.dom.css({'display': 'block'})
            ])
        ])
        return self

    def __str__(self):
        self.handle.style.css.float = self.options.side
        if self.options.side == 'left':
            self.drawers.style.css.width = self.options.width
            self.drawers.style.css.margin_right = "-%s" % self.options.width
        else:
            self.drawers.style.css.width = self.options.width
            self.drawers.style.css.margin_left = "-%s" % self.options.width
        return '''<div %(attr)s>%(panels)s<div name='drawer' class='%(cls)s' style='%(side)s:0'>
%(drawer)s</div>%(handle)s</div>''' % {
            'attr': self.get_attrs(css_class_names=self.style.get_classes()), 'htmlCode': self.html_code,
            'drawer': self.drawers.html(), 'handle': self.handle.html(), 'panels': self.panels.html(),
            'side': self.options.side, "cls": self.style_refs["html-drawer-panel"]}
