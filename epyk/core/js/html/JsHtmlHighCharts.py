
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects


class HighCharts(JsHtml.JsHtmlRich):

    def active(self):
        """ Return the active clicked point. """
        return JsObjects.JsObject.JsObject.get("{x: event.point.x, y: event.point.y, label: event.point.series.userOptions.name, category: event.point.category}")
