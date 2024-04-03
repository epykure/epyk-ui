#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import json
from typing import Optional, List
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.html import Html
from epyk.core.html import Defaults
from epyk.core.html.options import OptInputs

#
from epyk.core.js import packages
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlInput
from epyk.core.js.objects import JsComponents
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsTimepicker
from epyk.core.js.packages import JsQueryUi
from epyk.core.js.html import JsHtmlField
from epyk.core.js.html import JsHtmlJqueryUI

# The list of CSS classes
from epyk.core.css.styles import GrpClsInput


class Output(Html.Html):
    name = 'Output'
    tag = "output"

    def __str__(self):
        return '<%(tag)s %(strAttr)s>%(val)s</%(tag)s>' % {
            'strAttr': self.get_attrs(css_class_names=self.style.get_classes()), 'val': self.val, "tag": self.tag}


class Input(Html.Html):
    name = 'Input'
    _option_cls = OptInputs.OptionsInput

    def __init__(self, page: primitives.PageModel, text, placeholder, width, height, html_code, options, attrs,
                 profile):
        super(Input, self).__init__(page, text, html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height, 'box-sizing': 'border-box'})
        value = text['value'] if isinstance(text, dict) else self._vals
        self.set_attrs(attrs={"type": "text", "value": value, "spellcheck": False})
        if placeholder:
            self.attr["placeholder"] = placeholder
        self.set_attrs(attrs=attrs)
        if html_code is not None:
            self.attr["name"] = html_code
        self.style.css.padding = 0
        self.__focus = False
        if self.options.background:
            self.style.css.background_color = page.theme.colors[0]
        if width[0] is None:
            self.style.css.min_width = Defaults.INPUTS_MIN_WIDTH

    @property
    def options(self) -> OptInputs.OptionsInput:
        """Property to set all the input component properties"""
        return super().options

    @property
    def js(self) -> JsHtmlField.InputText:
        """Specific Javascript function for the input object"""
        if self._js is None:
            self._js = JsHtmlField.InputText(self, page=self.page)
        return self._js

    @property
    def dom(self) -> JsHtmlInput.Inputs:
        """Return all the Javascript functions defined for an HTML Input Component.
        Those functions will use plain javascript available for a DOM element by default.

        Usage::

          div = page.ui.input(htmlCode="testDiv")
          print(div.dom.content)

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtmlInput.Inputs(self, page=self.page)
        return self._dom

    @property
    def style(self) -> GrpClsInput.ClassInput:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpClsInput.ClassInput(self)
        return self._styleObj

    def value(self, value):
        self.attr["value"] = value
        return self

    def focus(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
              options: dict = None, source_event: str = None, on_ready: bool = False):
        """Action on focus.

        :param js_funcs: Optional. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param options: Optional. Specific Python options available for this component
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.__focus = True
        if js_funcs is None:
            js_funcs = []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        if options is not None:
            if options.get("reset", False):
                js_funcs.append(self.dom.empty())
            if options.get("select", False):
                js_funcs.append(self.dom.select())
        if self.options.reset:
            js_funcs.append(self.dom.empty())
        if self.options.select:
            js_funcs.append(self.dom.select())
        return self.on("focus", js_funcs, profile, source_event, on_ready)

    def validation(self, pattern: str = None, required: bool = True):
        """Add validation rules on the input component.

        `Doc Patterns <https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/pattern>`_
        `Doc input Patterns <https://www.w3schools.com/tags/att_input_pattern.asp>`_

        Usage::

          input.validation(pattern="[0-9]{5}")

        :param pattern: Optional. Specifies a regular expression that the <input> element's value is checked against
        :param required: Optional. The Boolean required attribute, if present, indicates that the user must specify a
          value for the input before the owning form can be submitted.

        :return: Self to allow the chaining
        """
        if pattern is None and required:
            self.attr["required"] = True
            return self

        self.attr["pattern"] = pattern
        if required:
            self.attr["required"] = None
        self.style.add_classes.input.is_valid()
        return self

    def validation_from(self, values, css_cls=None, disclaimer: str = "&#9888; Error - Invalid value",
                        css_disclaimer: dict = None, on_enter: bool = True):
        """Run more sophisticated validation checks using list or remote services.

        `Doc setCustomValidity <https://developer.mozilla.org/en-US/docs/Web/API/HTMLObjectElement/setCustomValidity>`_

        Usage::

          inp = page.ui.input(html_code="auto")
          request = page.js.post("/validation", components=[inp])
          inp.validation_from(request)

        :param values: Can be a list of items or a XMLHttp request
        :param css_cls: The CSS class for the input when validation error
        :param disclaimer: The disclaimer text
        :param css_disclaimer: CSS attributes for the disclaimer
        :param on_enter: If true, trigger the value when enter is pressed
        """
        dflt_css_disclaimer = {
            "display": "None",
            "font-weight": "900",
            "color": self.page.theme.danger.base
        }
        if css_disclaimer is not None:
            dflt_css_disclaimer.update(css_disclaimer)
        if css_cls is None:
            css_cls = self.style.add_classes.input.is_valid()
        if isinstance(css_cls, str):
            classname = css_cls
        else:
            classname = css_cls.classname
        self.page.properties.js.add_builders(JsUtils.jsConvertFncs([
            self.page.js.createElement("span", "%s_disclaimer" % self.html_code).setAttribute(
                "id", "%s_disclaimer" % self.html_code).css(dflt_css_disclaimer).innerHTML(disclaimer),
            self.dom.parentNode.appendAfter(
                self.page.js.getVar("%s_disclaimer" % self.html_code), self.dom)], toStr=True, profile=False))

        if isinstance(values, list):
            if on_enter:
                self.enter([self.dom.events.trigger("blur")])
            return self.on("blur", [
                self.page.js.if_(self.dom.content.isIn(values), [
                    self.dom.setCustomValidity(""),
                    self.page.js.getElementById("%s_disclaimer" % self.html_code).css("display", "None")
                ]).else_([
                    self.dom.focus(),
                    self.dom.addClass(classname).r,
                    self.dom.setCustomValidity("Invalid field."),
                    self.page.js.getElementById("%s_disclaimer" % self.html_code).css("display", "block")
                ]),
            ])

        elif hasattr(values, "onSuccess"):
            if on_enter:
                self.enter([self.dom.events.trigger("blur")])
            return self.on("blur", [
                values.onSuccess([
                    self.page.js.if_(self.page.js.objects["result"], [
                        self.dom.setCustomValidity(""),
                        self.page.js.getElementById("%s_disclaimer" % self.html_code).css("display", "None")
                    ]).else_([
                        self.dom.focus(),
                        self.dom.setCustomValidity("Invalid field."),
                        self.page.js.if_(self.page.js.objects["disclaimer"], [
                            self.page.js.getElementById("%s_disclaimer" % self.html_code).innerHTML(
                                self.page.js.objects["disclaimer"])
                        ]),
                        self.page.js.getElementById("%s_disclaimer" % self.html_code).css("display", "block")
                    ])
                ])
            ])

        raise ValueError("Validation not predefined for this type of object")

    def enter(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, source_event: str = None,
              on_ready: bool = False):
        """Add an javascript action when the key enter is pressed on the keyboard.

        Usage::

          component.input(placeholder="Put your tag").enter("alert()")

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded

        :return: The python object itself.
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_funcs.append(self.dom.select())
        self.keydown.enter(js_funcs, profile, source_event=source_event)
        return self

    def leave(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
              source_event: str = None, on_ready: bool = False):
        """Add a javascript action when the key enter is pressed on the keyboard.

        Usage::

          component.input(placeholder="Put your tag").enter("alert()")

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded

        :return: The python object itself.
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_funcs.append(self.dom.select())
        self.on("blur", js_funcs, profile, source_event=source_event)
        return self

    def change(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
               source_event: str = None, on_ready: bool = False):
        """The input event fires when the value of an <input>, <select>, or <textarea> element has been changed.

        `Doc event input <https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if on_ready:
            self.page.body.onReady([self.dom.events.trigger("input")])
        return self.on("input", js_funcs, profile, source_event)

    def oninput(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                source_event: str = None, on_ready: bool = False):
        """The input event fires when the value of an <input>, <select>, or <textarea> element has been changed.

        `Doc event input <https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        return self.change(js_funcs=js_funcs, profile=profile, source_event=source_event, on_ready=on_ready)

    def readonly(self, flag: bool = True):
        """Set the input component to be readonly.

        `w3schools <https://www.w3schools.com/tags/att_input_readonly.asp>`_

        :param flag: Optional. Add the HTML readonly tag to the component
        """
        if flag:
            self.attr["readonly"] = "readonly"
        else:
            if "readonly" in self.attr:
                del self.attr["readonly"]

        return self

    @packages.packageImport('jqueryui', 'jqueryui')
    def autocomplete(self, values: List[str], options: dict = None, dataflows: List[dict] = None, css: dict = None,
                     literal: str = None):
        """Add autocompletion for the input html component. Autocompletion is coming from a list of values.

        Usage::

          input = page.ui.inputs.input("test autocomplete")
          input.autocomplete(["AAAAA", "AAABBB", "AAACCC"])
          input.focus(options={"reset": True})

          input.autocomplete(["AUDDDD"], dataflows=[
              {"name": "(function(data){return [{value: 'USDDD', label: 'toto',  desc: 'This is a description'} ]})"}
          ], css={"color": "red"}, literal="<div>${item.label} <br> ${item.desc}</div>")

        `jqueryui <https://jqueryui.com/autocomplete/>`_

        :param values:
        :param options:
        :param dataflows: Chain of data transformations
        :param css: The CSS attributes for the component
        :param literal: The literal expression for the autocompletion items
        """
        if self.attr["type"] != "text":
            raise ValueError("Autocomplete can only be used with input text components")

        css_attrs = ""
        if css is not None:
            css_attrs = ".css(%s)" % json.dumps(css)
        values = JsUtils.dataFlows(values, dataflows, self.page)
        options = options or {}
        if literal is not None:
            self.page.body.onReady('''
%(jqId)s.autocomplete(Object.assign({source: %(vals)s}, %(options)s))%(css)s;
%(jqId)s.autocomplete("instance")._renderItem = function( ul, item ) {
      return $( "<li>" ).append(`<div>%(literal)s</div>`).appendTo(ul)}''' % {
                "jqId": JsQuery.decorate_var(self.dom.varId, convert_var=False), "vals": values, "options": options,
                "css": css_attrs, "literal": literal})
        else:
            self.page.body.onReady('''
%(jqId)s.autocomplete(Object.assign({source: %(vals)s}, %(options)s))%(css)s''' % {
                "jqId": JsQuery.decorate_var(self.dom.varId, convert_var=False), "vals": values, "options": options,
                "css": css_attrs})

    @packages.packageImport('jqueryui', 'jqueryui')
    def autocomplete_from(self, xml_http_request, min_length: int = 3, prefix: str = None, options: dict = None,
                          with_cache: bool = True, dataflows: List[dict] = None, css: dict = None, literal: str = None):
        """Add autocomplete features on textarea from remote service.

        This will use jquery UI.

        Usage::

          t = page.ui.input()
          t.autocomplete_from(page.js.get("/autocomplete"), with_cache=False)

        `jqueryui <https://jqueryui.com/autocomplete//>`_

        :param xml_http_request: The request object to the remote server. Returned data must be a list
        :param prefix: The prefix to be added to the selected item
        :param min_length: The min length before querying the remove server
        :param options: Autocomplete extra options
        :param with_cache: Flag to cache the result to save server calls
        :param dataflows: Chain of data transformations
        :param css: The CSS attributes for the component
        :param literal: The literal expression for the autocompletion items
        """
        if self.attr["type"] != "text":
            raise ValueError("Autocomplete can only be used with input text components")

        cached_var = "cached%s" % self.html_code
        prefix_val = '%s + ui.item.value' % JsUtils.jsConvertData(prefix,
                                                                  None) if prefix is not None else 'ui.item.value'
        css_attrs = ""
        if css is not None:
            css_attrs = ".css(%s)" % json.dumps(css)
        xml_http_request.onSuccess(['''%s = %s; resp($.ui.autocomplete.filter(%s, request.term)) ''' % (
            cached_var, JsUtils.dataFlows(JsUtils.jsWrap("data"), dataflows, self.page), cached_var)])
        options = options or {}
        if literal is not None:
            self.page.body.onReady('''
var %(cachedVar)s; 
%(jqUI)s.autocomplete(Object.assign({
  minLength: %(minLength)s,
  source: function(request, resp) {
    if(%(useCache)s){
      if(typeof %(cachedVar)s === 'undefined'){%(request)s}
      else{resp($.ui.autocomplete.filter(%(cachedVar)s, request.term))}}
    else{%(request)s}},
  }, %(options)s))%(css)s;
%(jqUI)s.autocomplete("instance")._renderItem = function( ul, item ) {
  return $("<li>").append(`<div>%(literal)s</div>`).appendTo(ul)}
''' % {
                "cachedVar": cached_var, "jqUI": JsQuery.decorate_var(self.dom.varId, convert_var=False),
                "useCache": JsUtils.jsConvertData(with_cache, None), "minLength": min_length, "css": css_attrs,
                "request": xml_http_request.toStr(), "options": options, "literal": literal})
        else:
            self.page.body.onReady('''
var %(cachedVar)s; 
%(jqUI)s.autocomplete(Object.assign({
  minLength: %(minLength)s,
  source: function(request, resp) {
    if(%(useCache)s){
      if(typeof %(cachedVar)s === 'undefined'){%(request)s}
      else{resp($.ui.autocomplete.filter(%(cachedVar)s, request.term))}}
    else{%(request)s}},
  }, %(options)s))%(css)s
''' % {
                "cachedVar": cached_var, "jqUI": JsQuery.decorate_var(self.dom.varId, convert_var=False),
                "useCache": JsUtils.jsConvertData(with_cache, None), "minLength": min_length, "css": css_attrs,
                "request": xml_http_request.toStr(), "options": options})

    def __str__(self):
        if not self.__focus and (self.options.reset or self.options.select):
            self.focus()
        if self.options.css:
            self.css(self.options.css)
        if self.options.borders == "bottom":
            self.style.no_class()
            self.style.add_classes.input.basic_border_bottom()
            self.options.borders = None
        elif not self.options.borders and self.options.borders is not None:
            self.style.no_class()
            self.style.add_classes.input.basic_noborder()
            self.options.borders = None
        return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(css_class_names=self.style.get_classes())}


class InputFile(Input):
    name = 'InputFile'
    _option_cls = OptInputs.OptionsInputFile

    def __init__(self, page: primitives.PageModel, text, placeholder, width, height, html_code, options, attrs,
                 profile):
        super(InputFile, self).__init__(page, text, placeholder, width, height, html_code, options, attrs, profile)
        self.set_attrs({"type": 'file'})
        self.set_attrs({"name": "%s[]" % self.html_code})

    @property
    def options(self) -> OptInputs.OptionsInputFile:
        """ Property to set all the input component properties. """
        return super().options

    @property
    def dom(self) -> JsHtmlInput.InputFiles:
        """Return all the Javascript functions defined for an HTML Input Component.

        Those functions will use plain javascript available for a DOM element by default.

        Usage::

          div = page.ui.input(htmlCode="testDiv")
          print(div.dom.content)

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtmlInput.InputFiles(self, page=self.page)
        return self._dom


