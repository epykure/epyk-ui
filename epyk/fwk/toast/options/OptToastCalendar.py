
from epyk.core.html.options import Options
from epyk.core.html.options import Enums
from epyk.core.js import JsUtils


class EnumDates(Enums):

  def today(self):
    """
    Description:
    ------------
    Set the today date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/tutorial-example08-daterangepicker
    """
    self._set_value(js_type=True)

  def current(self):
    """
    Description:
    ------------
    Set the today date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/tutorial-example08-daterangepicker
    """
    self._set_value(value="new Date()", js_type=True)

  def previous(self, n=1):
    """
    Description:
    ------------
    Set the today date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/tutorial-example08-daterangepicker
    """
    self._set_value(value="(function(){var dt = new Date(); dt.setDate(dt.getDate() - %s); return dt})()" % n, js_type=True)

  def cob(self):
    """
    Description:
    ------------
    Set the today date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/tutorial-example08-daterangepicker
    """
    self._set_value(value="(function(){var cob = new Date(); var days = cob.getDay(); if(days == 1){cob.setDate(cob.getDate() - 3)} else { cob.setDate(cob.getDate() - 1)}; return cob})()", js_type=True)


class EnumViews(Enums):
  def week(self):
    """
    Description:
    ------------
    Set the calendar view type.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    self._set_value()

  def month(self):
    """
    Description:
    ------------
    Set the calendar view type.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    self._set_value()

  def day(self):
    """
    Description:
    ------------
    Set the calendar view type.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    self._set_value()


class EnumTaskViews(Enums):

  def milestone(self):
    """
    Description:
    ------------
    Set the calendar task view type.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    self._set_value()

  def task(self):
    """
    Description:
    ------------
    Set the calendar task view type.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    self._set_value()

  def true(self):
    """
    Description:
    ------------
    Set the calendar task view type.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    self._set_value(js_type=True)


class EnumScheduleViews(Enums):

  def allday(self):
    """
    Description:
    ------------
    Set the calendar task view type.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    self._set_value()

  def time(self):
    """
    Description:
    ------------
    Set the calendar task view type.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    self._set_value()

  def true(self):
    """
    Description:
    ------------
    Set the calendar task view type.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    self._set_value(js_type=True)


class OptionDateInput(Options):

  @property
  def element(self):
    """
    Description:
    ------------
    """
    return self._config_get("")

  @element.setter
  def element(self, val):
    self._config(val)

  @property
  def format(self):
    """
    Description:
    ------------
    """
    return self._config_get("yyyy-MM-dd")

  @format.setter
  def format(self, val):
    self._config(val)


class EnumStyleDateTypes(Enums):

  def date(self):
    """
    Description:
    ------------
    DatePicker type. Determine whether to choose a date, month, or year.

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    self._set_value()

  def month(self):
    """
    Description:
    ------------
    DatePicker type. Determine whether to choose a date, month, or year.

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    self._set_value()

  def year(self):
    """
    Description:
    ------------
    DatePicker type. Determine whether to choose a date, month, or year.

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    self._set_value()


