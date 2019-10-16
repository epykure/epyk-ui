"""
Entry point for the different Javascript primitives

"""

from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsDate
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsBoolean

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.objects import JsData


class JsObjects(object):
  def __init__(self, jsObj):
    self._jsObj = jsObj

  @property
  def this(self):
    """
    Interface to the Javascript Object primitive

    :return: The Javascript "this" object
    """
    return JsObject.JsObject.get("this")

  @property
  def jqThis(self):
    """
    Interface to the Javascript Object primitive

    :return: The Javascript "this" object
    """
    from epyk.core.js.packages import JsQuery
    return JsQuery.JQuery(self._jsObj._src, selector="jQuery(this)", setVar=False)

  @classmethod
  def get(cls, varName):
    """
    Interface to the Javascript Object primitive

    :return: The requested Python JsObject primitive
    """
    return JsObject.JsObject.get(varName)

  @classmethod
  def new(cls, data=None, varName=None, isPyData=False):
    """
    Interface to the Javascript Object primitive

    :return: A Python generic JsObject primitive
    """
    return JsObject.JsObject.new(data, varName, isPyData)

  @property
  def number(self):
    """
    Interface to the Javascript Number primitive

    Documentation
    https://www.w3schools.com/jsref/jsref_number.asp

    :return: A Python JsNumber primitive
    """
    return JsNumber.JsNumber

  @property
  def string(self):
    """
    Interface to the Javascript String primitive

    Documentation
    https://www.w3schools.com/jsref/jsref_obj_string.asp

    :return: A Python JsString primitive
    """
    return JsString.JsString

  @property
  def array(self):
    """
    Interface to the Javascript Array primitive

    Documentation
    https://www.w3schools.com/jsref/jsref_obj_array.asp

    :return: A Python JsArray primitive
    """
    return JsArray.JsArray

  @property
  def date(self):
    """
    Interface to the Javascript Date primitive

    Documentation
    https://www.w3schools.com/jsref/jsref_obj_date.asp

    :return: A Python JsDate object
    """
    return JsDate.JsDate

  @property
  def boolean(self):
    """
    Interface to the Javascript Boolean primitive

    Documentation
    https://www.w3schools.com/jsref/jsref_obj_boolean.asp

    :return: A Python JsBoolean primitive
    """
    return JsBoolean.JsBoolean

  @property
  def dom(self):
    """
    Interface to the Javascript Dom class

    Documentation

    :rtype: epyk.Lib.js.objects.JsNodeDom.JsDoms
    :return: A Python Document
    """
    return JsNodeDom.JsDoms

  @property
  def null(self):
    """
    Similar as None in Python

    Documentation
    https://www.w3schools.com/js/js_datatypes.asp

    :return: A Python Js Null object
    """
    return JsObject.JsObject("null")

  @property
  def undefined(self):
    """
    Similar as the None in Python

    Documentation
    https://www.w3schools.com/jsref/jsref_undefined.asp

    :return: A Python Js undefined object
    """
    return JsObject.JsObject("undefined", isPyData=False)

  @property
  def NaN(self):
    """
    The NaN property represents "Not-a-Number" value. This property indicates that a value is not a legal number.

    The NaN property is the same as the Number.Nan property.

    Example

    Documentation:
    https://www.w3schools.com/jsref/jsref_number_nan.asp
    https://www.w3schools.com/jsref/jsref_isnan.asp

    :return:
    """
    return JsNumber.JsNumber("Number.NaN")

  @property
  def true(self):
    """
    Similar as True in Python

    Example

    Documentation
    https://www.w3schools.com/js/js_booleans.asp

    :return: A Python Js True object
    """
    return JsBoolean.JsBoolean.get('true')

  @property
  def false(self):
    """
    Similar as False in Python

    Documentation
    https://www.w3schools.com/js/js_booleans.asp
    
    :return: A Python Js False object
    """
    return JsBoolean.JsBoolean.get('false')

  def record(self, varName):
    """
    Get a record object

    :param varName: A string with of the existing variable name

    :return:
    """
    return JsData.RawData.get(self._jsObj, varName)
