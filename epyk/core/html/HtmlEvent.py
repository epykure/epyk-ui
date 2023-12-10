#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
from typing import Union, Optional, Any
from pathlib import Path

from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.html import Html
from epyk.core.html.options import OptSliders
from epyk.core.html.options import OptList

from epyk.core.html.entities import EntHtml4

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlJqueryUI
from epyk.core.js.html import JsHtmlList
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi
from epyk.core.js.packages import JsComponents

# The list of CSS classes
from epyk.core.css.styles import GrpClsJqueryUI
from epyk.core.css import Defaults as cssDefaults


class ProgressBar(Html.Html):
    requirements = ('jqueryui',)
    name = 'Progress Bar'
    _option_cls = OptSliders.OptionsProgBar
    tag = "div"

    def __init__(self, page: primitives.PageModel, number: float, total, width: tuple,
                 height: tuple, helper: Optional[str], options: Optional[dict], html_code: Optional[str],
                 profile: Optional[Union[dict, bool]], verbose: bool = False):
        options['max'] = total
        super(ProgressBar, self).__init__(page, number, html_code=html_code, profile=profile, options=options,
                                          css_attrs={"width": width, "height": height, 'box-sizing': 'border-box'},
                                          verbose=verbose)
        self.add_helper(helper)
        self.options.background = self.page.theme.success.base
        self.style.css.background = self.page.theme.greys[0]
        self.options.border_color = self.page.theme.greys[0]

    @property
    def options(self) -> OptSliders.OptionsProgBar:
        """The progress bar is designed to display the current percent complete for a process.
        The bar is coded to be flexibly sized through CSS and will scale to fit inside its parent container by default.

        `Package Doc <https://api.jqueryui.com/progressbar>`_
        """
        return super().options

    def to(self, number: float, timer: int = 10):
        """Move the progress bar to a defined level in a specific amount of time in millisecond.

        :param number: The final state for the progress bar
        :param timer: Optional. the appended of the increase in millisecond
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

    _js__builder__ = '''options.value = parseFloat(data);
var tooltip_val = ""+ (options.value / options.max * 100).toFixed(options.digits) +"%% ("+ options.value +" / "+ options.max +")";
%(jqId)s.progressbar(options).find('div').attr("data-toggle", "tooltip").attr("title", tooltip_val).attr("alt", tooltip_val).css(options.css);
if(options.show_percentage){%(jqId)s.children('span').html(data + '%%')};
''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

    @property
    def js(self) -> JsQueryUi.ProgressBar:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        `Package Doc <https://api.jqueryui.com/progressbar>`_

        :return: A Javascript Dom object
        """
        if self._js is None:
            self._js = JsQueryUi.ProgressBar(self, page=self.page)
        return self._js

    @property
    def dom(self) -> JsHtmlJqueryUI.JsHtmlProgressBar:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlJqueryUI.JsHtmlProgressBar(self, page=self.page)
        return self._dom

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        if self.options.show_percentage:
            return '<div %s><span style="position: absolute;margin: -1px 0 0 5px; "></span></div>%s' % (
                self.get_attrs(css_class_names=self.style.get_classes()), self.helper)

        return '<%s %s></%s>%s' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag, self.helper)


class Menu(Html.Html):
    requirements = ('jqueryui',)
    name = 'Menu'
    _option_cls = OptSliders.OptionsMenu
    tag = "ul"

    def __init__(self, page, records, width, height, helper, options, html_code, profile, verbose: bool = False):
        super(Menu, self).__init__(page, records, html_code=html_code, profile=profile, options=options,
                                   css_attrs={"width": width, "height": height}, verbose=verbose)
        self.add_helper(helper)
        self.style.css.display = 'block'
        self.style.css.position = 'relative'

    @property
    def style(self) -> GrpClsJqueryUI.ClassMenu:
        """Property to the CSS Style of the component."""
        if self._styleObj is None:
            self._styleObj = GrpClsJqueryUI.ClassMenu(self)
        return self._styleObj

    @property
    def options(self) -> OptSliders.OptionsMenu:
        """Property to the comments component options.
        Optional can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.

        `Package Doc <https://api.jqueryui.com/menu>`_
        """
        return super().options

    @property
    def js(self) -> JsQueryUi.Menu:
        """The Javascript functions defined for this component.
        Those can be specific ones for the module or generic ones from the language.

        `Package Doc <https://api.jqueryui.com/menu>`_

        :return: A Javascript Dom object
        """
        if self._js is None:
            self._js = JsQueryUi.Menu(self, page=self.page)
        return self._js

    @property
    def dom(self) -> JsHtmlJqueryUI.JsHtmlProgressBar:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlJqueryUI.JsHtmlProgressBar(self, page=self.page)
        return self._dom

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<%(tag)s %(attrs)s></%(tag)s>%(helper)s' % {
            "attrs": self.get_attrs(css_class_names=self.style.get_classes()), "helper": self.helper, "tag": self.tag}


