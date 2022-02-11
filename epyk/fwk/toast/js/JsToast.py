
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class JsDebounce:

  @staticmethod
  def set(js_funcs, delay, js_code: str, profile=None):
    """
    Description:
    ------------
    Creates a throttled function that only invokes fn at most once per every interval milliseconds.
    You can use this throttle short time repeatedly invoking functions. (e.g MouseMove, Resize ...)
    if you need reuse throttled method. you must remove slugs (e.g. flag variable) related with throttling.

    Related Pages:

      https://nhn.github.io/tui.code-snippet/latest/tricks#debounce

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param delay: Integer. The delay to run the function.
    :param str js_code: the variable reference.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    delay = JsUtils.jsConvertData(delay, None)
    return JsUtils.jsWrap("window['%s'] = tui.util.debounce(function(){%s}, %s)" % (
      js_code, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), delay))

  @staticmethod
  def run(js_code: str):
    """
    Description:
    ------------
    Run the function.

    Attributes:
    ----------
    :param str js_code: the variable reference.
    """
    return JsUtils.jsWrap("%s()" % js_code)


class JsThrottle:

  @staticmethod
  def set(js_funcs, interval: int, js_code: str, profile=None):
    """
    Description:
    ------------
    Creates a throttled function that only invokes fn at most once per every interval milliseconds.
    You can use this throttle short time repeatedly invoking functions. (e.g MouseMove, Resize ...)
    if you need reuse throttled method. you must remove slugs (e.g. flag variable) related with throttling.

    Related Pages:

      https://nhn.github.io/tui.code-snippet/latest/tricks#throttle

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param int interval: The interval between two function trigger.
    :param str js_code: the variable reference.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    interval = JsUtils.jsConvertData(interval, None)
    return JsUtils.jsWrap("window['%s'] = tui.util.throttle(function(){%s}, %s)" % (
      js_code, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), interval))

  @staticmethod
  def run(js_code: str):
    """
    Description:
    ------------
    Run the function.

    Attributes:
    ----------
    :param str js_code: The variable reference.
    """
    return JsUtils.jsWrap("%s()" % js_code)

  @staticmethod
  def reset(js_code: str):
    """
    Attributes:
    ----------
    :param str js_code: The variable reference.
    """
    return JsUtils.jsWrap("%s.reset()" % js_code)


class Js:

  def __init__(self, page=None, component=None):
    # The underlying source object is not supposed to be touched in the underlying classes
    self.component, self.page = component, page

  def util(self):
    return JsObjects.JsObjects.get("tui.util")

  def zip(self, *args):
    """
    Description:
    ------------
    Zip together multiple lists into a single array.

    Related Pages:

      https://nhn.github.io/tui.code-snippet/latest/array#zip
    """
    return JsObjects.JsArray.JsArray.get("tui.util.zip(...%s)" % list(args))

  def range(self, start, end, step=1):
    """
    Description:
    ------------
    Generate an integer Array containing an arithmetic progression.

    Related Pages:

      https://nhn.github.io/tui.code-snippet/latest/array#range

    Attributes:
    ----------
    :param start: Number. start index.
    :param end: Number. stop index.
    :param step: Number. Optional. next visit index = current index + step.
    """
    return JsObjects.JsArray.JsArray.get("tui.util.range(%s, %s, %s)" % (start, end, step))

  def inArray(self, search_element, array, start_index=0):
    """
    Description:
    ------------
    Returns the first index at which a given element can be found in the array
    from start index(default 0), or -1 if it is not present.
    It compares searchElement to elements of the Array using strict equality
    (the same method used by the ===, or triple-equals, operator).

    Related Pages:

      https://nhn.github.io/tui.code-snippet/latest/array#inArray

    Attributes:
    ----------
    :param search_element: String. Element to locate in the array.
    :param array: Array. Array that will be traversed.
    :param start_index: Number. Optional. Start index in array for searching (default 0)
    """
    search_element = JsUtils.jsConvertData(search_element, None)
    array = JsUtils.jsConvertData(array, None)
    start_index = JsUtils.jsConvertData(start_index, None)
    return JsObjects.JsArray.JsArray.get("tui.util.inArray(%s, %s, %s)" % (search_element, array, start_index))

  def extend(self, target, objects):
    """
    Description:
    ------------
    Extend the target object from other objects.

    Related Pages:

      https://nhn.github.io/tui.code-snippet/latest/object#extend

    Attributes:
    ----------
    :param target: Object. Object that will be extended.
    :param objects: Object. Objects as sources.
    """
    target = JsUtils.jsConvertData(target, None)
    objects = JsUtils.jsConvertData(objects, None)
    return JsObjects.JsArray.JsArray.get("tui.util.extend(%s, %s)" % (target, objects))

  def pick(self, obj, paths):
    """
    Description:
    ------------
    Retrieve a nested item from the given object/array.

    Related Pages:

      https://nhn.github.io/tui.code-snippet/latest/object#pick

    Attributes:
    ----------
    :param obj: Object | Array. Object for retrieving.
    :param paths: String | Number. Paths of property.
    """
    obj = JsUtils.jsConvertData(obj, None)
    paths = JsUtils.jsConvertData(paths, None)
    return JsObjects.JsArray.JsArray.get("tui.util.pick(%s, %s)" % (obj, paths))

  @property
  def debounce(self):
    """
    Description:
    ------------
    Creates a debounced function that delays invoking fn until after delay milliseconds has elapsed
    since the last time the debouced function was invoked.

    Related Pages:

      https://nhn.github.io/tui.code-snippet/latest/tricks#debounce
    """
    return JsDebounce

  @property
  def throttle(self):
    """
    Description:
    ------------
    Creates a throttled function that only invokes fn at most once per every interval milliseconds.
    You can use this throttle short time repeatedly invoking functions. (e.g MouseMove, Resize ...)
    if you need reuse throttled method. you must remove slugs (e.g. flag variable) related with throttling.

    Related Pages:

      https://nhn.github.io/tui.code-snippet/latest/tricks#throttle

    Usage::

      page.body.onReady([
        page.web.tui.js.throttle.set([page.js.console.log("test")], 300, "testThrottle"),
        page.web.tui.js.throttle.run("testThrottle"),
        page.web.tui.js.throttle.run("testThrottle"),
        page.web.tui.js.throttle.run("testThrottle"),
        page.web.tui.js.throttle.run("testThrottle"),
        page.web.tui.js.throttle.run("testThrottle"),
        page.web.tui.js.throttle.run("testThrottle"),
        page.web.tui.js.throttle.run("testThrottle"),
        page.web.tui.js.throttle.run("testThrottle"),
        page.web.tui.js.throttle.reset("testThrottle"),
      ])
    """
    return JsThrottle
