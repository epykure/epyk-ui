"""
Wrapper to the different HTML input components
"""

import datetime
import json

from epyk.core.html import Html
from epyk.core.html import Defaults

#
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlField
from epyk.core.js.html import JsHtmlJqueryUI
from epyk.core.js.html import JsHtml

# The list of CSS classes
from epyk.core.css.categories import CssGrpClsInput
from epyk.core.css.categories import GrpCls


class Output(Html.Html):
  name, category, callFnc = 'Output', 'Inputs', '_output'

  def __str__(self):
    return '<output %(strAttr)s>%(val)s</output>' % {'strAttr': self.get_attrs(pyClassNames=self.pyStyle), 'val': self.val}


class Input(Html.Html):
  name, category, callFnc = 'Input', 'Inputs', 'input'
  _grpCls = CssGrpClsInput.CssClassInput

  def __init__(self, report, text, placeholder, size, width, height, htmlCode, filter, options, attrs, profile):
    super(Input, self).__init__(report, text, htmlCode=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                heightUnit=height[1], globalFilter=filter, profile=profile, options=options)
    value = text['value'] if isinstance(text, dict) else text
    self.set_attrs(attrs={"placeholder": placeholder, "type": "text", "value": value, "spellcheck": False})
    self.set_attrs(attrs=attrs)
    self.css({"font-size": "%s%s" % (size[0], size[1])})

  @property
  def _js__builder__(self):
    return '''htmlObj.value = data;
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def focus(self, jsFncs=None, profile=False, options=None):
    """
    Action on focus

    :param jsFncs: List or String with the Javascript events
    :param profile: Boolean to add the Javascript fragment to profile
    :param options: Python dictionary with special options (shortcuts) for the component
    """
    if options is not None:
      if jsFncs is None:
        jsFncs = []
      elif not isinstance(jsFncs, list):
        jsFncs = [jsFncs]
      if options.get("reset", False):
        jsFncs.append(self.dom.empty())
    return self.on("focus", jsFncs, profile)

  def autocomplete(self, source):
    """

    :param source:

    :return: Self to allow the chaining
    """
    self._report.js.addOnLoad(['%s.autocomplete({"source": %s})' % (self.dom.jquery.varId, source)])
    return self

  def validation(self, pattern, required=True):
    """
    Add validation rules on the input component

    Example
    input.validation(pattern="[0-9]{5}")

    :param pattern: String.
    :return: Self to allow the chaining
    """
    self.attr["pattern"] = pattern
    if required:
      self.attr["required"] = None
    self.style.addCls(["CssInputInValid", "CssInputValid"])
    return self

  def enter(self, jsFncs, profile=False):
    """
    Add an javascript action when the key enter is pressed on the keyboard

    Example
    htmlObj.input(placeholder="Put your tag").enter("alert()")

    :param jsFncs:
    :param profile:

    :return: The python object itself
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.on("keydown", "if(event.keyCode == 13){event.preventDefault(); %s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True), profile)
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
    return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(pyClassNames=self.pyStyle)}


class InputTime(Input):
  name, callFnc = 'Input Time', 'input'
  __reqCss, __reqJs = ['timepicker'], ['timepicker']
  _grpCls = CssGrpClsInput.CssClassTimePicker

  def __init__(self, report, text, placeholder, size, width, height, htmlCode, filter, options, attrs, profile):
    if text is None:
      text = {"value": str(datetime.datetime.now()).split(" ")[1].split(".")[0]}
    elif isinstance(text, str):
      text = {"value": text}
    if 'options' not in text:
      text['options'] = {'timeFormat': 'HH:mm:ss'}
      text['options']["_change"] = []
    super(InputTime, self).__init__(report, text, placeholder, size, width, height, htmlCode, filter, options, attrs, profile)

  @property
  def dom(self):
    """
    The Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlTimePicker
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlTimePicker(self, report=self._report)
    return self._dom

  @property
  def _js__builder__(self):
    return '''
      if (typeof data == "string"){jQuery(htmlObj).timepicker('setTime', data)
      } else {
        if (data.value == ''){data.time = new Date()} else{data.time = data.value};
        if (data.options._change.length > 0) {data.options.change = function(time){
            let data = {event_val: time.getHours() +':'+ time.getMinutes() +':'+ time.getSeconds(), event_code: htmlId}; 
            eval(data.options._change.join(";"))}};
        jQuery(htmlObj).timepicker(data.options); jQuery(htmlObj).timepicker('setTime', data.time)}'''

  def __str__(self):
    # Javascript builder is mandatory for this object
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(pyClassNames=self.pyStyle)}


class InputDate(Input):
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui']
  name, callFnc = 'Input Time', 'input'
  cssCls = ["datepicker"]
  _grpCls = CssGrpClsInput.CssClassDatePicker

  def __init__(self, report, records, placeholder, size, width, height, htmlCode, filter, options, attrs, profile):
    super(InputDate, self).__init__(report, records, placeholder, size, width, height, htmlCode, filter, options, attrs, profile)

  @property
  def dom(self):
    """
    The Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlDatePicker
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlDatePicker(self, report=self._report)
    return self._dom

  @property
  def _js__builder__(self):
    return '''
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
      jQuery(htmlObj).datepicker(data.options).datepicker('setDate', data.value)'''

  def __str__(self):
    # Javascript builder is mandatory for this object
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<input %(strAttr)s />' % {'strAttr': self.get_attrs(pyClassNames=self.pyStyle)}


class InputInteger(Input):
  _grpCls = CssGrpClsInput.CssClassInputInteger
  name, callFnc = 'Input Number', 'input'

  def quantity(self):
    factors, strFcts = {'K': 1000, 'M': 1000000, 'B': 1000000000}, []
    for f, val in factors.items():
      strFcts.append("if(event.key.toUpperCase() == '%s'){$(this).find('input').val($(this).find('input').val() * %s)}" % (f, val))
    self.on('keydown', ";".join(strFcts))
    return self


class InputRange(Input):
  name, callFnc = 'Input Range', 'input'
  _grpCls = GrpCls.CssGrpClass

  def __init__(self, report, text, min, max, step, placeholder, size, width, height, htmlCode, filter, options, attrs, profile):
    super(InputRange, self).__init__(report, text, placeholder, size, width, height, htmlCode, filter, options,
                                     attrs, profile)

    #
    self.input = report.ui.inputs.input(text, width=(None, "%"), placeholder=placeholder).css({"vertical-align": 'middle'})
    self.input.inReport = False
    self.input.pyStyle = CssGrpClsInput.CssClassInputRange(self)
    self.append_child(self.input)
    #
    self.output = self._report.ui.inputs._output(text).css({"margin-left": '5px', 'color': self._report.theme.success[1]})
    self.output.inReport = False
    self.append_child(self.output)
    self.input.set_attrs(attrs={"type": "range", "min": min, "max": max, "step": step,
                                "oninput": "%s.value=this.value" % self.output.htmlId})
    self.css({"display": 'inline-block', "vertical-align": 'middle', "line-height": '%spx' % Defaults.LINE_HEIGHT})

  def __str__(self):
    self.output.css({"display": 'inline-block'})
    return '<div %(strAttr)s></div>' % {'strAttr': self.get_attrs(pyClassNames=self.pyStyle)}


class Field(Html.Html):
  def __init__(self, report, input, label, placeholder, size, icon, width, height, htmlCode, helper, profile):
    super(Field, self).__init__(report, "", code=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                     heightUnit=height[1], profile=profile)
    # Add the component predefined elements
    self.add_label(label)
    self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
    # add the input item
    self.input = input
    self.append_child(self.input)
    self.add_icon(icon, position="after", css={"margin-left": '5px', 'color': self._report.theme.success[1]})
    self.css({"margin-top": '2px'})

  @property
  def dom(self):
    """
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtml
    """
    if self._dom is None:
      self._dom = JsHtmlField.JsHtmlFields(self, report=self._report)
    return self._dom

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else v for v in self.val])
    return "<div %s>%s%s</div>" % (self.get_attrs(pyClassNames=self.pyStyle), str_div, self.helper)


class FieldInput(Field):

  def __init__(self, report, value, label, placeholder, size, icon, width, height, htmlCode, helper, profile):
    input = report.ui.inputs.input(value, width=(None, "%"), placeholder=placeholder)
    super(FieldInput, self).__init__(report, input, label, placeholder, size, icon, width, height, htmlCode, helper, profile)


class FieldRange(Field):

  def __init__(self, report, value, min, max, step, label, placeholder, size, icon, width, height, htmlCode, helper, profile):
    input = report.ui.inputs.d_range(value, min=min, max=max, step=step, width=(None, "%"), placeholder=placeholder)
    super(FieldRange, self).__init__(report, input, label, placeholder, size, icon, width, height, htmlCode, helper, profile)


class FieldCheckBox(Field):
  def __init__(self, report, value, label, size, icon, width, height, htmlCode, helper, profile):
    input = report.ui.inputs.checkbox(value, width=(None, "%"))
    super(FieldCheckBox, self).__init__(report, input, label, "", size, icon, width, height, htmlCode, helper, profile)


class FieldInteger(Field):

  def __init__(self, report, value, label, placeholder, size, icon, width, height, htmlCode, helper, profile):
    input = report.ui.inputs.d_int(value, width=(None, "%"), placeholder=placeholder)
    super(FieldInteger, self).__init__(report, input, label, placeholder, size, icon, width, height, htmlCode, helper, profile)


class FieldPassword(Field):
  def __init__(self, report, value, label, placeholder, size, icon, width, height, htmlCode, helper, profile):
    input = report.ui.inputs.password(value, width=(None, "%"), placeholder=placeholder)
    super(FieldPassword, self).__init__(report, input, label, placeholder, size, icon, width, height, htmlCode, helper, profile)


class FieldTextArea(Field):
  def __init__(self, report, value, label, placeholder, size, icon, width, height, htmlCode, helper, profile):
    input = report.ui.inputs.textarea(value, width=(100, "%"), placeholder=placeholder)
    super(FieldTextArea, self).__init__(report, input, label, placeholder, size, icon, width, height, htmlCode, helper, profile)


class FieldSelect(Field):
  def __init__(self, report, value, label, size, icon, width, height, htmlCode, helper, profile):
    input = report.ui.select(value, width=(100, "%"))
    super(FieldSelect, self).__init__(report, input, label, "", size, icon, width, height, htmlCode, helper, profile)


class Checkbox(Html.Html):
  name, category, callFnc = 'Checkbox', 'Inputs', 'checkbox'
  _grpCls = CssGrpClsInput.CssClassInput

  def __init__(self, report, flag, label, group_name, size, width, height, htmlCode, filter, options, attrs, profile):
    super(Checkbox, self).__init__(report, {"value": flag, 'text': label}, htmlCode=htmlCode, width=width[0],
                                   widthUnit=width[1], height=height[0], heightUnit=height[1], globalFilter=filter,
                                   profile=profile, options=options)
    self.set_attrs(attrs={"type": "checkbox"})
    self.set_attrs(attrs=attrs)
    self.css({"font-size": "%s%s" % (size[0], size[1]), "cursor": 'pointer', 'display': 'inline-block',
              'vertical-align': 'middle', 'margin-left': '2px'})

  @property
  def _js__builder__(self):
    return '''htmlObj.checked = data.value; 
      if(data.text !== null){
        htmlObj.parentNode.insertBefore(document.createTextNode(data.text), htmlObj.nextSibling)};
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def __str__(self):
    return '<input %(strAttr)s>' % {'strAttr': self.get_attrs(pyClassNames=self.defined)}


