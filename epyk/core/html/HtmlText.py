#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os

from typing import Optional, Union
from epyk.core.py import primitives

from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.html.options import OptText
from epyk.core.html import Defaults as Default_html

# The list of Javascript classes
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.packages import JsCompNumber
from epyk.core.js.html import JsHtml
from epyk.core.css.styles import GrpCls


class Label(MixHtmlState.HtmlStates, Html.Html):
    name = 'Label'
    tag = "label"
    _option_cls = OptText.OptionsText

    def __init__(self, page: primitives.PageModel, text: str = None, color: str = None, align: str = None,
                 width=None, height=None, html_code: str = None, tooltip: str = None, profile=None, options=None):
        text = text or []
        if not isinstance(text, list):
            text = [text]
        for obj in text:
            if hasattr(obj, 'options'):
                obj.options.managed = False
        super(Label, self).__init__(page, text, html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height, 'color': color, 'text-align': align})
        self.css({'margin': '0 5px', 'float': 'left', 'display': 'inline-block',
                  'line-height': '%spx' % Default_html.LINE_HEIGHT,
                  'vertical-align': 'middle', 'text-align': 'left'})
        if tooltip:
            self.set_attrs(name='title', value=tooltip)

    @property
    def dom(self) -> JsHtml.JsHtmlRich:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript available for a DOM element by default.

        Usage::

          div = page.ui.label(htmlCode="testDiv")
          print(div.dom.content)

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlRich(self, page=self.page)
        return self._dom

    @property
    def id_html(self) -> JsNodeDom.JsDoms:
        """Get the element by id.
        This will return a DOM object and use document.getElementById to select the component.

        `Doc getElementsByTagName<https://developer.mozilla.org/fr/docs/Web/API/Element/getElementsByTagName>`_
        """
        return JsNodeDom.JsDoms.get("document.getElementById('%s')" % self.htmlCode)

    @property
    def options(self) -> OptText.OptionsText:
        """Property to set all the possible object for a button"""
        return super().options

    def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """Add a click event for a component.
        The event will be automatically added to the onload section to be activated once the component.
        has been build.

        Usage::

          select.label.click(str(page.js.console.log("test")))

        `Doc event <https://www.w3schools.com/js/js_htmldom_eventlistener.asp>`_
        `Doc onload <https://www.w3schools.com/jsref/event_onload.asp>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded

        :return: The component for the chaining.
        """
        self.css({"cursor": "pointer"})
        self.on("click", js_funcs, profile, source_event=source_event, on_ready=on_ready)
        return self

    def selectable(self, flag: bool = False):
        """Make the label component not selectable.
        This will be done by adding the class CssTextNotSelectable to the component.

        :param flag: Optional. Set the text not selectable.

        :return: self to allow the chains
        """
        if not flag:
            self.style.add_classes.text.no_selection()
        return self

    def __str__(self):
        res = []
        for v in self.val:
            if hasattr(v, 'html'):
                res.append(v.html())
            else:
                if self.options.showdown:
                    res.append(self.page.py.markdown.all(self.val))
                else:
                    res.append(str(v))
        self.onReady([self.dom.setAttribute("data-content", self.dom.content)])
        return '<%s %s>%s</%s>%s' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), "".join(res), self.tag, self.helper)


