#!/usr/bin/python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Union, Optional, List
from epyk.core.py import primitives

import collections

from epyk.core.html import Html

from epyk.core.js import expr
from epyk.core.css import Selector
from epyk.core.css import Defaults_css

# The list of CSS classes
from epyk.core.css.styles import GrpClsMenu
from epyk.core.html.HtmlList import Li
from epyk.core.html.options import OptList, OptNavigation


class HtmlNavBar(Html.Html):
    name = 'Nav Bar'
    _option_cls = OptNavigation.OptionsBar

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-navbar.css"
    ]

    style_refs = {
        "html-navbar": "html-navbar",
        "html-navbar-horizontal": "html-navbar-horizontal",
        "html-navbar-vertical": "html-navbar-vertical",
        "html-navbar-title": "html-navbar-title",
        "html-navbar-subtitle": "html-navbar-subtitle",
        "html-navbar-logo": "html-navbar-logo",
        "html-navbar-scroll": "html-navbar-scroll",
        "html-navbar-item": "html-navbar-item",
        "html-navbar-item-h": "html-navbar-item-h",
        "html-navbar-item-v": "html-navbar-item-v",
        "html-navbar-panel": "html-navbar-panel",
        "html-navbar-panel-right": "html-navbar-panel-right",
    }

    def __init__(self, page: primitives.PageModel, components: Optional[List[Html.Html]], logo: str, title: str,
                 avatar: Union[bool, str], size: tuple, options: Optional[dict], html_code: str,
                 profile: Optional[Union[dict, bool]]):
        self.avatar, self.status = None, None
        super(HtmlNavBar, self).__init__(page, [], html_code=html_code, profile=profile, options=options)
        self.classList.add(self.style_refs["html-navbar"])
        self.background, self.logo = True, None
        self.options.size = size

        # Logo
        if logo is None:
            self.logo = self.page.ui.icons.epyk()
            self.logo.style.clear_all(True, False)
        else:
            if not hasattr(logo, 'options'):  # if it is not an option it is considered as a path
                logo_url = logo
                self.logo = self.page.ui.div()
                self.logo.style.clear_all(True, False)

                if logo_url:
                    self.logo.style.css.background_url(logo_url)
            else:
                self.logo = logo
        self.logo.options.managed = False
        self.logo.classList.add(self.style_refs["html-navbar-logo"])
        self.val.append(self.logo)
        self.logo.tooltip(title)

        # Title component
        #title = self.__format_text(title, self.page.body.style.globals.font.normal(5), italic=False)
        self.title = self.page.ui.div(title, html_code=self.sub_html_code("title"))
        self.title.style.clear_all(True, False)
        self.title.options.managed = False
        self.title.classList.add(self.style_refs["html-navbar-title"])
        self.val.append(self.title)

        self.panel = self.page.ui.div([], html_code=self.sub_html_code("panel", auto_inc=True))
        self.panel.style.clear_all(True, False)
        self.panel.classList.add(self.style_refs["html-navbar-panel"])
        self.panel.options.managed = False

        self.settings = self.page.ui.div(html_code=self.sub_html_code("right", auto_inc=True))
        self.settings.style.clear_all(True, False)
        self.settings.classList.add(self.style_refs["html-navbar-panel-right"])
        self.settings.options.managed = False

        if components is not None:
            if not isinstance(components, list):
                components = [components]
            for c in components:
                self.__add__(c)

        self.buttons = []
        self.options.avatar = avatar

    @property
    def options(self) -> OptNavigation.OptionsBar:
        """Component options"""
        return super().options

    def move(self):
        """Move the object to this position in the final page. """
        super(HtmlNavBar, self).move()
        self.style.css.position = None
        return self

    def __add__(self, component: Html.Html):
        """Add items to the footer """
        if not hasattr(component, 'options'):
            component = self.page.ui.div(component, html_code=self.sub_html_code("menu", auto_inc=True))
            component.style.add_classes.div.color_hover()
        component.classList.add(self.style_refs["html-navbar-item-%s" % self.options.orient[0]])
        # Has to be defined here otherwise it is set to late
        component.options.managed = False
        if component.css('height') is None:
            component.style.css.vertical_align = 'middle'
        if component.css('width') == '100%':
            component.style.css.width = None
        self.panel.val.append(component)
        if hasattr(self, 'buttons'):
            self.buttons.append(component)
        return self

    def no_background(self, to_top: bool = True):
        """Remove the default navigation bar background and remove the padding.

        :param to_top: Optional. To define if the padding must be removed
        """
        self.background = False
        self.style.css.background_color = "#11ffee00"
        self.style.css.border_bottom = None
        if to_top:
            self.page.body.style.css.padding_top = 0
        return self

    def set_theme(self):
        """Set a default style for the component with background and border bottom"""
        self.style.css.background_color = self.page.theme.colors[0]
        self.style.css.border_bottom = "1px solid %s" % self.page.theme.greys[0]
        return self

    def add_right(self, component: Union[Html.Html, List[Html.Html]], css: Optional[dict] = None, prepend: bool = False,
                  with_css_cls: bool = True) -> Html.Html:
        """Add component to the right.

        :param component: Internal component to the framework
        :param css: Optional. The CSS attributes
        :param prepend: Optional
        :param with_css_cls: Add the default hover CSS class to the component
        """
        if isinstance(component, list):
            component = self.page.ui.div(component, html_code=self.sub_html_code("menu", auto_inc=True))
            component.style.clear(no_default=True)
            component.classList.add(self.style_refs["html-navbar-item"])
            component.options.managed = False
            if css is not None:
                component.css(css)

        if not hasattr(component, 'options'):
            component = self.page.ui.text(
                component, width=("auto", ''), html_code=self.sub_html_code("menu", auto_inc=True))
            component.classList.add(self.style_refs["html-navbar-item"])
            component.options.managed = False
            if css is not None:
                component.css(css)
        if with_css_cls:
            component.style.add_classes.div.color_hover()
        component.style.css.color = self.page.theme.greys[self.page.theme.index]
        if prepend:
            self.settings.insert(0, component)
        else:
            self.settings.add(component)
        self.buttons.append(component)
        return component

    def add_text(self, text: Union[Html.Html, str]) -> Html.Html:
        """Add an item to the nav bar.

        Usage::
          n = page.ui.navbar()
          n.add_text("Nav bar title")

        :param text: The link to be added to the navbar
        """
        if not hasattr(text, 'options'):
            text = self.page.ui.text(text, html_code=self.sub_html_code("menu", auto_inc=True))
            text.style.css.height = "100%"
            text.style.css.vertical_align = 'middle'
        self.__add__(text)
        return text

    def __str__(self):
        status_html = ""
        if self.avatar is not None:
            self.add_right(self.avatar, with_css_cls=False)
        if self.options.orient == "vertical":
            self.style.css.width = "%s%s" % (self.options.size[0], self.options.size[1])
            self.title.style.css.display = None
            self.settings.style.css.align_self = "flex-end"
            self.settings.style.css.width = "100%"
            self.logo.style.css.width = "%s%s" % (self.options.size[0] - 20, self.options.size[1])
            if self.page.body.style.css.padding_left:
                padding_left = self.page.body.style.css.padding_left
                if str(padding_left).endswith("px"):
                    padding_left = int(padding_left[:-2])
                self.page.body.style.css.padding_left = max(padding_left, self.options.size[0] + 5)
            else:
                self.page.body.style.css.padding_left = self.options.size[0] + 5
        else:
            self.style.css.height = "%s%s" % (self.options.size[0], self.options.size[1])
            self.logo.style.css.height = "%s%s" % (self.options.size[0] - 15, self.options.size[1])
            self.settings.style.css.float = "right"
            self.style.css.line_height = self.options.size[0]
            scroll_height = 5 if self.options.status else 0
            if self.page.body.style.css.padding_top:
                padding_top = self.page.body.style.css.padding_top
                if str(padding_top).endswith("px"):
                    padding_top = int(padding_top[:-2])
                self.page.body.style.css.padding_top = max(padding_top, self.options.size[0] + scroll_height)
            else:
                self.page.body.style.css.padding_top = self.options.size[0] + scroll_height
            if self.options.scroll:
                self.page.body.onReady([self.page.js.number(0, "window.prevScrollpos")])
                self.page.body.scroll(['''var currentScrollPos = window.pageYOffset;
if(window.prevScrollpos > currentScrollPos) {%(dom)s.style.top = "0"} else {%(dom)s.style.top = "-%(height)spx"};
window.prevScrollpos = currentScrollPos''' % {"dom": self.dom.varName, "height": self.options.size[0]}])
            if self.options.status:
                status_html = self.status.html()
        str_h = "".join([h.html() for h in self.val])
        self.classList.add(self.style_refs["html-navbar-%s" % self.options.orient])
        return "<div %s>%s%s%s%s</div>" % (
            self.get_attrs(css_class_names=self.style.get_classes()), str_h, self.panel.html(), self.settings.html(),
            status_html)


