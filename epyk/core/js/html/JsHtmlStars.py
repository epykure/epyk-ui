
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects


class Stars(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    ------------
    The Javascript data object. A dictionary with all the specific metadata attached to the component
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.dataset.level, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self.varName))

  @property
  def content(self):
    """
    Description:
    ------------
    The Javascript value of the component. This returned only a value corresponding to the state of the component
    """
    return JsHtml.ContentFormatters(self._report, "%s.dataset.level" % self.varName)


class Slides(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    ------------
    The Javascript value of the component. This returned only a value corresponding to the state of the component
    """
    return JsHtml.ContentFormatters(self._report, "%s.getAttribute('data-current_slide')" % self.varName)

  def goTo(self, number):
    """
    Description:
    ------------

    :param number:
    """
    return JsObjects.JsObjects.get('''%s.setAttribute('data-current_slide', Math.min(%s, %s)-2);
      %s ''' % (self.varName, number, len(self._src.val), self._src.next.dom.events.trigger('click')))

