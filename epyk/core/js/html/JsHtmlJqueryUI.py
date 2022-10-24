#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, List
from epyk.core.py import primitives

from epyk.core.js.html import JsHtml
from epyk.core.js.fncs import JsFncs
from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsObjects


class JsHtmlDatePicker(JsHtml.JsHtml):

  @property
  def val(self):
    """

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.val(), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.component.dom.jquery.varId))

  @property
  def content(self):
    """

    """
    return JsHtml.ContentFormatters(self.page, '%s.val()' % self.component.dom.jquery.varId)

  def empty(self):
    """

    :return:
    """
    return JsUtils.jsWrap("%s.val('')" % self.component.dom.jquery.varId)


class JsHtmlDateFieldPicker(JsHtml.JsHtml):

  @property
  def val(self):
    """

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.val, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.content.toStr()))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """

    """
    return JsHtml.ContentFormatters(self.page, '%s.val()' % self.component.input.dom.jquery.varId)

  def empty(self):
    """

    :return:
    """
    return JsUtils.jsWrap("%s.val('')" % self.component.input.dom.jquery.varId)


class JsHtmlProgressBar(JsHtml.JsHtml):

  @property
  def val(self):
    """

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.progressbar('value'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.component.dom.jquery.varId))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """

    """
    return JsHtml.ContentFormatters(self.page, '%s.progressbar("value")' % self.component.dom.jquery.varId)

  def to(self, number: int, timer: int = 10):
    """
 
    :param int number:
    :param int timer: Optional. the speed of the increase in millisecond.
    """
    return JsUtils.jsConvertFncs([
      self.page.js.objects.number(self.content.unformat(), js_code="%s_counter" % self.htmlCode, set_var=True),
      self.page.js.window.setInterval([
        self.page.js.if_(
          self.page.js.objects.number.get("window.%s_counter" % self.htmlCode) < number, [
            self.page.js.objects.number(
              self.page.js.objects.number.get("window.%s_counter" % self.htmlCode) + 1,
              js_code="window.%s_counter" % self.htmlCode, set_var=True),
            self.component.build(self.page.js.objects.number.get("window.%s_counter" % self.htmlCode))
          ]).else_(self.page.js.window.clearInterval("%s_interval" % self.htmlCode))
      ], "%s_interval" % self.htmlCode, timer)
    ], toStr=True)

  def position(self, val, js_funcs: Union[List[Union[str, primitives.JsDataModel]], str]):
    """
 
    :param val:
    :param Union[List[Union[str, primitives.JsDataModel]], str] js_funcs: Javascript functions.
    """
    return JsFncs.JsFunction("if((%(content)s >= %(val)s) && (%(content)s <= %(val)s + 10)){%(fnc)s}" % {
      'content': self.content, 'val': val, 'fnc': JsUtils.jsConvertFncs(js_funcs, toStr=True)})

  def max(self, js_funcs: Union[List[Union[str, primitives.JsDataModel]], str]):
    """
 
    :param Union[List[Union[str, primitives.JsDataModel]], str] js_funcs: Javascript functions.
    """
    return self.position(self.component.options.max, js_funcs)

  def empty(self):
    """ Empty the progress bar with the min value.
    """
    return JsUtils.jsWrap('%s.progressbar("value", %s)' % (self.component.dom.jquery.varId, self.component.options.min))


class JsHtmlTimePicker(JsHtml.JsHtml):

  @property
  def val(self) -> JsObjects.JsObject.JsObject:
    """

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.val(), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.component.dom.jquery.varId))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """

    """
    return JsHtml.ContentFormatters(self.page, '%s.val()' % self.component.dom.jquery.varId)

  def hide(self):
    """   Close the timepicker dropdown.

    Usage::

      input.js.hide()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/
    """
    return JsObjects.JsObjects.get("%s.timepicker('hide')" % self.component.dom.jquery.varId)

  def show(self) -> JsObjects.JsObject.JsObject:
    """   Display the timepicker dropdown.

    Usage::

      input.js.hide()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/
    """
    return JsObjects.JsObjects.get("%s.timepicker('show')" % self.component.dom.jquery.varId)

  def empty(self):
    return JsUtils.jsWrap("%s.val('')" % self.component.dom.jquery.varId)