class OptionDate(Options):
  component_properties = ("usageStatistics",)

  @property
  def calendar(self):
    """
    Description:
    ------------
    Calendar options. Refer to the Calendar instance's options.

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
      http://nhn.github.io/tui.date-picker/latest/DateRangePicker
    """
    return self._config_get()

  @calendar.setter
  def calendar(self, val):
    self._config(val)

  @property
  def date(self):
    """
    Description:
    ------------
    Initial date. Set by a Date instance or a number(timestamp). (default: no initial date).

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    return self._config_get("")

  @date.setter
  def date(self, val):
    year, month, day = val.split("-")
    self._config("new Date(%s, %s-1, %s)" % (year, month, day), js_type=True)

  @property
  def dates(self):
    """
    Description:
    ------------
    Initial date of the start picker. Set by a Date instance or a number(timestamp). (default: no initial date).

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DateRangePicker
    """
    return EnumDates(self, "date")

  @property
  def defaultView(self):
    """
    Description:
    ------------
    """
    return self._config_get("")

  @defaultView.setter
  def defaultView(self, val):
    self._config(val)

  @property
  def type(self):
    """
    Description:
    ------------
    DatePicker type. Determine whether to choose a date, month, or year.

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    return self._config_get("")

  @type.setter
  def type(self, val):
    self._config(val)

  @property
  def timePicker(self):
    """
    Description:
    ------------
    TimePicker options. Refer to the TimePicker instance's options. To create the TimePicker without customization,
    set to true.

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
      http://nhn.github.io/tui.date-picker/latest/DateRangePicker
    """
    return self._config_get()

  @timePicker.setter
  def timePicker(self, val):
    self._config(val)

  @property
  def types(self):
    return EnumStyleDateTypes(self, "type")

  @property
  def language(self):
    """
    Description:
    ------------
    Language code. English('en') and Korean('ko') are provided as default. To set to the other languages,
    use DatePicker.localeTexts.

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    return self._config_get("en")

  @language.setter
  def language(self, val):
    self._config(val)

  @property
  def input(self):
    """
    Description:
    ------------

    Related Pages:

      https://ui.toast.com/tui-date-picker

    :rtype: OptionDateInput
    """
    return self._config_sub_data("input", OptionDateInput)

  @property
  def selectableRanges(self):
    """
    Description:
    ------------
    Ranges of selectable date. Set by Date instances or numbers(timestamp).

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    return self._config_get()

  @selectableRanges.setter
  def selectableRanges(self, val):
    self._config(val)

  @property
  def openers(self):
    """
    Description:
    ------------
    List of the openers to open the DatePicker (example - icon, button, etc.).

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    return self._config_get()

  @openers.setter
  def openers(self, val):
    self._config(val)

  @property
  def showAlways(self):
    """
    Description:
    ------------
    Show the DatePicker always.

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    return self._config_get(False)

  @showAlways.setter
  def showAlways(self, val):
    self._config(val)

  @property
  def autoClose(self):
    """
    Description:
    ------------
    Close the DatePicker after clicking the date.

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    return self._config_get(True)

  @autoClose.setter
  def autoClose(self, val):
    self._config(val)

  @property
  def usageStatistics(self):
    """
    Description:
    ------------
    Send a hostname to Google Analytics (default: true).

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    return self._config_get(False)

  @usageStatistics.setter
  def usageStatistics(self, val):
    self._config(val)

  @property
  def weekStartDay(self):
    """
    Description:
    ------------
    Start of the week. 'Sun', 'Mon', ..., 'Sat'(default: 'Sun'(start on Sunday)).

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    return self._config_get('Sun')

  @weekStartDay.setter
  def weekStartDay(self, val):
    self._config(val)

  @property
  def showToday(self):
    """
    Description:
    ------------

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    return self._config_get(True)

  @showToday.setter
  def showToday(self, val):
    self._config(val)

  @property
  def showJumpButtons(self):
    """
    Description:
    ------------

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DatePicker
    """
    return self._config_get(False)

  @showJumpButtons.setter
  def showJumpButtons(self, val):
    self._config(val)


class OptionDateRangePicker(Options):
  @property
  def input(self):
    """
    Description:
    ------------
    Startpicker input element or selector.

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DateRangePicker
    """
    return self._config_get()

  @input.setter
  def input(self, val):
    self._config(val)

  @property
  def container(self):
    """
    Description:
    ------------
    Startpicker container element or selector.

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DateRangePicker
    """
    return self._config_get()

  @container.setter
  def container(self, val):
    self._config(val)

  @property
  def date(self):
    """
    Description:
    ------------
    Initial date of the start picker. Set by a Date instance or a number(timestamp). (default: no initial date).

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DateRangePicker
    """
    return self._config_get()

  @date.setter
  def date(self, val):
    self._config(val)

  @property
  def dates(self):
    """
    Description:
    ------------
    Initial date of the start picker. Set by a Date instance or a number(timestamp). (default: no initial date).

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DateRangePicker
    """
    return EnumDates(self, "date")

  @property
  def weekStartDay(self):
    """
    Description:
    ------------
    Start of the week. 'Sun', 'Mon', ..., 'Sat'(default: 'Sun'(start on Sunday)).

    Related Pages:

      http://nhn.github.io/tui.date-picker/latest/DateRangePicker
    """
    return self._config_get("Sun")

  @weekStartDay.setter
  def weekStartDay(self, val):
    self._config(val)


