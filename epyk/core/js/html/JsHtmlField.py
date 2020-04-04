
from epyk.core.js.html import JsHtml

from epyk.core.js.primitives import JsObjects


class Check(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get('''{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), name: %s}}
        ''' % (self.htmlId, self.content.toStr(), self.getAttribute('name')))

  @property
  def content(self):
    """
    Description:
    -----------

    :return:
    """
    return JsHtml.ContentFormatters(self._report, "%s.checked" % self.varName)


class JsHtmlFields(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    -----------

    :return:
    """
    return self._src.input.dom.val

  @property
  def content(self):
    """
    Description:
    -----------

    :return:
    """
    return self._src.input.dom.content

  def empty(self):
    """
    Description:
    -----------

    :return:
    """
    return JsObjects.JsObjects.get('%s = ""' % self.content.toStr())
