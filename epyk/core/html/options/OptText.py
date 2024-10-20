#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, List
from epyk.core.html.options import Options
from epyk.core.html.options import OptionsWithTemplates
from epyk.core.js.packages import packageImport


class OptionsText(OptionsWithTemplates):

    @property
    def editable(self):
        """Set the content of the component editable.
        `w3schools <https://www.w3schools.com/tags/att_global_contenteditable.asp>`_
        """
        if self.component.attr is not None:
            return self.component.attr.get("contenteditable", False)

        return False

    @editable.setter
    def editable(self, flag: bool):
        self.component.page.body.style.contenteditable()
        if self.component.attr is None:
            self.component.attr = {}
        self.component.attr["contenteditable"] = flag
        if flag:
            self.spellcheck = False

    @property
    def spellcheck(self):
        """The spellcheck attribute specifies whether the element is to have its spelling and grammar checked or not.
        `w3schools <https://www.w3schools.com/tags/att_global_spellcheck.asp>`_
        """
        return self.component.attr.get("spellcheck", False)

    @spellcheck.setter
    def spellcheck(self, flag: bool):
        self.component.page.body.style.contenteditable()
        self.component.attr["spellcheck"] = flag

    @property
    def reset(self):
        return self._config_get(False)

    @reset.setter
    def reset(self, flag: bool):
        self._config(flag)

    @property
    def maxlength(self):
        return self._config_get(None)

    @maxlength.setter
    def maxlength(self, num: int):
        self._config(num)

    @property
    def markdown(self):
        """Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
        Showdown can be used client side (in the browser) or server side (with NodeJs).
        `showdownjs <https://github.com/showdownjs/showdown>`_
        """
        return self._config_get(False)

    @markdown.setter
    @packageImport("showdown", if_true=True)
    def markdown(self, values: Union[bool, dict]):
        if isinstance(values, bool):
            self._config(values)
            self._config({} if values is True else values, 'showdown')
        else:
            self._config(True)
            self._config(values, 'showdown')

    @property
    def showdown(self):
        """Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
        Showdown can be used client side (in the browser) or server side (with NodeJs).
        `showdownjs <https://github.com/showdownjs/showdown>`_
        """
        return self._config_get(False)

    @showdown.setter
    @packageImport("showdown")
    def showdown(self, values: dict):
        self._config(True, 'markdown')
        self._config(values)

    @property
    def limit_char(self):
        """ """
        return self._config_get(None, 'limit_char')

    @limit_char.setter
    def limit_char(self, value: int):
        self._config(value, "maxlength")

    @property
    def red(self):
        """ """
        return self._config_get(self.page.theme.danger.base)

    @red.setter
    def red(self, value):
        self._config(value)

    @property
    def green(self):
        """ """
        return self._config_get(self.page.theme.success[1])

    @green.setter
    def green(self, value):
        self._config(value)

    @property
    def orange(self):
        """ """
        return self._config_get(self.page.theme.warning.base)

    @orange.setter
    def orange(self, value):
        self._config(value)

    @property
    def font_size(self):
        """ """
        return self._config_get('none')

    @font_size.setter
    def font_size(self, value):
        self._config(value)

    @property
    def status(self):
        return self._config_get('none')

    @status.setter
    def status(self, value):
        if hasattr(self.page.theme, str(value)):
            color = getattr(self.page.theme, str(value))[1]
        else:
            color = self.component.page.theme.colors[-1]
        self.component.style.css.border_left = '5px solid %s' % color
        self.component.style.css.padding_left = 5
        self._config(value)

    @property
    def style_select(self):
        """Internal CSS class name to be used when the component is selected"""
        return self._config_get(None)

    @style_select.setter
    def style_select(self, value):
        self._config(value)

    @property
    def html_encode(self):
        """Encode Python content to HTML format"""
        return self._config_get(True)

    @html_encode.setter
    def html_encode(self, flag: bool):
        self._config(flag)

    @property
    def multiline(self):
        """Replace the Python \n to the HTML tag <br/>."""
        return self._config_get(False)

    @multiline.setter
    def multiline(self, flag: bool):
        self._config(flag)

    @property
    def template(self):
        return self._config_get(None)

    @template.setter
    def template(self, value: str):
        self._config("function(data){return %s}" % value, js_type=True)

    @property
    def templateLoading(self):
        return self._config_get(None)

    @templateLoading.setter
    def templateLoading(self, value: str):
        self._config("function(data){return %s}" % value, js_type=True)

    @property
    def templateError(self):
        return self._config_get(None)

    @templateError.setter
    def templateError(self, value: str):
        self._config("function(data){return %s}" % value, js_type=True)

    @property
    def value(self):
        return self._config_get()

    @value.setter
    def value(self, value: str):
        self._config(value)


