from epyk.core.js.html import JsHtml


class DomCheck(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    ------------
    Common function to get the component content.
    """
    return JsHtml.ContentFormatters(self._report, "%s.checked" % self.varName)