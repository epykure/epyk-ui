#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional, List
from epyk.core.py import primitives

from epyk.core.js.fncs import JsFncs
from epyk.core.css import Colors
from epyk.core.css.styles.effects import Effects

from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsArray

from epyk.core.js.objects import JsNodeDomRect

from epyk.core.js import JsUtils


class JsDomEvents(primitives.JsDataModel):

  def __init__(self, component: primitives.HtmlModel = None, js_code: str = None):
    self.component = component
    self._js = []
    if js_code is not None:
      self.varName = js_code
    else:
      self.varName = "document.getElementById('%s')" % self.component.htmlCode

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

  def blur(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    FocusEvent

    The event occurs when an element loses focus

    Related Pages:

      https://www.w3schools.com/jsref/event_onblur.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("blur", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def click(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when the user clicks on an element.

    Usage::

      select.label.dom.events.click(rptObj.js.console.log("test"))

    Related Pages:

      https://www.w3schools.com/jsref/event_onclick.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("click", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def change(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when the content of a form element, the selection, or the checked state have changed (for <input>,
    <select>, and <textarea>)

    Usage::

      select.dom.events.change(rptObj.js.window.alert("test"))

    Related Pages:

      https://www.w3schools.com/jsref/event_onchange.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("change", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def dblclick(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when the user double-clicks on an element.

    Related Pages:

      https://www.w3schools.com/jsref/event_ondblclick.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("dblclick", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def focus(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when an element gets focus.

    Related Pages:

      https://www.w3schools.com/jsref/event_onfocusin.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("focus", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def focusin(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when an element is about to get focus.

    Related Pages:

      https://www.w3schools.com/jsref/event_onfocusin.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("focusin", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def focusout(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when an element is about to lose focus.

    Related Pages:

      https://www.w3schools.com/jsref/event_onfocusout.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("focusin", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def keydown(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when the user is pressing a key

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeydown.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append(
      'addEventListener("keydown", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def keypress(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when the user presses a key

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeypress.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("keypress", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def keyup(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when the user releases a key.

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeyup.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("keyup", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def mousedown(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when the user presses a mouse button over an element.

    Related Pages:

      https://www.w3schools.com/jsref/event_onmousedown.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mousedown", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def mouseenter(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when the pointer is moved onto an element.

    Related Pages:

      https://www.w3schools.com/jsref/event_onmouseenter.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mousedown", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def mouseleave(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when the pointer is moved out of an element

    Usage::

      select.label.dom.events.mouseleave(rptObj.js.console.log("test"))

    Related Pages:

      https://www.w3schools.com/jsref/event_onmouseleave.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseleave", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def mouseover(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when the pointer is moved onto an element, or onto one of its children.

    Related Pages:

      https://www.w3schools.com/jsref/event_onmouseover.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseover", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def mouseup(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when a user releases a mouse button over an element

    Related Pages:

      https://www.w3schools.com/jsref/event_onmouseup.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseover", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def mouseout(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The event occurs when a user releases a mouse button over an element.

    Related Pages:

      https://www.w3schools.com/jsref/event_onmouseout.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: An array of Js functions or string. Or a string with the Js.

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseout", function(){%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True))
    return self

  def trigger(self, event: Union[str, primitives.JsDataModel], with_focus: bool = True,
              options: dict = None, event_name: str = "clickEvent"):
    """
    Description:
    ------------
    Trigger a javascript event

    Related Pages:

      https://www.w3schools.com/jsref/met_html_focus.asp
      https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Creating_and_triggering_events

    Usage::

      page.body.onReady([
        b.dom.events.trigger("click")
      ])

    Attributes:
    ----------
    :param event: The event name
    :param with_focus: Boolean. Optional. a boolean to define if the focus needs to be set to this component
    :param options: Dictionary. Optional. Possibility to pass time option in second to set an implicit interval on the event
    :param event_name: String.  Optional.

    :return: The Javascript string of this function
    """
    if event == 'enter':
      event = "new Event('keypress'); %s.keyCode = 13" % event_name
    else:
      event = "new Event(%s)" % JsUtils.jsConvertData(event, None)
    if with_focus:
      if options is not None and 'timer' in options:
        return JsFncs.JsFunction(
          "window['%(htmlCode)s_timer'] = setInterval(function(){var %(event_name)s = %(event)s; %(elem)s.focus(); %(elem)s.dispatchEvent(%(event_name)s)}, %(timer)s)" % {
            "htmlCode": self.component.htmlCode, "event_name": event_name, "event": event, "elem": self.varName,
            'timer': options['timer'] * 1000})

      else:
        return JsFncs.JsFunction(
          "(function(){var %(event_name)s = %(event)s; %(elem)s.focus(); %(elem)s.dispatchEvent(%(event_name)s)})()" % {
            "event": event, "event_name": event_name, "elem": self.varName})

    if options is not None and 'timer' in options:
      return JsFncs.JsFunction('''
        window['%(htmlCode)s_timer'] = setInterval(function(){var %(event_name)s = %(event)s; 
          %(elem)s.dispatchEvent(%(event_name)s)}, %(timer)s)''' % {
        "htmlCode": self.component.htmlCode, "event_name": event_name, "event": event, "elem": self.varName,
        'timer': options['timer'] * 1000})

    else:
      return JsFncs.JsFunction(
        "(function(){var %(event_name)s = %(event)s; %(elem)s.dispatchEvent(%(event_name)s)})()" % {
          "event": event, "event_name": event_name, "elem": self.varName})

  def toStr(self):
    if self.component.htmlCode is None:
      raise ValueError("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self.component.htmlCode

    str_data = "%(varName)s.%(items)s" % {
      'varName': self.varName, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return str_data


class JsDomsTransforms:

  def __init__(self, page, selector):
    self.page, self.selector = page, selector

  def initial(self):
    """
    Description:
    -----------
    Sets this property to its default value

    """
    return "%s.initial" % self.selector

  def inherit(self):
    """
    Description:
    -----------
    Inherits this property from its parent element.

    """
    return "%s.initial" % self.selector

  def matrix(self, scale_x: float, skew_y: float, skew_x: float, scale_y: float, translate_x: float,
             translate_y: float):
    """
    Description:
    ------------
    Defines a 2D transformation, using a matrix of six values.

    Usage::

      Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/matrix

    Attributes:
    ----------
    :param float scale_x:
    :param float skew_y:
    :param float skew_x:
    :param float scale_y:
    :param float translate_x:
    :param float translate_y:
    """
    return "%s.style.transform = 'matrix(%s, %s, %s, %s, %s, %s)'" % (
      self.selector, scale_x, skew_y, skew_x, scale_y, translate_x, translate_y)

  def translateX(self, x: int, unit: str = 'px'):
    """
    Description:
    ------------
    The translateX() CSS function repositions an element horizontally on the 2D plane. Its result is a
    <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/translateX
      https://www.w3schools.com/jsref/prop_style_transform.asp

    Attributes:
    ----------
    :param int x:
    :param str unit: The unit used for the transformation (px, cm, rem...)
    """
    return "%s.style.transform = 'translateX(%s%s)'" % (self.selector, x, unit)

  def translateY(self, y: int, unit: str = 'px'):
    """
    Description:
    ------------
    The translateY() CSS function repositions an element vertically on the 2D plane. Its result is a
    <transform-function> data type.

    Related Pages:

      https://www.w3schools.com/jsref/prop_style_transform.asp

    Attributes:
    ----------
    :param int y:
    :param float unit: The unit used for the transformation (px, cm, rem...)
    """
    return "%s.style.transform = 'translateY(%s%s)'" % (self.selector, y, unit)

  def translate(self, x: int, y: int, unit: str = 'px'):
    """
    Description:
    ------------
    The translate() CSS function repositions an element in the horizontal and/or vertical directions.
    Its result is a <transform-function> data type.

    Related Pages:

      https://www.w3schools.com/jsref/prop_style_transform.asp

    Attributes:
    ----------
    :param int x:
    :param int y:
    :param str unit: The unit used for the transformation (px, cm, rem...)
    """
    return "%s.style.transform = 'translate(%s%s, %s%s)'" % (self.selector, x, unit, y, unit)

  def perspective(self, d: int, unit: str = 'px'):
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
    :param int d: Is a <length> representing the distance from the user to the z=0 plane.
              If it is 0 or a negative value, no perspective transform is applied.
    :param str unit: The unit used for the transformation (px, cm, rem...)
    """
    return "%s.style.transform = 'perspective(%s%s)'" % (self.selector, d, unit)

  def scale(self, x: float, y: float):
    """
    Description:
    ------------
    The scale() CSS function defines a transformation that resizes an element on the 2D plane.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/scale

    Attributes:
    ----------
    :param float x: A <number> representing the abscissa of the scaling vector.
    :param float y: A <number> representing the ordinate of the scaling vector.
              If not defined, its default value is sx, resulting in a uniform scaling that preserves the element's
              aspect ratio.
    """
    return "%s.style.transform = 'scale(%s, %s)'" % (self.selector, x, y)

  def scaleX(self, x: float):
    """
    Description:
    ------------
    The scaleX() CSS function defines a transformation that resizes an element along the x-axis (horizontally).
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/scaleX

    Attributes:
    ----------
    :param float x: Is a <number> representing the scaling factor to apply on the abscissa of each point of the
    element.
    """
    return "%s.style.transform = 'scaleX(%s)'" % (self.selector, x)

  def scaleY(self, y: float):
    """
    Description:
    ------------
    The scaleY() CSS function defines a transformation that resizes an element along the y-axis (vertically).
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/scaleY

    Attributes:
    ----------
    :param float y: Is a <number> representing the scaling factor to apply on the ordinate of each point of the
    element.
    """
    return "%s.style.transform = 'scaleY(%s)'" % (self.selector, y)

  def skew(self, angle_x: float, angle_y: float = 0, unit: str = 'deg'):
    """
    Description:
    ------------
    The skew() CSS function defines a transformation that skews an element on the 2D plane.
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/skew

    Attributes:
    ----------
    :param float angle_x: Is an <angle> representing the angle to use to distort the element along the abscissa.
    :param float angle_y: Is an <angle> representing the angle to use to distort the element along the ordinate.
    If not defined, its default value is 0, resulting in a purely horizontal skewing.
    :param str unit: The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'skew(%s%s, %s%s)'" % (self.selector, angle_x, unit, angle_y, unit)

  def skewX(self, angle: float, unit: str = 'deg'):
    """
    Description:
    ------------
    The skewX() CSS function defines a transformation that skews an element in the horizontal direction on the 2D plane.
    Its result is a <transform-function> data type.

    Usage::

      i.label.dom.transform.skewX(20)

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/skewX

    Attributes:
    ----------
    :param float angle: Is an <angle> representing the angle to use to distort the element along the abscissa.
    :param str unit: The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'skewX(%s%s)'" % (self.selector, angle, unit)

  def skewY(self, angle: float, unit: str = 'deg'):
    """
    Description:
    ------------
    The skewY() CSS function defines a transformation that skews an element in the vertical direction on the 2D plane.
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/skewY

    Attributes:
    ----------
    :param float angle: Is an <angle> representing the angle to use to distort the element along the ordinate.
    :param str unit: The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'skewY(%s%s)'" % (self.selector, angle, unit)

  def rotate(self, r: float, unit: str = 'deg'):
    """
    Description:
    ------------
    The rotate() CSS function defines a transformation that rotates an element around a fixed point on the 2D plane,
    without deforming it.
    Its result is a <transform-function> data type.

    Usage::

      i.label.dom.transform.rotate(90)

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate

    Attributes:
    ----------
    :param float r: Is an <angle> representing the angle of the rotation. A positive angle denotes a clockwise rotation,
    a negative angle a counter-clockwise one.
    :param str unit: The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'rotate(%s%s)'" % (self.selector, r, unit)

  def rotate3d(self, x: float, y: float, z: float, a: float, unit: str = 'deg'):
    """
    Description:
    ------------
    The rotate3d() CSS function defines a transformation that rotates an element around a fixed axis in 3D space,
    without deforming it.
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d

    Attributes:
    ----------
    :param float x: Is a <number> describing the x-coordinate of the vector denoting the axis of rotation which could between 0 and 1.
    :param float y: Is a <number> describing the y-coordinate of the vector denoting the axis of rotation which could between 0 and 1.
    :param float z: Is a <number> describing the z-coordinate of the vector denoting the axis of rotation which could between 0 and 1.
    :param float a: Is an <angle> representing the angle of the rotation. A positive angle denotes a clockwise rotation, a negative angle a counter-clockwise one.
    :param str unit: The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'rotate3d(%s, %s, %s, %s%s)'" % (self.selector, x, y, z, a, unit)

  def rotateX(self, r: float, unit: str = 'deg'):
    """
    Description:
    ------------
    The rotateX() CSS function defines a transformation that rotates an element around the abscissa (horizontal axis)
    without deforming it.
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotateX

    Attributes:
    ----------
    :param float r: Is an <angle> representing the angle of the rotation. A positive angle denotes a clockwise rotation,
    a negative angle a counter-clockwise one.
    :param str unit: The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'rotateX(%s%s)'" % (self.selector, r, unit)

  def rotateY(self, r: float, unit: str = 'deg'):
    """
    Description:
    ------------
    The rotateY() CSS function defines a transformation that rotates an element around the ordinate (vertical axis)
    without deforming it.
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotateY

    Attributes:
    ----------
    :param float r: Is an <angle> representing the angle of the rotation. A positive angle denotes a clockwise rotation,
    a negative angle a counter-clockwise one.
    :param str unit: The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'rotateY(%s%s)'" % (self.selector, r, unit)

  def rotateZ(self, r: float, unit: str = 'deg'):
    """
    Description:
    ------------
    The rotateZ() CSS function defines a transformation that rotates an element around the z-axis without deforming it.
    Its result is a <transform-function> data type.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotateZ

    Attributes:
    ----------
    :param float r: Is an <angle> representing the angle of the rotation. A positive angle denotes a clockwise rotation,
    a negative angle a counter-clockwise one.
    :param str unit: The unit for the transformation (deg, turn, rad...)
    """
    return "%s.style.transform = 'rotateZ(%s%s)'" % (self.selector, r, unit)


class JsDomEffects:

  def __init__(self, page: primitives.PageModel, component: primitives.HtmlModel):
    self._effects = Effects.Effects(page)
    self.component = component

  def glow(self, color, radius=50, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite",
           direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param color:
    :param radius:
    :param duration:
    :param timing_fnc:
    :param delay:
    :param iteration_count:
    :param direction:
    :param fill_mode:
    """
    name = self._effects.glow(color, radius, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    return self.component.dom.css('animation', "%s %ss %s %ss %s %s %s" % (
      name, duration, timing_fnc, delay, iteration_count, direction, fill_mode))

  def blink(self, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate",
            fill_mode='forwards'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:
    :param timing_fnc:
    :param delay:
    :param iteration_count:
    :param direction:
    :param fill_mode:
    """
    name = self._effects.blink(duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    return self.component.dom.css('animation', "%s %ss %s %ss %s %s" % (
      name, duration, timing_fnc, delay, iteration_count, direction))

  def fade_out(self, duration=5, timing_fnc="ease-in-out", delay=0, iteration_count=1, direction="normal",
               fill_mode='forwards'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:
    :param timing_fnc:
    :param delay:
    :param iteration_count:
    :param direction:
    :param fill_mode:
    :return:
    """
    name = self._effects.fade_out(duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    return self.component.dom.css('animation', "%s %ss %s %ss %s %s" % (
      name, duration, timing_fnc, delay, iteration_count, direction))

  def fade_in(self, duration=5, timing_fnc="ease-in-out", delay=0, iteration_count=1, direction="normal",
              fill_mode='forwards'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:
    :param timing_fnc:
    :param delay:
    :param iteration_count:
    :param direction:
    :param fill_mode:
    """
    name = self._effects.fade_in(duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    return self.component.dom.css('animation', "%s %ss %s %ss %s %s %s" % (
      name, duration, timing_fnc, delay, iteration_count, direction, fill_mode))


class JsClassList:

  def __init__(self, js_code: str, component: primitives.HtmlModel = None):
    self.varId = js_code
    self.component = component

  @property
  def length(self):
    """
    Description:
    ------------
    Returns the number of classes in the list.

    Related Pages:

        https://www.w3schools.com/jsref/prop_element_classlist.asp
    """
    return JsNumber.JsNumber.get("%s.length" % self.varId)

  @property
  def style_select(self):
    """
    Get the style_select from the component options.
    """
    if self.component is None:
      raise ValueError("Cannot use select if select_style not defined for the component")

    return self.component.options.style_select

  def add(self, cls_names: Union[list, str]):
    """
    Description:
    ------------
    Adds one or more class names to an element.

    If the specified class already exist, the class will not be added.

    Related Pages:

        https://www.w3schools.com/jsref/prop_element_classlist.asp

    Attributes:
    ----------
    :param Union[list, str] cls_names: The class names.
    """
    if not hasattr(cls_names, 'toStr'):
      if not isinstance(cls_names, list):
        cls_names = [cls_names]
      cls_names = ", ".join([str(JsUtils.jsConvertData(c, None)) for c in cls_names])
    return JsObject.JsObject.get("%s.add(%s)" % (self.varId, cls_names))

  def contains(self, cls_name: str):
    """
    Description:
    ------------
    Returns a Boolean value, indicating whether an element has the specified class name.

    Possible values:

    true - the element contains the specified class name
    false - the element does not contain the specified class name

    Related Pages:

        https://www.w3schools.com/jsref/prop_element_classlist.asp

    Attributes:
    ----------
    :param str cls_name: The CSS classname.
    """
    cls_name = JsUtils.jsConvertData(cls_name, None)
    return JsBoolean.JsBoolean.get("%s.contains(%s)" % (self.varId, cls_name))

  def is_missing(self, cls_name: str):
    """
    Description:
    ------------
    Check if a CSS class is missing in the component classes definitions.

    Attributes:
    ----------
    :param str cls_name: The CSS classname.
    """
    cls_name = JsUtils.jsConvertData(cls_name, None)
    return JsBoolean.JsBoolean.get("!%s.contains(%s)" % (self.varId, cls_name))

  def item(self, index: int):
    """
    Description:
    ------------
    Returns the class name with a specified index number from an element. Index starts at 0.

    Returns null if the index is out of range

    Related Pages:

        https://www.w3schools.com/jsref/prop_element_classlist.asp

    Attributes:
    ----------
    :param int index: The index of the class.
    """
    return JsNumber.JsNumber.get("%s.item(%s)" % (self.varId, index))

  def items(self):
    """
    Description:
    ------------
    Return all the CSS classes for a given DOM object.
    """
    return JsNumber.JsNumber.get("%s" % self.varId)

  def remove(self, cls_names: Union[list, str]):
    """
    Description:
    ------------
    Removes one or more class names from an element.

    Note: Removing a class that does not exist, does NOT throw an error

    Related Pages:

        https://www.w3schools.com/jsref/prop_element_classlist.asp

    Attributes:
    ----------
    :param Union[list, str] cls_names: The class names.
    """
    if not hasattr(cls_names, 'toStr'):
      if not isinstance(cls_names, list):
        cls_names = [cls_names]
      cls_names = ", ".join([str(JsUtils.jsConvertData(c, None)) for c in cls_names])
    return JsObject.JsObject.get("%s.remove(%s)" % (self.varId, cls_names))

  def toggle(self, cls_name: Union[str, primitives.JsDataModel],
             flag: Union[bool, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Toggles between a class name for an element.

    The first parameter removes the specified class from an element, and returns false.
    If the class does not exist, it is added to the element, and the return value is true.

    The optional second parameter is a Boolean value that forces the class to be added or removed,
    regardless of whether or not it already existed. For example:

    Remove a class: element.classList.toggle("classToRemove", false);
    Add a class: element.classList.toggle("classToAdd", true);

    Related Pages:

        https://www.w3schools.com/jsref/prop_element_classlist.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] cls_name: The CSS classname.
    :param Union[bool, primitives.JsDataModel] flag: forces the class to be added or removed, regardless of
    whether or not it already existed.
    """
    cls_name = JsUtils.jsConvertData(cls_name, None)
    if flag is None:
      return JsObject.JsObject.get("%s.toggle(%s)" % (self.varId, cls_name))

    flag = JsUtils.jsConvertData(flag, None)
    return JsObject.JsObject.get("%s.toggle(%s, %s)" % (self.varId, cls_name, flag))

  def select(self, flag: bool = True):
    """
    Description:
    ------------
    Shortcut to add the predefined selected class for the component.
    This will add the internal predefined classname.

    Attributes:
    ----------
    :param bool flag: To specific if the select style need to be added or removed from the ClassList.
    """
    if self.component is None:
      raise ValueError("Cannot use select if select_style not defined for the component")

    if flag:
      return self.add(self.component.options.style_select)

    return self.remove(self.component.options.style_select)


class JsDoms(JsObject.JsObject):
  _id = None
  display_value = 'block'

  @classmethod
  def new(cls, tag_name: Union[str, primitives.JsDataModel] = None, js_code: str = None, is_py_data: bool = True,
          set_var: bool = True, page: primitives.PageModel = None):
    """
    Description:
    ------------
    Create a new dom object to be added to the HTML page

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_date.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] tag_name: The tag name to be created.
    :param str js_code: Optional,
    :param bool is_py_data: Optional,
    :param bool set_var: Optional,
    :param primitives.PageModel page: Optional,

    :return: The Python Javascript Date primitive
    """
    tag_name = JsUtils.jsConvertData(tag_name, None)
    return cls(
      data="document.createElement('%s')" % tag_name, js_code=js_code, set_var=set_var, is_py_data=is_py_data,
      page=page)

  @property
  def parentNode(self):
    """
    Description:
    ------------
    The parentNode property returns the parent node of the specified node, as a Node object.

    Note: In HTML, the document itself is the parent node of the HTML element, HEAD and BODY are child nodes of
    the HTML element.

    Related Pages:

      https://www.w3schools.com/jsref/prop_node_parentnode.asp
    """
    return JsDoms('', js_code="%s.parentNode" % self.toStr())

  def querySelector(self, tag: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Get element by tag.

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] tag: The DOM tag reference.
    """
    tag = JsUtils.jsConvertData(tag, None)
    return JsDoms("%s.querySelector(%s)" % (self.toStr(), tag))

  def querySelectorAll(self, tag: Union[str, primitives.JsDataModel], js_code: str = None):
    """
    Description:
    ------------
    The querySelectorAll() method returns all elements in the document that matches a specified CSS selector(s),
    as a static NodeList object.

    Related Pages:

      https://www.w3schools.com/jsref/met_document_queryselectorall.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] tag: The tag name.
    :param str js_code: The variable name on the javascript side.

    :return: A javascript Array object
    """
    tag = JsUtils.jsConvertData(tag, None)
    if js_code is None:
      return JsArray.JsArray("%s.querySelectorAll(%s)" % (self.toStr(), tag), is_py_data=False)

    return JsArray.JsArray(
      "%s.querySelectorAll(%s)" % (self.toStr(), tag), js_code=js_code, set_var=True, is_py_data=False)

  def empty(self):
    """
    Description:
    ------------
    Shortcut function to emtpy an HTML component.
    This will only reuse the innerHTML property
    """
    return JsObject.JsObject('%s.innerHTML = ""' % self.varId)

  @property
  def events(self) -> JsDomEvents:
    """
    Description:
    -----------
    Link to the events attached to a Javascript DOM object.

    :rtype: JsDomEvents
    """
    return JsDomEvents(self.page, js_code=self.varName)

  @property
  def effects(self):
    """
    Description:
    ------------
    Add CSS pre defined events from a dom object.
    """
    return JsDomEffects(self.page, self.component)

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
    return JsDomsTransforms(self.page, self.varId)

  @property
  def jquery(self):
    """
    Description:
    ------------
    Link to the Jquery package

    The id attribute must be defined
    """
    from epyk.core.js.packages import JsQuery

    if self._id is None:
      raise ValueError("Id must be defined to attach Jquery features to this object")

    if getattr(self, '_jq', None) is None:
      self._jq = JsQuery.JQuery(self.page, selector="jQuery('#%s')" % self._id, set_var=False)
    return self._jq

  def addEventListener(self, event: Union[str, primitives.JsDataModel], js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The addEventListener() method attaches an event handler to the specified element.

    Related Pages:

      https://www.w3schools.com/jsref/met_element_addeventlistener.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] event:
    :param Union[list, str] js_funcs: The Javascript functions
    """
    event = JsUtils.jsConvertData(event, None)
    self._js.append('addEventListener(%s, function(){%s})' % (event, ";".join(JsUtils.jsConvertFncs(js_funcs))))
    return self

  def dispatchEvent(self, event: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Dispatches an Event at the specified EventTarget, (synchronously) invoking the affected EventListeners in
    the appropriate order.
    The normal event processing rules (including the capturing and optional bubbling phase) also apply to events
    dispatched manually with dispatchEvent().

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] event: event is the Event object to be dispatched.
    """
    event = JsUtils.jsConvertData(event, None)
    self._js.append('dispatchEvent(%s)' % event)
    return self

  def addOnReady(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    The ready event occurs when the DOM (document object model) has been loaded.

    Related Pages:

      https://www.w3schools.com/jquery/event_ready.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions
    """
    self.page._props.setdefault('js', {}).setdefault(
      'onCompReady', {})[self.varId] = ";".join(JsUtils.jsConvertFncs(js_funcs))

  def innerText(self, text: Union[str, primitives.JsDataModel] = None, append: bool = False, val_type=None):
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
    :param Union[str, primitives.JsDataModel] text: Optional, The Javascript String to be added.
    :param append: Boolean. Mention if the component should replace or append the data.
    :param val_type: The type of data expected in the component.

    :return: The JsObj to allow the chaining
    """
    if text is None:
      return JsString.JsString("%s.innerText" % self.varId, is_py_data=False)

    if append:
      if val_type == int:
        self._js.append("%s.innerText = parseInt(%s.innerText) + %s" % (
          self.varId, self.varId, JsUtils.jsConvertData(text, None)))
      elif val_type == float:
        self._js.append("%s.innerText = parseFloat(%s.innerText) + %s" % (
          self.varId, self.varId, JsUtils.jsConvertData(text, None)))
      else:
        self._js.append("%s.innerText += %s" % (self.varId, JsUtils.jsConvertData(text, None)))
    else:
      self._js.append("%s.innerText = %s" % (self.varId, JsUtils.jsConvertData(text, None)))
    return self

  def textContent(self, text: Union[str, primitives.JsDataModel] = None, append: bool = False, val_type=None):
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
    :param Union[str, primitives.JsDataModel] text: Optional, The Javascript String to be added.
    :param append: Boolean. Mention if the component should replace or append the data.
    :param val_type: Type: The type of data expected in the component.

    :return: The JsObj to allow the chaining
    """
    if text is None:
      return JsString.JsString("%s.textContent" % self.varId, is_py_data=False)

    if append:
      if val_type == int:
        self._js.append("%s.textContent = parseInt(%s.textContent) + %s" % (
        self.varId, self.varId, JsUtils.jsConvertData(text, None)))
      elif val_type == float:
        self._js.append("%s.textContent = parseFloat(%s.textContent) + %s" % (
        self.varId, self.varId, JsUtils.jsConvertData(text, None)))
      else:
        self._js.append("%s.textContent += %s" % (self.varId, JsUtils.jsConvertData(text, None)))
    else:
      self._js.append("%s.textContent = %s" % (self.varId, JsUtils.jsConvertData(text, None)))
    return self

  def innerHTML(self, text: Union[str, primitives.JsDataModel] = None, append: bool = False, val_type=None):
    """
    Description:
    ------------
    Sets or returns the content of an element.

    Usage::

      select.label.dom.innerHTML("<p style='color:red'>Changed !</p>")
      page.js.console.log(tabs.dom[2].innerText())

    Related Pages:

      https://www.w3schools.com/jsref/prop_html_innerhtml.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] text: Optional, The Javascript String to be added.
    :param append: Boolean. Mention if the component should replace or append the data.
    :param val_type: Type: The type of data expected in the component.

    :return: self to allow the chaining
    """
    if text is None:
      return JsString.JsString("%s.innerHTML" % self.varId, is_py_data=False)

    if append:
      if val_type == int:
        self._js.append("%s.innerHTML = parseInt(%s.innerHTML) + %s" % (
          self.varId, self.varId, JsUtils.jsConvertData(text, None)))
      elif val_type == int:
        self._js.append("%s.innerHTML = parseFloat(%s.innerHTML) + %s" % (
          self.varId, self.varId, JsUtils.jsConvertData(text, None)))
      else:
        self._js.append("%s.innerHTML += %s" % (self.varId, JsUtils.jsConvertData(text, None)))
    else:
      self._js.append("%s.innerHTML = %s" % (self.varId, JsUtils.jsConvertData(text, None)))
    return self

  def outerText(self, text: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    The outerText property sets or returns the text content of the specified node.

    Related Pages:

      https://www.w3schools.com/jsref/prop_node_outertext.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] text: Optional, The Javascript String to be set.

    :return: self to allow the chaining
    """
    if text is None:
      return JsString.JsString("%s.outerText" % self.varId, is_py_data=False)

    self._js.append("%s.outerText = %s" % (self.varId, JsUtils.jsConvertData(text, None)))
    return self

  def outerHTML(self, text: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    The outerHTML property sets or returns the HTML element and all it's content, including the start tag,
    it's attributes, and the end tag.

    Related Pages:

      https://www.w3schools.com/jsref/prop_html_outerhtml.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] text: Optional, The Javascript String to be set.

    :return: self to allow the chaining
    """
    if text is None:
      return JsString.JsString("%s.outerHTML" % self.varId, is_py_data=False)

    self._js.append("%s.outerHTML = %s" % (self.varId, JsUtils.jsConvertData(text, None)))
    return self

  def value(self, text: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    The value attribute specifies the value of an <input> element.

    Related Pages:

      https://www.w3schools.com/tags/att_input_value.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] text: Optional. Set the input value.
    """
    if text is None:
      return JsString.JsString("%s.value" % self.varId, is_py_data=False)

    self._js.append("%s.value = %s" % (self.varId, JsUtils.jsConvertData(text, None)))
    return self

  def nodeValue(self, text: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    The nodeValue property sets or returns the node value of the specified node.

    If the node is an element node, the nodeValue property will return null.

    Related Pages:

      https://www.w3schools.com/jsref/prop_node_nodevalue.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] text: Optional. Set the node value.
    """
    if text is None:
      return JsString.JsString("%s.nodeValue" % self.varId, is_py_data=False)

    self._js.append("%s.nodeValue = %s" % (self.varId, JsUtils.jsConvertData(text, None)))
    return self

  def attr(self, value: Union[dict, str, primitives.JsDataModel],
           data: Union[str, bool, float, primitives.JsDataModel] = None):
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
    :param Union[str, primitives.JsDataModel] value: A String with the type of parameter or a python dictionary.
    :param Union[str, primitives.JsDataModel] data: A JsObj with the value to be set.

    :return: A JsObj
    """
    if data is None:
      if isinstance(value, dict):
        for k, v in value.items():
          if k == "id":
            self._id = v
          self._js.append("%s.setAttribute('%s', %s)" % (self.varId, k, JsUtils.jsConvertData(v, None)))
      else:
        value = JsUtils.jsConvertData(value, None)
        return JsObject.JsObject("%s.getAttribute(%s)" % (self.varId, value))

    else:
      if value == "id":
        self._id = data
      value = JsUtils.jsConvertData(value, None)
      self._js.append("%s.setAttribute(%s, %s)" % (self.varId, value, JsUtils.jsConvertData(data, None)))
    return self

  def setAttribute(self, attribute_name: Union[str, primitives.JsDataModel],
                   attribute_value: Union[str, bool, float, primitives.JsDataModel]):
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
    :param Union[str, primitives.JsDataModel] attribute_name: The name of the attribute you want to add.
    :param Union[str, bool, primitives.JsDataModel] attribute_value: The value of the attribute you want to add.
    """
    attribute_name = JsUtils.jsConvertData(attribute_name, None)
    self._js.append("%s.setAttribute(%s, %s)" % (
      self.varId, attribute_name, JsUtils.jsConvertData(attribute_value, None)))
    return self

  def addClass(self, cls_name: str, attrs: dict = None, event_attrs: dict = None, extend: bool = True):
    """
    Description:
    -----------
    Adds the specified class(es) to each element in the set of matched elements.

    This function can either use an existing class or create one if the attrs or eventAttrs are defined.

    Usage::

      table.dom.addClass("red", {"border": "1px solid green"}, extend=False)

    Related Pages:

      https://www.w3schools.com/jsref/met_element_setattribute.asp

    Attributes:
    ----------
    :param str cls_name: The Css classname.
    :param dict attrs: A python dictionary with the css attributes.
    :param dict event_attrs: A nested python dictionary with the css attributes for each event.
    :param bool extend: To set if the class should replace the existing style definition.
    """
    if attrs is not None or event_attrs is not None:
      cls_name = self.page.style.cssName(cls_name)
      self.page.style.cssCls(cls_name, attrs, event_attrs, False)
    if extend:
      self._js.append('%s.setAttribute("class", %s.getAttribute("class") + " %s")' % (self.varId, self.varId, cls_name))
    else:
      self._js.append('%s.setAttribute("class", "%s")' % (self.varId, cls_name))
    return self

  def removeClass(self, cls_name: Union[str, primitives.JsDataModel]):
    """
    Description:
    -----------
    Remove a class from the defined classes of the DOM element

    Related Pages:

      https://www.w3schools.com/howto/howto_js_remove_class.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] cls_name: String. Required. The classname.
    """
    cls_name = JsUtils.jsConvertData(cls_name, None)
    self._js.append('%s.classList.remove(%s)' % (self.varId, cls_name))
    return self

  @property
  def classList(self):
    """
    Description:
    -----------
    The classList property returns the class name(s) of an element, as a DOMTokenList object.

    Related Pages:

      https://www.w3schools.com/jsref/prop_element_classlist.asp
    """
    return JsClassList("%s.classList" % self.varId, self.component)

  def css(self, attr: Union[dict, str], data: Union[str, primitives.JsDataModel] = None, duration: int = None):
    """
    Description:
    -----------
    Replicate in plain Js the Jquery CSS function.

    Usage::

      select.label.dom.css({"color": "red"})

    Related Pages:

      https://www.w3schools.com/jsref/met_element_setattribute.asp

    Attributes:
    ----------
    :param Union[dict, str] attr: A String with the type of parameter or a python dictionary
    :param Union[str, primitives.JsDataModel] data: A JsObj with the value to be set
    :param int duration: Integer

    :return: A JsObj
    """
    if data is None and isinstance(attr, dict):
      for k, v in attr.items():
        if "-" in k:
          split_css = k.split("-")
          k = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
        self._js.append("%s.style.%s = %s" % (self.varId, k, JsUtils.jsConvertData(v, None)))
    elif data is None:
      if "-" in attr:
        split_css = attr.split("-")
        attr = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
      return JsObject.JsObject("%s.style.%s" % (self.varId, attr))

    else:
      if "-" in attr:
        split_css = attr.split("-")
        attr = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
      self._js.append("%s.style.%s = %s" % (self.varId, attr, JsUtils.jsConvertData(data, None)))
    return self

  def position(self, x: int = None, y: int = None, dx: int = 0, dy: int = 0):
    """
    Description:
    -----------
    Set the position of the component in the page.
    By default the component will be fixed at the mouse level (this should be used in an event).

    Usage::

      page.js.createElement("div", "popup").innerHTML("uygk,k,kj..kj.kjyf").attr('id', 'popup').css({
        'color': 'red', 'display': 'block'}).position()

    Attributes:
    ----------
    :param int x: The position from the top of the page
    :param int y: The position from the left
    :param int dx:
    :param int dy:

    :return: A JsObj
    """
    if x is None and y is None:
      self.css({
        "position": 'absolute',
        'top': JsObject.JsObject.get("(event.clientY + window.scrollY + %s) + 'px'" % dy),
        'left': JsObject.JsObject.get("(event.clientX + window.scrollX + %s) + 'px'" % dx)})
    else:
      self.css({"position": 'absolute', 'top': "%spx" % x or 0, 'left': "%spx" % x or 0})
    return self

  def toggle_transition(self, attribute, value, value2, duration: int = 1,
                        timing_func: str = 'ease', delay: float = None):
    """
    Description:
    ------------
    Toggle a transition.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_transition.asp

    Attributes:
    ----------
    :param attribute: String or List. Specifies the name of the CSS property the transition effect is for
    :param value: String or List. Specifies the value of the CSS property the transition effect is for
    :param value2: String or List. Specifies the value of the CSS property the transition effect is for
    :param duration: Number or List. Specifies how many seconds or milliseconds the transition effect takes to complete
    :param delay: Number. Defines when the transition effect will start
    :param timing_func: String. The transition-timing-function property specifies the speed curve of the transition effect.
    """
    if "-" in attribute:
      split_css = attribute.split("-")
      css_attr = "%s%s" % (split_css[0], split_css[1].title())
    else:
      css_attr = attribute
    tmp = list(self._js)
    self._js = []
    self.transition(attribute, value, duration, delay, timing_func)
    if_ = "; ".join(self._js)

    self._js = []
    self.transition(attribute, value2, duration, delay, timing_func)
    else_ = "; ".join(self._js)
    self._js = tmp
    self._js.append("if(%s.style.%s != '%s') {%s} else {%s}" % (self.varId, css_attr, value, if_, else_))
    return self

  def transition(self, attribute: Union[str, list], value: Optional[Union[str, list, primitives.JsDataModel]],
                 duration: Union[float, List[float]] = 1, delay: int = None, timing_fnc: str = 'ease',
                 reverse: bool = False):
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

  def invisible(self):
    """
    Description:
    ------------
    Component not visible by setting the CSS property visibility to hidden.

    Usage:

      input.dom.invisible()
    """
    return self.css("visibility", "hidden")

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

  def show(self, display_value: str = None, duration: int = None):
    """
    Description:
    ------------

    Usage::

      input.js.hide()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    Attributes:
    ----------
    :param display_value:
    :param duration:
    """
    self.css("display", display_value or self.display_value)
    if duration is not None:
      self._js.append("setTimeout(function(){%s.style.display = 'none'}, %s)" % (self.varId, duration * 1000))
    return self

  def toggle(self, attr: str = "display", val_1: str = None, val_2: str = "none"):
    """
    Description:
    ------------
    Hexadecimal colors should be converted to rgb code as only the computed style will be compared.
    To do so you can use: Colors.getHexToRgb(self._report.theme.success[1]) from epyk.core.css import Colors

    Attributes:
    ----------
    :param str attr:
    :param str val_1:
    :param str val_2:
    """
    if attr == 'display' and val_1 is None:
      val_1 = self.display_value
    if "-" in attr:
      split_css = attr.split("-")
      attr = "%s%s" % (split_css[0], split_css[1].title())
    self._js.append("if(window.getComputedStyle(%(varId)s).%(attr)s == '%(jsVal1)s'){ %(varId)s.style.%(attr)s = '%(jsVal2)s'} else { %(varId)s.style.%(attr)s = '%(jsVal1)s'}" % {
      "varId": self.varId, "attr": attr, "jsVal1": val_1, "jsVal2": val_2})
    return self

  def toggleAttrs(self, pivot_key, pivot_val, attrs_off: dict, attrs_on: dict):
    """
    Description:
    ------------
    Toggle some CSS attributes

    Attributes:
    ----------
    :param pivot_key:
    :param pivot_val:
    :param dict attrs_on: A python dictionary with CSS attributes
    :param dict attrs_off: A python dictionary with CSS attributes
    """
    if pivot_key in ["color"] and not pivot_val.startswith("rgb"):
      colors_def = Colors.defined[pivot_val.upper()]
      pivot_val = "rgb%s" % colors_def['rgb']
    css_attrs_on = self.css(attrs_on).toStr()
    css_attrs_off = self.css(attrs_off).toStr()
    self._js.append("if(window.getComputedStyle(%(varId)s)['%(pivot_key)s'] == '%(pivot_val)s') {%(css_attrs_on)s} else {%(css_attrs_off)s}" % {"pivot_val": pivot_val, "varId": self.varId, "pivot_key": pivot_key, 'css_attrs_on': css_attrs_on, 'css_attrs_off': css_attrs_off})
    return self

  def toggleText(self, string_1: Union[str, primitives.JsDataModel], string_2: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Toggle (change) the content of the HTML component

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] string_1: String. The content
    :param Union[str, primitives.JsDataModel] string_2: String. The new content
    """
    str1 = JsUtils.jsConvertData(string_1, None)
    str2 = JsUtils.jsConvertData(string_2, None)
    self._js.append("if(%(varId)s.innerText == %(str2)s) {%(varId)s.innerText = %(str1)s} else {%(varId)s.innerText = %(str2)s}" % {"varId": self.varId, "str1": str1, "str2": str2})
    return self

  @property
  def clientHeight(self):
    """
    Description:
    ------------
    The Element.clientHeight read-only property is zero for elements with no CSS or inline layout boxes; otherwise,
    it's the inner height of an element in pixels.
    It includes padding but excludes borders, margins, and horizontal scrollbars (if present).

    Usage::

      rptObj.js.alert(rptObj.js.body.clientHeight)

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Element/clientHeight
    """
    return JsNumber.JsNumber("%s.clientHeight" % self.varId)

  def toggleClass(self, cls_name: Union[str, primitives.JsDataModel], propagate: bool = False):
    """
    Description:
    ------------
    Toggle a class name

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] cls_name: The classname to be toggled.
    :param propagate: Boolean. Optional.
    """
    cls_name = JsUtils.jsConvertData(cls_name, None)
    if propagate:
      self._js.append('%(varId)s.parentNode.childNodes.forEach(function(e){e.classList.remove(%(data)s)})' % {
        "varId": self.varId, 'data': cls_name})
    self._js.append('var classes = %(data)s.split(" "); classes.forEach(function(cls){ %(varId)s.classList.toggle(cls); })' % {
      "varId": self.varId, 'data': cls_name})
    return self

  def switchClass(self, cls_name_1: Union[str, primitives.JsDataModel], cls_name_2: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Switch from one CSS class to another.

    Usage::

      icon.dom.switchClass("fa-folder", "fa-folder-open")

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] cls_name_1: A class name or a string with a list of classname space
    separated.
    :param Union[str, primitives.JsDataModel] cls_name_2: A class name or a string with a list of classname space
    separated.

    :return: Self to allow the chaining
    """
    self.toggleClass(cls_name_1)
    self.toggleClass(cls_name_2)
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
    return JsDoms('', js_code="%s.firstChild" % self.varId)

  def child(self, i: int):
    """
    Description:
    ------------
    Returns the requested child DOM object on the JavaScript side.

    Attributes:
    ----------
    :param int i: The position of the child.
    """
    return JsDoms("%s.childNodes[%s]" % (self.varId, i))

  @property
  def nextSibling(self):
    """
    Description:
    ------------
    The nextSibling property returns the node immediately following the specified node, in the same tree level.

    Related Pages:

      https://www.w3schools.com/jsref/prop_node_nextsibling.asp
    """
    return JsDoms('', js_code="%s.nextSibling" % self.varId)

  def contains(self, node: str):
    """
    Description:
    ------------
    The contains() method returns a Boolean value indicating whether a node is a descendant of a specified node.

    Related Pages:

      https://www.w3schools.com/jsref/met_node_contains.asp

    Attributes:
    ----------
    :param str node: Specifies the node that may be contained by (a descendant of) a specified node.

    :return: A Boolean
    """
    return JsBoolean.JsBoolean('%s.contains(%s)' % (self.varId, node))

  def getAttribute(self, attribute_name: Union[str, primitives.JsDataModel]):
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
    :param Union[str, primitives.JsDataModel] attribute_name: The name of the attribute you want to get the value from

    :return: A String, representing the specified attribute's value.
    """
    return JsObject.JsObject(
      "%s.getAttribute(%s)" % (self.varId, JsUtils.jsConvertData(attribute_name, None)), is_py_data=False)

  def getAttributeNode(self, attribute_name: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    The getAttributeNode() method returns the attribute node with the specified name of an element, as an Attr object.

    Related Pages:

      https://www.w3schools.com/jsref/met_element_getattributenode.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] attribute_name: The name of the attribute you want to return.

    :return: An Attr object, representing the specified attribute node.
    """
    attribute_name = JsUtils.jsConvertData(attribute_name, None)
    return JsString.JsString("%s.getAttributeNode(%s)" % (self.varId, attribute_name))

  def getComputedStyle(self, attribute_name: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] attribute_name: String. Optional.
    """
    if attribute_name is None:
      return JsString.JsString("getComputedStyle(%s)" % self.varId, is_py_data=False)

    if "-" in attribute_name:
      split_css = attribute_name.split("-")
      attribute_name = "%s%s" % (split_css[0], split_css[1].title())
    return JsString.JsString("getComputedStyle(%s).%s" % (self.varId, attribute_name), is_py_data=False)

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
    return JsBoolean.JsBoolean("%s.hasChildNodes()" % self.varId, is_py_data=False)

  def hasClass(self, cls_name: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] cls_name:
    """
    cls_name = JsUtils.jsConvertData(cls_name, None)
    return JsBoolean.JsBoolean("%s.classList.contains(%s)" % (self.varId, cls_name), is_py_data=False)

  def text(self, value: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Javascript Function

    Shortcut in charge oa creating a text node object and adding the text.

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] value: The Javascript String of the text node component.

    :return: The main Python Dom Object
    """
    return self.appendChild(JsFncs.JsFunction("document.createTextNode(%s)" % JsUtils.jsConvertData(value, None)))

  @property
  def childNodes(self):
    """
    Description:
    ------------
    The childNodes property returns a collection of a node's child nodes, as a NodeList object.

    The nodes in the collection are sorted as they appear in the source code and can be accessed by index numbers.
    The index starts at 0.

    Related Pages:

      https://www.w3schools.com/jsref/prop_node_childnodes.asp

    :return: A NodeList object, representing a collection of nodes. The nodes in the returned collection are sorted as
    they appear in the source code
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
    return JsString.JsString("%s.tagName" % self.varId, is_py_data=False)

  @property
  def offsetTop(self):
    """
    Description:
    ------------
    The HTMLElement.offsetTop read-only property returns the distance of the current element relative to the top of
    the offsetParent node.

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/API/HTMLElement/offsetTop
    """
    return JsString.JsString("%s.offsetTop" % self.varId, is_py_data=False)

  def contentEditable(self, flag: Union[bool, primitives.JsDataModel]):
    """
    Description:
    ------------
    Set content editable

    Usage::

      rptObj.ui.text("This is a text").dom.contentEditable(True)

    Attributes:
    ----------
    :param Union[bool, primitives.JsDataModel] flag: Set the content editable flag to the Dom object

    :return: Return a JsBoolean object
    """
    return JsBoolean.JsBoolean.get("%s.contentEditable = %s" % (self.varId, JsUtils.jsConvertData(flag, None)))

  def className(self, cls_name: Union[str, primitives.JsDataModel] = None):
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
    :param Union[str, primitives.JsDataModel] cls_name: Specifies the class name of an element. To apply multiple classes, separate them with
    spaces, like "test demo"

    :return: A String, representing the class, or a space-separated list of classes, of an element
    """
    if cls_name is None:
      return JsString.JsString("%s.className" % self.varId, is_py_data=False)

    # TODO fix this properly
    return JsString.JsString("%s; %s.className = %s" % (
      self.toStr(), self.varId, JsUtils.jsConvertData(cls_name, None)), is_py_data=False)

  def cloneNode(self, deep: Union[bool, primitives.JsDataModel] = True):
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
    :param Union[bool, primitives.JsDataModel] deep: Optional. Specifies whether all descendants of the node should be
    cloned.

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

  def removeAttribute(self, dom: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    The removeAttribute() method removes the specified attribute from an element.

    Related Pages:

      https://www.w3schools.com/jsref/met_element_removeattribute.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] dom: The name of the attribute you want to remove.
    """
    self._js.append("%s.removeAttribute(%s)" % (self.varId, JsUtils.jsConvertData(dom, None)))
    return self

  def removeChild(self, dom: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Removes a child node from an element.

    Related Pages:

      https://www.w3schools.com/jsref/met_node_removechild.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] dom: The node object you want to remove.

    :return: A Node object, representing the removed node, or null if the node does not exist.
    """
    return JsDoms("%s.removeChild(%s)" % (self.varId, dom))

  def appendChild(self, dom: Union[str, primitives.JsDataModel]):
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
    :param Union[str, primitives.JsDataModel] dom: The node object you want to append.

    :return: 	A Node Object, representing the appended node
    """
    self._js.append("%s.appendChild(%s)" % (self.varId, JsUtils.jsConvertData(dom, None)))
    return self

  def insertBefore(self, new_node, existing_node=None):
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
    :param new_node: The node object you want to insert
    :param existing_node: Optional. The child node you want to insert the new node before. If set to null,
    the insertBefore method will insert the new_node at the end
    """
    if existing_node is None:
      self._js.append("%s.insertBefore(%s, %s)" % (self.varId, new_node, self.firstChild))
    else:
      self._js.append("%s.insertBefore(%s, %s)" % (self.varId, new_node, existing_node))
    return self

  def click(self, js_funcs: Union[str, list] = None):
    """
    Description:
    -----------
    Trigger a click event.
    This function will not set the event

    Attributes:
    ----------
    :param Union[str, list] js_funcs: The Javascript functions.
    """
    if js_funcs is None:
      return JsObject.JsObject("%s.click()" % self.varId)

    self._js.append("%s.click(%s)" % (self.varId, JsUtils.jsConvertFncs(js_funcs, toStr=True)))
    return self

  def onclick(self, js_funcs: Union[str, list], auto_style: bool = True):
    """
    Description:
    -----------
    Execute a JavaScript when a button is clicked

    Related Pages:

      https://www.w3schools.com/jsref/event_onclick.asp

    Attributes:
    ----------
    :param Union[str, list] js_funcs: Required. The Javascript function.
    :param bool auto_style: Optional. Some predefined style attributes added to this event
    (self.css({"cursor": "pointer"}))

    :return: The PyDom object
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    if auto_style:
      self.css({"cursor": "pointer"})
    self._js.append("%s.onclick = function(){%s}" % (self.varId, JsUtils.jsConvertFncs(js_funcs, toStr=True)))
    return self

  def onVisible(self, js_funcs: Union[str, list]):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param js_funcs: String or List. The Javascript functions
    """
    self._js.append("var rect = %s.getBoundingClientRect()" % self.varId)
    return self

  def getContext(self, context_type: str, context_attributes: Union[dict, primitives.JsDataModel] = None):
    """
    Description:
    ------------
    Function dedicated to DOM Canvas types.

    The HTMLCanvasElement.getContext() method returns a drawing context on the canvas,
    or null if the context identifier is not supported.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext

    Attributes:
    ----------
    :param str context_type: Is a DOMString containing the context identifier defining the drawing context associated to the canvas
    :param Union[dict, primitives.JsDataModel] context_attributes: Dictionary with specific context attributes (depending on the type

    TODO: Add a check on the tag
    """
    types = ["2d", "webgl", "experimental-webgl", "webgl2", "bitmaprenderer"]
    if context_type not in types:
      raise ValueError("Context type %s not recognised" % context_type)

    if context_attributes is None:
      return JsFncs.JsFunction("%s.getContext('%s')" % (self.varId, context_type))

    context_attributes = JsUtils.jsConvertData(context_attributes, None)
    return JsFncs.JsFunction("%s.getContext('%s', %s)" % (self.varId, context_type, context_attributes))

  def custom(self, frg: str):
    """
    Description:
    ------------
    Bespoke function to be called from the dom element.

    This can be use if a function is missing from the wrapper interface.

    Attributes:
    ----------
    :param str frg: The DOM feature.
    """
    return JsObject.JsObject("%s.%s" % (self.varId, frg))


class JsDomsList(JsArray.JsArray):

  def all(self, js_funcs: Union[str, list]):
    """
    Description:
    ------------
    Apply a set of functions on all the elements with this name.

    Attributes:
    ----------
    :param Union[str, list] js_funcs: List of Javascript fragments.
    """
    self._js.append("%s.forEach(function(elt, index){%s})" % (self.varId, JsUtils.jsConvertFncs(js_funcs, toStr=True)))
    return self

  @property
  def first(self):
    """
    Description:
    ------------
    Get the first dom item in corresponding to the name criteria
    """
    return JsDoms.get("%s[0]" % self.toStr())

  def css(self, attr: Union[str, dict], data: Union[dict, str, primitives.JsDataModel] = None):
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
    :param Union[str, dict] attr: A String with the type of parameter or a python dictionary
    :param Union[dict, str, primitives.JsDataModel] data: A JsObj with the value to be set

    :return: A JsObj
    """
    if data is None and isinstance(attr, dict):
      for k, v in attr.items():
        if "-" in k:
          split_css = k.split("-")
          k = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
        self._js.append("for(let e of %s){ e.style.%s = %s }" % (self.varId, k, JsUtils.jsConvertData(v, None)))
    elif data is None:
      if "-" in attr:
        split_css = attr.split("-")
        attr = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
      return JsObject.JsObject("for(let e of %s){ e.style.%s }" % (self.varId, attr))
    else:
      if "-" in attr:
        split_css = attr.split("-")
        attr = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
      self._js.append("for(let e of %s){ e.style.%s = %s }" % (self.varId, attr, JsUtils.jsConvertData(data, None)))
    return self

  def log(self):
    """
    Description:
    ------------
    Add a print to the loop to assist on the implementation
    """
    self._js.append("for(let e of %s){ console.log(e) }" % self.varId)
    return self

  def attr(self, value: Union[str, dict], data: Union[dict, str, bool, primitives.JsDataModel] = None):
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
    :param Union[str, dict] value: A String with the type of parameter or a python dictionary.
    :param Union[dict, str, primitives.JsDataModel] data: A JsObj with the value to be set.
    """
    if data is None and isinstance(value, dict):
      for k, v in value.items():
        if k == "id":
          self._id = v
        self._js.append("for(let e of %s){ e.setAttribute('%s', %s) }" % (
          self.varId, k, JsUtils.jsConvertData(v, None)))
    else:
      if value == "id":
        self._id = data
      self._js.append("for(let e of %s){ e.setAttribute('%s', %s) }" % (
        self.varId, value, JsUtils.jsConvertData(data, None)))
    return self

  def __getitem__(self, index: int):
    """
    Description:
    ------------
    Get the nth item corresponding to the name in the HTML page.

    Attributes:
    ----------
    :param int index: The index number of the item.
    """
    return JsDoms.get("%s[%s]" % (self.toStr(), index))
