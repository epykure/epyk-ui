"""
Module in charge of the testing of the trees
"""


from epyk.core.Page import Report
from epyk.tests import test_statics

# Create a basic report object
rptObj = Report()

rptObj.ui.forms.input("", "POST")

popup = rptObj.ui.layouts.popup(rptObj.ui.title('Test'), color="red")
popup + rptObj.ui.texts.paragraph('Test')

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_form"))
