#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional, List
from epyk.core.py import primitives
from epyk.core.py import types

import json

from epyk.core.js import JsUtils
from epyk.core.html import Defaults
from epyk.core.js.statements import JsIf
from epyk.core.js.fncs import JsFncs

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsD3
from epyk.core.js.packages import JsQueryUi
from epyk.core.js.packages import JsCrossFilter
from epyk.core.js.packages import packageImport


class FmtNumber:

    def __init__(self, page: primitives.PageModel, selector: str, value):
        self.page, self._val = page, value
        self.selector = selector

    def toFixed(self, value: Optional[int] = None):
        """
        The toFixed() method converts a number into a string, keeping a specified number of decimals.

        Related Pages:

          https://www.w3schools.com/jsref/jsref_tofixed.asp

        :param value: Optional. The number of digit to be displayed.
        """
        if value is None:
            return JsObjects.JsObjects.get("%s = %s.toFixed()" % (self.selector, self._val))

        return JsObjects.JsObjects.get("%s = %s.toFixed(%s)" % (self.selector, self._val, value))

    def toPrecision(self, value: Optional[int] = None):
        """
        The toPrecision() method formats a number to a specified length.

        Related Pages:

          https://www.w3schools.com/jsref/jsref_toprecision.asp

        :param value: Optional. The number of digit to be displayed.
        """
        if value is None:
            return JsObjects.JsObjects.get("%s = %s.toPrecision()" % (self.selector, self._val))

        return JsObjects.JsObjects.get("%s = %s.toPrecision(%s)" % (self.selector, self._val, value))

    def toExponential(self):
        """
        The toExponential() method converts a number into an exponential notation.

        Related Pages:

          https://www.w3schools.com/jsref/jsref_toexponential.asp
        """
        return JsObjects.JsObjects.get("%s = %s.toExponential()" % (self.selector, self._val))


class Formatters:

    def __init__(self, page: primitives.PageModel, selector: str):
        self.page = page
        self.selector = selector

    @property
    def number(self):
        """
        Standard conversion to number.

        Related Pages:

          https://www.w3schools.com/jsref/jsref_obj_number.asp
        """
        return FmtNumber(self.page, self.selector, "parseFloat(%s)" % self.selector)

    @packageImport("accounting")
    def toNumber(self, digit: int = 0, thousand_sep: List[Union[str, primitives.JsDataModel]] = "."):
        """
        Convert to number using the accounting Javascript module.

        Related Pages:

          https://openexchangerates.github.io/accounting.js/

        :param digit: Optional. The number of digit to be displayed
        :param thousand_sep: Optional. The thousand symbol separator
        """
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        return JsObjects.JsObjects.get("%s = accounting.formatNumber(%s, %s, %s)" % (
            self.selector, self.selector, digit, thousand_sep))

    @packageImport("accounting")
    def toMoney(self, symbol: str = "", digit: int = 0, thousand_sep: str = ".", decimal_sep: str = ","):
        """
        Convert to number with a symbol using the accounting Javascript module.

        Related Pages:

          https://openexchangerates.github.io/accounting.js/

        :param symbol: Optional. The currency symbol
        :param digit: Optional. The number of digit to be displayed
        :param thousand_sep: Optional. The thousand symbol separator
        :param decimal_sep: Optional. The decimal symbol separator
        """
        symbol = JsUtils.jsConvertData(symbol, None)
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
        return JsObjects.JsObjects.get("%s = accounting.formatMoney(%s, %s, %s, %s, %s)" % (
            self.selector, self.selector, symbol, digit, thousand_sep, decimal_sep))


class ContentFormatters:

    def __init__(self, page: primitives.PageModel, selector: str):
        self.page = page
        self.selector = selector

    def __ge__(self, obj):
        return "%s >= %s" % (self.selector, JsUtils.jsConvertData(obj, None))

    def __gt__(self, obj):
        return "%s > %s" % (self.selector, JsUtils.jsConvertData(obj, None))

    def __le__(self, obj):
        return "%s <= %s" % (self.selector, JsUtils.jsConvertData(obj, None))

    def __lt__(self, obj):
        return "%s < %s" % (self.selector, JsUtils.jsConvertData(obj, None))

    def __eq__(self, obj):
        return "%s == %s" % (self.selector, JsUtils.jsConvertData(obj, None))

    def __ne__(self, obj):
        return "%s <> %s" % (self.selector, JsUtils.jsConvertData(obj, None))

    def __truediv__(self, obj):
        return JsObjects.JsObjects.get("%s / %s" % (self.selector, JsUtils.jsConvertData(obj, None)))

    def __floordiv__(self, obj):
        return JsObjects.JsObjects.get("%s // %s" % (self.selector, JsUtils.jsConvertData(obj, None)))

    def isIn(self, values: Union[list, primitives.JsDataModel]) -> JsObjects.JsBoolean.JsBoolean:
        """
        Check if value is in a list.

        Usage::

          inp = page.ui.input()
          values = ["A", "B"]
          inp.enter([page.js.if_(self.dom.content.isIn(values), [page.js.alert("Ok")]).else_([])])

        :param values: The values to use on the JavaScript side for the if statement
        """
        return JsObjects.JsBoolean.JsBoolean.get(
            "%s.includes(%s)" % (JsUtils.jsConvertData(values, None), self.selector))

    def isTrue(self):
        return JsObjects.JsObjects.get("%s == true" % self.selector)

    @packageImport("showdown")
    def fromMarkdown(self, options: dict = None):
        """
        Convert markdown to HTML string.

        Usage::

          t.dom.content.fromMarkdown()

        Related Pages:

          https://github.com/showdownjs/showdown

        :param options: Optional. Options allowed in the showdown module
        """
        options = JsUtils.jsConvertData(options or {}, None)
        return JsObjects.JsObjects.get(
            "%s = (function(){ var conv = new showdown.Converter(%s); return conv.makeHtml(%s)})()" % (
                self.selector, options, self.selector))

    @packageImport("accounting")
    def toNumber(self, digit: int = 0, thousand_sep: str = "."):
        """
        Convert to number using the accounting Javascript module.

        Related Pages:

          https://openexchangerates.github.io/accounting.js/

        :param digit: Optional. The number of digit to be displayed
        :param thousand_sep: Optional. The thousand symbol separator
        """
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        return JsObjects.JsObjects.get("accounting.formatNumber(%s, %s, %s)" % (self.selector, digit, thousand_sep))

    @packageImport("accounting")
    def toMoney(self, symbol: str = "", digit: int = 0, thousand_sep: str = ".", decimal_sep: str = ","):
        """
        Convert to number with a symbol using the accounting Javascript module.

        Related Pages:

          https://openexchangerates.github.io/accounting.js/

        :param symbol: Optional. The currency symbol
        :param digit: Optional. The number of digit to be displayed
        :param thousand_sep: Optional. The thousand symbol separator
        :param decimal_sep: Optional. The decimal symbol separator
        """
        symbol = JsUtils.jsConvertData(symbol, None)
        thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
        decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
        return JsObjects.JsObjects.get("accounting.formatMoney(%s,%s, %s, %s, %s)" % (
            self.selector, symbol, digit, thousand_sep, decimal_sep))

    @packageImport("accounting")
    def unformat(self):
        """
        parse a value from any formatted number/currency string.

        Related Pages:

          http://openexchangerates.github.io/accounting.js/
        """
        return JsObjects.JsNumber.JsNumber("accounting.unformat(%s)" % self.selector)

    @property
    def number(self):
        """ Standard conversion to number. """
        return JsObjects.JsNumber.JsNumber("parseFloat(%s)" % self.selector)

    @property
    def string(self):
        """ Standard conversion to string. """
        return JsObjects.JsString.JsString("String(%s)" % self.selector, is_py_data=False)

    @property
    def date(self):
        """ Standard conversion to Date object. """
        return JsObjects.JsDate.JsDate("new Date(%s)" % self.selector)

    def toStr(self):
        return self.selector

    @property
    def dict(self):
        """ Consider the object as a JavaScript Object """
        return JsObjects.JsObject.JsObject.get("%s" % self.selector)

    @property
    def array(self):
        """ Consider the object as a JavaScript array """
        return JsObjects.JsArray.JsArray.get("%s" % self.selector)

    @property
    def toJson(self):
        """ Cast the Javascript object to a Json object """
        return JsObjects.JsObject.JsObject.get("JSON.parse(%s)" % self.selector)

    def stringify(self):
        """ Cast the Javascript object to a string object """
        return JsObjects.JsObject.JsObject.get("JSON.stringify(%s)" % self.selector)


