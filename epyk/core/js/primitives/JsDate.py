
from typing import Optional, Union
from epyk.core.py import primitives
import json

from epyk.core.js.primitives import JsObject
from epyk.core.js import JsUtils

MONTHS = [
  'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
  'December'
]


class JsDate(JsObject.JsObject):
  _jsClass = "Date"

  def __init__(self, data=None, js_code: Optional[str] = None, set_var: bool = False, is_py_data: bool = False,
               local_time: bool = True, page: primitives.PageModel = None):
    """ Create a JavaScript date object.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_date.asp
 
    :param data:
    :param js_code: Optional.
    :param set_var: Optional.
    :param is_py_data: Optional.
    :param local_time: Optional. Flag to return the local time or the ISO date time.
    """
    if set_var:
      if data is not None:
        is_py_data = False
        data = "new Date(%s)" % json.dumps(data) if is_py_data else "new Date(%s)" % data
    date_expr = ""
    if local_time:
      date_expr = "(function(date){return date.getTime() - (date.getTimezoneOffset() * 60000)})(new Date())"
    if data is None:
      is_py_data = False
      data = "new Date(%s)" % date_expr if set_var else "(new Date(%s))" % date_expr
    if not hasattr(data, 'varName') and is_py_data:
      is_py_data = True
      data = "new Date(%s)" % json.dumps(data)
    super(JsDate, self).__init__(data=data, js_code=js_code, set_var=set_var, is_py_data=is_py_data, page=page)

  @classmethod
  def get(cls, js_code: str):
    """ Get the Javascript Object by its reference.

    Usage::

      JsDate.new("2019-05-03", varName="MyDate")
      JsDate.get("MyDate")

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_date.asp
 
    :param js_code: The Javascript object reference.

    :return: The python Javascript object
    """
    if "-" in js_code:
      # assume it a valid date
      return cls(data=None, js_code='new Date("%s")' % js_code, set_var=False)

    JsUtils.getJsValid(js_code)
    return cls(data=None, js_code=js_code, set_var=False)

  @property
  def isWeedend(self):
    """   

    Usage::

      page.js.objects.date.get("dateTest").isWeedend
    """
    from epyk.core.js.primitives import JsBoolean
    return JsBoolean.JsBoolean("(%(varId)s.getDay() === 6) || (%(varId)s.getDay() === 0)" % {
      "varId": self.varId}, is_py_data=False)

  @staticmethod
  def now():
    """ The Date.now() method returns the number of milliseconds since January 1, 1970 00:00:00 UTC.

    Usage::

      page.js.objects.date.now()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_now.asp

    :return: A Number, representing the number of milliseconds since midnight January 1, 1970
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("Date.now()", is_py_data=False)

  @staticmethod
  def today():
    """ Return the String date in the standard format YYYY-MM-DD.

    Usage::

      page.js.objects.date.today()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A Python / Javascript object
    """
    from epyk.core.js.primitives import JsString
    return JsString.JsString("function(){return new Date}().toISOString().slice(0, 10)", is_py_data=False)

  def getDate(self):
    """ The getDate() method returns the day of the month (from 1 to 31) for the specified date.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_getdate.asp
    """
    return JsDate("%s.getDate()" % self.varId, is_py_data=False, page=self.page)

  def getDay(self):
    """ The getDay() method returns the day of the week (from 0 to 6) for the specified date.

    Usage::

      page.js.objects.date.new("2019-01-01", varName="dateTest")
      page.js.objects.date.get("dateTest").getDay()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_getday.asp
    """
    from epyk.core.js.primitives import JsNumber
    return JsNumber.JsNumber("%s.getDay()" % self.varId, is_py_data=False)

  def getFullYear(self):
    """ The getFullYear() method returns the year (four digits for dates between year 1000 and 9999) of
    the specified date.

    Usage::

      page.js.objects.date.new("2019-01-01", varName="dateTest")
      page.js.objects.date.get("dateTest").getFullYear()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_getfullyear.asp

    :return: A Number, representing the year of the specified date
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.getFullYear()" % self.varId, is_py_data=False)

  def getHours(self):
    """ The getHours() method returns the hour (from 0 to 23) of the specified date and time.

    Usage::

      page.js.objects.date.new("2019-01-01", varName="dateTest")
      page.js.objects.date.get("dateTest").getHours()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_gethours.asp

    :return: A Number, from 0 to 23, representing the hour
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.getHours()" % self.varId, is_py_data=False)

  def getMilliseconds(self):
    """ The getMilliseconds() method returns the milliseconds (from 0 to 999) of the specified date and time.

    Usage::

      page.js.objects.date.new("2019-01-01", varName="dateTest")
      page.js.objects.date.get("dateTest").getMilliseconds()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_getmilliseconds.asp

    :return: A Number, from 0 to 999, representing milliseconds
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.getMilliseconds()" % self.varId, is_py_data=False)

  def getMonth(self):
    """ The getMonth() method returns the month (from 0 to 11) for the specified date, according to local time.

    Usage::

      page.js.objects.date.new("2019-01-01", varName="dateTest")
      page.js.objects.date.get("dateTest").getMonth()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_getmonth.asp

    :return: A Number, from 0 to 11, representing the month
    """
    from epyk.core.js.primitives import JsNumber
    return JsNumber.JsNumber("%s.getMonth()" % self.varId, is_py_data=False)

  def getMonthName(self):
    """ Use getMonth() method returns the month name from the definition in the module.

    Usage::

      page.js.objects.date.new("2019-01-01", varName="dateTest")
      page.js.objects.date.get("dateTest").getMonthName()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_getmonth.asp

    :return: A Number, from 0 to 11, representing the month
    """
    from epyk.core.js.primitives import JsNumber
    return JsNumber.JsNumber("(function(x){return %s[x]})(%s.getMonth())" % (MONTHS, self.varId), is_py_data=False)

  def setDate(self, day: Union[primitives.JsDataModel, int]):
    """ The setDate() method sets the day of the month to the date object.

    Usage::

      page.js.objects.date.new("2019-01-01", varName="dateTest")
      page.js.objects.date.get("dateTest").setDate(5)

    Related Pages:

      https://www.w3schools.com/jsref/jsref_setdate.asp
 
    :param day: An integer representing the day of a month

    :return: A Number, representing the number of milliseconds between the date object and midnight January 1 1970
    """
    return JsDate("%s.setDate(%s)" % (self.varId, day), is_py_data=False, page=self.page)

  def setMonth(self, month: Union[primitives.JsDataModel, int], day: Union[primitives.JsDataModel, int] = None):
    """ The setMonth() method sets the month of a date object.
    Return a new date object.

    Usage::

      page.js.objects.date.new("2019-01-01", varName="dateTest")
      page.js.objects.date.get("dateTest").setMonth(5)

    Related Pages:

      https://www.w3schools.com/jsref/jsref_setmonth.asp
 
    :param month: An integer representing the month
    :param day: Optional. An integer representing the day of month

    :return: A Number, representing the number of milliseconds between the date object and midnight January 1 1970
    """
    if day is not None:
      return JsDate("new Date(%s.setMonth(%s, %s))" % (self.varId, month, day), is_py_data=False, page=self.page)

    return JsDate("new Date(%s.setMonth(%s))" % (self.varId, month), is_py_data=False, page=self.page)

  def toDateString(self):
    """ The toDateString() method converts the date (not the time) of a Date object into a readable string.

    Usage::

      jsType.date.new(varName="Test")
      jsType.date.get("Test").toDateString()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_todatestring.asp

    :return: A String, representing the date as a string
    """
    from epyk.core.js.primitives import JsString

    return JsString.JsString("%s.toDateString()" % self.varId, is_py_data=False)

  def toISOString(self):
    """ The toISOString() method converts a Date object into a string, using the ISO standard.

    Usage::

      jsType.date.new(varName="Test")
      jsType.date.get("Test").toISOString()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A String, representing the date and time using the ISO standard format.
    """
    from epyk.core.js.primitives import JsString

    return JsString.JsString("%s.toISOString()" % self.varId, is_py_data=False)

  def getStrDate(self):
    """ Return the String date in the standard format YYYY-MM-DD.

    Usage::

      page.js.objects.date.new("2019-01-01", varName="dateTest")
      jsType.date.get("dateTest").getStrDate()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A Python / Javascript object
    """
    from epyk.core.js.primitives import JsString

    return JsString.JsString("%s.toISOString().slice(0, 10)" % self.varId, is_py_data=False)

  def getStrTimeStamp(self):
    """ The toISOString() method converts a Date object into a string, using the ISO standard.

    Usage::

      page.js.objects.date.new("2019-01-01", varName="dateTest")
      jsType.date.get("dateTest").getStrTimeStamp()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A Python / Javascript object
    """
    from epyk.core.js.primitives import JsString

    return JsString.JsString("%s.toISOString().replace('T', ' ').slice(0, 19)" % self.varId, is_py_data=False)

  def getTime(self, in_seconds: bool = True, js_code: str = None, set_var: bool = False):
    """ To get the unix timestamp using JavaScript you need to use the getTime() function of the build in Date object.
    As this returns the number of milliseconds then we must divide the number by 1000 and round it in order to get the
    timestamp in seconds.
 
    :param in_seconds: In second conversion of the Javascript timestamp
    :param js_code:
    :param set_var:
    """
    from epyk.core.js.primitives import JsNumber
    if js_code is not None:
      set_var = True
    if in_seconds:
      return JsNumber.JsNumber("%s.getTime()/1000" % self.varId, js_code=js_code, set_var=set_var, is_py_data=False)

    return JsNumber.JsNumber("%s.getTime()" % self.varId, js_code=js_code, set_var=set_var, is_py_data=False)

  def add(self, n: Union[primitives.JsDataModel, int]):
    """ Simple wrapper to the Javascript add method.
    This will just return the Js string corresponding to the add.

    This function is used in the addDays method.

    Usage::

      page.js.objects.date.this().getDate().add(1)
 
    :param n: the number of days.

    :return: A Python Js object
    """
    js_data = JsUtils.jsConvertData(n, None)
    return super(JsDate, self).add(js_data)

  def addDays(self, js_obj, n: int, weekend: bool = False):
    """ Add some days to a Javascript date.

    Usage::

      page.js.objects.date.get("MyDate").addDays(jsObj, 6).getStrDate()

    Related Pages:

      https://stackoverflow.com/questions/563406/add-days-to-javascript-date
 
    :param js_obj: The internal JS object used to store the prototype extension
    :param int n: The number of days to be added
    :param weekend: Optional. flag to specify if the weekends should be considered in the count. Default False

    :type js_obj: epyk.Lib.js.Js.JsBase
    """
    js_obj.extendProto(self, "addDays", [
      js_obj.objects.date.this().setDate(js_obj.objects.date.this().getDate().add(js_obj.parseInt(js_obj.objects.get("n")))),
      js_obj.if_([js_obj.objects.date.this().isWeedend, js_obj.objects.boolean.get("weekend").not_], [
        js_obj.if_(js_obj.objects.date.this().getDay() == 0, js_obj.objects.date.this().setDate(js_obj.objects.date.this().getDate().add(1))),
        js_obj.if_(js_obj.objects.date.this().getDay() == 6, js_obj.objects.date.this().setDate(js_obj.objects.date.this().getDate().add(2)))
      ]),
      js_obj.return_(js_obj.objects.date.this())
    ], pmts=["n", "weekend"])
    return JsDate("%s.addDays(%s, %s)" % (self.varId, n, json.dumps(weekend)), page=self.page)
