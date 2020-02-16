"""
Module in charge of the structured date objects
"""

import time

from epyk.core.html import Html
from epyk.core.js.packages import JsQuery


class DatePicker(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui']
  cssCls = ["datepicker"]
  name, category, callFnc = 'Date Picker', 'Dates', 'date'
  # _grpCls = GrpCls.CssGrpClassBase

  def __init__(self, report, value, label, icon, color, htmlCode, profile, options, helper):
    dfltOptions = {'dateFormat': 'yy-mm-dd'}
    dfltOptions.update(options)
    super(DatePicker, self).__init__(report, {"value": value, "options": dfltOptions}, htmlCode=htmlCode, profile=profile)
    # Add all the internal components input, label, icon and helper
    self.input = self._report.ui.inputs.d_date(self.val).css({"padding": 0})
    #self.input.attributes({"class": ['time']})
    self.prepend_child(self.input)
    self.add_icon(icon, css={"margin-left": '5px', 'color': self._report.theme.success[1]}, position="after")
    if self.icon is not None:
      self.icon.click(self.input.dom.events.trigger("click").toStr())
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"color": color or 'inherit', "vertical-align": "middle", "display": "block", "width": 'auto',
              'margin-top': '2px'})

  def selectable(self, dts):
    """
    Restrict the selection on a list of dates

    :param dts: A Python list of dates in the format YYYY-MM-DD

    :return: The Python date object
    """
    self._vals['options']["selectedDts"] = dts
    return self

  def add_options(self, options=None, name=None, value=None):
    """
    Add TimePicker options

    Documentation
    https://timepicker.co/options/

    :param key: A string or a Python dictionary with the options to set
    :param val: Optional.

    :return:
    """
    if options is None and name is None:
      raise Exception("Either the attrs or the name should be specified")

    if options is None:
      options = {name: value}
    for k, v in options.items():
      self.vals['options'][k] = v
    return self

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
        %s.datepicker(data.options).datepicker('setDate', data.value)
      ''' % JsQuery.decorate_var("htmlObj.querySelector('input')", convert_var=False)

  def __str__(self):
    return '<div %(attr)s>%(helper)s</div>' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'helper': self.helper}


class TimePicker(Html.Html):
  __reqCss, __reqJs = ['timepicker'], ['timepicker']
  name, category, callFnc = 'Time Picker', 'Dates', 'date'
  # _grpCls = GrpCls.CssGrpClassBase

  def __init__(self, report, value, label, icon, color, htmlCode, profile, options, helper):
    super(TimePicker, self).__init__(report, value, htmlCode=htmlCode, profile=profile)
    # Add the internal components (label, icon)
    self.input = self._report.ui.inputs.d_time(value)
    self.input.set_attrs(name="class", value='time').css({"padding": 0})
    self.prepend_child(self.input)
    self.add_icon(icon, css={"margin-left": '5px', 'color': self._report.theme.success[1]}, position="after")
    if self.icon is not None:
      self.icon.click(self.input.dom.events.trigger("click").toStr())
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"color": color or 'inherit', "vertical-align": "middle", 'margin-top': '2px'})
    self.options = options

  @property
  def _js__builder__(self):
    return '''
      if (typeof data == "string"){jQuery(htmlObj).timepicker('setTime', data)
      } else {
        if (data.time == ''){data.time = new Date()};
        if (data.options._change.length > 0) {data.options.change = function(time){
            let data = {event_val: time.getHours() +':'+ time.getMinutes() +':'+ time.getSeconds(), event_code: htmlId}; 
            eval(data.options._change.join(";"))}};
        %(jqId)s.timepicker(data.options); %(jqId)s.timepicker('setTime', data.time)}
      ''' % {"jqId": JsQuery.decorate_var("jQuery(htmlObj)", convert_var=False)}

  def add_options(self, options=None, name=None, value=None):
    """
    Add TimePicker options

    Documentation
    https://timepicker.co/options/

    :param key: A string or a Python dictionary with the options to set
    :param val: Optional.

    :return:
    """
    if options is None and name is None:
      raise Exception("Either the attrs or the name should be specified")

    if options is None:
      options = {name: value}
    for k, v in options.items():
      self.vals['options'][k] = v
    return self

  def change(self, jsFnc):
    """

    :param jsFnc:

    :return:
    """
    if isinstance(jsFnc, list):
      self.vals['options']['_change'] += jsFnc
    else:
      self.vals['options']['_change'].append(jsFnc)
    return self

  def __str__(self):
    return '<div %(attr)s>%(helper)s</div>' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'helper': self.helper}


class CountDownDate(Html.Html):
  name, category, callFnc = 'Countdown', 'Dates', 'countdown'
  # _grpCls = GrpCls.CssGrpClassBase

  def __init__(self, report, yyyy_mm_dd, label, icon, timeInMilliSeconds, width, height, htmlCode, helper, profile):
    super(CountDownDate, self).__init__(report, yyyy_mm_dd, code=htmlCode, profile=profile,
                                        css_attrs={"width": width, "height": height})
    self._jsStyles = {"delete": True}
    self.timeInMilliSeconds = timeInMilliSeconds
    # Add the underlying components
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_icon(icon)
    self.add_helper(helper)

  @property
  def jqId(self):
    return "$('#%s span')" % self.htmlId

  @property
  def _js__builder__(self):
    return ''' 
      var splitDt = data.split("-"); var endDate = new Date(splitDt[0], parseInt(splitDt[1])-1, splitDt[2]);
      var now = new Date().getTime(); var distance = endDate.getTime() - now;

      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance %% (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance %% (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance %% (1000 * 60)) / 1000);

      htmlObj.innerHTML = "<b>"+ days +"d "+ hours +"h "+ minutes + "m "+ seconds +"s </b>"; 
      if ((distance < 0) && (options.delete)){clearInterval(htmlObj.id +"_interval")
      }''' % {"report_name": self._report.run.report_name, "script_name": self._report.run.script_name}

  def __str__(self):
    self.jsUpdateDataFnc = '''var %(htmlId)s_interval = setInterval(function(){%(refresh)s}, %(timeInMilliSeconds)s)
              ''' % {'htmlId': self.htmlId, 'refresh': self.refresh(), 'timeInMilliSeconds': self.timeInMilliSeconds}
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.jsUpdateDataFnc)
    return '<div %s><span></span>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class LastUpdated(Html.Html):
  name, category, callFnc = 'Last Update', 'Text', 'update'

  def __init__(self, report, label, color, width, height, htmlCode, profile):
    super(LastUpdated, self).__init__(report, "%s %s" % (label or "Last update", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())),
                                      htmlCode, css_attrs={"width": width, "height": height, "color": color}, profile=profile)

  def __str__(self):
    return '<div %(strAttr)s>%(content)s</div>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'content': self.val}
