#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import datetime

from epyk.core.html import Html
from epyk.core.html.options import OptCalendars

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsQuery
from epyk.core.js.html import JsHtmlJqueryUI

from epyk.core.css import Defaults


class DatePicker(Html.Html):
  requirements = ('jqueryui', )
  name = 'Date Picker'

  def __init__(self, report, value, label, icon, width, height, color, htmlCode, profile, options, helper):
    super(DatePicker, self).__init__(report, value, htmlCode=htmlCode, profile=profile)
    # Add all the internal components input, label, icon and helper
    if width[0] is not None and width[1] == 'px':
      width = (width[0] - 30, width[1])
    self.input = self._report.ui.inputs.d_date(self.val, width=width, height=height, options=options).css({"padding": 0})
    self.prepend_child(self.input)
    if not self.input.options.inline:
      self.add_icon(icon, htmlCode=self.htmlCode, css={"margin-top": '-4px', "margin-left": '5px',
                                                       'color': self._report.theme.success[1]},
                    position="after", family=options.get("icon_family"))
    else:
      self.icon = None
    if self.icon is not None:
      self.icon.click([self.input.dom.events.trigger("click").toStr()])
    self.add_label(label, htmlCode=self.htmlCode, css={'height': 'auto', 'margin-top': '1px', 'margin-bottom': '1px'}, options=options)
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"color": color or 'inherit', "vertical-align": "middle", "display": "block", "width": 'auto'})

  @property
  def dom(self):
    """
    Description:
    ------------
    The Javascript Dom proxy to the input object.

    Usage:
    -----

      today = page.ui.fields.today()
      today.select([
        page.js.console.log(today.dom.content)
      ])

    :rtype: JsHtmlJqueryUI.JsHtmlDateFieldPicker
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlDateFieldPicker(self, report=self._report)
    return self._dom

  def select(self, jsFncs):
    """
    Description:
    -----------
    Event trigger when the datepicker component changes.

    Usage:
    -----

      today = page.ui.fields.today()
      today.select([
        page.js.console.log(today.dom.content)
      ])

    Attributes:
    ----------
    :param jsFncs: String | List. The Javascript events when the datepicker selection changes.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if self.icon is not None:
      self.icon.tooltip(self.input.dom.content)
      jsFncs.append(self.icon.dom.setattr("title", self.input.dom.content))
    self.input.options.onSelect = jsFncs
    return self

  def excluded_dates(self, dts=None, jsFncs=None):
    """
    Description:
    -----------
    Exclude some dates from the date picker selection.
    Those dates will be visible but no available for selection.

    Usage:
    -----

      today = page.ui.fields.today()
      today.excluded_dates(["2021-01-01"])

    Attributes:
    ----------
    :param dts: List. A list of dates format YYYY-MM-DD.
    :param jsFncs: List or String. Optional. Javascript functions.
    """
    return self.input.excluded_dates(dts, jsFncs)

  def included_dates(self, dts=None, jsFncs=None):
    """
    Description:
    -----------
    Include some date to be available for selection.
    All the other dates will be visible but not valid ones.

    Usage:
    -----

      today = page.ui.fields.today()
      today.included_dates(["2021-01-01"])

    Attributes:
    ----------
    :param dts: List. A list of dates format YYYY-MM-DD.
    :param jsFncs: List or String. Optional. Javascript functions.
    """
    return self.input.included_dates(dts, jsFncs)

  def add_options(self, options=None, name=None, value=None):
    """
    Description:
    -----------
    Add DatePicker options

    Usage:
    -----

    Related Pages:

      https://timepicker.co/options/

    Attributes:
    ----------
    :param options:
    :param name: Optional. A string or a Python dictionary with the options to set
    :param value: Optional.
    """
    if options is None and name is None:
      raise Exception("Either the attrs or the name should be specified")

    if options is None:
      options = {name: value}
    for k, v in options.items():
      setattr(self.input.options, k, v)
    return self

  def __str__(self):
    return '<div %(attr)s>%(helper)s</div>' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'helper': self.helper}