class JsHtml(JsNodeDom.JsDoms):
    display_value = "inline-block"

    def __init__(self, component: primitives.HtmlModel, js_code: Optional[str] = None, set_var: bool = True,
                 is_py_data: bool = True, page: primitives.PageModel = None):
        self.htmlCode = js_code if js_code is not None else component.html_code
        self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
        self.component, self.page = component, page
        self._js, self._container = [], self.element
        self._jquery, self._jquery_ui, self._d3 = None, None, None

    @property
    def container(self):
        """ Return the container level for the HTML component """
        if self.component is not None:
            return self._container

    @property
    def element(self):
        """ Return always the real DOM element. """
        if self.component is not None:
            return "document.getElementById('%s')" % self.component.html_code

    @property
    def val(self):
        """ Return a Javascript val object. """
        return JsObjects.JsObjects.get(
            "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
                self.htmlCode, self.content.toStr()))

    @property
    def by_name(self) -> JsNodeDom.JsDomsList:
        """  """
        if self.component.attr.get('name') is not None:
            return JsNodeDom.JsDomsList(
                None, "document.getElementsByName('%s')" % self.component.attr.get('name'), page=self.page)

        return self

    @property
    def isInViewPort(self) -> JsBoolean.JsBoolean:
        """ Check if the component is in the visible part of the page (the viewport). """
        flag = JsBoolean.JsBoolean(
            "!(rect.bottom < 0 || rect.top - viewHeight >= 0)", js_code="visibleFlag", set_var=True, is_py_data=False)
        flag._js.insert(0, self.page.js.viewHeight.setVar('viewHeight'))
        flag._js.insert(0, self.getBoundingClientRect().setVar("rect"))
        return JsFncs.JsAnonymous(flag.r).return_("visibleFlag").call()

    def onViewPort(self, js_funcs: types.JS_FUNCS_TYPES):
        """
        Trigger some code when the component is visible on the visible part of the page (the viewpport).

        :param js_funcs: The Javascript events
        """
        return self.page.js.if_(self.isInViewPort, js_funcs)

    def copyToClipboard(self, include_html: bool = False):
        """
        Copy the component content to the clipboard.

        :param include_html: Optional. Store the full HTML (Default False)
        """
        if include_html:
            return self.page.js.clipboard(self.innerHTML())

        return self.page.js.clipboard(self.innerText())

    @property
    def content(self) -> ContentFormatters:
        """ Get the component content. """
        if self.component.attr.get('type') == "number":
            return ContentFormatters(self.page, "parseFloat(%s.value)" % self.varName)

        return ContentFormatters(self.page, "%s.value" % self.varName)

    def empty(self):
        """ Empty the component. """
        return '%s.value = ""' % self.varName

    @property
    def events(self) -> JsNodeDom.JsDomEvents:
        """ Link to the events attached to a Javascript DOM object. """
        return JsNodeDom.JsDomEvents(self.component)

    @property
    def jquery(self) -> JsQuery.JQuery:
        """ Link to the JQuery functions. """
        if self._jquery is None:
            self._jquery = JsQuery.JQuery(
                component=self.component, selector=JsQuery.decorate_var("#%s" % self.component.html_code), set_var=False)
        return self._jquery

    @property
    def d3(self) -> JsD3.D3Select:
        """ Wrapper to the D3 library. """
        if self._d3 is None:
            self._d3 = JsD3.D3Select(
                component=self.component, page=self.page, selector="d3.select('#%s')" % self.component.html_code)
        return self._d3

    @property
    def jquery_ui(self) -> JsQueryUi.JQueryUI:
        """ Wrapper to the JqueryUI component. """
        if self._jquery_ui is None:
            self._jquery_ui = JsQueryUi.JQueryUI(
                component=self.component, selector=JsQuery.decorate_var("#%s" % self.component.html_code), set_var=False,
                page=self.page)
        return self._jquery_ui

    @property
    def objects(self) -> JsObjects.JsObjects:
        """ Interface to the main Javascript Classes and Primitives. """
        return JsObjects.JsObjects(page=self.page, component=self.component)

    @property
    def crossfilter(self):
        """
        Interface to CrossFilter package.

        Related Pages:

          https://github.com/square/crossfilter/wiki/API-Reference#group_all
        """
        return JsCrossFilter.CrossFilter

    @property
    def format(self) -> Formatters:
        """ Specific formatters for the HTML components. """
        return Formatters(self.page, self.content.toStr())

    def style(self, attrs: dict):
        """
        Style property to change from the javascript the CSS attributes of an HTML object.

        Usage::

          button.js.style({"backgroundColor": 'red'})
          button.js.style({"backgroundColor": None})

        Related Pages:

          https://www.w3.org/TR/DOM-Level-2-Style/css.html#CSS-CSSStyleRule-style

        :param attrs: The CSS attributes
        """
        styles = []
        for k, v in attrs.items():
            if "-" in k:
                split_css = k.split("-")
                k = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
            styles.append("this.style.%s = %s" % (k, json.dumps(v)))
        return JsUtils.jsConvertFncs(styles, toStr=True)

    def registerFunction(self, fnc_name: str, js_funcs: types.JS_FUNCS_TYPES, pmts: Optional[list] = None,
                         profile: types.PROFILE_TYPE = None):
        """
        Javascript Framework extension.

        Register a predefined Javascript function.
        This is only dedicated to specific Javascript transformation functions.

        :param fnc_name: The function name
        :param js_funcs: The Javascript function definition
        :param pmts: Optional. The parameters for the function
        :param profile: Optional. A flag to set the component performance storage

        :return: The JsObject
        """
        self.page.properties.js.add_function(fnc_name, js_funcs, pmts)
        return self

    def hide(self):
        """
        Hide the component.

        Usage::

          input.js.hide()

        Related Pages:

          https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/
        """
        return self.css("display", "none")

    def show(self, inline: Optional[str] = None, duration: Optional[int] = None, display_value: Optional[str] = None):
        """
        Show the component.

        This will use the display attribute of the component.

        Usage::

          input.js.show()

        Related Pages:

          https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

        :param inline: Optional. Set the CSS display attribute to inline-block instead of block
        :param duration: Optional. A time in second for the component display
        :param display_value: Optional. The value to display. Default inline-block
        """
        display_value = display_value or self.display_value
        if duration is not None:
            return super(JsHtml, self).show('inline-block' if inline else display_value, duration)

        return JsUtils.jsConvertData(self.css("display", 'inline-block' if inline else display_value), None)

    def display(self, flag: bool, inline: Optional[str] = None, display_value: Optional[str] = None):
        """
        Change the CSS display attribute.

        Related Pages:

          https://www.w3schools.com/cssref/pr_class_display.asp

        :param flag: A flag to specify the display type show or None
        :param inline: Optional. Set the CSS display attribute to inline-block instead of block
        :param display_value: Optional. The default CSS attribute for this component
        """
        flag = JsUtils.jsConvertData(flag, None)
        return JsObjects.JsVoid("if(%s){%s} else{%s}" % (
            flag, self.show(inline, display_value=display_value).r, self.hide().r))

    def visible(self, flag: bool = True, inverse: bool = False):
        """
        The visibility property specifies whether or not an element is visible.

        Tip: Hidden elements take up space on the page. Use the display property to both hide and remove an element from
        the document layout!

        Related Pages:

          https://www.w3schools.com/cssref/pr_class_visibility.asp

        Usage::

          mode_switch = page.ui.fields.toggle({"off": 'hidden', "on": "visible"}, is_on=True, label="", htmlCode="switch")
          mode_switch.input.click([icon.dom.visible(mode_switch.input.dom.content)])

        :param flag: Optional. specify the state of the component. Default True
        :param inverse: Optional. To specify the effect of the data flag
        """
        flag = JsUtils.jsConvertData(flag, None)
        if inverse:
            return self.css("visibility", JsObjects.JsVoid(
                "(function(flag){if(flag){ return 'hidden' } else {return 'visible'}})(%s)" % flag)).r

        return self.css("visibility", JsObjects.JsVoid(
            "(function(flag){if(!flag){ return 'hidden' } else {return 'visible'}})(%s)" % flag)).r

    def invisible(self):
        """
        The visibility property specifies whether or not an element is visible.

        Tip: Hidden elements take up space on the page. Use the display property to both hide and remove an element from
        the document layout!

        Related Pages:

          https://www.w3schools.com/cssref/pr_class_visibility.asp

        Usage::

          icon = page.web.bs.icons.danger()
          icon.style.css.invisble()
        """
        return self.css("visibility", "hidden").r

    def select(self):
        """   Select the content of the HTMl component. """
        return JsObjects.JsObjects.get("%s.select()" % self.varName)

    def focus(self, prevent_scroll: bool = False):
        """
        Add focus to the content of the HTMl component.

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus

        :param prevent_scroll: A Boolean value indicating whether or not the browser should scroll the document to bring
          the newly-focused element into view. A value of false for preventScroll (the default) means that the browser will
          scroll the element into view after focusing it. If preventScroll is set to true, no scrolling will occur.
        """
        return JsObjects.JsObjects.get("%s.focus({preventScroll: %s})" % (
            self.varName, JsUtils.jsConvertData(prevent_scroll, None)))

    def toggle(self, attr: str = "display", val_1: Optional[str] = None, val_2: str = "none"):
        """
        Toggle (hide / show) the display of the component.

        Usage::

          input.js.toggle()
          input.js.toggle("background", "red", "blue")

        Related Pages:

          https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

        :param attr:
        :param val_1:
        :param val_2:

        :return: A Javascript if statement
        """
        if attr == 'display' and val_1 is None:
            val_1 = self.display_value
        return JsIf.JsIf(self.css(attr) == val_2, [self.css(attr, val_1)]).else_([self.css(attr, val_2)])

    def highlight(self, css_attrs: Optional[dict] = None, time_event: int = 1000):
        """

        Usage::

          s.dom.highlight()
          s.dom.highlight(css_attrs={"background": "red"}),

        :param css_attrs: Optional. The CSS attributes.
        :param time_event: Optional. The time of the event.
        """
        if css_attrs is None:
            css_attrs, css_attrs_origin = {}, {}
            for k, v in Defaults.HTML_HIGHLIGHT.items():
                if isinstance(v, dict):
                    dyn_attrs, dyn_attrs_orign = {}, {}
                    if 'color' in v:
                        dyn_attrs['color'] = getattr(self.page.theme, *v['color'])
                        dyn_attrs_orign['color'] = self.page.theme.greys[0]
                    css_attrs[k] = v['attr'] % dyn_attrs
                    css_attrs_origin[k] = self.component.attr[k] if k in self.component.attr else v[
                                                                                                      'attr'] % dyn_attrs_orign
                else:
                    css_attrs[k] = v
                    css_attrs_origin[k] = self.component.attr[k] if k in self.component.attr else "none"
        else:
            css_attrs_origin = {}
            for k in css_attrs.keys():
                if k in self.component.attr:
                    css_attrs_origin[k] = self.component.attr[k]
                else:
                    css_attrs_origin[k] = "none"
        return '''%s; setTimeout(function(){%s}, %s)
      ''' % (self.css(css_attrs).r, self.css(css_attrs_origin).r, time_event)

    def loadHtml(self, components: List[primitives.HtmlModel], append: bool = False,
                 profile: types.PROFILE_TYPE = None):
        """
        Load during a Javascript event a component within the one using this method.
        This cannot be tested during the Python execution and should be tested in the browser.

        Tip: It is possible to add a break point to debug in the browser by adding.

        Usage::

          d = page.ui.div().css({"border": "1px solid black"})
          b = page.ui.button("test")
          b.click([
            page.js.console.debugger,
            d.dom.loadHtml(page.ui.texts.label("test label").css({"color": 'blue', 'float': 'none'}))])

        :param components: The different HTML objects to be added to the component
        :param append: Mention if the component should replace or append the data
        :param profile: Optional. A flag to set the component performance storage

        :return: The Javascript string to be added to the page
        """
        if not isinstance(components, list):
            components = [components]

        js_funcs = []
        for i, h in enumerate(components):
            h.options.managed = False
            js_funcs.append(self.page.js.objects.new(str(h), is_py_data=True, js_code="obj_%s" % i))
            js_funcs.append(self.innerHTML(self.page.js.objects.get("obj_%s" % i), append=append).r)
        return JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)

    def options(self, options: Optional[dict] = None):
        """
        Return the builder options used to generate the object on the Javascript side.
        This is not necessarily the same object as the component options as some can be only used on the Python side.

        This will not change the original option object used during the first object creation.

        :param options: Optional. The value to be changed.
        """
        opt = dict(self.component._jsStyles)
        if options is not None:
            opt.update(options)
        return opt

    def trigger(self, event: str):
        """
        Shortcut to the trigger event.

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/Document/createEvent

        :param event: The event to be triggered for the component
        """
        return self.events.trigger(event)

    @packageImport("html2canvas")
    def capture(self):
        """ Copy a screenshot of the component to the Clipboard """
        return '''html2canvas(%(id)s).then((canvas) => {
  canvas.toBlob(blob => navigator.clipboard.write([new ClipboardItem({'image/png': blob})]))})''' % {
            "id": self.component.dom.varId}

    def press(self):
        """ DOM event to trigger a click based on the pressed' aria tag """
        return self.page.js.if_(self.component.aria.js_is("pressed", "false"), [self.trigger("click")])

    def unpress(self):
        """ DOM event to trigger a click based on the pressed' aria tag """
        return self.page.js.if_(self.component.aria.js_is("pressed", "true"), [self.trigger("click")])

    def createWidget(self, html_code: str, container: str = None, options: types.JS_DATA_TYPES = None):
        if self.component.tag is None:
            raise Exception("No JavaScript define to generate this component")

        self.component.options.managed = False
        return JsUtils.jsWrap('''
(function(containerId, tag, htmlCode, attrs){
    const newDiv = document.createElement(tag);
    Object.keys(attrs).forEach(function(key) {newDiv.setAttribute(key, attrs[key]);}); newDiv.id = htmlCode;
    if(!containerId){document.body.appendChild(newDiv)} else {document.getElementById(containerId).appendChild(newDiv)};
    return newDiv })(%(container)s, "%(tag)s", %(html_code)s, %(attrs)s)''' % {
            "html_code": JsUtils.jsConvertData(html_code or self.component.html_code, None),
            "attrs": self.component.get_attrs(css_class_names=self.component.style.get_classes(), to_str=False),
            "tag": self.component.tag, "container": JsUtils.jsConvertData(container, None)})


