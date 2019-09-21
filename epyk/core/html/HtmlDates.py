"""
Module in charge of the structured date objects
"""

import json
import time

from epyk.core.html import Html


class DatePicker(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui']
  name, category, callFnc = 'Date Picker', 'Dates', 'date'
  __pyStyle = ['CssDivNoBorder', 'CssDatePicker']

  def __init__(self, report, value, label, icon, color, size, htmlCode, profile, options, helper):
    dfltOptions = {'dateFormat': 'yy-mm-dd'}
    dfltOptions.update(options)
    super(DatePicker, self).__init__(report, {"value": value, "options": dfltOptions}, htmlCode=htmlCode, profile=profile)
    # Add all the internal components input, label, icon and helper
    self.input = self._report.ui.inputs.d_date(self.vals)
    self.input.add_attrs({"class": ['time']})
    self.prepend_child(self.input)
    self.add_icon(icon, css={"margin-left": '5px', 'color': self.getColor("success", 1)})
    if self.icon is not None:
      self.icon.click(self.input.dom.events.trigger("click").toStr())
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"color": color or 'inherit', "vertical-align": "middle", "font-size": "%s%s" % (size[0], size[1])})

  def selectable(self, dts):
    """
    Restrict the selection on a list of dates

    :param dts: A Python list of dates in the format YYYY-MM-DD

    :return: The Python date object
    """
    self.vals['options']["selectedDts"] = dts
    return self

  def add_options(self, opts, isPyData=True):
    """
    Add Date Picker options

    Documentation
    https://api.jqueryui.com/datepicker/

    :param opts: Python dictionary with options
    :param isPyData: Optional. Flag to convert the values to Javascript. Default True

    :return: The Html Python Date object
    """
    if isPyData:
      for k, v in opts.items():
        self.vals['options'][k] = json.dumps(v)
    else:
      for k, v in opts.items():
        self.vals['options'][k] = v
    return self

  @property
  def val(self): return '%s.val()' % self.jqId

  @property
  def jqId(self):
    return "$('#%s input')" % self.htmlId

  def jsGenerate(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsStyles=None, jsFnc=None):
    """
    Propagate the update event
    """
    return self.input.jsGenerate(jsData, jsDataKey, isPyData, jsParse, jsStyles, jsFnc)

  def __str__(self):
    return '<div %(attr)s>%(helper)s</div>' % {'attr': self.strAttr(pyClassNames=['CssDivNoBorder', 'CssDivCursor']), 'helper': self.helper}


class TimePicker(Html.Html):
  __reqCss, __reqJs = ['timepicker'], ['timepicker']
  name, category, callFnc = 'Time Picker', 'Dates', 'date'
  __pyStyle = ['CssDivNoBorder']

  def __init__(self, report, value, label, icon, color, size, htmlCode, profile, options, helper):
    super(TimePicker, self).__init__(report, value, htmlCode=htmlCode, profile=profile)
    # Add the internal components (label, icon)
    self.input = self._report.ui.inputs.d_time(value)
    self.input.add_attrs({"class": ['time']})
    self.prepend_child(self.input)
    self.add_icon(icon, css={"margin-left": '5px', 'color': self.getColor("success", 1)})
    if self.icon is not None:
      self.icon.click(self.input.dom.events.trigger("click").toStr())
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"margin-top": '1px', "color": color or 'inherit', "vertical-align": "middle", "font-size": "%s%s" % (size[0], size[1])})
    self.options = options

  @property
  def val(self): return '%s.val()' % self.jqId

  @property
  def jqId(self):
    return "$('#%s input')" % self.htmlId

  @property
  def jsQueryData(self):
    if self.htmlCode is not None:
      return "{event_val: %(jqId)s.val(), event_code: '%(jqId)s', %(htmlCode)s: %(jqId)s.val()}" % {'jqId': self.jqId, 'htmlCode': self.htmlCode}

    return "{event_val: %(jqId)s.val(), event_code: '%(jqId)s'}" % {'jqId': self.jqId}

  def jsGenerate(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsStyles=None, jsFnc=None):
    """
    Propagate the update event
    """
    return self.input.jsGenerate(jsData, jsDataKey, isPyData, jsParse, jsStyles, jsFnc)

  def add_options(self, key, val=None, isPyData=True):
    """
    Add TimePicker options

    Documentation
    https://timepicker.co/options/

    :param key: A string or a Python dictionary with the options to set
    :param val: Optional.
    :param isPyData: Optional

    :return:
    """
    if isinstance(key, dict):
      for k, v in key.items():
        if isPyData:
          v = json.dumps(v)
        self.vals['options'][k] = v
    else:
      if isPyData:
        val = json.dumps(val)
      self.vals['options'][key] = val

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
    return '<div %(attr)s>%(helper)s</div>' % {'attr': self.strAttr(pyClassNames=['CssDivNoBorder', 'CssDivCursor']), 'helper': self.helper}


class CountDownDate(Html.Html):
  name, category, callFnc = 'Countdown', 'Dates', 'countdown'

  def __init__(self, report, yyyy_mm_dd, label, icon, timeInMilliSeconds, width, height, htmlCode, helper, profile):
    super(CountDownDate, self).__init__(report, yyyy_mm_dd, code=htmlCode, width=width[0], widthUnit=width[1],
                                        height=height[0], heightUnit=height[1], profile=profile)
    self._jsStyles = {"delete": True}
    self.timeInMilliSeconds = timeInMilliSeconds
    #
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_icon(icon)
    self.add_helper(helper)

  @property
  def jqId(self):
    return "$('#%s span')" % self.htmlId

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, ''' 
      var splitDt = data.split("-"); var endDate = new Date(splitDt[0], parseInt(splitDt[1])-1, splitDt[2]);
      var now = new Date().getTime(); var distance = endDate.getTime() - now;

      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance %% (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance %% (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance %% (1000 * 60)) / 1000);

      htmlObj.html("<b>"+ days +"d "+ hours +"h "+ minutes + "m "+ seconds +"s </b>"); 
      if ((distance < 0) && (jsStyles.delete)){clearInterval(htmlObj.attr('id') +"_interval")
      }''' % {"report_name": self._report.run.report_name, "script_name": self._report.run.script_name}, '')

  def onDocumentReady(self):
    self.jsUpdateDataFnc = '''var %(htmlId)s_interval = setInterval(function(){%(pyCls)s(%(jqId)s, %(htmlId)s_data, %(jsStyles)s)}, 
            %(timeInMilliSeconds)s)''' % {'htmlId': self.htmlId, 'pyCls': self.__class__.__name__, 'jqId': self.jqId,
                                          "jsStyles": json.dumps(self._jsStyles),
                                          'timeInMilliSeconds': self.timeInMilliSeconds}
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.jsUpdateDataFnc)

  def __str__(self):
    return '<div %s><span></span>%s</div>' % (self.strAttr(pyClassNames=self.pyStyle), self.helper)


class LastUpdated(Html.Html):
  name, category, callFnc = 'Last Update', 'Text', 'update'

  def __init__(self, report, label, size, color, width, height, htmlCode, profile):
    super(LastUpdated, self).__init__(report, "%s %s" % (label or "Last update", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())),
                                      htmlCode, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                                      profile=profile)
    if color is not None:
      self.css("color", color)
    if size is not None:
      self.css("font-size", "%s%s" % (size[0], size[1]))

  def __str__(self):
    return '<div %(strAttr)s>%(content)s</div>' % {'strAttr': self.strAttr(pyClassNames=['CssDivNoBorder']), 'content': self.vals}