class OptionDateRange(OptionDate):

  @property
  def startpicker(self):
    """

    http://nhn.github.io/tui.date-picker/latest/DateRangePicker

    :rtype: OptionDateRangePicker
    """
    return self._config_sub_data("startpicker", OptionDateRangePicker)

  @property
  def endpicker(self):
    """

    http://nhn.github.io/tui.date-picker/latest/DateRangePicker

    :rtype: OptionDateRangePicker
    """
    return self._config_sub_data("endpicker", OptionDateRangePicker)


class OptionsCalMonth(Options):

  @property
  def daynames(self):
    """
    Description:
    ------------
    The day names in monthly. Default values are 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/MonthOptions
    """
    return self._config_get()

  @daynames.setter
  def daynames(self, values):
    self._config(values)

  @property
  def startDayOfWeek(self):
    """
    Description:
    ------------
    The start day of week.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/MonthOptions
    """
    return self._config_get(0)

  @startDayOfWeek.setter
  def startDayOfWeek(self, num):
    self._config(num)

  @property
  def narrowWeekend(self):
    """
    Description:
    ------------
    Make weekend column narrow(1/2 width).

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/MonthOptions
    """
    return self._config_get(True)

  @narrowWeekend.setter
  def narrowWeekend(self, flag):
    self._config(flag)

  @property
  def visibleWeeksCount(self):
    """
    Description:
    ------------
    The visible week count in monthly(0 or null are same with 6).

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/MonthOptions
    """
    return self._config_get(0)

  @visibleWeeksCount.setter
  def visibleWeeksCount(self, num):
    self._config(num)

  @property
  def isAlways6Week(self):
    """
    Description:
    ------------
    Always show 6 weeks. If false, show 5 weeks or 6 weeks based on the month..

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/MonthOptions
    """
    return self._config_get(0)

  @isAlways6Week.setter
  def isAlways6Week(self, flag):
    self._config(flag)

  @property
  def workweek(self):
    """
    Description:
    ------------
    Show only 5 days except for weekend.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/MonthOptions
    """
    return self._config_get(False)

  @workweek.setter
  def workweek(self, flag):
    self._config(flag)

  @property
  def visibleScheduleCount(self):
    """
    Description:
    ------------
    The visible schedule count in monthly grid.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/MonthOptions
    """
    return self._config_get()

  @visibleScheduleCount.setter
  def visibleScheduleCount(self, num):
    self._config(num)

  @property
  def moreLayerSize(self):
    """
    Description:
    ------------
    The more layer size.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/MonthOptions
    """
    return self._config_get()

  @moreLayerSize.setter
  def moreLayerSize(self, value):
    self._config(value)

  @property
  def grid(self):
    """
    Description:
    ------------
    The grid's header and footer information.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/MonthOptions
    """
    return self._config_get()

  @grid.setter
  def grid(self, value):
    self._config(value)

  def scheduleFilter(self, jsFuncs, profile):
    """

    :param jsFuncs:
    :param profile:
    """
    self._config("function (value){%s}" % JsUtils.jsConvertFncs(jsFuncs, toStr=True, profile=profile), js_type=True)


