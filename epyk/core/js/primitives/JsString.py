#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Wrapper to the String Javascript primitives

Most of the documentation in this module is coming from the website https://www.w3schools.com/jsref

This module will ensure the conversion from Python to Javascript and from Javascript to Python.
Those intermediary object will be used as a bridge between the two languages.

They should be used in Js specific functions (expecting jsFncs or jsData) in order to be correctly converted.

Each function will have it is specific documentation and a simple example.

More examples can be found in the tests folder if needed.
If necessary the tests folder can be updated in order to catch some specific regressions

Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_string.asp
"""


import json

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject


class JsString(JsObject.JsObject):
  _jsClass = "String"

  def __init__(self, data, varName=None, setVar=False, isPyData=True, report=None):
    if not hasattr(data, 'varName') and isPyData:
      isPyData = True
      data = json.dumps(data)
    self.isPyData = isPyData
    super(JsString, self).__init__(data, varName, setVar, isPyData, report=report)

  def __add__(self, value):
    return JsString("%s + %s" % (self.varId, JsUtils.jsConvertData(value, None)), isPyData=False)

  def __getitem__(self, value):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param value:
    """
    return JsString(None, "%s[%s]" % (self.varId, value), setVar=False)

  def startswith(self, val):
    """
    Description:
    ------------
    Proxy to the Python method startswith.

    Usage:
    -----

    Attributes:
    ----------
    :param val: The Python value.

    :return: Always False as this is dedicated to be a Javascript Object
    """
    return False

  @property
  def length(self):
    """
    Description:
    ------------
    The length property of an array returns the length of an array (the number of array elements).

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_length_string.asp

    :return: The length of a string
    """
    from epyk.core.js.primitives import JsNumber

    newObj = JsNumber.JsNumber("%s.length" % self.varId, isPyData=False)
    newObj._js.extend(self._js)
    return newObj

  def prepend(self, data):
    """
    Description:
    ------------
    Prepend Object to the String Javascript Object.

    Usage:
    -----

    Attributes:
    ----------
    :param data: Object. String or other Javascript objects.
    """
    self.varData = "%s + %s" % (JsUtils.jsConvertData(data, None), self.varData)
    return self

  def add(self, strVal):
    """
    Description:
    ------------
    Add object to the String Javascript object.

    Usage:
    -----

    Attributes:
    ----------
    :param strVal: Object. String or other Javascript objects.

    :return: return a new JString object
    """
    return JsString("%s + %s" % (self.varId, JsUtils.jsConvertData(strVal, None)), isPyData=False)

  def indexOf(self, searchvalue, start=0):
    """
    Description:
    ------------
    The indexOf() method returns the position of the first occurrence of a specified value in a string.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_indexof.asp

    Attributes:
    ----------
    :param searchvalue: String. Required. The string to search for.
    :param start: Integer. Optional. Default 0. At which position to start the search.

    :rtype: JsNumber.JsNumber
    """
    from epyk.core.js.primitives import JsNumber

    searchvalue = JsUtils.jsConvertData(searchvalue, None)
    return JsNumber.JsNumber("%s.indexOf(%s, %s)" % (self.varId, searchvalue, start), isPyData=False)

  def lastIndexOf(self, searchvalue, start=0):
    """
    Description:
    ------------
    The lastIndexOf() method returns the position of the last occurrence of a specified value in a string.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/jsref_lastindexof.asp

    Attributes:
    ----------
    :param searchvalue: Required. The string to search for.
    :param start: Integer. Optional. Default 0. At which position to start the search.

    :rtype: JsNumber.JsNumber
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.lastIndexOf(%s)" % (self.varId, searchvalue), isPyData=False)

  def substring(self, start=0, end=None):
    """
    Description:
    ------------
    The substring() method extracts the characters from a string, between two specified indices, and returns the new sub string.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/jsref_substring.asp

    Attributes:
    ----------
    :param start: Integer. Required. The position where to start the extraction. First character is at index 0.
    :param end: Integer. Optional. The position (up to, but not including) where to end the extraction. If omitted, it extracts the rest of the string
    """
    if end is None:
      end = self.length
    return JsString("%s.substring(%s, %s)" % (self.varId, start, end), isPyData=False)

  def substr(self, start=0, length=None):
    """
    Description:
    ------------
    The substr() method extracts parts of a string, beginning at the character at the specified position, and returns the specified number of characters.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_substr.asp

    Attributes:
    ----------
    :param start: Integer. Required. The position where to start the extraction. First character is at index 0.
    :param length: Integer. Optional. The number of characters to extract. If omitted, it extracts the rest of the string.
    """
    if length is None:
      return JsString("%s.substr(%s)" % (self.varId, start), isPyData=False)

    return JsString("%s.substr(%s, %s)" % (self.varId, start, length), isPyData=False)

  def replace(self, searchvalue, newvalue, isPyData=True):
    """
    Description:
    ------------
    The replace() method replaces a specified value with another value in a string

    The replace() method does not change the string it is called on. It returns a new string.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/js/js_string_methods.asp

    Attributes:
    ----------
    :param searchvalue: Required. The value, or regular expression, that will be replaced by the new value.
    :param newvalue: Required. The value to replace the search value with.
    :param isPyData: Boolean. Optional.
    """
    if isPyData:
      searchvalue = json.dumps(searchvalue)
      newvalue = json.dumps(newvalue)
    return JsString("%s.replace(%s, %s)" % (self.varId, searchvalue, newvalue), isPyData=False)

  def slice(self, start, end):
    """
    Description:
    ------------
    The slice() method extracts parts of a string and returns the extracted parts in a new string.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_slice_string.asp

    Attributes:
    ----------
    :param start: Integer. Required. The position where to begin the extraction. First character is at position 0.
    :param end: Integer. Optional. The position (up to, but not including) where to end the extraction.
                If omitted, slice() selects all characters from the start-position to the end of the string
    """
    return JsString("%s.replace(%s, %s)" % (self.varId, start, end), isPyData=False)

  def search(self, searchvalue, isPyData=True):
    """
    Description:
    ------------
    The search() method searches a string for a specified value, and returns the position of the match.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_search.asp

    Attributes:
    ----------
    :param searchvalue: String. Required. A regular expression. A string will automatically be converted to a regular expression..
    :param isPyData: Boolean. Optional.
    """
    from epyk.core.js.primitives import JsNumber

    if isPyData:
      searchvalue = json.dumps(searchvalue)
    return JsNumber.JsNumber("%s.search(%s)" % (self.varId, searchvalue), isPyData=False)

  def concat(self, *args, newVarName=None, isPyData=True):
    """
    Description:
    ------------
    The concat() method is used to join two or more strings.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_concat_string.asp

    Attributes:
    ----------
    :param args: Required. The strings to be joined
    :param newVarName: The new Javascript Variable Name
    :param isPyData: The data input type

    :return: A new String, containing the text of the combined strings
    """
    vars = []
    for a in args:
      if isPyData:
        vars.append(json.dumps(a))
      else:
        vars.append(a)

    if newVarName is not None:
      return "var %s = %s.concat(%s)" % (newVarName, self.varId, ",".join(vars))

    return JsString("%s.concat(%s)" % (self.varId, ",".join(vars)), isPyData=False)

  def clean(self):
    """
    Description:
    ------------
    Remove the special characts in a string and only keep the ones necessary to be considered as a valid Javascript
    variable name. Indeed some rules are defined for the variable names and the HTML codes values must follow those rules.
    Check are on the Python side with an exception raised but it can also be added on the Javascript side

    Usage:
    -----

      page.js.string("iib$% rni233n", varName="MyTest").clean() => returns "iibrni233n"

    Related Pages:

      https://www.w3schools.com/js/js_conventions.asp

    :return: The Python Javascript String transformed to be a variable name
    """
    return JsString("%s.trim().replace(/\W+/g, '')" % self.varId, isPyData=False)

  def leftTrim(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return JsString("%s.leftTrim()" % self.varId, isPyData=False)

  def trim(self):
    """
    Description:
    ------------
    The trim() method removes whitespace from both sides of a string.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_trim_string.asp

    :return: A String, representing the string with removed whitespace from both ends
    """
    return JsString("%s.trim()" % self.varId, isPyData=False)

  def charAt(self, i):
    """
    Description:
    ------------
    The charAt() method returns the character at the specified index in a string.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_charat.asp

    Attributes:
    ----------
    :param i: Required. An integer representing the index of the character you want to return.

    :return: A String, representing the character at the specified index, or an empty string if the index number is not found
    """
    return JsString("%s.charAt(%s)" % (self.varId, i), isPyData=False)

  def charCodeAt(self, i):
    """
    Description:
    ------------
    The charCodeAt() method returns the Unicode of the character at the specified index in a string.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_charcodeat.asp

    Attributes:
    ----------
    :param i: Required. A number representing the index of the character you want to return.

    :return: A Number, representing the unicode of the character at the specified index.
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.charCodeAt(%s)" % (self.varId, i), isPyData=False)

  def toLowerCase(self):
    """
    Description:
    ------------
    The toLocaleLowerCase() method converts a string to lowercase letters, according to the host's current locale.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_tolocalelowercase.asp

    :return: A String, representing the value of a string converted to lowercase according to the host's current locale
    """
    return JsString("%s.toLowerCase()" % self.varId, isPyData=False)

  def toUpperCase(self):
    """
    Description:
    ------------
    The toUpperCase() method converts a string to uppercase letters.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_touppercase.asp

    :return: A String, representing the value of a string converted to uppercase
    """
    return JsString("%s.toUpperCase()" % self.varId, isPyData=False)

  def includes(self, searchvalue, start=0, jsFnc=None, jsObj=None):
    """
    Description:
    ------------
    The includes() method determines whether a string contains the characters of a specified string.
    This function might not work with older browser, so to guarantee a good compatibility the jsObj must be defined.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_includes.asp

    Attributes:
    ----------
    :param searchvalue: String. Required. The string to search for.
    :param start: Integer. Optional. Default 0. At which position to start the search.
    :param jsObj: Integer. Optional. The base Javascript object to add the pollyfill to the Javascript imports.

    :return: A Boolean. Returns true if the string contains the value, otherwise it returns false
    """
    from epyk.core.js.primitives import JsBoolean

    searchvalue = JsUtils.jsConvertData(searchvalue, jsFnc)
    if jsObj is not None:
      # Add a polyfill to ensure the browser compatibility
      jsObj._addImport("babel-polyfill")
    return JsBoolean.JsBoolean("%s.includes(%s, %s)" % (self.varId, searchvalue, start), isPyData=False)

  def startsWith(self, searchvalue, start=0, jsFnc=None, jsObj=None):
    """
    Description:
    ------------
    The startsWith() method determines whether a string begins with the characters of a specified string.
    This function might not work with older browser, so to guarantee a good compatibility the jsObj must be defined.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_startswith.asp

    Attributes:
    ----------
    :param searchvalue: String. Required. The string to search for.
    :param start: Integer. Optional. Default 0. At which position to start the search.
    :param jsFnc: List | String. Javascript functions.
    :param jsObj:

    :return: A Boolean. Returns true if the string starts with the value, otherwise it returns false
    """
    from epyk.core.js.primitives import JsBoolean

    if jsObj is not None:
      # Add a polyfill to ensure the browser compatibility
      jsObj._addImport("babel-polyfill")

    searchvalue = JsUtils.jsConvertData(searchvalue, jsFnc)
    return JsBoolean.JsBoolean("%s.startsWith(%s, %s)" % (self.varId, searchvalue, start), isPyData=False)

  def endsWith(self, searchvalue, length=None, jsFnc=None):
    """
    Description:
    ------------
    The endsWith() method determines whether a string ends with the characters of a specified string.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_endswith.asp

    Attributes:
    ----------
    :param searchvalue: Required. The string to search for.
    :param length: Optional. Specify the length of the string to search. If omitted, the default value is the length of the string.
    :param jsFnc: List | String. Javascript functions.

    :return: A Boolean. Returns true if the string ends with the value, otherwise it returns false
    """
    from epyk.core.js.primitives import JsBoolean

    searchvalue = JsUtils.jsConvertData(searchvalue, jsFnc)
    if length is not None:
      return JsBoolean.JsBoolean("%s.endsWith(%s, %s)" % (self.varId, searchvalue, length), isPyData=False)

    return JsBoolean.JsBoolean("%s.endsWith(%s)" % (self.varId, searchvalue), isPyData=False)

  def repeat(self, count):
    """
    Description:
    ------------
    The repeat() method returns a new string with a specified number of copies of the string it was called on.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_repeat.asp

    Attributes:
    ----------
    :param count: Integer. Required. The number of times the original string value should be repeated in the new string.

    :return: A String, a new string containing copies of the original string
    """
    return JsString("%s.repeat(%s)" % (self.varId, count), isPyData=False)

  def split(self, separator="", limit=None):
    """
    Description:
    ------------
    The split() method is used to split a string into an array of substrings, and returns the new array.
    The empty value is a List with as a first value an emtpy String.

    Usage:
    -----

    Related Pages:

      https//www.w3schools.com/jsref/jsref_split.asp

    Attributes:
    ----------
    :param separator: String. Optional. Specifies the character, or the regular expression, to use for splitting the string.
                                If omitted, the entire string will be returned (an array with only one item).
    :param limit: Integer. Optional. An integer that specifies the number of splits, items after the split limit will not be included in the array

    :return: A Python JsArray
    """
    from epyk.core.js.primitives.JsArray import JsArray

    if limit is not None:
      return JsArray("%s.split('%s', %s)" % (self.varId, separator, limit), isPyData=False)

    return JsArray("%s.split('%s')" % (self.varId, separator), isPyData=False)

  def splitEmptyArray(self, page, separator, limit=None):
    """
    Description:
    ------------
    The splitEmptyArray() method is used to split a string into an array of substrings, and returns the new array.
    The empty value is an emtpy list.

    Usage:
    -----

    Related Pages:

      https://stackoverflow.com/questions/5164883/the-confusion-about-the-split-function-of-javascript

    Attributes:
    ----------
    :param page: Report. The report object in order to register the prototype extension.
    :param separator: String. Optional. Specifies the character, or the regular expression, to use for splitting the string.
                      If omitted, the entire string will be returned (an array with only one item).
    :param limit: Integer. Optional. An integer that specifies the number of splits, items after the split limit will not be included in the array

    :return: A Python JsArray
    """
    from epyk.core.js.primitives.JsArray import JsArray

    page._props.setdefault('js', {}).setdefault('prototypes', {})['String.prototype.splitEmptyArray'] = "function(sep) {var a = this.split(sep); if(a[0] == '' && a.length == 1){ return []}; return a}"
    if limit is not None:
      return JsArray("%s.splitEmptyArray('%s', %s)" % (self.varId, separator, limit), isPyData=False)

    return JsArray("%s.splitEmptyArray('%s')" % (self.varId, separator), isPyData=False)

  def formatMoney(self, jsObj, decPlaces, countryCode='UK'):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param jsObj:
    :param decPlaces:
    :param countryCode:
    """
    jsObj.extendProto(self, "formatMoney", '''var n = parseFloat(this); n.formatMoney(decPlaces, thouSeparator, decSeparator);
      ''', pmts=["decPlaces", "thouSeparator", "decSeparator"])
    return self.parseFloat().formatMoney(jsObj, decPlaces, countryCode)

  def parseFloat(self):
    """
    Description:
    ------------

    Usage:
    -----

    Related Pages:

    :return: A Python Javascript Number
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("parseFloat(%s)" % self.varId, isPyData=False)

  def parseInt(self):
    """
    Description:
    ------------

    Usage:
    -----

    Related Pages:

    :return: A Python Javascript Integer
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("parseInt(%s)" % self.varId, isPyData=False)

  def toDate(self, jsFormat="YYYY-MM-DD"):
    """
    Description:
    ------------

    Usage:
    -----

    """
    from epyk.core.js.primitives import JsDate

    jsDate = JsDate.JsDate.new("%s" % self.varId, isPyData=False)
    jsDate._js = self._js + jsDate._js
    return jsDate
