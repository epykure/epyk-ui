#!/usr/bin/python
# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Union, Optional, List
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.html import Html, HtmlContainer
from epyk.core.html.options import OptJsonFormatter
from epyk.core.html.options import OptText
from epyk.core.html.options import OptQrCode
from epyk.core.html.options import OptQuill

from epyk.core.js.html import JsHtmlStars
from epyk.core.js.html import JsHtmlJson
from epyk.core.js.html import JsHtmlQuill
from epyk.core.js.packages import JsJsonFormatter
from epyk.core.js.packages import JsQrCode
from epyk.core.js.packages import JsQuill
from epyk.core.js.primitives import JsObjects

from epyk.core.js import JsUtils

# The list of CSS classes
from epyk.core.css.styles import GrpClsLayout
from epyk.core.css import Defaults

from epyk.core import data


class Hr(Html.Html):
    name = 'Line delimiter'
    tag = "hr"

    def __init__(self, page: primitives.PageModel, background_color: str, width: tuple, height: tuple, align: str,
                 options: Optional[dict], profile: Optional[Union[dict, bool]]):
        super(Hr, self).__init__(page, "", options=options, profile=profile,
                                 css_attrs={"height": height, 'width': width,
                                            'border-color': background_color or page.theme.greys[5],
                                            'background-color': background_color or page.theme.greys[5]})
        if align == "center":
            self.style.css.margin = "auto"

    def margin(self, left: int = 0, right: int = 0, unit: str = '%'):
        """Shortcut to set the margin let and right for this HTML component.

        :param left: Optional. The margin left
        :param right: Optional. The margin right
        :param unit: Optional. The unit by default percentage
        """
        if left:
            self.style.css.margin_left = "%s%s" % (left, unit)
        if right:
            self.style.css.margin_right = "%s%s" % (right, unit)
        self.style.css.width = "calc(100%% - %s%s)" % (left + right, unit)
        return self

    @property
    def style(self) -> GrpClsLayout.ClassStandard:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpClsLayout.ClassStandard(self)
        return self._styleObj

    def __str__(self):
        return '<%s %s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()))


class Newline(Html.Html):
    name = 'New line'
    tag = "br"

    def __str__(self):
        return "".join(['<%s />' % self.tag] * self.val)


