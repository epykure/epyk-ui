from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()
rptObj.ui.side_bar()

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)