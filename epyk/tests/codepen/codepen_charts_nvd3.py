from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()

data = [
  {"x": 0, "y": 1},
  {"x": 2, "y": 2},
  {"x": 4, "y": 2},
  {"x": 6, "y": 6},
]

bar = rptObj.ui.charts.nvd3.pie(data, seriesNames=["y"], xAxis="x")

# bar.style.defined.chart.container_border().remove()
# bar.chart.width(30)
# bar.chart.xAxis.axisLabel("test").tickFormat(12)

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)