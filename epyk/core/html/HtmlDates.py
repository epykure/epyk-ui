#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import datetime

from typing import Union, Optional, List
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.html import Html
from epyk.core.html.options import OptCalendars
from epyk.core.html.options import OptText

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlJqueryUI, JsHtml

from epyk.core.css import Defaults


class DatePicker(Html.Html):
  requirements = ('jqueryui', )
  name = 'Date Picker'
  _option_cls = OptCalendars.OptionDatePicker

  def __init__(self, page: primitives.PageModel, value, label: Optional[str], icon: Optional[str], width: tuple,
               height: tuple, color: Optional[str], html_code: Optional[str],
               profile: Optional[Union[dict, bool]], options: Optional[dict], helper: Optional[str]):
    super(DatePicker, self).__init__(page, value, html_code=html_code, profile=profile)
    # Add all the internal components input, label, icon and helper
    if width[0] is not None and width[1] == 'px':
      width = (width[0] - 30, width[1])
    self.input = self.page.ui.inputs.d_date(self.val, width=width, height=height, options=options,
      html_code="%s_input" % html_code if html_code is not None else html_code).css({"padding": 0})
    if html_code is not None:
      self.input.attr["name"] = "%s_input" % html_code
    self.prepend_child(self.input)
    if not self.input.options.inline and icon:
      self.add_icon(icon, html_code=self.htmlCode,
                    css={"margin-top": '-4px', "margin-left": '5px', 'color': color or "inherit"},
                    position="after", family=options.get("icon_family"))
    else:
      self.icon = None
    if self.icon is not None:
      self.icon.click([self.input.dom.events.trigger("click").toStr()])
    self.add_label(label, html_code=self.htmlCode, css={'height': 'auto', 'margin-top': '1px', 'margin-bottom': '1px'},
                   options=options)
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"color": color or 'inherit', "vertical-align": "middle", "display": "block", "width": 'auto'})

  @property
  def options(self) -> OptCalendars.OptionDatePicker:
    """ Property to set all the DatePicker properties. """
    return super().options

  @property
  def dom(self) -> JsHtmlJqueryUI.JsHtmlDateFieldPicker:
    """
    The Javascript Dom proxy to the input object.

    Usage::

      today = page.ui.fields.today()
      today.select([
        page.js.console.log(today.dom.content)
      ])
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlDateFieldPicker(self, page=self.page)
    return self._dom

  def select(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Event trigger when the DatePicker component changes.

    Usage::

      today = page.ui.fields.today()
      today.select([
        page.js.console.log(today.dom.content)
      ])

    :param js_funcs: The Javascript events when the DatePicker selection changes
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    if self.icon is not None:
      self.icon.tooltip(self.input.dom.content)
      js_funcs.append(self.icon.dom.setattr("title", self.input.dom.content))
    self.input.options.onSelect(js_funcs, profile)
    return self

  def excluded_dates(self, dts: Optional[List[str]] = None, js_funcs: types.JS_FUNCS_TYPES = None,
                     profile: types.PROFILE_TYPE = False):
    """
    Exclude some dates from the date picker selection.

    Those dates will be visible but no available for selection.

    Usage::

      today = page.ui.fields.today()
      today.excluded_dates(["2021-01-01"])

    :param dts: Optional. A list of dates format YYYY-MM-DD
    :param js_funcs: Optional. Javascript functions
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console
    """
    return self.input.excluded_dates(dts, js_funcs, profile)

  def included_dates(self, dts: List[str] = None, selected: str = None,
                     js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = False):
    """
    Include some date to be available for selection.

    All the other dates will be visible but not valid ones.

    Usage::

      today = page.ui.fields.today()
      today.included_dates(["2021-01-01"])

    :param dts: Optional. A list of dates format YYYY-MM-DD
    :param selected: Optional. The selected date from the range. Default max
    :param js_funcs: Optional. Javascript functions
    :param profile: Optional. Set to true to get the profile or a function on the console
    """
    return self.input.included_dates(dts, selected, js_funcs, profile)

  def add_options(self, options: dict = None, name: str = None, value: str = None):
    """
    Add DatePicker options.

    Related Pages:

      https://timepicker.co/options/

    :param options: Optional. Specific Python options available for this component
    :param name: Optional. Python dictionary with the options to set
    :param value: Optional. The option value
    """
    if options is None and name is None:
      raise ValueError("Either the attrs or the name should be specified")

    if options is None:
      options = {name: value}
    for k, v in options.items():
      setattr(self.input.options, k, v)
    return self

  def __str__(self):
    return '<div %(attr)s>%(helper)s</div>' % {
      'attr': self.get_attrs(css_class_names=self.style.get_classes()), 'helper': self.helper}


class TimePicker(Html.Html):
  requirements = ('timepicker', )
  name = 'Time Picker'

  def __init__(self, page: primitives.PageModel, value, label: Optional[str], icon: Optional[str],
               color: Optional[str], html_code: Optional[str], profile: Optional[Union[bool, dict]],
               options: Optional[dict], helper: Optional[str]):
    super(TimePicker, self).__init__(page, None, html_code=html_code, profile=profile)
    self.input = self.page.ui.inputs.d_time(
      value, options=options, html_code="%s_input" % html_code if html_code is not None else html_code)
    self.input.set_attrs(name="class", value='time').css({"padding": 0})
    if html_code is not None:
      self.input.attr["name"] = "%s_input" % html_code
    self.prepend_child(self.input)
    self.add_icon(icon, html_code=self.htmlCode, css={"margin-left": '5px', 'color': self.page.theme.success.base},
                  position="after", family=options.get("icon_family"))
    if self.icon is not None:
      self.icon.click(self.input.dom.events.trigger("click").toStr())
    self.add_label(label, css={'height': 'auto', 'margin-top': '1px', 'margin-bottom': '1px'}, options=options)
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"color": color or 'inherit', "vertical-align": "middle"})

  @property
  def dom(self) -> JsHtmlJqueryUI.JsHtmlDateFieldPicker:
    """
    The Javascript Dom proxy to the input object.

    Usage::

      time_picker = page.ui.fields.time()
      time_picker.change([
        page.js.console.log(time_picker.dom.content)
      ])
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlDateFieldPicker(self, page=self.page)
    return self._dom

  def change(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, on_ready: bool = False):
    """
    Event triggered when the value of the input field changes.

    A Date object containing the selected time is passed as the first argument of the callback.
    Note: the variable time is a function parameter received in the Javascript side.

    Usage::

      morning = page.ui.fields.time("8:13:00", label="Time field")
      morning.change([
        page.js.alert("time", skip_data_convert=True)
      ])

    Related Pages:

      https://timepicker.co/options/

    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
    """
    self.input.change(js_funcs, profile, on_ready=on_ready)
    return self

  def __str__(self):
    return '<div %(attr)s>%(helper)s</div>' % {
      'attr': self.get_attrs(css_class_names=self.style.get_classes()), 'helper': self.helper}


