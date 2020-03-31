from epyk.core.js.html import JsHtml
from epyk.core.js.fncs import JsFncs
from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsObjects


class JsHtmlDatePicker(JsHtml.JsHtml):
  @property
  def val(self):
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.val(), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlId, self._src.dom.jquery.varId))

  @property
  def content(self):
    return JsObjects.JsObjects.get('%s.val()' % self._src.dom.jquery.varId)


class JsHtmlProgressBar(JsHtml.JsHtml):

  @property
  def val(self):
    """

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.progressbar('value'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlId, self._src.dom.jquery.varId))

  @property
  def content(self):
    """

    """
    return JsObjects.JsObjects.get('%s.progressbar("value")' % self._src.dom.jquery.varId)

  def position(self, val, jsFnc):
    """

    :param val:
    :param jsFnc:
    """
    return JsFncs.JsFunction("if((%(content)s >= %(val)s) && (%(content)s <= %(val)s + 10)){%(fnc)s}" % {'content': self.content, 'val': val, 'fnc': JsUtils.jsConvertFncs(jsFnc, toStr=True)})

  def max(self, jsFnc):
    """

    :param jsFnc:
    """
    return self.position(100, jsFnc)


class JsHtmlTimePicker(JsHtml.JsHtml):
  @property
  def val(self):
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.val(), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlId, self._src.dom.jquery.varId))

  @property
  def content(self):
    return JsObjects.JsObjects.get('%s.val()' % self._src.dom.jquery.varId)


class JsHtmlSlider(JsHtml.JsHtml):

  @property
  def val(self):
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.slider('value'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlId, self._src.dom.jquery.varId))

  @property
  def content(self):
    return JsObjects.JsObjects.get('%s.slider("value")' % self._src.dom.jquery.varId)