class Dialog(Html.Html):
    requirements = ('jqueryui',)
    name = 'Menu'
    tag = "div"
    _option_cls = OptSliders.OptionDialog

    def __init__(self, report: primitives.PageModel, text: Union[Html.Html, str], width: tuple, height: tuple,
                 helper: str,
                 options: Optional[dict], html_code: Optional[str], profile: Optional[Union[bool, dict]],
                 verbose: bool = False):
        super(Dialog, self).__init__(report, text, css_attrs={"width": width, "height": height}, html_code=html_code,
                                     profile=profile, options=options, verbose=verbose)
        self.add_helper(helper)
        if hasattr(text, "options"):
            self.components[text.htmlCode] = text
            text.options.managed = False
            self.options.empty = False
            self._vals = ""

    @property
    def options(self) -> OptSliders.OptionDialog:
        """Property to the comments component options.
        Optional can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.

        `Package Doc <https://jqueryui.com/dialog/>`_
        """
        return super().options

    _js__builder__ = '''if(options.empty){%(jqId)s.empty()}; %(jqId)s.append('<p>'+ data +'</p>'); %(jqId)s.dialog(options)''' % {
        "jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

    @property
    def js(self) -> JsQueryUi.Dialog:
        """Open content in an interactive overlay.
        `Package Doc <https://jqueryui.com/dialog/>`_

        :return: A Javascript Dom object
        """
        if self._js is None:
            self._js = JsQueryUi.Dialog(self, page=self.page)
        return self._js

    @property
    def dom(self) -> JsHtmlJqueryUI.JsHtmlProgressBar:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlJqueryUI.JsHtmlProgressBar(self, page=self.page)
        return self._dom

    def __str__(self):
        static_content = []
        for component in self.components.values():
            static_content.append(str(component))
        # TODO Find a fix for this
        if self.options.verbose and "bootstrap" in self.page.jsImports:
            logging.warning("JqueryUI Dialog:")
            logging.warning("This component might have some conflicts with Bootstrap")
            logging.warning(
                "More details https://stackoverflow.com/questions/8681707/jqueryui-modal-dialog-does-not-show-close-button-x")
        self.page.properties.js.add_builders(self.refresh())
        return '<%s %s>%s%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), "".join(static_content), self.helper,
            self.tag)


