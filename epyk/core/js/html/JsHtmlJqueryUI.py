
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
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.val(), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlCode, self._src.dom.jquery.varId))

  @property
  def content(self):
    """
    Description:
    ------------

    """
    return JsHtml.ContentFormatters(self._report, '%s.val()' % self._src.dom.jquery.varId)


class JsHtmlDateFieldPicker(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.val, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlCode, self.content.toStr()))

  @property
  def content(self):
    """
    Description:
    ------------

    """
    return JsHtml.ContentFormatters(self._report, '%s.val()' % self._src.input.dom.jquery.varId)


class JsHtmlProgressBar(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.progressbar('value'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self._src.dom.jquery.varId))

  @property
  def content(self):
    """
    Description:
    ------------

    """
    return JsHtml.ContentFormatters(self._report, '%s.progressbar("value")' % self._src.dom.jquery.varId)

  def to(self, number, timer=10):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param number:
    :param timer: Integer. the spped of the increase in millisecond
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

    Attributes:
    ----------
    :param val:
    :param jsFnc:
    """
    return JsFncs.JsFunction("if((%(content)s >= %(val)s) && (%(content)s <= %(val)s + 10)){%(fnc)s}" % {'content': self.content, 'val': val, 'fnc': JsUtils.jsConvertFncs(jsFnc, toStr=True)})

  def max(self, jsFnc):
    """
    Description:
    ------------

    :param jsFnc:
    """
    return self.position(100, jsFnc)


class JsHtmlTimePicker(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.val(), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self._src.dom.jquery.varId))

  @property
  def content(self):
    """
    Description:
    ------------

    """
    return JsHtml.ContentFormatters(self._report, '%s.val()' % self._src.dom.jquery.varId)


class JsHtmlSlider(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.slider('value'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self._src.dom.jquery.varId))

  @property
  def content(self):
    """
    Description:
    ------------

    """
    return JsHtml.ContentFormatters(self._report, '%s.slider("value")' % self._src.dom.jquery.varId)


class JsHtmlSliderRange(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.slider('values'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self._src.dom.jquery.varId))

  @property
  def content(self):
    """
    Description:
    ------------

    """
    return JsHtml.ContentFormatters(self._report, '%s.slider("values")' % self._src.dom.jquery.varId)


class JsHtmlSliderDate(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.content.toStr()))

  @property
  def content(self):
    """
    Description:
    ------------

    """
    return JsHtml.ContentFormatters(self._report, 'new Date(%s.slider("value") * 1000).toISOString().split("T")[0]' % self._src.dom.jquery.varId)


class JsHtmlSliderDates(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.content.toStr()))

  @property
  def content(self):
    """
    Description:
    ------------

    """
    return JsHtml.ContentFormatters(self._report, 'function() {return [new Date(%s.slider("values")[0] * 1000).toISOString().split("T")[0], new Date(%s.slider("values")[1] * 1000).toISOString().split("T")[0]]}()' % (self._src.dom.jquery.varId, self._src.dom.jquery.varId))


class JsHtmlSparkline(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self.region))

  @property
  def content(self):
    """
    Description:
    ------------

    """
    if self._src._jsStyles['type'] in ['bar']:
      return JsHtml.ContentFormatters(self._report, 'event.sparklines[0].getCurrentRegionFields()[0].value')

    return JsHtml.ContentFormatters(self._report, 'event.sparklines[0].getCurrentRegionFields().y')

  @property
  def value(self):
    if self._src._jsStyles['type'] in ['bar']:
      return JsHtml.ContentFormatters(self._report, 'event.sparklines[0].getCurrentRegionFields()[0].value')

    return JsObjects.JsNumber.JsNumber("event.sparklines[0].getCurrentRegionFields().y", isPyData=False)

  @property
  def region(self):
    return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields()")

  @property
  def x(self):
    if self._src._jsStyles['type'] in ['bar']:
      return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields().offset")

    return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields().x")

  @property
  def offset(self):
    if self._src._jsStyles['type'] in ['bar']:
      return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields()[0].offset")

    return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields().offset")

  @property
  def y(self):
    if self._src._jsStyles['type'] in ['bar']:
      return JsObjects.JsObjects.get("event.sparklines[0].getCurrentRegionFields()[0].value")

    return JsObjects.JsNumber.JsNumber("event.sparklines[0].getCurrentRegionFields().y", isPyData=False)
