#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO finalize module

from typing import Union, Any
from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class CrossFilter(JsPackage):
  lib_alias = {'js': "crossfilter"}

  def __init__(self, data, component: primitives.HtmlModel = None, js_code: str = None, set_var=True,
               page: primitives.PageModel = None):
    super(CrossFilter, self).__init__(
      component=component, js_code=js_code, selector="crossfilter(%s)" % data, set_var=set_var, page=page)

  @staticmethod
  def permute(array: Union[list, primitives.JsDataModel], index: int):
    """
    Description:
    -----------
    Returns a permutation of the specified array using the specified index.
    The returned array contains the corresponding element in array for each index in index, in order.
    For example, permute(["a", "b", "c"], [1, 2, 0]) returns ["b", "c", "a"].
    It is acceptable for the array and index to be different lengths, and for indexes to be duplicated or omitted

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param Union[list, primitives.JsDataModel] array:
    :param int index:
    """
    return JsObjects.JsArray.JsArray("permute(%s, %s)" % (JsUtils.jsConvertData(array, None), index))

  def add(self, records: Any):
    """
    Description:
    -----------
    Adds the specified records to this crossfilter.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param Any records:
    """
    return self.fnc_closure("add(%s)" % JsUtils.jsConvertData(records, None))

  def removeByValue(self, column: Union[str, primitives.JsDataModel], value: Any):
    """
    Description:
    -----------
    Removes all records that match the current filters from this crossfilter.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] column: The column name in the underlying data
    :param Any value: The value
    """
    return self.fnc_closure("remove(function (d,i) { return d[%s] === %s;})" % (
      JsUtils.jsConvertData(column, None), JsUtils.jsConvertData(value, None)))

  def size(self):
    """
    Description:
    -----------
    Returns the number of records in the crossfilter, independent of any filters.
    For example, if you only added a single batch of records to the Crossfilter, this method would return records.length.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsNumber.JsNumber("%s.size()" % self.varId)

  def groupAll(self, js_code: str):
    """
    Description:
    -----------
    A convenience function for grouping all records and reducing to a single value. See groupAll for details.
    Note: unlike a dimension's groupAll, this grouping observes all current filters.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param js_code: String. The Javascript variable name
    """
    group = GroupAll(selector="%s.groupAll()" % self.varId, js_code=js_code, set_var=True)
    return group

  def dimension(self, columns: Union[list, int], js_code: str = None):
    """
    Description:
    -----------
    Constructs a new dimension using the specified value accessor function

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param Union[list, int] columns: The column name on which the dimension will be defined
    :param str js_code: The Javascript variable name
    """
    ools = {}
    if js_code is None:
      return Dimension(selector=self.toStr(), set_var=False)

    if not isinstance(columns, list):
      columns = [(columns, int)]

    if len(columns) == 1:
      js_columns = "d[%s]" % JsUtils.jsConvertData(columns[0][0], None)
      ools[columns[0][0]] = 0
    else:
      js_frg = []
      for i, col_def in enumerate(columns):
        ools[col_def[0]] = i
        if col_def[1] == str:
          js_frg.append("d[%s]" % JsUtils.jsConvertData(col_def[0], None))
        else:
          js_frg.append("+d[%s]" % JsUtils.jsConvertData(col_def[0], None))
      js_columns = "[%s]" % ", ".join(js_frg)
    dim = Dimension(js_code=js_code, selector="%s.dimension(function(d) { return %s })" % (
      self.varId, js_columns), set_var=True)
    dim.cols = ools
    return dim


class Bissect(JsPackage):

  def by(self, value):
    """
    Description:
    -----------
    Constructs a new bisector using the specified value accessor function, which must return a naturally-ordered value.

    Attributes:
    ----------
    :param value:
    """
    raise NotImplementedError()

  @property
  def right(self):
    """
    Description:
    -----------
    Similar to bisect.left, but returns an insertion point which comes after (to the right of) any existing entries of
    value in array.

    """
    raise NotImplementedError()

  @property
  def left(self):
    """

    """
    raise NotImplementedError()


class Heap(JsPackage):

  def byColumn(self, name: Union[str, JsUtils.jsConvertData]):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param name:
    """
    name = JsUtils.jsConvertData(name, None)
    return self.fnc("function(d) { return d[%s]; }" % name)


class Heapselect(JsPackage):

  def byColumn(self, name: Union[str, JsUtils.jsConvertData]):
    """
    Description:
    -----------
    Constructs a new heapselect function using the specified value accessor function, which must return a
    naturally-ordered value.
    For example, to create a heapselect function for objects based on their property

    Attributes:
    ----------
    :param Union[str, JsUtils.jsConvertData] name: The column name
    """
    name = JsUtils.jsConvertData(name, None)
    return self.fnc("function(d) { return d[%s]; }" % name)