class InputRadio(Input):
    name = 'Input'

    def __init__(self, page: primitives.PageModel, flag: bool, group_name: str, placeholder: str, width: tuple,
                 height, html_code, options, attrs, profile):
        super(InputRadio, self).__init__(page, "", placeholder, width, height, html_code, options, attrs, profile)
        self.set_attrs({"type": 'radio'})
        if flag:
            self.set_attrs({"checked": json.dumps(flag)})
        if group_name is not None:
            self.set_attrs({"name": group_name})


class AutoComplete(Input):
    name = 'Input Autocomplete'
    requirements = ('jqueryui',)
    _option_cls = OptInputs.OptionAutoComplete

    def __init__(self, page, text, placeholder, width, height, html_code, options, attrs, profile):
        if text is None:
            text = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
        super(AutoComplete, self).__init__(page, text, placeholder, width, height, html_code, options, attrs, profile)
        self.__focus = False
        if self.options.borders == "bottom":
            self.style.clear_class("CssInput")
            self.style.add_classes.input.basic_border_bottom()
            self.options.borders = None
        elif not self.options.borders and self.options.borders is not None:
            self.style.clear_class("CssInput")
            self.style.add_classes.input.basic_noborder()
            self.options.borders = None

    _js__builder__ = '''if(typeof data === 'object'){%(jqId)s.autocomplete(Object.assign(data, options))}
else{%(jqId)s.autocomplete(options)}''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

    @property
    def options(self) -> OptInputs.OptionAutoComplete:
        """Property to set all the input TimePicker component properties.

        `jqueryui <https://timepicker.co/options/>`_
        """
        return super().options

    def focus(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None, options: dict = None,
              source_event: str = None, on_ready: bool = False):
        """Action on focus.

        :param js_funcs: Optional. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param options: Optional. Specific Python options available for this component
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.__focus = True
        if js_funcs is None:
            js_funcs = []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        if options is not None:
            if options.get("reset", False):
                js_funcs.append(self.dom.empty())
            if options.get("select", False):
                js_funcs.append(self.dom.select())
        if self.options.reset:
            js_funcs.append(self.dom.empty())
        if self.options.select:
            js_funcs.append(self.dom.select())
        return self.on("focus", js_funcs, profile, source_event, on_ready)

    @property
    def style(self) -> GrpClsInput.ClassInputAutocomplete:
        """ Property to the CSS Style of the component. """
        if self._styleObj is None:
            self._styleObj = GrpClsInput.ClassInputAutocomplete(self)
        return self._styleObj

    @property
    def js(self) -> JsQueryUi.Autocomplete:
        """ The Javascript functions defined for this component.

        Those can be specific ones for the module or generic ones from the language.
        """
        if self._js is None:
            self._js = JsQueryUi.Autocomplete(self, page=self.page)
        return self._js

    def __str__(self):
        if not self.__focus and (self.options.reset or self.options.select):
            self.focus()
        self.page.properties.js.add_builders(self.refresh())
        return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(css_class_names=self.style.get_classes())}


class InputTime(Input):
    name = 'Input Time'
    requirements = ('timepicker',)
    _option_cls = OptInputs.OptionsTimePicker

    def __init__(self, page: primitives.PageModel, text, placeholder, width, height,
                 html_code, options, attrs, profile):
        if text is None:
            text = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
        super(InputTime, self).__init__(page, text, placeholder, width, height, html_code, options, attrs, profile)
        self.style.css.background_color = page.theme.colors[0]
        self.style.css.line_height = Defaults.LINE_HEIGHT
        self.style.css.text_align = "center"

    @property
    def options(self) -> OptInputs.OptionsTimePicker:
        """Property to set all the input TimePicker component properties.

        `jqueryui <https://timepicker.co/options/>`_
        """
        return super().options

    @property
    def style(self) -> GrpClsInput.ClassInputTime:
        """ Property to the CSS Style of the component. """
        if self._styleObj is None:
            self._styleObj = GrpClsInput.ClassInputTime(self)
        return self._styleObj

    @property
    def dom(self) -> JsHtmlJqueryUI.JsHtmlTimePicker:
        """ The Javascript Dom object. """
        if self._dom is None:
            self._dom = JsHtmlJqueryUI.JsHtmlTimePicker(self, page=self.page)
        return self._dom

    @property
    def js(self) -> JsTimepicker.Timepicker:
        """The Javascript functions defined for this component.

        Those can be specific ones for the module or generic ones from the language.
        """
        if self._js is None:
            self._js = JsTimepicker.Timepicker(self, page=self.page)
        return self._js

    _js__builder__ = '''if (typeof data == "string"){%(jqId)s.timepicker('setTime', data)}
