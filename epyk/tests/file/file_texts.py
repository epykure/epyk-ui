"""
Module in charge of the testing of the trees
"""


from epyk.core.Page import Report
from epyk.tests import test_statics

# Create a basic report object
rptObj = Report()


print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_text"))
