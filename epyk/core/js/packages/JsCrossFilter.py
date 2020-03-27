
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class CrossFilter(JsPackage):
  lib_alias = {'js': "crossfilter"}

  def __init__(self, src, varName, data, setVar=True):
    super(CrossFilter, self).__init__(src=src, varName=varName, selector="crossfilter(%s)" % data, setVar=setVar)

  @staticmethod
  def permute(array, index):
    """
    Description:
    -----------
    Returns a permutation of the specified array using the specified index.
    The returned array contains the corresponding element in array for each index in index, in order.
    For example, permute(["a", "b", "c"], [1, 2, 0]) returns ["b", "c", "a"].
    It is acceptable for the array and index to be different lengths, and for indexes to be duplicated or omitted

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param array:
    :param index:
    """
    return JsObjects.JsArray.JsArray("permute(%s, %s)" % (JsUtils.jsConvertData(array, None), index))

  def add(self, records):
    """
    Description:
    -----------
    Adds the specified records to this crossfilter.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param records:
    """
    self.fnc_closure("add(%s)" % JsUtils.jsConvertData(records, None))

  def remove(self):
    """
    Description:
    -----------
    Removes all records that match the current filters from this crossfilter.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """

  def size(self):
    """
    Description:
    -----------
    Returns the number of records in the crossfilter, independent of any filters.
    For example, if you only added a single batch of records to the Crossfilter, this method would return records.length.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsNumber.JsNumber("%s.size()" % self.varId)

  def groupAll(self):
    """
    Description:
    -----------
    A convenience function for grouping all records and reducing to a single value. See groupAll for details.
    Note: unlike a dimension's groupAll, this grouping observes all current filters.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """

  def dimension(self, columns, varName=None):
    """
    Description:
    -----------
    Constructs a new dimension using the specified value accessor function

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param column: The column name on which the dimension will be defined
    :param varName:
    """
    # self.fnc("dimension(function(d) { return d.%s })" % column)
    if varName is None:
      return Dimension(selector=self.toStr(), setVar=False)

    if not isinstance(columns, list):
      columns = [(columns, int)]

    if len(columns) == 1:
      js_columns = "d['%s']" % columns[0][0]
    else:
      js_columns = "[%s]" % ", ".join(["d['%s']" % d if v == str else "+d['%s']" % d for d, v in columns])
    return Dimension(varName=varName, selector="%s.dimension(function(d) { return %s })" % (self.varId, js_columns), setVar=True)


class Bissect(object):

  def __init__(self, array, value, lo, hi):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param array:
    :param value:
    :param lo:
    :param hi:
    """
    self.array, self.value, self.lo, self.hi = array, value, lo, hi
    self._js = []

  def by(self, value):
    """
    Description:
    -----------
    Constructs a new bisector using the specified value accessor function, which must return a naturally-ordered value.

    Attributes:
    ----------
    :param value:
    """
    return JsObjects.JsObject.JsObject(
      "%s.bisect.by(%s)(%s, %s, %s, %s)" % (self.toStr(), value, self.array, self.value, self.lo, self.hi))

  @property
  def right(self):
    """
    Description:
    -----------
    Similar to bisect.left, but returns an insertion point which comes after (to the right of) any existing entries of value in array.

    """
    return JsObjects.JsObject.JsObject("%s.bisect.right(%s, %s, %s, %s)" % (self.toStr(), self.array, self.value, self.lo, self.hi))

  @property
  def left(self):
    """

    """
    return JsObjects.JsObject.JsObject("%s.bisect.left(%s, %s, %s, %s)" % (self.toStr(), self.array, self.value, self.lo, self.hi))


class Heap(object):

  def __init__(self, array, lo, hi):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param array:
    :param lo:
    :param hi:
    """
    self.array, self.lo, self.hi = array, lo, hi
    self._js = []

  def by(self, value):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param value:
    """

  @property
  def sort(self):
    """

    """


class Heapselect(object):

  def __init__(self, array, lo, hi, k):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param array:
    :param lo:
    :param hi:
    :param k:
    """

  def by(self, value):
    """

    """


class Insertionsort(object):

  def __init__(self, array, lo, hi):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param array:
    :param lo:
    :param hi:
    """

  def by(self, accessor):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param accessor:
    """


class Quicksort(object):

  def __init__(self, array, lo, hi):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param array:
    :param lo:
    :param hi:
    """

  def by(self, accessor):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param accessor:
    """


