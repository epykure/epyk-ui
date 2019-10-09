"""

"""

from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.tests import test_statics


# Create a blank Javascript Python object
jsObj = Js.JsBase()

# Write the results to a Javascript file with a Launcher
f = JsUtils.JsFile("DataExamples", path=test_statics.OUTPUT_PATHS)

record = jsObj.data.records([{"B": 'RR3', "A": 0}, {"B": 'RR5', "A": 3}, {"B": 'RR3', "A": 2}])
record.f.count("B")#.top("count_distinct", n=2, order="asc")


# Write the Javascript fragments to the file
f.writeJs([
  jsObj.console.log(record)
])

# Close the file and print the location of the launcher
print(f.close(jsObj))
