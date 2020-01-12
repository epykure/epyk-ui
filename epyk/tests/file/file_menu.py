"""

"""


from epyk.core.Page import Report
from epyk.tests import test_statics


# Create a basic report object
rptObj = Report()

rptObj.ui.layouts.menu()

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_menu"))