class Stars(Html.Html):
    name = 'Stars'
    tag = "div"
    _option_cls = OptText.OptionsSurveys

    def __init__(self, page: primitives.PageModel, val, label, color, align, best, html_code, helper, options, profile):
        if options is None:
            options = {}
        options.update({"best": best, "position": val, "label": label})
        icons = options.get("icon", "star")
        icon_details, colors = [], []
        if isinstance(icons, list):
            options["scale"] = True
            for icon in icons:
                icon_details.append(page.icons.get(icon))
        else:
            options["scale"] = False
            icon = page.icons.get(icons)
            for i in range(best):
                icon_details.append(icon)
        if options.get("colors"):
            colors = options["colors"]
        elif color is None:
            for i in range(best):
                colors.append(page.theme.success.base)
        elif isinstance(color, list):
            colors = color
        else:
            for i in range(best):
                colors.append(color)

        super(Stars, self).__init__(page, val, html_code=html_code, profile=profile, options=options)
        # Add the HTML components
        self._spans, self.popup = [], None
        self.options.colors = colors
        for i in range(best):
            self.add_span("", position="after", css=False)
            self._sub_htmls[-1].attr['class'].add(icon_details[i]["icon"])
            self._sub_htmls[-1].css(self.options.style)
            self._sub_htmls[-1].set_attrs(name="data-level", value=i)
            if len(self.options.tooltips) > i:
                self._sub_htmls[-1].set_attrs(name="title", value=self.options.tooltips[i])
            if val and self.options.tail and i < val:
                self._sub_htmls[-1].css({"color": self.options.colors[i]})
            elif val and not self.options.tail and i == val - 1:
                self._sub_htmls[-1].css({"color": self.options.colors[i]})
            self._spans.append(self._sub_htmls[-1])
        self.set_attrs(name='data-level', value=val)
        self.add_label(label, self.options.style_label, html_code=self.html_code, position="after")
        self.add_helper(helper)
        if self.helper:
            self.helper.css({"margin": '1px 4px'})
        self.css({'text-align': align, "display": 'block'})

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
    def options(self) -> OptText.OptionsSurveys:
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def message(self, placeholder: str = "write your comment",
                cancel: str = "&#x2718;Cancel", save: str = "&#10003;Save",
                profile: types.PROFILE_TYPE = None):
        """Add a input section when component is clicked.
        Default CSS will be applied to sub component but this can be checked using the popup text, cancel amd save
        properties.

        Usage::
          s = page.ui.rich.stars()
          s.message().click([
              page.js.console.log(s.dom.content), s.dom.tooltip(s.popup.text.dom.content).r, s.popup.dom.hide()])

        :param placeholder: Optional. Placeholder's label
        :param cancel: Optional. Cancel button label
        :param save: Optional. Save button label
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        """
        t = self.page.ui.textarea(placeholder=placeholder)
        t.style.css.text_align = "left"
        t.attr["tabindex"] = "0"
        c = self.page.ui.text(cancel)
        c.attr["tabindex"] = "0"
        c.style.css.margin = "0 5px"
        c.style.css.color = "#9C0006"
        s = self.page.ui.text(save)
        s.attr["tabindex"] = "0"
        s.style.css.margin = "0 5px"
        s.style.css.color = "#006100"
        self.popup = self.page.ui.div([t, c, s], width=None, html_code=self.sub_html_code("popup"))
        self.popup.style.css.display = None
        self.popup.style.css.padding = 5
        self.popup.style.css.background = self.page.theme.greys[0]
        self.popup.style.css.text_align = "right"
        self.popup.style.css.min_width = 100
        self.popup.style.css.z_index = 300
        self.popup.style.css.position = "absolute"
        self.popup.text = t
        self.popup.cancel = c
        self.popup.save = s
        self.popup.focusout([self.popup.dom.hide()], profile=profile)
        self.click([self.popup.dom.show(), self.popup.text.dom.empty(), self.popup.text.dom.focus()], profile=profile)
        c.click([self.popup.text.dom.empty(), self.popup.dom.hide()], profile=profile)
        return s

    @property
    def dom(self) -> JsHtmlStars.Stars:
        """The JavaScript dom object to be used in any events"""
        if self._dom is None:
            self._dom = JsHtmlStars.Stars(self, page=self.page)
        return self._dom

    def click(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """Add the event click and double click to the starts item.
        The Javascript function will be triggered after the change of content of the component.

        Usage::
          stars = page.ui.rich.stars(3, label="test Again")
          stars.click(page.js.console.log("test").toStr())

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded

        :return: self to allow the chains
        """
        self.css({"cursor": "pointer"})
        if js_funcs is None:
            js_funcs = []
        else:
            if not isinstance(js_funcs, list):
                js_funcs = [js_funcs]
        js_funcs = ["var data = parseInt(event.target.dataset.level)+1",
                    self.build(data=JsObjects.JsObjects.get("data"))] + js_funcs
        str_fncs = JsUtils.jsConvertFncs(js_funcs)
        for span in self._spans:
            span.click(str_fncs, profile, source_event=source_event, on_ready=on_ready)
        return self

    def __str__(self):
        if not self.popup:
            return "<%s %s>%s</%s>" % (
                self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.helper, self.tag)

        return "<%s %s>%s</%s>%s" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.helper, self.tag,
            self.popup.html())


class Help(Html.Html):
    name = 'Info'
    tag = "i"

    def __init__(self, page: primitives.PageModel, val, width: tuple, profile: Optional[Union[bool, dict]],
                 html_code: Optional[str], options: Optional[dict]):
        icon_details = page.icons.get("info")
        super(Help, self).__init__(page, val, html_code=html_code, css_attrs={"width": width}, profile=profile)
        self.attr['class'].add(icon_details["icon"])
        self.attr['title'] = val
        self._jsStyles = options

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
    def style(self) -> GrpClsLayout.ClassHelp:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpClsLayout.ClassHelp(self)
        return self._styleObj

    def __str__(self):
        return '<%(t)s %(a)s></%(t)s>' % {"a": self.get_attrs(css_class_names=self.style.get_classes()), "t": self.tag}


