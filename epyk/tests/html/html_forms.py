"""
Module in charge of the Forms testing
"""
from epyk.core.Page import Report


# Create a basic report object
rpt = Report()

# Create an input form
form = rpt.ui.forms.input("test")

#
form.input()

