#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional, List
from epyk.core.py import primitives, types

from epyk.core.html.options import OptText

from epyk.core.html import Html
from epyk.core.html import Defaults as Default_html
from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils


class HtmlGeneric(Html.Html):
    name = 'GenericTag'
    _option_cls = OptText.OptionsText

    def __init__(self, page: primitives.PageModel, tag: Union[str], text: Union[str, list, primitives.HtmlModel],
                 width: tuple, height: tuple, html_code: Optional[str], tooltip: str, options: Optional[dict],
                 profile: Optional[Union[bool, dict]]):
        self.tag = tag
        super(HtmlGeneric, self).__init__(page, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                          options=options, profile=profile)
        if self.options.html_encode:
            text = self.page.py.encode_html(text)
        if self.options.multiline:
            text = text.replace("\n", "<br/>")
        self.add(text)
        if tooltip:
            self.tooltip(tooltip)
        if options is not None and not options.get('managed', True):
            self.options.managed = False

    @property
    def options(self) -> OptText.OptionsText:
        """Property to set all the possible object for a button"""
        return super().options

    def __getitem__(self, i: int) -> Html.Html:
        if not isinstance(self.val, list):
            return self.val

        return self.val[i]

    def __add__(self, components: Union[List[Html.Html], Html.Html]):
        """Add items to a container"""
        # Has to be defined here otherwise it is set to late
        if not isinstance(components, list):
            components = [components]
        for component in components:
            if component is None:
                continue

            if hasattr(component, "options"):
                component.options.managed = False
            self.val.append(component)
        return self

    def press(self, js_press_funcs: types.JS_FUNCS_TYPES = None, js_release_funcs: types.JS_FUNCS_TYPES = None,
              profile: types.PROFILE_TYPE = None, pressed_class: str = None, on_ready: bool = False):
        """Special click event to keep in memory the state of the component.

        Usage::

          i = page.ui.icon("Click Me")

        :param js_press_funcs: Optional. Javascript functions
        :param js_release_funcs: Optional. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param pressed_class: Optional. The CSS class when component's status is pressed
        :param on_ready: Optional. Event when component is ready on HTML side
        """
        self.style.css.cursor = "pointer"
        self.style.css.border_radius = 20
        self.style.css.remove("color")
        self.style.add_classes.button.basic()
        self.aria.pressed = False
        if pressed_class is None:
            self.page.properties.css.add_text(
                ".event-pressed {background-color: %s; color: %s; border: 1px solid %s" % (
                    self.page.theme.notch(), self.page.theme.greys[0], self.page.theme.notch()), "event-pressed")
            pressed_class = "event-pressed"
        if not isinstance(js_press_funcs, list):
            js_press_funcs = [js_press_funcs]
        js_press_funcs.insert(0, self.dom.setAttribute("aria-pressed", True))
        js_press_funcs.append(self.dom.addClass(pressed_class))
        str_fnc = "if(%s.getAttribute('aria-pressed') == 'false'){%s}" % (
            self.dom.varId, JsUtils.jsConvertFncs(js_press_funcs, toStr=True))
        if js_release_funcs is not None:
            if not isinstance(js_release_funcs, list):
                js_release_funcs = [js_release_funcs]
            js_release_funcs.insert(0, self.dom.setAttribute("aria-pressed", False))
            js_release_funcs.append(self.dom.removeClass(pressed_class))
            str_fnc = "%s else{%s}" % (str_fnc, JsUtils.jsConvertFncs(js_release_funcs, toStr=True))
        return self.on("click", str_fnc, profile, on_ready=on_ready)

    @property
    def dom(self) -> JsHtml.JsHtmlRich:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlRich(self, page=self.page)
        return self._dom

    def __str__(self):
        if self.tag is None:
            if isinstance(self.val, list):
                str_val = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
                return '%s%s' % (str_val, self.helper)

            return '%s%s' % (self.val, self.helper)

        if isinstance(self.val, list):
            str_val = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
            return '<%s %s>%s</%s>%s' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_val,
                                         self.tag, self.helper)

        return '<%s %s>%s</%s>%s' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.val,
                                     self.tag, self.helper)

    def loading(self, status: bool = True, label: str = Default_html.TEMPLATE_LOADING_ONE_LINE,
                data: types.JS_DATA_TYPES = None):
        """Display a loading message in the component.

        Usage::

          btn.click([t.loading(True, label="`Loading: ${data.result}`", data={"result": "Waiting for response"})])

        :param status: The message status (true is active)
        :param label: The message template
        :param data: The message parameter to feed the template
        """
        self.options.templateLoading = label
        if status:
            return self.build(data, options={"templateMode": 'loading'})

        return ""

    def error(self, status: bool = True, label: str = Default_html.TEMPLATE_ERROR_LINE,
              data: types.JS_DATA_TYPES = None):
        """Display an error message in the component.

    Usage::

      btn.click([t.error(True, label="`Error: ${data.result}`", data={"result": "Wrong Parameter"})])

    :param status: The message status (true is active)
    :param label: The message template
    :param data: The message parameter to feed the template
    """
        self.options.templateError = label
        if status:
            return self.build(data, options={"templateMode": 'error'})

        return ""


class HtmlGenericLink(HtmlGeneric):
    name = 'tagLink'
    builder_name = "HtmlGeneric"

    def preview(self, url: str, profile: Optional[Union[bool, dict]] = None):
        """
        :param url: The url path.
        :param profile: Optional. A flag to set the component performance storage.
        """
        self.on('mouseenter', [
            self.page.js.request_http("test", 'GET', url).send().onSuccess([
                self.page.js.createElement("div", "popup").innerHTML(
                    self.page.js.object("data")).attr('id', 'popup').css(
                    {'color': 'red', 'display': 'block', 'background': 'white', 'width': '250px',
                     'padding': '10px'}).position(),
                self.page.body.dom.appendChild(self.page.js.object("popup"))]
            )
        ], profile=profile)

        self.on('mouseleave', [self.page.js.getElementById("popup").remove()], profile=profile)


class HtmlComment(Html.Html):
    name = 'comment'

    def __str__(self):
        return '<!--%s-->' % self.val