class Loading(Html.Html):
    name = 'Loading'
    tag = "div"

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-loading.css",
    ]

    style_refs = {
        "html-loading": "html-loading",
        "html-loading-message": "html-loading-message",
        "html-loading-fixed": "html-loading-fixed",
        "html-loading-page": "html-loading-page",
    }

    def __init__(self, page: primitives.PageModel, text: str, color: str, size: tuple, options: Optional[dict],
                 html_code: Optional[str], profile: Optional[Union[bool, dict]]):
        icon_details = page.icons.get("spin")
        super(Loading, self).__init__(page, text, html_code=html_code, profile=profile)
        self.color = self.page.theme.greys[-1] if color is None else color
        self.size = size[0]
        self.message = self.page.ui.div("")
        self.message.style.clear_all()
        self.message.options.managed = False
        self.add_icon("%s fa-spin" % icon_details["icon"], html_code=self.html_code,
                      css={"font-size": "%spx" % (self.size + 8)}, family=icon_details["icon_family"])
        self.classList.add(self.style_refs["html-loading"])
        if options.get('fixed', False):
            self.icon.css({"margin-right": '5px', "font-size": 'inherit'})
            self.classList.add(self.style_refs["html-loading-fixed"])
            self.span = self.page.ui.tags.span("%s..." % text, width="auto")
        if options.get('page', False):
            self.icon.css({"margin-right": '5px', "font-size": 'inherit'})
            self.classList.add(self.style_refs["html-loading-page"])
            self.span = self.page.ui.tags.span("%s..." % text, width="auto")
            self.message.attr["class"].add("html-loading-message")
            self.span.options.managed = False
        else:
            self.span = self.page.ui.tags.span("%s..." % text)
            self.span.style.css.margin = "5px"
        self.span.options.managed = False

    @classmethod
    def get_requirements(cls, page: primitives.PageModel, options: types.OPTION_TYPE = None) -> tuple:
        """Update requirements with the defined Icons' family.

        :param page: Page context
        :param options: Component input options
        """
        if options and options.get('icon_family') is not None:
            return (options['icon_family'],)

        return (page.icons.family,)

    def fixed(self, css: Optional[dict] = None, icon_css: Optional[dict] = None):
        """Set css attributes of the loading div to be fixed.
        This can be done directly in options in the component constructor options={"fixed": True}.

        :param css: Optional. The css attributes
        :param icon_css: Optional. The CSS attributes

        :return: self to allow the chains.
        """
        dfl_css = {"position": 'fixed', 'bottom': '5px', 'right': '5px'}
        if css is not None:
            dfl_css.update(css)
        dfl_css_icon = {"margin-right": '5px', "font-size": 'inherit'}
        if icon_css is not None:
            dfl_css_icon.update(icon_css)
        self.icon.css(dfl_css_icon)
        self.css(dfl_css)
        return self

    def __str__(self):
        return '<%(t)s %(a)s>%(s)s%(c)s</%(t)s>' % {
            "a": self.get_attrs(css_class_names=self.style.get_classes()), "s": self.span.html(),
            "c": self.message.html(), "t": self.tag}


class HtmlJson(Html.Html):
    name = 'Pretty Json'
    tag = "div"
    requirements = ('json-formatter-js',)
    _option_cls = OptJsonFormatter.OptionsJsonFmt

    def __init__(self, page: primitives.PageModel, tree_data, width, height, options, profile):
        super(HtmlJson, self).__init__(page, tree_data, profile=profile, options=options,
                                       css_attrs={"height": height, "width": width})

    @property
    def dom(self) -> JsHtmlJson.JsonFormatter:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript available for a DOM element by default.
        """
        if self._dom is None:
            self._dom = JsHtmlJson.JsonFormatter(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptJsonFormatter.OptionsJsonFmt:
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def js(self) -> JsJsonFormatter.Json:
        """Return the Javascript internal object.

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsJsonFormatter.Json(page=self.page, js_code=self.js_code, set_var=False, component=self)
        return self._js

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<%(t)s %(a)s></%(t)s>' % {"t": self.tag, "a": self.get_attrs(css_class_names=self.style.get_classes())}


