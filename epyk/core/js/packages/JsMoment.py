
from typing import Any
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class MomentDate(JsPackage):

  def week(self, number: float = None):
    """ Gets or sets the week of the year.

    Related Pages:

      https://momentjs.com/docs/#/get-set/week/

    :param number: Optional. The week's number
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.week()" % self.varId)

    return JsUtils.jsWrap("%s.week(%s)" % (self.varId, number))

  def weeks(self, number: float = None):
    """  Gets or sets the week of the year.

    Related Pages:

      https://momentjs.com/docs/#/get-set/week/

    :param number: Optional. The week's number.
    """
    return self.week(number)

  def weekYear(self, number: float = None):
    """  Gets or sets the week-year according to the locale.

    Related Pages:

      https://momentjs.com/docs/#/get-set/week-year/

    :param number: Optional. The week's number from this year
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.weekYear()" % self.varId)

    return JsUtils.jsWrap("%s.weekYear(%s)" % (self.varId, number))

  def get(self, text: str):
    """ Getter.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-weeks-in-year/

    :param text: The object property name
    """
    text = JsUtils.jsConvertData(text, None)
    return JsObjects.JsObject.JsObject.get("%s.get(%s)" % (self.varId, text))

  def set(self, name, value):
    """ Getter.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-weeks-in-year/

    :param name: The object property name
    :param value: The object property value
    """
    name = JsUtils.jsConvertData(name, None)
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObject.JsObject.get("%s.set(%s, %s)" % (self.varId, name, value))

  def isoWeekYear(self, number: float = None):
    """ Gets or sets the ISO week-year.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-week-year/

    :param number: Optional. The week's number from this year
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.isoWeekYear()" % self.varId)

    return JsUtils.jsWrap("%s.isoWeekYear(%s)" % (self.varId, number))

  def weeksInYear(self) -> JsObjects.JsNumber.JsNumber:
    """ Gets the number of weeks in the current moment's year, according to ISO weeks.

    Related Pages:

      https://momentjs.com/docs/#/get-set/weeks-in-year/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.weeksInYear()" % self.varId)

  def isoWeeksInYear(self):
    """ Gets the number of weeks in the current moment's year, according to ISO weeks.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-weeks-in-year/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.isoWeeksInYear()" % self.varId)

  def isValid(self):
    """  

    Related Pages:

      https://momentjs.com/docs/#/parsing/is-valid/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.isValid()" % self.varId)

  def invalid(self):
    """ You can create your own invalid Moment objects, which is useful in making your own parser.

    Related Pages:

      https://momentjs.com/docs/#/utilities/invalid/
    """

  def format(self, value: float = None):
    """ This is the most robust display option.
    It takes a string of tokens and replaces them with their corresponding values.

    Related Pages:

      https://momentjs.com/docs/#/displaying/format/

    :param value: Optional. The format definition
    """
    if value is None:
      return JsObjects.JsObjects.get("%s.format()" % self.varId)

    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get("%s.format(%s)" % (self.varId, value))

  def quarter(self, number: float = None):
    """ Gets / Sets the quarter (1 to 4).

    Related Pages:

      https://momentjs.com/docs/#/get-set/quarter/

    :param number: Optional. The quarter's number
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.quarter()" % self.varId)

    return JsUtils.jsWrap("%s.quarter(%s)" % (self.varId, number))

  def add(self, unit: int, value: str, js_code: str = None):
    """ Add value.

    Related Pages:

      https://momentjs.com/docs/#/displaying/difference/

    :param unit:
    :param value:
    :param js_code: Optional. The variable name created in the Javascript
    """
    unit = JsUtils.jsConvertData(unit, None)
    value = JsUtils.jsConvertData(value, None)
    if js_code is not None:
      return MomentDate(selector="%s.add(%s, %s)" % (self.varId, unit, value), js_code=js_code, set_var=True)

    return MomentDate(selector="%s.add(%s, %s)" % (self.varId, unit, value), set_var=False)

  def subtract(self, unit: int, value: str, js_code: str = None):
    """ Subtract value.

    Related Pages:

      https://momentjs.com/docs/#/displaying/difference/

    :param unit:
    :param value:
    :param js_code: Optional. The variable name created in the Javascript
    """
    unit = JsUtils.jsConvertData(unit, None)
    value = JsUtils.jsConvertData(value, None)
    if js_code is not None:
      return MomentDate(selector="%s.subtract(%s, %s)" % (self.varId, unit, value), js_code=js_code, set_var=True)

    return MomentDate(selector="%s.subtract(%s, %s)" % (self.varId, unit, value), set_var=False)

  def year(self, number: int = None):
    """   Gets or sets the year.

    Related Pages:

      https://momentjs.com/docs/#/get-set/year/

    :param number: Optional. The year's number
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.year()" % self.varId)

    return JsUtils.jsWrap("%s.year(%s)" % (self.varId, number))

  def clone(self, js_code: str = None):
    """ All moments are mutable. If you want a clone of a moment, you can do so implicitly or explicitly.

    Related Pages:

      https://momentjs.com/docs/#/parsing/moment-clone/

    :param js_code: Optional. The variable name created in the Javascript
    """
    if js_code is not None:
      return MomentDate(selector="%s.clone()" % self.varId, js_code=js_code, set_var=True)

    return MomentDate(selector="%s.clone()" % self.varId, set_var=False)

  def date(self, number: int = None):
    """ Gets or sets the day of the month.

    Accepts numbers from 1 to 31. If the range is exceeded, it will bubble up to the months.

    Related Pages:

      https://momentjs.com/docs/#/get-set/date/

    :param number: Optional. The month number of days
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.date()" % self.varId)

    return JsUtils.jsWrap("%s.date(%s)" % (self.varId, number))

  def isoWeek(self, number: int = None):
    """ Gets or sets the ISO week of the year.

    When setting the week of the year, the day of the week is retained.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-week/

    :param number: Optional. The year's number
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.isoWeek()" % self.varId)

    return JsUtils.jsWrap("%s.isoWeek(%s)" % (self.varId, number))

  def isoWeekday(self, number=None):
    """  
    Gets or sets the ISO day of the week with 1 being Monday and 7 being Sunday.

    As with moment#day, if the range is exceeded, it will bubble up to other weeks.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-weekday/

    :param number: Number. Optional. The year's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.isoWeekday()" % self.varId)

    return JsUtils.jsWrap("%s.isoWeekday(%s)" % (self.varId, number))

  def weekday(self, number=None):
    """  
    Gets or sets the day of the week according to the locale.

    If the locale assigns Monday as the first day of the week, moment().weekday(0) will be Monday.
    If Sunday is the first day of the week, moment().weekday(0) will be Sunday.

    Related Pages:

      https://momentjs.com/docs/#/get-set/weekday/
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.weekday()" % self.varId)

    return JsUtils.jsWrap("%s.weekday(%s)" % (self.varId, number))

  def dayOfYear(self, number=None):
    """  
    Gets or sets the day of the year.

    Accepts numbers from 1 to 366. If the range is exceeded, it will bubble up to the years.

    Related Pages:

      https://momentjs.com/docs/#/get-set/min/

    :param number: Number. Optional. The day of year number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.dayOfYear()" % self.varId)

    return JsUtils.jsWrap("%s.dayOfYear(%s)" % (self.varId, number))

  def day(self, number=None):
    """  
    Gets or sets the day of the week.

    This method can be used to set the day of the week, with Sunday as 0 and Saturday as 6.

    Related Pages:

      https://momentjs.com/docs/#/get-set/day/

    :param number: Number. Optional. The day's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.day()" % self.varId)

    return JsUtils.jsWrap("%s.day(%s)" % (self.varId, number))

  def days(self, number=None):
    """  
    Gets or sets the day of the week.

    This method can be used to set the day of the week, with Sunday as 0 and Saturday as 6.

    Related Pages:

      https://momentjs.com/docs/#/get-set/day/

    :param number: Number. Optional. The day's number.
    """
    return self.day(number)

  def second(self, number=None):
    """  
    Gets or sets the seconds.

    Accepts numbers from 0 to 59. If the range is exceeded, it will bubble up to the minutes.

    Related Pages:

      https://momentjs.com/docs/#/get-set/second/

    :param number: Number. Optional. The second's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.second()" % self.varId)

    return JsUtils.jsWrap("%s.second(%s)" % (self.varId, number))

  def seconds(self, number=None):
    """  
    Gets or sets the seconds.

    Accepts numbers from 0 to 59. If the range is exceeded, it will bubble up to the minutes.

    Related Pages:

      https://momentjs.com/docs/#/get-set/second/

    :param number: Number. Optional. The second's number.
    """
    return self.day(number)

  def minute(self, number=None):
    """  
    Gets or sets the minutes.

    Accepts numbers from 0 to 59. If the range is exceeded, it will bubble up to the hour.

    Related Pages:

      https://momentjs.com/docs/#/get-set/minute/

    :param number: Number. Optional. The minute's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.second()" % self.varId)

    return JsUtils.jsWrap("%s.second(%s)" % (self.varId, number))

  def minutes(self, number=None):
    """  
    Gets or sets the minutes.

    Accepts numbers from 0 to 59. If the range is exceeded, it will bubble up to the hour.

    Related Pages:

      https://momentjs.com/docs/#/get-set/minute/

    :param number: Number. Optional. The minute's number.
    """
    return self.minute(number)

  def hour(self, number=None):
    """  
    Gets or sets the hour.

    Accepts numbers from 0 to 23. If the range is exceeded, it will bubble up to the day.

    Related Pages:

      https://momentjs.com/docs/#/get-set/hour/

    :param number: Number. Optional. The hour's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.hour()" % self.varId)

    return JsUtils.jsWrap("%s.hour(%s)" % (self.varId, number))

  def hours(self, number=None):
    """  
    Gets or sets the hour.

    Accepts numbers from 0 to 23. If the range is exceeded, it will bubble up to the day.

    Related Pages:

      https://momentjs.com/docs/#/get-set/hour/

    :param number: Number. Optional. The hour's number.
    """
    return self.hour(number)

  def utcOffset(self, number=None, flag=None):
    """  
    Get or set the UTC offset in minutes.

    Related Pages:

      https://momentjs.com/docs/#/manipulating/utc-offset/
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.utcOffset()" % self.varId)

    if flag is None:
      return JsObjects.JsNumber.JsNumber.get("%s.utcOffset(%s)" % (self.varId, number))

    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsNumber.JsNumber.get("%s.utcOffset(%s, %s)" % (self.varId, number, flag))

  def invalidAt(self):
    raise NotImplementedError()

  def creationData(self):
    """  
    After a moment object is created, all of the inputs can be accessed with creationData() method:

    Related Pages:

      https://momentjs.com/docs/#/parsing/creation-data/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.creationData()" % self.varId)

  def millisecond(self, number=None):
    """  
    Gets or sets the milliseconds.

    Accepts numbers from 0 to 999. If the range is exceeded, it will bubble up to the seconds.

    Related Pages:

      https://momentjs.com/docs/#/get-set/millisecond/

    :param number: Number. Optional. The second's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.millisecond()" % self.varId)

    return JsUtils.jsWrap("%s.millisecond(%s)" % (self.varId, number))

  def milliseconds(self, number=None):
    """  
    Gets or sets the milliseconds.

    Accepts numbers from 0 to 999. If the range is exceeded, it will bubble up to the seconds.

    Related Pages:

      https://momentjs.com/docs/#/get-set/millisecond/

    :param number: Number. Optional. The second's number.
    """
    return self.millisecond(number)

  def startOf(self, text):
    """  
    Mutates the original moment by setting it to the start of a unit of time.

    Related Pages:

      https://momentjs.com/docs/#/manipulating/start-of/
    """
    text = JsUtils.jsConvertData(text, None)
    return JsObjects.JsNumber.JsNumber.get("%s.startOf(%s)" % (self.varId, text))

  def endOf(self, text):
    """  
    Mutates the original moment by setting it to the end of a unit of time.

    Related Pages:

      https://momentjs.com/docs/#/manipulating/end-of/
    """
    text = JsUtils.jsConvertData(text, None)
    return JsObjects.JsNumber.JsNumber.get("%s.endOf(%s)" % (self.varId, text))

  def fromNow(self, flag=None):
    """  
    A common way of displaying time is handled by moment#fromNow. This is sometimes called timeago or relative time.

    Related Pages:

      https://momentjs.com/docs/#/displaying/fromnow/

    :param flag:
    """
    if flag is None:
      return JsObjects.JsNumber.JsNumber.get("%s.fromNow()" % self.varId)

    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsNumber.JsNumber.get("%s.fromNow(%s)" % (self.varId, flag))

  def fromDate(self, value, flag=None):
    """
    Related Pages:

      https://momentjs.com/docs/#/displaying/from/

    """
    value = JsUtils.jsConvertData(value, None)
    if flag is None:
      return JsObjects.JsNumber.JsNumber.get("%s.from(%s)" % (self.varId, value))

    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsNumber.JsNumber.get("%s.from(%s, %s)" % (self.varId, value, flag))

  def toNow(self, flag=None):
    """  
    A common way of displaying time is handled by moment#toNow. This is sometimes called timeago or relative time.

    Related Pages:

      https://momentjs.com/docs/#/displaying/tonow/

    """
    if flag is None:
      return JsObjects.JsNumber.JsNumber.get("%s.toNow()" % self.varId)

    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsNumber.JsNumber.get("%s.toNow(%s)" % (self.varId, flag))

  def to(self, value, flag=None):
    """  
    You may want to display a moment in relation to a time other than now. In that case, you can use moment#to.

    Related Pages:

      https://momentjs.com/docs/#/displaying/to/
    """
    value = JsUtils.jsConvertData(value, None)
    if flag is None:
      return JsObjects.JsNumber.JsNumber.get("%s.to(%s)" % (self.varId, value))

    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsNumber.JsNumber.get("%s.to(%s, %s)" % (self.varId, value, flag))

  def calendar(self, value=None):
    """  
    Calendar time displays time relative to a given referenceDay (defaults to the start of today),
    but does so slightly differently than moment#fromNow.

    Related Pages:

      https://momentjs.com/docs/#/displaying/calendar-time/
    """
    if value is None:
      return JsObjects.JsNumber.JsNumber.get("%s.calendar()" % self.varId)

    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsNumber.JsNumber.get("%s.calendar(%s)" % (self.varId, value))

  def diff(self, dt):
    """  
    To get the difference in milliseconds, use moment#diff like you would use moment#from

    Related Pages:

      https://momentjs.com/docs/#/displaying/difference/
    """
    dt = JsUtils.jsConvertData(dt, None)
    return JsObjects.JsNumber.JsNumber.get("%s.diff(%s)" % (self.varId, dt))

  def daysInMonth(self):
    """  
    Get the number of days in the current month.

    Related Pages:

      https://momentjs.com/docs/#/displaying/days-in-month/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.daysInMonth()" % self.varId)

  def toDate(self):
    """  
    To get a copy of the native Date object that Moment.js wraps, use moment#toDate.

    Related Pages:

      https://momentjs.com/docs/#/displaying/as-javascript-date/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.toDate()" % self.varId)

  def toArray(self):
    """  
    This returns an array that mirrors the parameters from new Date().

    Related Pages:

      https://momentjs.com/docs/#/displaying/as-array/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.toArray()" % self.varId)

  def toJSON(self):
    """  
    When serializing an object to JSON, if there is a Moment object, it will be represented as an ISO8601 string,
    adjusted to UTC.

    Related Pages:

      https://momentjs.com/docs/#/displaying/as-json/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.toJSON()" % self.varId)

  def toISOString(self, keep_offset=None):
    """  
    Formats a string to the ISO8601 standard.

    Related Pages:

      https://momentjs.com/docs/#/displaying/as-iso-string/

    :param keep_offset: Boolean. Optional.
    """
    if keep_offset is None:
      return JsObjects.JsNumber.JsNumber.get("%s.toISOString()" % self.varId)

    keep_offset = JsUtils.jsConvertData(keep_offset, None)
    return JsObjects.JsNumber.JsNumber.get("%s.toISOString(%s)" % (self.varId, keep_offset))

  def inspect(self):
    """  
    Returns a machine readable string, that can be evaluated to produce the same moment.
    Because of the name its also used in node interactive shell to display objects.

    Related Pages:

      https://momentjs.com/docs/#/displaying/inspect/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.inspect()" % self.varId)

  def isBefore(self, value, precision=None):
    """  
    Check if a moment is before another moment.

    Related Pages:

      https://momentjs.com/docs/#/query/is-before/

    :param value: Object. the value to compare.
    :param precision: String. Optional. The category to compare.
    """
    value = JsUtils.jsConvertData(value, None)
    if precision is None:
      return JsObjects.JsBoolean.JsBoolean.get("%s.isBefore(%s)" % (self.varId, value))

    precision = JsUtils.jsConvertData(precision, None)
    return JsObjects.JsBoolean.JsBoolean.get("%s.isBefore(%s, %s)" % (self.varId, value, precision))

  def isAfter(self, value, precision=None):
    """  
    Check if a moment is after another moment. The first argument will be parsed as a moment, if not already so.

    Related Pages:

      https://momentjs.com/docs/#/query/is-after/

    :param value: Object. the value to compare.
    :param precision: String. Optional. The category to compare.
    """
    value = JsUtils.jsConvertData(value, None)
    if precision is None:
      return JsObjects.JsBoolean.JsBoolean.get("%s.isAfter(%s)" % (self.varId, value))

    precision = JsUtils.jsConvertData(precision, None)
    return JsObjects.JsBoolean.JsBoolean.get("%s.isAfter(%s, %s)" % (self.varId, value, precision))

  def isSameOrBefore(self, value, precision=None):
    """  
    Check if a moment is before or the same as another moment. The first argument will be parsed as a moment,
    if not already so.

    Related Pages:

      https://momentjs.com/docs/#/query/is-same-or-before/

    :param value: Object. the value to compare.
    :param precision: String. Optional. The category to compare.
    """
    value = JsUtils.jsConvertData(value, None)
    if precision is None:
      return JsObjects.JsBoolean.JsBoolean.get("%s.isSameOrBefore(%s)" % (self.varId, value))

    precision = JsUtils.jsConvertData(precision, None)
    return JsObjects.JsBoolean.JsBoolean.get("%s.isSameOrBefore(%s, %s)" % (self.varId, value, precision))

  def isSameOrAfter(self, value, precision=None):
    """  
    Check if a moment is after or the same as another moment. The first argument will be parsed as a moment,
    if not already so.

    Related Pages:

      https://momentjs.com/docs/#/query/is-same-or-after/

    :param value: Object. the value to compare.
    :param precision: String. Optional. The category to compare.
    """
    value = JsUtils.jsConvertData(value, None)
    if precision is None:
      return JsObjects.JsBoolean.JsBoolean.get("%s.isSameOrAfter(%s)" % (self.varId, value))

    precision = JsUtils.jsConvertData(precision, None)
    return JsObjects.JsBoolean.JsBoolean.get("%s.isSameOrAfter(%s, %s)" % (self.varId, value, precision))

  def isBetween(self, dt1, dt2=None):
    """  
    Check if a moment is between two other moments, optionally looking at unit scale (minutes, hours, days, etc).

    Related Pages:

      https://momentjs.com/docs/#/query/is-between/

    :param dt1: Object. The start date for the range.
    :param dt2: Object. optional. The end date for the range. (Default undefined).
    """
    dt1 = JsUtils.jsConvertData(dt1, None)
    dt2 = JsUtils.jsConvertData(dt2, None)
    return JsObjects.JsBoolean.JsBoolean.get("%s.isBetween(%s, %s)" % (self.varId, dt1, dt2))

  def isSame(self, value, precision=None):
    """  
    Check if a moment is the same as another moment. The first argument will be parsed as a moment, if not already so.

    Related Pages:

      https://momentjs.com/docs/#/query/is-same/

    :param value: Object. the value to compare.
    :param precision: String. Optional. The category to compare.
    """
    value = JsUtils.jsConvertData(value, None)
    if precision is None:
      return JsObjects.JsBoolean.JsBoolean.get("%s.isSame(%s)" % (self.varId, value))

    precision = JsUtils.jsConvertData(precision, None)
    return JsObjects.JsBoolean.JsBoolean.get("%s.isSame(%s, %s)" % (self.varId, value, precision))

  def isDST(self):
    """  
    moment#isDST checks if the current moment is in daylight saving time

    Related Pages:

      https://momentjs.com/docs/#/query/is-daylight-saving-time/
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.isDST()" % self.varId)

  def isLeapYear(self):
    """  
    moment#isLeapYear returns true if that year is a leap year, and false if it is not.

    Related Pages:

      https://momentjs.com/docs/#/query/is-daylight-saving-time/
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.isLeapYear()" % self.varId)

  def unix(self):
    """  
    moment#unix outputs a Unix timestamp (the number of seconds since the Unix Epoch).

    Related Pages:

      https://momentjs.com/docs/#/displaying/unix-timestamp/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.unix()" % self.varId)