class OptionsTitle(OptionsText):

    @property
    def content_table(self):
        """ """
        return self._config_get(True)

    @content_table.setter
    def content_table(self, flag: bool):
        self._config(flag)

    @property
    def uppercase(self):
        """Set the CSS Style for the component to uppercase"""
        return self._config_get(True)

    @uppercase.setter
    def uppercase(self, flag: bool):
        if flag:
            self.component.style.css.text_transform = "uppercase"
        self._config(flag)


class OptionsNumber(OptionsText):

    @property
    def digits(self):
        """decimal point separator.
        `openexchangerates <http://openexchangerates.github.io/accounting.js/>`_
        """
        return self._config_get(0)

    @digits.setter
    def digits(self, num: int):
        self._config(num)

    @property
    def format(self):
        """controls output: %s = symbol, %v = value/number.
        `openexchangerates <http://openexchangerates.github.io/accounting.js/>`_
        """
        return self._config_get("%s%v")

    @format.setter
    def format(self, num: str):
        self._config(num)

    @property
    def symbol(self):
        """default currency symbol is ''.
        `openexchangerates <http://openexchangerates.github.io/accounting.js/#documentation>`_
        """
        return self._config_get("")

    @symbol.setter
    def symbol(self, value):
        self._config("money", name="type_number")
        self._config(value)

    @property
    def thousand_sep(self):
        """thousands separator.
        `openexchangerates <http://openexchangerates.github.io/accounting.js/>`_
        """
        return self._config_get(",")

    @thousand_sep.setter
    def thousand_sep(self, value: str):
        self._config(value)

    @property
    def decimal_sep(self):
        """decimal point separator.
        `openexchangerates <http://openexchangerates.github.io/accounting.js/>`_
        """
        return self._config_get(".")

    @decimal_sep.setter
    def decimal_sep(self, value: str):
        self._config(value)


class OptionsNumberMoves(OptionsNumber):
    component_properties = ("css", "label", "rotate", "font_size", "css_stats", "icon_up", "icon_down", "digits_percent")

    @property
    def css(self):
        """The label attached to a number component.

        :prop attrs: Dictionary. The CSS attributes.
        """
        return self._config_get({"text-align": "center", "margin-top": "5px",
                                 "font-size": self.page.body.style.globals.font.normal(10)})

    @css.setter
    def css(self, attrs: dict):
        self._config(attrs)

    @property
    def label(self):
        """The label attached to a number component.

        :prop attrs: Dictionary. The CSS attributes.
        """
        return self._config_get("")

    @label.setter
    def label(self, value: str):
        self._config(value)

    @property
    def rotate(self):
        """
        `w3schools <https://www.w3schools.com/cssref/css3_pr_transform.asp>`_
        """
        return self._config_get(40)

    @rotate.setter
    def rotate(self, value: int):
        self._config(value)

    @property
    def font_size(self):
        """The font size used by the percentage and difference.
        `w3schools <https://www.w3schools.com/cssref/css3_pr_transform.asp>`_
        """
        return self._config_get(self.page.body.style.globals.font.normal(2))

    @font_size.setter
    def font_size(self, value: int):
        self._config(value)

    @property
    def css_stats(self):
        return self._config_get({})

    @css_stats.setter
    def css_stats(self, attrs: dict):
        self._config(attrs)

    @property
    def icon_up(self):
        return self._config_get("fas fa-arrow-up")

    @icon_up.setter
    def icon_up(self, attrs: str):
        self._config(attrs)

    @property
    def icon_down(self):
        return self._config_get("")

    @icon_down.setter
    def icon_down(self, attrs: str):
        self._config(attrs)

    @property
    def digits_percent(self):
        return self._config_get(2)

    @digits_percent.setter
    def digits_percent(self, num: int):
        self._config(num)