class Slider(Html.Html):
    requirements = ('jqueryui',)
    name = 'Slider'
    _option_cls = OptSliders.OptionsSlider
    is_range = False

    def __init__(self, page: primitives.PageModel, number: int, min_val: float, max_val: float,
                 width: tuple, height: tuple, helper: Optional[str], options: Optional[dict],
                 html_code: Optional[str], profile: Optional[Union[bool, dict]], verbose: bool = False):
        options.update({'max': max_val, 'min': min_val})
        super(Slider, self).__init__(page, number, html_code=html_code, profile=profile, options=options,
                                     css_attrs={"width": width, "height": height}, verbose=verbose)
        if self.options.show_min_max:
            self.style.css.padding = "0 10px"
        self.style.css.margin = "15px 0"
        self.add_helper(helper)
        self.__output = None

    @property
    def output(self) -> Html.Html:
        if self.__output is None:
            self.__output = self.page.ui.tags.span(html_code="out_%s" % self.html_code)
            self.__output.attr["class"].clear()
            self.__output.css({"position": "relative", "top": "15px", "font-size": "14px", "width": "80px",
                               "display": "inline-block", "text-align": "center", "left": "-35px"})
            self.__output.attr["name"] = "out_%s" % self.html_code
            self.__output.onReady(["%(jqId)s.find('.ui-slider-handle').append(%(outComp)s)" % {
                "jqId": self.js.varId,
                "outComp": self.__output.js.jquery.varId}])
            self.options.js_tree['out_builder_opts'] = self.__output.options.config_js()
            native_path = os.environ.get("NATIVE_JS_PATH")
            internal_native_path = Path(Path(__file__).resolve().parent, "..", "js", "native")
            if native_path is None:
                native_path = internal_native_path
            native_builder = Path(native_path, "%s.js" % self.__output.builder_name)
            internal_native_builder = Path(internal_native_path, "%s.js" % self.__output.builder_name)
            if native_builder.exists():
                self.page.js.customFile("%s.js" % self.__output.builder_name, path=native_path)
                self.options.js_tree['out_builder_fnc'] = "%s%s" % (
                self.__output.builder_name[0].lower(), self.__output.builder_name[1:])
                self.page.properties.js.add_constructor(self.__output.builder_name, None)
            elif internal_native_builder.exists():
                self.page.js.customFile("%s.js" % self.__output.builder_name, path=internal_native_builder)
                self.options.js_tree['out_builder_fnc'] = "%s%s" % (
                    self.__output.builder_name[0].lower(), self.__output.builder_name[1:])
                self.__output.page.properties.js.add_constructor(self.__output.builder_name, None)
            else:
                self.page.properties.js.add_constructor(self.__output.builder_name,
                                                        "function %s(htmlObj, data, options){%s}" % (
                                                            self.__output.builder_name, self.__output._js__builder__))
        return self.__output

    @output.setter
    def output(self, component: Html.Html):
        self.__output = component
        self.options.force_show_current = True
        native_path = os.environ.get("NATIVE_JS_PATH")
        internal_native_path = Path(Path(__file__).resolve().parent, "..", "js", "native")
        if native_path is None:
            native_path = internal_native_path
        native_builder = Path(native_path, "%s.js" % self.__output.builder_name)
        internal_native_builder = Path(internal_native_path, "%s.js" % self.__output.builder_name)
        if native_builder.exists():
            self.page.js.customFile("%s.js" % self.__output.builder_name, path=native_path)
            self.options.js_tree['out_builder_fnc'] = "%s%s" % (
            self.__output.builder_name[0].lower(), self.__output.builder_name[1:])
            self.page.properties.js.add_constructor(self.__output.builder_name, None)
        elif internal_native_builder.exists():
            self.page.js.customFile("%s.js" % self.__output.builder_name, path=internal_native_builder)
            self.options.js_tree['out_builder_fnc'] = "%s%s" % (
            self.__output.builder_name[0].lower(), self.__output.builder_name[1:])
            self.page.properties.js.add_constructor(self.__output.builder_name, None)
        else:
            self.options.js_tree['out_builder_fnc'] = self.__output.builder_name
            self.options.js_tree['out_builder_opts'] = self.__output.options.config_js()
            self.page.properties.js.add_constructor(self.__output.builder_name,
                                                    "function %s(htmlObj, data, options){%s}" % (
                                                        self.__output.builder_name, self.__output._js__builder__))
        component.attr["name"] = "out_%s" % self.html_code

    @property
    def options(self) -> OptSliders.OptionsSlider:
        """Property to the comments component options.
        Optional can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def style(self) -> GrpClsJqueryUI.ClassSlider:
        """Property to the CSS Style of the component. """
        if self._styleObj is None:
            self._styleObj = GrpClsJqueryUI.ClassSlider(self)
        return self._styleObj

    @property
    def js(self) -> JsQueryUi.Slider:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        `Related Pages <https://api.jqueryui.com/slider>`_

        :return: A Javascript Dom object
        """
        if self._js is None:
            self._js = JsQueryUi.Slider(self, page=self.page)
        return self._js

    def change(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, on_ready: bool = False):
        """Triggered after the user slides a handle, if the value has changed
        or if the value is changed programmatically via the value method.

        `Related Pages <https://api.jqueryui.com/slider/#event-change>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param on_ready: Optional. Trigger the change event when page is ready
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.options.change(JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self

    def start(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Triggered when the user starts sliding.

        `Related Pages <https://api.jqueryui.com/slider/#event-start>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._jsStyles["start"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True,
                                                                                    profile=profile)
        return self

    def slide(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Triggered when the user starts sliding.

        `Related Pages <https://api.jqueryui.com/slider/#event-slide>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._jsStyles["slide"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(
            js_funcs, toStr=True, profile=profile)
        return self

    def stop(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Triggered after the user slides a handle.

        `Related Pages <https://api.jqueryui.com/slider/#event-stop>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._jsStyles["stop"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(
            js_funcs, toStr=True, profile=profile)
        return self

    @property
    def dom(self) -> JsHtmlJqueryUI.JsHtmlSlider:
        """ The Javascript Dom object. """
        if self._dom is None:
            self._dom = JsHtmlJqueryUI.JsHtmlSlider(self, page=self.page)
        return self._dom

    _js__builder__ = '''options.value = data; %(jqId)s.slider(options).css(options.css);
if (typeof options.handler_css !== 'undefined'){%(jqId)s.find('.ui-slider-handle').css(options.handler_css)}
if((typeof options.out_builder_fnc !== "undefined") && (typeof window[options.out_builder_fnc] !== "undefined")){
  window[options.out_builder_fnc](document.getElementsByName('out_'+ htmlObj.id)[0], data, options.out_builder_opts); 
}''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        if 'slide' in self.options.js_tree:
            self.page.properties.js.add_builders(self.js.slide(self._vals))

        if self.options.show_min_max:
            return '''<div %(strAttr)s>
  <div style="width:100%%;height:20px">
    <span style="float:left;display:inline-block">%(min)s</span>
    <span style="float:right;display:inline-block">%(max)s</span>
  </div>
  <div id="%(htmlCode)s"></div>
</div>%(helper)s''' % {"strAttr": self.get_attrs(with_id=False), "min": self.options.min,
                       "htmlCode": self.htmlCode, "max": self.options.max, "helper": self.helper}
        return '''<div %(strAttr)s>
  <div id="%(htmlCode)s"></div>
</div>%(helper)s''' % {"strAttr": self.get_attrs(with_id=False), "min": self.options.min,
                       "htmlCode": self.htmlCode, "max": self.options.max, "helper": self.helper}


class Range(Slider):
    name = "Slider Range"
    is_range = True

    _js__builder__ = '''options.values = [Math.min(...data), Math.max(...data)]; %(jqId)s.slider(options).css(options.css);
if (typeof options.handler_css !== 'undefined'){%(jqId)s.find('.ui-slider-handle').css(options.handler_css)}
''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}


class SliderDate(Slider):
    name = "Slider Date"

    def __init__(self, page: primitives.PageModel, number: Union[float, list], min_val: float, max_val: float,
                 width: Union[tuple, int], height: Union[tuple, int], helper: str, options: dict, html_code: str,
                 profile: Union[dict, bool], verbose: bool = False):
        super(SliderDate, self).__init__(page, number, min_val, max_val, width, height, helper, options, html_code,
                                         profile, verbose=verbose)
        self.options.min, self.options.max, self.options.step = min_val, max_val, 86400

    _js__builder__ = '''
const minDt = new Date(options.min).getTime() / 1000; const maxDt = new Date(options.max).getTime() / 1000;      
options.min = minDt; options.max = maxDt; options.value = new Date(data).getTime() / 1000;
%(jqId)s.slider(options).css(options.css)''' % {
        "jqId": JsQuery.decorate_var("jQuery(htmlObj)", convert_var=False)}

    @property
    def dom(self) -> JsHtmlJqueryUI.JsHtmlSliderDate:
        """The Javascript Dom object. """
        if self._dom is None:
            self._dom = JsHtmlJqueryUI.JsHtmlSliderDate(self, page=self.page)
        return self._dom


class SliderDates(SliderDate):
    _js__builder__ = '''const minDt = new Date(options.min).getTime() / 1000; 
const maxDt = new Date(options.max).getTime() / 1000; options.min = minDt; options.max = maxDt; 
options.values = [new Date(data[0]).getTime() / 1000, new Date(data[1]).getTime() / 1000];
%(jqId)s.slider(options).css(options.css)''' % {
        "jqId": JsQuery.decorate_var("jQuery(htmlObj)", convert_var=False)}

    @property
    def dom(self) -> JsHtmlJqueryUI.JsHtmlSliderDates:
        """The Javascript Dom object. """
        if self._dom is None:
            self._dom = JsHtmlJqueryUI.JsHtmlSliderDates(self, page=self.page)
        return self._dom


class SkillBar(Html.Html):
    name = 'Skill Bars'
    _option_cls = OptSliders.OptionsSkillbars

    def __init__(self, page: primitives.PageModel, data, y_column, x_axis, title, width, height, html_code,
                 options, profile, verbose: bool = False):
        super(SkillBar, self).__init__(page, "", html_code=html_code, profile=profile, options=options,
                                       css_attrs={"width": width, "height": height}, verbose=verbose)
        self.add_title(title, options={'content_table': False})
        self.innerPyHTML = page.ui.layouts.table(options={"header": False})
        self.innerPyHTML.options.managed = False
        self.options.value = y_column
        self.options.label = x_axis
        for rec in data:
            value = page.ui.div(EntHtml4.NO_BREAK_SPACE).css(
                {"width": '%s%s' % (rec[y_column], options.get("unit", '%')), 'margin-left': "2px",
                 "background": options.get("background", page.theme.success.light)})
            value.options.managed = False
            if options.get("values", False):
                self.innerPyHTML += [rec[x_axis], value, "%s%s" % (int(rec[y_column]), options.get("unit", 'px'))]
                self.innerPyHTML[-1][2].style.css.padding = "0 5px"
            else:
                self.innerPyHTML += [rec[x_axis], value]
            self.innerPyHTML[-1][1].attr["align"] = 'left'
            self.innerPyHTML[-1][0].style.css.padding = "0 5px"
            self.innerPyHTML[-1][1].style.css.width = "100%"
            if options.get("borders", False):
                self.innerPyHTML[-1][1].style.css.border = "1px solid %s" % page.theme.greys[4]
                self.innerPyHTML[-1][1][0].style.css.margin_left = 0
        self.innerPyHTML.style.clear()
        self.css({"margin": '5px 0'})
        self.options.set_thresholds()

    @property
    def options(self) -> OptSliders.OptionsSkillbars:
        """Property to the comments component options.

        Optional can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def js(self) -> JsComponents.SkillBar:
        """The JavaScript predefined functions for this component.

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsComponents.SkillBar(self, js_code=self.dom.varName, page=self.page)
        return self._js

    def __str__(self):
        for row in self.innerPyHTML:
            if row is None:
                break

            percent = int(float(row[1][0].css("width")[:-1]))
            if percent > self.options.thresholds[1]:
                row[1][0].style.css.background = self.options.success
            elif percent > self.options.thresholds[0]:
                row[1][0].style.css.background = self.options.warning
            else:
                row[1][0].style.css.background = self.options.danger
            row[1][0].style.css.line_height = row[1][0].style.css.line_height or 20
            row[1][0].style.css.font_factor(-2)
            if self.options.percentage:
                row[1][0]._vals = [row[1][0].css("width")]
                row[1][0].style.css.padding_left = 5
        return '<div %s>%s</div>' % (self.get_attrs(css_class_names=self.style.get_classes()), self.content)


class OptionsBar(Html.Html):
    requirements = (cssDefaults.ICON_FAMILY,)
    name = 'Options'
    _option_cls = OptSliders.OptionBar
    tag = "div"

    def __init__(self, page: primitives.PageModel, records, width: tuple, height: tuple, color: str,
                 options: Optional[dict], profile: Optional[Union[bool, dict]], verbose: bool = False):
        super(OptionsBar, self).__init__(page, [], css_attrs={"width": width, 'height': height},
                                         profile=profile, options=options, verbose=verbose)
        self.css({'padding': '0', 'display': 'block', 'text-align': 'middle', 'color': color, 'margin-left': '5px',
                  'background': self.page.theme.greys[0]})
        for rec in records:
            self += rec
        if self.options.draggable:
            self.draggable()

    @property
    def options(self) -> OptSliders.OptionBar:
        """Property to the comments component options.

        Optional can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def __add__(self, icon):
        """Add items to a container """
        icon = self.page.ui.icon(icon)
        icon.style.css.margin = "5px"
        super(OptionsBar, self).__add__(icon)
        return self

    def draggable(self, options: dict = None, *args, **kwargs):
        self.css({'border-radius': '5px', "border": "1px dotted %s" % self.page.theme.success.base})
        self.page.properties.js.add_builders(self.dom.jquery_ui.draggable(options).toStr())
        return self

    def __str__(self):
        str_html = "".join([v.html() for v in self.val])
        return '<%(tag)s %(attrs)s>%(icons)s</%(tag)s>' % {
            "tag": self.tag, 'attrs': self.get_attrs(css_class_names=self.style.get_classes()), 'icons': str_html}


