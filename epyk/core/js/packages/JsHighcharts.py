from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class Highcharts(JsPackage):
    lib_alias = {'js': 'highcharts'}

    def empty(self):
        """ """
        return JsObjects.JsVoid(
            "while (%(varName)s.series.length) {chart.series[0].remove();}" % {"varName": self.varName})

    def update(self):
        return JsUtils.jsWrap('''
''')
