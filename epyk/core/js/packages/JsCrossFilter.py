"""
CrossFilter API

https://github.com/square/crossfilter/wiki/API-Reference

Example
https://jsfiddle.net/LouisNicolle/k4h8rpmb/2/
https://gist.github.com/phoebebright/3822981

"""

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class CrossFilter(JsPackage):
  lib_alias = "crossfilter"

  def __init__(self, src, varName, data, setVar=True):
    super(CrossFilter, self).__init__(src=src, varName=varName, selector="crossfilter(%s)" % data)
    self.src.jsImports.add(self.lib_alias)

  @staticmethod
  def permute(array, index):
    """
    Returns a permutation of the specified array using the specified index.
    The returned array contains the corresponding element in array for each index in index, in order.
    For example, permute(["a", "b", "c"], [1, 2, 0]) returns ["b", "c", "a"].
    It is acceptable for the array and index to be different lengths, and for indexes to be duplicated or omitted

    :param array:
    :param index:
    :return:
    """
    array = JsUtils.jsConvertData(array, None)
    return JsObjects.JsArray.JsArray("permute(%s, %s)" % (array, index))

  def add(self, records):
    """
    Adds the specified records to this crossfilter.

    :param records:
    :return:
    """

  def remove(self):
    """
    Removes all records that match the current filters from this crossfilter.

    :return:
    """

  def size(self):
    """
    Returns the number of records in the crossfilter, independent of any filters. For example, if you only added a single batch of records to the Crossfilter, this method would return records.length.

    :return:
    """

  def groupAll(self):
    """
    A convenience function for grouping all records and reducing to a single value. See groupAll for details.
    Note: unlike a dimension's groupAll, this grouping observes all current filters.

    :return:
    """

  def dimension(self, column):
    """
    Constructs a new dimension using the specified value accessor function

    :param column: The column name on which the dimension will be defined

    :return:
    """
    self._js.append("dimension(function(d) { return d.%s })" % column)
    return Dimension(varName=self.toStr(), setVar=False)


class Bissect(object):
  def __init__(self, array, value, lo, hi):
    """

    :param array:
    :param value:
    :param lo:
    :param hi:
    """
    self.array, self.value, self.lo, self.hi = array, value, lo, hi
    self._js = []

  def by(self, value):
    """
    Constructs a new bisector using the specified value accessor function, which must return a naturally-ordered value.

    :param value:
    :return:
    """
    return JsObjects.JsObject.JsObject(
      "%s.bisect.by(%s)(%s, %s, %s, %s)" % (self.toStr(), value, self.array, self.value, self.lo, self.hi))

  @property
  def right(self):
    """
    Similar to bisect.left, but returns an insertion point which comes after (to the right of) any existing entries of value in array.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.bisect.right(%s, %s, %s, %s)" % (self.toStr(), self.array, self.value, self.lo, self.hi))

  @property
  def left(self):
    """

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.bisect.left(%s, %s, %s, %s)" % (self.toStr(), self.array, self.value, self.lo, self.hi))


class Heap(object):
  def __init__(self, array, lo, hi):
    """

    :param array:
    :param lo:
    :param hi:
    """
    self.array, self.lo, self.hi = array, lo, hi
    self._js = []

  def by(self, value):
    """

    :param value:
    :return:
    """

  @property
  def sort(self):
    """

    :return:
    """


class Heapselect(object):
  def __init__(self, array, lo, hi, k):
    """

    :param array:
    :param lo:
    :param hi:
    :param k:
    """

  def by(self, value):
    """

    :return:
    """


class Insertionsort(object):
  def __init__(self, array, lo, hi):
    """

    :param array:
    :param lo:
    :param hi:
    """

  def by(self, accessor):
    """

    :param accessor:
    :return:
    """


class Quicksort(object):
  def __init__(self, array, lo, hi):
    """

    :param array:
    :param lo:
    :param hi:
    """

  def by(self, accessor):
    """

    :param accessor:
    :return:
    """


