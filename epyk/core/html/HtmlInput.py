#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import json

from epyk.core.html import Html
from epyk.core.html import Defaults
from epyk.core.html.options import OptInputs

#
from epyk.core.js import JsUtils
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

  def __str__(self):
    return '<output %(strAttr)s>%(val)s</output>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'val': self.val}


class Input(Html.Html):
  name = 'Input'

  def __init__(self, report, text, placeholder, width, height, htmlCode, options, attrs, profile):
    super(Input, self).__init__(report, text, htmlCode=htmlCode, css_attrs={"width": width, "height": height, 'box-sizing': 'border-box'},
                                profile=profile, options=options)
    value = text['value'] if isinstance(text, dict) else text
    self.set_attrs(attrs={"placeholder": placeholder, "type": "text", "value": value, "spellcheck": False})
    self.set_attrs(attrs=attrs)
    self.__options, self.__focus = OptInputs.OptionsInput(self, options), False
    if width[0] is None:
      self.style.css.min_width = Defaults.INPUTS_MIN_WIDTH

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the input component properties

    :rtype: OptInputs.OptionsInput
    """
    return self.__options

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component

    :rtype: GrpClsInput.ClassInput
    """
    if self._styleObj is None:
      self._styleObj = GrpClsInput.ClassInput(self)
    return self._styleObj

  @property
  def _js__builder__(self):
    return '''
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}
      if(typeof options.formatMoney !== 'undefined'){ htmlObj.value = accounting.formatMoney(data, 
        options.formatMoney.symbol, options.formatMoney.digit, 
        options.formatMoney.thousand, options.formatMoney.decimal)}
      else if(typeof options.formatNumber !== 'undefined'){ htmlObj.value = accounting.formatNumber(data,
        options.formatNumber.digit, options.formatNumber.thousand)}
      else if(typeof options.toFixed !== 'undefined'){ htmlObj.value = accounting.toFixed(data, options.toFixed) }
      else { htmlObj.value = data; }
      '''

  def focus(self, jsFncs=None, profile=False, options=None, source_event=None, onReady=False):
    """
    Description:
    -----------
    Action on focus

    Attributes:
    ----------
    :param jsFncs: List or String with the Javascript events
    :param profile: Boolean to add the Javascript fragment to profile
    :param options: Python dictionary with special options (shortcuts) for the component
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded
    """
    self.__focus = True
    if jsFncs is None:
      jsFncs = []
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if options is not None:
      if options.get("reset", False):
        jsFncs.append(self.dom.empty())
      if options.get("select", False):
        jsFncs.append(self.dom.select())
    if self.options.reset:
      jsFncs.append(self.dom.empty())
    if self.options.select:
      jsFncs.append(self.dom.select())
    return self.on("focus", jsFncs, profile, source_event, onReady)

  def validation(self, pattern, required=True):
    """
    Description:
    -----------
    Add validation rules on the input component

    Usage::

      input.validation(pattern="[0-9]{5}")

    Attributes:
    ----------
    :param pattern: String.
    :return: Self to allow the chaining
    """
    self.attr["pattern"] = pattern
    if required:
      self.attr["required"] = None
    self.style.add_classes.input.is_valid()
    return self

  def enter(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------
    Add an javascript action when the key enter is pressed on the keyboard

    Usage::

      htmlObj.input(placeholder="Put your tag").enter("alert()")

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    :param source_event:
    :param onReady:

    :return: The python object itself
    """

    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    jsFncs.append(self.dom.select())
    self.keydown.enter(jsFncs, profile, source_event=source_event)
    return self

  def readonly(self, flag=True):
    """

    :param flag:
    :return:
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
    if 'css' in self._jsStyles:
      self.css(self._jsStyles['css'])
    return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class InputRadio(Input):
  name = 'Input'

  def __init__(self, report, flag, group_name, placeholder, width, height, htmlCode, options, attrs, profile):
    super(InputRadio, self).__init__(report, "", placeholder, width, height, htmlCode, options, attrs, profile)
    self.set_attrs({"type": 'radio'})
    if flag:
      self.set_attrs({"checked": json.dumps(flag)})
    if group_name is not None:
      self.set_attrs({"name": group_name})


class AutoComplete(Input):
  name = 'Input Time'
  requirements = ('jqueryui', )

  def __init__(self, report, text, placeholder, width, height, htmlCode, options, attrs, profile):
    if text is None:
      text = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
    super(AutoComplete, self).__init__(report, text, placeholder, width, height, htmlCode, options, attrs, profile)
    self.__options = OptInputs.OptionAutoComplete(self, options)

  @property
  def _js__builder__(self):
    return "if(typeof data === 'object'){jQuery(htmlObj).autocomplete(Object.assign(data, options))} else{jQuery(htmlObj).autocomplete(options)}"

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the input timepicker component properties

    Related Pages:

      https://timepicker.co/options/

    :rtype: OptInputs.OptionAutoComplete
    """
    return self.__options

  @property
  def js(self):
    """
    Description:
    -----------

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsQueryUi.Autocomplete
    """
    if self._js is None:
      self._js = JsQueryUi.Autocomplete(self, report=self._report)
    return self._js

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class InputTime(Input):
  name = 'Input Time'
  requirements = ('timepicker', )

  def __init__(self, report, text, placeholder, width, height, htmlCode, options, attrs, profile):
    if text is None:
      text = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
    super(InputTime, self).__init__(report, text, placeholder, width, height, htmlCode, options, attrs, profile)
    self.__options = OptInputs.OptionsTimePicker(self, options)
    self.style.css.background_color = report.theme.colors[0]
    self.style.css.line_height = Defaults.LINE_HEIGHT
    self.style.css.text_align = "center"

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the input timepicker component properties

    Related Pages:

      https://timepicker.co/options/

    :rtype: OptInputs.OptionsTimePicker
    """
    return self.__options

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component

    :rtype: GrpClsInput.ClassInputTime
    """
    if self._styleObj is None:
      self._styleObj = GrpClsInput.ClassInputTime(self)
    return self._styleObj

  @property
  def dom(self):
    """
    Description:
    ------------
    The Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlTimePicker
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlTimePicker(self, report=self._report)
    return self._dom

  @property
  def js(self):
    """
    Description:
    -----------

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsTimepicker.Timepicker
    """
    if self._js is None:
      self._js = JsTimepicker.Timepicker(self, report=self._report)
    return self._js

  @property
  def _js__builder__(self):
    """
    else {
        if (data.value == ''){data.time = new Date()} else{data.time = data.value};
        if (data.options._change.length > 0) {data.options.change = function(time){
            let data = {event_val: time.getHours() +':'+ time.getMinutes() +':'+ time.getSeconds(), event_code: htmlCode};
            eval(data.options._change.join(";"))}};
        jQuery(htmlObj).timepicker(data.options); jQuery(htmlObj).timepicker('setTime', data.time)}

    :return:
    """
    return '''
      if (typeof data == "string"){%(jqId)s.timepicker('setTime', data)} 
      %(jqId)s.timepicker(options); ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  def change(self, jsFnc):
    """
    Description:
    -----------
    Event triggerd when the value of the input field changes. A Date object containing the selected time is passed as the first argument of the callback.
    Note: the variable time is a function parameter received in the Javascript side

    Related Pages:

      https://timepicker.co/options/

    :param jsFnc:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self._jsStyles["change"] = "function(time){ %s }" % JsUtils.jsConvertFncs(jsFnc, toStr=True)
    return self

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class InputDate(Input):
  requirements = ('jqueryui', )
  name = 'Input Time'

  def __init__(self, report, records, placeholder, width, height, htmlCode, options, attrs, profile):
    super(InputDate, self).__init__(report, records, placeholder, width, height, htmlCode, options, attrs, profile)
    self.__options = OptInputs.OptionsDatePicker(self, options)

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the input Datepicker component properties

    Related Pages:

      https://timepicker.co/options/

    :rtype: OptInputs.OptionsDatePicker
    """
    return self.__options

  @property
  def js(self):
    """
    Description:
    -----------

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsQueryUi.Datepicker
    """
    if self._js is None:
      self._js = JsQueryUi.Datepicker(self, report=self._report)
    return self._js

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component

    :rtype: GrpClsInput.ClassInputDate
    """
    if self._styleObj is None:
      self._styleObj = GrpClsInput.ClassInputDate(self)
    return self._styleObj

  @property
  def dom(self):
    """
    Description:
    ------------
    The Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlDatePicker
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlDatePicker(self, report=self._report)
    return self._dom

  def excluded_dates(self, dts=None, jsFncs=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param dts:
    :param jsFncs:
    """
    self._jsStyles['beforeShowDay'] = '''function (date) {
            var utc = date.getTime() - date.getTimezoneOffset()*60000; var newDate = new Date(utc); const dts = %(dts)s;
            %(jsFnc)s; if(dts.includes(newDate.toISOString().split('T')[0])){return [false, '', '']} else {return [true, '', '']}
          }''' % {"dts": json.dumps(dts or []), 'jsFnc': JsUtils.jsConvertFncs(jsFncs, toStr=True)}

  def included_dates(self, dts=None, jsFncs=None):
    """

    Attributes:
    ----------
    :param dts:
    :param jsFncs:
    """
    self._jsStyles['beforeShowDay'] = '''function (date) {
        var utc = date.getTime() - date.getTimezoneOffset()*60000; var newDate = new Date(utc); const dts = %(dts)s;
        %(jsFnc)s; if(!dts.includes(newDate.toISOString().split('T')[0])){return [false, '', '']} else {return [true, '', '']}
      }''' % {"dts": json.dumps(dts or []), 'jsFnc': JsUtils.jsConvertFncs(jsFncs, toStr=True)}

  @property
  def _js__builder__(self):
    '''
    if ((typeof data.options.selectedDts !== "undefined") && (data.options.selectedDts.length > 0)){
        var selectedDt = {};
        data.options.selectedDts.forEach(function(dt){var jsDt = new Date(dt); selectedDt[jsDt.toISOString().split('T')[0]] = jsDt}) ;
        if (data.options.excludeDts === true){
          function renderCalendarCallbackExc(intDate) {var utc = intDate.getTime() - intDate.getTimezoneOffset()*60000; var newDate = new Date(utc); var Highlight = selectedDt[newDate.toISOString().split('T')[0]]; if(Highlight){return [false, '', '']} else {return [true, '', '']}};
          data.options.beforeShowDay = renderCalendarCallbackExc;
        } else{
          function renderCalendarCallback(intDate) {var utc = intDate.getTime() - intDate.getTimezoneOffset()*60000; var newDate = new Date(utc); var Highlight = selectedDt[newDate.toISOString().split('T')[0]]; if(Highlight){return [true, "%s", '']} else {return [false, '', '']}};
          data.options.beforeShowDay = renderCalendarCallback;};
        delete data.options.selectedDts};
      jQuery(htmlObj).datepicker(data.options).datepicker('setDate', data.value)
    :return:
    '''
    return '''%(jqId)s.datepicker(options).datepicker('setDate', data)''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  def __str__(self):
    # Javascript builder is mandatory for this object
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    if self.options.inline:
      return '<div %(strAttr)s></div>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}

    return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class InputInteger(Input):
  name = 'Input Number'

  def __init__(self, report, text, placeholder, width, height, htmlCode, options, attrs, profile):
    super(InputInteger, self).__init__(report, text, placeholder, width, height, htmlCode, options, attrs, profile)
    self.__options = OptInputs.OptionsInputInteger(self, options)

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the input component properties

    :rtype: OptInputs.OptionsInputInteger
    """
    return self.__options

  def quantity(self):
    factors, strFcts = {'K': 1000, 'M': 1000000, 'B': 1000000000}, []
    for f, val in factors.items():
      strFcts.append("if(event.key.toUpperCase() == '%s'){this.value *= %s}" % (f, val))
    self.on('keydown', ";".join(strFcts))
    return self


class InputRange(Input):
  name = 'Input Range'

  def __init__(self, report, text, min, max, step, placeholder, width, height, htmlCode, options, attrs, profile):
    super(InputRange, self).__init__(report, text, placeholder, width, height, htmlCode, options, attrs, profile)
    self.__options = OptInputs.OptionsInputRange(self, options)
    #
    self.input = report.ui.inputs.input(text, width=(None, "px"), placeholder=placeholder).css({"vertical-align": 'middle'})
    self.append_child(self.input)
    #
    self.input.set_attrs(attrs={"type": "range", "min": min, "max": max, "step": step})
    if self.options.output:
      self.output = self._report.ui.inputs._output(text).css({
        "width": '15px', "text-align": 'center', "margin-left": '2px', 'color': self._report.theme.success[1]})
      self.append_child(self.output)
      self.input.set_attrs(attrs={"oninput": "%s.value=this.value" % self.output.htmlCode})
    self.css({"display": 'inline-block', "vertical-align": 'middle', "line-height": '%spx' % Defaults.LINE_HEIGHT})

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set input range properties

    :rtype: OptSelect.OptionsInputRange
    """
    return self.__options

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component

    :rtype: GrpClsInput.ClassInputRange
    """
    if self._styleObj is None:
      self._styleObj = GrpClsInput.ClassInputRange(self)
    return self._styleObj#

  def __str__(self):
    if hasattr(self, 'output'):
      self.output.css({"display": 'inline-block'})
    return '<div %(strAttr)s></div>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class Field(Html.Html):
  name = 'Field'

  def __init__(self, report, input, label, placeholder, icon, width, height, htmlCode, helper, options, profile):
    super(Field, self).__init__(report, "", htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._vals = ""
    # Add the component predefined elements
    self.add_label(label, htmlCode=self.htmlCode, css={'height': 'auto', 'margin-top': '1px', 'margin-bottom': '1px'}, position=options.get("position", 'before'),  options=options)
    self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
    # add the input item
    self.input = input
    self.append_child(self.input)
    self.add_icon(icon, htmlCode=self.htmlCode, position="after", css={"margin-left": '5px', 'color': self._report.theme.success[1]},
                  family=options.get("icon_family"))
    self.css({"margin-top": '2px'})

  @property
  def dom(self):
    """
    Description:
    -----------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlField.JsHtmlFields
    """
    if self._dom is None:
      self._dom = JsHtmlField.JsHtmlFields(self, report=self._report)
    return self._dom

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else v for v in self.val])
    return "<div %s>%s%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_div, self.helper)


class FieldInput(Field):
  name = 'Field Input'

  def __init__(self, report, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile):
    input = report.ui.inputs.input(report.inputs.get(htmlCode, value), width=(None, "%"), placeholder=placeholder, options=options)
    super(FieldInput, self).__init__(report, input, label, placeholder, icon, width, height, htmlCode, helper, options, profile)


class FieldAutocomplete(Field):
  name = 'Field Autocomplete'

  def __init__(self, report, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile):
    input = report.ui.inputs.autocomplete(report.inputs.get(htmlCode, value), width=(None, "%"), placeholder=placeholder, options=options)
    super(FieldAutocomplete, self).__init__(report, input, label, placeholder, icon, width, height, htmlCode, helper, options, profile)

  def change(self, jsFnc, profile=None):
    """
    Description:
    -----------
    Event triggerd when the value of the input field changes.
    A Date object containing the selected time is passed as the first argument of the callback.
    Note: the variable time is a function parameter received in the Javascript side

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-change

    :param jsFnc:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self._jsStyles["change"] = "function( event, ui ){ %s }" % JsUtils.jsConvertFncs(jsFnc, toStr=True)
    return self

  def search(self, jsFnc, profile=None):
    """
    Description:
    -----------
    Triggered before a search is performed, after minLength and delay are met.
    If canceled, then no request will be started and no items suggested.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-search

    :param jsFnc:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self._jsStyles["search"] = "function( event, ui ){ %s }" % JsUtils.jsConvertFncs(jsFnc, toStr=True)
    return self

  def focus(self, jsFnc, profile=None):
    """
    Description:
    -----------
    Triggered when focus is moved to an item (not selecting).
    The default action is to replace the text field's value with the value of the focused item, though only if the event was triggered by a keyboard interaction.
    Canceling this event prevents the value from being updated, but does not prevent the menu item from being focused.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-focus

    Attributes:
    ----------
    :param jsFnc:
    :param profile:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self._jsStyles["focus"] = "function( event, ui ){ %s }" % JsUtils.jsConvertFncs(jsFnc, toStr=True)
    return self

  def close(self, jsFnc, profile=None):
    """
    Description:
    -----------
    Triggered when the menu is hidden. Not every close event will be accompanied by a change event.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-close

    Attributes:
    ----------
    :param jsFnc:
    :param profile:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self._jsStyles["close"] = "function( event, ui ){ %s }" % JsUtils.jsConvertFncs(jsFnc, toStr=True)
    return self

  def select(self, jsFnc, profile=None):
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
    :param jsFnc:
    :param profile:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self._jsStyles["select"] = "function( event, ui ){ %s }" % JsUtils.jsConvertFncs(jsFnc, toStr=True)
    return self

  def response(self, jsFnc, profile=None):
    """
    Description:
    -----------
    Triggered after a search completes, before the menu is shown.
    Useful for local manipulation of suggestion data, where a custom source option callback is not required.
    This event is always triggered when a search completes, even if the menu will not be shown because there are no results or the Autocomplete is disabled.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-response

    Attributes:
    ----------
    :param jsFnc:
    :param profile:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self._jsStyles["response"] = "function( event, ui ){ %s }" % JsUtils.jsConvertFncs(jsFnc, toStr=True)


class FieldRange(Field):
  name = 'Field Range'

  def __init__(self, report, value, min, max, step, label, placeholder, icon, width, height, htmlCode, helper, options, profile):
    input = report.ui.inputs.d_range(report.inputs.get(htmlCode, value), min=min, max=max, step=step, width=(None, "%"), placeholder=placeholder, options=options)
    super(FieldRange, self).__init__(report, input, label, placeholder, icon, width, height, htmlCode, helper, options, profile)


class FieldCheckBox(Field):
  name = 'Field Checkbox'

  def __init__(self, report, value, label, icon, width, height, htmlCode, helper, options, profile):
    input = report.ui.inputs.checkbox(report.inputs.get(htmlCode, value), width=(None, "%"), options=options)
    super(FieldCheckBox, self).__init__(report, input, label, "", icon, width, height, htmlCode, helper, options, profile)
    if label is not None and options.get('position') == 'after':
      self.label.style.css.float = None
      self.label.style.css.width = 'auto'
      self.input.style.css.float = 'left'
      self.input.style.css.margin_top = 5
    self.style.css.line_height = Defaults.LINE_HEIGHT


class FieldInteger(Field):
  name = 'Field Integer'

  def __init__(self, report, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile):
    input = report.ui.inputs.d_int(report.inputs.get(htmlCode, value), width=(None, "%"), placeholder=placeholder, options=options)
    super(FieldInteger, self).__init__(report, input, label, placeholder, icon, width, height, htmlCode, helper, options, profile)


class FieldFile(Field):
  name = 'Field Integer'

  def __init__(self, report, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile):
    input = report.ui.inputs.file(report.inputs.get(htmlCode, value), width=(None, "%"), placeholder=placeholder, options=options)
    super(FieldFile, self).__init__(report, input, label, placeholder, icon, width, height, htmlCode, helper, options, profile)


class FieldPassword(Field):
  name = 'Field Password'

  def __init__(self, report, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile):
    input = report.ui.inputs.password(report.inputs.get(htmlCode, value), width=(None, "%"), placeholder=placeholder, options=options)
    super(FieldPassword, self).__init__(report, input, label, placeholder, icon, width, height, htmlCode, helper, options, profile)


class FieldTextArea(Field):
  name = 'Field Textarea'

  def __init__(self, report, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile):
    input = report.ui.inputs.textarea(report.inputs.get(htmlCode, value), width=(100, "%"), placeholder=placeholder, options=options)
    super(FieldTextArea, self).__init__(report, input, label, placeholder, icon, width, height, htmlCode, helper, options, profile)


class FieldSelect(Field):
  name = 'Field Select'

  def __init__(self, report, value, label, icon, width, height, htmlCode, helper, options, profile):
    input = report.ui.select(report.inputs.get(htmlCode, value), "%s_input" % htmlCode if htmlCode is not None else htmlCode,
                             width=(100, "%"), options=options)
    super(FieldSelect, self).__init__(report, input, label, "", icon, width, height, htmlCode, helper, options, profile)


class Checkbox(Html.Html):
  name = 'Checkbox'

  def __init__(self, report, flag, label, group_name, width, height, htmlCode, options, attrs, profile):
    super(Checkbox, self).__init__(report, {"value": flag}, htmlCode=htmlCode, css_attrs={"width": width, "height": height},
                                   profile=profile, options=options)
    self.set_attrs(attrs={"type": "checkbox"})
    self.set_attrs(attrs=attrs)
    self.css({"cursor": 'pointer', 'display': 'inline-block', 'vertical-align': 'middle', 'margin-left': '2px'})
    self.style.css.line_height = Defaults.LINE_HEIGHT
    self._label = label or ''

  @property
  def dom(self):
    """
    Description:
    -----------

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsHtmlField.Check
    """
    if self._dom is None:
      self._dom = JsHtmlField.Check(self, report=self._report)
    return self._dom

  @property
  def _js__builder__(self):
    return '''htmlObj.checked = data.value; 
      if(data.text !== null){
        htmlObj.parentNode.insertBefore(document.createTextNode(data.text), htmlObj.nextSibling)};
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def __str__(self):
    return '<input %(strAttr)s>%(label)s' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'label': self._label}


class Radio(Html.Html):
  name = 'Radio'

  def __init__(self, report, flag, label, group_name, icon, width, height, htmlCode, helper, options, profile):
    super(Radio, self).__init__(report, {"value": flag, 'text': label}, htmlCode=htmlCode,
                                         css_attrs={"width": width, 'height': height}, profile=profile)
    self.add_input("", position="before", css={"width": 'none', "vertical-align": 'middle'})
    self.add_label(label, htmlCode=self.htmlCode, position="after", css={"display": 'inline-block', "width": "None", 'float': 'none'})
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
    self.add_icon(icon, htmlCode=self.htmlCode, position="after", css={"margin-left": '5px', 'color': self._report.theme.success[1]},
                  family=options.get("icon_family"))

  @property
  def dom(self):
    """
    Description:
    -----------

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsHtmlField.Radio
    """
    if self._dom is None:
      self._dom = JsHtmlField.Radio(self, report=self._report)
    return self._dom

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript Functions

    :rtype: JsComponents.Radio
    """
    if self._js is None:
      self._js = JsComponents.Radio(self, report=self._report)
    return self._js

  @property
  def _js__builder__(self):
    return '''htmlObj.checked = data.value; 
      if(data.text !== null){
        htmlObj.parentNode.insertBefore(document.createTextNode(data.text), htmlObj.nextSibling)};
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def __str__(self):
    return '<div %(strAttr)s>%(helper)s</div>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'helper': self.helper}


class TextArea(Html.Html):
  name = 'Text Area'

  def __init__(self, report, text, width, rows, placeholder, background_color, htmlCode, options, profile):
    super(TextArea, self).__init__(report, text, htmlCode=htmlCode, css_attrs={"width": width, 'box-sizing': 'border-box'}, profile=profile)
    self.rows, self.backgroundColor = rows, background_color
    self.style.add_classes.input.textarea()
    self.set_attrs({"rows": rows, "placeholder": placeholder or ""})
    self.__options = OptInputs.OptionsTextarea(self, options)

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the input component properties

    :rtype: OptInputs.OptionsTextarea
    """
    return self.__options

  def selectable(self, jsFncs=None, profile=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:

    :return: self. to allow the function chaining
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.attr['onclick'] = "this.blur();this.select();%s" % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  @property
  def dom(self):
    """
    Description:
    -----------
    Return the HTML DOM object

    Related Pages:

      https://www.w3schools.com/js/js_htmldom.asp

    :rtype: JsHtmlField.Textarea
    """
    if self._dom is None:
      self._dom = JsHtmlField.Textarea(self, report=self._report)
    return self._dom

  @property
  def _js__builder__(self):
    return 'htmlObj.innerHTML = data'

  def __str__(self):
    return '<textarea %(strAttr)s>%(val)s</textarea>' % {"strAttr": self.get_attrs(pyClassNames=self.style.get_classes()), 'val': self.val}


class Search(Html.Html):
  name = 'Search'

  def __init__(self, report, text, placeholder, color, height, htmlCode, tooltip, extensible, options, profile):
    super(Search, self).__init__(report, "", htmlCode=htmlCode, css_attrs={"height": height}, profile=profile)
    self.color = self._report.theme.colors[-1] if color is None else color
    self.css({"display": "inline-block", "margin-bottom": '2px', 'box-sizing': 'border-box'})
    #
    if not extensible:
      self.style.add_classes.layout.search()
      self.style.css.width = "100%"
    else:
      self.style.add_classes.layout.search_extension()
    self.add_input(text).input.set_attrs({"placeholder": placeholder, "spellcheck": False})
    self.input.css({"text-align": 'left', 'padding-left': '%spx' % Defaults.LINE_HEIGHT})
    self.add_icon("fas fa-search", htmlCode=self.htmlCode, family=options.get("icon_family")).icon.attr['id'] = "%s_button" % self.htmlCode
    self.icon.css({"margin": '6px 0 6px 5px', 'display': 'block', 'cursor': 'pointer', 'position': 'absolute', 'vertical-align': 'top'})
    self.tooltip(tooltip)

  @property
  def dom(self):
    """

    :rtype: JsHtmlField.JsHtmlFields
    """
    if self._dom is None:
      self._dom = JsHtmlField.JsHtmlFields(self, report=self._report)
    return self._dom

  @property
  def _js__builder__(self):
    return '''htmlObj.find('input').val(data)'''

  def click(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs: String or List. The Javascript functions
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded
    """
    return self.icon.click(jsFncs, profile, source_event, onReady=onReady)

  def enter(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    -----------
    Add an javascript action when the key enter is pressed on the keyboard

    Example
    htmlObj.enter(" alert() ")

    Attributes:
    ----------
    :param jsFncs: String or List. The Javascript functions
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded

    :return: The python object itself
    """
    self.click(jsFncs)
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return self.on("keydown", ["if (event.keyCode  == 13) {event.preventDefault(); %(jsFnc)s } " % {"jsFnc": JsUtils.jsConvertFncs(jsFncs, toStr=True)}],
                   profile=profile, source_event=source_event, onReady=onReady)

  def __str__(self):
    return '<div %(attr)s></div>' % {"attr": self.get_attrs(pyClassNames=self.style.get_classes())}
