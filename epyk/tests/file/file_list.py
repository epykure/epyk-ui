"""
Module in charge of the testing of the buttons
"""

from epyk.core.Page import Report
from epyk.tests import test_statics


# Create a basic report object
rptObj = Report()

button = rptObj.ui.button("test")


print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_list"))