from epyk.core.Ares import Report
from epyk.tests import test_statics


rptObj = Report()

rptObj.ui.input()
rptObj.ui.inputs.search()

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)