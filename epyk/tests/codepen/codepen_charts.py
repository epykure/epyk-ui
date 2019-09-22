from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()

data = [{"name": "Apple", "count": 80}, {"name": "Orange", "count": 10},
        {"name": "Grapes", "count": 50}, {"name": "Mango", "count": 40}]

rptObj.ui.charts.dc.bubble(data)


rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS, target="_self")
