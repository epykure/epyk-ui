"""
Wrapper for the Javascript Math module

Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_math.asp
"""


from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsNumber


class JsMaths:

  @property
  def E(self):
    """
    Description:
    ------------
    The E property returns the Euler's number and the base of natural logarithms, approximately 2.718.

    Usage::

      page.js.math.E

    Related Pages:

      https//www.w3schools.com/jsref/jsref_e.asp

    :return: Returns Euler's number (approx. 2.718)
    """
    return JsNumber.JsNumber("Math.E", isPyData=False)

  @property
  def LN2(self):
    """
    Description:
    ------------
    The LN2 property returns the natural logarithm of 2, approximately 0.693.

    Usage::

      jsObj.math.LN2

    Related Pages:

      https//www.w3schools.com/jsref/jsref_ln2.asp

    :return: Returns the natural logarithm of 2 (approx. 0.693)
    """
    return JsNumber.JsNumber("Math.LN2", isPyData=False)

  @property
  def LN10(self):
    """
    Description:
    ------------
    The LN10 property returns the natural logarithm of 10, approximately 2.302.

    Usage::

      jsObj.math.LN10

    Related Pages:

      https://www.w3schools.com/jsref/jsref_ln10.asp

    :return: Returns the natural logarithm of 10 (approx. 2.302)
    """
    return JsNumber.JsNumber("Math.LN10", isPyData=False)

  @property
  def LOG2E(self):
    """
    Description:
    ------------
    The LOG2E property returns the base-2 logarithm of E, approximately 1.442

    Usage::

      jsObj.math.LOG2E

    Related Pages:

      https//www.w3schools.com/jsref/jsref_log2e.asp

    :return: Returns the base-2 logarithm of E (approx. 1.442)
    """
    return JsNumber.JsNumber("Math.LOG2E", isPyData=False)

  @property
  def SQRT1_2(self):
    """
    Description:
    ------------
    The SQRT1_2 property returns the square root of 1/2, approximately 0.707.

    Usage::

      jsObj.math.SQRT1_2

    Related Pages:

      https//www.w3schools.com/jsref/jsref_sqrt1_2.asp

    :return: Returns the square root of 1/2 (approx. 0.707)
    """
    return JsNumber.JsNumber("Math.SQRT1_2", isPyData=False)

  @property
  def SQRT2(self):
    """
    Description:
    ------------
    The SQRT2 property returns the square root of 2, approximately 1.414.

    Usage::

      jsObj.math.SQRT2

    Example
    rptObj.js.math.SQRT2

    Related Pages:

      https//www.w3schools.com/jsref/jsref_sqrt2.asp

    :return: Returns the square root of 2 (approx. 1.414)
    """
    return JsNumber.JsNumber("Math.SQRT2", isPyData=False)

  @property
  def PI(self):
    """
    Description:
    ------------
    The PI property returns the ratio of a circle's area to the square of its radius, approximately 3.14.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_pi.asp
    """
    return JsNumber.JsNumber("Math.PI", isPyData=False)

  def random(self, min_val=0, max_val=1):
    """
    Description:
    ------------
    Math.random() returns a random number between 0 (inclusive),  and 1 (exclusive):

    Usage::

      page.js.math.random()
      jsObj.math.random(10, 100)

    Related Pages:

      https://www.w3schools.com/js/js_random.asp

    Attributes:
    ----------
    :param min_val: Integer. Optional The minimum value for the random function.
    :param max_val: Integer. Optional The maximum value for the random function.

    :return: A Number, representing a number from 0 up to but not including 1.
    """
    if min_val == 0 and max_val == 1:
      return JsNumber.JsNumber("Math.random()", isPyData=False)

    min_val = JsUtils.jsConvertData(min_val, None)
    max_val = JsUtils.jsConvertData(max_val, None)
    return JsNumber.JsNumber("Math.random() * (%(max)s - %(min)s + 1) + %(min)s" % {"min": min_val, "max": max_val})

  def min(self, *args):
    """
    Description:
    ------------
    The min() method returns the number with the lowest value.

    Usage::

      jsObj.math.min(10, 45, 100, -3, 56)

    Related Pages:

      https://www.w3schools.com/jsref/jsref_min.asp

    Attributes:
    ----------
    :param args: Optional. One or more numbers to compare

    :return: A Number, representing the lowest number of the arguments, or Infinity
    if no arguments are given, or NaN if one or more arguments are not numbers
    """
    jsArgs = [JsUtils.jsConvertData(a, None) for a in args]
    return JsNumber.JsNumber("Math.min(%s)" % ",".join([str(jsa) for jsa in jsArgs]), isPyData=False)

  def max(self, *args):
    """
    Description:
    ------------
    The max() method returns the number with the highest value.

    Usage::

      jsObj.math.max(10, 45, 100, -3, 56)

    Related Pages:

      https://www.w3schools.com/jsref/jsref_max.asp
      https://www.jstips.co/en/javascript/calculate-the-max-min-value-from-an-array/

    Attributes:
    ----------
    :param args: Optional. One or more numbers to compare

    :return: A Number, representing the highest number of the arguments, or -Infinity if no arguments are given, or NaN
    if one or more arguments are not numbers
    """
    jsArgs = [JsUtils.jsConvertData(a, None) for a in args]
    if len(jsArgs) == 1 and getattr(jsArgs[0], '_jsClass', None) == "Array":
      # ES2015 use of the new spread operator
      jsArgs[0] = "...%s" % jsArgs[0]
    return JsNumber.JsNumber("Math.max(%s)" % ",".join([str(jsa) for jsa in jsArgs]), isPyData=False)

  def floor(self, number):
    """
    Description:
    ------------
    The floor() method rounds a number DOWNWARDS to the nearest integer, and returns the result.

    Usage::

      jsObj.math.floor(13.566)

    Related Pages:

      https//www.w3schools.com/jsref/jsref_floor.asp

    Attributes:
    ----------
    :param number: Number. Required. The number you want to round.

    :return: A Number, representing the nearest integer when rounding downwards
    """
    number = JsUtils.jsConvertData(number, None)
    return JsNumber.JsNumber("Math.floor(%s)" % number, isPyData=False)

  def trunc(self, number):
    """
    Description:
    ------------
    The trunc() method returns the integer part of a number.

    Usage::

      page.js.math.trunc(rptObj.js.math.SQRT2)

    Related Pages:

      https//www.w3schools.com/jsref/jsref_trunc.asp

    Attributes:
    ----------
    :param number: Number. Required. A number.

    :return: Returns the integer part of a number (x).
    """
    number = JsUtils.jsConvertData(number, None)
    return JsNumber.JsNumber("Math.trunc(%s)" % number, isPyData=False)

  def abs(self, number):
    """
    Description:
    ------------
    The abs() method returns the absolute value of a number.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_abs.asp

    Attributes:
    ----------
    :param number: Required. A number

    :return: Returns the absolute value of x
    """
    number = JsUtils.jsConvertData(number, None)
    return JsNumber.JsNumber("Math.abs(%s)" % number, isPyData=False)

  def cos(self, number):
    """
    Description:
    ------------
    The acos() method returns the cosinus of a number as a value value between 0 and PI radians.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_cos.asp

    Attributes:
    ----------
    :param number: Number. Returns the cosine of x (x is in radians).

    :return: A Number, from -1 to 1, representing the cosine of an angle, or NaN if the value is empty.
    """
    number = JsUtils.jsConvertData(number, None)
    return JsNumber.JsNumber("Math.cos(%s)" % number, isPyData=False)

  def sin(self, number):
    """
    Description:
    ------------
    The sin() method returns the sinus of a number as a value value between 0 and PI radians.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_sin.asp

    Attributes:
    ----------
    :param number: Returns the sinus of x (x is in radians).

    :return: Number. from -1 to 1, representing the sine of an angle, or NaN if the value is empty.
    """
    number = JsUtils.jsConvertData(number, None)
    return JsNumber.JsNumber("Math.sin(%s)" % number, isPyData=False)

  def log(self, number):
    """
    Description:
    ------------
    The log() method returns the natural logarithm (base E) of a number.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_log.asp

    Attributes:
    ----------
    :param number: Number. Required. A number.

    :return: Returns the natural logarithm (base E) of x.
    """
    number = JsUtils.jsConvertData(number, None)
    return JsNumber.JsNumber("Math.log(%s)" % number, isPyData=False)

  def exp(self, number):
    """
    Description:
    ------------
    The exp() method returns the value of Ex, where E is Euler's number (approximately 2.7183) and x is the
    number passed to it.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_exp.asp

    Attributes:
    ----------
    :param number: Number. Required. A number,

    :return: Returns the value of exponential of x,
    """
    number = JsUtils.jsConvertData(number, None)
    return JsNumber.JsNumber("Math.exp(%s)" % number, isPyData=False)

  def round(self, number):
    """
    Description:
    ------------
    The round() method rounds a number to the nearest integer.

    Note: 2.49 will be rounded down (2), and 2.5 will be rounded up (3).

    Usage::

      jsObj.objects.number.new(23.6, varName="MyNumber")
      jsObj.math.round(jsObj.objects.number.get("MyNumber"))

    Related Pages:

      https//www.w3schools.com/jsref/jsref_round.asp

    Attributes:
    ----------
    :param number: Number. Required. The number to be rounded.

    :return: Rounds x to the nearest integer.
    """
    number = JsUtils.jsConvertData(number, None)
    return JsNumber.JsNumber("Math.round(%s)" % number, isPyData=False)

  def sqrt(self, number):
    """
    Description:
    ------------
    The sqrt() method returns the square root of a number.

    Usage::

      jsObj.objects.number.new(23.6, varName="MyNumber")
      jsObj.math.sqrt(jsObj.objects.number.get("MyNumber"))

    Related Pages:

      https//www.w3schools.com/jsref/jsref_sqrt.asp

    Attributes:
    ----------
    :param number: Number. Required. A number

    :return: A Number. If x is a negative number, NaN is returned.
    """
    number = JsUtils.jsConvertData(number, None)
    return JsNumber.JsNumber("Math.sqrt(%s)" % number, isPyData=False)

  def ceil(self, number):
    """
    Description:
    ------------
    The ceil() method rounds a number UPWARDS to the nearest integer, and returns the result.

    Usage::

      jsObj.math.ceil(jsObj.objects.number.get("MyNumber"))

    Related Pages:

      https//www.w3schools.com/jsref/jsref_ceil.asp

    Attributes:
    ----------
    :param number: Number. Required. The number you want to round.

    :return: Returns x, rounded upwards to the nearest integer.
    """
    number = JsUtils.jsConvertData(number, None)
    return JsNumber.JsNumber("Math.ceil(%s)" % number, isPyData=False)

  @staticmethod
  def pow(number, power):
    """
    Description:
    ------------
    The pow() method returns the value of x to the power of y (xy).

    Usage::

      jsObj.objects.number.new(23.6, varName="MyNumber")
      jsObj.math.pow(jsObj.objects.number.get("MyNumber"), 2)

    Related Pages:

      https//www.w3schools.com/jsref/jsref_pow.asp

    Attributes:
    ----------
    :param number: Number. Required. The base.
    :param power: Number. Required. The exponent

    :return: Returns the value of x to the power of y.
    """
    number = JsUtils.jsConvertData(number, None)
    power = JsUtils.jsConvertData(power, None)
    return JsNumber.JsNumber("Math.pow(%s, %s)" % (number, power), isPyData=False)