class HtmlFooter(Html.Html):
    name = 'footer'

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-footer.css"
    ]

    style_refs = {
        "html-footer": "html-footer",
        "html-footer-logo": "html-footer-logo",
    }

    def __init__(self, page: primitives.PageModel, components: List[Html.Html], logo: str, width: tuple,
                 height: tuple, options: Optional[dict], profile: Optional[Union[dict, bool]]):
        super(HtmlFooter, self).__init__(page, [], css_attrs={"width": width, "height": height},
                                         options=options, profile=profile)
        self.logo = None
        if logo is not None:
            if not hasattr(logo, 'options'):  # if it is not an option it is considered as a path
                logo_url = logo
                self.logo = self.page.ui.div()
                self.logo.style.clear_all(True, False)
                if logo_url:
                    self.logo.style.css.background_url(logo_url)
            else:
                self.logo = logo
            self.logo.options.managed = False
            self.logo.classList.add(self.style_refs["html-footer-logo"])
            self.val.append(self.logo)

        self.classList.add(self.style_refs["html-footer"])
        self.__col_lst = None
        if components is not None:
            if not isinstance(components, list):
                components = [components]
            for component in components:
                self.__add__(component)

    @property
    def sections(self) -> list:
        if not self.__col_lst:
            self.__col_lst = []
        return self.__col_lst

    @sections.setter
    def sections(self, col_lst: list):
        """
        :param col_lst:
        """
        self.__col_lst = col_lst

    def __add__(self, component: Union[Html.Html, str]):
        """ Add items to the footer """
        if not hasattr(component, 'options'):
            component = self.page.ui.div(component, html_code=self.sub_html_code("panel", auto_inc=True))
        # Has to be defined here otherwise it is set to late
        component.options.managed = False
        self.val.append(component)
        return self

    def __getitem__(self, i: int) -> Html.Html:
        """Return the internal column in the row for the given index.

        :param i: the column index.
        """
        return self.val[i]

    def add_menu(self, context_menu):
        pass

    def __str__(self):
        row = []
        for val in self.val:
            if hasattr(val, "html"):
                row.append(val.html())
            else:
                row.append(val)
        return "<footer %s>%s</footer>" % (self.get_attrs(css_class_names=self.style.get_classes()), "".join(row))