%(jqId)s.timepicker(options); ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

    def change(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, source_event: str = None,
               on_ready: bool = False):
        """Event triggered when the value of the input field changes.

        A Date object containing the selected time is passed as the first argument of the callback.
        Note: the variable time is a function parameter received in the Javascript side.

        `timepicker <https://timepicker.co/options/>`_

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.on("change", js_funcs, profile, self.dom.jquery.varId, on_ready)
        self._browser_data['mouse']['change'][self.dom.jquery.varId]["fncType"] = "on"
        return self

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(css_class_names=self.style.get_classes())}


class InputDate(Input):
    requirements = ('jqueryui',)
    name = 'Input Time'
    _option_cls = OptInputs.OptionsDatePicker

    def __init__(self, page: primitives.PageModel, records, placeholder, width, height,
                 html_code, options, attrs, profile):
        super(InputDate, self).__init__(page, records, placeholder, width, height, html_code, options, attrs, profile)
        if options is not None and options.get("date_from_js", None) is not None:
            self.options.dateJsOvr(options["date_from_js"])

    @property
    def options(self) -> OptInputs.OptionsDatePicker:
        """Property to set all the input DatePicker component properties.

        `timepicker <https://timepicker.co/options/>`_
        """
        return super().options

    @property
    def js(self) -> JsQueryUi.Datepicker:
        """The Javascript functions defined for this component.

        Those can be specific ones for the module or generic ones from the language.
        """
        if self._js is None:
            self._js = JsQueryUi.Datepicker(self, page=self.page)
        return self._js

    @property
    def style(self) -> GrpClsInput.ClassInputDate:
        """ Property to the CSS Style of the component. """
        if self._styleObj is None:
            self._styleObj = GrpClsInput.ClassInputDate(self)
        return self._styleObj

    @property
    def dom(self) -> JsHtmlJqueryUI.JsHtmlDatePicker:
        """ The Javascript Dom object. """
        if self._dom is None:
            self._dom = JsHtmlJqueryUI.JsHtmlDatePicker(self, page=self.page)
        return self._dom

    def excluded_dates(self, dts: List[str] = None, js_funcs: types.JS_FUNCS_TYPES = None,
                       dataflows: List[dict] = None, profile: types.PROFILE_TYPE = None):
        """List of dates to be excluded from the available dates in the DatePicker component.

        :param dts: Optional. Dates excluded format YYYY-MM-DD
        :param js_funcs: Optional. Javascript functions
        :param dataflows: Optional. Chain of data transformations
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        """
        dts = JsUtils.dataFlows(dts, dataflows, self.page)
        self.options.beforeShowDay([''' var utc = value.getTime() - value.getTimezoneOffset()*60000; 
      var newDate = new Date(utc); const dts = %(dts)s; %(jsFnc)s; 
      if(dts.includes(newDate.toISOString().split('T')[0])){return [false, '', '']} 
      else {return [true, '', '']}''' % {
            "dts": dts, 'jsFnc': JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)}], profile=profile)

    def included_dates(self, dts: List[str] = None, selected: str = None, js_funcs: types.JS_FUNCS_TYPES = None,
                       dataflows: List[dict] = None, profile: types.PROFILE_TYPE = None):
        """Define some specific date to be the only ones available from the DatePicker component.

        :param dts: Optional. Dates included format YYYY-MM-DD
        :param selected: Optional. The selected date from the range. Default max
        :param js_funcs: Optional. Javascript functions
        :param dataflows: Optional. Chain of data transformations
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        """
        self._vals = selected or sorted(dts)[-1]
        dts = JsUtils.dataFlows(dts, dataflows, self.page)
        self.options.beforeShowDay(['''
var utc = value.getTime() - value.getTimezoneOffset()*60000; var newDate = new Date(utc); const dts = %(dts)s;
%(jsFnc)s; if(!dts.includes(newDate.toISOString().split('T')[0])){return [false, '', '']} 
else {return [true, '', '']}''' % {
            "dts": dts, 'jsFnc': JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)}], profile=profile)

    def format_dates(self, class_name: str, dts: List[str] = None, css: Optional[dict] = None, tooltip: str = "",
                     profile: types.PROFILE_TYPE = None, dataflows: List[dict] = None):
        """Change the CSS style for some selected dates in the DateIicker.

        This function can be also used on the Javascript side from the js property.

        :param class_name: The name of the CSS added to the page with the CSS attributes
        :param dts: Optional. A list of dates format YYYY-MM-DD
        :param css: Optional. The CSS Attributes for the CSS class
        :param tooltip: Optional. The tooltip when the mouse is hover
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param dataflows: Chain of data transformations
        """
        dts = dts or []
        if css is not None:
            self.page.body.style.custom_class(css, classname="%s a" % class_name)
        self.options.beforeShowDay(['''
var utc = value.getTime() - value.getTimezoneOffset()*60000; var newDate = new Date(utc); const dts = %(dts)s;
if(dts.includes(newDate.toISOString().split('T')[0])){return [true, '%(class_name)s', '%(tooltip)s']} 
else {return [true, '', '']}''' % {
            "dts": JsUtils.dataFlows(dts, dataflows, self.page), 'tooltip': tooltip,
            "class_name": class_name}], profile=profile)

    _js__builder__ = '''if(data == null || options.dateJsOvr){data = options.dateJsOvr}
%(jqId)s.datepicker(options).datepicker('setDate', data)''' % {
        "jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        if self.options.inline:
            return '<div %(strAttr)s></div>' % {'strAttr': self.get_attrs(css_class_names=self.style.get_classes())}

        return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(css_class_names=self.style.get_classes())}


class InputInteger(Input):
    name = 'Input Number'
    _option_cls = OptInputs.OptionsInputInteger

    def __init__(self, page: primitives.PageModel, text, placeholder, width, height, html_code,
                 options, attrs, profile):
        super(InputInteger, self).__init__(page, text, placeholder, width, height, html_code, options, attrs, profile)

    @property
    def options(self) -> OptInputs.OptionsInputInteger:
        """ Property to set all the input component properties. """
        return super().options

    def quantity(self):
        """Add quantity shortcuts to the component.

        This will then check the input and remap if they are K, M and B to the corresponding value.
        """
        factors, units_lookup = {'K': 1000, 'M': 1000000, 'B': 1000000000}, []
        for f, val in factors.items():
            units_lookup.append("if(event.key.toUpperCase() == '%s'){this.value *= %s}" % (f, val))
        self.on('keydown', ";".join(units_lookup))
        return self


class InputRange(Input):
    name = 'Input Range'
    _option_cls = OptInputs.OptionsInputRange

    def __init__(self, page: primitives.PageModel, text, min_val, max_val, step, placeholder, width,
                 height, html_code, options, attrs, profile):
        super(InputRange, self).__init__(page, text, placeholder, width, height, html_code, options, attrs, profile)
        self.input = page.ui.inputs.input(
            text, width=(None, "px"), placeholder=placeholder).css({"vertical-align": 'middle'})
        self.append_child(self.input)
        self.input.set_attrs(attrs={"type": "range", "min": min_val, "max": max_val, "step": step})
        if self.options.output:
            self.style.css.position = "relative"
            self.output = self.page.ui.inputs._output(text).css({
                "width": '15px', "text-align": 'center', "margin-left": '2px', "position": "absolute",
                'color': self.page.theme.colors[-1]})
            self.append_child(self.output)
            self.input.set_attrs(attrs={"oninput": "%s.value=this.value" % self.output.htmlCode})
        self.css({"display": 'inline-block', "vertical-align": 'middle', "line-height": '%spx' % Defaults.LINE_HEIGHT})

    @property
    def options(self) -> OptInputs.OptionsInputRange:
        """ Property to set input range properties. """
        return super().options

    @property
    def style(self) -> GrpClsInput.ClassInputRange:
        """ Property to the CSS Style of the component. """
        if self._styleObj is None:
            self._styleObj = GrpClsInput.ClassInputRange(self)
        return self._styleObj

    def __str__(self):
        if hasattr(self, 'output'):
            self.output.css({"display": 'inline-block'})
        return '<div %(strAttr)s></div>' % {'strAttr': self.get_attrs(css_class_names=self.style.get_classes())}


class Field(Html.Html):
    name = 'Field'

    def __init__(self, page: primitives.PageModel, html_input, label, icon, width, height, html_code,
                 helper, options, profile):
        super(Field, self).__init__(
            page, "", html_code=html_code, profile=profile, css_attrs={"width": width, "height": height})
        self._vals = ""
        # Add the component predefined elements
        self.add_label(label, html_code=self.htmlCode,
                       css={'height': 'auto', 'margin-top': '1px', 'margin-bottom': '1px'},
                       position=options.get("position", 'before'), options=options)
        if self.label and options.get("format") == "column":
            self.label.style.css.float = None
            self.label.style.css.display = "block"
            self.label.style.css.color = self.page.theme.notch()
            self.label.style.css.bold()
            html_input.style.css.width = "auto"
        self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
        # add the input item
        self.input = html_input
        if html_code is not None:
            if "name" not in self.input.attr:
                self.input.attr["name"] = self.input.htmlCode
        self.append_child(self.input)
        self.add_icon(icon, html_code=self.htmlCode, position="after", family=options.get("icon_family"),
                      css={"margin-left": '5px', 'color': self.page.theme.colors[-1]})
        self.css({"margin-top": '5px'})

    @property
    def dom(self) -> JsHtmlField.JsHtmlFields:
        """The HTML Dom object linked to this component.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlField.JsHtmlFields(self, page=self.page)
        return self._dom

    def __str__(self):
        str_div = "".join([v.html() if hasattr(v, 'html') else v for v in self.val])
        return "<div %s>%s%s</div>" % (self.get_attrs(css_class_names=self.style.get_classes()), str_div, self.helper)