class Radio(Html.Html):
  name, category, callFnc = 'Radio', 'Inputs', 'radio'

  def __init__(self, report, flag, label, group_name, icon, size, width, height, htmlCode, helper, profile):
    super(Radio, self).__init__(report, {"value": flag, 'text': label}, htmlCode=htmlCode, width=width[0], widthUnit=width[1],
                                height=height[0], heightUnit=height[1], profile=profile)
    self.add_input("", position="before", css={"width": 'none', "vertical-align": 'middle'})
    self.add_label(label, position="after", css={"display": 'inline-block', "width": "None", 'float': 'none'})
    self.input.inReport = False
    if flag:
      self.input.set_attrs({"checked": json.dumps(flag)})
    self.input.pyStyle = GrpCls.CssGrpClass(self)
    if group_name is not None:
      self.input.set_attrs(name="name", value=group_name)
    self.input.set_attrs(attrs={"type": "radio"})
    self.input.css({"font-size": "%s%s" % (size[0], size[1]), "cursor": 'pointer', 'display': 'inline-block',
                    'vertical-align': 'middle', 'min-width': 'none'})
    self.css({'vertical-align': 'middle', 'text-align': "left"})
    self.add_icon(icon, position="after", css={"margin-left": '5px', 'color': self._report.theme.success[1]})

  @property
  def _js__builder__(self):
    return '''htmlObj.checked = data.value; 
      if(data.text !== null){
        htmlObj.parentNode.insertBefore(document.createTextNode(data.text), htmlObj.nextSibling)};
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def __str__(self):
    return '<div %(strAttr)s></div>' % {'strAttr': self.get_attrs(pyClassNames=self.defined)}


class TextArea(Html.Html):
  name, category, callFnc = 'Text Area', 'Inputs', 'textArea'
  _grpCls = CssGrpClsInput.CssClassTextArea

  def __init__(self, report, text, width, rows, placeholder, size, background_color, htmlCode, options, profile):
    super(TextArea, self).__init__(report, text, htmlCode=htmlCode, width=width[0], widthUnit=width[1], profile=profile)
    self.width, self.rows, self.backgroundColor = width, rows, background_color
    self.css({"font-size": "%s%s" % (report.style.defaults.font.size, report.style.defaults.font.unit),
              "font-family": report.style.defaults.font.family})
    if not options.get("selectable", True):
      self.attr['onclick'] = "this.blur();this.select()"
      options["readOnly"] = True
      del options["selectable"]

    options.update({"rows": rows, "placeholder": placeholder or ""})
    self.set_attrs(attrs=options)
    self.css({"font-size": "%s%s" % (size[0], size[1])})

  def jsAppend(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsStyles=None, jsFnc=None):
    return "%s.append(%s+ '\\r\\n')" % (self.jqId, self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc))

  @property
  def _js__builder__(self):
    return 'htmlObj.innerHTML = data'

  def empty(self): return 'document.getElementById("%s").value = ""' % self.htmlId

  def __str__(self):
    return '<textarea %(strAttr)s></textarea>' % {"strAttr": self.get_attrs(pyClassNames=self.defined)}


class Search(Html.Html):
  name, category, callFnc = 'Search', 'Inputs', 'search'
  _grpCls = GrpCls.CssGrpClassBase

  def __init__(self, report, text, placeholder, color, size, height, htmlCode, tooltip, extensible, profile):
    self.size = "%s%s" % (size[0], size[1])
    super(Search, self).__init__(report, "", htmlCode=htmlCode, height=height[0], heightUnit=height[1], profile=profile)
    self.color = self._report.theme.colors[-1] if color is None else color
    self.css({"display": "inline-block", "margin-bottom": '2px'})
    #
    if not extensible:
      self._report.style.cssCls('CssSearch')
      pyCssCls = self._report.style.cssName('CssSearch')
      self.css({"width": "100%"})
    else:
      self._report.style.cssCls('CssSearchExt')
      pyCssCls = self._report.style.cssName('CssSearchExt')
    self.add_input(text).input.set_attrs({"class": [pyCssCls], "placeholder": placeholder, "spellcheck": False})
    self.input.css({"text-align": 'left', 'padding-left': '%spx' % Defaults.LINE_HEIGHT})
    self.add_icon("fas fa-search").icon.attr['id'] = "%s_button" % self.htmlId
    self.icon.css({"margin": '6px 0 6px 5px', 'display': 'block', 'cursor': 'pointer', 'position': 'absolute'})
    if tooltip != '':
      self.tooltip(tooltip)

  @property
  def dom(self):
    if self._dom is None:
      self._dom = JsHtmlField.JsHtmlFields(self, report=self._report)
    return self._dom

  @property
  def _js__builder__(self):
    return '''htmlObj.find('input').val(data)'''

  def click(self, jsFncs, profile=False):
    return self.icon.click(jsFncs, profile)

  def enter(self, jsFncs, profile=False):
    """
    Add an javascript action when the key enter is pressed on the keyboard

    Example
    htmlObj.enter(" alert() ")

    :param jsFncs:
    :return: The python object itself
    """
    self.click(jsFncs)
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return self.on("keydown", ["if (event.keyCode  == 13) {event.preventDefault(); %(jsFnc)s } " % {"jsFnc": JsUtils.jsConvertFncs(jsFncs, toStr=True)}], profile=profile)

  def __str__(self):
    return '<div %(attr)s></div>' % {"attr": self.get_attrs(pyClassNames=self.defined)}
