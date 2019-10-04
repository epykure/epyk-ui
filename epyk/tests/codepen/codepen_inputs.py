from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()

rptObj.ui.input()
rptObj.ui.inputs.search()
rptObj.ui.inputs.password()
rptObj.ui.inputs.textarea()
rptObj.ui.inputs.d_search("")
rptObj.ui.inputs.d_int()

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)