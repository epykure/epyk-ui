"""
Module dedicated to wrap the Javascript Date

https://www.w3schools.com/jsref/jsref_obj_date.asp
"""


import json

from epyk.core.js.primitives import JsObject
from epyk.core.js import JsUtils


class JsDate(JsObject.JsObject):
  _jsClass = "Date"

  def __init__(self, data=None, varName=None, setVar=False, isPyData=False):
    """

    Documentation
    https://www.w3schools.com/jsref/jsref_obj_date.asp

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
    Get the Javascript Object by its reference

    Example
    JsDate.new("2019-05-03", varName="MyDate")
    JsDate.get("MyDate")

    Documentation
    https://www.w3schools.com/jsref/jsref_obj_date.asp

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

    Example
    jsObj.objects.date.get("dateTest").isWeedend

    :return:
    """
    from epyk.core.js.primitives import JsBoolean
    return JsBoolean.JsBoolean("(%(varId)s.getDay() === 6) || (%(varId)s.getDay() === 0)" % {"varId": self.varId}, isPyData=False)

  @staticmethod
  def now():
    """
    The Date.now() method returns the number of milliseconds since January 1, 1970 00:00:00 UTC.

    Example
    jsObj.objects.date.now()

    Documentation
    https://www.w3schools.com/jsref/jsref_now.asp

    :return: A Number, representing the number of milliseconds since midnight January 1, 1970
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("Date.now()", isPyData=False)

  @staticmethod
  def today():
    """
    Return the String date in the standard format YYYY-MM-DD

    Example
    rptObj.js.objects.date.today()

    Documentation
    https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A Python / Javascript object
    """
    from epyk.core.js.primitives import JsString
    return JsString.JsString("function(){return new Date}().toISOString().slice(0, 10)", isPyData=False)

  def getDate(self):
    """
    The getDate() method returns the day of the month (from 1 to 31) for the specified date.

    Documentation
    https://www.w3schools.com/jsref/jsref_getdate.asp

    :return:
    """
    return JsDate("%s.getDate()" % self.varId, isPyData=False)

  def getDay(self):
    """
    The getDay() method returns the day of the week (from 0 to 6) for the specified date.

    Documentation
    https://www.w3schools.com/jsref/jsref_getday.asp

    :return:
    """
    from epyk.core.js.primitives import JsNumber
    return JsNumber.JsNumber("%s.getDay()" % self.varId, isPyData=False)

  def getFullYear(self):
    """
    The getFullYear() method returns the year (four digits for dates between year 1000 and 9999) of the specified date.

    Documentation
    https://www.w3schools.com/jsref/jsref_getfullyear.asp

    :return: A Number, representing the year of the specified date
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.getFullYear()" % self.varId, isPyData=False)

  def getHours(self):
    """
    The getHours() method returns the hour (from 0 to 23) of the specified date and time.

    Documentation
    https://www.w3schools.com/jsref/jsref_gethours.asp

    :return: A Number, from 0 to 23, representing the hour
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.getHours()" % self.varId, isPyData=False)

  def getMilliseconds(self):
    """
    The getMilliseconds() method returns the milliseconds (from 0 to 999) of the specified date and time.

    Example

    Documentation
    https://www.w3schools.com/jsref/jsref_getmilliseconds.asp

    :return: A Number, from 0 to 999, representing milliseconds
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.getMilliseconds()" % self.varId, isPyData=False)

  def getMonth(self):
    """
    The getMonth() method returns the month (from 0 to 11) for the specified date, according to local time.

    Example
    jsObj.objects.date.new("2019-01-01", varName="dateTest")
    jsObj.objects.date.get("dateTest").getMonth()

    Documentation:
    https://www.w3schools.com/jsref/jsref_getmonth.asp

    :return: A Number, from 0 to 11, representing the month
    """
    from epyk.core.js.primitives import JsNumber
    return JsNumber.JsNumber("%s.getMonth()" % self.varId, isPyData=False)

  def setDate(self, day):
    """
    The setDate() method sets the day of the month to the date object.

    Example
    jsObj.objects.date.new("2019-01-01", varName="dateTest")
    jsObj.objects.date.get("dateTest").setDate(5)

    Documentation
    https://www.w3schools.com/jsref/jsref_setdate.asp

    :param day: Required. An integer representing the day of a month.

    :return: A Number, representing the number of milliseconds between the date object and midnight January 1 1970
    """
    return JsDate("%s.setDate(%s)" % (self.varId, day), isPyData=False)

  def setMonth(self, month, day=None):
    """
    The setMonth() method sets the month of a date object.
    Return a new date object

    Example
    jsObj.objects.date.new("2019-01-01", varName="dateTest")
    jsObj.objects.date.get("dateTest").setMonth(5)

    Documentation
    https://www.w3schools.com/jsref/jsref_setmonth.asp

    :param month: Required. An integer representing the month
    :param day: Optional. An integer representing the day of month

    :return: A Number, representing the number of milliseconds between the date object and midnight January 1 1970
    """
    if day is not None:
      return JsDate("new Date(%s.setMonth(%s, %s))" % (self.varId, month, day), isPyData=False)

    return JsDate("new Date(%s.setMonth(%s))" % (self.varId, month), isPyData=False)

  def toDateString(self):
    """
    The toDateString() method converts the date (not the time) of a Date object into a readable string.

    Example
    jsType.date.new(varName="Test")
    jsType.date.get("Test").toDateString()

    Documentation:
    https://www.w3schools.com/jsref/jsref_todatestring.asp

    :return: A String, representing the date as a string
    """
    from epyk.core.js.primitives import JsString

    return JsString.JsString("%s.toDateString()" % self.varId, isPyData=False)

  def toISOString(self):
    """
    The toISOString() method converts a Date object into a string, using the ISO standard.

    Example
    jsType.date.new(varName="Test")
    jsType.date.get("Test").toISOString()

    Documentation:
    https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A String, representing the date and time using the ISO standard format
    """
    from epyk.core.js.primitives import JsString

    return JsString.JsString("%s.toISOString()" % self.varId, isPyData=False)

  def getStrDate(self):
    """
    Return the String date in the standard format YYYY-MM-DD

    Example
    jsObj.objects.date.new("2019-01-01", varName="dateTest")
    jsType.date.get("dateTest").getStrDate()

    Documentation
    https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A Python / Javascript object
    """
    from epyk.core.js.primitives import JsString
    return JsString.JsString("%s.toISOString().slice(0, 10)" % self.varId, isPyData=False)

  def getStrTimeStamp(self):
    """
    The toISOString() method converts a Date object into a string, using the ISO standard.

    Example
    jsObj.objects.date.new("2019-01-01", varName="dateTest")
    jsType.date.get("dateTest").getStrTimeStamp()

    Documentation
    https://www.w3schools.com/jsref/jsref_toisostring.asp

    :return: A Python / Javascript object
    """
    from epyk.core.js.primitives import JsString
    return JsString.JsString("%s.toISOString().replace('T', ' ').slice(0, 19)" % self.varId, isPyData=False)

  def add(self, n):
    """
    Simple wrapper to the Javascript add method.
    This will just return the Js string corresponding to the add

    This function is used in the addDays method

    Example
    jsObj.objects.date.this().getDate().add(1)

    :param n: Integer the number of days

    :return: A Python Js object
    """
    jsData = JsUtils.jsConvertData(n, None)
    return super(JsDate, self).add(jsData)

  def addDays(self, jsObj, n, weekend=False):
    """
    Add some days to a Javascript date

    Example
    jsObj.objects.date.get("MyDate").addDays(jsObj, 6).getStrDate()

    Documentation
    https://stackoverflow.com/questions/563406/add-days-to-javascript-date

    :type jsObj: epyk.Lib.js.Js.JsBase
    :param jsObj: The internal JS object used to store the prototype extension
    :param n: The number of days to be added
    :param weekend: Boolean flag to specify if the weekends should be considered in the count. Default False

    :return:
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