class OptionsNumberDelta(OptionsNumber):
    component_properties = ("threshold1", "threshold2", "previous_label")

    @property
    def threshold1(self):
        """The first threshold."""
        return self._config_get(100)

    @threshold1.setter
    def threshold1(self, value: int):
        self._config(value)

    @property
    def threshold2(self):
        """The second threshold (smaller than the first one)."""
        return self._config_get(50)

    @threshold2.setter
    def threshold2(self, value: int):
        self._config(value)

    @property
    def previous_label(self):
        """Set the label displayed before the previous value in the component."""
        return self._config_get("Previous number: ")

    @previous_label.setter
    def previous_label(self, value: str):
        self._config(value)


class OptionsLink(OptionsText):

    @property
    def url(self):
        """The href attribute specifies the URL of the page the link goes to.
        `W3schools <https://www.w3schools.com/tags/att_a_href.asp>`_
        """
        return self.component.attr.get("href", '#')

    @url.setter
    def url(self, value: str):
        self.component.attr['href'] = value

    @property
    def href(self):
        """The href attribute specifies the URL of the page the link goes to.
        `w3schools <https://www.w3schools.com/tags/att_a_href.asp>`_
        """
        return self.component.attr.get("href", '#')

    @href.setter
    def href(self, value: str):
        self.component.attr['href'] = value

    @property
    def target(self):
        """The target attribute specifies where to open the linked document.
        `w3schools <https://www.w3schools.com/tags/att_a_target.asp>`_
        """
        return self.component.attr.get("target", '_self')

    @target.setter
    def target(self, value: str):
        self.component.attr['target'] = value


class OptionsConsole(OptionsText):
    component_properties = ("scroll_to_bottom",)

    @property
    def timestamp(self) -> bool:
        """Add the timestamp to any lines added"""
        return self.get(False)

    @timestamp.setter
    def timestamp(self, flag: bool):
        self.set(flag)

    @property
    def scroll_to_bottom(self) -> bool:
        """Force the console content to allow display the last lines when updated"""
        return self.get(True)

    @scroll_to_bottom.setter
    def scroll_to_bottom(self, flag: bool):
        self.set(flag)


class OptionsComposite(Options):

    @property
    def reset_class(self):
        """ """
        return self.get(False)

    @reset_class.setter
    def reset_class(self, flag: bool):
        self.set(flag)


class OptionsStatus(Options):
    component_properties = ("change_menu",)

    @property
    def states(self):
        """ """
        return self.get({})

    @states.setter
    def states(self, values: dict):
        self.set({k.upper(): v for k, v in values.items()})

    @property
    def color(self):
        """ """
        return self.get('white')

    @color.setter
    def color(self, color: str):
        self.set(color)

    @property
    def background(self):
        """ """
        return self.get('grey')

    @background.setter
    def background(self, color: str):
        self.set(color)

    @property
    def change_menu(self):
        """ """
        return self.get(False)

    @change_menu.setter
    def change_menu(self, flag: bool):
        self.set(flag)
        if flag:
            self.component.context = self.page.ui.menus.contextual(
                html_code="{}_context".format(
                    self.component.html_code) if self.component.html_code is not None else self.component.html_code)
            self.component.contextMenu(self.component.context, js_funcs=[])


class OptContents(Options):

    @property
    def manual(self):
        """Define the way the content table is updated."""
        return self.get("manual", False)

    @manual.setter
    def manual(self, flag: bool):
        self.set(flag)


