"""
Module in charge of the testing of the Button items
"""


from epyk.core.Page import Report
from epyk.tests import test_statics


# Create a basic report object
rptObj = Report()

# Simple button
b = rptObj.ui.button("test")
b.click(rptObj.js.alert("ok"))

# Press Button
b2 = rptObj.ui.button("test 2", width=100)
b2.press(rptObj.js.alert("test"))

# Press Button and unlock
b3 = rptObj.ui.button("test 3", width=100)
b3.press(
  rptObj.js.console.log("test"),
  [rptObj.js.console.log("unlock")])

b4 = rptObj.ui.button("test 4")
b4.click(rptObj.js.console.log(b3.dom.val))

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_buttons"))