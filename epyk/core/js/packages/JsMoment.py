
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class MomentDate(JsPackage):

  def week(self, number=None):
    """
    Description:
    ------------
    Gets or sets the week of the year.

    Related Pages:

      https://momentjs.com/docs/#/get-set/week/

    Attributes:
    ----------
    :param number: Number. Optional. The week's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.week()" % self.varId)

    return JsUtils.jsWrap("%s.week(%s)" % (self.varId, number))

  def weeks(self, number=None):
    """
    Description:
    ------------
    Gets or sets the week of the year.

    Related Pages:

      https://momentjs.com/docs/#/get-set/week/

    Attributes:
    ----------
    :param number: Number. Optional. The week's number.
    """
    return self.week(number)

  def weekYear(self, number=None):
    """
    Description:
    ------------
    Gets or sets the week-year according to the locale.

    Related Pages:

      https://momentjs.com/docs/#/get-set/week-year/

    Attributes:
    ----------
    :param number: Number. Optional. The week's number from this year.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.weekYear()" % self.varId)

    return JsUtils.jsWrap("%s.weekYear(%s)" % (self.varId, number))

  def get(self, text):
    """
    Description:
    ------------
    Getter.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-weeks-in-year/

    Attributes:
    ----------
    :param text: String. The object property name.
    """
    text = JsUtils.jsConvertData(text, None)
    return JsObjects.JsObject.JsObject.get("%s.get(%s)" % (self.varId, text))

  def set(self, name, value):
    """
    Description:
    ------------
    Getter.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-weeks-in-year/

    Attributes:
    ----------
    :param name: String. The object property name.
    :param value: String. The object property value.
    """
    name = JsUtils.jsConvertData(name, None)
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObject.JsObject.get("%s.set(%s, %s)" % (self.varId, name, value))

  def isoWeekYear(self, number=None):
    """
    Description:
    ------------
    Gets or sets the ISO week-year.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-week-year/

    Attributes:
    ----------
    :param number: Number. Optional. The week's number from this year.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.isoWeekYear()" % self.varId)

    return JsUtils.jsWrap("%s.isoWeekYear(%s)" % (self.varId, number))

  def weeksInYear(self):
    """
    Description:
    ------------
    Gets the number of weeks in the current moment's year, according to ISO weeks.

    Related Pages:

      https://momentjs.com/docs/#/get-set/weeks-in-year/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.weeksInYear()" % self.varId)

  def isoWeeksInYear(self):
    """
    Description:
    ------------
    Gets the number of weeks in the current moment's year, according to ISO weeks.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-weeks-in-year/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.isoWeeksInYear()" % self.varId)

  def isValid(self):
    """
    Description:
    ------------

    Related Pages:

      https://momentjs.com/docs/#/parsing/is-valid/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.isValid()" % self.varId)

  def invalid(self):
    """
    Description:
    ------------
    You can create your own invalid Moment objects, which is useful in making your own parser.

    Related Pages:

      https://momentjs.com/docs/#/utilities/invalid/
    """

  def format(self, value=None):
    """
    Description:
    ------------
    This is the most robust display option.
    It takes a string of tokens and replaces them with their corresponding values.

    Related Pages:

      https://momentjs.com/docs/#/displaying/format/

    Attributes:
    ----------
    :param value: Object. Optional. The format definition.
    """
    if value is None:
      return JsObjects.JsObjects.get("%s.format()" % self.varId)

    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get("%s.format(%s)" % (self.varId, value))

  def quarter(self, number=None):
    """
    Description:
    ------------
    Gets / Sets the quarter (1 to 4).

    Related Pages:

      https://momentjs.com/docs/#/get-set/quarter/

    Attributes:
    ----------
    :param number: Number. Optional. The quarter's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.quarter()" % self.varId)

    return JsUtils.jsWrap("%s.quarter(%s)" % (self.varId, number))

  def add(self, unit, value, varName=None):
    """
    Description:
    ------------
    Add value.

    Related Pages:

      https://momentjs.com/docs/#/displaying/difference/

    Attributes:
    ----------
    :param unit: Integer.
    :param value: String.
    :param varName: String. Optional. The variable name created in the Javascript.
    """
    unit = JsUtils.jsConvertData(unit, None)
    value = JsUtils.jsConvertData(value, None)
    if varName is not None:
      return MomentDate(selector="%s.add(%s, %s)" % (self.varId, unit, value), varName=varName, setVar=True)

    return MomentDate(selector="%s.add(%s, %s)" % (self.varId, unit, value), setVar=False)

  def subtract(self, unit, value, varName=None):
    """
    Description:
    ------------
    Subtract value.

    Related Pages:

      https://momentjs.com/docs/#/displaying/difference/

    Attributes:
    ----------
    :param unit: Integer.
    :param value: String.
    :param varName: String. Optional. The variable name created in the Javascript.
    """
    unit = JsUtils.jsConvertData(unit, None)
    value = JsUtils.jsConvertData(value, None)
    if varName is not None:
      return MomentDate(selector="%s.subtract(%s, %s)" % (self.varId, unit, value), varName=varName, setVar=True)

    return MomentDate(selector="%s.subtract(%s, %s)" % (self.varId, unit, value), setVar=False)

  def year(self, number=None):
    """
    Description:
    ------------
    Gets or sets the year..

    Related Pages:

      https://momentjs.com/docs/#/get-set/year/

    Attributes:
    ----------
    :param number: Number. Optional. The year's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.year()" % self.varId)

    return JsUtils.jsWrap("%s.year(%s)" % (self.varId, number))

  def clone(self, varName=None):
    """
    Description:
    ------------
    All moments are mutable. If you want a clone of a moment, you can do so implicitly or explicitly.

    Related Pages:

      https://momentjs.com/docs/#/parsing/moment-clone/

    Attributes:
    ----------
    :param varName: String. Optional. The variable name created in the Javascript.
    """
    if varName is not None:
      return MomentDate(selector="%s.clone()" % self.varId, varName=varName, setVar=True)

    return MomentDate(selector="%s.clone()" % self.varId, setVar=False)

  def date(self, number=None):
    """
    Description:
    ------------
    Gets or sets the day of the month.

    Accepts numbers from 1 to 31. If the range is exceeded, it will bubble up to the months.

    Related Pages:

      https://momentjs.com/docs/#/get-set/date/

    Attributes:
    ----------
    :param number: Number. Optional. The month number of days.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.date()" % self.varId)

    return JsUtils.jsWrap("%s.date(%s)" % (self.varId, number))

  def isoWeek(self, number=None):
    """
    Description:
    ------------
    Gets or sets the ISO week of the year.

    When setting the week of the year, the day of the week is retained.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-week/

    Attributes:
    ----------
    :param number: Number. Optional. The year's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.isoWeek()" % self.varId)

    return JsUtils.jsWrap("%s.isoWeek(%s)" % (self.varId, number))

  def isoWeekday(self, number=None):
    """
    Description:
    ------------
    Gets or sets the ISO day of the week with 1 being Monday and 7 being Sunday.

    As with moment#day, if the range is exceeded, it will bubble up to other weeks.

    Related Pages:

      https://momentjs.com/docs/#/get-set/iso-weekday/

    Attributes:
    ----------
    :param number: Number. Optional. The year's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.isoWeekday()" % self.varId)

    return JsUtils.jsWrap("%s.isoWeekday(%s)" % (self.varId, number))

  def weekday(self, number=None):
    """
    Description:
    ------------
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
    Description:
    ------------
    Gets or sets the day of the year.

    Accepts numbers from 1 to 366. If the range is exceeded, it will bubble up to the years.

    Related Pages:

      https://momentjs.com/docs/#/get-set/min/

    Attributes:
    ----------
    :param number: Number. Optional. The day of year number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.dayOfYear()" % self.varId)

    return JsUtils.jsWrap("%s.dayOfYear(%s)" % (self.varId, number))

  def day(self, number=None):
    """
    Description:
    ------------
    Gets or sets the day of the week.

    This method can be used to set the day of the week, with Sunday as 0 and Saturday as 6.

    Related Pages:

      https://momentjs.com/docs/#/get-set/day/

    Attributes:
    ----------
    :param number: Number. Optional. The day's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.day()" % self.varId)

    return JsUtils.jsWrap("%s.day(%s)" % (self.varId, number))

  def days(self, number=None):
    """
    Description:
    ------------
    Gets or sets the day of the week.

    This method can be used to set the day of the week, with Sunday as 0 and Saturday as 6.

    Related Pages:

      https://momentjs.com/docs/#/get-set/day/

    Attributes:
    ----------
    :param number: Number. Optional. The day's number.
    """
    return self.day(number)

  def second(self, number=None):
    """
    Description:
    ------------
    Gets or sets the seconds.

    Accepts numbers from 0 to 59. If the range is exceeded, it will bubble up to the minutes.

    Related Pages:

      https://momentjs.com/docs/#/get-set/second/

    Attributes:
    ----------
    :param number: Number. Optional. The second's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.second()" % self.varId)

    return JsUtils.jsWrap("%s.second(%s)" % (self.varId, number))

  def seconds(self, number=None):
    """
    Description:
    ------------
    Gets or sets the seconds.

    Accepts numbers from 0 to 59. If the range is exceeded, it will bubble up to the minutes.

    Related Pages:

      https://momentjs.com/docs/#/get-set/second/

    Attributes:
    ----------
    :param number: Number. Optional. The second's number.
    """
    return self.day(number)

  def minute(self, number=None):
    """
    Description:
    ------------
    Gets or sets the minutes.

    Accepts numbers from 0 to 59. If the range is exceeded, it will bubble up to the hour.

    Related Pages:

      https://momentjs.com/docs/#/get-set/minute/

    Attributes:
    ----------
    :param number: Number. Optional. The minute's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.second()" % self.varId)

    return JsUtils.jsWrap("%s.second(%s)" % (self.varId, number))

  def minutes(self, number=None):
    """
    Description:
    ------------
    Gets or sets the minutes.

    Accepts numbers from 0 to 59. If the range is exceeded, it will bubble up to the hour.

    Related Pages:

      https://momentjs.com/docs/#/get-set/minute/

    Attributes:
    ----------
    :param number: Number. Optional. The minute's number.
    """
    return self.minute(number)

  def hour(self, number=None):
    """
    Description:
    ------------
    Gets or sets the hour.

    Accepts numbers from 0 to 23. If the range is exceeded, it will bubble up to the day.

    Related Pages:

      https://momentjs.com/docs/#/get-set/hour/

    Attributes:
    ----------
    :param number: Number. Optional. The hour's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.hour()" % self.varId)

    return JsUtils.jsWrap("%s.hour(%s)" % (self.varId, number))

  def hours(self, number=None):
    """
    Description:
    ------------
    Gets or sets the hour.

    Accepts numbers from 0 to 23. If the range is exceeded, it will bubble up to the day.

    Related Pages:

      https://momentjs.com/docs/#/get-set/hour/

    Attributes:
    ----------
    :param number: Number. Optional. The hour's number.
    """
    return self.hour(number)

  def utcOffset(self, number=None, flag=None):
    """
    Description:
    ------------
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
    pass

  def creationData(self):
    """
    Description:
    ------------
    After a moment object is created, all of the inputs can be accessed with creationData() method:

    Related Pages:

      https://momentjs.com/docs/#/parsing/creation-data/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.creationData()" % self.varId)

  def millisecond(self, number=None):
    """
    Description:
    ------------
    Gets or sets the milliseconds.

    Accepts numbers from 0 to 999. If the range is exceeded, it will bubble up to the seconds.

    Related Pages:

      https://momentjs.com/docs/#/get-set/millisecond/

    Attributes:
    ----------
    :param number: Number. Optional. The second's number.
    """
    if number is None:
      return JsObjects.JsNumber.JsNumber.get("%s.millisecond()" % self.varId)

    return JsUtils.jsWrap("%s.millisecond(%s)" % (self.varId, number))

  def milliseconds(self, number=None):
    """
    Description:
    ------------
    Gets or sets the milliseconds.

    Accepts numbers from 0 to 999. If the range is exceeded, it will bubble up to the seconds.

    Related Pages:

      https://momentjs.com/docs/#/get-set/millisecond/

    Attributes:
    ----------
    :param number: Number. Optional. The second's number.
    """
    return self.millisecond(number)

  def startOf(self, text):
    """
    Description:
    ------------
    Mutates the original moment by setting it to the start of a unit of time.

    Related Pages:

      https://momentjs.com/docs/#/manipulating/start-of/
    """
    text = JsUtils.jsConvertData(text, None)
    return JsObjects.JsNumber.JsNumber.get("%s.startOf(%s)" % (self.varId, text))

  def endOf(self, text):
    """
    Description:
    ------------
    Mutates the original moment by setting it to the end of a unit of time.

    Related Pages:

      https://momentjs.com/docs/#/manipulating/end-of/
    """
    text = JsUtils.jsConvertData(text, None)
    return JsObjects.JsNumber.JsNumber.get("%s.endOf(%s)" % (self.varId, text))

  def fromNow(self, flag=None):
    """
    Description:
    ------------
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
    Description:
    ------------
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
    Description:
    ------------
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
    Description:
    ------------
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
    Description:
    ------------
    To get the difference in milliseconds, use moment#diff like you would use moment#from

    Related Pages:

      https://momentjs.com/docs/#/displaying/difference/
    """
    dt = JsUtils.jsConvertData(dt, None)
    return JsObjects.JsNumber.JsNumber.get("%s.diff(%s)" % (self.varId, dt))

  def daysInMonth(self):
    """
    Description:
    ------------
    Get the number of days in the current month.

    Related Pages:

      https://momentjs.com/docs/#/displaying/days-in-month/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.daysInMonth()" % self.varId)

  def toDate(self):
    """
    Description:
    ------------
    To get a copy of the native Date object that Moment.js wraps, use moment#toDate.

    Related Pages:

      https://momentjs.com/docs/#/displaying/as-javascript-date/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.toDate()" % self.varId)

  def toArray(self):
    """
    Description:
    ------------
    This returns an array that mirrors the parameters from new Date().

    Related Pages:

      https://momentjs.com/docs/#/displaying/as-array/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.toArray()" % self.varId)

  def toJSON(self):
    """
    Description:
    ------------
    When serializing an object to JSON, if there is a Moment object, it will be represented as an ISO8601 string,
    adjusted to UTC.

    Related Pages:

      https://momentjs.com/docs/#/displaying/as-json/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.toJSON()" % self.varId)

  def toISOString(self, keepOffset=None):
    """
    Description:
    ------------
    Formats a string to the ISO8601 standard.

    Related Pages:

      https://momentjs.com/docs/#/displaying/as-iso-string/

    Attributes:
    ----------
    :param keepOffset: Boolean. Optional.
    """
    if keepOffset is None:
      return JsObjects.JsNumber.JsNumber.get("%s.toISOString()" % self.varId)

    keepOffset = JsUtils.jsConvertData(keepOffset, None)
    return JsObjects.JsNumber.JsNumber.get("%s.toISOString(%s)" % (self.varId, keepOffset))

  def inspect(self):
    """
    Description:
    ------------
    Returns a machine readable string, that can be evaluated to produce the same moment.
    Because of the name its also used in node interactive shell to display objects.

    Related Pages:

      https://momentjs.com/docs/#/displaying/inspect/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.inspect()" % self.varId)

  def isBefore(self, value, precision=None):
    """
    Description:
    ------------
    Check if a moment is before another moment.

    Related Pages:

      https://momentjs.com/docs/#/query/is-before/

    Attributes:
    ----------
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
    Description:
    ------------
    Check if a moment is after another moment. The first argument will be parsed as a moment, if not already so.

    Related Pages:

      https://momentjs.com/docs/#/query/is-after/

    Attributes:
    ----------
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
    Description:
    ------------
    Check if a moment is before or the same as another moment. The first argument will be parsed as a moment,
    if not already so.

    Related Pages:

      https://momentjs.com/docs/#/query/is-same-or-before/

    Attributes:
    ----------
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
    Description:
    ------------
    Check if a moment is after or the same as another moment. The first argument will be parsed as a moment,
    if not already so.

    Related Pages:

      https://momentjs.com/docs/#/query/is-same-or-after/

    Attributes:
    ----------
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
    Description:
    ------------
    Check if a moment is between two other moments, optionally looking at unit scale (minutes, hours, days, etc).

    Related Pages:

      https://momentjs.com/docs/#/query/is-between/

    Attributes:
    ----------
    :param dt1: Object. The start date for the range.
    :param dt2: Object. optional. The end date for the range. (Default undefined).
    """
    dt1 = JsUtils.jsConvertData(dt1, None)
    dt2 = JsUtils.jsConvertData(dt2, None)
    return JsObjects.JsBoolean.JsBoolean.get("%s.isBetween(%s, %s)" % (self.varId, dt1, dt2))

  def isSame(self, value, precision=None):
    """
    Description:
    ------------
    Check if a moment is the same as another moment. The first argument will be parsed as a moment, if not already so.

    Related Pages:

      https://momentjs.com/docs/#/query/is-same/

    Attributes:
    ----------
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
    Description:
    ------------
    moment#isDST checks if the current moment is in daylight saving time

    Related Pages:

      https://momentjs.com/docs/#/query/is-daylight-saving-time/
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.isDST()" % self.varId)

  def isLeapYear(self):
    """
    Description:
    ------------
    moment#isLeapYear returns true if that year is a leap year, and false if it is not.

    Related Pages:

      https://momentjs.com/docs/#/query/is-daylight-saving-time/
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.isLeapYear()" % self.varId)

  def unix(self):
    """
    Description:
    ------------
    moment#unix outputs a Unix timestamp (the number of seconds since the Unix Epoch).

    Related Pages:

      https://momentjs.com/docs/#/displaying/unix-timestamp/
    """
    return JsObjects.JsNumber.JsNumber.get("%s.unix()" % self.varId)


class Moment(JsPackage):

  lib_alias = {"js": 'moment'}
  lib_selector = 'moment'

  def now(self, varName=None):
    """
    Description:
    ------------
    To get the current date and time, just call moment() with no parameters.

    Related Pages:

      https://momentjs.com/docs/#/parsing/now/

    Attributes:
    ----------
    :param varName: String. Optional. The variable name created in the Javascript.
    """
    if varName is not None:
      return MomentDate(selector="moment()", varName=varName, setVar=True)

    return MomentDate(selector="moment()", setVar=False)

  def time(self, hour, minute, second, varName=None):
    """
    Description:
    ------------
    To get the current time, just call moment() with no parameters.

    Related Pages:

      https://momentjs.com/docs/#/parsing/now/

    Attributes:
    ----------
    :param hour: Integer. Optional. The hours' value
    :param minute: Integer. Optional. The minutes' value.
    :param second: Integer. Optional. The seconds' value.
    :param varName: String. Optional. The variable name created in the Javascript.
    """
    if varName is not None:
      return MomentDate(
        selector="moment().hour(%s).minute(%s).second(%s)" % (hour, minute, second), varName=varName, setVar=True)

    return MomentDate(selector="moment().hour(%s).minute(%s).second(%s)" % (hour, minute, second), setVar=False)

  def var(self, varName):
    """
    Description:
    ------------
    Get the defined moment variable.

    Related Pages:

      https://momentjs.com/docs/#/parsing/now/

    Attributes:
    ----------
    :param varName: String. Optional. The variable name created in the Javascript.
    """
    return MomentDate(selector=varName, setVar=False)

  def new(self, date=None, format=None, varName=None):
    """
    Description:
    ------------
    When creating a moment from a string, we first check if the string matches known ISO 8601 formats,

    Related Pages:

      https://momentjs.com/docs/#/parsing/string/

    Attributes:
    ----------
    :param date:
    :param format:
    :param varName: String. Optional. The variable name created in the Javascript.
    """
    if date is None:
      return self.now()

    date = JsUtils.jsConvertData(date, None)
    if format is None:
      if varName is not None:
        return MomentDate(selector="moment(%s)" % date, varName=varName, setVar=True)

      return MomentDate(selector="moment(%s)" % date, setVar=False)

    format = JsUtils.jsConvertData(format, None)
    if varName is not None:
      return MomentDate(selector="moment(%s, %s)" % (date, format), varName=varName, setVar=True)

    return MomentDate(selector="moment(%s, %s)" % (date, format), setVar=False)

  def parseZone(self, date=None, format=None, varName=None):
    """
    Description:
    ------------

    Related Pages:

      https://momentjs.com/docs/#/parsing/parse-zone/

    Attributes:
    ----------
    :param date:
    :param format:
    :param varName: String. Optional. The variable name created in the Javascript.
    """
    if date is None:
      if varName is not None:
        return MomentDate(selector="%s.parseZone()" % self.varId, varName=varName, setVar=True)

      return MomentDate(selector="%s.parseZone()" % self.varId, setVar=False)

    date = JsUtils.jsConvertData(date, None)
    if format is None:
      if varName is not None:
        return MomentDate(selector="%s.parseZone(%s)" % (self.varId, date), varName=varName, setVar=True)

      return MomentDate(selector="%s.parseZone(%s)" % (self.varId, date), setVar=False)

    format = JsUtils.jsConvertData(format, None)
    if varName is not None:
      return MomentDate(selector="%s.parseZone(%s, %s)" % (self.varId, date, format), varName=varName, setVar=True)

    return MomentDate(selector="%s.parseZone(%s, %s)" % (self.varId, date, format), setVar=False)

  def isMoment(self):
    """
    Description:
    ------------
    To check if a variable is a moment object, use moment.isMoment().

    Related Pages:

      https://momentjs.com/docs/#/query/is-a-moment/
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.isMoment()" % self.varId)

  def isDate(self):
    """
    Description:
    ------------
    To check if a variable is a native js Date object, use moment.isDate().

    Related Pages:

      https://momentjs.com/docs/#/query/is-a-date/
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.isDate()" % self.varId)

  def lang(self, value):
    """
    Description:
    ------------
    The local lang

    Related Pages:

      https://momentjs.com/docs/#/i18n/changing-locale/

    Attributes:
    ----------
    :param value: String. The lang reference.
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

  def locale(self, value="en"):
    """
    Description:
    ------------

    Related Pages:

      https://momentjs.com/docs/#/i18n/changing-locale/

    Attributes:
    ----------
    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    return JsUtils.jsWrap("%s.locale(%s)" % (self.varId, value))

  def locales(self):
    """
    Description:
    ------------
    As of version 2.12.0 it is possible to list all locales that have been loaded and are available to use:

    Related Pages:

      https://momentjs.com/docs/#/i18n/getting-locale/
    """
    return JsUtils.jsWrap("%s.locales()" % self.varId)

  def updateLocale(self, category, values):
    """
    Description:
    ------------

    Related Pages:

      https://momentjs.com/docs/#/customization/month-names/

    Attributes:
    ----------
    :param category: String.
    :param values: Dictionary.
    """
    category = JsUtils.jsConvertData(category, None)
    values = JsUtils.jsConvertData(values, None)
    return JsUtils.jsWrap("%s.updateLocale(%s, %s)" % (self.varId, category, values))

  def utc(self, value=None, varName=None):
    """
    Description:
    ------------
    By default, moment parses and displays in local time.

    If you want to parse or display a moment in UTC, you can use moment.utc() instead of moment().

    Related Pages:

      https://momentjs.com/docs/#/parsing/utc/

    Attributes:
    ----------
    :param value:
    :param varName: String. Optional. The variable name created in the Javascript.
    """
    if value is None:
      if varName is not None:
        return MomentDate(selector="%s.utc()" % self.varId, varName=varName, setVar=True)

      return MomentDate(selector="%s.utc()" % self.varId, setVar=False)

    value = JsUtils.jsConvertData(value, None)
    if varName is not None:
      return MomentDate(selector="%s.utc(%s)" % (self.varId, value), varName=varName, setVar=True)

    return MomentDate(selector="%s.utc(%s)" % (self.varId, value), setVar=False)

  def months(self):
    """
    Description:
    ------------
    Returns the list of months in the current locale.

    Related Pages:

      https://momentjs.com/docs/#/i18n/listing-months-weekdays/
    """
    return JsObjects.JsArray.JsArray.get("%s.months()" % self.varId)

  def weekdays(self, value, index=None):
    """
    Description:
    ------------
    Week days names.

    Related Pages:

      https://momentjs.com/docs/#/i18n/listing-months-weekdays/
      https://momentjs.com/docs/#/customization/weekday-names/

    Attributes:
    ----------
    :param value:
    :param index:
    """
    value = JsUtils.jsConvertData(value, None)
    if index is None:
      return JsObjects.JsArray.JsArray.get("%s.weekdays(%s)" % (self.varId, value))

    return JsObjects.JsArray.JsArray.get("%s.weekdays(%s, %s)" % (self.varId, value, index))

  def weekdaysShort(self, value=None, index=None):
    """
    Description:
    ------------
    Weekdays abbreviations.

    Related Pages:

      https://momentjs.com/docs/#/i18n/listing-months-weekdays/
      https://momentjs.com/docs/#/customization/weekday-abbreviations/

    Attributes:
    ----------
    :param value:
    :param index:
    """
    if value is None:
      return JsObjects.JsArray.JsArray.get("%s.weekdaysShort()" % self.varId)

    value = JsUtils.jsConvertData(value, None)
    if index is None:
      return JsObjects.JsArray.JsArray.get("%s.weekdaysShort(%s)" % (self.varId, value))

    return JsObjects.JsArray.JsArray.get("%s.weekdaysShort(%s, %s)" % (self.varId, value, index))

  def weekdaysMin(self, value=None, index=None):
    """
    Description:
    ------------
    Minimal Weekday Abbreviations.

    Related Pages:

      https://momentjs.com/docs/#/i18n/listing-months-weekdays/
      https://momentjs.com/docs/#/customization/weekday-min/

    Attributes:
    ----------
    :param value:
    :param index:
    """
    if value is None:
      return JsObjects.JsArray.JsArray.get("%s.weekdaysMin()" % self.varId)

    value = JsUtils.jsConvertData(value, None)
    if index is None:
      return JsObjects.JsArray.JsArray.get("%s.weekdaysMin(%s)" % (self.varId, value))

    return JsObjects.JsArray.JsArray.get("%s.weekdaysMin(%s, %s)" % (self.varId, value, index))

  def monthsShort(self, value=None, index=None):
    """
    Description:
    ------------
    Month abbreviations.

    Related Pages:

      https://momentjs.com/docs/#/i18n/listing-months-weekdays/
      https://momentjs.com/docs/#/customization/month-abbreviations/

    Attributes:
    ----------
    :param value:
    :param index:
    """
    if value is None:
      return JsObjects.JsArray.JsArray.get("%s.monthsShort()" % self.varId)

    value = JsUtils.jsConvertData(value, None)
    if index is None:
      return JsObjects.JsArray.JsArray.get("%s.monthsShort(%s)" % (self.varId, value))

    return JsObjects.JsArray.JsArray.get("%s.monthsShort(%s, %s)" % (self.varId, value, index))

