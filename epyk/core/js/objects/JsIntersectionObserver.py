from typing import Union
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsArray

from epyk.core.js import JsUtils


class IntersectionObserverEntry:

  def __init__(self, js_code: str = "entry"):
    self.varId = js_code

  @property
  def boundingClientRect(self):
    """
    The IntersectionObserverEntry interface's read-only boundingClientRect property returns a DOMRectReadOnly
    which in essence describes a rectangle describing the smallest rectangle that contains the entire target element.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/boundingClientRect
    """
    return JsUtils.jsWrap("%s.boundingClientRect" % self.varId)

  @property
  def intersectionRatio(self):
    """
    The IntersectionObserverEntry interface's read-only intersectionRatio property tells you how much of
    the target element is currently visible within the root's intersection ratio, as a value between 0.0 and 1.0.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRatio
    """
    return JsUtils.jsWrap("%s.intersectionRatio" % self.varId)

  @property
  def intersectionRect(self):
    """
    The IntersectionObserverEntry interface's read-only intersectionRect property is a DOMRectReadOnly object
    which describes the smallest rectangle that contains the entire portion of the target element which is currently
    visible within the intersection root.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRect
    """
    return JsUtils.jsWrap("%s.intersectionRect" % self.varId)

  @property
  def isIntersecting(self):
    """
    The IntersectionObserverEntry interface's read-only isIntersecting property is a Boolean value which is true
    if the target element intersects with the intersection observer's root.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/isIntersecting
    """
    return JsUtils.jsWrap("%s.isIntersecting" % self.varId)

  @property
  def rootBounds(self):
    """
    The IntersectionObserverEntry interface's read-only rootBounds property is a DOMRectReadOnly corresponding to the
    target's root intersection rectangle, offset by the IntersectionObserver.rootMargin if one is specified.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/rootBounds
    """
    return JsUtils.jsWrap("%s.rootBounds" % self.varId)

  @property
  def target(self):
    """
    The IntersectionObserverEntry interface's read-only target property indicates which targeted Element has changed
    its amount of intersection with the intersection root.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/target
    """
    return JsUtils.jsWrap("%s.target" % self.varId)

  @property
  def time(self):
    """
    The IntersectionObserverEntry interface's read-only time property is a DOMHighResTimeStamp that indicates the time
    at which the intersection change occurred relative to the time at which the document was created.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/time
    """
    return JsUtils.jsWrap("%s.time" % self.varId)

  def toStr(self):
    return JsUtils.jsWrap(self.varId)