class CountDownDate(Html.Html):
  name = 'Countdown'

  def __init__(self, page: primitives.PageModel, day: int, month: int, year: int, hour: int, minute: int, second: int,
               label: Optional[str], icon: Optional[str], timestamp, width, height, html_code, helper, options, profile):
    super(CountDownDate, self).__init__(page, {'day': day, 'month': month, 'year': year, 'hour': hour,
                                               'minute': minute, 'second': second}, html_code=html_code,
                                        profile=profile, css_attrs={"width": width, "height": height})
    self._jsStyles = {"delete": True, 'reload': False}
    # timestamp in milliseconds
    self.timeInMilliSeconds = timestamp
    # Add the underlying components
    self.add_label(label, html_code=self.htmlCode, css={
      "padding": '2px 0', 'height': 'auto', "width": "none", "line-height": "none"})
    self.add_icon(icon, html_code=self.htmlCode, family=options.get("icon_family"))
    self.add_helper(helper)
    self._jquery_ref = '#%s span' % self.htmlCode

  def end(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Events triggered at the end of the timer.

    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles["end"] = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    self.page.properties.js.add_builders(
      '''var %(htmlCode)s_interval = setInterval(function(){%(refresh)s}, %(timeInMilliSeconds)s)
          ''' % {'htmlCode': self.htmlCode, 'refresh': self.refresh(), 'timeInMilliSeconds': self.timeInMilliSeconds})
    return '<div %s><span name="dt_time"></span>%s</div>' % (
      self.get_attrs(css_class_names=self.style.get_classes()), self.helper)


class LastUpdated(Html.Html):
  name = 'Last Update'
  _option_cls = OptText.OptionsUpdate

  def __init__(self, page: primitives.PageModel, label: Optional[str], color: Optional[str], width: tuple,
               height: tuple, html_code: Optional[str], options: Optional[dict], profile: Optional[Union[bool, dict]]):
    self._label = "Last update: " if label is None else label
    super(LastUpdated, self).__init__(
      page, "%s%s" % (self._label, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), html_code, profile=profile,
      options=options, css_attrs={"width": width, "height": height, "color": color})
    self.attr["data-value"] = None

  @property
  def options(self) -> OptText.OptionsUpdate:
    """ Property to set all the DatePicker properties. """
    return super().options

  @property
  def dom(self) -> JsHtml.JsHtmlRich:
    """
    Return all the Javascript functions defined for an HTML Component.

    Those functions will use plain javascript available for a DOM element by default.

    Usage::

      div = page.ui.div(htmlCode="testDiv")
      print(div.dom.content)

    :return: A Javascript Dom object.
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, page=self.page)
    return self._dom

  def refresh(self):
    """
    Javascript shortcut to change the timestamp to this component.

    Usage::

      update = page.ui.rich.update()
      update.click([
        update.refresh()
      ])
    """
    return self.build(self.page.js.objects.date(
      local_time=self.options.local_time).getStrTimeStamp().prepend(self._label))

  def __str__(self):
    return '<div %(strAttr)s>%(content)s</div>' % {
      'strAttr': self.get_attrs(css_class_names=self.style.get_classes()), 'content': self.val}


class Calendar(Html.Html):
  name = 'Calendar'
  requirements = ('jquery', )
  _option_cls = OptCalendars.OptionDays

  def __init__(self, page: primitives.PageModel, content: Optional[str], width: tuple, height: tuple,
               align: Optional[str], options: Optional[dict], html_code: Optional[str],
               profile: Optional[Union[bool, dict]]):
    super(Calendar, self).__init__(page,  content, html_code, css_attrs={"width": width, "height": height},
                                   profile=profile, options=options)
    self.labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    self.tasks, self.caption = {}, ""
    self.style.css.border_collapse = "collapse"
    self.style.css.border_spacing = 0
    if align is not None:
      if align == 'center':
        self.style.css.margin_left = 'auto'
        self.style.css.margin_right = 'auto'
      else:
        self.style.css.text_align = align

  @property
  def options(self) -> OptCalendars.OptionDays:
    """ Property to set all the Calendar properties. """
    return super().options

  def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
            source_event: str = None, on_ready: bool = False):
    """
    Add a click event to the Calendar component.

    :param js_funcs: A Javascript Python function.
    :param profile: Optional. Set to true to profile or a function on the Js console.
    :param source_event: Optional. The source target for the event.
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.__click = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def task(self, name: str, start: str, capacity: Union[List[float], float], end: Optional[str] = None,
           weekend: bool = False, options: dict = None):
    """

    :param name: The task name
    :param start: The task start date format YYYY-MM-DD
    :param capacity: A figure in percentage
    :param end: The task end date format YYYY-MM-DD
    :param weekend: Optional. Flag to specify if the weekends should be considered
    :param options: Optional. Specific Python options available for this component
    """
    if self.options.unit != 100 and options is None:
      options = {'unit': self.options.unit}
    if options is not None and 'unit' in options:
      if isinstance(capacity, list):
        capacity = [100 * c / options['unit'] for c in capacity]
      else:
        capacity = 100 * capacity / options['unit']
    if name not in self.tasks:
      self.tasks[name] = self.page.theme.charts[len(self.tasks)]
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
              i += 1
            elif end is None:
              dt['tasks'].append({"name": name, 'capacity': value, 'color': self.tasks[name]})
              i += 1
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

  def weekly(self, name, start, capacity, frequency: int = 1, weekend: bool = False, options: Optional[dict] = None):
    """


    :param name:
    :param start:
    :param capacity:
    :param frequency:
    :param weekend: Optional. Flag to specify if the weekends should be considered.
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
    header = ["<th style='width:%s%%;%s'>%s</th>" % (
      100 / len(self.labels), Defaults.inline(self.options.header), d) for d in self.labels]
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
          row.append("<td data-placement='right' data-toggle='tooltip' data-html='true' title='<div>%s</div>' style='%s;background:%s'>%s%s</td>" % ("".join(tooltip), cell_style, self.page.theme.success.light, numer_day, tasks))
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
    #self.page.properties.js.add_on_ready(
    #  "%s.tooltip()" % JsQuery.decorate_var("'[data-toggle=tooltip]'", convert_var=False))
    return '<table %(strAttr)s><caption style="text-align:right">%(caption)s</caption><tr>%(header)s</tr>%(content)s</table>' % {
      'strAttr': self.get_attrs(css_class_names=self.style.get_classes()), 'caption': self.caption, 'header': "".join(header), 'content': "".join(body)}


class Timer(Html.Html):
  name = 'Timer'

  def __init__(self, page: primitives.PageModel, minutes: int, text: Optional[str], width: tuple, height: tuple,
               align: Optional[str], options: Optional[dict], html_code: Optional[str],
               profile: Optional[Union[dict, bool]]):
    super(Timer, self).__init__(page, {"minutes": minutes, 'text': text}, html_code, options=options,
                                css_attrs={"width": width, "height": height}, profile=profile)
    if align is not None:
      if align == 'center':
        self.style.css.margin_left = 'auto'
        self.style.css.margin_right = 'auto'

  def end(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Events triggered at the end of the timer.

    :param js_funcs: Javascript functions
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles["end"] = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % (self.get_attrs(css_class_names=self.style.get_classes()))


class Elapsed(Html.Html):
  name = 'elapsed'

  def __init__(self, page: primitives.PageModel, day: int, month: int, year: int, label: Optional[str],
               icon: Optional[str], width: tuple, height: tuple,
               html_code: Optional[str], helper: Optional[str], options: Optional[dict],
               profile: Optional[Union[bool, dict]]):
    super(Elapsed, self).__init__(page, {'day': day, 'month': month, 'year': year}, html_code=html_code,
                                  profile=profile, css_attrs={"width": width, "height": height})
    # Add the underlying components
    self.add_label(label, html_code=self.htmlCode, css={"padding": '2px 0', 'height': 'auto'})
    self.add_icon(icon, html_code=self.htmlCode, family=options.get("icon_family"))
    self.add_helper(helper)

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s><span name="clock"></span>%s</div>' % (
      self.get_attrs(css_class_names=self.style.get_classes()), self.helper)