class ContextMenu(Html.Html):
    name = 'Context Menu'
    source = None
    _option_cls = OptList.OptionsLi

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-menu.css",
    ]

    style_refs = {
        "html-menu": "html-menu",
    }

    def __init__(self, page: primitives.PageModel, components: List[Html.Html], width: str, height: str,
                 visible: bool, html_code: Optional[str], options: Optional[dict],
                 profile: Optional[Union[dict, bool]]):
        options = options or {}
        super(ContextMenu, self).__init__(page, [], css_attrs={"width": width, "height": height}, html_code=html_code,
                                          profile=profile, options=options)
        self.classList.add(self.style_refs["html-menu"])
        self.style.css.display = 'block' if visible else 'none'
        self.style.configs.shadow(
            hexa_color=options.get("shadow", {}).get("hexa_color"),
            size=options.get("shadow", {}).get("size", 1),
            opacity=options.get("shadow", {}).get("opacity", 0.5),
            position=options.get("shadow", {}).get("position"),
            radius=options.get("shadow", {}).get("radius"))
        for component in components:
            self.__add__(component)

    @property
    def options(self) -> OptList.OptionsLi:
        """Component options"""
        return super().options

    def add_item(self, value: str, icon: Optional[str] = None):
        """Add Item to the context menu.

        :param value:
        :param icon: Optional. The Font awesome icon
        """
        self += {"value": value, 'icon': icon}
        return self

    def add(self, component: Html.Html, **kwargs) -> Html.Html:
        """Add component to the menu container.

        :param component: Internal component to the framework.
        """
        self.__add__(component)
        return self.val[-1].val

    def set(self, name: Union[Html.Html, str], js_funcs: Union[list, str]) -> Html.Html:
        """Set a item with a click function to the menu

        :param name: Item component or name
        :param js_funcs: JavaScript function when clicked
        """
        menu = self.add(name)
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        menu.click(js_funcs)
        return self.val[-1].val

    def __add__(self, component: Html.Html):
        """
        :param component: The new HTML component to be added to the main component
        """
        if not hasattr(component, 'options'):
            if isinstance(component, dict):
                if component.get('icon') is not None:
                    i = self.page.ui.icon(component['icon'])
                    i.css({'display': 'inline', 'margin-right': '5px'})
                    v = self.page.ui.text(component['value'])
                    v.css({'display': 'inline'})
                    component = self.page.ui.div(
                        [i, v], html_code="{}_context_item_{}".format(
                            self.html_code, len(self.val)) if self.html_code is not None else self.html_code)
                else:
                    component = self.page.ui.div(
                        component['value'],
                        html_code="{}_context_item_{}".format(
                            self.html_code, len(self.val)) if self.html_code is not None else self.html_code)
            else:
                component = self.page.ui.div(
                    component,
                    html_code="{}_context_item_{}".format(
                        self.html_code, len(self.val)) if self.html_code is not None else self.html_code)
        li_obj = Li(self.page, component) if not isinstance(component, Li) else component
        li_obj.css({"padding": "5px", 'cursor': 'pointer'})
        li_obj.options.managed = False
        component.options.managed = False
        self.val.append(li_obj)
        return self

    def __getitem__(self, i: int) -> Html.Html:
        return self.val[i].val

    def __str__(self):
        # TODO: Add a condition in the init to display the context menu only for some columns or rows when table for example
        if getattr(self, 'source') is None:
            raise ValueError("Context Menu should be added to a component with the function contextMenu")

        str_vals = "".join([i.html() for i in self.val]) if self.val is not None else ""
        # hide when mouse leave the component
        self.mouse(out_funcs=[self.dom.hide()])
        return '''
<nav %(attr)s name='context_menus'>
  <ul style='list-style:none;padding:0px;margin:0'>%(val)s</ul>
</nav>''' % {'attr': self.get_attrs(css_class_names=self.style.get_classes()), 'val': str_vals}


