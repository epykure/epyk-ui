
from epyk.core.js.html import JsHtml

from epyk.core.js.primitives import JsObjects


class Radio(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return JsObjects.JsObjects.get('''{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), name: %s, selected: %s}}
        ''' % (self.htmlCode, self.content.toStr(), self.getAttribute('name'), self.selected.toStr()))

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return JsHtml.ContentFormatters(self._report, "%s.checked" % self._src.input.dom.varName)

  @property
  def selected(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return JsHtml.ContentFormatters(self._report, "document.body.querySelector('input[name='+%s+']:checked').getAttribute('data-content')" % self._src.input.dom.getAttribute('name'))


class Check(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return JsObjects.JsObjects.get('''{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), name: %s}}
        ''' % (self.htmlCode, self.content.toStr(), self.getAttribute('name')))

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return JsHtml.ContentFormatters(self._report, "%s.checked" % self.varName)


class JsHtmlFields(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return self._src.input.dom.val

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return self._src.input.dom.content

  def empty(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return JsObjects.JsObjects.get('%s = ""' % self.content.toStr())


class Textarea(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return JsHtml.ContentFormatters(self._report, "%s.value" % self.varName)
