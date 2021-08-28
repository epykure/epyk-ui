#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class Calendar(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.varName, self.varData, self.__var_def = varName, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def changeView(self, newViewName, force):
    """
    Description:
    -----------
    Change current view with view name('day', 'week', 'month')

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#changeView

    Attributes:
    ----------
    :param newViewName: String. The New view name to render.
    :param force: Boolean. Force render despite of current view and new view are equal.
    """
    newViewName = JsUtils.jsConvertData(newViewName, None)
    force = JsUtils.jsConvertData(force, None)
    return JsUtils.jsWrap("%s.changeView(%s, %s)" % (self._src.var, newViewName, force))

  def clear(self, immediately=False):
    """
    Description:
    -----------
    Delete all schedules and clear view. The real rendering occurs after requestAnimationFrame.
    If you have to render immediately, use the 'immediately' parameter as true.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#clear

    Attributes:
    ----------
    :param immediately: Boolean. Optional. Render it immediately.
    """
    immediately = JsUtils.jsConvertData(immediately, None)
    return JsUtils.jsWrap("%s.clear(%s)" % (self._src.var, immediately))

  def createSchedules(self, schedules, silent=False):
    """
    Description:
    -----------
    Create schedules and render calendar.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#createSchedules

    Attributes:
    ----------
    :param schedules: Array. Schedule data list.
    :param silent: Boolean. Optional. No auto render after creation when set true.
    """
    schedules = JsUtils.jsConvertData(schedules, None)
    silent = JsUtils.jsConvertData(silent, None)
    return JsUtils.jsWrap("%s.createSchedules(%s, %s)" % (self._src.var, schedules, silent))

  def deleteSchedule(self, scheduleId, calendarId, silent=False):
    """
    Description:
    -----------
    Delete a schedule.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#deleteSchedule

    Attributes:
    ----------
    :param scheduleId: String. ID of schedule to delete.
    :param calendarId: String. The CalendarId of the schedule to delete.
    :param silent: Boolean. Optional. No auto render after creation when set true.
    """
    scheduleId = JsUtils.jsConvertData(scheduleId, None)
    calendarId = JsUtils.jsConvertData(calendarId, None)
    silent = JsUtils.jsConvertData(silent, None)
    return JsUtils.jsWrap("%s.deleteSchedule(%s, %s, %s)" % (self._src.var, scheduleId, calendarId, silent))

  def destroy(self):
    """
    Description:
    -----------
    destroy calendar instance.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#destroy
    """
    return JsUtils.jsWrap("%s.destroy()" % self._src.var)

  def getDate(self):
    """
    Description:
    -----------
    Current rendered date (TZDate for further information)

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getDate
    """
    return JsUtils.jsWrap("%s.getDate()" % self._src.var)

  def getDateRangeEnd(self):
    """
    Description:
    -----------
    End time of rendered date range (TZDate for further information)

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getDateRangeEnd
    """
    return JsUtils.jsWrap("%s.getDateRangeEnd()" % self._src.var)

  def getDateRangeStart(self):
    """
    Description:
    -----------
    Start time of rendered date range (TZDate for further information)

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getDateRangeStart
    """
    return JsUtils.jsWrap("%s.getDateRangeStart()" % self._src.var)

  def getElement(self, scheduleId, calendarId):
    """
    Description:
    -----------

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getElement

    Attributes:
    ----------
    :param scheduleId: String. ID of schedule.
    :param calendarId: String. calendarId of schedule.
    """
    scheduleId = JsUtils.jsConvertData(scheduleId, None)
    calendarId = JsUtils.jsConvertData(calendarId, None)
    return JsUtils.jsWrap("%s.getElement(%s, %s)" % (self._src.var, scheduleId, calendarId))

  def getOptions(self):
    """
    Description:
    -----------
    Get current Options.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getOptions
    """
    return JsUtils.jsWrap("%s.getOptions()" % self._src.var)

  def getSchedule(self, scheduleId, calendarI):
    """
    Description:
    -----------
    Get a Schedule object by schedule id and calendar id.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getSchedule

    Attributes:
    ----------
    :param scheduleId: String. ID of schedule.
    :param calendarI: String. calendarId of the schedule.
    """
    scheduleId = JsUtils.jsConvertData(scheduleId, None)
    calendarI = JsUtils.jsConvertData(calendarI, None)
    return JsUtils.jsWrap("%s.getSchedule(%s, %s)" % (self._src.var, scheduleId, calendarI))

  def getViewName(self):
    """
    Description:
    -----------
    Get current view name('day', 'week', 'month')

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#getViewName
    """
    return JsObjects.JsString.JsString.get("%s.getViewName()" % self._src.var)

  def hideMoreView(self):
    """
    Description:
    -----------
    Hide the more view.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#hideMoreView
    """
    return JsUtils.jsWrap("%s.hideMoreView()" % self._src.var)

  def next(self):
    """
    Description:
    -----------
    Move the calendar forward a day, a week, a month, 2 weeks, 3 weeks.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#next
    """
    return JsUtils.jsWrap("%s.next()" % self._src.var)

  def openCreationPopup(self, schedule):
    """
    Description:
    -----------
    Open schedule creation popup

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#openCreationPopup

    Attributes:
    ----------
    :param schedule: Schedule. The preset Schedule data.
    """
    schedule = JsUtils.jsConvertData(schedule, None)
    return JsUtils.jsWrap("%s.openCreationPopup(%s)" % (self._src.var, schedule))

  def prev(self):
    """
    Description:
    -----------
    Move the calendar backward a day, a week, a month, 2 weeks, 3 weeks.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#prev
    """
    return JsUtils.jsWrap("%s.prev()" % self._src.var)

  def render(self, immediately=False):
    """
    Description:
    -----------
    Render the calendar. The real rendering occurs after requestAnimationFrame.
    If you have to render immediately, use the 'immediately' parameter as true.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#render

    Attributes:
    ----------
    :param immediately: Boolean. Optional. Render it immediately.
    """
    immediately = JsUtils.jsConvertData(immediately, None)
    return JsUtils.jsWrap("%s.render(%s)" % (self._src.var, immediately))

  def scrollToNow(self):
    """
    Description:
    -----------
    Scroll to current time on today in case of daily, weekly view

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar#scrollToNow
    """
    return JsUtils.jsWrap("%s.scrollToNow()" % self._src.var)