class PanelsBar(Html.Html):
    name = 'Panel Bar'

    def __init__(self, page: primitives.PageModel, width: tuple, height: tuple, options: Optional[dict],
                 helper: str, profile: Optional[Union[dict, bool]]):
        super(PanelsBar, self).__init__(page, None, profile=profile, css_attrs={"width": width, "height": height})
        self.add_helper(helper)
        self.menus = page.ui.div(options={'inline': True})
        self.menus.options.managed = False
        self.panels = page.ui.div()
        self.panels.options.managed = False
        self.menu_mapping = collections.OrderedDict()
        #
        self.panels.style.css.display = False
        self.panels.style.css.position = 'absolute'
        #
        self.style.css.position = 'relative'
        self.__options = options
        if options.get('position', 'top') == 'top':
            self.panels.style.css.padding_bottom = 10
            self.menus.style.css.top = 0
            self.panels.style.css.border_bottom = '1px solid %s' % page.theme.colors[-1]
        else:
            self.style.css.position = 'relative'
            self.panels.style.css.border_top = '1px solid %s' % page.theme.colors[-1]
            self.panels.style.css.bottom = 0
            self.menus.style.css.bottom = 0

        self.menus.style.css.position = 'absolute'
        self.menus.style.css.background = page.theme.colors[-1]
        self.menus.style.css.color = page.theme.colors[0]
        self.menus.style.css.padding = '5px 0'

    def add_panel(self, text: str, content: Html.Html):
        """Add a panel to the panel bar.

        :param text: The anchor visible linked to a panel
        :param content: The panel
        """
        content.style.css.padding = "0 5px"
        if not hasattr(text, 'options'):
            text = self.page.ui.div(text)
        text.style.css.display = 'inline-block'
        text.style.css.width = 'auto'
        text.style.css.cursor = 'pointer'
        text.style.css.padding = '0 5px'
        self.menu_mapping[text] = content
        self.menus += text
        self.panels += content
        return self

    def __str__(self):
        css_menu = {"height": "auto", 'display': 'block', 'margin-top': '30px'} if self.__options[
                                                                                       'position'] == 'top' else {
            "height": "auto", 'display': 'block', 'margin-bottom': '30px'}
        for menu_item, panel in self.menu_mapping.items():
            menu_item.click([
                self.page.js.querySelectorAll(
                    Selector.Selector(self.panels).with_child_element("div").excluding(panel)).css(
                    {"display": 'none'}),
                #
                expr.if_(self.page.js.querySelector(
                    Selector.Selector(self.panels)).getAttribute("data-panel") == menu_item.htmlCode, [
                             self.page.js.querySelector(Selector.Selector(self.panels)).setAttribute("data-panel", ""),
                             self.page.js.querySelector(Selector.Selector(self.panels)).css({"display": 'none'})
                         ]).else_([
                    self.page.js.querySelector(Selector.Selector(self.panels)).setAttribute("data-panel",
                                                                                            menu_item.htmlCode),
                    self.page.js.querySelector(Selector.Selector(self.panels)).css(css_menu),
                    self.page.js.querySelector(Selector.Selector(panel)).css({'display': 'block'})
                ])
            ])

        return "<div %s>%s%s</div>%s" % (
            self.get_attrs(css_class_names=self.style.get_classes()), self.menus.html(), self.panels.html(),
            self.helper)


