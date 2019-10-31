"""
Module in charge of the testing of the buttons
"""

from epyk.core.Page import Report
from epyk.tests import test_statics


# Create a basic report object
rptObj = Report()

button = rptObj.ui.button("test")
rptObj.ui.title("Example of title", level=1)
rptObj.ui.input()
rptObj.ui.css({"border": "1px solid red"})


print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_list"))