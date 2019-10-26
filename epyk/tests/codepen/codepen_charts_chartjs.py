from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()

data = test_statics.get_data("flights.txt", n=10)

line = rptObj.ui.charts.chartJs.line(data, y_columns=["delay"], x_axis="distance")
line.chart


rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)