#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional, Any, List
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.html import Html
from epyk.core.html import Defaults as Default_html
from epyk.core.js.html import JsHtml
from epyk.core.js.html import JsHtmlField
from epyk.core.html.options import OptText


class ExternalLink(Html.Html):
    name = 'External link'
    tag = "a"
    _option_cls = OptText.OptionsLink

    def __init__(self, page: primitives.PageModel, text: str, url: str, icon: str, helper: str, height: tuple,
                 decoration: bool, html_code: Optional[str], options: Optional[dict],
                 profile: Optional[Union[bool, dict]],
                 verbose: bool = False):
        super(ExternalLink, self).__init__(page, {"text": text, "url": url}, html_code=html_code, options=options,
                                           css_attrs={'height': height}, profile=profile, verbose=verbose)
        # Add the internal components icon and helper
        self.add_icon(icon, html_code=self.html_code, family=options.get("icon_family"), options=options.get("icon"))
        self.add_helper(helper, options=options.get("helper"))
        self.decoration, self.__url = decoration, {}
        if 'url' not in self.val:
            self.options.url = self.val['text']
        else:
            self.options.url = self.val['url']

    @property
    def dom(self) -> JsHtml.JsHtmlLink:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.
        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlLink(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptText.OptionsLink:
        """Property to set all the possible object for a button. """
        return super().options

    @property
    def js(self) -> JsHtmlField.Href:
        """Specific Javascript function for the input object. """
        if self._js is None:
            self._js = JsHtmlField.Href(self, page=self.page)
        return self._js

    def anchor(self, component: Html.Html):
        """Create a link to an HTML component defined in the page.
        This will create a shortcut to directly scroll to this component.
        :param component: A link to this HTML component
        """
        self.val["url"] = "#%s" % component.html_code
        self.options.url = "#%s" % component.html_code
        return self

    def no_decoration(self, color: Optional[str] = None):
        """Property to remove the list default style.

        :param color: Optional. The color code
        """
        self.style.css.text_decoration = None
        self.style.list_style_type = None
        if color is None:
            color = self.page.theme.greys[-1]
        self.style.css.color = color
        return self

    def build(self, data: types.JS_FUNCS_TYPES = None, options: dict = None,
              profile: types.PROFILE_TYPE = False, component_id: str = None,
              dataflows: List[dict] = None, **kwargs):
        """Return the JavaScript fragment to refresh the component content.

        :param data: The component expected content
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The component reference (the htmlCode)
        :param dataflows: Optional. Chain of data transformations
        """
        if not hasattr(data, 'toStr'):
            if not isinstance(data, dict):
                data = {"text": data}
            if "url" not in data:
                data["url"] = self.val["url"]
        return super(ExternalLink, self).build(data, options, profile, component_id, dataflows=dataflows)

    def __str__(self):
        return '<%s %s>%s</%s>%s' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.val['text'], self.tag, self.helper)

    def loading(self, status: bool = True, label: str = Default_html.TEMPLATE_LOADING_ONE_LINE,
                data: types.JS_DATA_TYPES = None) -> str:
        """Display a loading message in the component.

        Usage::

          btn.click([t.loading(True, label="`Loading: ${data.result}`", data={"result": "Waiting for response"})])

        :param status: Optional. The message status (true is active)
        :param label: Optional. The message template
        :param data: Optional. The message parameter to feed the template
        """
        self.options.templateLoading = label
        if status:
            return self.build(data, options={"templateMode": 'loading'})

        return ""

    def error(self, status: bool = True, label: str = Default_html.TEMPLATE_ERROR_LINE,
              data: types.JS_DATA_TYPES = None) -> str:
        """Display an error message in the component.

        Usage::

          btn.click([t.error(True, label="`Error: ${data.result}`", data={"result": "Wrong Parameter"})])

        :param status: Optional. The message status (true is active)
        :param label: Optional. The message template
        :param data: Optional. The message parameter to feed the template
        """
        self.options.templateError = label
        if status:
            return self.build(data, options={"templateMode": 'error'})

        return ""


class DataLink(Html.Html):
    name = 'Data link'
    filename = "Download"
    tag = "a"
    _option_cls = OptText.OptionsLink

    def __init__(self, page: primitives.PageModel, text: str, value: Any, width: tuple, height: tuple, fmt: str,
                 options: Optional[str], profile: Optional[Union[bool, dict]], verbose: bool = False):
        super(DataLink, self).__init__(page, {"text": text, 'value': value}, profile=profile, options=options,
                                       css_attrs={"width": width, 'height': height}, verbose=verbose)
        self.format = fmt

    @property
    def options(self) -> OptText.OptionsLink:
        """Property to set all the possible object for a button"""
        return super().options

    @property
    def no_decoration(self):
        """Property to remove the list default style. """
        self.style.css.text_decoration = None
        self.style.css.list_style_type = None
        return self

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<%(tag)s %(attr)s href="#" download="%(filename)s.%(format)s" type="text/%(format)s">%(val)s</%(tag)s>' % {
            "filename": self.filename, 'attr': self.get_attrs(css_class_names=self.style.get_classes()),
            'val': self.val['text'], "tag": self.tag, 'format': self.format}

    def loading(self, status: bool = True, label: str = Default_html.TEMPLATE_LOADING_ONE_LINE,
                data: types.JS_DATA_TYPES = None):
        """Display a loading message in the component.

        Usage::

          btn.click([t.loading(True, label="`Loading: ${data.result}`", data={"result": "Waiting for response"})])

        :param status: Optional. The message status (true is active)
        :param label: Optional. The message template
        :param data: Optional. The message parameter to feed the template
        """
        self.options.templateLoading = label
        if status:
            return self.build(data, options={"templateMode": 'loading'})

        return ""

    def error(self, status: bool = True, label: str = Default_html.TEMPLATE_ERROR_LINE,
              data: types.JS_DATA_TYPES = None) -> str:
        """Display an error message in the component.

        Usage::

          btn.click([t.error(True, label="`Error: ${data.result}`", data={"result": "Wrong Parameter"})])

        :param status: Optional. The message status (true is active)
        :param label: Optional. The message template
        :param data: Optional. The message parameter to feed the template
        """
        self.options.templateError = label
        if status:
            return self.build(data, options={"templateMode": 'error'})

        return ""