class Breadcrumb(Html.Html):
    name = 'Breadcrumb'
    tag = "div"
    _option_cls = OptText.OptBreadCrumb

    def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
        super(Breadcrumb, self).__init__(page, [], profile=profile, options=options, html_code=html_code,
                                         css_attrs={"height": height, "width": width})
        self.style.css.line_height = height[0]
        self.style.css.vertical_align = 'middle'
        self.options.height = height[0]
        if records is not None:
            for rec in records:
                if not hasattr(rec, 'options'):
                    if isinstance(rec, dict):
                        records = page.ui.div(
                            rec['text'], width=("auto", '')) if options['selected'] == rec['text'] else page.ui.link(
                            rec['text'], rec['url'])
                        records.style.css.vertical_align = 'middle'
                    else:
                        records = page.ui.div(rec, width=("auto", '')) if options['selected'] == rec else page.ui.link(
                            rec)
                        records.style.css.vertical_align = 'middle'
                    records.style.css.display = 'inline-block'
                self.add(records)
        self.style.background = page.theme.greys[1]

    @property
    def options(self) -> OptText.OptBreadCrumb:
        """Property to set all the possible object for a breadcrumb definition"""
        return super().options

    def __add__(self, component: Union[primitives.HtmlModel, str]):
        """Add items to a container"""
        if hasattr(component, 'htmlCode'):
            component.options.managed = False
        self.val.append(component)
        return self

    def __str__(self):
        rows = [component.html() if hasattr(component, 'html') else str(component) for component in self.val]
        return '<%s %s>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.options.delimiter.join(rows),
            self.tag)


class Legend(Html.Html):
    name = 'Legend'
    tag = "div"
    _option_cls = OptJsonFormatter.OptionsLegend

    def __init__(self, page: primitives.PageModel, record, width: tuple, height: tuple, options: Optional[dict],
                 html_code: str, profile: Optional[Union[dict, bool]]):
        super(Legend, self).__init__(page, record, options=options, html_code=html_code,
                                     css_attrs={"width": width, "height": height}, profile=profile)

    @property
    def options(self) -> OptJsonFormatter.OptionsLegend:
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def __str__(self):
        divs = []
        css_inline = Defaults.inline(self.options.style)
        for i, val in enumerate(self.val):
            val["css_inline"] = css_inline
            if "id" not in val:
                val["id"] = self.sub_html_code("value_%s" % i)
            divs.append("<div><div id='%(id)s' style='background:%(color)s;%(css_inline)s'></div>%(name)s</div>" % val)
        return '<%s %s>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), "".join(divs), self.tag)


