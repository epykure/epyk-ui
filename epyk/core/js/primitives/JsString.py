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


from typing import Union, Optional
from epyk.core.py import primitives

import json

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject


class JsString(JsObject.JsObject):
  _jsClass = "String"

  def __init__(self, data, js_code: Optional[str] = None, set_var: bool = False, is_py_data: bool = True, page=None):
    if not hasattr(data, 'varName') and is_py_data:
      is_py_data = True
      data = json.dumps(data)
    self.is_py_data = is_py_data
    super(JsString, self).__init__(data, js_code, set_var, is_py_data, page=page)

  def __add__(self, value: Union[primitives.JsDataModel, str, float]):
    return JsString("%s + %s" % (self.varId, JsUtils.jsConvertData(value, None)), is_py_data=False)

  def __getitem__(self, value):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    """
    return JsString(None, "%s[%s]" % (self.varId, value), set_var=False)

  def startswith(self, val: Union[str, primitives.JsDataModel], position: int = None):
    """
    Description:
    ------------
    Proxy to the Python method startswith.

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] val: The Python value.
    :param int position:

    :return: Always False as this is dedicated to be a Javascript Object.
    """
    from epyk.core.js.primitives import JsBoolean

    val = JsUtils.jsConvertData(val, None)
    if position is None:
      return JsBoolean.JsBoolean("%s.startswith(%s)" % (self.varId, val), is_py_data=False)

    return JsBoolean.JsBoolean("%s.startswith(%s, %s)" % (self.varId, val, position), is_py_data=False)

  @property
  def length(self):
    """
    Description:
    ------------
    The length property of an array returns the length of an array (the number of array elements).

    Related Pages:

      https//www.w3schools.com/jsref/jsref_length_string.asp

    :return: The length of a string
    """
    from epyk.core.js.primitives import JsNumber

    new_obj = JsNumber.JsNumber("%s.length" % self.varId, is_py_data=False)
    new_obj._js.extend(self._js)
    return new_obj

  def prepend(self, data: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Prepend Object to the String Javascript Object.

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] data: Object. String or other Javascript objects.
    """
    self.varData = "%s + %s" % (JsUtils.jsConvertData(data, None), self.varData)
    return self

  def padStart(self, num: Union[int, primitives.JsDataModel], text: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    The padStart() method pads the current string with another string (multiple times,
    if needed) until the resulting string reaches the given length.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padStart

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] num: The length of the resulting string once the current str has been
    padded.
    :param Union[str, primitives.JsDataModel] text: The string to pad the current str with.
    """
    return JsString("%s.padStart(%s, %s)" % (
      self.varId, JsUtils.jsConvertData(num, None), JsUtils.jsConvertData(text, None)), is_py_data=False)

  def padEnd(self, num: Union[int, primitives.JsDataModel], text: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    The padEnd() method pads the current string with a given string (repeated,
    if needed) so that the resulting string reaches a given length.
    The padding is applied from the end of the current string.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padEnd

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] num: The length of the resulting string once the current str has been
    padded.
    :param Union[str, primitives.JsDataModel] text: The string to pad the current str with.
    """
    return JsString("%s.padEnd(%s, %s)" % (
      self.varId, JsUtils.jsConvertData(num, None), JsUtils.jsConvertData(text, None)), is_py_data=False)

  def add(self, value: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Add object to the String Javascript object.

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] value: String or other Javascript objects.

    :return: return a new JString object
    """
    return JsString("%s + %s" % (self.varId, JsUtils.jsConvertData(value, None)), is_py_data=False)

  def indexOf(self, search_value: Union[str, primitives.JsDataModel], start: Union[int, primitives.JsDataModel] = 0):
    """
    Description:
    ------------
    The indexOf() method returns the position of the first occurrence of a specified value in a string.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_indexof.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] search_value: The string to search for.
    :param Union[int, primitives.JsDataModel] start:  Optional. Default 0. At which position to start the search.

    :rtype: JsNumber.JsNumber
    """
    from epyk.core.js.primitives import JsNumber

    search_value = JsUtils.jsConvertData(search_value, None)
    return JsNumber.JsNumber("%s.indexOf(%s, %s)" % (self.varId, search_value, start), is_py_data=False)

  def lastIndexOf(self, search_value: Union[str, primitives.JsDataModel],
                  start: Union[int, primitives.JsDataModel] = 0):
    """
    Description:
    ------------
    The lastIndexOf() method returns the position of the last occurrence of a specified value in a string.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_lastindexof.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] search_value: The string to search for.
    :param Union[int, primitives.JsDataModel] start: Integer. Optional. Default 0. At which position to start the
    search.

    :rtype: JsNumber.JsNumber
    """
    from epyk.core.js.primitives import JsNumber

    search_value = JsUtils.jsConvertData(search_value, None)
    return JsNumber.JsNumber("%s.lastIndexOf(%s, %s)" % (self.varId, search_value, start), is_py_data=False)

  def substring(self, start: Union[int, primitives.JsDataModel] = 0,
                end: Optional[Union[int, primitives.JsDataModel]] = None):
    """
    Description:
    ------------
    The substring() method extracts the characters from a string, between two specified indices, and returns the new
    sub string.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_substring.asp

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] start: The position where to start the extraction. First character is at
    index 0.
    :param Optional[Union[int, primitives.JsDataModel]] end: Optional. The position (up to, but not including) where to
    end the extraction.
    If omitted, it extracts the rest of the string
    """
    if end is None:
      end = self.length
    return JsString("%s.substring(%s, %s)" % (self.varId, start, end), is_py_data=False)

  def substr(self, start: Union[int, primitives.JsDataModel] = 0,
             length: Optional[Union[int, primitives.JsDataModel]] = None):
    """
    Description:
    ------------
    The substr() method extracts parts of a string, beginning at the character at the specified position, and returns
    the specified number of characters.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_substr.asp

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] start: The position where to start the extraction. First character is at index 0.
    :param Optional[Union[int, primitives.JsDataModel]] length: Optional. The number of characters to extract.
    If omitted, it extracts the rest of the string.
    """
    if length is None:
      return JsString("%s.substr(%s)" % (self.varId, start), is_py_data=False)

    return JsString("%s.substr(%s, %s)" % (self.varId, start, length), is_py_data=False)

  def replace(self, search_value: Union[str, primitives.JsDataModel], new_value: Union[str, primitives.JsDataModel],
              is_py_data: bool = True):
    """
    Description:
    ------------
    The replace() method replaces a specified value with another value in a string

    The replace() method does not change the string it is called on. It returns a new string.

    Related Pages:

      https://www.w3schools.com/js/js_string_methods.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] search_value: Required. The value, or regular expression,
    that will be replaced by the new value.
    :param Union[str, primitives.JsDataModel] new_value: Required. The value to replace the search value with.
    :param bool is_py_data: Optional.
    """
    if is_py_data:
      search_value = json.dumps(search_value)
      new_value = json.dumps(new_value)
    return JsString("%s.replace(%s, %s)" % (self.varId, search_value, new_value), is_py_data=False)

  def slice(self, start: Union[int, primitives.JsDataModel], end: Optional[Union[int, primitives.JsDataModel]]):
    """
    Description:
    ------------
    The slice() method extracts parts of a string and returns the extracted parts in a new string.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_slice_string.asp

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] start: The position where to begin the extraction.
    First character is at position 0.
    :param Union[int, primitives.JsDataModel] end: Optional.
    The position (up to, but not including) where to end the extraction.
    If omitted, slice() selects all characters from the start-position to the end of the string
    """
    return JsString("%s.replace(%s, %s)" % (self.varId, start, end), is_py_data=False)

  def search(self, search_value: Union[str, primitives.JsDataModel], is_py_data: bool = True):
    """
    Description:
    ------------
    The search() method searches a string for a specified value, and returns the position of the match.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_search.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] search_value: A regular expression. A string will automatically be
    converted to a regular expression..
    :param bool is_py_data: Optional.
    """
    from epyk.core.js.primitives import JsNumber

    if is_py_data:
      search_value = json.dumps(search_value)
    return JsNumber.JsNumber("%s.search(%s)" % (self.varId, search_value), is_py_data=False)

  def concat(self, *args, new_var_name: Optional[str] = None, is_py_data: bool = True):
    """
    Description:
    ------------
    The concat() method is used to join two or more strings.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_concat_string.asp

    Attributes:
    ----------
    :param args: Required. The strings to be joined.
    :param Optional[str] new_var_name: The new Javascript Variable Name.
    :param bool is_py_data: The data input type.

    :return: A new String, containing the text of the combined strings
    """
    variables = []
    for a in args:
      if is_py_data:
        variables.append(json.dumps(a))
      else:
        variables.append(a)

    if new_var_name is not None:
      return "var %s = %s.concat(%s)" % (new_var_name, self.varId, ",".join(variables))

    return JsString("%s.concat(%s)" % (self.varId, ",".join(variables)), is_py_data=False)

  def clean(self):
    """
    Description:
    ------------
    Remove the special characters in a string and only keep the ones necessary to be considered as a valid Javascript
    variable name.
    Indeed some rules are defined for the variable names and the HTML codes values must follow those rules.
    Check are on the Python side with an exception raised but it can also be added on the Javascript side

    Usage::

      page.js.string("iib$% rni233n", varName="MyTest").clean() => returns "iibrni233n"

    Related Pages:

      https://www.w3schools.com/js/js_conventions.asp

    :return: The Python Javascript String transformed to be a variable name
    """
    return JsString("%s.trim().replace(/\W+/g, '')" % self.varId, is_py_data=False)

  def leftTrim(self):
    """
    Description:
    ------------

    """
    return JsString("%s.leftTrim()" % self.varId, is_py_data=False)

  def trim(self):
    """
    Description:
    ------------
    The trim() method removes whitespace from both sides of a string.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_trim_string.asp

    :return: A String, representing the string with removed whitespace from both ends
    """
    return JsString("%s.trim()" % self.varId, is_py_data=False)

  def trimStart(self):
    """
    Description:
    ------------
    The trimStart() method removes whitespace from the beginning of a string. trimLeft() is an alias of this method.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trimStart

    :return: A String, representing the string with removed from the beginning
    """
    return JsString("%s.trimStart()" % self.varId, is_py_data=False)

  def trimEnd(self):
    """
    Description:
    ------------
    The trimEnd() method removes whitespace from the end of a string. trimRight() is an alias of this method.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trimEnd

    :return: A String, representing the string with removed whitespace at the end
    """
    return JsString("%s.trimEnd()" % self.varId, is_py_data=False)

  def charAt(self, i: Union[int, primitives.JsDataModel]):
    """
    Description:
    ------------
    The charAt() method returns the character at the specified index in a string.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_charat.asp

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] i: An integer representing the index of the character you want to return.

    :return: A String, representing the character at the specified index, or an empty string if the index number
    is not found
    """
    return JsString("%s.charAt(%s)" % (self.varId, i), is_py_data=False)

  def charCodeAt(self, i: Union[int, primitives.JsDataModel]):
    """
    Description:
    ------------
    The charCodeAt() method returns the Unicode of the character at the specified index in a string.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_charcodeat.asp

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] i: A number representing the index of the character you want to return.

    :return: A Number, representing the unicode of the character at the specified index.
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.charCodeAt(%s)" % (self.varId, i), is_py_data=False)

  def toLowerCase(self):
    """
    Description:
    ------------
    The toLocaleLowerCase() method converts a string to lowercase letters, according to the host's current locale.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_tolocalelowercase.asp

    :return: A String, representing the value of a string converted to lowercase according to the host's current locale
    """
    return JsString("%s.toLowerCase()" % self.varId, is_py_data=False)

  def toUpperCase(self):
    """
    Description:
    ------------
    The toUpperCase() method converts a string to uppercase letters.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_touppercase.asp

    :return: A String, representing the value of a string converted to uppercase
    """
    return JsString("%s.toUpperCase()" % self.varId, is_py_data=False)

  def toLocaleUpperCase(self, locale: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    The toLocaleUpperCase() method returns the calling string value converted to upper case,
    according to any locale-specific case mappings.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] locale: The locale parameter indicates the locale to be used to convert
    to upper case according to any locale-specific case mappings.

    :return: A String, representing the value of a string converted to uppercase
    """
    return JsString("%s.toLocaleUpperCase(%s)" % (self.varId, JsUtils.jsConvertData(locale, None)), is_py_data=False)

  def includes(self, search_value: Union[str, primitives.JsDataModel], start: Union[int, primitives.JsDataModel] = 0,
               js_funcs: Optional[Union[list, str]] = None, jsObj=None):
    """
    Description:
    ------------
    The includes() method determines whether a string contains the characters of a specified string.
    This function might not work with older browser, so to guarantee a good compatibility the jsObj must be defined.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_includes.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] search_value: The string to search for.
    :param Union[int, primitives.JsDataModel] start: Optional. Default 0. At which position to start the search.
    :param jsObj: Optional. The base Javascript object to add the pollyfill to the Javascript imports.
    :param Optional[Union[list, str]] js_funcs: Optional. The Javascript functions.

    :return: A Boolean. Returns true if the string contains the value, otherwise it returns false
    """
    from epyk.core.js.primitives import JsBoolean

    search_value = JsUtils.jsConvertData(search_value, js_funcs)
    # Add a polyfill to ensure the browser compatibility
    if jsObj is not None:
      jsObj._addImport("babel-polyfill")
    return JsBoolean.JsBoolean("%s.includes(%s, %s)" % (self.varId, search_value, start), is_py_data=False)

  def startsWith(self, search_value: Union[str, primitives.JsDataModel], start: Union[int, primitives.JsDataModel] = 0,
                 js_funcs: Optional[Union[list, str]] = None, jsObj=None):
    """
    Description:
    ------------
    The startsWith() method determines whether a string begins with the characters of a specified string.
    This function might not work with older browser, so to guarantee a good compatibility the jsObj must be defined.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_startswith.asp

    Attributes:
    ----------
    :param str Union[str, primitives.JsDataModel] search_value: The string to search for.
    :param Union[int, primitives.JsDataModel] start: Optional. Default 0. At which position to start the search.
    :param Optional[Union[list, str]] js_funcs: Javascript functions.
    :param jsObj:

    :return: A Boolean. Returns true if the string starts with the value, otherwise it returns false
    """
    from epyk.core.js.primitives import JsBoolean

    # Add a polyfill to ensure the browser compatibility
    if jsObj is not None:
      jsObj._addImport("babel-polyfill")
    search_value = JsUtils.jsConvertData(search_value, js_funcs)
    return JsBoolean.JsBoolean("%s.startsWith(%s, %s)" % (self.varId, search_value, start), is_py_data=False)

  def endsWith(self, search_value: Union[str, primitives.JsDataModel],
               length: Optional[Union[int, primitives.JsDataModel]] = None,
               js_funcs: Optional[Union[list, str]] = None):
    """
    Description:
    ------------
    The endsWith() method determines whether a string ends with the characters of a specified string.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_endswith.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] search_value: The string to search for.
    :param Optional[Union[int, primitives.JsDataModel]] length: Optional. Specify the length of the string to search.
    If omitted, the default value is the length
    of the string.
    :param Optional[Union[list, str]] js_funcs: Javascript functions.

    :return: A Boolean. Returns true if the string ends with the value, otherwise it returns false
    """
    from epyk.core.js.primitives import JsBoolean

    search_value = JsUtils.jsConvertData(search_value, js_funcs)
    if length is not None:
      return JsBoolean.JsBoolean("%s.endsWith(%s, %s)" % (self.varId, search_value, length), is_py_data=False)

    return JsBoolean.JsBoolean("%s.endsWith(%s)" % (self.varId, search_value), is_py_data=False)

  def repeat(self, count: Union[int, primitives.JsDataModel]):
    """
    Description:
    ------------
    The repeat() method returns a new string with a specified number of copies of the string it was called on.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_repeat.asp

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] count: The number of times the original string value should be
    repeated in the new string.

    :return: A String, a new string containing copies of the original string
    """
    return JsString("%s.repeat(%s)" % (self.varId, count), is_py_data=False)

  def split(self, separator: str = "", limit: Optional[int] = None):
    """
    Description:
    ------------
    The split() method is used to split a string into an array of substrings, and returns the new array.
    The empty value is a List with as a first value an emtpy String.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_split.asp

    Attributes:
    ----------
    :param str separator: Optional. Specifies the character, or the regular expression, to use for splitting the string.
                          If omitted, the entire string will be returned (an array with only one item).
    :param Optional[int] limit: Optional. An integer that specifies the number of splits, items after the split limit
    will not be included in the array

    :return: A Python JsArray
    """
    from epyk.core.js.primitives.JsArray import JsArray

    if limit is not None:
      return JsArray("%s.split('%s', %s)" % (self.varId, separator, limit), is_py_data=False)

    return JsArray("%s.split('%s')" % (self.varId, separator), is_py_data=False)

  def splitEmptyArray(self, page: primitives.PageModel, separator: str,
                      limit: Optional[Union[int, primitives.JsDataModel]] = None):
    """
    Description:
    ------------
    The splitEmptyArray() method is used to split a string into an array of substrings, and returns the new array.
    The empty value is an emtpy list.

    Related Pages:

      https://stackoverflow.com/questions/5164883/the-confusion-about-the-split-function-of-javascript

    Attributes:
    ----------
    :param page: Report. The report object in order to register the prototype extension.
    :param str separator: Optional. Specifies the character, or the regular expression, to use for splitting the string.
                      If omitted, the entire string will be returned (an array with only one item).
    :param Optional[Union[int, primitives.JsDataModel]] limit: Optional. An integer that specifies the number of splits,
    items after the split limit will not be included in the array

    :return: A Python JsArray
    """
    from epyk.core.js.primitives.JsArray import JsArray

    page._props.setdefault('js', {}).setdefault('prototypes', {})[
      'String.prototype.splitEmptyArray'] = "function(sep) {var a = this.split(sep); if(a[0] == '' && a.length == 1){ return []}; return a}"
    if limit is not None:
      return JsArray("%s.splitEmptyArray('%s', %s)" % (self.varId, separator, limit), is_py_data=False)

    return JsArray("%s.splitEmptyArray('%s')" % (self.varId, separator), is_py_data=False)

  def formatMoney(self, jsObj, dec_places: Union[int, primitives.JsDataModel],
                  country_code: str = 'UK', profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------


    Attributes:
    ----------
    :param jsObj:
    :param Union[int, primitives.JsDataModel] dec_places: Optional. The number of decimal.
    :param str country_code: Optional. The country code. Default uk.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    jsObj.extendProto(self, "formatMoney", '''var n = parseFloat(this); n.formatMoney(decPlaces, thouSeparator, decSeparator);
      ''', pmts=["decPlaces", "thouSeparator", "decSeparator"], profile=profile)
    return self.parseFloat().formatMoney(jsObj, dec_places, country_code)

  def parseFloat(self):
    """
    Description:
    ------------
    Convert the object to float on the JavaScript side.

    :return: A Python Javascript Number
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("parseFloat(%s)" % self.varId, is_py_data=False)

  def parseInt(self):
    """
    Description:
    ------------
    Convert the object to integer on the JavaScript side.

    :return: A Python Javascript Integer
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("parseInt(%s)" % self.varId, is_py_data=False)

  def toDate(self, js_format: str = "YYYY-MM-DD"):
    """
    Description:
    ------------
    Convert the object to a date object on the JavaScript side.

    TODO: Implement the use of the date format.

    Attributes:
    ----------
    :param str js_format: The date format.
    """
    from epyk.core.js.primitives import JsDate

    js_date = JsDate.JsDate.new("%s" % self.varId, is_py_data=False)
    js_date._js = self._js + js_date._js
    return js_date
