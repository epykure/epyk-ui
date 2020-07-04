#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

from epyk.core.html import Html
from epyk.core.js.html import JsHtmlJqueryUI


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
      self.add_icon(icon, css={"margin-left": '5px', 'color': self._report.theme.success[1]}, position="after", family=options.get("icon_family"))
    else:
      self.icon = None
    if self.icon is not None:
      self.icon.click([self.input.dom.events.trigger("click").toStr()])
      self.icon.tooltip(self.input.dom.content)
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"color": color or 'inherit', "vertical-align": "middle", "display": "block", "width": 'auto', 'margin-top': '2px'})

  @property
  def dom(self):
    """
    Description:
    ------------
    The Javascript Dom proxy to the input object

    :rtype: JsHtmlJqueryUI.JsHtmlDateFieldPicker
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlDateFieldPicker(self, report=self._report)
    return self._dom

  def select(self, jsFncs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if self.icon is not None:
      jsFncs.append(self.icon.dom.setattr("title", self.input.dom.content))
    self.input.options.onSelect = jsFncs
    return self

  def excluded_dates(self, dts=None, jsFncs=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param dts:
    :param jsFncs:
    """
    return self.input.excluded_dates(dts, jsFncs)

  def included_dates(self, dts=None, jsFncs=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param dts:
    :param jsFncs:
    """
    return self.input.included_dates(dts, jsFncs)

  def add_options(self, options=None, name=None, value=None):
    """
    Description:
    -----------
    Add TimePicker options

    Related Pages:

      https://timepicker.co/options/

    Attributes:
    ----------
    :param key: A string or a Python dictionary with the options to set
    :param val: Optional.
    """
    if options is None and name is None:
      raise Exception("Either the attrs or the name should be specified")

    if options is None:
      options = {name: value}
    for k, v in options.items():
      self.vals['options'][k] = v
    return self

  def __str__(self):
    return '<div %(attr)s>%(helper)s</div>' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'helper': self.helper}


class TimePicker(Html.Html):
  requirements = ('timepicker', )
  name = 'Time Picker'

  def __init__(self, report, value, label, icon, color, htmlCode, profile, options, helper):
    super(TimePicker, self).__init__(report, None, htmlCode=htmlCode, profile=profile)
    # Add the internal components (label, icon)
    self.input = self._report.ui.inputs.d_time(value, options=options)
    self.input.set_attrs(name="class", value='time').css({"padding": 0})
    self.prepend_child(self.input)
    self.add_icon(icon, css={"margin-left": '5px', 'color': self._report.theme.success[1]}, position="after", family=options.get("icon_family"))
    if self.icon is not None:
      self.icon.click(self.input.dom.events.trigger("click").toStr())
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"color": color or 'inherit', "vertical-align": "middle", 'margin-top': '2px'})

  @property
  def dom(self):
    """
    Description:
    ------------
    The Javascript Dom proxy to the input object

    :rtype: JsHtmlJqueryUI.JsHtmlDateFieldPicker
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlDateFieldPicker(self, report=self._report)
    return self._dom

  # @property
  # def options(self):
  #   """
  #   Description:
  #   -----------
  #   The progress bar is designed to display the current percent complete for a process.
  #   The bar is coded to be flexibly sized through CSS and will scale to fit inside its parent container by default.
  #
  #   Related Pages:
  #
	# 		https://api.jqueryui.com/menu
  #
  #   :rtype: OptInputs.OptionsTimePicker
  #   """
  #   return self.input.options

  def change(self, jsFnc):
    """
    Description:
    -----------
    Event triggerd when the value of the input field changes. A Date object containing the selected time is passed as the first argument of the callback.
    Note: the variable time is a function parameter received in the Javascript side

    Usage::

      morning = rptObj.ui.fields.time("8:13:00", label="Time field")
    morning.change([
      rptObj.js.alert("time", skip_data_convert=True)
    ])

    Related Pages:

      https://timepicker.co/options/

    Attributes:
    ----------
    :param jsFnc:
    """
    self.input.change(jsFnc)
    return self

  def __str__(self):
    return '<div %(attr)s>%(helper)s</div>' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'helper': self.helper}


