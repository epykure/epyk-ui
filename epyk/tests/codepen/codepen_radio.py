from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()


rptObj.ui.buttons.radio(["A", "B"], label="Test", helper="helper")
# rptObj.ui.buttons.switch(["A", "B"])


rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)