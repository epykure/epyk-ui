from epyk.core.Ares import Report
from epyk.tests import test_statics

rptObj = Report()
rptObj.ui.icons.capture().color("red", "yellow")
rptObj.ui.icons.table(tooltip="helper")
rptObj.ui.icons.awesome("fas fa-stopwatch", tooltip="helper")


rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)