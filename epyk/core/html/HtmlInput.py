#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import json
from typing import Union, Optional, List

from epyk.core.html import Html
from epyk.core.html import Defaults
from epyk.core.html.options import OptInputs

#
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
from epyk.core.css import Defaults as Defaults_css


class Output(Html.Html):
  name = 'Output'

  def __str__(self):
    return '<output %(strAttr)s>%(val)s</output>' % {
      'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'val': self.val}


class Input(Html.Html):
  name = 'Input'
  _option_cls = OptInputs.OptionsInput

  def __init__(self, report, text, placeholder, width, height, html_code, options, attrs, profile):
    super(Input, self).__init__(report, text, html_code=html_code, profile=profile, options=options,
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
      self.style.css.background_color = report.theme.colors[0]
    if width[0] is None:
      self.style.css.min_width = Defaults.INPUTS_MIN_WIDTH

  @property
  def options(self) -> OptInputs.OptionsInput:
    """
    Description:
    -----------
    Property to set all the input component properties.

    :rtype: OptInputs.OptionsInput
    """
    return super().options

  @property
  def js(self) -> JsHtmlField.InputText:
    """
    Description:
    -----------
    Specific Javascript function for the input object.

    :rtype: JsHtmlField.InputText
    """
    if self._js is None:
      self._js = JsHtmlField.InputText(self, self.page)
    return self._js

  @property
  def dom(self) -> JsHtmlInput.Inputs:
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Input Component.
    Those functions will use plain javascript available for a DOM element by default.

    Usage::

      div = page.ui.input(htmlCode="testDiv")
      print(div.dom.content)

    :return: A Javascript Dom object.

    :rtype: JsHtmlInput.Inputs
    """
    if self._dom is None:
      self._dom = JsHtmlInput.Inputs(self, report=self.page)
    return self._dom

  @property
  def style(self) -> GrpClsInput.ClassInput:
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: GrpClsInput.ClassInput
    """
    if self._styleObj is None:
      self._styleObj = GrpClsInput.ClassInput(self)
    return self._styleObj

  def value(self, value):
    self.attr["value"] = value
    return self

  _js__builder__ = '''
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}
      if(typeof options.formatMoney !== 'undefined'){ htmlObj.value = accounting.formatMoney(data, 
        options.formatMoney.symbol, options.formatMoney.digit, 
        options.formatMoney.thousand, options.formatMoney.decimal)}
      else if(typeof options.formatNumber !== 'undefined'){ htmlObj.value = accounting.formatNumber(data,
        options.formatNumber.digit, options.formatNumber.thousand)}
      else if(typeof options.toFixed !== 'undefined'){ htmlObj.value = accounting.toFixed(data, options.toFixed) }
      else { htmlObj.value = data; }
      '''

  def focus(self, js_funcs=None, profile=None, options=None, source_event=None, on_ready=False):
    """
    Description:
    -----------
    Action on focus.

    Attributes:
    ----------
    :param js_funcs: List | String. Optional. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param source_event: String. Optional. The JavaScript DOM source for the event (can be a sug item).
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
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

  def validation(self, pattern: str, required: bool = True):
    """
    Description:
    -----------
    Add validation rules on the input component.

    Usage::

      input.validation(pattern="[0-9]{5}")

    Attributes:
    ----------
    :param str pattern:
    :param bool required: Optional.

    :return: Self to allow the chaining
    """
    self.attr["pattern"] = pattern
    if required:
      self.attr["required"] = None
    self.style.add_classes.input.is_valid()
    return self

  def enter(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    ------------
    Add an javascript action when the key enter is pressed on the keyboard.

    Usage::

      component.input(placeholder="Put your tag").enter("alert()")

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.

    :return: The python object itself.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append(self.dom.select())
    self.keydown.enter(js_funcs, profile, source_event=source_event)
    return self

  def leave(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    ------------
    Add an javascript action when the key enter is pressed on the keyboard.

    Usage::

      component.input(placeholder="Put your tag").enter("alert()")

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.

    :return: The python object itself.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append(self.dom.select())
    self.on("blur", js_funcs, profile, source_event=source_event)
    return self

  def change(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
             source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    ------------
    The input event fires when the value of an <input>, <select>, or <textarea> element has been changed.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if on_ready:
      self.page.body.onReady([self.dom.events.trigger("input")])
    return self.on("input", js_funcs, profile, source_event)

  def readonly(self, flag: bool = True):
    """
    Description:
    ------------
    Set the input component to be readonly.

    Related Pages:

      https://www.w3schools.com/tags/att_input_readonly.asp

    Attributes:
    ----------
    :param flag: Boolean. Optional. Add the HTML readonly tag to the component.
    """
    if flag:
      self.attr["readonly"] = "readonly"
    else:
      if "readonly" in self.attr:
        del self.attr["readonly"]

    return self

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

    return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class InputRadio(Input):
  name = 'Input'

  def __init__(self, report, flag, group_name, placeholder, width, height, html_code, options, attrs, profile):
    super(InputRadio, self).__init__(report, "", placeholder, width, height, html_code, options, attrs, profile)
    self.set_attrs({"type": 'radio'})
    if flag:
      self.set_attrs({"checked": json.dumps(flag)})
    if group_name is not None:
      self.set_attrs({"name": group_name})


class AutoComplete(Input):
  name = 'Input Autocomplete'
  requirements = ('jqueryui', )
  _option_cls = OptInputs.OptionAutoComplete

  def __init__(self, report, text, placeholder, width, height, html_code, options, attrs, profile):
    if text is None:
      text = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
    super(AutoComplete, self).__init__(report, text, placeholder, width, height, html_code, options, attrs, profile)
    self.__focus = False
    if self.options.borders == "bottom":
      self.style.clear_class("CssInput")
      self.style.add_classes.input.basic_border_bottom()
      self.options.borders = None
    elif not self.options.borders and self.options.borders is not None:
      self.style.clear_class("CssInput")
      self.style.add_classes.input.basic_noborder()
      self.options.borders = None

  _js__builder__ = '''
    if(typeof data === 'object'){%(jqId)s.autocomplete(Object.assign(data, options))}
    else{%(jqId)s.autocomplete(options)}
    ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  @property
  def options(self) -> OptInputs.OptionAutoComplete:
    """
    Description:
    ------------
    Property to set all the input TimePicker component properties.

    Related Pages:

      https://timepicker.co/options/

    :rtype: OptInputs.OptionAutoComplete
    """
    return super().options

  def focus(self, js_funcs=None, profile=None, options=None, source_event=None, on_ready=False):
    """
    Description:
    -----------
    Action on focus.

    Attributes:
    ----------
    :param js_funcs: List | String. Optional. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
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
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: GrpClsInput.ClassInputAutocomplete
    """
    if self._styleObj is None:
      self._styleObj = GrpClsInput.ClassInputAutocomplete(self)
    return self._styleObj

  @property
  def js(self) -> JsQueryUi.Autocomplete:
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    :rtype: JsQueryUi.Autocomplete
    """
    if self._js is None:
      self._js = JsQueryUi.Autocomplete(self, report=self.page)
    return self._js

  def __str__(self):
    if not self.__focus and (self.options.reset or self.options.select):
      self.focus()
    self.page.properties.js.add_builders(self.refresh())
    return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class InputTime(Input):
  name = 'Input Time'
  requirements = ('timepicker', )
  _option_cls = OptInputs.OptionsTimePicker

  def __init__(self, report, text, placeholder, width, height, html_code, options, attrs, profile):
    if text is None:
      text = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
    super(InputTime, self).__init__(report, text, placeholder, width, height, html_code, options, attrs, profile)
    self.style.css.background_color = report.theme.colors[0]
    self.style.css.line_height = Defaults.LINE_HEIGHT
    self.style.css.text_align = "center"

  @property
  def options(self) -> OptInputs.OptionsTimePicker:
    """
    Description:
    ------------
    Property to set all the input TimePicker component properties.

    Related Pages:

      https://timepicker.co/options/

    :rtype: OptInputs.OptionsTimePicker
    """
    return super().options

  @property
  def style(self) -> GrpClsInput.ClassInputTime:
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: GrpClsInput.ClassInputTime
    """
    if self._styleObj is None:
      self._styleObj = GrpClsInput.ClassInputTime(self)
    return self._styleObj

  @property
  def dom(self) -> JsHtmlJqueryUI.JsHtmlTimePicker:
    """
    Description:
    ------------
    The Javascript Dom object.

    :rtype: JsHtmlJqueryUI.JsHtmlTimePicker
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlTimePicker(self, report=self.page)
    return self._dom

  @property
  def js(self) -> JsTimepicker.Timepicker:
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    :rtype: JsTimepicker.Timepicker
    """
    if self._js is None:
      self._js = JsTimepicker.Timepicker(self, report=self.page)
    return self._js

  _js__builder__ = '''
      if (typeof data == "string"){%(jqId)s.timepicker('setTime', data)}
      %(jqId)s.timepicker(options); ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  def change(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    -----------
    Event triggered when the value of the input field changes.

    A Date object containing the selected time is passed as the first argument of the callback.
    Note: the variable time is a function parameter received in the Javascript side.

    Related Pages:

      https://timepicker.co/options/

    Attributes:
    ----------
    :param js_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    self.on("change", js_funcs, profile, self.dom.jquery.varId, on_ready)
    self._browser_data['mouse']['change'][self.dom.jquery.varId]["fncType"] = "on"
    return self

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class InputDate(Input):
  requirements = ('jqueryui', )
  name = 'Input Time'
  _option_cls = OptInputs.OptionsDatePicker

  def __init__(self, report, records, placeholder, width, height, html_code, options, attrs, profile):
    super(InputDate, self).__init__(report, records, placeholder, width, height, html_code, options, attrs, profile)
    if options.get("date_from_js", None) is not None:
      self.options.dateJsOvr(options["date_from_js"])

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the input DatePicker component properties.

    Related Pages:

      https://timepicker.co/options/

    :rtype: OptInputs.OptionsDatePicker
    """
    return super().options

  @property
  def js(self):
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    :rtype: JsQueryUi.Datepicker
    """
    if self._js is None:
      self._js = JsQueryUi.Datepicker(self, report=self.page)
    return self._js

  @property
  def style(self) -> GrpClsInput.ClassInputDate:
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: GrpClsInput.ClassInputDate
    """
    if self._styleObj is None:
      self._styleObj = GrpClsInput.ClassInputDate(self)
    return self._styleObj

  @property
  def dom(self) -> JsHtmlJqueryUI.JsHtmlDatePicker:
    """
    Description:
    ------------
    The Javascript Dom object.

    :rtype: JsHtmlJqueryUI.JsHtmlDatePicker
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlDatePicker(self, report=self.page)
    return self._dom

  def excluded_dates(self, dts: List[str] = None, js_funcs: Optional[Union[list, str]] = None,
                     profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    ------------
    List of dates to be excluded from the available dates in the DatePicker component.

    Attributes:
    ----------
    :param List[str] dts: Optional. Dates excluded format YYYY-MM-DD.
    :param Optional[Union[list, str]] js_funcs: Optional. Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. Set to true to get the profile for the function on the Javascript console.
    """
    self.options.beforeShowDay([''' var utc = value.getTime() - value.getTimezoneOffset()*60000; 
      var newDate = new Date(utc); const dts = %(dts)s; %(jsFnc)s; 
      if(dts.includes(newDate.toISOString().split('T')[0])){return [false, '', '']} 
      else {return [true, '', '']}''' % {
        "dts": json.dumps(dts or []), 'jsFnc': JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)}],
                               profile=profile)

  def included_dates(self, dts: List[str] = None, selected: str = None, js_funcs: Optional[Union[list, str]] = None,
                     profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    ------------
    Define some specific date to be the only ones available from the DatePicker component.

    Attributes:
    ----------
    :param List[str] dts: Optional. Dates included format YYYY-MM-DD.
    :param str selected: Optional. The selected date from the range. Default max.
    :param Optional[Union[list, str]] js_funcs: Optional. Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. Set to true to get the profile for the function on the Javascript console.
    """
    self._vals = selected or sorted(dts)[-1]
    self.options.beforeShowDay(['''
      var utc = value.getTime() - value.getTimezoneOffset()*60000; var newDate = new Date(utc); const dts = %(dts)s;
      %(jsFnc)s; if(!dts.includes(newDate.toISOString().split('T')[0])){return [false, '', '']} 
      else {return [true, '', '']}''' % {
        "dts": json.dumps(dts or []), 'jsFnc': JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)}],
                               profile=profile)

  def format_dates(self, class_name: str, dts: List[str] = None, css: Optional[dict] = None, tooltip: str = "",
                   profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    ------------
    Change the CSS style for some selected dates in the DateIicker.
    This function can be also used on the Javascript side from the js property.

    Attributes:
    ----------
    :param str class_name: The name of the CSS added to the page with the CSS attributes.
    :param List[str] dts: Optional. A list of dates format YYYY-MM-DD.
    :param Optional[dict] css: Optional. The CSS Attributes for the CSS class.
    :param str tooltip: Optional. The tooltip when the mouse is hover.
    :param Optional[Union[bool, dict]] profile: Optional. Set to true to get the profile for the function on the Javascript console.
    """
    dts = dts or []
    if css is not None:
      self.page.body.style.custom_class(css, classname="%s a" % class_name)
    self.options.beforeShowDay(['''
        var utc = value.getTime() - value.getTimezoneOffset()*60000; var newDate = new Date(utc); const dts = %(dts)s;
        if(dts.includes(newDate.toISOString().split('T')[0])){return [true, '%(class_name)s', '%(tooltip)s']} 
        else {return [true, '', '']}''' % {"dts": JsUtils.jsConvertData(dts, None), 'tooltip': tooltip,
                                           "class_name": class_name}], profile=profile)

  _js__builder__ = '''
      if(data == null || options.dateJsOvr){data = options.dateJsOvr}
      %(jqId)s.datepicker(options).datepicker('setDate', data)''' % {
    "jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    if self.options.inline:
      return '<div %(strAttr)s></div>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}

    return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class InputInteger(Input):
  name = 'Input Number'
  _option_cls = OptInputs.OptionsInputInteger

  def __init__(self, report, text, placeholder, width, height, html_code, options, attrs, profile):
    super(InputInteger, self).__init__(report, text, placeholder, width, height, html_code, options, attrs, profile)

  @property
  def options(self) -> OptInputs.OptionsInputInteger:
    """
    Description:
    -----------
    Property to set all the input component properties.

    :rtype: OptInputs.OptionsInputInteger
    """
    return super().options

  def quantity(self):
    """
    Description:
    -----------
    Add quantity shortcuts to the component.
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

  def __init__(self, report, text, min_val, max_val, step, placeholder, width, height, html_code, options, attrs,
               profile):
    super(InputRange, self).__init__(report, text, placeholder, width, height, html_code, options, attrs, profile)
    self.input = report.ui.inputs.input(text, width=(None, "px"),
                                        placeholder=placeholder).css({"vertical-align": 'middle'})
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
    """
    Description:
    ------------
    Property to set input range properties.

    :rtype: OptInputs.OptionsInputRange
    """
    return super().options

  @property
  def style(self) -> GrpClsInput.ClassInputRange:
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: GrpClsInput.ClassInputRange
    """
    if self._styleObj is None:
      self._styleObj = GrpClsInput.ClassInputRange(self)
    return self._styleObj

  def __str__(self):
    if hasattr(self, 'output'):
      self.output.css({"display": 'inline-block'})
    return '<div %(strAttr)s></div>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class Field(Html.Html):
  name = 'Field'

  def __init__(self, report, html_input, label, icon, width, height, html_code, helper, options, profile):
    super(Field, self).__init__(report, "", html_code=html_code, profile=profile,
                                css_attrs={"width": width, "height": height})
    self._vals = ""
    # Add the component predefined elements
    self.add_label(label, html_code=self.htmlCode, css={'height': 'auto', 'margin-top': '1px', 'margin-bottom': '1px'},
                   position=options.get("position", 'before'),  options=options)
    if self.label and options.get("format") == "column":
      self.label.style.css.float = None
      self.label.style.css.display = "block"
      self.label.style.css.color = self.page.theme.notch()
      self.label.style.css.bold()
      html_input.style.css.min_width = "100%"
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
    """
    Description:
    -----------
    The HTML Dom object linked to this component.

    :return: A Javascript Dom object

    :rtype: JsHtmlField.JsHtmlFields
    """
    if self._dom is None:
      self._dom = JsHtmlField.JsHtmlFields(self, report=self.page)
    return self._dom

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else v for v in self.val])
    return "<div %s>%s%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_div, self.helper)


class FieldInput(Field):
  name = 'Field Input'

  def __init__(self, report, value, label, placeholder, icon, width, height, html_code, helper, options, profile):
    html_input = report.ui.inputs.input(report.inputs.get(html_code, value), width=(None, "%"), placeholder=placeholder,
                                        html_code="%s_input" % html_code if html_code is not None else html_code,
                                        options=options)
    super(FieldInput, self).__init__(
      report, html_input, label, icon, width, height, html_code, helper, options, profile)


class FieldAutocomplete(Field):
  name = 'Field Autocomplete'

  def __init__(self, report, value, label, placeholder, icon, width, height, html_code, helper, options, profile):
    html_input = report.ui.inputs.autocomplete(report.inputs.get(html_code, value), width=(None, "%"),
                                               placeholder=placeholder, options=options)
    super(FieldAutocomplete, self).__init__(report, html_input, label, icon, width, height, html_code, helper, options,
                                            profile)

  def change(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    -----------
    Event triggered when the value of the input field changes.

    A Date object containing the selected time is passed as the first argument of the callback.
    Note: the variable time is a function parameter received in the Javascript side.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-change

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles["change"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def search(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    -----------
    Triggered before a search is performed, after minLength and delay are met.
    If canceled, then no request will be started and no items suggested.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-search

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles["search"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def focus(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    -----------
    Triggered when focus is moved to an item (not selecting).
    The default action is to replace the text field's value with the value of the focused item, though only
    if the event was triggered by a keyboard interaction.
    Canceling this event prevents the value from being updated, but does not prevent the menu item from being focused.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-focus

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles["focus"] = "function( event, ui ){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def close(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    -----------
    Triggered when the menu is hidden. Not every close event will be accompanied by a change event.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-close

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles["close"] = "function( event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def select(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    -----------
    Triggered when an item is selected from the menu.
    The default action is to replace the text field's value with the value of the selected item.
    Canceling this event prevents the value from being updated, but does not prevent the menu from closing.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-select

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles["select"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def response(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    -----------
    Triggered after a search completes, before the menu is shown.

    Useful for local manipulation of suggestion data, where a custom source option callback is not required.
    This event is always triggered when a search completes, even if the menu will not be shown because there are no
    results or the Autocomplete is disabled.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-response

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles["response"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile)
    return self


class FieldRange(Field):
  name = 'Field Range'

  def __init__(self, report, value, min_val, max_val, step, label, placeholder, icon, width, height, html_code, helper,
               options, profile):
    html_input = report.ui.inputs.d_range(report.inputs.get(html_code, value),
                                          min_val=min_val, max_val=max_val, step=step,
                                          width=(None, "%"), placeholder=placeholder, options=options)
    super(FieldRange, self).__init__(
      report, html_input, label, icon, width, height, html_code, helper, options, profile)
    if icon is not None and html_input.options.output:
      html_input.output.style.css.margin_left = 25
    if html_input.options.output:
      self.style.css.min_height = 45


class FieldCheckBox(Field):
  name = 'Field Checkbox'

  def __init__(self, report, value, label, icon, width, height, html_code, helper, options, profile):
    html_input = report.ui.inputs.checkbox(report.inputs.get(html_code, value), width=(None, "%"), options=options)
    super(FieldCheckBox, self).__init__(report, html_input, label, icon, width, height, html_code, helper, options,
                                        profile)
    if label is not None and options.get('position') == 'after':
      self.label.style.css.float = None
      self.label.style.css.width = 'auto'
      self.input.style.css.float = 'left'
      self.input.style.css.margin_top = 5
    self.style.css.line_height = Defaults.LINE_HEIGHT


class FieldInteger(Field):
  name = 'Field Integer'

  def __init__(self, report, value, label, placeholder, icon, width, height, html_code, helper, options, profile):
    html_input = report.ui.inputs.d_int(report.inputs.get(html_code, value), width=(None, "%"), placeholder=placeholder,
                                        options=options)
    super(FieldInteger, self).__init__(report, html_input, label, icon, width, height, html_code, helper,
                                       options, profile)


class FieldFile(Field):
  name = 'Field Integer'

  def __init__(self, report, value, label, placeholder, icon, width, height, html_code, helper, options, profile):
    html_input = report.ui.inputs.file(report.inputs.get(html_code, value), width=(None, "%"), placeholder=placeholder,
                                       options=options)
    super(FieldFile, self).__init__(report, html_input, label, icon, width, height, html_code, helper, options,
                                    profile)


class FieldPassword(Field):
  name = 'Field Password'

  def __init__(self, report, value, label, placeholder, icon, width, height, html_code, helper, options, profile):
    html_input = report.ui.inputs.password(report.inputs.get(html_code, value), width=(None, "%"),
                                           placeholder=placeholder, options=options)
    super(FieldPassword, self).__init__(report, html_input, label, icon, width, height, html_code, helper,
                                        options, profile)


class FieldTextArea(Field):
  name = 'Field Textarea'

  def __init__(self, report, value, label, placeholder, icon, width, height, html_code, helper, options, profile):
    html_input = report.ui.inputs.textarea(report.inputs.get(html_code, value), width=(100, "%"),
                                           placeholder=placeholder, options=options)
    super(FieldTextArea, self).__init__(report, html_input, label, icon, width, height, html_code, helper,
                                        options, profile)


class FieldSelect(Field):
  name = 'Field Select'

  def __init__(self, report, value, label, icon, width, height, html_code, helper, options, profile):
    html_input = report.ui.select(report.inputs.get(html_code, value),
                                  "%s_input" % html_code if html_code is not None else html_code,
                                  width=(100, "%"), options=options)
    html_input.options.iconBase = "iconBase"
    icon_details = Defaults_css.get_icon("check")
    html_input.options.tickIcon = icon_details["icon"]
    if icon_details['icon_family'] != 'bootstrap-icons':
      self.requirements = (icon_details['icon_family'],)
    super(FieldSelect, self).__init__(
      report, html_input, label, icon, width, height, html_code, helper, options, profile)
    if label is not None:
      self.label.style.css.line_height = None


class Checkbox(Html.Html):
  name = 'Checkbox'

  def __init__(self, report, flag, label, group_name, width, height, html_code, options, attrs, profile):
    super(Checkbox, self).__init__(report, {"value": flag}, html_code=html_code, profile=profile, options=options,
                                   css_attrs={"width": width, "height": height})
    self.set_attrs(attrs={"type": "checkbox"})
    if group_name is not None:
      self.attr["name"] = group_name
    self.set_attrs(attrs=attrs)
    self.css({"cursor": 'pointer', 'display': 'inline-block', 'vertical-align': 'middle', 'margin-left': '2px'})
    self.style.css.line_height = Defaults.LINE_HEIGHT
    self._label = label or ''
    self.style.add_classes.div.no_focus_outline()

  @property
  def dom(self) -> JsHtmlField.Check:
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :rtype: JsHtmlField.Check
    """
    if self._dom is None:
      self._dom = JsHtmlField.Check(self, report=self.page)
    return self._dom

  @property
  def js(self) -> JsComponents.Radio:
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    :rtype: JsComponents.Radio
    """
    if self._js is None:
      self._js = JsComponents.Radio(self, report=self.page)
    return self._js

  _js__builder__ = '''htmlObj.checked = data.value; 
      if((typeof data.text !== 'undefined') || (data.text !== null)){
        htmlObj.parentNode.insertBefore(document.createTextNode(data.text), htmlObj.nextSibling)};
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def __str__(self):
    return '<input %(strAttr)s>%(label)s' % {
      'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'label': self._label}


class Radio(Html.Html):
  name = 'Radio'

  def __init__(self, report, flag, label, group_name, icon, width, height, html_code, helper, options, profile):
    super(Radio, self).__init__(report, {"value": flag, 'text': label}, html_code=html_code,
                                css_attrs={"width": width, 'height': height}, profile=profile)
    self.add_input("", position="before", css={"width": 'none', "vertical-align": 'middle'})
    self.add_label(label, html_code=self.htmlCode, position="after",
                   css={"display": 'inline-block', "width": "None", 'float': 'none'})
    self.input.set_attrs(name="data-content", value=label)
    if flag:
      self.input.set_attrs({"checked": json.dumps(flag)})
    self.input.style.clear()
    if group_name is not None:
      self.input.set_attrs(name="name", value=group_name)
    else:
      self.input.set_attrs(name="name", value=self.htmlCode)
    self.input.set_attrs(attrs={"type": "radio"})
    self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
    self.input.css({"cursor": 'pointer', 'display': 'inline-block', 'vertical-align': 'middle', 'min-width': 'none'})
    self.css({'vertical-align': 'middle', 'text-align': "left"})
    self.add_icon(icon, html_code=self.htmlCode, position="after", family=options.get("icon_family"),
                  css={"margin-left": '5px', 'color': self.page.theme.success[1]})

  @property
  def dom(self) -> JsHtmlField.Radio:
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :rtype: JsHtmlField.Radio
    """
    if self._dom is None:
      self._dom = JsHtmlField.Radio(self, report=self.page)
    return self._dom

  @property
  def js(self) -> JsComponents.Radio:
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    :rtype: JsComponents.Radio
    """
    if self._js is None:
      self._js = JsComponents.Radio(self, report=self.page)
    return self._js

  _js__builder__ = '''htmlObj.checked = data.value; 
      if(data.text !== null){
        htmlObj.parentNode.insertBefore(document.createTextNode(data.text), htmlObj.nextSibling)};
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def __str__(self):
    return '<div %(strAttr)s>%(helper)s</div>' % {
      'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'helper': self.helper}


class TextArea(Html.Html):
  name = 'Text Area'

  def __init__(self, report, text, width, rows, placeholder, background_color, html_code, options, profile):
    super(TextArea, self).__init__(report, text, html_code=html_code, profile=profile,
                                   css_attrs={"width": width, 'box-sizing': 'border-box'})
    self.rows, self.backgroundColor = rows, background_color
    self.style.add_classes.input.textarea()
    self.set_attrs({"rows": rows, "placeholder": placeholder or ""})
    self.__options = OptInputs.OptionsTextarea(self, options)

  @property
  def options(self) -> OptInputs.OptionsTextarea:
    """
    Description:
    -----------
    Property to set all the input component properties.

    :rtype: OptInputs.OptionsTextarea
    """
    return self.__options

  def selectable(self, js_funcs: Union[list, str] = None, profile: Optional[Union[bool, dict]]= None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: Optional. Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.

    :return: self. to allow the function chaining
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.attr['onclick'] = "this.blur();this.select();%s" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  @property
  def dom(self) -> JsHtmlField.Textarea:
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Related Pages:

      https://www.w3schools.com/js/js_htmldom.asp

    :rtype: JsHtmlField.Textarea
    """
    if self._dom is None:
      self._dom = JsHtmlField.Textarea(self, report=self.page)
    return self._dom

  def change(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
             source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    ------------
    The input event fires when the value of an <input>, <select>, or <textarea> element has been changed.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] source_event: Optional. The source target for the event.
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if on_ready:
      self.page.body.onReady([self.dom.events.trigger("input")])
    return self.on("input", js_funcs, profile, source_event)

  _js__builder__ = 'htmlObj.innerHTML = data'

  def __str__(self):
    return '<textarea %(strAttr)s>%(val)s</textarea>' % {
      "strAttr": self.get_attrs(pyClassNames=self.style.get_classes()), 'val': self.val}


class Search(Html.Html):
  name = 'Search'

  def __init__(self, report, text, placeholder, color, width, height, html_code, tooltip, extensible, options, profile):
    if options.get('icon_family') is not None and options['icon_family'] != 'bootstrap-icons':
      self.requirements = (options['icon_family'],)
    super(Search, self).__init__(report, "", html_code=html_code, css_attrs={"height": height}, profile=profile)
    self.color = 'inherit' if color is None else color
    self.css({"display": "inline-block", "margin-bottom": '2px', 'box-sizing': 'border-box'})
    if not extensible:
      self.style.add_classes.layout.search()
      self.style.css.width = "%s%s" % (width[0], width[1])
    else:
      self.style.add_classes.layout.search_extension(max_width=width)
    self.add_input(text, options=options).input.set_attrs({"placeholder": placeholder, "spellcheck": False})
    if options["icon"]:
      self.add_icon(options["icon"], css={"color": report.theme.colors[4]}, html_code=self.htmlCode,
                    family=options.get("icon_family")).icon.attr['id'] = "%s_button" % self.htmlCode
      self.icon.style.css.z_index = 10
      self.dom.trigger = self.icon.dom.trigger
    else:
      self.icon = False
    self.style.css.position = "relative"

    if options.get("position", 'left') == 'left':
      self.input.css({"text-align": 'left', 'padding-left': '2px', 'padding-right': '2px'})
      if self.icon:
        self.input.css({'padding-left': '%spx' % Defaults.LINE_HEIGHT})
        self.icon.css({"margin": '5px 5px 5px 5px', 'display': 'block', 'cursor': 'pointer', 'position': 'absolute',
                       'vertical-align': 'top'})
    else:
      self.input.css({"text-align": 'left', 'padding-left': "2px", 'padding-right': '2px'})
      if self.icon:
        self.input.css({'padding-right': '%spx' % Defaults.LINE_HEIGHT})
        self.icon.css({"margin": '5px 5px 5px 5px', 'cursor': 'pointer', "right": 0,
                       'position': 'absolute', 'vertical-align': 'top'})
    if options.get("groups") is not None:
      self.select = self.page.ui.select([{"value": g, "name": g} for g in options.get("groups")], width=(200, 'px'),
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
    self.input.style.css.padding_left = 25
    self.input.attr["type"] = "search"

  @property
  def dom(self) -> JsHtmlField.JsHtmlFields:
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :rtype: JsHtmlField.JsHtmlFields
    """
    if self._dom is None:
      self._dom = JsHtmlField.JsHtmlFields(self, report=self.page)
    return self._dom

  _js__builder__ = '''htmlObj.find('input').val(data)'''

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] source_event: Optional. The JavaScript DOM source for the event (can be a sug item).
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    return self.icon.click(js_funcs, profile, source_event, on_ready=on_ready)

  def enter(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    -----------
    Add an javascript action when the key enter is pressed on the keyboard.

    Usage::

      component.enter(" alert() ")

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] source_event: Optional. The JavaScript DOM source for the event (can be a sug item).
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.

    :return: The python object itself
    """
    if self.icon:
      self.click(js_funcs)
      return self.on("keydown", ["if (event.keyCode  == 13) {event.preventDefault(); %(jsFnc)s} " % {
        "jsFnc": self.icon.dom.events.trigger("click")}], profile=profile, source_event=source_event, on_ready=on_ready)

    return self.on("keydown", ["if (event.keyCode  == 13) {event.preventDefault(); %(jsFnc)s} " % {
        "jsFnc": JsUtils.jsConvertFncs(
          js_funcs, toStr=True, profile=profile)}], profile=profile, source_event=source_event, on_ready=on_ready)

  def __str__(self):
    return '<div %(attr)s></div>' % {"attr": self.get_attrs(pyClassNames=self.style.get_classes())}