class JsHtmlRich(JsHtml):

    @property
    def val(self):
        """  Return the val object. """
        values = ["'%s': %s" % (k, self.page.components[k].dom.content.toStr()) for k in
                  self.component._internal_components]
        return JsObjects.JsObjects.get(
            "{%s, offset: new Date().getTimezoneOffset()}" % ", ".join(values))

    @property
    def content(self):
        if hasattr(self.component.options, "markdown") and self.component.options.markdown:
            self.page.jsImports.add("showdown")  # Add the import in case it is not defined in the component
            return ContentFormatters(self.page, '''(function(domObl){const converter = new showdown.Converter();
if(domObl.hasAttribute('data-value')){return converter.makeMarkdown(domObl.getAttribute('data-value'))} 
else {return converter.makeMarkdown(domObl.innerHTML)}})(%(varName)s)''' % {"varName": self.varName})
        else:
            return ContentFormatters(self.page, '''(function(domObl){
if(domObl.hasAttribute('data-value')){ return domObl.getAttribute('data-value')} 
else {return domObl.innerHTML}})(%(varName)s)''' % {"varName": self.varName})

    @property
    def format(self):
        """ Specific formatters for the HTML components. """
        return Formatters(self.page, "%s.innerHTML" % self.varName)

    def toggleContent(self, current_val: str, new_val: str, current_funcs: types.JS_FUNCS_TYPES = None,
                      new_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None):
        """
        Toggle (change) the content of the HTML component.

        :param current_val: The content of the HTML component
        :param new_val: The new content of the HTML component
        :param current_funcs: Optional. The functions to be triggered when currentVal is visible
        :param new_funcs: Optional. The functions to be triggered when newVal is visible
        :param profile: Optional. A flag to set the component performance storage
        """
        content = JsUtils.jsConvertData(current_val, None)
        content2 = JsUtils.jsConvertData(new_val, None)
        return JsObjects.JsVoid('''
if(%(varName)s.innerHTML == %(content)s){%(varName)s.innerHTML = %(content2)s; %(jsFncs)s}
else {%(varName)s.innerHTML = %(content)s; %(jsFncs2)s}
''' % {'varName': self.varName, 'content2': content2, 'content': content,
       'jsFncs': JsUtils.jsConvertFncs(current_funcs, toStr=True, profile=profile),
       'jsFncs2': JsUtils.jsConvertFncs(new_funcs, toStr=True, profile=profile)
       })

    def select(self):
        """  Select the content of the HTMl component. """
        return JsObjects.JsObjects.get('''
(function(node){
if (document.body.createTextRange) {
  const range = document.body.createTextRange(); range.moveToElementText(node); range.select();
} else if (window.getSelection) {
  const selection = window.getSelection(); const range = document.createRange(); range.selectNodeContents(node);
  selection.removeAllRanges(); selection.addRange(range); }
}(%s))''' % self.varName)

    def append(self, value, new_line: bool = True, options: Optional[dict] = None):
        """

        :param value:
        :param new_line: Boolean. Optional.
        :param options: Optional.
        """
        value = JsUtils.jsConvertData(value, None)
        if options is not None and options.get('showdown') is not None:
            self.page.jsImports.add("showdown")
            value = '''(function(d){ var conv = new showdown.Converter(%s); 
let frag = document.createRange().createContextualFragment(conv.makeHtml(d)); 
frag.firstChild.style.display = 'inline-block';frag.firstChild.style.margin = 0;  
return frag.firstChild.outerHTML})(%s)''' % (json.dumps({}), value)
        if new_line:
            return JsObjects.JsObjects.get("%s.innerHTML += (%s+'<br />')" % (self.htmlCode, value))
            # return JsObjects.JsObjects.get("%s.innerHTML += (%s+'\\r\\n')" % (self.htmlCode, value))

        return JsObjects.JsObjects.get("%s.innerHTML += %s" % (self.htmlCode, value))

    def empty(self):
        """ Empty the content of the HTML component using the innerHTML JavaScript property. """
        return JsUtils.jsWrap('%s.innerHTML = ""' % self.varName)


