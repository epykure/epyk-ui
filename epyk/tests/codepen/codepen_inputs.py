from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()

# Add different type of inputs
rptObj.ui.input()
rptObj.ui.inputs.search()
rptObj.ui.inputs.password()
rptObj.ui.inputs.textarea()
rptObj.ui.inputs.d_search("")
rptObj.ui.inputs.d_int()

# Create a tag component
tags = rptObj.ui.tags(["A", "B"])

# Add a button with a click event
b = rptObj.ui.button("add tag")
b.click(tags.jsAdd("Ok"))

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)