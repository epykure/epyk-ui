#!/usr/bin/python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Optional, List, Union
from epyk.core.py import primitives

from epyk.core.html import Html
from epyk.core.html.options import OptPanel
from epyk.core.js.html import JsHtmlPopup


class Popup(Html.Html):
    name = 'Popup Container'
    tag = "div"

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

    def __init__(self, page: primitives.PageModel, components: List[Html.Html], width: tuple, height: tuple,
                 options: Optional[dict], profile: Optional[Union[bool, dict]], verbose: bool = False,
                 html_code: Optional[str] = None):
        super(Popup, self).__init__(
            page, [], html_code=html_code, profile=profile,
            verbose=verbose)
        self.__options = OptPanel.OptionPopup(self, options)
        self.classList.add(self.style_refs["html-popup"])
        self.classList.add(self.style_refs["html-popup-background"] if self.options.background else self.style_refs["html-popup-nobackground"])
        self.style.css.z_index = self.options.z_index
        self.set_attrs(name="name", value=self.options.popup_name)
        self.window = self.page.ui.div(width=width, height=height, html_code=self.sub_html_code("window"))
        self.window.classList.add(self.style_refs["html-popup-window"])
        self.window.options.managed = False
        self.window.set_attrs(name="tabindex", value=0)

        self.container = page.ui.div(
            components, width=(100, '%'), height=(100, '%'), html_code=self.sub_html_code("content"))
        self.container.options.managed = False
        self.container.classList.add(self.style_refs["html-popup-container"])

        self.body = page.ui.div(
            [self.container], width=(100, '%'), height=(100, '%'), html_code=self.sub_html_code("parent"))
        self.body.options.managed = False
        self.body.classList.add(self.style_refs["html-popup-body"])

        self.window.add(self.body)
        if not self.options.background and self.options.draggable:
            page.body.onReady([self.window.dom.jquery_ui.draggable()])

    @property
    def js(self) -> JsHtmlPopup.JsHtmlPopup:
        """Specific JavaScript features for the popup component.

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsHtmlPopup.JsHtmlPopup(page=self.page, component=self)
        return self._js

    def add(self, component: Html.Html):
        """Add a component to the popup.
        If this is a list then they will be added in a row.

        :param component: The component to be added to the underlying list
        """
        return self.container.add(component)

    def extend(self, components: List[Html.Html]):
        """Append list of component to the popup.

        :param components: The component to be added to the underlying list
        """
        return self.container.extend(components)

    def insert(self, n: int, component: Html.Html):
        """Insert a component to the popup at a specific place.

        :param n: The position in the popup
        :param component: The component to be added to the underlying list
        """
        return self.container.insert(n, component)

    @property
    def options(self) -> OptPanel.OptionPopup:
        """Property to set all the possible object for a button. """
        return self.__options

    def add_title(self, text: str, align: str = 'center', level: Optional[int] = 5, css: Optional[dict] = None,
                  position: str = "before", options: Optional[dict] = None):
        """Add a title to the popup.

        :param text: The value to be displayed to the component
        :param align: Optional. The text-align property within this component
        :param level: Optional.
        :param css: Optional. The CSS attributes to be added to the HTML component
        :param position: Optional. The position compared to the main component tag
        :param options: Specific Python options available for this component
        """
        if not hasattr(text, 'options'):
            title = self.page.ui.title(
                text, align=align, level=level, options=options,
                html_code=self.sub_html_code("title", auto_inc=True))
        else:
            title = text
        self.container.insert(0, title)
        return self

    def __str__(self):
        if self.options.close_on_background:
            self.click([self.page.js.if_(self.page.js.object("event.target === this"), [self.dom.hide()])])
        if self.options.closure:
            self.close.classList.add(self.style_refs["html-popup-close"])
            self.close.options.managed = False
            self.close.click([self.dom.hide()])
            self.window.add(self.close)
        return '''<%s %s>%s</%s>''' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.window.html(), self.tag)