class FieldInput(Field):
    name = 'Field Input'

    def __init__(self, page: primitives.PageModel, value, label, placeholder, icon, width, height, html_code,
                 helper, options, profile):
        html_input = page.ui.inputs.input(page.inputs.get(html_code, value), width=(None, "%"), placeholder=placeholder,
                                          html_code="%s_input" % html_code if html_code is not None else html_code,
                                          options=options)
        super(FieldInput, self).__init__(page, html_input, label, icon, width, height, html_code, helper, options,
                                         profile)


class FieldAutocomplete(Field):
    name = 'Field Autocomplete'

    def __init__(self, page: primitives.PageModel, value, label, placeholder, icon, width, height, html_code,
                 helper, options, profile):
        html_input = page.ui.inputs.autocomplete(page.inputs.get(html_code, value), width=(None, "%"),
                                                 placeholder=placeholder, options=options)
        super(FieldAutocomplete, self).__init__(page, html_input, label, icon, width, height, html_code, helper,
                                                options,
                                                profile)

    def change(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Event triggered when the value of the input field changes.

        A Date object containing the selected time is passed as the first argument of the callback.
        Note: the variable time is a function parameter received in the Javascript side.

        `jqueryui <https://api.jqueryui.com/autocomplete/#event-change>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._jsStyles["change"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True,
                                                                                     profile=profile)
        return self

    def search(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Triggered before a search is performed, after minLength and delay are met.

        If canceled, then no request will be started and no items suggested.

        `jqueryui <https://api.jqueryui.com/autocomplete/#event-search>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._jsStyles["search"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True,
                                                                                     profile=profile)
        return self

    def focus(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Triggered when focus is moved to an item (not selecting).

        The default action is to replace the text field's value with the value of the focused item, though only
        if the event was triggered by a keyboard interaction.
        Canceling this event prevents the value from being updated, but does not prevent the menu item from being focused.

        `jqueryui <https://api.jqueryui.com/autocomplete/#event-focus>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._jsStyles["focus"] = "function( event, ui ){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True,
                                                                                      profile=profile)
        return self

    def close(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Triggered when the menu is hidden. Not every close event will be accompanied by a change event.

        `jqueryui <ttps://api.jqueryui.com/autocomplete/#event-close>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._jsStyles["close"] = "function( event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True,
                                                                                     profile=profile)
        return self

    def select(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Triggered when an item is selected from the menu.

        The default action is to replace the text field's value with the value of the selected item.
        Canceling this event prevents the value from being updated, but does not prevent the menu from closing.

        `jqueryui <ttps://api.jqueryui.com/autocomplete/#event-select>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._jsStyles["select"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True,
                                                                                     profile=profile)
        return self

    def response(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Triggered after a search completes, before the menu is shown.

        Useful for local manipulation of suggestion data, where a custom source option callback is not required.
        This event is always triggered when a search completes, even if the menu will not be shown because there are no
        results or the Autocomplete is disabled.

        `jqueryui <ttps://api.jqueryui.com/autocomplete/#event-response>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._jsStyles["response"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(
            js_funcs, toStr=True, profile=profile)
        return self


