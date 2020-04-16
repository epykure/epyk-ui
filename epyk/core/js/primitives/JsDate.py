"""
Module dedicated to wrap the Javascript Date

https://www.w3schools.com/jsref/jsref_obj_date.asp
"""


import json

from epyk.core.js.primitives import JsObject
from epyk.core.js import JsUtils

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


class JsDate(JsObject.JsObject):
  _jsClass = "Date"

  def __init__(self, data=None, varName=None, setVar=False, isPyData=False):
    """
    Description:
    -----------

    Related Pages:


    https://www.w3schools.com/jsref/jsref_obj_date.asp

    Attributes:
    ----------
    :param data: Required,
    :param varName: Optional,
    :param setVar: Optional,
    """
    if setVar:
      if data is not None:
        isPyData = False
        data = "new Date(%s)" % json.dumps(data) if isPyData else "new Date(%s)" % data
    if data is None:
      isPyData = False
      data = "new Date()"
    if not hasattr(data, 'varName') and isPyData:
      isPyData = True
      data = "new Date(%s)" % json.dumps(data)
    super(JsDate, self).__init__(data=data, varName=varName, setVar=setVar, isPyData=isPyData)

  @classmethod
  def get(cls, varName):
    """
    Description:
    -----------
    Get the Javascript Object by its reference

    Usage::

      JsDate.new("2019-05-03", varName="MyDate")
      JsDate.get("MyDate")

    Related Pages:


    https://www.w3schools.com/jsref/jsref_obj_date.asp

    Attributes:
    ----------
    :param varName: The Javascript object reference

    :return: The python Javascript object
    """
    if "-" in varName:
      # assume it a valid date
      return cls(data=None, varName='new Date("%s")' % varName, setVar=False)

    JsUtils.getJsValid(varName)
    return cls(data=None, varName=varName, setVar=False)

  @property
  def isWeedend(self):
    """
    Description:
    -----------

    Usage::

      jsObj.objects.date.get("dateTest").isWeedend
    """
    from epyk.core.js.primitives import JsBoolean
    return JsBoolean.JsBoolean("(%(varId)s.getDay() === 6) || (%(varId)s.getDay() === 0)" % {"varId": self.varId}, isPyData=False)

  @staticmethod
  def now():
    """
    Description:
    -----------
    The Date.now() method returns the number of milliseconds since January 1, 1970 00:00:00 UTC.

    Usage::

      jsObj.objects.date.now()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_now.asp

    :return: A Number, representing the number of milliseconds since midnight January 1, 1970
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("Date.now()", isPyData=False)

  @staticmethod
  def today():
    """
    Description:
    -----------
    Return the String date in the standard format YYYY-MM-DD

    Usage::

      rptObj.js.objects.date.today()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A Python / Javascript object
    """
    from epyk.core.js.primitives import JsString
    return JsString.JsString("function(){return new Date}().toISOString().slice(0, 10)", isPyData=False)

  def getDate(self):
    """
    Description:
    -----------
    The getDate() method returns the day of the month (from 1 to 31) for the specified date.

    Related Pages:


    https://www.w3schools.com/jsref/jsref_getdate.asp

    :return:
    """
    return JsDate("%s.getDate()" % self.varId, isPyData=False)

  def getDay(self):
    """
    Description:
    -----------
    The getDay() method returns the day of the week (from 0 to 6) for the specified date.

    Usage::

      jsObj.objects.date.new("2019-01-01", varName="dateTest")
      jsObj.objects.date.get("dateTest").getDay()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_getday.asp

    :return:
    """
    from epyk.core.js.primitives import JsNumber
    return JsNumber.JsNumber("%s.getDay()" % self.varId, isPyData=False)

  def getFullYear(self):
    """
    Description:
    -----------
    The getFullYear() method returns the year (four digits for dates between year 1000 and 9999) of the specified date.

    Usage::

      jsObj.objects.date.new("2019-01-01", varName="dateTest")
      jsObj.objects.date.get("dateTest").getFullYear()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_getfullyear.asp

    :return: A Number, representing the year of the specified date
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.getFullYear()" % self.varId, isPyData=False)

  def getHours(self):
    """
    Description:
    -----------
    The getHours() method returns the hour (from 0 to 23) of the specified date and time.

    Usage::

      jsObj.objects.date.new("2019-01-01", varName="dateTest")
      jsObj.objects.date.get("dateTest").getHours()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_gethours.asp

    :return: A Number, from 0 to 23, representing the hour
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.getHours()" % self.varId, isPyData=False)

  def getMilliseconds(self):
    """
    Description:
    -----------
    The getMilliseconds() method returns the milliseconds (from 0 to 999) of the specified date and time.

    Usage::

      jsObj.objects.date.new("2019-01-01", varName="dateTest")
      jsObj.objects.date.get("dateTest").getMilliseconds()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_getmilliseconds.asp

    :return: A Number, from 0 to 999, representing milliseconds
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.getMilliseconds()" % self.varId, isPyData=False)

  def getMonth(self):
    """
    Description:
    -----------
    The getMonth() method returns the month (from 0 to 11) for the specified date, according to local time.

    Usage::

      jsObj.objects.date.new("2019-01-01", varName="dateTest")
      jsObj.objects.date.get("dateTest").getMonth()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_getmonth.asp

    :return: A Number, from 0 to 11, representing the month
    """
    from epyk.core.js.primitives import JsNumber
    return JsNumber.JsNumber("%s.getMonth()" % self.varId, isPyData=False)

  def getMonthName(self):
    """
    Description:
    -----------
    Use getMonth() method returns the month the month name from the definition in the module .

    Usage::

      jsObj.objects.date.new("2019-01-01", varName="dateTest")
      jsObj.objects.date.get("dateTest").getMonthName()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_getmonth.asp

    :return: A Number, from 0 to 11, representing the month
    """
    from epyk.core.js.primitives import JsNumber
    return JsNumber.JsNumber("(function(x){return %s[x]})(%s.getMonth())" % (MONTHS, self.varId), isPyData=False)

  def setDate(self, day):
    """
    Description:
    -----------
    The setDate() method sets the day of the month to the date object.

    Usage::

      jsObj.objects.date.new("2019-01-01", varName="dateTest")
      jsObj.objects.date.get("dateTest").setDate(5)

    Related Pages:


    https://www.w3schools.com/jsref/jsref_setdate.asp

    Attributes:
    ----------
    :param day: Required. An integer representing the day of a month.

    :return: A Number, representing the number of milliseconds between the date object and midnight January 1 1970
    """
    return JsDate("%s.setDate(%s)" % (self.varId, day), isPyData=False)

  def setMonth(self, month, day=None):
    """
    Description:
    -----------
    The setMonth() method sets the month of a date object.
    Return a new date object

    Usage::

      jsObj.objects.date.new("2019-01-01", varName="dateTest")
      jsObj.objects.date.get("dateTest").setMonth(5)

    Related Pages:


    https://www.w3schools.com/jsref/jsref_setmonth.asp

    Attributes:
    ----------
    :param month: Required. An integer representing the month
    :param day: Optional. An integer representing the day of month

    :return: A Number, representing the number of milliseconds between the date object and midnight January 1 1970
    """
    if day is not None:
      return JsDate("new Date(%s.setMonth(%s, %s))" % (self.varId, month, day), isPyData=False)

    return JsDate("new Date(%s.setMonth(%s))" % (self.varId, month), isPyData=False)

  def toDateString(self):
    """
    Description:
    -----------
    The toDateString() method converts the date (not the time) of a Date object into a readable string.

    Usage::

      jsType.date.new(varName="Test")
      jsType.date.get("Test").toDateString()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_todatestring.asp

    :return: A String, representing the date as a string
    """
    from epyk.core.js.primitives import JsString

    return JsString.JsString("%s.toDateString()" % self.varId, isPyData=False)

  def toISOString(self):
    """
    Description:
    -----------
    The toISOString() method converts a Date object into a string, using the ISO standard.

    Usage::

      jsType.date.new(varName="Test")
      jsType.date.get("Test").toISOString()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A String, representing the date and time using the ISO standard format
    """
    from epyk.core.js.primitives import JsString

    return JsString.JsString("%s.toISOString()" % self.varId, isPyData=False)

  def getStrDate(self):
    """
    Description:
    -----------
    Return the String date in the standard format YYYY-MM-DD

    Usage::

      jsObj.objects.date.new("2019-01-01", varName="dateTest")
      jsType.date.get("dateTest").getStrDate()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A Python / Javascript object
    """
    from epyk.core.js.primitives import JsString
    return JsString.JsString("%s.toISOString().slice(0, 10)" % self.varId, isPyData=False)

  def getStrTimeStamp(self):
    """
    Description:
    -----------
    The toISOString() method converts a Date object into a string, using the ISO standard.

    Usage::

      jsObj.objects.date.new("2019-01-01", varName="dateTest")
      jsType.date.get("dateTest").getStrTimeStamp()

    Related Pages:


    https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A Python / Javascript object
    """
    from epyk.core.js.primitives import JsString
    return JsString.JsString("%s.toISOString().replace('T', ' ').slice(0, 19)" % self.varId, isPyData=False)

  def getTime(self, in_seconds=True):
    """
    Description:
    -----------
    To get the unix timestamp using JavaScript you need to use the getTime() function of the build in Date object.
    As this returns the number of milliseconds then we must divide the number by 1000 and round it in order to get the timestamp in seconds.

    Attributes:
    ----------
    :param in_seconds: Boolean. In second conversion of the Javascript timestamp
    """
    from epyk.core.js.primitives import JsNumber

    if in_seconds:
      return JsNumber.JsNumber("%s.getTime()/1000" % self.varId, isPyData=False)

    return JsNumber.JsNumber("%s.getTime()" % self.varId, isPyData=False)

  def add(self, n):
    """
    Description:
    -----------
    Simple wrapper to the Javascript add method.
    This will just return the Js string corresponding to the add

    This function is used in the addDays method

    Usage::

      jsObj.objects.date.this().getDate().add(1)

    Attributes:
    ----------
    :param n: Integer the number of days

    :return: A Python Js object
    """
    jsData = JsUtils.jsConvertData(n, None)
    return super(JsDate, self).add(jsData)

  def addDays(self, jsObj, n, weekend=False):
    """
    Description:
    -----------
    Add some days to a Javascript date

    Usage::

      jsObj.objects.date.get("MyDate").addDays(jsObj, 6).getStrDate()

    Related Pages:


    https://stackoverflow.com/questions/563406/add-days-to-javascript-date

    Attributes:
    ----------
    :param jsObj: The internal JS object used to store the prototype extension
    :param n: The number of days to be added
    :param weekend: Boolean flag to specify if the weekends should be considered in the count. Default False

    :type jsObj: epyk.Lib.js.Js.JsBase
    """
    jsObj.extendProto(self, "addDays", [
      jsObj.objects.date.this().setDate(jsObj.objects.date.this().getDate().add(jsObj.parseInt(jsObj.objects.get("n")))),
      jsObj.if_([jsObj.objects.date.this().isWeedend, jsObj.objects.boolean.get("weekend").not_], [
        jsObj.if_(jsObj.objects.date.this().getDay() == 0, jsObj.objects.date.this().setDate(jsObj.objects.date.this().getDate().add(1))),
        jsObj.if_(jsObj.objects.date.this().getDay() == 6, jsObj.objects.date.this().setDate(jsObj.objects.date.this().getDate().add(2)))
      ]),
      jsObj.return_(jsObj.objects.date.this())
    ], pmts=["n", "weekend"])
    return JsDate("%s.addDays(%s, %s)" % (self.varId, n, json.dumps(weekend)))