class SignIn(Html.Html):
    requirements = (cssDefaults.ICON_FAMILY,)
    name = 'SignIn'

    def __init__(self, page: primitives.PageModel, text: Optional[str], size: tuple, icon: Optional[str],
                 verbose: bool = False):
        super(SignIn, self).__init__(page, text, css_attrs={"width": size, 'height': size}, verbose=verbose)
        self.size, self.icon = "%s%s" % (size[0] - 8, size[1]), icon
        self.css({"text-align": "center", "padding": 0, 'color': self.page.theme.colors[3],
                  "margin": 0, "border-radius": "%s%s" % (size[0], size[1]), "display": "inline-block",
                  "border": "1px solid %s" % self.page.theme.colors[3], 'cursor': 'pointer'})

    def __str__(self):
        if not hasattr(self.page, 'user') or self.page.user == 'local':
            icon_details = self.page.icons.get(self.icon or "user")
            self.attr["class"].add(icon_details["icon"])
            self.style.css.font_family = "Font Awesome 5 Free"
            self.style.css.padding = "2px"
            self.style.css.font_size = self.size
            return '<i title="Guest Mode" %(attrs)s></i>' % {
                'size': self.size, 'attrs': self.get_attrs(css_class_names=self.style.get_classes())}

        return '''<div title="%(user)s" %(attrs)s>
<p style="font-size:%(size)s;line-height:%(height)s;margin:0;padding:0">%(letter)s</p>
</div> ''' % {'size': self.size, 'height': self.style.css.height, 'letter': self.page.user[0].upper(),
              'user': self.page.user, 'attrs': self.get_attrs(css_class_names=self.style.get_classes())}


