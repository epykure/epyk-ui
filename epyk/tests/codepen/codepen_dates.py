from epyk.core.Ares import Report
from epyk.tests import test_statics

rptObj = Report()
cob = rptObj.ui.date()
today = rptObj.ui.dates.today(label="Date", helper="This is the report timestamp")
rptObj.ui.dates.cob(label="Date").selectable(["2019-09-01", "2019-09-06"])
rptObj.ui.dates.now(label="timestamp", color="red", helper="This is the report timestamp")
rptObj.ui.dates.countdown("2019-09-24", label="Countdown")
rptObj.ui.dates.update()
#date.click([rptObj.js.window.alert("test")])



rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)