class JsHtmlImg(JsHtml):

    @property
    def content(self):
        return ContentFormatters(self.page, "%s.src" % self.varName)

    def src(self, image: str):
        """

        :param image:
        """
        image = JsUtils.jsConvertData(image, None)
        return JsFncs.JsFunctions("%s.src = %s" % (self.varName, image))


class JsHtmlButton(JsHtml):

    @property
    def val(self):
        return JsObjects.JsObjects.get('''{%s: {value: %s.innerHTML, timestamp: Date.now(), 
offset: new Date().getTimezoneOffset(), locked: %s === 'true', name: %s}}
''' % (self.htmlCode, self.varName, self.getAttribute('data-locked'), self.getAttribute('name')))

    @property
    def content(self):
        return ContentFormatters(self.page, "%s.innerHTML" % self.varName)

    def loading(self, flag: bool, multiple: bool = False):
        """
        Add a loading icon to the button.

        Usage::

          b = component.ui.button("test")
          b.click([
            b.dom.loading(True),
            rptObj.js.window.setTimeout([b.dom.loading(False)], 5000)])

        :param flag:
        :param multiple: Optional.
        """
        i_loading = '<i class="fas fa-spinner fa-spin" style="margin-right:5px"></i>'
        fnc = self.disable(False) if multiple else self.disable(flag)
        if flag:
            fnc.append("%s.innerHTML = '%s' + %s.innerHTML" % (self.varName, i_loading, self.varName))
        else:
            fnc.append("%s.innerHTML = %s.innerHTML.replace('%s', '')" % (self.varName, self.varName, i_loading))
        return fnc

    def error(self, time: int, color: str = "red"):
        """

        :param time:
        :param color: Optional.
        """
        return JsFncs.JsFunction('''var bgColor = %s.style.borderColor; %s.style.borderColor = '%s'; 
setTimeout(function() {%s.style.borderColor = bgColor}, %s)''' % (
            self.varName, self.varName, color, self.varName, time))

    def disable(self, flag: bool = True):
        """

        :param flag: Optional.
        """
        flag = JsUtils.jsConvertData(flag, None)
        return JsFncs.JsFunctions("%s.disabled = %s" % (self.varName, flag))

    def release(self, by_name: bool = False):
        """

        :param by_name: Optional.
        """
        if by_name:
            funcs = JsFncs.JsFunctions(self.by_name.css("color", ''))
            funcs.append(self.by_name.css("background-color", ''))
            funcs.append(self.by_name.css("cursor", "pointer"))
            funcs.append(self.by_name.attr('data-locked', False))
        else:
            funcs = JsFncs.JsFunctions(self.css("color", ''))
            funcs.append(self.css("background-color", ''))
            funcs.append(self.css("cursor", "pointer"))
            funcs.append(self.attr('data-locked', False))
        return funcs

    def lock(self, not_allowed: bool = True):
        """

        :param not_allowed: Optional.
        """
        funcs = JsFncs.JsFunctions(self.css("color", self.getComputedStyle('color')))
        funcs.append(self.css("background-color", self.getComputedStyle('background-color')))
        if not_allowed:
            funcs.append(self.css("cursor", "not-allowed"))
            funcs.append(self.attr('data-locked', True))
        else:
            funcs.append(self.css("cursor", "default"))
            funcs.append(self.attr('data-locked', True))
        return funcs

    def empty(self):
        return '%s.innerHTML = ""' % self.varName