class Filters(Html.Html):
    name = 'Filters'
    requirements = (cssDefaults.ICON_FAMILY,)
    _option_cls = OptList.OptionsTagItems

    def __init__(self, page: primitives.PageModel, items, width, height, html_code, helper, options, profile,
                 verbose: bool = False):
        super(Filters, self).__init__(page, items, html_code=html_code, profile=profile, options=options,
                                      css_attrs={"width": width, "min-height": height}, verbose=verbose)
        self.input = self.page.ui.input()
        self.input.style.css.text_align = 'left'
        self.input.style.css.padding = '0 5px'
        self.input.options.managed = False
        self.selections = self.page.ui.div()
        self.selections.options.managed = False
        self.selections.attr["name"] = "panel"
        self.selections.css({'min-height': '30px', 'padding': '5px 2px'})
        self.add_helper(helper)
        self.__enter_def = False

    @property
    def options(self) -> OptList.OptionsTagItems:
        """Property to the comments component options.

        Optional can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def enter(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Javascript event triggered by the enter key.

        :param js_funcs: The JavaScript events.
        :param profile: Optional. A flag to set the component performance storage.
        """
        self.__enter_def = True
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.keydown.enter([JsUtils.jsConvertFncs(js_funcs, toStr=True),
                            self.dom.add(self.dom.input)] + js_funcs + [self.input.dom.empty()], profile)
        return self

    def drop(self, js_funcs: types.JS_FUNCS_TYPES, prevent_default: bool = True, profile: types.PROFILE_TYPE = None):
        """

        :param js_funcs: The Javascript functions.
        :param prevent_default:
        :param profile: Optional. A flag to set the component performance storage.
        """
        self.style.css.border = "1px dashed black"
        self.tooltip("Drag and drop values here")
        return super(Filters, self).drop(js_funcs, prevent_default, profile)

    def delete(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """

        :param js_funcs: The Javascript functions.
        :param profile: Optional. A flag to set the component performance storage.
        """
        if self.__enter_def:
            raise ValueError("delete on chip must be triggered before enter")

        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._jsStyles['delete'] = JsUtils.jsConvertFncs(
            ["this.parentNode.remove()"] + js_funcs, toStr=True, profile=profile)
        return self

    def append(self, value: Any, category: Optional[str] = None, name: Optional[str] = None,
               disabled: bool = False, fixed: bool = False):
        """

        :param value:
        :param category:
        :param name:
        :param disabled:
        :param fixed:
        """
        rec = {"value": value, 'disabled': disabled, 'fixed': fixed, 'category': category, 'name': name}
        if category is None:
            rec['category'] = name or self.options.category
        rec['name'] = name or rec['category']
        self._vals.append(rec)

    def draggable(self, js_funcs: types.JS_FUNCS_TYPES = None, options: dict = None,
                  profile: types.PROFILE_TYPE = None, source_event: str = None):
        """Set the Filters component draggable.

        :param js_funcs: Javascript functions
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        js_funcs = js_funcs or []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_funcs.append('event.dataTransfer.setData("text", value)')
        self.options.draggable = "function(event, value){%s} " % JsUtils.jsConvertFncs(
            js_funcs, toStr=True, profile=profile)
        return self

    @property
    def dom(self) -> JsHtmlList.Tags:
        """The Javascript Dom object. """
        if self._dom is None:
            self._dom = JsHtmlList.Tags(self, page=self.page)
        return self._dom

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        self.page.properties.js.add_constructor('ChipAdd', '''function chipAdd(panel, record, options){
if(typeof(record.category !== "undefined")){options.category = record.category}
var div = document.createElement("div"); 
for (var key in options.item_css){div.style[key] = options.item_css[key]};
div.setAttribute('data-category', record.category);
if(typeof(record.css !== "undefined")){
  for (var key in record.css){ div.style[key] = record.css[key]}};
var content = document.createElement("span"); 
for (var key in options.value_css){ content.style[key] = options.value_css[key]};
content.setAttribute('name', 'chip_value'); content.innerHTML = record.value; 
if(options.visible){
  var p = document.createElement("p"); 
  for (var key in options.category_css){p.style[key] = options.category_css[key]};
  p.innerHTML = record.name; div.appendChild(p)}
div.appendChild(content);
if(!record.fixed && options.delete){
  var icon = document.createElement("i"); 
  for (var key in options.icon_css){icon.style[key] = options.icon_css[key] };
  icon.classList.add('fas'); icon.classList.add('fa-times'); 
  icon.addEventListener('click', function(){eval(options.delete)});
  div.appendChild(icon)}
if(typeof options.draggable !== 'undefined'){
  div.setAttribute('draggable', true); div.style.cursor = 'grab';
  div.ondragstart = function(event){ var value = this.innerHTML; options.draggable(event, value) }
}
panel.appendChild(div);

const maxHeight = options.max_height;
if(maxHeight > 0){
  panel.style.maxHeight = ""+ maxHeight + "px";
  panel.style.overflow = "hidden"; panel.style.position = "relative";
  var div = document.createElement("div"); div.style.color = "#3366BB";
  div.innerHTML = "Show all"; div.style.position = "absolute"; 
  div.style.bottom = 0; div.style.cursor = "pointer";
  div.addEventListener("click", function(event){ 
    var targetElement = event.target || event.srcElement;
    if (targetElement.innerHTML != "reduce"){panel.style.maxHeight = null; targetElement.innerHTML = "reduce"} 
    else {panel.style.maxHeight = ""+ maxHeight + "px"; targetElement.innerHTML = "Show all"}});
  div.style.right = "5px"; panel.appendChild(div)
}}''')
        if not self.options.visible:
            self.input.style.css.display = False
        return '''<div %(attrs)s>%(input)s%(selections)s</div>%(helper)s''' % {
            'attrs': self.get_attrs(css_class_names=self.style.get_classes()),
            'input': self.input.html(), 'selections': self.selections.html(), 'helper': self.helper}
