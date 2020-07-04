#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core import html
from epyk.core.css import Defaults


class Calendar(object):

  def __init__(self, context):
    self.context = context

  def days(self, month, content=None, year=None, width=(None, "%"), height=(None, "px"), align=None, options=None, htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param month:
    :param content:
    :param width:
    :param height:
    :param options:
    :param htmlCode:
    :param profile:
    """

    today = datetime.date.today()
    content = content or {}
    dfl_options = {
      'overload': {'font-size': Defaults.font(5), 'text-align': 'center', 'color': self.context.rptObj.theme.danger[1],
                   'font-weight': 'bold', 'cursor': 'pointer'},
      'number': {"font-size": Defaults.font(5), "text-align": "center"},
      'today': {"padding": "0 0 5px 0", "border-bottom": "1px solid grey"},
      'header': {'font-size': Defaults.font(3), "background": self.context.rptObj.theme.colors[-1],
                 "color": self.context.rptObj.theme.colors[0], "padding": "5px 2px", "text-align": "center"}
    }
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
        tasks_view.append({"name": t, 'capacity': day_tasks.get(t, 0), 'color': tasks[t]})
      days_data.append({'today': today == start, "number": start.day, 'tasks': tasks_view, 'date': start.isoformat(), 'weekend': start.weekday() >= 5})
      start += datetime.timedelta(days=1)
    html_table = html.HtmlDates.Calendar(self.context.rptObj, days_data, width, height, align, dfl_options, htmlCode, profile)
    html_table.tasks = tasks
    html_table.caption = "%s %s" % (datetime.date(year, month, 1).strftime("%B"), year)
    return html_table

  def months(self, year=None, content=None, width=(None, "%"), height=(None, "px"), align=None, options=None, htmlCode=None, profile=None):
    """
    Description:
    ------------

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
    dfl_options = {
      'overload': {'font-size': Defaults.font(5), 'text-align': 'center', 'color': self.context.rptObj.theme.danger[1],
                   'font-weight': 'bold', 'cursor': 'pointer'},
      'number': {"font-size": Defaults.font(5), "text-align": "center"},
      'today': {"padding": "0 0 5px 0", "border-bottom": "1px solid grey"},
      'header': {'font-size': Defaults.font(3), "background": self.context.rptObj.theme.colors[-1],
                 "color": self.context.rptObj.theme.colors[0], "padding": "5px 2px", "text-align": "center"}
    }
    if options is not None:
      dfl_options.update(options)
    days_data = []
    html_table = html.HtmlDates.Calendar(self.context.rptObj, days_data, width, height, align, dfl_options, htmlCode, profile)
    html_table.labels =["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October",
                        "November", "December"]
    return html_table

  def legend(self, records, width=(None, "%"), height=(None, "px"), align=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param records:
    :param width:
    :param height:
    :param align:
    :param options:
    :param profile:
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
    if options is not None:
      dfl_options.update(options)
    html_legend = html.HtmlOthers.Legend(self.context.rptObj, data, width, height, align, dfl_options, profile)
    return html_legend

  def forecast(self, month_period, content=None, width=(100, "%"), height=(None, "px"), poaition="top", options=None, profile=None):
    """
    Description:
    ------------
    Display a forecast based on a dictionary containing the values for several months

    Attributes:
    ----------
    :param month_period: Integer. Number of months of forecast
    :param content:
    :param width:
    :param height:
    :param poaition:
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
    return self.context.rptObj.ui.grid([row], position=poaition, profile=profile)
