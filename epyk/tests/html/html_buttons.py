"""
Module in charge of the testing of the buttons
"""

from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()

button = rptObj.ui.button("test")
#button.defined.
