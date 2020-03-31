
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects


class TimePicker(JsHtml.JsHtml):

  @property
  def val(self):
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.timepicker('getTime'), timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlId, self._src.dom.jquery.varId))

  @property
  def content(self):
    return JsObjects.JsObjects.get("%s.timepicker('getTime')" % self._src.dom.jquery.varId)