class TimePicker(Html.Html):
  requirements = ('timepicker', )
  name = 'Time Picker'

  def __init__(self, report, value, label, icon, color, htmlCode, profile, options, helper):
    super(TimePicker, self).__init__(report, None, htmlCode=htmlCode, profile=profile)
    self.input = self._report.ui.inputs.d_time(value, options=options)
    self.input.set_attrs(name="class", value='time').css({"padding": 0})
    self.prepend_child(self.input)
    self.add_icon(icon, htmlCode=self.htmlCode, css={"margin-left": '5px', 'color': self._report.theme.success[1]},
                  position="after", family=options.get("icon_family"))
    if self.icon is not None:
      self.icon.click(self.input.dom.events.trigger("click").toStr())
    self.add_label(label, css={'height': 'auto', 'margin-top': '1px', 'margin-bottom': '1px'}, options=options)
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"color": color or 'inherit', "vertical-align": "middle"})

  @property
  def dom(self):
    """
    Description:
    ------------
    The Javascript Dom proxy to the input object.

    Usage:
    -----

      time_picker = page.ui.fields.time()
      time_picker.change([
        page.js.console.log(time_picker.dom.content)
      ])

    :rtype: JsHtmlJqueryUI.JsHtmlDateFieldPicker
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlDateFieldPicker(self, report=self._report)
    return self._dom

  def change(self, jsFncs, profile=False):
    """
    Description:
    -----------
    Event triggered when the value of the input field changes. A Date object containing the selected time is passed as the first argument of the callback.
    Note: the variable time is a function parameter received in the Javascript side

    Usage:
    -----

      morning = rptObj.ui.fields.time("8:13:00", label="Time field")
      morning.change([
      rptObj.js.alert("time", skip_data_convert=True)
    ])

    Related Pages:

      https://timepicker.co/options/

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile:
    """
    self.input.change(jsFncs, profile)
    return self

  def __str__(self):
    return '<div %(attr)s>%(helper)s</div>' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'helper': self.helper}


class CountDownDate(Html.Html):
  name = 'Countdown'

  def __init__(self, report, day, month, year, hour, minute, second, label, icon, timeInMilliSeconds, width, height, htmlCode, helper, options, profile):
    super(CountDownDate, self).__init__(report, {'day': day, 'month': month, 'year': year, 'hour': hour, 'minute': minute, 'second': second},
      htmlCode=htmlCode, profile=profile, css_attrs={"width": width, "height": height})
    self._jsStyles = {"delete": True, 'reload': False}
    self.timeInMilliSeconds = timeInMilliSeconds
    # Add the underlying components
    self.add_label(label, htmlCode=self.htmlCode, css={"padding": '2px 0', 'height': 'auto'})
    self.add_icon(icon, htmlCode=self.htmlCode, family=options.get("icon_family"))
    self.add_helper(helper)

  @property
  def jqId(self):
    return "$('#%s span')" % self.htmlCode

  _js__builder__ = '''
      var endDate = new Date(data.year, data.month-1, data.day, data.hour, data.minute, data.second);
      var now = new Date().getTime(); var distance = endDate.getTime() - now;

      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      htmlObj.innerHTML = "<b>"+ days +"d "+ hours +"h "+ minutes + "m "+ seconds +"s </b>"; 
      if ((distance < 0) && (options.delete)){
        if(typeof options.end !== 'undefined'){eval(options.end)}
        htmlObj.remove(); if (options.reload){location.reload()}
        clearInterval(window[htmlObj.id +"_interval"])
      }'''

  def end(self, jsFncs):
    """
    Description:
    -----------
    Events triggered at the end of the timer.

    Usage:
    -----

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._jsStyles["end"] = JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  def __str__(self):
    self.jsUpdateDataFnc = '''var %(htmlCode)s_interval = setInterval(function(){%(refresh)s}, %(timeInMilliSeconds)s)
              ''' % {'htmlCode': self.htmlCode, 'refresh': self.refresh(), 'timeInMilliSeconds': self.timeInMilliSeconds}
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.jsUpdateDataFnc)
    return '<div %s><span></span>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class LastUpdated(Html.Html):
  name = 'Last Update'

  def __init__(self, report, label, color, width, height, htmlCode, profile):
    self._label = label or "Last update: "
    super(LastUpdated, self).__init__(report, "%s%s" % (self._label, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())),
                                      htmlCode, css_attrs={"width": width, "height": height, "color": color}, profile=profile)

  def refresh(self):
    """
    Description:
    ------------
    Javascript shortcut to change the timestamp to this component.

    Usage:
    -----

      update = page.ui.rich.update()
      update.click([
        update.refresh()
      ])
    """
    return self.dom.innerHTML(self._report.js.objects.date().getStrTimeStamp().prepend(self._label))

  def __str__(self):
    return '<div %(strAttr)s>%(content)s</div>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'content': self.val}


