#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js.fncs import JsFncs
from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsObjects


class JsHtmlDatePicker(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.val(), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlCode, self._src.dom.jquery.varId))

  @property
  def content(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsHtml.ContentFormatters(self._report, '%s.val()' % self._src.dom.jquery.varId)


class JsHtmlDateFieldPicker(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.val, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlCode, self.content.toStr()))

  @property
  def content(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsHtml.ContentFormatters(self._report, '%s.val()' % self._src.input.dom.jquery.varId)


class JsHtmlProgressBar(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.progressbar('value'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self._src.dom.jquery.varId))

  @property
  def content(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsHtml.ContentFormatters(self._report, '%s.progressbar("value")' % self._src.dom.jquery.varId)

  def to(self, number, timer=10):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param number: Integer.
    :param timer: Integer. Optional. the spped of the increase in millisecond.
    """
    return JsUtils.jsConvertFncs([
      self._report.js.objects.number(self.content.unformat(), varName="%s_counter" % self.htmlCode, setVar=True),
      self._report.js.window.setInterval([
        self._report.js.if_(
          self._report.js.objects.number.get("window.%s_counter" % self.htmlCode) < number, [
            self._report.js.objects.number(
              self._report.js.objects.number.get("window.%s_counter" % self.htmlCode) + 1,
              varName="window.%s_counter" % self.htmlCode, setVar=True),
            self._src.build(self._report.js.objects.number.get("window.%s_counter" % self.htmlCode))
          ]).else_(self._report.js.window.clearInterval("%s_interval" % self.htmlCode))
      ], "%s_interval" % self.htmlCode, timer)
    ], toStr=True)

  def position(self, val, jsFnc):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param val:
    :param jsFnc: List | String. Javascript functions.
    """
    return JsFncs.JsFunction("if((%(content)s >= %(val)s) && (%(content)s <= %(val)s + 10)){%(fnc)s}" % {'content': self.content, 'val': val, 'fnc': JsUtils.jsConvertFncs(jsFnc, toStr=True)})

  def max(self, jsFnc):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param jsFnc: List | String. Javascript functions.
    """
    return self.position(100, jsFnc)


class JsHtmlTimePicker(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.val(), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self._src.dom.jquery.varId))

  @property
  def content(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsHtml.ContentFormatters(self._report, '%s.val()' % self._src.dom.jquery.varId)


class JsHtmlSlider(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.slider('value'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.component.dom.jquery.varId))

  @property
  def content(self):
    """
    Description:
    ------------

    Usage:
    -----
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
  def max_select(self):
    """
    Description:
    ------------
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
  def min_select(self):
    """
    Description:
    ------------
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
  def upper_bound(self):
    """
    Description:
    ------------

    :return:
    """
    if self.component.options.range:
      return JsHtml.ContentFormatters(self.page, '%s.slider("option", "max")' % self.component.dom.jquery.varId)

    return self.content

  @property
  def lower_bound(self):
    """
    Description:
    ------------

    :return:
    """
    if self.component.options.range:
      return JsHtml.ContentFormatters(self.page, '%s.slider("option", "min")' % self.component.dom.jquery.varId)

    return self.content


class JsHtmlSliderRange(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.slider('values'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self._src.dom.jquery.varId))

  @property
  def content(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsHtml.ContentFormatters(self._report, '%s.slider("values")' % self._src.dom.jquery.varId)


class JsHtmlSliderDate(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.content.toStr()))

  @property
  def content(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsHtml.ContentFormatters(self._report, 'new Date(%s.slider("value") * 1000).toISOString().split("T")[0]' % self._src.dom.jquery.varId)


class JsHtmlSliderDates(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.content.toStr()))

  @property
  def content(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsHtml.ContentFormatters(self._report, 'function() {return [new Date(%s.slider("values")[0] * 1000).toISOString().split("T")[0], new Date(%s.slider("values")[1] * 1000).toISOString().split("T")[0]]}()' % (self._src.dom.jquery.varId, self._src.dom.jquery.varId))


class JsHtmlSparkline(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self.region))

  @property
  def content(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    if self._src._jsStyles['type'] in ['bar']:
      return JsHtml.ContentFormatters(self._report, 'event.sparklines[0].getCurrentRegionFields()[0].value')

    return JsHtml.ContentFormatters(self._report, 'event.sparklines[0].getCurrentRegionFields().y')

  @property
  def value(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    if self._src._jsStyles['type'] in ['bar']:
      return JsHtml.ContentFormatters(self._report, 'event.sparklines[0].getCurrentRegionFields()[0].value')

    return JsObjects.JsNumber.JsNumber("event.sparklines[0].getCurrentRegionFields().y", isPyData=False)

  @property
  def region(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields()")

  @property
  def x(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    if self._src._jsStyles['type'] in ['bar']:
      return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields().offset")

    return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields().x")

  @property
  def offset(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    if self._src._jsStyles['type'] in ['bar']:
      return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields()[0].offset")

    return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields().offset")

  @property
  def y(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    if self._src._jsStyles['type'] in ['bar']:
      return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields()[0].value")

    return JsObjects.JsNumber.JsNumber("event.sparklines[0].getCurrentRegionFields().y", isPyData=False)
