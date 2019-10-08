"""

"""

from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.tests import test_statics


# Create a blank Javascript Python object
jsObj = Js.JsBase()


# Write the results to a Javascript file with a Launcher
f = JsUtils.JsFile("DataExamples", path=test_statics.OUTPUT_PATHS)

jsObj.data.records([])

# Write the Javascript fragments to the file
f.writeJs([
])

# Close the file and print the location of the launcher
print(f.close(jsObj))