class Calendar(Html.Html):
  name = 'Calendar'

  def __init__(self, report, content, width, height, align, options, htmlCode, profile):
    super(Calendar, self).__init__(report,  content, htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptCalendars.OptionDays(self, options)
    self.labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    self.tasks, self.caption = {}, ""
    self.style.css.border_collapse = "collapse"
    self.style.css.border_spacing = 0
    if align is not None:
      if align == 'center':
        self.style.css.margin_left = 'auto'
        self.style.css.margin_right = 'auto'

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the Calendar properties.

    Usage:
    -----

    :rtype: OptCalendars.OptionDays
    """
    return self.__options

  def click(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param jsFncs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__click = JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  def task(self, name, start, capacity, end=None, weekend=False, options=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param name:
    :param start:
    :param capacity: Float. A figure in percentage
    :param end:
    :param weekend:
    :param options:
    """
    if self.options.unit != 100 and options is None:
      options = {'unit': self.options.unit}
    if options is not None and 'unit' in options:
      if isinstance(capacity, list):
        capacity = [100 * c / options['unit'] for c in capacity]
      else:
        capacity = 100 * capacity / options['unit']
    if name not in self.tasks:
      self.tasks[name] = self._report.theme.charts[len(self.tasks)]
      i = 0
      for dt in self._vals:
        if 'date' in dt:
          if dt["weekend"] and not weekend:
            continue

          if start <= dt['date']:
            if not isinstance(capacity, list):
              value = capacity
            else:
              if i >= len(capacity):
                value = capacity[-1]
              else:
                value = capacity[i]
            if end is not None and end >= dt['date']:
              dt['tasks'].append({"name": name, 'capacity': value, 'color': self.tasks[name]})
              i +=1
            elif end is None:
              dt['tasks'].append({"name": name, 'capacity': value, 'color': self.tasks[name]})
              i +=1
    else:
      i = 0
      for dt in self._vals:
        if 'date' in dt:
          if dt["weekend"] and not weekend:
            continue

          if start <= dt['date']:
            if not isinstance(capacity, list):
              value = capacity
            else:
              if i >= len(capacity):
                value = capacity[-1]
              else:
                value = capacity[i]

            if end is not None and end >= dt['date']:
              for t in dt['tasks']:
                if t['name'] == name:
                  t['capacity'] = value
                  i += 1
                  break
            elif end is None:
              for t in dt['tasks']:
                if t['name'] == name:
                  t['capacity'] = value
                  i += 1
                  break

  def weekly(self, name, start, capacity, frequency=1, weekend=False, options=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param name:
    :param start:
    :param capacity:
    :param frequency:
    :param weekend:
    :param options:
    """
    dt = datetime.date(*map(lambda x: int(x), start.split("-")))
    c = []
    month = dt.month
    while dt.month == month:
      if len(c) % (frequency * 5) == 0:
        c.append(capacity)
      else:
        c.append(0)
      dt += datetime.timedelta(days=1)
    self.task(name, start, c, weekend=weekend, options=options)

  def __str__(self):
    header = ["<th style='width:%s%%;%s'>%s</th>" % (100 / len(self.labels), Defaults.inline(self.options.header), d) for d in self.labels]
    body, row = [], []
    for i, day in enumerate(self.val):
      if 'number' in day:
        total_capacity, tooltip = 0, ["<b>%s</b>" % day['date']]
        for t in day.get("tasks", []):
          c = t.get("capacity", 0)
          total_capacity += c
          tooltip.append("<div>%s: %s%%</div>" % (t['name'], c))
        if total_capacity > 100:
          day["total_capacity"] = total_capacity
          day["style"] = Defaults.inline(self.options.overload)
          numer_day = "<div style='%(style)s' data-html='true' data-toggle='tooltip' title='overload: %(total_capacity)s%%'>%(number)s</div>" % day
        else:
          day["style"] = Defaults.inline(self.options.number)
          numer_day = "<div style='%(style)s'>%(number)s</div>" % day
        tasks = "<div>%s</div>" % "".join(["<div style='width:100%%;height:20px;display:block;vertical-align:middle'><div style='background:%(color)s;width:100%%;height:%(capacity)s%%;display:inline-block' title='%(name)s: %(capacity)s%%'></div></div>" % t for t in day.get("tasks", [])])
        cell_style = Defaults.inline(self.options.today)
        if day.get("today", False):
          row.append("<td data-placement='right' data-toggle='tooltip' data-html='true' title='<div>%s</div>' style='%s;background:%s'>%s%s</td>" % ("".join(tooltip), cell_style, self._report.theme.success[0], numer_day, tasks))
        else:
          row.append("<td data-placement='right' data-toggle='tooltip' data-html='true' title='<div>%s</div>' style='%s'>%s%s</td>" % ("".join(tooltip), cell_style, numer_day, tasks))
      else:
        row.append("<td style='padding:0'></td>")
      if i % len(self.labels) == 0:
        body.append("<tr>%s</tr>" % "".join(row))
        row = []
    if row:
      for i in range(7 - len(row)):
        row.append("<td style='padding:0'></td>")
      body.append("<tr>%s</tr>" % "".join(row))
    self._report._props['js']['onReady'].add("%s.tooltip()" % JsQuery.decorate_var("'[data-toggle=tooltip]'", convert_var=False))
    return '<table %(strAttr)s><caption style="text-align:right">%(caption)s</caption><tr>%(header)s</tr>%(content)s</table>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'caption': self.caption, 'header': "".join(header), 'content': "".join(body)}


class Timer(Html.Html):
  name = 'Timer'

  def __init__(self, report, minutes, text, width, height, align, options, htmlCode, profile):
    super(Timer, self).__init__(report, {"minutes": minutes, 'text': text}, htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    if align is not None:
      if align == 'center':
        self.style.css.margin_left = 'auto'
        self.style.css.margin_right = 'auto'

  _js__builder__ = '''     
      var time = data.minutes * 60, r = htmlObj, tmp=time;
      window["time_" + htmlObj.id] = setInterval(function(){ 
        if(tmp < 0){
          if(typeof options.end !== 'undefined'){eval(options.end)}
          clearInterval(window["time_" + htmlObj.id])}
        if (tmp >= 0){
          var c=tmp--, m = (c/60)>>0, s=(c-m*60)+'';
          r.textContent = data.text + ' '+ m +':'+ (s.length>1?'': '0')+ s}
        tmp != 0 || (tmp=0)}, 1000)'''

  def end(self, jsFncs):
    """
    Description:
    -----------
    Events triggered at the end of the timer.

    Usage:
    -----

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._jsStyles["end"] = JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % (self.get_attrs(pyClassNames=self.style.get_classes()))


class Elapsed(Html.Html):
  name = 'elapsed'

  def __init__(self, report, day, month, year, label, icon, width, height, htmlCode, helper, options, profile):
    super(Elapsed, self).__init__(report, {'day': day, 'month': month, 'year': year},
      htmlCode=htmlCode, profile=profile, css_attrs={"width": width, "height": height})
    # Add the underlying components
    self.add_label(label, htmlCode=self.htmlCode, css={"padding": '2px 0', 'height': 'auto'})
    self.add_icon(icon, htmlCode=self.htmlCode, family=options.get("icon_family"))
    self.add_helper(helper)

  _js__builder__ = '''
      var startDate = new Date(data.year, data.month-1, data.day);
      var now = new Date().getTime(); var distance = now - startDate.getTime();
      var days = Math.floor(distance / (1000 * 60 * 60 * 24)); var years = 0;
      if (days > 365){years = Math.floor(days / 365); days = days - years * 365}
      if (years > 0){htmlObj.querySelector("span[name=clock]").innerHTML = "<b>"+ years +"y, "+ days +"d </b>"}
      else {htmlObj.querySelector("span[name=clock]").innerHTML = "<b>"+ days +"d </b>"}'''

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s><span name="clock"></span>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)