class Dimension(JsPackage):
  def filter(self, jsData):
    """
    Filters records such that this dimension's value matches value, and returns this dimension.

    :return:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    self._js.append("filter(%s)" % jsData)
    return self

  def filterExact(value):
    """
    Filters records such that this dimension's value equals value, and returns this dimension. For example:

    :param value:
    :return:
    """

  def filterRange(self, min, max):
    """
    Filters records such that this dimension's value is greater than or equal to range[0], and less than range[1], returning this dimension.

    :param min:
    :param max:

    :return:
    """
    self._js.append("filterRange([%s, %s])" % (min, max))
    return self

  def filterFunction(function):
    """
    ilters records such that the specified function returns truthy when called with this dimension's value, and returns this dimension.

    :param function:
    :return:
    """

  def filterAll(self):
    """

    :return:
    """
    self._js.append("filterAll()")
    return self

  def top(self, k):
    """
    Returns a new array containing the top k records, according to the natural order of this dimension.
    The returned array is sorted by descending natural order.

    :param k: The number of entries to keep

    :return: An array with the data
    """
    k = JsUtils.jsConvertData(k, None)
    self._js.append("top(%s)" % k)
    return self

  def bottom(self, k):
    """
    Returns a new array containing the bottom k records, according to the natural order of this dimension.

    :param k: The number of entries to keep

    :return: An array with the data
    """
    return JsObjects.JsArray.JsArray("%s.bottom(%s)" % (self.toStr(), k))

  def dispose(self):
    """
    Removes this dimension (and its groups) from its crossfilter.
    This frees up space for other dimensions to be added to this crossfilter.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.dispose()" % self.toStr())

  def group(self, jsFnc):
    """
    Constructs a new grouping for the given dimension, according to the specified groupValue function, which takes a dimension value as input and returns the corresponding rounded value.

    :return:
    """
    groupObj = Group("%s.group(%s)" % (self.toStr(), jsFnc))
    groupObj._set_var = self._set_var
    return groupObj


class Group(object):
  def __init__(self, selector):
    self._selector = selector
    self._js, self._set_var = [], ""

  def size(self):
    """
    Returns the number of distinct values in the group, independent of any filters; the cardinality.

    :return:
    """
    obj = JsObjects.JsNumber.JsNumber(0)
    obj._js.append(self._set_var)
    obj._js.append("%s.size()" % (self.toStr()))
    return obj

  def reduce(self, add, remove, initial):
    """
    Specifies the reduce functions for this grouping, and returns this grouping.
    The default behavior, reduce by count, is implemented as follows

    :param add:
    :param remove:
    :param initial:
    :return:
    """

  def reduceCount(self):
    """
    A convenience method for setting the reduce functions to count records; returns this group.

    :return: returns this group
    """
    self._js.append("%s.reduceCount()" % self.toStr())
    return self

  def reduceSum(self, value):
    """
    A convenience method for setting the reduce functions to sum records using the specified value accessor function;

    :param value:

    :return: returns this group
    """
    self._js.append("%s.reduceSum(%s)" % (self.toStr(), value))
    return self

  def order(self, orderValue):
    """

    :param orderValue:
    :return:
    """

  def orderNatural(self):
    """
    A convenience method for using natural order for reduce values. Returns this grouping

    :return:
    """
    groupObj = Group("%s.orderNatural()" % self.toStr())
    return groupObj

  def top(self, k):
    """
    Returns a new array containing the top k groups, according to the group order of the associated reduce value.

    :param k:
    :return:
    """
    return JsObjects.JsArray.JsArray("%s.top(%s)" % (self.toStr(), k))

  def all(self):
    """
    Returns the array of all groups, in ascending natural order by key. Like top, the returned objects contain key and value attributes.

    :return:
    """
    return JsObjects.JsArray.JsArray("%s.all()" % self.toStr())

  def dispose(self):
    """
    Removes this group from its dimension.
    This group will no longer update when new filters are applied to the crossfilter, and it may be garbage collected if there are no other references to it remaining.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.dispose()" % self.toStr())

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._selector

    strData = "%(jqId)s.%(items)s" % {'jqId': self._selector, 'items': ".".join(self._js)}
    return JsObjects.JsObject.JsObject.get(strData)


class GroupAll(object):
  def __init__(self, selector):
    self._selector = selector
    self._js = []

  def reduce(self, add, remove, initial):
    """

    :param add:
    :param remove:
    :param initial:
    :return:
    """

  def value(self):
    """
    Equivalent to group.all()[0].value.

    :return:
    """
    return JsObjects.JsNumber.JsNumber("%s.all()" % self.toStr())

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._selector

    strData = "%(jqId)s.%(items)s" % {'jqId': self._selector, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return JsObjects.JsObject.JsObject.get(strData)
