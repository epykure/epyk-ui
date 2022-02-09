#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.js.primitives import JsObject
from epyk.core.js.fncs import JsFncs

from epyk.core.js import JsUtils


class JsArray(JsObject.JsObject):
  _jsClass = "Array"

  @property
  def length(self):
    """
    Description:
    -----------
    The length property of an array returns the length of an array (the number of array elements).

    Related Pages:

      https://www.w3schools.com/JS/js_arrays.asp

    :return: A python Javascript Number
    """
    from epyk.core.js.primitives import JsNumber
    return JsNumber.JsNumber("%s.length" % self.varId, is_py_data=False)

  @classmethod
  def set(cls, js_code: str, data: Optional[list] = None, page: primitives.PageModel = None):
    """
    Description:
    -----------
    Define an array. Set an empty array by default

    Attributes:
    ----------
    :param str js_code: The variable name for the speech recognition object.
    :param Optional[list] data:
    :param primitives.PageModel page:
    """
    if data is None:
      data = []
    return cls(data=data, js_code=js_code, set_var=True, page=page)

  def some_(self, js_funcs: Union[list, str]):
    """
    Description:
    -----------
    The some() method checks if any of the elements in an array pass a test (provided as a function).

    Related Pages:

    https://www.w3schools.com/jsref/jsref_some.asp

    Attributes:
    ----------
    :param js_funcs: function(currentValue, index, arr) A function to be run for each element in the array.

    :return: A Javascript Boolean
    """
    from epyk.core.js.primitives import JsBoolean

    return JsBoolean.JsBoolean("%s.some(%s)" % (self.varId, js_funcs), is_py_data=False)

  def every_(self, js_funcs: Union[list, str], js_value: Optional[str] = None, profile: Union[dict, bool] = False):
    """
    Description:
    -----------
    The every() method checks if all elements in an array pass a test (provided as a function).
    Data Structure used in this method is like obj(val, index, array)

    Usage::

      Related Pages:

      https://www.w3schools.com/jsref/jsref_every.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: A function to be run for each element in the array
    :param Optional[str] js_value: Optional. A value to be passed to the function to be used as its "this" value.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if js_value is None:
      return JsFncs.JsFunction("%s.every(function(val, index, arr){%s})" % (self.varId, js_funcs))

    return JsFncs.JsFunction("%s.every(function(val, index, arr){%s}, %s)" % (self.varId, js_funcs, js_value))

  def filter_(self, js_funcs: Union[list, str], js_value: Optional[str] = None, profile: Union[dict, bool] = False):
    """
    Description:
    -----------
    The filter() method creates an array filled with all array elements that pass a test (provided as a function)

    Related Pages:

    https://www.w3schools.com/jsref/jsref_filter.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: A function to be run for each element in the array
    :param Optional[str] js_value: Optional. A value to be passed to the function to be used as its "this" value.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if js_value is None:
      return JsFncs.JsFunction("%s.filter(function(val, index, arr){%s))" % (self.varId, js_funcs))

    return JsFncs.JsFunction("%s.filter(function(val, index, arr){%s), %s)" % (self.varId, js_funcs, js_value))

  def find(self, js_funcs: Union[list, str]):
    """
    Description:
    -----------
    The find() method returns the value of the first element in an array that pass a test (provided as a function)

    Usage::

      Related Pages:

      https://www.w3schools.com/jsref/jsref_find.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: function(currentValue, index, arr)	Required. A function to be run for each
    element in the array.

    :return: Returns the array element value if any of the elements in the array pass the test, otherwise it
    """
    return "%s.find(%s)" % (self.varId, js_funcs)

  def findIndex(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """
    Description:
    -----------
    The find() method returns the value of the first element in an array that pass a test (provided as a function)

    Usage::

      jsObj.console.log(jsObj.objects.array.get("MyArray").findIndex([
      jsObj.if_(jsObj.data.loop.val <= 0, [jsObj.return_(jsObj.objects.true)]),
      jsObj.return_(jsObj.objects.false)
      ]))

    Related Pages:

      https://www.w3schools.com/jsref/jsref_findindex.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: function(currentValue, index, arr)	Required. A function to be run for each
    element in the array.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.

    :return: Returns the array element index if any of the elements in the array pass the test, otherwise it returns -1
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsFncs.JsFunction("%s.findIndex(function(value, index, arr){%s})" % (self.varId, js_funcs))

  def forEach(self, js_funcs: Union[list, str], value: str = "value", profile: Union[dict, bool] = False):
    """
    Description:
    -----------
    The forEach() method calls a provided function once for each element in an array, in order.

    Usage::

      jsObj.objects.get("MyObject").keys().forEach([
      jsObj.console.log(jsObj.data.loop.val)])

    Related Pages:

      https://www.w3schools.com/jsref/jsref_foreach.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: A function to be run for each element in the array
    :param Optional[str] value: Optional. A value to be passed to the function to be used as its "this" value.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsFncs.JsFunction("%s.forEach(function(%s, index, arr){%s})" % (self.varId, value, js_funcs))

  def map(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """
    Description:
    -----------
    The map() method creates a new array with the results of calling a function for every array element.

    Usage::

      jsObj.console.log(jsObj.objects.array.get("MyArray").map([
      jsObj.data.loop.val * jsObj.math.max(jsObj.data.loop.arr.toArgs()),
      jsObj.return_(jsObj.data.loop.val)]))

    Related Pages:

      https://www.w3schools.com/jsref/jsref_map.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: function(currentValue, index, arr)	Required. A function to be run for each
    element in the array.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.

    :return: An Array containing the results of calling the provided function for each element in the original array.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if self.varName is not None:
      return JsArray("%s = %s" % (self.varId, JsArray("%s.map(function(value, index, arr){%s; return value})" % (
        self.varId, js_funcs), is_py_data=False)), is_py_data=False)

    return JsArray("%s.map(function(value, index, arr){%s})" % (self.varId, ";".join(js_funcs)), is_py_data=False)

  def sort(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """
    Description:
    -----------
    The sort() method sorts an array alphabetically:

    Usage::

      jsObj.console.log(jsObj.objects.array.new([2, 5, 12, -3], "MyArray").shift()),
      jsObj.objects.array.get("MyArray").sort()

    Related Pages:

      https://www.w3schools.com/js/js_array_sort.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: function(currentValue, index, arr)	Required. A function to be run for each
    element in the array.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.

    :return: An Array object, representing the joined array
    """
    if js_funcs is not None:
      if not isinstance(js_funcs, list):
        js_funcs = [js_funcs]
      js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
      return JsArray("%s.sort(function(a, b){%s})" % (self.varId, js_funcs))

    return JsArray("%s.sort()" % self.varId, is_py_data=False)

  def reduce(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """
    Description:
    -----------
    The reduce() method reduces the array to a single value.

    Usage::

      jsObj.console.log(jsObj.objects.array.get("MyArray").reduce([
      jsObj.data.reduce.val + jsObj.data.reduce.rVal,
      jsObj.return_(jsObj.data.reduce.val)]))

    Related Pages:

      https://www.w3schools.com/jsref/jsref_reduce.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: function(currentValue, index, arr)	Required. A function to be run for each
    element in the array.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.

    :return: A Python / Javascript Number
    """
    from epyk.core.js.primitives import JsNumber

    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsNumber.JsNumber("%s.reduce(function (r, o, i){%s})" % (self.varId, js_funcs))

  def shift(self):
    """
    Description:
    -----------
    The shift() method removes the first item of an array.

    Usage::

      jsObj.console.log(jsObj.objects.array.new([2, 5, 12, -3], "MyArray").shift()),
      jsObj.console.log(jsObj.objects.array.get("MyArray")),

    Related Pages:

      https://www.w3schools.com/jsref/jsref_shift.asp

    :return: Any type*, representing the removed array item. *An array item can be a string, a number, an array, a
    boolean, or any other object types that are allowed in an array.
    """
    return JsObject.JsObject("%s.shift()" % self.varId, is_py_data=False)

  def slice(self, start: Union[primitives.JsDataModel, int], end: Union[primitives.JsDataModel, int]):
    """
    Description:
    -----------
    The numbers in the table specify the first browser version that fully supports the method

    Usage::

      jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
      jsObj.objects.array.get("MyArray").slice(3, 5)

    Related Pages:

      https://www.w3schools.com/jsref/jsref_slice_array.asp

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, int] start: The index number in the array.
    :param Union[primitives.JsDataModel, int] end: The index number in the array.

    :return: A new Array, containing the selected elements
    """
    start = JsUtils.jsConvertData(start, None)
    end = JsUtils.jsConvertData(end, None)
    return JsArray("%s.slice(%s, %s)" % (self.varId, start, end), is_py_data=False)

  def pop(self):
    """
    Description:
    -----------
    The pop() method removes the last element of an array, and returns that element.

    Usage::

      jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
      jsObj.objects.array.get("MyArray").pop()

    Related Pages:

      https://www.w3schools.com/js/js_array_methods.asp

    :return: Any type*, representing the removed array item. *An array item can be a string, a number, an array,
    a boolean, or any other object types that are allowed in an array.
    """
    return JsObject.JsObject("%s.pop()" % self.varId, is_py_data=False)

  def delete(self, value: Union[float, primitives.JsDataModel]):
    """
    Description:
    -----------
    Since JavaScript arrays are objects, elements can be deleted by using the JavaScript operator
    Using delete may leave undefined holes in the array. Use pop() or shift() instead.

    Usage::

      jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
      jsObj.objects.array.get("MyArray").delete(2)

    Related Pages:

      https://www.w3schools.com/js/js_array_methods.asp

    Attributes:
    ----------
    :param Union[float, primitives.JsDataModel] value: The index of the value in the array to be removed.

    :return: Void, The Javascript String
    """
    value = JsUtils.jsConvertData(value, None)
    return JsFncs.JsFunction("delete %s[%s]" % (self.varId, value))

  def join(self, sep: Union[primitives.JsDataModel, str]):
    """
    Description:
    -----------
    The join() method joins the elements of an array into a string, and returns the string.

    Usage::

      page.js.array(varName="newUrl").join("&")

    Related Pages:

      https://www.w3schools.com/jsref/jsref_join.asp

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, str] sep: Optional. The separator to be used. If omitted, the elements are
    separated with a comma.
    :return: A String, representing the array values, separated by the specified separator.
    """
    from epyk.core.js.primitives import JsString

    sep = JsUtils.jsConvertData(sep, None)
    return JsString.JsString("%s.join(%s)" % (self.varId, JsUtils.jsConvertData(sep, None)), is_py_data=False)

  def copyWithin(self, start: Union[primitives.JsDataModel, int] = 0,
                 end: Optional[Union[primitives.JsDataModel, int]] = None):
    """
    Description:
    -----------
    The copyWithin() method copies array elements within the array, to and from specified positions.

    Usage::

      jsObj.objects.array.new([2, 5, 12, -3], "MyArray")

    Related Pages:

      https://www.w3schools.com/jsref/jsref_copywithin.asp

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, int] start: Optional. The index position to start copying elements from (default is 0)
    :param Optional[Union[primitives.JsDataModel, int]] end: Optional. The index position to stop copying elements from (default is array.length)

    :return: An Array, the changed array
    """
    if end is None:
      end = self.length
    return JsArray("%s.copyWithin(%s, %s)" % (self.varId, start, end), set_var=True, is_py_data=False)

  def fill(self, data: primitives.JsDataModel, start: Union[primitives.JsDataModel, int] = 0,
           end: Optional[Union[primitives.JsDataModel, int]] = None,
           js_funcs: Union[list, str] = None, js_obj=None):
    """
    Description:
    -----------
    The fill() method fills the specified elements in an array with a static value.
    The fill() method is not supported in Internet Explorer 11 and earlier versions.

    Usage::

      jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
      jsObj.objects.array.get("MyArray").fill("test", 0, 2)

    Related Pages:

      https://www.w3schools.com/jsref/jsref_fill.asp

    Attributes:
    ----------
    :param primitives.JsDataModel data: The value to fill the array with.
    :param Union[primitives.JsDataModel, int] start: Optional. The index to start filling the array (default is 0).
    :param Optional[Union[primitives.JsDataModel, int]] end: Optional. The index to stop filling the array (default is array.length).
    :param Union[list, str] js_funcs: Optional. The Javascript functions.
    :param js_obj: Optional, The base Python Javascript object to add the polyfill.

    :return: An Array, the changed array
    """
    if js_obj is not None:
      # Add a polyfill to ensure the browser compatibility
      js_obj._addImport("babel-polyfill")
    data = JsUtils.jsConvertData(data, js_funcs)
    if start is not None:
      start = JsUtils.jsConvertData(start, None)
      if end is not None:
        end = JsUtils.jsConvertData(end, None)
        return JsArray("%s.fill(%s, %s, %s)" % (self.varId, data, start, end), is_py_data=False)

      else:
        return JsArray("%s.fill(%s, %s)" % (self.varId, data, start), is_py_data=False)

    return JsArray("%s.fill(%s)" % (self.varId, data), is_py_data=False)

  def concat(self, *args):
    """
    Description:
    -----------
    The concat() method is used to join two or more arrays.
    This method does not change the existing arrays, but returns a new array, containing the values of the joined
    arrays.

    Usage::

      jsObj.objects.array.new([2, 5, 12, -3], "MyArray"),
      jsObj.objects.array.new([3, -9, 2, -6], "MyArray2"),
      jsObj.objects.array.new([], "MyArray3"),
      jsObj.console.log(
        jsObj.objects.array.get("MyArray3").concat(jsObj.objects.array.get("MyArray"),
        jsObj.objects.array.get("MyArray2"))),

    Related Pages:

      https://www.w3schools.com/jsref/jsref_concat_array.asp

    Attributes:
    ----------
    :param args: Existing Javascript Arrays

    :return: An Array object, representing the joined array
    """
    return JsArray("%s.concat(%s)" % (
      self.varId, ", ".join([str(JsUtils.jsConvertData(a, None)) for a in args])), is_py_data=False)

  def append(self, js_obj, val: Union[primitives.JsDataModel, str]):
    """
    Description:
    -----------
    Equivalent to append Python function for the Javascript

    Usage::

      jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
      jsObj.objects.array.get("MyArray").append(jsObj, 34).append(jsObj, -47)

    Related Pages:

      https://www.w3schools.com/js/js_array_methods.asp
      https://www.w3schools.com/python/ref_list_append.asp

    Attributes:
    ----------
    :param js_obj: The Python Javascript base object.
    :param val: The value to be added.

    :return: The Python / Javascript Array
    """
    js_obj.extendProto(self, "append", [
      js_obj.objects.array.get("this").push(js_obj.objects.get("val")),
      js_obj.return_(js_obj.objects.array.get("this"))], pmts=["val"])
    return JsArray("%s.append(%s)" % (self.varId, JsUtils.jsConvertData(val, None)), is_py_data=False)

  def push(self, *args):
    """
    Description:
    -----------
    The push() method adds new items to the end of an array, and returns the new length.

    Usage::

      jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
      jsObj.objects.array.get("MyArray").push(55, -17)

    Related Pages:

      https://www.w3schools.com/js/js_array_methods.asp

    Attributes:
    ----------
    :param args: A list of object to be added to the JsArray object

    :return: A Number, representing the new length of the array
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("%s.push(%s)" % (
      self.varId, ", ".join([str(JsUtils.jsConvertData(a, None)) for a in args])), is_py_data=False)

  def push_dict(self, **kwargs):
    """
    Description:
    -----------

    page.js.objects.array.get("myArray").push_dict(x="a", y=45)

    Attributes:
    ----------
    :param kwargs:
    """
    args = []
    for k, v in kwargs.items():
      args.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
    return self.push(JsObject.JsObject.get("{%s}" % ", ".join(args)))

  def reverse(self):
    """
    Description:
    -----------
    The reverse() method reverses the elements in an array.

    Usage::

      jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
      jsObj.objects.array.get("MyArray").reverse()

    Related Pages:

      https://www.w3schools.com/js/js_array_sort.asp

    :return: An Array, representing the array after it has been reversed
    """
    return JsArray("%s.reverse()" % self.varId, is_py_data=False)

  def flat(self, depth: Union[primitives.JsDataModel, int] = 1):
    """
    Description:
    -----------
    The flat() method creates a new array with all sub-array elements concatenated into it recursively up to the
    specified depth.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, int] depth: The depth level specifying how deep a nested array structure
    should be flattened. Defaults to 1.
    """
    return JsArray("%s.flat(%s)" % (self.varId, JsUtils.jsConvertData(depth, None)), is_py_data=False)

  def flatMap(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """
    Description:
    -----------
    The flatMap() method first maps each element using a mapping function, then flattens the result into a new array.
    It is identical to a map() followed by a flat() of depth 1, but flatMap() is often quite useful, as merging both
    into one method is slightly more efficient.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap

    Attributes:
    ----------
    :param Union[list, str] js_funcs: function(currentValue, index, arr). A function to be run for each element in the array.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.

    :return: An Array containing the results of calling the provided function for each element in the original array.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if self.varName is not None:
      return JsArray("%s = %s" % (self.varId, JsArray(
        "%s.flatMap(function(value, index, arr){%s; return value})" % (
          self.varId, js_funcs), is_py_data=False)), is_py_data=False)

    return JsArray("%s.flatMap(function(value, index, arr){%s})" % (self.varId, js_funcs), is_py_data=False)

  def includes(self, element: Union[primitives.JsDataModel, str], start: int = 0):
    """
    Description:
    -----------
    The includes() method determines whether an array contains a specified element.

    This method returns true if the array contains the element, and false if not.

    Note: The includes() method is case sensitive.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_includes_array.asp

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, str] element: Object. The element to search for.
    :param int start: Optional. Default 0. At which position in the array to start the search.
    """
    from epyk.core.js.primitives import JsBoolean

    return JsBoolean.JsBoolean("%s.includes(%s, %s)" % (
      self.varId, JsUtils.jsConvertData(element, None), start), is_py_data=False)

  def unshift(self, *args):
    """
    Description:
    -----------
    The unshift() method adds a new element to an array (at the beginning), and "unshifts" older elements.

    Usage::

      jsObj.objects.array.new([2, 5, 12, -3], "MyArray")
    jsObj.objects.array.get("MyArray").unshift(22)

    Related Pages:

      https://www.w3schools.com/js/js_array_methods.asp

    Attributes:
    ----------
    :param args: Required. The item(s) to add to the beginning of the array

    :return: A Number, representing the new length of the array
    """
    return JsArray("%s.unshift(%s)" % (self.varId, ", ".join([str(JsUtils.jsConvertData(a, None)) for a in args])))

  def splice(self, i: int, j: int, data: Union[primitives.JsDataModel, str],
             js_funcs: Optional[Union[list, str]] = None):
    """
    Description:
    -----------
    The splice() method can be used to add new items to an array
    With clever parameter setting, you can use splice() to remove elements without leaving "holes" in the array

    Related Pages:

    https://www.w3schools.com/js/js_array_methods.asp

    Attributes:
    ----------
    :param int i: An integer that specifies at what position to add/remove items, Use negative values to.
    specify the position from the end of the array.
    :param int j: Optional. The number of items to be removed. If set to 0, no items will be removed.
    :param Union[primitives.JsDataModel, str] data: Optional. The new item(s) to be added to the array.
    :param Optional[Union[list, str]] js_funcs: Optional. The Javascript functions.

    :return: A new Array, containing the removed items (if any)
    """
    data = JsUtils.jsConvertData(data, js_funcs)
    return JsArray("%s.splice(%s, %s, %s)" % (self.varId, i, j, data))

  def __getitem__(self, index: int):
    if not isinstance(index, int):
      return JsObject.JsObject("%s[%s]" % (self.varId, index), page=self.page)

    if index < 0:
      return JsObject.JsObject("%s[%s %s]" % (self.varId, self.length, index), page=self.page)

    return JsObject.JsObject("%s[%s]" % (self.varId, index), page=self.page)

  def unique(self, js_obj):
    """
    Description:
    -----------
    Prototype Extension

    Usage::

      jsObj.objects.array.new([2, 2, -3, -3], "MyArray")
      jsObj.objects.array.get("MyArray").unique()

    Attributes:
    ----------
    :param js_obj: The Python Javascript base object.

    :return: A new Python Javascript Array with unique values.
    """
    js_obj.extendProto(self, "unique", '''
      var arrayResult = [];this.forEach(function(item){
      if(arrayResult.indexOf(item) < 0){arrayResult.push(item)}}); return arrayResult''')
    return JsArray("%s.unique()" % self.varId)

  def contains(self, js_obj, data: primitives.JsDataModel):
    """
    Description:
    -----------
    Prototype Extension

    Alternative to the includes function and compatible with all the browsers

    Usage::

      jsObj.objects.array.new([2, 2, -3, -3], "MyArray")
      jsObj.objects.array.get("MyArray").contains(2)

    Attributes:
    ----------
    :param js_obj: The Python Javascript base object.
    :param primitives.JsDataModel data: The object to look for in the array.

    :return: A Python Javascript boolean.
    """
    from epyk.core.js.primitives import JsBoolean

    js_obj.extendProto(self, "contains", '''
      var i = this.length; while (i--){if (this[i] === obj){return true}}; return false
      ''', pmts=["data"])
    return JsBoolean.JsBoolean("%s.contains(%s)" % (self.varId, JsUtils.jsConvertData(data, None)), is_py_data=False)

  def toArgs(self):
    """
    Description:
    -----------

    """
    return JsObject.JsObject("...%s" % self.varId)

  def toDict(self, header: list):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param list header:
    """
    return JsObject.JsObject(
      "(function(r, h){var rec = {}; h.forEach(function(c, i){rec[c] = r[i]}); return rec})(%s, %s)" % (
        self.varId, header))

  def sample(self, n: Union[int, primitives.JsDataModel] = None, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Produce a random sample from the list. Pass a number to return n random elements from the list.
    Otherwise a single random item will be returned.

    Related Pages:

      https://underscorejs.org/#arrays

    Attributes:
    ----------
    :param Optional[int, primitives.JsDataModel] n: An index.
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    if n is not None:
      if self.varName is None:
        return JsArray("(function(){return _.sample(%s, %s)})()" % (self.toStr(), n), page=page)

      return JsArray("(function(){%s; return _.sample(%s, %s)})()" % (self.toStr(), self.varName, n), page=page)

    if self.varName is None:
      return JsArray("(function(){return _.sample(%s)})()" % self.toStr(), page=page)

    return JsArray("(function(){%s; return _.sample(%s)})()" % (self.toStr(), self.varName), page=page)

  def first(self, n: Union[int, primitives.JsDataModel] = None, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Returns the first element of an array. Passing n will return the first n elements of the array.

    Usage::

      page.js.objects.list([1, 2, 3, 4, 5, 6])

    Related Pages:

      https://underscorejs.org/#arrays

    Attributes:
    ----------
    :param Optional[int, primitives.JsDataModel] n: An index.
    :param Optional[primitives.PageModel] page: The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    if n is not None:
      if self.varName is None:
        return JsArray("(function(){return _.first(%s, %s)})()" % (self.toStr(), n), page=page)

      return JsArray("(function(){%s; return _.first(%s, %s)})()" % (self.toStr(), self.varName, n), page=page)

    if self.varName is None:
      return JsArray("(function(){return _.first(%s)})()" % self.varName, page=page)

    return JsArray("(function(){%s; return _.first(%s)})()" % (self.toStr(), self.varName), page=page)

  def last(self, n: Union[int, primitives.JsDataModel] = None, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Returns the last element of an array. Passing n will return the last n elements of the array.

    Usage::

      page.data.js.list("test", [1, 2, 3, 4, 5, 6]).sample(3).last(1)

    Related Pages:

      https://underscorejs.org/#arrays

    Attributes:
    ----------
    :param Optional[int, primitives.JsDataModel] n: An index.
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    if n is not None:
      if self.varName is None:
        return JsArray("(function(){return _.last(%s, %s)})()" % (self.toStr(), n), page=page)

      return JsArray("(function(){%s; return _.last(%s, %s)})()" % (self.toStr(), self.varName, n), page=page)

    if self.varName is None:
      return JsArray("(function(){return _.last(%s)})()" % self.varName, page=page)

    return JsArray("(function(){%s; return _.last(%s)})()" % (self.toStr(), self.varName), page=page)

  def chunk(self, n: Union[int, primitives.JsDataModel] = None, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Chunks an array into multiple arrays, each containing length or fewer items.

    Usage::

      page.data.js.list("test", [1, 2, 3, 4, 5, 6]).sample(3).last(1)

    Related Pages:

      https://underscorejs.org/#chunk

    Attributes:
    ----------
    :param Optional[int, primitives.JsDataModel] n: The length of the sub lists.
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    if n is not None:
      if self.varName is None:
        return JsArray("(function(){return _.chunk(%s, %s)})()" % (self.toStr(), n), page=page)

      return JsArray("(function(){%s; return _.chunk(%s, %s)})()" % (self.toStr(), self.varName, n), page=page)

    if self.varName is None:
      return JsArray("(function(){return _.chunk(%s)})()" % self.varName, page=page)

    return JsArray("(function(){%s; return _.chunk(%s)})()" % (self.toStr(), self.varName), page=page)

  def initial(self, n: Union[int, primitives.JsDataModel] = None, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Returns everything but the last entry of the array. Especially useful on the arguments object.
    Pass n to exclude the last n elements from the result.

    Usage::

      page.data.js.list("test", [1, 2, 3, 4, 5, 6]).initial(3)

    Related Pages:

      https://underscorejs.org/#initial

    Attributes:
    ----------
    :param Optional[int, primitives.JsDataModel] n: An index.
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    if n is not None:
      if self.varName is None:
        return JsArray("(function(){return _.initial(%s, %s)})()" % (self.toStr(), n), page=page)

      return JsArray("(function(){%s; return _.initial(%s, %s)})()" % (self.toStr(), self.varName, n), page=page)

    if self.varName is None:
      return JsArray("(function(){return _.initial(%s)})()" % self.varName, page=page)

    return JsArray("(function(){%s; return _.initial(%s)})()" % (self.toStr(), self.varName), page=page)

  def rest(self, n: Union[int, primitives.JsDataModel] = None, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Returns the rest of the elements in an array. Pass an index to return the values of the array from that index
    onward.

    Usage::

      page.data.js.list("test", [1, 2, 3, 4, 5, 6]).sample(3).rest(1)

    Related Pages:

      https://underscorejs.org/#arrays

    Attributes:
    ----------
    :param Optional[int, primitives.JsDataModel] n: An index.
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    if n is not None:
      if self.varName is None:
        return JsArray("(function(){return _.rest(%s, %s)})()" % (self.toStr(), n), page=page)

      return JsArray("(function(){%s; return _.rest(%s, %s)})()" % (self.varName, self.varName, n), page=page)

    if self.varName is None:
      return JsArray("(function(){return _.rest(%s)})()" % self.toStr(), page=page)

    return JsArray("(function(){%s; return _.rest(%s)})()" % (self.toStr(), self.varName), page=page)

  def where(self, values: Union[list, primitives.JsDataModel] = None, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Looks through each value in the list, returning an array of all the values that matches the key-value pairs
    listed in properties.

    Related Pages:

      https://underscorejs.org/#where

    Attributes:
    ----------
    :param Optional[list, primitives.JsDataModel] values: All the values to be removed.
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    values = JsUtils.jsConvertData(values, None)
    page = page or self.page
    page.jsImports.add('underscore')
    if self.varName is None:
      return JsArray("(function(){return _.where(%s, %s)})()" % (self.toStr(), values), page=page)

    return JsArray("(function(){%s; return _.where(%s, %s)})()" % (self.toStr, self.varName, values), page=page)

  def without(self, values: Union[list, primitives.JsDataModel] = None, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Returns a copy of the array with all instances of the values removed.

    Related Pages:

      https://underscorejs.org/#arrays

    Attributes:
    ----------
    :param Optional[list, primitives.JsDataModel] values: All the values to be removed.
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    if self.varName is None:
      return JsArray("(function(){return _.without(%s, %s)})()" % (self.toStr(), values), page=page)

    return JsArray("(function(){%s; return _.without(%s, %s)})()" % (self.toStr, self.varName, values), page=page)

  def union(self, arrays: Union[primitives.JsDataModel, list] = None, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Computes the union of the passed-in arrays: the list of unique items, in order, that are present in one or more
    of the arrays.

    Related Pages:

      https://underscorejs.org/#arrays

    Attributes:
    ----------
    :param Optional[primitives.JsDataModel, list] arrays: The list of lists to sum.
    :param page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    arrays = JsUtils.jsConvertData(arrays, None)
    if self.varName is None:
      return JsArray("(function(){return _.union(%s, ...%s)})()" % (self.toStr(), arrays), page=page)

    return JsArray("(function(){%s; return _.union(%s, ...%s)})()" % (self.toStr, self.varName, arrays), page=page)

  def intersection(self, arrays: Union[primitives.JsDataModel, list] = None,
                   page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Computes the union of the passed-in arrays: the list of unique items, in order, that are present in one or more
    of the arrays.

    Related Pages:

      https://underscorejs.org/#intersection

    Attributes:
    ----------
    :param Optional[primitives.JsDataModel, list] arrays: The list of lists to process.
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    arrays = JsUtils.jsConvertData(arrays, None)
    if self.varName is None:
      return JsArray("(function(){return _.intersection(%s, ...%s)})()" % (self.toStr(), arrays), page=page)

    return JsArray("(function(){%s; return _.intersection(%s, ...%s)})()" % (
      self.toStr, self.varName, arrays), page=page)

  def uniq(self, is_sorted: Union[bool, primitives.JsDataModel] = False, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Computes the union of the passed-in arrays: the list of unique items, in order, that are present in one or more
    of the arrays.

    Related Pages:

      https://underscorejs.org/#arrays

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] is_sorted: Flag to specify if the list is sorted.
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    is_sorted = JsUtils.jsConvertData(is_sorted, None)
    if is_sorted:
       return JsArray("_.uniq(%s, %s)" % (self.varId, is_sorted), page=page)

    return JsArray("_.uniq(%s)" % self.varId, page=page)

  @property
  def every(self):
    """
    Description:
    -----------
    Returns true if all of the values in the list pass the predicate truth test.
    Short-circuits and stops traversing the list if a false element is found. predicate is transformed through iteratee
    to facilitate shorthand syntaxes.
    """
    return JaArrayRejector("every", self.toStr(), self.varName, self.page)

  @property
  def some(self):
    """
    Description:
    -----------
    Returns true if any of the values in the list pass the predicate truth test.
    Short-circuits and stops traversing the list if a true element is found. predicate is transformed through iteratee
    to facilitate shorthand syntaxes.
    """
    return JaArrayRejector("some", self.toStr(), self.varName, self.page)

  @property
  def reject(self):
    """
    Description:
    -----------
    Returns the values in list without the elements that the truth test (predicate) passes.
    The opposite of filter. predicate is transformed through iteratee to facilitate shorthand syntaxes.
    """
    return JaArrayRejector("reject", self.toStr(), self.varName, self.page)

  @property
  def filter(self):
    """
    Description:
    -----------

    """
    return JaArrayRejector("filter", self.toStr(), self.varName, self.page)

  def range(self, stop: int, start: int = 0, step: int = 1, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    A function to create flexibly-numbered lists of integers, handy for each and map loops. start, if omitted, defaults
    to 0; step defaults to 1.
    Returns a list of integers from start (inclusive) to stop (exclusive), incremented (or decremented) by
    step, exclusive.
    Note that ranges that stop before they start are considered to be zero-length instead of negative — if you'd like
    a negative range, use a negative step.

    Related Pages:

      https://underscorejs.org/#arrays

    Attributes:
    ----------
    :param int stop: The index of the last value
    :param int start: The index of the first value
    :param int step: The step
    :param Optional[primitives.PageModel] page: Optional. The report object
    """
    page = page or self.page
    page.jsImports.add('underscore')
    return JsArray("_.range(%s, %s, %s)" % (start, stop, step), page=page)

  def object(self, keys: list, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Converts arrays into objects. Pass either a single list of [key, value] pairs, or a list of keys, and a list
    of values.
    Passing by pairs is the reverse of pairs. If duplicate keys exist, the last value wins.

    Related Pages:

      https://underscorejs.org/#arrays

    Attributes:
    ----------
    :param list keys: The keys for the dictionary.
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    return JsObject.JsObject("_.zip(%s, %s)" % (keys, self.varId), page=page)


class JaArrayRejector:

  def __init__(self, func_name: str, data, js_code: str, page: primitives.PageModel):
    self.page, self.varName, self.data, self.func_name = page, js_code, data, func_name

  def modulo(self, n: Union[int, primitives.JsDataModel]):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[int, primitives.JsDataModel] n:
    """
    if self.varName is None:
      return JsArray("_.%s(%s, function(num){ return num %% %s == 0; })" % (
        self.func_name, self.data, n), page=self.page)

    return JsArray("(function(){%s; return _.%s(%s, function(num){ return num %% %s == 0; })})()" % (
      self.data, self.func_name, self.varName, n), page=self.page)

  def equal(self, val: Union[primitives.JsDataModel, list]):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, list] val:
    """
    val = JsUtils.jsConvertData(val, None)
    if self.varName is None:
      return JsArray("_.%s(%s, function(num){ return num == %s; })" % (
        self.func_name, self.data, val), page=self.page)

    return JsArray("(function(){%s; return _.%s(%s, function(num){ return num == %s; })})()" % (
      self.data, self.func_name, self.varName, val), page=self.page)

  def includes(self, values: Union[primitives.JsDataModel, list]):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, list] values:
    """
    values = JsUtils.jsConvertData(values, None)
    if self.varName is None:
      return JsArray("_.%s(%s, function(num){ return %s.includes(num); })" % (
        self.func_name, self.data, values), page=self.page)

    return JsArray("(function(){%s; return _.%s(%s, function(num){ return %s.includes(num); })})()" % (
      self.data, self.func_name, self.varName, values), page=self.page)

  def custom(self, js_expr: str):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param str js_expr: The JavaScript expression.
    """
    if self.varName is None:
      return JsArray("_.%s(%s, function(num){ %s; })" % (self.func_name, self.data, js_expr), page=self.page)

    return JsArray("(function(){%s; return _.%s(%s, function(num){ %s; })})()" % (
      self.data, self.func_name, self.varName, js_expr), page=self.page)


class JsRecordSet(JsArray):

  def distinct(self, col_name: Union[primitives.JsDataModel, str]):
    """
    Description:
    -----------
    Return a sorted list based on a column in the recordset.
    This can be used to feed a selection box or a list component

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, str] col_name: The column in the dictionary.
    """
    col_name = JsUtils.jsConvertData(col_name, None)
    return JsArray.get("(function(data){var result = {}; data.forEach(function(rec){result[rec[%s]] = true}); return Object.keys(result).sort() })(%s)" % (col_name, self.toStr()))

  def to_dict(self, col_name: Union[primitives.JsDataModel, str], value_name: Union[primitives.JsDataModel, str]):
    """
    Description:
    -----------
    Return a dictionary from the records. This function will sum the values to aggregate the data per colName.

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, str] col_name: The column in the dictionary.
    :param Union[primitives.JsDataModel, str] value_name: The column in the dictionary.
    """
    col_name = JsUtils.jsConvertData(col_name, None)
    value_name = JsUtils.jsConvertData(value_name, None)
    return JsArray.get("(function(data){var result = {}; data.forEach(function(rec){if (!(rec[%(col)s] in result)){result[rec[%(col)s]] = 0}; result[rec[%(col)s]] += parseFloat(rec[%(val)s])}); return result })(%(record)s)" % {"col": col_name, "val": value_name, "record": self.toStr()})
