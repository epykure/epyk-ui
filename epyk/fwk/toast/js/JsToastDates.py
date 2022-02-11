#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import primitives

from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class DateBase(JsPackage):

  def __init__(self, component, js_code: str = None, set_var: bool = True, is_py_data: bool = True, page = None):
    self.varName, self.varData, self.__var_def = js_code, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def addCssClass(self, class_name: Union[str, primitives.JsDataModel]):
    """
    Description:
    -----------
    Apply a CSS class to the date picker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/Calendar#addCssClass

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] class_name: Class name.
    """
    class_name = JsUtils.jsConvertData(class_name, None)
    return JsUtils.jsWrap("%s.addCssClass(%s)" % (self.component.input.dom.varName, class_name))

  def changeLanguage(self, language: Union[str, primitives.JsDataModel]):
    """
    Description:
    -----------
    Change language.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#changeLanguage

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] language: Language code. English('en') and Korean('ko') are
      provided as default.
    """
    language = JsUtils.jsConvertData(language, None)
    return JsUtils.jsWrap("%s.changeLanguage(%s)" % (self.component.input.dom.varName, language))

  def destroy(self):
    """
    Description:
    -----------
    Destroy the date picker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#destroy
    """
    return JsUtils.jsWrap("%s.destroy()" % self.component.input.dom.varName)

  def on(self, event, js_funcs, profile=None):
    """
    Description:
    -----------

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#event-change

    Attributes:
    ----------
    :param event: String. The JavaScript DOM source for the event (can be a sug item).
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    event = JsUtils.jsConvertData(event, None)
    return JsUtils.jsWrap("%s.on(%s, function(){%s})" % (
      self.component.input.dom.varName, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def off(self, event, js_funcs, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param event: String. The JavaScript DOM source for the event (can be a sug item).
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    event = JsUtils.jsConvertData(event, None)
    return JsUtils.jsWrap("%s.off(%s, function(){%s})" % (
      self.component.input.dom.varName, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def draw(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Occur after the calendar is drawn.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#event-draw

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("draw", js_funcs, profile)

  def getDate(self):
    """
    Description:
    -----------
    Return the selected date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#getDate
    """
    return JsObjects.JsObjects.get("%s.getDate()" % self.component.input.dom.varName)

  def getDateElements(self):
    """
    Description:
    -----------
    Return the date elements on the calendar.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#getDateElements
      https://nhn.github.io/tui.date-picker/latest/Calendar#getDateElements
    """
    return JsObjects.JsObjects.get("%s.getDateElements()" % self.component.input.dom.varName)

  def getType(self):
    """
    Description:
    -----------
    Return the date picker's type.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#getType
    """
    return JsObjects.JsString.JsString.get("%s.getType()" % self.component.input.dom.varName)

  def removeCssClass(self, class_name: Union[str, primitives.JsDataModel]):
    """
    Description:
    -----------
    Remove a CSS class from the date picker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#removeCssClass
      https://nhn.github.io/tui.date-picker/latest/Calendar#removeCssClass

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] class_name: Class name.
    """
    class_name = JsUtils.jsConvertData(class_name, None)
    return JsUtils.jsWrap("%s.removeCssClass(%s)" % (self.component.input.dom.varName, class_name))


class Calendar(DateBase):

  def drawNext(self):
    """
    Description:
    -----------
    Draw the next page.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/Calendar#drawNext
    """
    return JsUtils.jsWrap("%s.drawNext()" % self.component.input.dom.varName)

  def drawPrev(self):
    """
    Description:
    -----------
    Draw the previous page.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/Calendar#drawPrev
    """
    return JsUtils.jsWrap("%s.drawPrev()" % self.component.input.dom.varName)

  def getNextDate(self):
    """
    Description:
    -----------
    Return the next date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/Calendar#getNextDate
    """
    return JsObjects.JsObjects.get("%s.getNextDate()" % self.component.input.dom.varName)

  def getNextYearDate(self):
    """
    Description:
    -----------
    Return the date a year later.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/Calendar#getNextDate
    """
    return JsObjects.JsObjects.get("%s.getNextYearDate()" % self.component.input.dom.varName)

  def getPrevDate(self):
    """
    Description:
    -----------
    Return the previous date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/Calendar#getPrevDate
    """
    return JsObjects.JsObjects.get("%s.getPrevDate()" % self.component.input.dom.varName)

  def getPrevYearDate(self):
    """
    Description:
    -----------
    Return the date a year previously.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/Calendar#getPrevYearDate
    """
    return JsObjects.JsObjects.get("%s.getPrevYearDate()" % self.component.input.dom.varName)

  def hide(self):
    """
    Description:
    -----------
    Hide the calendar.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/Calendar#hide
    """
    return JsUtils.jsWrap("%s.hide()" % self.component.input.dom.varName)

  def show(self):
    """
    Description:
    -----------
    Show the calendar.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/Calendar#show
    """
    return JsUtils.jsWrap("%s.show()" % self.component.input.dom.varName)


class DatePickerRange(DateBase):

  def addRange(self, start, end):
    """
    Description:
    -----------
    Add a selectable range. Use Date instances or numbers(timestamp).

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#addRange

    Attributes:
    ----------
    :param start: Date | Number. the start date.
    :param end: Date | Number. the end date.
    """
    start = JsUtils.jsConvertData(start, None)
    end = JsUtils.jsConvertData(end, None)
    return JsObjects.JsObjects.get("%s.addRange(%s, %s)" % (self.component.input.dom.varName, start, end))

  def getEndDate(self):
    """
    Description:
    -----------
    Return the end date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#getEndDate
    """
    return JsObjects.JsObjects.get("%s.getEndDate()" % self.component.input.dom.varName)

  def getEndpicker(self):
    """
    Description:
    -----------
    Return a end-datepicker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#getEndpicker
    """
    return JsObjects.JsObjects.get("%s.getEndpicker()" % self.component.input.dom.varName)

  def getStartDate(self):
    """
    Description:
    -----------
    Return the start date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#getStartDate
    """
    return JsObjects.JsObjects.get("%s.getStartDate()" % self.component.input.dom.varName)

  def getStartpicker(self):
    """
    Description:
    -----------
    Return a start-datepicker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#getStartpicker
    """
    return JsObjects.JsObjects.get("%s.getStartpicker()" % self.component.input.dom.varName)

  def removeRange(self, start, end, type):
    """
    Description:
    -----------
    Remove a range. Use Date instances or numbers(timestamp).

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#removeRange

    Attributes:
    ----------
    :param start: Date | Number. the start date.
    :param end: Date | Number. the end date.
    :param str type: null'date''month''year'. Range type. If falsy, start and end values are considered as timestamp.
    """
    start = JsUtils.jsConvertData(start, None)
    end = JsUtils.jsConvertData(end, None)
    type = JsUtils.jsConvertData(type, None)
    return JsObjects.JsObjects.get("%s.removeRange(%s, %s, %s)" % (self.component.input.dom.varName, start, end, type))

  def setEndDate(self, date):
    """
    Description:
    -----------
    Set the end date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#date

    Attributes:
    ----------
    :param date: Date. End date.
    """
    date = JsUtils.jsConvertData(date, None)
    return JsObjects.JsObjects.get("%s.setEndDate(%s)" % (self.component.input.dom.varName, date))

  def setRanges(self, ranges):
    """
    Description:
    -----------
    Set selectable ranges.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#setRanges

    Attributes:
    ----------
    :param ranges: Array<Date | Number>. Selectable ranges. Use Date instances or numbers(timestamp).
    """
    ranges = JsUtils.jsConvertData(ranges, None)
    return JsObjects.JsObjects.get("%s.setRanges(%s)" % (self.component.input.dom.varName, ranges))

  def setStartDate(self, date):
    """
    Description:
    -----------
    Set the start date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#setStartDate

    Attributes:
    ----------
    :param date: Date. Start date.
    """
    date = JsUtils.jsConvertData(date, None)
    return JsObjects.JsObjects.get("%s.setStartDate(%s)" % (self.component.input.dom.varName, date))

  def on_change_start(self, js_funcs, profile=None):
    """
    Description:
    -----------

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#event-change:start

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("change:start", js_funcs, profile)

  def off_change_start(self, js_funcs, profile=None):
    """
    Description:
    -----------

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#event-change:start

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.off("change:start", js_funcs, profile)

  def on_change_end(self, js_funcs, profile=None):
    """
    Description:
    -----------

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#event-change:end

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("change:end", js_funcs, profile)

  def off_change_end(self, js_funcs, profile=None):
    """
    Description:
    -----------

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker#event-change:end

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.off("change:end", js_funcs, profile)


class DatePicker(DateBase):

  def addRange(self, start, end):
    """
    Description:
    -----------
    Add a selectable range. Use Date instances or numbers(timestamp).

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#addRange

    Attributes:
    ----------
    :param start: Date | Number. The start date.
    :param end: Date | Number. The end date.
    """
    start = JsUtils.jsConvertData(start, None)
    end = JsUtils.jsConvertData(end, None)
    return JsUtils.jsWrap("%s.addRange(%s, %s)" % (self.component.input.dom.varName, start, end))

  def close(self):
    """
    Description:
    -----------
    Close the date picker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#close
    """
    return JsUtils.jsWrap("%s.close()" % self.component.input.dom.varName)

  def disable(self):
    """
    Description:
    -----------
    Disable the date picker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#disable
    """
    return JsUtils.jsWrap("%s.disable()" % self.component.input.dom.varName)

  def drawLowerCalendar(self, date):
    """
    Description:
    -----------
    Lower the calendar type. (year -> month -> date).

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#drawLowerCalendar

    Attributes:
    ----------
    :param date: Date. Date to set.
    """
    date = JsUtils.jsConvertData(date, None)
    return JsUtils.jsWrap("%s.drawLowerCalendar(%s)" % (self.component.input.dom.varName, date))

  def drawUpperCalendar(self, date):
    """
    Description:
    -----------
    Raise the calendar type. (date -> month -> year).

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#drawUpperCalendar

    Attributes:
    ----------
    :param date: Date. Date to set.
    """
    date = JsUtils.jsConvertData(date, None)
    return JsUtils.jsWrap("%s.drawUpperCalendar(%s)" % (self.component.input.dom.varName, date))

  def enable(self):
    """
    Description:
    -----------
    Enable the date picker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#enable
    """
    return JsUtils.jsWrap("%s.enable()" % self.component.input.dom.varName)

  def findOverlappedRange(self, startDate, endDate):
    """
    Description:
    -----------
    Raise the calendar type. (date -> month -> year).

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#findOverlappedRange

    Attributes:
    ----------
    :param startDate: Date | number. Start date to find overlapped range.
    :param endDate: Date | number. End date to find overlapped range.
    """
    startDate = JsUtils.jsConvertData(startDate, None)
    endDate = JsUtils.jsConvertData(endDate, None)
    return JsUtils.jsWrap("%s.findOverlappedRange(%s, %s)" % (self.component.input.dom.varName, startDate, endDate))

  def getCalendar(self):
    """
    Description:
    -----------
    Return the calendar instance.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#getCalendar
    """
    return JsObjects.JsObjects.get("%s.getCalendar()" % self.component.input.dom.varName)

  def getCalendarType(self):
    """
    Description:
    -----------
    Return the current calendar's type.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#getCalendarType
    """
    return JsObjects.JsObjects.get("%s.getCalendarType()" % self.component.input.dom.varName)

  def getLocaleText(self):
    """
    Description:
    -----------
    Return the locale text object.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#getLocaleText
    """
    return JsObjects.JsString.JsString.get("%s.getLocaleText()" % self.component.input.dom.varName)

  def getTimePicker(self):
    """
    Description:
    -----------
    Return the time picker instance.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#getTimePicker
    """
    return JsObjects.JsObjects.get("%s.getTimePicker()" % self.component.input.dom.varName)

  def isDisabled(self):
    """
    Description:
    -----------
    Return whether the date picker is disabled.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#isDisabled
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.isDisabled()" % self.component.input.dom.varName)

  def isOpened(self):
    """
    Description:
    -----------
    Return whether the datepicker opens or not.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#isOpened
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.isOpened()" % self.component.input.dom.varName)

  def isSelectable(self, date):
    """
    Description:
    -----------
    Return whether the date is selectable.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#isSelectable

    Attributes:
    ----------
    :param date: Date. Date to check.
    """
    date = JsUtils.jsConvertData(date, None)
    return JsObjects.JsBoolean.JsBoolean.get("%s.isSelectable(%s)" % (self.component.input.dom.varName, date))

  def isSelected(self, date):
    """
    Description:
    -----------
    Return whether the date is selected.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#isSelected

    Attributes:
    ----------
    :param date: Date. Date to check.
    """
    date = JsUtils.jsConvertData(date, None)
    return JsObjects.JsBoolean.JsBoolean.get("%s.isSelected(%s)" % (self.component.input.dom.varName, date))

  def open(self):
    """
    Description:
    -----------
    Open the date picker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#open
    """
    return JsUtils.jsWrap("%s.open()" % self.component.input.dom.varName)

  def removeAllOpeners(self):
    """
    Description:
    -----------
    Remove all openers.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#removeAllOpeners
    """
    return JsUtils.jsWrap("%s.removeAllOpeners()" % self.component.input.dom.varName)

  def removeRange(self, start, end, type):
    """
    Description:
    -----------
    Remove a range. Use Date instances or numbers(timestamp).

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#removeRange

    Attributes:
    ----------
    :param start: Date | Number. the start date.
    :param end: Date | Number. the end date.
    :param type: String. Range type. If falsy, start and end values are considered as timestamp.
    """
    start = JsUtils.jsConvertData(start, None)
    end = JsUtils.jsConvertData(end, None)
    type = JsUtils.jsConvertData(type, None)
    return JsUtils.jsWrap("%s.removeRange(%s, %s, %s)" % (self.component.input.dom.varName, start, end, type))

  def setDate(self, date):
    """
    Description:
    -----------
    Select the date.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#setDate

    Attributes:
    ----------
    :param date: Date | Number. Date instance or timestamp to set.
    """
    date = JsUtils.jsConvertData(date, None)
    return JsUtils.jsWrap("%s.setDate(%s)" % (self.component.input.dom.varName, date))

  def setDateFormat(self, format):
    """
    Description:
    -----------
    Select the date by the date string format.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#setDateFormat

    Attributes:
    ----------
    :param format: String. The date format.
    """
    format = JsUtils.jsConvertData(format, None)
    return JsUtils.jsWrap("%s.setDateFormat(%s)" % (self.component.input.dom.varName, format))

  def setInput(self, element, options):
    """
    Description:
    -----------
    Select the date by the date string format.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#setInput

    Attributes:
    ----------
    :param element: String. Input element or selector.
    :param options: Dictionary.
    """
    element = JsUtils.jsConvertData(element, None)
    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.setInput(%s, %s)" % (self.component.input.dom.varName, element, options))

  def setNull(self):
    """
    Description:
    -----------
    Set no date to be selected. (Selected date: null).

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#setNull
    """
    return JsUtils.jsWrap("%s.setNull()" % self.component.input.dom.varName)

  def setRanges(self, ranges):
    """
    Description:
    -----------
    Set selectable ranges. Previous ranges will be removed.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#setRanges

    Attributes:
    ----------
    :param ranges: Array<Date> | Array<Number>. Selectable ranges. Use Date instances or numbers(timestamp).
    """
    ranges = JsUtils.jsConvertData(ranges, None)
    return JsUtils.jsWrap("%s.setRanges(%s)" % (self.component.input.dom.varName, ranges))

  def setType(self, type):
    """
    Description:
    -----------
    Set the calendar's type.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#setType

    Attributes:
    ----------
    :param type: String. Calendar type.
    """
    type = JsUtils.jsConvertData(type, None)
    return JsUtils.jsWrap("%s.setType(%s)" % (self.component.input.dom.varName, type))

  def toggle(self):
    """
    Description:
    -----------
    Toggle the date picker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#toggle
    """
    return JsUtils.jsWrap("%s.toggle()" % self.component.input.dom.varName)

  def on_close(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Occur after the date picker closes..

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#event-close

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("close", js_funcs, profile)

  def on_open(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Occur after the calendar is drawn.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#event-open

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("open", js_funcs, profile)


class TimePicker(JsPackage):

  def __init__(self, component, js_code=None, set_var=True, is_py_data=True, page=None):
    self.varName, self.varData, self.__var_def = js_code, "", None
    self.component, self._report = component, page
    self._js, self._jquery = [], None

  def changeLanguage(self, language):
    """
    Description:
    -----------
    Change locale text of meridiem by language code.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#changeLanguage

    Attributes:
    ----------
    :param language: String. Language code
    """
    language = JsUtils.jsConvertData(language, None)
    return JsUtils.jsWrap("%s.changeLanguage(%s)" % (self.component.var, language))

  def destroy(self):
    """
    Description:
    -----------
    Destroy the date picker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DatePicker#destroy
    """
    return JsUtils.jsWrap("%s.destroy()" % self.component.var)

  def getHout(self):
    """
    Description:
    -----------
    Get hour.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#getHour
    """
    return JsObjects.JsNumber.JsNumber.get("%s.getHour()" % self.component.var)

  def getHourStep(self):
    """
    Description:
    -----------
    Get step of hour.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#getHourStep
    """
    return JsObjects.JsNumber.JsNumber.get("%s.getHourStep()" % self.component.var)

  def getMinute(self):
    """
    Description:
    -----------
    Get minute.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#getMinute
    """
    return JsObjects.JsNumber.JsNumber.get("%s.getMinute()" % self.component.var)

  def getMinuteStep(self):
    """
    Description:
    -----------
    Get step of minute.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#getMinuteStep
    """
    return JsObjects.JsNumber.JsNumber.get("%s.getMinuteStep()" % self.component.var)

  def hide(self):
    """
    Description:
    -----------
    Hide time picker element.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#hide
    """
    return JsUtils.jsWrap("%s.hide()" % self.component.var)

  def resetMinuteRange(self):
    """
    Description:
    -----------
    Reset minute selectable range.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#resetMinuteRange
    """
    return JsUtils.jsWrap("%s.resetMinuteRange()" % self.component.var)

  def setHour(self, hour):
    """
    Description:
    -----------
    Set hour

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#setHour

    Attributes:
    ----------
    :param hour: Number. for time picker - (0~23).
    """
    hour = JsUtils.jsConvertData(hour, None)
    return JsUtils.jsWrap("%s.setHour(%s)" % (self.component.var, hour))

  def setHourStep(self, step):
    """
    Description:
    -----------
    Set step of hour

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#setHourStep

    Attributes:
    ----------
    :param step: Array. Step to create items of hour.
    """
    step = JsUtils.jsConvertData(step, None)
    return JsUtils.jsWrap("%s.setHourStep(%s)" % (self.component.var, step))

  def setMinute(self, minute):
    """
    Description:
    -----------
    Set minute.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#setMinute

    Attributes:
    ----------
    :param minute: Number. for time picker
    """
    minute = JsUtils.jsConvertData(minute, None)
    return JsUtils.jsWrap("%s.setMinute(%s)" % (self.component.var, minute))

  def setMinuteStep(self, step):
    """
    Description:
    -----------
    Set step of minute.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#setMinuteStep

    Attributes:
    ----------
    :param step: Array. Step to create items of minute
    """
    step = JsUtils.jsConvertData(step, None)
    return JsUtils.jsWrap("%s.setMinuteStep(%s)" % (self.component.var, step))

  def setRange(self, begin, end=None):
    """
    Description:
    -----------
    Set selectable range

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#setRange

    Attributes:
    ----------
    :param begin: Dictionary. Contain begin hour and minute of range.
    :param end: Dictionary. Optional. Contain end hour and minute of range
    """
    begin = JsUtils.jsConvertData(begin, None)
    if end is not None:
      end = JsUtils.jsConvertData(end, None)
      return JsUtils.jsWrap("%s.setRange(%s, %s)" % (self.component.var, begin, end))

    return JsUtils.jsWrap("%s.setRange(%s)" % (self.component.var, begin))

  def setTime(self, hour, minute):
    """
    Description:
    -----------
    Set time.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#setTime

    Attributes:
    ----------
    :param hour: Number. for time picker - (0~23).
    :param minute: Number. for time picker.
    """
    hour = JsUtils.jsConvertData(hour, None)
    minute = JsUtils.jsConvertData(minute, None)
    return JsUtils.jsWrap("%s.setTime(%s, %s)" % (self.component.var, hour, minute))

  def show(self):
    """
    Description:
    -----------
    Show time picker element.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#show
    """
    return JsUtils.jsWrap("%s.show()" % self.component.var)

  def change(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Change event - TimePicker.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker#event-change

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    event = JsUtils.jsConvertData("change", None)
    return JsUtils.jsWrap("%s.on(%s, function(){%s})" % (
      self.component.var, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