class FieldRange(Field):
    name = 'Field Range'

    def __init__(self, page: primitives.PageModel, value, min_val, max_val, step, label, placeholder, icon, width,
                 height, html_code, helper, options, profile):
        html_input = page.ui.inputs.d_range(page.inputs.get(html_code, value), min_val=min_val, max_val=max_val,
                                            step=step,
                                            width=(None, "%"), placeholder=placeholder, options=options)
        super(FieldRange, self).__init__(page, html_input, label, icon, width, height, html_code, helper, options,
                                         profile)
        if icon is not None and html_input.options.output:
            html_input.output.style.css.margin_left = 25
        if html_input.options.output:
            self.style.css.min_height = 45


class FieldCheckBox(Field):
    name = 'Field Checkbox'

    def __init__(self, page: primitives.PageModel, value, label, icon, width, height, html_code,
                 helper, options, profile):
        html_input = page.ui.inputs.checkbox(page.inputs.get(html_code, value), width=(None, "%"), options=options)
        super(FieldCheckBox, self).__init__(
            page, html_input, label, icon, width, height, html_code, helper, options, profile)
        if label is not None:
            self.label.style.css.line_height = Defaults.LINE_HEIGHT
            self.label.style.css.margin_bottom = "auto"
            self.label.style.css.margin_top = "auto"
            if options.get('position') == 'after':
                self.label.style.css.float = None
                self.label.style.css.width = 'auto'
                self.input.style.css.float = 'left'
        self.style.css.line_height = Defaults.LINE_HEIGHT
        self.css({"margin-top": '0px'})


class FieldInteger(Field):
    name = 'Field Integer'

    def __init__(self, page: primitives.PageModel, value, label, placeholder, icon, width, height,
                 html_code, helper, options, profile):
        html_input = page.ui.inputs.d_int(
            page.inputs.get(html_code, value), width=(None, "%"), placeholder=placeholder, options=options)
        super(FieldInteger, self).__init__(
            page, html_input, label, icon, width, height, html_code, helper, options, profile)


class FieldFile(Field):
    name = 'Field Integer'

    def __init__(self, page: primitives.PageModel, value, label, placeholder, icon, width, height, html_code,
                 helper, options, profile):
        html_input = page.ui.inputs.file(
            page.inputs.get(html_code, value), width=(None, "%"), placeholder=placeholder, options=options)
        super(FieldFile, self).__init__(
            page, html_input, label, icon, width, height, html_code, helper, options, profile)


