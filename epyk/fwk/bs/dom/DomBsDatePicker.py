from epyk.core.js.html import JsHtml


class DomDate(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Common function to get the component content.
    """
    return JsHtml.ContentFormatters(self.page, "%s.value" % self.querySelector("input").varId)
