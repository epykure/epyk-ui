from epyk.core.Page import Report
from epyk.tests import test_statics

rptObj = Report()

rptObj.ui.icons.capture().color("red", "yellow")
rptObj.ui.icons.table(tooltip="helper")
rptObj.ui.icons.awesome("fas fa-stopwatch", tooltip="helper")

rptObj.ui.icon("fab fa-css3-alt")
rptObj.ui.images.badge("5", "Label", icon="fas fa-align-center")
rptObj.ui.images.badge("New")


rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)