class Span(MixHtmlState.HtmlStates, Html.Html):
    name = 'Span'
    tag = "span"
    _option_cls = OptText.OptionsText

    def __init__(self, page: primitives.PageModel, text="", color=None, align=None, width=None,
                 height=None, html_code=None, tooltip=None, options=None, profile=None):
        super(Span, self).__init__(page, text, html_code=html_code, profile=profile, options=options,
                                   css_attrs={"width": width, "height": height, "color": color, 'text-align': align})
        self.css({'line-height': '%spx' % Default_html.LINE_HEIGHT, 'margin': '0 5px', 'display': 'inline-block',
                  'vertical-align': 'middle'})
        if tooltip is not None:
            self.tooltip(tooltip)

    @property
    def options(self) -> OptText.OptionsText:
        """Property to set all the possible object for a button"""
        return super().options

    @property
    def id_container(self):
        return self.htmlCode

    @property
    def id_jquery(self):
        return JsNodeDom.JsDoms.get("$('#%s')" % self.htmlCode)

    @property
    def id_html(self):
        """Get the element by id.
        This will return a DOM object and use document.getElementById to select the component.

        `Doc getElementsByTagName <https://developer.mozilla.org/fr/docs/Web/API/Element/getElementsByTagName>`_
        """
        return JsNodeDom.JsDoms.get("document.getElementById('%s')" % self.htmlCode)

    @property
    def dom(self) -> JsHtml.JsHtmlRich:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlRich(self, page=self.page)
        return self._dom

    def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """Add a click event for a component.
        The event will be automatically added to the onload section to be activated once the component
        has been build.

        Usage::

          select.label.click(str(page.js.console.log("test")))

        `Doc event <https://www.w3schools.com/js/js_htmldom_eventlistener.asp>`_
        `Doc onload <https://www.w3schools.com/jsref/event_onload.asp>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded

        :return: The HTML component.
        """
        self.css({"cursor": "pointer"})
        self.on("click", js_funcs, profile, source_event, on_ready)
        return self

    def __str__(self):
        self.onReady([self.dom.setAttribute("data-content", self.dom.content)])
        val = self.page.py.markdown.all(self.val) if self.options.showdown is not False else self.val
        return '<%s %s>%s</%s>%s' % (
          self.tag, self.get_attrs(css_class_names=self.style.get_classes()), val, self.tag, self.helper)


class Position(Span):

    def digits(self, flag: bool = False):
        """Specify if the count should be done from the commas.

        :param flag: Boolean (default false)
        """
        self._jsStyles["digits"] = flag
        return self

    def position(self, index: int, style: dict):
        """Set the CSS format for a specific character at a given position.

        :param index: A number
        :param style: The CSS Style to be used
        """
        self._jsStyles.setdefault("positions", {})[index] = style
        return self

    def __str__(self):
        self.onReady([self.dom.setAttribute("data-content", self.dom.content)])
        self.page.properties.js.add_builders(self.refresh())
        return '<%s %s>%s</%s>%s' % (
          self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.val, self.tag, self.helper)