class Moment(JsPackage):

  lib_alias = {"js": 'moment'}
  lib_selector = 'moment'

  def now(self, js_code: str = None):
    """ To get the current date and time, just call moment() with no parameters.

    Related Pages:

      https://momentjs.com/docs/#/parsing/now/

    :param js_code: Optional. The variable name created in the Javascript
    """
    if js_code is not None:
      return MomentDate(selector="moment()", js_code=js_code, set_var=True)

    return MomentDate(selector="moment()", set_var=False)

  def time(self, hour: int, minute: int, second: int, js_code: str = None) -> MomentDate:
    """ To get the current time, just call moment() with no parameters.

    Related Pages:

      https://momentjs.com/docs/#/parsing/now/

    :param hour: Optional. The hours' value
    :param minute: Optional. The minutes' value
    :param second: Optional. The seconds' value
    :param js_code: Optional. The variable name created in the Javascript
    """
    if js_code is not None:
      return MomentDate(
        selector="moment().hour(%s).minute(%s).second(%s)" % (hour, minute, second), js_code=js_code, set_var=True)

    return MomentDate(selector="moment().hour(%s).minute(%s).second(%s)" % (hour, minute, second), set_var=False)

  def var(self, js_code: str):
    """ Get the defined moment variable.

    Related Pages:

      https://momentjs.com/docs/#/parsing/now/

    :param js_code: Optional. The variable name created in the Javascript
    """
    return MomentDate(selector=js_code, set_var=False)

  def new(self, date: Any = None, format: str = None, js_code: str = None) -> MomentDate:
    """ When creating a moment from a string, we first check if the string matches known ISO 8601 formats,

    Usages:

      page.js.moment.new(1399919400000).format('dddd, MMMM Do YYYY, h:mm:ss a')

    Related Pages:

      https://momentjs.com/docs/#/parsing/string/

    :param date: The initial date to be loaded
    :param format: The resulting format for the date
    :param js_code: Optional. The variable name created in the Javascript
    """
    if date is None:
      return self.now()

    date = JsUtils.jsConvertData(date, None)
    if format is None:
      if js_code is not None:
        return MomentDate(selector="moment(%s)" % date, js_code=js_code, set_var=True)

      return MomentDate(selector="moment(%s)" % date, set_var=False)

    fmt = JsUtils.jsConvertData(format, None)
    if js_code is not None:
      return MomentDate(selector="moment(%s, %s)" % (date, fmt), js_code=js_code, set_var=True)

    return MomentDate(selector="moment(%s, %s)" % (date, fmt), set_var=False)

  def parseZone(self, date=None, format=None, js_code=None) -> MomentDate:
    """  

    Related Pages:

      https://momentjs.com/docs/#/parsing/parse-zone/

    :param date:
    :param format:
    :param js_code: Optional. The variable name created in the Javascript
    """
    if date is None:
      if js_code is not None:
        return MomentDate(selector="%s.parseZone()" % self.varId, js_code=js_code, set_var=True)

      return MomentDate(selector="%s.parseZone()" % self.varId, set_var=False)

    date = JsUtils.jsConvertData(date, None)
    if format is None:
      if js_code is not None:
        return MomentDate(selector="%s.parseZone(%s)" % (self.varId, date), js_code=js_code, set_var=True)

      return MomentDate(selector="%s.parseZone(%s)" % (self.varId, date), set_var=False)

    format = JsUtils.jsConvertData(format, None)
    if js_code is not None:
      return MomentDate(selector="%s.parseZone(%s, %s)" % (self.varId, date, format), js_code=js_code, set_var=True)

    return MomentDate(selector="%s.parseZone(%s, %s)" % (self.varId, date, format), set_var=False)

  def isMoment(self):
    """ To check if a variable is a moment object, use moment.isMoment().

    Related Pages:

      https://momentjs.com/docs/#/query/is-a-moment/
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.isMoment()" % self.varId)

  def isDate(self):
    """ To check if a variable is a native js Date object, use moment.isDate().

    Related Pages:

      https://momentjs.com/docs/#/query/is-a-date/
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.isDate()" % self.varId)

  def lang(self, value: str) -> JsUtils.jsWrap:
    """ The local lang.

    Related Pages:

      https://momentjs.com/docs/#/i18n/changing-locale/

    :param value: The lang reference
    """
    value = JsUtils.jsConvertData(value, None)
    return JsUtils.jsWrap("%s.lang(%s)" % (self.varId, value))

  def max(self):
    """

    https://momentjs.com/docs/#/get-set/max/
    """

  def min(self):
    """

    https://momentjs.com/docs/#/get-set/min/
    """

  def locale(self, value: str = "en") -> JsUtils.jsWrap:
    """  

    Related Pages:

      https://momentjs.com/docs/#/i18n/changing-locale/

    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    return JsUtils.jsWrap("%s.locale(%s)" % (self.varId, value))

  def locales(self) -> JsUtils.jsWrap:
    """ As of version 2.12.0 it is possible to list all locales that have been loaded and are available to use:

    Related Pages:

      https://momentjs.com/docs/#/i18n/getting-locale/
    """
    return JsUtils.jsWrap("%s.locales()" % self.varId)

  def updateLocale(self, category: str, values: dict) -> JsUtils.jsWrap:
    """  

    Related Pages:

      https://momentjs.com/docs/#/customization/month-names/

    :param category:
    :param values:
    """
    category = JsUtils.jsConvertData(category, None)
    values = JsUtils.jsConvertData(values, None)
    return JsUtils.jsWrap("%s.updateLocale(%s, %s)" % (self.varId, category, values))

  def utc(self, value=None, js_code: str = None) -> MomentDate:
    """ By default, moment parses and displays in local time.

    If you want to parse or display a moment in UTC, you can use moment.utc() instead of moment().

    Related Pages:

      https://momentjs.com/docs/#/parsing/utc/

    :param value:
    :param js_code: Optional. The variable name created in the Javascript
    """
    if value is None:
      if js_code is not None:
        return MomentDate(selector="%s.utc()" % self.varId, js_code=js_code, set_var=True)

      return MomentDate(selector="%s.utc()" % self.varId, set_var=False)

    value = JsUtils.jsConvertData(value, None)
    if js_code is not None:
      return MomentDate(selector="%s.utc(%s)" % (self.varId, value), js_code=js_code, set_var=True)

    return MomentDate(selector="%s.utc(%s)" % (self.varId, value), set_var=False)

  def months(self) -> JsObjects.JsArray.JsArray:
    """ Returns the list of months in the current locale.

    Related Pages:

      https://momentjs.com/docs/#/i18n/listing-months-weekdays/
    """
    return JsObjects.JsArray.JsArray.get("%s.months()" % self.varId)

  def weekdays(self, value, index: int = None) -> JsObjects.JsArray.JsArray:
    """ Week days names.

    Related Pages:

      https://momentjs.com/docs/#/i18n/listing-months-weekdays/
      https://momentjs.com/docs/#/customization/weekday-names/

    :param value:
    :param index:
    """
    value = JsUtils.jsConvertData(value, None)
    if index is None:
      return JsObjects.JsArray.JsArray.get("%s.weekdays(%s)" % (self.varId, value))

    return JsObjects.JsArray.JsArray.get("%s.weekdays(%s, %s)" % (self.varId, value, index))

  def weekdaysShort(self, value=None, index: int = None) -> JsObjects.JsArray.JsArray:
    """ Weekdays abbreviations.

    Related Pages:

      https://momentjs.com/docs/#/i18n/listing-months-weekdays/
      https://momentjs.com/docs/#/customization/weekday-abbreviations/

    :param value:
    :param index:
    """
    if value is None:
      return JsObjects.JsArray.JsArray.get("%s.weekdaysShort()" % self.varId)

    value = JsUtils.jsConvertData(value, None)
    if index is None:
      return JsObjects.JsArray.JsArray.get("%s.weekdaysShort(%s)" % (self.varId, value))

    return JsObjects.JsArray.JsArray.get("%s.weekdaysShort(%s, %s)" % (self.varId, value, index))

  def weekdaysMin(self, value=None, index: int = None) -> JsObjects.JsArray.JsArray:
    """ Minimal Weekday Abbreviations.

    Related Pages:

      https://momentjs.com/docs/#/i18n/listing-months-weekdays/
      https://momentjs.com/docs/#/customization/weekday-min/

    :param value:
    :param index:
    """
    if value is None:
      return JsObjects.JsArray.JsArray.get("%s.weekdaysMin()" % self.varId)

    value = JsUtils.jsConvertData(value, None)
    if index is None:
      return JsObjects.JsArray.JsArray.get("%s.weekdaysMin(%s)" % (self.varId, value))

    return JsObjects.JsArray.JsArray.get("%s.weekdaysMin(%s, %s)" % (self.varId, value, index))

  def monthsShort(self, value=None, index=None) -> JsObjects.JsArray.JsArray:
    """ Month abbreviations.

    Related Pages:

      https://momentjs.com/docs/#/i18n/listing-months-weekdays/
      https://momentjs.com/docs/#/customization/month-abbreviations/

    :param value:
    :param index:
    """
    if value is None:
      return JsObjects.JsArray.JsArray.get("%s.monthsShort()" % self.varId)

    value = JsUtils.jsConvertData(value, None)
    if index is None:
      return JsObjects.JsArray.JsArray.get("%s.monthsShort(%s)" % (self.varId, value))

    return JsObjects.JsArray.JsArray.get("%s.monthsShort(%s, %s)" % (self.varId, value, index))