class JsHtmlButtonChecks(JsHtml):

    @property
    def val(self):
        """
        Get the full content of the list.

        This will return the current list status. Selected items but also the full content.
        It will return also the common parameters.
        """
        return ""

    @property
    def content(self):
        """
        Get the content of the list.

        This will return all the selected items in a list.
        """
        return ""

    def disable(self):
        return JsObjects.JsObjects.get('''
      ''')

    def add(self, data: Union[str, primitives.JsDataModel, float, dict, list], is_unique: bool = True,
            css_style: Optional[dict] = None, position: str = "bottom"):
        """
        Add an item to the list.

        This will add the item at the end of the list by default.
        By default the list will not add duplicated entries.

        Usage::

          data = [
            {"value": "Test 1", "checked": True, "name": 'name'},
            {"value": "Test 2", "dsc": 'description'}]
          cb = page.ui.buttons.checkboxes(data)
          a = page.ui.button("Add")
          a.click([cb.dom.add([{"value": "test"}])])

        :param data: The Python Javascript data
        :param is_unique: Optional. Flag to specify if only distinct values should be added (no duplicates)
        :param css_style: Optional. The CSS style of the added item
        :param position: Optional. The position of the new item in the list (bottom or top)
        """
        css_style = css_style or {'margin': 0, 'display': 'block', 'position': 'relative', 'cursor': 'pointer'}
        is_unique = JsUtils.jsConvertData(is_unique, None)
        data = JsUtils.jsConvertData(data, None)
        css_style = JsUtils.jsConvertData(css_style, None)
        return JsObjects.JsObjects.get('''
var existingCols = {}; var options = %(options)s;
if (%(unique)s){%(jqId)s.find('span').each(function(){
  var pItem = $(this); existingCols[pItem.data('content')] = true})};
%(jsData)s.forEach(function(rec){
  if ((!%(unique)s) || (%(unique)s && (!(rec.value in existingCols))) ){
    var style = %(styls)s;
    var strCss = []; for (key in style) {strCss.push(key + ":" + style[key])}; checkData = '&nbsp;';
    if (rec.color != undefined){style.color = rec.color};
    if (rec.name == undefined) {rec.name = rec.value};
    if (rec.checked){var checkData = '<i class="'+ options.icon + '" style="margin:2px"></i>'};
    var spanContent = '<span data-content="'+ rec.value + '" style="width:16px;display:inline-block;float:left;margin:0">'+ checkData +'</span><p style="margin:0" title="'+ rec.dsc + '">' + rec.name + '</p>';
    %(jqId)s.append($('<label style="' + strCss.join(";") + '">'+ spanContent +'</label>'))}
}) ''' % {"styls": css_style, "options": {}, "jqId": self.jquery.varId, "unique": is_unique, "jsData": data})

    def empty(self):
        """
        Empty the list content.

        Usage::

          data = [
            {"value": "Test 1", "checked": True, "name": 'name'},
            {"value": "Test 2", "dsc": 'description'}]
          cb = page.ui.buttons.checkboxes(data)
          d = page.ui.button("Empty")
          d.click([cb.dom.empty()])
        """
        return '%s.empty()' % self.jquery.varId

    def delete(self, data: types.JS_DATA_TYPES, data_ref: str = "compData"):
        """
        Delete an item to the checkbox buttons.

        Usage::

          data = [
            {"value": "Test 1", "checked": True, "name": 'name'},
            {"value": "Test 2", "dsc": 'description'}]
          cb = page.ui.buttons.checkboxes(data)
          d = page.ui.button("Delete")
          d.click([cb.dom.delete("test 2")])

        :param data:
        """
        data = JsUtils.jsConvertData(data, None)
        return JsObjects.JsObjects.get('''
var %(dataRef)s = %(jsData)s;
if (%(dataRef)s === true) {%(jqId)s.empty()}
else {%(jqId)s.find('span').each(function(){
    if (%(dataRef)s.indexOf($(this).data('content')) > -1){$(this).parent().remove()}
})}''' % {"jsData": data, "jqId": self.jquery.varId, "dataRef": data_ref})

    def check(self, data: types.JS_DATA_TYPES, data_ref: str = "compData"):
        """
        Check an a checkbox.

        Usage::

          data = [
            {"value": "Test 1", "checked": True, "name": 'name'},
            {"value": "Test 2", "dsc": 'description'}]
          cb = page.ui.buttons.checkboxes(data)
          d = page.ui.button("Check")
          d.click([cb.dom.check("test 2")])

        :param data:
        """
        data = JsUtils.jsConvertData(data, None)
        return JsObjects.JsObjects.get('''
var %(dataRef)s = %(jsData)s;
%(jqId)s.find('span').each(function(){
  var itemCode = $(this).data('content');
  if(typeof %(dataRef)s === "boolean"){
    if (%(dataRef)s === true && $(this).find("i").attr("class") === undefined){$(this).trigger("click")}
    if (!%(dataRef)s && $(this).find("i").attr("class") !== undefined){$(this).trigger("click")}}
  else if (%(dataRef)s.indexOf(itemCode) > -1){if ($(this).find("i").attr("class") === undefined){$(this).trigger("click")}}
})''' % {"jsData": data, "jqId": self.jquery.varId, "dataRef": data_ref})

    @property
    def current(self):
        """  Return the current value in the list. """
        return JsObjects.JsVoid("$(this).find('p').text()")

    def css_label(self, data: types.JS_DATA_TYPES, attrs: dict, data_ref: str = "compData"):
        """
        Change the CSS style of a given item.

        Usage::

          data = [
            {"value": "Test 1", "checked": True, "name": 'name'},
            {"value": "Test 2", "dsc": 'description'}]
          cb = page.ui.buttons.checkboxes(data)
          s = page.ui.button("Style")
          s.click([cb.dom.css_label("Test 2", {"color": 'orange'})])

        :param data:
        :param dict attrs:
        """
        data = JsUtils.jsConvertData(data, None)
        attrs = JsUtils.jsConvertData(attrs, None)
        return JsObjects.JsObjects.get('''
      var %(dataRef)s = %(jsData)s; var compAttrs = %(attrs)s;
      %(jqId)s.find('span').each(function(){
        var itemCode = $(this).data('content');
        if (%(dataRef)s.indexOf(itemCode) > -1){$(this).parent().find("p").css(compAttrs)}
      }) ''' % {"jsData": data, "jqId": self.jquery.varId, "attrs": attrs, "dataRef": data_ref})


