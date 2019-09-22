from epyk.core.Page import Report
from epyk.tests import test_statics

from epyk.core.js.objects import JsChartDC
from epyk.core.js.packages import JsD3


rptObj = Report()

data = [{"name": "Apple", "count": 80}, {"name": "Orange", "count": 10},
        {"name": "Grapes", "count": 50}, {"name": "Mango", "count": 40}]

rptObj.ui.charts.dc.bubble(data)

d3Obj = JsD3.JsD3(rptObj, d3Id="d3")
print( d3Obj.scaleBand().domain().toStr() )

config = JsChartDC.JsLine(rptObj, data, []).x("d3.scaleBand()")
print(config.toStr())


#rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS, target="_self")
