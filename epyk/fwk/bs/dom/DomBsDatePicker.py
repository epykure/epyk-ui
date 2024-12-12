from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils


class DomDate(JsHtml.JsHtmlRich):

    @property
    def content(self) -> JsHtml.ContentFormatters:
        """Common function to get the component content."""
        return JsHtml.ContentFormatters(self.page, "%s.value" % self.querySelector("input").varId)

    def empty(self) -> JsUtils.jsWrap:
        """Emtpy the datepicker component"""
        return JsUtils.jsWrap("%s.value = ''" % self.querySelector("input").varId)
