from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()


rptObj.ui.texts.number(12345697, options={"decPlaces": 5, "decSeparator": "@"})
# rptObj.ui.buttons.switch(["A", "B"])


rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)