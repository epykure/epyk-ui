"""

"""

from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.tests import test_statics

# Create a blank Javascript Python object
jsObj = Js.JsBase()

# Define a dataSet using Vis library
dataset = jsObj.data.dataset(data=[{"column": 200}], var_name="test")
opts = dataset.options()
opts.height(100)
print(opts)
dataset.setOptions(opts)

jsObj.data.dataview([])
# Write the results to a Javascript file with a Launcher
f = JsUtils.JsFile("DataSet", path=test_statics.OUTPUT_PATHS)

# Write the Javascript fragments to the file
f.writeJs([
  dataset.toStr(),
])

# Close the file and print the location of the launcher
print(f.close(jsObj))