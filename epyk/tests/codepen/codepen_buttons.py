"""
Sample of Python code ready to be sent to Codepen.
This is dedicated to test the code transpiled to Javascript, CSS and HTML.

The function rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS) will directly send data to codepen
using the API.
"""

from epyk.core.Page import Report
from epyk.tests import test_statics

# Create an empty report in the webpage
rptObj = Report()
# Creates a test button
button = rptObj.ui.button("Test", icon="fab fa-codepen")
# Add a click event on the button
button.click([rptObj.js.window.alert("test")])

# Create a second button in the report with a click event
button2 = rptObj.ui.buttons.validate("phone").click([rptObj.js.window.alert("phone")])
# Change the CSS Style of the second button
button2.css({"margin-left": '5px'})

# Transpile to Javascriot and create a report in codepen (python will automatically open the default browser)
rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)
