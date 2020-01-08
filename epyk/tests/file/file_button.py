"""
Module in charge of the testing of the Button items
"""


from epyk.core.Page import Report
from epyk.tests import test_statics


# Create a basic report object
rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

# Simple button
b = rptObj.ui.button("test")
b.click([c.write(" **ok**, this is a test")])

# Press Button
b2 = rptObj.ui.button("test 2", width=100)
b2.press(c.write(b2.dom.content + "' is locked'"))

# Press Button and unlock
b3 = rptObj.ui.button("test 3", width=100)
b3.press(
  c.write("Button 3 locked"),
  c.write("Button 3 unlocked"))

# Create a group of buttons
b5 = rptObj.ui.button("test 5")
b6 = rptObj.ui.button("test 6")
b7 = rptObj.ui.button("test 7")

# Change button CSS styles
b8 = rptObj.ui.button("test 8")
b8.style.clear() # Remove all CSS styles
b8.css({"background-color": 'blue', 'color': 'white', 'border': 'None'})

rptObj.ui.layouts.hr()
# Create a CSS class
b8_bis = rptObj.ui.button("test CSS Class")
b8_bis.style.clear()
css_cls = rptObj.style.cssCls("test_css", {"color": "orange"}, {"hover": {"color": 'red'}})
b8_bis.style.cssCls("test_css")

rptObj.ui.layouts.new_line(1)
# Change button hover CSS style
b9 = rptObj.ui.button("test 9")
b9.color("red")

# Button middle page
b10 = rptObj.ui.button("test 10")
rptObj.ui.div(b10).css({"text-align": 'center'})

# Create a button with an icon
b11 = rptObj.ui.button("test 11", icon="fab fa-python")

# Buttons groups
b12 = rptObj.ui.buttons.buttons(["test 15", "test 13", "test 14"])
for i in b12:
  i.press(
    rptObj.js.console.log("test"),
    [rptObj.js.console.log("unlock")])

# Buttons groups (manual)
b15 = rptObj.ui.button("test 15", options={"group": "test_group"})
b16 = rptObj.ui.button("test 16", options={"group": "test_group"})
b15.options.multiple = True
b16.options.multiple = True
b15.press(
  rptObj.js.console.log("test"),
  [rptObj.js.console.log("unlock")])
b16.press(
  c.write("Ok"),
  rptObj.js.console.log("test"),
  [rptObj.js.console.log("unlock")])

rptObj.ui.layouts.new_line(2)
# Get button status
b4 = rptObj.ui.button("test 4")
b4.click([
  rptObj.js.console.log(b3.dom.val),
  rptObj.js.console.log(b16.dom.val),
  rptObj.js.console.log(b12[0].dom.val),
  rptObj.js.console.log(b12[1].dom.content),
  b3.build("Test") # Change value
]
)

# Events

# Change a CSS Style
b12[0].click([
  b12[0].dom.css("color", "green")
])

# go to another page

# run a service

# add attributes to the url

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_buttons"))