class OptBreadCrumb(Options):
    component_properties = ("delimiter", "style_selected")

    def set_style(self, name: str):
        """Set the breadcrumb to a predefined style.
        Do not hesitate to share on Github if you think that a new configuration should be promoted to the package.

        :param name: The predefined style
        """
        defined_styles = {
            'pills': {
                "delimiter": '',
                "style": {"border-radius": "10px", "border": "1px solid %s" % self.page.theme.greys[4],
                          "background": self.page.theme.greys[0],
                          "margin": "0 2px", "width": '80px', "display": 'inline-block', "text-align": "center"},
                'selected': {"color": self.page.theme.greys[0], "background": self.page.theme.colors[-1]}},
            'tabs': {
                "delimiter": '',
                "style": {
                    "border-bottom": "5px solid inherit",
                    "margin": "0 2px", "width": '80px',
                    "display": 'inline-block',
                    "text-align": "center"},
                'selected': {
                    "color": self.page.theme.success[1],
                    "border-bottom": "5px solid %s" % self.page.theme.success[1]}},

        }
        self.style = defined_styles[name]["style"]
        self.delimiter = defined_styles[name]["delimiter"]
        self.style_selected = defined_styles[name]["selected"]

    @property
    def delimiter(self):
        """Set the delimiter for the breadcrumb categories.

        :prop value: String. The delimiter. Default /.
        """
        return self._config_get(' / ')

    @delimiter.setter
    def delimiter(self, value: str):
        self._config(value)

    @property
    def height(self):
        """Set the height for the breadcrumb items.

        :prop number: Integer. The height in pixel. Default 0.
        """
        return self._config_get(0)

    @height.setter
    def height(self, number: int):
        self._config(number)

    @property
    def style_selected(self):
        """Set the style for the selected item. This style will be added on top of the common CSS style.
        `w3schools <https://www.w3schools.com/cssref/>`_

        :prop values: Dictionary. The CSS styles.
        """
        return self._config_get({})

    @style_selected.setter
    def style_selected(self, values: dict):
        self._config(values)


class OptionsHighlights(Options):
    component_properties = ("close", "markdown")

    @property
    def close(self):
        """ """
        return self._config_get(True)

    @close.setter
    def close(self, flag: bool):
        self._config(flag)

    @property
    def close_css(self):
        """ """
        return self._config_get({"float": "right", "font-size": "20px", "cursor": "pointer"})

    @close_css.setter
    def close_css(self, values: dict):
        self._config(values)

    @property
    def reset(self):
        """ """
        return self._config_get(False)

    @reset.setter
    def reset(self, flag: bool):
        self._config(flag)

    @property
    def markdown(self):
        """Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
        Showdown can be used client side (in the browser) or server side (with NodeJs).
        `showdownjs <https://github.com/showdownjs/showdown>`_
        """
        return self._config_get(False)

    @markdown.setter
    @packageImport("showdown")
    def markdown(self, values):
        if isinstance(values, bool):
            self._config(values)
            self._config({} if values is True else values, 'showdown')
        else:
            self._config(True)
            self._config(values, 'showdown')

    @property
    def showdown(self):
        """Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
        Showdown can be used client side (in the browser) or server side (with NodeJs).
        `showdownjs <https://github.com/showdownjs/showdown>`_
        """
        return self._config_get(False)

    @showdown.setter
    @packageImport("showdown")
    def showdown(self, values):
        self._config(True, 'markdown')
        self._config(values)

    @property
    def template(self):
        return self._config_get(None)

    @template.setter
    def template(self, value: str):
        self._config("function(data){return %s}" % value, js_type=True)

    @property
    def templateLoading(self):
        return self._config_get(None)

    @templateLoading.setter
    def templateLoading(self, value: str):
        self._config("function(data){return %s}" % value, js_type=True)

    @property
    def templateError(self):
        return self._config_get(None)

    @templateError.setter
    def templateError(self, value: str):
        self._config("function(data){return %s}" % value, js_type=True)


