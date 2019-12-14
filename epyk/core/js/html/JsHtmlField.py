"""

"""

from epyk.core.js.html import JsHtml

from epyk.core.js.primitives import JsObjects


class JsHtmlFields(JsHtml.JsHtmlRich):
  @property
  def val(self):
    """

    :return:
    """
    return self._src.input.dom.val

  @property
  def content(self):
    return self._src.input.dom.content

  def empty(self): return '%s.innerHTML = ""' % self.varName
