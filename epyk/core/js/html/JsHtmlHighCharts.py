
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.py import types


class HighCharts(JsHtml.JsHtmlRich):

    def active(self):
        """Return the active clicked point"""
        return JsObjects.JsObject.JsObject.get(
            "{x: event.point.x, y: event.point.y, label: event.point.series.userOptions.name, category: event.point.category}")

    def createWidget(self, html_code: str, container: str = None, options: types.JS_DATA_TYPES = None):
        self.component.options.managed = False
        self.component.js_code = html_code
        js_code = JsUtils.jsConvertData(self.component.js_code, None).toStr()
        if js_code.startswith("window"):
            js_code = js_code[7:-1]
        return JsUtils.jsWrap('''(function(containerId, tag, htmlCode, jsCode, ctx, attrs){
    const newDiv = document.createElement(tag); Object.keys(attrs).forEach(
        function(key) {newDiv.setAttribute(key, attrs[key]);}); newDiv.id = htmlCode;
    if(!containerId){document.body.appendChild(newDiv)} else {document.getElementById(containerId).appendChild(newDiv)};
    window[jsCode] = Highcharts.chart(htmlCode, ctx); return newDiv
})(%(container)s, "%(tag)s", %(html_code)s, %(js_code)s, %(ctx)s, %(attrs)s)
            ''' % {
            "js_code": js_code,
            "attrs": self.component.get_attrs(css_class_names=self.component.style.get_classes(), to_str=False),
            "html_code": JsUtils.jsConvertData(html_code or self.component.html_code, None),
            "tag": self.component.tag, "ctx": self.component.options.config_js(options).toStr(),
            "container": JsUtils.jsConvertData(container, None),
        })