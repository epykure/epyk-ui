from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.tests import test_statics

# Create a blank Javascript Python object
jsObj = Js.JsBase()

# Define a dataSet using CrossFilter library
crossFilter = jsObj.data.crossfilter(data=[{"column": 200}], var_name="test")

# Write the results to a Javascript file with a Launcher
f = JsUtils.JsFile("CrossFilter", path=test_statics.OUTPUT_PATHS)

# Write the Javascript fragments to the file
f.writeJs([
  crossFilter.toStr(),
  crossFilter.dimension("column").filterAll().filterRange(100, 400).top(10).toStr(),
  jsObj.console.log(crossFilter.var)
])

# Close the file and print the location of the launcher
print(f.close(jsObj))