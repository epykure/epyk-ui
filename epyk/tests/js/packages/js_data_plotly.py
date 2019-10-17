"""

"""

from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.tests import test_statics

# Create a blank Javascript Python object
jsObj = Js.JsBase()

# Write the results to a Javascript file with a Launcher
f = JsUtils.JsFile("DataExamplesPlolty", path=test_statics.OUTPUT_PATHS)


# Write the Javascript fragments to the file
f.writeJs([

])

import json

#data = test_statics.get_data("stocks.json")

# Close the file and print the location of the launcher
print(f.close(jsObj))
