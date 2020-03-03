
from epyk.core.js.objects import JsNodeDomRect

from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsArray

from epyk.core.js.fncs import JsFncs

from epyk.core.js import JsUtils


class IntersectionObserverEntry(object):

  @property
  def boundingClientRect(self):
    """
    Description:
    ------------
    The IntersectionObserverEntry interface's read-only boundingClientRect property returns a DOMRectReadOnly which in essence describes a rectangle describing the smallest rectangle that contains the entire target element.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/boundingClientRect
    """

  @property
  def intersectionRatio(self):
    """
    Description:
    ------------
    The IntersectionObserverEntry interface's read-only intersectionRatio property tells you how much of the target element is currently visible within the root's intersection ratio, as a value between 0.0 and 1.0.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRatio
    """

  @property
  def intersectionRect(self):
    """
    Description:
    ------------
    The IntersectionObserverEntry interface's read-only intersectionRect property is a DOMRectReadOnly object which describes the smallest rectangle that contains the entire portion of the target element which is currently visible within the intersection root.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRect
    """

  @property
  def isIntersecting(self):
    """
    Description:
    ------------
    The IntersectionObserverEntry interface's read-only isIntersecting property is a Boolean value which is true if the target element intersects with the intersection observer's root.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/isIntersecting
    """

  @property
  def rootBounds(self):
    """
    Description:
    ------------
    The IntersectionObserverEntry interface's read-only rootBounds property is a DOMRectReadOnly corresponding to the target's root intersection rectangle, offset by the IntersectionObserver.rootMargin if one is specified.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/rootBounds
    """

  @property
  def target(self):
    """
    Description:
    ------------
    The IntersectionObserverEntry interface's read-only target property indicates which targeted Element has changed its amount of intersection with the intersection root.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/target
    """

  @property
  def time(self):
    """
    Description:
    ------------
    The IntersectionObserverEntry interface's read-only time property is a DOMHighResTimeStamp that indicates the time at which the intersection change occurred relative to the time at which the document was created.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/time
    """
    return JsNumber.JsNumber("%s.time")


class IntersectionObserver(object):

  def __init__(self):
    pass

  @property
  def root(self):
    """
    Description:
    ------------
    The IntersectionObserver interface's read-only root property identifies the Element whose bounds are treated as the bounding box of the viewport for the element which is the observer's target.
    If the root is null, then the bounds of the actual document viewport are used.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/root
    """
    return JsObject.JsObject("%s.root", isPyData=False)

  @property
  def rootMargin(self):
    """
    Description:
    ------------
    The IntersectionObserver interface's read-only rootMargin property is a string with syntax similar to that of the CSS margin property.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/rootMargin
    """
    return JsString.JsString("%s.rootMargin", isPyData=False)



  @property
  def thresholds(self):
    """
    Description:
    ------------
    The IntersectionObserver interface's read-only thresholds property returns the list of intersection thresholds that was specified when the observer was instantiated with IntersectionObserver().
    If only one threshold ratio was provided when instanitating the object, this will be an array containing that single value.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/thresholds
    """
    return JsArray.JsArray("%s.thresholds", isPyData=False)

  def observe(self, targetElement):
    """
    Description:
    ------------
    The IntersectionObserver method observe() adds an element to the set of target elements being watched by the IntersectionObserver.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/observe

    Attributes:
    ----------
    :param targetElement: An element whose visibility within the root is to be monitored.
                          This element must be a descendant of the root element (or contained wtihin the current document, if the root is the document's viewport).
    :return:
    """
    return

  def disconnect(self):
    """
    Description:
    ------------
    The IntersectionObserver method disconnect() stops watching all of its target elements for visibility changes.

    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/disconnect
    """
    return JsFncs.JsFunction("%s.disconnect()")

  def takeRecords(self):
    """
    Description:
    ------------
    The IntersectionObserver method takeRecords() returns an array of IntersectionObserverEntry objects, one for each targeted element which has experienced an intersection change since the last time the intersections were checked, either explicitly through a call to this method or implicitly by an automatic call to the observer's callback.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/takeRecords

    :return: An array of IntersectionObserverEntry objects, one for each target element whose intersection with the root has changed since the last time the intersections were checked.
    """
    return JsFncs.JsFunction("%s.takeRecords()")

  def unobserve(self, targetElement):
    """
    Description:
    ------------
    The IntersectionObserver method unobserve() instructs the IntersectionObserver to stop observing the specified target element.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/unobserve

    Attributes:
    ----------
    :param targetElement: The Element to cease observing. If the specified element isn't being observed, this method does nothing and no exception is thrown.
    """
    return JsFncs.JsFunction("%s.unobserve()")
