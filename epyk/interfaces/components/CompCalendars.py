#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core import html
from epyk.core.css import Defaults
from epyk.interfaces import Arguments


class Calendar(object):

  def __init__(self, context):
    self.context = context

  def days(self, month=None, content=None, year=None, width=(None, "%"), height=(None, "px"), align=None, options=None, htmlCode=None, profile=None):
    """
    Description:
    ------------

    Usage::


    Related Pages:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py

    Attributes:
    ----------
    :param month:
    :param content:
    :param width:
    :param height:
    :param align:
    :param options:
    :param htmlCode:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    today = datetime.date.today()
    month = month or today.month
    content = content or {}
    dfl_options = {
      'overload': {'font-size': Defaults.font(5), 'text-align': 'center', 'color': self.context.rptObj.theme.danger[1],
                   'font-weight': 'bold', 'cursor': 'pointer'},
      'number': {"font-size": Defaults.font(5), "text-align": "center"},
      'today': {"padding": "0 0 5px 0", "border-bottom": "1px solid grey"},
      'header': {'font-size': Defaults.font(3), "background": self.context.rptObj.theme.colors[-1],
                 "color": self.context.rptObj.theme.colors[0], "padding": "5px 2px", "text-align": "center"}
    }
    factor = 100 / options.get("unit", 100) if options is not None else 1
    if options is not None:
      dfl_options.update(options)
    year = year or today.year
    start = datetime.date(year, month, 1)
    days_data, tasks = [], {}
    for values in content.values():
      for t in values.keys():
        tasks[t] = None
    sorted_tasks = sorted(list(tasks))
    for i, t in enumerate(sorted_tasks):
      tasks[t] = dfl_options.get('colors', {}).get(t, self.context.rptObj.theme.charts[i])
    for _ in range(start.weekday() + 1):
      days_data.append({})
    while start.month == month:
      day_tasks = content.get(start.isoformat(), {})
      tasks_view = []
      for i, t in enumerate(sorted_tasks):
        tasks_view.append({"name": t, 'capacity': factor * day_tasks.get(t, 0), 'color': tasks[t]})
      days_data.append({'today': today == start, "number": start.day, 'tasks': tasks_view, 'date': start.isoformat(), 'weekend': start.weekday() >= 5})
      start += datetime.timedelta(days=1)
    html_table = html.HtmlDates.Calendar(self.context.rptObj, days_data, width, height, align, dfl_options, htmlCode, profile)
    html_table.tasks = tasks
    html_table.caption = "%s %s" % (datetime.date(year, month, 1).strftime("%B"), year)
    return html_table

  def timer(self, minutes, text="", width=(None, "%"), height=(None, "px"), align=None, options=None, htmlCode=None, profile=None):
    """
    Description:
    ------------

    Usage::


    Attributes:
    ----------
    :param minutes:
    :param text: String. Optional. The value to be displayed to the timer
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param align: String. The text-align property within this component
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_timer = html.HtmlDates.Timer(self.context.rptObj, minutes, text, width, height, align, options, htmlCode, profile)
    return html_timer

  def months(self, year=None, content=None, width=(None, "%"), height=(None, "px"), align=None, options=None, htmlCode=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Related Pages:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py

    Attributes:
    ----------
    :param year:
    :param content:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    :param profile:
    """
    today = datetime.date.today()
    content = content or {}
    options = options or {}
    labels = options.get('months', ["January", "February", "March", "April", "May", "June", "July", "August",
                                    "September", "October", "November", "December"])
    rows, tasks = [], {}
    for i, l in enumerate(labels):
      record = []
      for j, k in enumerate(sorted(content.get(i + 1, {}))):
        record.append({"name": k, 'capacity': content[j + 1][k]})
        tasks[k] = self.context.rptObj.theme.charts[j]
      pie = self.context.rptObj.ui.charts.chartJs.pie(record, y_columns=["capacity"], x_axis="name", height=(100, "px"))
      pie.options.legend.display = False
      pie.options.title.text = labels[i]
      pie.options.title.display = True
      pie.options.title.fontSize = Defaults.Font.size + 5
      pie.options.title.fontColor = self.context.rptObj.theme.success[1]
      rows.append(pie)
    row = self.context.rptObj.ui.row(rows)
    row.tasks = tasks
    row[today.month-1].style.css.border = "1px solid %s" % self.context.rptObj.theme.success[0]
    return row

  def legend(self, records, width=(None, "%"), height=(None, "px"), align=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::


    Related Pages:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py

    Attributes:
    ----------
    :param records:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param align: String. The text-align property within this component
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    data = []
    if isinstance(records, dict):
      for k, v in records.items():
        data.append({"name": k, "color": v})
    else:
      for i, rec in enumerate(records):
        if isinstance(rec, dict):
          row = dict(rec)
          row['color'] = self.context.rptObj.theme.charts[i] if not 'color' in rec else rec['color']
        else:
          row = {"name": rec, "color": self.context.rptObj.theme.charts[i]}
        data.append(row)
    dfl_options = {"style": {"vertical-align": 'middle', "border-radius": '5px', 'width': '10px', 'height': '10px', 'display': 'inline-block', 'margin-right': '2px'}}
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if options is not None:
      dfl_options.update(options)
    html_legend = html.HtmlOthers.Legend(self.context.rptObj, data, width, height, align, dfl_options, profile)
    return html_legend

  def forecast(self, month_period, content=None, width=(100, "%"), height=(None, "px"), position="top", options=None, profile=None):
    """
    Description:
    ------------
    Display a forecast based on a dictionary containing the values for several months

    Usage::


    Related Pages:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py

    Attributes:
    ----------
    :param month_period: Integer. Number of months of forecast
    :param content:
    :param width:
    :param height:
    :param position:
    :param options:
    :param profile:
    """
    today = datetime.date.today()
    year = today.year
    row = []
    for i in range(month_period):
      next_month = today.month + i
      next_year = year
      if next_month > 11:
        next_year = year + (next_month // 11)
        next_month = next_month % 11
      calendar = self.context.rptObj.ui.calendars.days(next_month, content, next_year, width, height, None, options, profile=profile)
      if options.get("legend", True):
        row.append([calendar, self.context.rptObj.ui.calendars.legend(calendar.tasks)])
      else:
        row.append(calendar)
    return self.context.rptObj.ui.grid([row], position=position, profile=profile)

  def google(self, task, start, end, details=None, location=None, icon="fab fa-google-plus", text="Add to Google Calendar", options=None, profile=None):
    """
    Description:
    ------------
    Add link to the google calendar. Will add the event to the Calendar.

    Usage::

      page.ui.calendars.google("hrehr", "Test", "20200801T153000Z", "20200802T163000Z")

    Related Pages:

      https://stackoverflow.com/questions/5179760/add-events-to-google-calendar-yahoo-calendar-outlook-and-ical
    https://codepen.io/vlemoine/pen/MLwygX

    TODO: improve the time management in this component

    Attributes:
    ----------
    :param task:
    :param start: String. Date format YYYYMMDD
    :param end: String. Date format YYYYMMDD
    :param details:
    :param location:
    :param icon:
    :param text:
    :param options:
    :param profile:
    """
    icon = self.context.rptObj.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(5)
    icon.icon.style.css.color = self.context.rptObj.theme.greys[-1]
    icon.options.managed = False
    google_url = "http://www.google.com/calendar/event?action=TEMPLATE"
    link = self.context.rptObj.ui.link("%s %s" % (icon.html(), text),
      self.context.rptObj.js.objects.get("%(url)s&text=%(task)s&dates=%(start)s/%(end)s&details=%(details)s&location=%(location)s" % {'url': google_url, "task": task, 'start': start, 'end': end, 'details': details or task, 'location': location or ''}))
    link.style.css.background = self.context.rptObj.theme.greys[0]
    link.style.css.color = self.context.rptObj.theme.greys[-1]
    link.style.css.padding = '2px 5px'
    link.style.css.margin = 2
    link.style.css.display = 'inline-block'
    link.style.css.border = "1px solid %s" % self.context.rptObj.theme.greys[3]
    link.style.css.border_radius = 20
    return link

  def agenda(self, task, start, end, details=None, location=None, icon="far fa-calendar-alt", text="Add to Calendar", options=None, profile=None):
    """
    Description:
    ------------

    Usage::


    Related Pages:

      https://stackoverflow.com/questions/5179760/add-events-to-google-calendar-yahoo-calendar-outlook-and-ical
    https://codepen.io/vlemoine/pen/MLwygX

    TODO: improve the time management in this component

    Attributes:
    ----------
    :param task:
    :param start:
    :param end:
    :param details:
    :param location:
    :param icon:
    :param text:
    :param options:
    :param profile:
    """
    # Default options
    calendar_options = {'CALSCALE': 'GREGORIAN', 'VERSION': '2.0'}
    events_options = {'DTSTART;VALUE=DATE': start, 'DTEND;VALUE=DATE': end, 'SUMMARY': task or '', 'LOCATION': location or '',
                      'DESCRIPTION': details or '', 'STATUS': 'CONFIRMED', 'SEQUENCE': 3}

    str_calendar = "BEGIN:VCALENDAR\n%s\n%%s\nEND:VCALENDAR" % "\n".join(["%s:%s" % (k, v) for k, v in calendar_options.items()])
    str_event = "BEGIN:VEVENT\n%s\nEND:VEVENT"% "\n".join(["%s:%s" % (k, v) for k, v in events_options.items()])

    link = self.context.rptObj.ui.links.data("<i style='font-size:%s;color:%s' class='%s'></i> %s" % (Defaults.font(5), self.context.rptObj.theme.greys[-1], icon, text), str_calendar % str_event)
    link.attr['download'] = 'event.ics'
    link.style.css.background = self.context.rptObj.theme.greys[0]
    link.style.css.color = self.context.rptObj.theme.greys[-1]
    link.style.css.padding = '2px 5px'
    link.style.css.margin = 2
    link.style.css.display = 'inline-block'
    link.style.css.border = "1px solid %s" % self.context.rptObj.theme.greys[3]
    link.style.css.border_radius = 20
    return link

  def pill(self, text, value=None, group=None, width=("auto", ""), height=(None, "px"), htmlCode=None, tooltip=None, profile=None, options=None):
    but = self.context.rptObj.ui.text(text, width=width, height=height, htmlCode=htmlCode, tooltip=tooltip,
                                      profile=profile, options=options)
    but.style.css.background = self.context.rptObj.theme.greys[3]
    but.options.style_select = "pill_selected"
    but.style.css.border_radius = 20
    but.style.css.padding = "0 5px"
    but.style.css.margin_right = 5
    date = datetime.date.today()
    if value is None and text.endswith("M"):
      for i in range(int(text[:-1])):
        date = date - datetime.timedelta(days=date.day)
      value = date.isoformat()
    if value is None and text.endswith("Y"):
      date = datetime.date(date.year - int(text[:-1]), date.month, date.day)
      value = date.isoformat()
    but.attr["data-value"] = value or text
    but.style.add_classes.div.color_background_hover()
    if group is not None:
      self.context.rptObj.body.style.custom_class({
        "background": "%s !IMPORTANT" % self.context.rptObj.theme.colors[6],
        "color": "%s !IMPORTANT" % self.context.rptObj.theme.greys[0],
      }, classname="pill_selected")
      but.attr["data-group"] = group
    return but
