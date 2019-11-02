"""
Module in charge of the testing of the buttons
"""

from epyk.core.Page import Report
from epyk.tests import test_statics


# Create a basic report object
rptObj = Report()

button = rptObj.ui.button("test")
# button.style.clear()

# Create a new CSS class on the fly dedicated to the small devices
button.style.cssCls("test", {"background-color": 'yellow'}, isMedia=True)
# Derive from an existing CSS class
button.defined.ovr("CssButtonBasic", eventAttrs={'hover': {"cursor": "cell"}})
button.click(rptObj.js.window.alert("test"))

# Change the style for the CSS HTML Title component
title = rptObj.ui.title("Example of title", level=1)
title.css({"color": 'red'})

# title.style.clear()

# Change the style for the CSS HTML Text component
text = rptObj.ui.text("This is a text")
text.style.clear().cssCls("class_text", {"color": 'red'}, {"hover": {"color": 'green', "cursor": "all-scroll"}})
text.tooltip("This is a tooltip")

rptObj.ui.input()
rptObj.ui.css({"border": "1px solid red"})


print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_list"))