class Slides(Html.Html):
    name = 'Slides'
    _option_cls = OptText.OptionsText

    def __init__(self, page: primitives.PageModel, start, width: tuple, height: tuple, options: Optional[dict],
                 html_code: str, profile: Optional[Union[dict, bool]]):
        icon_details_right = page.icons.get("arrow_right")
        icon_details_left = page.icons.get("arrow_left")
        super(Slides, self).__init__(page, [], options=options, html_code=html_code,
                                     css_attrs={"width": width, 'height': height}, profile=profile)
        self.attr['data-current_slide'] = start
        self.title = self.page.ui.title("", html_code=self.sub_html_code("title"))
        self.title.style.css.border_bottom = "1px solid %s" % page.theme.colors[7]
        self.title.style.css.color = page.theme.colors[7]
        self.title.style.css.margin = 0
        self.title.options.managed = False
        if 'contents' in options:
            del page._content_table

            self._content_table = options['contents']
            self._content_table.style.css.z_index = 100
        if 'timer' in options:
            self.timer = self.page.ui.calendars.timer(options['timer'], html_code=self.sub_html_code("timer")).css(
                {"position": 'fixed', "font-size": '15px', 'top': '8px', "padding": '8px', "right": '15px',
                 'width': 'none',
                 'color': page.theme.greys[5]})
        self.next = self.page.ui.icon(icon_details_right["icon"], html_code=self.sub_html_code("next")).css(
            {"position": 'fixed', "font-size": '35px', 'bottom': '0', "padding": '8px', "right": '10px',
             'width': 'none'})
        self.previous = self.page.ui.icon(icon_details_left["icon"], html_code=self.sub_html_code("prev")).css(
            {"position": 'fixed', "font-size": '35px', 'bottom': '0', "padding": '8px', "left": '10px',
             'width': 'none'})

        self.page_number = self.page.ui.text("", html_code=self.sub_html_code("value")).css(
            {"position": 'fixed', 'z-index': 101, "font-size": '25px', 'bottom': '0', "padding": '8px', "left": '50%',
             'width': 'none'})

        self.next.click([
            self.page.js.getElementsByName(self.html_code).all([data.loops.dom_list.hide()]),
            data.primitives.float(self.dom.attr("data-current_slide").toString().parseFloat().add(1), 'slide_index'),

            self.js.if_(page.js.object('slide_index') <= self.dom.attr('data-last_slide'), [
                self.title.build(self.page.js.getElementsByName(
                    self.html_code)[page.js.object('slide_index')].attr('data-slide_title')),
                self.dom.attr("data-current_slide", page.js.object('slide_index')),
                self.page.js.getElementsByName(self.html_code)[page.js.object('slide_index')].show(
                    display_value='flex'),
                self.page.js.getElementById(
                    "%s_count" % self.html_code).innerHTML(
                    page.js.object('slide_index').toString().parseFloat().add(1)),
            ]).else_([
                self.title.build(self.page.js.getElementsByName(
                    self.html_code)[page.js.object('slide_index').add(-1)].attr('data-slide_title')),
                self.page.js.getElementsByName(
                    self.html_code)[page.js.object('slide_index').add(-1)].show(display_value='flex')]),

            self.js.if_(page.js.object('slide_index') > 0, [self.previous.dom.show()]),
            self.js.if_(page.js.object('slide_index') == self.dom.attr('data-last_slide'), [self.next.dom.hide()])
        ])

        self.previous.click([
            self.page.js.getElementsByName(self.html_code).all([data.loops.dom_list.hide()]),
            data.primitives.float(self.dom.attr("data-current_slide").toString().parseFloat().add(-1), 'slide_index'),

            self.js.if_(page.js.object('slide_index') >= 0, [
                self.title.build(self.page.js.getElementsByName(
                    self.html_code)[page.js.object('slide_index')].attr('data-slide_title')),
                self.dom.attr("data-current_slide", page.js.object('slide_index')),
                self.page.js.getElementsByName(self.html_code)[page.js.object('slide_index')].show(
                    display_value='flex'),
                self.page.js.getElementById(
                    "%s_count" % self.html_code).innerHTML(
                    page.js.object('slide_index').toString().parseFloat().add(1)),
            ]).else_([
                self.title.build(self.page.js.getElementsByName(self.html_code)[0].attr('data-slide_title')),
                self.page.js.getElementsByName(self.html_code)[0].show(display_value='flex')]),

            self.js.if_(page.js.object('slide_index') == 0, [self.previous.dom.hide()]),
            self.js.if_(page.js.object('slide_index') < self.dom.attr('data-last_slide'), [self.next.dom.show()])
        ])

        # Add the keyboard shortcut
        page.body.keydown.right([self.next.dom.events.trigger("click")])
        page.body.keydown.left([self.previous.dom.events.trigger("click")])
        self.style.css.padding = "0 20px 20px 20px"

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
    def options(self) -> OptText.OptionsText:
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def dom(self) -> JsHtmlStars.Slides:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript available for a DOM element by default.
        """
        if self._dom is None:
            self._dom = JsHtmlStars.Slides(component=self, page=self.page)
        return self._dom

    def add(self, component: Union[Html.Html, str], **kwargs):
        """Add a component to the slide.

        :param component: The HTML component to be added to this component
        """
        if isinstance(component, list):
            for c in component:
                if hasattr(c, 'options'):
                    c.options.managed = False
            component = self.page.ui.div(component)
            component.style.css.width = "100%"
            component.style.css.height = "90%"
            component.style.css.display = "flex"
            component.style.css.padding = 5
            component.style.css.justify_content = "center"
            component.style.css.align_items = "center"
            component.style.css.flex_direction = "column"
        if hasattr(component, 'options'):
            component.options.managed = False
            component.style.css.margin_top = '10px'
            component.style.css.overflow = 'auto'
        self.val.append(component)
        return self

    def add_slide(self, title: str, component: Union[Html.Html, str], options: Optional[dict] = None):
        """Add a slide.

        :param title: The title value in the slide
        :param component: The HTML component
        :param options: Optional. The various component options
        """
        self.add(component)
        self.val[-1].attr["data-slide_title"] = title
        if options is not None:
            options.get('contents', self._content_table).anchor(
                options.get('contents_title', title), options.get('contents_level', 0))
            options.get('contents', self._content_table)[-1].click([self.dom.goTo(len(self.val))])
        elif hasattr(self, '_content_table'):
            if options is not None:
                self._content_table.anchor(options.get('contents_title', title), options.get('contents_level', 0))
            else:
                self._content_table.anchor(title)
            self._content_table[-1].click([self.dom.goTo(len(self.val))])
        return self

    def __str__(self):
        self.page.body.style.css.height = '100%'
        self.page_number._vals = '<font id="%s_count" ondblclick="this.contentEditable = true" onkeydown="if (event.keyCode == 13){document.getElementById(\'%s\').setAttribute(\'data-current_slide\', Math.min(parseInt(this.innerHTML), %s) -2); %s; this.contentEditable = false}">%s</font> / %s' % (
        self.htmlCode, self.htmlCode, len(self.val), self.next.dom.events.trigger('click').toStr(),
        self.attr['data-current_slide'] + 1, len(self.val))
        comps = []
        self.attr['data-last_slide'] = len(self.val) - 1
        for i, s in enumerate(self.val):
            s.attr['name'] = self.html_code
            if i != self.attr['data-current_slide']:
                s.style.css.display = False
            else:
                self.title._vals = s.attr.get("data-slide_title", "")
                s.style.css.display = 'flex'
            comps.append(s.html())
        return '<div %s>%s%s</div>' % (
            self.get_attrs(css_class_names=self.style.get_classes()), self.title.html(), "".join(comps))


class HtmlQRCode(Html.Html):
    name = 'QR Code'
    tag = "div"
    requirements = ('qrcodejs',)
    _option_cls = OptQrCode.OptionsQrCode

    def __init__(self, page: primitives.PageModel, record, width: tuple, height: tuple, options: Optional[dict],
                 profile: Optional[Union[bool, dict]]):
        super(HtmlQRCode, self).__init__(page, record, profile=profile, options=options,
                                         css_attrs={"height": height, "width": width})
        self.options.width = width[0]
        self.options.height = height[0]

    @property
    def options(self) -> OptQrCode.OptionsQrCode:
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def jsonId(self):
        """Return the Javascript variable of the json object"""
        return "%s_obj" % self.html_code

    @property
    def js(self) -> JsQrCode.QrCode:
        """Return the Javascript internal object.

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsQrCode.QrCode(js_code=self.jsonId, set_var=False, component=self, page=self.page)
        return self._js

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<%(t)s %(a)s></%(t)s>' % {"a": self.get_attrs(css_class_names=self.style.get_classes()), "t": self.tag}