class FieldPassword(Field):
    name = 'Field Password'

    def __init__(self, page: primitives.PageModel, value, label, placeholder, icon, width, height, html_code,
                 helper, options, profile):
        html_input = page.ui.inputs.password(
            page.inputs.get(html_code, value), width=(None, "%"), placeholder=placeholder, options=options)
        super(FieldPassword, self).__init__(
            page, html_input, label, icon, width, height, html_code, helper, options, profile)


class FieldTextArea(Field):
    name = 'Field Textarea'

    # TODO add autocomplete: https://jsfiddle.net/Twisty/yfdjyq79/

    def __init__(self, page: primitives.PageModel, value, label, placeholder, icon, width, height, html_code,
                 helper, options, profile):
        html_input = page.ui.inputs.textarea(
            page.inputs.get(html_code, value), width=(100, "%"), placeholder=placeholder, options=options)
        super(FieldTextArea, self).__init__(
            page, html_input, label, icon, width, height, html_code, helper, options, profile)


class FieldSelect(Field):
    name = 'Field Select'

    def __init__(self, page: primitives.PageModel, value, label, icon, width, height, html_code, helper,
                 options, profile):
        html_input = page.ui.select(
            page.inputs.get(html_code, value), "%s_input" % html_code if html_code is not None else html_code,
            width=(100, "%"), options=options)
        html_input.options.iconBase = "iconBase"
        icon_details = page.icons.get("check")
        html_input.options.tickIcon = icon_details["icon"]
        if icon_details['icon_family'] != 'bootstrap-icons':
            self.requirements = (icon_details['icon_family'],)
        super(FieldSelect, self).__init__(page, html_input, label, icon, width, height, html_code, helper, options,
                                          profile)
        if label is not None:
            self.label.style.css.line_height = None


class InputCheckbox(Html.Html):
    name = 'Checkbox'

    def __init__(self, page: primitives.PageModel, flag, label, group_name, width, height, html_code, options,
                 attrs, profile):
        if html_code in page.inputs:
            page.inputs[html_code] = True if page.inputs[html_code] == 'true' else False
            if page.inputs[html_code]:
                flag = True
        if flag:
            attrs["checked"] = flag
        super(InputCheckbox, self).__init__(
            page, {"value": flag}, html_code=html_code, profile=profile, options=options,
            css_attrs={"width": width, "height": height})
        self.set_attrs(attrs={"type": "checkbox"})
        if group_name is not None:
            self.attr["name"] = group_name
        self.set_attrs(attrs=attrs)
        self.css({"cursor": 'pointer', 'display': 'inline-block', 'vertical-align': 'middle', 'margin-left': '2px'})
        self.style.css.height = Defaults.LINE_HEIGHT
        self._label = label or ''
        self.style.add_classes.div.no_focus_outline()

    @property
    def dom(self) -> JsHtmlField.Check:
        """Return all the Javascript functions defined for an HTML Component.

        Those functions will use plain javascript by default.
        """
        if self._dom is None:
            self._dom = JsHtmlField.Check(self, page=self.page)
        return self._dom

    @property
    def js(self) -> JsComponents.Radio:
        """The Javascript functions defined for this component.

        Those can be specific ones for the module or generic ones from the language.
        """
        if self._js is None:
            self._js = JsComponents.Radio(self, page=self.page)
        return self._js

    def __str__(self):
        return '<input %(strAttr)s>%(label)s' % {
            'strAttr': self.get_attrs(css_class_names=self.style.get_classes()), 'label': self._label}


class Radio(Html.Html):
    name = 'Radio'

    def __init__(self, page: primitives.PageModel, flag, label, group_name, icon, width, height, html_code, helper,
                 options, profile):
        super(Radio, self).__init__(page, {"value": flag, 'text': label}, html_code=html_code,
                                    css_attrs={"width": width, 'height': height}, profile=profile)
        self.add_input("", position="before", css={
            "width": 'none', "vertical-align": 'middle', "margin-bottom": 0,
            "height": "{}px".format(Defaults.LINE_HEIGHT)})
        self.add_label(label, html_code=self.html_code, position="after",
                       css={"display": 'inline-block', "width": "auto", 'float': "none"})
        self.input.set_attrs(name="data-content", value=label)
        if flag:
            self.input.set_attrs({"checked": json.dumps(flag)})
        self.input.style.clear()
        if group_name is not None:
            self.input.set_attrs(name="name", value=group_name)
        else:
            self.input.set_attrs(name="name", value=self.html_code)
        self.input.set_attrs(attrs={"type": "radio"})
        self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
        self.input.css(
            {"cursor": 'pointer', 'display': 'inline-block', 'vertical-align': 'middle', 'min-width': 'none'})
        self.css({'vertical-align': 'middle', 'text-align': "left"})
        self.add_icon(icon, html_code=self.html_code, position="after", family=options.get("icon_family"),
                      css={"margin-left": '5px', 'color': self.page.theme.success[1]})
        self.style.css.line_height = Defaults.LINE_HEIGHT
        self.label.click([self.input.dom.events.fire("click")])
        self.badge = ""

    @property
    def dom(self) -> JsHtmlField.Radio:
        """Return all the Javascript functions defined for an HTML Component.

        Those functions will use plain javascript by default.
        """
        if self._dom is None:
            self._dom = JsHtmlField.Radio(self, page=self.page)
        return self._dom

    @property
    def js(self) -> JsComponents.Radio:
        """The Javascript functions defined for this component.

        Those can be specific ones for the module or generic ones from the language.
        """
        if self._js is None:
            self._js = JsComponents.Radio(self, page=self.page)
        return self._js

    def add_badge(self, value, background_color: str = None, parent_html_code: str = None, **kwargs):
        """Add badge to a defined component.

        :param value: Badge value
        :param background_color: Badge's background color
        :param parent_html_code: Badge's parent code
        """
        if self.label:
            self.label.add_badge(value, background_color)
            self.badge = self.label.badge
            return self

        self.label.style.css.margin = "0 5px 0 0"
        return super(Radio, self).add_badge(
            value, width="5px", background_color=background_color, parent_html_code=self.input.html_code)

    def __str__(self):
        return '<div %(strAttr)s>%(badge)s%(helper)s</div>' % {
            'strAttr': self.get_attrs(css_class_names=self.style.get_classes()), 'helper': self.helper,
            "badge": "" if self.label else self.badge}


