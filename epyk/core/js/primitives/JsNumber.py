#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Description:
------------
Wrapper to the Number Javascript primitives

Most of the documentation in this module is coming from the website https://www.w3schools.com/jsref/jsref_number.asp

This module will ensure the conversion from Python to Javascript and from Javascript to Python.
Those intermediary object will be used as a bridge between the two languages.

They should be used in Js specific functions (expecting jsFncs or jsData) in order to be correctly converted.

Each function will have it is specific documentation and a simple example.

More examples can be found in the tests folder if needed.
If necessary the test folders can be updated in order to catch some specific regressions
"""

from typing import Union
from epyk.core.py import primitives

from epyk.core.js.primitives import JsObject
from epyk.core.js import JsUtils


class JsNumber(JsObject.JsObject):
  _jsClass = "Number"

  @property
  def NEGATIVE_INFINITY(self):
    """
    The NEGATIVE_INFINITY property represents negative infinity.
    Negative infinity can be explained as something that is lower than any other number.

    Usage::

      jsObj.objects.number.get("MyNumber").NEGATIVE_INFINITY

    Related Pages:

      https://www.w3schools.com/jsref/jsref_negative_infinity.asp
    """
    return JsNumber("Number.NEGATIVE_INFINITY")

  @classmethod
  def POSITIVE_INFINITY(cls):
    """
    The POSITIVE_INFINITY property represents positive infinity.
    Positive infinity can be explained as something that is higher than any other number.

    Usage::

      jsObj.objects.number.get("MyNumber").POSITIVE_INFINITY

    Related Pages:

      https://www.w3schools.com/jsref/jsref_positive_infinity.asp
    """
    return JsNumber("Number.POSITIVE_INFINITY")

  @classmethod
  def MAX_VALUE(cls):
    """
    The MAX_VALUE property returns the largest number possible in JavaScript.

    This static property has a value of 1.7976931348623157e+308.

    Usage::

      jsObj.objects.number.get("MyNumber").MAX_VALUE

    Related Pages:

      https://www.w3schools.com/jsref/jsref_max_value.asp
    """
    return JsNumber("Number.MAX_VALUE")

  @property
  def MIN_VALUE(self):
    """
    The MIN_VALUE property returns the smallest positive number possible in JavaScript.

    This static property has a value of 5e-324.

    Usage::

      jsObj.objects.number.get("MyNumber").MIN_VALUE

    Related Pages:

      https://www.w3schools.com/jsref/jsref_min_value.asp
    """
    return JsNumber("Number.MIN_VALUE")

  def isNaN(self):
    """
    Check whether the value is NaN.

    Usage::

      string.parseFloat().isNaN()

    Related Pages:

      https//www.w3schools.com/jsref/jsref_isnan_number.asp

    :return: A Javascript boolean
    """
    from epyk.core.js.primitives import JsBoolean
    return JsBoolean.JsBoolean("Number.isNaN(%s)" % self.varId, is_py_data=False)

  def add(self, n: Union[primitives.JsDataModel, float]):
    """
    Add a value to a Javascript Number.
    The value will be added and it will return a new number object on the Javascript side.

    Usage::

      jsNumber.add(34.5)

    :param n: The number value.

    :return: A new Python Javascript Number
    """
    return JsNumber("%s + %s" % (self.varId, n), is_py_data=False)

  def min(self, value: Union[primitives.JsDataModel, float]):
    """
    Add a cap to the value using the min function.

    :param value: The maximum value for this object.
    """
    return JsNumber("Math.min(%s, %s)" % (self.varId, JsUtils.jsConvertData(value, None)), is_py_data=False)

  def max(self, value: Union[primitives.JsDataModel, float]):
    """
    Add a floor to the value using the max function.

    Usage::

    :param value: The minimum value for this object.
    """
    return JsNumber("Math.max(%s, %s)" % (self.varId, JsUtils.jsConvertData(value, None)), is_py_data=False)

  def sub(self, n: Union[primitives.JsDataModel, float]):
    """
    Subtract a value to a Javascript Number.
    The value will be subtracted and it will return a new number object on the Javascript side.

    Usage::

      jsNumber.sub(34.5)

    :param n: The number value.

    :return: A new Python Javascript Number.
    """
    return JsNumber("%s - %s" % (self.varId, n), is_py_data=False)

  def toExponential(self):
    """
    Convert a number into an exponential notation.

    Usage::

      jsObj.objects.number.get("MyNumber").toExponential()

    Related Pages:

      https//www.w3schools.com/jsref/jsref_toexponential.asp

    :return: A Javascript Number
    """
    return JsNumber("%s.toExponential()" % self.varId, is_py_data=False)

  def toFixed(self, digits: Union[primitives.JsDataModel, int] = 2):
    """
    Convert a number into a string, keeping only two decimals.

    Usage::

      jsObj.objects.number.get("MyNumber").toFixed()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_tofixed.asp

    :param Union[primitives.JsDataModel, int] digits: Optional. The number of digits after the decimal point.
    Default is 2 (2 digits after the decimal point)

    :return: A Javascript Number
    """
    return JsNumber("%s.toFixed(%s)" % (self.varId, digits), is_py_data=False)

  def isFinite(self):
    """
    Check whether a value is a finite number.

    Usage::

      jsObj.objects.number.get("MyNumber").isFinite()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_isfinite_number.asp

    :return: A Javascript boolean
    """
    from epyk.core.js.primitives import JsBoolean

    return JsBoolean.JsBoolean("Number.isFinite(%s)" % self.varId, is_py_data=False)

  def toPrecision(self, n: Union[primitives.JsDataModel, int]):
    """
    Format a number into a specified length:

    Usage::

      page.js.number(varName="myNumber").toPrecision(10) for 5776 returns 5776.000000

    Related Pages:

      https://www.w3schools.com/jsref/jsref_toprecision.asp

    :param n: Optional. The number of digits. If omitted, it returns the entire number (without any formatting).

    :return: A Javascript Number
    """
    return JsNumber("%s.toPrecision(%s)" % (self.varId, n), is_py_data=False)

  def __add__(self, value: Union[primitives.JsDataModel, float]):
    return JsNumber("%s + %s" % (self.varId, value), is_py_data=False)

  def __sub__(self, value: Union[primitives.JsDataModel, float]):
    return JsNumber("%s - %s" % (self.varId, value), is_py_data=False)

  def __iadd__(self, value: Union[primitives.JsDataModel, float]):
    # TODO: Fix this
    self.varData = "%s += %s" % (self.varData, value)
    return self

  def __isub__(self, value: Union[primitives.JsDataModel, float]):
    # TODO: Fix this
    self.varData = "%s -= %s" % (self.varData, value)
    return self

  def __mul__(self, value: Union[primitives.JsDataModel, float]):
    return JsNumber("%s * %s" % (self.varId, value), is_py_data=False)

  def __truediv__(self, value: Union[primitives.JsDataModel, float]):
    return JsNumber("%s / %s" % (self.varId, value), is_py_data=False)

  def __mod__(self, value: Union[primitives.JsDataModel, float]):
    return JsNumber("%s %%= %s" % (self.varId, value), is_py_data=False)

  def __pow__(self, value: Union[primitives.JsDataModel, float]):
    from epyk.core.js import JsMaths

    return JsNumber("%s = %s" % (self.varId, JsMaths.JsMaths.pow(self, value)))

  @classmethod
  def proto(cls, js_obj, func_name):
    """

    Usage::

    :param js_obj: The base Javascript Python object
    :param func_name: The function name.
    """
    js_obj.extendProto(cls, "formatMoney", '''
var n = this, decPlaces = isNaN(decPlaces = Math.abs(decPlaces)) ? 2 : decPlaces, decSeparator = decSeparator == undefined ? "." : decSeparator,
thouSeparator = thouSeparator == undefined ? "," : thouSeparator, sign = n < 0 ? "-" : "", i = parseInt(n = Math.abs(+n || 0).toFixed(decPlaces)) + "",
j = (j = i.length) > 3 ? j % 3 : 0;
return sign + (j ? i.substr(0, j) + thouSeparator : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + thouSeparator) + (decPlaces ? decSeparator + Math.abs(n - i).toFixed(decPlaces).slice(2) : "");
''', pmts=["decPlaces", "thouSeparator", "decSeparator"])

  def formatMoney(self, js_obj, dec_places: Union[int, primitives.JsDataModel] = 0, country_code: str = 'UK'):
    """
    Wrapper function.

    Related Pages:

      https://en.wikipedia.org/wiki/Decimal_separator
      https://docs.oracle.com/cd/E19455-01/806-0169/overview-9/index.html

    :param js_obj: The base Javascript Python object
    :param dec_places: Optional. The number of decimal.
    :param country_code: Optional. The country code. Default uk.
    """
    thou_separator, dec_separator = (",", ".") if country_code.upper() in ["UK", 'US'] else (" ", ".")
    js_obj.extendProto(self, "formatMoney", '''
      var n = this, decPlaces = isNaN(decPlaces = Math.abs(decPlaces)) ? 2 : decPlaces, decSeparator = decSeparator == undefined ? "." : decSeparator,
      thouSeparator = thouSeparator == undefined ? "," : thouSeparator, sign = n < 0 ? "-" : "", i = parseInt(n = Math.abs(+n || 0).toFixed(decPlaces)) + "",
      j = (j = i.length) > 3 ? j % 3 : 0;
      return sign + (j ? i.substr(0, j) + thouSeparator : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + thouSeparator) + (decPlaces ? decSeparator + Math.abs(n - i).toFixed(decPlaces).slice(2) : "");
      ''', pmts=["decPlaces", "thouSeparator", "decSeparator"])
    from epyk.core.js.primitives import JsString

    return JsString.JsString("%s.formatMoney(%s, '%s', '%s')" % (
      self.varId, dec_places, thou_separator, dec_separator), is_py_data=False)