class Text(MixHtmlState.HtmlStates, Html.Html):
    """Text component (based on DIV)"""
    name = 'Text'
    tag = "div"
    _option_cls = OptText.OptionsText

    def __init__(self, page: primitives.PageModel, text: str, color: str, align: str, width, height, html_code: str,
                 tooltip: str, options, helper: str, profile, verbose: bool = False):
        super(Text, self).__init__(page, text, css_attrs={"color": color, "width": width, "height": height},
                                   html_code=html_code, profile=profile, options=options, verbose=verbose)
        self.add_helper(helper)
        self.css({'text-align': align})
        if tooltip is not None:
            self.tooltip(tooltip)

    def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """Add a click event on the text component.
        The style of the mouse on the component will be changed to make the event more visible.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.style.css.cursor = 'pointer'
        if "data-group" in self.attr:
            return super(Text, self).click(js_funcs + [
                "document.querySelectorAll('[data-group=%s]').forEach(function(dom){dom.classList.remove('%s')})" % (
                    self.attr["data-group"], self.dom.classList.style_select),
                self.dom.classList.select()], profile, source_event, on_ready)

        return super(Text, self).click(js_funcs, profile, source_event, on_ready)

    def goto(self, url: str, js_funcs: Union[list, str] = None, profile: Optional[Union[bool, dict]] = None,
             target: str = "_blank", source_event: Optional[str] = None, on_ready: bool = False):
        """Click event which redirect to another page.

        :param url: The url link
        :param js_funcs: The Javascript Events triggered before the redirection
        :param profile: Optional. A flag to set the component performance storage
        :param target: Optional.
        :param source_event: Optional. The event source
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        js_funcs = js_funcs or []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_funcs.append(self.js.location.open_new_tab(url, target))
        return self.click(js_funcs, profile, source_event, on_ready)

    @property
    def val(self):
        """Property to get the jquery value of the HTML object in a python HTML object.
        This method can be used in any jsFunction to get the value of a component in the browser.
        This method will only be used on the javascript side, so please do not consider it in your algorithm in Python

        :returns: Javascript string with the function to get the current value of the component
        """
        return self._vals

    @val.setter
    def val(self, val):
        self._vals = val

    @property
    def dom(self) -> JsHtml.JsHtmlRich:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlRich(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptText.OptionsText:
        """Property to set all the possible object for a button"""
        return super().options

    def editable(self):
        """Change the component properties to be editable if double clicked.

        Usage::

          page.ui.text("This is a text").editable()

        :return: Self to allow the chaining.
        """
        self.style.add_classes.text.content_editable()
        self.set_attrs({"contenteditable": "false", "ondblclick": "this.contentEditable=true;this.className='inEdit'",
                        "onblur": "this.contentEditable=false;this.className=''"})
        return self

    def write(self, timer: int = 50):
        """Add a typing effect on this text.

        `Doc typewriter <https://www.w3schools.com/howto/howto_js_typewriter.asp>`_

        :param timer: Optional. The speed for the typing effect
        """
        value = self.val
        self.val = ""
        self.page.body.onReady([
            self.page.js.objects.string(value, js_code="%s_writer" % self.htmlCode, set_var=True),
            self.page.js.objects.number(0, js_code="%s_pos" % self.htmlCode, set_var=True),
            self.build(""),
            self.page.js.window.setInterval([
                self.page.js.if_(
                    self.page.js.objects.number.get(
                        "window.%s_pos" % self.htmlCode) < self.page.js.objects.string.get(
                        "window.%s_writer" % self.htmlCode).length, [
                        self.page.js.objects.number(
                            self.page.js.objects.number.get(
                                "window.%s_pos" % self.htmlCode) + 1, js_code="window.%s_pos" % self.htmlCode,
                            set_var=True),
                        self.dom.append(
                            self.page.js.objects.string.get(
                                "window.%s_writer" % self.htmlCode).charAt(
                                self.page.js.objects.number.get("window.%s_pos" % self.htmlCode)), new_line=False)
                    ]).else_(self.page.js.window.clearInterval("%s_interval" % self.htmlCode))
            ], "%s_interval" % self.htmlCode, timer)
        ])
        return self

    def __str__(self):
        self.onReady([self.dom.setAttribute("data-content", self.dom.content)])
        if self.options.markdown:
            self.page.properties.js.add_builders(self.refresh())
            return '<%s %s></%s>%s' % (
              self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag, self.helper)

        return '<%s %s>%s</%s>%s' % (
          self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.content, self.tag, self.helper)


class Pre(MixHtmlState.HtmlStates, Html.Html):
    """Pre-formatted text component"""
    name = 'Pre formatted text'
    tag = "pre"
    _option_cls = OptText.OptionsText

    def __init__(self, page: primitives.PageModel, vals, color, width, height, html_code, options, helper, profile):
        super(Pre, self).__init__(page, vals, html_code=html_code, profile=profile, options=options,
                                  css_attrs={"width": width, 'height': height, 'color': color})
        self.css({"text-align": 'left'})
        self.add_helper(helper)

    @property
    def dom(self) -> JsHtml.JsHtmlRich:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlRich(self, page=self.page)
        return self._dom

    def selectable(self, flag: bool = False):
        """Make the label component not selectable.
        This will be done by adding the class CssTextNotSelectable to the component.

        :param flag: Optional. A flag to the set items selectable

        :return: self to allow the chains.
        """
        if not flag:
            self.style.add_classes.text.no_selection()
        return self

    @property
    def options(self) -> OptText.OptionsText:
        """Property to set all the possible object for a button"""
        return super().options

    def __str__(self):
        self.onReady([self.dom.setAttribute("data-content", self.dom.content)])
        val = self.page.py.markdown.all(self.val) if self.options.showdown is not False else self.val
        return '<%s %s>%s</%s>%s' % (
          self.tag, self.get_attrs(css_class_names=self.style.get_classes()), val, self.tag, self.helper)


class Paragraph(MixHtmlState.HtmlStates, Html.Html):
    """Paragraph component"""
    name = 'Paragraph'
    tag = "div"
    _option_cls = OptText.OptionsText

    def __init__(self, page: primitives.PageModel, text, color, background_color, border, width, height, html_code,
                 encoding, helper, options, profile):
        tmp_text = []
        if not isinstance(text, list):
            content = []
            for line in text.strip().split("\n"):
                content.append(line.strip())
            text = [" ".join(content)]
        for t in text:
            css_styles, js_attr = re.search(" css\{(.*)\}", t), {}
            if css_styles is not None:
                content = t.replace(css_styles.group(0), '').decode(encoding) if hasattr(t, 'decode') else t.replace(
                    css_styles.group(0), '')
                tmp_text.append(content)
                for css_attr in css_styles.group(1).split(","):
                    css_key, css_val = css_attr.split(":")
                    js_attr[css_key.strip()] = css_val.strip()
            else:
                if hasattr(t, 'decode'):
                    tmp_text.append(t.decode(encoding))
                else:
                    tmp_text.append(t)
            options["classes"].append(js_attr)
        super(Paragraph, self).__init__(page, tmp_text, html_code=html_code, options=options,
                                        css_attrs={'color': color, "width": width, "height": height,
                                                   "background-color": background_color}, profile=profile)
        self.add_helper(helper)
        if border:
            self.css('border', '1px solid %s' % self.page.theme.greys[9])
        self.css({'text-align': 'justify', 'margin-top': '3px', "text-justify": 'distribute'})
        self.style.css.margin_top = 10
        self.style.css.margin_bottom = 10

    @property
    def options(self) -> OptText.OptionsText:
        """Property to set all the possible object for a button"""
        return super().options

    @property
    def dom(self) -> JsHtml.JsHtmlRich:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlRich(self, page=self.page)
        return self._dom

    def __str__(self):
        self.onReady([self.dom.setAttribute("data-content", self.dom.content)])
        self.page.properties.js.add_builders(self.refresh())
        return '<%s %s></%s>%s' % (
          self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag, self.helper)


class BlockQuote(Html.Html):
    name = 'Block quotation'
    tag = "blockquote"

    def __init__(self, page: primitives.PageModel, text, author, color, width, height, html_code, helper, options,
                 profile):
        super(BlockQuote, self).__init__(page, {'text': text, 'author': author}, html_code=html_code, profile=profile,
                                         css_attrs={"width": width, "height": height, 'color': color})
        self.add_helper(helper)
        self.__options = OptText.OptionsText(self, options)

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '''<%s %s>
    <div style="padding:5px;border-left:2px solid %s"></div>
    <div style="text-align:right"></div>
</%s>%s''' % (
      self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.page.theme.colors[3], self.tag,
      self.helper)


class Title(MixHtmlState.HtmlStates, Html.Html):
    name = 'Title'
    tag = "div"
    _option_cls = OptText.OptionsTitle

    def __init__(self, page: primitives.PageModel, text, level, name, contents, color, picture,
                 icon, marginTop, html_code, width, height, align, options, profile):

        css_styles = re.search(" css\{(.*)\}", text)
        if css_styles is not None:
            text = text.replace(css_styles.group(0), '')
            for css_attr in css_styles.group(1).split(","):
                css_key, css_val = css_attr.split(":")
                options[css_key.strip()] = css_val.strip()
        super(Title, self).__init__(page, text, html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
        self._name, self.level, self.picture = name, level, picture
        self.add_icon(icon, html_code=self.htmlCode, family=options.get("icon_family"))
        if contents is not None:
            self._name = contents.add(text, level or 1, name)
        if level is not None and level < 6:
            getattr(self.style.add_classes.text, "title_%s" % level)()
            self.css({'margin': '%spx 0 5px 0' % marginTop,
                      'font-size': self.page.body.style.globals.font.normal({1: 8, 2: 6, 3: 4, 4: 2, 5: -2}[level])})
        else:
            self.style.add_classes.text.title()
            self.css({'margin': '%spx 0 5px 0' % marginTop, 'font-size': self.page.body.style.globals.font.normal(5)})
        if color is not None:
            self.style.css.color = color
        if align == 'center':
            self.css({'margin': '5px auto 10px auto', 'display': 'inline-block', 'text-align': 'center'})
        elif align is not None:
            self.css({'margin': '5px auto 10px auto', 'display': 'inline-block', 'text-align': align})
        else:
            self.css({'display': 'inline-block'})  # , "margin-right": "10px"
        if hasattr(page, '_content_table') and not page._content_table.options.manual and self.__options.content_table:
            page._content_table.add_title(self, level=level)

    @property
    def style(self) -> GrpCls.ClassHtmlEmpty:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpCls.ClassHtmlEmpty(self)
        return self._styleObj

    @property
    def dom(self) -> JsHtml.JsHtmlRich:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlRich(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptText.OptionsTitle:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """Add a click event for a component.
        The event will be automatically added to the onload section to be activated once the component
        has been build.

        Usage::

          select.label.click(str(page.js.console.log("test")))

        `Doc eventlistener <https://www.w3schools.com/js/js_htmldom_eventlistener.asp>`_
        `Doc onload <https://www.w3schools.com/jsref/event_onload.asp>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded

        :return: The HTML component.
        """
        self.css({"cursor": "pointer"})
        return super(Title, self).click(js_funcs, profile, source_event, on_ready)

    def __str__(self):
        self.onReady([self.dom.setAttribute("data-content", self.dom.content)])
        anchor_name = ' name="%s"' % self._name if self._name is not None else ''
        val = self.page.py.markdown.all(self.val) if self.options.showdown is not False else self.val
        if self.picture is not None:
            path = Default_html.SERVER_PATH or os.path.split(self.picture)[0]
            return '<%s %s><img src="%s/%s" />&nbsp;<a%s></a>%s%s</%s>' % (
                self.tag, self.get_attrs(css_class_names=self.style.get_classes()), path, self.picture, anchor_name,
                val, self.helper, self.tag)

        return '<%s %s><a%s></a>%s%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), anchor_name, val, self.helper, self.tag)


class Numeric(MixHtmlState.HtmlStates, Html.Html):
    """Numeric component"""
    name = 'Number'
    tag = "div"
    requirements = ('accounting',)
    _option_cls = OptText.OptionsNumber

    def __init__(self, page: primitives.PageModel, number, title, label, icon, color, tooltip, html_code, options,
                 helper, width, profile):
        super(Numeric, self).__init__(page, number, html_code=html_code, profile=profile, options=options,
                                      css_attrs={"width": width, "color": color})
        # Add the components label and icon
        self.add_label(label, css={"float": "none", "width": 'auto', 'margin-right': '10px'}, html_code=self.htmlCode)
        self.add_icon(icon, html_code=self.htmlCode, family=options.get("icon_family"))
        self.add_helper(helper, css={"line-height": '20px'})
        self.add_title(title, level=4, options={'content_table': False},
                       css={"margin-bottom": 0, "margin-right": 0, "padding": 0})

        # Update the CSS Style of the component
        self.css({'text-align': 'center', 'display': 'inline-block'})
        self.tooltip(tooltip)

    def money(self, symbol: str = "", digit: int = 0, thousand_sep: str = ".", decimal_sep: str = ",",
              fmt: str = "%s%v"):
        """Format any number into currency.

        `Doc accounting<http://openexchangerates.github.io/accounting.js`>_

        :param symbol: Optional. custom symbol
        :param digit: Optional. Number of digit
        :param thousand_sep: Optional. The thousand separator
        :param decimal_sep: Optional. The decimal separator
        :param fmt: Optional. Format representation for the value (%v) and currency (%s)
        """
        self.options.symbol = symbol
        self.options.format = fmt
        self.options.digit = digit
        self.options.thousand_sep = thousand_sep
        self.options.decimal_sep = decimal_sep
        return self

    def number(self, digits: int = 0, thousand_sep: str = ',', decimal_sep: str = ","):
        """Format a number with custom precision and localisation.

        `Doc accounting <http://openexchangerates.github.io/accounting.js/>`_

        :param digits: Optional. Number of digit
        :param thousand_sep: Optional. The thousand separator
        :param decimal_sep: Optional. The decimal separator
        """
        self._jsStyles["type_number"] = "number"
        self.options.digits = digits
        self.options.thousand_sep = thousand_sep
        self.options.decimal_sep = decimal_sep
        return self

    @property
    def dom(self) -> JsHtml.JsHtmlNumeric:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlNumeric(self, page=self.page)
        return self._dom

    @property
    def js(self) -> JsCompNumber.CompNumber:
        """Return the Javascript internal object"""
        if self._js is None:
            self._js = JsCompNumber.CompNumber(page=self.page, selector=self.dom.varId, set_var=False, component=self)
        return self._js

    def to(self, number: int, timer: int = 1):
        """
        :param int number:
        :param int timer: The increase in millisecond
        """
        self.page.body.onReady([
            self.page.js.objects.number(self.val, js_code="%s_counter" % self.htmlCode, set_var=True),
            self.page.js.window.setInterval([
                self.page.js.if_(
                    self.page.js.objects.number.get("window.%s_counter" % self.htmlCode) < number, [
                        self.page.js.objects.number(
                            self.page.js.objects.number.get("window.%s_counter" % self.htmlCode) + 1,
                            js_code="window.%s_counter" % self.htmlCode, set_var=True),
                        self.build(self.page.js.objects.number.get("window.%s_counter" % self.htmlCode))
                    ]).else_(self.page.js.window.clearInterval("%s_interval" % self.htmlCode))
            ], "%s_interval" % self.htmlCode, timer)
        ])
        return self

    def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """Add a click event to the HTML component.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.style.add_classes.div.color_hover()
        return super(Numeric, self).click(js_funcs, profile, source_event, on_ready)

    @property
    def options(self) -> OptText.OptionsNumber:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        self.onReady([self.dom.setAttribute("data-content", self.dom.content)])
        return "<%s %s><font style='vertical-align:middle;height:100%%;padding:0;margin:0;display:inline-block'>%s</font>%s</%s>" % (
          self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.val, self.helper, self.tag)


class Highlights(MixHtmlState.HtmlStates, Html.Html):
    name = 'Highlights'
    tag = "div"
    requirements = ('bootstrap',)
    _option_cls = OptText.OptionsHighlights

    def __init__(self, page: primitives.PageModel, text, title, icon, type, color, width, height, html_code,
                 helper, options, profile):
        super(Highlights, self).__init__(page, text, css_attrs={"width": width, "height": height},
                                         html_code=html_code, profile=profile, options=options)
        self.add_helper(helper)
        self.style.css.color = color if color is not None else self.page.theme.greys[-1]
        # Add the components title and icon
        self.add_title(title, css={"width": "none", "font-weight": 'bold', 'margin-top': 0},
                       options={'content_table': False})
        self.add_icon(icon, {"float": "left", "color": 'inherit'}, html_code=self.htmlCode,
                      family=options.get("icon_family"))
        if self.icon is not None and self.icon != "":
            self.icon.style.css.font_factor(2)
        # Change the style of the component
        self.css({"margin": "5px 0", 'padding': "5px", "min-height": "25px"})
        self.attr['class'].add('alert alert-%s' % type)
        self.set_attrs(name='role', value="alert")
        self.dom.display_value = "block"

    @property
    def options(self) -> OptText.OptionsHighlights:
        """Property to set all the possible object for a button"""
        return super().options

    def __str__(self):
        self.onReady([self.dom.setAttribute("data-content", self.dom.content)])
        val = self.page.py.markdown.all(self.val) if self.options.showdown is not False else self.val
        if self.options.close:
            return '''<%s %s>
<span aria-hidden='true' style='float:right;font-size:20px;cursor:pointer' onclick='this.parentNode.remove()'>&times;</span>
<div name='content'>%s</div></%s>%s''' % (
                self.tag, self.get_attrs(css_class_names=self.style.get_classes()), val, self.tag, self.helper)

        return '''<%s %s><div name='content'>%s</div></%s>%s
          ''' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), val, self.tag, self.helper)


class Fieldset(MixHtmlState.HtmlStates, Html.Html):
    name = 'Fieldset'
    tag = "fieldset"
    _option_cls = OptText.OptionsText

    def __init__(self, page: primitives.PageModel, legend: str, width: str, height: str, helper: Optional[str],
                 options: Optional[dict], profile: Optional[Union[bool, dict]]):
        super(Fieldset, self).__init__(page, legend, css_attrs={"width": width, "height": height},
                                       profile=profile, options=options)
        self.add_helper(helper)
        self.css({'padding': '5px', 'border': '1px groove %s' % self.page.theme.greys[3], 'display': 'block',
                  'margin': '5px 0'})

    @property
    def options(self) -> OptText.OptionsText:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def __add__(self, component: Html.Html):
        """Add items to a container"""
        component.options.managed = False  # Has to be defined here otherwise it is set to late
        self.components[component.htmlCode] = component
        return self

    def __getitem__(self, component_id: Union[int, str]):
        if isinstance(component_id, int) and component_id not in self.components:
            return list(self.components.items())[component_id][1]

        return self.components[component_id]

    def __str__(self):
        self.onReady([self.dom.setAttribute("data-content", self.dom.content)])
        str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.components.values()])
        val = self.page.py.markdown.all(self.val) if self.options.showdown is not False else self.val
        return '<%s %s><legend style="width:auto">%s</legend>%s</%s>%s' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), val, str_div, self.tag, self.helper)
