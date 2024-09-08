from epyk.core.js.html import JsHtml


class Quill(JsHtml.JsHtmlRich):

    @property
    def content(self) -> JsHtml.ContentFormatters:
        """
        The Javascript value of the component.
        This returned only a value corresponding to the state of the component.
        """
        return self.component.js.getSemanticHTML()

    def empty(self):
        """Empty the content of the HTML component using the innerHTML JavaScript property"""
        return self.component.js.setText("")