class JsHtmlSlider(JsHtml.JsHtml):

  @property
  def val(self) -> JsObjects.JsObject.JsObject:
    """

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.slider('value'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.component.dom.jquery.varId))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """

    """
    if self.component.options.range:
      if self.component.options.range == "min":
        return JsHtml.ContentFormatters(
          self.page, '[%(varId)s.slider("value"), %(varId)s.slider("option", "max")]' % {
            "varId": self.component.dom.jquery.varId})

      if self.component.options.range == "max":
        return JsHtml.ContentFormatters(
          self.page, '[%(varId)s.slider("option", "min"), %(varId)s.slider("value")]' % {
            "varId": self.component.dom.jquery.varId})

      return JsHtml.ContentFormatters(self.page, '%s.slider("values")' % self.component.dom.jquery.varId)

    return JsHtml.ContentFormatters(self.page, '%s.slider("value")' % self.component.dom.jquery.varId)

  @property
  def max_select(self) -> JsHtml.ContentFormatters:
    """
    Get the maximum value selected for range slider, returns the value otherwise.
    """
    if self.component.options.range:
      if self.component.options.range == "max":
        return JsHtml.ContentFormatters(self.page, '%s.slider("option", "max")' % self.component.dom.jquery.varId)

      if self.component.options.range == "min":
        return JsHtml.ContentFormatters(self.page, '%s.slider("value")' % self.component.dom.jquery.varId)

      return JsHtml.ContentFormatters(self.page, '%s.slider("values")[1]' % self.component.dom.jquery.varId)

    return self.content

  @property
  def min_select(self) -> JsHtml.ContentFormatters:
    """
    Get the minimum value selected for range slider, returns the value otherwise.
    """
    if self.component.options.range:
      if self.component.options.range == "min":
        return JsHtml.ContentFormatters(self.page, '%s.slider("option", "min")' % self.component.dom.jquery.varId)

      if self.component.options.range == "max":
        return JsHtml.ContentFormatters(self.page, '%s.slider("value")' % self.component.dom.jquery.varId)

      return JsHtml.ContentFormatters(self.page, '%s.slider("values")[0]' % self.component.dom.jquery.varId)

    return self.content

  @property
  def upper_bound(self) -> JsHtml.ContentFormatters:
    """

    """
    if self.component.options.range:
      return JsHtml.ContentFormatters(self.page, '%s.slider("option", "max")' % self.component.dom.jquery.varId)

    return self.content

  @property
  def lower_bound(self) -> JsHtml.ContentFormatters:
    """

    """
    if self.component.options.range:
      return JsHtml.ContentFormatters(self.page, '%s.slider("option", "min")' % self.component.dom.jquery.varId)

    return self.content


class JsHtmlSliderRange(JsHtml.JsHtml):

  @property
  def val(self) -> JsObjects.JsObject.JsObject:
    """

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.slider('values'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.component.dom.jquery.varId))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """

    """
    return JsHtml.ContentFormatters(self.page, '%s.slider("values")' % self.component.dom.jquery.varId)


class JsHtmlSliderDate(JsHtml.JsHtml):

  @property
  def val(self) -> JsObjects.JsObject.JsObject:
    """

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.content.toStr()))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """

    """
    return JsHtml.ContentFormatters(
      self.page, 'new Date(%s.slider("value") * 1000).toISOString().split("T")[0]' % self.component.dom.jquery.varId)


class JsHtmlSliderDates(JsHtml.JsHtml):

  @property
  def val(self) -> JsObjects.JsObject.JsObject:
    """

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.content.toStr()))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """

    """
    return JsHtml.ContentFormatters(
      self.page, 'function() {return [new Date(%s.slider("values")[0] * 1000).toISOString().split("T")[0], new Date(%s.slider("values")[1] * 1000).toISOString().split("T")[0]]}()' % (
        self.component.dom.jquery.varId, self.component.dom.jquery.varId))


class JsHtmlSparkline(JsHtml.JsHtml):

  @property
  def val(self):
    """

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self.region))

  @property
  def content(self) -> JsHtml.ContentFormatters:
    """

    """
    if self.component._jsStyles['type'] in ['bar']:
      return JsHtml.ContentFormatters(self.page, 'event.sparklines[0].getCurrentRegionFields()[0].value')

    return JsHtml.ContentFormatters(self.page, 'event.sparklines[0].getCurrentRegionFields().y')

  @property
  def value(self):
    """

    """
    if self.component._jsStyles['type'] in ['bar']:
      return JsHtml.ContentFormatters(self.page, 'event.sparklines[0].getCurrentRegionFields()[0].value')

    return JsObjects.JsNumber.JsNumber("event.sparklines[0].getCurrentRegionFields().y", is_py_data=False)

  @property
  def region(self):
    """

    """
    return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields()")

  @property
  def x(self):
    """

    """
    if self.component._jsStyles['type'] in ['bar']:
      return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields().offset")

    return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields().x")

  @property
  def offset(self):
    """

    """
    if self.component._jsStyles['type'] in ['bar']:
      return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields()[0].offset")

    return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields().offset")

  @property
  def y(self):
    """

    """
    if self.component._jsStyles['type'] in ['bar']:
      return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields()[0].value")

    return JsObjects.JsNumber.JsNumber("event.sparklines[0].getCurrentRegionFields().y", is_py_data=False)