class OptionCalendars(Options):

  @property
  def id(self):
    """
    Description:
    ------------
    The calendar id.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/CalendarProps
    """
    return self._config_get()

  @id.setter
  def id(self, value):
    self._config(value)

  @property
  def name(self):
    """
    Description:
    ------------
    The calendar name.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/CalendarProps
    """
    return self._config_get()

  @name.setter
  def name(self, text):
    self._config(text)

  @property
  def color(self):
    """
    Description:
    ------------
    The text color when schedule is displayed.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/CalendarProps
    """
    return self._config_get()

  @color.setter
  def color(self, text):
    self._config(text)

  @property
  def bgColor(self):
    """
    Description:
    ------------
    The background color schedule is displayed.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/CalendarProps
    """
    return self._config_get()

  @bgColor.setter
  def bgColor(self, text):
    self._config(text)

  @property
  def borderColor(self):
    """
    Description:
    ------------
    The color of left border or bullet point when schedule is displayed.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/CalendarProps
    """
    return self._config_get()

  @borderColor.setter
  def borderColor(self, text):
    self._config(text)

  @property
  def dragBgColor(self):
    """
    Description:
    ------------
    The background color when schedule dragging

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/CalendarProps
    """
    return self._config_get()

  @dragBgColor.setter
  def dragBgColor(self, text):
    self._config(text)


class OptionCalendar(Options):

  @property
  def defaultView(self):
    """
    Description:
    ------------
    """
    return self._config_get("")

  @defaultView.setter
  def defaultView(self, val):
    self._config(val)

  @property
  def defaultViews(self):
    """
    Description:
    ------------
    Initial date of the start picker. Set by a Date instance or a number(timestamp). (default: no initial date).

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar

    :rtype: defaultView
    """
    return EnumViews(self, "defaultView")

  @property
  def taskView(self):
    """
    Description:
    ------------
    """
    return self._config_get("")

  @taskView.setter
  def taskView(self, val):
    self._config(val)

  @property
  def taskViews(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    return EnumTaskViews(self, "taskView")

  @property
  def scheduleView(self):
    """
    Description:
    ------------
    """
    return self._config_get("")

  @scheduleView.setter
  def scheduleView(self, val):
    self._config(val)

  @property
  def scheduleViews(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    return EnumScheduleViews(self, "scheduleView")

  @property
  def month(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Options

    :rtype: OptionsCalMonth
    """
    return self._config_sub_data("month", OptionsCalMonth)

  @property
  def week(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Options

    :rtype: OptionsCalMonth
    """
    return self._config_sub_data("week", OptionsCalMonth)

  @property
  def useCreationPopup(self):
    """
    Description:
    ------------
    Whether use default creation popup or not. The default value is false.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    return self._config_get(False)

  @useCreationPopup.setter
  def useCreationPopup(self, flag):
    self._config(flag)

  @property
  def useDetailPopup(self):
    """
    Description:
    ------------
    Whether use default detail popup or not. The default value is false.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    return self._config_get(False)

  @useDetailPopup.setter
  def useDetailPopup(self, flag):
    self._config(flag)

  @property
  def disableDblClick(self):
    """
    Description:
    ------------
    Disable double click to create a schedule. The default value is false.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    return self._config_get(False)

  @disableDblClick.setter
  def disableDblClick(self, flag):
    self._config(flag)

  @property
  def disableClick(self):
    """
    Description:
    ------------
    Disable click to create a schedule. The default value is false.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    return self._config_get(False)

  @disableClick.setter
  def disableClick(self, flag):
    self._config(flag)

  @property
  def isReadOnly(self):
    """
    Description:
    ------------
    Calendar is read-only mode and a user can't create and modify any schedule. The default value is false.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    return self._config_get(False)

  @isReadOnly.setter
  def isReadOnly(self, flag):
    self._config(flag)

  @property
  def usageStatistics(self):
    """
    Description:
    ------------
    Let us know the hostname. If you don't want to send the hostname, please set to false.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar
    """
    return self._config_get(False)

  @usageStatistics.setter
  def usageStatistics(self, flag):
    self._config(flag)

  def add_calendars(self, name, bgColor='#ffbb3b'):
    """
    Description:
    -----------

    :rtype: OptionCalendars
    """
    calendar = self._config_sub_data_enum("calendars", OptionCalendars)
    calendar.name = name
    calendar.bgColor = bgColor
    return calendar
