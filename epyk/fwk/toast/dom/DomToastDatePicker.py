from epyk.core.js.html import JsHtml


class DomTime(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    ------------
    Common function to get the component content.
    """
    return JsHtml.ContentFormatters(self._report, "%(var)s.getHour()+ ':'+ %(var)s.getMinute()" % {
      "var": self._src.var})


class DomDate(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    ------------
    Common function to get the component content.
    """
    return JsHtml.ContentFormatters(self._report, "%(var)s.getDate().toISOString().split('T')[0]" % {
      "var": self._src.var})
