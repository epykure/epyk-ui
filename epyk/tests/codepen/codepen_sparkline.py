from epyk.core.Ares import Report
from epyk.tests import test_statics

rptObj = Report()
data = [1, 2, 3, 4, 5]
rptObj.ui.charts.sparkline("box", [1, 2, 3, 4, 5, 4, 3, 2, 1])
rptObj.ui.charts.sparkline("bar", [1, 2, 3, 4, 5, 4, 3, 2, 10])
rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)