class CountDownDate(Html.Html):
  name = 'Countdown'

  def __init__(self, report, yyyy_mm_dd, label, icon, timeInMilliSeconds, width, height, htmlCode, helper, options, profile):
    super(CountDownDate, self).__init__(report, yyyy_mm_dd, htmlCode=htmlCode, profile=profile, css_attrs={"width": width, "height": height})
    self._jsStyles = {"delete": True}
    self.timeInMilliSeconds = timeInMilliSeconds
    # Add the underlying components
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_icon(icon, family=options.get("icon_family"))
    self.add_helper(helper)

  @property
  def jqId(self):
    return "$('#%s span')" % self.htmlCode

  @property
  def _js__builder__(self):
    return ''' 
      var splitDt = data.split("-"); var endDate = new Date(splitDt[0], parseInt(splitDt[1])-1, splitDt[2]);
      var now = new Date().getTime(); var distance = endDate.getTime() - now;

      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      htmlObj.innerHTML = "<b>"+ days +"d "+ hours +"h "+ minutes + "m "+ seconds +"s </b>"; 
      if ((distance < 0) && (options.delete)){clearInterval(htmlObj.id +"_interval")
      }'''

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
    Javascript shortcut to change the timestamp to this component
    """
    return self.dom.innerHTML(self._report.js.objects.date().getStrTimeStamp().prepend(self._label))

  def __str__(self):
    return '<div %(strAttr)s>%(content)s</div>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'content': self.val}


class Calendar(Html.Html):
  name = 'Calendar'

  def __init__(self, report, content, width, height, align, options, htmlCode, profile):
    super(Calendar, self).__init__(report,  content, htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    self.tasks, self.caption = {}, ""
    self.style.css.border_collapse = "collapse"
    self.style.css.border_spacing = 0
    if align is not None:
      if align == 'center':
        self.style.css.margin_left = 'auto'
        self.style.css.margin_right = 'auto'

  def task(self, name, start, capacity, end=None, weekend=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param start:
    :param capacity: Float. A figure in percentage
    :param end:
    """
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

  def __str__(self):
    header = ["<th style='width:%s%%;background:grey;color:white;padding:5px 2px;text-align:center'>%s</th>" % (100 / len(self.labels), d) for d in self.labels]
    body, row = [], []
    for i, day in enumerate(self.val):
      if 'number' in day:
        total_capacity = 0
        for t in day.get("tasks", []):
          total_capacity += t.get("capacity", 0)
        if total_capacity > 100:
          day["total_capacity"] = total_capacity
          numer_day = "<div style='font-size:20px;text-align:center;color:red;font-weight:bold;cursor:pointer' title='overload: %(total_capacity)s%%'>%(number)s</div>" % day
        else:
          numer_day = "<div style='font-size:20px;text-align:center'>%(number)s</div>" % day
        tasks = "<div>%s</div>" % "".join(["<div style='width:100%%;height:20px;display:block;vertical-align:middle'><div style='background:%(color)s;width:100%%;height:%(capacity)s%%;display:inline-block' title='%(name)s: %(capacity)s%%'></div></div>" % t for t in day.get("tasks", [])])
        if day.get("today", False):
          row.append("<td style='padding:0;border-bottom:1px solid grey;background:%s'>%s%s</td>" % (self._report.theme.success[0], numer_day, tasks))
        else:
          row.append("<td style='padding:0;border-bottom:1px solid grey'>%s%s</td>" % (numer_day, tasks))
        #row.append("<td style='padding:0'>%s%s<div style='background:yellow;width:100%%;height:20px;display:block'><div><div style='background: orange;width:100%%;height:10px;display:block'><div></td>" % day)
      else:
        row.append("<td style='padding:0'></td>")
      if i % len(self.labels) == 0:
        body.append("<tr>%s</tr>" % "".join(row))
        row = []
    if row:
      for i in range(7 - len(row)):
        row.append("<td style='padding:0'></td>")
      body.append("<tr>%s</tr>" % "".join(row))
    return '<table %(strAttr)s><caption style="text-align:right">%(caption)s</caption><tr>%(header)s</tr>%(content)s</table>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'caption': self.caption, 'header': "".join(header), 'content': "".join(body)}

