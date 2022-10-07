#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class Calendar(JsPackage):

  def __init__(self, component, js_code=None, set_var=True, is_py_data=True, page: primitives.PageModel = None):
    self.varName, self.varData, self.__var_def = js_code, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def changeView(self, new_view_name: str, force):
    """   Change current view with view name('day', 'week', 'month')

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#changeView

    :param str new_view_name: The New view name to render.
    :param force: Boolean. Force render despite of current view and new view are equal.
    """
    new_view_name = JsUtils.jsConvertData(new_view_name, None)
    force = JsUtils.jsConvertData(force, None)
    return JsUtils.jsWrap("%s.changeView(%s, %s)" % (self.component.var, new_view_name, force))

  def clear(self, immediately=False):
    """   Delete all schedules and clear view. The real rendering occurs after requestAnimationFrame.
    If you have to render immediately, use the 'immediately' parameter as true.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#clear

    :param immediately: Boolean. Optional. Render it immediately.
    """
    immediately = JsUtils.jsConvertData(immediately, None)
    return JsUtils.jsWrap("%s.clear(%s)" % (self.component.var, immediately))

  def createSchedules(self, schedules, silent=False):
    """   Create schedules and render calendar.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#createSchedules

    :param schedules: Array. Schedule data list.
    :param silent: Boolean. Optional. No auto render after creation when set true.
    """
    schedules = JsUtils.jsConvertData(schedules, None)
    silent = JsUtils.jsConvertData(silent, None)
    return JsUtils.jsWrap("%s.createSchedules(%s, %s)" % (self.component.var, schedules, silent))

  def deleteSchedule(self, schedule_id: str, calendar_id: str, silent: bool = False):
    """   Delete a schedule.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#deleteSchedule

    :param str schedule_id: ID of schedule to delete.
    :param str calendar_id: The CalendarId of the schedule to delete.
    :param bool silent: Optional. No auto render after creation when set true.
    """
    schedule_id = JsUtils.jsConvertData(schedule_id, None)
    calendar_id = JsUtils.jsConvertData(calendar_id, None)
    silent = JsUtils.jsConvertData(silent, None)
    return JsUtils.jsWrap("%s.deleteSchedule(%s, %s, %s)" % (self.component.var, schedule_id, calendar_id, silent))

  def destroy(self):
    """   destroy calendar instance.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#destroy
    """
    return JsUtils.jsWrap("%s.destroy()" % self.component.var)

  def getDate(self):
    """   Current rendered date (TZDate for further information)

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getDate
    """
    return JsUtils.jsWrap("%s.getDate()" % self.component.var)

  def getDateRangeEnd(self):
    """   End time of rendered date range (TZDate for further information)

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getDateRangeEnd
    """
    return JsUtils.jsWrap("%s.getDateRangeEnd()" % self.component.var)

  def getDateRangeStart(self):
    """   Start time of rendered date range (TZDate for further information)

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getDateRangeStart
    """
    return JsUtils.jsWrap("%s.getDateRangeStart()" % self.component.var)

  def getElement(self, schedule_id: str, calendar_id: str):
    """   

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getElement

    :param str schedule_id: ID of schedule.
    :param str calendar_id: calendarId of schedule.
    """
    schedule_id = JsUtils.jsConvertData(schedule_id, None)
    calendar_id = JsUtils.jsConvertData(calendar_id, None)
    return JsUtils.jsWrap("%s.getElement(%s, %s)" % (self.component.var, schedule_id, calendar_id))

  def getOptions(self):
    """   Get current Options.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getOptions
    """
    return JsUtils.jsWrap("%s.getOptions()" % self.component.var)

  def getSchedule(self, schedule_id: str, calendar_id: str):
    """   Get a Schedule object by schedule id and calendar id.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getSchedule

    :param str schedule_id: ID of schedule.
    :param str calendar_id: calendarId of the schedule.
    """
    schedule_id = JsUtils.jsConvertData(schedule_id, None)
    calendar_id = JsUtils.jsConvertData(calendar_id, None)
    return JsUtils.jsWrap("%s.getSchedule(%s, %s)" % (self.component.var, schedule_id, calendar_id))

  def getViewName(self):
    """   Get current view name('day', 'week', 'month')

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getViewName
    """
    return JsObjects.JsString.JsString.get("%s.getViewName()" % self.component.var)

  def hideMoreView(self):
    """   Hide the more view.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#hideMoreView
    """
    return JsUtils.jsWrap("%s.hideMoreView()" % self.component.var)

  def next(self):
    """   Move the calendar forward a day, a week, a month, 2 weeks, 3 weeks.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#next
    """
    return JsUtils.jsWrap("%s.next()" % self.component.var)

  def openCreationPopup(self, schedule):
    """   Open schedule creation popup

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#openCreationPopup

    :param schedule: Schedule. The preset Schedule data.
    """
    schedule = JsUtils.jsConvertData(schedule, None)
    return JsUtils.jsWrap("%s.openCreationPopup(%s)" % (self.component.var, schedule))

  def prev(self):
    """   Move the calendar backward a day, a week, a month, 2 weeks, 3 weeks.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#prev
    """
    return JsUtils.jsWrap("%s.prev()" % self.component.var)

  def render(self, immediately=False):
    """   Render the calendar. The real rendering occurs after requestAnimationFrame.
    If you have to render immediately, use the 'immediately' parameter as true.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#render

    :param immediately: Boolean. Optional. Render it immediately.
    """
    immediately = JsUtils.jsConvertData(immediately, None)
    return JsUtils.jsWrap("%s.render(%s)" % (self.component.var, immediately))

  def scrollToNow(self):
    """   Scroll to current time on today in case of daily, weekly view

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#scrollToNow
    """
    return JsUtils.jsWrap("%s.scrollToNow()" % self.component.var)