class Dimension(JsPackage):

  def filter(self, jsData):
    """
    Description:
    -----------
    Filters records such that this dimension's value matches value, and returns this dimension.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    self._js.append("filter(%s)" % JsUtils.jsConvertData(jsData, None))
    return self

  def filterExact(value):
    """
    Description:
    -----------
    Filters records such that this dimension's value equals value, and returns this dimension. For example:

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param value:
    """

  def filterRange(self, min, max):
    """
    Description:
    -----------
    Filters records such that this dimension's value is greater than or equal to range[0], and less than range[1], returning this dimension.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param min:
    :param max:
    """
    self._js.append("filterRange([%s, %s])" % (min, max))
    return self

  def filterOnColumn(self, value, column_index=None):
    """

    :param column_index:
    :param value:
    """
    if column_index is None:
      return self.fnc("filter(function(d) { return d === %(value)s} )" % {'value': JsUtils.jsConvertData(value, None)})

    return self.fnc("filter(function(d) {console.log(d[%(column)s]=== %(value)s) ; return d[%(column)s] === %(value)s} )" % {'column': column_index, 'value': JsUtils.jsConvertData(value, None)})

  def filterFunction(function):
    """
    Description:
    -----------
    ilters records such that the specified function returns truthy when called with this dimension's value, and returns this dimension.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param function:
    """

  def filterAll(self):
    """
    Description:
    -----------
    Clears any filters on this dimension, selecting all records and returning this dimension. For example:

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return self.fnc("filterAll()")

  def top(self, k=None):
    """
    Description:
    -----------
    Returns a new array containing the top k records, according to the natural order of this dimension.
    The returned array is sorted by descending natural order.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param k: The number of entries to keep

    :return: An array with the data
    """
    if k is None:
      return JsObjects.JsArray.JsArray("%s.top(Infinity)" % self.varId)

    return JsObjects.JsArray.JsArray("%s.top(%s)" % (self.varId, k))

  def bottom(self, k):
    """
    Description:
    -----------
    Returns a new array containing the bottom k records, according to the natural order of this dimension.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param k: The number of entries to keep

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
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsObject.JsObject("%s.dispose()" % self.toStr())

  def group(self, varName):
    """
    Description:
    -----------
    Constructs a new grouping for the given dimension, according to the specified groupValue function, which takes a dimension value as input and returns the corresponding rounded value.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    groupObj = Group(selector="%s.group()" % self.varId, varName=varName, setVar=True)
    return groupObj

  def groupFunction(self, varName, Fnc):
    groupObj = Group(selector="%s.group(%s)" % (self.varId, Fnc), varName=varName, setVar=True)
    return groupObj

    # groupObj = Group("%s.group(%s)" % (self.toStr(), jsFnc))
    # groupObj._set_var = self._set_var
    # return groupObj

  def hasCurrentFilter(self):
    """
    Description:
    -----------
    Returns truthy if a filter has been set, or falsy if a filter has not been set on this dimension.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.hasCurrentFilter()" % self.varId)


class Group(JsPackage):

  def size(self):
    """
    Description:
    -----------
    Returns the number of distinct values in the group, independent of any filters; the cardinality.

    Related Pages:
    --------------
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
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param add:
    :param remove:
    :param initial:
    """

  def reduceCount(self):
    """
    Description:
    -----------
    A convenience method for setting the reduce functions to count records; returns this group.

    :return: returns this group
    """
    return self.fnc("reduceCount()")

  def reduceSum(self, value):
    """
    Description:
    -----------
    A convenience method for setting the reduce functions to sum records using the specified value accessor function;

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param value:

    :return: returns this group
    """
    return self.fnc("reduceSum(function(d) {console.log(d) ; return d['%s'] ;})" % value)

  def order(self, orderValue):
    """
    Description:
    -----------

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    :param orderValue:
    """

  def orderNatural(self):
    """
    A convenience method for using natural order for reduce values. Returns this grouping

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    groupObj = Group("%s.orderNatural()" % self.toStr())
    return groupObj

  def top(self, k=None):
    """
    Description:
    -----------
    Returns a new array containing the top k groups, according to the group order of the associated reduce value.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    :param k:
    """
    if k is None:
      return JsObjects.JsArray.JsArray("%s.top()" % self.varId)

    return JsObjects.JsArray.JsArray("%s.top(%s)" % (self.varId, k))

  def all(self):
    """
    Description:
    -----------
    Returns the array of all groups, in ascending natural order by key. Like top, the returned objects contain key and value attributes.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsArray.JsArray("%s.all()" % self.varId)

  def dispose(self):
    """
    Description:
    -----------
    Removes this group from its dimension.
    This group will no longer update when new filters are applied to the crossfilter, and it may be garbage collected if there are no other references to it remaining.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsObject.JsObject("%s.dispose()" % self.toStr())


class GroupAll(object):
  def __init__(self, selector):
    self._selector = selector
    self._js = []

  def reduce(self, add, remove, initial):
    """
    Description:
    -----------

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param add:
    :param remove:
    :param initial:
    """
    return JsObjects.JsNumber.JsNumber("%s.all()" % self.toStr())

  def value(self):
    """
    Description:
    -----------
    Equivalent to group.all()[0].value.

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference
    """
    return JsObjects.JsNumber.JsNumber("%s.all()" % self.toStr())

  def toStr(self):
    """
    Description:
    -----------
    Javascript representation

    Related Pages:
    --------------
    https://github.com/crossfilter/crossfilter/wiki/API-Reference

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._selector

    strData = "%(jqId)s.%(items)s" % {'jqId': self._selector, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return JsObjects.JsObject.JsObject.get(strData)