class Insertionsort(JsPackage):

  def byColumn(self, name: Union[str, JsUtils.jsConvertData]):
    """
    Description:
    -----------
    Constructs a new insertionsort function using the specified value accessor function,
    which must return a naturally-ordered value.
    For example, to create a insertionsort function for objects based on their property

    Attributes:
    ----------
    :param Union[str, JsUtils.jsConvertData] name:
    """
    name = JsUtils.jsConvertData(name, None)
    return self.fnc("function(d) { return d[%s]; }" % name)


class Quicksort(JsPackage):

  def byColumn(self, name: Union[str, JsUtils.jsConvertData]):
    """
    Description:
    -----------
    Constructs a new quicksort function using the specified value accessor function, which must return a
    naturally-ordered value.
    For example, to create a quicksort function for objects based on their property

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param Union[str, JsUtils.jsConvertData] name: The column name
    """
    name = JsUtils.jsConvertData(name, None)
    return self.fnc("function(d) { return d[%s]; }" % name)


class Dimension(JsPackage):

  def filter(self, data):
    """
    Description:
    -----------
    Filters records such that this dimension's value matches value, and returns this dimension.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param data:
    """
    self._js.append("filter(%s)" % JsUtils.jsConvertData(data, None))
    return self

  def filterExact(self, value):
    """
    Description:
    -----------
    Filters records such that this dimension's value equals value, and returns this dimension. For example:

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param value:
    """
    raise NotImplementedError()

  def filterRange(self, min: float, max: float):
    """
    Description:
    -----------
    Filters records such that this dimension's value is greater than or equal to range[0], and less than range[1], r
    eturning this dimension.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param float min:
    :param float max:
    """
    self._js.append("filterRange([%s, %s])" % (min, max))
    return self

  def filterOnColumn(self, value: Any, column: str = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Any value:
    :param str column:
    """
    if column is None:
      return JsObjects.JsObject.JsObject("%(id)s.filter(function(d) { return d === %(value)s} )" % {
        'id': self.varId, 'value': JsUtils.jsConvertData(value, None)})

    return JsObjects.JsObject.JsObject("%(id)s.filter(function(d) { return d[%(column)s] === %(value)s} )" % {
      'id': self.varId, 'column': self.cols[column], 'value': JsUtils.jsConvertData(value, None)})

  def filterFunction(self, function):
    """
    Description:
    -----------
    ilters records such that the specified function returns truthy when called with this dimension's value,
    and returns this dimension.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param function:
    """
    raise NotImplementedError()

  def filterAll(self):
    """
    Description:
    -----------
    Clears any filters on this dimension, selecting all records and returning this dimension. For example:

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return self.fnc("filterAll()")

  def id(self):
    """
    Description:
    -----------
    Returns the numeric id of the dimension. For use with crossfilter.isElementFiltered.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference#dimension_group
    """
    return JsObjects.JsNumber.JsNumber("%s.id()" % self.varId)

  def top(self, k: int = None):
    """
    Description:
    -----------
    Returns a new array containing the top k records, according to the natural order of this dimension.
    The returned array is sorted by descending natural order.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param int k: The number of entries to keep

    :return: An array with the data
    """
    if k is None:
      return JsObjects.JsArray.JsArray("%s.top(Infinity)" % self.varId)

    return JsObjects.JsArray.JsArray("%s.top(%s)" % (self.varId, k))

  def bottom(self, k: int):
    """
    Description:
    -----------
    Returns a new array containing the bottom k records, according to the natural order of this dimension.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param int k: The number of entries to keep

    :return: An array with the data
    """
    return JsObjects.JsArray.JsArray("%s.bottom(%s)" % (self.varId, k))

  def dispose(self):
    """
    Description:
    -----------
    Removes this dimension (and its groups) from its crossfilter.
    This frees up space for other dimensions to be added to this crossfilter.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return self.fnc_closure("dispose()")

  def group(self, js_code: str):
    """
    Description:
    -----------
    Constructs a new grouping for the given dimension, according to the specified groupValue function,
    which takes a dimension value as input and returns the corresponding rounded value.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param str js_code: The variable reference for the group.

    """
    group = Group(selector="%s.group()" % self.varId, js_code=js_code, set_var=True)
    return group

  def GroupAll(self, js_code: str):
    """
    Description:
    -----------
    Constructs a new grouping for the given dimension, according to the specified groupValue function,
    which takes a dimension value as input and returns the corresponding rounded value.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param str js_code: The variable reference for the group.
    """
    group = GroupAll(selector="%s.groupAll()" % self.varId, js_code=js_code, set_var=True)
    return group

  def groupFunction(self, js_code: str, func):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_code:
    :param func:
    """
    group = Group(selector="%s.group(%s)" % (self.varId, func), js_code=js_code, set_var=True)
    return group

  def hasCurrentFilter(self):
    """
    Description:
    -----------
    Returns truthy if a filter has been set, or falsy if a filter has not been set on this dimension.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.hasCurrentFilter()" % self.varId)

  def quicksort(self, js_code: str):
    """
    Description:
    -----------
    Sorts the specified subset of the array in-place, returning the array; the lower bound lo is an inclusive index,
    and the upper bound hi is an exclusive index.
    To sort the entire array, specify a lo of 0 and a hi of array.length.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference#dimension_group

    Attributes:
    ----------
    :param str js_code: The variable reference on the Js side of this group.
    """
    return Quicksort(selector="%s.quicksort" % self.varId, js_code=js_code, set_var=True)

  def insertionsort(self, js_code: str):
    """
    Description:
    -----------
    Sorts the specified subset of the array in-place, returning the array; the lower bound lo is an inclusive index,
    and the upper bound hi is an exclusive index.
    To sort the entire array, specify a lo of 0 and a hi of array.length.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference#dimension_group

    Attributes:
    ----------
    :param str js_code: The variable reference on the Js side of this group.
    """
    return Insertionsort(selector="%s.insertionsort" % self.varId, js_code=js_code, set_var=True)

  def heapselect(self, js_code: str):
    """
    Description:
    -----------
    The identity heapselect function; suitable for numbers, dates, strings, and other naturally-comparable objects.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference#dimension_group

    Attributes:
    ----------
    :param str js_code: The variable reference on the Js side of this group.
    """
    return Heapselect(selector="%s.heapselect" % self.varId, js_code=js_code, set_var=True)

  def heap(self, js_code):
    """
    Description:
    -----------
    The identity heapselect function; suitable for numbers, dates, strings, and other naturally-comparable objects.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference#dimension_group

    Attributes:
    ----------
    :param js_code:
    """
    return Heap(selector="%s.heap" % self.varId, js_code=js_code, set_var=True)


class Group(JsPackage):

  def size(self):
    """
    Description:
    -----------
    Returns the number of distinct values in the group, independent of any filters; the cardinality.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsNumber.JsNumber("%s.size()" % self.varId)

  def reduce(self, add, remove, initial):
    """
    Description:
    -----------
    Specifies the reduce functions for this grouping, and returns this grouping.
    The default behavior, reduce by count, is implemented as follows

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param add:
    :param remove:
    :param initial:
    """
    raise NotImplementedError()

  def reduceCount(self, value):
    """
    Description:
    -----------
    A convenience method for setting the reduce functions to count records; returns this group.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference#dimension_group

    Attributes:
    ----------
    :param value: String. The column name

    :return: returns this group
    """
    return self.fnc("reduceCount(function(d) { return d['%s'] ;})" % value)

  def reduceSum(self, value):
    """
    Description:
    -----------
    A convenience method for setting the reduce functions to sum records using the specified value accessor function;

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param value: String. The column name

    :return: returns this group
    """
    return self.fnc("reduceSum(function(d) { return d['%s'] ;})" % value)

  def order(self, order_value):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param order_value:
    """
    raise NotImplementedError()

  def orderNatural(self):
    """
    A convenience method for using natural order for reduce values. Returns this grouping

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    group = Group("%s.orderNatural()" % self.toStr())
    return group

  def top(self, k=None):
    """
    Description:
    -----------
    Returns a new array containing the top k groups, according to the group order of the associated reduce value.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param k:
    """
    if k is None:
      return JsObjects.JsArray.JsArray("%s.top()" % self.varId)

    return JsObjects.JsArray.JsArray("%s.top(%s)" % (self.varId, k))

  def all(self):
    """
    Description:
    -----------
    Returns the array of all groups, in ascending natural order by key. Like top, the returned objects contain key
    and value attributes.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsArray.JsArray("%s.all()" % self.varId)

  def dispose(self):
    """
    Description:
    -----------
    Removes this group from its dimension.
    This group will no longer update when new filters are applied to the crossfilter,
    and it may be garbage collected if there are no other references to it remaining.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsObject.JsObject("%s.dispose()" % self.toStr())


class GroupAll(JsPackage):

  def reduceCount(self, value):
    """
    Description:
    -----------
    A convenience method for setting the reduce functions to count records; returns this group.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference#dimension_group

    Attributes:
    ----------
    :param value: String. The column name

    :return: returns this group
    """
    return self.fnc("reduceCount(function(d) { return d['%s'] ;})" % value)

  def reduceSum(self, value):
    """
    Description:
    -----------
    A convenience method for setting the reduce functions to sum records using the specified value accessor function;

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param value: String. The column name

    :return: returns this group
    """
    return self.fnc("reduceSum(function(d) { return d['%s'] ;})" % value)

  def value(self):
    """
    Description:
    -----------
    Equivalent to group.all()[0].value.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsNumber.JsNumber("%s.value()" % self.varId)