class JsHtmlButtonMenu(JsHtmlButton):

    @property
    def val(self):
        """ """
        return JsObjects.JsObjects.get('''
{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), label: %s.innerHTML, name: %s}}
''' % (self.htmlCode, self.content.toStr(), self.component.label.dom.varName, self.getAttribute('name')))

    @property
    def content(self):
        """ """
        check = self.component.options.icon_check.split(" ")[-1]
        return ContentFormatters(self.page, "%s.querySelector('i').classList.contains('%s')" % (self.varName, check))


class JsHtmlIcon(JsHtml):

    @property
    def val(self):
        """ """
        return JsObjects.JsObjects.get(
            "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
                self.htmlCode, self.component.dom.getAttribute("class")))

    @property
    def content(self):
        """ """
        return self.component.dom.getAttribute("class")

    def spin(self, status: bool = True):
        """
        Add spin class to the font awesome.

        :param status: Optional. The spin status
        """
        if status:
            return self.component.dom.classList.add("fa-spin")

        return self.component.dom.classList.remove("fa-spin")

    def pulse(self, status: bool = True):
        """
        Add pulse class to the font awesome.

        :param status: Optional. The spin status
        """
        if status:
            return self.component.dom.classList.add("fa-pulse")

        return self.component.dom.classList.remove("fa-pulse")


