
from epyk.core.js.fncs import JsFncs
from epyk.core.css import Colors

from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsArray

from epyk.core.js.objects import JsNodeDomRect

from epyk.core.js import JsUtils


class JsDomEvents(object):
  class __internal(object):
    htmlCode = None

  def __init__(self, src=None):
    self._src = src if src is not None else self.__internal()
    self._js = []

  def stopPropagation(self):
    """
    Description:
    ------------
    The stopPropagation() method prevents propagation of the same event from being called.

    Related Pages:

      https://www.w3schools.com/jsref/event_stoppropagation.asp

    :return: The Python Dom object
    """
    self._js.append('stopPropagation()')
    return self

  def blur(self, jsFncs):
    """
    Description:
    ------------
    FocusEvent

    The event occurs when an element loses focus

    Related Pages:

      https://www.w3schools.com/jsref/event_onblur.asp

    Attributes:
    ----------
    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("blur", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def click(self, jsFncs):
    """
    Description:
    ------------
    The event occurs when the user clicks on an element

    Example
    select.label.dom.events.click(rptObj.js.console.log("test"))

    Related Pages:

      https://www.w3schools.com/jsref/event_onclick.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("click", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def change(self, jsFncs):
    """
    Description:
    ------------
    The event occurs when the content of a form element, the selection, or the checked state have changed (for <input>, <select>, and <textarea>)

    Example
    select.dom.events.change(rptObj.js.window.alert("test"))

    Related Pages:

      https://www.w3schools.com/jsref/event_onchange.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("change", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def dblclick(self, jsFncs):
    """
    Description:
    ------------
    The event occurs when the user double-clicks on an element

    Related Pages:

      https://www.w3schools.com/jsref/event_ondblclick.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("dblclick", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def focus(self, jsFncs):
    """
    Description:
    ------------
    The event occurs when an element gets focus

    Related Pages:

      https://www.w3schools.com/jsref/event_onfocusin.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("focus", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def focusin(self, jsFncs):
    """
    Description:
    ------------
    The event occurs when an element is about to get focus

    Related Pages:

      https://www.w3schools.com/jsref/event_onfocusin.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("focusin", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def focusout(self, jsFncs):
    """
    The event occurs when an element is about to lose focus

    Related Pages:

      https://www.w3schools.com/jsref/event_onfocusout.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("focusin", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def keydown(self, jsFncs):
    """
    The event occurs when the user is pressing a key

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeydown.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("keydown", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def keypress(self, jsFncs):
    """
    The event occurs when the user presses a key

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeypress.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("keypress", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def keyup(self, jsFncs):
    """
    The event occurs when the user releases a key

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeyup.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("keyup", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mousedown(self, jsFncs):
    """
    The event occurs when the user presses a mouse button over an element

    Related Pages:

      https://www.w3schools.com/jsref/event_onmousedown.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mousedown", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mouseenter(self, jsFncs):
    """
    The event occurs when the pointer is moved onto an element

    Related Pages:

      https://www.w3schools.com/jsref/event_onmouseenter.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mousedown", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mouseleave(self, jsFncs):
    """
    The event occurs when the pointer is moved out of an element

    Example
    select.label.dom.events.mouseleave(rptObj.js.console.log("test"))

    Related Pages:

      https://www.w3schools.com/jsref/event_onmouseleave.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseleave", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mouseover(self, jsFncs):
    """
    The event occurs when the pointer is moved onto an element, or onto one of its children

    Related Pages:

      https://www.w3schools.com/jsref/event_onmouseover.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseover", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mouseup(self, jsFncs):
    """
    The event occurs when a user releases a mouse button over an element

    Related Pages:

      https://www.w3schools.com/jsref/event_onmouseup.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseover", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mouseout(self, jsFncs):
    """
    The event occurs when a user releases a mouse button over an element

    Related Pages:

      https://www.w3schools.com/jsref/event_onmouseout.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseout", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def trigger(self, event, withFocus=True):
    """
    Trigger a javascript event

    Related Pages:

      https://www.w3schools.com/jsref/met_html_focus.asp
    https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Creating_and_triggering_events

    :param event: The event name
    :param withFocus: Optional, a boolean to define if the focus needs to be set to this component

    :return: The Javascript string of this function
    """
    item = "document.getElementById('%(htmlCode)s')" % {'htmlCode': self._src.htmlCode}
    if withFocus:
      return JsFncs.JsFunction('(function(){var clickEvent = new Event("%(event)s"); %(elem)s.focus(); %(elem)s.dispatchEvent(clickEvent)})()' % {"event": event, "elem": item})

    return JsFncs.JsFunction('(function(){var clickEvent = new Event("%(event)s"); %(elem)s.dispatchEvent(clickEvent)})()' % {"event": event, "elem": item})

  def toStr(self):
    if self._src.htmlCode is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._src.htmlCode

    strData = "document.getElementById('%(htmlCode)s').%(items)s" % {'htmlCode': self._src.htmlCode, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return strData


class JsDomsTransforms(object):

  def __init__(self, src, selector):
    self._src, self.selector = src, selector

  def initial(self):
    """
    Sets this property to its default value

    """
    return "%s.initial" % self.selector

  def inherit(self):
    """
    Inherits this property from its parent element.

    """
    return "%s.initial" % self.selector

  def matrix(self, scaleX, skewY, skewX, scaleY, translateX, translateY):
    """
    Description:
    ------------
    Defines a 2D transformation, using a matrix of six values

    Usage::

      Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/matrix

    Attributes:
    ----------
    :param scaleX: Number.
    :param skewY: Number.
    :param skewX: Number.
    :param scaleY: Number.
    :param translateX: Number.
    :param translateY: Number.
    """
    return "%s.style.transform = 'matrix(%s, %s, %s, %s, %s, %s)'" % (self.selector, scaleX, skewY, skewX, scaleY, translateX, translateY)

  def translateX(self, x, unit='px'):
    """
    Description:
    ------------
    The translateX() CSS function repositions an element horizontally on the 2D plane. Its result is a <transform-function> data type.

    Usage::

      Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/translateX
    https://www.w3schools.com/jsref/prop_style_transform.asp

    Attributes:
    ----------
    :param x: Number.
    :param unit: String. The unit used for the transformation (px, cm, rem...)
    """
    return "%s.style.transform = 'translateX(%s%s)'" % (self.selector, x, unit)

  def translateY(self, y, unit='px'):
    """
    Description:
    ------------
    The translateY() CSS function repositions an element vertically on the 2D plane. Its result is a <transform-function> data type.

    Related Pages:

      https://www.w3schools.com/jsref/prop_style_transform.asp

    Attributes:
    ----------
    :param y:
    :param unit: String. The unit used for the transformation (px, cm, rem...)
    """
    return "%s.style.transform = 'translateY(%s%s)'" % (self.selector, y, unit)

  def translate(self, x, y, unit='px'):
    """
    Description:
    ------------
    The translate() CSS function repositions an element in the horizontal and/or vertical directions. Its result is a <transform-function> data type.

    Related Pages:

      https://www.w3schools.com/jsref/prop_style_transform.asp

    Attributes:
    ----------
    :param x:
    :param y:
    :param unit: String. The unit used for the transformation (px, cm, rem...)
    """
    return "%s.style.transform = 'translate(%s%s, %s%s)'" % (self.selector, x, unit, y, unit)

  def perspective(self, d, unit='px'):
    """
    Description:
    ------------
    The perspective() CSS function defines a transformation that sets the distance between the user and the z=0 plane,
    the perspective from which the viewer would be if the 2-dimensional interface were 3-dimensional.
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/perspective

    Attributes:
    ----------
    :param d: Is a <length> representing the distance from the user to the z=0 plane.
              If it is 0 or a negative value, no perspective transform is applied.
    :param unit: String. The unit used for the transformation (px, cm, rem...)
    """
    return "%s.style.transform = 'perspective(%s%s)'" % (self.selector, d, unit)

  def scale(self, x, y):
    """
    Description:
    ------------
    The scale() CSS function defines a transformation that resizes an element on the 2D plane.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/scale

    Attributes:
    ----------
    :param x: Number. A <number> representing the abscissa of the scaling vector.
    :param y: Number. A <number> representing the ordinate of the scaling vector.
              If not defined, its default value is sx, resulting in a uniform scaling that preserves the element's aspect ratio.
    """
    return "%s.style.transform = 'scale(%s, %s)'" % (self.selector, x, y)

  def scaleX(self, x):
    """
    Description:
    ------------
    The scaleX() CSS function defines a transformation that resizes an element along the x-axis (horizontally). Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/scaleX

    Attributes:
    ----------
    :param x: Number. Is a <number> representing the scaling factor to apply on the abscissa of each point of the element.
    """
    return "%s.style.transform = 'scaleX(%s)'" % (self.selector, x)

  def scaleY(self, y):
    """
    Description:
    ------------
    The scaleY() CSS function defines a transformation that resizes an element along the y-axis (vertically). Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/scaleY

    Attributes:
    ----------
    :param y: Number. Is a <number> representing the scaling factor to apply on the ordinate of each point of the element.
    """
    return "%s.style.transform = 'scaleY(%s)'" % (self.selector, y)

  def skew(self, angleX, angleY=0, unit='deg'):
    """
    Description:
    ------------
    The skew() CSS function defines a transformation that skews an element on the 2D plane. Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/skew

    Attributes:
    ----------
    :param angleX: Number. Is an <angle> representing the angle to use to distort the element along the abscissa.
    :param angleY: Number. Is an <angle> representing the angle to use to distort the element along the ordinate.
                           If not defined, its default value is 0, resulting in a purely horizontal skewing.
    :param unit: String. The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'skew(%s%s, %s%s)'" % (self.selector, angleX, unit, angleY, unit)

  def skewX(self, angle, unit='deg'):
    """
    Description:
    ------------
    The skewX() CSS function defines a transformation that skews an element in the horizontal direction on the 2D plane.
    Its result is a <transform-function> data type.

    Usage::

      i.label.dom.transform.skewX(20),

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/skewX

    Attributes:
    ----------
    :param angle: Number. Is an <angle> representing the angle to use to distort the element along the abscissa.
    :param unit: String. The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'skewX(%s%s)'" % (self.selector, angle, unit)

  def skewY(self, angle, unit='deg'):
    """
    Description:
    ------------
    The skewY() CSS function defines a transformation that skews an element in the vertical direction on the 2D plane.
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/skewY

    Attributes:
    ----------
    :param angle: Number. Is an <angle> representing the angle to use to distort the element along the ordinate.
    :param unit: String. The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'skewY(%s%s)'" % (self.selector, angle, unit)

  def rotate(self, r, unit='deg'):
    """
    Description:
    ------------
    The rotate() CSS function defines a transformation that rotates an element around a fixed point on the 2D plane, without deforming it.
    Its result is a <transform-function> data type.

    Usage::

      i.label.dom.transform.rotate(90)

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate

    Attributes:
    ----------
    :param r: Is an <angle> representing the angle of the rotation. A positive angle denotes a clockwise rotation, a negative angle a counter-clockwise one.
    :param unit: String. The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'rotate(%s%s)'" % (self.selector, r, unit)

  def rotate3d(self, x, y, z, a, unit='deg'):
    """
    Description:
    ------------
    The rotate3d() CSS function defines a transformation that rotates an element around a fixed axis in 3D space, without deforming it.
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d

    Attributes:
    ----------
    :param x: Is a <number> describing the x-coordinate of the vector denoting the axis of rotation which could between 0 and 1.
    :param y: Is a <number> describing the y-coordinate of the vector denoting the axis of rotation which could between 0 and 1.
    :param z: Is a <number> describing the z-coordinate of the vector denoting the axis of rotation which could between 0 and 1.
    :param a: Is an <angle> representing the angle of the rotation. A positive angle denotes a clockwise rotation, a negative angle a counter-clockwise one.
    :param unit: String. The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'rotate3d(%s, %s, %s, %s%s)'" % (self.selector, x, y, z, a, unit)

  def rotateX(self, r, unit='deg'):
    """
    Description:
    ------------
    The rotateX() CSS function defines a transformation that rotates an element around the abscissa (horizontal axis) without deforming it.
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotateX

    Attributes:
    ----------
    :param r: Is an <angle> representing the angle of the rotation. A positive angle denotes a clockwise rotation, a negative angle a counter-clockwise one.
    :param unit: String. The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'rotateX(%s%s)'" % (self.selector, r, unit)

  def rotateY(self, r, unit='deg'):
    """
    Description:
    ------------
    The rotateY() CSS function defines a transformation that rotates an element around the ordinate (vertical axis) without deforming it.
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotateY

    Attributes:
    ----------
    :param r: Is an <angle> representing the angle of the rotation. A positive angle denotes a clockwise rotation, a negative angle a counter-clockwise one.
    :param unit: String. The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'rotateY(%s%s)'" % (self.selector, r, unit)

  def rotateZ(self, r, unit='deg'):
    """
    Description:
    ------------
    The rotateZ() CSS function defines a transformation that rotates an element around the z-axis without deforming it. Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotateZ

    Attributes:
    ----------
    :param r: Is an <angle> representing the angle of the rotation. A positive angle denotes a clockwise rotation, a negative angle a counter-clockwise one.
    :param unit: String. The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'rotateZ(%s%s)'" % (self.selector, r, unit)


class JsDoms(JsObject.JsObject):
  _id = None
  display_value = 'block'

  @classmethod
  def new(cls, tagName=None, varName=None, isPyData=True, setVar=True, report=None):
    """
    Description:
    ------------
    Create a new dom object to be added to the HTML page

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_date.asp

    Attributes:
    ----------
    :param tagName: The tag name to be created
    :param varName: Optional,
    :param isPyData: Optional,

    :return: The Python Javascript Date primitive
    """
    return cls(data="document.createElement('%s')" % tagName, varName=varName, setVar=setVar, isPyData=isPyData, report=report)

  def querySelector(self, tag):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param tag:

    :return:
    """
    return JsDoms("%s.querySelector('%s')" % (self.toStr(), tag))

  def querySelectorAll(self, tag, varName=None):
    """
    Description:
    ------------
    The querySelectorAll() method returns all elements in the document that matches a specified CSS selector(s), as a static NodeList object.

    Related Pages:

      https://www.w3schools.com/jsref/met_document_queryselectorall.asp

    Attributes:
    ----------
    :param tag: String. The tag name
    :param varName: String. The variable name on the javascript side

    :return: A javascript Array object
    """
    if varName is None:
      return JsArray.JsArray("%s.querySelectorAll('%s')" % (self.toStr(), tag), isPyData=False)

    return JsArray.JsArray("%s.querySelectorAll('%s')" % (self.toStr(), tag), varName=varName, setVar=True, isPyData=False)

  def empty(self):
    """
    Description:
    ------------
    Shortcup function to emtpy an HTML compnent.
    This will only reuse the innerHTML property
    """
    return JsObject.JsObject('%s.innerHTML = ""' % (self.varId))

  @property
  def transform(self):
    """
    Description:
    ------------
    The transform property applies a 2D or 3D transformation to an element.
    This property allows you to rotate, scale, move, skew, etc., elements.

    Related Pages:

      https://www.w3schools.com/jsref/prop_style_transform.asp
    https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function
    """
    return JsDomsTransforms(self._report, self.varId)

  @property
  def jquery(self):
    """
    Description:
    ------------
    Link to the Jquery package

    THe id attribute must be defined
    """
    from epyk.core.js.packages import JsQuery

    if self._id is None:
      raise Exception("Id must be defined to attach Jquery features to this object")

    if getattr(self, '_jq', None) is None:
      self._jq = JsQuery.JQuery(self._report, selector="jQuery('#%s')" % self._id, setVar=False)
    return self._jq

  def addEventListener(self, event, jsFncs):
    """
    Description:
    ------------
    The addEventListener() method attaches an event handler to the specified element.

    Related Pages:

      https://www.w3schools.com/jsref/met_element_addeventlistener.asp

    Attributes:
    ----------
    :param event:
    :param jsFncs:
    """
    self._js.append('addEventListener("%s", function(){%s})' % (event, ";".join(JsUtils.jsConvertFncs(jsFncs))))
    return self

  def dispatchEvent(self, event):
    """
    Description:
    ------------
    Dispatches an Event at the specified EventTarget, (synchronously) invoking the affected EventListeners in the appropriate order.
    The normal event processing rules (including the capturing and optional bubbling phase) also apply to events dispatched manually with dispatchEvent().

    Attributes:
    ----------
    :param event: event is the Event object to be dispatched.
    """
    event = JsUtils.jsConvertData(event, None)
    self._js.append('dispatchEvent(%s)' % event)
    return self

  def addOnReady(self, jsFncs):
    """
    Description:
    ------------
    The ready event occurs when the DOM (document object model) has been loaded.

    Related Pages:

      https://www.w3schools.com/jquery/event_ready.asp

    Attributes:
    ----------
    :param jsFncs: The Javascript functions to be added to this section
    """
    self._report._props.setdefault('js', {}).setdefault('onCompReady', {})[self.varId] = ";".join(JsUtils.jsConvertFncs(jsFncs))

  def innerText(self, jsString=None, append=False, valType=None):
    """
    Description:
    ------------
    The innerText property sets or returns the text content of the specified node, and all its descendants.

    Usage::

      select.label.dom.innerText("test Change")

    Related Pages:

      https://www.w3schools.com/jsref/prop_node_innertext.asp

    Attributes:
    ----------
    :param jsString: Optional, The Javascript String to be added
    :param append: Boolean. Mention if the component should replace or append the data
    :param valType: Type: The type of data expected in the component

    :return: The JsObj to allow the chaining
    """
    if jsString is None:
      return JsString.JsString("%s.innerText" % self.varId, isPyData=False)

    if append:
      if valType == int:
        self._js.append("%s.innerText = parseInt(%s.innerText) + %s" % (self.varId, self.varId, JsUtils.jsConvertData(jsString, None)))
      elif valType == float:
        self._js.append("%s.innerText = parseFloat(%s.innerText) + %s" % (self.varId, self.varId, JsUtils.jsConvertData(jsString, None)))
      else:
        self._js.append("%s.innerText += %s" % (self.varId, JsUtils.jsConvertData(jsString, None)))
    else:
      self._js.append("%s.innerText = %s" % (self.varId, JsUtils.jsConvertData(jsString, None)))
    return self

  def textContent(self, jsString=None, append=False, valType=None):
    """
    Description:
    ------------
    The textContent property returns the text with spacing, but without inner element tags.

    Usage::

      select.label.dom.innerText("test Change")

    Related Pages:

      https://www.w3schools.com/jsref/prop_node_innertext.asp

    Attributes:
    ----------
    :param jsString: Optional, The Javascript String to be added
    :param append: Boolean. Mention if the component should replace or append the data
    :param valType: Type: The type of data expected in the component

    :return: The JsObj to allow the chaining
    """
    if jsString is None:
      return JsString.JsString("%s.textContent" % self.varId, isPyData=False)

    if append:
      if valType == int:
        self._js.append("%s.textContent = parseInt(%s.textContent) + %s" % (
        self.varId, self.varId, JsUtils.jsConvertData(jsString, None)))
      elif valType == float:
        self._js.append("%s.textContent = parseFloat(%s.textContent) + %s" % (
        self.varId, self.varId, JsUtils.jsConvertData(jsString, None)))
      else:
        self._js.append("%s.textContent += %s" % (self.varId, JsUtils.jsConvertData(jsString, None)))
    else:
      self._js.append("%s.textContent = %s" % (self.varId, JsUtils.jsConvertData(jsString, None)))
    return self

  def innerHTML(self, jsString=None, append=False, valType=None):
    """
    Description:
    ------------
    Sets or returns the content of an element

    Usage::

      select.label.dom.innerHTML("<p style='color:red'>Changed !</p>")

    Related Pages:

      https://www.w3schools.com/jsref/prop_html_innerhtml.asp

    Attributes:
    ----------
    :param jsString: Optional, The Javascript String to be added
    :param append: Boolean. Mention if the component should replace or append the data
    :param valType: Type: The type of data expected in the component

    :return: The JsObj
    """
    if jsString is None:
      return JsString.JsString("%s.innerHTML" % self.varId, isPyData=False)

    if append:
      if valType == int:
        self._js.append("%s.innerHTML = parseInt(%s.innerHTML) + %s" % (self.varId, self.varId, JsUtils.jsConvertData(jsString, None)))
      elif valType == int:
        self._js.append("%s.innerHTML = parseFloat(%s.innerHTML) + %s" % (self.varId, self.varId, JsUtils.jsConvertData(jsString, None)))
      else:
        self._js.append("%s.innerHTML += %s" % (self.varId, JsUtils.jsConvertData(jsString, None)))
    else:
      self._js.append("%s.innerHTML = %s" % (self.varId, JsUtils.jsConvertData(jsString, None)))
    return self

  def attr(self, type, jsObject=None):
    """
    Description:
    -----------
    The attr() method adds the specified attribute to an element, and gives it the specified value.
    It will use the underlying setAttribute() method

    Usage::

      select.label.dom.attr("title", "Tooltip")
    select.label.dom.attr({"title": "Tooltip"})

    Related Pages:

      https://www.w3schools.com/jsref/met_element_setattribute.asp

    Attributes:
    ----------
    :param type: A String with the type of parameter or a python dictionary
    :param jsObject: A JsObj with the value to be set

    :return: A JsObj
    """
    if jsObject is None and isinstance(type, dict):
      for k, v in type.items():
        if k == "id":
          self._id = v
        self._js.append("%s.setAttribute('%s', %s)" % (self.varId, k, JsUtils.jsConvertData(v, None)))
    else:
      if type == "id":
        self._id = jsObject
      self._js.append("%s.setAttribute('%s', %s)" % (self.varId, type, JsUtils.jsConvertData(jsObject, None)))
    return self

  def setAttribute(self, attributename, attributevalue):
    """
    Description:
    -----------
    The setAttribute() method adds the specified attribute to an element, and gives it the specified value.

    Usage::

      select.label.dom.setAttribute("title", "Tooltip")

    Related Pages:

      https://www.w3schools.com/jsref/met_element_setattribute.asp

    Attributes:
    ----------
    :param attributename: Required. The name of the attribute you want to add
    :param attributevalue: Required. The value of the attribute you want to add
    """
    self._js.append("%s.setAttribute('%s', %s)" % (self.varId, attributename, JsUtils.jsConvertData(attributevalue, None)))
    return self

  def addClass(self, clsName, attrs=None, eventAttrs=None, extend=True):
    """
    Description:
    -----------
    Adds the specified class(es) to each element in the set of matched elements.

    This function can either use an existing class or create one if the attrs or eventAttrs are defined

    Usage::

      table.dom.addClass("red", {"border": "1px solid green"}, extend=False)

    Related Pages:

      https://www.w3schools.com/jsref/met_element_setattribute.asp

    Attributes:
    ----------
    :param clsName: The Css classname
    :param attrs: A python dictionary with the css attributes
    :param eventAttrs: A nested python dictionary with the css attributes for each events
    :param extend: Boolean. To set if the class should replace the existing style definition

    :return:
    """
    if attrs is not None or eventAttrs is not None:
      clsName = self._report.style.cssName(clsName)
      self._report.style.cssCls(clsName, attrs, eventAttrs, False)
    if extend:
      self._js.append('%s.setAttribute("class", %s.getAttribute("class") + " %s")' % (self.varId, self.varId, clsName))
    else:
      self._js.append('%s.setAttribute("class", "%s")' % (self.varId, clsName))
    return self

  def css(self, type, jsObject=None, duration=None):
    """
    Description:
    -----------
    Replicate in plain Js the Jquery CSS function

    Usage::

      select.label.dom.css({"color": "red"})

    Related Pages:

      https://www.w3schools.com/jsref/met_element_setattribute.asp

    Attributes:
    ----------
    :param type: A String with the type of parameter or a python dictionary
    :param jsObject: A JsObj with the value to be set

    :return: A JsObj
    """
    if jsObject is None and isinstance(type, dict):
      for k, v in type.items():
        if "-" in k:
          split_css = k.split("-")
          k = "%s%s" % (split_css[0], split_css[1].title())
        self._js.append("%s.style.%s = %s" % (self.varId, k, JsUtils.jsConvertData(v, None)))
    elif jsObject is None:
      if "-" in type:
        split_css = type.split("-")
        type = "%s%s" % (split_css[0], split_css[1].title())
      return JsObject.JsObject("%s.style.%s" % (self.varId, type))
    else:
      if "-" in type:
        split_css = type.split("-")
        type = "%s%s" % (split_css[0], split_css[1].title())
      self._js.append("%s.style.%s = %s" % (self.varId, type, JsUtils.jsConvertData(jsObject, None)))
    return self

  def position(self, x=None, y=None, dx=0, dy=0):
    """
    Description:
    -----------
    Set the position of the component in the page.
    By default the component will be fixed at the mouse level (this should be used in an event).

    Usage::

      rptObj.js.createElement("div", "popup").innerHTML("uygk,k,kj..kj.kjyf").attr('id', 'popup').css({
        'color': 'red', 'display': 'block'}).position()

    Attributes:
    ----------
    :param x: Integer. The positinn from the top of the page
    :param y: Integer. The position from the left
    :param dx: Integer.
    :param dy: Integer.

    :return: A JsObj
    """
    if x is None and y is None:
      self.css({"position": 'absolute', 'top': JsObject.JsObject.get("(event.clientY + window.scrollY + %s) + 'px'" % dy),
                'left': JsObject.JsObject.get("(event.clientX + window.scrollX + %s) + 'px'" % dx)})
    else:
      self.css({"position": 'absolute', 'top': "%spx" % x or 0, 'left': "%spx" % x or 0})
    return self

  def toggle_transition(self, attribute, value, value2, duration=1, timing_fnc='ease', delay=None):
    """
    Description:
    ------------
    Toogle a transition

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_transition.asp

    Attributes:
    ----------
    :param attribute: String or List. Specifies the name of the CSS property the transition effect is for
    :param value: String or List. Specifies the value of the CSS property the transition effect is for
    :param value2: String or List. Specifies the value of the CSS property the transition effect is for
    :param duration: Number or List. Specifies how many seconds or milliseconds the transition effect takes to complete
    :param delay: Number. Defines when the transition effect will start
    :param timing_fnc: String. The transition-timing-function property specifies the speed curve of the transition effect.
    """
    if "-" in attribute:
      split_css = attribute.split("-")
      css_attr = "%s%s" % (split_css[0], split_css[1].title())
    else:
      css_attr = attribute
    tmp = list(self._js)
    self._js = []
    self.transition(attribute, value, duration, delay, timing_fnc)
    if_ = "; ".join(self._js)

    self._js = []
    self.transition(attribute, value2, duration, delay, timing_fnc)
    else_ = "; ".join(self._js)
    self._js = tmp
    self._js.append("if(%s.style.%s != '%s') {%s} else {%s}" % (self.varId, css_attr, value, if_, else_))
    return self

  def transition(self, attribute, value, duration=1, delay=None, timing_fnc='ease', reverse=False):
    """
    Description:
    ------------
    The transition property is a shorthand property for:
      - transition-property
      - transition-duration
      - transition-timing-function
      - transition-delay

    Usage::

      i.label.dom.transition('margin-left', '100px', 2, reverse=True),
    i.label.dom.transition('color', 'red', 5, reverse=True),

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_transition.asp

    Attributes:
    ----------
    :param attribute: String or List. Specifies the name of the CSS property the transition effect is for
    :param value: String or List. Specifies the value of the CSS property the transition effect is for
    :param duration: Number or List. Specifies how many seconds or milliseconds the transition effect takes to complete
    :param delay: Number. Defines when the transition effect will start
    :param timing_fnc: String. The transition-timing-function property specifies the speed curve of the transition effect.
    :param reverse: Boolean. Rewind the transition animation
    """
    self.css("transition-property", ",".join(attribute) if isinstance(attribute, list) else attribute)
    if isinstance(duration, list):
      self.css("transition-duration", "%ss" % "s, ".join(map(lambda x: str(x), duration)))
    else:
      self.css("transition-duration", "%ss" % duration)
    self.css("transition-timing-function", timing_fnc)
    if delay is not None:
      if isinstance(delay, int):
        self.css("transition-delay", "%ss" % delay)
      else:
        self.css("transition-delay", delay)
    if reverse:
      if isinstance(attribute, list):
        for i, attr in enumerate(attribute):
          self._js.append(self.css(attr).setVar("css_transition_%s" % i).r)
          self._js.append("setTimeout(function(){%s = css_transition_%s}, %s)" % (self.css(attr), i, duration[i] * 1000))
      else:
        self._js.append(self.css(attribute).setVar("css_transition").r)
        self._js.append("setTimeout(function(){%s = css_transition}, %s)" % (self.css(attribute), duration * 1000))

    if isinstance(attribute, list):
      for i, attr in enumerate(attribute):
        self.css(attr, value[i])
    else:
      self.css(attribute, value)
    self.css("transition-property", "initial")
    return self

  def hide(self):
    """
    Description:
    ------------

    Usage::

      input.js.hide()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/
    """
    return self.css("display", "none")

  def show(self, display_value=None, duration=None):
    """
    Description:
    ------------

    Usage::

      input.js.hide()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/
    """
    self.css("display", display_value or self.display_value)
    if duration is not None:
      self._js.append("setTimeout(function(){%s.style.display = 'none'}, %s)" % (self.varId, duration))
    return self

  def toggle(self, attr="display", jsVal1=None, jsVal2="none"):
    """
    Description:
    ------------
    Hexadecimal colors should be converted to rgb code as only the computed style will be compared.
    To do so you can use: Colors.getHexToRgb(self._report.theme.success[1]) from epyk.core.css import Colors

    Attributes:
    ----------
    :param attr:
    :param jsVal1:
    :param jsVal2:
    """
    if attr == 'display' and jsVal1 is None:
      jsVal1 = self.display_value
    if "-" in attr:
      split_css = attr.split("-")
      attr = "%s%s" % (split_css[0], split_css[1].title())
    self._js.append("if(window.getComputedStyle(%(varId)s).%(attr)s == '%(jsVal1)s'){ %(varId)s.style.%(attr)s = '%(jsVal2)s'} else { %(varId)s.style.%(attr)s = '%(jsVal1)s'}" % {"varId": self.varId, "attr": attr, "jsVal1": jsVal1, "jsVal2": jsVal2})
    return self

  def toggleAttrs(self, pivot_key, pivot_val, attrs_off, attrs_on):
    """
    Description:
    ------------
    Toggle some CSS attributes

    Attributes:
    ----------
    :param pivot_key:
    :param pivot_val:
    :param attrs_on: A python dictionary with CSS attributes
    :param attrs_off: A python dictionary with CSS attributes
    """
    if pivot_key in ["color"] and not pivot_val.startswith("rgb"):
      colors_def = Colors.defined[pivot_val.upper()]
      pivot_val = "rgb%s" % colors_def['rgb']
    css_attrs_on = self.css(attrs_on).toStr()
    css_attrs_off = self.css(attrs_off).toStr()
    self._js.append("if(window.getComputedStyle(%(varId)s)['%(pivot_key)s'] == '%(pivot_val)s') {%(css_attrs_on)s} else {%(css_attrs_off)s}" % {"pivot_val": pivot_val, "varId": self.varId, "pivot_key": pivot_key, 'css_attrs_on': css_attrs_on, 'css_attrs_off': css_attrs_off})
    return self

  def toggleText(self, jsString1, jsString2):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsString:
    """
    str1 = JsUtils.jsConvertData(jsString1, None)
    str2 = JsUtils.jsConvertData(jsString2, None)
    self._js.append("if(%(varId)s.innerText == %(str2)s) {%(varId)s.innerText = %(str1)s} else {%(varId)s.innerText = %(str2)s}" % {"varId": self.varId, "str1": str1, "str2": str2})
    return self

  @property
  def clientHeight(self):
    """
    Description:
    ------------
    The Element.clientHeight read-only property is zero for elements with no CSS or inline layout boxes; otherwise, it's the inner height of an element in pixels.
    It includes padding but excludes borders, margins, and horizontal scrollbars (if present).

    Usage::

      rptObj.js.alert(rptObj.js.body.clientHeight)

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Element/clientHeight
    """
    return JsNumber.JsNumber("%s.clientHeight" % self.varId)

  def toggleClass(self, clsName, propagate=False):
    """
    Description:
    ------------
    Toggle a class name

    Attributes:
    ----------
    :param clsName: The classname to be toggle

    :return:
    """
    clsName = JsUtils.jsConvertData(clsName, None)
    if propagate:
      self._js.append('%(varId)s.parentNode.childNodes.forEach(function(e){e.classList.remove(%(data)s)})' % {"varId": self.varId, 'data': clsName})
    self._js.append('var classes = %(data)s.split(" "); classes.forEach(function(cls){ %(varId)s.classList.toggle(cls); })' % {"varId": self.varId, 'data': clsName})
    return self

  def switchClass(self, clsName1, clsName2):
    """
    Description:
    ------------
    Switch from one CSS class to another.

    Usage::

      icon.dom.switchClass("fa-folder", "fa-folder-open")

    Attributes:
    ----------
    :param clsName1: String. A class name or a string with a list of classname space separated
    :param clsName2: String. A class name or a string with a list of classname space separated

    :return: Self to allow the chaining
    """
    self.toggleClass(clsName1)
    self.toggleClass(clsName2)
    return self

  @property
  def firstChild(self):
    """
    Description:
    ------------
    The firstChild property returns the first child node of the specified node, as a Node object.

    Usage::

      select.dom.firstChild
    select.dom.firstChild.css({"color": "yellow"})

    Related Pages:

      https://www.w3schools.com/jsref/prop_node_firstchild.asp

    :return: A new JsDom python object
    """
    return JsDoms("%s.firstChild" % self.varId)

  @property
  def nextSibling(self):
    """
    Description:
    ------------
    The nextSibling property returns the node immediately following the specified node, in the same tree level.

    Related Pages:

      https://www.w3schools.com/jsref/prop_node_nextsibling.asp
    """
    return JsDoms("%s.nextSibling" % self.varId)

  def contains(self, node):
    """
    Description:
    ------------
    The contains() method returns a Boolean value indicating whether a node is a descendant of a specified node.

    Related Pages:

      https://www.w3schools.com/jsref/met_node_contains.asp

    Attributes:
    ----------
    :param node: Required. Specifies the node that may be contained by (a descendant of) a specified node

    :return: A Boolean
    """
    return JsBoolean.JsBoolean('%s.contains(%s)' % (self.varId, node))

  def getAttribute(self, attributename):
    """
    Description:
    ------------
    The getAttribute() method returns the value of the attribute with the specified name, of an element.

    Usage::

      select.dom.getAttribute("class")

    Related Pages:

      https://www.w3schools.com/jsref/met_element_getattribute.asp

    Attributes:
    ----------
    :param attributename: Required. The name of the attribute you want to get the value from

    :return: A String, representing the specified attribute's value.
    """
    return JsObject.JsObject("%s.getAttribute(%s)" % (self.varId, JsUtils.jsConvertData(attributename, None)), isPyData=False)

  def getAttributeNode(self, attributename):
    """
    Description:
    ------------
    The getAttributeNode() method returns the attribute node with the specified name of an element, as an Attr object.

    Related Pages:

      https://www.w3schools.com/jsref/met_element_getattributenode.asp

    Attributes:
    ----------
    :param attributename: Required. The name of the attribute you want to return

    :return: An Attr object, representing the specified attribute node.
    """
    return JsString.JsString(varId="%s.getAttributeNode('%s')" % (self.varId, attributename))

  def getComputedStyle(self, attributename=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param attributename:
    """
    if attributename is None:
      return JsString.JsString("getComputedStyle(%s)" % self.varId, isPyData=False)

    if "-" in attributename:
      split_css = attributename.split("-")
      attributename = "%s%s" % (split_css[0], split_css[1].title())
    return JsString.JsString("getComputedStyle(%s).%s" % (self.varId, attributename), isPyData=False)

  def getBoundingClientRect(self):
    """
    Description:
    -----------
    The getBoundingClientRect() method returns the size of an element and its position relative to the viewport.

    Related Pages:

      https://www.w3schools.com/jsref/met_element_getboundingclientrect.asp
    https://developer.mozilla.org/en-US/docs/Web/API/DOMRect
    """
    return JsNodeDomRect.JsDOMRect("%s.getBoundingClientRect()" % self.varId)

  @property
  def hasChildNodes(self):
    """
    Description:
    ------------
    Returns true if an element has any child nodes, otherwise false

    Usage::

      select.dom.hasChildNodes

    Related Pages:

      https://www.w3schools.com/jsref/met_node_haschildnodes.asp

    :return: A Boolean, returns true if the node has child nodes, false otherwise
    """
    return JsBoolean.JsBoolean("%s.hasChildNodes()" % self.varId, isPyData=False)

  def hasClass(self, className):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param className:

    :return:
    """
    className = JsUtils.jsConvertData(className, None)
    return JsBoolean.JsBoolean("%s.classList.contains(%s)" % (self.varId, className), isPyData=False)

  def text(self, jsString):
    """
    Description:
    ------------
    Javascript Function

    Shortcut in charge oa creating a text node object and adding the text.

    Related Pages:
Attributes:
    ----------
    :param jsString: The Javascript String of the text node component

    :return: The main Python Dom Object
    """
    return self.appendChild(JsFncs.JsFunction("document.createTextNode(%s)" % JsUtils.jsConvertData(jsString, None)))

  @property
  def childNodes(self):
    """
    Description:
    ------------
    The childNodes property returns a collection of a node's child nodes, as a NodeList object.

    The nodes in the collection are sorted as they appear in the source code and can be accessed by index numbers. The index starts at 0.

    Related Pages:

      https://www.w3schools.com/jsref/prop_node_childnodes.asp

    :return: A NodeList object, representing a collection of nodes. The nodes in the returned collection are sorted as they appear in the source code
    """
    self._js.append("%s.childNodes" % self.varId)
    return self

  @property
  def tagName(self):
    """
    Description:
    ------------
    The tagName property returns the tag name of the element

    Usage::

      select.dom.tagName

    Related Pages:

      https://www.w3schools.com/jsref/prop_element_tagname.asp

    :return: A String, representing the tag name of the element in uppercase
    """
    return JsString.JsString("%s.tagName" % self.varId, isPyData=False)

  @property
  def offsetTop(self):
    """
    Description:
    ------------
    The HTMLElement.offsetTop read-only property returns the distance of the current element relative to the top of the offsetParent node.

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/API/HTMLElement/offsetTop
    """
    return JsString.JsString("%s.offsetTop" % self.varId, isPyData=False)

  def contentEditable(self, bool):
    """
    Description:
    ------------
    Set content editable

    Usage::

      rptObj.ui.text("This is a text").dom.contentEditable(True)

    Attributes:
    ----------
    :param bool: Boolean. Set the content editable flag to the Dom object

    :return: Return a JsBoolean object
    """
    return JsBoolean.JsBoolean.get("%s.contentEditable = %s" % (self.varId, JsUtils.jsConvertData(bool, None)))

  def className(self, className=None):
    """
    Description:
    ------------
    The className property sets or returns the class name of an element (the value of an element's class attribute).

    Usage::

      select.dom.className()

    Related Pages:

      https://www.w3schools.com/jsref/prop_html_classname.asp

    Attributes:
    ----------
    :param className: Specifies the class name of an element. To apply multiple classes, separate them with spaces, like "test demo"

    :return: A String, representing the class, or a space-separated list of classes, of an element
    """
    if className is None:
      return JsString.JsString("%s.className" % self.varId, isPyData=False)

    # TODO fix this properly
    return JsString.JsString("%s; %s.className = %s" % (self.toStr(), self.varId, JsUtils.jsConvertData(className, None)), isPyData=False)

  def cloneNode(self, deep=True):
    """
    Description:
    ------------
    The cloneNode() method creates a copy of a node, and returns the clone.

    The cloneNode() method clones all attributes and their values.

    Usage::

      select.dom.cloneNode()

    Related Pages:

      https://www.w3schools.com/jsref/met_node_clonenode.asp

    Attributes:
    ----------
    :param deep: Optional. Specifies whether all descendants of the node should be cloned.

    :return: A Node object, representing the cloned node
    """
    return JsDoms("%s.cloneNode(%s)" % (self.varId, JsUtils.jsConvertData(deep, None)))

  def remove(self):
    """
    Description:
    ------------
    Remove the current dom object from the page

    Usage::

      select.dom.remove()

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/API/ChildNode/remove
    """
    return JsFncs.JsFunction("%s.remove()" % self.varId)

  def removeChild(self, jsDom):
    """
    Description:
    ------------
    Removes a child node from an element

    Related Pages:

      https://www.w3schools.com/jsref/met_node_removechild.asp

    Attributes:
    ----------
    :param jsDom: Required. The node object you want to remove

    :return: A Node object, representing the removed node, or null if the node does not exist
    """
    return JsDoms("%s.removeChild(%s)" % (self.varId, jsDom))

  def appendChild(self, jsDom):
    """
    Description:
    ------------
    The appendChild() method appends a node as the last child of a node.

    Usage::

      select.dom.appendChild(select.label.dom.cloneNode())

    Related Pages:

      https://www.w3schools.com/jsref/met_node_appendchild.asp

    Attributes:
    ----------
    :param jsDom: Required. The node object you want to append

    :return: 	A Node Object, representing the appended node
    """
    self._js.append("%s.appendChild(%s)" % (self.varId, JsUtils.jsConvertData(jsDom, None)))
    return self

  def insertBefore(self, newnode, existingnode=None):
    """
    Description:
    ------------
    The insertBefore() method inserts a node as a child, right before an existing child, which you specify.

    Usage::

      select.dom.insertBefore(select.label.dom.cloneNode())

    Related Pages:

      https://www.w3schools.com/jsref/met_node_insertbefore.asp

    Attributes:
    ----------
    :param newnode: Required. The node object you want to insert
    :param existingnode: Optional. The child node you want to insert the new node before. If set to null, the insertBefore method will insert the newnode at the end
    """
    if existingnode is None:
      self._js.append("%s.insertBefore(%s, %s)" % (self.varId, newnode, self.firstChild))
    else:
      self._js.append("%s.insertBefore(%s, %s)" % (self.varId, newnode, existingnode))
    return self

  def click(self, jsFncs=None):
    """
    Description:
    -----------
    Trigger a click event.
    This function will not set the event

    Attributes:
    ----------
    :param jsFncs:
    """
    if jsFncs is None:
      return JsObject.JsObject("%s.click()" % self.varId)

    self._js.append("%s.click(%s)" % (self.varId, ";".join(JsUtils.jsConvertFncs(jsFncs))))
    return self

  def onclick(self, jsFncs, autoStyle=True):
    """
    Description:
    -----------
    Execute a JavaScript when a button is clicked

    Related Pages:

      https://www.w3schools.com/jsref/event_onclick.asp

    Attributes:
    ----------
    :param jsFncs: The Javascript function
    :param autoStyle: Some predefined style attributes added to this event (self.css({"cursor": "pointer"}))

    :return: The PyDom object
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if autoStyle:
      self.css({"cursor": "pointer"})
    self._js.append("%s.onclick = function(){%s}" % (self.varId, ";".join(JsUtils.jsConvertFncs(jsFncs))))
    return self

  def onVisible(self, jsFncs):
    """
    Description:
    ------------

    :param jsFncs:

    :return:
    """
    self._js.append("var rect = elm.getBoundingClientRect()" % self.varId)
    return self

  def getContext(self, contextType, contextAttributes=None):
    """
    Function dedicated to DOM Canvas types.

    The HTMLCanvasElement.getContext() method returns a drawing context on the canvas, or null if the context identifier is not supported.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext

    Attributes:
    ----------
    :param contextType: Is a DOMString containing the context identifier defining the drawing context associated to the canvas
    :param contextAttributes: Dictionary with specific context attributes (depending on the type

    TODO: Add a check on the tag

    :return:
    """
    types = ["2d", "webgl", "experimental-webgl", "webgl2", "bitmaprenderer"]
    if contextType not in types:
      raise Exception("Context type %s not recognised" % contextType)

    if contextAttributes is None:
      return JsFncs.JsFunction("%s.getContext('%s')" % (self.varId, contextType))

    contextAttributes = JsUtils.jsConvertData(contextAttributes, None)
    return JsFncs.JsFunction("%s.getContext('%s', %s)" % (self.varId, contextType, contextAttributes))


class JsDomsList(JsArray.JsArray):

  def all(self, jsFncs):
    """
    Description:
    ------------
    Apply a set of functions on all the elements with this name.

    Attributes:
    ----------
    :param jsFncs: Array. List of Javascript fragments
    """
    self._js.append("%s.forEach(function(elt, index){%s})" % (self.varId, JsUtils.jsConvertFncs(jsFncs, toStr=True)))
    return self

  @property
  def first(self):
    """
    Description:
    ------------
    Get the first dom item in corresponding to the name criteria
    """
    return JsDoms.get("%s[0]" % self.toStr())

  def css(self, type, jsObject=None):
    """
    Description:
    ------------
    Replicate in plain Js the Jquery CSS function

    Usage::

      select.label.dom.css({"color": "red"})

    Related Pages:

      https://www.w3schools.com/jsref/met_element_setattribute.asp

    Attributes:
    ----------
    :param type: A String with the type of parameter or a python dictionary
    :param jsObject: A JsObj with the value to be set

    :return: A JsObj
    """
    if jsObject is None and isinstance(type, dict):
      for k, v in type.items():
        if "-" in k:
          split_css = k.split("-")
          k = "%s%s" % (split_css[0], split_css[1].title())
        self._js.append("for(let e of %s){ e.style.%s = %s }" % (self.varId, k, JsUtils.jsConvertData(v, None)))
    elif jsObject is None:
      if "-" in type:
        split_css = type.split("-")
        type = "%s%s" % (split_css[0], split_css[1].title())
      return JsObject.JsObject("for(let e of %s){ e.style.%s }" % (self.varId, type))
    else:
      if "-" in type:
        split_css = type.split("-")
        type = "%s%s" % (split_css[0], split_css[1].title())
      self._js.append("for(let e of %s){ e.style.%s = %s }" % (self.varId, type, JsUtils.jsConvertData(jsObject, None)))
    return self

  def log(self):
    """
    Description:
    ------------
    Add a print to the loop to assist on the implementation
    """
    self._js.append("for(let e of %s){ console.log(e) }" % self.varId)
    return self

  def attr(self, type, jsObject=None):
    """
    Description:
    ------------
    The attr() method adds the specified attribute to an element, and gives it the specified value.
    It will use the underlying setAttribute() method

    Usage::

      select.label.dom.attr("title", "Tooltip")
    select.label.dom.attr({"title": "Tooltip"})

    Related Pages:

      https://www.w3schools.com/jsref/met_element_setattribute.asp

    Attributes:
    ----------
    :param type: A String with the type of parameter or a python dictionary
    :param jsObject: A JsObj with the value to be set

    :return: A JsObj
    """
    if jsObject is None and isinstance(type, dict):
      for k, v in type.items():
        if k == "id":
          self._id = v
        self._js.append("for(let e of %s){ e.setAttribute('%s', %s) }" % (self.varId, k, JsUtils.jsConvertData(v, None)))
    else:
      if type == "id":
        self._id = jsObject
      self._js.append("for(let e of %s){ e.setAttribute('%s', %s) }" % (self.varId, type, JsUtils.jsConvertData(jsObject, None)))
    return self

  def __getitem__(self, index):
    """
    Description:
    ------------
    Get the nth item corresponding to the name in the HTML page

    Attributes:
    ----------
    :param index: Integer. The index number of the item
    """
    return JsDoms.get("%s[%s]" % (self.toStr(), index))