class TextArea(Html.Html):
    name = 'Text Area'

    def __init__(self, page: primitives.PageModel, text, width, rows, placeholder, background_color,
                 html_code, options, profile):
        super(TextArea, self).__init__(page, text, html_code=html_code, profile=profile,
                                       css_attrs={"width": width, 'box-sizing': 'border-box'})
        self.rows, self.background_color = rows, background_color
        self.style.add_classes.input.textarea()
        self.set_attrs({"rows": rows, "placeholder": placeholder or ""})
        self.__options = OptInputs.OptionsTextarea(self, options)

    @property
    def options(self) -> OptInputs.OptionsTextarea:
        """ Property to set all the input component properties. """
        return self.__options

    def selectable(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None):
        """

        :param js_funcs: Optional. Javascript functions
        :param profile: Optional. A flag to set the component performance storage

        :return: self. to allow the function chaining
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.attr['onclick'] = "this.blur();this.select();%s" % JsUtils.jsConvertFncs(js_funcs, toStr=True,
                                                                                      profile=profile)
        return self

    @packages.packageImport('jqueryui', 'jqueryui')
    def autocomplete(self, values: List[str], min_length: int = 0, prefix: str = None,
                     options: dict = None, dataflows: List[dict] = None, css: dict = None):
        """Add autocomplete features on textarea.

        This will use jquery UI.

        Usage::

          t = page.ui.textarea()
          t.autocomplete(["Python", "Pascal", "JavaScript", "Java"])
          t.autocomplete(["Python", "Pascal", "JavaScript", "Java"], prefix="\u2022 ")

        `jqueryui <https://jqueryui.com/autocomplete/>`_

        :param values: static values for the autocomplete
        :param prefix: The prefix to be added to the selected item
        :param min_length: The min length before displaying the result
        :param options: Autocomplete extra options
        :param dataflows: Chain of data transformations
        :param css: Optional. CSS attributes
        """
        values = JsUtils.dataFlows(values, dataflows, self.page)
        options = options or {}
        prefix_val = '%s + ui.item.value' % JsUtils.jsConvertData(prefix,
                                                                  None) if prefix is not None else 'ui.item.value'
        css_attrs = ""
        if css is not None:
            css_attrs = ".css(%s)" % json.dumps(css)
        self.page.body.onReady('''
%s.autocomplete(Object.assign({
  minLength: %s,
  source: function(request, response){
    response($.ui.autocomplete.filter(%s, request.term.split("\\n").pop()))},
  focus: function() {return false},
  select: function(event, ui) {
      var terms = this.value.split("\\n"); terms.pop();
      terms.push(%s); terms.push("");
      this.value = terms.join("\\r\\n"); return false}
  }, %s))%s
''' % (JsQuery.decorate_var(self.dom.varId, convert_var=False), min_length, values, prefix_val, options, css_attrs))

    @packages.packageImport('jqueryui', 'jqueryui')
    def autocomplete_from(self, xml_http_request, min_length: int = 3, prefix: str = None, options: dict = None,
                          with_cache: bool = True, dataflows: List[dict] = None, css: dict = None):
        """Add autocomplete features on textarea from remote service.

        This will use jquery UI.

        Usage::

          t = page.ui.textarea()
          t.autocomplete_from(page.js.get("/autocomplete"), with_cache=False)

        `jqueryui <https://jqueryui.com/autocomplete/>`_

        :param xml_http_request: The request object to the remote server. Returned data must be a list
        :param prefix: Optional. The prefix to be added to the selected item
        :param min_length: Optional. The min length before querying the remove server
        :param options: Optional. Autocomplete extra options
        :param with_cache: Optional. Flag to cache the result to save server calls
        :param dataflows: Optional. Chain of data transformations
        :param css: Optional. CSS attributes
        """
        cached_var = "cached%s" % self.html_code
        prefix_val = '%s + ui.item.value' % JsUtils.jsConvertData(prefix,
                                                                  None) if prefix is not None else 'ui.item.value'
        data_ref = JsUtils.dataFlows(JsUtils.jsWrap("data"), dataflows, self.page)
        xml_http_request.onSuccess(['''
resp($.ui.autocomplete.filter(%s = %s, request.term.split("\\n").pop())) 
''' % (cached_var, data_ref)])
        options = options or {}
        css_attrs = ""
        if css is not None:
            css_attrs = ".css(%s)" % json.dumps(css)
        self.page.body.onReady('''
var %(cachedVar)s; 
%(jqUI)s.autocomplete(Object.assign({
  minLength: %(minLength)s,
  source: function(request, resp) {
    if(%(useCache)s){
      if(typeof %(cachedVar)s === 'undefined'){%(request)s}
      else{resp($.ui.autocomplete.filter(%(cachedVar)s, request.term.split("\\n").pop()))}}
    else{%(request)s}
  },
  focus: function() {return false},
  select: function(event, ui){
      var terms = this.value.split("\\n"); terms.pop();
      terms.push(%(prefixVal)s); terms.push("");
      this.value = terms.join("\\r\\n"); return false}
  }, %(options)s))%(css)s
''' % {"cachedVar": cached_var, "jqUI": JsQuery.decorate_var(self.dom.varId, convert_var=False),
       "useCache": JsUtils.jsConvertData(with_cache, None), "minLength": min_length, "css": css_attrs,
       "prefixVal": prefix_val, "request": xml_http_request.toStr(), "options": options})

    def validation(self, pattern: str, required: bool = True):
        """Add validation rules on the input component.

        Usage::

          input.validation(pattern="[0-9]{5}")

        :param pattern:
        :param required: Optional.

        :return: Self to allow the chaining
        """
        self.attr["pattern"] = pattern
        if required:
            self.attr["required"] = None
        self.style.add_classes.input.is_valid()
        return self

    def validation_from(self, values, css_cls=None, disclaimer="&#9888; Error - Invalid value",
                        css_disclaimer: dict = None, on_enter: bool = True):
        """Run more sophisticated validation checks using list or remote services.

        Usage::

          inp = page.ui.input(html_code="auto")
          request = page.js.post("/validation", components=[inp])
          inp.validation_from(request)

        :param values: Can be a list of items or a XMLHttp request
        :param css_cls: Optional. The CSS class for the input when validation error
        :param disclaimer: Optional. The disclaimer text
        :param css_disclaimer: Optional. CSS attributes for the disclaimer
        :param on_enter: Optional. If trye, trigger the value when enter is pressed
        """
        dflt_css_disclaimer = {
            "display": "None",
            "font-weight": "900",
            "color": self.page.theme.danger.base
        }
        if css_disclaimer is not None:
            dflt_css_disclaimer.update(css_disclaimer)
        if css_cls is None:
            css_cls = self.style.add_classes.input.is_valid()
        if isinstance(css_cls, str):
            classname = css_cls
        else:
            classname = css_cls.classname
        self.page.properties.js.add_builders(JsUtils.jsConvertFncs([
            self.page.js.createElement("span", "%s_disclaimer" % self.html_code).setAttribute(
                "id", "%s_disclaimer" % self.html_code).css(dflt_css_disclaimer).innerHTML(disclaimer),
            self.dom.parentNode.appendAfter(
                self.page.js.getVar("%s_disclaimer" % self.html_code), self.dom)], toStr=True, profile=False))

        if isinstance(values, list):
            if on_enter:
                self.enter([self.dom.events.trigger("blur")])
            return self.on("blur", [
                self.page.js.if_(self.dom.content.isIn(values), [
                    self.dom.setCustomValidity(""),
                    self.page.js.getElementById("%s_disclaimer" % self.html_code).css("display", "None")
                ]).else_([
                    self.dom.focus(),
                    self.dom.addClass(classname).r,
                    self.dom.setCustomValidity("Invalid field."),
                    self.page.js.getElementById("%s_disclaimer" % self.html_code).css("display", "block")
                ]),
            ])

        elif hasattr(values, "onSuccess"):
            if on_enter:
                self.enter([self.dom.events.trigger("blur")])
            return self.on("blur", [
                values.onSuccess([
                    self.page.js.if_(self.page.js.objects["result"], [
                        self.dom.setCustomValidity(""),
                        self.page.js.getElementById("%s_disclaimer" % self.html_code).css("display", "None")
                    ]).else_([
                        self.dom.focus(),
                        self.dom.setCustomValidity("Invalid field."),
                        self.page.js.if_(self.page.js.objects["disclaimer"], [
                            self.page.js.getElementById("%s_disclaimer" % self.html_code).innerHTML(
                                self.page.js.objects["disclaimer"])
                        ]),
                        self.page.js.getElementById("%s_disclaimer" % self.html_code).css("display", "block")
                    ])
                ])
            ])

        raise ValueError("Validation not predefined for this type of object")

    @property
    def dom(self) -> JsHtmlField.Textarea:
        """Return all the Javascript functions defined for an HTML Component.

        Those functions will use plain javascript by default.

        `w3schools <https://www.w3schools.com/js/js_htmldom.asp/>`_
        """
        if self._dom is None:
            self._dom = JsHtmlField.Textarea(self, page=self.page)
        return self._dom

    def change(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
               source_event: str = None, on_ready: bool = False):
        """The input event fires when the value of an <input>, <select>, or <textarea> element has been changed.

        `mozilla <hhttps://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event/>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if on_ready:
            self.page.body.onReady([self.dom.events.trigger("input")])
        return self.on("input", js_funcs, profile, source_event)

    def enter(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
              source_event: str = None, on_ready: bool = False):
        """Add a javascript action when the key enter is pressed on the keyboard.

        Usage::

          component.enter(" alert() ")

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded

        :return: The python object itself
        """
        return self.on("keydown", ["if (event.keyCode  == 13) {event.preventDefault(); %(jsFnc)s} " % {
            "jsFnc": JsUtils.jsConvertFncs(
                js_funcs, toStr=True, profile=profile)}], profile=profile, source_event=source_event, on_ready=on_ready)

    def __str__(self):
        return '<textarea %(strAttr)s>%(val)s</textarea>' % {
            "strAttr": self.get_attrs(css_class_names=self.style.get_classes()), 'val': self.val}


class Search(Html.Html):
    name = 'Search'

    def __init__(self, page: primitives.PageModel, text, placeholder, color, width, height, html_code, tooltip,
                 extensible, options, profile):
        if options.get('icon_family') is not None and options['icon_family'] != 'bootstrap-icons':
            self.requirements = (options['icon_family'],)
        super(Search, self).__init__(page, "", html_code=html_code, css_attrs={"height": height}, profile=profile)
        self.color = 'inherit' if color is None else color
        self.css({"display": "inline-block", "margin-bottom": '2px', 'box-sizing': 'border-box'})
        if not extensible:
            self.style.add_classes.layout.search()
            self.style.css.width = "%s%s" % (width[0], width[1])
        else:
            self.style.add_classes.layout.search_extension(max_width=width)
        self.add_input(text, options=options).input.set_attrs({"placeholder": placeholder, "spellcheck": False})
        if options["icon"]:
            self.add_icon(options["icon"], css={"color": page.theme.colors[4]}, html_code=self.htmlCode,
                          family=options.get("icon_family")).icon.attr['id'] = "%s_button" % self.htmlCode
            self.icon.style.css.z_index = 10
            self.icon.style.css.font_factor(-3)
            self.dom.trigger = self.icon.dom.trigger
        else:
            self.icon = False
        self.style.css.position = "relative"

        if options.get("position", 'left') == 'left':
            self.input.css({"text-align": 'left', 'padding-left': '2px', 'padding-right': '2px'})
            if self.icon:
                self.input.css({'padding-left': '%spx' % self.page.body.style.globals.line_height})
                self.icon.css(
                    {"margin": '5px 5px 5px 5px', 'display': 'block', 'cursor': 'pointer', 'position': 'absolute',
                     'vertical-align': 'top'})
        else:
            self.input.css({"text-align": 'left', 'padding-left': "2px", 'padding-right': '2px'})
            if self.icon:
                self.input.css({'padding-right': '%spx' % self.page.body.style.globals.line_height})
                self.icon.css({"margin": '5px 5px 5px 5px', 'cursor': 'pointer', "right": 0,
                               'position': 'absolute', 'vertical-align': 'top'})
        if options.get("groups") is not None:
            self.select = self.page.ui.select([{"value": g, "name": g} for g in options.get("groups")],
                                              width=(200, 'px'),
                                              html_code="%s_select" % html_code if html_code is not None else None)
            self.select.style.clear_all(no_default=True)
            self.page.properties.css.add_text('''
.bootstrap-select .btn:focus{
    outline: 0 !important;
    -webkit-box-shadow: inset 0 0 0 rgba(0,0,0,.075),0 0 0 rgba(102,175,233,.6);
    box-shadow: inset 0 0 0 rgba(0,0,0,.075),0 0 0 rgba(102,175,233,.6);
}''')
            self.prepend_child(self.select)
            self.input.style.css.width = "calc(100% - 250px)"
            if self.icon:
                self.icon.css({"margin": '-35px 5px 5px 205px'})
        self.tooltip(tooltip)
        self.input.style.css.background = "inherit"
        self.input.style.css.padding_left = self.page.body.style.globals.line_height
        self.input.attr["type"] = "search"

    @property
    def dom(self) -> JsHtmlField.JsHtmlFields:
        """Return all the Javascript functions defined for an HTML Component.

        Those functions will use plain javascript by default.
        """
        if self._dom is None:
            self._dom = JsHtmlField.JsHtmlFields(self, page=self.page)
        return self._dom

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
              source_event: str = None, on_ready: bool = False):
        """

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        return self.icon.click(js_funcs, profile, source_event, on_ready=on_ready)

    def enter(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
              source_event: str = None, on_ready: bool = False):
        """Add an javascript action when the key enter is pressed on the keyboard.

        Usage::

          component.enter(" alert() ")

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded

        :return: The python object itself
        """
        if self.icon:
            self.click(js_funcs)
            return self.on("keydown", ["if (event.keyCode  == 13) {event.preventDefault(); %(jsFnc)s} " % {
                "jsFnc": self.icon.dom.events.trigger("click")}], profile=profile, source_event=source_event,
                           on_ready=on_ready)

        return self.on("keydown", ["if (event.keyCode  == 13) {event.preventDefault(); %(jsFnc)s} " % {
            "jsFnc": JsUtils.jsConvertFncs(
                js_funcs, toStr=True, profile=profile)}], profile=profile, source_event=source_event, on_ready=on_ready)

    def __str__(self):
        return '<div %(attr)s></div>' % {"attr": self.get_attrs(css_class_names=self.style.get_classes())}
