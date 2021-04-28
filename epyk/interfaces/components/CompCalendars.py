#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core import html
from epyk.interfaces import Arguments


class Calendar:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def days(self, month=None, content=None, year=None, width=(None, "%"), height=(None, "px"), align=None, options=None,
           html_code=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      content = {
        "2020-07-02": {'task1': 50, 'task2': 50},
        "2020-07-03": {'task1': 100},
        "2020-07-21": {'task4': 100},
        "2020-07-22": {'task4': 100}
      }

      july = page.ui.calendars.days(7, content, align="center", options={"colors": {"task4": 'red'}})
      july.task('task1', start="2020-07-10", capacity=[50, 30, 10, 80])
      july.task('task4', start="2020-07-20", capacity=[50, 40, 10])
      july.weekly("task6", start="2020-07-02", capacity=3, frequency=2, options={'unit': 8})

    Templates:

    Related Pages:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py

    Attributes:
    ----------
    :param month: Integer. Optional. The month number.
    :param content:
    :param year:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    today = datetime.date.today()
    month = month or today.month
    content = content or {}
    dfl_options = {
      'overload': {'font-size': self.page.body.style.globals.font.normal(5), 'text-align': 'center',
                   'color': self.page.theme.danger[1],
                   'font-weight': 'bold', 'cursor': 'pointer'},
      'number': {"font-size": self.page.body.style.globals.font.normal(5), "text-align": "center"},
      'today': {"padding": "0 0 5px 0", "border-bottom": "1px solid grey"},
      'header': {'font-size': self.page.body.style.globals.font.normal(3), "background": self.page.theme.colors[-1],
                 "color": self.page.theme.colors[0], "padding": "5px 2px", "text-align": "center"}
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
      tasks[t] = dfl_options.get('colors', {}).get(t, self.page.theme.charts[i])
    for _ in range(start.weekday() + 1):
      days_data.append({})
    while start.month == month:
      day_tasks = content.get(start.isoformat(), {})
      tasks_view = []
      for i, t in enumerate(sorted_tasks):
        tasks_view.append({"name": t, 'capacity': factor * day_tasks.get(t, 0), 'color': tasks[t]})
      days_data.append({'today': today == start, "number": start.day, 'tasks': tasks_view, 'date': start.isoformat(),
                        'weekend': start.weekday() >= 5})
      start += datetime.timedelta(days=1)
    html_table = html.HtmlDates.Calendar(
      self.page, days_data, width, height, align, dfl_options, html_code, profile)
    html_table.tasks = tasks
    html_table.caption = "%s %s" % (datetime.date(year, month, 1).strftime("%B"), year)
    return html_table

  @html.Html.css_skin()
  def timer(self, minutes, text="", width=(None, "%"), height=(None, "px"), align=None, options=None, html_code=None,
            profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
    :param minutes:
    :param text: String. Optional. The value to be displayed to the timer
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param align: String. The text-align property within this component
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_timer = html.HtmlDates.Timer(self.page, minutes, text, width, height, align, options, html_code, profile)
    return html_timer

  @html.Html.css_skin()
  def months(self, content=None, width=(None, "%"), height=(None, "px"), align=None, options=None,
             html_code=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

        records = {
          1: {"Project 1": 12, "Project 2": 30},
          2: {"Project 1": 12, "Project 2": 30},
          3: {"Project 1": 42, "Project 2": 30},
          4: {"Project 1": 15, "Project 2": 30},
          5: {"Project 1": 12, "Project 2": 30},
          6: {"Project 1": 12, "Project 2": 30},
          7: {"Project 1": 12, "Project 2": 30},
        }

        monthly = page.ui.calendars.months(content=records, align="center")

    Templates:

    Related Pages:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py

    Attributes:
    ----------
    :param content: Dictionary. Optional. The Pie charts values.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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
        tasks[k] = self.page.theme.charts[j]
      html_code_chart = "%s_%s" % (html_code, i) if html_code is not None else html_code
      pie = self.page.ui.charts.chartJs.pie(
        record, y_columns=["capacity"], x_axis="name", html_code=html_code_chart, height=(150, "px"), options=options,
        profile=profile)
      pie.options.legend.display = False
      pie.options.title.text = labels[i]
      pie.options.title.display = True
      pie.options.title.fontSize = self.page.body.style.globals.font.normal(5)
      pie.options.title.fontColor = self.page.theme.colors[-1]
      rows.append(pie)
    row = self.page.ui.row(rows, width=width, height=height, align=align, options=options, profile=profile)
    row.tasks = tasks
    row.pies = rows
    row[today.month-1].style.css.border = "1px solid %s" % self.page.theme.success[0]
    return row

  @html.Html.css_skin()
  def legend(self, record, width=(None, "%"), height=(None, "px"), align=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a legend to a Calendar component.

    :tags:
    :categories:

    Usage::

        monthly = page.ui.calendars.months(content=records, align="center")
        page.ui.calendars.legend(monthly.tasks)

    Templates:

    Related Pages:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The text-align property within this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    data = []
    if isinstance(record, dict):
      for k, v in record.items():
        data.append({"name": k, "color": v})
    else:
      for i, rec in enumerate(record):
        if isinstance(rec, dict):
          row = dict(rec)
          row['color'] = self.page.theme.charts[i] if 'color' not in rec else rec['color']
        else:
          row = {"name": rec, "color": self.page.theme.charts[i]}
        data.append(row)
    dfl_options = {"style": {"vertical-align": 'middle', "border-radius": '5px', 'width': '10px', 'height': '10px',
                             'display': 'inline-block', 'margin-right': '2px'}}
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if options is not None:
      dfl_options.update(options)
    html_legend = html.HtmlOthers.Legend(self.page, data, width, height, dfl_options, profile)
    return html_legend

  @html.Html.css_skin()
  def forecast(self, month_period, content=None, width=(100, "%"), height=(None, "px"), position="top", options=None,
               profile=None):
    """
    Description:
    ------------
    Display a forecast based on a dictionary containing the values for several months

    Usage::

    :tags:
    :categories:

    Templates:

    Related Pages:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py

    Attributes:
    ----------
    :param month_period: Integer. Number of months of forecast.
    :param content: String. Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param position: String. Optional. The position compared to the main component tag.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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
      calendar = self.page.ui.calendars.days(
        next_month, content, next_year, width, height, None, options, profile=profile)
      if options.get("legend", True):
        row.append([calendar, self.page.ui.calendars.legend(calendar.tasks)])
      else:
        row.append(calendar)
    return self.page.ui.grid([row], position=position, profile=profile)

  @html.Html.css_skin()
  def google(self, task, start, end, details=None, location=None, icon="fab fa-google-plus",
             text="Add to Google Calendar", options=None, profile=None):
    """
    Description:
    ------------
    Add link to the google calendar. Will add the event to the Calendar.

    Usage::

      page.ui.calendars.google("hrehr", "Test", "20200801T153000Z", "20200802T163000Z")

    Templates:

    :tags:
    :categories:

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
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param text: String. Optional. The value to be displayed to the button.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    icon = self.page.ui.icons.awesome(icon, options=options, profile=profile)
    icon.icon.style.css.font_factor(5)
    icon.icon.style.css.color = self.page.theme.greys[-1]
    icon.options.managed = False
    google_url = "http://www.google.com/calendar/event?action=TEMPLATE"
    link = self.page.ui.link("%s %s" % (icon.html(), text),
      self.page.js.objects.get("%(url)s&text=%(task)s&dates=%(start)s/%(end)s&details=%(details)s&location=%(location)s" % {'url': google_url, "task": task, 'start': start, 'end': end, 'details': details or task, 'location': location or ''}))
    link.style.css.background = self.page.theme.greys[0]
    link.style.css.color = self.page.theme.greys[-1]
    link.style.css.padding = '2px 5px'
    link.style.css.margin = 2
    link.style.css.display = 'inline-block'
    link.style.css.border = "1px solid %s" % self.page.theme.greys[3]
    link.style.css.border_radius = 20
    return link

  @html.Html.css_skin()
  def agenda(self, task, start, end, details=None, location=None, icon="far fa-calendar-alt", text="Add to Calendar",
             options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    :tags:
    :categories:

    Templates:

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
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param text: String. Optional. The value to be displayed to the button.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    # Default options
    calendar_options = {'CALSCALE': 'GREGORIAN', 'VERSION': '2.0'}
    events_options = {'DTSTART;VALUE=DATE': start, 'DTEND;VALUE=DATE': end, 'SUMMARY': task or '', 'LOCATION': location or '',
                      'DESCRIPTION': details or '', 'STATUS': 'CONFIRMED', 'SEQUENCE': 3}

    str_calendar = "BEGIN:VCALENDAR\n%s\n%%s\nEND:VCALENDAR" % "\n".join(["%s:%s" % (k, v) for k, v in calendar_options.items()])
    str_event = "BEGIN:VEVENT\n%s\nEND:VEVENT"% "\n".join(["%s:%s" % (k, v) for k, v in events_options.items()])

    link = self.page.ui.links.data("<i style='font-size:%s;color:%s' class='%s'></i> %s" % (
      self.page.body.style.globals.font.normal(5), self.page.theme.greys[-1], icon, text), str_calendar % str_event,
                                   options=options, profile=profile)
    link.attr['download'] = 'event.ics'
    link.style.css.background = self.page.theme.greys[0]
    link.style.css.color = self.page.theme.greys[-1]
    link.style.css.padding = '2px 5px'
    link.style.css.margin = 2
    link.style.css.display = 'inline-block'
    link.style.css.border = "1px solid %s" % self.page.theme.greys[3]
    link.style.css.border_radius = 20
    return link

  @html.Html.css_skin()
  def pill(self, text, value=None, group=None, width=("auto", ""), height=(None, "px"), html_code=None, tooltip=None,
           profile=None, options=None):
    """
    Description:
    ------------

    Usage::

      pill = page.ui.calendars.pill("4D")
      page.ui.button("Click").click([page.js.alert(pill.dom.content)])

    Templates:

    :tags:
    :categories:

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param value:
    :param group:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    but = self.page.ui.text(
      text, width=width, height=height, html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    but.style.css.background = self.page.theme.greys[3]
    but.options.style_select = "pill_selected"
    but.style.css.border_radius = 20
    but.style.css.padding = "0 5px"
    but.style.css.margin_right = 5
    date = datetime.date.today()
    if value is None and text.endswith("D"):
      date = date - datetime.timedelta(days=int(text[:-1]))
      value = date.isoformat()
    elif value is None and text.endswith("W"):
      date = date - datetime.timedelta(days=7 * int(text[:-1]))
      value = date.isoformat()
    elif value is None and text.endswith("M"):
      for i in range(int(text[:-1])):
        date = date - datetime.timedelta(days=date.day)
      value = date.isoformat()
    elif value is None and text.endswith("Y"):
      date = datetime.date(date.year - int(text[:-1]), date.month, date.day)
      value = date.isoformat()
    but.attr["data-value"] = value or text
    but.style.add_classes.div.color_background_hover()
    if group is not None:
      self.page.body.style.custom_class({
        "background": "%s !IMPORTANT" % self.page.theme.colors[6],
        "color": "%s !IMPORTANT" % self.page.theme.greys[0],
      }, classname="pill_selected")
      but.attr["data-group"] = group
    return but