class HtmlCaptcha(Html.Html):
    name = 'Google Catch'
    tag = "button"
    requirements = ('google-captcha',)

    def __init__(self, page: primitives.PageModel, record, width: tuple, height: tuple, options: Optional[dict],
                 html_code: str, profile: Optional[Union[bool, dict]]):
        super(HtmlCaptcha, self).__init__(page, record, profile=profile, options=options, html_code=html_code,
                                          css_attrs={"height": height, "width": width})
        self.attr["data-callback"] = "onSubmit"
        self.attr["data-action"] = "submit"
        self.style.add_classes.external("g-recaptcha")

    def __str__(self):
        return '<%s %s>%s</%s>' % (
        self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self._vals, self.tag)


class HtmlQuill(Html.Html):
    name = 'Wysiwyg'
    tag = "div"
    requirements = ('quill',)
    _option_cls = OptQuill.OptionsQuill

    class Toolbar(HtmlContainer.Div):

        def select(self, cls: str, values: list, auto_prefix: bool = True):
            """Add select to the toolbar.

            :param cls: CSS Class name for the component
            :param values: Component values
            :param auto_prefix: Auto prefix class name with ql if missing
            """
            sl = self.page.ui.div([], tag="select", html_code=self.sub_html_code("_button", auto_inc=True))
            if values:
                for v in values:
                    if not isinstance(v, dict):
                        v = {"value": v}
                    opt = self.page.ui.div(v.get("text", ""), tag="option", html_code=self.sub_html_code("_button", auto_inc=True))
                    opt.attr["value"] = v["value"]
                    sl.add(opt)
            sl.style.clear_all(True, False)
            if auto_prefix and not cls.startswith("ql"):
                sl.classList.add("ql-%s" % cls)
                sl.attr["class"] = "ql-%s" % cls
            else:
                sl.classList.add(cls)
            self.add(sl)
            return sl

        def button(self, cls: str, auto_prefix: bool = True):
            """Add button to the toolbar.

            :param cls: CSS Class name for the component
            :param auto_prefix: Auto prefix class name with ql if missing
            """
            bt = self.page.ui.div("", tag="button", html_code=self.sub_html_code("_button", auto_inc=True))
            bt.style.clear_all(True, False)
            if auto_prefix and not cls.startswith("ql"):
                bt.classList.add("ql-%s" % cls)
            else:
                bt.classList.add(cls)
            self.add(bt)
            return bt

    def __init__(self, page: primitives.PageModel, record, width: tuple, height: tuple, options: Optional[dict],
                 html_code: str, profile: Optional[Union[bool, dict]]):
        super(HtmlQuill, self).__init__(
            page, record, profile=profile, options=options, html_code=html_code, css_attrs={
                "height": height, "width": width})
        self.toolbar = None

    @property
    def options(self) -> OptQuill.OptionsQuill:
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def build(self, data: types.JS_DATA_TYPES = None, options: types.JS_DATA_TYPES = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """Update Quill component with context and / or data changes.

        :param data: Optional. Text
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. Not used
        :param stop_state: Remove the top panel for the component state (error, loading...)
        :param dataflows: Chain of data transformations
        """
        builder_fnc = self.options.config_js(options).toStr()
        if data:
            data = self.js.setText(JsUtils.dataFlows(data, dataflows, self.page)).toStr()
        return '''%(chartId)s = new Quill(document.getElementById(%(hmlCode)s), %(builder)s); %(expr)s
                ''' % {
            "chartId": self.js_code, "hmlCode": JsUtils.jsConvertData(component_id or self.html_code, None),
            'builder': builder_fnc, "expr": data}

    def set_toolbar(self) -> Toolbar:
        """The Toolbar module allow users to easily format Quill's contents.
        `Quill <https://quilljs.com/docs/modules/toolbar>`_
        """
        self.toolbar = self.Toolbar(
            self.page, [], None, None, None, None, None,
            False, "", None, self.sub_html_code("toolbar"),
            "div", None, {}, None)
        self.toolbar.style.clear_all(True, False)
        self.toolbar.options.managed = False
        self.options.modules.toolbar = "#%s" % self.sub_html_code("toolbar")
        return self.toolbar

    @property
    def dom(self) -> JsHtmlQuill.Quill:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript available for a DOM element by default.
        """
        if self._dom is None:
            self._dom = JsHtmlQuill.Quill(component=self, page=self.page)
        return self._dom

    @property
    def js(self) -> JsQuill.Quill:
        """Return the Javascript internal object.

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsQuill.Quill(
                selector="window['%s']" % self.js_code, set_var=False, component=self, page=self.page)
        return self._js

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        if self.toolbar:
            return '%s<%s %s>%s</%s>' % (
                self.toolbar.html(), self.tag,
                self.get_attrs(css_class_names=self.style.get_classes()), self._vals, self.tag)

        return '<%s %s>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self._vals, self.tag)
