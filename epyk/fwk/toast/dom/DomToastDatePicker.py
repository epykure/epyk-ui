from epyk.core.js.html import JsHtml


class DomTime(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Common function to get the component content.
    """
    return JsHtml.ContentFormatters(self.page, "%(var)s.getHour()+ ':'+ %(var)s.getMinute()" % {
      "var": self.component.var})


class DomDate(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Common function to get the component content.
    """
    return JsHtml.ContentFormatters(self.page, "%(var)s.getDate().toISOString().split('T')[0]" % {
      "var": self.component.var})