class JsHtmlList(JsHtml):

    @property
    def val(self):
        """ Return the standard value object with the fields (value, timestamp, offset). """
        return JsObjects.JsObjects.get(
            "{%s: {value: %s.querySelector('[data-select=true]').innerHTML, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
                self.htmlCode, self.varName))

    @property
    def content(self):
        """ Return the values of the items in the list. """
        return JsObjects.JsArray.JsArray.get('''
(function(){
   var values = []; %(component)s.querySelectorAll("%(item)s").forEach(function(dom){values.push(dom.innerText)});
   return values
})()''' % {"component": self.component.dom.varName, "item": self.component.options.item_type})

    @property
    def classList(self):
        """ Return the class name of the list item. """
        return self.component.dom.getAttribute("class")

    def add(self, item: str, unique: bool = True, draggable: bool = False):
        """
        Add a new item to the list.

        :param item: The Item to be added to the list
        :param unique: Optional. Only add the item if it is not already in the list
        :param draggable: Optional. Set the new entry as draggable
        """
        if hasattr(item, 'dom'):
            item = item.dom.content
        item = JsUtils.jsConvertData(item, None)
        unique = JsUtils.jsConvertData(unique, None)
        draggable = JsUtils.jsConvertData(draggable, None)
        options = JsUtils.jsConvertData(self.component.options, None)
        return JsObjects.JsVoid('''
var listItems = %(item)s; 
var listItemOptions = %(options)s; 
var lenCurrentItems = %(component)s.querySelectorAll("li").length;
if(!Array.isArray(listItems)){listItems = [listItems]};
if ((typeof listItemOptions.max === 'undefined') || (listItemOptions.max === null) || (lenCurrentItems < listItemOptions.max)){
  listItems.forEach(function(item){
    var li = document.createElement("li");
    if(typeof listItemOptions.li_css !== 'undefined'){
      Object.keys(listItemOptions.li_css).forEach(function(key){li.style[key] = listItemOptions.li_css[key]})}
    if (%(draggable)s){
      li.setAttribute('draggable', true);
      li.addEventListener('dragstart', function(event){event.dataTransfer.setData("text", event.target.innerHTML)})
    }
    if(%(unique)s){
      var hasItems = false;
      %(component)s.querySelectorAll("li").forEach(function(dom){if (dom.innerText == item){hasItems = true}})
      if(!hasItems){
        li.appendChild(document.createTextNode(item)); li.style.cursor = "pointer"; li.style['text-align'] = "left";
        li.addEventListener("dblclick", function(){this.remove()});
        %(component)s.appendChild(li)}
    }else{
      li.appendChild(document.createTextNode(item)); li.style.cursor = "pointer"; li.style['text-align'] = "left";
      li.addEventListener("dblclick", function(){this.remove()}); %(component)s.appendChild(li)
    }
})}''' % {"item": item, "component": self.component.dom.varName, 'unique': unique, 'draggable': draggable,
          "options": options})

    def append(self, items: list, unique: bool = True, draggable: bool = False):
        """
        Add new items to the list.

        :param items: The Items to be added to the list
        :param unique: Optional. Only add the item if it is not already in the list
        :param draggable: Optional. Set the new entry as draggable
        """
        items = JsUtils.jsConvertData(items, None)
        return JsObjects.JsVoid(
            "%s.forEach(function(newItem){%s})" % (items, self.add(
                JsUtils.jsWrap("newItem"), unique=unique, draggable=draggable).toStr()))

    def clear(self):
        """ Clear all the items in the list. """
        return JsObjects.JsVoid("%s.innerHTML = ''" % self.component.dom.varName)

    @property
    def dropped_value(self):
        """
        Get the current dropped values to the list.
        Object can be structure (DOM) so the text content is wrapped in a specific variable.
        """
        return JsObjects.JsString.JsString.get("wrapper.innerText")

    def unactive(self, current_index: int = -1, data_ref: str = "list_items"):
        """
        Set to unactive all the items in the list.

        Usage::

          bnts = page.web.bs.lists.buttons(["US", "ES", "IT"], html_code="cty")
          for i, bnt in enumerate(bnts):
            bnt.click([bnts.dom.unactive(i)])

        :param int current_index: Optional. The item of the current item
        :param data_ref: The variable name for the data
        """
        return JsObjects.JsVoid('''
let %(data_ref)s = %(comp)s.children; for (var i = 0; i < %(data_ref)s.length; i++) { 
  if (%(data_ref)s[i].classList.contains('active') && (i != %(current_index)s)){%(data_ref)s[i].classList.remove('active')}
}''' % {"comp": self.component.dom.varName, "current_index": current_index, "data_ref": data_ref})


class JsHtmlBackground(JsHtml):

    @property
    def val(self):
        """ """
        return JsObjects.JsObjects.get(
            "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
                self.htmlCode, self.content.toStr()))

    @property
    def content(self):
        """ """
        return ContentFormatters(self.page, self.component.dom.querySelector("div").css("backgroundColor").toStr())


class JsHtmlNumeric(JsHtmlRich):

    def to(self, number: float, timer: int = 1, profile: types.PROFILE_TYPE = None):
        """

        :param number:
        :param timer: The time spent for the increase in millisecond
        :param profile: Optional. A flag to set the component performance storage
        """
        return JsUtils.jsConvertFncs([
            self.page.js.objects.number(self.content.unformat(), js_code="%s_counter" % self.htmlCode, set_var=True),
            self.page.js.window.setInterval([
                self.page.js.if_(
                    self.page.js.objects.number.get("window.%s_counter" % self.htmlCode) < number, [
                        self.page.js.objects.number(
                            self.page.js.objects.number.get("window.%s_counter" % self.htmlCode) + 1,
                            js_code="window.%s_counter" % self.htmlCode, set_var=True),
                        self.component.build(self.page.js.objects.number.get("window.%s_counter" % self.htmlCode))
                    ]).else_(self.page.js.window.clearInterval("%s_interval" % self.htmlCode))
            ], "%s_interval" % self.htmlCode, timer)
        ], toStr=True, profile=profile)

    def add(self, item: float):
        """
        Add a value to the component value.

        :param item: The value to be added
        """
        return JsObjects.JsVoid('''
%(component)s.innerText = parseFloat(%(component)s.innerText) + %(value)s''' % {
          'value': item, 'component': self.component.dom.varName})


