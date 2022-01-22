"""
Wrapper to the Javascript Performance Module

The Performance interface provides access to performance-related information for the current page.
It's part of the High Resolution Time API, but is enhanced by the Performance Timeline API, the Navigation Timing API,
the User Timing API, and the Resource Timing API

Related Pages:

      https://developer.mozilla.org/fr/docs/Web/API/Performance

"""


from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.fncs import JsFncs
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsArray


class JsPerformance:
  def __init__(self, src=None):
    self.__src = src
    self.__marks = set([])
    self.__count = 0

  def add_profiling(self, js_funcs: Optional[Union[list, str]]):
    """
    Description:
    ------------
    Wrap the Javascript functions with function to asset on the execution time.

    Usage::

      page.js.performance.add_profiling(fncs['content'])

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Performance/now

    Attributes:
    ----------
    :param Optional[Union[list, str]] js_funcs: The Javascript functions.

    :return: The profile variable name
    """
    profile_var = "profile_%s" % self.__count
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.insert(0, "var %s_start = %s" % (profile_var, self.now))
    js_funcs.append("var %s = %s - %s_start" % (profile_var, self.now, profile_var))
    self.__count += 1
    return profile_var

  def clearMarks(self, name: Optional[str] = None):
    """
    Description:
    ------------
    The clearMarks() method removes the named mark from the browser's performance entry buffer.
    If the method is called with no arguments, all performance entries with an entry type of "mark" will be removed
    from the performance entry buffer.

    Usage::

      performance.clearMarks("a")

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Performance/clearMarks

    Attributes:
    ----------
    :param Optional[str] name: Optional. The mark name.

    :return: Void, the String for the Javascript side
    """
    if name is not None:
      if name not in self.__marks:
        raise ValueError("Mark %s not defined in the performances" % name)

      return JsFncs.JsFunction("performance.clearMarks(%s)" % name)

    return JsFncs.JsFunction("performance.clearMarks()")

  def clearMeasures(self, name: Optional[str] = None):
    """
    Description:
    ------------
    The clearMeasures() method removes the named measure from the browser's performance entry buffer.
    If the method is called with no arguments, all performance entries with an entry type of "measure" will be removed
    from the performance entry buffer.

    Usage::

      performance.clearMeasures("a");

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Performance/clearMeasures

    Attributes:
    ----------
    :param Optional[str] name: Optional. The name of the mark to be cleared.

    :return: Void, the String for the Javascript side
    """
    if name is not None:
      self.__marks.remove(name)
      return JsFncs.JsFunction("performance.clearMeasures(%s)" % name)

    return JsFncs.JsFunction("performance.clearMeasures()")

  def clearResourceTimings(self):
    """
    Description:
    ------------
    The clearResourceTimings() method removes all performance entries with an entryType of "resource" from
    the browser's performance data buffer and sets the size of the performance data buffer to zero.
    To set the size of the browser's performance data buffer, use the Performance.setResourceTimingBufferSize() method.

    Usage::

      performance.clearResourceTimings()

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Performance/clearResourceTimings

    :return: This method has no return value, but only the String for the Javascript side
    """
    return JsFncs.JsFunction("performance.clearResourceTimings()")

  def getEntries(self):
    """
    Description:
    ------------
    The getEntries() method returns a list of all PerformanceEntry objects for the page.
    The list's members (entries) can be created by making performance marks or
    measures (for example by calling the mark() method) at explicit points in time.
    If you are only interested in performance entries of certain types or that have certain names,
    see getEntriesByType() and getEntriesByName().

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Performance/getEntries

    :return: An array of PerformanceEntry objects
    """
    return JsArray.JsArray("window.performance.getEntries()", isPyData=False)

  def getEntriesByName(self, name: Union[primitives.JsDataModel, str], type: Optional[str] = None):
    """
    Description:
    ------------
    The getEntriesByName() method returns a list of PerformanceEntry objects for the given name and type.
    The list's members (entries) can be created by making performance marks or
    measures (for example by calling the mark() method) at explicit points in time.

    Usage::

      performance.getEntriesByName("Begin", "mark")

    Related Pages:

      https//developer.mozilla.org/en-US/docs/Web/API/Performance/getEntriesByName

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, str] name: The name of the entry to retrieve.
    :param Optional[str] type: Optional. The type of entry to retrieve such as "mark".

    :return: A list of PerformanceEntry objects that have the specified name and type
    """
    if name not in self.__marks:
      raise ValueError("Mark %s not defined in the performances" % name)

    name = JsUtils.jsConvertData(name, None)
    if type is not None:
      return JsArray.JsArray("window.performance.getEntriesByName(%s, %s)" % (name, type), isPyData=False)

    return JsArray.JsArray("window.performance.getEntriesByName(%s)" % name, isPyData=False)

  def getEntriesByType(self, type: str):
    """
    Description:
    ------------
    The getEntriesByType() method returns a list of PerformanceEntry objects for a given type.
    The list's members (entries) can be created by making performance marks or
    measures (for example by calling the mark() method) at explicit points in time.

    Usage::

      performance.getEntriesByType("mark")

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Performance/getEntriesByType

    Attributes:
    ----------
    :param str type: The type of entry to retrieve such as "mark".

    :return: A list of PerformanceEntry objects that have the specified type.
    """
    return JsArray.JsArray("window.performance.getEntriesByType('%s')" % type, isPyData=False)

  def mark(self, name: Union[primitives.JsDataModel, str]):
    """
    Description:
    ------------
    The mark() method creates a timestamp in the browser's performance entry buffer with the given name.
    The application defined timestamp can be retrieved by one of the Performance interface's getEntries*() methods
    (getEntries(), getEntriesByName() or getEntriesByType()).

    Usage::

      performance.mark("a")

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Performance/mark

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, str] name: A DOMString representing the name of the mark.

    :return: Void, The String for the Javascript side.
    """
    self.__marks.add(name)
    name = JsUtils.jsConvertData(name, None)
    return JsFncs.JsFunction("performance.mark(%s)" % name)

  def measure(self, name: Union[primitives.JsDataModel, str], startMark: Optional[str] = None,
              endMark: Optional[str] = None):
    """
    Description:
    ------------
    The measure() method creates a named timestamp in the browser's performance entry buffer between marks,
    the navigation start time, or the current time.

    When measuring between two marks, there is a start mark and end mark, respectively.
    The named timestamp is referred to as a measure.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Performance/measure

    Attributes:
    ----------
    :param str name: A DOMString representing the name of the measure.
    :param Optional[str] startMark: Optional. A DOMString representing the name of the measure's starting mark.
    :param Optional[str] endMark: Optional, A DOMString representing the name of the measure's ending mark.

    :return: Void, The String for the Javascript side
    """
    name = JsUtils.jsConvertData(name, None)
    if startMark is not None:
      if startMark not in self.__marks:
        raise ValueError("Mark %s not defined in the performances" % startMark)

      if endMark is not None:
        if startMark not in self.__marks:
          raise ValueError("Mark %s not defined in the performances" % startMark)

        return JsFncs.JsFunction("performance.measure(%s, %s, %s)" % (name, startMark, endMark))
      else:
        return JsFncs.JsFunction("performance.measure(%s, '%s')" % (name, startMark))

    return JsFncs.JsFunction("performance.measure(%s)" % name)

  @property
  def now(self):
    """
    Description:
    ------------
    The performance.now() method returns a DOMHighResTimeStamp, measured in milliseconds.

    Usage::

      var t0 = performance.now();

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Performance/now

    :return: A Javascript Number
    """
    return JsNumber.JsNumber("performance.now()", isPyData=False)

  def setResourceTimingBufferSize(self, maxSize: int):
    """
    Description:
    ------------
    The setResourceTimingBufferSize() method sets the browser's resource timing buffer size to the specified number
    of "resource" performance entry type objects.

    Usage::

      performance.setResourceTimingBufferSize(maxSize)

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Performance/setResourceTimingBufferSize

    Attributes:
    ----------
    :param int maxSize: The buffer meximum size.

    :return: Void, the String for the Javascript side.
    """
    return JsFncs.JsFunction("performance.setResourceTimingBufferSize(%s)" % maxSize)

  def toJSON(self):
    """
    Description:
    ------------
    The toJSON() method of the Performance interface is a standard serializer: it returns a JSON representation of
    the performance object's properties.

    Usage::

      performance.toJSON()

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Performance/toJSON

    :return: A JSON object that is the serialization of the Performance object.
    """
    return JsObject.JsObject("performance.toJSON()", isPyData=False)