class OptSearchResult(Options):
    component_properties = ("title", "dsc", "url", "visited", "link")

    @property
    def title(self):
        """ """
        return self._config_get({
            'color': self.page.theme.colors[-1], "font-weight": 900,
            'font-size': '18px'})

    @title.setter
    def title(self, attrs: dict):
        self._config(attrs)

    @property
    def dsc(self):
        """ """
        return self._config_get(
            {'color': self.page.theme.greys[6], "padding-bottom": "10px"})

    @dsc.setter
    def dsc(self, attrs):
        self._config(attrs)

    @property
    def url(self):
        """ """
        return self._config_get(
            {"font-style": 'italic', 'color': self.page.theme.notch(), 'font-size': '14px'})

    @url.setter
    def url(self, attrs: dict):
        self._config(attrs)

    @property
    def visited(self):
        """ """
        return self._config_get({'color': self.page.theme.greys[5]})

    @visited.setter
    def visited(self, attrs: dict):
        self._config(attrs)

    @property
    def link(self):
        """ """
        return self._config_get({'color': self.page.theme.colors[7], 'cursor': 'pointer'})

    @link.setter
    def link(self, attrs: dict):
        self._config(attrs)

    @property
    def pageNumber(self):
        """ """
        return self._config_get(0)

    @pageNumber.setter
    def pageNumber(self, num: int):
        self._config(num)

    @property
    def currPage(self):
        """ """
        return self._config_get(0)

    @currPage.setter
    def currPage(self, num: int):
        self._config(num)

    @property
    def grey(self):
        """ """
        return self._config_get(self.page.theme.colors[9])

    @grey.setter
    def grey(self, color: str):
        self._config(color)

    @property
    def white(self):
        """ """
        return self._config_get(self.page.theme.colors[0])

    @white.setter
    def white(self, color: str):
        self._config(color)


class OptionsUpdate(Options):
    component_properties = ("local_time", 'icon')

    @property
    def icon(self):
        """ """
        return self._config_get("fas fa-clock")

    @icon.setter
    def icon(self, text: str):
        self._config(text)

    @property
    def local_time(self):
        return self._config_get(True)

    @local_time.setter
    def local_time(self, flag: bool):
        self._config(flag)

    @property
    def template(self):
        return self._config_get(None)

    @template.setter
    def template(self, value: str):
        self.component._label = ""
        self._config("function(date){return %s}" % value, js_type=True)


class OptionsSurveys(OptionsWithTemplates):
    component_properties = ("style_label", "names", "tail")

    @property
    def best(self) -> int:
        return self._config_get(None)

    @best.setter
    def best(self, value: int):
        self._config(value)

    @property
    def icon(self) -> Union[List[str], str]:
        return self._config_get("star")

    @icon.setter
    def icon(self, icon: Union[List[str], str]):
        self._config(icon)

    @property
    def scale(self) -> bool:
        return self._config_get(False)

    @scale.setter
    def scale(self, scale: bool):
        self._config(scale)

    @property
    def colors(self) -> str:
        return self._config_get(None)

    @colors.setter
    def colors(self, values: List[str]):
        self._config(values)

    @property
    def tail(self) -> bool:
        return self._config_get(True)

    @tail.setter
    def tail(self, value: bool):
        self._config(value)

    @property
    def style(self) -> dict:
        return self._config_get({"margin": 0, "padding": 0})

    @style.setter
    def style(self, values: dict):
        self._config(values)

    @property
    def names(self) -> dict:
        return self._config_get([])

    @names.setter
    def names(self, values: List[str]):
        self._config(values)

    @property
    def tooltips(self) -> dict:
        return self._config_get([])

    @tooltips.setter
    def tooltips(self, values: List[str]):
        self._config(values)

    @property
    def style_label(self) -> dict:
        return self._config_get({
            "margin": "0 0 0 5px", 'height': 'none', "text-align": "left", "display": "inline-block", 'float': 'None',
            "font-size": self.page.body.style.globals.font.normal(), "color": self.page.theme.black
        })

    @style_label.setter
    def style_label(self, values: dict):
        self._config(values)

    @property
    def position(self) -> int:
        return self._config_get(None)

    @position.setter
    def position(self, value: int):
        self._config(value)

    @property
    def label(self) -> int:
        return self._config_get("")

    @label.setter
    def label(self, value: str):
        self._config(value)


class OptionsTrafficLight(Options):
    component_properties = ("red", 'green', 'orange')

    @property
    def green(self):
        return self._config_get(self.page.theme.success.base)

    @green.setter
    def green(self, value: str):
        self._config(value)

    @property
    def orange(self):
        return self._config_get(self.page.theme.warning.base)

    @orange.setter
    def orange(self, value: str):
        self._config(value)

    @property
    def red(self):
        return self._config_get(self.page.theme.danger.base)

    @red.setter
    def red(self, value: str):
        self._config(value)