class Shortcut(Html.Html):
    name = 'shortcut'

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-shortcut.css"
    ]

    style_refs = {
        "html-shortcut": "html-shortcut",
    }

    def __init__(self, page: primitives.PageModel, components: List[Html.Html],
                 logo: Union[str, Html.Html], width: tuple, height: tuple, html_code: Optional[str],
                 options: Optional[dict], profile: Optional[Union[dict, bool]]):
        super(Shortcut, self).__init__(page, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                       profile=profile)
        self.classList.add(self.style_refs["html-shortcut"])
        self.logo = logo
        if hasattr(self.logo, 'options'):
            self.logo.options.managed = False
        self.__options = options
        for component in components:
            self.__add__(component)
        if options['position'] in ['left', 'right']:
            self.css({'text-align': 'center'})
        elif options['position'] == 'top':
            self.css({'top': '0'})
        elif options['position'] == 'bottom':
            self.css({'bottom': '0'})

    @property
    def style(self) -> GrpClsMenu.ClassShortcut:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpClsMenu.ClassShortcut(self)
        return self._styleObj

    def __add__(self, component: Html.Html):
        """Add items to a container"""
        if not hasattr(component, 'options'):
            component = self.page.ui.icons.awesome(component)
            component.icon.style.css.font_size = 20
            component.style.css.margin_bottom = 5
            component.style.css.margin_top = 5
        component.options.managed = False

        if self.__options['position'] in ['left', 'right']:
            component.style.css.text_align = component.style.css.text_align or 'center'
            component.style.css.display = 'block'
            component.style.css.margin_bottom = 5

        if self.__options['position'] == 'top':
            component.style.css.line_height = self.css("height")
            component.style.css.height = self.css("height")
            component.style.css.vertical_align = 'top'
            if component.style.css.position is None:
                component.style.css.position = 'relative'
            component.style.css.top = -3
            component.style.css.display = 'inline-block'

        component.style.css.margin = 'auto'
        self.val.append(component)
        return self

    def add_logo(self, icon: str, path: Optional[str] = None, align: str = "center",
                 width: tuple = (32, 'px'), height: tuple = (32, 'px')):
        """
        :param icon: The component icon content from font-awesome references
        :param path: Optional.
        :param align: Optional. A string with the horizontal position of the component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        """
        self.logo = self.page.ui.img(icon, path=path, align=align, width=width, height=height)
        self.logo.options.managed = False
        return self

    def __str__(self):
        if self.logo is None:
            self.logo = self.page.ui.icons.epyk(size=(20, "px"))
        else:
            self.logo.style.css.margin_top = 5
            self.logo.style.css.display = 'block'
            self.logo.style.css.margin = 'auto'
            if self.__options['position'] in ['left', 'right']:
                self.logo.style.css.margin_bottom = 15
                self.logo.style.css.margin_right = 0
            else:
                self.logo.style.css.margin_right = 10
        self.logo.options.managed = False
        self.logo.style.css.margin_bottom = 40
        self.page.body.style.css.padding_left = "%spx" % (int(self.css("width")[:-2]) + 5)
        str_div = "".join([self.logo.html()] + [v.html() if hasattr(v, 'html') else str(v) for v in self.val])
        return "<div %s>%s</div>" % (self.get_attrs(css_class_names=self.style.get_classes()), str_div)
