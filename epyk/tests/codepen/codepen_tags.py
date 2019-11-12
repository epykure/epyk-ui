from epyk.core.Page import Report
from epyk.tests import test_statics

rptObj = Report()

abbr = rptObj.ui.tags.bdi("abbr")
abbr.click(rptObj.js.alert("test"))
abbr.css({'cursor': 'pointer', 'border': '1px solid black'})


rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS, open_browser=True)