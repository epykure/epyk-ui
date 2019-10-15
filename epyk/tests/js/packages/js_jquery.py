"""

"""

from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.tests import test_statics

# Create a blank Javascript Python object
jsObj = Js.JsBase()
dom = jsObj.createElement("div", "testDom")


# Write the results to a Javascript file with a Launcher
f = JsUtils.JsFile("TestJquery", path=test_statics.OUTPUT_PATHS)

# Write the Javascript fragments to the file
f.writeJs([
  dom,
  jsObj.body.appendChild(dom),
  dom.text("youpi")
])

# Close the file and print the location of the launcher
print(f.close(jsObj))