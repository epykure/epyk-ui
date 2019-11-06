"""
Module in charge of the testing of the buttons
"""

from epyk.core.Page import Report
from epyk.tests import test_statics

from epyk.core.css import Defaults

Defaults.Font.size = 20
Defaults.Font.family = "cursive"

# Create a basic report object
rptObj = Report()

# This line will never be sent to the Javascript as not in any container or dedicated Js function
# rptObj.js.alert("Display")
#
# rptObj.js.addOnReady([
#   rptObj.js.console.log("This is a Javascript Log"),
#   rptObj.js.console.log(rptObj.js.location.pathname),
#   rptObj.js.console.log(rptObj.js.math.log(2)),
#   rptObj.js.localStorage.setItem("A", 30),
#   rptObj.js.console.log(rptObj.js.localStorage["A"])
# ])
#
# # Create a variable
# rptObj.js.addOnReady([
#   rptObj.js.objects.number(344, varName="test_number", setVar=True),
#   rptObj.js.objects.number.get("test_number") + 5,
#   rptObj.js.console.log(rptObj.js.objects.number.get("test_number")),
#
#   #
#   rptObj.js.fncs.inline("MyFncs", [rptObj.js.alert(rptObj.js.objects.get("a"))], ["a"]),
#   rptObj.js.fncs.get("MyFncs", "test call")
# ])


# Create a Javascript function

#button = rptObj.ui.button("test")
# # button.style.clear()
#
# # Create a new CSS class on the fly dedicated to the small devices
# button.style.cssCls("test", {"background-color": 'yellow'}, isMedia=True)
# # Derive from an existing CSS class
# button.defined.ovr("CssButtonBasic", eventAttrs={'hover': {"cursor": "cell"}})
# button.click(rptObj.js.window.alert("test"))

# Change the style for the CSS HTML Title component
# title = rptObj.ui.title("Example of title", level=1)
# title.style.cssCls("title_style", {"color": 'orange'})

# title.style.clear()

# Change the style for the CSS HTML Text component
# text = rptObj.ui.text("This is a text")
# text.style.clear().cssCls("class_text", {"color": 'red'}, {"hover": {"color": 'green', "cursor": "all-scroll"}})
# text.tooltip("This is a tooltip")
#
# rptObj.ui.input()
# rptObj.ui.css({"border": "1px solid red"})

# Javascript tests

data = [{"A": 1, "B": 2}]
table = rptObj.ui.tables.tabulators.table(data, cols=["A"], rows=["B"])
table.on("dblclick", rptObj.js.alert("test"), profile=False)

rptObj.ui.button("Test").click(rptObj.js.alert("test"))
rptObj.ui.rich.info("info")
span = rptObj.ui.texts.span("youpi")
span.mouse([
  span.dom.css("color", "red"),
  span.dom.css("cursor", "pointer").r],
  span.dom.css("color", "blue").r)

#span.on("mouseover", span.dom.css("color", "red"))
#span.on("mouseleave", span.dom.css("color", "blue"))

label = rptObj.ui.texts.label("label")

pre = rptObj.ui.texts.preformat("Super").notSelectable()

pre.click([
  rptObj.js.console.log(pre.dom.val),
  rptObj.js.console.log(span.dom.val),
  rptObj.js.console.log(label.dom.val),
])

from datetime import datetime

timestamp_s = rptObj.py.dates.from_timestamp(1573074335010, 0)
print(timestamp_s)

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_list"))