class JsHtmlLink(JsHtml):

    @property
    def content(self):
        """ """
        return ContentFormatters(self.page, "%s.innerText" % self.varName)

    def url(self, url: str):
        """
        The href attribute specifies the URL of the page the link goes to.

        Related Pages::

          https://www.w3schools.com/tags/att_a_href.asp

        :param url: The url path
        """
        url = JsUtils.jsConvertData(url, None)
        return JsFncs.JsFunctions("%s.href = %s" % (self.varName, url))

    def href(self, url: str):
        """
        The href attribute specifies the URL of the page the link goes to.

        Related Pages::

          https://www.w3schools.com/tags/att_a_href.asp

        :param url: The url path
        """
        url = JsUtils.jsConvertData(url, None)
        return JsFncs.JsFunctions("%s.href = %s" % (self.varName, url))

    def target(self, name: str):
        """
        The target attribute specifies where to open the linked document.

        Related Pages::

          https://www.w3schools.com/tags/att_a_target.asp

        :param name: The target name
        """
        name = JsUtils.jsConvertData(name, None)
        return JsFncs.JsFunctions("%s.target = %s" % (self.varName, name))


class JsMedia(JsHtml):

    # TODO: Implement properly this with JsMediaRecorder

    def start(self):
        """
        Start the camera.
        This can only work with https and localhost urls.

        Related Pages::

          https://developer.mozilla.org/fr/docs/WebRTC/Prendre_des_photos_avec_la_webcam
        """
        return '''
var mediaConfig =  { video: true };
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia(mediaConfig).then(function(stream) {
%(varId)s.srcObject = stream; %(varId)s.play();});}
else if(navigator.getUserMedia) { 
navigator.getUserMedia(mediaConfig, function(stream) {
  %(varId)s.src = stream; %(varId)s.play();}, errBack);
} else if(navigator.webkitGetUserMedia) {
navigator.webkitGetUserMedia(mediaConfig, function(stream){
  %(varId)s.src = window.webkitURL.createObjectURL(stream); %(varId)s.play();}, errBack);
} else if(navigator.mozGetUserMedia) {
navigator.mozGetUserMedia(mediaConfig, function(stream){
  %(varId)s.src = window.URL.createObjectURL(stream); %(varId)s.play();}, errBack);} ''' % {"varId": self.varId}

    def stop(self):
        """

        Related Pages::

          https://developer.mozilla.org/fr/docs/WebRTC/Prendre_des_photos_avec_la_webcam
        """
        return '''var stream = %s.srcObject; var tracks = stream.getTracks();
for (var i = 0; i < tracks.length; i++) {var track = tracks[i]; track.stop()}
video.srcObject = null;''' % self.varId

    def play(self):
        return '''%s.play()''' % self.varId

    def takepicture(self, width: int = 50, height: int = 50):
        """

        Related Pages::

          https://developer.mozilla.org/fr/docs/WebRTC/Prendre_des_photos_avec_la_webcam
        """
        return '''
var canvas = document.createElement("canvas"); canvas.width = %(width)s; canvas.height = %(height)s;
canvas.getContext('2d').drawImage(%(varId)s, 0, 0, canvas.width, canvas.height);
var data = canvas.toDataURL('image/png'); photo.setAttribute('src', data)''' % {
            "varId": self.varId, "width": width, "height": height}

    def record(self, start: bool = True):
        """

        Related Pages::

          https://developer.mozilla.org/fr/docs/WebRTC/Prendre_des_photos_avec_la_webcam
        """
        if not start:
            return ''' window.recorder.stop() '''

        return '''
var stream = %(varId)s.srcObject;
window.recorder = new MediaRecorder(stream, {mimeType: 'video/webm'});

const chunks = [];
window.recorder.ondataavailable = e => chunks.push(e.data);
window.recorder.onstop = e => {
    const blob = new Blob(chunks, { type: chunks[0].type });
    stream.getVideoTracks()[0].stop();

    filename="yourCustomFileName"
    if(window.navigator.msSaveOrOpenBlob) {window.navigator.msSaveBlob(blob, filename)}
    else{
        var elem = window.document.createElement('a');
        elem.href = window.URL.createObjectURL(blob); elem.download = filename;        
        document.body.appendChild(elem); elem.click(); document.body.removeChild(elem)}
}; window.recorder.start()''' % {"varId": self.varId}


class JsHtmlButtonFilter(JsHtml):

    @property
    def content(self):
        """ """
        if self.component.options.is_number:
            return ContentFormatters(
                self.page, "{filter: %s, input: parseFloat(%s), radio: %s, filter2: %s, input2: parseFloat(%s)}" % (
                    self.component.select.dom.content.toStr(),
                    self.component.input.dom.content.toStr(),
                    self.component.radios.dom.content.toStr(),
                    self.component.select2.dom.content.toStr(),
                    self.component.input2.dom.content.toStr()))
        return ContentFormatters(self.page, "{filter: %s, input: %s, radio: %s, filter2: %s, input2: %s}" % (
            self.component.select.dom.content.toStr(),
            self.component.input.dom.content.toStr(),
            self.component.radios.dom.content.toStr(),
            self.component.select2.dom.content.toStr(),
            self.component.input2.dom.content.toStr()))


class JsHtmlTable(JsHtml):

    @property
    def content(self):
        return JsObjects.JsArray.JsArray.get('''
(function(){
   var values = []; %(component)s.querySelectorAll("tr").forEach(function(row){
      var rec = []; row.childNodes.forEach(function(cell){rec.push(cell.innerText)}); values.push(rec)
});return values })()''' % {"component": self.component.dom.varName})


class JsHtmlLi(JsHtmlRich):

    def has_state(self, state: str, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """
        Check if the item in the list has a specific class.
        If it is the case it will run the function.

        :param state: The CSS class
        :param js_funcs: The function to run if the state is defined
        :param profile: Optional. A flag to set the component performance storage
        """
        return self.component.js.if_("%s.classList.contains(%s)" % (
            self.varName, JsUtils.jsConvertData(state, None)), js_funcs, profile=profile)

    def is_active(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """
        Check if the item in the list has the class active.

        :param js_funcs: The function to run if the state is defined
        :param profile: Optional. A flag to set the component performance storage
        """
        return self.has_state("active", js_funcs, profile=profile)
