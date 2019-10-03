from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()

rptObj.ui.layouts.multiFilter(["A", "B"], title="Test")

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)