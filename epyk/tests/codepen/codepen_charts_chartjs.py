from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()

data = [
  {"x": 0, "y": 1},
  {"x": 2, "y": 2},
  {"x": 4, "y": 2},
  {"x": 6, "y": 6},
]

rptObj.ui.charts.chartJs.line(data, seriesNames=["y"], xAxis="x")

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)