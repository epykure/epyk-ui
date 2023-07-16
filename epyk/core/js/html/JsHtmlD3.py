from epyk.core.py import primitives
from epyk.core.js.html import JsHtml


class JsHtmlD3(JsHtml.JsHtml):

    def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
                 is_py_data: bool = True, page: primitives.PageModel = None):
        super(JsHtmlD3, self).__init__(component, js_code, set_var, is_py_data, page)
        self.varName = "d3.select('#%s')" % self.htmlCode