class IntersectionObserver:

  def __init__(self, page: primitives.PageModel, js_code: str):
    self.page = page
    self.page.jsImports.add("intersection-observer")
    self._js = []
    self.js_code = js_code

  @property
  def varId(self):
    return self.js_code

  def entry(self, i: int = 0, entry_code: str = "entry") -> IntersectionObserverEntry:
    """

    :param i: Optional.
    :param entry_code: Optional. The entry variable name on JavaScript side.
    """
    return IntersectionObserverEntry(js_code="%s[%s]" % (entry_code, i))

  def new(self, callback, options: dict = None, observe_once: bool = False, profile: types.PROFILE_TYPE = None,
          entry_code: str = "entry"):
    """

    :param callback:
    :param observe_once:
    :param options:
    :param profile:
    :param entry_code:
    """
    if observe_once:
      callback.append(
        self.page.js.if_(self.page.js.objects.entry().isIntersecting,
        self.page.js.intersectionObserver(js_code=self.js_code).disconnect()))
    str_funcs = JsUtils.jsConvertFncs(callback, toStr=True, profile=profile)
    if options is not None:
      self._js.append("var %s = new IntersectionObserver(%s => {%s}, %s)" % (self.varId, entry_code, str_funcs, options))
    else:
      self._js.append("var %s = new IntersectionObserver(%s => {%s})" % (self.varId, entry_code, str_funcs))
    return self

  @property
  def POLL_INTERVAL(self):
    """
    """
    return JsObject.JsObject("%s.POLL_INTERVAL" % self.varId, is_py_data=False)

  @POLL_INTERVAL.setter
  def POLL_INTERVAL(self, mill_second: int):
    self._js.append("%s.POLL_INTERVAL = %s" % (self.varId, mill_second))

  @property
  def USE_MUTATION_OBSERVER(self):
    """
    """
    return JsObject.JsObject("%s.USE_MUTATION_OBSERVER" % self.varId, is_py_data=False)

  @USE_MUTATION_OBSERVER.setter
  def USE_MUTATION_OBSERVER(self, flag: bool):
    self._js.append("%s.USE_MUTATION_OBSERVER = %s" % (self.varId, flag))

  @property
  def root(self):
    """
    The IntersectionObserver interface's read-only root property identifies the Element whose bounds are treated as
    the bounding box of the viewport for the element which is the observer's target.
    If the root is null, then the bounds of the actual document viewport are used.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/root
    """
    return JsObject.JsObject("%s.root" % self.varId, is_py_data=False)

  @property
  def rootMargin(self):
    """
    The IntersectionObserver interface's read-only rootMargin property is a string with syntax similar to that of
    the CSS margin property.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/rootMargin
    """
    return JsString.JsString("%s.rootMargin" % self.varId, is_py_data=False)

  @property
  def thresholds(self):
    """
    The IntersectionObserver interface's read-only thresholds property returns the list of intersection thresholds that
    was specified when the observer was instantiated with IntersectionObserver().
    If only one threshold ratio was provided when instantiating the object, this will be an array containing
    that single value.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/thresholds
    """
    return JsArray.JsArray("%s.thresholds" % self.varId, is_py_data=False)

  def observe(self, target_element: Union[primitives.HtmlModel, str]):
    """
    The IntersectionObserver method observe() adds an element to the set of target elements being watched by the
    IntersectionObserver.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/observe

    :param target_element: An element whose visibility within the root is to be monitored.
                          This element must be a descendant of the root element (or contained wtihin the current
                          document, if the root is the document's viewport).
    """
    if hasattr(target_element, "dom"):
      js_code = target_element.dom.varId
    else:
      js_code = JsUtils.jsConvertData(target_element, None)
    self._js.append("%s.observe(%s)" % (self.varId, js_code))
    return self

  def disconnect(self):
    """
    The IntersectionObserver method disconnect() stops watching all of its target elements for visibility changes.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/disconnect
    """
    self._js.append("%s.disconnect()" % self.varId)
    return self

  def takeRecords(self, js_code: str = None):
    """
    The IntersectionObserver method takeRecords() returns an array of IntersectionObserverEntry objects, one for each
    targeted element which has experienced an intersection change since the last time the intersections were checked,
    either explicitly through a call to this method or implicitly by an automatic call to the observer's callback.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/takeRecords
      https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/takeRecords

    :param js_code: Optional. The entries variable name.

    :return: An array of IntersectionObserverEntry objects, one for each target element whose intersection with the
       root has changed since the last time the intersections were checked.
    """
    return JsArray.JsArray("%s.takeRecords()" % self.varId, js_code=js_code)

  def eachRecord(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, entry_code: str = "entry"):
    """

    :param js_funcs: A Javascript Python function.
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console.
    :param entry_code: Optional. The entry variable name on JavaScript side.
    """
    str_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsUtils.jsWrap("%s.takeRecords().forEach(function(%s){%s})" % (self.varId, entry_code, str_funcs))

  def unobserve(self, target_element: Union[primitives.HtmlModel, str]):
    """
    The IntersectionObserver method unobserve() instructs the IntersectionObserver to stop observing the specified
    target element.

    Run the unobserve a target Element algorithm, providing this and target.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/unobserve
      https://w3c.github.io/IntersectionObserver/#dom-intersectionobserver-intersectionobserver

    :param target_element: The Element to cease observing.
        If the specified element isn't being observed, this method does nothing and no exception is thrown.
    """
    if hasattr(target_element, "dom"):
      js_code = target_element.dom.varId
    else:
      js_code = JsUtils.jsConvertData(target_element, None)
    self._js.append("%s.unobserve(%s)" % (self.varId, js_code))
    return self

  def toStr(self):
    str_content = "; ".join(self._js)
    self._js = []
    return str_content
